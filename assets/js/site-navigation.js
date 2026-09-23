/* Keep the background video in the same document while visiting site pages. */
(function () {
  "use strict";
  if (!window.fetch || !window.DOMParser || !document.getElementById("site-content")) return;

  var pending;
  var currentPage = location.pathname + location.search;
  var loadedScripts = new Set(Array.from(document.scripts, function (script) { return script.src; }));
  var metadata = 'meta[name="description"], meta[property^="og:"], meta[name^="twitter:"], link[rel="canonical"], script[type="application/ld+json"]';

  function cancelPending() {
    if (pending) pending.abort();
    pending = null;
    document.getElementById("site-content").removeAttribute("aria-busy");
  }

  function saveScroll() {
    history.replaceState(Object.assign({}, history.state, { siteScroll: [scrollX, scrollY] }), "");
  }
  saveScroll();
  history.scrollRestoration = "manual";
  window.addEventListener("pagehide", saveScroll);
  var scrollTimer;
  window.addEventListener("scroll", function () {
    clearTimeout(scrollTimer);
    scrollTimer = setTimeout(saveScroll, 100);
  }, { passive: true });

  function restoreScroll(url, position) {
    if (position) {
      window.scrollTo(position[0], position[1]);
    } else if (url.hash) {
      var target = document.getElementById(decodeURIComponent(url.hash.slice(1)));
      if (target) target.scrollIntoView();
      else window.scrollTo(0, 0);
    } else {
      window.scrollTo(0, 0);
    }
  }

  async function activateScripts(container) {
    for (var original of container.querySelectorAll("script")) {
      if (original.type && !["text/javascript", "application/javascript", "module"].includes(original.type)) continue;
      if (original.src && loadedScripts.has(original.src)) continue;
      var script = document.createElement("script");
      for (var attribute of original.attributes) script.setAttribute(attribute.name, attribute.value);
      script.textContent = original.textContent;
      var ready = script.src ? new Promise(function (resolve, reject) {
        script.onload = resolve;
        script.onerror = reject;
      }) : Promise.resolve();
      original.replaceWith(script);
      await ready;
      if (script.src) loadedScripts.add(script.src);
    }
  }

  function refreshPage() {
    // The masthead and its existing responsive-menu handlers stay mounted.
    document.querySelectorAll(".masthead__menu-item").forEach(function (item) {
      var link = item.querySelector("a");
      if (!link) return;
      var path = new URL(link.href).pathname;
      item.classList.toggle("selected", path === "/" ? location.pathname === "/" : location.pathname.startsWith(path));
    });
    document.querySelectorAll("#site-content .author__urls-wrapper button").forEach(function (button) {
      button.addEventListener("click", function () {
        if (window.jQuery) {
          window.jQuery(".author__urls").fadeToggle("fast");
          button.classList.toggle("open");
        }
      });
    });
    if (window.fitvids) window.fitvids();
    window.dispatchEvent(new Event("resize"));
    document.dispatchEvent(new Event("site:load"));
    if (window.MathJax && window.MathJax.typesetPromise) window.MathJax.typesetPromise().catch(function () {});
  }

  async function visit(url, fromHistory, position) {
    if (pending) pending.abort();
    var controller = new AbortController();
    pending = controller;
    var timeout = setTimeout(function () { controller.abort(); }, 15000);
    var container = document.getElementById("site-content");
    container.setAttribute("aria-busy", "true");
    try {
      var response = await fetch(url.href, { signal: controller.signal, headers: { Accept: "text/html" } });
      if (!response.ok || !response.headers.get("content-type").includes("text/html")) throw new Error("Not a site page");
      var page = new DOMParser().parseFromString(await response.text(), "text/html");
      var next = page.getElementById("site-content");
      if (!next || !page.querySelector(".site-background-video")) throw new Error("Different page layout");
      if (pending !== controller) return;
      clearTimeout(timeout);
      clearTimeout(scrollTimer);
      if (!fromHistory) {
        saveScroll();
        history.pushState({ siteScroll: [0, 0] }, "", url.href);
      }
      currentPage = url.pathname + url.search;
      document.title = page.title;
      document.head.querySelectorAll(metadata).forEach(function (node) { node.remove(); });
      page.head.querySelectorAll(metadata).forEach(function (node) { document.head.appendChild(document.importNode(node, true)); });
      // Never remove, move, reload or seek the video element.
      container.replaceChildren(...Array.from(next.childNodes));
      await activateScripts(container);
      if (pending !== controller) return;
      refreshPage();
      restoreScroll(url, position);
      var heading = container.querySelector("h1");
      if (heading) {
        heading.setAttribute("tabindex", "-1");
        heading.focus({ preventScroll: true });
      }
    } catch (error) {
      // Superseded requests are ignored; unavailable pages retain normal navigation.
      if (pending === controller) location.assign(url.href);
    } finally {
      clearTimeout(timeout);
      if (pending === controller) {
        pending = null;
        container.removeAttribute("aria-busy");
      }
    }
  }

  document.addEventListener("click", function (event) {
    var link = event.target.closest("a[href]");
    if (!link || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    if (link.hasAttribute("download") || (link.target && link.target !== "_self") || link.hasAttribute("data-full-navigation")) return;
    var url = new URL(link.href);
    if (url.origin !== location.origin || !/^https?:$/.test(url.protocol)) return;
    if (/\.[^/]+$/.test(url.pathname) && !/\.html?$/.test(url.pathname)) return;
    if (url.pathname + url.search === currentPage) {
      cancelPending();
      if (!url.hash) { event.preventDefault(); window.scrollTo(0, 0); }
      return; // Native fragment navigation without reloading the current page.
    }
    event.preventDefault();
    visit(url, false);
  });

  window.addEventListener("popstate", function (event) {
    clearTimeout(scrollTimer);
    var url = new URL(location.href);
    if (url.pathname + url.search === currentPage) {
      cancelPending();
      restoreScroll(url, event.state && event.state.siteScroll);
      return;
    }
    visit(url, true, event.state && event.state.siteScroll);
  });
})();
