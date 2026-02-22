(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    var tocAside = document.getElementById('rightToc');
    if (!tocAside) return;

    var tocNav = tocAside.querySelector('.toc__content nav');
    if (!tocNav) return;

    // If Hugo already generated TOC with items, just set up interactions
    if (tocNav.querySelector('li')) {
      setupInteractions(tocNav, tocAside);
      return;
    }

    // Strategy 1: Clone TOC from .doc-include #toc (AsciiDoc include pages)
    var docToc = document.querySelector('.doc-include #toc');
    if (docToc) {
      var tocList = docToc.querySelector('ul');
      if (tocList) {
        var cloned = tocList.cloneNode(true);
        tocNav.appendChild(cloned);
        setupInteractions(tocNav, tocAside);
        return;
      }
    }

    // Strategy 2: Build TOC from h2/h3 headings in content
    var content = document.querySelector('.doc-include') ||
                  document.querySelector('.doc-content__body') ||
                  document.querySelector('.layout__main');
    if (!content) {
      tocAside.style.display = 'none';
      return;
    }

    var headings = Array.from(content.querySelectorAll('h2, h3'));
    if (headings.length === 0) {
      tocAside.style.display = 'none';
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

    // Build ul tree
    var rootUl = document.createElement('ul');
    var currentH2Li = null;
    var currentH3Ul = null;

    headings.forEach(function (h) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent.trim();
      li.appendChild(a);

      if (h.tagName === 'H2') {
        currentH2Li = li;
        currentH3Ul = null;
        rootUl.appendChild(li);
      } else {
        if (!currentH3Ul) {
          currentH3Ul = document.createElement('ul');
          (currentH2Li || rootUl).appendChild(currentH3Ul);
        }
        currentH3Ul.appendChild(li);
      }
    });

    tocNav.appendChild(rootUl);
    setupInteractions(tocNav, tocAside);
  });

  function setupInteractions(tocNav, tocAside) {
    // Final check: if still no items, hide
    if (!tocNav.querySelector('li')) {
      tocAside.style.display = 'none';
      return;
    }

    var links = tocNav.querySelectorAll('a[href^="#"]');
    var headingEls = [];

    links.forEach(function (link) {
      var id = link.getAttribute('href').slice(1);
      var el = document.getElementById(id);
      if (el) headingEls.push({ el: el, link: link });
    });

    // Smooth scroll
    links.forEach(function (link) {
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
      var active = null;

      for (var i = headingEls.length - 1; i >= 0; i--) {
        var headingTop = headingEls[i].el.getBoundingClientRect().top + scrollY;
        if (scrollY >= headingTop - offset) {
          active = headingEls[i];
          break;
        }
      }

      links.forEach(function (link) {
        link.classList.toggle(
          'is-active',
          active !== null && link === active.link
        );
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
