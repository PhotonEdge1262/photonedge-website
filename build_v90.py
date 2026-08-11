#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PhotonEdge V90 Build Script
- Homepage 3.0 redesign
- 5 Application pages depth enhancement (sub-applications, specs table, related articles)
- Engineering page enhancement (custom design, tolerance capability, coating, prototype-production)
- 5 Material detail pages (BK7, UV Fused Silica, CaF2, ZnSe, Sapphire)
- Case Studies page population
- Knowledge Center categorization upgrade
- Translation keys update
- Sitemap update
"""

import os
import re
import json
import sys

BASE = '/app/data/所有对话/主对话/PhotonEdge-V90'

def read_file(path):
    with open(os.path.join(BASE, path), 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

# =============================================
# PART 1: Homepage 3.0 Redesign
# =============================================

def build_homepage():
    """Rebuild index.html with new 10-screen structure"""
    content = read_file('index.html')
    
    # We'll replace the body content between <body> and footer
    # Strategy: keep header, footer, scripts; replace everything in between
    
    # Find body start
    body_start = content.find('<body>') + len('<body>')
    # Find footer start
    footer_start = content.find('<footer class="footer">')
    
    new_body = '''
    <header class="header">
        <div class="container">
            <a href="/" class="logo">
    <picture>
        <source srcset="images/logo.webp" type="image/webp">
        <img src="https://photonedgeoptics.com/logo.png" alt="PhotonEdge" width="160" height="40">
    </picture>
</a>
            <nav class="nav">
                <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">&#9776;</button>
                
                <ul class="nav-list">
                    <li><a href="/products.html" class="nav-link" data-i18n="navProducts">Products</a></li>
                    <li><a href="/applications.html" class="nav-link" data-i18n="navApplications">Applications</a></li>
                    <li><a href="/engineering.html" class="nav-link" data-i18n="navEngineering">Engineering</a></li>
                    <li><a href="/knowledge-center/" class="nav-link" data-i18n="navKnowledgeCenter">Knowledge Center</a></li>
                    <li><a href="/ai-optical-engineer.html" class="nav-link" data-i18n="navAIOptical">AI Optical Engineer</a></li>
                    <li><a href="/about.html" class="nav-link" data-i18n="navAbout">About</a></li>
                    <li><a href="/contact.html" class="btn btn-primary nav-cta-btn" data-i18n="navRFQ" style="padding:8px 20px;border-radius:6px;font-size:14px;color:white;text-decoration:none;">Request Engineering Review</a></li>
                </ul>
                <a href="/compare.html" class="cart-icon" title="Compare" style="margin-left: 15px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                    <span class="cart-badge" id="compareBadge">0</span>
                </a>
                <a href="/cart.html" class="cart-icon" title="Shopping Cart">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
                    <span class="cart-badge" id="cartBadge">0</span>
                </a>
                <div class="lang-switcher">
                    <button class="lang-btn notranslate active" onclick="setLanguage('en')">EN</button>
                    <button class="lang-btn notranslate" onclick="setLanguage('zh')">中文</button>
                </div>
            </nav>
        </div>
    </header>

    
    <div class="request-quote-float">
        <a href="/contact.html" class="quote-btn">
            <span class="quote-icon">&#9993;</span>
            <span data-i18n="navRFQ">Request Engineering Review</span>
        </a>
    </div>

<!-- ============ SCREEN 1: HERO + AI Mini Entry ============ -->
<section class="hero v90-hero">
    <div class="container">
        <div class="v90-hero-grid">
            <div class="v90-hero-text">
                <h1 data-i18n="v90HeroTitle">Precision Optical Components for Advanced Photonics Systems</h1>
                <p class="subtitle" data-i18n="v90HeroSubtitle">From material selection to volume production — we engineer optical solutions that perform in the real world, not just on spec sheets.</p>
                <!-- Trust Bar -->
                <div class="hero-trust-bar v90-trust-bar">
                    <div class="trust-item">
                        <span class="trust-number">15+ Years</span>
                        <span class="trust-label">Optical Engineering</span>
                    </div>
                    <div class="trust-divider"></div>
                    <div class="trust-item">
                        <span class="trust-number">30+ Materials</span>
                        <span class="trust-label">Optical Materials</span>
                    </div>
                    <div class="trust-divider"></div>
                    <div class="trust-item">
                        <span class="trust-number">ISO 9001</span>
                        <span class="trust-label">Quality System</span>
                    </div>
                    <div class="trust-divider"></div>
                    <div class="trust-item">
                        <span class="trust-number">Custom</span>
                        <span class="trust-label">Engineering Support</span>
                    </div>
                </div>
                <!-- CTA Buttons -->
                <div class="hero-btns v90-hero-btns">
                    <a href="/contact.html" class="btn btn-primary" data-i18n="v90HeroCTA1">Talk With Optical Engineer</a>
                    <a href="/applications.html" class="btn btn-secondary" data-i18n="v90HeroCTA2">Explore Solutions</a>
                </div>
            </div>
            <div class="v90-hero-ai-card">
                <div class="v90-ai-badge">
                    <span style="background: linear-gradient(135deg,#3b82f6,#8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight:700;">AI Optical Engineer</span>
                </div>
                <p class="v90-ai-desc" data-i18n="v90HeroAIDesc">Describe your optical requirement — get instant material, coating and tolerance recommendations.</p>
                <div class="v90-ai-input-row">
                    <input type="text" class="v90-ai-input" data-i18n-placeholder="v90HeroAIPlaceholder" placeholder="e.g., 532nm laser window for industrial use" onclick="window.location.href='/ai-optical-engineer.html'" readonly>
                    <button class="v90-ai-btn" onclick="window.location.href='/ai-optical-engineer.html'" data-i18n="v90HeroAIButton">Start Analysis</button>
                </div>
                <div class="v90-ai-samples">
                    <span class="v90-ai-chip" onclick="window.location.href='/ai-optical-engineer.html'">Laser window</span>
                    <span class="v90-ai-chip" onclick="window.location.href='/ai-optical-engineer.html'">Imaging lens</span>
                    <span class="v90-ai-chip" onclick="window.location.href='/ai-optical-engineer.html'">Coating design</span>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ============ SCREEN 2: OPTICAL CHALLENGES ============ -->
<section class="v90-challenges" style="padding: 80px 0; background: #f8fafc;">
    <div class="container">
        <div style="text-align: center; margin-bottom: 50px;">
            <span class="v90-section-tag" data-i18n="v90ChallengesTag">Industry Solutions</span>
            <h2 class="v90-section-title" data-i18n="v90ChallengesTitle">Optical Challenges We Solve</h2>
            <p class="v90-section-subtitle" data-i18n="v90ChallengesSubtitle">Every industry has unique optical demands. We engineer components that address your specific constraints — from high-power lasers to ultra-precise inspection systems.</p>
        </div>
        <div class="v90-challenges-grid">
            <!-- Laser Systems -->
            <div class="v90-challenge-card">
                <div class="v90-challenge-icon" style="background: linear-gradient(135deg, #fef3c7, #fde68a);">
                    &#128300;
                </div>
                <h3 class="v90-challenge-title" data-i18n="v90ChallengeLaserTitle">Laser Systems</h3>
                <div class="v90-challenge-pain">
                    <h4 data-i18n="v90ChallengePainLabel">Key Challenges</h4>
                    <ul>
                        <li data-i18n="v90ChallengeLaserPain1">Thermal lensing under high-power CW operation</li>
                        <li data-i18n="v90ChallengeLaserPain2">Laser-induced damage at coating interfaces</li>
                        <li data-i18n="v90ChallengeLaserPain3">Beam quality degradation from surface irregularities</li>
                    </ul>
                </div>
                <div class="v90-challenge-solution">
                    <h4 data-i18n="v90ChallengeSolutionLabel">Our Solution</h4>
                    <p data-i18n="v90ChallengeLaserSolution">Fused silica and ZnSe optics with high-LIDT coatings. Engineered for thermal stability from 100W to multi-kilowatt systems.</p>
                </div>
                <a href="/applications/laser-optics/" class="v90-challenge-btn" data-i18n="v90ChallengeLaserBtn">Explore Laser Solutions &rarr;</a>
            </div>
            <!-- Semiconductor -->
            <div class="v90-challenge-card">
                <div class="v90-challenge-icon" style="background: linear-gradient(135deg, #dbeafe, #bfdbfe);">
                    &#128187;
                </div>
                <h3 class="v90-challenge-title" data-i18n="v90ChallengeSemiTitle">Semiconductor Equipment</h3>
                <div class="v90-challenge-pain">
                    <h4 data-i18n="v90ChallengePainLabel">Key Challenges</h4>
                    <ul>
                        <li data-i18n="v90ChallengeSemiPain1">Sub-nanometer flatness for wafer inspection optics</li>
                        <li data-i18n="v90ChallengeSemiPain2">UV-grade material purity to avoid solarization</li>
                        <li data-i18n="v90ChallengeSemiPain3">Particle-free cleanroom-compatible packaging</li>
                    </ul>
                </div>
                <div class="v90-challenge-solution">
                    <h4 data-i18n="v90ChallengeSolutionLabel">Our Solution</h4>
                    <p data-i18n="v90ChallengeSemiSolution">UV fused silica optics with &#955;/20 flatness. Super-polished surfaces with Class 100 cleanroom inspection and packaging.</p>
                </div>
                <a href="/applications/semiconductor-inspection/" class="v90-challenge-btn" data-i18n="v90ChallengeSemiBtn">Explore Semiconductor Solutions &rarr;</a>
            </div>
            <!-- Medical Imaging -->
            <div class="v90-challenge-card">
                <div class="v90-challenge-icon" style="background: linear-gradient(135deg, #fce7f3, #fbcfe8);">
                    &#10084;
                </div>
                <h3 class="v90-challenge-title" data-i18n="v90ChallengeMedicalTitle">Medical Imaging</h3>
                <div class="v90-challenge-pain">
                    <h4 data-i18n="v90ChallengePainLabel">Key Challenges</h4>
                    <ul>
                        <li data-i18n="v90ChallengeMedicalPain1">Biocompatible materials for patient-contact optics</li>
                        <li data-i18n="v90ChallengeMedicalPain2">High-resolution imaging requires low distortion</li>
                        <li data-i18n="v90ChallengeMedicalPain3">Sterilization-resistant coatings and materials</li>
                    </ul>
                </div>
                <div class="v90-challenge-solution">
                    <h4 data-i18n="v90ChallengeSolutionLabel">Our Solution</h4>
                    <p data-i18n="v90ChallengeMedicalSolution">Precision lenses and windows with medical-grade coatings. Sapphire and fused silica options for sterilizable systems.</p>
                </div>
                <a href="/applications/medical-imaging/" class="v90-challenge-btn" data-i18n="v90ChallengeMedicalBtn">Explore Medical Solutions &rarr;</a>
            </div>
        </div>
    </div>
</section>

<!-- ============ SCREEN 3: CORE PRODUCTS ============ -->
<section class="v90-products" style="padding: 80px 0; background: #ffffff;">
    <div class="container">
        <div style="text-align: center; margin-bottom: 50px;">
            <span class="v90-section-tag" data-i18n="v90ProductsTag">Core Products</span>
            <h2 class="v90-section-title" data-i18n="v90ProductsTitle">Six Optical Component Families</h2>
            <p class="v90-section-subtitle" data-i18n="v90ProductsSubtitle">Engineered in standard and custom specifications across UV, visible, and infrared spectra.</p>
        </div>
        <div class="v90-products-grid">
            <a href="/products.html?category=Optical%20Lenses" class="v90-product-card">
                <div class="v90-product-icon">&#10753;</div>
                <h3 data-i18n="v90ProdLensesTitle">Optical Lenses</h3>
                <p data-i18n="v90ProdLensesDesc">Spherical, aspheric, cylindrical, achromatic, ball and rod lenses for imaging, focusing and collimation.</p>
                <span class="v90-product-link" data-i18n="v90ProdViewSpec">View Specifications &rarr;</span>
            </a>
            <a href="/products.html?category=Optical%20Windows" class="v90-product-card">
                <div class="v90-product-icon">&#9673;</div>
                <h3 data-i18n="v90ProdWindowsTitle">Optical Windows</h3>
                <p data-i18n="v90ProdWindowsDesc">Protection windows and substrates in BK7, fused silica, sapphire, CaF&#8322;, ZnSe and other materials.</p>
                <span class="v90-product-link" data-i18n="v90ProdViewSpec">View Specifications &rarr;</span>
            </a>
            <a href="/products.html?category=Optical%20Mirrors" class="v90-product-card">
                <div class="v90-product-icon">&#9672;</div>
                <h3 data-i18n="v90ProdMirrorsTitle">Optical Mirrors</h3>
                <p data-i18n="v90ProdMirrorsDesc">Dielectric, metallic and laser-line mirrors with reflectance up to 99.99% at design wavelength.</p>
                <span class="v90-product-link" data-i18n="v90ProdViewSpec">View Specifications &rarr;</span>
            </a>
            <a href="/products.html?category=Optical%20Filters" class="v90-product-card">
                <div class="v90-product-icon">&#9674;</div>
                <h3 data-i18n="v90ProdFiltersTitle">Optical Filters</h3>
                <p data-i18n="v90ProdFiltersDesc">Bandpass, shortpass, longpass, neutral density and dichroic filters for precise wavelength control.</p>
                <span class="v90-product-link" data-i18n="v90ProdViewSpec">View Specifications &rarr;</span>
            </a>
            <a href="/products.html?category=Optical%20Prisms" class="v90-product-card">
                <div class="v90-product-icon">&#9650;</div>
                <h3 data-i18n="v90ProdPrismsTitle">Optical Prisms</h3>
                <p data-i18n="v90ProdPrismsDesc">Right angle, penta, dove, dispersing, cube beamsplitter and polarizing prisms for beam manipulation.</p>
                <span class="v90-product-link" data-i18n="v90ProdViewSpec">View Specifications &rarr;</span>
            </a>
            <a href="/products.html?category=Waveplates%20%26%20Polarizers" class="v90-product-card">
                <div class="v90-product-icon">&#9671;</div>
                <h3 data-i18n="v90ProdWaveplatesTitle">Waveplates &amp; Polarizers</h3>
                <p data-i18n="v90ProdWaveplatesDesc">Zero-order and multi-order waveplates, polarizers and retarders for polarization control.</p>
                <span class="v90-product-link" data-i18n="v90ProdViewSpec">View Specifications &rarr;</span>
            </a>
        </div>
    </div>
</section>

<!-- ============ SCREEN 4: WHY PHOTONEDGE ============ -->
<section class="v90-why" style="padding: 80px 0; background: #f8fafc;">
    <div class="container">
        <div style="text-align: center; margin-bottom: 50px;">
            <span class="v90-section-tag" data-i18n="v90WhyTag">Why PhotonEdge</span>
            <h2 class="v90-section-title" data-i18n="v90WhyTitle">Engineering Expertise You Can Measure</h2>
            <p class="v90-section-subtitle" data-i18n="v90WhySubtitle">We do not just sell components — we help engineers solve optical problems.</p>
        </div>
        <div class="v90-why-grid">
            <div class="v90-why-card">
                <div class="v90-why-number">15+</div>
                <h3 data-i18n="v90Why1Title">Years of Optical Experience</h3>
                <p data-i18n="v90Why1Desc">Founded by optical engineers. Thousands of custom designs delivered for laser, semiconductor and medical systems.</p>
            </div>
            <div class="v90-why-card">
                <div class="v90-why-number">30+</div>
                <h3 data-i18n="v90Why2Title">Optical Materials Available</h3>
                <p data-i18n="v90Why2Desc">From standard BK7 to exotic IR materials. We select the right material for your wavelength, power and environment.</p>
            </div>
            <div class="v90-why-card">
                <div class="v90-why-number">ISO</div>
                <h3 data-i18n="v90Why3Title">Quality Management System</h3>
                <p data-i18n="v90Why3Desc">ISO 9001:2015 certified. Every component inspected with laser interferometry before it leaves our facility.</p>
            </div>
            <div class="v90-why-card">
                <div class="v90-why-number">Custom</div>
                <h3 data-i18n="v90Why4Title">Engineering Support Included</h3>
                <p data-i18n="v90Why4Desc">Every quote includes a free engineering review. Material selection, coating optimization and tolerance advice at no extra cost.</p>
            </div>
        </div>
    </div>
</section>

<!-- ============ SCREEN 5: MANUFACTURING PROCESS ============ -->
<section class="v90-manufacturing" style="padding: 80px 0; background: #ffffff;">
    <div class="container">
        <div style="text-align: center; margin-bottom: 50px;">
            <span class="v90-section-tag" data-i18n="v90MfgTag">Manufacturing</span>
            <h2 class="v90-section-title" data-i18n="v90MfgTitle">How Precision Optics Are Made</h2>
            <p class="v90-section-subtitle" data-i18n="v90MfgSubtitle">Every optic goes through a controlled 7-step process. Skip a step and you compromise quality.</p>
        </div>
        <div class="v90-mfg-steps">
            <div class="v90-mfg-step">
                <div class="v90-mfg-step-num">01</div>
                <div class="v90-mfg-step-icon">&#128202;</div>
                <h3 data-i18n="v90MfgStep1Title">Material Selection</h3>
                <p data-i18n="v90MfgStep1Desc">Grade-A optical blanks selected for your wavelength, power and environmental requirements.</p>
            </div>
            <div class="v90-mfg-step-arrow">&rarr;</div>
            <div class="v90-mfg-step">
                <div class="v90-mfg-step-num">02</div>
                <div class="v90-mfg-step-icon">&#9881;</div>
                <h3 data-i18n="v90MfgStep2Title">Precision Grinding</h3>
                <p data-i18n="v90MfgStep2Desc">CNC grinding to achieve near-net shape with controlled surface generation.</p>
            </div>
            <div class="v90-mfg-step-arrow">&rarr;</div>
            <div class="v90-mfg-step">
                <div class="v90-mfg-step-num">03</div>
                <div class="v90-mfg-step-icon">&#10024;</div>
                <h3 data-i18n="v90MfgStep3Title">Polishing</h3>
                <p data-i18n="v90MfgStep3Desc">Sub-aperture and full-aperture polishing to achieve nanometer-scale surface finish.</p>
            </div>
            <div class="v90-mfg-step-arrow">&rarr;</div>
            <div class="v90-mfg-step">
                <div class="v90-mfg-step-num">04</div>
                <div class="v90-mfg-step-icon">&#127919;</div>
                <h3 data-i18n="v90MfgStep4Title">Centering</h3>
                <p data-i18n="v90MfgStep4Desc">Precision edging to ensure optical and mechanical axes align within arc-second tolerances.</p>
            </div>
            <div class="v90-mfg-step-arrow">&rarr;</div>
            <div class="v90-mfg-step">
                <div class="v90-mfg-step-num">05</div>
                <div class="v90-mfg-step-icon">&#127912;</div>
                <h3 data-i18n="v90MfgStep5Title">Coating</h3>
                <p data-i18n="v90MfgStep5Desc">Physical vapor deposition coatings — AR, HR, bandpass, dichroic — designed for your specifications.</p>
            </div>
            <div class="v90-mfg-step-arrow">&rarr;</div>
            <div class="v90-mfg-step">
                <div class="v90-mfg-step-num">06</div>
                <div class="v90-mfg-step-icon">&#128269;</div>
                <h3 data-i18n="v90MfgStep6Title">Inspection</h3>
                <p data-i18n="v90MfgStep6Desc">100% inspection with interferometer, spectrophotometer and surface analysis before release.</p>
            </div>
            <div class="v90-mfg-step-arrow">&rarr;</div>
            <div class="v90-mfg-step">
                <div class="v90-mfg-step-num">07</div>
                <div class="v90-mfg-step-icon">&#128230;</div>
                <h3 data-i18n="v90MfgStep7Title">Packaging</h3>
                <p data-i18n="v90MfgStep7Desc">Cleanroom packaging with full inspection documentation. Ready for your assembly line.</p>
            </div>
        </div>
        <div style="text-align: center; margin-top: 40px;">
            <a href="/engineering.html" class="btn btn-primary" data-i18n="v90MfgExploreBtn">Explore Manufacturing Capability &rarr;</a>
        </div>
    </div>
</section>

<!-- ============ SCREEN 6: PRECISION REQUIRES MEASUREMENT ============ -->
<section class="v90-measurement" style="padding: 80px 0; background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: white;">
    <div class="container">
        <div style="text-align: center; margin-bottom: 50px;">
            <span class="v90-section-tag v90-tag-light" data-i18n="v90MeasTag">Quality Assurance</span>
            <h2 class="v90-section-title" style="color: white;" data-i18n="v90MeasTitle">Precision Requires Measurement</h2>
            <p class="v90-section-subtitle" style="color: rgba(255,255,255,0.7);" data-i18n="v90MeasSubtitle">Every component verified to specification. Full inspection data with every shipment.</p>
            <p class="v90-meas-quote" data-i18n="v90MeasTagline">"If you cannot measure it, you cannot guarantee it."</p>
        </div>
        <div class="v90-meas-grid">
            <div class="v90-meas-card">
                <div class="v90-meas-icon">&#128269;</div>
                <h3 data-i18n="v90Meas1Title">Interferometer</h3>
                <p data-i18n="v90Meas1Desc">Wavefront measurement at &#955;/100 resolution. Verifies surface flatness, curvature and transmitted wavefront distortion.</p>
            </div>
            <div class="v90-meas-card">
                <div class="v90-meas-icon">&#127752;</div>
                <h3 data-i18n="v90Meas2Title">Spectrophotometer</h3>
                <p data-i18n="v90Meas2Desc">Spectral transmission and reflection measurement from 190 nm to 25 &#956;m. Validates coating performance across design bandwidth.</p>
            </div>
            <div class="v90-meas-card">
                <div class="v90-meas-icon">&#128270;</div>
                <h3 data-i18n="v90Meas3Title">Surface Inspection</h3>
                <p data-i18n="v90Meas3Desc">MIL-PRF-13830B compliant surface quality inspection. Scratch-dig verification from 60-40 to 10-5 precision grade.</p>
            </div>
            <div class="v90-meas-card">
                <div class="v90-meas-icon">&#128207;</div>
                <h3 data-i18n="v90Meas4Title">Dimension Measurement</h3>
                <p data-i18n="v90Meas4Desc">High-precision metrology for thickness, diameter, wedge angle and centering. Dimensional tolerances to &#177;0.01 mm.</p>
            </div>
        </div>
    </div>
</section>

<!-- ============ SCREEN 7: TECHNICAL KNOWLEDGE HUB ============ -->
<section class="v90-knowledge" style="padding: 80px 0; background: #f8fafc;">
    <div class="container">
        <div style="text-align: center; margin-bottom: 50px;">
            <span class="v90-section-tag" data-i18n="v90KbTag">Knowledge Center</span>
            <h2 class="v90-section-title" data-i18n="v90KbTitle">Technical Knowledge Hub</h2>
            <p class="v90-section-subtitle" data-i18n="v90KbSubtitle">Practical engineering guides to help you specify, select and deploy optical components with confidence.</p>
        </div>
        <div class="v90-kb-grid" id="v90KnowledgeGrid">
            <!-- Filled by JS from blog data -->
        </div>
        <div style="text-align: center; margin-top: 40px;">
            <a href="/knowledge-center/" class="btn btn-secondary" data-i18n="v90KbAllBtn">View All Technical Resources &rarr;</a>
        </div>
    </div>
</section>

<!-- ============ SCREEN 8: AI OPTICAL ENGINEER ============ -->
<section class="v90-ai-section" style="padding: 80px 0; background: #ffffff;">
    <div class="container">
        <div class="v90-ai-grid">
            <div class="v90-ai-left">
                <span class="v90-section-tag" data-i18n="v90AI2Tag">AI-Powered</span>
                <h2 class="v90-section-title v90-ai-title" data-i18n="v90AI2Title">AI Optical Engineer</h2>
                <p class="v90-ai-desc-full" data-i18n="v90AI2Desc">Describe your optical problem in plain English. Our AI Optical Engineer will recommend materials, coatings, surface quality specs and tolerance ranges — instantly.</p>
                <ul class="v90-ai-benefits">
                    <li data-i18n="v90AI2Benefit1">&#10003; Get material recommendations based on wavelength and power</li>
                    <li data-i18n="v90AI2Benefit2">&#10003; Understand which coatings matter for your application</li>
                    <li data-i18n="v90AI2Benefit3">&#10003; Learn what tolerances are actually necessary</li>
                    <li data-i18n="v90AI2Benefit4">&#10003; Export spec sheet to send to your team</li>
                </ul>
                <a href="/ai-optical-engineer.html" class="btn btn-primary" data-i18n="v90AI2CTA">Start Optical Analysis &rarr;</a>
            </div>
            <div class="v90-ai-mockup">
                <div class="v90-chat-window">
                    <div class="v90-chat-header">
                        <div class="v90-chat-avatar">AI</div>
                        <span>PhotonEdge AI Optical Engineer</span>
                    </div>
                    <div class="v90-chat-body">
                        <div class="v90-chat-msg user-msg">
                            <p data-i18n="v90ChatUserMsg">Need a 532nm laser window for industrial system</p>
                        </div>
                        <div class="v90-chat-msg ai-msg">
                            <p data-i18n="v90ChatAI1"><strong>Material:</strong> UV Fused Silica — high transmission at 532nm, excellent thermal stability, good LIDT.</p>
                            <p data-i18n="v90ChatAI2"><strong>Coating:</strong> Dual-band AR @ 532nm, R&#60;0.2% per surface. Specify LIDT based on your laser power.</p>
                            <p data-i18n="v90ChatAI3"><strong>Surface Quality:</strong> 20-10 scratch-dig for visible laser use. 10-5 for intra-cavity.</p>
                            <p data-i18n="v90ChatAI4">Want a full specification sheet with drawing-ready tolerances?</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ============ SCREEN 9: CASE STUDIES ============ -->
<section class="v90-cases" style="padding: 80px 0; background: #f8fafc;">
    <div class="container">
        <div style="text-align: center; margin-bottom: 50px;">
            <span class="v90-section-tag" data-i18n="v90CaseTag">Case Studies</span>
            <h2 class="v90-section-title" data-i18n="v90CaseTitle">Real Problems, Engineered Solutions</h2>
            <p class="v90-section-subtitle" data-i18n="v90CaseSubtitle">See how we collaborated with engineering teams to solve demanding optical challenges.</p>
        </div>
        <div class="v90-cases-grid">
            <div class="v90-case-card">
                <span class="v90-case-industry" data-i18n="v90Case1Industry">Laser Systems</span>
                <h3 data-i18n="v90Case1Title">UV Laser Window Optimization</h3>
                <div class="v90-case-body">
                    <p><strong data-i18n="v90CaseChallenge">Challenge:</strong> <span data-i18n="v90Case1Challenge">355nm UV laser system experiencing rapid optics degradation and power drop within 1000 hours of operation.</span></p>
                    <p><strong data-i18n="v90CaseSolution">Solution:</strong> <span data-i18n="v90Case1Solution">Switched from standard fused silica to high-purity synthetic silica with solarization-resistant coating. Surface quality upgraded to 10-5.</span></p>
                    <p><strong data-i18n="v90CaseResult">Result:</strong> <span data-i18n="v90Case1Result">Lifetime extended to 8000+ hours with stable transmission. Power fluctuation reduced by 70%.</span></p>
                </div>
                <a href="/case-studies.html" class="v90-case-link" data-i18n="v90CaseReadMore">Read Full Case &rarr;</a>
            </div>
            <div class="v90-case-card">
                <span class="v90-case-industry" data-i18n="v90Case2Industry">Medical Imaging</span>
                <h3 data-i18n="v90Case2Title">Precision Imaging Lens Assembly</h3>
                <div class="v90-case-body">
                    <p><strong data-i18n="v90CaseChallenge">Challenge:</strong> <span data-i18n="v90Case2Challenge">Diagnostic imaging system needed a 3-element lens achieving diffraction-limited performance across 400-700nm with &#60;0.1% distortion.</span></p>
                    <p><strong data-i18n="v90CaseSolution">Solution:</strong> <span data-i18n="v90Case2Solution">Achromatic doublet plus correction element design. BK7 and SF11 glasses with optimized cemented interface. Centration to 30 arc-sec.</span></p>
                    <p><strong data-i18n="v90CaseResult">Result:</strong> <span data-i18n="v90Case2Result">MTF exceeded specification across all fields. Batch consistency maintained over 20 production runs.</span></p>
                </div>
                <a href="/case-studies.html" class="v90-case-link" data-i18n="v90CaseReadMore">Read Full Case &rarr;</a>
            </div>
        </div>
        <div style="text-align: center; margin-top: 40px;">
            <a href="/case-studies.html" class="btn btn-secondary" data-i18n="v90CaseAllBtn">View All Case Studies &rarr;</a>
        </div>
    </div>
</section>

<!-- ============ SCREEN 10: RFQ CTA ============ -->
<section style="padding: 80px 0; background: linear-gradient(135deg,#1e3a5f 0%,#2d5a87 100%); text-align: center; color: white;">
    <div class="container">
        <h2 style="color: white; margin-bottom: 16px; font-size: 36px;" data-i18n="v90RFQTitle">Discuss Your Optical Requirement</h2>
        <p style="color: rgba(255,255,255,0.9); margin-bottom: 40px; font-size: 18px; max-width: 600px; margin-left: auto; margin-right: auto;" data-i18n="v90RFQSubtitle">Tell us about your project. An optical engineer will review and respond with recommendations within 24 hours.</p>
        <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
            <div class="final-cta-item">
                <a href="/contact.html" class="final-cta-btn primary" data-i18n="v90RFQBtn1">Submit Optical Requirement</a>
                <p class="final-cta-desc" data-i18n="v90RFQDesc1">For engineers with clear specifications</p>
            </div>
            <div class="final-cta-item">
                <a href="/contact.html" class="final-cta-btn secondary" data-i18n="v90RFQBtn2">Request Engineering Review</a>
                <p class="final-cta-desc" data-i18n="v90RFQDesc2">Need help with material or coating selection?</p>
            </div>
        </div>
    </div>
</section>
'''
    
    new_content = content[:body_start] + new_body + content[footer_start:]
    write_file('index.html', new_content)
    print("  [OK] Homepage 3.0 built")

# =============================================
# PART 2: Application Pages Enhancement
# =============================================

def build_application_pages():
    """Enhance 5 application pages with sub-applications, specs table, related articles"""
    
    apps = {
        'laser-optics': {
            'title': 'Laser Optics',
            'titleZh': '激光光学',
            'subApps': [
                {
                    'en': {'name': 'Fiber Laser Systems', 'desc': 'High-power fiber lasers require optics with excellent thermal management and high LIDT. Key components: fused silica collimators, beam expanders, and output couplers optimized for 1064-1080nm.', 'products': 'Fused Silica Lenses, Laser Line Mirrors, Beam Expanders'},
                    'zh': {'name': '光纤激光系统', 'desc': '高功率光纤激光器需要具有出色热管理和高激光损伤阈值的光学元件。关键组件：熔融石英准直镜、扩束镜和针对1064-1080nm优化的输出耦合镜。', 'products': '熔融石英透镜、激光线反射镜、扩束镜'}
                },
                {
                    'en': {'name': 'UV Laser Systems', 'desc': 'UV wavelengths demand high-purity materials resistant to solarization. 355nm and 266nm systems require UV-grade fused silica with specialized coatings.', 'products': 'UV Fused Silica Windows, UV AR Coatings, UV Mirrors'},
                    'zh': {'name': '紫外激光系统', 'desc': '紫外波长需要耐日晒老化的高纯度材料。355nm和266nm系统需要带有特殊镀膜的紫外级熔融石英。', 'products': '紫外熔融石英窗口、紫外增透膜、紫外反射镜'}
                },
                {
                    'en': {'name': 'CO₂ Laser Systems', 'desc': '10.6μm CO₂ lasers use ZnSe and GaAs optics for their excellent infrared transmission and thermal conductivity. Critical for cutting, engraving and welding systems.', 'products': 'ZnSe Windows, ZnSe Lenses, CO₂ Laser Mirrors'},
                    'zh': {'name': 'CO₂激光系统', 'desc': '10.6μm CO₂激光器使用ZnSe和GaAs光学元件，具有出色的红外透射率和热导率。对切割、雕刻和焊接系统至关重要。', 'products': 'ZnSe窗口、ZnSe透镜、CO₂激光反射镜'}
                },
                {
                    'en': {'name': 'Semiconductor Lasers', 'desc': 'Diode lasers and semiconductor optical amplifiers need precision collimation and beam shaping. Fast-axis and slow-axis collimation with aspheric and cylindrical lenses.', 'products': 'Aspheric Lenses, Cylindrical Lenses, Facet Windows'},
                    'zh': {'name': '半导体激光器', 'desc': '二极管激光器和半导体光放大器需要精密准直和光束整形。使用非球面和柱面透镜进行快轴和慢轴准直。', 'products': '非球面透镜、柱面透镜、腔面窗口'}
                },
                {
                    'en': {'name': 'Ultrafast Lasers', 'desc': 'Femtosecond and picosecond pulses require low-dispersion optics. GDD-controlled coatings and CaF₂ or fused silica substrates minimize pulse broadening.', 'products': 'Dispersion-Controlled Mirrors, CaF₂ Windows, Ultrafast Optics'},
                    'zh': {'name': '超快激光器', 'desc': '飞秒和皮秒脉冲需要低色散光学元件。群延迟色散控制镀膜和CaF₂或熔融石英基底可最大限度减少脉冲展宽。', 'products': '色散控制反射镜、CaF₂窗口、超快光学'}
                }
            ],
            'specs': [
                {'param': 'Surface Quality', 'en': '20-10 (standard) / 10-5 (precision)', 'zh': '20-10（标准）/ 10-5（精密）'},
                {'param': 'Surface Flatness', 'en': 'λ/4 to λ/20 @ 633nm', 'zh': 'λ/4 至 λ/20 @ 633nm'},
                {'param': 'LIDT (CW)', 'en': '100 W/cm² to 10+ kW/cm² (coating dependent)', 'zh': '100 W/cm² 至 10+ kW/cm²（取决于镀膜）'},
                {'param': 'LIDT (Pulsed)', 'en': '1-15 J/cm² @ 1064nm, 10ns', 'zh': '1-15 J/cm² @ 1064nm, 10ns'},
                {'param': 'Wavefront Distortion', 'en': 'λ/10 to λ/4 transmitted', 'zh': 'λ/10 至 λ/4 透射波前'},
                {'param': 'Coating Types', 'en': 'AR, HR, Partial Reflector, Polarizing', 'zh': '增透膜、高反膜、部分反射膜、偏振膜'}
            ],
            'relatedArticles': ['laser-damage-threshold-guide', 'laser-resonator-optics-output-couplers-guide', 'anti-reflection-coating-selection-guide']
        },
        'semiconductor-inspection': {
            'title': 'Semiconductor Inspection',
            'titleZh': '半导体检测',
            'subApps': [
                {
                    'en': {'name': 'Wafer Inspection', 'desc': 'Automated optical inspection of wafers requires UV and deep-UV optics with exceptional wavefront quality. Imaging resolution down to sub-micron feature sizes.', 'products': 'UV Fused Silica Lenses, UV Windows, Inspection Optics'},
                    'zh': {'name': '晶圆检测', 'desc': '晶圆自动光学检测需要具有出色波前质量的紫外和深紫外光学元件。成像分辨率可达亚微米特征尺寸。', 'products': '紫外熔融石英透镜、紫外窗口、检测光学'}
                },
                {
                    'en': {'name': 'Lithography Alignment', 'desc': 'Photolithography alignment systems rely on precision reference optics and alignment markers. Sub-nanometer stability and minimal thermal drift are essential.', 'products': 'Precision Flat Mirrors, Reference Windows, Alignment Optics'},
                    'zh': {'name': '光刻对准', 'desc': '光刻对准系统依赖于精密参考光学和对准标记。亚纳米级稳定性和最小热漂移至关重要。', 'products': '精密平面反射镜、参考窗口、对准光学'}
                },
                {
                    'en': {'name': 'Metrology Systems', 'desc': 'Optical metrology for critical dimension measurement and overlay. Interferometric and scatterometric techniques demand calibrated, stable optics.', 'products': 'Interferometer Reference Flats, Beam Splitters, Precision Windows'},
                    'zh': {'name': '计量系统', 'desc': '用于关键尺寸测量和套刻的光学计量。干涉和散射测量技术需要经过校准的稳定光学元件。', 'products': '干涉仪参考平片、分束器、精密窗口'}
                },
                {
                    'en': {'name': 'Photomask Inspection', 'desc': 'Reticle and photomask inspection requires deep-UV transmission and ultra-high surface quality. Any defect on the optic is reproduced in the inspection image.', 'products': 'DUV Fused Silica Windows, Super-Polished Optics, Inspection Lenses'},
                    'zh': {'name': '光罩检测', 'desc': '掩模版和光罩检测需要深紫外透射和超高表面质量。光学元件上的任何缺陷都会在检测图像中再现。', 'products': '深紫外熔融石英窗口、超精密抛光光学元件、检测透镜'}
                }
            ],
            'specs': [
                {'param': 'Surface Quality', 'en': '10-5 (standard) / 5-2 (super-polished)', 'zh': '10-5（标准）/ 5-2（超精密抛光）'},
                {'param': 'Surface Flatness', 'en': 'λ/10 to λ/50 @ 633nm', 'zh': 'λ/10 至 λ/50 @ 633nm'},
                {'param': 'Material Purity', 'en': 'Synthetic fused silica, low metal content', 'zh': '合成熔融石英，低金属含量'},
                {'param': 'Transmitted Wavefront', 'en': 'λ/10 to λ/30 RMS', 'zh': 'λ/10 至 λ/30 RMS'},
                {'param': 'Cleanliness', 'en': 'Class 100 cleanroom packaging', 'zh': '100级洁净室包装'},
                {'param': 'Coating Types', 'en': 'UV AR, VIS AR, Dual-Band AR', 'zh': '紫外增透膜、可见增透膜、双波段增透膜'}
            ],
            'relatedArticles': ['bk7-vs-uv-fused-silica', 'optical-component-cleaning-maintenance-guide', 'custom-optics-specification-guide']
        },
        'medical-imaging': {
            'title': 'Medical Imaging',
            'titleZh': '医学成像',
            'subApps': [
                {
                    'en': {'name': 'Ophthalmology', 'desc': 'Eye care and vision correction systems need precision optics with excellent image quality. Intraocular lenses, surgical microscopes, and diagnostic instruments demand biocompatible materials.', 'products': 'Achromatic Lenses, Aspheric Lenses, Sapphire Windows'},
                    'zh': {'name': '眼科学', 'desc': '眼科和视力矫正系统需要具有出色成像质量的精密光学元件。人工晶状体、手术显微镜和诊断仪器需要生物相容性材料。', 'products': '消色差透镜、非球面透镜、蓝宝石窗口'}
                },
                {
                    'en': {'name': 'Endoscopy', 'desc': 'Medical endoscopes and borescopes use miniature optics for imaging through small apertures. GRIN lenses, ball lenses, and fiber bundles deliver high resolution in tight spaces.', 'products': 'Ball Lenses, Rod Lenses, GRIN Lenses'},
                    'zh': {'name': '内窥镜', 'desc': '医用内窥镜和管道镜使用微型光学元件通过小孔径成像。自聚焦透镜、球透镜和光纤束在狭小空间内提供高分辨率。', 'products': '球透镜、棒透镜、自聚焦透镜'}
                },
                {
                    'en': {'name': 'Dental Imaging', 'desc': 'Intraoral cameras, dental microscopes, and imaging systems require compact, high-resolution optics with reliable sterilization compatibility.', 'products': 'Miniature Lenses, Sapphire Windows, Imaging Assemblies'},
                    'zh': {'name': '牙科成像', 'desc': '口内相机、牙科显微镜和成像系统需要紧凑的高分辨率光学元件，并具有可靠的灭菌兼容性。', 'products': '微型透镜、蓝宝石窗口、成像组件'}
                },
                {
                    'en': {'name': 'Diagnostic Instruments', 'desc': 'From fluorescence microscopes to blood analyzers, diagnostic equipment uses precision filters and lenses for accurate spectral analysis and imaging.', 'products': 'Bandpass Filters, Achromatic Lenses, Dichroic Mirrors'},
                    'zh': {'name': '诊断仪器', 'desc': '从荧光显微镜到血液分析仪，诊断设备使用精密滤光片和透镜进行精确的光谱分析和成像。', 'products': '带通滤光片、消色差透镜、二向色镜'}
                }
            ],
            'specs': [
                {'param': 'Image Quality', 'en': 'Diffraction-limited MTF performance', 'zh': '衍射极限MTF性能'},
                {'param': 'Distortion', 'en': '< 0.1% (imaging lenses)', 'zh': '< 0.1%（成像透镜）'},
                {'param': 'Surface Quality', 'en': '20-10 standard, 10-5 for critical', 'zh': '标准20-10，关键应用10-5'},
                {'param': 'Material Options', 'en': 'BK7, Fused Silica, Sapphire, CaF₂', 'zh': 'BK7、熔融石英、蓝宝石、CaF₂'},
                {'param': 'Sterilization', 'en': 'Autoclave-compatible materials available', 'zh': '可提供高压灭菌兼容材料'},
                {'param': 'Coating Types', 'en': 'Broadband AR, Multiband AR, IR Coatings', 'zh': '宽带增透膜、多波段增透膜、红外镀膜'}
            ],
            'relatedArticles': ['choose-right-optical-lens', 'optical-windows-buying-guide', 'anti-reflection-coatings-guide']
        },
        'aerospace-defense': {
            'title': 'Aerospace & Defense',
            'titleZh': '航空航天与国防',
            'subApps': [
                {
                    'en': {'name': 'LiDAR Systems', 'desc': 'Light detection and ranging for autonomous navigation and mapping. Requires fast-response optics with high laser damage threshold and stable performance across temperature.', 'products': 'Narrow Bandpass Filters, Laser Mirrors, Scanner Windows'},
                    'zh': {'name': 'LiDAR系统', 'desc': '用于自主导航和测绘的光探测与测距。需要具有高激光损伤阈值和跨温度稳定性能的快速响应光学元件。', 'products': '窄带滤光片、激光反射镜、扫描窗口'}
                },
                {
                    'en': {'name': 'Targeting Systems', 'desc': 'Precision targeting and tracking optics for defense applications. Ruggedized design with shock, vibration and environmental qualification.', 'products': 'Achromatic Lenses, Precision Prisms, Ruggedized Mirrors'},
                    'zh': {'name': '瞄准系统', 'desc': '国防应用的精密瞄准和跟踪光学元件。加固设计，通过冲击、振动和环境鉴定。', 'products': '消色差透镜、精密棱镜、加固反射镜'}
                },
                {
                    'en': {'name': 'Space Optics', 'desc': 'Satellite and space-borne optical systems. Radiation-hardened materials, ultra-low outgassing, and space-qualified coatings for mission-critical performance.', 'products': 'Fused Silica Optics, Zerodur Components, Space-Grade Coatings'},
                    'zh': {'name': '空间光学', 'desc': '卫星和星载光学系统。抗辐射材料、极低出气率和空间级镀膜，满足关键任务性能要求。', 'products': '熔融石英光学元件、零膨胀玻璃组件、空间级镀膜'}
                },
                {
                    'en': {'name': 'Thermal Imaging', 'desc': 'Infrared imaging systems for surveillance and target acquisition. Germanium, silicon and chalcogenide optics for MWIR and LWIR wavelengths.', 'products': 'Ge Lenses, Si Windows, IR Imaging Optics'},
                    'zh': {'name': '热成像', 'desc': '用于监视和目标捕获的红外成像系统。锗、硅和硫系玻璃光学元件，适用于中波和长波红外波长。', 'products': '锗透镜、硅窗口、红外成像光学'}
                }
            ],
            'specs': [
                {'param': 'Environmental', 'en': '-40°C to +85°C operating range', 'zh': '-40°C 至 +85°C 工作温度范围'},
                {'param': 'Vibration / Shock', 'en': 'MIL-STD-810 compliant designs', 'zh': '符合MIL-STD-810标准的设计'},
                {'param': 'Surface Quality', 'en': '60-40 to 10-5 per MIL-PRF-13830B', 'zh': '60-40 至 10-5，符合MIL-PRF-13830B'},
                {'param': 'Optical Axis', 'en': 'Arc-second centration stability', 'zh': '弧秒级定心稳定性'},
                {'param': 'Materials', 'en': 'Sapphire, Fused Silica, Ge, Si, ZnSe', 'zh': '蓝宝石、熔融石英、锗、硅、ZnSe'},
                {'param': 'Coating Types', 'en': 'IR AR, Diamond-Like Carbon, Broadband', 'zh': '红外增透膜、类金刚石膜、宽带膜'}
            ],
            'relatedArticles': ['infrared-optical-materials-comparison', 'sapphire-optical-properties-applications', 'custom-optics-manufacturing-process']
        },
        'research-laboratory': {
            'title': 'Research & Laboratory',
            'titleZh': '科研与实验室',
            'subApps': [
                {
                    'en': {'name': 'Spectroscopy', 'desc': 'UV-Vis-NIR and IR spectroscopy systems require broadband transmission and precise wavelength selection. Dispersing prisms, diffraction gratings, and precision filters are core components.', 'products': 'Dispersing Prisms, Bandpass Filters, Collimating Lenses'},
                    'zh': {'name': '光谱学', 'desc': '紫外-可见-近红外和红外光谱系统需要宽带透射和精确的波长选择。色散棱镜、衍射光栅和精密滤光片是核心组件。', 'products': '色散棱镜、带通滤光片、准直透镜'}
                },
                {
                    'en': {'name': 'Interferometry', 'desc': 'Optical metrology and testing using interference patterns. Requires ultra-flat reference optics, precision beam splitters, and low-coherence or single-wavelength sources.', 'products': 'Reference Flats, Cube Beamsplitters, Precision Windows'},
                    'zh': {'name': '干涉测量', 'desc': '使用干涉图案进行光学计量和测试。需要超平参考光学元件、精密分束器和低相干或单波长光源。', 'products': '参考平片、立方分束器、精密窗口'}
                },
                {
                    'en': {'name': 'Microscopy', 'desc': 'Research-grade microscopes for biology, materials science and nanotechnology. Objectives, tube lenses, and illumination optics with diffraction-limited performance.', 'products': 'Microscope Objectives, Achromatic Doublets, Illumination Optics'},
                    'zh': {'name': '显微镜', 'desc': '用于生物学、材料科学和纳米技术的研究级显微镜。物镜、镜筒透镜和照明光学元件，具有衍射极限性能。', 'products': '显微物镜、消色差双胶合透镜、照明光学'}
                },
                {
                    'en': {'name': 'Quantum Optics', 'desc': 'Quantum information and photonics research requires ultra-precise polarization control and single-photon-level detection. High-extinction-ratio polarizers and waveplates are critical.', 'products': 'Glan-Taylor Prisms, Zero-Order Waveplates, High-Extinction Polarizers'},
                    'zh': {'name': '量子光学', 'desc': '量子信息和光子学研究需要超精密偏振控制和单光子级探测。高消光比偏振器和波片至关重要。', 'products': '格兰泰勒棱镜、零级波片、高消光比偏振器'}
                }
            ],
            'specs': [
                {'param': 'Wavelength Range', 'en': 'Deep UV to Far IR (190nm - 20μm)', 'zh': '深紫外至远红外（190nm - 20μm）'},
                {'param': 'Wavefront Quality', 'en': 'Up to λ/20 transmitted wavefront', 'zh': '最高λ/20透射波前'},
                {'param': 'Surface Quality', 'en': '10-5 precision grade standard', 'zh': '标准10-5精密级'},
                {'param': 'Polarization Extinction', 'en': '1000:1 to 100,000:1 (PBS / Polarizers)', 'zh': '1000:1 至 100,000:1（偏振分束器/偏振器）'},
                {'param': 'Material Range', 'en': '30+ optical materials available', 'zh': '可提供30+种光学材料'},
                {'param': 'Custom Specs', 'en': 'Small-batch custom specifications welcome', 'zh': '欢迎小批量定制规格'}
            ],
            'relatedArticles': ['optical-beamsplitter-selection-complete-guide', 'infrared-optical-materials-comparison', 'laser-damage-threshold-guide']
        }
    }
    
    for app_slug, app_data in apps.items():
        path = f'applications/{app_slug}/index.html'
        if not os.path.exists(os.path.join(BASE, path)):
            print(f"  [SKIP] {path} not found")
            continue
            
        content = read_file(path)
        
        # Find the FAQ section heading to insert before it
        # We'll add sub-applications, key specs, and related articles sections
        # Look for the FAQ section as insertion point
        
        # Build sub-applications section HTML
        sub_apps_html = '''
<section style="padding: 60px 0; background: white;">
    <div class="container" style="max-width: 1100px;">
        <h2 style="font-size: 30px; color: #1e3a5f; margin-bottom: 12px; text-align: center;" data-i18n="v90AppSubAppTitle">Sub-Application Scenarios</h2>
        <p style="color: #64748b; margin-bottom: 40px; font-size: 17px; text-align: center;" data-i18n="v90AppSubAppSubtitle">Detailed optical requirements and recommended components for each sub-application within this industry.</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 24px;">
'''
        
        for i, sub in enumerate(app_data['subApps']):
            sub_app_key = app_slug.replace('-', '') + 'Sub' + str(i + 1)
            card = '''
            <div style="background: #f8fafc; border-radius: 12px; padding: 28px; border: 1px solid #e2e8f0; transition: all 0.3s;" onmouseover="this.style.boxShadow='0 4px 16px rgba(0,0,0,0.08)';this.style.transform='translateY(-2px)'" onmouseout="this.style.boxShadow='none';this.style.transform='translateY(0)'">
                <div style="width: 44px; height: 44px; background: linear-gradient(135deg, #3b82f6, #60a5fa); border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 18px; margin-bottom: 16px;">__NUM__</div>
                <h3 style="color: #1e293b; font-size: 20px; margin-bottom: 10px;" data-i18n="v90App__KEY__Name">__NAME__</h3>
                <p style="color: #475569; line-height: 1.7; margin-bottom: 14px; font-size: 15px;" data-i18n="v90App__KEY__Desc">__DESC__</p>
                <p style="color: #3b82f6; font-size: 14px; font-weight: 600;">
                    <strong style="color: #64748b;" data-i18n="v90AppRecommendedLabel">Recommended: </strong>
                    <span data-i18n="v90App__KEY__Products">__PRODS__</span>
                </p>
            </div>
'''
            card = card.replace('__NUM__', str(i + 1))
            card = card.replace('__KEY__', sub_app_key)
            card = card.replace('__NAME__', sub['en']['name'])
            card = card.replace('__DESC__', sub['en']['desc'])
            card = card.replace('__PRODS__', sub['en']['products'])
            sub_apps_html += card
        
        sub_apps_html += '''
        </div>
    </div>
</section>
'''
        
        # Build key specs table section
        specs_html = '''
<section style="padding: 60px 0; background: #f8fafc;">
    <div class="container" style="max-width: 900px;">
        <h2 style="font-size: 30px; color: #1e3a5f; margin-bottom: 12px; text-align: center;" data-i18n="v90AppSpecsTitle">Key Specifications for This Industry</h2>
        <p style="color: #64748b; margin-bottom: 36px; font-size: 17px; text-align: center;" data-i18n="v90AppSpecsSubtitle">Typical parameter ranges for optical components used in this field. Your exact requirements may vary.</p>
        <div style="background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
            <table style="width: 100%; border-collapse: collapse;">
                <thead style="background: linear-gradient(135deg, #1e3a5f, #2d5a87); color: white;">
                    <tr>
                        <th style="padding: 16px 20px; text-align: left; font-weight: 600;" data-i18n="v90AppSpecParam">Parameter</th>
                        <th style="padding: 16px 20px; text-align: left; font-weight: 600;" data-i18n="v90AppSpecTypicalRange">Typical Range</th>
                    </tr>
                </thead>
                <tbody>
'''
        for j, spec in enumerate(app_data['specs']):
            bg = '#ffffff' if j % 2 == 0 else '#f8fafc'
            specs_html += f'''
                    <tr style="background: {bg};">
                        <td style="padding: 14px 20px; border-bottom: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;">{spec['param']}</td>
                        <td style="padding: 14px 20px; border-bottom: 1px solid #e2e8f0; color: #475569;" data-i18n="v90App{app_slug.replace('-', '')}Spec{j+1}">{spec['en']}</td>
                    </tr>
'''
        specs_html += '''
                </tbody>
            </table>
        </div>
        <p style="text-align: center; margin-top: 20px; color: #94a3b8; font-size: 14px;" data-i18n="v90AppSpecsNote">Need tighter specifications? Contact our engineering team for custom capabilities.</p>
    </div>
</section>
'''
        
        # Build related articles section
        related_html = '''
<section style="padding: 60px 0; background: white;">
    <div class="container" style="max-width: 1000px;">
        <h2 style="font-size: 30px; color: #1e3a5f; margin-bottom: 12px; text-align: center;" data-i18n="v90AppRelatedTitle">Related Technical Articles</h2>
        <p style="color: #64748b; margin-bottom: 36px; font-size: 17px; text-align: center;" data-i18n="v90AppRelatedSubtitle">Deep-dive technical guides relevant to this application area.</p>
        <div id="v90AppRelatedArticles" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;" data-slugs="''' + ','.join(app_data['relatedArticles']) + '''">
        </div>
    </div>
</section>
'''
        
        # Insert before FAQ section
        faq_marker = '<section'
        faq_idx = content.find('id="faqSection"')
        if faq_idx == -1:
            # Try finding FAQ heading
            faq_idx = content.find('>FAQ<')
        if faq_idx == -1:
            faq_idx = content.find('>Frequently Asked Questions<')
        
        if faq_idx > 0:
            # Find the section start before FAQ
            section_start = content.rfind('<section', 0, faq_idx)
            if section_start > 0:
                insert_html = sub_apps_html + specs_html + related_html
                content = content[:section_start] + insert_html + content[section_start:]
            else:
                # Append before footer
                footer_idx = content.find('<footer')
                if footer_idx > 0:
                    insert_html = sub_apps_html + specs_html + related_html
                    content = content[:footer_idx] + insert_html + content[footer_idx:]
        else:
            # Append before footer
            footer_idx = content.find('<footer')
            if footer_idx > 0:
                insert_html = sub_apps_html + specs_html + related_html
                content = content[:footer_idx] + insert_html + content[footer_idx:]
        
        # Add related articles rendering script
        script_insert = '''
<script>
function renderAppRelatedArticles() {
    var container = document.getElementById('v90AppRelatedArticles');
    if (!container || typeof BLOG_POSTS === 'undefined') return;
    var slugs = container.getAttribute('data-slugs').split(',');
    var useZh = localStorage.getItem('lang') === 'zh';
    var html = '';
    for (var i = 0; i < slugs.length; i++) {
        var slug = slugs[i].trim();
        var post = null;
        for (var j = 0; j < BLOG_POSTS.length; j++) {
            if (BLOG_POSTS[j].slug === slug) { post = BLOG_POSTS[j]; break; }
        }
        if (!post) continue;
        var postTitle = useZh && post.titleZh ? post.titleZh : post.title;
        var postExcerpt = useZh && post.excerptZh ? post.excerptZh : post.excerpt;
        if (postExcerpt.length > 140) postExcerpt = postExcerpt.substring(0, 140) + '...';
        html += '<a href="/blog/' + post.slug + '/" style="background: #f8fafc; border-radius: 12px; padding: 24px; text-decoration: none; display: block; border: 1px solid #e2e8f0; transition: all 0.3s;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none'">';
        html += '<div style="font-size: 12px; color: #3b82f6; font-weight: 600; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">' + (useZh && post.categoryZh ? post.categoryZh : post.category) + '</div>';
        html += '<h3 style="color: #1e293b; margin-bottom: 10px; font-size: 17px; line-height: 1.4;">' + postTitle + '</h3>';
        html += '<p style="color: #64748b; font-size: 14px; line-height: 1.6; margin-bottom: 12px;">' + postExcerpt + '</p>';
        html += '<span style="color: #3b82f6; font-weight: 600; font-size: 14px;">Read Article &rarr;</span>';
        html += '</a>';
    }
    container.innerHTML = html;
}
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderAppRelatedArticles);
} else {
    renderAppRelatedArticles();
}
</script>
'''
        
        # Insert before the main render script
        if '<script src="/js/chatbot.js"></script>' in content:
            content = content.replace('<script src="/js/chatbot.js"></script>', script_insert + '<script src="/js/chatbot.js"></script>')
        elif '</body>' in content:
            content = content.replace('</body>', script_insert + '</body>')
        
        # Ensure blog-data.js is loaded
        if 'blog-data.js' not in content:
            if 'translations.js' in content:
                content = content.replace(
                    '<script src="/js/translations.js"></script>',
                    '<script src="/js/blog-data.js"></script>\n    <script src="/js/translations.js"></script>'
                )
        
        write_file(path, content)
        print(f"  [OK] Application page enhanced: {app_slug}")

# =============================================
# PART 3: Engineering Page Enhancement
# =============================================

def build_engineering_page():
    """Enhance engineering.html with custom design capability, tolerance table, coating list, prototype-to-production"""
    content = read_file('engineering.html')
    
    # We'll add new sections before the final CTA
    cta_section_start = content.find('<!-- CTA -->')
    
    new_sections = '''
<!-- Custom Design Capability -->
<section style="padding: 60px 0; background: #f8fafc;">
    <div class="container" style="max-width: 1000px;">
        <h2 style="font-size: 30px; color: #1e3a5f; margin-bottom: 12px; text-align: center;" data-i18n="v90EngCustomTitle">Custom Design Capability</h2>
        <p style="color: #64748b; margin-bottom: 40px; font-size: 17px; text-align: center;" data-i18n="v90EngCustomSubtitle">From simple custom dimensions to complex multi-element assemblies — we design optics around your requirements.</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
            <div style="background: white; border-radius: 12px; padding: 28px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                <div style="font-size: 36px; margin-bottom: 14px;">&#128290;</div>
                <h3 style="color: #1e3a5f; margin-bottom: 10px;" data-i18n="v90EngCustom1Title">Standard Customization</h3>
                <p style="color: #475569; line-height: 1.7; font-size: 15px;" data-i18n="v90EngCustom1Desc">Custom dimensions, thickness, and coatings on standard optical forms. Fast turnaround — typical lead time 1-3 weeks.</p>
                <ul style="color: #475569; line-height: 2; margin-top: 10px; padding-left: 20px; font-size: 14px;">
                    <li data-i18n="v90EngCustom1Item1">Custom sizes from 1mm to 300mm</li>
                    <li data-i18n="v90EngCustom1Item2">Custom thickness and wedge</li>
                    <li data-i18n="v90EngCustom1Item3">Customer-specified coatings</li>
                    <li data-i18n="v90EngCustom1Item4">Standard and precision grades</li>
                </ul>
            </div>
            <div style="background: white; border-radius: 12px; padding: 28px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                <div style="font-size: 36px; margin-bottom: 14px;">&#9881;</div>
                <h3 style="color: #1e3a5f; margin-bottom: 10px;" data-i18n="v90EngCustom2Title">Complex Custom Optics</h3>
                <p style="color: #475569; line-height: 1.7; font-size: 15px;" data-i18n="v90EngCustom2Desc">Aspheres, free-form surfaces, and unusual geometries. Designed from your optical system specifications.</p>
                <ul style="color: #475569; line-height: 2; margin-top: 10px; padding-left: 20px; font-size: 14px;">
                    <li data-i18n="v90EngCustom2Item1">Aspheric surfaces</li>
                    <li data-i18n="v90EngCustom2Item2">Cylindrical and toroidal optics</li>
                    <li data-i18n="v90EngCustom2Item3">Custom prism geometries</li>
                    <li data-i18n="v90EngCustom2Item4">Specialty window profiles</li>
                </ul>
            </div>
            <div style="background: white; border-radius: 12px; padding: 28px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                <div style="font-size: 36px; margin-bottom: 14px;">&#128295;</div>
                <h3 style="color: #1e3a5f; margin-bottom: 10px;" data-i18n="v90EngCustom3Title">Optical Assemblies</h3>
                <p style="color: #475569; line-height: 1.7; font-size: 15px;" data-i18n="v90EngCustom3Desc">Multi-element lens assemblies, beam expanders, and integrated optical sub-systems delivered as complete modules.</p>
                <ul style="color: #475569; line-height: 2; margin-top: 10px; padding-left: 20px; font-size: 14px;">
                    <li data-i18n="v90EngCustom3Item1">Achromatic and apochromatic assemblies</li>
                    <li data-i18n="v90EngCustom3Item2">Beam expander modules</li>
                    <li data-i18n="v90EngCustom3Item3">Imaging lens groups</li>
                    <li data-i18n="v90EngCustom3Item4">Mounted and aligned assemblies</li>
                </ul>
            </div>
        </div>
    </div>
</section>

<!-- Tolerance Capability Table -->
<section style="padding: 60px 0; background: white;">
    <div class="container" style="max-width: 900px;">
        <h2 style="font-size: 30px; color: #1e3a5f; margin-bottom: 12px; text-align: center;" data-i18n="v90EngTolTitle">Tolerance Capability</h2>
        <p style="color: #64748b; margin-bottom: 36px; font-size: 17px; text-align: center;" data-i18n="v90EngTolSubtitle">What we can achieve — from commercial grade to ultra-precision specifications.</p>
        <div style="background: #f8fafc; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0;">
            <table style="width: 100%; border-collapse: collapse;">
                <thead style="background: linear-gradient(135deg, #1e3a5f, #2d5a87); color: white;">
                    <tr>
                        <th style="padding: 14px 18px; text-align: left; font-weight: 600;" data-i18n="v90EngTolParam">Parameter</th>
                        <th style="padding: 14px 18px; text-align: left; font-weight: 600;" data-i18n="v90EngTolStandard">Standard Grade</th>
                        <th style="padding: 14px 18px; text-align: left; font-weight: 600;" data-i18n="v90EngTolPrecision">Precision Grade</th>
                        <th style="padding: 14px 18px; text-align: left; font-weight: 600;" data-i18n="v90EngTolUltra">Ultra-Precision</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;" data-i18n="v90EngTolSurfQual">Surface Quality</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">60-40 / 40-20</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">20-10</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">10-5 / 5-2</td>
                    </tr>
                    <tr style="background: white;">
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;" data-i18n="v90EngTolFlatness">Surface Flatness</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">&#955;/2 to &#955;/4</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">&#955;/10</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">&#955;/20 to &#955;/50</td>
                    </tr>
                    <tr>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;" data-i18n="v90EngTolCenterThk">Center Thickness</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">&#177;0.1 mm</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">&#177;0.02 mm</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">&#177;0.005 mm</td>
                    </tr>
                    <tr style="background: white;">
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;" data-i18n="v90EngTolDimension">Dimensional Tolerance</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">&#177;0.1 mm</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">&#177;0.02 mm</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">&#177;0.01 mm</td>
                    </tr>
                    <tr>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;" data-i18n="v90EngTolParallelism">Parallelism / Wedge</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">5 arc-min</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">30 arc-sec</td>
                        <td style="padding: 12px 18px; border-bottom: 1px solid #e2e8f0; color: #475569;">5 arc-sec</td>
                    </tr>
                    <tr style="background: white;">
                        <td style="padding: 12px 18px; font-weight: 600; color: #1e293b;" data-i18n="v90EngTolCentration">Centration (lenses)</td>
                        <td style="padding: 12px 18px; color: #475569;">3 arc-min</td>
                        <td style="padding: 12px 18px; color: #475569;">1 arc-min</td>
                        <td style="padding: 12px 18px; color: #475569;">30 arc-sec</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <p style="text-align: center; margin-top: 20px; color: #94a3b8; font-size: 14px;" data-i18n="v90EngTolNote">Actual achievable tolerances depend on material, size, and geometry. Contact us for specific capability review.</p>
    </div>
</section>

<!-- Coating Design Capability -->
<section style="padding: 60px 0; background: #f8fafc;">
    <div class="container" style="max-width: 1000px;">
        <h2 style="font-size: 30px; color: #1e3a5f; margin-bottom: 12px; text-align: center;" data-i18n="v90EngCoatingTitle">Coating Design Capability</h2>
        <p style="color: #64748b; margin-bottom: 36px; font-size: 17px; text-align: center;" data-i18n="v90EngCoatingSubtitle">Physical vapor deposition coatings designed for your exact wavelength, angle and performance requirements.</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
            <div style="background: white; border-radius: 12px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                <div style="width: 48px; height: 48px; background: #dbeafe; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 16px;">&#10024;</div>
                <h3 style="color: #1e3a5f; margin-bottom: 10px; font-size: 18px;" data-i18n="v90EngCoat1Title">Anti-Reflection (AR)</h3>
                <ul style="color: #475569; line-height: 2; font-size: 14px; padding-left: 18px; margin: 0;">
                    <li data-i18n="v90EngCoat1Item1">Single-layer MgF&#8322;</li>
                    <li data-i18n="v90EngCoat1Item2">Multi-layer broadband AR</li>
                    <li data-i18n="v90EngCoat1Item3">Dual-band and triple-band</li>
                    <li data-i18n="v90EngCoat1Item4">V-coat (single wavelength)</li>
                    <li data-i18n="v90EngCoat1Item5">Laser-line AR with LIDT spec</li>
                </ul>
            </div>
            <div style="background: white; border-radius: 12px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                <div style="width: 48px; height: 48px; background: #fef3c7; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 16px;">&#9672;</div>
                <h3 style="color: #1e3a5f; margin-bottom: 10px; font-size: 18px;" data-i18n="v90EngCoat2Title">High-Reflectance (HR)</h3>
                <ul style="color: #475569; line-height: 2; font-size: 14px; padding-left: 18px; margin: 0;">
                    <li data-i18n="v90EngCoat2Item1">Protected Aluminum / Silver / Gold</li>
                    <li data-i18n="v90EngCoat2Item2">Enhanced Aluminum / Silver</li>
                    <li data-i18n="v90EngCoat2Item3">Dielectric HR (99.9%+)</li>
                    <li data-i18n="v90EngCoat2Item4">Laser-line HR mirrors</li>
                    <li data-i18n="v90EngCoat2Item5">Broadband dielectric mirrors</li>
                </ul>
            </div>
            <div style="background: white; border-radius: 12px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                <div style="width: 48px; height: 48px; background: #dcfce7; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 16px;">&#127912;</div>
                <h3 style="color: #1e3a5f; margin-bottom: 10px; font-size: 18px;" data-i18n="v90EngCoat3Title">Filter Coatings</h3>
                <ul style="color: #475569; line-height: 2; font-size: 14px; padding-left: 18px; margin: 0;">
                    <li data-i18n="v90EngCoat3Item1">Narrow bandpass filters</li>
                    <li data-i18n="v90EngCoat3Item2">Shortpass / Longpass edge</li>
                    <li data-i18n="v90EngCoat3Item3">Dichroic / Notch filters</li>
                    <li data-i18n="v90EngCoat3Item4">Neutral density (ND)</li>
                    <li data-i18n="v90EngCoat3Item5">Multi-band bandpass</li>
                </ul>
            </div>
            <div style="background: white; border-radius: 12px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                <div style="width: 48px; height: 48px; background: #fce7f3; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 16px;">&#127752;</div>
                <h3 style="color: #1e3a5f; margin-bottom: 10px; font-size: 18px;" data-i18n="v90EngCoat4Title">Specialty Coatings</h3>
                <ul style="color: #475569; line-height: 2; font-size: 14px; padding-left: 18px; margin: 0;">
                    <li data-i18n="v90EngCoat4Item1">Diamond-Like Carbon (DLC)</li>
                    <li data-i18n="v90EngCoat4Item2">Phase coatings for prisms</li>
                    <li data-i18n="v90EngCoat4Item3">Dispersion-compensated GTI</li>
                    <li data-i18n="v90EngCoat4Item4">Partial reflectors / output couplers</li>
                    <li data-i18n="v90EngCoat4Item5">Polarizing / non-polarizing beam splitter</li>
                </ul>
            </div>
        </div>
    </div>
</section>

<!-- Prototype to Production -->
<section style="padding: 60px 0; background: white;">
    <div class="container" style="max-width: 1000px;">
        <h2 style="font-size: 30px; color: #1e3a5f; margin-bottom: 12px; text-align: center;" data-i18n="v90EngProtoTitle">Prototype to Production</h2>
        <p style="color: #64748b; margin-bottom: 40px; font-size: 17px; text-align: center;" data-i18n="v90EngProtoSubtitle">One consistent process from first prototype to volume production. No surprises when scaling up.</p>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 0; position: relative;">
            <div style="flex: 1; min-width: 180px; text-align: center; padding: 24px 16px; background: #f8fafc; border-right: 2px solid #e2e8f0;">
                <div style="display: inline-block; width: 56px; height: 56px; background: linear-gradient(135deg, #3b82f6, #60a5fa); color: white; border-radius: 50%; line-height: 56px; font-weight: 700; font-size: 20px; margin-bottom: 14px;">1</div>
                <h3 style="color: #1e3a5f; font-size: 16px; margin-bottom: 8px;" data-i18n="v90EngProtoStep1Title">Design Review</h3>
                <p style="color: #64748b; font-size: 13px; line-height: 1.6;" data-i18n="v90EngProtoStep1Desc">Engineering review of specs, material and coating selection, DFM feedback</p>
                <p style="color: #3b82f6; font-weight: 600; font-size: 13px; margin-top: 10px;" data-i18n="v90EngProtoStep1Time">24-48 hours</p>
            </div>
            <div style="flex: 1; min-width: 180px; text-align: center; padding: 24px 16px; background: #f8fafc; border-right: 2px solid #e2e8f0;">
                <div style="display: inline-block; width: 56px; height: 56px; background: linear-gradient(135deg, #3b82f6, #60a5fa); color: white; border-radius: 50%; line-height: 56px; font-weight: 700; font-size: 20px; margin-bottom: 14px;">2</div>
                <h3 style="color: #1e3a5f; font-size: 16px; margin-bottom: 8px;" data-i18n="v90EngProtoStep2Title">Prototype</h3>
                <p style="color: #64748b; font-size: 13px; line-height: 1.6;" data-i18n="v90EngProtoStep2Desc">1-10 pieces. Full inspection report. Validate performance in your system</p>
                <p style="color: #3b82f6; font-weight: 600; font-size: 13px; margin-top: 10px;" data-i18n="v90EngProtoStep2Time">1-3 weeks</p>
            </div>
            <div style="flex: 1; min-width: 180px; text-align: center; padding: 24px 16px; background: #f8fafc; border-right: 2px solid #e2e8f0;">
                <div style="display: inline-block; width: 56px; height: 56px; background: linear-gradient(135deg, #3b82f6, #60a5fa); color: white; border-radius: 50%; line-height: 56px; font-weight: 700; font-size: 20px; margin-bottom: 14px;">3</div>
                <h3 style="color: #1e3a5f; font-size: 16px; margin-bottom: 8px;" data-i18n="v90EngProtoStep3Title">Pilot Run</h3>
                <p style="color: #64748b; font-size: 13px; line-height: 1.6;" data-i18n="v90EngProtoStep3Desc">50-500 pieces. Process documentation, yield verification, batch consistency</p>
                <p style="color: #3b82f6; font-weight: 600; font-size: 13px; margin-top: 10px;" data-i18n="v90EngProtoStep3Time">3-6 weeks</p>
            </div>
            <div style="flex: 1; min-width: 180px; text-align: center; padding: 24px 16px; background: #f8fafc;">
                <div style="display: inline-block; width: 56px; height: 56px; background: linear-gradient(135deg, #3b82f6, #60a5fa); color: white; border-radius: 50%; line-height: 56px; font-weight: 700; font-size: 20px; margin-bottom: 14px;">4</div>
                <h3 style="color: #1e3a5f; font-size: 16px; margin-bottom: 8px;" data-i18n="v90EngProtoStep4Title">Production</h3>
                <p style="color: #64748b; font-size: 13px; line-height: 1.6;" data-i18n="v90EngProtoStep4Desc">Volume manufacturing. SPC, batch inspection, scheduled deliveries</p>
                <p style="color: #3b82f6; font-weight: 600; font-size: 13px; margin-top: 10px;" data-i18n="v90EngProtoStep4Time">4-8 weeks recurring</p>
            </div>
        </div>
    </div>
</section>
'''
    
    if cta_section_start > 0:
        content = content[:cta_section_start] + new_sections + content[cta_section_start:]
    
    # Update CTA button text
    content = content.replace(
        '<a href="/contact.html" style="display: inline-block; padding: 16px 40px; font-size: 18px; background: white; color: #1e3a5f; border-radius: 8px; text-decoration: none; font-weight: 600;">Request Engineering Review</a>',
        '<a href="/contact.html" class="final-cta-btn primary" data-i18n="v90EngFinalCTA">Talk With Optical Engineer</a>'
    )
    
    write_file('engineering.html', content)
    print("  [OK] Engineering page enhanced")

# =============================================
# PART 4: Material Detail Pages
# =============================================

def build_material_pages():
    """Create 5 individual material detail pages"""
    
    materials = {
        'bk7': {
            'name': 'BK7 Optical Glass',
            'nameZh': 'BK7光学玻璃',
            'slug': 'bk7',
            'properties': {
                'transmissionRange': '350 nm – 2.0 μm',
                'refractiveIndex': '1.5168 @ 587.6nm',
                'thermalExpansion': '7.1 × 10⁻⁶ /K (20-300°C)',
                'density': '2.51 g/cm³',
                'knoopHardness': '610 HK'
            },
            'propertiesZh': {
                'transmissionRange': '350 nm – 2.0 μm',
                'refractiveIndex': '1.5168 @ 587.6nm',
                'thermalExpansion': '7.1 × 10⁻⁶ /K (20-300°C)',
                'density': '2.51 g/cm³',
                'knoopHardness': '610 HK'
            },
            'introEn': 'BK7 is the most widely used optical glass for visible and near-infrared applications. A borosilicate crown glass, BK7 offers excellent optical clarity, good homogeneity, and reasonable cost — making it the default choice for many general-purpose optical components.',
            'introZh': 'BK7是可见光和近红外应用中使用最广泛的光学玻璃。作为硼硅酸盐冕牌玻璃，BK7具有出色的光学清晰度、良好的均匀性和合理的成本，使其成为许多通用光学元件的默认选择。',
            'prosEn': ['Excellent visible transmission (>92% per surface uncoated)', 'High material homogeneity and consistency', 'Good chemical resistance and stability', 'Cost-effective — widely available in stock sizes', 'Suitable for most visible and NIR applications'],
            'prosZh': ['出色的可见光透射率（未镀膜每面>92%）', '高材料均匀性和一致性', '良好的耐化学性和稳定性', '成本效益高——库存尺寸广泛可用', '适用于大多数可见光和近红外应用'],
            'consEn': ['Not suitable for UV below 350nm', 'Higher thermal expansion than fused silica', 'Lower LIDT than fused silica for high-power lasers', 'Hygroscopic under extreme humidity conditions', 'Limited IR transmission beyond 2μm'],
            'consZh': ['不适用于350nm以下的紫外线', '热膨胀系数高于熔融石英', '高功率激光器的损伤阈值低于熔融石英', '极端湿度条件下会吸潮', '2μm以上的红外透射有限'],
            'applicationsEn': ['Imaging lenses and objectives', 'Beam splitters and prisms', 'General-purpose windows', 'Spectrometer optics', 'Machine vision systems'],
            'applicationsZh': ['成像透镜和物镜', '分束器和棱镜', '通用窗口', '光谱仪光学元件', '机器视觉系统'],
            'coatingsEn': ['Broadband AR (VIS, VIS-NIR)', 'Anti-reflection single-layer MgF₂', 'Protected/enhanced aluminum', 'Dielectric HR and partial reflector', 'Beam splitter coatings'],
            'coatingsZh': ['宽带增透膜（可见光、可见-近红外）', '单层氟化镁增透膜', '保护/增强铝膜', '介质高反膜和部分反射膜', '分束镀膜'],
            'relatedProducts': ['/products/bk7-windows/', '/products/bk7-plano-convex/', '/products/bk7-bi-convex/', '/products/bk7-right-angle-prisms/'],
            'relatedArticles': ['bk7-vs-uv-fused-silica', 'choose-right-optical-lens', 'optical-windows-buying-guide']
        },
        'uv-fused-silica': {
            'name': 'UV Fused Silica',
            'nameZh': '紫外熔融石英',
            'slug': 'uv-fused-silica',
            'properties': {
                'transmissionRange': '180 nm – 2.2 μm',
                'refractiveIndex': '1.4585 @ 587.6nm',
                'thermalExpansion': '0.55 × 10⁻⁶ /K (20-300°C)',
                'density': '2.20 g/cm³',
                'knoopHardness': '630 HK'
            },
            'propertiesZh': {
                'transmissionRange': '180 nm – 2.2 μm',
                'refractiveIndex': '1.4585 @ 587.6nm',
                'thermalExpansion': '0.55 × 10⁻⁶ /K (20-300°C)',
                'density': '2.20 g/cm³',
                'knoopHardness': '630 HK'
            },
            'introEn': 'UV Fused Silica (UVFS) is a high-purity amorphous silica glass with exceptional transmission from the deep UV through the near infrared. Its low coefficient of thermal expansion and high laser damage threshold make it the material of choice for high-power laser and UV applications.',
            'introZh': '紫外熔融石英（UVFS）是一种高纯度非晶石英玻璃，具有从深紫外到近红外的出色透射率。其低热膨胀系数和高激光损伤阈值使其成为高功率激光和紫外应用的首选材料。',
            'prosEn': ['Excellent deep UV transmission (down to 180nm)', 'Exceptionally low thermal expansion (13x lower than BK7)', 'Very high laser damage threshold', 'Excellent optical homogeneity', 'Good chemical durability and resistance', 'High thermal shock resistance'],
            'prosZh': ['出色的深紫外透射率（低至180nm）', '极低的热膨胀系数（比BK7低13倍）', '非常高的激光损伤阈值', '出色的光学均匀性', '良好的化学耐久性和耐受性', '高抗热震性'],
            'consEn': ['Higher material cost than BK7', 'More difficult to process (harder material)', 'Higher refractive index temperature coefficient (dn/dT) than some glasses', 'Not suitable for mid-IR and far-IR', 'Polishing requires diamond tooling'],
            'consZh': ['材料成本高于BK7', '加工难度更大（材料更硬）', '折射率温度系数（dn/dT）高于某些玻璃', '不适用于中红外和远红外', '抛光需要金刚石工具'],
            'applicationsEn': ['High-power laser systems', 'UV lithography and inspection', 'Spectroscopy and analytical instruments', 'High-precision reference optics', 'Semiconductor manufacturing equipment'],
            'applicationsZh': ['高功率激光系统', '紫外光刻和检测', '光谱学和分析仪器', '高精度参考光学元件', '半导体制造设备'],
            'coatingsEn': ['UV AR coatings (190-400nm)', 'Broadband AR (UV-VIS-NIR)', 'Laser-line AR and HR coatings', 'UV-enhanced aluminum', 'Dichroic and bandpass UV filters'],
            'coatingsZh': ['紫外增透膜（190-400nm）', '宽带增透膜（紫外-可见-近红外）', '激光线增透和高反膜', '紫外增强铝膜', '二向色和紫外带通滤光片'],
            'relatedProducts': ['/products/uv-fused-silica-windows/', '/products/uv-fused-silica-plano-convex/', '/products/laser-line-high-reflected-mirrors/'],
            'relatedArticles': ['bk7-vs-uv-fused-silica', 'laser-damage-threshold-guide', 'custom-optics-specification-guide']
        },
        'caf2': {
            'name': 'Calcium Fluoride (CaF₂)',
            'nameZh': '氟化钙（CaF₂）',
            'slug': 'caf2',
            'properties': {
                'transmissionRange': '170 nm – 9.0 μm',
                'refractiveIndex': '1.4338 @ 587.6nm',
                'thermalExpansion': '18.9 × 10⁻⁶ /K (20-300°C)',
                'density': '3.18 g/cm³',
                'knoopHardness': '158 HK'
            },
            'propertiesZh': {
                'transmissionRange': '170 nm – 9.0 μm',
                'refractiveIndex': '1.4338 @ 587.6nm',
                'thermalExpansion': '18.9 × 10⁻⁶ /K (20-300°C)',
                'density': '3.18 g/cm³',
                'knoopHardness': '158 HK'
            },
            'introEn': 'Calcium Fluoride (CaF₂) is a crystalline optical material with an extraordinarily broad transmission range spanning from the deep ultraviolet through the mid-infrared. Its extremely low dispersion makes it invaluable for UV optics, spectroscopy, and ultrafast laser systems.',
            'introZh': '氟化钙（CaF₂）是一种晶体光学材料，具有从深紫外到中红外的超宽透射范围。其极低的色散使其在紫外光学、光谱学和超快激光系统中具有不可替代的价值。',
            'prosEn': ['Extremely broad transmission (170nm to 9μm)', 'Very low dispersion (Abbe number ~95)', 'Deep UV transparency — no solarization', 'Low refractive index for simple AR coating', 'Useful for UV, VIS, and IR simultaneously'],
            'prosZh': ['极宽的透射范围（170nm至9μm）', '极低的色散（阿贝数~95）', '深紫外透明——无日晒老化', '低折射率，增透膜设计简单', '可同时用于紫外、可见和红外'],
            'consEn': ['Soft material — easily scratched (low hardness)', 'High thermal expansion coefficient', 'Cleaves easily — special handling required', 'Hygroscopic (absorbs moisture over time)', 'More expensive than glass materials'],
            'consZh': ['材料较软——容易刮伤（硬度低）', '热膨胀系数高', '易解理——需要特殊处理', '吸湿性（随时间吸收水分）', '比玻璃材料更贵'],
            'applicationsEn': ['Deep UV spectroscopy', 'Ultrafast laser systems (low dispersion)', 'Excimer laser optics', 'FTIR and IR spectroscopy', 'Lithography and UV imaging'],
            'applicationsZh': ['深紫外光谱学', '超快激光系统（低色散）', '准分子激光光学', '傅里叶变换红外和红外光谱', '光刻和紫外成像'],
            'coatingsEn': ['Deep UV AR coatings', 'Broadband VIS-IR AR', 'Partial reflection coatings', 'Anti-reflection for 193nm / 248nm', 'IR anti-reflection coatings'],
            'coatingsZh': ['深紫外增透膜', '宽带可见-红外增透膜', '部分反射膜', '193nm / 248nm增透膜', '红外增透膜'],
            'relatedProducts': ['/products/caf2-windows/'],
            'relatedArticles': ['infrared-optical-materials-comparison', 'laser-damage-threshold-guide', 'optical-windows-buying-guide']
        },
        'znse': {
            'name': 'Zinc Selenide (ZnSe)',
            'nameZh': '硒化锌（ZnSe）',
            'slug': 'znse',
            'properties': {
                'transmissionRange': '0.6 μm – 18 μm',
                'refractiveIndex': '2.4028 @ 10.6μm',
                'thermalExpansion': '7.1 × 10⁻⁶ /K (20-300°C)',
                'density': '5.27 g/cm³',
                'knoopHardness': '120 HK'
            },
            'propertiesZh': {
                'transmissionRange': '0.6 μm – 18 μm',
                'refractiveIndex': '2.4028 @ 10.6μm',
                'thermalExpansion': '7.1 × 10⁻⁶ /K (20-300°C)',
                'density': '5.27 g/cm³',
                'knoopHardness': '120 HK'
            },
            'introEn': 'Zinc Selenide (ZnSe) is a polycrystalline infrared material with excellent transmission from the visible through the far infrared. It is the standard material for CO₂ laser optics and is widely used in thermal imaging and IR spectroscopy systems.',
            'introZh': '硒化锌（ZnSe）是一种多晶红外材料，具有从可见光到远红外的出色透射率。它是CO₂激光光学的标准材料，广泛用于热成像和红外光谱系统。',
            'prosEn': ['Excellent IR transmission (0.6μm to 18μm)', 'Good thermal conductivity for CO₂ lasers', 'Standard material for 10.6μm CO₂ optics', 'Visible and IR transmission — useful for alignment', 'Low absorption at CO₂ wavelength'],
            'prosZh': ['出色的红外透射率（0.6μm至18μm）', 'CO₂激光器的良好导热性', '10.6μm CO₂光学的标准材料', '可见光和红外透射——便于对准', 'CO₂波长下低吸收'],
            'consEn': ['Soft material — easily scratched', 'Toxic material — special handling required', 'High refractive index requires AR coating', 'More expensive than Ge or Si', 'Yellow/orange color (visible light absorption)'],
            'consZh': ['材料较软——容易刮伤', '有毒材料——需要特殊处理', '高折射率需要增透膜', '比锗或硅更贵', '黄/橙色（可见光吸收）'],
            'applicationsEn': ['CO₂ laser windows and lenses', 'Thermal imaging systems', 'FTIR spectroscopy', 'Medical laser systems', 'IR optical sensors'],
            'applicationsZh': ['CO₂激光窗口和透镜', '热成像系统', '傅里叶变换红外光谱', '医疗激光系统', '红外光学传感器'],
            'coatingsEn': ['AR coatings for 10.6μm', 'Broadband IR AR (8-12μm)', 'Dual-band AR (visible + CO₂)', 'Diamond-Like Carbon (DLC)', 'Partial reflection for output couplers'],
            'coatingsZh': ['10.6μm增透膜', '宽带红外增透膜（8-12μm）', '双波段增透膜（可见光+CO₂）', '类金刚石碳（DLC）', '输出耦合器部分反射膜'],
            'relatedProducts': ['/products/znse-windows/'],
            'relatedArticles': ['infrared-optical-materials-comparison', 'laser-damage-threshold-guide']
        },
        'sapphire': {
            'name': 'Sapphire (Al₂O₃)',
            'nameZh': '蓝宝石（Al₂O₃）',
            'slug': 'sapphire',
            'properties': {
                'transmissionRange': '170 nm – 5.5 μm',
                'refractiveIndex': '1.768 @ 587.6nm (ordinary)',
                'thermalExpansion': '5.3 × 10⁻⁶ /K (20-300°C)',
                'density': '3.97 g/cm³',
                'knoopHardness': '2200 HK'
            },
            'propertiesZh': {
                'transmissionRange': '170 nm – 5.5 μm',
                'refractiveIndex': '1.768 @ 587.6nm (寻常光)',
                'thermalExpansion': '5.3 × 10⁻⁶ /K (20-300°C)',
                'density': '3.97 g/cm³',
                'knoopHardness': '2200 HK'
            },
            'introEn': 'Sapphire is a single-crystal form of aluminum oxide (Al₂O₃) with extraordinary mechanical, thermal and optical properties. Its extreme hardness and broad transmission make it the material of choice for demanding environments where durability matters.',
            'introZh': '蓝宝石是氧化铝（Al₂O₃）的单晶形式，具有非凡的机械、热和光学性能。其极高的硬度和宽透射范围使其成为耐用性至关重要的苛刻环境的首选材料。',
            'prosEn': ['Extremely hard and scratch-resistant (2nd only to diamond)', 'Very broad transmission (UV to mid-IR)', 'Excellent thermal conductivity', 'High melting point (2040°C)', 'Chemically inert and biocompatible', 'Excellent abrasion and wear resistance'],
            'prosZh': ['极其坚硬和耐刮擦（仅次于金刚石）', '非常宽的透射范围（紫外到中红外）', '出色的导热性', '高熔点（2040°C）', '化学惰性和生物相容性', '优异的耐磨和耐磨损性'],
            'consEn': ['Birefringent material (not isotropic)', 'Higher cost than glass materials', 'Difficult to process and polish', 'High refractive index requires good AR coating', 'Material size limitations for large optics'],
            'consZh': ['双折射材料（非各向同性）', '成本高于玻璃材料', '加工和抛光难度大', '高折射率需要优质增透膜', '大尺寸光学元件的材料尺寸限制'],
            'applicationsEn': ['Extreme-environment windows', 'Medical and dental optics', 'Aerospace and defense systems', 'High-pressure and vacuum systems', 'Wear-resistant optical surfaces'],
            'applicationsZh': ['极端环境窗口', '医疗和牙科光学', '航空航天和国防系统', '高压和真空系统', '耐磨光学表面'],
            'coatingsEn': ['Broadband AR (UV-VIS-NIR)', 'Mid-wave IR AR coatings', 'Diamond-Like Carbon (DLC)', 'Anti-reflection for multi-band use', 'High-temperature resistant coatings'],
            'coatingsZh': ['宽带增透膜（紫外-可见-近红外）', '中波红外增透膜', '类金刚石碳（DLC）', '多波段使用增透膜', '耐高温镀膜'],
            'relatedProducts': ['/products/sapphire-windows/'],
            'relatedArticles': ['sapphire-optical-properties-applications', 'optical-windows-buying-guide', 'custom-optics-manufacturing-process']
        }
    }
    
    # Read materials.html to extract header, footer patterns
    template_content = read_file('materials.html')
    
    # Extract header
    header_end = template_content.find('<!-- Page Content')
    if header_end == -1:
        header_end = template_content.find('<div class="breadcrumb-wrapper"')
    
    # Extract footer
    footer_start = template_content.find('<footer class="footer">')
    if footer_start == -1:
        footer_start = template_content.find('<!-- WhatsApp')
    
    header_html = template_content[:header_end]
    footer_html = template_content[footer_start:]
    
    for mat_slug, mat in materials.items():
        mat_prefix = mat_slug.replace("-", "").title()
        dir_path = f'materials/{mat_slug}'
        file_path = f'materials/{mat_slug}/index.html'
        
        # Build page content
        content = header_html.replace(
            '<title>Optical Materials Database',
            f'<title>{mat["name"]} - Properties, Applications & Specifications | PhotonEdge'
        ).replace(
            'content="Optical materials database',
            f'content="{mat["name"]} — comprehensive guide to optical properties, advantages, limitations, typical applications, and available coatings. PhotonEdge custom optics.'
        )
        
        # Update og:title and og:description
        content = content.replace(
            'property="og:title" content="Optical Materials Database"',
            f'property="og:title" content="{mat["name"]} - Properties & Applications | PhotonEdge"'
        )
        
        # Update canonical
        content = content.replace(
            'href="https://photonedgeoptics.com/materials.html"',
            f'href="https://photonedgeoptics.com/materials/{mat_slug}/"'
        )
        content = content.replace(
            'href="https://photonedgeoptics.com/materials.html?lang=zh"',
            f'href="https://photonedgeoptics.com/materials/{mat_slug}/?lang=zh"'
        )
        
        # Build the main content
        main_content = f'''
    <div class="breadcrumb-wrapper">
        <div class="container">
            <nav class="breadcrumb">
                <a href="/">Home</a>
                <span class="breadcrumb-separator">/</span>
                <a href="/materials.html" data-i18n="v90MatBcMaterials">Materials</a>
                <span class="breadcrumb-separator">/</span>
                <span>{mat['name']}</span>
            </nav>
        </div>
    </div>

    <div class="request-quote-float">
        <a href="/contact.html" class="quote-btn">
            <span class="quote-icon">&#9993;</span>
            <span data-i18n="navRFQ">Request Engineering Review</span>
        </a>
    </div>

    <!-- Hero -->
    <section style="padding: 60px 0 40px; background: linear-gradient(135deg, #f0f4f8 0%, #e8eef5 100%);">
        <div class="container" style="max-width: 1000px;">
            <div style="display: flex; align-items: center; gap: 30px; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 300px;">
                    <span style="display: inline-block; background: #dbeafe; color: #1e40af; padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; margin-bottom: 16px;" data-i18n="v90MatMaterial">Optical Material</span>
                    <h1 style="font-size: 38px; font-weight: 700; color: #1e3a5f; margin-bottom: 16px;">{mat['name']}</h1>
                    <p style="font-size: 17px; color: #475569; line-height: 1.7;" data-i18n="v90Mat{mat_prefix}Intro">{mat['introEn']}</p>
                    <div style="margin-top: 20px;">
                        <a href="/contact.html" class="btn btn-primary" data-i18n="v90MatCta">Request Custom Quote</a>
                    </div>
                </div>
                <div style="width: 200px; height: 200px; background: linear-gradient(135deg, #e0e7ff, #c7d2fe); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 80px;">
                    &#9673;
                </div>
            </div>
        </div>
    </section>

    <!-- Key Properties Table -->
    <section style="padding: 60px 0; background: white;">
        <div class="container" style="max-width: 800px;">
            <h2 style="font-size: 28px; color: #1e3a5f; margin-bottom: 24px; text-align: center;" data-i18n="v90MatPropsTitle">Key Optical Properties</h2>
            <div style="background: #f8fafc; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0;">
                <table style="width: 100%; border-collapse: collapse;">
                    <tr style="background: linear-gradient(135deg, #1e3a5f, #2d5a87); color: white;">
                        <th style="padding: 14px 20px; text-align: left; font-weight: 600;" data-i18n="v90MatPropProperty">Property</th>
                        <th style="padding: 14px 20px; text-align: left; font-weight: 600;" data-i18n="v90MatPropValue">Value</th>
                    </tr>
                    <tr>
                        <td style="padding: 12px 20px; border-bottom: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;" data-i18n="v90MatPropTransmission">Transmission Range</td>
                        <td style="padding: 12px 20px; border-bottom: 1px solid #e2e8f0; color: #475569;">{mat['properties']['transmissionRange']}</td>
                    </tr>
                    <tr style="background: white;">
                        <td style="padding: 12px 20px; border-bottom: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;" data-i18n="v90MatPropRefractive">Refractive Index</td>
                        <td style="padding: 12px 20px; border-bottom: 1px solid #e2e8f0; color: #475569;">{mat['properties']['refractiveIndex']}</td>
                    </tr>
                    <tr>
                        <td style="padding: 12px 20px; border-bottom: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;" data-i18n="v90MatPropThermal">Thermal Expansion</td>
                        <td style="padding: 12px 20px; border-bottom: 1px solid #e2e8f0; color: #475569;">{mat['properties']['thermalExpansion']}</td>
                    </tr>
                    <tr style="background: white;">
                        <td style="padding: 12px 20px; border-bottom: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;" data-i18n="v90MatPropDensity">Density</td>
                        <td style="padding: 12px 20px; border-bottom: 1px solid #e2e8f0; color: #475569;">{mat['properties']['density']}</td>
                    </tr>
                    <tr>
                        <td style="padding: 12px 20px; font-weight: 600; color: #1e293b;" data-i18n="v90MatPropHardness">Knoop Hardness</td>
                        <td style="padding: 12px 20px; color: #475569;">{mat['properties']['knoopHardness']}</td>
                    </tr>
                </table>
            </div>
        </div>
    </section>

    <!-- Advantages & Limitations -->
    <section style="padding: 60px 0; background: #f8fafc;">
        <div class="container" style="max-width: 1000px;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">
                <div style="background: white; border-radius: 12px; padding: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
                        <div style="width: 44px; height: 44px; background: #dcfce7; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 22px;">&#10003;</div>
                        <h3 style="color: #1e3a5f; font-size: 22px; margin: 0;" data-i18n="v90MatAdvTitle">Advantages</h3>
                    </div>
                    <ul style="color: #475569; line-height: 2; padding-left: 24px; margin: 0;">
'''
        for pro in mat['prosEn']:
            idx = mat['prosEn'].index(pro) + 1
            main_content += f'                        <li data-i18n="v90Mat{mat_prefix}Pro{idx}">{pro}</li>\n'
        
        main_content += '''
                    </ul>
                </div>
                <div style="background: white; border-radius: 12px; padding: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
                        <div style="width: 44px; height: 44px; background: #fee2e2; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 22px;">&#9888;</div>
                        <h3 style="color: #1e3a5f; font-size: 22px; margin: 0;" data-i18n="v90MatLimitTitle">Limitations</h3>
                    </div>
                    <ul style="color: #475569; line-height: 2; padding-left: 24px; margin: 0;">
'''
        for con in mat['consEn']:
            idx = mat['consEn'].index(con) + 1
            main_content += f'                        <li data-i18n="v90Mat{mat_prefix}Con{idx}">{con}</li>\n'
        
        main_content += f'''
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Typical Applications -->
    <section style="padding: 60px 0; background: white;">
        <div class="container" style="max-width: 900px;">
            <h2 style="font-size: 28px; color: #1e3a5f; margin-bottom: 24px; text-align: center;" data-i18n="v90MatAppTitle">Typical Applications</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
'''
        for app in mat['applicationsEn']:
            idx = mat['applicationsEn'].index(app) + 1
            main_content += f'''
                <div style="background: #f8fafc; border-radius: 10px; padding: 20px; border-left: 4px solid #3b82f6;">
                    <p style="color: #1e293b; font-weight: 500; margin: 0;" data-i18n="v90Mat{mat_prefix}App{idx}">{app}</p>
                </div>
'''
        
        main_content += f'''
            </div>
        </div>
    </section>

    <!-- Common Coating Options -->
    <section style="padding: 60px 0; background: #f8fafc;">
        <div class="container" style="max-width: 900px;">
            <h2 style="font-size: 28px; color: #1e3a5f; margin-bottom: 24px; text-align: center;" data-i18n="v90MatCoatingTitle">Common Coating Options</h2>
            <p style="color: #64748b; margin-bottom: 30px; font-size: 16px; text-align: center;" data-i18n="v90MatCoatingSubtitle">Standard coating types available for this material. Custom coating designs available on request.</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
'''
        for coat in mat['coatingsEn']:
            idx = mat['coatingsEn'].index(coat) + 1
            main_content += f'''
                <div style="background: white; border-radius: 10px; padding: 18px 20px; border: 1px solid #e2e8f0; display: flex; align-items: center; gap: 12px;">
                    <span style="color: #3b82f6; font-size: 18px;">&#9679;</span>
                    <span style="color: #475569; font-size: 15px;" data-i18n="v90Mat{mat_prefix}Coat{idx}">{coat}</span>
                </div>
'''
        
        main_content += '''
            </div>
        </div>
    </section>

    <!-- Related Products -->
    <section style="padding: 60px 0; background: white;">
        <div class="container" style="max-width: 1000px;">
            <h2 style="font-size: 28px; color: #1e3a5f; margin-bottom: 24px; text-align: center;" data-i18n="v90MatRelProdTitle">Related Products</h2>
            <div id="v90MatRelatedProducts" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px;" data-slugs="''' + ','.join([p.split('/')[-2] for p in mat['relatedProducts']]) + '''">
            </div>
        </div>
    </section>

    <!-- Related Articles -->
    <section style="padding: 60px 0; background: #f8fafc;">
        <div class="container" style="max-width: 1000px;">
            <h2 style="font-size: 28px; color: #1e3a5f; margin-bottom: 24px; text-align: center;" data-i18n="v90MatRelArtTitle">Related Technical Articles</h2>
            <div id="v90MatRelatedArticles" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;" data-slugs="''' + ','.join(mat['relatedArticles']) + '''">
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section style="padding: 70px 0; background: linear-gradient(135deg,#1e3a5f 0%,#2d5a87 100%); text-align: center; color: white;">
        <div class="container">
            <h2 style="color: white; margin-bottom: 14px; font-size: 30px;" data-i18n="v90MatCtaTitle">Need Custom Optics in This Material?</h2>
            <p style="color: rgba(255,255,255,0.9); margin-bottom: 30px; font-size: 16px; max-width: 550px; margin-left: auto; margin-right: auto;" data-i18n="v90MatCtaSubtitle">Send us your specifications. Our engineering team will review and respond with material and coating recommendations within 24 hours.</p>
            <a href="/contact.html" class="final-cta-btn primary" data-i18n="v90MatCtaBtn">Request Engineering Review</a>
        </div>
    </section>
'''
        # Note: mat_prefix defined at top of loop for f-string usage
        
        # Add scripts at the bottom before footer
        scripts = f'''
<script src="/js/products-data.js"></script>
<script src="/js/blog-data.js"></script>
<script>
function renderMatRelatedProducts() {{
    var container = document.getElementById('v90MatRelatedProducts');
    if (!container || typeof PRODUCTS === 'undefined') return;
    var slugs = container.getAttribute('data-slugs').split(',');
    var useZh = localStorage.getItem('lang') === 'zh';
    var html = '';
    for (var i = 0; i < slugs.length; i++) {{
        var slug = slugs[i].trim();
        var product = null;
        for (var j = 0; j < PRODUCTS.length; j++) {{
            if (PRODUCTS[j].slug === slug) {{ product = PRODUCTS[j]; break; }}
        }}
        if (!product) continue;
        var displayName = useZh && product.nameZh ? product.nameZh : product.name;
        html += '<a href="' + product.url + '" style="background: #f8fafc; border-radius: 12px; padding: 20px; text-decoration: none; display: block; border: 1px solid #e2e8f0; transition: all 0.3s;" onmouseover="this.style.transform=\\'translateY(-2px)\\';this.style.boxShadow=\\'0 4px 12px rgba(0,0,0,0.08)\\'" onmouseout="this.style.transform=\\'translateY(0)\\';this.style.boxShadow=\\'none\\'">';
        html += '<div style="font-size: 30px; margin-bottom: 10px;">&#9673;</div>';
        html += '<h3 style="color: #1e293b; font-size: 15px; margin-bottom: 6px;">' + displayName + '</h3>';
        html += '<span style="color: #3b82f6; font-weight: 600; font-size: 13px;">View Details &rarr;</span>';
        html += '</a>';
    }}
    container.innerHTML = html;
}}

function renderMatRelatedArticles() {{
    var container = document.getElementById('v90MatRelatedArticles');
    if (!container || typeof BLOG_POSTS === 'undefined') return;
    var slugs = container.getAttribute('data-slugs').split(',');
    var useZh = localStorage.getItem('lang') === 'zh';
    var html = '';
    for (var i = 0; i < slugs.length; i++) {{
        var slug = slugs[i].trim();
        var post = null;
        for (var j = 0; j < BLOG_POSTS.length; j++) {{
            if (BLOG_POSTS[j].slug === slug) {{ post = BLOG_POSTS[j]; break; }}
        }}
        if (!post) continue;
        var postTitle = useZh && post.titleZh ? post.titleZh : post.title;
        var postExcerpt = useZh && post.excerptZh ? post.excerptZh : post.excerpt;
        if (postExcerpt.length > 120) postExcerpt = postExcerpt.substring(0, 120) + '...';
        html += '<a href="/blog/' + post.slug + '/" style="background: white; border-radius: 12px; padding: 22px; text-decoration: none; display: block; border: 1px solid #e2e8f0; transition: all 0.3s;" onmouseover="this.style.transform=\\'translateY(-3px)\\';this.style.boxShadow=\\'0 6px 20px rgba(0,0,0,0.08)\\'" onmouseout="this.style.transform=\\'translateY(0)\\';this.style.boxShadow=\\'none\\'">';
        html += '<div style="font-size: 12px; color: #3b82f6; font-weight: 600; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">' + (useZh && post.categoryZh ? post.categoryZh : post.category) + '</div>';
        html += '<h3 style="color: #1e293b; margin-bottom: 8px; font-size: 16px; line-height: 1.4;">' + postTitle + '</h3>';
        html += '<p style="color: #64748b; font-size: 13px; line-height: 1.6; margin-bottom: 10px;">' + postExcerpt + '</p>';
        html += '<span style="color: #3b82f6; font-weight: 600; font-size: 13px;">Read Article &rarr;</span>';
        html += '</a>';
    }}
    container.innerHTML = html;
}}

document.addEventListener('DOMContentLoaded', function() {{
    renderMatRelatedProducts();
    renderMatRelatedArticles();
    if (typeof updatePageTranslations === 'function') updatePageTranslations();
}});
</script>
'''
        
        full_page = content + main_content + scripts + footer_html
        write_file(file_path, full_page)
        print(f"  [OK] Material page created: {mat_slug}")

# =============================================
# PART 5: Case Studies Page
# =============================================

def build_case_studies_page():
    """Populate case-studies.html with 4 full case studies"""
    content = read_file('case-studies.html')
    
    # Find the main content area
    body_start = content.find('<body>') + len('<body>')
    footer_start = content.find('<footer')
    
    cases_html = '''
    <div style="background: linear-gradient(135deg, #f0f4f8 0%, #e8eef5 100%); padding: 60px 0 40px;">
        <div class="container" style="text-align: center; max-width: 800px;">
            <span style="display: inline-block; background: #dbeafe; color: #1e40af; padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; margin-bottom: 16px;" data-i18n="v90CaseHeroTag">Case Studies</span>
            <h1 style="font-size: 42px; font-weight: 700; color: #1e3a5f; margin-bottom: 16px;" data-i18n="v90CaseHeroTitle">Real Engineering Challenges, Solved</h1>
            <p style="font-size: 18px; color: #475569; line-height: 1.7;" data-i18n="v90CaseHeroDesc">See how we collaborate with engineering teams to solve demanding optical problems. Each case documents the challenge, our approach, and the measured results.</p>
        </div>
    </div>

    <div style="padding: 60px 0; background: #ffffff;">
        <div class="container" style="max-width: 1000px;">
            
            <!-- Case 1 -->
            <article class="v90-case-full" style="background: white; border-radius: 16px; border: 1px solid #e2e8f0; margin-bottom: 40px; overflow: hidden;">
                <div style="background: linear-gradient(135deg, #fef3c7, #fde68a); padding: 20px 30px;">
                    <span style="background: #d97706; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600;" data-i18n="v90Case1Industry">Laser Systems</span>
                </div>
                <div style="padding: 30px;">
                    <h2 style="color: #1e3a5f; font-size: 26px; margin-bottom: 20px;" data-i18n="v90Case1FullTitle">UV Laser Window Optimization for 355nm Industrial System</h2>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin-bottom: 24px;">
                        <div>
                            <h3 style="color: #dc2626; font-size: 18px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                                <span style="background: #fee2e2; width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">!</span>
                                <span data-i18n="v90CaseChallenge">The Challenge</span>
                            </h3>
                            <p style="color: #475569; line-height: 1.8;" data-i18n="v90Case1FullChallenge">A UV laser equipment manufacturer was experiencing premature optical degradation in their 355nm solid-state laser systems. The output coupling windows showed increasing absorption and visible color center formation within 1000 hours of operation, causing output power to drop by more than 30%. The existing supplier had provided standard fused silica windows with standard AR coating, which proved insufficient for the combined UV and power density requirements of the application.</p>
                        </div>
                        <div>
                            <h3 style="color: #059669; font-size: 18px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                                <span style="background: #d1fae5; width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">&#10003;</span>
                                <span data-i18n="v90CaseSolution">Our Solution</span>
                            </h3>
                            <p style="color: #475569; line-height: 1.8;" data-i18n="v90Case1FullSolution">We performed a failure analysis and identified two root causes: (1) standard-grade fused silica with trace metal impurities was causing solarization under UV exposure, and (2) the AR coating was not optimized for high UV power density. Our solution: switch to high-purity synthetic fused silica with low metallic impurity content, upgrade the surface quality from 40-20 to 10-5 scratch-dig to minimize scattering-initiated damage, and apply a UV-optimized AR coating with demonstrated LIDT > 5 J/cm² at 355nm, 10ns. We also recommended a slight increase in substrate thickness for better thermal management.</p>
                        </div>
                    </div>
                    <div style="background: linear-gradient(135deg, #dbeafe, #bfdbfe); border-radius: 10px; padding: 20px 24px;">
                        <h3 style="color: #1e3a5f; font-size: 18px; margin-bottom: 12px;" data-i18n="v90CaseResult">Measured Results</h3>
                        <ul style="color: #1e293b; line-height: 2; margin: 0; padding-left: 24px;">
                            <li data-i18n="v90Case1Result1">Optical lifetime extended from 1,000 hours to 8,000+ hours</li>
                            <li data-i18n="v90Case1Result2">Output power fluctuation reduced by 70% over operating lifetime</li>
                            <li data-i18n="v90Case1Result3">Initial transmission improved by 2.5% (99.7% vs 97.2%)</li>
                            <li data-i18n="v90Case1Result4">Zero field failures reported in first 12 months of deployment</li>
                        </ul>
                    </div>
                </div>
            </article>

            <!-- Case 2 -->
            <article class="v90-case-full" style="background: white; border-radius: 16px; border: 1px solid #e2e8f0; margin-bottom: 40px; overflow: hidden;">
                <div style="background: linear-gradient(135deg, #fce7f3, #fbcfe8); padding: 20px 30px;">
                    <span style="background: #db2777; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600;" data-i18n="v90Case2Industry">Medical Imaging</span>
                </div>
                <div style="padding: 30px;">
                    <h2 style="color: #1e3a5f; font-size: 26px; margin-bottom: 20px;" data-i18n="v90Case2FullTitle">Precision Imaging Lens Assembly for Diagnostic Instrument</h2>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin-bottom: 24px;">
                        <div>
                            <h3 style="color: #dc2626; font-size: 18px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                                <span style="background: #fee2e2; width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">!</span>
                                <span data-i18n="v90CaseChallenge">The Challenge</span>
                            </h3>
                            <p style="color: #475569; line-height: 1.8;" data-i18n="v90Case2FullChallenge">A medical diagnostic equipment manufacturer needed a custom 3-element imaging lens achieving diffraction-limited MTF performance across the full 400-700nm visible spectrum. The system required less than 0.1% distortion over the entire field of view, with tight centration tolerances to maintain image quality at the sensor. Their initial single-vendor approach was failing to meet MTF specifications consistently across production batches.</p>
                        </div>
                        <div>
                            <h3 style="color: #059669; font-size: 18px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                                <span style="background: #d1fae5; width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">&#10003;</span>
                                <span data-i18n="v90CaseSolution">Our Solution</span>
                            </h3>
                            <p style="color: #475569; line-height: 1.8;" data-i18n="v90Case2FullSolution">Our engineering team collaborated on the optical design, recommending an achromatic doublet plus a correction element configuration using BK7 and SF11 glass types. We optimized the cemented interface for minimum wavefront error and specified centration to 30 arc-seconds on the doublet assembly. We introduced a detailed incoming inspection protocol with interferometric testing of each element before assembly, and a final assembled-lens MTF verification step. Our DFM review also identified that the initial center thickness tolerances could be relaxed on one element without affecting system performance, reducing cost by 15%.</p>
                        </div>
                    </div>
                    <div style="background: linear-gradient(135deg, #dbeafe, #bfdbfe); border-radius: 10px; padding: 20px 24px;">
                        <h3 style="color: #1e3a5f; font-size: 18px; margin-bottom: 12px;" data-i18n="v90CaseResult">Measured Results</h3>
                        <ul style="color: #1e293b; line-height: 2; margin: 0; padding-left: 24px;">
                            <li data-i18n="v90Case2Result1">MTF exceeded specification across all fields and wavelengths</li>
                            <li data-i18n="v90Case2Result2">Distortion measured at 0.06% (well under 0.1% target)</li>
                            <li data-i18n="v90Case2Result3">Batch-to-batch consistency maintained over 20+ production runs</li>
                            <li data-i18n="v90Case2Result4">15% cost reduction through DFM tolerance optimization</li>
                        </ul>
                    </div>
                </div>
            </article>

            <!-- Case 3 -->
            <article class="v90-case-full" style="background: white; border-radius: 16px; border: 1px solid #e2e8f0; margin-bottom: 40px; overflow: hidden;">
                <div style="background: linear-gradient(135deg, #dbeafe, #bfdbfe); padding: 20px 30px;">
                    <span style="background: #2563eb; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600;" data-i18n="v90CaseSemiIndustry">Semiconductor</span>
                </div>
                <div style="padding: 30px;">
                    <h2 style="color: #1e3a5f; font-size: 26px; margin-bottom: 20px;" data-i18n="v90Case3FullTitle">High-Purity Fused Silica Windows for Wafer Inspection System</h2>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin-bottom: 24px;">
                        <div>
                            <h3 style="color: #dc2626; font-size: 18px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                                <span style="background: #fee2e2; width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">!</span>
                                <span data-i18n="v90CaseChallenge">The Challenge</span>
                            </h3>
                            <p style="color: #475569; line-height: 1.8;" data-i18n="v90Case3FullChallenge">A semiconductor equipment manufacturer was developing a new wafer inspection system operating at 266nm deep-UV wavelength. The system required optical windows with exceptional wavefront quality (λ/20 at 266nm) and extremely low particulate contamination. Their initial supplier could not consistently meet the flatness specification, and delivered components with unacceptable particle counts on the surface and edges.</p>
                        </div>
                        <div>
                            <h3 style="color: #059669; font-size: 18px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                                <span style="background: #d1fae5; width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">&#10003;</span>
                                <span data-i18n="v90CaseSolution">Our Solution</span>
                            </h3>
                            <p style="color: #475569; line-height: 1.8;" data-i18n="v90Case3FullSolution">We proposed synthetic fused silica (Corning 7980 equivalent) for its superior UV transmission and material homogeneity. We implemented a super-polish process to achieve the required λ/20 flatness, verified at 266nm using a calibrated UV interferometer. For contamination control, all final cleaning and inspection was performed in a Class 100 cleanroom environment. We also introduced a custom double-container packaging approach with cleanroom-compatible materials to maintain cleanliness from our facility to the customer's assembly line. Each window is accompanied by a particle count report.</p>
                        </div>
                    </div>
                    <div style="background: linear-gradient(135deg, #dbeafe, #bfdbfe); border-radius: 10px; padding: 20px 24px;">
                        <h3 style="color: #1e3a5f; font-size: 18px; margin-bottom: 12px;" data-i18n="v90CaseResult">Measured Results</h3>
                        <ul style="color: #1e293b; line-height: 2; margin: 0; padding-left: 24px;">
                            <li data-i18n="v90Case3Result1">Wavefront flatness achieved: λ/22 @ 266nm (exceeds λ/20 spec)</li>
                            <li data-i18n="v90Case3Result2">Zero out-of-spec particle counts across all delivered batches</li>
                            <li data-i18n="v90Case3Result3">System signal-to-noise ratio improved by 18% vs. previous windows</li>
                            <li data-i18n="v90Case3Result4">Consistent performance across 15+ production batches</li>
                        </ul>
                    </div>
                </div>
            </article>

            <!-- Case 4 -->
            <article class="v90-case-full" style="background: white; border-radius: 16px; border: 1px solid #e2e8f0; margin-bottom: 40px; overflow: hidden;">
                <div style="background: linear-gradient(135deg, #dcfce7, #bbf7d0); padding: 20px 30px;">
                    <span style="background: #16a34a; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600;" data-i18n="v90CaseResearchIndustry">Research & Laboratory</span>
                </div>
                <div style="padding: 30px;">
                    <h2 style="color: #1e3a5f; font-size: 26px; margin-bottom: 20px;" data-i18n="v90Case4FullTitle">Custom CaF₂ Prism Pair for Ultrafast Pulse Compression</h2>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin-bottom: 24px;">
                        <div>
                            <h3 style="color: #dc2626; font-size: 18px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                                <span style="background: #fee2e2; width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">!</span>
                                <span data-i18n="v90CaseChallenge">The Challenge</span>
                            </h3>
                            <p style="color: #475569; line-height: 1.8;" data-i18n="v90Case4FullChallenge">A university research laboratory specializing in ultrafast laser science needed a matched pair of CaF₂ prisms for a pulse compression setup in a femtosecond Ti:Sapphire laser system operating at 800nm. The prisms needed precise apex angle matching (better than 1 arc-minute between the pair) and exceptionally low wavefront distortion to avoid degrading pulse quality. Standard catalog prisms had too much angle variation between individual pieces.</p>
                        </div>
                        <div>
                            <h3 style="color: #059669; font-size: 18px; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
                                <span style="background: #d1fae5; width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center;">&#10003;</span>
                                <span data-i18n="v90CaseSolution">Our Solution</span>
                            </h3>
                            <p style="color: #475569; line-height: 1.8;" data-i18n="v90Case4FullSolution">We manufactured a pair of CaF₂ equilateral prisms with matched apex angles. The key to success was a controlled grinding and polishing process where both prisms were processed in the same batch, using identical tooling and process parameters. We applied a broadband AR coating at 700-900nm optimized for the P-polarization state used in prism compressors. Final verification included apex angle measurement via autocollimator and transmitted wavefront measurement at 633nm. The two prisms were matched and delivered as a set with comparison data showing angle variation of less than 20 arc-seconds between them.</p>
                        </div>
                    </div>
                    <div style="background: linear-gradient(135deg, #dbeafe, #bfdbfe); border-radius: 10px; padding: 20px 24px;">
                        <h3 style="color: #1e3a5f; font-size: 18px; margin-bottom: 12px;" data-i18n="v90CaseResult">Measured Results</h3>
                        <ul style="color: #1e293b; line-height: 2; margin: 0; padding-left: 24px;">
                            <li data-i18n="v90Case4Result1">Apex angle matching: 15 arc-seconds (exceeds 1 arc-min target)</li>
                            <li data-i18n="v90Case4Result2">Transmitted wavefront: λ/12 @ 633nm per prism</li>
                            <li data-i18n="v90Case4Result3">Pulse compression achieved: <30 femtoseconds</li>
                            <li data-i18n="v90Case4Result4">Second identical pair ordered for expanded beam setup</li>
                        </ul>
                    </div>
                </div>
            </article>

        </div>
    </div>

    <!-- CTA -->
    <section style="padding: 70px 0; background: linear-gradient(135deg,#1e3a5f 0%,#2d5a87 100%); text-align: center; color: white;">
        <div class="container">
            <h2 style="color: white; margin-bottom: 14px; font-size: 32px;" data-i18n="v90CaseCtaTitle">Have a Similar Optical Challenge?</h2>
            <p style="color: rgba(255,255,255,0.9); margin-bottom: 30px; font-size: 17px; max-width: 550px; margin-left: auto; margin-right: auto;" data-i18n="v90CaseCtaDesc">Tell us about your application and requirements. Our optical engineers will review and respond with recommendations within 24 hours.</p>
            <a href="/contact.html" class="final-cta-btn primary" data-i18n="v90CaseCtaBtn">Request Engineering Review</a>
        </div>
    </section>
'''
    
    # Replace the body content while keeping header and footer
    new_content = content[:body_start] + cases_html + content[footer_start:]
    write_file('case-studies.html', new_content)
    print("  [OK] Case studies page populated")

# =============================================
# PART 6: Knowledge Center Upgrade
# =============================================

def build_knowledge_center():
    """Upgrade knowledge-center/index.html with categorized blog archive"""
    content = read_file('knowledge-center/index.html')
    
    # Category mapping from blog categories to KC categories
    # Blog categories: Technical Guide, Application Guide, Buying Guide, Company
    # KC categories: Technical Guides, Material Selection, Coating Knowledge, Design Tips, Manufacturing
    
    # Define the new content
    body_start = content.find('<body>') + len('<body>')
    footer_start = content.find('<footer')
    
    kc_html = '''
    <div style="background: linear-gradient(135deg, #f0f4f8 0%, #e8eef5 100%); padding: 60px 0 40px;">
        <div class="container" style="text-align: center; max-width: 800px;">
            <span style="display: inline-block; background: #dbeafe; color: #1e40af; padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; margin-bottom: 16px;" data-i18n="v90KcTag">Knowledge Center</span>
            <h1 style="font-size: 42px; font-weight: 700; color: #1e3a5f; margin-bottom: 16px;" data-i18n="v90KcTitle">Optical Engineering Knowledge Hub</h1>
            <p style="font-size: 18px; color: #475569; line-height: 1.7;" data-i18n="v90KcDesc">Technical guides, material comparisons, coating knowledge and design tips — everything you need to specify and select optical components with confidence.</p>
            
            <!-- Search Box -->
            <div style="max-width: 560px; margin: 30px auto 0;">
                <div style="position: relative;">
                    <input type="text" id="kcSearchInput" placeholder="Search technical articles..." style="width: 100%; padding: 14px 40px 14px 18px; border: 2px solid #cbd5e1; border-radius: 10px; font-size: 16px; outline: none; transition: border-color 0.3s;" onfocus="this.style.borderColor='#3b82f6'" onblur="this.style.borderColor='#cbd5e1'" onkeyup="kcSearchOnKey(event)">
                    <button onclick="performKcSearch()" style="position: absolute; right: 6px; top: 50%; transform: translateY(-50%); background: #3b82f6; color: white; border: none; padding: 9px 18px; border-radius: 8px; cursor: pointer; font-weight: 600; font-size: 14px;" data-i18n="v90KcSearchBtn">Search</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Category Filter Tabs -->
    <div style="padding: 30px 0; background: white; border-bottom: 1px solid #e2e8f0; position: sticky; top: 0; z-index: 100;">
        <div class="container">
            <div class="v90-kc-tabs" style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;">
                <button class="v90-kc-tab active" onclick="filterKcCategory('all', this)" data-i18n="v90KcTabAll">All Articles</button>
                <button class="v90-kc-tab" onclick="filterKcCategory('technical-guides', this)" data-i18n="v90KcTabTechnical">Technical Guides</button>
                <button class="v90-kc-tab" onclick="filterKcCategory('material-selection', this)" data-i18n="v90KcTabMaterial">Material Selection</button>
                <button class="v90-kc-tab" onclick="filterKcCategory('coating-knowledge', this)" data-i18n="v90KcTabCoating">Coating Knowledge</button>
                <button class="v90-kc-tab" onclick="filterKcCategory('design-tips', this)" data-i18n="v90KcTabDesign">Design Tips</button>
                <button class="v90-kc-tab" onclick="filterKcCategory('manufacturing', this)" data-i18n="v90KcTabManufacturing">Manufacturing</button>
            </div>
        </div>
    </div>

    <!-- Articles Grid -->
    <div style="padding: 50px 0 70px; background: #f8fafc;">
        <div class="container" style="max-width: 1100px;">
            <div style="margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <h2 id="kcCategoryTitle" style="font-size: 24px; color: #1e3a5f; margin: 0;" data-i18n="v90KcAllTitle">All Technical Articles</h2>
                <span id="kcCountLabel" style="color: #64748b; font-size: 14px;">36 articles</span>
            </div>
            <div id="kcArticlesGrid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 24px;">
                <!-- Filled by JS -->
            </div>
            <div id="kcNoResults" style="display: none; text-align: center; padding: 60px 20px; color: #94a3b8;">
                <p style="font-size: 18px;" data-i18n="v90KcNoResults">No articles found matching your search.</p>
            </div>
        </div>
    </div>
'''
    
    # Add JS for filtering and rendering
    scripts = '''
<script src="/js/blog-data.js"></script>
<script>
// Category mapping: blog category + keyword -> KC category
function getKcCategory(post) {
    var title = post.title.toLowerCase();
    var excerpt = (post.excerpt || '').toLowerCase();
    var text = title + ' ' + excerpt;
    
    // Material Selection
    if (title.indexOf('vs') !== -1 || title.indexOf('comparison') !== -1 || 
        title.indexOf('sapphire') !== -1 || title.indexOf('infrared materials') !== -1 ||
        text.indexOf('material') !== -1 && (text.indexOf('select') !== -1 || text.indexOf('comparison') !== -1 || text.indexOf('vs ') !== -1)) {
        return 'material-selection';
    }
    
    // Coating Knowledge
    if (text.indexOf('coating') !== -1 || text.indexOf('anti-reflection') !== -1 || 
        text.indexOf('ar coat') !== -1 || text.indexOf('hr coat') !== -1) {
        return 'coating-knowledge';
    }
    
    // Manufacturing
    if (text.indexOf('manufacturing') !== -1 || text.indexOf('production process') !== -1 || 
        text.indexOf('cleaning') !== -1 || text.indexOf('maintenance') !== -1 ||
        text.indexOf('custom optics') !== -1 && (text.indexOf('manufactur') !== -1 || text.indexOf('process') !== -1)) {
        return 'manufacturing';
    }
    
    // Design Tips
    if (text.indexOf('design') !== -1 || text.indexOf('tolerance') !== -1 || 
        text.indexOf('specification') !== -1 || text.indexOf('choosing') !== -1 ||
        text.indexOf('selection guide') !== -1 || text.indexOf('buying guide') !== -1 ||
        text.indexOf('spec') !== -1) {
        return 'design-tips';
    }
    
    // Default: Technical Guides
    return 'technical-guides';
}

var currentCategory = 'all';
var currentSearch = '';

function renderKcArticles() {
    var grid = document.getElementById('kcArticlesGrid');
    var noResults = document.getElementById('kcNoResults');
    if (!grid || typeof BLOG_POSTS === 'undefined') return;
    
    var useZh = localStorage.getItem('lang') === 'zh';
    var search = currentSearch.toLowerCase().trim();
    var filtered = [];
    
    for (var i = 0; i < BLOG_POSTS.length; i++) {
        var post = BLOG_POSTS[i];
        var cat = getKcCategory(post);
        if (currentCategory !== 'all' && cat !== currentCategory) continue;
        
        if (search) {
            var haystack = (post.title + ' ' + (post.excerpt || '') + ' ' + (post.titleZh || '') + ' ' + (post.excerptZh || '')).toLowerCase();
            if (haystack.indexOf(search) === -1) continue;
        }
        
        filtered.push(post);
    }
    
    // Update count
    var countLabel = document.getElementById('kcCountLabel');
    if (countLabel) {
        var countText = useZh ? '篇文章' : ' articles';
        countLabel.textContent = filtered.length + countText;
    }
    
    // Update category title
    var titleEl = document.getElementById('kcCategoryTitle');
    if (titleEl) {
        // handled by translations
    }
    
    if (filtered.length === 0) {
        grid.innerHTML = '';
        noResults.style.display = 'block';
        return;
    }
    
    noResults.style.display = 'none';
    var html = '';
    
    for (var i = 0; i < filtered.length; i++) {
        var post = filtered[i];
        var postTitle = useZh && post.titleZh ? post.titleZh : post.title;
        var postExcerpt = useZh && post.excerptZh ? post.excerptZh : post.excerpt;
        var postCategory = useZh && post.categoryZh ? post.categoryZh : post.category;
        if (postExcerpt.length > 150) postExcerpt = postExcerpt.substring(0, 150) + '...';
        
        html += '<a href="/blog/' + post.slug + '/" style="background: white; border-radius: 12px; padding: 24px; text-decoration: none; display: block; border: 1px solid #e2e8f0; transition: all 0.3s;" onmouseover="this.style.transform=\\'translateY(-4px)\\';this.style.boxShadow=\\'0 8px 24px rgba(0,0,0,0.08)\\'" onmouseout="this.style.transform=\\'translateY(0)\\';this.style.boxShadow=\\'none\\'">';
        html += '<div style="font-size: 12px; color: #3b82f6; font-weight: 600; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.5px;">' + postCategory + '</div>';
        html += '<h3 style="color: #1e293b; margin-bottom: 10px; font-size: 17px; line-height: 1.4;">' + postTitle + '</h3>';
        html += '<p style="color: #64748b; font-size: 14px; line-height: 1.6; margin-bottom: 14px;">' + postExcerpt + '</p>';
        html += '<div style="display: flex; justify-content: space-between; align-items: center; font-size: 13px; color: #94a3b8;">';
        html += '<span>' + (post.date || '') + '</span>';
        html += '<span style="color: #3b82f6; font-weight: 600;">Read &rarr;</span>';
        html += '</div></a>';
    }
    
    grid.innerHTML = html;
}

function filterKcCategory(cat, btn) {
    currentCategory = cat;
    // Update active tab
    var tabs = document.querySelectorAll('.v90-kc-tab');
    for (var i = 0; i < tabs.length; i++) {
        tabs[i].classList.remove('active');
    }
    if (btn) btn.classList.add('active');
    renderKcArticles();
}

function performKcSearch() {
    var input = document.getElementById('kcSearchInput');
    if (input) {
        currentSearch = input.value;
        renderKcArticles();
    }
}

function kcSearchOnKey(event) {
    if (event.key === 'Enter') {
        performKcSearch();
    }
}

document.addEventListener('DOMContentLoaded', function() {
    renderKcArticles();
    if (typeof updatePageTranslations === 'function') updatePageTranslations();
});
</script>
'''
    
    new_content = content[:body_start] + kc_html + scripts + content[footer_start:]
    write_file('knowledge-center/index.html', new_content)
    print("  [OK] Knowledge Center upgraded")

# =============================================
# PART 7: Translations Update
# =============================================

def update_translations():
    """Add all V90 translation keys to translations.js"""
    content = read_file('js/translations.js')
    
    # Check if already added
    if 'v90HomeHeroTitle' in content:
        print("  [SKIP] V90 translations already added")
        return
    
    # Read the V90 translations dict
    from v90_translations import V90_TRANSLATIONS
    
    # File structure:
    # var translations = {
    # en: {
    #     ... (en keys, no quotes on keys)
    # },   <-- en closing
    #     zh: {
    #         ... (zh keys, quoted keys)
    # }
    # }
    # function t()...
    
    # Find en section closing (before zh:)
    zh_open_idx = content.find('zh: {')
    if zh_open_idx == -1:
        zh_open_idx = content.find('zh : {')
    if zh_open_idx == -1:
        print("  [ERROR] Could not find zh: section opening")
        return
    
    # Find en closing } before zh: going backwards
    # Pattern: the line before zh: block with just } or  },
    en_close_idx = content.rfind('},', 0, zh_open_idx)
    if en_close_idx == -1:
        print("  [ERROR] Could not find en section closing")
        return
    
    # Find zh section closing (before function t())
    func_marker = 'function t('
    func_idx = content.find(func_marker)
    if func_idx == -1:
        print("  [ERROR] Could not find function t()")
        return
    
    # The zh object closes with a } on its own line (no comma, no indent)
    # Search for the closing pattern of zh block before function t()
    # It's the last } before the function, on a line by itself
    zh_close_idx = content.rfind('}', 0, func_idx)
    # But we need to find the zh block closing specifically, 
    # which is the second-to-last } before the function (outer object is the last)
    # Actually looking at the file:
    # }     <-- zh closing
    # }     <-- translations closing
    # function t()...
    # So we need the one before the very last }
    last_brace = content.rfind('}', 0, func_idx)
    zh_close_idx = content.rfind('}', 0, last_brace)
    
    if zh_close_idx == -1:
        print("  [ERROR] Could not find zh section closing")
        return
    
    # Build new translation strings
    new_en_keys = '\n    // V90 - Website 3.0 Upgrade\n'
    new_zh_keys = '\n        // V90 - Website 3.0 Upgrade\n'
    
    for key, vals in V90_TRANSLATIONS.items():
        en_val = vals['en']
        zh_val = vals['zh']
        # Escape special chars for JS string
        en_val_escaped = en_val.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
        zh_val_escaped = zh_val.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n')
        
        # en keys: no quotes on key name
        new_en_keys += f"    {key}: '{en_val_escaped}',\n"
        # zh keys: quoted key name
        new_zh_keys += f"        \"{key}\": '{zh_val_escaped}',\n"
    
    # Insert into en section (before the closing },)
    content = content[:en_close_idx] + new_en_keys + content[en_close_idx:]
    
    # Recalculate zh close position since we added content
    offset = len(new_en_keys)
    zh_close_idx += offset
    
    # Insert into zh section (before its closing })
    content = content[:zh_close_idx] + new_zh_keys + content[zh_close_idx:]
    
    write_file('js/translations.js', content)
    print(f"  [OK] Translations updated ({len(V90_TRANSLATIONS)} new keys)")

# =============================================
# PART 8: Homepage Knowledge Grid + CSS
# =============================================

def add_homepage_knowledge_script():
    """Add script to render knowledge grid on homepage from blog data"""
    content = read_file('index.html')
    
    script = '''
<script>
function renderV90Knowledge() {
    var grid = document.getElementById('v90KnowledgeGrid');
    if (!grid || typeof BLOG_POSTS === 'undefined') return;
    var useZh = localStorage.getItem('lang') === 'zh';
    // Featured slugs for homepage
    var featuredSlugs = [
        'laser-damage-threshold-guide',
        'bk7-vs-uv-fused-silica',
        'optical-beamsplitter-selection-complete-guide'
    ];
    var html = '';
    var count = 0;
    for (var i = 0; i < BLOG_POSTS.length && count < 3; i++) {
        var post = BLOG_POSTS[i];
        // Use featured first, then fall back to latest
        if (featuredSlugs.indexOf(post.slug) === -1 && count < featuredSlugs.length) continue;
        var postTitle = useZh && post.titleZh ? post.titleZh : post.title;
        var postExcerpt = useZh && post.excerptZh ? post.excerptZh : post.excerpt;
        var postCategory = useZh && post.categoryZh ? post.categoryZh : post.category;
        if (postExcerpt.length > 150) postExcerpt = postExcerpt.substring(0, 150) + '...';
        html += '<a href="/blog/' + post.slug + '/" class="v90-kb-card">';
        html += '<div class="v90-kb-cat">' + postCategory + '</div>';
        html += '<h3>' + postTitle + '</h3>';
        html += '<p>' + postExcerpt + '</p>';
        html += '<span class="v90-kb-link">Read Article &rarr;</span>';
        html += '</a>';
        count++;
    }
    // If we didn't get 3 from featured, grab latest
    if (count < 3) {
        for (var i = 0; i < BLOG_POSTS.length && count < 3; i++) {
            var post = BLOG_POSTS[i];
            var alreadyFeatured = false;
            // Check if already rendered
            for (var j = 0; j < featuredSlugs.length; j++) {
                if (featuredSlugs[j] === post.slug) { alreadyFeatured = true; break; }
            }
            if (alreadyFeatured) continue;
            var postTitle = useZh && post.titleZh ? post.titleZh : post.title;
            var postExcerpt = useZh && post.excerptZh ? post.excerptZh : post.excerpt;
            var postCategory = useZh && post.categoryZh ? post.categoryZh : post.category;
            if (postExcerpt.length > 150) postExcerpt = postExcerpt.substring(0, 150) + '...';
            html += '<a href="/blog/' + post.slug + '/" class="v90-kb-card">';
            html += '<div class="v90-kb-cat">' + postCategory + '</div>';
            html += '<h3>' + postTitle + '</h3>';
            html += '<p>' + postExcerpt + '</p>';
            html += '<span class="v90-kb-link">Read Article &rarr;</span>';
            html += '</a>';
            count++;
        }
    }
    grid.innerHTML = html;
}
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderV90Knowledge);
} else {
    renderV90Knowledge();
}
</script>
'''
    
    # Insert before chatbot.js
    if '<script src="/js/chatbot.js"></script>' in content:
        content = content.replace('<script src="/js/chatbot.js"></script>', script + '<script src="/js/chatbot.js"></script>')
    
    write_file('index.html', content)
    print("  [OK] Homepage knowledge script added")


def add_v90_css():
    """Add V90 CSS styles to style.css"""
    css = read_file('css/style.css')
    
    # Check if V90 styles already added
    if '/* V90 Styles */' in css:
        print("  [SKIP] V90 CSS already added")
        return
    
    v90_css = '''

/* =============================================
   V90 Homepage & Content Styles
   ============================================= */

/* Section tag */
.v90-section-tag {
    display: inline-block;
    background: #dbeafe;
    color: #1e40af;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 16px;
}
.v90-tag-light {
    background: rgba(255,255,255,0.15);
    color: #93c5fd;
}
.v90-section-title {
    font-size: 36px;
    color: #1e3a5f;
    margin-bottom: 12px;
    font-weight: 700;
}
.v90-section-subtitle {
    color: #64748b;
    font-size: 17px;
    max-width: 650px;
    margin: 0 auto 0 auto;
    line-height: 1.7;
}

/* Hero V90 */
.v90-hero-grid {
    display: grid;
    grid-template-columns: 1.3fr 1fr;
    gap: 50px;
    align-items: center;
}
.v90-hero-text h1 {
    font-size: 48px;
    line-height: 1.15;
}
.v90-hero-ai-card {
    background: white;
    border-radius: 20px;
    padding: 28px;
    box-shadow: 0 10px 40px rgba(30,58,95,0.1);
    border: 1px solid #e2e8f0;
}
.v90-ai-badge {
    margin-bottom: 12px;
    font-size: 14px;
}
.v90-ai-desc {
    color: #475569;
    font-size: 15px;
    margin-bottom: 18px;
    line-height: 1.6;
}
.v90-ai-input-row {
    display: flex;
    gap: 8px;
    margin-bottom: 16px;
}
.v90-ai-input {
    flex: 1;
    padding: 10px 14px;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    font-size: 14px;
    outline: none;
    cursor: pointer;
    transition: border-color 0.3s;
}
.v90-ai-input:focus {
    border-color: #3b82f6;
}
.v90-ai-btn {
    padding: 10px 18px;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    font-size: 14px;
    cursor: pointer;
    transition: transform 0.2s;
    white-space: nowrap;
}
.v90-ai-btn:hover {
    transform: translateY(-1px);
}
.v90-ai-samples {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}
.v90-ai-chip {
    padding: 4px 12px;
    background: #f1f5f9;
    color: #475569;
    border-radius: 20px;
    font-size: 12px;
    cursor: pointer;
    transition: background 0.2s;
}
.v90-ai-chip:hover {
    background: #e2e8f0;
}
.v90-trust-bar {
    margin: 25px 0;
}
.v90-hero-btns {
    margin-top: 20px;
}

/* Challenges grid */
.v90-challenges-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    max-width: 1200px;
    margin: 0 auto;
}
.v90-challenge-card {
    background: white;
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    transition: all 0.3s;
    border: 1px solid #e2e8f0;
}
.v90-challenge-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.1);
}
.v90-challenge-icon {
    width: 56px;
    height: 56px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    margin-bottom: 18px;
}
.v90-challenge-title {
    font-size: 22px;
    color: #1e293b;
    margin-bottom: 18px;
    font-weight: 700;
}
.v90-challenge-pain, .v90-challenge-solution {
    margin-bottom: 16px;
}
.v90-challenge-pain h4, .v90-challenge-solution h4 {
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
    font-weight: 700;
}
.v90-challenge-pain h4 {
    color: #dc2626;
}
.v90-challenge-solution h4 {
    color: #059669;
}
.v90-challenge-pain ul {
    list-style: none;
    padding: 0;
    margin: 0;
}
.v90-challenge-pain li {
    color: #475569;
    font-size: 14px;
    line-height: 1.6;
    padding-left: 18px;
    position: relative;
    margin-bottom: 6px;
}
.v90-challenge-pain li::before {
    content: "✕";
    position: absolute;
    left: 0;
    color: #fca5a5;
    font-size: 11px;
    top: 2px;
}
.v90-challenge-solution p {
    color: #475569;
    font-size: 14px;
    line-height: 1.6;
    margin: 0;
}
.v90-challenge-btn {
    display: inline-block;
    color: #3b82f6;
    font-weight: 600;
    text-decoration: none;
    font-size: 14px;
    padding: 8px 0;
    transition: transform 0.2s;
}
.v90-challenge-btn:hover {
    transform: translateX(4px);
}

/* Core Products */
.v90-products-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    max-width: 1100px;
    margin: 0 auto;
}
.v90-product-card {
    background: #f8fafc;
    border-radius: 14px;
    padding: 28px;
    text-decoration: none;
    display: block;
    border: 1px solid #e2e8f0;
    transition: all 0.3s;
}
.v90-product-card:hover {
    background: white;
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    border-color: #3b82f6;
}
.v90-product-icon {
    font-size: 42px;
    margin-bottom: 14px;
    color: #3b82f6;
}
.v90-product-card h3 {
    color: #1e293b;
    font-size: 20px;
    margin-bottom: 8px;
}
.v90-product-card p {
    color: #64748b;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 14px;
}
.v90-product-link {
    color: #3b82f6;
    font-weight: 600;
    font-size: 14px;
}

/* Why PhotonEdge */
.v90-why-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    max-width: 1200px;
    margin: 0 auto;
}
.v90-why-card {
    background: white;
    border-radius: 14px;
    padding: 28px;
    text-align: center;
    border: 1px solid #e2e8f0;
    transition: all 0.3s;
}
.v90-why-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
}
.v90-why-number {
    font-size: 36px;
    font-weight: 800;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 12px;
}
.v90-why-card h3 {
    color: #1e293b;
    font-size: 17px;
    margin-bottom: 10px;
}
.v90-why-card p {
    color: #64748b;
    font-size: 14px;
    line-height: 1.6;
}

/* Manufacturing Process */
.v90-mfg-steps {
    display: flex;
    align-items: stretch;
    justify-content: center;
    gap: 0;
    flex-wrap: wrap;
    max-width: 1300px;
    margin: 0 auto;
}
.v90-mfg-step {
    flex: 1;
    min-width: 140px;
    background: white;
    border-radius: 12px;
    padding: 20px 14px;
    text-align: center;
    border: 1px solid #e2e8f0;
}
.v90-mfg-step-num {
    font-size: 28px;
    font-weight: 800;
    color: #3b82f6;
    margin-bottom: 8px;
    opacity: 0.3;
}
.v90-mfg-step-icon {
    font-size: 32px;
    margin-bottom: 10px;
}
.v90-mfg-step h3 {
    font-size: 14px;
    color: #1e293b;
    margin-bottom: 8px;
    font-weight: 700;
}
.v90-mfg-step p {
    font-size: 12px;
    color: #64748b;
    line-height: 1.5;
}
.v90-mfg-step-arrow {
    display: flex;
    align-items: center;
    color: #cbd5e1;
    font-size: 20px;
    padding: 0 4px;
}

/* Measurement */
.v90-meas-quote {
    font-style: italic;
    font-size: 18px;
    color: rgba(255,255,255,0.8);
    margin-top: 20px;
    font-weight: 500;
}
.v90-meas-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    max-width: 1100px;
    margin: 0 auto;
}
.v90-meas-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 14px;
    padding: 28px;
    text-align: center;
    backdrop-filter: blur(10px);
    transition: all 0.3s;
}
.v90-meas-card:hover {
    background: rgba(255,255,255,0.12);
    transform: translateY(-3px);
}
.v90-meas-icon {
    font-size: 40px;
    margin-bottom: 14px;
}
.v90-meas-card h3 {
    color: white;
    font-size: 18px;
    margin-bottom: 10px;
}
.v90-meas-card p {
    color: rgba(255,255,255,0.7);
    font-size: 14px;
    line-height: 1.6;
}

/* Knowledge Hub */
.v90-kb-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    max-width: 1100px;
    margin: 0 auto;
}
.v90-kb-card {
    background: white;
    border-radius: 14px;
    padding: 28px;
    text-decoration: none;
    display: block;
    border: 1px solid #e2e8f0;
    transition: all 0.3s;
}
.v90-kb-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.1);
}
.v90-kb-cat {
    font-size: 12px;
    color: #3b82f6;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 10px;
}
.v90-kb-card h3 {
    color: #1e293b;
    font-size: 17px;
    margin-bottom: 10px;
    line-height: 1.4;
}
.v90-kb-card p {
    color: #64748b;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 14px;
}
.v90-kb-link {
    color: #3b82f6;
    font-weight: 600;
    font-size: 14px;
}

/* AI Section */
.v90-ai-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
    max-width: 1100px;
    margin: 0 auto;
}
.v90-ai-title {
    text-align: left;
    font-size: 34px;
}
.v90-ai-desc-full {
    color: #475569;
    font-size: 17px;
    line-height: 1.7;
    margin-bottom: 20px;
}
.v90-ai-benefits {
    list-style: none;
    padding: 0;
    margin: 0 0 28px 0;
}
.v90-ai-benefits li {
    color: #1e293b;
    padding: 8px 0;
    font-size: 15px;
}

/* Chat Mockup */
.v90-chat-window {
    background: white;
    border-radius: 18px;
    box-shadow: 0 20px 60px rgba(30,58,95,0.15);
    border: 1px solid #e2e8f0;
    overflow: hidden;
}
.v90-chat-header {
    background: linear-gradient(135deg, #1e3a5f, #2d5a87);
    color: white;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
    font-weight: 600;
    font-size: 15px;
}
.v90-chat-avatar {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: 700;
}
.v90-chat-body {
    padding: 20px;
    max-height: 340px;
    overflow-y: auto;
    background: #f8fafc;
}
.v90-chat-msg {
    margin-bottom: 14px;
    max-width: 85%;
}
.v90-chat-msg p {
    margin: 0 0 6px 0;
    font-size: 14px;
    line-height: 1.6;
}
.user-msg {
    margin-left: auto;
    text-align: right;
}
.user-msg p {
    display: inline-block;
    background: #3b82f6;
    color: white;
    padding: 10px 14px;
    border-radius: 14px 14px 4px 14px;
    text-align: left;
}
.ai-msg p {
    background: white;
    color: #1e293b;
    padding: 10px 14px;
    border-radius: 4px 14px 14px 14px;
    border: 1px solid #e2e8f0;
}

/* Cases */
.v90-cases-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
    max-width: 1100px;
    margin: 0 auto;
}
.v90-case-card {
    background: white;
    border-radius: 16px;
    padding: 28px;
    border: 1px solid #e2e8f0;
    transition: all 0.3s;
}
.v90-case-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.1);
}
.v90-case-industry {
    display: inline-block;
    background: #dbeafe;
    color: #1e40af;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 14px;
}
.v90-case-card h3 {
    color: #1e293b;
    font-size: 20px;
    margin-bottom: 16px;
}
.v90-case-body p {
    color: #475569;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 10px;
}
.v90-case-body strong {
    color: #1e293b;
}
.v90-case-link {
    display: inline-block;
    color: #3b82f6;
    font-weight: 600;
    text-decoration: none;
    font-size: 14px;
    margin-top: 8px;
}

/* Knowledge Center Tabs */
.v90-kc-tab {
    padding: 9px 20px;
    background: #f1f5f9;
    color: #475569;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
}
.v90-kc-tab:hover {
    background: #e2e8f0;
    color: #1e293b;
}
.v90-kc-tab.active {
    background: #3b82f6;
    color: white;
    border-color: #3b82f6;
}

/* Responsive */
@media (max-width: 1024px) {
    .v90-hero-grid { grid-template-columns: 1fr; }
    .v90-hero-text h1 { font-size: 38px; }
    .v90-challenges-grid { grid-template-columns: repeat(2, 1fr); }
    .v90-why-grid { grid-template-columns: repeat(2, 1fr); }
    .v90-meas-grid { grid-template-columns: repeat(2, 1fr); }
    .v90-ai-grid { grid-template-columns: 1fr; }
}
@media (max-width: 768px) {
    .v90-section-title { font-size: 28px; }
    .v90-hero-text h1 { font-size: 30px; }
    .v90-challenges-grid { grid-template-columns: 1fr; }
    .v90-products-grid { grid-template-columns: repeat(2, 1fr); }
    .v90-kb-grid { grid-template-columns: 1fr; }
    .v90-cases-grid { grid-template-columns: 1fr; }
    .v90-mfg-step-arrow { display: none; }
    .v90-mfg-steps { flex-direction: column; gap: 12px; }
}
@media (max-width: 480px) {
    .v90-products-grid { grid-template-columns: 1fr; }
    .v90-why-grid { grid-template-columns: 1fr; }
    .v90-meas-grid { grid-template-columns: 1fr; }
    .v90-ai-input-row { flex-direction: column; }
    .v90-ai-btn { width: 100%; }
}
'''
    
    # Append to CSS
    with open(os.path.join(BASE, 'css/style.css'), 'a', encoding='utf-8') as f:
        f.write(v90_css)
    
    print("  [OK] V90 CSS styles added")

# =============================================
# PART 9: Sitemap Update
# =============================================

def update_sitemap():
    """Add new URLs to sitemap.xml"""
    content = read_file('sitemap.xml')
    
    new_urls = [
        # Material pages
        '/materials/bk7/',
        '/materials/uv-fused-silica/',
        '/materials/caf2/',
        '/materials/znse/',
        '/materials/sapphire/',
    ]
    
    today = '2026-08-11'
    
    # Check which URLs already exist
    added = 0
    for url in new_urls:
        full_url = f'https://photonedgeoptics.com{url}'
        if full_url in content:
            continue
        
        url_entry = f'''
  <url>
    <loc>{full_url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
'''
        # Insert before </urlset>
        content = content.replace('</urlset>', url_entry + '</urlset>')
        added += 1
    
    write_file('sitemap.xml', content)
    print(f"  [OK] Sitemap updated ({added} new URLs)")

# =============================================
# MAIN
# =============================================

def main():
    print("=" * 60)
    print("PhotonEdge V90 Build Script")
    print("=" * 60)
    
    print("\n1. Building Homepage 3.0...")
    build_homepage()
    add_homepage_knowledge_script()
    
    print("\n2. Enhancing Application Pages...")
    build_application_pages()
    
    print("\n3. Enhancing Engineering Page...")
    build_engineering_page()
    
    print("\n4. Building Material Detail Pages...")
    build_material_pages()
    
    print("\n5. Building Case Studies Page...")
    build_case_studies_page()
    
    print("\n6. Upgrading Knowledge Center...")
    build_knowledge_center()
    
    print("\n7. Adding V90 CSS Styles...")
    add_v90_css()
    
    print("\n8. Updating Sitemap...")
    update_sitemap()
    
    print("\n9. Updating Translations...")
    update_translations()
    
    print("\n" + "=" * 60)
    print("V90 Build Complete!")
    print("=" * 60)

if __name__ == '__main__':
    main()
