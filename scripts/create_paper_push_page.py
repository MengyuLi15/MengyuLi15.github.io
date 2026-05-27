from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / "_pages"

TEMPLATE = """---
layout: archive
title: "Paper Push: {date}"
permalink: /activities/paper-push/{date}/
author_profile: true
---

{{% include base_path %}}
{{% include paper-push-assets.html %}}

{{% assign issue_date = "{date}" %}}
{{% assign issue = site.data.paper_pushes | where: "date", issue_date | first %}}

<p><a href="{{{{ base_path }}}}/activities/paper-push/">Back to date list</a></p>

## {{{{ issue.title }}}}

<p class="paper-push-meta">{{{{ issue.summary }}}}</p>

{{% if issue.docx %}}
<p><a class="btn" href="{{{{ issue.docx }}}}">Download Word summary</a></p>
{{% endif %}}

{{% if issue.figure %}}
<p><img src="{{{{ issue.figure }}}}" alt="Mechanism sketch for the daily paper push"></p>
{{% endif %}}

<div class="paper-push-toolbar">
  <input class="paper-push-input" type="search" placeholder="Search saved papers" data-favorites-filter>
  <button class="paper-push-button" type="button" data-export-favorites>Export saved papers CSV</button>
</div>

<div data-favorites-table></div>

{{% assign current_group = "" %}}
{{% for paper in issue.papers %}}
{{% if paper.group != current_group %}}
{{% assign current_group = paper.group %}}
<h2>{{{{ current_group }}}}</h2>
{{% endif %}}

<article class="paper-push-paper">
  <h3>{{{{ forloop.index }}}}. {{{{ paper.title }}}}</h3>
  <p class="paper-push-meta">
    {{{{ paper.authors }}}}<br>
    {{{{ paper.journal }}}} &middot; {{{{ paper.published }}}} &middot; DOI:
    <a href="https://doi.org/{{{{ paper.doi }}}}">{{{{ paper.doi }}}}</a>
  </p>
  <p><strong>Tags:</strong> {{{{ paper.tags }}}}</p>
  <p>{{{{ paper.summary }}}}</p>
  <div class="paper-push-paper-actions">
    <a class="paper-push-button" href="{{{{ paper.url }}}}">Open paper</a>
    <button
      class="favorite-button"
      type="button"
      data-favorite-paper
      data-issue-date="{{{{ issue.date | escape }}}}"
      data-title="{{{{ paper.title | escape }}}}"
      data-authors="{{{{ paper.authors | escape }}}}"
      data-journal="{{{{ paper.journal | escape }}}}"
      data-published="{{{{ paper.published | escape }}}}"
      data-doi="{{{{ paper.doi | escape }}}}"
      data-url="{{{{ paper.url | escape }}}}"
      data-summary="{{{{ paper.summary | escape }}}}"
      aria-pressed="false">Save</button>
  </div>
</article>
{{% endfor %}}
"""


def main() -> int:
    if len(sys.argv) != 2 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", sys.argv[1]):
        print("Usage: python scripts/create_paper_push_page.py YYYY-MM-DD", file=sys.stderr)
        return 2

    date = sys.argv[1]
    out_path = PAGES_DIR / f"paper-push-{date}.md"
    if out_path.exists():
        print(f"Exists: {out_path}")
        return 0

    out_path.write_text(TEMPLATE.format(date=date), encoding="utf-8")
    print(f"Created: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
