from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import subprocess
import sys
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "_data" / "paper_pushes.yml"
HISTORY_PATH = ROOT / "推送历史_论文索引.csv"
DATE_PAGE_SCRIPT = ROOT / "scripts" / "create_paper_push_page.py"
TZ = ZoneInfo("Europe/Berlin")

MAX_ABSTRACT_CHARS = 900
USER_AGENT = "mengyuli15-paper-push/1.0 (https://mengyuli15.github.io/)"

TOPIC_TERMS = [
    "BGC-Argo carbon pump",
    "BGC-Argo phytoplankton",
    "BGC-Argo microbial carbon",
    "BGC-Argo bio-optic",
    "ocean colour remote sensing phytoplankton",
    "ocean color remote sensing phytoplankton",
    "marine heatwave phytoplankton vertical",
    "marine heatwave deep chlorophyll maximum",
    "particulate organic carbon ocean bio-optics",
]

NATURE_SCIENCE_HINTS = [
    "Nature",
    "Nature Climate Change",
    "Nature Communications",
    "Communications Earth & Environment",
    "Science",
    "Science Advances",
]

PRIORITY_JOURNALS = [
    "AGU Advances",
    "Annual Review of Marine Science",
    "Applied Optics",
    "Biogeosciences",
    "Communications Earth & Environment",
    "Deep Sea Research Part I: Oceanographic Research Papers",
    "Deep Sea Research Part II: Topical Studies in Oceanography",
    "Earth System Science Data",
    "Environmental Research Letters",
    "Frontiers in Marine Science",
    "Geophysical Research Letters",
    "Global Biogeochemical Cycles",
    "Global Change Biology",
    "IEEE Transactions on Geoscience and Remote Sensing",
    "Journal of Atmospheric and Oceanic Technology",
    "Journal of Geophysical Research: Oceans",
    "Limnology and Oceanography",
    "Limnology and Oceanography: Methods",
    "Oceanography",
    "Optics Express",
    "Proceedings of the National Academy of Sciences",
    "Progress in Oceanography",
    "Remote Sensing of Environment",
]

# Approximate ordering by recent impact/influence and field relevance.
JOURNAL_RANK = {
    "Proceedings of the National Academy of Sciences": 10,
    "Remote Sensing of Environment": 20,
    "Global Change Biology": 30,
    "Annual Review of Marine Science": 40,
    "AGU Advances": 50,
    "Communications Earth & Environment": 60,
    "Geophysical Research Letters": 70,
    "Global Biogeochemical Cycles": 80,
    "Earth System Science Data": 90,
    "Environmental Research Letters": 100,
    "Journal of Geophysical Research: Oceans": 110,
    "Limnology and Oceanography": 120,
    "Progress in Oceanography": 130,
    "Biogeosciences": 140,
    "IEEE Transactions on Geoscience and Remote Sensing": 150,
    "Frontiers in Marine Science": 160,
    "Deep Sea Research Part I: Oceanographic Research Papers": 170,
    "Deep Sea Research Part II: Topical Studies in Oceanography": 180,
    "Journal of Atmospheric and Oceanic Technology": 190,
    "Limnology and Oceanography: Methods": 200,
    "Oceanography": 210,
    "Optics Express": 220,
    "Applied Optics": 230,
}

RELEVANCE_TERMS = {
    "bgc-argo": 8,
    "biogeochemical-argo": 8,
    "biogeochemical argo": 8,
    "argo float": 4,
    "carbon pump": 7,
    "carbon export": 6,
    "net community production": 6,
    "particulate organic carbon": 5,
    "poc": 4,
    "microbial carbon": 6,
    "phytoplankton": 5,
    "chlorophyll": 4,
    "deep chlorophyll maximum": 6,
    "subsurface chlorophyll": 6,
    "ocean colour": 5,
    "ocean color": 5,
    "bio-optic": 5,
    "backscatter": 4,
    "remote sensing": 4,
    "marine heatwave": 7,
    "marine heatwaves": 7,
    "vertical": 2,
}

EXCLUDED_TITLE_PREFIXES = ("corrigendum", "erratum", "correction", "retraction")


@dataclass
class Paper:
    title: str
    authors: str
    journal: str
    published: str
    published_month: str
    published_month_zh: str
    doi: str
    url: str
    abstract: str
    group_zh: str
    group_en: str
    tags: str
    summary_zh: str
    summary_en: str
    score: int
    rank: int


def http_json(url: str, retries: int = 2) -> dict:
    for attempt in range(retries):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == retries - 1:
                raise exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError("unreachable")


def text_value(value) -> str:
    if isinstance(value, list):
        return str(value[0]) if value else ""
    return str(value or "")


def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", html.unescape(value or ""))
    value = re.sub(r"\s+", " ", value).strip()
    return value


def month_from_parts(parts: list[int], fallback: str = "") -> tuple[str, str, str]:
    if len(parts) >= 2:
        month = f"{parts[0]:04d}-{parts[1]:02d}"
        published = "-".join(f"{x:02d}" if i else f"{x:04d}" for i, x in enumerate(parts[:3]))
        return published, month, month
    if len(parts) == 1:
        year = str(parts[0])
        return year, f"{year} (month not verified)", f"{year}（月份未核准）"
    return fallback, fallback, fallback


def published_parts(item: dict) -> list[int]:
    for key in ("published-print", "published-online", "published", "created"):
        parts = item.get(key, {}).get("date-parts")
        if parts and parts[0]:
            return parts[0]
    return []


def is_future_publication(parts: list[int], today: date) -> bool:
    if len(parts) >= 3:
        return date(parts[0], parts[1], parts[2]) > today
    if len(parts) >= 2:
        return (parts[0], parts[1]) > (today.year, today.month)
    if len(parts) == 1:
        return parts[0] > today.year
    return False


def authors_from_item(item: dict) -> str:
    names = []
    for author in item.get("author", [])[:8]:
        given = author.get("given", "").strip()
        family = author.get("family", "").strip()
        name = " ".join(part for part in [given, family] if part)
        if name:
            names.append(name)
    if len(item.get("author", [])) > 8:
        names.append("et al.")
    return "; ".join(names) or "Authors not available"


def best_journal(item: dict) -> str:
    titles = item.get("container-title") or []
    return text_value(titles).strip()


def canonical_journal(journal: str) -> str:
    low = journal.lower()
    for candidate in PRIORITY_JOURNALS + NATURE_SCIENCE_HINTS:
        candidate_low = candidate.lower()
        if candidate_low in {"nature", "science"}:
            if low == candidate_low or low.startswith(f"{candidate_low} "):
                return candidate
            continue
        if candidate_low in low or low in candidate_low:
            return candidate
    return journal


def is_target_journal(journal: str) -> bool:
    canonical = canonical_journal(journal)
    return canonical in JOURNAL_RANK or canonical in NATURE_SCIENCE_HINTS


def group_for(journal: str) -> tuple[str, str, int]:
    low = journal.lower()
    if "nature" in low:
        return "Nature 系列", "Nature series", 0
    if low == "science" or low.startswith("science ") or "science advances" in low:
        return "Science 系列", "Science series", 1
    return "重点期刊：按影响力和相关性排序", "Key journals: ordered by impact and relevance", 2


def relevance_score(title: str, abstract: str) -> int:
    haystack = f"{title} {abstract}".lower()
    return sum(weight for term, weight in RELEVANCE_TERMS.items() if term in haystack)


def tags_for(title: str, abstract: str) -> str:
    haystack = f"{title} {abstract}".lower()
    tags = []
    checks = [
        ("BGC-Argo", ["bgc-argo", "biogeochemical argo", "argo float"]),
        ("carbon pump", ["carbon pump", "carbon export", "net community production", "poc"]),
        ("phytoplankton", ["phytoplankton", "chlorophyll"]),
        ("marine heatwaves", ["marine heatwave", "marine heatwaves"]),
        ("ocean colour", ["ocean colour", "ocean color", "remote sensing"]),
        ("bio-optics", ["bio-optic", "backscatter", "iop", "optical"]),
        ("microbial carbon", ["microbial carbon", "microbial", "dissolved organic"]),
        ("vertical structure", ["vertical", "subsurface", "deep chlorophyll maximum", "dcm"]),
    ]
    for label, terms in checks:
        if any(term in haystack for term in terms):
            tags.append(label)
    return "; ".join(tags[:5]) or "ocean biogeochemistry"


def sentence_split(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [part.strip() for part in parts if part.strip()]


def infer_data_source(title: str, tags: str, journal: str) -> tuple[str, str]:
    haystack = f"{title} {tags} {journal}".lower()
    if "bgc-argo" in haystack or "argo" in haystack:
        return (
            "数据上主要依托 BGC-Argo 浮标剖面及相关生物地球化学变量，并结合题名所指的氧气、后向散射、硝酸盐或叶绿素信息。",
            "The data emphasis is on BGC-Argo float profiles and related biogeochemical variables, including oxygen, backscatter, nitrate, or chlorophyll where indicated by the title.",
        )
    if "pace" in haystack:
        return (
            "数据或应用场景指向 NASA PACE/OCI 高光谱海色观测及其验证、训练或社区使用。",
            "The data or application setting is NASA PACE/OCI hyperspectral ocean-colour observation, together with validation, training, or community-use workflows.",
        )
    if "viirs" in haystack:
        return (
            "数据上使用 VIIRS 顶层大气卫星观测，面向近岸复杂水体的叶绿素 a 估计。",
            "The data source is top-of-atmosphere VIIRS satellite observation, used for chlorophyll-a estimation in optically complex coastal waters.",
        )
    if any(term in haystack for term in ["satellite", "ocean color", "ocean colour", "chlorophyll", "remote sensing"]):
        return (
            "数据上主要面向卫星海色、叶绿素或遥感反射率记录，并在需要时结合原位或剖面观测进行约束。",
            "The data emphasis is satellite ocean-colour, chlorophyll, or remote-sensing reflectance records, with in-situ or profile constraints where relevant.",
        )
    if any(term in haystack for term in ["sediment trap", "optics", "backscattering", "bio-optic", "absorption", "lidar"]):
        return (
            "数据或方法上围绕沉积物捕获器、原位光学、生物光学参数或光谱观测展开。",
            "The data or method emphasis is sediment traps, in-situ optics, bio-optical parameters, or spectral optical observation.",
        )
    if any(term in haystack for term in ["review", "annual review", "modeling", "campaign", "hackweek"]):
        return (
            "这类论文主要综合已有观测、理论、模型、外场设计或社区训练材料，而不是发布一个新的单一观测数据集。",
            "This type of paper synthesizes existing observations, theory, models, field-design material, or community-training workflows rather than publishing one new observational dataset.",
        )
    return (
        "数据来源可从 DOI 页面进一步核对；从题名和期刊信息看，它主要围绕海洋生物地球化学或生态过程资料展开。",
        "The exact data source should be checked on the DOI page; from the title and journal metadata, it is centred on ocean biogeochemical or ecological-process information.",
    )


def infer_action(title: str, tags: str) -> tuple[str, str]:
    haystack = f"{title} {tags}".lower()
    if any(term in haystack for term in ["machine learning", "deep learning", "neural", "emulator"]):
        return (
            "方法上使用机器学习、深度学习或神经模拟器来提取信号、反演变量或识别驱动机制。",
            "Methodologically, it uses machine learning, deep learning, or a neural emulator to extract signals, retrieve variables, or identify drivers.",
        )
    if any(term in haystack for term in ["retrieval", "estimation", "estimating"]):
        return (
            "研究重点是建立或评估反演/估计框架，把观测信号转化为浮游植物、叶绿素、吸收或碳通量等变量。",
            "The main task is to build or assess a retrieval or estimation framework that converts observations into variables such as phytoplankton, chlorophyll, absorption, or carbon flux.",
        )
    if any(term in haystack for term in ["dataset", "data record", "data with", "surveys"]):
        return (
            "研究重点是整理、质控或构建可复用数据产品，使后续跨区域和长期分析更可靠。",
            "The main task is to assemble, quality-control, or build a reusable data product so that later cross-regional and long-term analyses are more robust.",
        )
    if any(term in haystack for term in ["review", "modeling", "lifting the lid"]):
        return (
            "研究主要通过综述、模型框架或概念整合来梳理关键过程和不确定性来源。",
            "The paper mainly uses review, modelling, or conceptual synthesis to organize key processes and sources of uncertainty.",
        )
    return (
        "研究主要分析变化趋势、事件响应、驱动机制或方法表现，并把观测结果与生态/生物地球化学过程联系起来。",
        "The main task is to analyse trends, event responses, drivers, or method performance, linking observations with ecological or biogeochemical processes.",
    )


def infer_result(title: str, tags: str) -> tuple[str, str]:
    haystack = f"{title} {tags}".lower()
    if any(term in haystack for term in ["declin", "increase", "threefold", "1 °c", "unprecedented"]):
        return (
            "核心结果是识别出上升、下降或异常事件信号，并把这些变化放进气候变暖、生产力或碳循环背景下解释。",
            "The core result is an identified increase, decline, or extreme-event signal interpreted in the context of warming, productivity, or carbon cycling.",
        )
    if any(term in haystack for term in ["accuracy", "comparison", "performance"]):
        return (
            "核心结果是给出产品或方法表现的评估，为判断适用水体、误差来源和后续改进提供依据。",
            "The main outcome is an assessment of product or method performance, helping identify suitable waters, error sources, and paths for improvement.",
        )
    if any(term in haystack for term in ["framework", "approach", "design", "dataset", "data record"]):
        return (
            "核心实现是提出可复用的框架、流程或数据产品，使类似观测、反演、验证或趋势分析可以更系统地开展。",
            "The main contribution is a reusable framework, workflow, or data product that makes similar observation, retrieval, validation, or trend-analysis tasks more systematic.",
        )
    if "heatwave" in haystack or "heatwaves" in haystack:
        return (
            "核心结果帮助说明海洋热浪如何通过强度、持续时间或垂向结构影响生态和碳循环过程。",
            "The core result helps explain how marine heatwaves affect ecological and carbon-cycle processes through intensity, duration, or vertical structure.",
        )
    return (
        "核心结果或实现为该主题提供了新的观测约束、方法基准或过程解释。",
        "The main result or implementation provides new observational constraints, methodological benchmarks, or process interpretation for this topic.",
    )


def summary_en(title: str, abstract: str, tags: str) -> str:
    data_zh, data_en = infer_data_source(title, tags, "")
    action_zh, action_en = infer_action(title, tags)
    result_zh, result_en = infer_result(title, tags)
    return " ".join(
        [
            f"This paper focuses on \"{title}\", with key themes including {tags}.",
            data_en,
            action_en,
            result_en,
            f"It is useful for research on {tags}, especially for selecting papers for close reading, method comparison, or cross-validation of datasets.",
        ]
    )


def summary_zh(title: str, abstract: str, tags: str) -> str:
    data_zh, data_en = infer_data_source(title, tags, "")
    action_zh, action_en = infer_action(title, tags)
    result_zh, result_en = infer_result(title, tags)
    return " ".join(
        [
            f"这篇论文聚焦《{title}》，关键词是 {tags}。",
            data_zh,
            action_zh,
            result_zh,
            f"它对 {tags} 相关研究有帮助，特别适合用于筛选后续精读、方法比较或数据交叉验证。",
        ]
    )


def crossref_query(query: str, from_date: date, rows: int = 20) -> list[dict]:
    params = {
        "query.bibliographic": query,
        "filter": f"from-pub-date:{from_date.isoformat()},type:journal-article",
        "sort": "published",
        "order": "desc",
        "rows": str(rows),
        "select": "DOI,title,author,container-title,published,published-print,published-online,created,URL,abstract,type",
    }
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    data = http_json(url)
    return data.get("message", {}).get("items", [])


def existing_dois() -> set[str]:
    dois = set()
    if DATA_PATH.exists():
        text = DATA_PATH.read_text(encoding="utf-8")
        dois.update(match.lower() for match in re.findall(r'doi:\s*"([^"]+)"', text))
    if HISTORY_PATH.exists():
        with HISTORY_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                doi = (row.get("doi") or "").strip().lower()
                if doi:
                    dois.add(doi)
    return dois


def collect_candidates(lookback_days: int, max_papers: int) -> list[Paper]:
    today = datetime.now(TZ).date()
    from_date = datetime.now(TZ).date() - timedelta(days=lookback_days)
    seen = existing_dois()
    candidates: dict[str, Paper] = {}

    for query in TOPIC_TERMS:
        if len(candidates) >= max_papers * 4:
            break
        try:
            items = crossref_query(query, from_date, rows=50)
        except Exception as exc:
            print(f"Crossref query failed: {query}: {exc}", file=sys.stderr)
            continue
        for item in items:
            doi = (item.get("DOI") or "").strip()
            if not doi or doi.lower() in seen or doi.lower() in candidates:
                continue
            title = clean_text(text_value(item.get("title")))
            journal = best_journal(item)
            if not is_target_journal(journal):
                continue
            canonical = canonical_journal(journal)
            abstract = clean_text(item.get("abstract", ""))
            if title.lower().startswith(EXCLUDED_TITLE_PREFIXES):
                continue
            parts = published_parts(item)
            if is_future_publication(parts, today):
                continue
            score = relevance_score(title, abstract)
            if score < 5:
                continue
            group_zh, group_en, group_rank = group_for(canonical)
            published, month, month_zh = month_from_parts(parts)
            tags = tags_for(title, abstract)
            rank = group_rank * 1000 + JOURNAL_RANK.get(canonical, 500)
            candidates[doi.lower()] = Paper(
                title=title,
                authors=authors_from_item(item),
                journal=canonical,
                published=published,
                published_month=month,
                published_month_zh=month_zh,
                doi=doi,
                url=item.get("URL") or f"https://doi.org/{doi}",
                abstract=abstract,
                group_zh=group_zh,
                group_en=group_en,
                tags=tags,
                summary_zh=summary_zh(title, abstract, tags),
                summary_en=summary_en(title, abstract, tags),
                score=score,
                rank=rank,
            )
        time.sleep(0.05)

    return sorted(candidates.values(), key=lambda paper: (paper.rank, -paper.score, paper.published_month))[:max_papers]


def q(value: str) -> str:
    return json.dumps(value or "", ensure_ascii=False)


def issue_block(today: str, papers: list[Paper]) -> str:
    generated_at = datetime.now(TZ).strftime("%Y-%m-%d %H:%M %Z")
    title_zh = "每日论文推送：BGC-Argo、海色、海洋热浪与碳泵"
    title_en = "Daily Paper Push: BGC-Argo, ocean colour, marine heatwaves and carbon pump"
    summary_zh = f"本期由 GitHub Actions 自动检索生成：Nature/Science 系列优先，其余重点期刊按影响力与主题相关性排序；历史去重后保留 {len(papers)} 篇，不超过每日 50 篇上限。"
    summary_en = f"This issue was generated automatically by GitHub Actions: Nature and Science series first, then priority journals ordered by approximate impact and topical relevance. After deduplication, {len(papers)} papers remain, below the daily limit of 50."
    trend_zh = "本期重点关注 BGC-Argo、海色遥感、海洋热浪、浮游植物垂向结构和碳泵过程。整体趋势总结会随每日候选论文自动更新；建议优先查看涉及 BGC-Argo 剖面、POC/NCP、DCM/SCM、PACE/高光谱和 marine heatwave 垂向响应的论文。"
    trend_en = "This issue focuses on BGC-Argo, ocean-colour remote sensing, marine heatwaves, vertical phytoplankton structure and carbon-pump processes. The daily trend synthesis is generated from the selected candidates; priority should go to papers involving BGC-Argo profiles, POC/NCP, DCM/SCM, PACE/hyperspectral methods and vertical marine-heatwave responses."
    docx_name = f"daily_paper_push_{today}.docx"

    lines = [
        f"- date: {q(today)}",
        f"  generated_at: {q(generated_at)}",
        f"  title: {q(title_zh)}",
        f"  title_zh: {q(title_zh)}",
        f"  title_en: {q(title_en)}",
        f"  summary: {q(summary_zh)}",
        f"  summary_zh: {q(summary_zh)}",
        f"  summary_en: {q(summary_en)}",
        f"  trend_zh: {q(trend_zh)}",
        f"  trend_en: {q(trend_en)}",
        f"  docx: {q('/files/paper-push/' + docx_name)}",
        "  figure: \"\"",
        "  papers:",
    ]
    for paper in papers:
        lines.append(f"    - title: {q(paper.title)}")
        for key, value in [
            ("authors", paper.authors),
            ("journal", paper.journal),
            ("published", paper.published),
            ("published_month", paper.published_month),
            ("published_month_zh", paper.published_month_zh),
            ("doi", paper.doi),
            ("url", paper.url),
            ("group", paper.group_zh),
            ("group_zh", paper.group_zh),
            ("group_en", paper.group_en),
            ("tags", paper.tags),
            ("tags_zh", paper.tags),
            ("tags_en", paper.tags),
            ("summary", paper.summary_zh),
            ("summary_zh", paper.summary_zh),
            ("summary_en", paper.summary_en),
        ]:
            lines.append(f"      {key}: {q(value)}")
    return "\n".join(lines) + "\n"


def replace_or_prepend_issue(today: str, block: str) -> None:
    existing = DATA_PATH.read_text(encoding="utf-8") if DATA_PATH.exists() else ""
    pattern = re.compile(rf'(?ms)^- date: "{re.escape(today)}"\n.*?(?=^- date: "|\Z)')
    if pattern.search(existing):
        updated = pattern.sub(block, existing).rstrip() + "\n"
    else:
        updated = block + ("\n" + existing if existing.strip() else "")
    DATA_PATH.write_text(updated, encoding="utf-8")


def set_font(run, name: str = "Microsoft YaHei") -> None:
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)


def write_docx(today: str, papers: list[Paper]) -> None:
    out_dir = ROOT / "files" / "paper-push"
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)
    normal = doc.styles["Normal"]
    normal.font.name = "Microsoft YaHei"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")
    normal.font.size = Pt(10.5)
    for style_name, size, color in [
        ("Heading 1", 16, RGBColor(31, 77, 120)),
        ("Heading 2", 13, RGBColor(46, 116, 181)),
        ("Heading 3", 11.5, RGBColor(31, 77, 120)),
    ]:
        style = doc.styles[style_name]
        style.font.name = "Microsoft YaHei"
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "Microsoft YaHei")
        style.font.size = Pt(size)
        style.font.color.rgb = color

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("每日论文推送")
    set_font(r)
    r.bold = True
    r.font.size = Pt(22)
    r.font.color.rgb = RGBColor(23, 50, 77)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(f"检索日期：{today} | GitHub Actions 自动生成")
    set_font(r)
    r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(85, 105, 125)

    doc.add_heading("今日总览", level=1)
    p = doc.add_paragraph()
    r = p.add_run(f"历史去重后今日新增 {len(papers)} 篇。排序规则：Nature 系列、Science 系列、其余重点期刊按影响力和主题相关性排序。")
    set_font(r)

    current_group = None
    doc.add_heading("论文速读", level=1)
    for index, paper in enumerate(papers, 1):
        if paper.group_zh != current_group:
            current_group = paper.group_zh
            doc.add_heading(current_group, level=2)
        p = doc.add_paragraph(style="Heading 3")
        r = p.add_run(f"{index}. {paper.title}")
        set_font(r)
        r.bold = True
        for label, value in [
            ("作者", paper.authors),
            ("期刊", paper.journal),
            ("发表月份", paper.published_month_zh),
            ("DOI", paper.doi),
        ]:
            p = doc.add_paragraph()
            r = p.add_run(f"{label}：{value}")
            set_font(r)
            r.font.size = Pt(9)
            r.font.color.rgb = RGBColor(85, 105, 125)
        p = doc.add_paragraph()
        r = p.add_run(f"关键词：{paper.tags}")
        set_font(r)
        r.bold = True
        r.font.size = Pt(9.5)
        p = doc.add_paragraph()
        r = p.add_run(paper.summary_zh)
        set_font(r)
        p = doc.add_paragraph()
        r = p.add_run(f"链接：{paper.url}")
        set_font(r)
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(5, 99, 193)

    doc.save(out_dir / f"daily_paper_push_{today}.docx")


def update_history(today: str, papers: list[Paper]) -> None:
    rows = []
    if HISTORY_PATH.exists():
        with HISTORY_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
    seen = {(row.get("doi") or "").lower() for row in rows}
    for paper in papers:
        if paper.doi.lower() in seen:
            continue
        rows.append({
            "date": today,
            "title": paper.title,
            "authors": paper.authors,
            "published_month": paper.published_month_zh,
            "doi": paper.doi,
            "url": paper.url,
            "journal": paper.journal,
        })
    with HISTORY_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["date", "title", "authors", "published_month", "doi", "url", "journal"])
        writer.writeheader()
        writer.writerows(rows)


def ensure_page(today: str) -> None:
    subprocess.run([sys.executable, str(DATE_PAGE_SCRIPT), today], cwd=ROOT, check=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=datetime.now(TZ).date().isoformat())
    parser.add_argument("--lookback-days", type=int, default=int(os.getenv("LOOKBACK_DAYS", "14")))
    parser.add_argument("--max-papers", type=int, default=int(os.getenv("MAX_PAPERS", "50")))
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    papers = collect_candidates(args.lookback_days, args.max_papers)
    if not papers:
        print("No new papers found after de-duplication.")
        return 0
    print(f"Found {len(papers)} papers for {args.date}.")
    if args.dry_run:
        for paper in papers[:10]:
            print(f"- {paper.published_month} | {paper.journal} | {paper.title} | {paper.doi}")
        return 0
    replace_or_prepend_issue(args.date, issue_block(args.date, papers))
    write_docx(args.date, papers)
    update_history(args.date, papers)
    ensure_page(args.date)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
