#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate products-data.js V34 from official product catalog data"""

import json

products = []

# Helper
def add(id, name, nameZh, category, categoryZh, desc, descZh, slug, cat_folder, params, part_numbers):
    products.append({
        "id": id,
        "name": name,
        "nameZh": nameZh,
        "category": category,
        "categoryZh": categoryZh,
        "description": desc,
        "descriptionZh": descZh,
        "image": "images/products/{}/{}.jpg".format(cat_folder, slug),
        "parameters": params,
        "price": 0,
        "priceUnit": "USD",
        "priceNote": "Contact for pricing",
        "priceNoteZh": "询价",
        "slug": slug,
        "partNumbers": part_numbers
    })

# ========== 1. Optical Lenses (23) ==========
add(1, "BK7 Plano-Convex Lenses", "K9平凸球面透镜",
    "Optical Lenses", "光学透镜",
    "Plano-convex lenses have a positive focal length and are widely used for focusing and collimating light beams. Made from K9(BK7) optical glass with high uniformity, free of streaks, impurities and bubbles.",
    "平凸透镜具有正焦距，被广泛地应用于光束的聚焦和准直。采用K9(BK7)光学玻璃，均匀性好，无纹理、杂质、气泡。",
    "bk7-plano-convex", "optical-lenses",
    {"material": "K9(BK7)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "A:AR 350-650nm / B:AR 650-950nm / C:AR 950-1250nm"},
    [{"partNumber": "LOPCXB6.0-10.0", "diameter": "6.00mm", "focalLength": "10.00mm", "centerThickness": "2.46mm", "edgeThickness": "1.50mm", "backFocalLength": "8.37mm"},
     {"partNumber": "LOPCXB10-15", "diameter": "10.00mm", "focalLength": "15.00mm", "centerThickness": "3.80mm", "edgeThickness": "2.00mm", "backFocalLength": "12.50mm"},
     {"partNumber": "LOPCXB15-30", "diameter": "15.00mm", "focalLength": "30.00mm", "centerThickness": "3.90mm", "edgeThickness": "2.00mm", "backFocalLength": "27.40mm"},
     {"partNumber": "LOPCXB25.4-50", "diameter": "25.40mm", "focalLength": "50.00mm", "centerThickness": "5.20mm", "edgeThickness": "2.00mm", "backFocalLength": "46.60mm"},
     {"partNumber": "LOPCXB25.4-100", "diameter": "25.40mm", "focalLength": "100.00mm", "centerThickness": "3.50mm", "edgeThickness": "2.00mm", "backFocalLength": "97.70mm"},
     {"partNumber": "LOPCXB50.8-100", "diameter": "50.80mm", "focalLength": "100.00mm", "centerThickness": "9.70mm", "edgeThickness": "3.00mm", "backFocalLength": "93.60mm"},
     {"partNumber": "LOPCXB50.8-200", "diameter": "50.80mm", "focalLength": "200.00mm", "centerThickness": "6.20mm", "edgeThickness": "3.00mm", "backFocalLength": "195.91mm"},
     {"partNumber": "LOPCXB75-150", "diameter": "75.00mm", "focalLength": "150.00mm", "centerThickness": "12.70mm", "edgeThickness": "3.00mm", "backFocalLength": "141.62mm"}]
)

add(2, "BK7 Bi-Convex Lenses", "K9双凸球面透镜",
    "Optical Lenses", "光学透镜",
    "Bi-convex lenses have a positive focal length and are mainly used for collimating and focusing light. Made from H-K9L(BK7) optical glass with strict quality control.",
    "双凸透镜具有正焦距，主要用于光的准直、聚焦等。采用H-K9L(BK7)光学玻璃，严格按技术规格加工检验。",
    "bk7-bi-convex", "optical-lenses",
    {"material": "H-K9L(BK7)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "A:AR 350-650nm / B:AR 650-950nm / C:AR 950-1250nm"},
    [{"partNumber": "LOBCXB6-10", "diameter": "6.00mm", "focalLength": "10.00mm", "centerThickness": "2.40mm", "edgeThickness": "1.50mm", "backFocalLength": "9.17mm"},
     {"partNumber": "LOBCXB12.7-25", "diameter": "12.70mm", "focalLength": "25.00mm", "centerThickness": "3.43mm", "edgeThickness": "1.80mm", "backFocalLength": "23.84mm"},
     {"partNumber": "LOBCXB25.4-50", "diameter": "25.40mm", "focalLength": "50.00mm", "centerThickness": "5.24mm", "edgeThickness": "2.00mm", "backFocalLength": "48.24mm"},
     {"partNumber": "LOBCXB25.4-100", "diameter": "25.40mm", "focalLength": "100.00mm", "centerThickness": "3.58mm", "edgeThickness": "2.00mm", "backFocalLength": "98.81mm"},
     {"partNumber": "LOBCXB25.4-200", "diameter": "25.40mm", "focalLength": "200.00mm", "centerThickness": "2.79mm", "edgeThickness": "2.00mm", "backFocalLength": "199.06mm"},
     {"partNumber": "LOBCXB50-100", "diameter": "50.00mm", "focalLength": "100.00mm", "centerThickness": "9.10mm", "edgeThickness": "3.00mm", "backFocalLength": "98.50mm"}]
)

add(3, "BK7 Plano-Concave Lenses", "K9平凹球面透镜",
    "Optical Lenses", "光学透镜",
    "Plano-concave lenses have a negative focal length. Parallel light beams passing through a plano-concave lens will diverge. Made from H-K9L(BK7) with high uniformity, free of streaks, impurities and bubbles.",
    "平凹透镜的焦距是负焦距，平行光束通过平凹透镜后会呈发散状。采用H-K9L(BK7)材料，均匀性好，无纹理、杂质、气泡。",
    "bk7-plano-concave", "optical-lenses",
    {"material": "H-K9L(BK7)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "A:AR 350-650nm / B:AR 650-950nm / C:AR 950-1250nm"},
    [{"partNumber": "LOPCCB6-10", "diameter": "6.00mm", "focalLength": "-10.00mm", "centerThickness": "2.00mm", "edgeThickness": "2.90mm", "backFocalLength": "-11.30mm"},
     {"partNumber": "LOPCCB12.7-25.4", "diameter": "12.70mm", "focalLength": "-25.40mm", "centerThickness": "3.00mm", "edgeThickness": "4.90mm", "backFocalLength": "-27.20mm"},
     {"partNumber": "LOPCCB25.4-50", "diameter": "25.40mm", "focalLength": "-50.00mm", "centerThickness": "2.50mm", "edgeThickness": "5.84mm", "backFocalLength": "-51.65mm"},
     {"partNumber": "LOPCCB25.4-100", "diameter": "25.40mm", "focalLength": "-100.00mm", "centerThickness": "2.50mm", "edgeThickness": "4.08mm", "backFocalLength": "-101.65mm"},
     {"partNumber": "LOPCCB50.8-100", "diameter": "50.80mm", "focalLength": "-100.00mm", "centerThickness": "2.50mm", "edgeThickness": "9.17mm", "backFocalLength": "-101.65mm"}]
)

add(4, "BK7 Bi-Concave Lenses", "K9双凹球面透镜",
    "Optical Lenses", "光学透镜",
    "Bi-concave lenses have a negative focal length, mainly used for diverging parallel light and forming virtual images. Available in multiple specifications from H-K9L(BK7) material.",
    "双凹透镜具有负焦距，主要用于发散平行光并形成虚像。采用H-K9L(BK7)材料，可提供多种规格。",
    "bk7-bi-concave", "optical-lenses",
    {"material": "H-K9L(BK7)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "A:AR 350-650nm / B:AR 650-950nm / C:AR 950-1250nm"},
    [{"partNumber": "LOBCCB12.7-20", "diameter": "12.70mm", "focalLength": "-20.00mm", "centerThickness": "2.00mm", "edgeThickness": "3.97mm", "backFocalLength": "-20.65mm"},
     {"partNumber": "LOBCCB12.7-50", "diameter": "12.70mm", "focalLength": "-50.00mm", "centerThickness": "3.50mm", "edgeThickness": "4.30mm", "backFocalLength": "-52.10mm"},
     {"partNumber": "LOBCCB25.4-100", "diameter": "25.40mm", "focalLength": "-100.00mm", "centerThickness": "4.00mm", "edgeThickness": "5.60mm", "backFocalLength": "-101.31mm"},
     {"partNumber": "LOBCCB50.8-200", "diameter": "50.80mm", "focalLength": "-200.00mm", "centerThickness": "2.50mm", "edgeThickness": "5.63mm", "backFocalLength": "-200.83mm"}]
)

add(5, "BK7 Positive Meniscus Lenses", "K9正弯月球面透镜",
    "Optical Lenses", "光学透镜",
    "Positive meniscus lenses are convex-concave lenses that are thicker at the center than at the edge. They are generally used to reduce spherical aberration. When combined with other lenses, they can reduce the focal length of the system and increase the numerical aperture.",
    "正弯月透镜是一种中间比边缘厚的凸凹透镜。正弯月透镜一般用来减小球差，当和其他的透镜组合时，可以减小系统的焦距，并且扩大数值孔径。",
    "bk7-positive-meniscus", "optical-lenses",
    {"material": "K9(BK7)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "A:AR 350-650nm / B:AR 650-950nm / C:AR 950-1250nm"},
    [{"partNumber": "LOPM25.4-100", "diameter": "25.40mm", "focalLength": "100.00mm", "centerThickness": "3.60mm", "edgeThickness": "2.00mm", "backFocalLength": "96.19mm"},
     {"partNumber": "LOPM25.4-200", "diameter": "25.40mm", "focalLength": "200.00mm", "centerThickness": "2.80mm", "edgeThickness": "2.00mm", "backFocalLength": "197.12mm"},
     {"partNumber": "LOPM50.8-150", "diameter": "50.80mm", "focalLength": "150.00mm", "centerThickness": "7.30mm", "edgeThickness": "2.70mm", "backFocalLength": "142.23mm"},
     {"partNumber": "LOPM50.8-300", "diameter": "50.80mm", "focalLength": "300.00mm", "centerThickness": "5.10mm", "edgeThickness": "3.00mm", "backFocalLength": "294.80mm"},
     {"partNumber": "LOPM50.8-1000", "diameter": "50.80mm", "focalLength": "1000.00mm", "centerThickness": "5.00mm", "edgeThickness": "4.40mm", "backFocalLength": "995.42mm"}]
)

add(6, "BK7 Negative Meniscus Lenses", "K9负弯月球面透镜",
    "Optical Lenses", "光学透镜",
    "Negative meniscus lenses are convex-concave lenses that are thinner at the center than at the edge. They can reduce spherical aberration and, when combined with other lenses, can reduce the numerical aperture of the system.",
    "负弯月透镜是一种中间比边缘薄的凸凹透镜，负弯月透镜可以减小球差，负弯月透镜和其他的透镜组合可以降低系统的数值孔径。",
    "bk7-negative-meniscus", "optical-lenses",
    {"material": "H-K9L(BK7)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "A:AR 350-650nm / B:AR 650-950nm / C:AR 950-1250nm"},
    [{"partNumber": "LONM25.4-100", "diameter": "25.40mm", "focalLength": "-100.00mm", "centerThickness": "3.00mm", "edgeThickness": "4.70mm", "backFocalLength": "-98.79mm"},
     {"partNumber": "LONM25.4-200", "diameter": "25.40mm", "focalLength": "-200.00mm", "centerThickness": "3.00mm", "edgeThickness": "3.80mm", "backFocalLength": "-197.82mm"},
     {"partNumber": "LONM25.4-500", "diameter": "25.40mm", "focalLength": "-500.00mm", "centerThickness": "3.00mm", "edgeThickness": "3.30mm", "backFocalLength": "-496.94mm"},
     {"partNumber": "LONM25.4-1000", "diameter": "25.40mm", "focalLength": "-1000.00mm", "centerThickness": "3.00mm", "edgeThickness": "3.20mm", "backFocalLength": "-995.30mm"}]
)

add(7, "UV Fused Silica Plano-Convex Lenses", "紫外融石英平凸透镜",
    "Optical Lenses", "光学透镜",
    "UV fused silica plano-convex lenses offer high transmittance in the 195nm-2100nm wavelength range. The ideal choice for UV band applications. Custom coating designs available.",
    "紫外融石英透镜在195nm-2100nm波段范围有较高的透过率，如需用在紫外波段的透镜，紫外融石英透镜是较好的选择。支持定制镀膜。",
    "uv-fused-silica-plano-convex", "optical-lenses",
    {"material": "UV Fused Silica(JGS1)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "Custom Design"},
    [{"partNumber": "LOPCXF10-15", "diameter": "10.00mm", "focalLength": "15.00mm", "centerThickness": "4.10mm", "edgeThickness": "2.00mm", "backFocalLength": "12.20mm"},
     {"partNumber": "LOPCXF25.4-50", "diameter": "25.40mm", "focalLength": "50.00mm", "centerThickness": "5.70mm", "edgeThickness": "1.90mm", "backFocalLength": "46.10mm"},
     {"partNumber": "LOPCXF25.4-100", "diameter": "25.40mm", "focalLength": "100.00mm", "centerThickness": "3.70mm", "edgeThickness": "1.90mm", "backFocalLength": "97.50mm"},
     {"partNumber": "LOPCXF50.8-100", "diameter": "50.80mm", "focalLength": "100.00mm", "centerThickness": "10.70mm", "edgeThickness": "3.00mm", "backFocalLength": "92.66mm"},
     {"partNumber": "LOPCXF50.8-200", "diameter": "50.80mm", "focalLength": "200.00mm", "centerThickness": "6.60mm", "edgeThickness": "3.00mm", "backFocalLength": "195.47mm"}]
)

add(8, "UV Fused Silica Bi-Convex Lenses", "紫外融石英双凸透镜",
    "Optical Lenses", "光学透镜",
    "UV fused silica bi-convex lenses provide high transmittance in the 195-2100nm range. Compared to BK7, UV fused silica offers superior UV band performance. Custom coating designs available.",
    "紫外融石英在195-2100nm波段范围的透过率比较高，相比于K9材料，石英材料可在紫外波段有较高的透过率。支持定制镀膜。",
    "uv-fused-silica-bi-convex", "optical-lenses",
    {"material": "UV Fused Silica(JGS1)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "Custom Design"},
    [{"partNumber": "LOBCXF6-10", "diameter": "6.00mm", "focalLength": "10.00mm", "centerThickness": "2.60mm", "edgeThickness": "1.50mm", "backFocalLength": "9.05mm"},
     {"partNumber": "LOBCXF12.7-30", "diameter": "12.70mm", "focalLength": "30.00mm", "centerThickness": "3.30mm", "edgeThickness": "1.80mm", "backFocalLength": "28.85mm"},
     {"partNumber": "LOBCXF25.4-50", "diameter": "25.40mm", "focalLength": "50.00mm", "centerThickness": "5.70mm", "edgeThickness": "2.00mm", "backFocalLength": "48.01mm"},
     {"partNumber": "LOBCXF25.4-100", "diameter": "25.40mm", "focalLength": "100.00mm", "centerThickness": "3.80mm", "edgeThickness": "2.00mm", "backFocalLength": "98.69mm"},
     {"partNumber": "LOBCXF50.8-100", "diameter": "50.80mm", "focalLength": "100.00mm", "centerThickness": "4.80mm", "edgeThickness": "2.00mm", "backFocalLength": "98.40mm"}]
)

add(9, "UV Fused Silica Plano-Concave Lenses", "紫外融石英平凹透镜",
    "Optical Lenses", "光学透镜",
    "UV fused silica plano-concave lenses offer high transmittance in the 195-2100nm range with a negative focal length for beam divergence. Custom coating designs available.",
    "紫外融石英平凹透镜在195-2100nm波段范围透过率高，具有负焦距，用于光束发散。支持定制镀膜。",
    "uv-fused-silica-plano-concave", "optical-lenses",
    {"material": "UV Fused Silica(JGS1)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "Custom Design"},
    [{"partNumber": "LOPCCF12.7-25.4", "diameter": "12.70mm", "focalLength": "-25.40mm", "centerThickness": "3.00mm", "edgeThickness": "4.90mm", "backFocalLength": "-27.20mm"},
     {"partNumber": "LOPCCF25.4-50", "diameter": "25.40mm", "focalLength": "-50.00mm", "centerThickness": "2.50mm", "edgeThickness": "5.55mm", "backFocalLength": "-51.71mm"},
     {"partNumber": "LOPCCF25.4-100", "diameter": "25.40mm", "focalLength": "-100.00mm", "centerThickness": "2.50mm", "edgeThickness": "4.29mm", "backFocalLength": "-103.72mm"},
     {"partNumber": "LOPCCF50.8-100", "diameter": "50.80mm", "focalLength": "-100.00mm", "centerThickness": "2.50mm", "edgeThickness": "8.60mm", "backFocalLength": "-101.71mm"}]
)

add(10, "UV Fused Silica Bi-Concave Lenses", "紫外融石英双凹透镜",
    "Optical Lenses", "光学透镜",
    "UV fused silica bi-concave lenses provide high transmittance in the 195-2100nm range with a negative focal length for beam divergence. Custom coating designs available.",
    "紫外融石英双凹透镜在195-2100nm波段范围透过率高，具有负焦距，用于光束发散。支持定制镀膜。",
    "uv-fused-silica-bi-concave", "optical-lenses",
    {"material": "UV Fused Silica(JGS1)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "Custom Design"},
    [{"partNumber": "LOBCCF12.7-25", "diameter": "12.70mm", "focalLength": "-25.00mm", "centerThickness": "2.00mm", "edgeThickness": "3.76mm", "backFocalLength": "-25.68mm"},
     {"partNumber": "LOBCCF25.4-50", "diameter": "25.40mm", "focalLength": "-50.00mm", "centerThickness": "2.00mm", "edgeThickness": "5.55mm", "backFocalLength": "-50.68mm"},
     {"partNumber": "LOBCCF25.4-100", "diameter": "25.40mm", "focalLength": "-100.00mm", "centerThickness": "2.00mm", "edgeThickness": "3.76mm", "backFocalLength": "-100.68mm"},
     {"partNumber": "LOBCCF50-100", "diameter": "50.00mm", "focalLength": "-100.00mm", "centerThickness": "3.00mm", "edgeThickness": "5.50mm", "backFocalLength": "-101.00mm"}]
)

# Cylindrical lenses
add(11, "BK7 Plano-Convex Cylindrical Lenses", "K9平凸柱透镜",
    "Optical Lenses", "光学透镜",
    "Plano-convex cylindrical lenses are mainly used for linear imaging and single-axis magnification over a wide range. They can focus laser beams or converge them into sheet beams, and also focus into a long thin line to illuminate distant targets.",
    "平凸柱透镜主要用于线性成像以及宽范围内单轴放大，可用于激光的汇聚，或汇聚成片状光束，还可汇聚为细长线照射远方。",
    "bk7-plano-convex-cylindrical", "optical-lenses",
    {"material": "H-K9L(BK7)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "A:AR 350-650nm / B:AR 650-950nm / C:AR 950-1250nm"},
    [{"partNumber": "LOCPCXB12-12.7", "width": "10.00mm", "length": "12.00mm", "focalLength": "12.70mm", "curvatureRadius": "6.56mm", "centerThickness": "4.31mm", "edgeThickness": "2.00mm"},
     {"partNumber": "LOCPCXB22-25", "width": "20.00mm", "length": "22.00mm", "focalLength": "25.00mm", "curvatureRadius": "12.92mm", "centerThickness": "6.74mm", "edgeThickness": "2.00mm"},
     {"partNumber": "LOCPCXB22-50", "width": "20.00mm", "length": "22.00mm", "focalLength": "50.00mm", "curvatureRadius": "25.84mm", "centerThickness": "4.01mm", "edgeThickness": "2.00mm"},
     {"partNumber": "LOCPCXB32-100", "width": "30.00mm", "length": "32.00mm", "focalLength": "100.00mm", "curvatureRadius": "51.68mm", "centerThickness": "5.22mm", "edgeThickness": "3.00mm"}]
)

add(12, "BK7 Plano-Concave Cylindrical Lenses", "K9平凹柱透镜",
    "Optical Lenses", "光学透镜",
    "Plano-concave cylindrical lenses have a negative effective focal length. They can diverge light in one dimension and can be combined with plano-convex cylindrical lenses for beam expansion applications.",
    "平凹柱透镜的有效焦距是负的，平凹柱透镜可以把光发散到一个维度，可以和平凸柱透镜结合起来进行光束的扩束应用。",
    "bk7-plano-concave-cylindrical", "optical-lenses",
    {"material": "H-K9L(BK7)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "A:AR 350-650nm / B:AR 650-950nm / C:AR 950-1250nm"},
    [{"partNumber": "LOCPCCB12-12.7", "width": "10.00mm", "length": "12.00mm", "focalLength": "-12.70mm", "curvatureRadius": "-6.56mm", "centerThickness": "2.00mm", "edgeThickness": "3.80mm"},
     {"partNumber": "LOCPCCB22-30", "width": "20.00mm", "length": "22.00mm", "focalLength": "-30.00mm", "curvatureRadius": "-15.50mm", "centerThickness": "2.00mm", "edgeThickness": "5.30mm"},
     {"partNumber": "LOCPCCB32-50", "width": "30.00mm", "length": "32.00mm", "focalLength": "-50.00mm", "curvatureRadius": "-25.84mm", "centerThickness": "2.00mm", "edgeThickness": "6.50mm"},
     {"partNumber": "LOCPCCB32-100", "width": "30.00mm", "length": "32.00mm", "focalLength": "-100.00mm", "curvatureRadius": "-51.68mm", "centerThickness": "3.00mm", "edgeThickness": "5.10mm"}]
)

add(13, "UV Fused Silica Plano-Convex Cylindrical Lenses", "紫外融石英平凸柱透镜",
    "Optical Lenses", "光学透镜",
    "UV fused silica plano-convex cylindrical lenses offer high transmittance in the 195nm-2100nm wavelength range, ideal for UV band applications. Custom coating designs available.",
    "紫外融石英平凸柱透镜在195nm-2100nm波长范围内有较高的透过率，是紫外波段的优选。支持定制镀膜。",
    "uv-fused-silica-plano-convex-cylindrical", "optical-lenses",
    {"material": "UV Fused Silica(JGS1)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "Custom Design"},
    [{"partNumber": "LOCPCXS14-10", "focalLength": "10.00mm", "width": "9.00mm", "length": "14.00mm", "curvatureRadius": "4.58mm", "centerThickness": "5.60mm", "edgeThickness": "2.00mm"},
     {"partNumber": "LOCPCXS22-25", "focalLength": "25.00mm", "width": "20.00mm", "length": "22.00mm", "curvatureRadius": "12.97mm", "centerThickness": "6.70mm", "edgeThickness": "2.00mm"},
     {"partNumber": "LOCPCXS35-25.4", "focalLength": "25.40mm", "width": "23.00mm", "length": "35.00mm", "curvatureRadius": "11.65mm", "centerThickness": "11.60mm", "edgeThickness": "2.00mm"},
     {"partNumber": "LOCPCXS30-75", "focalLength": "75.00mm", "width": "20.00mm", "length": "30.00mm", "curvatureRadius": "34.38mm", "centerThickness": "3.50mm", "edgeThickness": "2.00mm"}]
)

add(14, "UV Fused Silica Plano-Concave Cylindrical Lenses", "紫外融石英平凹柱透镜",
    "Optical Lenses", "光学透镜",
    "UV fused silica plano-concave cylindrical lenses offer high transmittance in the 195nm-2100nm wavelength range with a negative focal length. Multiple sizes available, custom orders accepted.",
    "紫外融石英平凹柱透镜在195nm-2100nm波长范围内透过率高，具有负焦距。可提供多种尺寸规格，接受订制。",
    "uv-fused-silica-plano-concave-cylindrical", "optical-lenses",
    {"material": "UV Fused Silica(JGS1)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "Custom Design"},
    [{"partNumber": "LOCPCCS15-12.7", "focalLength": "-12.70mm", "width": "10.00mm", "length": "15.00mm", "curvatureRadius": "-5.82mm", "centerThickness": "4.80mm", "edgeThickness": "2.00mm"},
     {"partNumber": "LOCPCCS30-25", "focalLength": "-25.00mm", "width": "20.00mm", "length": "30.00mm", "curvatureRadius": "-11.46mm", "centerThickness": "7.80mm", "edgeThickness": "2.00mm"},
     {"partNumber": "LOCPCCS33-25.4", "focalLength": "-25.40mm", "width": "22.00mm", "length": "33.00mm", "curvatureRadius": "-11.65mm", "centerThickness": "9.70mm", "edgeThickness": "2.00mm"}]
)

add(15, "Achromatic Doublet Lenses", "消色差双胶合透镜",
    "Optical Lenses", "光学透镜",
    "Achromatic doublet lenses are made by cementing a low-dispersion crown glass positive lens with a high-dispersion flint glass negative lens. Compared to single lenses, achromatic doublets have much smaller spherical aberration. Minimum spherical aberration when used at infinite conjugation.",
    "消色差双胶合透镜是一种把低分散的冕牌玻璃正透镜和高分散的火石玻璃负透镜粘接而成的消色差透镜。和单个透镜相比，消色差双胶合透镜的球差要小得多。使用于无限共轭状态时，其球差最小。",
    "achromatic-doublet", "optical-lenses",
    {"material": "K9/ZF2", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "A:AR 350-650nm / B:AR 650-950nm / C:AR 950-1250nm"},
    [{"partNumber": "LOADL12.7-50", "diameter": "12.70mm", "focalLength": "50.00mm", "centerThickness": "4.40mm", "edgeThickness": "3.79mm", "backFocalLength": "48.00mm"},
     {"partNumber": "LOADL25-100", "diameter": "25.00mm", "focalLength": "100.00mm", "centerThickness": "8.50mm", "edgeThickness": "6.61mm", "backFocalLength": "81.21mm"},
     {"partNumber": "LOADL25.4-100", "diameter": "25.40mm", "focalLength": "100.00mm", "centerThickness": "6.50mm", "edgeThickness": "4.70mm", "backFocalLength": "97.10mm"},
     {"partNumber": "LOADL50.8-200", "diameter": "50.80mm", "focalLength": "200.00mm", "centerThickness": "10.50mm", "edgeThickness": "6.70mm", "backFocalLength": "193.70mm"},
     {"partNumber": "LOADL50.8-500", "diameter": "50.80mm", "focalLength": "500.00mm", "centerThickness": "7.00mm", "edgeThickness": "5.50mm", "backFocalLength": "495.80mm"}]
)

add(16, "BK7 C-Lenses", "K9 C-透镜",
    "Optical Lenses", "光学透镜",
    "C-lenses are mainly used for fiber optic beam collimation, isolation, conversion, and other laser applications. Compared to other lenses, C-lenses offer lower cost, lower insertion loss at long working distances, and wider working range.",
    "C透镜主要用于光纤的光束准直，隔离，转换，以及其他激光应用，相较于其他的透镜，C透镜的价格比较低，在长工作距离有较低的插入损失，比较宽的工作范围等优势。",
    "bk7-c-lenses", "optical-lenses",
    {"material": "K9(BK7)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "focalLengthTolerance": "±1%", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "A:AR 350-650nm / B:AR 650-950nm / C:AR 950-1250nm"},
    [{"partNumber": "LOCL05", "diameter": "1.00mm", "length": "2.90mm", "wedgeAngle": "8°", "wavelength": "1550nm", "workingDistance": "68mm"},
     {"partNumber": "LOCL09", "diameter": "1.00mm", "length": "1.92mm", "wedgeAngle": "8°", "wavelength": "1550nm", "workingDistance": "10mm"},
     {"partNumber": "LOCL15", "diameter": "1.80mm", "length": "2.98mm", "wedgeAngle": "8°", "wavelength": "1550nm", "workingDistance": "67mm"},
     {"partNumber": "LOCL20", "diameter": "1.80mm", "length": "3.85mm", "wedgeAngle": "8°", "wavelength": "1550nm", "workingDistance": "100mm"}]
)

add(17, "BK7 Ball Lenses", "K9球透镜",
    "Optical Lenses", "光学透镜",
    "Ball lenses are mainly used for laser collimation, focusing, laser-to-fiber coupling, fiber-to-fiber coupling, and fiber-to-detector coupling. Made from H-K9L(BK7) optical glass.",
    "球透镜主要应用于激光准直、聚焦，激光和光纤耦合，光纤与光纤耦合，光纤和检测器耦合。采用H-K9L(BK7)光学玻璃。",
    "bk7-ball-lenses", "optical-lenses",
    {"material": "H-K9L(BK7)", "diameterTolerance": "±0.15mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%"},
    [{"partNumber": "LOBL1", "diameter": "1.00mm"}, {"partNumber": "LOBL2.0", "diameter": "2.00mm"}, {"partNumber": "LOBL3.0", "diameter": "3.00mm"}, {"partNumber": "LOBL5.0", "diameter": "5.00mm"}, {"partNumber": "LOBL10.0", "diameter": "10.00mm"}, {"partNumber": "LOBL15.0", "diameter": "15.00mm"}]
)

add(18, "UV Fused Silica Ball Lenses", "UV熔融石英球透镜",
    "Optical Lenses", "光学透镜",
    "UV fused silica ball lenses offer superior transmittance from UV to near-IR (185-2500nm). Ideal for fiber optic coupling, endoscopy, and laser diode collimation. Low thermal expansion coefficient ensures stability in demanding environments.",
    "UV熔融石英球透镜在紫外到近红外波段(185-2500nm)具有卓越的透过率。适用于光纤耦合、内窥镜和激光二极管准直。低热膨胀系数确保在苛刻环境中的稳定性。",
    "uv-fused-silica-ball-lenses", "optical-lenses",
    {"material": "UV Fused Silica(JGS1)", "diameterTolerance": "±0.15mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%"},
    [{"partNumber": "LOBS1", "diameter": "1.00mm"}, {"partNumber": "LOBS2.0", "diameter": "2.00mm"}, {"partNumber": "LOBS3.0", "diameter": "3.00mm"}, {"partNumber": "LOBS5.0", "diameter": "5.00mm"}, {"partNumber": "LOBS10.0", "diameter": "10.00mm"}]
)

add(19, "BK7 Rod Lenses", "K9棒镜",
    "Optical Lenses", "光学透镜",
    "Rod lenses are mainly used to focus a light spot into a line spot. After both ends of a rod lens are polished, it can also be used as a light guide rod. Multiple sizes available from H-K9L(BK7) material.",
    "棒镜主要用于将光斑聚焦成一个线光斑，将棒镜的两端抛光后，也可以作为导光棒。采用H-K9L(BK7)材料，可提供多种尺寸。",
    "bk7-rod-lenses", "optical-lenses",
    {"material": "H-K9L(BK7)", "diameterTolerance": "±0.15mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%"},
    [{"partNumber": "LORL3-10", "diameter": "3.00mm", "length": "10.00mm"}, {"partNumber": "LORL5-10", "diameter": "5.00mm", "length": "10.00mm"}, {"partNumber": "LORL6-15", "diameter": "6.00mm", "length": "15.00mm"}, {"partNumber": "LORL10-20", "diameter": "10.00mm", "length": "20.00mm"}, {"partNumber": "LORL15-20", "diameter": "15.00mm", "length": "20.00mm"}]
)

add(20, "UV Fused Silica Rod Lenses", "UV熔融石英棒镜",
    "Optical Lenses", "光学透镜",
    "UV fused silica rod lenses offer excellent UV transmittance (185-2500nm) for laser collimation and fiber coupling in UV applications. Multiple sizes available, custom orders accepted.",
    "UV熔融石英棒镜在紫外到近红外波段(185-2500nm)具有卓越的透过率，适用于紫外应用的激光准直和光纤耦合。可提供多种尺寸，接受订制。",
    "uv-fused-silica-rod-lenses", "optical-lenses",
    {"material": "UV Fused Silica(JGS1)", "diameterTolerance": "±0.15mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%"},
    [{"partNumber": "LORS3-10", "diameter": "3.00mm", "length": "10.00mm"}, {"partNumber": "LORS5-10", "diameter": "5.00mm", "length": "10.00mm"}, {"partNumber": "LORS6-15", "diameter": "6.00mm", "length": "15.00mm"}, {"partNumber": "LORS10-20", "diameter": "10.00mm", "length": "20.00mm"}]
)

add(21, "Aspherical Lenses", "非球面透镜",
    "Optical Lenses", "光学透镜",
    "Aspherical lenses have non-spherical surfaces. We provide aspherical lenses in various sizes, focal lengths, and materials. Custom orders are also accepted.",
    "非球面透镜的面是非球面的，我们可提供多种尺寸，焦距，材料的非球面透镜，同时也接受订制。",
    "aspherical-lenses", "optical-lenses",
    {"diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<3 arc min", "clearAperture": ">90%", "beveling": "0.25mm×45°", "coatings": "A:AR 350-650nm / B:AR 650-950nm / C:AR 950-1250nm"},
    [{"partNumber": "LOAL12-8.5", "diameter": "12.00mm", "focalLength": "8.50mm", "backFocalLength": "5.80mm", "centerThickness": "5.50mm", "edgeThickness": "1.60mm", "material": "B270"},
     {"partNumber": "LOAL25-20.0", "diameter": "25.00mm", "focalLength": "20.00mm", "backFocalLength": "15.10mm", "centerThickness": "7.50mm", "edgeThickness": "1.20mm", "material": "B270"},
     {"partNumber": "LOAL50-39.0", "diameter": "50.00mm", "focalLength": "39.00mm", "backFocalLength": "24.90mm", "centerThickness": "20.50mm", "edgeThickness": "2.80mm", "material": "B270"}]
)

add(22, "Laser Beam Expanders", "激光扩束镜",
    "Optical Lenses", "光学透镜",
    "Laser beam expanders are designed to expand or reduce the diameter of laser beams while maintaining beam quality. Available in various expansion ratios and wavelength ranges.",
    "激光扩束镜用于扩展或缩小激光束的直径，同时保持光束质量。提供多种扩束比和波长范围。",
    "laser-beam-expanders", "optical-lenses",
    {"wavelengthRange": "Custom Design", "expansionRatio": "2X-10X", "maxInputSpot": "Custom Design", "maxOutputSpot": "Custom Design"},
    [{"partNumber": "LOBEX-2X", "expansionRatio": "2X"}, {"partNumber": "LOBEX-3X", "expansionRatio": "3X"}, {"partNumber": "LOBEX-5X", "expansionRatio": "5X"}, {"partNumber": "LOBEX-10X", "expansionRatio": "10X"}]
)

add(23, "Microscope Objectives", "显微物镜",
    "Optical Lenses", "光学透镜",
    "Microscope objectives are precision optical components designed for high-resolution microscopy. Available in various magnifications and numerical apertures.",
    "显微物镜是为高分辨率显微镜设计的精密光学元件。提供多种放大倍率和数值孔径。",
    "microscope-objectives", "optical-lenses",
    {"magnification": "5X-60X", "numericalAperture": "0.1-0.85", "parfocalDistance": "Custom Design", "conjugateFocalDistance": "Custom Design"},
    [{"partNumber": "LOMO-5X", "magnification": "5X", "na": "0.10"}, {"partNumber": "LOMO-10X", "magnification": "10X", "na": "0.25"}, {"partNumber": "LOMO-20X", "magnification": "20X", "na": "0.40"}, {"partNumber": "LOMO-40X", "magnification": "40X", "na": "0.65"}, {"partNumber": "LOMO-60X", "magnification": "60X", "na": "0.85"}]
)

# Save to file - Part 1 complete, will append remaining products
print("Part 1: {} products generated (Optical Lenses: 23)".format(len(products)))

# Save intermediate data
with open("/tmp/v34_products_part1.json", "w") as f:
    json.dump(products, f, ensure_ascii=False)

# ========== 2. Optical Windows (7) ==========
add(24, "BK7 Windows", "K9窗口",
    "Optical Windows", "光学窗口",
    "BK7 optical windows provide high transmittance in the 330nm-2100nm wavelength range. With AR coating, transmittance can exceed 99.5%. Ideal for visible and near-IR applications.",
    "K9材料的窗口在330nm-2100nm的波段范围内有较高的透过率，该窗口镀上增透膜后，透过率可以在99.5%以上。",
    "bk7-windows", "optical-windows",
    {"material": "H-K9L(BK7)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "parallelism": "<1 arc min", "coatings": "A:AR 350-650nm / B:AR 650-950nm / C:AR 950-1250nm"},
    [{"partNumber": "LOWB12.7-3", "diameter": "12.70mm", "thickness": "3.00mm"}, {"partNumber": "LOWB25.4-3", "diameter": "25.40mm", "thickness": "3.00mm"}, {"partNumber": "LOWB25.4-5", "diameter": "25.40mm", "thickness": "5.00mm"}, {"partNumber": "LOWB50.8-5", "diameter": "50.80mm", "thickness": "5.00mm"}]
)

add(25, "UV Fused Silica Windows", "紫外融石英窗口",
    "Optical Windows", "光学窗口",
    "UV fused silica windows offer high transmittance in the 185-2500nm wavelength range, ideal for UV and high-power laser applications. Custom coating designs available.",
    "紫外融石英窗口在185-2500nm波段范围透过率高，适用于紫外和高功率激光应用。支持定制镀膜。",
    "uv-fused-silica-windows", "optical-windows",
    {"material": "UV Fused Silica(JGS1)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "parallelism": "<1 arc min", "coatings": "Custom Design"},
    [{"partNumber": "LOWS12.7-3", "diameter": "12.70mm", "thickness": "3.00mm"}, {"partNumber": "LOWS25.4-3", "diameter": "25.40mm", "thickness": "3.00mm"}, {"partNumber": "LOWS50.8-5", "diameter": "50.80mm", "thickness": "5.00mm"}]
)

add(26, "Sapphire Windows", "蓝宝石窗口",
    "Optical Windows", "光学窗口",
    "Sapphire windows feature extreme hardness and wide optical transmission from UV (190nm) to mid-IR. High acoustic velocity, high temperature resistance, corrosion resistance, and high transparency. Custom coating designs available.",
    "蓝宝石窗口具有极高硬度，光学穿透带宽从近紫外(190nm)到中红外。高声速、耐高温、抗腐蚀、高透光性。支持定制镀膜。",
    "sapphire-windows", "optical-windows",
    {"material": "Al2O3 (Sapphire)", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "parallelism": "<1 arc min", "coatings": "Custom Design"},
    [{"partNumber": "LOWSA12.7-2", "diameter": "12.70mm", "thickness": "2.00mm"}, {"partNumber": "LOWSA25.4-3", "diameter": "25.40mm", "thickness": "3.00mm"}, {"partNumber": "LOWSA50.8-5", "diameter": "50.80mm", "thickness": "5.00mm"}]
)

add(27, "CaF2 Windows", "氟化钙窗口",
    "Optical Windows", "光学窗口",
    "Calcium fluoride windows offer excellent transmittance in UV, visible, and IR wavelength ranges. Widely used in laser, IR optics, UV optics, and high-energy detector applications. Custom coating designs available.",
    "氟化钙窗口在紫外、可见光、红外波段有良好的透过率。广泛应用于激光、红外光学、紫外光学和高能探测器等领域。支持定制镀膜。",
    "caf2-windows", "optical-windows",
    {"material": "CaF2", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "80-50", "surfaceFlatness": "λ/2@632.8nm", "clearAperture": ">90%", "parallelism": "<1 arc min", "coatings": "Custom Design"},
    [{"partNumber": "LOWC12.7-3", "diameter": "12.70mm", "thickness": "3.00mm"}, {"partNumber": "LOWC25.4-3", "diameter": "25.40mm", "thickness": "3.00mm"}, {"partNumber": "LOWC50.8-5", "diameter": "50.80mm", "thickness": "5.00mm"}]
)

add(28, "Germanium Windows", "锗窗口",
    "Optical Windows", "光学窗口",
    "Germanium windows are commonly used in IR imaging systems and IR spectrometers. High hardness, good thermal conductivity, insoluble in water. Custom coating designs available.",
    "锗窗口是一种非常常用的红外光学材料，具有硬度高，导热性好，不溶于水等特点，广泛用于红外成像系统和红外光谱仪系统。支持定制镀膜。",
    "ge-windows", "optical-windows",
    {"material": "Ge", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "60-40", "surfaceFlatness": "λ/2@632.8nm", "clearAperture": ">80%", "parallelism": "<1 arc min", "coatings": "Custom Design"},
    [{"partNumber": "LOWG12.7-2", "diameter": "12.70mm", "thickness": "2.00mm"}, {"partNumber": "LOWG25.4-3", "diameter": "25.40mm", "thickness": "3.00mm"}, {"partNumber": "LOWG50.8-3", "diameter": "50.80mm", "thickness": "3.00mm"}]
)

add(29, "Silicon Windows", "硅窗口",
    "Optical Windows", "光学窗口",
    "Silicon windows have good transmittance in the 1-7μm wavelength range and also in the far-IR 50-300μm range. High hardness, insoluble in water. Custom coating designs available.",
    "硅窗口在1-7μm波段具有很好的透光性能，同时在远红外波段50-300μm也具有很好的透光性能。硬度高，不溶于水。支持定制镀膜。",
    "si-windows", "optical-windows",
    {"material": "Si", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "60-40", "surfaceFlatness": "λ/2@632.8nm", "clearAperture": ">80%", "parallelism": "<1 arc min", "coatings": "Custom Design"},
    [{"partNumber": "LOWSI12.7-2", "diameter": "12.70mm", "thickness": "2.00mm"}, {"partNumber": "LOWSI25.4-3", "diameter": "25.40mm", "thickness": "3.00mm"}, {"partNumber": "LOWSI50.8-3", "diameter": "50.80mm", "thickness": "3.00mm"}]
)

add(30, "ZnSe Windows", "硒化锌窗口",
    "Optical Windows", "光学窗口",
    "Zinc selenide windows are the preferred material for high-power CO2 laser optical components. Uniform refractive index makes them ideal for FLIR thermal imaging systems. Custom coating designs available.",
    "硒化锌窗口是高功率CO2激光光学元件的首选材料。折射率均匀和一致性好，是前视红外热成像系统中保护窗口和光学元件的理想材料。支持定制镀膜。",
    "znse-windows", "optical-windows",
    {"material": "ZnSe", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "60-40", "surfaceFlatness": "λ/2@632.8nm", "clearAperture": ">80%", "parallelism": "<1 arc min", "coatings": "Custom Design"},
    [{"partNumber": "LOWZ12.7-2", "diameter": "12.70mm", "thickness": "2.00mm"}, {"partNumber": "LOWZ25.4-3", "diameter": "25.40mm", "thickness": "3.00mm"}, {"partNumber": "LOWZ50.8-3", "diameter": "50.80mm", "thickness": "3.00mm"}]
)

# ========== 3. Optical Mirrors (7) ==========
add(31, "Laser Line High Reflected Mirrors", "激光线高反镜",
    "Optical Mirrors", "光学反射镜",
    "Laser line high reflected mirrors use dielectric coatings to achieve high reflectivity at specific laser wavelengths. Available for common laser wavelengths with high damage threshold.",
    "激光线高反镜采用介质膜在特定激光波长实现高反射率。适用于常见激光波长，具有高损伤阈值。",
    "laser-line-high-reflected-mirrors", "optical-mirrors",
    {"substrate": "BK7", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "centration": "<2 arc min", "clearAperture": ">90%"},
    [{"partNumber": "LOMLR12.7-3", "diameter": "12.70mm", "thickness": "3.00mm", "wavelength": "Custom Design"}, {"partNumber": "LOMLR25.4-4", "diameter": "25.40mm", "thickness": "4.00mm", "wavelength": "Custom Design"}, {"partNumber": "LOMLR50.8-6", "diameter": "50.80mm", "thickness": "6.00mm", "wavelength": "Custom Design"}]
)

add(32, "High Energy Laser Mirrors", "高功率激光反射镜",
    "Optical Mirrors", "光学反射镜",
    "High energy laser mirrors feature superior surface quality and flatness for high-power laser applications. High damage threshold dielectric coatings available.",
    "高功率激光反射镜具有优异的表面质量和面型精度，适用于高功率激光应用。提供高损伤阈值介质膜。",
    "high-energy-laser-mirrors", "optical-mirrors",
    {"substrate": "BK7", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "20-10", "surfaceFlatness": "λ/10@632.8nm", "clearAperture": ">90%"},
    [{"partNumber": "LOHEL12.7-3", "diameter": "12.70mm", "thickness": "3.00mm"}, {"partNumber": "LOHEL25.4-4", "diameter": "25.40mm", "thickness": "4.00mm"}, {"partNumber": "LOHEL50.8-6", "diameter": "50.80mm", "thickness": "6.00mm"}]
)

add(33, "Broadband Dielectric Mirrors", "宽带介质膜反射镜",
    "Optical Mirrors", "光学反射镜",
    "Broadband dielectric mirrors provide high reflectivity (>99%) over a wide wavelength range using multi-layer dielectric coatings. Suitable for various laser and imaging applications.",
    "宽带介质膜反射镜采用多层介质膜在宽波长范围内提供高反射率(>99%)。适用于各种激光和成像应用。",
    "broadband-dielectric-mirrors", "optical-mirrors",
    {"substrate": "BK7", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "20-10", "surfaceFlatness": "λ/10@632.8nm", "reflectivity": ">99%", "clearAperture": ">90%"},
    [{"partNumber": "LOBDM12.7-3", "diameter": "12.70mm", "thickness": "3.00mm"}, {"partNumber": "LOBDM25.4-4", "diameter": "25.40mm", "thickness": "4.00mm"}, {"partNumber": "LOBDM50.8-6", "diameter": "50.80mm", "thickness": "6.00mm"}]
)

add(34, "Protected Aluminum Mirrors", "保护铝膜反射镜",
    "Optical Mirrors", "光学反射镜",
    "Protected aluminum mirrors feature a durable aluminum coating with protective overcoat. R>85% reflectivity across visible and near-IR spectrum. Economical choice for general applications.",
    "保护铝膜反射镜采用耐久铝膜加保护层，在可见和近红外光谱范围R>85%反射率。通用应用的经济选择。",
    "protected-aluminum-mirrors", "optical-mirrors",
    {"substrate": "BK7", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "60-40", "surfaceFlatness": "λ/2@632.8nm", "clearAperture": ">90%", "coatings": "Protected Al R>85%"},
    [{"partNumber": "LOPAM12.7-3", "diameter": "12.70mm", "thickness": "3.00mm"}, {"partNumber": "LOPAM25.4-4", "diameter": "25.40mm", "thickness": "4.00mm"}, {"partNumber": "LOPAM50.8-6", "diameter": "50.80mm", "thickness": "6.00mm"}]
)

add(35, "Enhanced Aluminum Mirrors", "增强铝膜反射镜",
    "Optical Mirrors", "光学反射镜",
    "Enhanced aluminum mirrors feature a multi-layer enhanced aluminum coating for improved reflectivity. R>90% reflectivity with better performance than standard protected aluminum.",
    "增强铝膜反射镜采用多层增强铝膜，提高反射率。R>90%反射率，性能优于标准保护铝膜。",
    "enhanced-aluminum-mirrors", "optical-mirrors",
    {"substrate": "BK7", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "coatings": "Enhanced Al R>90%"},
    [{"partNumber": "LOEAM12.7-3", "diameter": "12.70mm", "thickness": "3.00mm"}, {"partNumber": "LOEAM25.4-4", "diameter": "25.40mm", "thickness": "4.00mm"}, {"partNumber": "LOEAM50.8-6", "diameter": "50.80mm", "thickness": "6.00mm"}]
)

add(36, "Protected Silver Mirrors", "保护银膜反射镜",
    "Optical Mirrors", "光学反射镜",
    "Protected silver mirrors offer high reflectivity (R>95%) across the visible to near-IR spectrum with a protective overcoat for durability. Excellent choice for broadband applications.",
    "保护银膜反射镜在可见到近红外光谱范围提供高反射率(R>95%)，带有保护层增强耐久性。宽带应用的优秀选择。",
    "protected-silver-mirrors", "optical-mirrors",
    {"substrate": "BK7", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "coatings": "Protected Ag R>95%"},
    [{"partNumber": "LOPSM12.7-3", "diameter": "12.70mm", "thickness": "3.00mm"}, {"partNumber": "LOPSM25.4-4", "diameter": "25.40mm", "thickness": "4.00mm"}, {"partNumber": "LOPSM50.8-6", "diameter": "50.80mm", "thickness": "6.00mm"}]
)

add(37, "Protected Gold Mirrors", "保护金膜反射镜",
    "Optical Mirrors", "光学反射镜",
    "Protected gold mirrors provide the highest reflectivity (R>98%) in the infrared spectrum. Ideal for IR laser and thermal imaging applications with a durable protective overcoat.",
    "保护金膜反射镜在红外光谱范围提供最高反射率(R>98%)。带有耐久保护层，是红外激光和热成像应用的理想选择。",
    "protected-gold-mirrors", "optical-mirrors",
    {"substrate": "BK7", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "coatings": "Protected Au R>98%"},
    [{"partNumber": "LOPGM12.7-3", "diameter": "12.70mm", "thickness": "3.00mm"}, {"partNumber": "LOPGM25.4-4", "diameter": "25.40mm", "thickness": "4.00mm"}, {"partNumber": "LOPGM50.8-6", "diameter": "50.80mm", "thickness": "6.00mm"}]
)

# ========== 4. Optical Prisms (7) ==========
add(38, "BK7 Right Angle Prisms", "BK7直角棱镜",
    "Optical Prisms", "光学棱镜",
    "Right angle prisms are used for redirecting light at 90 degrees or 180 degrees. Made from BK7 optical glass with precise angle control. Custom coating designs available.",
    "直角棱镜用于将光线偏转90度或180度。采用BK7光学玻璃，角度控制精确。支持定制镀膜。",
    "bk7-right-angle-prisms", "optical-prisms",
    {"material": "H-K9L(BK7)", "angleTolerance": "±10 arcsec", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "pyramidError": "<1 arcmin", "coatings": "Custom Design"},
    [{"partNumber": "LORAB5-5", "dimension": "5×5×5mm"}, {"partNumber": "LORAB10-10", "dimension": "10×10×10mm"}, {"partNumber": "LORAB15-15", "dimension": "15×15×15mm"}, {"partNumber": "LORAB25.4-25.4", "dimension": "25.4×25.4×25.4mm"}]
)

add(39, "UV Fused Silica Right Angle Prisms", "UV石英直角棱镜",
    "Optical Prisms", "光学棱镜",
    "UV fused silica right angle prisms offer high UV transmittance for applications requiring UV performance. Precise angle control with custom coating designs available.",
    "UV石英直角棱镜提供高紫外透过率，适用于需要紫外性能的应用。角度控制精确，支持定制镀膜。",
    "uv-fused-silica-right-angle-prisms", "optical-prisms",
    {"material": "UV Fused Silica(JGS1)", "angleTolerance": "±10 arcsec", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "pyramidError": "<1 arcmin", "coatings": "Custom Design"},
    [{"partNumber": "LORAU5-5", "dimension": "5×5×5mm"}, {"partNumber": "LORAU10-10", "dimension": "10×10×10mm"}, {"partNumber": "LORAU25.4-25.4", "dimension": "25.4×25.4×25.4mm"}]
)

add(40, "Penta Prisms", "五角棱镜",
    "Optical Prisms", "光学棱镜",
    "Penta prisms deviate light by 90 degrees without inverting or reversing the image. The deviation angle remains constant regardless of the prism orientation. Custom coating designs available.",
    "五角棱镜将光线偏转90度而不倒像或反转图像。偏转角不受棱镜方向影响。支持定制镀膜。",
    "penta-prisms", "optical-prisms",
    {"material": "H-K9L(BK7)", "angleTolerance": "±10 arcsec", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "coatings": "Custom Design"},
    [{"partNumber": "LOPP10-17", "dimension": "10×17mm"}, {"partNumber": "LOPP15-25", "dimension": "15×25mm"}, {"partNumber": "LOPP25.4-42", "dimension": "25.4×42mm"}]
)

add(41, "Corner Cube Prisms", "角锥棱镜",
    "Optical Prisms", "光学棱镜",
    "Corner cube prisms (retroreflectors) reflect light back to its source regardless of the angle of incidence. Ideal for alignment and measurement applications. Custom coating designs available.",
    "角锥棱镜（后向反射器）无论入射角如何都将光线反射回光源方向。适用于对准和测量应用。支持定制镀膜。",
    "corner-cube-prisms", "optical-prisms",
    {"material": "H-K9L(BK7)", "angleTolerance": "±10 arcsec", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "beamDeviation": "<3 arcsec", "coatings": "Custom Design"},
    [{"partNumber": "LOCC10", "dimension": "10mm"}, {"partNumber": "LOCC20", "dimension": "20mm"}, {"partNumber": "LOCC25.4", "dimension": "25.4mm"}]
)

add(42, "Dove Prisms", "道威棱镜",
    "Optical Prisms", "光学棱镜",
    "Dove prisms rotate an image by twice the prism rotation angle. When the prism is rotated, the image rotates at twice the rate. Custom coating designs available.",
    "道威棱镜将图像旋转棱镜旋转角度的两倍。当棱镜旋转时，图像以两倍速率旋转。支持定制镀膜。",
    "dove-prisms", "optical-prisms",
    {"material": "H-K9L(BK7)", "angleTolerance": "±1 arcmin", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "coatings": "Custom Design"},
    [{"partNumber": "LODP10-30", "dimension": "10×30mm"}, {"partNumber": "LODP15-45", "dimension": "15×45mm"}, {"partNumber": "LODP20-60", "dimension": "20×60mm"}]
)

add(43, "Equilateral Dispersing Prisms", "等边色散棱镜",
    "Optical Prisms", "光学棱镜",
    "Equilateral dispersing prisms separate white light into its component colors through dispersion. 60° angles with precise tolerance. Custom coating designs available.",
    "等边色散棱镜通过色散将白光分解成组成颜色。60°角，公差精确。支持定制镀膜。",
    "equilateral-dispersing-prisms", "optical-prisms",
    {"material": "H-K9L(BK7)", "angleTolerance": "±10 arcsec", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "coatings": "Custom Design"},
    [{"partNumber": "LOED10", "dimension": "10mm"}, {"partNumber": "LOED15", "dimension": "15mm"}, {"partNumber": "LOED25.4", "dimension": "25.4mm"}, {"partNumber": "LOED50", "dimension": "50mm"}]
)

add(44, "Roof Prisms", "屋脊棱镜",
    "Optical Prisms", "光学棱镜",
    "Roof prisms combine the function of a right angle prism with a roof surface, reversing the image left-to-right while deviating the beam by 90 degrees. Custom coating designs available.",
    "屋脊棱镜结合了直角棱镜和屋脊面的功能，在将光束偏转90度的同时左右反转图像。支持定制镀膜。",
    "roof-prisms", "optical-prisms",
    {"material": "H-K9L(BK7)", "angleTolerance": "±1 arcmin", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "clearAperture": ">90%", "coatings": "Custom Design"},
    [{"partNumber": "LORP10-14", "dimension": "10×14mm"}, {"partNumber": "LORP15-21", "dimension": "15×21mm"}, {"partNumber": "LORP25.4-36", "dimension": "25.4×36mm"}]
)

# ========== 5. Optical Filters (6) ==========
add(45, "Narrow Band Interference Filters", "窄带干涉滤光片",
    "Optical Filters", "光学滤光片",
    "Narrow band interference filters selectively transmit a specific wavelength band while blocking all other wavelengths. Precise center wavelength control with steep edges.",
    "窄带干涉滤光片选择性透过特定波长带，同时阻挡其他所有波长。中心波长精确控制，边缘陡峭。",
    "narrow-band-interference-filters", "optical-filters",
    {"diameterTolerance": "±0.2mm", "centerWavelengthTolerance": "±0.2nm", "surfaceQuality": "60-40", "surfaceFlatness": "λ/2@632.8nm", "clearAperture": ">90%"},
    [{"partNumber": "LONBI12.7-532", "diameter": "12.70mm", "cwl": "532nm", "fwhm": "10nm"}, {"partNumber": "LONBI25.4-632.8", "diameter": "25.40mm", "cwl": "632.8nm", "fwhm": "3nm"}, {"partNumber": "LONBI25.4-1064", "diameter": "25.40mm", "cwl": "1064nm", "fwhm": "10nm"}]
)

add(46, "Fixed Neutral Density Filters", "固定中性密度滤光片",
    "Optical Filters", "光学滤光片",
    "Fixed neutral density (ND) filters uniformly reduce light intensity across the spectrum without altering color balance. Available in various optical densities.",
    "固定中性密度(ND)滤光片在整个光谱范围内均匀降低光强而不改变色彩平衡。提供多种光学密度。",
    "fixed-neutral-density-filters", "optical-filters",
    {"diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "60-40", "surfaceFlatness": "λ/4@632.8nm", "odTolerance": "±1%"},
    [{"partNumber": "LOND12.7-0.3", "diameter": "12.70mm", "od": "0.3"}, {"partNumber": "LOND12.7-1.0", "diameter": "12.70mm", "od": "1.0"}, {"partNumber": "LOND25.4-2.0", "diameter": "25.40mm", "od": "2.0"}, {"partNumber": "LOND25.4-3.0", "diameter": "25.40mm", "od": "3.0"}]
)

add(47, "Variable Neutral Density Filters", "可变中性密度滤光片",
    "Optical Filters", "光学滤光片",
    "Variable neutral density filters allow continuous adjustment of light attenuation. Available in both circular and linear configurations for flexible light control.",
    "可变中性密度滤光片允许连续调节光的衰减。提供圆形和线性两种配置，灵活控制光强。",
    "variable-neutral-density-filters", "optical-filters",
    {"diameterTolerance": "±0.2mm", "surfaceQuality": "60-40", "surfaceFlatness": "λ/2@632.8nm", "type": "Circular / Linear"},
    [{"partNumber": "LOVND25-C", "diameter": "25.00mm", "type": "Circular", "odRange": "0-2.0"}, {"partNumber": "LOVND50-C", "diameter": "50.00mm", "type": "Circular", "odRange": "0-2.0"}, {"partNumber": "LOVND50-L", "dimension": "50×50mm", "type": "Linear", "odRange": "0-2.0"}]
)

add(48, "UV Bandpass Filters", "紫外带通滤光片",
    "Optical Filters", "光学滤光片",
    "UV bandpass filters selectively transmit ultraviolet wavelengths while blocking visible and IR. Ideal for UV imaging, fluorescence, and spectroscopy applications.",
    "紫外带通滤光片选择性透过紫外波长，同时阻挡可见光和红外。适用于紫外成像、荧光和光谱分析应用。",
    "uv-bandpass-filters", "optical-filters",
    {"diameterTolerance": "±0.2mm", "surfaceQuality": "60-40", "surfaceFlatness": "λ/2@632.8nm", "clearAperture": ">90%"},
    [{"partNumber": "LOUVBP25.4", "diameter": "25.40mm", "passband": "UV"}, {"partNumber": "LOUVBP50", "diameter": "50.00mm", "passband": "UV"}]
)

add(49, "IR Bandpass Filters", "红外带通滤光片",
    "Optical Filters", "光学滤光片",
    "IR bandpass filters selectively transmit infrared wavelengths while blocking visible and UV. Ideal for thermal imaging, IR spectroscopy, and sensor applications.",
    "红外带通滤光片选择性透过红外波长，同时阻挡可见光和紫外。适用于热成像、红外光谱和传感器应用。",
    "ir-bandpass-filters", "optical-filters",
    {"diameterTolerance": "±0.2mm", "surfaceQuality": "60-40", "surfaceFlatness": "λ/2@632.8nm", "clearAperture": ">90%"},
    [{"partNumber": "LOIRBP25.4", "diameter": "25.40mm", "passband": "IR"}, {"partNumber": "LOIRBP50", "diameter": "50.00mm", "passband": "IR"}]
)

add(50, "Bandpass Filters", "带通滤光片",
    "Optical Filters", "光学滤光片",
    "Bandpass filters selectively transmit a specific range of wavelengths while blocking shorter and longer wavelengths. Available in various center wavelengths and bandwidths.",
    "带通滤光片选择性透过特定波长范围，同时阻挡较短和较长波长。提供多种中心波长和带宽。",
    "bandpass-filters", "optical-filters",
    {"diameterTolerance": "±0.2mm", "surfaceQuality": "60-40", "surfaceFlatness": "λ/2@632.8nm", "clearAperture": ">90%"},
    [{"partNumber": "LOBP12.7-450", "diameter": "12.70mm", "cwl": "450nm"}, {"partNumber": "LOBP25.4-550", "diameter": "25.40mm", "cwl": "550nm"}, {"partNumber": "LOBP25.4-850", "diameter": "25.40mm", "cwl": "850nm"}]
)

# ========== 6. Optical Beamsplitters (4) ==========
add(51, "Beamsplitter Plates", "分光平片",
    "Optical Beamsplitters", "光学分光镜",
    "Beamsplitter plates split incident light into transmitted and reflected beams in various ratios. Default 50/50 beam splitting with custom ratios available. One side: dielectric partial reflection; other side: AR coating.",
    "分光板通过介质镀膜将入射光分成透射光和反射光，提供50/50、60/40、80/20、90/10等多种分光比。默认配置为50/50分光。一面：介质部分反射；另一面：增透膜。",
    "beamsplitter-plates", "optical-beamsplitters",
    {"material": "N-BK7/K9", "diameterTolerance": "±0.15mm", "thicknessTolerance": "±0.10mm", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "parallelism": "<1 arc min", "splitRatio": "50/50 ±2%"},
    [{"partNumber": "LOBP12.7-450/650", "diameter": "12.70mm", "thickness": "3.0mm", "wavelength": "450-650nm"}, {"partNumber": "LOBP25.4-450/650", "diameter": "25.40mm", "thickness": "3.0mm", "wavelength": "450-650nm"}, {"partNumber": "LOBP50.8-450/650", "diameter": "50.80mm", "thickness": "5.0mm", "wavelength": "450-650nm"}]
)

add(52, "Cube Beamsplitters", "普通立方体分光镜",
    "Optical Beamsplitters", "光学分光镜",
    "Cube beamsplitters consist of two right-angle prisms cemented together with a dielectric coating on the hypotenuse. They provide 50/50 splitting with minimal beam displacement.",
    "立方体分光镜由两个直角棱镜胶合而成，斜面上镀有介质膜。提供50/50分光，光束偏移最小。",
    "cube-beamsplitters", "optical-beamsplitters",
    {"material": "N-BK7/K9", "angleTolerance": "±10 arcsec", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "parallelism": "<1 arc min", "splitRatio": "50/50"},
    [{"partNumber": "LOCB10-450/650", "dimension": "10mm", "wavelength": "450-650nm"}, {"partNumber": "LOCB20-450/650", "dimension": "20mm", "wavelength": "450-650mm"}, {"partNumber": "LOCB25.4-450/650", "dimension": "25.4mm", "wavelength": "450-650nm"}]
)

add(53, "Non-Polarizing Cube Beamsplitters", "消偏振立方体分光棱镜",
    "Optical Beamsplitters", "光学分光镜",
    "Non-polarizing cube beamsplitters maintain equal splitting ratios for both s- and p-polarization states. T(P or S)=50±5%. Ideal for polarization-sensitive applications.",
    "消偏振立方体分光棱镜对s偏振和p偏振保持相同的分光比。T(P or S)=50±5%。适用于偏振敏感应用。",
    "non-polarizing-cube-beamsplitters", "optical-beamsplitters",
    {"material": "N-BK7/K9", "angleTolerance": "±10 arcsec", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "parallelism": "<1 arc min", "transmissionPolarization": "T(P or S)=50±5%"},
    [{"partNumber": "LONCB12.7-450/650", "dimension": "12.7mm", "wavelength": "450-650nm"}, {"partNumber": "LONCB25.4-450/650", "dimension": "25.4mm", "wavelength": "450-650nm"}]
)

add(54, "Polarizing Cube Beamsplitters", "偏振立方体分光棱镜",
    "Optical Beamsplitters", "光学分光镜",
    "Polarizing cube beamsplitters separate s- and p-polarization components. Extinction ratio >500:1, Tp>95%, Ts<1%. Ideal for polarization-based optical systems.",
    "偏振立方体分光棱镜分离s偏振和p偏振分量。消光比>500:1，Tp>95%，Ts<1%。适用于偏振光学系统。",
    "polarizing-cube-beamsplitters", "optical-beamsplitters",
    {"material": "N-BK7/K9", "angleTolerance": "±10 arcsec", "surfaceQuality": "40-20", "surfaceFlatness": "λ/4@632.8nm", "parallelism": "<1 arc min", "extinctionRatio": ">500:1", "tp": ">95%", "ts": "<1%"},
    [{"partNumber": "LOPCB12.7-450/650", "dimension": "12.7mm", "wavelength": "450-650nm"}, {"partNumber": "LOPCB25.4-450/650", "dimension": "25.4mm", "wavelength": "450-650nm"}]
)

# ========== 7. Optical Wave Plates (4) ==========
add(55, "Multiple Order Waveplates", "多级波片",
    "Optical Wave Plates", "光学波片",
    "Multiple order waveplates provide precise retardation at specific wavelengths. Made from high-quality quartz crystal with excellent surface quality and wavefront distortion control.",
    "多级波片在特定波长提供精确的相位延迟。采用高品质石英晶体，具有优异的表面质量和波前畸变控制。",
    "multiple-order-waveplates", "optical-wave-plates",
    {"material": "Quartz Crystal", "surfaceQuality": "20-10", "wavefrontDistortion": "λ/8", "phaseAccuracy": "λ/100", "parallelism": "<1 arc min", "diameterTolerance": "±0.15mm", "clearAperture": ">90%"},
    [{"partNumber": "LOMOW12.7-λ/2-532", "diameter": "12.70mm", "retardation": "λ/2", "wavelength": "532nm"}, {"partNumber": "LOMOW12.7-λ/4-632.8", "diameter": "12.70mm", "retardation": "λ/4", "wavelength": "632.8nm"}, {"partNumber": "LOMOW25.4-λ/2-1064", "diameter": "25.40mm", "retardation": "λ/2", "wavelength": "1064nm"}]
)

add(56, "Dual Wavelength Waveplates", "双波长波片",
    "Optical Wave Plates", "光学波片",
    "Dual wavelength waveplates provide specified retardation at two different wavelengths simultaneously. Ideal for dual-wavelength laser systems and frequency-doubled applications.",
    "双波长波片在两个不同波长同时提供指定的相位延迟。适用于双波长激光系统和倍频应用。",
    "dual-wavelength-waveplates", "optical-wave-plates",
    {"material": "Quartz Crystal", "surfaceQuality": "20-10", "wavefrontDistortion": "λ/8", "phaseAccuracy": "λ/100", "parallelism": "<1 arc min", "diameterTolerance": "±0.15mm", "clearAperture": ">90%"},
    [{"partNumber": "LODWW12.7-532/1064", "diameter": "12.70mm", "wavelength1": "532nm", "wavelength2": "1064nm"}, {"partNumber": "LODWW25.4-532/1064", "diameter": "25.40mm", "wavelength1": "532nm", "wavelength2": "1064nm"}]
)

add(57, "Cemented Zero Order Waveplates", "胶合零级波片",
    "Optical Wave Plates", "光学波片",
    "Cemented zero order waveplates consist of two multiple order waveplates cemented together with their optical axes crossed. Provides stable retardation over a wider wavelength and temperature range.",
    "胶合零级波片由两个多级波片光轴交叉胶合而成。在更宽的波长和温度范围内提供稳定的相位延迟。",
    "cemented-zero-order-waveplates", "optical-wave-plates",
    {"material": "Quartz Crystal", "surfaceQuality": "20-10", "wavefrontDistortion": "λ/8", "phaseAccuracy": "λ/100", "parallelism": "<1 arc min", "diameterTolerance": "±0.15mm", "clearAperture": ">90%"},
    [{"partNumber": "LOCZW12.7-λ/2-532", "diameter": "12.70mm", "retardation": "λ/2", "wavelength": "532nm"}, {"partNumber": "LOCZW12.7-λ/4-632.8", "diameter": "12.70mm", "retardation": "λ/4", "wavelength": "632.8nm"}, {"partNumber": "LOCZW25.4-λ/2-1064", "diameter": "25.40mm", "retardation": "λ/2", "wavelength": "1064nm"}]
)

add(58, "Air Spaced Zero Order Waveplates", "空气隙零级波片",
    "Optical Wave Plates", "光学波片",
    "Air spaced zero order waveplates consist of two multiple order waveplates separated by an air gap. Higher damage threshold than cemented type, suitable for high-power laser applications.",
    "空气隙零级波片由两个多级波片以空气隙间隔组成。比胶合型具有更高的损伤阈值，适用于高功率激光应用。",
    "air-spaced-zero-order-waveplates", "optical-wave-plates",
    {"material": "Quartz Crystal", "surfaceQuality": "20-10", "wavefrontDistortion": "λ/8", "phaseAccuracy": "λ/100", "parallelism": "<1 arc min", "diameterTolerance": "±0.15mm", "clearAperture": ">90%"},
    [{"partNumber": "LOAZW12.7-λ/2-532", "diameter": "12.70mm", "retardation": "λ/2", "wavelength": "532nm"}, {"partNumber": "LOAZW12.7-λ/4-632.8", "diameter": "12.70mm", "retardation": "λ/4", "wavelength": "632.8nm"}, {"partNumber": "LOAZW25.4-λ/2-1064", "diameter": "25.40mm", "retardation": "λ/2", "wavelength": "1064nm"}]
)

# ========== 8. Optical Polarizers (7) ==========
add(59, "Visible Linear Polarizers", "可见光线偏振片",
    "Optical Polarizers", "光学偏振片",
    "Visible linear polarizers transmit light oscillating in one plane while blocking orthogonal polarization. High transmission and excellent extinction ratio for visible spectrum applications.",
    "可见光线偏振片透过在一个平面内振动的光，同时阻挡正交偏振光。高透过率和优异的消光比，用于可见光谱应用。",
    "visible-linear-polarizers", "optical-polarizers",
    {"wavelengthRange": "400-700nm", "surfaceQuality": "60-40", "parallelism": "<1 arc min", "transmission": ">50%", "extinctionRatio": ">100:1"},
    [{"partNumber": "LOVLP12.7", "diameter": "12.70mm"}, {"partNumber": "LOVLP25.4", "diameter": "25.40mm"}, {"partNumber": "LOVLP50.8", "diameter": "50.80mm"}]
)

add(60, "Visible Circular Polarizers", "可见光圆偏振片",
    "Optical Polarizers", "光学偏振片",
    "Visible circular polarizers consist of a linear polarizer and a quarter-wave plate, producing circularly polarized light. Ideal for display and imaging applications.",
    "可见光圆偏振片由一个线偏振片和一个四分之一波片组成，产生圆偏振光。适用于显示和成像应用。",
    "visible-circular-polarizers", "optical-polarizers",
    {"wavelengthRange": "400-700nm", "surfaceQuality": "60-40", "parallelism": "<1 arc min", "transmission": ">45%"},
    [{"partNumber": "LOVCP12.7", "diameter": "12.70mm"}, {"partNumber": "LOVCP25.4", "diameter": "25.40mm"}, {"partNumber": "LOVCP50.8", "diameter": "50.80mm"}]
)

add(61, "IR Polarizers", "红外偏振片",
    "Optical Polarizers", "光学偏振片",
    "IR polarizers provide high extinction ratio polarization in the infrared spectrum. Extinction ratio >1000:1. Ideal for IR imaging and sensing applications.",
    "红外偏振片在红外光谱范围提供高消光比偏振。消光比>1000:1。适用于红外成像和传感应用。",
    "ir-polarizers", "optical-polarizers",
    {"wavelengthRange": "IR", "surfaceQuality": "60-40", "parallelism": "<1 arc min", "extinctionRatio": ">1000:1"},
    [{"partNumber": "LOIRP12.7", "diameter": "12.70mm"}, {"partNumber": "LOIRP25.4", "diameter": "25.40mm"}]
)

add(62, "Glan Taylor Prisms", "格兰泰勒棱镜",
    "Optical Polarizers", "光学偏振片",
    "Glan Taylor prisms are air-spaced polarizing prisms made from calcite. They provide high extinction ratio polarization with excellent wavefront quality for laser and analytical applications.",
    "格兰泰勒棱镜是空气隙偏振棱镜，由方解石制成。提供高消光比偏振和优异的波前质量，用于激光和分析应用。",
    "glan-taylor-prisms", "optical-polarizers",
    {"material": "Calcite", "surfaceQuality": "20-10", "wavefrontDistortion": "λ/4", "extinctionRatio": ">100000:1", "transmission": ">90%"},
    [{"partNumber": "LOGT8×8", "dimension": "8×8mm"}, {"partNumber": "LOGT12×12", "dimension": "12×12mm"}, {"partNumber": "LOGT15×15", "dimension": "15×15mm"}]
)

add(63, "Glan Laser Prisms", "格兰激光棱镜",
    "Optical Polarizers", "光学偏振片",
    "Glan laser prisms are air-spaced polarizing prisms optimized for high-power laser applications. Superior damage threshold with high extinction ratio.",
    "格兰激光棱镜是专为高功率激光应用优化的空气隙偏振棱镜。具有优异的损伤阈值和高消光比。",
    "glan-laser-prisms", "optical-polarizers",
    {"material": "Calcite", "surfaceQuality": "20-10", "wavefrontDistortion": "λ/4", "extinctionRatio": ">100000:1", "transmission": ">95%"},
    [{"partNumber": "LOGL8×8", "dimension": "8×8mm"}, {"partNumber": "LOGL12×12", "dimension": "12×12mm"}, {"partNumber": "LOGL15×15", "dimension": "15×15mm"}]
)

add(64, "Glan Thompson Prisms", "格兰汤普生棱镜",
    "Optical Polarizers", "光学偏振片",
    "Glan Thompson prisms are cemented calcite polarizing prisms with a wide acceptance angle. They provide high extinction ratio polarization for analytical and imaging applications.",
    "格兰汤普生棱镜是胶合方解石偏振棱镜，具有宽接收角。为分析和成像应用提供高消光比偏振。",
    "glan-thompson-prisms", "optical-polarizers",
    {"material": "Calcite", "surfaceQuality": "20-10", "wavefrontDistortion": "λ/4", "extinctionRatio": ">100000:1", "transmission": ">90%", "acceptanceAngle": ">26°"},
    [{"partNumber": "LOGT12×12", "dimension": "12×12mm"}, {"partNumber": "LOGT15×15", "dimension": "15×15mm"}, {"partNumber": "LOGT20×20", "dimension": "20×20mm"}]
)

add(65, "Wollaston Prisms", "渥拉斯通棱镜",
    "Optical Polarizers", "光学偏振片",
    "Wollaston prisms split incident light into two orthogonally polarized beams with a separation angle of approximately 19°. Ideal for polarization analysis and interferometry.",
    "渥拉斯通棱镜将入射光分成两束正交偏振光，分离角约为19°。适用于偏振分析和干涉测量。",
    "wollaston-prisms", "optical-polarizers",
    {"material": "Calcite", "surfaceQuality": "20-10", "wavefrontDistortion": "λ/4", "separationAngle": "~19°"},
    [{"partNumber": "LOWP12×12", "dimension": "12×12mm"}, {"partNumber": "LOWP15×15", "dimension": "15×15mm"}]
)

# ========== 9. Laser Protection (1) ==========
add(66, "Laser Safety Goggles", "激光护目镜",
    "Laser Protection", "激光防护",
    "Laser safety goggles provide OD 6+ optical density protection across multiple laser wavelengths. Visible light transmission (VLT) 60-85% for comfortable wear. CE certified.",
    "激光护目镜在多种激光波长提供OD 6+光学密度防护。可见光透过率(VLT)60-85%，佩戴舒适。CE认证。",
    "laser-safety-goggles", "laser-protection",
    {"opticalDensity": "OD 6+", "visibleLightTransmission": "60-85%", "certification": "CE", "wavelengthRange": "Multiple laser wavelengths"},
    [{"partNumber": "LOLSG-UV", "protection": "UV laser", "od": "6+", "vlt": "70%"}, {"partNumber": "LOLSG-VIS", "protection": "Visible laser", "od": "6+", "vlt": "60%"}, {"partNumber": "LOLSG-IR", "protection": "IR laser", "od": "6+", "vlt": "85%"}]
)

# ========== Generate JS output ==========
print("Total products: {}".format(len(products)))

# Count by category
cats = {}
for p in products:
    c = p["category"]
    cats[c] = cats.get(c, 0) + 1
for c, n in cats.items():
    print("  {}: {}".format(c, n))

# Write products-data.js
output_lines = []
output_lines.append("// PhotonEdge Products Data V34 - Based on Official Product Catalog")
output_lines.append("")
output_lines.append("var PRODUCTS = [")

for i, p in enumerate(products):
    js_obj = json.dumps(p, ensure_ascii=False, indent=2)
    # Fix JSON to JS: use double quotes for keys (json.dumps already does this)
    comma = "," if i < len(products) - 1 else ""
    output_lines.append("  " + js_obj + comma)

output_lines.append("];")

js_content = "\n".join(output_lines)

with open("/app/data/所有对话/主对话/v32-work/js/products-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Written to products-data.js ({} bytes)".format(len(js_content)))
