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

## <span data-paper-i18n="zh">{{{{ issue.title_zh | default: issue.title }}}}</span><span data-paper-i18n="en">{{{{ issue.title_en | default: issue.title }}}}</span>

<p class="paper-push-meta">
  <span data-paper-i18n="zh">{{{{ issue.summary_zh | default: issue.summary }}}}</span>
  <span data-paper-i18n="en">{{{{ issue.summary_en | default: issue.summary }}}}</span>
</p>

{{% if issue.docx %}}
<p><a class="btn" href="{{{{ issue.docx }}}}">Download Word summary</a></p>
{{% endif %}}

{{% if issue.figure %}}
<p><img src="{{{{ issue.figure }}}}" alt="Mechanism sketch for the daily paper push"></p>
{{% endif %}}

<div class="paper-push-toolbar">
  <div class="paper-push-language" aria-label="Paper push language">
    <button class="paper-push-button" type="button" data-paper-push-lang-button="zh" aria-pressed="false">中文</button>
    <button class="paper-push-button" type="button" data-paper-push-lang-button="en" aria-pressed="true">English</button>
  </div>
  <input class="paper-push-input" type="search" placeholder="Search saved papers" data-favorites-filter>
  <button class="paper-push-button" type="button" data-export-favorites>Export saved papers CSV</button>
</div>

<div data-favorites-table></div>

<section class="paper-push-trend">
  <h2><span data-paper-i18n="zh">趋势总结</span><span data-paper-i18n="en">Trend Summary</span></h2>
  <p class="paper-push-block" data-paper-i18n="zh">{{{{ issue.trend_zh | default: issue.summary_zh | default: issue.summary }}}}</p>
  <p class="paper-push-block" data-paper-i18n="en">{{{{ issue.trend_en | default: issue.summary_en | default: issue.summary }}}}</p>
</section>

{{% assign current_group = "" %}}
{{% for paper in issue.papers %}}
{{% if paper.group != current_group %}}
{{% assign current_group = paper.group %}}
<h2><span data-paper-i18n="zh">{{{{ paper.group_zh | default: paper.group }}}}</span><span data-paper-i18n="en">{{{{ paper.group_en | default: paper.group }}}}</span></h2>
{{% endif %}}

<article class="paper-push-paper">
  <h3>{{{{ forloop.index }}}}. {{{{ paper.title }}}}</h3>
  <p class="paper-push-meta">
    <strong><span data-paper-i18n="zh">作者</span><span data-paper-i18n="en">Authors</span>:</strong> {{{{ paper.authors }}}}<br>
    <strong><span data-paper-i18n="zh">发表月份</span><span data-paper-i18n="en">Publication month</span>:</strong>
    <span data-paper-i18n="zh">{{{{ paper.published_month_zh | default: paper.published_month | default: paper.published }}}}</span>
    <span data-paper-i18n="en">{{{{ paper.published_month | default: paper.published }}}}</span><br>
    {{{{ paper.journal }}}} &middot; DOI:
    <a href="https://doi.org/{{{{ paper.doi }}}}">{{{{ paper.doi }}}}</a>
  </p>
  <p>
    <strong><span data-paper-i18n="zh">关键词</span><span data-paper-i18n="en">Tags</span>:</strong>
    <span data-paper-i18n="zh">{{{{ paper.tags_zh | default: paper.tags }}}}</span>
    <span data-paper-i18n="en">{{{{ paper.tags_en | default: paper.tags }}}}</span>
  </p>
  <p class="paper-push-block" data-paper-i18n="zh">{{{{ paper.summary_zh | default: paper.summary }}}}</p>
  <p class="paper-push-block" data-paper-i18n="en">{{{{ paper.summary_en | default: paper.summary }}}}</p>
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
      data-published-month="{{{{ paper.published_month | default: paper.published | escape }}}}"
      data-doi="{{{{ paper.doi | escape }}}}"
      data-url="{{{{ paper.url | escape }}}}"
      data-summary="{{{{ paper.summary_zh | default: paper.summary | escape }}}}"
      data-summary-zh="{{{{ paper.summary_zh | default: paper.summary | escape }}}}"
      data-summary-en="{{{{ paper.summary_en | default: paper.summary | escape }}}}"
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
