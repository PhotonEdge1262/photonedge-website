#!/usr/bin/env python3
"""
PhotonEdge V4.0 Phase 2b - Business Conversion Optimization
"""
import os
import re
import sys

WORK_DIR = '/tmp/v156-work'
PRODUCTS_DIR = os.path.join(WORK_DIR, 'products')

KC_ARTICLES = {
    'Optical Lenses': [
        ('/knowledge-center/optical-materials-selection-handbook/', 'Optical Materials Selection Handbook'),
        ('/knowledge-center/laser-optics-components-guide/', 'Laser Optics Components Guide'),
    ],
    'Optical Windows': [
        ('/knowledge-center/optical-materials-selection-handbook/', 'Optical Materials Selection Handbook'),
        ('/knowledge-center/optical-window-material-selection-harsh-environments/', 'Window Material Selection for Harsh Environments'),
    ],
    'Optical Mirrors': [
        ('/knowledge-center/optical-coatings-complete-guide/', 'Optical Coatings Complete Guide'),
        ('/knowledge-center/laser-optics-components-guide/', 'Laser Optics Components Guide'),
    ],
    'Optical Filters': [
        ('/knowledge-center/optical-coatings-complete-guide/', 'Optical Coatings Complete Guide'),
        ('/knowledge-center/laser-optics-components-guide/', 'Laser Optics Components Guide'),
    ],
    'Prisms & Beamsplitters': [
        ('/knowledge-center/laser-optics-components-guide/', 'Laser Optics Components Guide'),
        ('/knowledge-center/optical-materials-selection-handbook/', 'Optical Materials Selection Handbook'),
    ],
    'Waveplates & Polarizers': [
        ('/knowledge-center/laser-optics-components-guide/', 'Laser Optics Components Guide'),
        ('/knowledge-center/optical-coatings-complete-guide/', 'Optical Coatings Complete Guide'),
    ],
    'Custom Optics': [
        ('/knowledge-center/optical-materials-selection-handbook/', 'Optical Materials Selection Handbook'),
        ('/knowledge-center/optical-coatings-complete-guide/', 'Optical Coatings Complete Guide'),
    ],
    'Optical Mounts': [
        ('/knowledge-center/laser-optics-components-guide/', 'Laser Optics Components Guide'),
    ],
}

AN_ARTICLES = {
    'Optical Lenses': [
        ('/application-notes/ar-coating-specification-multi-wavelength/', 'AR Coating Specification for Multi-Wavelength Systems'),
    ],
    'Optical Windows': [
        ('/application-notes/optical-window-material-selection-harsh-environments/', 'Window Material Selection for Harsh Environments'),
        ('/application-notes/optics-for-vacuum-and-cleanroom/', 'Optics for Vacuum and Cleanroom Applications'),
    ],
    'Optical Mirrors': [
        ('/application-notes/ar-coating-specification-multi-wavelength/', 'AR Coating Specification Guide'),
    ],
    'Optical Filters': [
        ('/application-notes/ar-coating-specification-multi-wavelength/', 'AR Coating Specification Guide'),
    ],
    'Prisms & Beamsplitters': [
        ('/application-notes/beam-expander-design-considerations/', 'Beam Expander Design Considerations'),
    ],
    'Waveplates & Polarizers': [
        ('/application-notes/ar-coating-specification-multi-wavelength/', 'AR Coating Specification Guide'),
    ],
}

GENERIC_FAQ = '''    <!-- FAQ Schema -->
    <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":"Can I order custom specifications for this product?","acceptedAnswer":{"@type":"Answer","text":"Yes. PhotonEdge supports custom diameters, wavelengths, coatings, surface qualities and quantities. Provide your drawing or specification and our engineering team will respond within 24 hours."}},
        {"@type":"Question","name":"What information should I include in my RFQ?","acceptedAnswer":{"@type":"Answer","text":"Include: (1) Material/substrate, (2) Dimensions, (3) Surface quality, (4) Coating type and wavelength, (5) Quantity, (6) Application context. Upload drawings in PDF/DXF/STEP format for fastest response."}},
        {"@type":"Question","name":"Do you provide inspection reports and certificates?","acceptedAnswer":{"@type":"Answer","text":"Yes. Dimensional inspection reports, surface quality verification, coating performance data, and Certificates of Conformance are available according to project requirements."}},
        {"@type":"Question","name":"What is the typical lead time?","acceptedAnswer":{"@type":"Answer","text":"Standard catalog items: 1-2 weeks. Custom specifications: 3-6 weeks depending on complexity. Rush orders available for urgent projects."}},
        {"@type":"Question","name":"How do I request a quote?","acceptedAnswer":{"@type":"Answer","text":"Click the Request a Quote button, fill in your specifications and upload drawings if available. Our engineering team will respond with a detailed quotation within 24 hours."}}
    ]}
    </script>
'''

def build_kc_links(category):
    kc = KC_ARTICLES.get(category, KC_ARTICLES.get('Custom Optics', []))
    an = AN_ARTICLES.get(category, [])
    links = ''
    for url, title in kc:
        links += '<a href="%s" style="display:inline-flex;align-items:center;padding:10px 18px;background:#f0f9ff;border:1px solid #bae6fd;border-radius:8px;text-decoration:none;color:#0369a1;font-size:0.9rem;font-weight:500;margin:4px;">%s</a>\n' % (url, title)
    for url, title in an:
        links += '<a href="%s" style="display:inline-flex;align-items:center;padding:10px 18px;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;text-decoration:none;color:#166534;font-size:0.9rem;font-weight:500;margin:4px;">%s</a>\n' % (url, title)
    if not an:
        links += '<a href="/application-notes/surface-quality-scratch-dig-explained/" style="display:inline-flex;align-items:center;padding:10px 18px;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;text-decoration:none;color:#166534;font-size:0.9rem;font-weight:500;margin:4px;">Surface Quality: Scratch-Dig Explained</a>\n'
    return links

def detect_category(slug, content):
    patterns = {
        'Optical Lenses': ['lens', 'lenses', 'doublet', 'achromatic', 'plano-convex', 'plano-concave', 'bi-convex', 'bi-concave', 'meniscus', 'aspheric', 'aspherical', 'ball-lens', 'rod-lens', 'cylindrical-lens', 'c-mount', 'microscope-objective', 'nbk7-achromatic', 'nbk7-plano', 'fused-silica-plano', 'fused-silica-bi', 'fused-silica-laser-lens', 'znse-plano', 'znse-co2', 'germanium-infrared', 'silicon-infrared', 'caf2-plano'],
        'Optical Windows': ['window', 'windows', 'substrate'],
        'Optical Mirrors': ['mirror', 'mirrors', 'reflective', 'retroreflector'],
        'Optical Filters': ['filter', 'filters', 'bandpass', 'longpass', 'shortpass', 'dichroic', 'neutral-density'],
        'Prisms & Beamsplitters': ['prism', 'prisms', 'beamsplitter', 'cube', 'penta', 'dove', 'roof', 'corner-cube', 'wollaston'],
        'Waveplates & Polarizers': ['waveplate', 'waveplates', 'retarder', 'polarizer', 'polarizers', 'glan'],
        'Custom Optics': ['custom'],
        'Optical Mounts': ['mount', 'frame', 'retaining-cell', 'rotating'],
    }
    slug_lower = slug.lower()
    for cat, pats in patterns.items():
        for p in pats:
            if p in slug_lower:
                return cat
    if 'Optical Lenses' in content: return 'Optical Lenses'
    if 'Optical Windows' in content: return 'Optical Windows'
    if 'Optical Mirrors' in content: return 'Optical Mirrors'
    if 'Optical Filters' in content: return 'Optical Filters'
    if 'Prism' in content or 'Beamsplitter' in content: return 'Prisms & Beamsplitters'
    if 'Waveplate' in content or 'Polarizer' in content: return 'Waveplates & Polarizers'
    return 'Custom Optics'

def is_v3(content): return 'product-hero-31' in content
def is_dynamic(content): return 'product-enhanced-render' in content

MID_CTA_V3 = '''
    <!-- Mid-Page CTA -->
    <section class="product-section-31" style="background:linear-gradient(135deg,#1e3a5f,#2563eb);padding:40px 20px;text-align:center;">
        <div style="max-width:800px;margin:0 auto;">
            <h2 style="color:white;font-size:1.4rem;margin-bottom:12px;">Have a Custom Optical Requirement?</h2>
            <p style="color:#bfdbfe;margin-bottom:20px;font-size:0.95rem;">Upload your drawing or describe your specification. Our engineering team will review and respond within 24 hours with a detailed quotation.</p>
            <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
                <a href="/contact.html" style="background:white;color:#1e3a5f;padding:12px 28px;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.95rem;">Upload Drawing / RFQ</a>
                <a href="/ai-optical-engineer.html" style="background:transparent;color:white;padding:12px 28px;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.95rem;border:1px solid rgba(255,255,255,0.4);">Ask AI Optical Engineer</a>
            </div>
        </div>
    </section>
'''

MID_CTA_SIMPLE = '''
    <!-- Mid-Page CTA -->
    <section style="background:linear-gradient(135deg,#1e3a5f,#2563eb);padding:40px 20px;text-align:center;margin:30px 0;">
        <div style="max-width:800px;margin:0 auto;">
            <h2 style="color:white;font-size:1.4rem;margin-bottom:12px;">Have a Custom Optical Requirement?</h2>
            <p style="color:#bfdbfe;margin-bottom:20px;font-size:0.95rem;">Upload your drawing or describe your specification. Our engineering team will review and respond within 24 hours.</p>
            <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
                <a href="/contact.html" style="background:white;color:#1e3a5f;padding:12px 28px;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.95rem;">Upload Drawing / RFQ</a>
                <a href="/ai-optical-engineer.html" style="background:transparent;color:white;padding:12px 28px;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.95rem;border:1px solid rgba(255,255,255,0.4);">Ask AI Optical Engineer</a>
            </div>
        </div>
    </section>
'''

BOTTOM_RFQ_V3 = '''
    <!-- Bottom RFQ -->
    <section class="product-section-31">
        <div class="rfq-section-31">
            <h2>Ready to Start Your Project?</h2>
            <p style="color:#475569;max-width:600px;margin:0 auto 16px;">Upload your drawing or describe your requirements. Our engineering team will respond within 24 hours with a detailed quotation and technical review.</p>
            <div style="margin:20px 0;">
                <a href="/contact.html" class="btn-primary-31" style="margin:0 6px;">Upload Drawing / RFQ</a>
                <a href="/ai-optical-engineer.html" class="btn-secondary-31" style="margin:0 6px;">Ask AI Optical Engineer</a>
            </div>
            <p style="color:#94a3b8;font-size:0.8rem;margin-top:12px;">We accept drawings in PDF, DXF, STEP, IGES formats. Include material, dimensions, surface quality, coating, and quantity for fastest response.</p>
        </div>
    </section>
'''

stats = {'total': 0, 'modified': 0, 'v3': 0, 'simple': 0, 'dynamic': 0,
         'mid_cta': 0, 'faq_schema': 0, 'kc_links': 0, 'bottom_rfq': 0}
modified_files = []

for slug in sorted(os.listdir(PRODUCTS_DIR)):
    fpath = os.path.join(PRODUCTS_DIR, slug, 'index.html')
    if not os.path.isfile(fpath): continue
    
    stats['total'] += 1
    with open(fpath, 'r', encoding='utf-8') as f:
        original = f.read()
    
    content = original
    category = detect_category(slug, content)
    changed = False
    
    had_mid = 'Mid-Page CTA' in content
    had_faq = 'FAQPage' in content
    had_kc = len(re.findall(r'/knowledge-center/', content)) > 1
    had_rfq = 'rfq-section' in content or ('Ready to Start' in content and 'Upload Drawing' in content)
    
    if is_v3(content):
        stats['v3'] += 1
        
        # 1. Mid-page CTA
        if not had_mid:
            inserted = False
            for marker in ['<!-- Applications -->', '<!-- Manufacturing & Quality -->', '<!-- Engineering Documentation -->', '<!-- FAQ -->']:
                if marker in content:
                    content = content.replace(marker, MID_CTA_V3 + '\n    ' + marker, 1)
                    inserted = True
                    break
            if not inserted:
                content = content.replace('<!-- Footer -->', MID_CTA_V3 + '\n    <!-- Footer -->', 1)
            changed = True
        
        # 2. Internal links
        if not had_kc:
            links = build_kc_links(category)
            section = '''
    <!-- Further Reading -->
    <section class="product-section-31 alt-bg">
        <div class="section-inner">
            <h2 class="section-title-31">Further Reading: Engineering Guides</h2>
            <p style="color:#64748b;margin-bottom:16px;">Deepen your understanding with our engineering guides and application notes:</p>
            <div style="display:flex;flex-wrap:wrap;gap:8px;">
                %s
                <a href="/knowledge-center/" style="display:inline-flex;align-items:center;padding:10px 18px;background:#fef3c7;border:1px solid #fde68a;border-radius:8px;text-decoration:none;color:#92400e;font-size:0.9rem;font-weight:500;margin:4px;">Browse All Knowledge Center Articles</a>
                <a href="/application-notes/" style="display:inline-flex;align-items:center;padding:10px 18px;background:#fef3c7;border:1px solid #fde68a;border-radius:8px;text-decoration:none;color:#92400e;font-size:0.9rem;font-weight:500;margin:4px;">Browse All Application Notes</a>
            </div>
        </div>
    </section>
''' % links
            for marker in ['<!-- FAQ -->', '<!-- AI Optical Engineer CTA -->', '<!-- Footer -->']:
                if marker in content:
                    content = content.replace(marker, section + '\n    ' + marker, 1)
                    break
            changed = True
        
        # 3. Bottom RFQ
        if not had_rfq:
            for marker in ['<!-- AI Optical Engineer CTA -->', '<!-- Footer -->']:
                if marker in content:
                    content = content.replace(marker, BOTTOM_RFQ_V3 + '\n    ' + marker, 1)
                    break
            changed = True
    
    elif is_dynamic(content):
        stats['dynamic'] += 1
        
        # 1. FAQ schema
        if not had_faq:
            content = content.replace('</head>', GENERIC_FAQ + '</head>', 1)
            changed = True
        
        # 2. Mid-page CTA
        if not had_mid:
            mid = '''
    <!-- Mid-Page CTA -->
    <section style="background:linear-gradient(135deg,#1e3a5f,#2563eb);padding:40px 20px;text-align:center;margin:30px 0;">
        <div class="container" style="max-width:800px;margin:0 auto;">
            <h2 style="color:white;font-size:1.4rem;margin-bottom:12px;">Have a Custom Optical Requirement?</h2>
            <p style="color:#bfdbfe;margin-bottom:20px;font-size:0.95rem;">Upload your drawing or describe your specification. Our engineering team will review and respond within 24 hours.</p>
            <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
                <a href="/contact.html" style="background:white;color:#1e3a5f;padding:12px 28px;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.95rem;">Upload Drawing / RFQ</a>
                <a href="/ai-optical-engineer.html" style="background:transparent;color:white;padding:12px 28px;border-radius:8px;text-decoration:none;font-weight:600;font-size:0.95rem;border:1px solid rgba(255,255,255,0.4);">Ask AI Optical Engineer</a>
            </div>
        </div>
    </section>
'''
            for marker in ['<section class="related-articles"', '<footer']:
                idx = content.find(marker)
                if idx > 0:
                    content = content[:idx] + mid + '\n' + content[idx:]
                    break
            changed = True
        
        # 3. Internal links
        if not had_kc:
            links = build_kc_links(category)
            section = '''
    <section style="padding:30px 20px;background:#fafbfc;border-top:1px solid #e2e8f0;">
        <div class="container" style="max-width:1200px;margin:0 auto;">
            <h3 style="font-size:1.1rem;font-weight:600;color:#1e293b;margin-bottom:16px;">Further Reading: Engineering Guides</h3>
            <p style="color:#64748b;font-size:0.9rem;margin-bottom:16px;">Deepen your understanding with our engineering guides and application notes:</p>
            <div style="display:flex;flex-wrap:wrap;gap:8px;">
                %s
                <a href="/knowledge-center/" style="display:inline-flex;align-items:center;padding:10px 18px;background:#fef3c7;border:1px solid #fde68a;border-radius:8px;text-decoration:none;color:#92400e;font-size:0.9rem;font-weight:500;margin:4px;">Browse All Knowledge Center</a>
                <a href="/application-notes/" style="display:inline-flex;align-items:center;padding:10px 18px;background:#fef3c7;border:1px solid #fde68a;border-radius:8px;text-decoration:none;color:#92400e;font-size:0.9rem;font-weight:500;margin:4px;">Browse All Application Notes</a>
            </div>
        </div>
    </section>
''' % links
            footer_idx = content.find('<footer')
            if footer_idx > 0:
                content = content[:footer_idx] + section + '\n' + content[footer_idx:]
            changed = True
        
        # 4. Bottom CTA
        if 'Upload Drawing' not in content.split('<footer')[0] if '<footer' in content else 'Upload Drawing' not in content:
            bottom = '''
    <div style="background:linear-gradient(135deg,#1e3a5f,#2563eb);padding:40px 20px;text-align:center;margin:30px 0;">
        <div class="container" style="max-width:800px;margin:0 auto;">
            <h2 style="color:white;font-size:1.4rem;margin-bottom:12px;">Ready to Start Your Project?</h2>
            <p style="color:#bfdbfe;margin-bottom:20px;">Upload your drawing or describe your requirements. Our engineering team responds within 24 hours.</p>
            <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
                <a href="/contact.html" style="background:white;color:#1e3a5f;padding:12px 28px;border-radius:8px;text-decoration:none;font-weight:600;">Upload Drawing / RFQ</a>
                <a href="/ai-optical-engineer.html" style="background:transparent;color:white;padding:12px 28px;border-radius:8px;text-decoration:none;font-weight:600;border:1px solid rgba(255,255,255,0.4);">Ask AI Optical Engineer</a>
            </div>
            <p style="color:#93c5fd;font-size:0.8rem;margin-top:12px;">We accept PDF, DXF, STEP, IGES drawings. Include material, dimensions, surface quality, coating, and quantity.</p>
        </div>
    </div>
'''
            footer_idx = content.find('<footer')
            if footer_idx > 0:
                content = content[:footer_idx] + bottom + '\n' + content[footer_idx:]
            changed = True
    
    else:  # simple static
        stats['simple'] += 1
        
        # 1. Mid-page CTA
        if not had_mid:
            inserted = False
            for marker in ['<h2>Frequently Asked Questions</h2>', '<h2>Related Products</h2>', 'ai-box']:
                idx = content.find(marker)
                if idx > 0:
                    search_back = content.rfind('<section', 0, idx)
                    search_back2 = content.rfind('<div class="container"', 0, idx)
                    insert_pos = max(search_back, search_back2)
                    if insert_pos > 0:
                        content = content[:insert_pos] + MID_CTA_SIMPLE + '\n' + content[insert_pos:]
                        inserted = True
                        break
            if not inserted:
                footer_idx = content.find('<footer')
                if footer_idx > 0:
                    content = content[:footer_idx] + MID_CTA_SIMPLE + '\n' + content[footer_idx:]
            changed = True
        
        # 2. Internal links
        if not had_kc:
            links = build_kc_links(category)
            section = '''
    <section class="product-section">
        <div class="container">
            <h2>Further Reading: Engineering Guides & Application Notes</h2>
            <div style="display:flex;flex-wrap:wrap;gap:8px;">
                %s
                <a href="/knowledge-center/" style="display:block;padding:10px 16px;background:#fef3c7;border-radius:8px;margin-bottom:8px;text-decoration:none;color:#92400e;font-size:14px;">Browse All Knowledge Center Articles</a>
                <a href="/application-notes/" style="display:block;padding:10px 16px;background:#fef3c7;border-radius:8px;margin-bottom:8px;text-decoration:none;color:#92400e;font-size:14px;">Browse All Application Notes</a>
            </div>
        </div>
    </section>
''' % links
            footer_idx = content.find('<footer')
            if footer_idx > 0:
                content = content[:footer_idx] + section + '\n' + content[footer_idx:]
            changed = True
        
        # 3. FAQ schema
        if not had_faq:
            faq_match = re.search(r'<h2>Frequently Asked Questions</h2>(.*?)</section>', content, re.DOTALL)
            if faq_match:
                faq_html = faq_match.group(1)
                questions = re.findall(r'font-weight:600[^>]*>(.*?)</div>', faq_html)
                answers = re.findall(r'line-height:1\.7[^>]*>(.*?)</div>', faq_html)
                if questions:
                    items = []
                    for i, q in enumerate(questions):
                        qc = re.sub(r'<[^>]+>', '', q).strip().replace('"', '\\"')
                        ac = re.sub(r'<[^>]+>', '', answers[i]).strip().replace('"', '\\"') if i < len(answers) else 'Contact our engineering team for details.'
                        items.append('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (qc, ac))
                    schema = '    <!-- FAQ Schema -->\n    <script type="application/ld+json">\n    {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}\n    </script>\n' % ','.join(items)
                    content = content.replace('</head>', schema + '</head>', 1)
                    changed = True
    
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        stats['modified'] += 1
        modified_files.append(slug)
        
        if not had_mid and ('Mid-Page CTA' in content or 'mid-cta' in content.lower()):
            stats['mid_cta'] += 1
        if not had_faq and 'FAQPage' in content:
            stats['faq_schema'] += 1
        if not had_kc and len(re.findall(r'/knowledge-center/', content)) > 1:
            stats['kc_links'] += 1
        if not had_rfq and ('rfq-section' in content or 'Ready to Start' in content or 'Upload Drawing' in content.split('<footer')[0] if '<footer' in content else 'Upload Drawing' in content):
            stats['bottom_rfq'] += 1

print('=' * 60)
print('Phase 2b Business Conversion Optimization - COMPLETE')
print('=' * 60)
print('Total pages processed: %d' % stats['total'])
print('Pages modified: %d' % stats['modified'])
print('  - V3.0 static: %d' % stats['v3'])
print('  - Simple static: %d' % stats['simple'])
print('  - Dynamic (JS): %d' % stats['dynamic'])
print('')
print('Changes applied:')
print('  - Mid-page CTA added: %d' % stats['mid_cta'])
print('  - FAQ Schema added: %d' % stats['faq_schema'])
print('  - Internal links added: %d' % stats['kc_links'])
print('  - Bottom RFQ added: %d' % stats['bottom_rfq'])
print('')
print('Modified files (%d):' % len(modified_files))
for f in modified_files:
    print('  - %s' % f)
