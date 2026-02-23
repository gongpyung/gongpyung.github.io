(function() {
  'use strict';
  document.addEventListener('DOMContentLoaded', function() {
    var containers = document.querySelectorAll('.doc-include');
    if (!containers.length) return;

    containers.forEach(function(container) {
      // 0. Remove embedded legacy styles/scripts so theme styles can take over
      container.querySelectorAll('style, script, link[rel="stylesheet"]').forEach(function(el) {
        el.remove();
      });

      // 1. Hide legacy wrappers (CSS backup)
      ['#header', '#toc', '#toctitle'].forEach(function(sel) {
        var el = container.querySelector(sel);
        if (el) el.style.display = 'none';
      });

      // 2. Neutralize legacy relative links
      container.querySelectorAll('a[href]').forEach(function(a) {
        var href = a.getAttribute('href');
        if (!href) return;

        // Preserve anchors
        if (href.startsWith('#')) return;
        // Preserve external links
        if (/^https?:\/\//i.test(href)) return;
        // Preserve same-site absolute links
        if (href.startsWith('/')) return;

        // Neutralize legacy relative links (../../manual/..., {token}.html, etc.)
        if (href.includes('../../') || /\{[^}]+\}/.test(href) || href.match(/^[^/]*\.html$/)) {
          a.removeAttribute('href');
          a.setAttribute('title', 'Link unavailable in current documentation');
          a.style.color = 'var(--text-muted)';
          a.style.cursor = 'default';
          a.style.textDecoration = 'none';
        }
      });

      // 3. Remove empty sections in Release Notes (headings with no content)
      var headings = container.querySelectorAll('h2, h3');
      headings.forEach(function(heading) {
        var next = heading.nextElementSibling;
        // Empty section: heading followed by another heading or nothing
        if (!next || /^H[1-6]$/.test(next.tagName)) {
          heading.style.display = 'none';
        }
        // AsciiDoc: heading followed by sectionbody with no meaningful content
        if (next && next.classList && next.classList.contains('sectionbody')) {
          var hasContent = next.querySelector('ul, ol, p, table, pre, .listingblock');
          if (!hasContent) {
            heading.style.display = 'none';
            next.style.display = 'none';
          }
        }
      });

      // 4. Remove trailing revision footer on Release Notes pages:
      // "Version X.Y.Z" + "Last updated ..."
      if (/\/docs\/\d+\.\d+\.\d+\/\d+\.\d+\.\d+\.\d+\/?$/.test(location.pathname)) {
        container.querySelectorAll('p').forEach(function(p) {
          var text = (p.textContent || '').replace(/\s+/g, ' ').trim();
          if (/^Version\s+\d+\.\d+\.\d+(?:\.\d+)?\s+Last updated\s+/i.test(text)) {
            p.remove();
          }
        });
      }
    });
  });
})();
