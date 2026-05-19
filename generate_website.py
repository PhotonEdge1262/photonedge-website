#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PhotonEdge 产品数据处理脚本
处理产品数据并生成网站文件
"""

import os
import shutil
import json
import re
from pathlib import Path

# 配置路径 - 使用绝对路径确保在任何目录下都能运行
SCRIPT_DIR = Path(__file__).parent.resolve()
SOURCE_DATA_DIR = SCRIPT_DIR.parent / "产品数据"
TARGET_WEBSITE_DIR = SCRIPT_DIR
SOURCE_WEBSITE_DIR = SCRIPT_DIR.parent / "photonedge-vercel"

# 分类映射 - 转换为URL友好格式
CATEGORY_MAPPING = {
    "Optical Lenses": "optical-lenses",
    "Optical Spherical Lenses": "optical-spherical-lenses",
    "Optical Cylindrical Lenses": "optical-cylindrical-lenses",
    "Optical Rod Lenses": "optical-rod-lenses",
    "Optical Half Ball Lenses": "optical-half-ball-lenses",
    "Optical Ball Lenses": "optical-ball-lenses",
    "Optical Windows": "optical-windows",
    "Optical Mirrors": "optical-mirrors",
    "Optical Prisms": "optical-prisms",
    "Optical Filters": "optical-filters",
    "Optical Beamsplitters": "optical-beamsplitters",
    "Optical Polarising Components": "optical-polarizing-components"
}

# 分类中文名
CATEGORY_NAMES_CN = {
    "Optical Lenses": "光学透镜",
    "Optical Spherical Lenses": "球面透镜",
    "Optical Cylindrical Lenses": "柱面透镜",
    "Optical Rod Lenses": "棒状透镜",
    "Optical Half Ball Lenses": "半球透镜",
    "Optical Ball Lenses": "球面透镜",
    "Optical Windows": "光学窗口",
    "Optical Mirrors": "光学反射镜",
    "Optical Prisms": "光学棱镜",
    "Optical Filters": "光学滤光片",
    "Optical Beamsplitters": "光学分束器",
    "Optical Polarising Components": "偏振光学组件"
}

def slugify(text):
    """将文本转换为URL友好的slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    text = text.strip('-')
    return text

def parse_csv():
    """解析产品汇总CSV文件"""
    products = []
    csv_path = SOURCE_DATA_DIR / "产品汇总.csv"
    
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        for line in lines[1:]:  # 跳过表头
            parts = line.strip().split(',')
            if len(parts) >= 6:
                # 处理CSV中可能包含逗号的情况
                seq = parts[0]
                category = parts[1]
                name = parts[2]
                product_id = parts[3]
                img_count = parts[4]
                # 描述可能包含逗号，从第6部分开始合并
                description = ','.join(parts[5:])
                
                products.append({
                    'seq': seq,
                    'category': category,
                    'name': name,
                    'product_id': product_id,
                    'img_count': img_count,
                    'description': description
                })
    
    return products

def create_directories():
    """创建目录结构"""
    dirs = [
        TARGET_WEBSITE_DIR / "images" / "products",
        TARGET_WEBSITE_DIR / "js",
        TARGET_WEBSITE_DIR / "css",
    ]
    
    # 创建分类子目录
    for cat_en, cat_slug in CATEGORY_MAPPING.items():
        dirs.append(TARGET_WEBSITE_DIR / "images" / "products" / cat_slug)
    
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    
    print(f"Created {len(dirs)} directories")

def find_product_image(product_name, category):
    """查找产品图片路径"""
    # 尝试不同的目录结构
    possible_paths = [
        SOURCE_DATA_DIR / category / product_name / "图片" / "main.jpg",
        SOURCE_DATA_DIR / category / product_name / "图片" / "main.png",
        SOURCE_DATA_DIR / category / product_name / "图片" / "main.jpeg",
    ]
    
    for path in possible_paths:
        if path.exists():
            return path
    
    # 尝试在子目录中查找
    category_path = SOURCE_DATA_DIR / category
    if category_path.exists():
        for item in category_path.iterdir():
            if item.is_dir() and product_name.lower() in item.name.lower():
                img_dir = item / "图片"
                if img_dir.exists():
                    for img in img_dir.iterdir():
                        if img.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                            return img
    
    return None

def copy_images(products):
    """复制并整理产品图片"""
    copied = 0
    not_found = []
    
    for product in products:
        src_path = find_product_image(product['name'], product['category'])
        if src_path:
            cat_slug = CATEGORY_MAPPING.get(product['category'], 'other')
            product_slug = slugify(product['name'])
            dst_filename = f"{product_slug}{src_path.suffix}"
            dst_path = TARGET_WEBSITE_DIR / "images" / "products" / cat_slug / dst_filename
            
            shutil.copy2(src_path, dst_path)
            product['image_path'] = f"images/products/{cat_slug}/{dst_filename}"
            copied += 1
        else:
            product['image_path'] = None
            not_found.append(f"{product['category']}/{product['name']}")
    
    print(f"Copied {copied} images")
    if not_found:
        print(f"Images not found for {len(not_found)} products:")
        for nf in not_found[:5]:
            print(f"  - {nf}")
    
    return products

def generate_products_data_js(products):
    """生成 products-data.js 文件"""
    # 按分类组织产品
    categories = {}
    
    for product in products:
        cat_en = product['category']
        cat_slug = CATEGORY_MAPPING.get(cat_en, slugify(cat_en))
        cat_name_cn = CATEGORY_NAMES_CN.get(cat_en, cat_en)
        
        if cat_en not in categories:
            categories[cat_en] = {
                'id': cat_slug,
                'name': cat_en,
                'name_cn': cat_name_cn,
                'products': []
            }
        
        product_data = {
            'id': str(product['product_id']),
            'name': product['name'],
            'name_cn': cat_name_cn,
            'slug': slugify(product['name']),
            'category': cat_slug,
            'category_name': cat_en,
            'image': product.get('image_path'),
            'description': product['description'],
            'specs': generate_specs(product)
        }
        
        categories[cat_en]['products'].append(product_data)
    
    # 构建最终数据结构
    data = {
        'categories': list(categories.values()),
        'total_products': len(products)
    }
    
    # 生成JS文件
    js_content = f'''// Products Data - Auto-generated from scraper
// Total: {len(products)} products in {len(categories)} categories

const productsData = {json.dumps(data, indent=2, ensure_ascii=False)};

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {{
    module.exports = productsData;
}}
'''
    
    js_path = TARGET_WEBSITE_DIR / "js" / "products-data.js"
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"Generated products-data.js with {len(products)} products in {len(categories)} categories")
    return data

def generate_specs(product):
    """根据产品生成规格参数"""
    name = product['name'].lower()
    specs = {
        'Material': 'BK7 / Fused Silica',
        'Surface Quality': '40-20 S/D',
        'Coating': 'Optional',
        'Dimensional Tolerance': '+/- 0.1mm'
    }
    
    # 根据产品类型添加特定参数
    if 'achromatic' in name:
        specs['Type'] = 'Achromatic Doublet'
        specs['Wavelength Range'] = '400-700nm'
    elif 'plano-convex' in name or 'plano convex' in name:
        specs['Type'] = 'Plano-Convex'
        specs['Focal Length'] = 'Customized'
    elif 'plano-concave' in name or 'plano concave' in name:
        specs['Type'] = 'Plano-Concave'
        specs['Focal Length'] = 'Customized'
    elif 'double convex' in name or 'double-convex' in name:
        specs['Type'] = 'Double-Convex'
        specs['Focal Length'] = 'Customized'
    elif 'double concave' in name or 'double-concave' in name:
        specs['Type'] = 'Double-Concave'
        specs['Focal Length'] = 'Customized'
    elif 'ball lens' in name:
        specs['Type'] = 'Ball Lens'
        specs['Diameter'] = '1-10mm'
    elif 'cylindrical' in name:
        specs['Type'] = 'Cylindrical'
        specs['Curve'] = 'Customized'
    elif 'window' in name:
        specs['Type'] = 'Window'
        specs['Thickness'] = '1-10mm'
        if 'sapphire' in name:
            specs['Material'] = 'Sapphire'
        elif 'germanium' in name:
            specs['Material'] = 'Germanium'
            specs['Wavelength'] = '2-12μm'
        elif 'caf2' in name or 'caf₂' in name:
            specs['Material'] = 'CaF₂'
            specs['Wavelength'] = '0.13-10μm'
        elif 'znse' in name:
            specs['Material'] = 'ZnSe'
            specs['Wavelength'] = '0.5-22μm'
        elif 'silicon' in name:
            specs['Material'] = 'Silicon'
            specs['Wavelength'] = '1.2-7μm'
        elif 'uv' in name or 'fused silica' in name:
            specs['Material'] = 'UV Fused Silica'
            specs['Wavelength'] = '185nm-2.1μm'
        else:
            specs['Material'] = 'BK7'
    elif 'mirror' in name:
        specs['Type'] = 'Mirror'
        if 'dielectric' in name:
            specs['Coating'] = 'Dielectric'
        elif 'gold' in name:
            specs['Coating'] = 'Gold'
            specs['Reflectivity'] = '>98% @ 2μm+'
        elif 'silver' in name:
            specs['Coating'] = 'Silver'
            specs['Reflectivity'] = '>95% @ 450nm-2μm'
        elif 'aluminum' in name:
            specs['Coating'] = 'Aluminum'
            specs['Reflectivity'] = '>90% @ VIS-NIR'
        if 'laser' in name:
            specs['Application'] = 'Laser'
    elif 'prism' in name:
        specs['Type'] = 'Prism'
        if 'right angle' in name:
            specs['Angle'] = '90°-45°-45°'
        elif 'penta' in name:
            specs['Angle'] = '45°-90°-45°-135°-45°'
        elif 'equilateral' in name:
            specs['Angle'] = '60°-60°-60°'
        elif 'corner cube' in name:
            specs['Type'] = 'Corner Cube'
        elif 'wedge' in name:
            specs['Type'] = 'Wedge Prism'
    elif 'filter' in name:
        specs['Type'] = 'Filter'
        if 'nd' in name or 'neutral' in name:
            specs['Type'] = 'Neutral Density'
            specs['OD Range'] = '0.1-4.0'
        elif 'bandpass' in name or 'narrow' in name:
            specs['Type'] = 'Bandpass'
            specs['Bandwidth'] = 'Customized'
        elif 'color' in name:
            specs['Type'] = 'Color Glass'
    elif 'beamsplitter' in name:
        specs['Type'] = 'Beamsplitter'
        specs['Ratio'] = '50/50 (typical)'
        if 'polarizing' in name:
            specs['Type'] = 'Polarizing Beamsplitter'
    elif 'waveplate' in name or 'wave plate' in name:
        specs['Type'] = 'Waveplate'
        if 'quarter' in name or 'λ/4' in name:
            specs['Retardation'] = 'λ/4'
        elif 'half' in name or 'λ/2' in name:
            specs['Retardation'] = 'λ/2'
        else:
            specs['Retardation'] = 'λ/4, λ/2, λ'
    elif 'polarizer' in name or 'polarizer' in name:
        specs['Type'] = 'Polarizer'
        specs['Extinction Ratio'] = '>1000:1'
    
    return specs

def generate_products_html():
    """生成 products.html 页面"""
    html_path = SOURCE_WEBSITE_DIR / "products.html"
    if not html_path.exists():
        print("products.html not found in source")
        return
    
    # 读取原模板
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换数据加载逻辑，改为使用本地JS文件
    new_script = '''
    <script>
        // ===== 本地产品数据 =====
        let localProductsData = null;
        
        // ===== 加载本地产品数据 =====
        async function loadLocalProducts() {
            try {
                // 加载本地产品数据
                const response = await fetch('js/products-data.js');
                const text = await response.text();
                eval(text);
                localProductsData = productsData;
                
                // 初始化产品列表
                if (localProductsData && localProductsData.categories) {
                    initProductList();
                }
            } catch (error) {
                console.error('Failed to load local products:', error);
            }
        }
        
        // ===== 初始化产品列表 =====
        function initProductList() {
            // 渲染分类标签
            renderCategoryTags();
            
            // 加载所有产品
            loadAllProducts();
        }
        
        // ===== 渲染分类标签 =====
        function renderCategoryTags() {
            const tagsContainer = document.querySelector('.category-tag').parentElement;
            const allButton = tagsContainer.querySelector('[data-category="all"]');
            
            if (localProductsData && localProductsData.categories) {
                // 保留"All"按钮
                let newTags = allButton.outerHTML;
                
                // 添加各分类按钮
                localProductsData.categories.forEach(cat => {
                    newTags += `
                        <button class="category-tag px-4 py-2 rounded-full text-sm font-medium bg-gray-100 text-gray-700 hover:bg-primary-50 hover:text-primary-600 transition-smooth"
                            data-category="${cat.id}">
                            ${cat.name}
                        </button>
                    `;
                });
                
                tagsContainer.innerHTML = newTags;
                
                // 重新绑定分类点击事件
                bindCategoryEvents();
            }
        }
        
        // ===== 绑定分类事件 =====
        function bindCategoryEvents() {
            document.querySelectorAll('.category-tag').forEach(tag => {
                tag.addEventListener('click', function() {
                    document.querySelectorAll('.category-tag').forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                    state.currentCategory = this.dataset.category;
                    loadAllProducts();
                });
            });
        }
        
        // ===== 加载所有产品 =====
        function loadAllProducts() {
            let filteredProducts = [];
            
            if (state.currentCategory === 'all') {
                // 显示所有产品
                localProductsData.categories.forEach(cat => {
                    filteredProducts = filteredProducts.concat(cat.products);
                });
            } else {
                // 按分类筛选
                const category = localProductsData.categories.find(c => c.id === state.currentCategory);
                if (category) {
                    filteredProducts = category.products;
                }
            }
            
            state.totalProducts = filteredProducts.length;
            state.products = filteredProducts;
            renderProducts(filteredProducts);
        }
        
        // ===== 页面加载完成后初始化 =====
        document.addEventListener('DOMContentLoaded', function() {
            loadLocalProducts();
            bindCategoryEvents();
        });
    </script>
    '''
    
    # 在</body>前插入新脚本
    content = content.replace('</body>', new_script + '</body>')
    
    # 保存到目标目录
    dst_path = TARGET_WEBSITE_DIR / "products.html"
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Generated products.html")

def generate_product_detail_html():
    """生成 product-detail.html 页面"""
    html_path = SOURCE_WEBSITE_DIR / "product-detail.html"
    if not html_path.exists():
        print("product-detail.html not found in source")
        return
    
    # 读取原模板
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 添加产品数据加载和渲染脚本
    detail_script = '''
    <script>
        // ===== 加载产品数据 =====
        let localProductsData = null;
        
        async function loadProductData() {
            try {
                const response = await fetch('js/products-data.js');
                const text = await response.text();
                eval(text);
                localProductsData = productsData;
                
                // 从URL获取产品ID
                const urlParams = new URLSearchParams(window.location.search);
                const productId = urlParams.get('id');
                
                if (productId && localProductsData) {
                    loadProductDetail(productId);
                } else {
                    showNotFound();
                }
            } catch (error) {
                console.error('Error loading product data:', error);
                showNotFound();
            }
        }
        
        // ===== 加载产品详情 =====
        function loadProductDetail(productId) {
            let product = null;
            let currentCategory = null;
            
            // 查找产品
            for (const category of localProductsData.categories) {
                const found = category.products.find(p => p.id === productId);
                if (found) {
                    product = found;
                    currentCategory = category;
                    break;
                }
            }
            
            if (!product) {
                showNotFound();
                return;
            }
            
            // 更新页面内容
            updateProductPage(product, currentCategory);
        }
        
        // ===== 更新产品页面 =====
        function updateProductPage(product, category) {
            // 更新标题
            document.title = `${product.name} - PhotonEdge`;
            
            // 更新面包屑和产品名
            const breadcrumb = document.querySelector('.breadcrumb');
            if (breadcrumb) {
                breadcrumb.innerHTML = `
                    <div class="breadcrumb-container">
                        <a href="index.html">Home</a>
                        <span>&gt;</span>
                        <a href="products.html">Products</a>
                        <span>&gt;</span>
                        <a href="products.html?category=${category.id}">${category.name}</a>
                        <span>&gt;</span>
                        <span class="current">${product.name}</span>
                    </div>
                `;
            }
            
            // 更新产品名称
            const productNameEl = document.querySelector('.product-info h1');
            if (productNameEl) {
                productNameEl.textContent = product.name;
            }
            
            // 更新分类标签
            const categoryEl = document.querySelector('.product-category');
            if (categoryEl) {
                categoryEl.textContent = category.name;
            }
            
            // 更新产品图片
            const mainImage = document.querySelector('.main-image img');
            if (mainImage) {
                if (product.image) {
                    mainImage.src = product.image;
                } else {
                    mainImage.src = 'https://s.coze.cn/image/aLbrCP5IcO0/';
                }
            }
            
            // 更新描述
            const descEl = document.querySelector('.product-description');
            if (descEl) {
                descEl.innerHTML = `<p>${product.description || 'No description available.'}</p>`;
            }
            
            // 更新规格参数表
            updateSpecsTable(product.specs);
            
            // 加载相关产品
            loadRelatedProducts(product, category);
            
            // 隐藏loading
            document.querySelector('.loading')?.classList.add('hidden');
        }
        
        // ===== 更新规格参数表 =====
        function updateSpecsTable(specs) {
            const tbody = document.querySelector('.parameters-table tbody');
            if (tbody && specs) {
                let html = '';
                for (const [key, value] of Object.entries(specs)) {
                    html += `<tr><td>${key}</td><td>${value}</td></tr>`;
                }
                tbody.innerHTML = html;
            }
        }
        
        // ===== 加载相关产品 =====
        function loadRelatedProducts(currentProduct, category) {
            const relatedGrid = document.querySelector('.related-grid');
            if (!relatedGrid) return;
            
            const related = category.products
                .filter(p => p.id !== currentProduct.id)
                .slice(0, 4);
            
            if (related.length === 0) {
                document.querySelector('.related-section')?.classList.add('hidden');
                return;
            }
            
            let html = '';
            related.forEach(product => {
                html += `
                    <div class="product-card" onclick="window.location.href='product-detail.html?id=${product.id}'">
                        <div class="product-card-image">
                            <img src="${product.image || 'https://s.coze.cn/image/aLbrCP5IcO0/'}" alt="${product.name}">
                        </div>
                        <div class="product-card-content">
                            <h3>${product.name}</h3>
                            <p>${category.name}</p>
                            <span class="view-btn">
                                View Details
                                <i class="fas fa-arrow-right"></i>
                            </span>
                        </div>
                    </div>
                `;
            });
            
            relatedGrid.innerHTML = html;
        }
        
        // ===== 显示404 =====
        function showNotFound() {
            const mainContent = document.querySelector('.product-section');
            if (mainContent) {
                mainContent.innerHTML = `
                    <div class="not-found">
                        <i class="fas fa-search"></i>
                        <h2>Product Not Found</h2>
                        <p>The product you're looking for doesn't exist.</p>
                        <a href="products.html" class="btn btn-primary">
                            <i class="fas fa-arrow-left"></i>
                            Back to Products
                        </a>
                    </div>
                `;
            }
        }
        
        // ===== 页面加载 =====
        document.addEventListener('DOMContentLoaded', loadProductData);
    </script>
    '''
    
    # 在</body>前插入脚本
    content = content.replace('</body>', detail_script + '</body>')
    
    # 保存到目标目录
    dst_path = TARGET_WEBSITE_DIR / "product-detail.html"
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Generated product-detail.html")

def copy_base_files():
    """复制基础文件"""
    files_to_copy = [
        ("index.html", "index.html"),
        ("about.html", "about.html"),
        ("applications.html", "applications.html"),
        ("news.html", "news.html"),
        ("downloads.html", "downloads.html"),
        ("contact.html", "contact.html"),
        ("logo.png", "logo.png"),
        (".gitignore", ".gitignore"),
        ("README.md", "README.md"),
        ("vercel.json", "vercel.json"),
    ]
    
    for src, dst in files_to_copy:
        src_path = SOURCE_WEBSITE_DIR / src
        dst_path = TARGET_WEBSITE_DIR / dst
        if src_path.exists():
            shutil.copy2(src_path, dst_path)
            print(f"Copied {src}")
    
    # 复制logo
    logo_src = SOURCE_WEBSITE_DIR / "logo.png"
    if logo_src.exists():
        shutil.copy2(logo_src, TARGET_WEBSITE_DIR / "logo.png")

def main():
    """主函数"""
    print("=" * 50)
    print("PhotonEdge Website Generator")
    print("=" * 50)
    
    # 1. 创建目录
    print("\n[1/6] Creating directories...")
    create_directories()
    
    # 2. 解析产品数据
    print("\n[2/6] Parsing product data...")
    products = parse_csv()
    print(f"Found {len(products)} products")
    
    # 3. 复制图片
    print("\n[3/6] Copying and organizing images...")
    products = copy_images(products)
    
    # 4. 生成产品数据JS
    print("\n[4/6] Generating products-data.js...")
    generate_products_data_js(products)
    
    # 5. 生成HTML页面
    print("\n[5/6] Generating HTML pages...")
    generate_products_html()
    generate_product_detail_html()
    
    # 6. 复制基础文件
    print("\n[6/6] Copying base files...")
    copy_base_files()
    
    print("\n" + "=" * 50)
    print("Website generation completed!")
    print(f"Output directory: {TARGET_WEBSITE_DIR}")
    print("=" * 50)

if __name__ == "__main__":
    main()
