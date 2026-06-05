(function () {
  var storageKey = "mengyu-paper-push-favorites-v1";
  var languageKey = "mengyu-paper-push-language-v2";

  function currentLanguage() {
    return localStorage.getItem(languageKey) || "en";
  }

  function applyLanguage(lang) {
    var selected = lang === "en" ? "en" : "zh";
    localStorage.setItem(languageKey, selected);
    document.documentElement.setAttribute("data-paper-push-lang", selected);
    document.querySelectorAll("[data-paper-push-lang-button]").forEach(function (button) {
      var active = button.dataset.paperPushLangButton === selected;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
    syncButtons();
    renderFavorites();
  }

  function readFavorites() {
    try {
      return JSON.parse(localStorage.getItem(storageKey) || "[]");
    } catch (error) {
      return [];
    }
  }

  function writeFavorites(items) {
    localStorage.setItem(storageKey, JSON.stringify(items));
  }

  function paperId(paper) {
    return (paper.doi || paper.title || "").toLowerCase().trim();
  }

  function buttonPaper(button) {
    var lang = currentLanguage();
    return {
      title: button.dataset.title || "",
      authors: button.dataset.authors || "",
      journal: button.dataset.journal || "",
      published: button.dataset.published || "",
      publishedMonth: button.dataset.publishedMonth || "",
      published_month: button.dataset.publishedMonth || "",
      doi: button.dataset.doi || "",
      url: button.dataset.url || "",
      issueDate: button.dataset.issueDate || "",
      summary: lang === "en" ? (button.dataset.summaryEn || button.dataset.summary || "") : (button.dataset.summaryZh || button.dataset.summary || ""),
      language: lang
    };
  }

  function setButtonState(button, active) {
    button.classList.toggle("is-favorite", active);
    button.setAttribute("aria-pressed", active ? "true" : "false");
    button.textContent = active ? "Saved" : "Save";
  }

  function syncButtons() {
    var favorites = readFavorites();
    var ids = favorites.map(paperId);
    document.querySelectorAll("[data-favorite-paper]").forEach(function (button) {
      setButtonState(button, ids.indexOf(paperId(buttonPaper(button))) !== -1);
    });
  }

  function escapeHtml(value) {
    var node = document.createElement("div");
    node.textContent = value || "";
    return node.innerHTML;
  }

  function escapeCsv(value) {
    return '"' + String(value || "").replace(/"/g, '""') + '"';
  }

  function exportCsv() {
    var favorites = readFavorites();
    var header = ["issue_date", "language", "title", "authors", "journal", "published", "published_month", "doi", "url", "summary"];
    var rows = favorites.map(function (paper) {
      return header.map(function (key) { return escapeCsv(paper[key]); }).join(",");
    });
    var csv = [header.join(",")].concat(rows).join("\n");
    var blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
    var url = URL.createObjectURL(blob);
    var link = document.createElement("a");
    link.href = url;
    link.download = "paper_push_favorites.csv";
    link.click();
    URL.revokeObjectURL(url);
  }

  function pointPath(points) {
    return points.map(function (point, index) {
      return (index === 0 ? "M" : "L") + point.x.toFixed(2) + " " + point.y.toFixed(2);
    }).join(" ");
  }

  function renderCumulativeChart() {
    var target = document.querySelector("[data-paper-push-cumulative-chart]");
    if (!target || target.dataset.rendered === "true") return;

    var data = Array.prototype.slice.call(target.querySelectorAll("[data-paper-push-cumulative-point]")).map(function (node) {
      return {
        date: node.dataset.date || "",
        time: node.dataset.time || node.dataset.date || "",
        papers: Number(node.dataset.papers || 0),
        cumulative: Number(node.dataset.cumulative || 0)
      };
    }).filter(function (point) {
      return point.date && Number.isFinite(point.cumulative);
    });

    if (!data.length) {
      target.innerHTML = '<p class="paper-push-empty">No paper-push records yet.</p>';
      target.dataset.rendered = "true";
      return;
    }

    var width = 860;
    var height = 320;
    var margin = { top: 24, right: 28, bottom: 46, left: 54 };
    var plotWidth = width - margin.left - margin.right;
    var plotHeight = height - margin.top - margin.bottom;
    var maxValue = Math.max.apply(null, data.map(function (point) { return point.cumulative; }));
    var yMax = Math.max(1, Math.ceil(maxValue * 1.12));

    var points = data.map(function (point, index) {
      var x = margin.left + (data.length === 1 ? plotWidth / 2 : (index / (data.length - 1)) * plotWidth);
      var y = margin.top + plotHeight - (point.cumulative / yMax) * plotHeight;
      return Object.assign({}, point, { x: x, y: y });
    });

    var areaPath = pointPath(points) + " L" + points[points.length - 1].x.toFixed(2) + " " + (margin.top + plotHeight) + " L" + points[0].x.toFixed(2) + " " + (margin.top + plotHeight) + " Z";
    var gridLines = [0, 0.25, 0.5, 0.75, 1].map(function (fraction) {
      var y = margin.top + plotHeight - fraction * plotHeight;
      var label = Math.round(yMax * fraction);
      return '<line class="paper-push-cumulative-grid" x1="' + margin.left + '" y1="' + y.toFixed(2) + '" x2="' + (width - margin.right) + '" y2="' + y.toFixed(2) + '"></line>' +
        '<text class="paper-push-cumulative-axis" x="' + (margin.left - 12) + '" y="' + (y + 4).toFixed(2) + '" text-anchor="end">' + label + "</text>";
    }).join("");

    var tickIndexes = data.length <= 6 ? data.map(function (_, index) { return index; }) : [0, Math.floor((data.length - 1) / 2), data.length - 1];
    var xLabels = tickIndexes.map(function (index) {
      var point = points[index];
      return '<text class="paper-push-cumulative-axis" x="' + point.x.toFixed(2) + '" y="' + (height - 14) + '" text-anchor="middle">' + escapeHtml(point.date) + "</text>";
    }).join("");

    var dots = points.map(function (point, index) {
      return '<circle class="paper-push-cumulative-hit" tabindex="0" role="button" aria-label="' + escapeHtml(point.time + ", " + point.cumulative + " cumulative papers") + '" data-chart-index="' + index + '" cx="' + point.x.toFixed(2) + '" cy="' + point.y.toFixed(2) + '" r="13"></circle>' +
        '<circle class="paper-push-cumulative-dot" cx="' + point.x.toFixed(2) + '" cy="' + point.y.toFixed(2) + '" r="4.5"></circle>';
    }).join("");

    target.innerHTML = [
      '<svg class="paper-push-cumulative-svg" viewBox="0 0 ' + width + " " + height + '" role="img" aria-label="Cumulative included papers over time">',
      gridLines,
      '<line class="paper-push-cumulative-grid" x1="' + margin.left + '" y1="' + margin.top + '" x2="' + margin.left + '" y2="' + (margin.top + plotHeight) + '"></line>',
      '<line class="paper-push-cumulative-grid" x1="' + margin.left + '" y1="' + (margin.top + plotHeight) + '" x2="' + (width - margin.right) + '" y2="' + (margin.top + plotHeight) + '"></line>',
      '<path class="paper-push-cumulative-area" d="' + areaPath + '"></path>',
      '<path class="paper-push-cumulative-line" d="' + pointPath(points) + '"></path>',
      dots,
      xLabels,
      '<text class="paper-push-cumulative-label" x="' + margin.left + '" y="16">Cumulative papers</text>',
      "</svg>",
      '<div class="paper-push-cumulative-tooltip" hidden></div>'
    ].join("");
    target.dataset.rendered = "true";

    var tooltip = target.querySelector(".paper-push-cumulative-tooltip");
    var hits = target.querySelectorAll(".paper-push-cumulative-hit");

    function showTooltip(index) {
      var point = points[index];
      if (!point || !tooltip) return;
      hits.forEach(function (hit) { hit.classList.toggle("is-active", Number(hit.dataset.chartIndex) === index); });
      tooltip.innerHTML = "<strong>" + escapeHtml(point.time) + "</strong>" +
        "<div>Cumulative papers: " + escapeHtml(point.cumulative) + "</div>" +
        "<div>Added in this update: " + escapeHtml(point.papers) + "</div>";
      tooltip.style.left = (point.x / width * 100) + "%";
      tooltip.style.top = (point.y / height * 100) + "%";
      tooltip.hidden = false;
    }

    function hideTooltip() {
      hits.forEach(function (hit) { hit.classList.remove("is-active"); });
      if (tooltip) tooltip.hidden = true;
    }

    hits.forEach(function (hit) {
      hit.addEventListener("mouseenter", function () { showTooltip(Number(hit.dataset.chartIndex)); });
      hit.addEventListener("focus", function () { showTooltip(Number(hit.dataset.chartIndex)); });
      hit.addEventListener("click", function () { showTooltip(Number(hit.dataset.chartIndex)); });
      hit.addEventListener("mouseleave", hideTooltip);
      hit.addEventListener("blur", hideTooltip);
    });
  }

  function renderFavorites() {
    var target = document.querySelector("[data-favorites-table]");
    if (!target) return;

    var queryInput = document.querySelector("[data-favorites-filter]");
    var query = queryInput ? queryInput.value.toLowerCase().trim() : "";
    var favorites = readFavorites().filter(function (paper) {
      var haystack = [paper.title, paper.authors, paper.journal, paper.doi, paper.summary].join(" ").toLowerCase();
      return !query || haystack.indexOf(query) !== -1;
    });

    if (!favorites.length) {
      target.innerHTML = '<p class="paper-push-empty">No saved papers yet.</p>';
      return;
    }

    var html = [
      '<table class="paper-push-favorites-table">',
      "<thead><tr><th>Title</th><th>Authors</th><th>Journal</th><th>Month</th><th>DOI</th><th></th></tr></thead><tbody>"
    ];
    favorites.forEach(function (paper) {
      html.push(
        "<tr>",
        '<td><a href="' + escapeHtml(paper.url) + '">' + escapeHtml(paper.title) + "</a></td>",
        "<td>" + escapeHtml(paper.authors) + "</td>",
        "<td>" + escapeHtml(paper.journal) + "</td>",
        "<td>" + escapeHtml(paper.publishedMonth || paper.published_month || paper.published) + "</td>",
        '<td><a href="https://doi.org/' + escapeHtml(paper.doi) + '">' + escapeHtml(paper.doi) + "</a></td>",
        '<td><button class="paper-push-button" data-remove-favorite="' + escapeHtml(paperId(paper)) + '">Remove</button></td>',
        "</tr>"
      );
    });
    html.push("</tbody></table>");
    target.innerHTML = html.join("");
  }

  document.addEventListener("click", function (event) {
    var button = event.target.closest("[data-favorite-paper]");
    if (button) {
      var paper = buttonPaper(button);
      var favorites = readFavorites();
      var id = paperId(paper);
      var index = favorites.map(paperId).indexOf(id);
      if (index === -1) {
        paper.savedAt = new Date().toISOString();
        favorites.push(paper);
      } else {
        favorites.splice(index, 1);
      }
      writeFavorites(favorites);
      syncButtons();
      renderFavorites();
      return;
    }

    var removeButton = event.target.closest("[data-remove-favorite]");
    if (removeButton) {
      var removeId = removeButton.dataset.removeFavorite;
      writeFavorites(readFavorites().filter(function (paper) { return paperId(paper) !== removeId; }));
      syncButtons();
      renderFavorites();
      return;
    }

    if (event.target.closest("[data-export-favorites]")) {
      exportCsv();
    }

    var languageButton = event.target.closest("[data-paper-push-lang-button]");
    if (languageButton) {
      applyLanguage(languageButton.dataset.paperPushLangButton);
    }
  });

  document.addEventListener("input", function (event) {
    if (event.target.matches("[data-favorites-filter]")) {
      renderFavorites();
    }
  });

  document.addEventListener("DOMContentLoaded", function () {
    applyLanguage(currentLanguage());
    syncButtons();
    renderFavorites();
    renderCumulativeChart();
  });
})();
