(function() {
  'use strict';

  function init() {
    document.querySelectorAll('pre').forEach(function(pre) {
      if (pre.querySelector('.code-block__copy')) return;

      var btn = document.createElement('button');
      btn.className = 'code-block__copy';
      btn.textContent = 'Copy';
      btn.setAttribute('aria-label', 'Copy code');

      btn.addEventListener('click', function() {
        var code = pre.querySelector('code');
        var text = code ? code.textContent : pre.textContent;

        navigator.clipboard.writeText(text).then(function() {
          btn.textContent = 'Copied!';
          btn.classList.add('is-copied');
          setTimeout(function() {
            btn.textContent = 'Copy';
            btn.classList.remove('is-copied');
          }, 2000);
        });
      });

      pre.style.position = 'relative';
      pre.appendChild(btn);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
