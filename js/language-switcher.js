// Enhanced Language Switcher for Hugo Geekdoc Theme
(function() {
    'use strict';
    
    // Language configuration
    const languages = {
        'ko': {
            name: '한국어',
            short: 'KO',
            flag: '🇰🇷'
        },
        'en': {
            name: 'English',
            short: 'EN',
            flag: '🇺🇸'
        }
    };
    
    // Get current language from URL or default
    function getCurrentLanguage() {
        const path = window.location.pathname;
        if (path.startsWith('/en/')) return 'en';
        if (path.startsWith('/ko/')) return 'ko';
        return 'ko'; // default language
    }
    
    // Get alternative language
    function getAlternativeLanguage() {
        const current = getCurrentLanguage();
        return current === 'ko' ? 'en' : 'ko';
    }
    
    // Switch language
    function switchLanguage() {
        const currentLang = getCurrentLanguage();
        const targetLang = getAlternativeLanguage();
        
        let newPath = window.location.pathname;
        
        // Remove current language prefix
        if (newPath.startsWith('/' + currentLang + '/')) {
            newPath = newPath.substring(3);
        }
        
        // Add target language prefix
        if (!newPath.startsWith('/')) {
            newPath = '/' + newPath;
        }
        newPath = '/' + targetLang + newPath;
        
        // Navigate to new URL
        window.location.href = newPath;
    }
    
    
    // Create language switcher button
    function createLanguageSwitcher() {
        const currentLang = getCurrentLanguage();
        
        // Create container
        const container = document.createElement('div');
        container.className = 'language-switcher-container';
        
        // Create button element
        const button = document.createElement('button');
        button.className = 'language-switcher';
        button.innerHTML = `
            <span class="lang-option" data-lang="ko">${languages.ko.name}</span>
            <span class="lang-option" data-lang="en">${languages.en.name}</span>
        `;
        button.title = `Switch to ${currentLang === 'ko' ? 'English' : '한국어'}`;
        button.onclick = switchLanguage;
        
        // Create sliding background
        const slider = document.createElement('div');
        slider.className = `language-slider ${currentLang}`;
        
        button.appendChild(slider);
        
        // Style the language options
        const langOptions = button.querySelectorAll('.lang-option');
        langOptions.forEach((option, index) => {
            const isActive = option.dataset.lang === currentLang;
            option.className = `lang-option ${isActive ? 'active' : 'inactive'}`;
        });
        
        // Store references
        button.slider = slider;
        button.langOptions = langOptions;
        button.currentLang = currentLang;
        
        // Function to update active state
        function updateActiveState(newLang) {
            // Update slider position
            slider.className = `language-slider ${newLang}`;
            
            // Update language options
            langOptions.forEach(option => {
                const isActive = option.dataset.lang === newLang;
                option.className = `lang-option ${isActive ? 'active' : 'inactive'}`;
            });
        }
        
        // Click handler with animation
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const targetLang = currentLang === 'ko' ? 'en' : 'ko';
            
            // Animate immediately
            updateActiveState(targetLang);
            
            // Add ripple effect
            const rect = button.getBoundingClientRect();
            const ripple = document.createElement('div');
            const size = Math.max(button.offsetWidth, button.offsetHeight);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.className = 'ripple';
            ripple.style.width = `${size}px`;
            ripple.style.height = `${size}px`;
            ripple.style.left = `${x}px`;
            ripple.style.top = `${y}px`;
            
            button.appendChild(ripple);
            
            // Ripple animation is now handled by CSS
            
            // Remove ripple after animation
            setTimeout(() => {
                if (ripple.parentNode) {
                    ripple.parentNode.removeChild(ripple);
                }
            }, 500);
            
            // Navigate after a short delay
            setTimeout(() => {
                switchLanguage();
            }, 200);
        });
        
        // Hover and press effects are now handled by CSS
        
        container.appendChild(button);
        return container;
    }
    
    // Initialize language switcher when DOM is ready
    function init() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', addLanguageSwitcher);
        } else {
            addLanguageSwitcher();
        }
        
    }
    
    function addLanguageSwitcher() {
        // Remove existing switcher
        const existing = document.querySelector('.language-switcher-container');
        if (existing) {
            existing.remove();
        }
        
        // Try to find the header or navigation area
        const selectors = [
            '.gdoc-menu-header'
        ];
        
        let targetElement = null;
        for (const selector of selectors) {
            targetElement = document.querySelector(selector);
            if (targetElement) break;
        }
        
        const switcher = createLanguageSwitcher();
        
        if (targetElement) {
            targetElement.prepend(switcher);
        } else {
            // Fallback: add to body with fixed position
            switcher.style.position = 'fixed';
            switcher.style.top = '20px';
            switcher.style.right = '20px';
            switcher.style.zIndex = '9999';
            document.body.appendChild(switcher);
        }
    }
    
    // Start the script
    init();
})();