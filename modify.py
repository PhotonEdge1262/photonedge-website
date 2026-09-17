#!/usr/bin/env python3
"""
V131 batch modifications:
1. 5 English application pages: lang toggle + positioning statement
2. 9 Chinese pages: fix English links in nav and footer
"""
import re
import os

# ============================================================
# TASK 1: English application pages
# ============================================================
APP_FILES = [
    "/tmp/v131-work/applications/aerospace-defense/index.html",
    "/tmp/v131-work/applications/laser-optics/index.html",
    "/tmp/v131-work/applications/medical-imaging/index.html",
    "/tmp/v131-work/applications/research-laboratory/index.html",
    "/tmp/v131-work/applications/semiconductor-inspection/index.html",
]

POSITIONING_HTML = '''<div style="margin-top:20px;padding:16px 20px;background:#f0f9ff;border-left:3px solid #3b82f6;border-radius:0 8px 8px 0;">
    <p style="color:#475569;font-size:0.95rem;line-height:1.7;margin:0;">PhotonEdge is an experienced, engineering-led optical company with flexible manufacturing and supply-chain capabilities. We coordinate production and quality across our network to deliver components that meet your exact specifications.</p>
</div>'''

NEW_LANG_LINK = '<a href="/zh/" class="lang-toggle" style="text-decoration:none;color:inherit;cursor:pointer;">\n                    <span>\u4e2d\u6587</span>\n                </a>'

stats = {}

for fpath in APP_FILES:
    fname = os.path.basename(os.path.dirname(fpath))
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    changes = {"lang_toggle": 0, "positioning": 0}
    
    # --- Task 1A: Replace lang-switcher block ---
    lang_pattern = r'<div class="lang-switcher">\s*<button class="lang-btn notranslate active">EN</button>\s*<a href="/zh/" class="lang-btn notranslate" style="text-decoration:none;">\u4e2d\u6587</a>\s*</div>'
    
    if re.search(lang_pattern, content):
        content = re.sub(lang_pattern, NEW_LANG_LINK, content)
        changes["lang_toggle"] = 1
        print(f"  [{fname}] Lang toggle: replaced lang-switcher div with new link")
    else:
        print(f"  [{fname}] Lang toggle: WARNING - pattern not found!")
    
    # --- Task 1B: Add positioning statement ---
    specs_heading = 'Key Specifications for This Industry'
    specs_pos = content.find(specs_heading)
    
    if specs_pos > 0:
        section_end = content.find('</section>', specs_pos)
        if section_end > 0:
            insert_str = '\n        ' + POSITIONING_HTML + '\n    '
            content = content[:section_end] + insert_str + content[section_end:]
            changes["positioning"] = 1
            print(f"  [{fname}] Positioning: added before Key Specifications </section>")
    else:
        last_section = content.rfind('</section>')
        if last_section > 0:
            insert_str = '\n        ' + POSITIONING_HTML + '\n    '
            content = content[:last_section] + insert_str + content[last_section:]
            changes["positioning"] = 1
            print(f"  [{fname}] Positioning: added before last </section> (fallback)")
    
    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
    
    stats[fname] = changes

print("\n=== Task 1 Summary ===")
for fname, changes in stats.items():
    print(f"  {fname}: lang_toggle={changes['lang_toggle']}, positioning={changes['positioning']}")


# ============================================================
# TASK 2: Chinese pages - fix English links
# ============================================================
ZH_DIR = "/tmp/v131-work/zh/"
ZH_FILES = [
    "about.html", "applications.html", "case-studies.html",
    "contact.html", "custom-optics.html", "faq.html",
    "index.html", "products.html", "quality.html"
]

LINK_MAP = {
    '/knowledge-center/': '/zh/faq.html',
    '/application-notes/': '/zh/faq.html',
    '/coatings/': '/zh/custom-optics.html',
    '/materials.html': '/zh/products.html',
}

zh_stats = {}

for fname in ZH_FILES:
    fpath = os.path.join(ZH_DIR, fname)
    if not os.path.exists(fpath):
        print(f"  [{fname}] WARNING: file not found!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    change_count = 0
    
    for old_href, new_href in LINK_MAP.items():
        old_pattern = 'href="' + old_href + '"'
        new_pattern = 'href="' + new_href + '"'
        
        count = content.count(old_pattern)
        if count > 0:
            content = content.replace(old_pattern, new_pattern)
            change_count += count
            print(f"  [{fname}] {old_href} -> {new_href} ({count} occurrences)")
    
    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
    
    zh_stats[fname] = change_count

print("\n=== Task 2 Summary ===")
total_zh = 0
for fname, count in zh_stats.items():
    print(f"  {fname}: {count} links fixed")
    total_zh += count
print(f"  TOTAL: {total_zh} links fixed across {len(ZH_FILES)} files")
