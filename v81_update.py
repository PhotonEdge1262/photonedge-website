#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V81 Update Script - Comprehensive site modifications"""

import os
import re
import json

BASE = '/app/data/所有对话/主对话/PhotonEdge-V81'

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Written: {path}')

# ============================================================
# 1. Update index.html - Complete homepage rebuild
# ============================================================
print('=== Updating index.html ===')
index_path = os.path.join(BASE, 'index.html')
index = read_file(index_path)

# 1a. Update head section - title, meta, schema
index = index.replace(
    '<title>PhotonEdge - Precision Optical Components Manufacturer | Custom Optics &amp; Lenses</title>',
    '<title>PhotonEdge - Precision Optical Solutions for Laser, Semiconductor &amp; Advanced Imaging</title>'
)

index = index.replace(
    'content="PhotonEdge: leading precision optics manufacturer in Beijing. ISO 9001 &amp; 13485 certified. Custom lenses, mirrors, prisms, windows &amp; coatings. Get a free quote."',
    'content="PhotonEdge provides precision optical solutions for laser, semiconductor, medical, and research industries. Custom optics, coating design, and engineering support. ISO 9001 &amp; 14001 certified."'
)

index = index.replace(
    'content="optical components manufacturer, custom optics, precision lenses supplier, Beijing Hengdingguang, PhotonEdge optics, 光学元件制造商,定制光学元件,精密光学透镜供应商,北京恒鼎光"',
    'content="precision optical solutions, custom optics, laser optics, semiconductor optics, optical engineering, PhotonEdge, 精密光学解决方案,定制光学元件,激光光学,光学工程"'
)

index = index.replace(
    'content="PhotonEdge - Precision Optical Components Manufacturer | Optical Lenses, Mirrors, Prisms Supplier"',
    'content="PhotonEdge - Precision Optical Solutions for Laser, Semiconductor &amp; Advanced Imaging"'
)

index = index.replace(
    'content="Leading precision optical components manufacturer in China. Supplying optical lenses, mirrors, windows, prisms, filters &amp; polarizing components. ISO 9001:2015 certified."',
    'content="PhotonEdge provides end-to-end optical solutions — from material selection to custom coating — for laser, semiconductor, medical, and research industries. ISO 9001 &amp; 14001 certified."'
)

index = index.replace(
    '"description": "Precision optical components manufacturer in Beijing, China"',
    '"description": "Precision optical solutions provider — helping global companies solve optical challenges from material selection to custom manufacturing"'
)

# 1b. Update nav - add Solutions and Knowledge Center, streamline nav
old_nav = '''<ul class="nav-list">
                    <li><a href="/" class="nav-link active" data-i18n="navHome">Home</a></li>
                    <li><a href="/products.html" class="nav-link " data-i18n="navProducts">Products</a></li>
                    <li><a href="/about.html" class="nav-link " data-i18n="navAbout">About Us</a></li>
                    <li class="nav-dropdown" onclick="if(window.innerWidth<=768){event.stopPropagation();this.classList.toggle('open')}">
                        <a href="/calculator.html" class="nav-link " data-i18n="navTools">Tools</a>
                        <div class="dropdown-menu">
                            <a href="/calculator.html" class="dropdown-item">
                                <span class="dropdown-icon">🧮</span>
                                <span data-i18n="menuCalculators">Optical Calculators</span>
                            </a>
                            <a href="/ray-tracer.html" class="dropdown-item">
                                <span class="dropdown-icon">🔬</span>
                                <span data-i18n="menuRayTracer">Ray Tracer Simulator</span>
                            </a>
                            <a href="/materials.html" class="dropdown-item">
                                <span class="dropdown-icon">📊</span>
                                <span data-i18n="menuMaterials">Materials Database</span>
                            </a>
                            <a href="/product-advisor.html" class="dropdown-item">
                                <span class="dropdown-icon">🎯</span>
                                <span data-i18n="menuSelector">Product Selector</span>
                            </a>
                        </div>
                    </li>
                    <li><a href="/faq.html" class="nav-link " data-i18n="navFAQ">FAQ</a></li>
                    <li><a href="/blog.html" class="nav-link " data-i18n="navBlog">Blog</a></li>
                    <li><a href="/downloads.html" class="nav-link" data-i18n="navDownloads">Downloads</a></li>
                    <li><a href="/case-studies.html" class="nav-link" data-i18n="navCaseStudies">Case Studies</a></li>
                    <li><a href="/contact.html" class="nav-link " data-i18n="navContact">Contact</a></li>
                    <li><a href="/news.html" class="nav-link" data-i18n="navNews">News</a></li>
                </ul>'''

new_nav = '''<ul class="nav-list">
                    <li><a href="/" class="nav-link active" data-i18n="navHome">Home</a></li>
                    <li><a href="/products.html" class="nav-link" data-i18n="navProducts">Products</a></li>
                    <li><a href="/solutions/" class="nav-link" data-i18n="navSolutions">Solutions</a></li>
                    <li><a href="/knowledge-center/" class="nav-link" data-i18n="navKnowledgeCenter">Knowledge Center</a></li>
                    <li class="nav-dropdown" onclick="if(window.innerWidth<=768){event.stopPropagation();this.classList.toggle('open')}">
                        <a href="/calculator.html" class="nav-link" data-i18n="navTools">Tools</a>
                        <div class="dropdown-menu">
                            <a href="/calculator.html" class="dropdown-item">
                                <span class="dropdown-icon">&#129518;</span>
                                <span data-i18n="menuCalculators">Optical Calculators</span>
                            </a>
                            <a href="/ray-tracer.html" class="dropdown-item">
                                <span class="dropdown-icon">&#128300;</span>
                                <span data-i18n="menuRayTracer">Ray Tracer Simulator</span>
                            </a>
                            <a href="/materials.html" class="dropdown-item">
                                <span class="dropdown-icon">&#128202;</span>
                                <span data-i18n="menuMaterials">Materials Database</span>
                            </a>
                            <a href="/product-advisor.html" class="dropdown-item">
                                <span class="dropdown-icon">&#127919;</span>
                                <span data-i18n="menuSelector">Product Selector</span>
                            </a>
                        </div>
                    </li>
                    <li><a href="/about.html" class="nav-link" data-i18n="navAbout">About Us</a></li>
                    <li><a href="/blog.html" class="nav-link" data-i18n="navBlog">Blog</a></li>
                    <li><a href="/contact.html" class="nav-link" data-i18n="navContact">Contact</a></li>
                </ul>'''

index = index.replace(old_nav, new_nav)

# 1c. Update Hero section
old_hero = '''<section class="hero">
        <div class="container">
            <h1 data-i18n="heroTitle">Precision Optical Components for Demanding Applications</h1>
            <p class="subtitle" data-i18n="heroSubtitle">15+ years of manufacturing excellence. 500+ global clients trust PhotonEdge for lenses, mirrors, windows, prisms &amp; custom solutions.</p>
            <p class="company" data-i18n="heroDesc">Beijing Hengdingguang Technology Co., Ltd.</p>
            <div class="hero-btns">
                <a href="/products.html" class="btn btn-primary" data-i18n="viewProducts">View Products</a>
                <a href="/about.html" class="btn btn-secondary" data-i18n="learnMore">Learn More</a>
            </div>
        </div>
    </section>'''

new_hero = '''<section class="hero">
        <div class="container">
            <h1 data-i18n="heroTitle">Precision Optical Solutions for Laser, Semiconductor &amp; Advanced Imaging</h1>
            <p class="subtitle" data-i18n="heroSubtitle">From material selection to custom coating — we solve your optical challenges. Prototype to volume production.</p>
            <div class="hero-btns">
                <a href="/contact.html" class="btn btn-primary" data-i18n="heroCTA1">Get Engineering Support</a>
                <a href="/solutions/" class="btn btn-secondary" data-i18n="heroCTA2">Explore Solutions</a>
            </div>
        </div>
    </section>'''

index = index.replace(old_hero, new_hero)

# 1d. Replace AI Selector section position - keep but move after industries
# 1e. Replace stats-bar-enhanced with Industries We Serve (new enhanced version)
old_stats = '''<!-- Home Trust Bar -->
    <section class="stats-bar-enhanced">
        <div class="container">
            <div class="stats-grid-enhanced">
                <div class="stat-item-enhanced">
                    <span class="stat-number-enhanced" data-i18n="statYears">15+</span>
                    <div class="stat-label-enhanced" data-i18n="statYearsLabel">Years of Experience</div>
                </div>
                <div class="stat-item-enhanced">
                    <span class="stat-number-enhanced" data-i18n="statCountries">50+</span>
                    <div class="stat-label-enhanced" data-i18n="statCountriesLabel">Countries Served</div>
                </div>
                <div class="stat-item-enhanced">
                    <span class="stat-number-enhanced" data-i18n="statProducts">70+</span>
                    <div class="stat-label-enhanced" data-i18n="statProductsLabel">Product Types</div>
                </div>
                <div class="stat-item-enhanced">
                    <span class="stat-number-enhanced" data-i18n="statClients">500+</span>
                    <div class="stat-label-enhanced" data-i18n="statClientsLabel">Global Clients</div>
                </div>
            </div>
        </div>
    </section>'''

new_stats = '''<!-- Industries We Serve - Screen 2 -->
    <section class="home-industries-section" style="padding: 60px 0; background: #f8fafc;">
        <div class="container">
            <h2 class="section-title" data-i18n="homeIndustriesTitle">Industries We Serve</h2>
            <p class="section-subtitle" data-i18n="homeIndustriesSubtitle">We understand the unique optical challenges of your industry</p>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; max-width: 1000px; margin: 0 auto;">
                <a href="/solutions/#laser" style="background: white; border-radius: 16px; padding: 32px 24px; text-align: center; text-decoration: none; transition: all 0.3s; border: 1px solid #e2e8f0; display: block;" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 8px 24px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none'">
                    <div style="font-size: 48px; margin-bottom: 12px;">&#128300;</div>
                    <h3 style="color: #1e293b; margin-bottom: 8px; font-size: 18px;" data-i18n="homeIndustryLaser">Laser Systems</h3>
                    <p style="color: #64748b; font-size: 14px; line-height: 1.5;" data-i18n="homeIndustryLaserDesc">High-LIDT coatings and low-absorption optics for high-power applications</p>
                </a>
                <a href="/solutions/#semiconductor" style="background: white; border-radius: 16px; padding: 32px 24px; text-align: center; text-decoration: none; transition: all 0.3s; border: 1px solid #e2e8f0; display: block;" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 8px 24px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none'">
                    <div style="font-size: 48px; margin-bottom: 12px;">&#128187;</div>
                    <h3 style="color: #1e293b; margin-bottom: 8px; font-size: 18px;" data-i18n="homeIndustrySemi">Semiconductor</h3>
                    <p style="color: #64748b; font-size: 14px; line-height: 1.5;" data-i18n="homeIndustrySemiDesc">Sub-nanometer roughness and cleanroom-grade precision optics</p>
                </a>
                <a href="/solutions/#medical" style="background: white; border-radius: 16px; padding: 32px 24px; text-align: center; text-decoration: none; transition: all 0.3s; border: 1px solid #e2e8f0; display: block;" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 8px 24px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none'">
                    <div style="font-size: 48px; margin-bottom: 12px;">&#10084;</div>
                    <h3 style="color: #1e293b; margin-bottom: 8px; font-size: 18px;" data-i18n="homeIndustryMedical">Medical</h3>
                    <p style="color: #64748b; font-size: 14px; line-height: 1.5;" data-i18n="homeIndustryMedicalDesc">Biocompatible, traceable optics with batch consistency</p>
                </a>
                <a href="/solutions/#research" style="background: white; border-radius: 16px; padding: 32px 24px; text-align: center; text-decoration: none; transition: all 0.3s; border: 1px solid #e2e8f0; display: block;" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 8px 24px rgba(0,0,0,0.1)'" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none'">
                    <div style="font-size: 48px; margin-bottom: 12px;">&#128218;</div>
                    <h3 style="color: #1e293b; margin-bottom: 8px; font-size: 18px;" data-i18n="homeIndustryResearch">Research</h3>
                    <p style="color: #64748b; font-size: 14px; line-height: 1.5;" data-i18n="homeIndustryResearchDesc">Ultra-precision and exotic material optics for cutting-edge experiments</p>
                </a>
            </div>
        </div>
    </section>'''

index = index.replace(old_stats, new_stats)

# 1f. Replace features section with "Why PhotonEdge" (Screen 4)
old_features = '''<section class="features">
        <div class="container">
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">&#128230;</div>
                    <h3 data-i18n="feature1Title">Complete Product Line</h3>
                    <p data-i18n="feature1Desc">Lenses, mirrors, windows, prisms, filters, waveplates, beamsplitters, polarizers</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">&#128142;</div>
                    <h3 data-i18n="feature2Title">Premium Materials</h3>
                    <p data-i18n="feature2Desc">K9(BK7), Quartz, ZnSe, Ge, Si, CaF2, Sapphire</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">&#9881;</div>
                    <h3 data-i18n="feature3Title">Advanced Equipment</h3>
                    <p data-i18n="feature3Desc">Precision optical processing and testing equipment</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">&#127919;</div>
                    <h3 data-i18n="feature4Title">Custom Solutions</h3>
                    <p data-i18n="feature4Desc">OEM customization available, fast delivery</p>
                </div>
            </div>
        </div>
    </section>'''

new_features = '''<!-- Why PhotonEdge - Screen 4 -->
    <section class="features">
        <div class="container">
            <h2 class="section-title" data-i18n="whyPETitle">Why PhotonEdge</h2>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">&#128736;</div>
                    <h3 data-i18n="whyPE1Title">Engineering Support</h3>
                    <p data-i18n="whyPE1Desc">Material selection, coating design, optical optimization — our engineers help you from concept to production</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">&#127919;</div>
                    <h3 data-i18n="whyPE2Title">Custom Solutions</h3>
                    <p data-i18n="whyPE2Desc">From prototype to volume production, any specification — we design and manufacture to your exact requirements</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">&#10004;</div>
                    <h3 data-i18n="whyPE3Title">Quality Assured</h3>
                    <p data-i18n="whyPE3Desc">ISO 9001 &amp; 14001 certified with full inspection reports — every component meets your specifications</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">&#127758;</div>
                    <h3 data-i18n="whyPE4Title">Global Delivery</h3>
                    <p data-i18n="whyPE4Desc">Reliable shipping to North America, Europe, and Asia — on-time delivery you can count on</p>
                </div>
            </div>
        </div>
    </section>'''

index = index.replace(old_features, new_features)

# 1g. Replace old industry-section + certifications + applications + testimonials with new sections
# Find and replace the industry section through to applications section end
old_industry_start = '    <!-- Home Industry Strip -->\n\n    <section class="categories">'
# We need to keep the categories (product grid) section - it's Screen 3
# So we just replace the industry-section, certifications, and applications sections

# Replace the industry section with Manufacturing & Quality Process (Screen 5)
old_industry = '''<section class="industry-section">
        <div class="container">
            <h2 class="section-title" data-i18n="industriesTitle">Industries We Serve</h2>
            <div class="industry-grid">
                <div class="industry-card">
                    <div class="industry-icon">&#128300;</div>
                    <div class="industry-name" data-i18n="industryLaser">Laser Systems</div>
                </div>
                <div class="industry-card">
                    <div class="industry-icon">&#10084;</div>
                    <div class="industry-name" data-i18n="industryMedical">Medical Devices</div>
                </div>
                <div class="industry-card">
                    <div class="industry-icon">&#128225;</div>
                    <div class="industry-name" data-i18n="industryTelecom">Telecommunications</div>
                </div>
                <div class="industry-card">
                    <div class="industry-icon">&#128218;</div>
                    <div class="industry-name" data-i18n="industryResearch">Research Institutions</div>
                </div>
                <div class="industry-card">
                    <div class="industry-icon">&#9876;</div>
                    <div class="industry-name" data-i18n="industryDefense">Defense &amp; Aerospace</div>
                </div>
                <div class="industry-card">
                    <div class="industry-icon">&#128187;</div>
                    <div class="industry-name" data-i18n="industrySemiconductor">Semiconductor</div>
                </div>
            </div>
            
            <!-- Certification Badges -->
            <div class="cert-badges">
                <div class="cert-badge">
                    <div class="cert-badge-icon">&#10004;</div>
                    <div class="cert-badge-text" data-i18n="certISO">ISO 9001:2015</div>
                    <div class="cert-badge-sub" data-i18n="certISODesc">Quality Management System</div>
                </div>
                <div class="cert-badge">
                    <div class="cert-badge-icon">&#127942;</div>
                    <div class="cert-badge-text" data-i18n="certCE">CE Compliant</div>
                    <div class="cert-badge-sub" data-i18n="certCEDesc">European Standards</div>
                </div>
                <div class="cert-badge">
                    <div class="cert-badge-icon">&#127795;</div>
                    <div class="cert-badge-text" data-i18n="certRoHS">RoHS Compliant</div>
                    <div class="cert-badge-sub" data-i18n="certRoHSDesc">Environmental Safety</div>
                </div>
            </div>
        </div>
    </section>

    <section class="certifications">
        <div class="container">
            <h2 class="section-title" data-i18n="certificationsTitle">Quality Certifications</h2>
            <div class="certifications-grid">
                <div class="certification-card">
                    <div class="cert-icon">&#10004;</div>
                    <h3>ISO 9001:2015</h3>
                    <p data-i18n="isoDesc">Quality Management System Certified</p>
                </div>
                <div class="certification-card">
                    <div class="cert-icon">&#10004;</div>
                    <h3 data-i18n="precisionTitle">Precision Manufacturing</h3>
                    <p data-i18n="precisionDesc">High-precision optical components with strict quality control</p>
                </div>
                <div class="certification-card">
                    <div class="cert-icon">&#10004;</div>
                    <h3 data-i18n="testingTitle">Full Testing</h3>
                    <p data-i18n="testingDesc">Every product undergoes rigorous inspection before shipment</p>
                </div>
            </div>
        </div>
    </section>'''

new_process = '''<!-- Manufacturing & Quality Process - Screen 5 -->
    <section style="padding: 60px 0; background: #ffffff;">
        <div class="container" style="text-align: center;">
            <h2 class="section-title" data-i18n="processTitle">Our Process — From Drawing to Delivery</h2>
            <p style="color: #64748b; margin-bottom: 40px; font-size: 18px;" data-i18n="processSubtitle">Every component follows our rigorous 8-step quality process</p>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; max-width: 1000px; margin: 0 auto 20px;">
                <div style="background: #f8fafc; border-radius: 12px; padding: 24px 16px; border-left: 4px solid #1e3a5f;">
                    <div style="font-size: 28px; margin-bottom: 8px;">&#128196;</div>
                    <h4 style="color: #1e293b; margin-bottom: 6px; font-size: 15px;" data-i18n="processStep1">1. Customer Requirements</h4>
                    <p style="color: #64748b; font-size: 13px;" data-i18n="processStep1Desc">Detailed specification review and feasibility assessment</p>
                </div>
                <div style="background: #f8fafc; border-radius: 12px; padding: 24px 16px; border-left: 4px solid #2d5a87;">
                    <div style="font-size: 28px; margin-bottom: 8px;">&#128269;</div>
                    <h4 style="color: #1e293b; margin-bottom: 6px; font-size: 15px;" data-i18n="processStep2">2. Technical Review</h4>
                    <p style="color: #64748b; font-size: 13px;" data-i18n="processStep2Desc">Engineering analysis and design optimization</p>
                </div>
                <div style="background: #f8fafc; border-radius: 12px; padding: 24px 16px; border-left: 4px solid #3b82f6;">
                    <div style="font-size: 28px; margin-bottom: 8px;">&#128300;</div>
                    <h4 style="color: #1e293b; margin-bottom: 6px; font-size: 15px;" data-i18n="processStep3">3. Material Selection</h4>
                    <p style="color: #64748b; font-size: 13px;" data-i18n="processStep3Desc">Optimal substrate and glass grade matching your wavelength</p>
                </div>
                <div style="background: #f8fafc; border-radius: 12px; padding: 24px 16px; border-left: 4px solid #6366f1;">
                    <div style="font-size: 28px; margin-bottom: 8px;">&#9881;</div>
                    <h4 style="color: #1e293b; margin-bottom: 6px; font-size: 15px;" data-i18n="processStep4">4. Precision Machining</h4>
                    <p style="color: #64748b; font-size: 13px;" data-i18n="processStep4Desc">CNC generating and grinding to near-net shape</p>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; max-width: 1000px; margin: 0 auto;">
                <div style="background: #f8fafc; border-radius: 12px; padding: 24px 16px; border-left: 4px solid #8b5cf6;">
                    <div style="font-size: 28px; margin-bottom: 8px;">&#10024;</div>
                    <h4 style="color: #1e293b; margin-bottom: 6px; font-size: 15px;" data-i18n="processStep5">5. Polishing</h4>
                    <p style="color: #64748b; font-size: 13px;" data-i18n="processStep5Desc">Precision polishing to achieve required surface figure and quality</p>
                </div>
                <div style="background: #f8fafc; border-radius: 12px; padding: 24px 16px; border-left: 4px solid #a855f7;">
                    <div style="font-size: 28px; margin-bottom: 8px;">&#127752;</div>
                    <h4 style="color: #1e293b; margin-bottom: 6px; font-size: 15px;" data-i18n="processStep6">6. Optical Coating</h4>
                    <p style="color: #64748b; font-size: 13px;" data-i18n="processStep6Desc">Thin-film deposition with spectral verification</p>
                </div>
                <div style="background: #f8fafc; border-radius: 12px; padding: 24px 16px; border-left: 4px solid #d946ef;">
                    <div style="font-size: 28px; margin-bottom: 8px;">&#128270;</div>
                    <h4 style="color: #1e293b; margin-bottom: 6px; font-size: 15px;" data-i18n="processStep7">7. Quality Inspection</h4>
                    <p style="color: #64748b; font-size: 13px;" data-i18n="processStep7Desc">100% inspection with interferometry and spectrophotometry</p>
                </div>
                <div style="background: #f8fafc; border-radius: 12px; padding: 24px 16px; border-left: 4px solid #ec4899;">
                    <div style="font-size: 28px; margin-bottom: 8px;">&#128230;</div>
                    <h4 style="color: #1e293b; margin-bottom: 6px; font-size: 15px;" data-i18n="processStep8">8. Global Delivery</h4>
                    <p style="color: #64748b; font-size: 13px;" data-i18n="processStep8Desc">Secure packaging and reliable shipping worldwide</p>
                </div>
            </div>
        </div>
    </section>'''

index = index.replace(old_industry, new_process)

# 1h. Replace applications section with Featured Knowledge (Screen 6)
old_applications = '''<section class="applications">
        <div class="container">
            <h2 class="section-title" data-i18n="appTitle">Applications</h2>
            <div class="applications-grid">
                <div class="app-item" data-i18n="appMedical">Medical Instruments</div>
                <div class="app-item" data-i18n="appOpto">Optoelectronic Instruments</div>
                <div class="app-item" data-i18n="appEdu">Educational Instruments</div>
                <div class="app-item" data-i18n="appFiber">Fiber Optic Communication</div>
                <div class="app-item" data-i18n="appMilitary">Military Equipment</div>
                <div class="app-item" data-i18n="appSurvey">Construction Surveying</div>
                <div class="app-item" data-i18n="appLaser">Laser Processing</div>
            </div>
        </div>
    </section>'''

new_knowledge = '''<!-- Featured Knowledge - Screen 6 -->
    <section style="padding: 60px 0; background: #f8fafc;">
        <div class="container" style="text-align: center;">
            <h2 class="section-title" data-i18n="featuredKnowledgeTitle">Optical Engineering Insights</h2>
            <p style="color: #64748b; margin-bottom: 40px; font-size: 18px;" data-i18n="featuredKnowledgeSubtitle">Expert guides that solve real optical engineering problems</p>
            <div id="featuredKnowledgeGrid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1000px; margin: 0 auto 32px;">
                <!-- Dynamically rendered by JS -->
            </div>
            <a href="/knowledge-center/" style="display: inline-block; background: #1e3a5f; color: white; padding: 14px 40px; border-radius: 8px; font-weight: 600; text-decoration: none; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'" data-i18n="featuredKnowledgeCTA">Visit Knowledge Center</a>
        </div>
    </section>'''

index = index.replace(old_applications, new_knowledge)

# 1i. Replace testimonials section with final CTA (Screen 8)
old_testimonials = '''<!-- Home Trust Banner with Testimonials -->
    <section class="home-trust-banner">
        <div class="container">
            <h2 class="section-title" data-i18n="homeTrustBannerTitle">Trusted by 500+ Clients Worldwide</h2>
            <p class="home-trust-banner-subtitle" data-i18n="homeTrustBannerSubtitle">Join thousands of research institutions, manufacturers, and laboratories who rely on PhotonEdge</p>
            <div class="home-testimonials-grid">
                <div class="home-testimonial-card">
                    <p class="home-testimonial-text" data-i18n="homeTestimonial1">"PhotonEdge delivers consistently high-quality optical components with competitive pricing. Their lead times are reliable and technical support is excellent."</p>
                    <p class="home-testimonial-author" data-i18n="homeTestimonial1Author">- R&amp;D Director, European Laser Manufacturer</p>
                </div>
                <div class="home-testimonial-card">
                    <p class="home-testimonial-text" data-i18n="homeTestimonial2">"We required custom optics with tight tolerances for our research project. PhotonEdge delivered prototypes within 3 weeks with exceptional quality."</p>
                    <p class="home-testimonial-author" data-i18n="homeTestimonial2Author">- Research Lead, Top 10 Asia-Pacific University - Physics Dept.</p>
                </div>
                <div class="home-testimonial-card">
                    <p class="home-testimonial-text" data-i18n="homeTestimonial3">"Consistency across 500 units was critical for our production line. Zero defects after 100% inspection - truly impressive quality control."</p>
                    <p class="home-testimonial-author" data-i18n="homeTestimonial3Author">- QA Manager, Fortune 500 Medical Device Company</p>
                </div>
            </div>
            <div class="home-client-types">
                <div class="home-client-type-tag">
                    <span class="home-client-type-tag-icon">&#128218;</span>
                    <span data-i18n="clientTypeUniversities">Universities</span>
                </div>
                <div class="home-client-type-tag">
                    <span class="home-client-type-tag-icon">&#127970;</span>
                    <span data-i18n="clientTypeResearchLabs">Research Labs</span>
                </div>
                <div class="home-client-type-tag">
                    <span class="home-client-type-tag-icon">&#128300;</span>
                    <span data-i18n="clientTypeLaserMfg">Laser Manufacturers</span>
                </div>
                <div class="home-client-type-tag">
                    <span class="home-client-type-tag-icon">&#10084;</span>
                    <span data-i18n="clientTypeMedical">Medical Device Companies</span>
                </div>
                <div class="home-client-type-tag">
                    <span class="home-client-type-tag-icon">&#9876;</span>
                    <span data-i18n="clientTypeDefense">Defense Contractors</span>
                </div>
            </div>
        </div>
    </section>'''

new_cta = '''<!-- Final CTA - Screen 8 -->
    <section style="padding: 80px 0; background: linear-gradient(135deg,#1e3a5f 0%,#2d5a87 100%); text-align: center; color: white;">
        <div class="container">
            <h2 style="color: white; margin-bottom: 16px; font-size: 36px;" data-i18n="finalCTATitle">Start Your Optical Project</h2>
            <p style="color: rgba(255,255,255,0.9); margin-bottom: 40px; font-size: 18px; max-width: 600px; margin-left: auto; margin-right: auto;" data-i18n="finalCTASubtitle">Tell us about your application. Our engineering team will design a solution.</p>
            <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
                <a href="/contact.html" style="background: white; color: #1e3a5f; padding: 14px 32px; border-radius: 8px; font-weight: 600; text-decoration: none; display: inline-block; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'" data-i18n="finalCTAQuote">Request Quote</a>
                <a href="/contact.html" style="background: transparent; color: white; padding: 14px 32px; border-radius: 8px; font-weight: 600; text-decoration: none; display: inline-block; border: 2px solid rgba(255,255,255,0.6); transition: all 0.3s;" onmouseover="this.style.borderColor='white';this.style.transform='translateY(-2px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.6)';this.style.transform='translateY(0)'" data-i18n="finalCTAEngineer">Talk to Engineer</a>
                <a href="/contact.html" style="background: transparent; color: white; padding: 14px 32px; border-radius: 8px; font-weight: 600; text-decoration: none; display: inline-block; border: 2px solid rgba(255,255,255,0.6); transition: all 0.3s;" onmouseover="this.style.borderColor='white';this.style.transform='translateY(-2px)'" onmouseout="this.style.borderColor='rgba(255,255,255,0.6)';this.style.transform='translateY(0)'" data-i18n="finalCTACustom">Custom Project</a>
            </div>
        </div>
    </section>'''

index = index.replace(old_testimonials, new_cta)

# 1j. Update footer description
index = index.replace(
    'Precision Optical Components Supplier',
    'Precision Optical Solutions Provider'
)

# 1k. Add Featured Knowledge rendering JS and blog-data.js include
# Add blog-data.js script before translations.js
index = index.replace(
    '<script src="/js/translations.js"></script>',
    '<script src="/js/blog-data.js"></script>\n    <script src="/js/translations.js"></script>'
)

# Add featured knowledge rendering script
old_render_script = 'renderFeaturedProducts();\n    </script>'

new_render_script = '''renderFeaturedProducts();
    renderFeaturedKnowledge();
    </script>

    <script>
    function renderFeaturedKnowledge() {
        var grid = document.getElementById('featuredKnowledgeGrid');
        if (!grid || typeof BLOG_POSTS === 'undefined') return;
        var useZh = localStorage.getItem('lang') === 'zh';
        var featuredSlugs = ['choose-right-optical-lens', 'bk7-vs-uv-fused-silica', 'laser-damage-threshold-guide', 'machine-vision-lens-selection-guide', 'optical-windows-buying-guide', 'optical-component-cleaning-maintenance-guide'];
        var html = '';
        for (var i = 0; i < BLOG_POSTS.length; i++) {
            var post = BLOG_POSTS[i];
            if (featuredSlugs.indexOf(post.slug) === -1) continue;
            var postTitle = useZh && post.titleZh ? post.titleZh : post.title;
            var postExcerpt = useZh && post.excerptZh ? post.excerptZh : post.excerpt;
            if (postExcerpt.length > 120) postExcerpt = postExcerpt.substring(0, 120) + '...';
            html += '<a href="/blog/' + post.slug + '/" style="background: white; border-radius: 16px; padding: 24px; text-decoration: none; display: block; border: 1px solid #e2e8f0; transition: all 0.3s;" onmouseover="this.style.transform=\\'translateY(-4px)\\';this.style.boxShadow=\\'0 8px 24px rgba(0,0,0,0.08)\\'" onmouseout="this.style.transform=\\'translateY(0)\\';this.style.boxShadow=\\'none\\'">';
            html += '<h3 style="color: #1e293b; margin-bottom: 8px; font-size: 16px;">' + postTitle + '</h3>';
            html += '<p style="color: #64748b; font-size: 14px; line-height: 1.5; margin-bottom: 12px;">' + postExcerpt + '</p>';
            html += '<span style="color: #3b82f6; font-weight: 600; font-size: 14px;">Read More &rarr;</span>';
            html += '</a>';
        }
        grid.innerHTML = html;
    }
    </script>'''

index = index.replace(old_render_script, new_render_script)

# 1l. Update footer - add Solutions link
index = index.replace(
    '''<li><a href="/about.html" data-i18n="navAbout">About Us</a></li>
                        <li><a href="/contact.html" data-i18n="navContact">Contact</a></li>''',
    '''<li><a href="/about.html" data-i18n="navAbout">About Us</a></li>
                        <li><a href="/solutions/" data-i18n="navSolutions">Solutions</a></li>
                        <li><a href="/contact.html" data-i18n="navContact">Contact</a></li>'''
)

write_file(index_path, index)

# ============================================================
# 2. Update about.html
# ============================================================
print('=== Updating about.html ===')
about_path = os.path.join(BASE, 'about.html')
about = read_file(about_path)

# Update title
about = about.replace(
    '<title>About PhotonEdge - 15+ Years Precision Optics Manufacturer | ISO Certified</title>',
    '<title>About PhotonEdge - Precision Optical Solutions Provider | ISO Certified</title>'
)

# Update meta description
about = about.replace(
    'content="PhotonEdge is a trusted precision optics manufacturer since 2010. ISO 9001, 13485, 14001 certified. 8 optical materials, advanced coatings, quality control."',
    'content="PhotonEdge helps global companies solve precision optical challenges — from material selection and coating design to custom manufacturing and quality assurance. ISO 9001, 13485, 14001 certified."'
)

# Update the rest of the broken meta
about = about.replace(
    "s 15+ years of optical manufacturing excellence. ISO 9001:2015 certified facility with advanced testing equipment.\"",
    "PhotonEdge helps global companies solve precision optical challenges — from material selection and coating design to custom manufacturing and quality assurance.\""
)

# Update og:title
about = about.replace(
    'content="About PhotonEdge - Precision Optical Components Manufacturer"',
    'content="About PhotonEdge - Precision Optical Solutions Provider"'
)

# Update page header subtitle
about = about.replace(
    '15+ Years of Precision Optical Manufacturing Excellence',
    'Precision Optical Solutions Provider'
)

# Update aboutDesc
about = about.replace(
    'Beijing Hengdingguang Technology Co., Ltd. is a professional company specializing in R&amp;D, production, and sales of optical components. As the core operator of the PhotonEdge brand, we are committed to providing high-quality precision optical components and solutions to global customers.',
    'PhotonEdge helps global companies solve precision optical challenges — from material selection and coating design to custom manufacturing and quality assurance. As the core operator of the PhotonEdge brand, we deliver end-to-end optical solutions, not just components.'
)

# Update aboutMore
about = about.replace(
    'With years of experience in the optical industry, we have established long-term partnerships with customers in Europe, North America, Asia Pacific, and other regions. Our products are widely used in medical equipment, laser technology, scientific research, industrial manufacturing, and defense industries.',
    'We partner with companies across laser systems, semiconductor metrology, medical devices, and scientific research — providing engineering support from initial concept through volume production. Our global clients in Europe, North America, and Asia-Pacific trust us for consistent quality, technical expertise, and reliable delivery.'
)

# Update nav in about.html - same pattern as index
about_old_nav = '''<ul class="nav-list">
                    <li><a href="/" class="nav-link " data-i18n="navHome">Home</a></li>
                    <li><a href="/products.html" class="nav-link " data-i18n="navProducts">Products</a></li>
                    <li><a href="/about.html" class="nav-link " data-i18n="navAbout">About Us</a></li>'''

about_new_nav = '''<ul class="nav-list">
                    <li><a href="/" class="nav-link" data-i18n="navHome">Home</a></li>
                    <li><a href="/products.html" class="nav-link" data-i18n="navProducts">Products</a></li>
                    <li><a href="/solutions/" class="nav-link" data-i18n="navSolutions">Solutions</a></li>
                    <li><a href="/knowledge-center/" class="nav-link" data-i18n="navKnowledgeCenter">Knowledge Center</a></li>
                    <li><a href="/about.html" class="nav-link" data-i18n="navAbout">About Us</a></li>'''

about = about.replace(about_old_nav, about_new_nav)

# Simplify about nav - remove FAQ, Downloads, Case Studies, News
about = about.replace(
    '''<li><a href="/faq.html" class="nav-link " data-i18n="navFAQ">FAQ</a></li>
                    <li><a href="/blog.html" class="nav-link " data-i18n="navBlog">Blog</a></li>
                    <li><a href="/downloads.html" class="nav-link" data-i18n="navDownloads">Downloads</a></li>
                    <li><a href="/case-studies.html" class="nav-link" data-i18n="navCaseStudies">Case Studies</a></li>
                    <li><a href="/contact.html" class="nav-link " data-i18n="navContact">Contact</a></li>
                    <li><a href="/news.html" class="nav-link" data-i18n="navNews">News</a></li>''',
    '''<li><a href="/blog.html" class="nav-link" data-i18n="navBlog">Blog</a></li>
                    <li><a href="/contact.html" class="nav-link" data-i18n="navContact">Contact</a></li>'''
)

# Update about footer
about = about.replace(
    'Precision Optical Components Supplier',
    'Precision Optical Solutions Provider'
)

write_file(about_path, about)

# ============================================================
# 3. Update translations.js
# ============================================================
print('=== Updating translations.js ===')
trans_path = os.path.join(BASE, 'js', 'translations.js')
trans = read_file(trans_path)

# Find the en: { section and add new keys after the first line of it
# Add new keys at the start of en: block
new_en_keys = '''en: {
        // V81 - New navigation items
        navSolutions: "Solutions",
        navKnowledgeCenter: "Knowledge Center",
        // V81 - Hero
        heroCTA1: "Get Engineering Support",
        heroCTA2: "Explore Solutions",
        // V81 - Why PhotonEdge
        whyPETitle: "Why PhotonEdge",
        whyPE1Title: "Engineering Support",
        whyPE1Desc: "Material selection, coating design, optical optimization \\u2014 our engineers help you from concept to production",
        whyPE2Title: "Custom Solutions",
        whyPE2Desc: "From prototype to volume production, any specification \\u2014 we design and manufacture to your exact requirements",
        whyPE3Title: "Quality Assured",
        whyPE3Desc: "ISO 9001 & 14001 certified with full inspection reports \\u2014 every component meets your specifications",
        whyPE4Title: "Global Delivery",
        whyPE4Desc: "Reliable shipping to North America, Europe, and Asia \\u2014 on-time delivery you can count on",
        // V81 - Home Industries
        homeIndustriesTitle: "Industries We Serve",
        homeIndustriesSubtitle: "We understand the unique optical challenges of your industry",
        homeIndustryLaser: "Laser Systems",
        homeIndustryLaserDesc: "High-LIDT coatings and low-absorption optics for high-power applications",
        homeIndustrySemi: "Semiconductor",
        homeIndustrySemiDesc: "Sub-nanometer roughness and cleanroom-grade precision optics",
        homeIndustryMedical: "Medical",
        homeIndustryMedicalDesc: "Biocompatible, traceable optics with batch consistency",
        homeIndustryResearch: "Research",
        homeIndustryResearchDesc: "Ultra-precision and exotic material optics for cutting-edge experiments",
        // V81 - Process
        processTitle: "Our Process \\u2014 From Drawing to Delivery",
        processSubtitle: "Every component follows our rigorous 8-step quality process",
        processStep1: "1. Customer Requirements",
        processStep1Desc: "Detailed specification review and feasibility assessment",
        processStep2: "2. Technical Review",
        processStep2Desc: "Engineering analysis and design optimization",
        processStep3: "3. Material Selection",
        processStep3Desc: "Optimal substrate and glass grade matching your wavelength",
        processStep4: "4. Precision Machining",
        processStep4Desc: "CNC generating and grinding to near-net shape",
        processStep5: "5. Polishing",
        processStep5Desc: "Precision polishing to achieve required surface figure and quality",
        processStep6: "6. Optical Coating",
        processStep6Desc: "Thin-film deposition with spectral verification",
        processStep7: "7. Quality Inspection",
        processStep7Desc: "100% inspection with interferometry and spectrophotometry",
        processStep8: "8. Global Delivery",
        processStep8Desc: "Secure packaging and reliable shipping worldwide",
        // V81 - Featured Knowledge
        featuredKnowledgeTitle: "Optical Engineering Insights",
        featuredKnowledgeSubtitle: "Expert guides that solve real optical engineering problems",
        featuredKnowledgeCTA: "Visit Knowledge Center",
        // V81 - Final CTA
        finalCTATitle: "Start Your Optical Project",
        finalCTASubtitle: "Tell us about your application. Our engineering team will design a solution.",
        finalCTAQuote: "Request Quote",
        finalCTAEngineer: "Talk to Engineer",
        finalCTACustom: "Custom Project",
        // V81 - Solutions page
        solutionsHeroTitle: "Optical Solutions by Industry",
        solutionsHeroSubtitle: "Every application has unique optical challenges. We provide end-to-end solutions \\u2014 from material selection to custom coating \\u2014 tailored to your industry\\u2019s demands.",
        solutionsLaserTitle: "Laser System Optics",
        solutionsLaserDesc: "High-power laser systems demand optics with exceptional damage thresholds, precise reflectivity, and stable performance under thermal load. PhotonEdge provides laser-optimized mirrors, windows, lenses, and beamsplitters with coating solutions for CO\\u2082, Nd:YAG, fiber, excimer, and ultrafast lasers.",
        solutionsChallengesTitle: "Key Challenges We Solve:",
        solutionsRecommendedTitle: "Recommended Components:",
        solutionsLaserChallenge1: "Mirror coating degradation at high power",
        solutionsLaserSolution1: "High-LIDT dielectric coatings",
        solutionsLaserChallenge2: "Thermal lensing in high-energy systems",
        solutionsLaserSolution2: "Low-absorption substrate selection",
        solutionsLaserChallenge3: "Beam quality maintenance",
        solutionsLaserSolution3: "Precision surface figure and roughness",
        solutionsLaserCTA: "Discuss Your Laser Optics Needs",
        solutionsSemiTitle: "Semiconductor & Metrology Optics",
        solutionsSemiDesc: "Wafer inspection, lithography support, and metrology systems require optics with extreme surface quality, sub-nanometer roughness, and exceptional cleanliness. PhotonEdge supplies precision windows, filters, and custom optics meeting semiconductor-grade requirements.",
        solutionsSemiChallenge1: "Particle contamination sensitivity",
        solutionsSemiSolution1: "Class 100 cleanroom packaging",
        solutionsSemiChallenge2: "Sub-nm surface roughness requirements",
        solutionsSemiSolution2: "MRF polishing capability",
        solutionsSemiChallenge3: "Narrow bandpass filtering for inspection",
        solutionsSemiSolution3: "Custom interference filters",
        solutionsSemiCTA: "Discuss Your Semiconductor Optics Needs",
        solutionsMedicalTitle: "Medical & Life Sciences Optics",
        solutionsMedicalDesc: "Medical imaging, endoscopy, microscopy, and diagnostic equipment require biocompatible, high-transmission optics with consistent quality across production batches. PhotonEdge delivers medical-grade optical components with full traceability and regulatory support.",
        solutionsMedicalChallenge1: "Batch-to-batch consistency",
        solutionsMedicalSolution1: "Statistical process control",
        solutionsMedicalChallenge2: "Bio-compatibility requirements",
        solutionsMedicalSolution2: "Material certification and documentation",
        solutionsMedicalChallenge3: "Miniaturized optics for endoscopes",
        solutionsMedicalSolution3: "Precision small-diameter manufacturing",
        solutionsMedicalCTA: "Discuss Your Medical Optics Needs",
        solutionsResearchTitle: "Scientific Research & Quantum Optics",
        solutionsResearchDesc: "Research laboratories and quantum optics experiments demand the highest specification optics \\u2014 ultra-high flatness, extreme surface quality, and exotic materials. PhotonEdge supports cutting-edge research with custom optics and fast turnaround.",
        solutionsResearchChallenge1: "Ultra-precise surface figure",
        solutionsResearchSolution1: "\\u03bb/20 and better flatness",
        solutionsResearchChallenge2: "Exotic material requirements",
        solutionsResearchSolution2: "CaF\\u2082, ZnSe, Ge, Sapphire sourcing",
        solutionsResearchChallenge3: "Fast prototype turnaround",
        solutionsResearchSolution3: "Expedited manufacturing options",
        solutionsResearchCTA: "Discuss Your Research Optics Needs",
        solutionsBottomCTATitle: "Don\\u2019t See Your Industry?",
        solutionsBottomCTADesc: "We solve optical challenges across many fields. Tell us your application, and our engineering team will design a solution.",
        solutionsBottomCTABtn: "Talk to Our Engineers",
        // V81 - Knowledge Center page
        kcHeroTitle: "Optical Knowledge Center",
        kcHeroSubtitle: "Your comprehensive resource for optical engineering \\u2014 from material selection to system design. Every article solves a real problem.",
        kcViewAllArticles: "View All Articles \\u2192",
        // V81 - Footer update
        '''

trans = trans.replace('en: {\n        \n', new_en_keys)

# Now add Chinese translations
# Find zh: { section
new_zh_keys = '''zh: {
        // V81 - New navigation items
        "navSolutions": "解决方案",
        "navKnowledgeCenter": "知识中心",
        // V81 - Hero
        "heroCTA1": "获取工程支持",
        "heroCTA2": "探索解决方案",
        // V81 - Why PhotonEdge
        "whyPETitle": "为什么选择恒鼎光",
        "whyPE1Title": "工程支持",
        "whyPE1Desc": "材料选择、镀膜设计、光学优化 —— 我们的工程师从概念到生产全程协助",
        "whyPE2Title": "定制方案",
        "whyPE2Desc": "从原型到量产，任何规格 —— 我们按您的精确要求设计和制造",
        "whyPE3Title": "质量保证",
        "whyPE3Desc": "ISO 9001和14001认证，提供完整检验报告 —— 每个元件都符合您的规格",
        "whyPE4Title": "全球交付",
        "whyPE4Desc": "可靠运送至北美、欧洲和亚洲 —— 准时交付值得信赖",
        // V81 - Home Industries
        "homeIndustriesTitle": "我们服务的行业",
        "homeIndustriesSubtitle": "我们了解您行业的独特光学挑战",
        "homeIndustryLaser": "激光系统",
        "homeIndustryLaserDesc": "高LIDT镀膜和低吸收光学元件，适用于高功率应用",
        "homeIndustrySemi": "半导体",
        "homeIndustrySemiDesc": "亚纳米粗糙度和洁净室级精密光学元件",
        "homeIndustryMedical": "医疗",
        "homeIndustryMedicalDesc": "生物相容、可追溯的批量一致性光学元件",
        "homeIndustryResearch": "科研",
        "homeIndustryResearchDesc": "超精密和特殊材料光学元件，用于前沿实验",
        // V81 - Process
        "processTitle": "我们的流程 —— 从图纸到交付",
        "processSubtitle": "每个元件遵循我们严格的8步质量流程",
        "processStep1": "1. 客户需求",
        "processStep1Desc": "详细规格审查和可行性评估",
        "processStep2": "2. 技术评审",
        "processStep2Desc": "工程分析和设计优化",
        "processStep3": "3. 材料选择",
        "processStep3Desc": "匹配您波长的最佳基底和玻璃等级",
        "processStep4": "4. 精密加工",
        "processStep4Desc": "CNC成型和研磨至近净形",
        "processStep5": "5. 抛光",
        "processStep5Desc": "精密抛光达到所需面形和表面质量",
        "processStep6": "6. 光学镀膜",
        "processStep6Desc": "薄膜沉积与光谱验证",
        "processStep7": "7. 质量检验",
        "processStep7Desc": "100%干涉仪和分光光度计检测",
        "processStep8": "8. 全球交付",
        "processStep8Desc": "安全包装和可靠的全球运输",
        // V81 - Featured Knowledge
        "featuredKnowledgeTitle": "光学工程洞察",
        "featuredKnowledgeSubtitle": "解决实际光学工程问题的专家指南",
        "featuredKnowledgeCTA": "访问知识中心",
        // V81 - Final CTA
        "finalCTATitle": "启动您的光学项目",
        "finalCTASubtitle": "告诉我们您的应用，我们的工程团队将为您设计解决方案。",
        "finalCTAQuote": "请求报价",
        "finalCTAEngineer": "与工程师交流",
        "finalCTACustom": "定制项目",
        // V81 - Solutions page
        "solutionsHeroTitle": "按行业分类的光学解决方案",
        "solutionsHeroSubtitle": "每个应用都有独特的光学挑战。我们提供端到端解决方案 —— 从材料选择到定制镀膜 —— 为您行业的需求量身定制。",
        "solutionsLaserTitle": "激光系统光学",
        "solutionsLaserDesc": "高功率激光系统需要具有卓越损伤阈值、精确反射率和热负载下稳定性能的光学元件。恒鼎光提供激光优化的反射镜、窗口、透镜和分束器，配备CO\\u2082、Nd:YAG、光纤、准分子和超快激光的镀膜解决方案。",
        "solutionsChallengesTitle": "我们解决的关键挑战：",
        "solutionsRecommendedTitle": "推荐产品：",
        "solutionsLaserChallenge1": "高功率下反射镜镀膜退化",
        "solutionsLaserSolution1": "高LIDT介电镀膜",
        "solutionsLaserChallenge2": "高能系统中的热透镜效应",
        "solutionsLaserSolution2": "低吸收基底选择",
        "solutionsLaserChallenge3": "光束质量维持",
        "solutionsLaserSolution3": "精密面形和粗糙度",
        "solutionsLaserCTA": "讨论您的激光光学需求",
        "solutionsSemiTitle": "半导体与计量光学",
        "solutionsSemiDesc": "晶圆检测、光刻支持和计量系统需要具有极端表面质量、亚纳米粗糙度和卓越洁净度的光学元件。恒鼎光提供满足半导体级要求的精密窗口、滤光片和定制光学元件。",
        "solutionsSemiChallenge1": "颗粒污染敏感性",
        "solutionsSemiSolution1": "百级洁净室包装",
        "solutionsSemiChallenge2": "亚纳米表面粗糙度要求",
        "solutionsSemiSolution2": "MRF抛光能力",
        "solutionsSemiChallenge3": "检测用窄带通滤波",
        "solutionsSemiSolution3": "定制干涉滤光片",
        "solutionsSemiCTA": "讨论您的半导体光学需求",
        "solutionsMedicalTitle": "医疗与生命科学光学",
        "solutionsMedicalDesc": "医学成像、内窥镜、显微镜和诊断设备需要生物相容、高透射的光学元件，且批次间质量一致。恒鼎光提供具有完整可追溯性和法规支持的医疗级光学元件。",
        "solutionsMedicalChallenge1": "批次间一致性",
        "solutionsMedicalSolution1": "统计过程控制",
        "solutionsMedicalChallenge2": "生物相容性要求",
        "solutionsMedicalSolution2": "材料认证和文档",
        "solutionsMedicalChallenge3": "内窥镜微型化光学",
        "solutionsMedicalSolution3": "精密小直径制造",
        "solutionsMedicalCTA": "讨论您的医疗光学需求",
        "solutionsResearchTitle": "科研与量子光学",
        "solutionsResearchDesc": "研究实验室和量子光学实验需要最高规格的光学元件 —— 超高平整度、极端表面质量和特殊材料。恒鼎光以定制光学元件和快速周转支持前沿研究。",
        "solutionsResearchChallenge1": "超精密面形",
        "solutionsResearchSolution1": "\\u03bb/20及更高平整度",
        "solutionsResearchChallenge2": "特殊材料需求",
        "solutionsResearchSolution2": "CaF\\u2082、ZnSe、Ge、蓝宝石供应",
        "solutionsResearchChallenge3": "快速原型周转",
        "solutionsResearchSolution3": "加急制造选项",
        "solutionsResearchCTA": "讨论您的科研光学需求",
        "solutionsBottomCTATitle": "没看到您的行业？",
        "solutionsBottomCTADesc": "我们解决许多领域的光学挑战。告诉我们您的应用，我们的工程团队将设计解决方案。",
        "solutionsBottomCTABtn": "与我们的工程师交流",
        // V81 - Knowledge Center page
        "kcHeroTitle": "光学知识中心",
        "kcHeroSubtitle": "您全面的光学工程资源 —— 从材料选择到系统设计。每篇文章解决一个实际问题。",
        "kcViewAllArticles": "查看所有文章 \\u2192",
        // V81 - Footer
        '''

trans = trans.replace('zh: {\n        \n', new_zh_keys)

# Update existing translation keys
# heroTitle
trans = trans.replace(
    'heroTitle: "Precision Optical Components for Demanding Applications"',
    'heroTitle: "Precision Optical Solutions for Laser, Semiconductor & Advanced Imaging"'
)

# heroSubtitle
trans = trans.replace(
    'heroSubtitle: "15+ years of manufacturing excellence. 500+ global clients trust PhotonEdge for lenses, mirrors, windows, prisms & custom solutions."',
    'heroSubtitle: "From material selection to custom coating \\u2014 we solve your optical challenges. Prototype to volume production."'
)

# footerDesc
trans = trans.replace(
    'footerDesc: "Precision Optical Components Supplier"',
    'footerDesc: "Precision Optical Solutions Provider"'
)

# aboutPageTitle - keep
# aboutPageSubtitle
trans = trans.replace(
    'aboutPageSubtitle: "15+ Years of Precision Optical Manufacturing Excellence"',
    'aboutPageSubtitle: "Precision Optical Solutions Provider"'
)

# aboutDesc
trans = trans.replace(
    'aboutDesc: "Beijing Hengdingguang Technology Co., Ltd. is a professional company specializing in R&D, production, and sales of optical components. As the core operator of the PhotonEdge brand, we are committed to providing high-quality precision optical components and solutions to global customers."',
    'aboutDesc: "PhotonEdge helps global companies solve precision optical challenges \\u2014 from material selection and coating design to custom manufacturing and quality assurance. As the core operator of the PhotonEdge brand, we deliver end-to-end optical solutions, not just components."'
)

# aboutMore
trans = trans.replace(
    'aboutMore: "With years of experience in the optical industry, we have established long-term partnerships with customers in Europe, North America, Asia Pacific, and other regions. Our products are widely used in medical equipment, laser technology, scientific research, industrial manufacturing, and defense industries."',
    'aboutMore: "We partner with companies across laser systems, semiconductor metrology, medical devices, and scientific research \\u2014 providing engineering support from initial concept through volume production. Our global clients in Europe, North America, and Asia-Pacific trust us for consistent quality, technical expertise, and reliable delivery."'
)

# Chinese heroTitle
trans = trans.replace(
    '"heroTitle": "精密光学元件，满足苛刻应用"',
    '"heroTitle": "激光、半导体与先进成像的精密光学解决方案"'
)

# Chinese heroSubtitle
trans = trans.replace(
    '"heroSubtitle": "15年以上制造经验。500+全球客户信赖恒鼎光提供的透镜、反射镜、窗口、棱镜和定制解决方案。"',
    '"heroSubtitle": "从材料选择到定制镀膜 —— 我们解决您的光学挑战。从原型到量产。"'
)

# Chinese footerDesc
trans = trans.replace(
    '"footerDesc": "精密光学元件供应商"',
    '"footerDesc": "精密光学解决方案提供商"'
)

# Chinese aboutPageSubtitle
trans = trans.replace(
    '"aboutPageSubtitle": "15+年精密光学制造卓越经验"',
    '"aboutPageSubtitle": "精密光学解决方案提供商"'
)

# Chinese aboutDesc
trans = trans.replace(
    '"aboutDesc": "北京恒鼎光科技有限公司是一家专业从事光学元件研发、生产和销售的公司。作为恒鼎光品牌的核心运营者，我们致力于为全球客户提供高质量的精密光学元件和解决方案。"',
    '"aboutDesc": "恒鼎光帮助全球公司解决精密光学挑战 —— 从材料选择和镀膜设计到定制制造和质量保证。作为恒鼎光品牌的核心运营者，我们提供端到端的光学解决方案，而不仅仅是元件。"'
)

# Chinese aboutMore
trans = trans.replace(
    '"aboutMore": "凭借多年光学行业的经验，我们与欧洲、北美、亚太等地区的客户建立了长期合作关系。我们的产品广泛应用于医疗设备、激光技术、科学研究、工业制造和国防工业。"',
    '"aboutMore": "我们与激光系统、半导体计量、医疗设备和科学研究的公司合作 —— 从初始概念到量产提供工程支持。我们在欧洲、北美和亚太地区的全球客户信赖我们的稳定质量、技术专长和可靠交付。"'
)

write_file(trans_path, trans)

# ============================================================
# 4. Update sitemap.xml
# ============================================================
print('=== Updating sitemap.xml ===')
sitemap_path = os.path.join(BASE, 'sitemap.xml')
sitemap = read_file(sitemap_path)

# Add Solutions and Knowledge Center URLs
new_urls = '''  <url>
    <loc>https://photonedgeoptics.com/solutions/</loc>
    <lastmod>2026-08-02</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://photonedgeoptics.com/knowledge-center/</loc>
    <lastmod>2026-08-02</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
'''

# Insert after the first URL entry (about.html)
sitemap = sitemap.replace(
    '  </url>\n  <url>\n    <loc>https://photonedgeoptics.com/applications.html',
    '  </url>\n' + new_urls + '  <url>\n    <loc>https://photonedgeoptics.com/applications.html'
)

# Update main page lastmod dates to 2026-08-02
sitemap = sitemap.replace('<lastmod>2026-07-31</lastmod>', '<lastmod>2026-08-02</lastmod>')

write_file(sitemap_path, sitemap)

# ============================================================
# 5. Update navigation in other HTML files
# ============================================================
print('=== Updating navigation in other HTML files ===')

# Navigation update pattern for non-index pages
def update_nav_in_file(filepath, active_page):
    """Update navigation in a file to match V81 nav structure"""
    try:
        content = read_file(filepath)
    except:
        print(f'  Skip (cannot read): {filepath}')
        return

    original = content

    # Find the nav-list and replace it
    # Pattern: from <ul class="nav-list"> to </ul> (first occurrence after nav-list)

    # Build new nav based on active page
    active_class = ' class="nav-link active"'
    inactive_class = ' class="nav-link"'

    def nav_item(href, i18n_key, text, is_active):
        cls = active_class if is_active else inactive_class
        return '<li><a href="' + href + '"' + cls + ' data-i18n="' + i18n_key + '">' + text + '</a></li>'

    new_nav_list = '<ul class="nav-list">\n' + \
        nav_item('/', 'navHome', 'Home', active_page == 'home') + '\n' + \
        nav_item('/products.html', 'navProducts', 'Products', active_page == 'products') + '\n' + \
        nav_item('/solutions/', 'navSolutions', 'Solutions', active_page == 'solutions') + '\n' + \
        nav_item('/knowledge-center/', 'navKnowledgeCenter', 'Knowledge Center', active_page == 'knowledge-center') + '\n' + \
        '''<li class="nav-dropdown" onclick="if(window.innerWidth<=768){event.stopPropagation();this.classList.toggle('open')}">
                        <a href="/calculator.html" class="nav-link" data-i18n="navTools">Tools</a>
                        <div class="dropdown-menu">
                            <a href="/calculator.html" class="dropdown-item">
                                <span class="dropdown-icon">&#129518;</span>
                                <span data-i18n="menuCalculators">Optical Calculators</span>
                            </a>
                            <a href="/ray-tracer.html" class="dropdown-item">
                                <span class="dropdown-icon">&#128300;</span>
                                <span data-i18n="menuRayTracer">Ray Tracer Simulator</span>
                            </a>
                            <a href="/materials.html" class="dropdown-item">
                                <span class="dropdown-icon">&#128202;</span>
                                <span data-i18n="menuMaterials">Materials Database</span>
                            </a>
                            <a href="/product-advisor.html" class="dropdown-item">
                                <span class="dropdown-icon">&#127919;</span>
                                <span data-i18n="menuSelector">Product Selector</span>
                            </a>
                        </div>
                    </li>''' + '\n' + \
        nav_item('/about.html', 'navAbout', 'About Us', active_page == 'about') + '\n' + \
        nav_item('/blog.html', 'navBlog', 'Blog', active_page == 'blog') + '\n' + \
        nav_item('/contact.html', 'navContact', 'Contact', active_page == 'contact') + '\n' + \
        '</ul>'

    # Replace old nav-list with new one
    # Find <ul class="nav-list"> ... </ul> and replace
    pattern = r'<ul class="nav-list">.*?</ul>'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_nav_list + content[match.end():]
        if content != original:
            write_file(filepath, content)
        else:
            print(f'  No changes: {filepath}')
    else:
        print(f'  Nav not found: {filepath}')

# Map of files to their active page
nav_files = {
    'products.html': 'products',
    'calculator.html': 'tools',
    'ray-tracer.html': 'tools',
    'materials.html': 'tools',
    'product-advisor.html': 'tools',
    'product-catalog.html': 'products',
    'product-detail.html': 'products',
    'blog.html': 'blog',
    'faq.html': 'faq',
    'contact.html': 'contact',
    'case-studies.html': 'casestudies',
    'compare.html': 'compare',
    'cart.html': 'cart',
    'downloads.html': 'downloads',
    'news.html': 'news',
    'optomechanics.html': 'products',
    'applications.html': 'applications',
}

for filename, active in nav_files.items():
    filepath = os.path.join(BASE, filename)
    if os.path.exists(filepath):
        update_nav_in_file(filepath, active)

# Also update blog post and product pages
for blog_slug in os.listdir(os.path.join(BASE, 'blog')):
    blog_path = os.path.join(BASE, 'blog', blog_slug, 'index.html')
    if os.path.exists(blog_path):
        update_nav_in_file(blog_path, 'blog')

for prod_slug in os.listdir(os.path.join(BASE, 'products')):
    prod_path = os.path.join(BASE, 'products', prod_slug, 'index.html')
    if os.path.exists(prod_path):
        update_nav_in_file(prod_path, 'products')

# Also update news pages
for news_slug in os.listdir(os.path.join(BASE, 'news')):
    news_path = os.path.join(BASE, 'news', news_slug, 'index.html')
    if os.path.exists(news_path):
        update_nav_in_file(news_path, 'news')

# Update footer in all HTML files (global replacement for footerDesc)
print('=== Updating footer across all files ===')
for root, dirs, files in os.walk(BASE):
    for fname in files:
        if fname.endswith('.html'):
            fpath = os.path.join(root, fname)
            try:
                content = read_file(fpath)
                original = content
                content = content.replace(
                    'Precision Optical Components Supplier',
                    'Precision Optical Solutions Provider'
                )
                # Also update any remaining "Manufacturer" references in visible text
                if content != original:
                    write_file(fpath, content)
            except:
                pass

# Also update Solutions and Knowledge Center footer
for page_dir in ['solutions', 'knowledge-center']:
    fpath = os.path.join(BASE, page_dir, 'index.html')
    if os.path.exists(fpath):
        content = read_file(fpath)
        content = content.replace('Precision Optical Components Supplier', 'Precision Optical Solutions Provider')
        write_file(fpath, content)

print('\n=== V81 Update Complete ===')
