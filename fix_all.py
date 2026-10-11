import os
import json
import re

BASE = "/tmp/v169-work"
PRODUCTS_DIR = os.path.join(BASE, "products")

# === Material mapping by product category ===
def get_materials_for_product(slug):
    s = slug.lower()
    # Infrared
    if any(k in s for k in ['germanium', 'silicon-infrared', 'znse', 'zns', 'ir-', 'infrared']):
        return [
            ('Germanium', '/materials/germanium/', '🔴'),
            ('Silicon', '/materials/silicon/', '⚫'),
            ('ZnSe', '/materials/znse/', '🟠'),
            ('ZnS', '/materials/zns/', '🟤'),
        ]
    # Mirror types
    if 'mirror' in s:
        return [
            ('UV Fused Silica', '/materials/uv-fused-silica/', '🟣'),
            ('BK7', '/materials/bk7/', '🔵'),
            ('Silicon', '/materials/silicon/', '⚫'),
        ]
    # Filter types
    if any(k in s for k in ['filter', 'dichroic', 'neutral-density']):
        return [
            ('BK7', '/materials/bk7/', '🔵'),
            ('UV Fused Silica', '/materials/uv-fused-silica/', '🟣'),
            ('CaF₂', '/materials/caf2/', '🟡'),
        ]
    # Prism / beamsplitter
    if any(k in s for k in ['prism', 'beamsplitter']):
        return [
            ('BK7', '/materials/bk7/', '🔵'),
            ('UV Fused Silica', '/materials/uv-fused-silica/', '🟣'),
        ]
    # Window types
    if 'window' in s:
        return [
            ('BK7', '/materials/bk7/', '🔵'),
            ('UV Fused Silica', '/materials/uv-fused-silica/', '🟣'),
            ('ZnS', '/materials/zns/', '🟤'),
            ('ZnSe', '/materials/znse/', '🟠'),
        ]
    # Lens types (default)
    return [
        ('BK7', '/materials/bk7/', '🔵'),
        ('UV Fused Silica', '/materials/uv-fused-silica/', '🟣'),
        ('Sapphire', '/materials/sapphire/', '🔷'),
    ]

# === CTA HTML ===
CTA_HTML = '''
<section style="padding:60px 0;background:linear-gradient(135deg,#1e40af,#3b82f6);text-align:center;">
  <div style="max-width:800px;margin:0 auto;padding:0 24px;">
    <h2 style="font-size:28px;font-weight:700;color:white;margin-bottom:12px;">Have a Custom Requirement?</h2>
    <p style="font-size:16px;color:rgba(255,255,255,0.9);margin-bottom:24px;">Upload your drawing or specifications. Our engineering team will review and respond within 24 business hours.</p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
      <a href="/contact.html" style="display:inline-block;padding:14px 32px;background:white;color:#1e40af;font-weight:600;border-radius:8px;text-decoration:none;font-size:15px;">Upload Your Drawing</a>
      <a href="/contact.html" style="display:inline-block;padding:14px 32px;background:transparent;color:white;font-weight:600;border-radius:8px;text-decoration:none;font-size:15px;border:2px solid rgba(255,255,255,0.5);">Request a Quote</a>
    </div>
  </div>
</section>
'''

# === FAQ JSON-LD ===
FAQ_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "Can I order custom specifications for this product?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. We support custom specifications including material, dimensions, coatings, and surface quality. Upload your drawing or contact us with your requirements for engineering review."
            }
        },
        {
            "@type": "Question",
            "name": "What is the typical lead time?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Standard catalog items typically ship within 1-2 weeks. Custom specifications require 2-4 weeks depending on complexity and material availability. Complex custom optics may take 4-6 weeks. All lead times are estimated and subject to final confirmation."
            }
        },
        {
            "@type": "Question",
            "name": "What inspection documentation is provided?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "We provide inspection reports including interferometer surface maps, spectrophotometer curves, and dimensional data. Certificates of Compliance (CoC) are included with every shipment."
            }
        },
        {
            "@type": "Question",
            "name": "Is there a minimum order quantity?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Standard catalog items have no minimum order quantity. Custom products can start from 1 piece for prototyping, with typical production MOQ of 5-10 pieces depending on specifications."
            }
        },
        {
            "@type": "Question",
            "name": "How do I request a quote?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Click 'Request a Quote' or 'Upload Your Drawing' to submit your specifications. Our engineering team reviews all inquiries and responds within 24 business hours with a detailed quotation."
            }
        }
    ]
}

# === How to Specify HTML ===
HOW_TO_SPECIFY_HTML = '''
<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;padding:32px;margin:40px 0;">
  <h3 style="font-size:20px;font-weight:700;color:#1e293b;margin-bottom:16px;">How to Specify</h3>
  <p style="color:#475569;font-size:14px;line-height:1.7;margin-bottom:12px;">When requesting a quote for this product, please specify the following parameters to help our engineering team provide an accurate quotation:</p>
  <ul style="color:#475569;font-size:14px;line-height:2;padding-left:20px;">
    <li>Material type and grade</li>
    <li>Dimensions (diameter, thickness, or custom geometry)</li>
    <li>Surface quality (scratch-dig or equivalent)</li>
    <li>Surface flatness (if applicable)</li>
    <li>Coating requirements (type, wavelength range, performance specs)</li>
    <li>Quantity and delivery timeline</li>
  </ul>
  <p style="color:#475569;font-size:14px;margin-top:12px;">Not sure about specifications? <a href="/contact.html" style="color:#2563eb;font-weight:600;">Upload your drawing</a> and our team will assist with engineering review.</p>
</div>
'''

def build_materials_html(slug):
    materials = get_materials_for_product(slug)
    links = []
    for name, path, emoji in materials:
        links.append('<a href="%s" style="display:inline-flex;align-items:center;padding:10px 18px;background:#e0e7ff;border-radius:8px;text-decoration:none;color:#3730a3;font-weight:500;font-size:0.9rem;transition:all 0.2s;"><span style="margin-right:8px;">%s</span>%s</a>' % (path, emoji, name))
    links_html = '\n'.join(links)
    return '''
<div class="related-materials-section" style="margin:40px 0;padding:24px;background:#f8fafc;border-radius:12px;">
  <h3 style="font-size:1.25rem;font-weight:600;color:#1e3a5f;margin-bottom:16px;text-align:center;">Related Optical Materials</h3>
  <p style="text-align:center;color:#64748b;font-size:0.9rem;margin-bottom:20px;">Learn more about the optical materials available for this product</p>
  <div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center;">
    %s
  </div>
  <div style="text-align:center;margin-top:20px;">
    <a href="/materials.html" style="color:#3b82f6;text-decoration:none;font-weight:500;font-size:0.9rem;">View All Materials →</a>
  </div>
</div>
''' % links_html

def fix_page(filepath, slug):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # === Fix 1: Upload Your Drawing CTA ===
    if 'Upload Your Drawing' not in content:
        # Insert before <!-- Footer --> or <footer
        footer_match = re.search(r'(\s*<!-- Footer -->|\s*<footer)', content)
        if footer_match:
            insert_pos = footer_match.start()
            content = content[:insert_pos] + '\n' + CTA_HTML + '\n' + content[insert_pos:]
            changes.append('CTA')
        else:
            # Try before </body>
            body_end = content.rfind('</body>')
            if body_end > 0:
                content = content[:body_end] + '\n' + CTA_HTML + '\n' + content[body_end:]
                changes.append('CTA-before-body')
    
    # === Fix 2: FAQ Schema ===
    if '"@type": "FAQPage"' not in content:
        faq_json = json.dumps(FAQ_SCHEMA, ensure_ascii=False)
        faq_script = '\n<script type="application/ld+json">\n%s\n</script>\n' % faq_json
        head_end = content.find('</head>')
        if head_end > 0:
            content = content[:head_end] + faq_script + content[head_end:]
            changes.append('FAQ-Schema')
    
    # === Fix 3: How to Specify ===
    if 'How to Specify' not in content:
        # Insert before <!-- FAQ --> section
        faq_comment = re.search(r'\s*<!-- FAQ -->', content)
        if faq_comment:
            insert_pos = faq_comment.start()
            content = content[:insert_pos] + '\n' + HOW_TO_SPECIFY_HTML + '\n' + content[insert_pos:]
            changes.append('HowToSpecify')
        else:
            # Try before FAQ section heading or before footer/CTA
            footer_match = re.search(r'(\s*<!-- Footer -->|\s*<footer)', content)
            if footer_match:
                insert_pos = footer_match.start()
                content = content[:insert_pos] + '\n' + HOW_TO_SPECIFY_HTML + '\n' + content[insert_pos:]
                changes.append('HowToSpecify-before-footer')
    
    # === Fix 4: Materials links ===
    if '/materials/' not in content:
        mat_html = build_materials_html(slug)
        # Insert before <!-- Footer --> or <footer
        footer_match = re.search(r'(\s*<!-- Footer -->|\s*<footer)', content)
        if footer_match:
            insert_pos = footer_match.start()
            content = content[:insert_pos] + '\n' + mat_html + '\n' + content[insert_pos:]
            changes.append('Materials')
        else:
            body_end = content.rfind('</body>')
            if body_end > 0:
                content = content[:body_end] + '\n' + mat_html + '\n' + content[body_end:]
                changes.append('Materials-before-body')
    
    if changes:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return changes

# === Main ===
stats = {'CTA': 0, 'FAQ-Schema': 0, 'HowToSpecify': 0, 'Materials': 0}
total_fixed = 0

for slug in sorted(os.listdir(PRODUCTS_DIR)):
    filepath = os.path.join(PRODUCTS_DIR, slug, 'index.html')
    if not os.path.isfile(filepath):
        continue
    changes = fix_page(filepath, slug)
    if changes:
        total_fixed += 1
        for c in changes:
            key = c.split('-')[0] if '-' in c else c
            if key in stats:
                stats[key] += 1
            else:
                stats[key] = stats.get(key, 0) + 1
        print("Fixed %s: %s" % (slug, ', '.join(changes)))

print("\n=== Summary ===")
print("Total pages modified: %d" % total_fixed)
for k, v in stats.items():
    print("  %s: %d pages" % (k, v))
