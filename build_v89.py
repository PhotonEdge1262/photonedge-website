import os
import re
import json

BASE = '/app/data/所有对话/主对话/v88-build'

# ========================================
# 1. APPLICATION PAGES -> PRODUCT INNER LINKS
# ========================================

# Map: (page, old_text) -> new linked HTML
# Each application page's table has category names that should link to product pages

product_links = {
    'applications/laser-optics/index.html': [
        ('Laser Windows', '<a href="/products/uv-fused-silica-windows/" style="color:#2563eb;text-decoration:underline;">Fused Silica Windows</a>, <a href="/products/znse-windows/" style="color:#2563eb;text-decoration:underline;">ZnSe Windows</a>, <a href="/products/si-windows/" style="color:#2563eb;text-decoration:underline;">Si Windows</a>'),
        ('Laser Mirrors', '<a href="/products/laser-line-high-reflected-mirrors/" style="color:#2563eb;text-decoration:underline;">Laser Line Mirrors</a>, <a href="/products/protected-silver-mirrors/" style="color:#2563eb;text-decoration:underline;">Protected Silver</a>, <a href="/products/protected-gold-mirrors/" style="color:#2563eb;text-decoration:underline;">Protected Gold</a>, <a href="/products/high-energy-laser-mirrors/" style="color:#2563eb;text-decoration:underline;">Dielectric HR</a>'),
        ('Laser Lenses', '<a href="/products/uv-fused-silica-plano-convex/" style="color:#2563eb;text-decoration:underline;">Plano-Convex</a>, <a href="/products/aspherical-lenses/" style="color:#2563eb;text-decoration:underline;">Aspheric</a>, <a href="/products/achromatic-doublet/" style="color:#2563eb;text-decoration:underline;">Achromatic</a>'),
        ('Beam Expanders', '<a href="/products/laser-beam-expanders/" style="color:#2563eb;text-decoration:underline;">Galilean & Keplerian Expanders</a>'),
        ('Laser Filters', '<a href="/products/variable-neutral-density-filters/" style="color:#2563eb;text-decoration:underline;">ND Filters</a>, <a href="/products/narrow-band-interference-filters/" style="color:#2563eb;text-decoration:underline;">Bandpass Filters</a>'),
    ],
    'applications/semiconductor-inspection/index.html': [
        ('Imaging Lenses', '<a href="/products/achromatic-doublet/" style="color:#2563eb;text-decoration:underline;">Achromatic Doublets</a>, <a href="/products/aspherical-lenses/" style="color:#2563eb;text-decoration:underline;">Aspheric Lenses</a>, <a href="/products/uv-fused-silica-plano-convex/" style="color:#2563eb;text-decoration:underline;">UV Fused Silica Lenses</a>'),
        ('Illumination Optics', '<a href="/products/uv-fused-silica-windows/" style="color:#2563eb;text-decoration:underline;">UV Fused Silica Windows</a>'),
        ('Precision Filters', '<a href="/products/narrow-band-interference-filters/" style="color:#2563eb;text-decoration:underline;">Narrow Bandpass Filters</a>, <a href="/products/uv-bandpass-filters/" style="color:#2563eb;text-decoration:underline;">UV Bandpass Filters</a>'),
        ('Beam Splitters', '<a href="/products/cube-beamsplitters/" style="color:#2563eb;text-decoration:underline;">UV Cube Beamsplitters</a>, <a href="/products/dichroic-mirrors/" style="color:#2563eb;text-decoration:underline;">Dichroic Mirrors</a>'),
        ('Reference Optics', '<a href="/products/broadband-dielectric-mirrors/" style="color:#2563eb;text-decoration:underline;">Precision Flat Mirrors</a>'),
    ],
    'applications/medical-imaging/index.html': [
        ('Miniature Lenses', '<a href="/products/bk7-ball-lenses/" style="color:#2563eb;text-decoration:underline;">Ball Lenses</a>, <a href="/products/aspherical-lenses/" style="color:#2563eb;text-decoration:underline;">Aspheric Lenses</a>, <a href="/products/microscope-objectives/" style="color:#2563eb;text-decoration:underline;">Microscope Objectives</a>'),
        ('Optical Filters', '<a href="/products/narrow-band-interference-filters/" style="color:#2563eb;text-decoration:underline;">Bandpass Filters</a>, <a href="/products/dichroic-mirrors/" style="color:#2563eb;text-decoration:underline;">Dichroic Mirrors</a>'),
        ('Optical Windows', '<a href="/products/bk7-windows/" style="color:#2563eb;text-decoration:underline;">BK7 Windows</a>, <a href="/products/sapphire-windows/" style="color:#2563eb;text-decoration:underline;">Sapphire Windows</a>, <a href="/products/uv-fused-silica-windows/" style="color:#2563eb;text-decoration:underline;">Fused Silica</a>'),
        ('Beam Splitters', '<a href="/products/cube-beamsplitters/" style="color:#2563eb;text-decoration:underline;">Cube Beamsplitters</a>, <a href="/products/polarizing-cube-beamsplitters/" style="color:#2563eb;text-decoration:underline;">Polarizing Beamsplitters</a>'),
        ('Custom Assemblies', '<a href="/contact.html" style="color:#2563eb;text-decoration:underline;">Contact for Custom Solutions</a>'),
    ],
    'applications/aerospace-defense/index.html': [
        ('IR Windows', '<a href="/products/ge-windows/" style="color:#2563eb;text-decoration:underline;">Ge Windows</a>, <a href="/products/znse-windows/" style="color:#2563eb;text-decoration:underline;">ZnSe Windows</a>, <a href="/products/si-windows/" style="color:#2563eb;text-decoration:underline;">Si Windows</a>'),
        ('IR Lenses', '<a href="/products/ge-windows/" style="color:#2563eb;text-decoration:underline;">Ge Substrates</a>, <a href="/products/znse-windows/" style="color:#2563eb;text-decoration:underline;">ZnSe Substrates</a>'),
        ('Ruggedized Mirrors', '<a href="/products/protected-gold-mirrors/" style="color:#2563eb;text-decoration:underline;">Protected Gold Mirrors</a>, <a href="/products/enhanced-aluminum-mirrors/" style="color:#2563eb;text-decoration:underline;">Enhanced Aluminum</a>'),
        ('Visible Optics', '<a href="/products/sapphire-windows/" style="color:#2563eb;text-decoration:underline;">Sapphire Windows</a>, <a href="/products/uv-fused-silica-windows/" style="color:#2563eb;text-decoration:underline;">Fused Silica</a>'),
        ('Beam Splitters', '<a href="/products/dichroic-mirrors/" style="color:#2563eb;text-decoration:underline;">Dichroic Mirrors</a>, <a href="/products/cube-beamsplitters/" style="color:#2563eb;text-decoration:underline;">Metallic Beamsplitters</a>'),
    ],
    'applications/research-laboratory/index.html': [
        ('>Lenses<', '><a href="/products/bk7-plano-convex/" style="color:#2563eb;text-decoration:underline;">Plano-Convex</a>, <a href="/products/aspherical-lenses/" style="color:#2563eb;text-decoration:underline;">Aspheric</a>, <a href="/products/achromatic-doublet/" style="color:#2563eb;text-decoration:underline;">Achromatic</a>, <a href="/products/bk7-plano-convex-cylindrical/" style="color:#2563eb;text-decoration:underline;">Cylindrical</a><'),
        ('>Windows<', '><a href="/products/bk7-windows/" style="color:#2563eb;text-decoration:underline;">BK7</a>, <a href="/products/uv-fused-silica-windows/" style="color:#2563eb;text-decoration:underline;">Fused Silica</a>, <a href="/products/caf2-windows/" style="color:#2563eb;text-decoration:underline;">CaF2</a>, <a href="/products/sapphire-windows/" style="color:#2563eb;text-decoration:underline;">Sapphire</a>, <a href="/products/znse-windows/" style="color:#2563eb;text-decoration:underline;">ZnSe</a>, <a href="/products/ge-windows/" style="color:#2563eb;text-decoration:underline;">Ge</a><'),
        ('>Mirrors<', '><a href="/products/protected-silver-mirrors/" style="color:#2563eb;text-decoration:underline;">Protected Silver</a>, <a href="/products/protected-gold-mirrors/" style="color:#2563eb;text-decoration:underline;">Protected Gold</a>, <a href="/products/high-energy-laser-mirrors/" style="color:#2563eb;text-decoration:underline;">Dielectric HR</a><'),
        ('>Prisms<', '><a href="/products/bk7-right-angle-prisms/" style="color:#2563eb;text-decoration:underline;">Right Angle</a>, <a href="/products/dove-prisms/" style="color:#2563eb;text-decoration:underline;">Dove</a>, <a href="/products/penta-prisms/" style="color:#2563eb;text-decoration:underline;">Penta</a>, <a href="/products/equilateral-dispersing-prisms/" style="color:#2563eb;text-decoration:underline;">Dispersing</a><'),
        ('>Waveplates<', '><a href="/products/cemented-zero-order-waveplates/" style="color:#2563eb;text-decoration:underline;">Zero-Order</a>, <a href="/products/multiple-order-waveplates/" style="color:#2563eb;text-decoration:underline;">Multi-Order</a>, <a href="/products/air-spaced-zero-order-waveplates/" style="color:#2563eb;text-decoration:underline;">Achromatic</a><'),
        ('>Filters<', '><a href="/products/narrow-band-interference-filters/" style="color:#2563eb;text-decoration:underline;">Bandpass</a>, <a href="/products/variable-neutral-density-filters/" style="color:#2563eb;text-decoration:underline;">ND</a>, <a href="/products/ir-bandpass-filters/" style="color:#2563eb;text-decoration:underline;">IR</a><'),
    ],
}

count_linked = 0
for page_path, replacements in product_links.items():
    filepath = os.path.join(BASE, page_path)
    if not os.path.exists(filepath):
        print(f"SKIP: {filepath} not found")
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old_text, new_text in replacements:
        if old_text.startswith('>') and old_text.endswith('<'):
            # For research page, replace within td content
            content = content.replace(old_text, new_text, 1)
        else:
            # For other pages, replace the category name in first <td> of each row
            # Pattern: find the text within the td
            old_pattern = old_text + '</td>'
            new_pattern = new_text + '</td>'
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern, 1)
                count_linked += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Product links added: {count_linked}")

# ========================================
# 2. APPLICATION PAGES -> FAQ SCHEMA + ARTICLE SCHEMA
# ========================================

faq_schemas = {
    'applications/laser-optics/index.html': [
        ("What optical material should I use for a CO2 laser at 10.6 μm?", "ZnSe is the standard choice. It offers excellent transmission at 10.6 μm with good thermal conductivity. For lower-power CO2 systems (< 100 W), high-resistivity silicon can also work as a more economical alternative."),
        ("How do I choose a laser window for my system?", "Start with wavelength compatibility. Then evaluate: power/energy density for thermal management, whether AR coating is required, surface quality requirements (40-20 for beam delivery, 20-10 for intra-cavity), and mounting method."),
        ("What is LIDT and why does it matter?", "LIDT is Laser-Induced Damage Threshold — the maximum power density (W/cm2 for CW) or energy density (J/cm2 for pulsed) an optic can withstand. Always specify LIDT with test conditions: pulse duration, beam diameter, wavelength, and measurement standard (ISO 21254)."),
        ("When should I use AR coating vs. HR coating?", "AR coatings go on transmissive optics (windows, lenses) to minimize reflection loss. HR coatings go on mirrors. For intra-cavity optics, you may need both."),
        ("Can the same optic handle both CW and pulsed laser operation?", "Not necessarily without re-evaluation. CW is limited by steady-state thermal effects. Pulsed is limited by peak fluence at the coating interface."),
        ("Why does my UV laser optic degrade over time?", "UV wavelengths carry high photon energy that breaks chemical bonds in optical materials, creating color centers (solarization) that increase absorption. Mitigation: UV-grade fused silica, hydrogen loading, and UV-durable coatings."),
    ],
    'applications/semiconductor-inspection/index.html': [
        ("What optics do you recommend for 365nm inspection systems?", "For i-line (365 nm) systems, UV-grade fused silica is the standard substrate material. For higher-performance requirements, synthetic fused silica offers even lower metallic impurity content. CaF2 is typically reserved for 193 nm and 248 nm systems."),
        ("Can you provide cleanroom-compatible optics?", "Yes. All optics for semiconductor applications undergo cleanroom-compatible packaging. We can accommodate Class 100 cleanroom packaging, particle count specifications, and special handling procedures."),
        ("What wavefront error can you achieve?", "Standard specification is lambda/10 at the operating wavelength. For critical inspection applications, we can achieve lambda/20 or better."),
        ("How do you ensure batch-to-batch consistency?", "We maintain material traceability from substrate supplier through final inspection. Every batch is measured against the same reference standards."),
        ("What is your typical lead time for semiconductor-grade optics?", "Standard specifications: 2-3 weeks. Custom specifications with tight tolerances: 3-5 weeks depending on material availability and coating requirements."),
    ],
    'applications/medical-imaging/index.html': [
        ("What materials are biocompatible for medical optics?", "Sapphire (ISO 10993 biocompatible), UV fused silica, and BK7 are commonly used. For repeated sterilization, sapphire offers the best chemical resistance and hardness."),
        ("Can you provide optics for autoclave sterilization?", "Yes. Sapphire and fused silica optics withstand repeated autoclave cycles. We specify coatings that maintain adhesion and optical performance through sterilization."),
        ("What tolerances are achievable for miniature medical optics?", "We can achieve sub-millimeter diameters with lambda/4 flatness and 20-10 surface quality for medical imaging applications."),
        ("Do you provide documentation for FDA submissions?", "Yes. We provide full material traceability, inspection reports, and certificates of conformance to support your regulatory submissions."),
    ],
    'applications/aerospace-defense/index.html': [
        ("What IR material is best for thermal imaging?", "Germanium for LWIR (8-14 μm), ZnSe for MWIR/LWIR broadband, and Silicon for MWIR (3-5 μm). Selection depends on wavelength band, thermal environment, and SWaP constraints."),
        ("Can optics operate at extreme temperatures?", "Yes. We specify materials and coatings for -40°C to +85°C and beyond. Athermalization designs compensate for thermal focus shift."),
        ("Do you meet MIL-SPEC requirements?", "We can manufacture to MIL-PRF-13830B surface quality standards and accommodate MIL-STD environmental testing requirements."),
        ("What coating is best for harsh environments?", "Protected Gold for IR, protected silver for VIS/NIR, and DLC (diamond-like carbon) for ZnSe IR windows in outdoor environments."),
    ],
    'applications/research-laboratory/index.html': [
        ("What is your minimum order for custom optics?", "No minimum for stock items. Custom orders start from 1 piece for prototypes."),
        ("How fast can you deliver research optics?", "Standard stock items ship within 1-2 business days. Custom prototypes: 5-10 business days depending on specifications."),
        ("Can you match material properties for reproducibility?", "Yes. We maintain material traceability and can provide matching batch properties for replacement optics ordered months or years later."),
        ("Do you provide full inspection documentation?", "Every order includes interferometry reports, spectrophotometry data, and surface quality analysis when specified."),
    ],
}

article_schemas = {
    'applications/laser-optics/index.html': {
        'title': 'Laser Optics Solutions - Material Selection & Coating Guide',
        'description': 'Engineering guide for selecting optical components in laser systems: material properties, coating design, thermal management, and LIDT considerations.',
    },
    'applications/semiconductor-inspection/index.html': {
        'title': 'Semiconductor Inspection Optics - DUV Material & Coating Selection',
        'description': 'Technical guide for optical components in semiconductor inspection systems: DUV compatibility, wavefront control, contamination management, and batch consistency.',
    },
    'applications/medical-imaging/index.html': {
        'title': 'Medical Imaging Optics - Biocompatible Materials & Component Selection',
        'description': 'Engineering guide for optical components in medical devices: biocompatibility, sterilization compatibility, compact form factors, and regulatory documentation.',
    },
    'applications/aerospace-defense/index.html': {
        'title': 'Aerospace & Defense Optics - IR Materials & Ruggedized Components',
        'description': 'Technical guide for optical components in defense and aerospace: IR material selection, thermal management, vibration resistance, and environmental sealing.',
    },
    'applications/research-laboratory/index.html': {
        'title': 'Research & Laboratory Optics - Broadband Components & Custom Specifications',
        'description': 'Guide to selecting optical components for research: broadband materials, custom specifications, small quantity orders, and full documentation.',
    },
}

count_schema = 0
for page_path in faq_schemas:
    filepath = os.path.join(BASE, page_path)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Build FAQ JSON-LD
    faq_entities = []
    for q, a in faq_schemas[page_path]:
        faq_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })
    
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_entities
    }
    
    # Build Article JSON-LD
    art_info = article_schemas[page_path]
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": art_info['title'],
        "description": art_info['description'],
        "publisher": {
            "@type": "Organization",
            "name": "PhotonEdge Optics",
            "url": "https://photonedgeoptics.com"
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": "https://photonedgeoptics.com/" + page_path
        }
    }
    
    schema_html = '\n<script type="application/ld+json">\n' + json.dumps(faq_schema, ensure_ascii=False, indent=2) + '\n</script>\n'
    schema_html += '<script type="application/ld+json">\n' + json.dumps(article_schema, ensure_ascii=False, indent=2) + '\n</script>\n'
    
    # Insert before </head>
    content = content.replace('</head>', schema_html + '</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count_schema += 1

print(f"FAQ + Article schemas added to {count_schema} pages")

# ========================================
# 3. FOOTER -> ADD APPLICATIONS COLUMN
# ========================================

# The current footer has 4 columns: Products | Company | Resources | Contact
# We need to add Applications column between Products and Company

old_footer_section = '''<div class="footer-col">
                <h4 data-i18n="footerCompany">Company</h4>'''

new_applications_col = '''<div class="footer-col">
                <h4>Applications</h4>
                <ul>
                    <li><a href="/applications/laser-optics/" style="color:rgba(255,255,255,0.7);text-decoration:none;">Laser Systems</a></li>
                    <li><a href="/applications/semiconductor-inspection/" style="color:rgba(255,255,255,0.7);text-decoration:none;">Semiconductor</a></li>
                    <li><a href="/applications/medical-imaging/" style="color:rgba(255,255,255,0.7);text-decoration:none;">Medical Imaging</a></li>
                    <li><a href="/applications/aerospace-defense/" style="color:rgba(255,255,255,0.7);text-decoration:none;">Aerospace & Defense</a></li>
                    <li><a href="/applications/research-laboratory/" style="color:rgba(255,255,255,0.7);text-decoration:none;">Research & Laboratory</a></li>
                    <li><a href="/engineering.html" style="color:rgba(255,255,255,0.7);text-decoration:none;">Engineering Services</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4 data-i18n="footerCompany">Company</h4>'''

# Update footer across ALL HTML files
html_files = []
for root, dirs, files in os.walk(BASE):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

footer_count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_footer_section in content and 'Applications</h4>' not in content:
        content = content.replace(old_footer_section, new_applications_col)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        footer_count += 1

print(f"Applications column added to footer in {footer_count} files")

# ========================================
# 4. CONTACT PAGE -> UPDATE OG DESCRIPTION
# ========================================

contact_path = os.path.join(BASE, 'contact.html')
with open(contact_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'Get in touch for optical component quotes and custom solutions. We respond to all inquiries within 24 hours.',
    'Submit your optical specifications for engineering review. Material selection, coating design, DFM feedback — we respond within 24 hours.'
)

# Also update the H2 from "Get In Touch" to something more engineering-oriented
content = content.replace(
    'Get In Touch',
    'Request Engineering Review',
    1  # only first occurrence
)
content = content.replace(
    'Our team is ready to help with your optical component needs',
    'Share your specifications and our engineering team will review your requirements within 24 hours.',
    1
)

with open(contact_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Contact page updated")

# ========================================
# 5. AI OPTICAL ENGINEER PAGE -> UPGRADE
# ========================================
# Create a standalone ai-optical-engineer.html page
# This replaces the link from product-advisor.html to a proper AI engineering page

ai_page = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Optical Engineer - Free Optical Component Recommendation | PhotonEdge</title>
    <meta name="description" content="Describe your optical challenge and get instant AI-powered recommendations for materials, components, coatings, and specifications. Free tool for optical engineers.">
    <meta name="keywords" content="optical component advisor, AI optical engineer, lens recommendation, optical material selector, coating advisor, free optical tool">
    <meta property="og:title" content="AI Optical Engineer - Free Optical Component Recommendation | PhotonEdge">
    <meta property="og:description" content="Describe your optical challenge and get instant AI-powered recommendations for materials, components, coatings, and specifications.">
    <meta property="og:url" content="https://photonedgeoptics.com/ai-optical-engineer.html">
    <link rel="canonical" href="https://photonedgeoptics.com/ai-optical-engineer.html">
    <link rel="stylesheet" href="/css/style.css">
    <style>
        .ai-hero {
            background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 50%, #0c4a6e 100%);
            color: white;
            padding: 80px 20px 60px;
            text-align: center;
        }
        .ai-hero h1 {
            font-size: 42px;
            font-weight: 800;
            margin-bottom: 16px;
        }
        .ai-hero p {
            font-size: 18px;
            opacity: 0.9;
            max-width: 700px;
            margin: 0 auto 30px;
            line-height: 1.7;
        }
        .ai-container {
            max-width: 900px;
            margin: -30px auto 60px;
            padding: 0 20px;
        }
        .ai-card {
            background: white;
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.12);
            padding: 40px;
            margin-bottom: 30px;
        }
        .ai-card h2 {
            font-size: 24px;
            color: #1e3a5f;
            margin-bottom: 24px;
            font-weight: 700;
        }
        .ai-input-group {
            margin-bottom: 20px;
        }
        .ai-input-group label {
            display: block;
            font-weight: 600;
            color: #374151;
            margin-bottom: 8px;
            font-size: 14px;
        }
        .ai-input-group select,
        .ai-input-group input,
        .ai-input-group textarea {
            width: 100%;
            padding: 12px 16px;
            border: 2px solid #e5e7eb;
            border-radius: 8px;
            font-size: 15px;
            transition: border-color 0.2s;
            box-sizing: border-box;
        }
        .ai-input-group select:focus,
        .ai-input-group input:focus,
        .ai-input-group textarea:focus {
            outline: none;
            border-color: #2563eb;
        }
        .ai-input-group textarea {
            min-height: 120px;
            resize: vertical;
            font-family: inherit;
        }
        .ai-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
        .ai-submit-btn {
            display: inline-block;
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            color: white;
            border: none;
            padding: 14px 40px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            width: 100%;
            margin-top: 10px;
        }
        .ai-submit-btn:hover {
            background: linear-gradient(135deg, #1d4ed8, #1e40af);
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(37,99,235,0.3);
        }
        .ai-result {
            display: none;
            background: #f0fdf4;
            border: 2px solid #86efac;
            border-radius: 12px;
            padding: 30px;
            margin-top: 30px;
        }
        .ai-result h3 {
            color: #166534;
            font-size: 20px;
            margin-bottom: 16px;
        }
        .ai-result table {
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
        }
        .ai-result th,
        .ai-result td {
            padding: 10px 14px;
            text-align: left;
            border-bottom: 1px solid #d1fae5;
            font-size: 14px;
        }
        .ai-result th {
            background: #dcfce7;
            color: #166534;
            font-weight: 600;
        }
        .ai-features {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
            margin: 40px 0;
        }
        .ai-feature {
            text-align: center;
            padding: 24px 16px;
            background: #f8fafc;
            border-radius: 12px;
        }
        .ai-feature-icon {
            font-size: 36px;
            margin-bottom: 12px;
        }
        .ai-feature h3 {
            font-size: 16px;
            color: #1e3a5f;
            margin-bottom: 8px;
        }
        .ai-feature p {
            font-size: 14px;
            color: #6b7280;
            line-height: 1.6;
        }
        .ai-examples {
            background: #f8fafc;
            border-radius: 12px;
            padding: 24px;
            margin-top: 24px;
        }
        .ai-examples h4 {
            font-size: 15px;
            color: #374151;
            margin-bottom: 12px;
        }
        .ai-example-tag {
            display: inline-block;
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 20px;
            padding: 6px 14px;
            margin: 4px;
            font-size: 13px;
            color: #4b5563;
            cursor: pointer;
            transition: all 0.2s;
        }
        .ai-example-tag:hover {
            border-color: #2563eb;
            color: #2563eb;
            background: #eff6ff;
        }
        @media (max-width: 768px) {
            .ai-row { grid-template-columns: 1fr; }
            .ai-features { grid-template-columns: 1fr; }
            .ai-hero h1 { font-size: 28px; }
        }
    </style>
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "AI Optical Engineer",
        "description": "Free AI-powered optical component recommendation tool. Describe your application and get instant recommendations for materials, components, coatings, and specifications.",
        "url": "https://photonedgeoptics.com/ai-optical-engineer.html",
        "applicationCategory": "DesignApplication",
        "operatingSystem": "Web Browser",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
        },
        "publisher": {
            "@type": "Organization",
            "name": "PhotonEdge Optics",
            "url": "https://photonedgeoptics.com"
        }
    }
    </script>
</head>
<body>
NAV_PLACEHOLDER
    <!-- Hero -->
    <section class="ai-hero">
        <h1>AI Optical Engineering Assistant</h1>
        <p>Describe your optical challenge below. Our AI will recommend materials, components, coatings, and specifications based on your application requirements.</p>
    </section>

    <div class="ai-container">
        <!-- Main Form -->
        <div class="ai-card">
            <h2>Tell Us About Your Application</h2>
            <form id="aiOpticalForm" onsubmit="return handleAIRecommend(event)">
                <div class="ai-row">
                    <div class="ai-input-group">
                        <label for="aiApplication">Application Area *</label>
                        <select id="aiApplication" required>
                            <option value="">Select your application...</option>
                            <option value="laser">Laser Systems (Cutting/Welding/Marking)</option>
                            <option value="semiconductor">Semiconductor Inspection & Metrology</option>
                            <option value="medical">Medical Imaging & Diagnostics</option>
                            <option value="spectroscopy">Spectroscopy & Analytical</option>
                            <option value="imaging">Machine Vision & Imaging</option>
                            <option value="telecom">Telecommunications & Fiber Optics</option>
                            <option value="defense">Defense & Aerospace (IR/Thermal)</option>
                            <option value="research">Research & Laboratory</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                    <div class="ai-input-group">
                        <label for="aiWavelength">Operating Wavelength *</label>
                        <select id="aiWavelength" required>
                            <option value="">Select wavelength range...</option>
                            <option value="duv">Deep UV (193-280 nm)</option>
                            <option value="uv">UV (280-400 nm)</option>
                            <option value="vis">Visible (400-700 nm)</option>
                            <option value="nir">Near IR (700-1400 nm)</option>
                            <option value="swir">SWIR (1400-3000 nm)</option>
                            <option value="mwir">MWIR (3-5 μm)</option>
                            <option value="lwir">LWIR (8-14 μm)</option>
                            <option value="broadband">Broadband / Multi-wavelength</option>
                        </select>
                    </div>
                </div>
                <div class="ai-row">
                    <div class="ai-input-group">
                        <label for="aiComponent">Component Type Needed</label>
                        <select id="aiComponent">
                            <option value="">Select component type...</option>
                            <option value="lens">Lenses (Plano-Convex, Aspheric, etc.)</option>
                            <option value="window">Windows & Substrates</option>
                            <option value="mirror">Mirrors (HR, Protected, etc.)</option>
                            <option value="filter">Filters (Bandpass, ND, etc.)</option>
                            <option value="prism">Prisms & Beamsplitters</option>
                            <option value="waveplate">Waveplates & Polarizers</option>
                            <option value="assembly">Custom Optical Assembly</option>
                            <option value="unsure">Not Sure — Need Recommendation</option>
                        </select>
                    </div>
                    <div class="ai-input-group">
                        <label for="aiPower">Laser Power / Energy (if applicable)</label>
                        <input type="text" id="aiPower" placeholder="e.g., 500W CW, 10mJ pulsed, N/A">
                    </div>
                </div>
                <div class="ai-input-group">
                    <label for="aiDescription">Describe Your Requirements *</label>
                    <textarea id="aiDescription" required placeholder="Tell us about your optical system: what it does, key performance requirements, environment, any constraints (size, budget, timeline)..."></textarea>
                </div>
                <button type="submit" class="ai-submit-btn">Get Optical Recommendation →</button>
            </form>
            
            <!-- AI Result -->
            <div class="ai-result" id="aiResult">
                <h3>📋 Recommended Optical Solution</h3>
                <div id="aiResultContent"></div>
                <div style="margin-top:24px;padding:20px;background:white;border-radius:8px;border:1px solid #d1fae5;">
                    <p style="font-size:15px;color:#374151;margin-bottom:16px;font-weight:600;">Get Detailed Engineering Review</p>
                    <p style="font-size:14px;color:#6b7280;margin-bottom:16px;">Our engineering team can provide a detailed specification review, material selection analysis, and custom quote for your application.</p>
                    <div class="ai-row">
                        <div class="ai-input-group">
                            <input type="email" id="aiEmail" placeholder="Your work email">
                        </div>
                        <div>
                            <a href="/contact.html" class="ai-submit-btn" style="display:block;text-align:center;text-decoration:none;" onclick="if(document.getElementById('aiEmail').value){return true;}">Request Engineering Review →</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Features -->
        <div class="ai-features">
            <div class="ai-feature">
                <div class="ai-feature-icon">🔬</div>
                <h3>Material Selection</h3>
                <p>40+ optical materials matched to your wavelength, power, and environmental requirements</p>
            </div>
            <div class="ai-feature">
                <div class="ai-feature-icon">⚡</div>
                <h3>Coating Recommendation</h3>
                <p>AR, HR, bandpass, and specialty coating designs optimized for your application</p>
            </div>
            <div class="ai-feature">
                <div class="ai-feature-icon">📐</div>
                <h3>Specification Review</h3>
                <p>Tolerance analysis and DFM feedback to optimize performance vs. cost</p>
            </div>
        </div>

        <!-- Example Queries -->
        <div class="ai-examples">
            <h4>Try these examples:</h4>
            <span class="ai-example-tag" onclick="fillExample('laser','nir','window','500W CW fiber laser at 1070nm, need output window for beam delivery')">Fiber laser output window</span>
            <span class="ai-example-tag" onclick="fillExample('semiconductor','duv','filter','365nm inspection system, need narrow bandpass filter for i-line illumination')">365nm inspection filter</span>
            <span class="ai-example-tag" onclick="fillExample('medical','vis','lens','Endoscope imaging system, need miniature achromatic doublet, 3mm diameter')">Miniature endoscope lens</span>
            <span class="ai-example-tag" onclick="fillExample('defense','lwir','window','Thermal imaging system at 8-12μm, need ruggedized window for outdoor use')">LWIR thermal window</span>
            <span class="ai-example-tag" onclick="fillExample('spectroscopy','uv','prism','Raman spectroscopy, need CaF2 prism for dispersion at 250-800nm')">CaF2 Raman prism</span>
            <span class="ai-example-tag" onclick="fillExample('research','broadband','mirror','Ultrafast laser system, need broadband mirrors for 700-1100nm range')">Broadband femtosecond mirrors</span>
        </div>
    </div>

    <!-- Also link to Smart Product Advisor -->
    <div style="max-width:900px;margin:0 auto 60px;padding:0 20px;">
        <div class="ai-card" style="background:#f8fafc;text-align:center;">
            <h2>Prefer Guided Selection?</h2>
            <p style="color:#6b7280;margin-bottom:20px;">Use our step-by-step Smart Product Advisor for component-by-component selection from our catalog.</p>
            <a href="/product-advisor.html" style="display:inline-block;background:#1e3a5f;color:white;padding:12px 30px;border-radius:8px;text-decoration:none;font-weight:600;">Open Smart Product Advisor →</a>
        </div>
    </div>

FOOTER_PLACEHOLDER

    <script>
    function fillExample(app, wl, comp, desc) {
        document.getElementById('aiApplication').value = app;
        document.getElementById('aiWavelength').value = wl;
        document.getElementById('aiComponent').value = comp;
        document.getElementById('aiDescription').value = desc;
        document.getElementById('aiDescription').scrollIntoView({behavior: 'smooth', block: 'center'});
    }

    var materialDB = {
        'duv': {primary: 'CaF2, Synthetic Fused Silica', note: 'Low metallic impurity, low birefringence required'},
        'uv': {primary: 'UV Fused Silica, CaF2', note: 'UV-grade with low OH content for solarization resistance'},
        'vis': {primary: 'BK7, UV Fused Silica, Sapphire', note: 'BK7 for cost-effective, Sapphire for durability'},
        'nir': {primary: 'BK7, UV Fused Silica, ZnSe', note: 'Depends on power level and thermal requirements'},
        'swir': {primary: 'Fused Silica, ZnSe, Sapphire', note: 'ZnSe for broadband IR, Sapphire for durability'},
        'mwir': {primary: 'Silicon, ZnSe', note: 'Si for lightweight, ZnSe for broadband'},
        'lwir': {primary: 'Germanium, ZnSe', note: 'Ge for compact designs, ZnSe for lower cost'},
        'broadband': {primary: 'CaF2, UV Fused Silica', note: 'CaF2 for widest range, Fused Silica for UV-NIR'}
    };

    var coatingDB = {
        'laser': 'High-LIDT AR coating optimized for your wavelength and power regime',
        'semiconductor': 'Precision bandpass/edge filters with tight center wavelength tolerance',
        'medical': 'Biocompatible coatings validated for sterilization compatibility',
        'spectroscopy': 'Broadband AR for maximum transmission across spectral range',
        'imaging': 'Multi-layer AR for visible range, optimized for sensor spectral response',
        'telecom': 'Fiber-matched coatings for minimum insertion loss',
        'defense': 'Ruggedized protective coatings (DLC for IR, protected metal for VIS)',
        'research': 'Custom coating designs for multi-wavelength or ultrafast applications',
        'other': 'Application-specific coating design based on your requirements'
    };

    function handleAIRecommend(e) {
        e.preventDefault();
        var app = document.getElementById('aiApplication').value;
        var wl = document.getElementById('aiWavelength').value;
        var comp = document.getElementById('aiComponent').value;
        var desc = document.getElementById('aiDescription').value;
        var power = document.getElementById('aiPower').value;

        var mat = materialDB[wl] || materialDB['vis'];
        var coat = coatingDB[app] || coatingDB['other'];

        var compRecs = {
            'lens': 'Plano-Convex / Aspheric / Achromatic Doublet (depending on imaging vs. beam shaping requirements)',
            'window': 'Circular/Square Window with AR coating on both sides',
            'mirror': 'Protected Metal or Dielectric HR mirror (depending on wavelength and power)',
            'filter': 'Bandpass / Edge / Longpass / Shortpass interference filter',
            'prism': 'Right-Angle / Dispersing / Beam Displacement prism',
            'waveplate': 'Zero-Order / Achromatic waveplate for polarization control',
            'assembly': 'Custom multi-element assembly per your specifications',
            'unsure': 'Based on your description, we recommend starting with a technical review to identify the optimal component type'
        };

        var html = '<table>';
        html += '<tr><th>Parameter</th><th>Recommendation</th></tr>';
        html += '<tr><td><strong>Recommended Material</strong></td><td>' + mat.primary + '<br><small style="color:#6b7280;">' + mat.note + '</small></td></tr>';
        html += '<tr><td><strong>Coating Type</strong></td><td>' + coat + '</td></tr>';
        if (comp && compRecs[comp]) {
            html += '<tr><td><strong>Component Type</strong></td><td>' + compRecs[comp] + '</td></tr>';
        }
        if (power) {
            html += '<tr><td><strong>Power Consideration</strong></td><td>' + power + ' — LIDT and thermal management will be factored into specification</td></tr>';
        }
        html += '<tr><td><strong>Surface Quality</strong></td><td>40-20 (standard) or 20-10 (precision) per MIL-PRF-13830B</td></tr>';
        html += '<tr><td><strong>Typical Lead Time</strong></td><td>Stock items: 1-3 days | Custom: 5-10 business days</td></tr>';
        html += '</table>';
        html += '<p style="margin-top:16px;font-size:14px;color:#374151;"><strong>Next Step:</strong> For a detailed specification and quote, submit your requirements for engineering review. Our team will respond within 24 hours with material verification, coating design options, and DFM feedback.</p>';

        document.getElementById('aiResultContent').innerHTML = html;
        document.getElementById('aiResult').style.display = 'block';
        document.getElementById('aiResult').scrollIntoView({behavior: 'smooth'});
        return false;
    }
    </script>
</body>
</html>'''

# Now inject navigation and footer from index.html
with open(os.path.join(BASE, 'index.html'), 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract nav
nav_match = re.search(r'(<header.*?</header>)', index_content, re.DOTALL)
if nav_match:
    nav_html = nav_match.group(1)
    # Update the AI Optical Engineer link to point to the new page
    nav_html = nav_html.replace('/product-advisor.html" class="nav-link" data-i18n="navAIOptical', '/ai-optical-engineer.html" class="nav-link" data-i18n="navAIOptical')
    ai_page = ai_page.replace('NAV_PLACEHOLDER', nav_html)

# Extract footer
footer_match = re.search(r'(<footer.*?</footer>)', index_content, re.DOTALL)
if footer_match:
    footer_html = footer_match.group(1)
    ai_page = ai_page.replace('FOOTER_PLACEHOLDER', footer_html)

# Also add WhatsApp float
if 'whatsapp-float' in index_content:
    wa_match = re.search(r'(<!-- WhatsApp Floating Button -->.*?</a>)', index_content, re.DOTALL)
    if wa_match:
        ai_page = ai_page.replace('</body>', wa_match.group(1) + '\n</body>')

# Add script tags
scripts = '''<script src="/js/translations.js"></script>
<script src="/js/products-data.js"></script>'''
ai_page = ai_page.replace('</body>', scripts + '\n</body>')

# Update AI Optical Engineer nav link across ALL files
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if '/product-advisor.html" class="nav-link" data-i18n="navAIOptical' in content:
        content = content.replace('/product-advisor.html" class="nav-link" data-i18n="navAIOptical', '/ai-optical-engineer.html" class="nav-link" data-i18n="navAIOptical')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# Write AI page
with open(os.path.join(BASE, 'ai-optical-engineer.html'), 'w', encoding='utf-8') as f:
    f.write(ai_page)
print("AI Optical Engineer page created")

# ========================================
# 6. UPDATE SITEMAP
# ========================================

with open(os.path.join(BASE, 'sitemap.xml'), 'r', encoding='utf-8') as f:
    sitemap = f.read()

new_urls = [
    'https://photonedgeoptics.com/ai-optical-engineer.html',
]

for url in new_urls:
    if url not in sitemap:
        entry = '''  <url>
    <loc>''' + url + '''</loc>
    <lastmod>2026-08-11</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
'''
        sitemap = sitemap.replace('</urlset>', entry + '</urlset>')

# Update lastmod for all application and engineering URLs
for url_pattern in ['/engineering.html', '/applications/laser-optics/', '/applications/semiconductor-inspection/', '/applications/medical-imaging/', '/applications/aerospace-defense/', '/applications/research-laboratory/']:
    sitemap = sitemap.replace(
        '<loc>https://photonedgeoptics.com' + url_pattern + '</loc>\n    <lastmod>2026-08-02</lastmod>',
        '<loc>https://photonedgeoptics.com' + url_pattern + '</loc>\n    <lastmod>2026-08-11</lastmod>'
    )

# Also update main pages lastmod
for url_pattern in ['/', '/about.html', '/contact.html', '/applications.html']:
    old = '<loc>https://photonedgeoptics.com' + url_pattern + '</loc>\n    <lastmod>2026-08-02</lastmod>'
    new = '<loc>https://photonedgeoptics.com' + url_pattern + '</loc>\n    <lastmod>2026-08-11</lastmod>'
    if url_pattern == '/':
        old = '<loc>https://photonedgeoptics.com/</loc>\n    <lastmod>2026-08-02</lastmod>'
        new = '<loc>https://photonedgeoptics.com/</loc>\n    <lastmod>2026-08-11</lastmod>'
    sitemap = sitemap.replace(old, new)

with open(os.path.join(BASE, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap)
print("Sitemap updated")

# ========================================
# 7. UPDATE HOMEPAGE - Machine Vision link fix
# ========================================
# Machine Vision currently links to research-laboratory, should have its own section or at least a clear note

# ========================================
# SUMMARY
# ========================================
print("\n=== V89 BUILD COMPLETE ===")
print("Changes:")
print("1. Application pages: Product inner links added")
print("2. Application pages: FAQ + Article Schema added")
print("3. Footer: Applications column added to ALL pages")
print("4. Contact page: Updated to RFQ-oriented")
print("5. AI Optical Engineer: New standalone page created")
print("6. Navigation: AI Optical Engineer link updated across ALL pages")
print("7. Sitemap: New URLs added, lastmod updated")
