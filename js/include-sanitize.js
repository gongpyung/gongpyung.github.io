(function() {
  'use strict';

  document.addEventListener('DOMContentLoaded', function() {
    var containers = document.querySelectorAll('.doc-include');
    if (!containers.length) return;

    var isReleaseNotesPage = /\/docs\/\d+\.\d+\.\d+\/\d+\.\d+\.\d+\.\d+\/?$/.test(location.pathname);

    containers.forEach(function(container) {
      // 1) Neutralize legacy relative links
      container.querySelectorAll('a[href]').forEach(function(a) {
        var href = a.getAttribute('href');
        if (!href) return;

        // Preserve anchors/external/same-site absolute links
        if (href.startsWith('#')) return;
        if (/^https?:\/\//i.test(href)) return;
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

      // 2) Release-notes-only cleanup
      if (!isReleaseNotesPage) return;

      // Remove empty sections (heading followed by heading or no meaningful sectionbody)
      var headings = container.querySelectorAll('h2, h3');
      headings.forEach(function(heading) {
        var next = heading.nextElementSibling;

        if (!next || /^H[1-6]$/.test(next.tagName)) {
          heading.style.display = 'none';
          return;
        }

        if (next.classList && next.classList.contains('sectionbody')) {
          var hasContent = next.querySelector('ul, ol, p, table, pre, .listingblock');
          if (!hasContent) {
            heading.style.display = 'none';
            next.style.display = 'none';
          }
        }
      });

      // Remove trailing revision footer: "Version X.Y.Z" + "Last updated ..."
      container.querySelectorAll('p').forEach(function(p) {
        var text = (p.textContent || '').replace(/\s+/g, ' ').trim();
        if (/^Version\s+\d+\.\d+\.\d+(?:\.\d+)?\s+Last updated\s+/i.test(text)) {
          p.remove();
        }
      });
    });
  });
})();
