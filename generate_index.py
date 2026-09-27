# -*- coding: utf-8 -*-
import os

BASE = '/tmp/v142-build'

# Read current index.html to extract the footer and scripts
with open(os.path.join(BASE, 'index.html'), 'r') as f:
    old = f.read()

# Extract footer (from <footer> to </footer>)
footer_start = old.find('    <footer class="footer">')
footer_end = old.find('</footer>') + len('</footer>')
footer = old[footer_start:footer_end]

# Extract all scripts after footer
scripts_start = old.find('\n<!-- WhatsApp Floating Button -->')
scripts = old[scripts_start:]

# New index.html
new_index = '''<!DOCTYPE html>
<html lang="en">
<head>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="dns-prefetch" href="https://www.google-analytics.com">
    
    <meta charset="UTF-8">
    <link rel="icon" type="image/png" sizes="32x32" href="https://photonedgeoptics.com/images/favicon-32.png">
    <link rel="icon" type="image/svg+xml" href="https://photonedgeoptics.com/images/favicon.svg">
    <link rel="apple-touch-icon" sizes="180x180" href="https://photonedgeoptics.com/images/apple-touch-icon.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title data-i18n="v142Title">PhotonEdge | Precision Optical Components, Materials &amp; Engineering Resources</title>
    <meta name="description" content="PhotonEdge connects optical components, materials databases and coating resources in one platform. Sourcing and specification platform for engineers and procurement teams.">
    <meta name="keywords" content="precision optical components, optical materials database, coating specifications, custom optics, optical sourcing, PhotonEdge">
    <meta property="og:title" content="PhotonEdge | Precision Optical Components, Materials &amp; Engineering Resources">
    <meta property="og:description" content="A sourcing and specification platform for engineers and procurement teams. Optical components, materials databases and coating resources.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://photonedgeoptics.com">
    <meta property="og:image" content="https://photonedgeoptics.com/images/logo.webp">
    <meta property="og:site_name" content="PhotonEdge">
    <link rel="canonical" href="https://photonedgeoptics.com/">
    <link rel="stylesheet" href="/css/style.css">
    
    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-E6J791MXZY"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-E6J791MXZY');
    </script>
    <link rel="alternate" hreflang="en" href="https://photonedgeoptics.com/">
    <link rel="alternate" hreflang="zh-CN" href="https://photonedgeoptics.com/zh/">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="PhotonEdge | Precision Optical Components, Materials &amp; Engineering Resources">
    <meta name="twitter:description" content="A sourcing and specification platform for engineers and procurement teams.">
    <meta name="twitter:image" content="https://photonedgeoptics.com/images/logo.webp">
    <link rel="stylesheet" href="/css/chatbot.css">

    <!-- Baidu Search Auto Push -->
    <script>
        (function(){
            var bp = document.createElement('script');
            var curProtocol = window.location.protocol.split(':')[0];
            if (curProtocol === 'https') {
                bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
            } else {
                bp.src = 'https://push.zhangzifan.com/linksubmit/push.js';
            }
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(bp, s);
        })();
    </script>
    <meta name="google" content="notranslate">
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "PhotonEdge Optics",
    "url": "https://photonedgeoptics.com",
    "description": "A sourcing and specification platform for optical components, materials and engineering resources.",
    "address": {"@type": "PostalAddress", "addressLocality": "Beijing", "addressCountry": "CN"},
    "email": "sales@photonedgeoptics.com",
    "sameAs": []
}
    </script>
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "PhotonEdge",
    "url": "https://photonedgeoptics.com",
    "potentialAction": {
        "@type": "SearchAction",
        "target": "https://photonedgeoptics.com/products/?q={search_term_string}",
        "query-input": "required name=search_term_string"
    }
}
    </script>
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://photonedgeoptics.com/"}
    ]
}
    </script>
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="/" class="logo">
    <picture>
        <source srcset="/images/logo.webp" type="image/webp">
        <img src="https://photonedgeoptics.com/logo.png" alt="PhotonEdge" width="160" height="40">
    </picture>
</a>
            <nav class="nav">
                <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">&#9776;</button>
                <ul class="nav-list">
                    <li class="nav-dropdown">
                    <a href="/products.html" class="nav-link" data-i18n="navProducts">Products &#9662;</a>
                    <div class="dropdown-menu">
                        <a href="/products.html?category=Optical+Lenses" class="dropdown-item"><span class="dropdown-icon">&#128269;</span> Optical Lenses</a>
                        <a href="/products.html?category=Optical+Windows" class="dropdown-item"><span class="dropdown-icon">&#129695;</span> Optical Windows</a>
                        <a href="/products.html?category=Optical+Mirrors" class="dropdown-item"><span class="dropdown-icon">&#129694;</span> Optical Mirrors</a>
                        <a href="/products.html?category=Optical+Filters" class="dropdown-item"><span class="dropdown-icon">&#127752;</span> Optical Filters</a>
                        <a href="/products.html?category=Beamsplitters" class="dropdown-item"><span class="dropdown-icon">&#9671;</span> Beamsplitters</a>
                        <a href="/products.html?category=Optical+Prisms" class="dropdown-item"><span class="dropdown-icon">&#128142;</span> Optical Prisms</a>
                        <a href="/products.html?category=Waveplates+%26+Polarizers" class="dropdown-item"><span class="dropdown-icon">&#128300;</span> Waveplates &amp; Polarizers</a>
                    </div>
                </li>
                    <li><a href="/applications.html" class="nav-link" data-i18n="navApplications">Applications</a></li>
                    <li><a href="/custom-optics.html" class="nav-link" data-i18n="navCustomOptics">Custom Optics</a></li>
                    <li><a href="/engineering.html" class="nav-link" data-i18n="navEngineering">Engineering</a></li>
                    <li class="nav-dropdown">
                        <a href="#" class="nav-link" data-i18n="navResources">Resources &#9662;</a>
                        <div class="dropdown-menu">
                            <a href="/knowledge-center/" class="dropdown-item" data-i18n="navKnowledgeCenter"><span class="dropdown-icon">&#128218;</span> Knowledge Center</a>
                            <a href="/application-notes/" class="dropdown-item" data-i18n="navApplicationNotes"><span class="dropdown-icon">&#128196;</span> Application Notes</a>
                            <a href="/materials.html" class="dropdown-item" data-i18n="navMaterials"><span class="dropdown-icon">&#129514;</span> Materials Database</a>
                            <a href="/coatings/" class="dropdown-item" data-i18n="navCoatings"><span class="dropdown-icon">&#128300;</span> Coating Database</a>
                            <a href="/ai-optical-assistant.html" class="dropdown-item" data-i18n="navAIAssistant"><span class="dropdown-icon">&#129302;</span> AI Optical Assistant</a>
                            <a href="/faq.html" class="dropdown-item" data-i18n="navFAQ"><span class="dropdown-icon">&#10067;</span> FAQ</a>
                            <a href="/blog.html" class="dropdown-item" data-i18n="navBlog"><span class="dropdown-icon">&#128221;</span> Blog</a>
                        </div>
                    </li>
                    <li class="nav-dropdown">
                        <a href="#" class="nav-link" data-i18n="navAboutDropdown">About &#9662;</a>
                        <div class="dropdown-menu">
                            <a href="/about.html" class="dropdown-item" data-i18n="navAboutPhotonEdge"><span class="dropdown-icon">&#127970;</span> About PhotonEdge</a>
                            <a href="/quality-assurance.html" class="dropdown-item" data-i18n="navQualityDoc"><span class="dropdown-icon">&#9989;</span> Quality &amp; Documentation</a>
                            <a href="/case-studies.html" class="dropdown-item" data-i18n="navCaseStudies"><span class="dropdown-icon">&#128203;</span> Case Studies</a>
                        </div>
                    </li>
                </ul>
                <div class="lang-switcher">
                    <button class="lang-btn notranslate active">EN</button>
                    <a href="/zh/index.html" class="lang-btn notranslate" style="text-decoration:none;">中文</a>
                </div>
                <a href="/contact.html" class="btn btn-primary nav-cta-btn" data-i18n="navCTA" style="padding:8px 20px;border-radius:6px;font-size:14px;color:white;text-decoration:none;margin-left:8px;">Request a Quote</a>
            </nav>
        </div>
    </header>
    
    <div class="request-quote-float">
        <a href="/contact.html" class="quote-btn">
            <span class="quote-icon">&#9993;</span>
            <span data-i18n="navCTA">Request a Quote</span>
        </a>
    </div>

<!-- ============ SECTION 1: HERO ============ -->
<section class="hero v90-hero" style="padding:160px 0 100px;">
    <div class="container">
        <div style="max-width:800px;">
            <h1 data-i18n="v142HeroTitle" style="font-size:44px;font-weight:800;color:white;margin-bottom:16px;letter-spacing:-1px;line-height:1.25;">Precision Optical Components, Materials &amp; Engineering Resources</h1>
            <p data-i18n="v142HeroSubtitle" style="font-size:20px;color:rgba(255,255,255,0.92);margin-bottom:20px;font-weight:500;">A sourcing and specification platform for engineers and procurement teams.</p>
            <p data-i18n="v142HeroDesc" style="font-size:16px;color:rgba(255,255,255,0.75);line-height:1.8;margin-bottom:36px;max-width:680px;">PhotonEdge connects optical components, materials databases and coating resources in one platform. Whether you know exactly what you need or are still defining specifications, you can find relevant technical information and submit a request for quotation.</p>
            <div style="display:flex;gap:16px;flex-wrap:wrap;">
                <a href="/contact.html" class="btn" style="background:white;color:#2563eb;padding:14px 28px;border-radius:8px;font-weight:600;font-size:16px;" data-i18n="v142HeroCTA1">Request a Quote</a>
                <a href="/ai-optical-assistant.html" class="btn" style="background:transparent;border:2px solid rgba(255,255,255,0.5);color:white;padding:14px 28px;border-radius:8px;font-weight:600;font-size:16px;" data-i18n="v142HeroCTA2">Talk to an Engineer</a>
                <a href="/engineering.html" class="btn" style="background:transparent;border:2px solid rgba(255,255,255,0.5);color:white;padding:14px 28px;border-radius:8px;font-weight:600;font-size:16px;" data-i18n="v142HeroCTA3">Read Specification Guide</a>
            </div>
        </div>
    </div>
</section>

<!-- ============ SECTION 2: WHAT WE PROVIDE ============ -->
<section style="padding:80px 0;background:#f8fafc;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;" data-i18n="v142S2Title">What We Provide</h2>
            <p style="color:#64748b;max-width:700px;margin:0 auto;font-size:16px;line-height:1.7;" data-i18n="v142S2Subtitle">PhotonEdge is an engineering-oriented platform for sourcing and specifying optical components.</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:24px;max-width:1100px;margin:0 auto;">
            <a href="/custom-optics.html" style="text-decoration:none;padding:32px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128300;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S2Card1Title">Custom Optics</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S2Card1Desc">Custom optical components based on your drawings and specifications. Material selection, coating requirements and manufacturing process review.</p>
            </a>
            <a href="/products.html" style="text-decoration:none;padding:32px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128269;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S2Card2Title">Standard Components</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S2Card2Desc">Catalog optical components including lenses, mirrors, windows, filters, beamsplitters and prisms with defined specifications.</p>
            </a>
            <a href="/engineering.html" style="text-decoration:none;padding:32px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128203;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S2Card3Title">Application Review</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S2Card3Desc">Help reviewing material suitability, coating selection and specification requirements before manufacturing.</p>
            </a>
            <a href="/materials.html" style="text-decoration:none;padding:32px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128214;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S2Card4Title">Technical Documentation</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S2Card4Desc">Material data sheets, coating specifications and application references for optical component selection.</p>
            </a>
        </div>
    </div>
</section>

<!-- ============ SECTION 3: WHY PHOTONEDGE ============ -->
<section style="padding:80px 0;background:white;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;" data-i18n="v142S3Title">Why PhotonEdge</h2>
            <p style="color:#64748b;max-width:700px;margin:0 auto;font-size:16px;line-height:1.7;" data-i18n="v142S3Subtitle">We focus on practical value for optical component sourcing and specification.</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:24px;max-width:1100px;margin:0 auto;">
            <div style="padding:32px;background:#f8fafc;border-radius:12px;border:1px solid #e2e8f0;">
                <div style="font-size:28px;margin-bottom:12px;">&#9989;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S3Card1Title">Qualified Supply</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S3Card1Desc">Manufacturing resources are selected and qualified for optical component production. Each project is matched to appropriate manufacturing capability.</p>
            </div>
            <div style="padding:32px;background:#f8fafc;border-radius:12px;border:1px solid #e2e8f0;">
                <div style="font-size:28px;margin-bottom:12px;">&#128270;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S3Card2Title">Engineering Review</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S3Card2Desc">Every inquiry receives technical review. We check material suitability, coating feasibility and specification completeness before confirming production.</p>
            </div>
            <div style="padding:32px;background:#f8fafc;border-radius:12px;border:1px solid #e2e8f0;">
                <div style="font-size:28px;margin-bottom:12px;">&#127919;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S3Card3Title">Application Matching</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S3Card3Desc">Components are recommended based on application requirements including wavelength, power, environment and system integration.</p>
            </div>
            <div style="padding:32px;background:#f8fafc;border-radius:12px;border:1px solid #e2e8f0;">
                <div style="font-size:28px;margin-bottom:12px;">&#128196;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S3Card4Title">Documentation Support</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S3Card4Desc">Inspection reports, material certificates and coating specifications are provided according to project requirements.</p>
            </div>
        </div>
    </div>
</section>

<!-- ============ SECTION 4: APPLICATIONS ============ -->
<section style="padding:80px 0;background:#f8fafc;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;" data-i18n="v123S4Title">Optical Solutions for Demanding Applications</h2>
            <p style="color:#64748b;max-width:700px;margin:0 auto;font-size:16px;line-height:1.7;" data-i18n="v123S4Subtitle">Different applications require different optical materials, coatings and specifications. We help customers select and source the right components for their systems.</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;max-width:1100px;margin:0 auto;">
            <a href="/applications/laser-optics/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v123App1Title">Laser Systems</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v123App1Desc">Laser windows, mirrors, lenses, beamsplitters and other components for industrial and scientific laser systems.</p>
            </a>
            <a href="/applications/research-laboratory/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v123App2Title">Scientific Research</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v123App2Desc">Custom optics for spectroscopy, microscopy, laboratory instruments and research systems.</p>
            </a>
            <a href="/applications/semiconductor-inspection/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v123App3Title">Semiconductor Equipment</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v123App3Desc">Optical components for inspection, measurement and precision equipment.</p>
            </a>
            <a href="/applications/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v123App4Title">Imaging &amp; Vision</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v123App4Desc">Lenses, windows, filters and optical assemblies for imaging and machine vision.</p>
            </a>
            <a href="/applications/medical-imaging/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v123App5Title">Medical &amp; Life Science</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v123App5Desc">Optical components for imaging, diagnostic and analytical equipment.</p>
            </a>
            <a href="/applications/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v123App6Title">Industrial Optics</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v123App6Desc">Custom optical components for sensing, measurement and industrial systems.</p>
            </a>
        </div>
        <div style="text-align:center;margin-top:40px;">
            <a href="/applications.html" style="color:#2563eb;font-weight:600;text-decoration:none;font-size:15px;" data-i18n="v123ExploreApps">Explore Applications &rarr;</a>
        </div>
    </div>
</section>

<!-- ============ SECTION 5: CORE PRODUCTS ============ -->
<section style="padding:80px 0;background:white;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;" data-i18n="v142S5Title">Core Product Categories</h2>
            <p style="color:#64748b;max-width:600px;margin:0 auto;font-size:16px;" data-i18n="v142S5Subtitle">Standard and custom optical components across seven categories.</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;max-width:1100px;margin:0 auto;">
            <a href="/products.html?category=Optical+Lenses" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;" data-i18n="v142S5Prod1">Optical Lenses</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;" data-i18n="v142S5Prod1Desc">Spherical, aspheric, cylindrical, achromatic and custom lenses for UV, visible and infrared applications.</p>
            </a>
            <a href="/products.html?category=Optical+Windows" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;" data-i18n="v142S5Prod2">Optical Windows</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;" data-i18n="v142S5Prod2Desc">Flat and curved windows in fused silica, BK7, sapphire, CaF&#8322;, ZnSe and other optical materials.</p>
            </a>
            <a href="/products.html?category=Optical+Mirrors" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;" data-i18n="v142S5Prod3">Optical Mirrors</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;" data-i18n="v142S5Prod3Desc">Flat, curved and dichroic mirrors with dielectric or metallic coatings.</p>
            </a>
            <a href="/products.html?category=Optical+Filters" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;" data-i18n="v142S5Prod4">Optical Filters</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;" data-i18n="v142S5Prod4Desc">Bandpass, longpass, shortpass, neutral density and dichroic filters.</p>
            </a>
            <a href="/products.html?category=Beamsplitters" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;" data-i18n="v142S5Prod5">Beamsplitters</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;" data-i18n="v142S5Prod5Desc">Plate and cube beamsplitters for beam splitting and combining.</p>
            </a>
            <a href="/products.html?category=Optical+Prisms" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;" data-i18n="v142S5Prod6">Optical Prisms</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;" data-i18n="v142S5Prod6Desc">Beam steering, dispersion and polarization prisms.</p>
            </a>
            <a href="/products.html?category=Waveplates+%26+Polarizers" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;" data-i18n="v142S5Prod7">Waveplates &amp; Polarizers</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;" data-i18n="v142S5Prod7Desc">Zero-order, multi-order waveplates and polarizing beamsplitters.</p>
            </a>
        </div>
        <div style="text-align:center;margin-top:40px;">
            <a href="/products.html" style="display:inline-block;background:#2563eb;color:white;padding:12px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:15px;" data-i18n="v142ViewAllProducts">View All Products &rarr;</a>
        </div>
    </div>
</section>

<!-- ============ SECTION 6: ENGINEERING RESOURCES ============ -->
<section style="padding:80px 0;background:#f8fafc;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;" data-i18n="v142S6Title">Engineering Resources</h2>
            <p style="color:#64748b;max-width:700px;margin:0 auto;font-size:16px;line-height:1.7;" data-i18n="v142S6Subtitle">Technical references for optical component selection and specification.</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:24px;max-width:1100px;margin:0 auto;">
            <a href="/materials.html" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#129514;</div>
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S6Res1">Materials Database</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S6Res1Desc">Optical, thermal and mechanical properties of common optical materials. Use this database to compare materials and understand application suitability.</p>
            </a>
            <a href="/coatings/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128300;</div>
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S6Res2">Coating Database</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S6Res2Desc">Optical coating types, specifications and application references. Understand coating selection for your wavelength and power requirements.</p>
            </a>
            <a href="/applications.html" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128218;</div>
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S6Res3">Application Guides</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S6Res3Desc">Application-specific references for laser systems, scientific research, semiconductor equipment, imaging and medical optics.</p>
            </a>
            <a href="/ai-optical-assistant.html" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#129302;</div>
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S6Res4">AI Optical Assistant</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S6Res4Desc">Get preliminary optical component recommendations and material suggestions based on your application requirements.</p>
            </a>
        </div>
        <div style="text-align:center;margin-top:40px;">
            <a href="/knowledge-center/" style="color:#2563eb;font-weight:600;text-decoration:none;font-size:15px;" data-i18n="v142ExploreResources">Explore All Resources &rarr;</a>
        </div>
    </div>
</section>

<!-- ============ SECTION 7: CUSTOM OPTICS CAPABILITY ============ -->
<section style="padding:80px 0;background:white;">
    <div class="container" style="max-width:900px;">
        <div style="text-align:center;margin-bottom:40px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;" data-i18n="v142S7Title">Custom Optics</h2>
            <p style="color:#64748b;max-width:700px;margin:0 auto;font-size:16px;line-height:1.7;" data-i18n="v142S7Subtitle">If your application requires non-standard optical components, PhotonEdge can help coordinate custom manufacturing.</p>
        </div>
        <div style="background:#f8fafc;border-radius:12px;border:1px solid #e2e8f0;padding:40px;">
            <p style="color:#374151;font-size:15px;line-height:1.8;margin-bottom:20px;" data-i18n="v142S7Desc1">Custom optical components are manufactured based on your drawings or specifications. We review your requirements including material, dimensions, surface quality, coating and quantity, then match appropriate manufacturing resources.</p>
            <p style="color:#374151;font-size:15px;line-height:1.8;margin-bottom:20px;" data-i18n="v142S7Desc2">Before production begins, we confirm:</p>
            <ul style="color:#374151;font-size:15px;line-height:2;margin:0 0 24px 20px;padding:0;">
                <li data-i18n="v142S7Item1">Material and coating feasibility</li>
                <li data-i18n="v142S7Item2">Manufacturing process route</li>
                <li data-i18n="v142S7Item3">Inspection method and acceptance criteria</li>
                <li data-i18n="v142S7Item4">Documentation requirements</li>
            </ul>
            <div style="text-align:center;">
                <a href="/contact.html" style="display:inline-block;background:#2563eb;color:white;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:16px;" data-i18n="v142S7CTA">Discuss Your Custom Requirements &rarr;</a>
            </div>
        </div>
    </div>
</section>

<!-- ============ SECTION 8: FINAL CTA ============ -->
<section style="padding:80px 0;background:linear-gradient(135deg,#1e3a5f 0%,#2563eb 100%);">
    <div class="container" style="text-align:center;">
        <h2 style="font-size:32px;font-weight:700;color:white;margin-bottom:16px;" data-i18n="v142FinalTitle">Have an Optical Requirement?</h2>
        <p style="color:rgba(255,255,255,0.85);font-size:16px;line-height:1.8;max-width:650px;margin:0 auto 32px;" data-i18n="v142FinalDesc">Whether you have a complete drawing or just an application description, send us what you have. We will help identify the right component and manufacturing approach.</p>
        <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
            <a href="/contact.html" style="display:inline-block;background:white;color:#2563eb;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:16px;" data-i18n="v142FinalCTA1">Request a Quote</a>
            <a href="/contact.html" style="display:inline-block;background:transparent;border:2px solid rgba(255,255,255,0.5);color:white;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:16px;" data-i18n="v142FinalCTA2">Upload Your Drawing</a>
            <a href="/ai-optical-assistant.html" style="display:inline-block;background:transparent;border:2px solid rgba(255,255,255,0.5);color:white;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:16px;" data-i18n="v142FinalCTA3">Ask AI Assistant</a>
        </div>
    </div>
</section>

''' + footer + '''

<!-- WhatsApp Floating Button -->
<a href="https://wa.me/8613693009175" target="_blank" class="whatsapp-float" title="Chat with us on WhatsApp">
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
    </svg>
    <div class="whatsapp-tooltip" data-i18n="whatsappTooltip">Chat with us</div>
</a>

<script src="/js/blog-data.js"></script>
<script src="/js/translations.js"></script>
<script src="/js/products-data.js"></script>
<script src="/js/ai-selector.js"></script>
<script src="/js/compare.js"></script>
<script src="/js/cart.js"></script>
<script src="/js/search.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        if (typeof updatePageTranslations === 'function') updatePageTranslations();
        var lang = getCurrentLang();
        var buttons = document.querySelectorAll('.lang-btn');
        for (var i = 0; i < buttons.length; i++) {
            buttons[i].classList.remove('active');
            if (buttons[i].textContent.toLowerCase() === (lang === 'en' ? 'en' : 'zh')) {
                buttons[i].classList.add('active');
            }
        }
    });
</script>
<script>
function toggleMobileMenu() {
    var navList = document.querySelector('.nav-list');
    if (navList) {
        navList.classList.toggle('active');
    }
}
</script>
<script src="/js/chatbot.js"></script>
</body>
</html>
'''

with open(os.path.join(BASE, 'index.html'), 'w') as f:
    f.write(new_index)

print("New index.html written. Lines: %d" % new_index.count('\n'))
