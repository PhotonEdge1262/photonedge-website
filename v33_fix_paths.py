#!/usr/bin/env python3
"""V33 Fix: Convert relative paths to root-relative in pre-rendered pages"""

import os
import re
import glob

WORK_DIR = "/app/data/所有对话/主对话/v32-work"

# Paths that need /prefix in subdirectory pages
# Only fix resource paths, not JS template strings
PATH_REPLACEMENTS = [
    # CSS
    ('href="css/style.css"', 'href="/css/style.css"'),
    # JS files
    ('src="js/translations.js"', 'src="/js/translations.js"'),
    ('src="js/products-data.js"', 'src="/js/products-data.js"'),
    ('src="js/blog-data.js"', 'src="/js/blog-data.js"'),
    ('src="js/search.js"', 'src="/js/search.js"'),
    ('src="js/cart.js"', 'src="/js/cart.js"'),
    ('src="js/compare.js"', 'src="/js/compare.js"'),
    # Navigation links (html files)
    ('href="index.html"', 'href="/index.html"'),
    ('href="products.html"', 'href="/products.html"'),
    ('href="about.html"', 'href="/about.html"'),
    ('href="blog.html"', 'href="/blog.html"'),
    ('href="contact.html"', 'href="/contact.html"'),
    ('href="cart.html"', 'href="/cart.html"'),
    ('href="faq.html"', 'href="/faq.html"'),
    ('href="calculator.html"', 'href="/calculator.html"'),
    ('href="compare.html"', 'href="/compare.html"'),
    ('href="downloads.html"', 'href="/downloads.html"'),
    ('href="news.html"', 'href="/news.html"'),
    ('href="applications.html"', 'href="/applications.html"'),
    ('href="product-catalog.html"', 'href="/product-catalog.html"'),
    ('href="case-studies.html"', 'href="/case-studies.html"'),
    ('href="404.html"', 'href="/404.html"'),
    # Image paths that are relative
    ('src="images/', 'src="/images/'),
    ('href="images/', 'href="/images/'),
]

# Special cases for product pages with query params
PRODUCT_QUERY_REPLACEMENTS = [
    ('href="products.html?category=', 'href="/products.html?category='),
]

# Blog pages use Tailwind, need to also fix its specific patterns
BLOG_SPECIFIC = [
    ('href="blog.html?lang=zh"', 'href="/blog.html?lang=zh"'),
]

def fix_prerendered_paths():
    print("=== Fixing relative paths in pre-rendered pages ===")
    
    total_fixed = 0
    
    for pattern in ["products/*/index.html", "blog/*/index.html"]:
        for filepath in glob.glob(os.path.join(WORK_DIR, pattern)):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            # Apply standard replacements
            for old, new in PATH_REPLACEMENTS:
                content = content.replace(old, new)
            
            # Apply product query replacements
            for old, new in PRODUCT_QUERY_REPLACEMENTS:
                content = content.replace(old, new)
            
            # Apply blog specific replacements
            for old, new in BLOG_SPECIFIC:
                content = content.replace(old, new)
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                total_fixed += 1
    
    print(f"  Fixed paths in {total_fixed} pre-rendered pages")
    return total_fixed

def main():
    fix_prerendered_paths()
    print("\n=== Path fix complete! ===")

if __name__ == "__main__":
    main()
