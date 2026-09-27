# -*- coding: utf-8 -*-
"""Generate V142 Chinese homepage zh/index.html"""
import os

BASE = '/tmp/v142-build'

# Read old zh/index.html to extract footer and scripts
with open(os.path.join(BASE, 'zh/index.html'), 'r') as f:
    old_zh = f.read()

footer_start = old_zh.find('    <footer class="footer">')
footer_end = old_zh.find('</footer>') + len('</footer>')
footer = old_zh[footer_start:footer_end]

scripts_start = old_zh.find('\n<!-- WhatsApp')
scripts = old_zh[scripts_start:] if scripts_start > 0 else ''

new_zh = u'''<!DOCTYPE html>
<html lang="zh">
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="dns-prefetch" href="https://www.google-analytics.com">
    <meta charset="UTF-8">
    <link rel="icon" type="image/png" sizes="32x32" href="https://photonedgeoptics.com/images/favicon-32.png">
    <link rel="icon" type="image/svg+xml" href="https://photonedgeoptics.com/images/favicon.svg">
    <link rel="apple-touch-icon" sizes="180x180" href="https://photonedgeoptics.com/images/apple-touch-icon.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>\u6052\u9f0e\u5149\u79d1\u6280 | \u7cbe\u5bc6\u5149\u5b66\u5143\u4ef6\u3001\u6750\u6599\u4e0e\u5de5\u7a0b\u8d44\u6e90\u5e73\u53f0</title>
    <meta name="description" content="PhotonEdge\u6052\u9f0e\u5149\u79d1\u6280\uff0c\u9762\u5411\u5de5\u7a0b\u5e08\u548c\u91c7\u8d2d\u56e2\u961f\u7684\u5149\u5b66\u5143\u4ef6\u9009\u578b\u4e0e\u89c4\u683c\u5e73\u53f0\u3002\u63d0\u4f9b\u5149\u5b66\u5143\u4ef6\u3001\u6750\u6599\u6570\u636e\u5e93\u3001\u9540\u819c\u8d44\u6e90\u548c\u5de5\u7a0b\u6280\u672f\u652f\u6301\u3002">
    <meta name="keywords" content="\u5149\u5b66\u5143\u4ef6,\u5149\u5b66\u6750\u6599,\u5149\u5b66\u9540\u819c,\u5b9a\u5236\u5149\u5b66,\u5149\u5b66\u900f\u955c,\u5149\u5b66\u7a97\u53e3,\u53cd\u5c04\u955c,\u6ee4\u5149\u7247,\u5206\u675f\u955c,\u68f1\u955c,\u6052\u9f0e\u5149,PhotonEdge">
    <meta property="og:title" content="\u6052\u9f0e\u5149\u79d1\u6280 | \u7cbe\u5bc6\u5149\u5b66\u5143\u4ef6\u3001\u6750\u6599\u4e0e\u5de5\u7a0b\u8d44\u6e90\u5e73\u53f0">
    <meta property="og:description" content="\u9762\u5411\u5de5\u7a0b\u5e08\u548c\u91c7\u8d2d\u56e2\u961f\u7684\u5149\u5b66\u5143\u4ef6\u9009\u578b\u4e0e\u89c4\u683c\u5e73\u53f0\u3002">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://photonedgeoptics.com/zh/">
    <meta property="og:image" content="https://photonedgeoptics.com/images/logo.webp">
    <meta property="og:site_name" content="\u6052\u9f0e\u5149\u79d1\u6280">
    <link rel="canonical" href="https://photonedgeoptics.com/zh/">
    <link rel="stylesheet" href="../css/style.css">
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
    <meta name="twitter:title" content="\u6052\u9f0e\u5149\u79d1\u6280 | \u7cbe\u5bc6\u5149\u5b66\u5143\u4ef6\u3001\u6750\u6599\u4e0e\u5de5\u7a0b\u8d44\u6e90\u5e73\u53f0">
    <meta name="twitter:description" content="\u9762\u5411\u5de5\u7a0b\u5e08\u548c\u91c7\u8d2d\u56e2\u961f\u7684\u5149\u5b66\u5143\u4ef6\u9009\u578b\u4e0e\u89c4\u683c\u5e73\u53f0\u3002">
    <link rel="stylesheet" href="../css/chatbot.css">
    <script>
        (function(){
            var bp = document.createElement('script');
            var curProtocol = window.location.protocol.split(':')[0];
            if (curProtocol === 'https') {
                bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
            } else {
                bp.src = 'https://push.zhangzifan.com/linksubmit/push.js';
            }
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(bp, s);
        })();
    </script>
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "PhotonEdge Optics",
    "url": "https://photonedgeoptics.com",
    "description": "\u9762\u5411\u5de5\u7a0b\u5e08\u548c\u91c7\u8d2d\u56e2\u961f\u7684\u5149\u5b66\u5143\u4ef6\u3001\u6750\u6599\u4e0e\u5de5\u7a0b\u8d44\u6e90\u5e73\u53f0\u3002",
    "address": {"@type": "PostalAddress", "addressLocality": "Beijing", "addressCountry": "CN"},
    "email": "sales@photonedgeoptics.com"
}
    </script>
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="/zh/" class="logo">
    <picture>
        <source srcset="/images/logo.webp" type="image/webp">
        <img src="https://photonedgeoptics.com/logo.png" alt="\u6052\u9f0e\u5149\u79d1\u6280" width="160" height="40">
    </picture>
</a>
            <nav class="nav">
                <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">&#9776;</button>
                <ul class="nav-list">
                    <li class="nav-dropdown">
                    <a href="/zh/products.html" class="nav-link">\u4ea7\u54c1 &#9662;</a>
                    <div class="dropdown-menu">
                        <a href="/products.html?category=Optical+Lenses" class="dropdown-item"><span class="dropdown-icon">&#128269;</span> \u5149\u5b66\u900f\u955c</a>
                        <a href="/products.html?category=Optical+Windows" class="dropdown-item"><span class="dropdown-icon">&#129695;</span> \u5149\u5b66\u7a97\u53e3</a>
                        <a href="/products.html?category=Optical+Mirrors" class="dropdown-item"><span class="dropdown-icon">&#129694;</span> \u5149\u5b66\u53cd\u5c04\u955c</a>
                        <a href="/products.html?category=Optical+Filters" class="dropdown-item"><span class="dropdown-icon">&#127752;</span> \u5149\u5b66\u6ee4\u5149\u7247</a>
                        <a href="/products.html?category=Beamsplitters" class="dropdown-item"><span class="dropdown-icon">&#9671;</span> \u5206\u675f\u955c</a>
                        <a href="/products.html?category=Optical+Prisms" class="dropdown-item"><span class="dropdown-icon">&#128142;</span> \u5149\u5b66\u68f1\u955c</a>
                        <a href="/products.html?category=Waveplates+%26+Polarizers" class="dropdown-item"><span class="dropdown-icon">&#128300;</span> \u6ce2\u7247\u4e0e\u504f\u632f\u5668</a>
                    </div>
                </li>
                    <li><a href="/zh/applications.html" class="nav-link">\u5e94\u7528\u9886\u57df</a></li>
                    <li><a href="/custom-optics.html" class="nav-link">\u5b9a\u5236\u5149\u5b66</a></li>
                    <li><a href="/engineering.html" class="nav-link">\u5de5\u7a0b\u670d\u52a1</a></li>
                    <li class="nav-dropdown">
                        <a href="#" class="nav-link">\u8d44\u6e90 &#9662;</a>
                        <div class="dropdown-menu">
                            <a href="/knowledge-center/" class="dropdown-item"><span class="dropdown-icon">&#128218;</span> \u77e5\u8bc6\u4e2d\u5fc3</a>
                            <a href="/application-notes/" class="dropdown-item"><span class="dropdown-icon">&#128196;</span> \u5e94\u7528\u7b14\u8bb0</a>
                            <a href="/materials.html" class="dropdown-item"><span class="dropdown-icon">&#129514;</span> \u6750\u6599\u6570\u636e\u5e93</a>
                            <a href="/coatings/" class="dropdown-item"><span class="dropdown-icon">&#128300;</span> \u9540\u819c\u6570\u636e\u5e93</a>
                            <a href="/ai-optical-assistant.html" class="dropdown-item"><span class="dropdown-icon">&#129302;</span> AI\u5149\u5b66\u52a9\u624b</a>
                            <a href="/zh/faq.html" class="dropdown-item"><span class="dropdown-icon">&#10067;</span> \u5e38\u89c1\u95ee\u9898</a>
                            <a href="/blog.html" class="dropdown-item"><span class="dropdown-icon">&#128221;</span> \u535a\u5ba2</a>
                        </div>
                    </li>
                    <li class="nav-dropdown">
                        <a href="#" class="nav-link">\u5173\u4e8e &#9662;</a>
                        <div class="dropdown-menu">
                            <a href="/about.html" class="dropdown-item"><span class="dropdown-icon">&#127970;</span> \u5173\u4e8e\u6052\u9f0e\u5149</a>
                            <a href="/quality-assurance.html" class="dropdown-item"><span class="dropdown-icon">&#9989;</span> \u8d28\u91cf\u4e0e\u6587\u6863</a>
                            <a href="/zh/case-studies.html" class="dropdown-item"><span class="dropdown-icon">&#128203;</span> \u6848\u4f8b</a>
                        </div>
                    </li>
                </ul>
                <div class="lang-switcher">
                    <a href="/index.html" class="lang-btn notranslate" style="text-decoration:none;">EN</a>
                    <button class="lang-btn notranslate active">\u4e2d\u6587</button>
                </div>
                <a href="/zh/contact.html" class="btn btn-primary nav-cta-btn" style="padding:8px 20px;border-radius:6px;font-size:14px;color:white;text-decoration:none;margin-left:8px;">\u8bf7\u6c42\u62a5\u4ef7</a>
            </nav>
        </div>
    </header>

<!-- ============ S1: HERO ============ -->
<section class="hero v90-hero" style="padding:160px 0 100px;">
    <div class="container">
        <div style="max-width:800px;">
            <h1 style="font-size:44px;font-weight:800;color:white;margin-bottom:16px;letter-spacing:-1px;line-height:1.25;">\u7cbe\u5bc6\u5149\u5b66\u5143\u4ef6\u3001\u6750\u6599\u4e0e\u5de5\u7a0b\u8d44\u6e90</h1>
            <p style="font-size:20px;color:rgba(255,255,255,0.92);margin-bottom:20px;font-weight:500;">\u9762\u5411\u5de5\u7a0b\u5e08\u548c\u91c7\u8d2d\u56e2\u961f\u7684\u5149\u5b66\u5143\u4ef6\u9009\u578b\u4e0e\u89c4\u683c\u5e73\u53f0\u3002</p>
            <p style="font-size:16px;color:rgba(255,255,255,0.75);line-height:1.8;margin-bottom:36px;max-width:680px;">PhotonEdge\u5c06\u5149\u5b66\u5143\u4ef6\u3001\u6750\u6599\u6570\u636e\u5e93\u548c\u9540\u819c\u8d44\u6e90\u96c6\u6210\u5728\u4e00\u4e2a\u5e73\u53f0\u4e0a\u3002\u65e0\u8bba\u60a8\u662f\u660e\u786e\u9700\u6c42\u8fd8\u662f\u6b63\u5728\u786e\u5b9a\u89c4\u683c\uff0c\u90fd\u53ef\u4ee5\u627e\u5230\u76f8\u5173\u6280\u672f\u4fe1\u606f\u5e76\u63d0\u4ea4\u62a5\u4ef7\u8bf7\u6c42\u3002</p>
            <div style="display:flex;gap:16px;flex-wrap:wrap;">
                <a href="/zh/contact.html" class="btn" style="background:white;color:#2563eb;padding:14px 28px;border-radius:8px;font-weight:600;font-size:16px;">\u8bf7\u6c42\u62a5\u4ef7</a>
                <a href="/ai-optical-assistant.html" class="btn" style="background:transparent;border:2px solid rgba(255,255,255,0.5);color:white;padding:14px 28px;border-radius:8px;font-weight:600;font-size:16px;">\u4e0e\u5de5\u7a0b\u5e08\u4ea4\u6d41</a>
                <a href="/engineering.html" class="btn" style="background:transparent;border:2px solid rgba(255,255,255,0.5);color:white;padding:14px 28px;border-radius:8px;font-weight:600;font-size:16px;">\u9605\u8bfb\u89c4\u683c\u6307\u5357</a>
            </div>
        </div>
    </div>
</section>

<!-- ============ S2: WHAT WE PROVIDE ============ -->
<section style="padding:80px 0;background:#f8fafc;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;">\u6211\u4eec\u63d0\u4f9b\u4ec0\u4e48</h2>
            <p style="color:#64748b;max-width:700px;margin:0 auto;font-size:16px;line-height:1.7;">PhotonEdge\u662f\u4e00\u4e2a\u9762\u5411\u5de5\u7a0b\u7684\u5149\u5b66\u5143\u4ef6\u9009\u578b\u4e0e\u89c4\u683c\u5e73\u53f0\u3002</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:24px;max-width:1100px;margin:0 auto;">
            <a href="/custom-optics.html" style="text-decoration:none;padding:32px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128300;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u5b9a\u5236\u5149\u5b66</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u57fa\u4e8e\u60a8\u7684\u56fe\u7eb8\u548c\u89c4\u683c\u7684\u5b9a\u5236\u5149\u5b66\u5143\u4ef6\u3002\u6750\u6599\u9009\u62e9\u3001\u9540\u819c\u8981\u6c42\u548c\u5236\u9020\u5de5\u827a\u5ba1\u67e5\u3002</p>
            </a>
            <a href="/products.html" style="text-decoration:none;padding:32px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128269;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u6807\u51c6\u5143\u4ef6</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u76ee\u5f55\u5149\u5b66\u5143\u4ef6\uff0c\u5305\u62ec\u900f\u955c\u3001\u53cd\u5c04\u955c\u3001\u7a97\u53e3\u3001\u6ee4\u5149\u7247\u3001\u5206\u675f\u955c\u548c\u68f1\u955c\uff0c\u5177\u6709\u660e\u786e\u89c4\u683c\u3002</p>
            </a>
            <a href="/engineering.html" style="text-decoration:none;padding:32px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128203;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u5e94\u7528\u5ba1\u67e5</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u5728\u5236\u9020\u4e4b\u524d\u5e2e\u52a9\u5ba1\u67e5\u6750\u6599\u9002\u7528\u6027\u3001\u9540\u819c\u9009\u62e9\u548c\u89c4\u683c\u8981\u6c42\u3002</p>
            </a>
            <a href="/materials.html" style="text-decoration:none;padding:32px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128214;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u6280\u672f\u6587\u6863</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u6750\u6599\u6570\u636e\u8868\u3001\u9540\u819c\u89c4\u683c\u548c\u5e94\u7528\u53c2\u8003\uff0c\u7528\u4e8e\u5149\u5b66\u5143\u4ef6\u9009\u578b\u3002</p>
            </a>
        </div>
    </div>
</section>

<!-- ============ S3: WHY PHOTONEDGE ============ -->
<section style="padding:80px 0;background:white;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;">\u4e3a\u4ec0\u4e48\u9009\u62e9\u6052\u9f0e\u5149</h2>
            <p style="color:#64748b;max-width:700px;margin:0 auto;font-size:16px;line-height:1.7;">\u6211\u4eec\u4e13\u6ce8\u4e8e\u5149\u5b66\u5143\u4ef6\u91c7\u8d2d\u548c\u89c4\u683c\u7684\u5b9e\u9645\u4ef7\u503c\u3002</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:24px;max-width:1100px;margin:0 auto;">
            <div style="padding:32px;background:#f8fafc;border-radius:12px;border:1px solid #e2e8f0;">
                <div style="font-size:28px;margin-bottom:12px;">&#9989;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u5408\u683c\u4f9b\u5e94</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u5236\u9020\u8d44\u6e90\u7ecf\u8fc7\u5149\u5b66\u5143\u4ef6\u751f\u4ea7\u7684\u7b5b\u9009\u548c\u8d44\u8d28\u8ba4\u5b9a\u3002\u6bcf\u4e2a\u9879\u76ee\u90fd\u5339\u914d\u5408\u9002\u7684\u5236\u9020\u80fd\u529b\u3002</p>
            </div>
            <div style="padding:32px;background:#f8fafc;border-radius:12px;border:1px solid #e2e8f0;">
                <div style="font-size:28px;margin-bottom:12px;">&#128270;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u5de5\u7a0b\u5ba1\u67e5</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u6bcf\u4e2a\u8be2\u4ef7\u90fd\u4f1a\u63a5\u53d7\u6280\u672f\u5ba1\u67e5\u3002\u6211\u4eec\u5728\u786e\u8ba4\u751f\u4ea7\u524d\u68c0\u67e5\u6750\u6599\u9002\u7528\u6027\u3001\u9540\u819c\u53ef\u884c\u6027\u548c\u89c4\u683c\u5b8c\u6574\u6027\u3002</p>
            </div>
            <div style="padding:32px;background:#f8fafc;border-radius:12px;border:1px solid #e2e8f0;">
                <div style="font-size:28px;margin-bottom:12px;">&#127919;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u5e94\u7528\u5339\u914d</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u6839\u636e\u5e94\u7528\u8981\u6c42\u63a8\u8350\u5143\u4ef6\uff0c\u5305\u62ec\u6ce2\u957f\u3001\u529f\u7387\u3001\u73af\u5883\u548c\u7cfb\u7edf\u96c6\u6210\u3002</p>
            </div>
            <div style="padding:32px;background:#f8fafc;border-radius:12px;border:1px solid #e2e8f0;">
                <div style="font-size:28px;margin-bottom:12px;">&#128196;</div>
                <h3 style="font-size:18px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u6587\u6863\u652f\u6301</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u6839\u636e\u9879\u76ee\u8981\u6c42\u63d0\u4f9b\u68c0\u6d4b\u62a5\u544a\u3001\u6750\u6599\u8bc1\u4e66\u548c\u9540\u819c\u89c4\u683c\u3002</p>
            </div>
        </div>
    </div>
</section>

<!-- ============ S4: APPLICATIONS ============ -->
<section style="padding:80px 0;background:#f8fafc;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;">\u5149\u5b66\u65b9\u6848\u670d\u52a1\u4e8e\u5404\u7c7b\u5e94\u7528\u9886\u57df</h2>
            <p style="color:#64748b;max-width:700px;margin:0 auto;font-size:16px;line-height:1.7;">\u4e0d\u540c\u7684\u5e94\u7528\u9700\u8981\u4e0d\u540c\u7684\u5149\u5b66\u6750\u6599\u3001\u9540\u819c\u548c\u89c4\u683c\u3002\u6211\u4eec\u5e2e\u52a9\u5ba2\u6237\u4e3a\u5176\u7cfb\u7edf\u9009\u62e9\u548c\u91c7\u8d2d\u5408\u9002\u7684\u5143\u4ef6\u3002</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;max-width:1100px;margin:0 auto;">
            <a href="/applications/laser-optics/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u6fc0\u5149\u7cfb\u7edf</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u6fc0\u5149\u7a97\u53e3\u3001\u53cd\u5c04\u955c\u3001\u900f\u955c\u3001\u5206\u675f\u955c\u7b49\u5de5\u4e1a\u548c\u79d1\u5b66\u6fc0\u5149\u7cfb\u7edf\u5143\u4ef6\u3002</p>
            </a>
            <a href="/applications/research-laboratory/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u79d1\u5b66\u7814\u7a76</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u5149\u8c31\u3001\u663e\u5fae\u955c\u3001\u5b9e\u9a8c\u5ba4\u4eea\u5668\u548c\u7814\u7a76\u7cfb\u7edf\u7684\u5b9a\u5236\u5149\u5b66\u5143\u4ef6\u3002</p>
            </a>
            <a href="/applications/semiconductor-inspection/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u534a\u5bfc\u4f53\u8bbe\u5907</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u7528\u4e8e\u68c0\u6d4b\u3001\u6d4b\u91cf\u548c\u7cbe\u5bc6\u8bbe\u5907\u7684\u5149\u5b66\u5143\u4ef6\u3002</p>
            </a>
            <a href="/applications/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u6210\u50cf\u4e0e\u89c6\u89c9</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u7528\u4e8e\u6210\u50cf\u548c\u673a\u5668\u89c6\u89c9\u7684\u900f\u955c\u3001\u7a97\u53e3\u3001\u6ee4\u5149\u7247\u548c\u5149\u5b66\u7ec4\u4ef6\u3002</p>
            </a>
            <a href="/applications/medical-imaging/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u533b\u7597\u4e0e\u751f\u547d\u79d1\u5b66</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u7528\u4e8e\u6210\u50cf\u3001\u8bca\u65ad\u548c\u5206\u6790\u8bbe\u5907\u7684\u5149\u5b66\u5143\u4ef6\u3002</p>
            </a>
            <a href="/applications/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u5de5\u4e1a\u5149\u5b66</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u7528\u4e8e\u4f20\u611f\u3001\u6d4b\u91cf\u548c\u5de5\u4e1a\u7cfb\u7edf\u7684\u5b9a\u5236\u5149\u5b66\u5143\u4ef6\u3002</p>
            </a>
        </div>
        <div style="text-align:center;margin-top:40px;">
            <a href="/zh/applications.html" style="color:#2563eb;font-weight:600;text-decoration:none;font-size:15px;">\u63a2\u7d22\u5e94\u7528\u9886\u57df &rarr;</a>
        </div>
    </div>
</section>

<!-- ============ S5: CORE PRODUCTS ============ -->
<section style="padding:80px 0;background:white;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;">\u6838\u5fc3\u4ea7\u54c1\u5206\u7c7b</h2>
            <p style="color:#64748b;max-width:600px;margin:0 auto;font-size:16px;">\u4e03\u5927\u7c7b\u522b\u7684\u6807\u51c6\u548c\u5b9a\u5236\u5149\u5b66\u5143\u4ef6\u3002</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;max-width:1100px;margin:0 auto;">
            <a href="/products.html?category=Optical+Lenses" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;">\u5149\u5b66\u900f\u955c</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;">\u7403\u9762\u3001\u975e\u7403\u9762\u3001\u5706\u67f1\u3001\u6d88\u8272\u5dee\u548c\u5b9a\u5236\u900f\u955c\uff0c\u9002\u7528\u4e8e\u7d2b\u5916\u3001\u53ef\u89c1\u5149\u548c\u7ea2\u5916\u3002</p>
            </a>
            <a href="/products.html?category=Optical+Windows" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;">\u5149\u5b66\u7a97\u53e3</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;">\u7d2b\u5916\u7194\u878d\u77f3\u82f1\u3001BK7\u3001\u84dd\u5b9d\u77f3\u3001CaF&#8322;\u3001ZnSe\u7b49\u6750\u6599\u7684\u5e73\u9762\u548c\u66f2\u9762\u7a97\u53e3\u3002</p>
            </a>
            <a href="/products.html?category=Optical+Mirrors" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;">\u5149\u5b66\u53cd\u5c04\u955c</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;">\u5e73\u9762\u3001\u66f2\u9762\u548c\u4e8c\u5411\u8272\u53cd\u5c04\u955c\uff0c\u5177\u6709\u4ecb\u8d28\u6216\u91d1\u5c5e\u9540\u819c\u3002</p>
            </a>
            <a href="/products.html?category=Optical+Filters" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;">\u5149\u5b66\u6ee4\u5149\u7247</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;">\u5e26\u901a\u3001\u957f\u901a\u3001\u77ed\u901a\u3001\u4e2d\u6027\u5bc6\u5ea6\u548c\u4e8c\u5411\u8272\u6ee4\u5149\u7247\u3002</p>
            </a>
            <a href="/products.html?category=Beamsplitters" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;">\u5206\u675f\u955c</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;">\u677f\u5f0f\u548c\u7acb\u65b9\u4f53\u5206\u675f\u955c\uff0c\u7528\u4e8e\u5149\u675f\u5206\u5272\u548c\u5408\u675f\u3002</p>
            </a>
            <a href="/products.html?category=Optical+Prisms" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;">\u5149\u5b66\u68f1\u955c</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;">\u5149\u675f\u8f6c\u5411\u3001\u8272\u6563\u548c\u504f\u632f\u68f1\u955c\u3002</p>
            </a>
            <a href="/products.html?category=Waveplates+%26+Polarizers" style="padding:24px;background:#f8fafc;border-radius:10px;border:1px solid #e2e8f0;text-decoration:none;transition:all 0.3s;" onmouseover="this.style.borderColor='#3b82f6'" onmouseout="this.style.borderColor='#e2e8f0'">
                <h3 style="font-size:16px;color:#1e293b;margin-bottom:6px;font-weight:600;">\u6ce2\u7247\u4e0e\u504f\u632f\u5668</h3>
                <p style="color:#64748b;font-size:13px;line-height:1.6;margin:0;">\u96f6\u7ea7\u3001\u591a\u7ea7\u6ce2\u7247\u548c\u504f\u632f\u5206\u675f\u955c\u3002</p>
            </a>
        </div>
        <div style="text-align:center;margin-top:40px;">
            <a href="/products.html" style="display:inline-block;background:#2563eb;color:white;padding:12px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:15px;">\u67e5\u770b\u5168\u90e8\u4ea7\u54c1 &rarr;</a>
        </div>
    </div>
</section>

<!-- ============ S6: ENGINEERING RESOURCES ============ -->
<section style="padding:80px 0;background:#f8fafc;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;">\u5de5\u7a0b\u8d44\u6e90</h2>
            <p style="color:#64748b;max-width:700px;margin:0 auto;font-size:16px;line-height:1.7;">\u5149\u5b66\u5143\u4ef6\u9009\u578b\u548c\u89c4\u683c\u7684\u6280\u672f\u53c2\u8003\u8d44\u6599\u3002</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:24px;max-width:1100px;margin:0 auto;">
            <a href="/materials.html" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#129514;</div>
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u6750\u6599\u6570\u636e\u5e93</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u5e38\u7528\u5149\u5b66\u6750\u6599\u7684\u5149\u5b66\u3001\u70ed\u5b66\u548c\u673a\u68b0\u6027\u80fd\u3002\u6bd4\u8f83\u6750\u6599\u5e76\u4e86\u89e3\u5e94\u7528\u9002\u7528\u6027\u3002</p>
            </a>
            <a href="/coatings/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128300;</div>
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u9540\u819c\u6570\u636e\u5e93</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u5149\u5b66\u9540\u819c\u7c7b\u578b\u3001\u89c4\u683c\u548c\u5e94\u7528\u53c2\u8003\u3002\u4e86\u89e3\u9488\u5bf9\u60a8\u7684\u6ce2\u957f\u548c\u529f\u7387\u8981\u6c42\u7684\u9540\u819c\u9009\u62e9\u3002</p>
            </a>
            <a href="/zh/applications.html" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128218;</div>
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;">\u5e94\u7528\u6307\u5357</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u6fc0\u5149\u7cfb\u7edf\u3001\u79d1\u5b66\u7814\u7a76\u3001\u534a\u5bfc\u4f53\u8bbe\u5907\u3001\u6210\u50cf\u548c\u533b\u7528\u5149\u5b66\u7684\u5e94\u7528\u53c2\u8003\u3002</p>
            </a>
            <a href="/ai-optical-assistant.html" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#129302;</div>
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;">AI \u5149\u5b66\u52a9\u624b</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;">\u6839\u636e\u60a8\u7684\u5e94\u7528\u8981\u6c42\u83b7\u53d6\u521d\u6b65\u7684\u5149\u5b66\u5143\u4ef6\u63a8\u8350\u548c\u6750\u6599\u5efa\u8bae\u3002</p>
            </a>
        </div>
        <div style="text-align:center;margin-top:40px;">
            <a href="/knowledge-center/" style="color:#2563eb;font-weight:600;text-decoration:none;font-size:15px;">\u63a2\u7d22\u6240\u6709\u8d44\u6e90 &rarr;</a>
        </div>
    </div>
</section>

<!-- ============ S7: CUSTOM OPTICS ============ -->
<section style="padding:80px 0;background:white;">
    <div class="container" style="max-width:900px;">
        <div style="text-align:center;margin-bottom:40px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;">\u5b9a\u5236\u5149\u5b66</h2>
            <p style="color:#64748b;max-width:700px;margin:0 auto;font-size:16px;line-height:1.7;">\u5982\u679c\u60a8\u7684\u5e94\u7528\u9700\u8981\u975e\u6807\u5149\u5b66\u5143\u4ef6\uff0c\u6052\u9f0e\u5149\u53ef\u4ee5\u5e2e\u52a9\u534f\u8c03\u5b9a\u5236\u5236\u9020\u3002</p>
        </div>
        <div style="background:#f8fafc;border-radius:12px;border:1px solid #e2e8f0;padding:40px;">
            <p style="color:#374151;font-size:15px;line-height:1.8;margin-bottom:20px;">\u5b9a\u5236\u5149\u5b66\u5143\u4ef6\u57fa\u4e8e\u60a8\u7684\u56fe\u7eb8\u6216\u89c4\u683c\u5236\u9020\u3002\u6211\u4eec\u5ba1\u67e5\u60a8\u7684\u8981\u6c42\uff0c\u5305\u62ec\u6750\u6599\u3001\u5c3a\u5bf8\u3001\u8868\u9762\u8d28\u91cf\u3001\u9540\u819c\u548c\u6570\u91cf\uff0c\u7136\u540e\u5339\u914d\u5408\u9002\u7684\u5236\u9020\u8d44\u6e90\u3002</p>
            <p style="color:#374151;font-size:15px;line-height:1.8;margin-bottom:20px;">\u751f\u4ea7\u5f00\u59cb\u524d\uff0c\u6211\u4eec\u786e\u8ba4\uff1a</p>
            <ul style="color:#374151;font-size:15px;line-height:2;margin:0 0 24px 20px;padding:0;">
                <li>\u6750\u6599\u548c\u9540\u819c\u53ef\u884c\u6027</li>
                <li>\u5236\u9020\u5de5\u827a\u8def\u7ebf</li>
                <li>\u68c0\u6d4b\u65b9\u6cd5\u548c\u9a8c\u6536\u6807\u51c6</li>
                <li>\u6587\u6863\u8981\u6c42</li>
            </ul>
            <div style="text-align:center;">
                <a href="/zh/contact.html" style="display:inline-block;background:#2563eb;color:white;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:16px;">\u8ba8\u8bba\u60a8\u7684\u5b9a\u5236\u9700\u6c42 &rarr;</a>
            </div>
        </div>
    </div>
</section>

<!-- ============ S8: FINAL CTA ============ -->
<section style="padding:80px 0;background:linear-gradient(135deg,#1e3a5f 0%,#2563eb 100%);">
    <div class="container" style="text-align:center;">
        <h2 style="font-size:32px;font-weight:700;color:white;margin-bottom:16px;">\u6709\u5149\u5b66\u9700\u6c42\uff1f</h2>
        <p style="color:rgba(255,255,255,0.85);font-size:16px;line-height:1.8;max-width:650px;margin:0 auto 32px;">\u65e0\u8bba\u60a8\u6709\u5b8c\u6574\u56fe\u7eb8\u8fd8\u662f\u53ea\u6709\u5e94\u7528\u63cf\u8ff0\uff0c\u8bf7\u53d1\u9001\u7ed9\u6211\u4eec\u3002\u6211\u4eec\u5c06\u5e2e\u52a9\u60a8\u786e\u5b9a\u5408\u9002\u7684\u5143\u4ef6\u548c\u5236\u9020\u65b9\u6848\u3002</p>
        <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
            <a href="/zh/contact.html" style="display:inline-block;background:white;color:#2563eb;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:16px;">\u8bf7\u6c42\u62a5\u4ef7</a>
            <a href="/zh/contact.html" style="display:inline-block;background:transparent;border:2px solid rgba(255,255,255,0.5);color:white;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:16px;">\u4e0a\u4f20\u60a8\u7684\u56fe\u7eb8</a>
            <a href="/ai-optical-assistant.html" style="display:inline-block;background:transparent;border:2px solid rgba(255,255,255,0.5);color:white;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:16px;">\u54a8\u8be2AI\u52a9\u624b</a>
        </div>
    </div>
</section>

''' + footer + scripts

with open(os.path.join(BASE, 'zh/index.html'), 'w') as f:
    f.write(new_zh)

print("zh/index.html written. Lines: %d" % new_zh.count('\n'))
