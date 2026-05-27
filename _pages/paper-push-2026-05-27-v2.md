---
layout: archive
title: "Paper Push: 2026-05-27 v2 test"
permalink: /activities/paper-push/2026-05-27-v2/
author_profile: true
---

{% include base_path %}
{% include paper-push-assets.html %}

{% assign issue_date = "2026-05-27-v2" %}
{% assign issue = site.data.paper_pushes | where: "date", issue_date | first %}

<p><a href="{{ base_path }}/activities/paper-push/">Back to date list</a></p>

## <span data-paper-i18n="zh">{{ issue.title_zh | default: issue.title }}</span><span data-paper-i18n="en">{{ issue.title_en | default: issue.title }}</span>

<p class="paper-push-meta">
  <span data-paper-i18n="zh">{{ issue.summary_zh | default: issue.summary }}</span>
  <span data-paper-i18n="en">{{ issue.summary_en | default: issue.summary }}</span>
</p>

<div class="paper-push-toolbar">
  <div class="paper-push-language" aria-label="Paper push language">
    <button class="paper-push-button" type="button" data-paper-push-lang-button="zh" aria-pressed="true">Chinese</button>
    <button class="paper-push-button" type="button" data-paper-push-lang-button="en" aria-pressed="false">English</button>
  </div>
</div>

<section class="paper-push-trend">
  <h2><span data-paper-i18n="zh">Test Note</span><span data-paper-i18n="en">Test Note</span></h2>
  <p class="paper-push-block" data-paper-i18n="zh">{{ issue.trend_zh | default: issue.summary_zh | default: issue.summary }}</p>
  <p class="paper-push-block" data-paper-i18n="en">{{ issue.trend_en | default: issue.summary_en | default: issue.summary }}</p>
</section>
