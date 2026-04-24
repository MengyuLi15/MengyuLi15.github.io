---
layout: archive
title: "Activities"
permalink: /teaching/
author_profile: true
---

<style>
/* 卡片 */
.activity-card {
  padding: 1.5rem 1.6rem;
  margin: 1.2rem 0;
  border-radius: 18px;
  border: 1px solid rgba(120,120,120,0.18);
  background: var(--global-bg-color, #ffffff);
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

/* 左右布局 */
.activity-flex {
  display: flex;
  gap: 1.4rem;
  align-items: stretch;   /* 👈 关键：让图片和卡片同高 */
}

.activity-flex-text {
  flex: 1;
  min-width: 0;
}

/* 右侧图片（整块） */
.activity-image-box {
  flex: 0 0 240px;   /* 控制宽度 */
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid rgba(120,120,120,0.15);
  display: flex;
}

/* 图片填满 */
.activity-image-box img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

/* hover 动效（可删） */
.activity-image-box:hover img {
  transform: scale(1.05);
}

/* 标题 */
.activity-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--global-text-color, #222);
  margin-bottom: 0.35rem;
}

/* 副标题 */
.activity-subtitle {
  font-size: 0.95rem;
  color: var(--global-text-color, #333);
  margin-bottom: 0.35rem;
}

/* meta 信息 */
.activity-meta {
  font-size: 0.88rem;
  color: var(--global-text-color-light, #666);
  margin-bottom: 0.6rem;
  line-height: 1.45;
}

/* 主列表 */
.activity-list {
  margin: 0.6rem 0 0 1.1rem;
  padding: 0;
  font-size: 0.92rem;
  line-height: 1.6;
  color: var(--global-text-color, #333);
}

.activity-list li {
  margin-bottom: 6px;
}

/* 日期列表 */
.activity-date-list {
  margin: 0.3rem 0 0.7rem 1.1rem;
  padding: 0;
  font-size: 0.88rem;
  line-height: 1.5;
  color: var(--global-text-color-light, #666);
}

/* 注释 */
.activity-note {
  margin-top: 0.7rem;
  font-size: 0.88rem;
  color: var(--global-text-color-light, #666);
  font-style: italic;
}

/* 链接 */
.activity-card a {
  color: var(--global-link-color, #2c6e91);
  text-decoration: none;
}

.activity-card a:hover {
  text-decoration: underline;
}

/* 响应式 */
@media (max-width: 700px) {
  .activity-flex {
    flex-direction: column;
  }

  .activity-image-box {
    width: 100%;
    max-width: 260px;
  }
}

/* 深色模式 */
html[data-theme="dark"] .activity-card {
  background: #1e1e1e;
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: 0 6px 18px rgba(0,0,0,0.35);
}

html[data-theme="dark"] .activity-title {
  color: #f1f1f1;
}

html[data-theme="dark"] .activity-subtitle,
html[data-theme="dark"] .activity-list {
  color: #e2e2e2;
}

html[data-theme="dark"] .activity-meta,
html[data-theme="dark"] .activity-date-list,
html[data-theme="dark"] .activity-note {
  color: #c8c8c8;
}

html[data-theme="dark"] .activity-card a {
  color: #7fc7ff;
}

html[data-theme="dark"] .activity-image-box {
  border: 1px solid rgba(255,255,255,0.1);
}
</style>

## Editorial & Review

<div class="activity-card">

  <div class="activity-title">Reviewer for peer-reviewed journals</div>

  <ul class="activity-list">
    <li><a href="https://www.sciencedirect.com/journal/progress-in-oceanography"><i>Progress in Oceanography</i></a></li>
    <li><a href="https://bg.copernicus.org/"><i>Biogeosciences</i></a></li>
  </ul>

  <br>

  <div class="activity-title">Guest Editor</div>

  <div class="activity-subtitle">
    <a href="https://www.mdpi.com/journal/remotesensing"><i>Remote Sensing</i></a>
  </div>

  <div class="activity-meta">
    Special Issue:
    <a href="https://www.mdpi.com/journal/remotesensing/special_issues/QRR07AH1D1">
      Advances in Machine Learning and Multi-Source Remote Sensing for Monitoring Marine Aquatic Environments
    </a>
  </div>

</div>

## Scientific Cruises

<div class="activity-card">

  <div class="activity-title">ITINERIS’ EYES Cruise (ITINERIS Project)</div>

  <div class="activity-meta">
    Mediterranean Sea · 24–29 Jul 2025 ·
    <a href="https://www.cnr.it/it/gaia-blu-speciale-campagna-itineris-eyes-2025">Project Link</a>
  </div>

  <ul class="activity-list">
    <li>Conducted in situ bio-optical measurements including HPLC pigments, CDOM absorption, and particle absorption</li>
    <li>Performed onboard data processing, quality control, and preliminary analysis of optical datasets</li>
  </ul>

</div>

<div class="activity-card">

  <div class="activity-flex">

    <div class="activity-flex-text">

      <div class="activity-title">National Natural Science Foundation of China Cruises</div>

      <div class="activity-meta">
        East China Sea · Bohai Sea · Yellow Sea · Yangtze River Estuary
      </div>

      <ul class="activity-date-list">
        <li>13–29 May 2019 (East China Sea)</li>
        <li>23 Jul–5 Aug 2019 (the Bohai Sea & the Yellow Sea)</li>
        <li>27 May–11 Jun 2020 (the Bohai Sea & the Yellow Sea)</li>
        <li>29 Jun–6 Jul 2020 (the Yangtze River Estuary & the East China Sea)</li>
      </ul>

      <ul class="activity-list">
        <li>Performed water sampling and onboard processing for HPLC pigments, TSM, and POC</li>
        <li>Operated optical instrumentation including absorption, scattering, backscattering, and beam attenuation</li>
        <li>Processed and quality-controlled datasets including remote sensing reflectance and IOPs</li>
        <li>Analysed particle characteristics including size distribution and refractive index</li>
        <li>Contributed to cross-cruise data standardization</li>
      </ul>

    </div>

    <div class="activity-image-box">
      <img src="/images/航次.jpg" alt="Scientific cruises">
    </div>

  </div>

</div>

## Data Analysis & Technical Experience

<div class="activity-card">

  <div class="activity-title">Data Analysis Internship</div>

  <div class="activity-subtitle">North China Sea Marine Forecasting Center</div>

  <div class="activity-meta">
    Qingdao, China · 1 Nov–12 Dec 2017
  </div>

  <ul class="activity-list">
    <li>Collected and organized global marine and atmospheric remote sensing datasets</li>
    <li>Integrated multi-source satellite observations (ocean colour, wind, salinity, SSH, temperature)</li>
    <li>Performed preprocessing and statistical analysis</li>
    <li>Supported data harmonization for forecasting applications</li>
  </ul>

  <div class="activity-note">
    Now renamed as North Sea Forecasting and Disaster Mitigation Centre (MNR)
  </div>

</div>

## Scientific Coordination & Service

<div class="activity-card">

  <div class="activity-title">National Partnership Coordinator</div>

  <div class="activity-subtitle">
    <a href="https://www.ecopdecade.org/">ECOP Programme (UN Ocean Decade)</a> – China Node
  </div>

  <div class="activity-meta">
    Online · 26 Jun–9 Oct 2023
  </div>

  <ul class="activity-list">
    <li>Developed national and international collaboration opportunities</li>
    <li>Supported outreach and dissemination activities</li>
  </ul>

</div>
