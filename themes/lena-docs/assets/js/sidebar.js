(function() {
  'use strict';

  function init() {
    var sidebar = document.getElementById('sidebar');
    var menuToggle = document.querySelector('.header__menu-toggle');
    var body = document.body;

    if (!sidebar) return;

    // ── Mobile overlay ──
    var overlay = document.createElement('div');
    overlay.className = 'sidebar-overlay';
    body.appendChild(overlay);

    function closeSidebar() {
      sidebar.classList.remove('is-open');
      overlay.classList.remove('is-visible');
      body.style.overflow = '';
    }

    if (menuToggle) {
      menuToggle.addEventListener('click', function() {
        var isOpen = sidebar.classList.toggle('is-open');
        overlay.classList.toggle('is-visible', isOpen);
        body.style.overflow = isOpen ? 'hidden' : '';
      });
    }

    overlay.addEventListener('click', closeSidebar);

    // Close on nav link click (mobile)
    sidebar.querySelectorAll('a.sidebar__link').forEach(function(link) {
      link.addEventListener('click', function() {
        if (window.innerWidth < 1024) {
          closeSidebar();
        }
      });
    });

    // ── Version selector ──
    var versionSelect = document.getElementById('versionSelect');
    if (versionSelect) {
      versionSelect.addEventListener('change', function() {
        var version = this.value;
        var lang = document.documentElement.getAttribute('lang');
        var prefix = (lang && lang !== 'ko') ? '/' + lang : '';
        window.location.href = prefix + '/docs/' + version + '/';
      });
    }

    // ── Section collapsible toggle ──
    sidebar.querySelectorAll('.sidebar__section-title').forEach(function(btn) {
      btn.addEventListener('click', function() {
        var section = this.closest('.sidebar__section');
        var isNowCollapsed = section.classList.toggle('is-collapsed');
        this.setAttribute('aria-expanded', String(!isNowCollapsed));
      });
    });

    // ── Patch version group accordion ──
    sidebar.querySelectorAll('.sidebar__group-btn').forEach(function(btn) {
      btn.addEventListener('click', function() {
        var isOpen = this.classList.toggle('is-open');
        this.setAttribute('aria-expanded', String(isOpen));
        var targetId = this.getAttribute('aria-controls');
        var submenu = targetId ? document.getElementById(targetId) : null;
        if (submenu) {
          submenu.classList.toggle('is-open', isOpen);
        }
      });
    });

    // ── Login button (opens login modal) ──
    var sidebarLoginBtn = document.getElementById('sidebarLoginBtn');
    if (sidebarLoginBtn) {
      sidebarLoginBtn.addEventListener('click', function() {
        var loginModal = document.getElementById('loginModal');
        if (loginModal) {
          loginModal.classList.add('is-open');
          closeSidebar();
          body.style.overflow = 'hidden';
        }
      });
    }

    // ── Search modal ──
    var searchToggle = document.getElementById('searchToggle');
    var searchModal = document.getElementById('searchModal');
    var searchOverlay = document.getElementById('searchOverlay');
    var searchInput = document.getElementById('searchInput');

    if (searchModal) {
      function openSearch() {
        searchModal.classList.add('is-open');
        body.style.overflow = 'hidden';
        if (searchInput) searchInput.focus();
      }
      function closeSearch() {
        searchModal.classList.remove('is-open');
        body.style.overflow = '';
      }

      if (searchToggle) searchToggle.addEventListener('click', openSearch);
      if (searchOverlay) searchOverlay.addEventListener('click', closeSearch);

      document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
          e.preventDefault();
          searchModal.classList.contains('is-open') ? closeSearch() : openSearch();
        }
        if (e.key === 'Escape' && searchModal.classList.contains('is-open')) {
          closeSearch();
        }
      });
    }

    // ── Login modal ──
    var loginToggle = document.getElementById('loginToggle');
    var loginModal = document.getElementById('loginModal');
    var loginOverlay = document.getElementById('loginOverlay');
    var loginClose = document.getElementById('loginClose');

    if (loginToggle && loginModal) {
      function closeLogin() {
        loginModal.classList.remove('is-open');
        body.style.overflow = '';
      }

      loginToggle.addEventListener('click', function() {
        loginModal.classList.add('is-open');
        body.style.overflow = 'hidden';
      });

      if (loginOverlay) loginOverlay.addEventListener('click', closeLogin);
      if (loginClose) loginClose.addEventListener('click', closeLogin);

      document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && loginModal.classList.contains('is-open')) {
          closeLogin();
        }
      });
    }

    // ── Desktop sidebar collapse ──
    var collapseBtn = document.getElementById('sidebarCollapseBtn');
    var expandBtn = document.getElementById('sidebarExpandBtn');

    function collapseSidebar() {
      body.classList.add('sidebar-collapsed');
      if (expandBtn) expandBtn.style.display = '';
      localStorage.setItem('sidebarCollapsed', 'true');
    }

    function expandSidebar() {
      body.classList.remove('sidebar-collapsed');
      if (expandBtn) expandBtn.style.display = 'none';
      localStorage.setItem('sidebarCollapsed', 'false');
    }

    if (collapseBtn) collapseBtn.addEventListener('click', collapseSidebar);
    if (expandBtn) {
      expandBtn.addEventListener('click', expandSidebar);
      // Restore state from localStorage (desktop only)
      if (window.innerWidth >= 1024 && localStorage.getItem('sidebarCollapsed') === 'true') {
        collapseSidebar();
      } else {
        expandBtn.style.display = 'none';
      }
    }

  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
