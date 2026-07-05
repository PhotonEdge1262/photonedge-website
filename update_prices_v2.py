#!/usr/bin/env python3
"""Update products-data.js with reference prices based on competitor analysis."""

import re

# Read the file
with open('/app/data/所有对话/主对话/v59-work/js/products-data.js', 'r') as f:
    content = f.read()

# Reference prices based on competitor analysis (Thorlabs, Edmund Optics, etc.)
# Format: slug -> (price_range_low, price_range_high)
reference_prices = {
    # Optical Lenses
    "bk7-plano-convex": (8, 68),
    "bk7-bi-convex": (10, 65),
    "bk7-plano-concave": (8, 60),
    "bk7-bi-concave": (10, 62),
    "bk7-positive-meniscus": (12, 70),
    "bk7-negative-meniscus": (12, 68),
    "uv-fused-silica-plano-convex": (35, 130),
    "uv-fused-silica-bi-convex": (38, 125),
    "uv-fused-silica-plano-concave": (35, 120),
    "uv-fused-silica-bi-concave": (38, 120),
    "bk7-plano-convex-cylindrical": (12, 55),
    "bk7-plano-concave-cylindrical": (12, 50),
    "uv-fused-silica-plano-convex-cylindrical": (35, 95),
    "uv-fused-silica-plano-concave-cylindrical": (35, 90),
    "achromatic-doublet": (35, 210),
    "bk7-c-lenses": (15, 65),
    "bk7-ball-lenses": (8, 45),
    "uv-fused-silica-ball-lenses": (25, 85),
    "bk7-rod-lenses": (10, 50),
    "uv-fused-silica-rod-lenses": (28, 75),
    "aspherical-lenses": (45, 350),
    "laser-beam-expanders": (50, 280),
    "microscope-objectives": (80, 1500),
    
    # Optical Windows
    "bk7-windows": (8, 55),
    "uv-fused-silica-windows": (18, 120),
    "sapphire-windows": (35, 200),
    "caf2-windows": (30, 180),
    "ge-windows": (80, 450),
    "si-windows": (60, 350),
    "znse-windows": (70, 400),
    
    # Optical Mirrors
    "laser-line-high-reflected-mirrors": (25, 180),
    "high-energy-laser-mirrors": (60, 350),
    "broadband-dielectric-mirrors": (45, 280),
    "protected-aluminum-mirrors": (15, 72),
    "enhanced-aluminum-mirrors": (18, 85),
    "protected-silver-mirrors": (20, 95),
    "protected-gold-mirrors": (25, 150),
    
    # Optical Prisms
    "bk7-right-angle-prisms": (8, 65),
    "uv-fused-silica-right-angle-prisms": (28, 120),
    "penta-prisms": (45, 160),
    "corner-cube-prisms": (70, 240),
    "dove-prisms": (30, 140),
    "equilateral-dispersing-prisms": (15, 100),
    "roof-prisms": (35, 150),
    
    # Optical Filters
    "narrow-band-interference-filters": (45, 290),
    "fixed-neutral-density-filters": (20, 120),
    "variable-neutral-density-filters": (55, 280),
    "uv-bandpass-filters": (40, 170),
    "ir-bandpass-filters": (45, 290),
    
    # Optical Beamsplitters
    "beamsplitter-plates": (18, 95),
    "cube-beamsplitters": (35, 180),
    "non-polarizing-cube-beamsplitters": (45, 250),
    "polarizing-cube-beamsplitters": (55, 300),
    
    # Optical Wave Plates
    "multiple-order-waveplates": (30, 150),
    "dual-wavelength-waveplates": (60, 250),
    "cemented-zero-order-waveplates": (80, 350),
    "air-spaced-zero-order-waveplates": (100, 450),
    
    # Optical Polarizers
    "visible-linear-polarizers": (15, 110),
    "visible-circular-polarizers": (20, 130),
    "ir-polarizers": (45, 250),
    "glan-taylor-prisms": (180, 670),
    "glan-laser-prisms": (200, 800),
    "glan-thompson-prisms": (150, 550),
    "wollaston-prisms": (180, 650),
    
    # Laser Protection
    "laser-safety-goggles": (55, 320),
    
    # Additional products
    "ndyag-output-couplers": (50, 250),
    "dichroic-mirrors": (40, 280),
}

# Strategy: for each product block, find the slug, then go BACKWARDS to find the price/priceNote fields
# Each product is a JSON-like object. Let's use regex to find and replace within each product block.

# Split the content into product blocks by finding each { ... } that contains a slug
# Actually, let's use a simpler approach: for each slug, find its position, 
# then find the nearest "price": 0, "priceNote": "Contact for pricing", "priceNoteZh": "询价" BEFORE it

updated_count = 0
for slug, (low, high) in reference_prices.items():
    slug_pattern = f'"slug": "{slug}"'
    slug_pos = content.find(slug_pattern)
    
    if slug_pos == -1:
        print(f"WARNING: Could not find slug '{slug}'")
        continue
    
    # Search backwards from slug position to find the price fields
    # They should be within the ~500 characters before the slug
    search_start = max(0, slug_pos - 600)
    region = content[search_start:slug_pos + len(slug_pattern)]
    
    # Replace in this region
    old_price = '"price": 0,'
    new_price = f'"price": {low},'
    
    old_note = '"priceNote": "Contact for pricing",'
    new_note = f'"priceNote": "Reference: ${low} - ${high}",'
    
    old_note_zh = '"priceNoteZh": "询价",'
    new_note_zh = f'"priceNoteZh": "参考价：¥{low*7} - ¥{high*7}",'
    
    # Find and replace in the region
    new_region = region.replace(old_price, new_price, 1)
    new_region = new_region.replace(old_note, new_note, 1)
    new_region = new_region.replace(old_note_zh, new_note_zh, 1)
    
    if new_region != region:
        content = content[:search_start] + new_region + content[slug_pos + len(slug_pattern):]
        updated_count += 1
    else:
        print(f"WARNING: No replacements made for slug '{slug}'")

# Write the updated file
with open('/app/data/所有对话/主对话/v59-work/js/products-data.js', 'w') as f:
    f.write(content)

print(f"Done! Updated {updated_count} products with reference prices.")
print(f"Total expected: {len(reference_prices)}")
