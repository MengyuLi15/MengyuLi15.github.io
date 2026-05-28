#!/usr/bin/env python3
"""Validate paper-push DOI metadata against Crossref.

The paper-push page must not publish a DOI beside a rewritten or mismatched
title. This script uses only the Python standard library so it can run inside
GitHub Actions without extra dependencies.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "_data" / "paper_pushes.yml"
USER_AGENT = "mengyuli15-paper-push-validator/1.0 (https://mengyuli15.github.io/)"
SUMMARY_PLACEHOLDER = "DOI-verified metadata correction"
MIN_SUMMARY_SENTENCES = 5
FORBIDDEN_SUMMARY_PHRASES = (
    "DOI 页面",
    "进一步核对",
    "从题名",
    "题名所示",
    "关键词是",
    "The exact data source should be checked",
    "from the title",
    "key themes including",
    "process indicated by the title",
)


def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", html.unescape(value or ""))
    value = value.replace("\u00a0", " ")
    return re.sub(r"\s+", " ", value).strip()


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", clean_text(value).lower()).strip()


def yaml_unquote(value: str) -> str:
    return value.replace(r"\"", '"').replace(r"\\", "\\")


def issue_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r'(?m)^- date: "([^"]+)"', text))
    blocks: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append((match.group(1), text[match.start() : end]))
    return blocks


def field(block: str, name: str) -> str:
    match = re.search(rf'(?m)^      {re.escape(name)}: "((?:\\.|[^"])*)"', block)
    return yaml_unquote(match.group(1)) if match else ""


def issue_flag(block: str, name: str) -> bool:
    return bool(re.search(rf'(?m)^  {re.escape(name)}:\s*true\s*$', block))


def parse_papers(issue: str) -> list[dict[str, str]]:
    papers = []
    pattern = re.compile(r'(?ms)^    - title: "([^"]*)"\r?\n(.*?)(?=^    - title: |\Z)')
    for index, match in enumerate(pattern.finditer(issue), start=1):
        block = match.group(2)
        papers.append(
            {
                "index": str(index),
                "title": yaml_unquote(match.group(1)),
                "authors": field(block, "authors"),
                "journal": field(block, "journal"),
                "published_month": field(block, "published_month"),
                "doi": field(block, "doi"),
                "summary_zh": field(block, "summary_zh") or field(block, "summary"),
                "summary_en": field(block, "summary_en") or field(block, "summary"),
            }
        )
    return papers


def crossref_work(doi: str) -> dict:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return payload["message"]


def crossref_month(work: dict) -> str:
    for key in ("published-print", "published-online", "published", "created"):
        parts = ((work.get(key) or {}).get("date-parts") or [[]])[0]
        if len(parts) >= 2:
            return f"{parts[0]:04d}-{parts[1]:02d}"
        if len(parts) == 1:
            return str(parts[0])
    return ""


def crossref_authors(work: dict) -> list[str]:
    authors = []
    for author in work.get("author", []):
        given = (author.get("given") or "").strip()
        family = (author.get("family") or "").strip()
        name = " ".join(part for part in (given, family) if part)
        if name:
            authors.append(name)
    return authors


def journal_matches(local: str, remote: str) -> bool:
    local_norm = normalize(local)
    remote_norm = normalize(remote)
    return bool(local_norm and remote_norm and (local_norm in remote_norm or remote_norm in local_norm))


def author_matches(local: str, remote_authors: list[str]) -> bool:
    if not local or not remote_authors:
        return False
    local_first = normalize(local.split(";")[0])
    remote_first = normalize(remote_authors[0])
    return bool(local_first and remote_first and (local_first in remote_first or remote_first in local_first))


def published_month_matches(local: str, remote: str) -> bool:
    if not local or not remote:
        return False
    if len(remote) == 4:
        return local.startswith(remote)
    return local == remote


def sentence_count(value: str) -> int:
    parts = re.split(r"[.!?\u3002\uff01\uff1f]+", clean_text(value))
    return len([part for part in parts if part.strip()])


def validate_summary_fields(paper: dict[str, str]) -> list[str]:
    errors: list[str] = []
    summary_zh = clean_text(paper["summary_zh"])
    summary_en = clean_text(paper["summary_en"])
    for label, value in (("summary_zh", summary_zh), ("summary_en", summary_en)):
        if not value:
            errors.append(f"{paper['index']}. {paper['doi']}: {label} is empty")
        if SUMMARY_PLACEHOLDER in value:
            errors.append(f"{paper['index']}. {paper['doi']}: {label} still contains a metadata-correction placeholder")
        for phrase in FORBIDDEN_SUMMARY_PHRASES:
            if phrase in value:
                errors.append(f"{paper['index']}. {paper['doi']}: {label} contains forbidden generated-text phrase: {phrase}")
        if sentence_count(value) < MIN_SUMMARY_SENTENCES:
            errors.append(f"{paper['index']}. {paper['doi']}: {label} has fewer than {MIN_SUMMARY_SENTENCES} sentences")
    if summary_zh and not re.search(r"[\u4e00-\u9fff]", summary_zh):
        errors.append(f"{paper['index']}. {paper['doi']}: summary_zh does not look Chinese")
    if summary_en and re.search(r"[\u4e00-\u9fff]", summary_en):
        errors.append(f"{paper['index']}. {paper['doi']}: summary_en contains Chinese characters")
    return errors


def validate(papers: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    for paper in papers:
        doi = paper["doi"]
        errors.extend(validate_summary_fields(paper))
        try:
            work = crossref_work(doi)
        except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError) as exc:
            errors.append(f"{paper['index']}. {doi}: Crossref lookup failed: {exc}")
            continue

        remote_title = clean_text((work.get("title") or [""])[0])
        remote_journal = clean_text((work.get("container-title") or [""])[0])
        remote_month = crossref_month(work)
        remote_authors = crossref_authors(work)

        if normalize(paper["title"]) != normalize(remote_title):
            errors.append(
                f"{paper['index']}. {doi}: title mismatch\n"
                f"  local:   {paper['title']}\n"
                f"  crossref:{remote_title}"
            )
        if not author_matches(paper["authors"], remote_authors):
            errors.append(
                f"{paper['index']}. {doi}: first author mismatch\n"
                f"  local:   {paper['authors'].split(';')[0] if paper['authors'] else ''}\n"
                f"  crossref:{remote_authors[0] if remote_authors else ''}"
            )
        if not published_month_matches(paper["published_month"], remote_month):
            errors.append(
                f"{paper['index']}. {doi}: publication month mismatch\n"
                f"  local:   {paper['published_month']}\n"
                f"  crossref:{remote_month}"
            )
        if remote_journal and not journal_matches(paper["journal"], remote_journal):
            errors.append(
                f"{paper['index']}. {doi}: journal mismatch\n"
                f"  local:   {paper['journal']}\n"
                f"  crossref:{remote_journal}"
            )
        time.sleep(0.12)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default=str(DEFAULT_DATA))
    parser.add_argument("--date", help="Validate one issue date; default validates the latest issue.")
    args = parser.parse_args()

    text = Path(args.data).read_text(encoding="utf-8-sig")
    issues = issue_blocks(text)
    if not issues:
        print("No paper-push issues found.", file=sys.stderr)
        return 1

    if args.date:
        selected = [(date, block) for date, block in issues if date == args.date]
        if not selected:
            print(f"No paper-push issue found for {args.date}.", file=sys.stderr)
            return 1
        issue_date, issue = selected[0]
    else:
        issue_date, issue = issues[0]

    papers = parse_papers(issue)
    if not papers:
        if issue_flag(issue, "no_update"):
            print(f"Skipped DOI validation for {issue_date}: no-update card has no paper list.")
            return 0
        print(f"No papers found for {issue_date}.", file=sys.stderr)
        return 1

    errors = validate(papers)
    if errors:
        print(f"DOI metadata validation failed for {issue_date}:", file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        return 1

    print(f"Validated {len(papers)} DOI records for {issue_date}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
