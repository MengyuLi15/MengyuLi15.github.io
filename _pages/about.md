---
permalink: /
title: "Mengyu Li @ CNR-ISMAR"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>


.hero-card {
  padding: 2rem 2.1rem;
  margin: 1rem 0 2rem 0;
  border-radius: 22px;

  background: rgba(255, 255, 255, 0.55);   /* 👈 从白改半透明 */
  backdrop-filter: blur(18px) saturate(130%);
  -webkit-backdrop-filter: blur(18px) saturate(130%);

  border: 1px solid rgba(255,255,255,0.4);
  box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}
  
.hero-dynamic {
  background: transparent !important;
}

.hero-card h2 {
  margin-top: 0;
  margin-bottom: 0.6rem;
  font-size: 2rem;
  line-height: 1.2;
  color: var(--global-text-color, #222);
}

.hero-dynamic {
  min-height: 2rem;
  margin-bottom: 1rem;
  font-size: 1.12rem;
  font-weight: 600;
  color: #2c6e91;
}

.hero-dynamic span {
  border-right: 2px solid #2c6e91;
  padding-right: 3px;
  animation: blinkCursor 0.8s infinite;
}

.hero-card p {
  margin-bottom: 0.8rem;
  font-size: 1.02rem;
  line-height: 1.75;
  color: var(--global-text-color, #333);
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 1rem;
  margin: 1.2rem 0 2rem 0;
}

.info-card {
  padding: 1.25rem 1.3rem;
  border-radius: 18px;
  border: 1px solid rgba(120,120,120,0.18);
  background: var(--global-bg-color, #ffffff);
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
  transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
  animation: fadeUp 0.85s ease-out;
}

.info-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0,0,0,0.10);
  border-color: rgba(44,110,145,0.30);
}

.info-card h3,
.address-card h3 {
  margin-top: 0;
  margin-bottom: 0.65rem;
  font-size: 1.08rem;
  line-height: 1.35;
  color: var(--global-text-color, #222);
}

.info-card p {
  margin-bottom: 0;
  font-size: 0.95rem;
  line-height: 1.65;
  color: var(--global-text-color, #333);
}

.topic-list {
  padding: 1.4rem 1.6rem;
  margin: 1rem 0 2rem 0;
  border-radius: 18px;
  border: 1px solid rgba(120,120,120,0.18);
  background: var(--global-bg-color, #ffffff);
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

.topic-list ul {
  margin-bottom: 0;
  font-size: 0.95rem;
  line-height: 1.65;
}

.pub-box {
  padding: 1.2rem 1.4rem;
  margin-top: 1rem;
  border-radius: 16px;
  border: 1px solid rgba(120,120,120,0.18);
  border-left: 4px solid #2c6e91;
  background: var(--global-bg-color, #ffffff);
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
  font-size: 0.95rem;
  line-height: 1.6;
}

.address-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem;
  align-items: stretch;
  margin-top: 1rem;
}

.address-card {
  flex: 1 1 280px;
  min-width: 260px;
  padding: 1.4rem 1.5rem;
  border-radius: 18px;
  border: 1px solid rgba(120,120,120,0.18);
  background: var(--global-bg-color, #ffffff);
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

.address-main {
  margin: 0 0 0.8rem 0;
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--global-text-color, #333);
}

.address-meta {
  margin: 0 0 0.7rem 0;
  font-size: 0.92rem;
  line-height: 1.55;
  color: var(--global-text-color-light, #666);
}

.map-card {
  flex: 1.25 1 360px;
  min-width: 280px;
  padding: 0.8rem;
  border-radius: 18px;
  border: 1px solid rgba(120,120,120,0.18);
  background: var(--global-bg-color, #ffffff);
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

.map-card iframe {
  border: 0;
  border-radius: 12px;
}

.home-card a,
.info-card a,
.pub-box a,
.address-card a {
  color: var(--global-link-color, #2c6e91);
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(14px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes blinkCursor {
  0%, 45% {
    border-color: #2c6e91;
  }
  46%, 100% {
    border-color: transparent;
  }
}

@media (max-width: 768px) {
  .hero-card {
    padding: 1.5rem 1.3rem;
    border-radius: 18px;
  }

  .hero-card h2 {
    font-size: 1.6rem;
  }

  .hero-dynamic {
    font-size: 1rem;
  }

  .card-grid {
    grid-template-columns: 1fr;
  }
}

html[data-theme="dark"] .hero-card,
html[data-theme="dark"] .info-card,
html[data-theme="dark"] .topic-list,
html[data-theme="dark"] .pub-box,
html[data-theme="dark"] .address-card,
html[data-theme="dark"] .map-card {
  background: #1e1e1e;
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: 0 6px 18px rgba(0,0,0,0.35);
}

html[data-theme="dark"] .hero-card h2,
html[data-theme="dark"] .info-card h3,
html[data-theme="dark"] .address-card h3 {
  color: #f1f1f1;
}

html[data-theme="dark"] .hero-dynamic {
  color: #7fc7ff;
}

html[data-theme="dark"] .hero-dynamic span {
  border-right-color: #7fc7ff;
}

html[data-theme="dark"] .hero-card p,
html[data-theme="dark"] .info-card p,
html[data-theme="dark"] .topic-list,
html[data-theme="dark"] .pub-box,
html[data-theme="dark"] .address-main {
  color: #e2e2e2;
}

html[data-theme="dark"] .address-meta {
  color: #c8c8c8;
}

html[data-theme="dark"] a {
  color: #7fc7ff;
}
</style>

<div class="hero-card">
  <h2>Hi, I’m Mengyu Li</h2>

  <div class="hero-dynamic">
    <span id="typed-text"></span>
  </div>

  <p>
    I am a Postdoctoral Researcher at CNR-ISMAR in Rome, working on marine bio-optics,
    BGC-Argo observations, and ocean biogeochemistry.
  </p>

  <p>
    My research focuses on ocean carbon cycling and bio-optical processes by integrating
    in situ observations, satellite remote sensing, and model outputs to better understand
    marine ecosystems under climate variability.
  </p>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const phrases = [
    "Marine bio-optics",
    "BGC-Argo observations",
    "Ocean colour remote sensing",
    "Ocean carbon cycling",
    "Biological and microbial carbon pumps"
  ];

  const target = document.getElementById("typed-text");
  let phraseIndex = 0;
  let charIndex = 0;
  let deleting = false;

  function typeLoop() {
    const currentPhrase = phrases[phraseIndex];

    if (!deleting) {
      target.textContent = currentPhrase.substring(0, charIndex + 1);
      charIndex++;

      if (charIndex === currentPhrase.length) {
        deleting = true;
        setTimeout(typeLoop, 1300);
        return;
      }
    } else {
      target.textContent = currentPhrase.substring(0, charIndex - 1);
      charIndex--;

      if (charIndex === 0) {
        deleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
      }
    }

    setTimeout(typeLoop, deleting ? 45 : 80);
  }

  typeLoop();
});
</script>

## Research Focus

<div class="card-grid">

  <div class="info-card">
    <h3>Marine Bio-optics</h3>
    <p>
      Quantifying relationships between chlorophyll, light attenuation, and optical depth
      metrics across different water types and oceanic regimes.
    </p>
  </div>

  <div class="info-card">
    <h3>BGC-Argo Observations</h3>
    <p>
      Using multi-sensor float observations to resolve the vertical structure and variability
      of bio-optical and biogeochemical properties.
    </p>
  </div>

  <div class="info-card">
    <h3>Remote Sensing</h3>
    <p>
      Combining satellite ocean-colour products with in situ observations to investigate
      phytoplankton dynamics, particle properties, and carbon-related processes.
    </p>
  </div>

  <div class="info-card">
    <h3>Ocean Carbon Cycling</h3>
    <p>
      Investigating particulate export and microbial carbon processing in the ocean,
      with a focus on carbon sequestration in oligotrophic systems.
    </p>
  </div>

</div>

## Technical Expertise

<div class="card-grid">

  <div class="info-card">
    <h3>Data Processing</h3>
    <p>
      MATLAB-based workflows for BGC-Argo processing, radiometric quality control,
      and multi-platform data integration.
    </p>
  </div>

  <div class="info-card">
    <h3>Optical Modelling</h3>
    <p>
      Development and evaluation of empirical and semi-analytical models for Kd,
      Zeu, and other bio-optical relationships.
    </p>
  </div>

  <div class="info-card">
    <h3>Field Measurements</h3>
    <p>
      Experience with HPLC pigments, CDOM absorption, particle absorption,
      and optical measurements from research cruises.
    </p>
  </div>

  <div class="info-card">
    <h3>Multi-platform Integration</h3>
    <p>
      Integration of floats, satellite observations, and model outputs for
      large-scale analysis of marine biogeochemical processes.
    </p>
  </div>

</div>

## Selected Research Topics

<div class="topic-list">
  <ul>
    <li>Relationships between chlorophyll and light attenuation</li>
    <li>Evaluation and refitting of bio-optical models</li>
    <li>Integration of BGC-Argo, satellite, and model datasets</li>
    <li>Carbon export in oligotrophic oceans</li>
    <li>Marine heatwaves and phytoplankton dynamics</li>
  </ul>
</div>

## Publications

<div class="pub-box">
  A full list of publications can be found on the <a href="/publications/">Publications</a> page.
</div>

## Address

<div class="address-wrap">

  <div class="address-card">
    <h3>Office</h3>

    <p class="address-main">
      <strong>Istituto di Scienze Marine – Consiglio Nazionale delle Ricerche</strong><br>
      Area della Ricerca di Roma 2 – Tor Vergata<br>
      Via del Fosso del Cavaliere 100<br>
      00133 Rome, Italy
    </p>

    <p class="address-meta">
      <strong>Affiliation</strong><br>
      CNR-ISMAR, Rome
    </p>

    <p class="address-meta" style="margin-bottom:0;">
      <a href="https://www.google.com/maps?q=Via+del+Fosso+del+Cavaliere+100+Roma" target="_blank">
        Open in Google Maps →
      </a>
    </p>
  </div>

  <div class="map-card">
    <iframe
      src="https://www.google.com/maps?q=Via+del+Fosso+del+Cavaliere+100+Roma&output=embed"
      width="100%"
      height="320"
      loading="lazy"
      referrerpolicy="no-referrer-when-downgrade">
    </iframe>
  </div>

</div>
