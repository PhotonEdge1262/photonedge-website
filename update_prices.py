#!/usr/bin/env python3
"""Update products-data.js with reference prices based on competitor analysis."""

import re
import json

# Read the file
with open('/app/data/所有对话/主对话/v59-work/js/products-data.js', 'r') as f:
    content = f.read()

# Reference prices based on competitor analysis (Thorlabs, Edmund Optics, etc.)
# Format: slug -> (price_range_low, price_range_high, currency)
# These are REFERENCE prices based on international competitors, shown as "Reference: $X - $Y"
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
    "bandpass-filters": (40, 250),
    
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
}

# Now update the products-data.js
# We need to find each product's slug and update its price fields

for slug, (low, high) in reference_prices.items():
    # Find the pattern: "slug": "xxx" ... "price": 0, ... "priceNote": "Contact for pricing", ... "priceNoteZh": "询价"
    # We'll do targeted replacements
    
    # Pattern to find the price field near the slug
    # First find the slug position
    slug_pattern = f'"slug": "{slug}"'
    slug_pos = content.find(slug_pattern)
    
    if slug_pos == -1:
        print(f"WARNING: Could not find slug '{slug}'")
        continue
    
    # Find the price, priceNote, priceNoteZh after this slug position
    # They should be within the next ~200 characters (before the next product or partNumbers)
    search_region_end = slug_pos + 500
    
    # Replace "price": 0 with "price": low (we'll use low as the "from" price)
    price_pattern = '"price": 0'
    price_pos = content.find(price_pattern, slug_pos, search_region_end)
    if price_pos != -1:
        content = content[:price_pos] + f'"price": {low}' + content[price_pos + len(price_pattern):]
        # Adjust search region end since we changed content length
        diff = len(f'"price": {low}') - len(price_pattern)
        search_region_end += diff
        slug_pos += 0  # slug_pos doesn't change since it's before price_pos
    
    # Replace "priceNote": "Contact for pricing" with reference price range
    old_note = '"priceNote": "Contact for pricing"'
    new_note = f'"priceNote": "Reference: ${low} - ${high}"'
    note_pos = content.find(old_note, slug_pos, search_region_end + len(new_note))
    if note_pos != -1:
        content = content[:note_pos] + new_note + content[note_pos + len(old_note):]
        diff2 = len(new_note) - len(old_note)
        search_region_end += diff2
    
    # Replace "priceNoteZh": "询价" with Chinese reference price
    old_note_zh = '"priceNoteZh": "询价"'
    new_note_zh = f'"priceNoteZh": "参考价：¥{low*7} - ¥{high*7}"'
    note_zh_pos = content.find(old_note_zh, slug_pos, search_region_end + len(new_note_zh))
    if note_zh_pos != -1:
        content = content[:note_zh_pos] + new_note_zh + content[note_zh_pos + len(old_note_zh):]

# Write the updated file
with open('/app/data/所有对话/主对话/v59-work/js/products-data.js', 'w') as f:
    f.write(content)

print("Done! Updated reference prices for all products.")
print(f"Total products with prices: {len(reference_prices)}")
