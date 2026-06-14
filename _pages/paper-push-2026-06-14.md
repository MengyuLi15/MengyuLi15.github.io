---
layout: archive
title: "Paper Push: 2026-06-14"
permalink: /activities/paper-push/2026-06-14/
author_profile: true
---

{% include base_path %}
{% include paper-push-assets.html %}

{% assign issue_date = "2026-06-14" %}
{% assign issue = site.data.paper_pushes | where: "date", issue_date | first %}

<p><a href="{{ base_path }}/activities/paper-push/">Back to date list</a></p>

## <span data-paper-i18n="zh">{{ issue.title_zh | default: issue.title }}</span><span data-paper-i18n="en">{{ issue.title_en | default: issue.title }}</span>

<p class="paper-push-meta">
  <span data-paper-i18n="zh">{{ issue.summary_zh | default: issue.summary }}</span>
  <span data-paper-i18n="en">{{ issue.summary_en | default: issue.summary }}</span>
</p>

{% if issue.docx %}
<p><a class="btn" href="{{ issue.docx }}">Download Word summary</a></p>
{% endif %}

{% if issue.figure and issue.figure != "" %}
<p><img src="{{ issue.figure }}" alt="Mechanism sketch for the daily paper push"></p>
{% else %}
<section class="paper-push-italian-card" aria-label="Daily Italian card">
  <p class="paper-push-system-note">
    <span data-paper-i18n="zh">无 mechanism sketch 图。今天的意大利语卡片：</span>
    <span data-paper-i18n="en">No mechanism sketch figure today. Daily Italian card:</span>
  </p>
  <h2><span data-paper-i18n="zh">每日一句意大利语</span><span data-paper-i18n="en">Daily Italian</span></h2>
  <p class="paper-push-italian-phrase">{{ issue.italian_phrase | default: "Nel mezzo del cammin di nostra vita, mi ritrovai per una selva oscura." }}</p>
  <p class="paper-push-meta">{{ issue.italian_source | default: "Dante, Commedia, Inferno I, 1-2; Italian original from Kalliope" }}</p>
  <p class="paper-push-block" data-paper-i18n="zh">{{ issue.italian_explanation_zh | default: "这是 Kalliope 所列《神曲》意大利语原文。现代意大利语可理解为“在人生旅程的中途，我发现自己走入一片黑暗森林”；常用来表达迷茫、转折和重新寻找方向。" }}</p>
  <p class="paper-push-block" data-paper-i18n="en">{{ issue.italian_explanation_en | default: "This follows the Italian original listed by Kalliope. In modern terms, it means that midway through life's journey, the speaker finds himself in a dark wood, a scene of disorientation and renewed searching." }}</p>
</section>
{% endif %}

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
  <p class="paper-push-block" data-paper-i18n="zh">{{ issue.trend_zh | default: issue.summary_zh | default: issue.summary }}</p>
  <p class="paper-push-block" data-paper-i18n="en">{{ issue.trend_en | default: issue.summary_en | default: issue.summary }}</p>
</section>

{% assign current_group = "" %}
{% for paper in issue.papers %}
{% if paper.group != current_group %}
{% assign current_group = paper.group %}
<h2><span data-paper-i18n="zh">{{ paper.group_zh | default: paper.group }}</span><span data-paper-i18n="en">{{ paper.group_en | default: paper.group }}</span></h2>
{% endif %}

<article class="paper-push-paper">
  <h3>{{ forloop.index }}. {{ paper.title }}</h3>
  <p class="paper-push-meta">
    <strong><span data-paper-i18n="zh">作者</span><span data-paper-i18n="en">Authors</span>:</strong> {{ paper.authors }}<br>
    <strong><span data-paper-i18n="zh">发表月份</span><span data-paper-i18n="en">Publication month</span>:</strong>
    <span data-paper-i18n="zh">{{ paper.published_month_zh | default: paper.published_month | default: paper.published }}</span>
    <span data-paper-i18n="en">{{ paper.published_month | default: paper.published }}</span><br>
    {{ paper.journal }} &middot; DOI:
    <a href="https://doi.org/{{ paper.doi }}">{{ paper.doi }}</a>
  </p>
  <p>
    <strong><span data-paper-i18n="zh">关键词</span><span data-paper-i18n="en">Tags</span>:</strong>
    <span data-paper-i18n="zh">{{ paper.tags_zh | default: paper.tags }}</span>
    <span data-paper-i18n="en">{{ paper.tags_en | default: paper.tags }}</span>
  </p>
  <p class="paper-push-block paper-push-abstract" data-paper-i18n="zh">{{ paper.summary_zh | default: paper.summary }}</p>
  <p class="paper-push-block paper-push-abstract" data-paper-i18n="en">{{ paper.summary_en | default: paper.summary }}</p>
  <div class="paper-push-paper-actions">
    <a class="paper-push-button" href="{{ paper.url }}">Open paper</a>
    <button
      class="favorite-button"
      type="button"
      data-favorite-paper
      data-issue-date="{{ issue.date | escape }}"
      data-title="{{ paper.title | escape }}"
      data-authors="{{ paper.authors | escape }}"
      data-journal="{{ paper.journal | escape }}"
      data-published="{{ paper.published | escape }}"
      data-published-month="{{ paper.published_month | default: paper.published | escape }}"
      data-doi="{{ paper.doi | escape }}"
      data-url="{{ paper.url | escape }}"
      data-summary="{{ paper.summary_zh | default: paper.summary | escape }}"
      data-summary-zh="{{ paper.summary_zh | default: paper.summary | escape }}"
      data-summary-en="{{ paper.summary_en | default: paper.summary | escape }}"
      aria-pressed="false">Save</button>
  </div>
</article>
{% endfor %}
