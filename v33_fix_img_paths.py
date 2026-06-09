#!/usr/bin/env python3
"""V33 Fix: Fix JS template image paths in pre-rendered pages"""

import os
import re
import glob

WORK_DIR = "/app/data/所有对话/主对话/v32-work"

def fix_product_page_img_paths():
    """Fix JS template strings using relative image paths in product pre-rendered pages"""
    print("=== Fixing JS image paths in product pages ===")
    fixed = 0
    
    for filepath in glob.glob(os.path.join(WORK_DIR, "products/*/index.html")):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Fix: currentProduct.image -> prepend / if used in src attribute
        # The JS builds HTML strings like: '<img src="' + currentProduct.image + '"'
        # We need to change to: '<img src="/' + currentProduct.image + '"'
        # But currentProduct.image already starts with "images/", so we need "/" prefix
        
        # Pattern 1: src="' + currentProduct.image + '" -> src="/' + currentProduct.image + '" 
        content = content.replace(
            "src=\"' + currentProduct.image + '\"",
            "src=\"/' + currentProduct.image + '\""
        )
        
        # Pattern 2: src="' + product.image + '" -> src="/' + product.image + '" 
        content = content.replace(
            "src=\"' + product.image + '\"",
            "src=\"/' + product.image + '\""
        )
        
        # Pattern 3: In og:image content, already has https://photonedgeoptics.com/ prefix - OK
        # Pattern 4: In Schema JSON, already has https://photonedgeoptics.com/ prefix - OK
        
        # Pattern 5: src="' + relatedProduct.image + '" for related products
        content = content.replace(
            "src=\"' + relatedProduct.image + '\"",
            "src=\"/' + relatedProduct.image + '\""
        )
        
        # Pattern 6: Any other product.image references in src
        content = content.replace(
            "src=\"' + p.image + '\"",
            "src=\"/' + p.image + '\""
        )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed += 1
    
    print(f"  Fixed image paths in {fixed} product pages")
    return fixed

def fix_blog_page_img_paths():
    """Fix JS template strings using relative image paths in blog pre-rendered pages"""
    print("=== Fixing JS image paths in blog pages ===")
    fixed = 0
    
    for filepath in glob.glob(os.path.join(WORK_DIR, "blog/*/index.html")):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Fix: src="' + post.image + '" -> src="/' + post.image + '" 
        content = content.replace(
            "src=\"' + post.image + '\"",
            "src=\"/' + post.image + '\""
        )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed += 1
    
    print(f"  Fixed image paths in {fixed} blog pages")
    return fixed

def main():
    fix_product_page_img_paths()
    fix_blog_page_img_paths()
    print("\n=== Image path fix complete! ===")

if __name__ == "__main__":
    main()
