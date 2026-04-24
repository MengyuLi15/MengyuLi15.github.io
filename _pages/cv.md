---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<style>
.cv-card {
  padding: 1.5rem 1.6rem;
  margin: 1.2rem 0;
  border-radius: 18px;
  border: 1px solid rgba(120,120,120,0.18);
  background: var(--global-bg-color, #ffffff);
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

.cv-header {
  display: flex;
  align-items: center;
  gap: 1.2rem;
}

/* 🔥 更大的2:1 logo */
.cv-logo-box {
  flex: 0 0 150px;
  aspect-ratio: 2 / 1;
  background: #ffffff;
  border-radius: 10px;
  border: 1px solid rgba(120,120,120,0.15);
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cv-logo-box img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.cv-header-text {
  flex: 1;
}

.cv-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--global-text-color, #222);
}

.cv-subtitle {
  font-size: 0.96rem;
  color: #2c6e91;
  margin-top: 3px;
}

.cv-meta {
  font-size: 0.85rem;
  color: var(--global-text-color-light, #777);
  margin-top: 3px;
}

/* 分割线 */
.cv-divider {
  margin: 1rem 0 0.8rem 0;
  height: 1px;
  background: rgba(120,120,120,0.15);
}

/* 内容对齐 */
.cv-content {
  padding-left: 168px; /* = logo + gap */
}

.cv-desc {
  font-size: 0.92rem;
  line-height: 1.65;
}

.cv-list {
  margin: 0;
  padding-left: 1.1rem;
  font-size: 0.92rem;
  line-height: 1.6;
}

.cv-list li {
  margin-bottom: 6px;
}

/* Skills grid */
.cv-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.cv-grid-3 .cv-card {
  margin: 0;
}

/* Responsive */
@media (max-width: 900px) {
  .cv-grid-3 {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 700px) {
  .cv-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .cv-logo-box {
    width: 160px;
  }

  .cv-content {
    padding-left: 0;
  }
}

/* Dark mode */
html[data-theme="dark"] .cv-card {
  background: #1e1e1e;
  border: 1px solid rgba(255,255,255,0.08);
}

html[data-theme="dark"] .cv-title {
  color: #f1f1f1;
}

html[data-theme="dark"] .cv-subtitle {
  color: #5fa8d3;
}

html[data-theme="dark"] .cv-meta {
  color: #aaaaaa;
}

html[data-theme="dark"] .cv-divider {
  background: rgba(255,255,255,0.1);
}

html[data-theme="dark"] .cv-desc,
html[data-theme="dark"] .cv-list {
  color: #e0e0e0;
}
</style>

## Work Experience

<div class="cv-card">
  <div class="cv-header">
    <div class="cv-logo-box">
      <img src="/images/School_Mar_Geo_logoISMAR.jpg">
    </div>
    <div class="cv-header-text">
      <div class="cv-title">Postdoctoral Researcher</div>
      <div class="cv-subtitle">CNR – Institute of Marine Sciences (ISMAR), Rome, Italy</div>
      <div class="cv-meta">Dec 2024 – Present · Supervisor: <a href="https://www.researchgate.net/profile/Emanuele-Organelli">Dr. Emanuele Organelli</a></div>
    </div>
  </div>

  <div class="cv-divider"></div>

  <div class="cv-content">
    <ul class="cv-list">
      <li>Investigation of ocean carbon cycling processes combining BGC-Argo, satellite observations, and reconstruction outputs</li>
      <li>Developed MATLAB-based BGC-Argo processing pipeline (QC + analysis)</li>
      <li>Established bio-optical and biogeochemical datasets from BGC-Argo profiles</li>
    </ul>
  </div>
</div>

## Education

<div class="cv-card">
  <div class="cv-header">
    <div class="cv-logo-box">
      <img src="/images/ecnu.png">
    </div>
    <div class="cv-header-text">
      <div class="cv-title">Doctor of Science in Physical Oceanography</div>
      <div class="cv-subtitle">East China Normal University (SKLEC)</div>
      <div class="cv-meta">Sep 2018 – Jun 2024 · GPA: 3.46/4</div>
    </div>
  </div>

  <div class="cv-divider"></div>

  <div class="cv-content">
    <p class="cv-desc">
      I explored inherent optical properties of marine particles. Designed experiments to quantify refractive indices of minerals, detritus, and phytoplankton. Investigated contributions to particulate organic carbon in optically complex waters. Developed MATLAB workflows and C++ scattering simulations, and served as laboratory administrator.
    </p>
  </div>
</div>

<div class="cv-card">
  <div class="cv-header">
    <div class="cv-logo-box">
      <img src="/images/School_Mar_Geo_logoISMAR.jpg">
    </div>
    <div class="cv-header-text">
      <div class="cv-title">Visiting PhD (CSC)</div>
      <div class="cv-subtitle">CNR – ISMAR, Rome</div>
      <div class="cv-meta">Oct 2022 – Oct 2023</div>
    </div>
  </div>

  <div class="cv-divider"></div>

  <div class="cv-content">
    <p class="cv-desc">
      Analysed particle optical properties and scattering simulations. Investigated marine heatwave impacts in the north-western Mediterranean using BGC-Argo data.
    </p>
  </div>
</div>

<div class="cv-card">
  <div class="cv-header">
    <div class="cv-logo-box">
      <img src="/images/OUC.png">
    </div>
    <div class="cv-header-text">
      <div class="cv-title">Bachelor of Science in Marine Technology</div>
      <div class="cv-subtitle">Ocean University of China</div>
      <div class="cv-meta">Sep 2014 – Jun 2018 · GPA: 3.55/4</div>
    </div>
  </div>

  <div class="cv-divider"></div>

  <div class="cv-content">
    <p class="cv-desc">
      Investigated relationships between dust deposition and phytoplankton using multi-source remote sensing. Developed programming skills across multiple languages with MATLAB as the main tool.
    </p>
  </div>
</div>

## Skills

<div class="cv-grid-3">

<div class="cv-card">
<div class="cv-title">Languages</div>
<div class="cv-divider"></div>
<ul class="cv-list">
<li>Chinese (native)</li>
<li>English (proficient)</li>
<li>Italian (conversational)</li>
<li>Japanese (conversational)</li>
</ul>
</div>

<div class="cv-card">
<div class="cv-title">Programming</div>
<div class="cv-divider"></div>
<ul class="cv-list">
<li>MATLAB</li>
<li>Python / R</li>
<li>C / C++ / Assembly</li>
<li>ENVI, SNAP, SeaDAS</li>
</ul>
</div>

<div class="cv-card">
<div class="cv-title">Scientific Instruments</div>
<div class="cv-divider"></div>
<ul class="cv-list">
<li>LISST-200X</li>
<li>HyperSAS</li>
<li>AC-S / ECO-BB9</li>
<li>Spectrophotometer</li>
<li>Mastersizer</li>
</ul>
</div>

</div>
