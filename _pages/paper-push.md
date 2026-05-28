---
layout: archive
title: "Paper Push"
permalink: /activities/paper-push/
author_profile: true
---

{% include base_path %}
{% include paper-push-assets.html %}

## Daily Literature Push

This page archives the daily BGC-Argo, ocean colour, marine heatwave and carbon-pump paper pushes.

<div class="paper-push-system-note">
  <strong>Automation note.</strong>
  This paper-push system is deployed on GitHub Actions for scheduled updates, with Codex maintaining the generation workflow, page updates, and ongoing automation adjustments.
</div>

<div class="paper-push-toolbar">
  <input class="paper-push-input" type="search" placeholder="Search saved papers" data-favorites-filter>
  <button class="paper-push-button" type="button" data-export-favorites>Export saved papers CSV</button>
</div>

<div data-favorites-table></div>

## Dates

<div class="paper-push-date-list">
{% for issue in site.data.paper_pushes %}
  <article class="paper-push-date-item">
    {% if issue.no_update %}
      <h3>{{ issue.date }}</h3>
    {% else %}
      <h3><a href="{{ base_path }}/activities/paper-push/{{ issue.date }}/">{{ issue.date }}</a></h3>
    {% endif %}
    <p class="paper-push-meta">Run date: {{ issue.generated_at | default: issue.display_date | default: issue.date }}</p>
    {% if issue.no_update %}
      <p class="paper-push-meta">{{ issue.summary_en | default: issue.summary }}</p>
    {% else %}
      <p class="paper-push-meta">Total papers: {{ issue.papers | size }}</p>
    {% endif %}
  </article>
{% endfor %}
</div>
