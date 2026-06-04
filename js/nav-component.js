// 导航栏组件 - 动态渲染避免代码重复
function renderNavigation() {
    var navHTML = '\
    <header class="header">\
        <div class="container">\
            <a href="index.html" class="logo">\
                <picture>\
                    <source srcset="images/logo.webp" type="image/webp">\
                    <img src="logo.png" alt="PhotonEdge" width="160" height="40">\
                </picture>\
            </a>\
            <nav class="nav">\
                <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">&#9776;</button>\
                <ul class="nav-list">\
                    <li><a href="index.html" class="nav-link" data-i18n="navHome">Home</a></li>\
                    <li><a href="products.html" class="nav-link" data-i18n="navProducts">Products</a></li>\
                    <li><a href="about.html" class="nav-link" data-i18n="navAbout">About Us</a></li>\
                    <li><a href="downloads.html" class="nav-link" data-i18n="navDownloads">Downloads</a></li>\
                    <li><a href="blog.html" class="nav-link" data-i18n="navBlog">Blog</a></li>\
                    <li><a href="contact.html" class="nav-link" data-i18n="navContact">Contact</a></li>\
                </ul>\
                <a href="cart.html" class="cart-icon" title="Shopping Cart">\
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>\
                    <span class="cart-badge" id="cartBadge">0</span>\
                </a>\
                <button class="theme-toggle" onclick="toggleDarkMode()">🌙</button>\
                <button class="lang-toggle" onclick="toggleLanguage()">EN</button>\
            </nav>\
        </div>\
    </header>';
    
    // 找到第一个script标签前插入，或者直接在body开头插入
    var body = document.body;
    var firstChild = body.firstChild;
    
    // 创建临时容器
    var temp = document.createElement('div');
    temp.innerHTML = navHTML;
    var header = temp.firstChild;
    
    // 如果已经有header，替换它；否则插入到最前面
    var existingHeader = document.querySelector('header.header');
    if (existingHeader) {
        existingHeader.parentNode.replaceChild(header, existingHeader);
    } else {
        body.insertBefore(header, firstChild);
    }
}

// 渲染底部导航栏（mobile）
function renderMobileNav() {
    var mobileNavHTML = '\
    <div class="mobile-nav">\
        <a href="index.html" class="mobile-nav-item" data-i18n="navHome">\
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>\
            <span>Home</span>\
        </a>\
        <a href="products.html" class="mobile-nav-item" data-i18n="navProducts">\
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>\
            <span>Products</span>\
        </a>\
        <a href="cart.html" class="mobile-nav-item" data-i18n="navCart">\
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>\
            <span>Cart</span>\
        </a>\
        <a href="about.html" class="mobile-nav-item" data-i18n="navAbout">\
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>\
            <span>About</span>\
        </a>\
        <a href="contact.html" class="mobile-nav-item" data-i18n="navContact">\
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>\
            <span>Contact</span>\
        </a>\
    </div>';
    
    var temp = document.createElement('div');
    temp.innerHTML = mobileNavHTML;
    var mobileNav = temp.firstChild;
    
    var existingMobileNav = document.querySelector('.mobile-nav');
    if (existingMobileNav) {
        existingMobileNav.parentNode.replaceChild(mobileNav, existingMobileNav);
    } else {
        document.body.appendChild(mobileNav);
    }
}

// 页面加载时渲染
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
        renderNavigation();
        renderMobileNav();
    });
} else {
    renderNavigation();
    renderMobileNav();
}
