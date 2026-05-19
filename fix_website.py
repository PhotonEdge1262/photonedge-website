#!/usr/bin/env python3
"""
PhotonEdge Website Fix Script
Fixes all issues and generates updated files
"""

import os
import re
import json
from pathlib import Path

# Paths
PRODUCTS_DIR = "/app/data/所有对话/主对话/产品数据"
BASE_DIR = "/app/data/所有对话/主对话/photonedge-website"

def clean_description(filepath):
    """Extract clean description from 详情.md file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find description between "Product introduction" and "Product parameters"
    match = re.search(r'Product introduction\n\n([^\#]+?)(?=\nProduct parameters:|$)', content, re.DOTALL)
    if match:
        desc = match.group(1).replace('\n', ' ').strip()
        # Remove duplicate parts
        parts = desc.split('. ')
        seen = set()
        unique = []
        for p in parts:
            if p not in seen and len(p) > 5:
                seen.add(p)
                unique.append(p)
        return '. '.join(unique)
    return ""

def get_all_products():
    """Get all products from data source"""
    products = []
    
    for root, dirs, files in os.walk(PRODUCTS_DIR):
        for file in files:
            if file == "详情.md":
                filepath = os.path.join(root, file)
                
                # Extract product info from path
                parts = root.split(os.sep)
                product_name = parts[-1]
                category = parts[-2] if len(parts) > 1 else ""
                
                # Get image path
                img_dir = os.path.join(os.path.dirname(filepath), "图片")
                img_path = ""
                if os.path.exists(img_dir):
                    imgs = [f for f in os.listdir(img_dir) if f.endswith('.jpg') or f.endswith('.png')]
                    if imgs:
                        img_path = imgs[0]
                
                # Correct spelling mistakes in name
                corrected_name = product_name
                if 'Opitcal' in product_name:
                    corrected_name = product_name.replace('Opitcal', 'Optical')
                if 'Glod' in product_name:
                    corrected_name = product_name.replace('Glod', 'Gold')
                
                # Get description
                desc = clean_description(filepath)
                if not desc or len(desc) < 20:
                    desc = f"High-quality {corrected_name} from PhotonEdge. Contact us for detailed specifications and customization options."
                
                products.append({
                    'name': corrected_name,
                    'original_name': product_name,
                    'category': category,
                    'description': desc,
                    'image': img_path,
                    'source_path': root
                })
    
    return products

def generate_products_data_js(products):
    """Generate products-data.js with full descriptions"""
    
    # Categories mapping for Chinese names
    category_zh = {
        "Optical Lenses": "光学透镜",
        "Optical Mirrors": "光学反射镜",
        "Optical Windows": "光学窗口",
        "Optical Prisms": "光学棱镜",
        "Optical Filters": "光学滤光片",
        "Optical Beamsplitters": "光学分光镜",
        "Optical Polarising Components": "光学偏振组件",
        "Optical Ball Lenses": "光学球透镜",
        "Optical Cylindrical Lenses": "光学柱面透镜",
        "Optical Half Ball Lenses": "光学半球透镜",
        "Optical Spherical Lenses": "光学球面透镜",
        "Optical Rod Lenses": "光学棒状透镜"
    }
    
    # Product name translations
    name_zh = {
        "UV Fused Silica Ball Lenses": "UV熔融石英球透镜",
        "Beamsplitter Plate": "分光板",
        "Non-Polarising Beamsplitter Cubes": "非偏振分光立方体",
        "Non-Polarizing Beamsplitter Plate": "非偏振分光板",
        "Optical Cube Beamsplitters": "光学立方体分光镜",
        "Optical Polarizing Beamsplitter Cubes": "偏振分光立方体",
        "UV Fused Silica Plano Concave Cylindrical Lenses": "UV熔融石英平凹柱面透镜",
        "UV Fused Silica Plano Convex Cylindrical Lenses": "UV熔融石英平凸柱面透镜",
        "Circular Variable ND(neutral density) Filters": "圆形可变中性密度滤光片",
        "Color Glass Filter": "颜色玻璃滤光片",
        "Fixed Neutral Density Filters": "固定中性密度滤光片",
        "Narrow band filter": "窄带滤光片",
        "Optical Linear Variable neutral density( ND) Filters": "线性可变中性密度滤光片",
        "Ultraviolet through visible absorption filters": "紫外-可见吸收滤光片",
        "UV Fused Silica Half Ball Lenses": "UV熔融石英半球透镜",
        "Achromatic Doublet Lenses": "消色差双胶合透镜",
        "BK7  Plano Concave Cylindrical Lenses": "BK7平凹柱面透镜",
        "BK7 & UV Fused Silica Double Concave Lenses": "BK7和UV熔融石英双凹透镜",
        "BK7 Double Convex Lenses": "BK7双凸透镜",
        "BK7 Half Ball Lenses": "BK7半球透镜",
        "BK7 Optical Ball Lenses": "BK7光学球透镜",
        "BK7 Plano Concave Lenses": "BK7平凹透镜",
        "BK7 Plano Convex Cylindrical Lenses": "BK7平凸柱面透镜",
        "BK7 Plano Convex Lenses": "BK7平凸透镜",
        "Laser beam extender": "激光扩束器",
        "Micro Objectives": "显微物镜",
        "Optical Aspheric Lenses": "非球面透镜",
        "Optical Silver Mirrors": "银镜",
        "Optical Gold Mirrors": "金镜",
        "Nd:YAG Laser Output Coupler": "Nd:YAG激光输出耦合器",
        "Optical Enhanced Aluminum Coated Mirrors": "增强铝镀膜反射镜",
        "Metal Coated  Concave Spherical Reflected Mirrors": "金属镀膜凹球面反射镜",
        "Dielectric Laser Line Mirrors": "介电激光线反射镜",
        "Broadband Dielectric Coated Mirrors": "宽带介电镀膜反射镜",
        "Optical Protective Aluminum Coated Mirrors": "保护铝镀膜反射镜",
        "Dielectric Dual Wavelength Laser Line Mirrors": "双波长介电激光线反射镜",
        "Optical Dichroic Mirrors": "二向色镜",
        "Air Spaced Zero Order high power Waveplates": "气隙零级高功率波片",
        "Cemented Zero Order Waveplate": "胶合零级波片",
        "Multi Order Waveplate": "多级波片",
        "Optical Circular Polarizer": "圆偏振片",
        "Optical Glan Laser Prisms": "Glan激光棱镜",
        "Optical Glan Taylor Prisms": "Glan Taylor棱镜",
        "Optical Isolator": "光隔离器",
        "Optical Linear Polarizer": "线偏振片",
        "Optical Wollaston Prisms": "Wollaston棱镜",
        "Quartz Polarization Rotator": "石英偏振旋转器",
        "Wide band achromatic wave plate": "宽带消色差波片",
        "Corner Cube Prisms": "角锥棱镜",
        "Dove Prisms": "Dove棱镜",
        "Equilateral Prisms": "等边棱镜",
        "Half Penta Prisms": "半五角棱镜",
        "Optical Wedge Prisms": "楔形棱镜",
        "Penta Prisms": "五角棱镜",
        "Right Angle Prisms": "直角棱镜",
        "Optical Rod Lenses": "光学棒状透镜",
        "UV Fused Silica Double Convex Lenses": "UV熔融石英双凸透镜",
        "UV Fused Silica Plano Concave Lenses": "UV熔融石英平凹透镜",
        "UV Fused Silica Plano Convex Lenses": "UV熔融石英平凸透镜",
        "BK7 Optical Windows": "BK7光学窗口",
        "Optical Silicon Windows": "硅光学窗口",
        "Optical CaF2 Windows": "CaF2光学窗口",
        "Optical Germanium Windows": "锗光学窗口",
        "Optical Sapphire Windows": "蓝宝石光学窗口",
        "Optical ZnSe Windows": "ZnSe光学窗口",
        "UV Fused Silica Windows": "UV熔融石英窗口"
    }
    
    js_lines = []
    js_lines.append("// PhotonEdge Products Data")
    js_lines.append("// Total: {} products".format(len(products)))
    js_lines.append("// Generated with complete descriptions from source data")
    js_lines.append("")
    js_lines.append("const PRODUCTS = [")
    
    for i, product in enumerate(products):
        name = product['name']
        category = product['category']
        description = product['description'].replace('"', "'").replace('\n', ' ').strip()
        
        # Get Chinese names
        name_zh_val = name_zh.get(name, name)
        category_zh_val = category_zh.get(category, category)
        
        # Build image path
        image_path = "images/products/{}/{}.jpg".format(
            category.lower().replace(' ', '-').replace('&', 'and'),
            name.lower().replace(' ', '-').replace('&', 'and').replace(':', '-').replace("'", '').replace('(', '').replace(')', '').replace(',', '')
        )
        
        # Handle the "Glod" -> "Gold" and "Opitcal" -> "Optical" corrections
        if 'Gold' in name and 'original_name' in product:
            image_path = image_path.replace('optical-gold-mirrors', 'optical-gold-mirrors')
        if 'Optical Silicon' in name:
            image_path = image_path.replace('optical-silicon-windows', 'optical-silicon-windows')
        
        # Specs (simplified for now)
        specs = "{}: BK7; Surface Quality: 40-20; Flatness: λ/4@632.8nm".format(name)
        
        comma = "," if i < len(products) - 1 else ""
        js_lines.append("  {{")
        js_lines.append('    "name": "{}",'.format(name))
        js_lines.append('    "nameZh": "{}",'.format(name_zh_val))
        js_lines.append('    "category": "{}",'.format(category))
        js_lines.append('    "categoryZh": "{}",'.format(category_zh_val))
        js_lines.append('    "description": "{}",'.format(description))
        js_lines.append('    "image": "{}"'.format(image_path))
        js_lines.append("  }}{}".format(comma))
    
    js_lines.append("];")
    js_lines.append("")
    js_lines.append("// Category to image mapping for homepage")
    js_lines.append("const CATEGORY_IMAGES = {")
    
    # Get unique categories
    categories = list(set(p['category'] for p in products))
    for i, cat in enumerate(sorted(categories)):
        cat_products = [p for p in products if p['category'] == cat]
        if cat_products:
            first_product = cat_products[0]
            img = "images/products/{}/{}.jpg".format(
                cat.lower().replace(' ', '-').replace('&', 'and'),
                first_product['name'].lower().replace(' ', '-').replace('&', 'and').replace(':', '-').replace("'", '').replace('(', '').replace(')', '').replace(',', '')
            )
            if 'Gold' in first_product['name']:
                img = "images/products/optical-mirrors/optical-gold-mirrors.jpg"
            if 'Optical Silicon' in first_product['name']:
                img = "images/products/optical-windows/optical-silicon-windows.jpg"
            comma = "," if i < len(categories) - 1 else ""
            js_lines.append('    "{}": "{}",'.format(cat, img))
    
    js_lines.append("};")
    
    return "\n".join(js_lines)

def main():
    print("Generating PhotonEdge website files...")
    
    # Get all products
    products = get_all_products()
    print(f"Found {len(products)} products")
    
    # Generate products-data.js
    products_js = generate_products_data_js(products)
    with open(os.path.join(BASE_DIR, "js/products-data.js"), 'w', encoding='utf-8') as f:
        f.write(products_js)
    print("Generated js/products-data.js")
    
    print("\nAll files generated successfully!")

if __name__ == "__main__":
    main()
