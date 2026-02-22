(function() {
  'use strict';

  var STORAGE_KEY = 'lena-docs-theme';

  function getSystemTheme() {
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function getStoredTheme() {
    return localStorage.getItem(STORAGE_KEY);
  }

  function applyTheme(theme) {
    if (theme === 'system') {
      document.documentElement.removeAttribute('data-theme');
    } else {
      document.documentElement.setAttribute('data-theme', theme);
    }
    updateToggleIcon(theme);
  }

  function updateToggleIcon(theme) {
    var trigger = document.querySelector('.theme-dropdown__trigger');
    if (!trigger) return;

    var icons = {
      light: '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="3" stroke="currentColor" stroke-width="1.5"/><path d="M8 1v2M8 13v2M1 8h2M13 8h2M3.05 3.05l1.414 1.414M11.536 11.536l1.414 1.414M3.05 12.95l1.414-1.414M11.536 4.464l1.414-1.414" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>',
      dark: '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M14 9.2A6 6 0 116.8 2 4.8 4.8 0 0014 9.2z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
      system: '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><rect x="2" y="3" width="12" height="8" rx="1" stroke="currentColor" stroke-width="1.5"/><path d="M5 14h6M8 11v3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'
    };

    trigger.innerHTML = icons[theme] || icons.system;

    // Update active state in menu
    document.querySelectorAll('.theme-dropdown__item').forEach(function(item) {
      item.classList.toggle('is-active', item.dataset.theme === theme);
    });
  }

  function setMenuOpen(menu, trigger, open) {
    menu.classList.toggle('is-open', open);
    trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  function init() {
    var container = document.getElementById('themeToggle');
    if (!container) return;

    container.innerHTML =
      '<div class="theme-dropdown">' +
        '<button class="theme-dropdown__trigger" aria-label="Toggle theme" aria-expanded="false" aria-haspopup="true"></button>' +
        '<div class="theme-dropdown__menu" role="menu">' +
          '<button class="theme-dropdown__item" data-theme="light" role="menuitem">' +
            '<svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="3" stroke="currentColor" stroke-width="1.5"/><path d="M8 1v2M8 13v2M1 8h2M13 8h2M3.05 3.05l1.414 1.414M11.536 11.536l1.414 1.414M3.05 12.95l1.414-1.414M11.536 4.464l1.414-1.414" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>' +
            ' Light' +
          '</button>' +
          '<button class="theme-dropdown__item" data-theme="dark" role="menuitem">' +
            '<svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M14 9.2A6 6 0 116.8 2 4.8 4.8 0 0014 9.2z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>' +
            ' Dark' +
          '</button>' +
          '<button class="theme-dropdown__item" data-theme="system" role="menuitem">' +
            '<svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true"><rect x="2" y="3" width="12" height="8" rx="1" stroke="currentColor" stroke-width="1.5"/><path d="M5 14h6M8 11v3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>' +
            ' System' +
          '</button>' +
        '</div>' +
      '</div>';

    var trigger = container.querySelector('.theme-dropdown__trigger');
    var menu = container.querySelector('.theme-dropdown__menu');

    trigger.addEventListener('click', function(e) {
      e.stopPropagation();
      var opening = !menu.classList.contains('is-open');
      setMenuOpen(menu, trigger, opening);
      // Close other dropdowns
      document.querySelectorAll('.lang-dropdown__menu.is-open').forEach(function(m) {
        var t = m.closest('.lang-dropdown').querySelector('.lang-dropdown__trigger');
        setMenuOpen(m, t, false);
      });
    });

    container.querySelectorAll('.theme-dropdown__item').forEach(function(item) {
      item.addEventListener('click', function() {
        var theme = this.dataset.theme;
        localStorage.setItem(STORAGE_KEY, theme);
        applyTheme(theme);
        setMenuOpen(menu, trigger, false);
      });
    });

    document.addEventListener('click', function() {
      setMenuOpen(menu, trigger, false);
    });

    // Keyboard: close on Escape
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        setMenuOpen(menu, trigger, false);
      }
    });

    // Reflect system theme changes when in system mode
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function() {
      if (getStoredTheme() === 'system' || !getStoredTheme()) {
        applyTheme('system');
      }
    });

    // Apply stored theme on init
    var stored = getStoredTheme() || 'system';
    applyTheme(stored);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
