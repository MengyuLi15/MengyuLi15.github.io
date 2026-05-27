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

<div class="paper-push-toolbar">
  <input class="paper-push-input" type="search" placeholder="Search saved papers" data-favorites-filter>
  <button class="paper-push-button" type="button" data-export-favorites>Export saved papers CSV</button>
</div>

<div data-favorites-table></div>

## Dates

<div class="paper-push-date-list">
{% for issue in site.data.paper_pushes %}
  <article class="paper-push-date-item">
    <h3><a href="{{ base_path }}/activities/paper-push/{{ issue.date }}/">{{ issue.date }}</a></h3>
    <p class="paper-push-meta">{{ issue.summary }}</p>
    <p class="paper-push-meta">{{ issue.papers | size }} papers</p>
  </article>
{% endfor %}
</div>
