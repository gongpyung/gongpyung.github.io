(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    var tocAside = document.getElementById('rightToc');

    var tocNav = tocAside ? tocAside.querySelector('.toc__content nav') : null;

    // If Hugo already generated TOC with items in right TOC
    if (tocNav && tocNav.querySelector('li')) {
      setupInteractions(tocNav, tocAside);
      return;
    }

    // Strategy 1: Clone TOC from .doc-include #toc (AsciiDoc include pages)
    var docToc = document.querySelector('.doc-include #toc');
    if (docToc) {
      var tocList = docToc.querySelector('ul');
      if (tocList) {
        if (tocNav) {
          tocNav.appendChild(tocList.cloneNode(true));
        }
        setupInteractions(tocNav, tocAside);
        return;
      }
    }

    // Strategy 2: Build TOC from h2/h3/h4 headings in content
    var content = document.querySelector('.doc-include') ||
                  document.querySelector('.doc-content__body') ||
                  document.querySelector('.layout__main');
    if (!content) {
      if (tocAside) tocAside.style.display = 'none';
      return;
    }

    var headings = Array.from(content.querySelectorAll('h2, h3, h4'));
    if (headings.length === 0) {
      if (tocAside) tocAside.style.display = 'none';
      return;
    }

    // Assign IDs to headings that don't have one
    headings.forEach(function (h, i) {
      if (!h.id) {
        h.id = 'dtoc-' + i + '-' + h.textContent.trim()
          .toLowerCase()
          .replace(/[^\w\s-]/g, '')
          .replace(/\s+/g, '-')
          .replace(/-+/g, '-')
          .slice(0, 50);
      }
    });

    // Build ul tree: h2 > h3 > h4
    var rootUl = document.createElement('ul');
    var currentH2Li = null;
    var currentH3Ul = null;
    var currentH3Li = null;
    var currentH4Ul = null;

    headings.forEach(function (h) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent.trim();
      li.appendChild(a);

      if (h.tagName === 'H2') {
        currentH2Li = li;
        currentH3Ul = null;
        currentH3Li = null;
        currentH4Ul = null;
        rootUl.appendChild(li);
      } else if (h.tagName === 'H3') {
        if (!currentH3Ul) {
          currentH3Ul = document.createElement('ul');
          (currentH2Li || rootUl).appendChild(currentH3Ul);
        }
        currentH3Li = li;
        currentH4Ul = null;
        currentH3Ul.appendChild(li);
      } else { // H4
        if (!currentH4Ul) {
          currentH4Ul = document.createElement('ul');
          (currentH3Li || currentH2Li || rootUl).appendChild(currentH4Ul);
        }
        currentH4Ul.appendChild(li);
      }
    });

    if (tocNav) {
      tocNav.appendChild(rootUl);
    }

    setupInteractions(tocNav, tocAside);
  });

  function setupInteractions(tocNav, tocAside) {
    var hasItems = tocNav && tocNav.querySelector('li');

    if (!hasItems) {
      if (tocAside) tocAside.style.display = 'none';
      return;
    }

    // Collect all links from right TOC
    var allLinks = [];
    if (tocNav) {
      tocNav.querySelectorAll('a[href^="#"]').forEach(function (l) { allLinks.push(l); });
    }

    // Build heading list (deduplicated by id)
    var headingEls = [];
    var seenIds = {};
    allLinks.forEach(function (link) {
      var id = link.getAttribute('href').slice(1);
      var el = document.getElementById(id);
      if (el && !seenIds[id]) {
        seenIds[id] = true;
        headingEls.push({ el: el, id: id });
      }
    });

    // Smooth scroll
    allLinks.forEach(function (link) {
      link.addEventListener('click', function (e) {
        e.preventDefault();
        var target = document.getElementById(link.getAttribute('href').slice(1));
        if (!target) return;
        var headerEl = document.querySelector('.header');
        var offset = headerEl ? headerEl.offsetHeight + 16 : 80;
        window.scrollTo({
          top: target.getBoundingClientRect().top + window.pageYOffset - offset,
          behavior: 'smooth'
        });
      });
    });

    // Scroll spy
    function getOffset() {
      var headerEl = document.querySelector('.header');
      return headerEl ? headerEl.offsetHeight + 24 : 100;
    }

    function updateActive() {
      var scrollY = window.pageYOffset;
      var offset = getOffset();
      var activeId = null;

      for (var i = headingEls.length - 1; i >= 0; i--) {
        var headingTop = headingEls[i].el.getBoundingClientRect().top + scrollY;
        if (scrollY >= headingTop - offset) {
          activeId = headingEls[i].id;
          break;
        }
      }

      allLinks.forEach(function (link) {
        var linkId = link.getAttribute('href').slice(1);
        link.classList.toggle('is-active', activeId !== null && linkId === activeId);
      });
    }

    updateActive();

    var ticking = false;
    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(function () {
          updateActive();
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }
})();
