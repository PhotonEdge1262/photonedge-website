#!/usr/bin/env python3
"""V33 Fix Script: Pre-rendered pages + blog links + robots.txt"""

import os
import re
import glob

WORK_DIR = "/app/data/所有对话/主对话/v32-work"

def fix_base_href_in_prerendered():
    print("=== P0-1: Removing base href from pre-rendered pages ===")
    fixed = 0
    
    for pattern in ["blog/*/index.html", "products/*/index.html"]:
        for filepath in glob.glob(os.path.join(WORK_DIR, pattern)):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '<base href="/"' in content:
                new_content = re.sub(r'\s*<base href="/">\s*\n?', '\n', content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                fixed += 1
    
    print(f"  Fixed {fixed} pre-rendered pages")
    return fixed

def fix_blog_links():
    print("=== P0-2: Fixing blog links to use static pre-rendered pages ===")
    
    # 1. Fix blog-data.js - add url field for each post
    blog_data_path = os.path.join(WORK_DIR, "js", "blog-data.js")
    with open(blog_data_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def add_url_field(match):
        slug = match.group(1)
        return '"slug": "' + slug + '",\n    "url": "/blog/' + slug + '/"'
    
    new_content = re.sub(r'"slug":\s*"([^"]+)"', add_url_field, content)
    
    with open(blog_data_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("  blog-data.js: Added url field for each post")
    
    # 2. Fix blog.html - change blog-post.html?slug= to /blog/slug/
    blog_html_path = os.path.join(WORK_DIR, "blog.html")
    with open(blog_html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_pattern = "blog-post.html?slug=' + post.slug + '"
    new_pattern = "/blog/' + post.slug + '/'"
    
    count = content.count(old_pattern)
    content = content.replace(old_pattern, new_pattern)
    
    with open(blog_html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  blog.html: Replaced {count} links")
    
    # 3. Fix blog-post.html - change related article links
    blog_post_path = os.path.join(WORK_DIR, "blog-post.html")
    with open(blog_post_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = content.count(old_pattern)
    content = content.replace(old_pattern, new_pattern)
    
    with open(blog_post_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  blog-post.html: Replaced {count} links")
    
    # 4. Fix pre-rendered blog pages - change related article links
    blog_fixed = 0
    for filepath in glob.glob(os.path.join(WORK_DIR, "blog/*/index.html")):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "blog-post.html?slug=" in content:
            content = content.replace(old_pattern, new_pattern)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            blog_fixed += 1
    
    print(f"  Pre-rendered blog pages: Fixed {blog_fixed} pages")
    return True

def fix_robots_txt():
    print("=== P0-3: Updating robots.txt Crawl-delay ===")
    
    robots_path = os.path.join(WORK_DIR, "robots.txt")
    with open(robots_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("Crawl-delay: 10", "Crawl-delay: 2")
    
    with open(robots_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  robots.txt: Crawl-delay 10 -> 2")
    return True

def fix_blog_og_image():
    print("=== P0-4: Fixing blog og:image ===")
    
    blog_data_path = os.path.join(WORK_DIR, "js", "blog-data.js")
    with open(blog_data_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    slug_image_map = {}
    posts = re.findall(r'"slug":\s*"([^"]+)"[\s\S]*?"image":\s*"([^"]+)"', content)
    for slug, image in posts:
        slug_image_map[slug] = image
    
    fixed = 0
    for filepath in glob.glob(os.path.join(WORK_DIR, "blog/*/index.html")):
        slug = os.path.basename(os.path.dirname(filepath))
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if slug in slug_image_map:
            new_image = "https://photonedgeoptics.com/" + slug_image_map[slug]
            old_pattern = r'property="og:image"\s+content="https://photonedgeoptics\.com/logo\.png"'
            if re.search(old_pattern, content):
                content = re.sub(
                    old_pattern,
                    'property="og:image" content="' + new_image + '"',
                    content
                )
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixed += 1
    
    print(f"  Fixed og:image in {fixed} blog pages")
    return fixed

def fix_blog_post_html_share():
    print("=== P0-5: Fixing blog-post.html share URLs ===")
    
    blog_post_path = os.path.join(WORK_DIR, "blog-post.html")
    with open(blog_post_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(
        'url=https://photonedgeoptics.com/blog-post.html',
        'url=https://photonedgeoptics.com/blog/'
    )
    
    with open(blog_post_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  blog-post.html: Fixed share URLs")
    return True

def main():
    print("Starting V33 fixes...\n")
    fix_base_href_in_prerendered()
    fix_blog_links()
    fix_robots_txt()
    fix_blog_og_image()
    fix_blog_post_html_share()
    print("\n=== V33 fixes complete! ===")

if __name__ == "__main__":
    main()
