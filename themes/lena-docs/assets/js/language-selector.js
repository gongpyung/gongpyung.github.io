(function() {
  'use strict';

  var languages = {
    'ko': { name: '한국어', code: 'KO' },
    'en': { name: 'English', code: 'EN' }
  };

  function getCurrentLanguage() {
    var path = window.location.pathname;
    if (path.startsWith('/en/') || path === '/en') return 'en';
    return 'ko';
  }

  function switchLanguage(targetLang) {
    var path = window.location.pathname;
    var currentLang = getCurrentLanguage();

    if (currentLang === targetLang) return;

    var newPath;
    if (currentLang === 'en') {
      // Strip /en prefix
      newPath = path.replace(/^\/en(\/|$)/, '/');
    } else {
      // Default lang (ko) has no prefix; strip /ko if somehow present
      newPath = path.replace(/^\/ko(\/|$)/, '/');
    }

    if (targetLang === 'en') {
      newPath = '/en' + (newPath.startsWith('/') ? '' : '/') + newPath;
    }

    window.location.href = newPath;
  }

  function setMenuOpen(menu, trigger, open) {
    menu.classList.toggle('is-open', open);
    trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
  }

  function init() {
    var container = document.getElementById('langSelector');
    if (!container) return;

    var currentLang = getCurrentLanguage();
    var currentInfo = languages[currentLang];

    var globeIcon = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><circle cx="7" cy="7" r="5.5" stroke="currentColor" stroke-width="1.2"/><path d="M1.5 7h11M7 1.5c-1.5 1.5-2 3.5-2 5.5s.5 4 2 5.5M7 1.5c1.5 1.5 2 3.5 2 5.5s-.5 4-2 5.5" stroke="currentColor" stroke-width="1.2"/></svg>';
    var chevronIcon = '<svg width="10" height="10" viewBox="0 0 10 10" fill="none" aria-hidden="true"><path d="M2.5 4l2.5 2.5L7.5 4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';

    var menuItems = Object.keys(languages).map(function(key) {
      var lang = languages[key];
      var activeClass = key === currentLang ? ' is-active' : '';
      return '<button class="lang-dropdown__item' + activeClass + '" data-lang="' + key + '" role="menuitem">' + lang.name + '</button>';
    }).join('');

    container.innerHTML =
      '<div class="lang-dropdown">' +
        '<button class="lang-dropdown__trigger" aria-label="Select language: ' + currentInfo.name + '" aria-expanded="false" aria-haspopup="true">' +
          globeIcon +
          ' ' + currentInfo.code + ' ' +
          chevronIcon +
        '</button>' +
        '<div class="lang-dropdown__menu" role="menu">' +
          menuItems +
        '</div>' +
      '</div>';

    var trigger = container.querySelector('.lang-dropdown__trigger');
    var menu = container.querySelector('.lang-dropdown__menu');

    trigger.addEventListener('click', function(e) {
      e.stopPropagation();
      var opening = !menu.classList.contains('is-open');
      setMenuOpen(menu, trigger, opening);
      // Close other dropdowns
      document.querySelectorAll('.theme-dropdown__menu.is-open').forEach(function(m) {
        var t = m.closest('.theme-dropdown').querySelector('.theme-dropdown__trigger');
        setMenuOpen(m, t, false);
      });
    });

    container.querySelectorAll('.lang-dropdown__item').forEach(function(item) {
      item.addEventListener('click', function() {
        switchLanguage(this.dataset.lang);
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
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
