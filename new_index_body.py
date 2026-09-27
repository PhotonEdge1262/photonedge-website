# -*- coding: utf-8 -*-
"""Generate the new V142 index.html body sections"""

# The new header (with updated nav including AI Optical Assistant)
HEADER = '''<!DOCTYPE html>
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
    <meta name="keywords" content="precision optical components, optical materials database, coating specifications, custom optics, optical sourcing, optical engineering resources, PhotonEdge">
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
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "Beijing",
        "addressCountry": "CN"
    },
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
'''

# Section 1: Hero
S1_HERO = '''
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
'''

# Section 2: What We Provide
S2_PROVIDE = '''
<!-- ============ SECTION 2: WHAT WE PROVIDE ============ -->
<section style="padding:80px 0;background:#f8fafc;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;" data-i18n="v142S2Title">What We Provide</h2>
            <p style="color:#64748b;max-width:700px;margin:0 auto;font-size:16px;line-height:1.7;" data-i18n="v142S2Subtitle">PhotonEdge is an engineering-oriented platform for sourcing and specifying optical components.</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:24px;max-width:1100px;margin:0 auto;">
            <a href="/custom-optics.html" style="text-decoration:none;padding:32px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128300;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S2Card1Title">Custom Optics</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S2Card1Desc">Custom optical components based on your drawings and specifications. Material selection, coating requirements and manufacturing process review.</p>
            </a>
            <a href="/products.html" style="text-decoration:none;padding:32px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128269;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S2Card2Title">Standard Components</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S2Card2Desc">Catalog optical components including lenses, mirrors, windows, filters, beamsplitters and prisms with defined specifications.</p>
            </a>
            <a href="/engineering.html" style="text-decoration:none;padding:32px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128203;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S2Card3Title">Application Review</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S2Card3Desc">Help reviewing material suitability, coating selection and specification requirements before manufacturing.</p>
            </a>
            <a href="/materials.html" style="text-decoration:none;padding:32px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128214;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v142S2Card4Title">Technical Documentation</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v142S2Card4Desc">Material data sheets, coating specifications and application references for optical component selection.</p>
            </a>
        </div>
    </div>
</section>
'''

# Section 3: Why PhotonEdge (NEW)
S3_WHY = '''
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
'''

# Section 4: Applications (kept from original, with links)
S4_APPS = '''
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
'''

print("Section variables defined.")
