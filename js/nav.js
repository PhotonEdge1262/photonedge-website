// 全站统一导航栏组件
// 只需要在每个HTML页面引入，不需要重复写导航HTML

function renderNavigation() {
    var navHTML = '\
        <nav class="nav">\
            <div class="nav-container">\
                <a href="index.html" class="logo">\
                    <picture>\
                        <source srcset="images/logo.webp" type="image/webp">\
                        <img src="logo.png" alt="PhotonEdge" width="160" height="40">\
                    </picture>\
                </a>\
                <ul class="nav-menu">\
                    <li><a href="products.html" data-i18n="navProducts">Products</a></li>\
                    <li><a href="about.html" data-i18n="navAbout">About Us</a></li>\
                    <li><a href="calculator.html" data-i18n="navTools">Tools</a></li>\
                    <li><a href="faq.html" data-i18n="navFAQ">FAQ</a></li>\
                    <li><a href="blog.html" data-i18n="navBlog">Blog</a></li>\
                    <li><a href="contact.html" class="nav-cta" data-i18n="navContact">Contact</a></li>\
                </ul>\
                <div class="nav-lang">\
                    <button class="lang-btn" onclick="setLanguage(\'en\')">EN</button>\
                    <button class="lang-btn" onclick="setLanguage(\'zh\')">中文</button>\
                </div>\
                <button class="nav-toggle" onclick="toggleMobileMenu()">☰</button>\
            </div>\
        </nav>';
    
    // 替换header或插入到body开头
    var header = document.querySelector('header');
    if (header) {
        header.innerHTML = navHTML;
    } else {
        // 如果没有header，创建一个
        var newHeader = document.createElement('header');
        newHeader.className = 'header';
        newHeader.innerHTML = navHTML;
        document.body.insertBefore(newHeader, document.body.firstChild);
    }
    
    // 更新语言按钮状态
    updateLangButtons();
}

function updateLangButtons() {
    var currentLang = localStorage.getItem('lang') || 'en';
    var buttons = document.querySelectorAll('.lang-btn');
    buttons.forEach(function(btn) {
        btn.classList.remove('active');
        if ((currentLang === 'en' && btn.textContent === 'EN') || 
            (currentLang === 'zh' && btn.textContent === '中文')) {
            btn.classList.add('active');
        }
    });
}

// 页面加载时渲染导航
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderNavigation);
} else {
    renderNavigation();
}
