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
  });
})();
