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
    });
  });
})();
