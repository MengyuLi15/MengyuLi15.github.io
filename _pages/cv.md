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

/* 🔥 1.8:1 logo */
.cv-logo-box {
  flex: 0 0 150px;
  aspect-ratio: 1.8 / 1;
  background: #ffffff;
  border-radius: 10px;
  border: 1px solid rgba(120,120,120,0.12);
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

/* 层级更清晰 */
.cv-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--global-text-color, #222);
}

.cv-line {
  font-size: 0.92rem;
  color: var(--global-text-color-light, #555);
  margin-top: 2px;
}

.cv-meta {
  font-size: 0.85rem;
  color: var(--global-text-color-light, #777);
  margin-top: 3px;
}

/* 内容对齐 */
.cv-content {
  padding-left: 168px;
  margin-top: 0.6rem;
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

/* Skills */
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

html[data-theme="dark"] .cv-line,
html[data-theme="dark"] .cv-meta,
html[data-theme="dark"] .cv-desc,
html[data-theme="dark"] .cv-list {
  color: #dcdcdc;
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
      <div class="cv-line">Institute of Marine Sciences (ISMAR)</div>
      <div class="cv-line">National Research Council of Italy (CNR)</div>
      <div class="cv-line">Rome, Italy</div>
      <div class="cv-meta">Dec 2024 – Present · Supervisor: <a href="https://www.researchgate.net/profile/Emanuele-Organelli">Dr. Emanuele Organelli</a></div>
    </div>
  </div>

  <div class="cv-content">
    <ul class="cv-list">
      <li>Investigation of ocean carbon cycling processes (biological and microbial carbon pumps) combining BGC-Argo, ocean colour satellite observations and reconstruction outputs</li>
      <li>Implemented a MATLAB-based processing pipeline for BGC-Argo data, integrating data processing, quality control (QC), and analysis workflows</li>
      <li>Bio-optical and biogeochemical data processes and dataset establishment from BGC-Argo profiles</li>
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
      <div class="cv-line">State Key Laboratory of Estuarine and Coastal Research (SKLEC)</div>
      <div class="cv-line">East China Normal University</div>
      <div class="cv-line">Shanghai, China</div>
      <div class="cv-meta">
        Sep 2018 – Jun 2024 · GPA: 3.46/4 · 
        Supervisor: <a href="https://www.researchgate.net/profile/Fang-Shen-6">Prof. Fang Shen</a>
      </div>
    </div>
  </div>

  <div class="cv-content">
    <p class="cv-desc">
      I explored the inherent optical properties of marine particle compositions. I designed and conducted laboratory experiments to quantify the refractive index of mineral particles, detritus, and different phytoplankton. Then I investigated the contributions of phytoplankton and organic detritus to particulate organic carbon in optically complex estuarine-coastal-shelf seas of China. I also analysed the changes in particle types under atmospheric deposition and the response of phytoplankton. I developed MATLAB-based workflows for analysing satellite and float datasets, and implemented C++ simulations of particle backscattering processes. In the meantime, I served as the optical and phytoplankton laboratory administrator.
    </p>
  </div>
</div>

<div class="cv-card">
  <div class="cv-header">
    <div class="cv-logo-box">
      <img src="/images/School_Mar_Geo_logoISMAR.jpg">
    </div>

    <div class="cv-header-text">
      <div class="cv-title">Visiting PhD (China Scholarship Council)</div>
      <div class="cv-line">Institute of Marine Sciences (ISMAR)</div>
      <div class="cv-line">National Research Council of Italy (CNR)</div>
      <div class="cv-line">Rome, Italy</div>
      <div class="cv-meta">
        Oct 2022 – Oct 2023 · 
        Co-supervisor: <a href="https://www.researchgate.net/profile/Emanuele-Organelli">Dr. Emanuele Organelli</a>
      </div>
    </div>
  </div>

  <div class="cv-content">
    <p class="cv-desc">
      The primary focus was on analyzing the inherent optical properties of particles and conducting scattering simulations in estuarine-coastal-shelf seas of China. Additionally, based on BGC-Argo data, the ecological impact of marine heatwaves (CAREHeat Project) on the upper waters of the north-western Mediterranean Sea was analysed.
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
      <div class="cv-line">College of Information Science and Engineering</div>
      <div class="cv-line">Ocean University of China</div>
      <div class="cv-line">Qingdao, China</div>
      <div class="cv-meta">
        Sep 2014 – Jun 2018 · GPA: 3.55/4 · 
        Supervisors: 
        <a href="https://www.researchgate.net/profile/Shuguo-Chen">Prof. Shuguo Chen</a>, 
        <a href="https://www.researchgate.net/profile/Chen-Ge-5">Prof. Ge Chen</a>
      </div>
    </div>
  </div>

  <div class="cv-content">
    <p class="cv-desc">
      My work utilizes multi-source remote sensing data to investigate the causal and time-lag relationships between East Asian dust storm deposition and phytoplankton biomass in the East China Sea. I developed programming skills in C, C++, Python, MATLAB, R, and Assembly, and ultimately applied MATLAB as the primary tool for data analysis and implementation of this study.
    </p>
  </div>
</div>

## Awards

<div class="cv-card">

  <ul class="cv-list">
    <li><strong>China Scholarship Council (CSC) Scholarship</strong> (Grant No. 202206140082), €16,200 per year (2022–2023)</li>
    <li>Outstanding Student Award, East China Normal University (2021–2022)</li>
    <li>Outstanding Undergraduate Dissertation Award, Ocean University of China (2018)</li>
    <li>Outstanding Student Award, Ocean University of China (2016–2017)</li>
    <li>Scholarship for Excellence in Academic Work, Ocean University of China (2014–2017)</li>
    <li>Scholarship for Participation in Social Activities, Ocean University of China (2016–2017)</li>
  </ul>

</div>

## Skills

<div class="cv-grid-3">

<div class="cv-card">
<div class="cv-title">Languages</div>
<ul class="cv-list">
<li>Chinese (Mandarin) <small>native</small></li>
<li>English <small>proficient</small></li>
<li>Italian <small>conversational</small></li>
<li>Japanese <small>conversational</small></li>
</ul>
</div>

<div class="cv-card">
<div class="cv-title">Programming & Software</div>
<ul class="cv-list">
<li>MATLAB <small>advanced</small></li>
<li>Python / R <small>intermediate</small></li>
<li>C / C++ / Assembly <small>basic</small></li>
</ul>
<p class="cv-desc"><small>Software: ENVI, SNAP, SeaDAS, Adobe Photoshop, Microsoft Office</small></p>
</div>

<div class="cv-card">
<div class="cv-title">Scientific Instruments</div>
<ul class="cv-list">
<li>LISST-200X (Sequoia Scientific)</li>
<li>HyperSAS (Sea-Bird Scientific)</li>
<li>AC-S / ECO-BB9 / ECO-VSF (WET Labs)</li>
<li>Spectrophotometer (PerkinElmer)</li>
<li>Mastersizer (Malvern)</li>
</ul>
</div>

</div>

## Certifications

<div class="cv-card">
<div class="cv-title">STCW Certifications</div>
<div class="cv-line">Tecno Italian Safety and Survival Training S.r.l, Italy</div>
<div class="cv-meta">Issued: Mar 2025</div>

<ul class="cv-list">
<li>Personal Survival Techniques</li>
<li>Fire Prevention and Fire Fighting</li>
<li>Elementary First Aid</li>
<li>Personal Safety and Social Responsibilities</li>
</ul>
</div>
