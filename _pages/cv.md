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
  padding: 1.2rem 1.4rem;
  margin: 1rem 0;
  border-radius: 16px;
  border: 1px solid rgba(120,120,120,0.18);
  background: var(--global-bg-color, #ffffff);
  box-shadow: 0 4px 14px rgba(0,0,0,0.06);
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.cv-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.10);
}

.cv-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--global-text-color, #222);
}

.cv-subtitle {
  font-size: 0.95rem;
  color: var(--global-text-color-light, #555);
  margin-top: 2px;
}

.cv-meta {
  font-size: 0.85rem;
  color: var(--global-text-color-light, #777);
  margin-top: 4px;
}

.cv-desc {
  font-size: 0.9rem;
  line-height: 1.6;
  color: var(--global-text-color, #333);
  margin-top: 0.75rem;
}

.cv-list {
  margin: 0.5rem 0 0 1.1rem;
  padding: 0;
  font-size: 0.9rem;
  line-height: 1.55;
}

.cv-list li {
  margin-bottom: 5px;
}

.cv-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  align-items: stretch;
}

.cv-grid-3 .cv-card {
  margin: 0;
  height: 100%;
}

@media (max-width: 900px) {
  .cv-grid-3 {
    grid-template-columns: 1fr;
  }
}

html[data-theme="dark"] .cv-card {
  background: #1e1e1e;
  border: 1px solid rgba(255,255,255,0.10);
  box-shadow: 0 4px 14px rgba(0,0,0,0.35);
}

html[data-theme="dark"] .cv-title {
  color: #f1f1f1;
}

html[data-theme="dark"] .cv-subtitle {
  color: #cfcfcf;
}

html[data-theme="dark"] .cv-meta {
  color: #aaaaaa;
}

html[data-theme="dark"] .cv-desc,
html[data-theme="dark"] .cv-list {
  color: #e2e2e2;
}
</style>

## Work Experience

<div class="cv-card">
  <div class="cv-title">Postdoctoral Researcher</div>
  <div class="cv-subtitle">National Research Council of Italy (CNR), Institute of Marine Sciences (ISMAR), Rome, Italy</div>
  <div class="cv-meta">Dec 2024 – Present · Supervisor: <a href="https://www.researchgate.net/profile/Emanuele-Organelli">Dr. Emanuele Organelli</a></div>
  <ul class="cv-list">
    <li>Investigation of ocean carbon cycling processes, including biological and microbial carbon pumps, by combining BGC-Argo observations, ocean colour satellite observations, and reconstruction outputs.</li>
    <li>Implemented a MATLAB-based processing pipeline for BGC-Argo data, integrating data processing, quality control (QC), and analysis workflows.</li>
    <li>Bio-optical and biogeochemical data processing and dataset establishment from BGC-Argo profiles.</li>
  </ul>
</div>

## Education

<div class="cv-card">
  <div class="cv-title">Doctor of Science in Physical Oceanography</div>
  <div class="cv-subtitle">East China Normal University, State Key Laboratory of Estuarine and Coastal Research (SKLEC), Shanghai, China</div>
  <div class="cv-meta">Sep 2018 – Jun 2024 · GPA: 3.46/4 · Supervisor: <a href="https://www.researchgate.net/profile/Fang-Shen-6">Prof. Fang Shen</a></div>
  <div class="cv-desc">
    I explored the inherent optical properties of marine particle compositions. I designed and conducted laboratory experiments to quantify the refractive indices of mineral particles, detritus, and different phytoplankton groups. I then investigated the contributions of phytoplankton and organic detritus to particulate organic carbon in optically complex estuarine, coastal, and shelf seas of China. I also analysed changes in particle types under atmospheric deposition and the associated phytoplankton responses. I developed MATLAB-based workflows for analysing satellite and float datasets, and implemented C++ simulations of particle backscattering processes. During this period, I also served as the administrator of the optical and phytoplankton laboratory.
  </div>
</div>

<div class="cv-card">
  <div class="cv-title">Visiting PhD (China Scholarship Council)</div>
  <div class="cv-subtitle">National Research Council of Italy (CNR), Institute of Marine Sciences (ISMAR), Rome, Italy</div>
  <div class="cv-meta">Oct 2022 – Oct 2023 · Co-supervisor: <a href="https://www.researchgate.net/profile/Emanuele-Organelli">Dr. Emanuele Organelli</a></div>
  <div class="cv-desc">
    The primary focus was on analysing the inherent optical properties of particles and conducting scattering simulations in the estuarine, coastal, and shelf seas of China. In addition, based on BGC-Argo data, I analysed the ecological impact of marine heatwaves on the upper waters of the north-western Mediterranean Sea within the CAREHeat Project.
  </div>
</div>

<div class="cv-card">
  <div class="cv-title">Bachelor of Science in Marine Technology</div>
  <div class="cv-subtitle">Ocean University of China, College of Information Science and Engineering, Qingdao, China</div>
  <div class="cv-meta">Sep 2014 – Jun 2018 · GPA: 3.55/4 · Supervisors: 
  <a href="https://www.researchgate.net/profile/Shuguo-Chen">Prof. Shuguo Chen</a> and 
  <a href="https://www.researchgate.net/profile/Chen-Ge-5">Prof. Ge Chen</a></div>
  <div class="cv-desc">
    My work utilized multi-source remote sensing data to investigate the causal and time-lag relationships between East Asian dust storm deposition and phytoplankton biomass in the East China Sea. I developed programming skills in C, C++, Python, MATLAB, R, and Assembly, and ultimately applied MATLAB as the primary tool for data analysis and implementation of this study.
  </div>
</div>

## Awards

<div class="cv-card">
<ul class="cv-list">
  <li>China Scholarship Council (CSC) Scholarship, Grant No. 202206140082, €16,200 per year, 2022 to 2023</li>
  <li>Outstanding Student Award, East China Normal University, 2021 to 2022</li>
  <li>Outstanding Undergraduate Dissertation Award, Ocean University of China, 2018</li>
  <li>Outstanding Student Award, Ocean University of China, 2016 to 2017</li>
  <li>Scholarship for Excellence in Academic Work, Ocean University of China, 2014 to 2017</li>
  <li>Scholarship for Participation in Social Activities, Ocean University of China, 2016 to 2017</li>
</ul>
</div>

## Skills

<div class="cv-grid-3">

<div class="cv-card">
  <div class="cv-title">Languages</div>
  <ul class="cv-list">
    <li>Chinese, Mandarin <small>native</small></li>
    <li>English <small>proficient</small></li>
    <li>Italian <small>conversational</small></li>
    <li>Japanese <small>conversational</small></li>
  </ul>
</div>

<div class="cv-card">
  <div class="cv-title">Programming</div>
  <ul class="cv-list">
    <li>MATLAB <small>advanced</small></li>
    <li>Python / R <small>intermediate</small></li>
    <li>C / C++ / Assembly <small>basic</small></li>
    <li>ENVI, SNAP, SeaDAS</li>
    <li>Adobe Photoshop, Microsoft Office</li>
  </ul>
</div>

<div class="cv-card">
  <div class="cv-title">Scientific Instruments / Measurements</div>
  <ul class="cv-list">
    <li>LISST-200X, Sequoia Scientific</li>
    <li>HyperSAS, Sea-Bird Scientific</li>
    <li>AC-S / ECO-BB9 / ECO-VSF, WET Labs</li>
    <li>Spectrophotometer, PerkinElmer</li>
    <li>Mastersizer, Malvern</li>
  </ul>
</div>

</div>

## Certifications

<div class="cv-card">
  <div class="cv-title">STCW Certifications</div>
  <div class="cv-subtitle">Tecno Italian Safety and Survival Training S.r.l, Italy</div>
  <div class="cv-meta">Issued: Mar 2025</div>
  <ul class="cv-list">
    <li>Personal Survival Techniques</li>
    <li>Fire Prevention and Fire Fighting</li>
    <li>Elementary First Aid</li>
    <li>Personal Safety and Social Responsibilities</li>
  </ul>
</div>
