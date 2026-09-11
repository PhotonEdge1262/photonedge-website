# -*- coding: utf-8 -*-
import os, re

BASE = '/Coze/Drive/萧邮/v123-work'

# New nav content for navbar pattern (product/material pages)
NEW_NAVBAR = '''<nav class="navbar">
        <div class="container">
            <a href="/" class="nav-logo">
                <img src="/logo.png" alt="PhotonEdge Optics" class="nav-logo-img">
            </a>
            <ul class="nav-list">
                <li><a href="/products.html" class="nav-link" data-i18n="navProducts">Products</a></li>
                <li><a href="/applications.html" class="nav-link" data-i18n="navApplications">Applications</a></li>
                <li><a href="/contact.html" class="nav-link" data-i18n="navCustomOptics">Custom Optics</a></li>
                <li class="nav-dropdown">
                    <a href="#" class="nav-link" data-i18n="navResources">Resources &#9662;</a>
                    <div class="dropdown-menu">
                        <a href="/knowledge-center/" class="dropdown-item" data-i18n="navKnowledgeCenter"><span class="dropdown-icon">📚</span> Knowledge Center</a>
                        <a href="/application-notes/" class="dropdown-item" data-i18n="navApplicationNotes"><span class="dropdown-icon">📄</span> Application Notes</a>
                        <a href="/coatings/" class="dropdown-item" data-i18n="navCoatings"><span class="dropdown-icon">🔬</span> Coating Database</a>
                        <a href="/materials.html" class="dropdown-item" data-i18n="navMaterials"><span class="dropdown-icon">🧪</span> Materials Guide</a>
                        <a href="/faq.html" class="dropdown-item" data-i18n="navFAQ"><span class="dropdown-icon">❓</span> FAQ</a>
                        <a href="/ai-optical-engineer.html" class="dropdown-item" data-i18n="navAIOptical"><span class="dropdown-icon">🤖</span> AI Optical Engineer</a>
                    </div>
                </li>
                <li class="nav-dropdown">
                    <a href="#" class="nav-link" data-i18n="navAboutDropdown">About &#9662;</a>
                    <div class="dropdown-menu">
                        <a href="/about.html" class="dropdown-item" data-i18n="navAboutPhotonEdge"><span class="dropdown-icon">🏢</span> About PhotonEdge</a>
                        <a href="/quality-assurance.html" class="dropdown-item" data-i18n="navQualityDoc"><span class="dropdown-icon">✅</span> Quality &amp; Documentation</a>
                        <a href="/case-studies.html" class="dropdown-item" data-i18n="navCaseStudies"><span class="dropdown-icon">📋</span> Case Studies</a>
                    </div>
                </li>
            </ul>
            <div class="nav-actions">
                <button class="lang-toggle" id="langToggle" onclick="toggleLanguage()">
                    <span data-i18n="langSwitch">中文</span>
                </button>
                <button class="mobile-menu-btn" onclick="toggleMobileMenu()">☰</button>
            </div>
        </div>
    </nav>'''

# New nav for materials.html which uses <nav class="nav"> but isn't in <header>
NEW_NAV_SIMPLE = '''<nav class="nav">
                <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">&#9776;</button>
                <ul class="nav-list">
                    <li><a href="/products.html" class="nav-link" data-i18n="navProducts">Products</a></li>
                    <li><a href="/applications.html" class="nav-link" data-i18n="navApplications">Applications</a></li>
                    <li><a href="/contact.html" class="nav-link" data-i18n="navCustomOptics">Custom Optics</a></li>
                    <li class="nav-dropdown">
                        <a href="#" class="nav-link" data-i18n="navResources">Resources &#9662;</a>
                        <div class="dropdown-menu">
                            <a href="/knowledge-center/" class="dropdown-item" data-i18n="navKnowledgeCenter"><span class="dropdown-icon">📚</span> Knowledge Center</a>
                            <a href="/application-notes/" class="dropdown-item" data-i18n="navApplicationNotes"><span class="dropdown-icon">📄</span> Application Notes</a>
                            <a href="/coatings/" class="dropdown-item" data-i18n="navCoatings"><span class="dropdown-icon">🔬</span> Coating Database</a>
                            <a href="/materials.html" class="dropdown-item" data-i18n="navMaterials"><span class="dropdown-icon">🧪</span> Materials Guide</a>
                            <a href="/faq.html" class="dropdown-item" data-i18n="navFAQ"><span class="dropdown-icon">❓</span> FAQ</a>
                            <a href="/ai-optical-engineer.html" class="dropdown-item" data-i18n="navAIOptical"><span class="dropdown-icon">🤖</span> AI Optical Engineer</a>
                        </div>
                    </li>
                    <li class="nav-dropdown">
                        <a href="#" class="nav-link" data-i18n="navAboutDropdown">About &#9662;</a>
                        <div class="dropdown-menu">
                            <a href="/about.html" class="dropdown-item" data-i18n="navAboutPhotonEdge"><span class="dropdown-icon">🏢</span> About PhotonEdge</a>
                            <a href="/quality-assurance.html" class="dropdown-item" data-i18n="navQualityDoc"><span class="dropdown-icon">✅</span> Quality &amp; Documentation</a>
                            <a href="/case-studies.html" class="dropdown-item" data-i18n="navCaseStudies"><span class="dropdown-icon">📋</span> Case Studies</a>
                        </div>
                    </li>
                </ul>
                <div class="lang-switcher">
                    <button class="lang-btn notranslate active" onclick="setLanguage('en')">EN</button>
                    <button class="lang-btn notranslate" onclick="setLanguage('zh')">中文</button>
                </div>
                <a href="/contact.html" class="btn btn-primary nav-cta-btn" data-i18n="navCTA" style="padding:8px 20px;border-radius:6px;font-size:14px;color:white;text-decoration:none;margin-left:8px;">Request a Quote</a>
            </nav>'''

count_navbar = 0
count_nav = 0
count_no_nav = 0
failed = []

for root, dirs, files in os.walk(BASE):
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        rel = os.path.relpath(fpath, BASE)
        
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip already updated files
        if 'navCustomOptics' in content:
            continue
        
        is_about = (rel == 'about.html')
        
        # Pattern 1: <nav class="navbar">...</nav> (product/material pages)
        navbar_match = re.search(r'<nav class="navbar">.*?</nav>', content, re.DOTALL)
        if navbar_match:
            new_nav = NEW_NAVBAR
            if is_about:
                new_nav = new_nav.replace(
                    '<a href="#" class="nav-link" data-i18n="navAboutDropdown">',
                    '<a href="#" class="nav-link active" data-i18n="navAboutDropdown">'
                )
            new_content = content[:navbar_match.start()] + new_nav + content[navbar_match.end():]
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count_navbar += 1
            continue
        
        # Pattern 2: <nav class="nav">...</nav> (materials.html etc, without header wrapper)
        nav_match = re.search(r'<nav class="nav">.*?</nav>', content, re.DOTALL)
        if nav_match:
            new_nav = NEW_NAV_SIMPLE
            if is_about:
                new_nav = new_nav.replace(
                    '<a href="#" class="nav-link" data-i18n="navAboutDropdown">',
                    '<a href="#" class="nav-link active" data-i18n="navAboutDropdown">'
                )
            new_content = content[:nav_match.start()] + new_nav + content[nav_match.end():]
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count_nav += 1
            continue
        
        # No nav found
        count_no_nav += 1
        failed.append(rel)

print(f"navbar pattern updated: {count_navbar}")
print(f"nav pattern updated: {count_nav}")
print(f"No nav found (skipped): {count_no_nav}")
if failed:
    print(f"Files without nav: {failed}")
