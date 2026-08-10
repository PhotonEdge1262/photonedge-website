#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V87 Daily Blog Update - Blog #36: Optical Beamsplitter Selection Complete Guide
"""

import os
import json
import shutil
import re

BASE = "/app/data/所有对话/主对话/PhotonEdge-V87"

# ========== BLOG #36 DATA ==========
blog36 = {
    "id": 36,
    "title": "Optical Beamsplitters Complete Selection Guide: Plate, Cube, Polarizing & Non-Polarizing",
    "slug": "optical-beamsplitter-selection-complete-guide",
    "url": "/blog/optical-beamsplitter-selection-complete-guide/",
    "excerpt": "Complete guide to optical beamsplitters: how to choose between plate beamsplitters, cube beamsplitters, polarizing and non-polarizing cubes. Learn about split ratios, extinction ratio, damage threshold, and application-specific selection for lasers, interferometry, machine vision, and fiber optics.",
    "category": "Technical Guide",
    "date": "2026-08-10",
    "readTime": "12 min",
    "image": "images/blog/beamsplitter-selection-guide.jpg",
    "author": "PhotonEdge Technical Team",
    "titleZh": "光学分束器完全选型指南：平板、立方、偏振与非偏振分束器",
    "excerptZh": "光学分束器完全选型指南：如何在平板分束器、立方分束器、偏振立方与非偏振立方之间选择。了解分束比、消光比、损伤阈值以及针对激光、干涉测量、机器视觉和光纤通信的应用选型建议。",
    "categoryZh": "技术指南",
}

# Read the content generated in the previous script
content_en_file = ""  # Will be filled below
content_zh_file = ""  # Will be filled below

# ========== STEP 1: UPDATE blog-data.js ==========
def update_blog_data():
    """Insert blog #36 at the beginning of BLOG_POSTS array."""
    blog_data_path = os.path.join(BASE, "js", "blog-data.js")
    with open(blog_data_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Read content parts
    from blog36_generate import content_en, content_zh
    
    blog36_entry = blog36.copy()
    blog36_entry["content"] = content_en
    blog36_entry["contentZh"] = content_zh
    
    # Convert to JSON string
    blog_json = json.dumps(blog36_entry, ensure_ascii=False, indent=4)
    
    # Find the opening of the array and insert
    # Find 'var BLOG_POSTS = [' and insert after it
    pattern = r'(var BLOG_POSTS = \[)\s*\{'
    match = re.search(pattern, content)
    if match:
        insert_pos = match.start(1) + len(match.group(1))
        new_content = content[:insert_pos] + "\n  " + blog_json.rstrip() + ",\n\n  " + content[insert_pos:]
        
        with open(blog_data_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print("✅ blog-data.js updated with blog #36")
        return True
    else:
        print("❌ Could not find BLOG_POSTS array in blog-data.js")
        return False

# ========== STEP 2: CREATE BLOG HTML PAGE ==========
def create_blog_html():
    """Create the blog detail HTML page based on the latest blog template."""
    blog_dir = os.path.join(BASE, "blog", blog36["slug"])
    os.makedirs(blog_dir, exist_ok=True)
    
    # Read template from latest blog
    template_path = os.path.join(BASE, "blog", "laser-resonator-optics-output-couplers-guide", "index.html")
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    from blog36_generate import content_en, content_zh
    
    # Replace title
    html = html.replace(
        "<title>Output Couplers & Laser Resonator Optics Selection Guide | PhotonEdge Optics Blog</title>",
        f"<title>{blog36['title']} | PhotonEdge Optics Blog</title>"
    )
    
    # Replace meta description
    html = html.replace(
        'content="Complete guide to laser resonator optics: output couplers, high reflector mirrors, intracavity lenses, prism assemblies, and laser safety. Learn how to select the right components for solid-state laser systems."',
        f'content="{blog36["excerpt"]}"'
    )
    
    # Replace meta keywords
    keywords_en = "Beamsplitter, Optical Beamsplitter, Cube Beamsplitter, Plate Beamsplitter, Polarizing Beamsplitter, Non-Polarizing Beamsplitter, Beam Splitter Selection, 50/50 Beamsplitter, High Power Beamsplitter"
    keywords_zh = "分束器, 光学分束器, 立方分束器, 平板分束器, 偏振分束器, 非偏振分束器, 分束器选型, 50/50分束器, 高功率分束器"
    html = html.replace(
        '<meta name="keywords" content="Output Coupler, Laser Resonator, Laser Mirror, Nd:YAG Output Coupler, Resonator Optics, Laser Cavity, Laser Safety Goggles, High Reflector Mirror, 输出耦合镜, 激光谐振腔, 高反射镜, 激光防护眼镜">',
        f'<meta name="keywords" content="{keywords_en}, {keywords_zh}">'
    )
    
    # Replace og:title
    html = html.replace(
        '<meta property="og:title" content="Output Couplers & Laser Resonator Optics Selection Guide | PhotonEdge Optics Blog">',
        f'<meta property="og:title" content="{blog36["title"]} | PhotonEdge Optics Blog">'
    )
    
    # Replace og:description
    html = html.replace(
        '<meta property="og:description" content="Complete guide to laser resonator optics: output couplers, high reflector mirrors, intracavity lenses, prism assemblies, and laser safety. Learn how to select the right components for solid-state laser systems.">',
        f'<meta property="og:description" content="{blog36["excerpt"]}">'
    )
    
    # Replace og:url and canonical and hreflang
    old_slug = "laser-resonator-optics-output-couplers-guide"
    new_slug = blog36["slug"]
    html = html.replace(old_slug, new_slug)
    
    # Replace og:image
    html = html.replace(
        "images/blog/laser-resonator-optics-guide.jpg",
        blog36["image"]
    )
    
    # Replace JSON-LD Article
    # headline
    html = html.replace(
        '"headline": "Output Couplers & Laser Resonator Optics Selection Guide"',
        f'"headline": "{blog36["title"]}"'
    )
    # description
    html = html.replace(
        '"description": "Complete guide to laser resonator optics: output couplers, high reflector mirrors, intracavity lenses, prism assemblies, and laser safety. Learn how to select the right components for solid-state laser systems.",',
        f'"description": "{blog36["excerpt"]}",'
    )
    # image
    html = html.replace(
        'laser-resonator-optics-guide.jpg',
        'beamsplitter-selection-guide.jpg'
    )
    # datePublished and dateModified
    html = html.replace(
        '"datePublished": "2026-08-09",\n  "dateModified": "2026-08-09"',
        f'"datePublished": "{blog36["date"]}",\n  "dateModified": "{blog36["date"]}"'
    )
    
    # Breadcrumb
    html = html.replace(
        '"name": "Output Couplers & Laser Resonator Optics Selection Guide",',
        f'"name": "{blog36["title"]}",'
    )
    
    # Twitter card
    html = html.replace(
        '<meta name="twitter:title" content="Output Couplers & Laser Resonator Optics Selection Guide | PhotonEdge Blog">',
        f'<meta name="twitter:title" content="{blog36["title"]} | PhotonEdge Blog">'
    )
    html = html.replace(
        '<meta name="twitter:description" content="Complete guide to laser resonator optics: output couplers, high reflector mirrors, intracavity lenses, prism assemblies, and laser safety. Learn how to select the right components for solid-state laser systems.">',
        f'<meta name="twitter:description" content="{blog36["excerpt"]}">'
    )
    
    # Article header data attributes
    html = html.replace(
        'data-en-category="Technical Guide" data-zh-category="技术指南">Technical Guide',
        f'data-en-category="{blog36["category"]}" data-zh-category="{blog36["categoryZh"]}">{blog36["category"]}'
    )
    html = html.replace(
        'id="articleTitle" data-en-title="Output Couplers & Laser Resonator Optics Selection Guide" data-zh-title="输出耦合镜与激光谐振腔光学元件选型指南">Output Couplers & Laser Resonator Optics Selection Guide',
        f'id="articleTitle" data-en-title="{blog36["title"]}" data-zh-title="{blog36["titleZh"]}">{blog36["title"]}'
    )
    html = html.replace(
        '<span id="articleDate">2026-08-09</span>',
        f'<span id="articleDate">{blog36["date"]}</span>'
    )
    html = html.replace(
        'data-en-time="12 min" data-zh-time="12 分钟">12 min',
        f'data-en-time="{blog36["readTime"]}" data-zh-time="12 分钟">{blog36["readTime"]}'
    )
    
    # Replace Chinese content
    # Find the div with id="articleContentZh" and replace its content
    zh_start = html.find('<div id="articleContentZh"')
    zh_end = html.find('</div>\n<div id="articleContentEn">')
    if zh_start != -1 and zh_end != -1:
        # Find the actual content start (after the opening div tag)
        zh_content_start = html.find('>', zh_start) + 1
        html = html[:zh_content_start] + "\n" + content_zh + "\n    " + html[zh_end:]
    
    # Replace English content
    en_start = html.find('<div id="articleContentEn">')
    # Find the closing of article-body div
    en_end_marker = '    </div>\n    \n    <div class="article-cta">'
    en_end = html.find(en_end_marker, en_start)
    if en_start != -1 and en_end != -1:
        en_content_start = html.find('>', en_start) + 1
        html = html[:en_content_start] + "\n" + content_en + "\n" + html[en_end:]
    
    # Save
    output_path = os.path.join(blog_dir, "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"✅ Blog HTML page created: {output_path}")
    return True

# ========== STEP 3: UPDATE SITEMAP.XML ==========
def update_sitemap():
    """Add new blog URL to sitemap.xml."""
    sitemap_path = os.path.join(BASE, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_url = f"""  <url>
    <loc>https://photonedgeoptics.com{blog36['url']}</loc>
    <lastmod>{blog36['date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>"""
    
    # Insert before the closing </urlset>
    insert_pos = content.find("</urlset>")
    if insert_pos != -1:
        content = content[:insert_pos] + new_url + "\n" + content[insert_pos:]
        
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print("✅ sitemap.xml updated with new blog URL")
        return True
    else:
        print("❌ Could not find </urlset> in sitemap.xml")
        return False

# ========== STEP 4: VERIFY JS FILES ==========
def verify_js():
    """Verify all JS files with node --check."""
    import subprocess
    
    js_files = [
        os.path.join(BASE, "js", "blog-data.js"),
        os.path.join(BASE, "js", "products-data.js"),
        os.path.join(BASE, "js", "translations.js"),
        os.path.join(BASE, "js", "main.js"),
    ]
    
    all_ok = True
    for js_file in js_files:
        result = subprocess.run(["node", "--check", js_file], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {os.path.basename(js_file)}: OK")
        else:
            print(f"❌ {os.path.basename(js_file)}: {result.stderr}")
            all_ok = False
    
    return all_ok

# ========== MAIN ==========
if __name__ == "__main__":
    print("=" * 60)
    print("PhotonEdge V87 - Daily Blog Update #36")
    print("=" * 60)
    print()
    
    # Step 1
    print("Step 1: Updating blog-data.js...")
    if not update_blog_data():
        print("FAILED at Step 1")
        exit(1)
    print()
    
    # Step 2
    print("Step 2: Creating blog HTML page...")
    if not create_blog_html():
        print("FAILED at Step 2")
        exit(1)
    print()
    
    # Step 3
    print("Step 3: Updating sitemap.xml...")
    if not update_sitemap():
        print("FAILED at Step 3")
        exit(1)
    print()
    
    # Step 4
    print("Step 4: Verifying JS files...")
    if not verify_js():
        print("FAILED at Step 4 - JS syntax error!")
        exit(1)
    print()
    
    print("=" * 60)
    print("All steps completed successfully!")
    print("=" * 60)
