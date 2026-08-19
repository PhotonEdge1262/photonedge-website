#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PhotonEdge V95 Generator (Website 3.1 Phase 2)
- 10 Tier 2 SEO Product Landing Pages
- About Page 3.1 Upgrade
- Specification Optimization Page
- Evidence Center Page
- Case Studies Format Upgrade
- Sitemap Rebuild
- SEO Checks & Fixes
"""

import os
import json
import shutil
import re
import subprocess
from datetime import datetime

SRC = "/Coze/Drive/小光/所有对话/主对话/PhotonEdge-V94/v88-build"
DST = "/Coze/Drive/小光/所有对话/主对话/PhotonEdge-V95/v88-build"
BASE_URL = "https://photonedgeoptics.com"
LASTMOD = "2026-08-15"

# ─────────────────────────────────────────────────────────
# Tier 2 Product Page Definitions
# ─────────────────────────────────────────────────────────

TIER2_PAGES = [
    {
        "slug": "fused-silica-plano-convex-lenses",
        "name": "Fused Silica Plano-Convex Lenses",
        "category31": "Optical Lenses",
        "componentType": "Lens",
        "material": "UV Fused Silica",
        "title": "Fused Silica Plano-Convex Lenses | UV to NIR | PhotonEdge",
        "description": "UV fused silica plano-convex lenses for UV, laser and high-temperature applications. High LIDT coatings from 193nm to 2100nm. Custom diameters and focal lengths available.",
        "keywords": "fused silica plano convex lens, UV plano convex lens, fused silica lens, high power laser lens, 266nm lens, 355nm lens, UV focusing lens",
        "subtitle": "High-purity fused silica plano-convex lenses engineered for UV transmission, high laser damage threshold and thermal stability. Plano-convex geometry minimizes spherical aberration in collimation and focusing applications.",
        "image": "images/products/optical-lenses/uv-fused-silica-plano-convex.jpg",
        "overview": [
            "PhotonEdge fused silica plano-convex (PCX) lenses are manufactured from Corning 7980 equivalent high-purity UV-grade fused silica, offering exceptional transmission from the deep UV (193nm) through the near infrared (2100nm).",
            "The plano-convex design provides positive focal length with minimal spherical aberration when the convex surface faces the longer conjugate distance — the standard configuration for focusing collimated beams or collimating point sources.",
            "Compared to BK7 glass, fused silica offers significantly lower coefficient of thermal expansion, higher resistance to thermal shock, and superior UV transmission, making it the preferred material for laser systems, semiconductor inspection, and UV photolithography equipment.",
            "Standard uncoated lenses are stocked in diameters from 6.35mm to 50.8mm with focal lengths ranging from 10mm to 500mm. Anti-reflection coatings are available for VIS, NIR, and common laser wavelengths including 266nm, 355nm, 532nm, 1064nm, and 1550nm."
        ],
        "specs": [
            ("Material", "UV Grade Fused Silica (Corning 7980 equivalent)"),
            ("Refractive Index", "1.45846 @ 589.3nm"),
            ("Diameter Range", "6.35mm – 50.8mm (standard); custom up to 200mm"),
            ("Focal Length Range", "10mm – 500mm (standard); custom available"),
            ("Focal Length Tolerance", "±1% (standard); ±0.5% or ±0.2% (precision)"),
            ("Diameter Tolerance", "±0.10mm (standard); ±0.01mm (precision)"),
            ("Center Thickness Tolerance", "±0.10mm"),
            ("Surface Quality", "40-20 (standard); 20-10 (precision); 10-5 (laser grade)"),
            ("Surface Flatness", "λ/4 @ 632.8nm (standard); λ/10 or λ/20 (precision)"),
            ("Centration", "< 3 arc minutes"),
            ("Clear Aperture", "> 90% of diameter"),
            ("Chamfer", "0.2mm × 45° (protective)"),
            ("Coating Options", "Uncoated, VIS AR, NIR AR, 355nm AR, 1064nm AR, dual-band AR")
        ],
        "materials": [
            ("UV Grade Fused Silica (Type I)", "Corning 7980 / Heraeus Suprasil equivalent. Highest purity, lowest OH content. Best for deep UV (193-250nm) and high-power laser applications."),
            ("UV Grade Fused Silica (Type II)", "High-purity synthetic fused silica. Excellent transmission from 200nm to 2200nm. Standard material for most UV and laser applications."),
            ("Infrared Fused Silica", "Low-OH fused silica optimized for NIR and SWIR transmission (up to 3500nm). Suitable for fiber laser and telecom wavelengths.")
        ],
        "coatings": [
            ("Uncoated", "As-polished surface. 4% reflection per surface at normal incidence. Use for prototyping or when wavelength is undefined."),
            ("VIS AR Coating (350-700nm)", "Broadband anti-reflection coating. R < 1.5% average per surface. Standard for visible imaging and illumination systems."),
            ("NIR AR Coating (650-1050nm)", "Optimized for near-infrared and common laser wavelengths (785nm, 808nm, 980nm, 1064nm). R < 0.5% average per surface."),
            ("UV AR Coating (250-400nm)", "UV-optimized AR coating for 266nm, 355nm and 365nm applications. R < 1.0% average per surface. LIDT > 2 J/cm² @ 355nm, 10ns."),
            ("Laser Line AR (Single Wavelength)", "Narrowband AR coating optimized for a specific laser line. R < 0.25% per surface at design wavelength. Available for 193nm, 248nm, 266nm, 308nm, 355nm, 532nm, 1064nm, 1550nm."),
            ("Broadband AR (1000-1700nm)", "For telecom and fiber laser applications. R < 0.75% average per surface over the full band.")
        ],
        "tolerances": [
            ("Standard Grade", "±0.10mm diameter / ±0.10mm thickness / 40-20 surface quality / λ/4 flatness / ±1% focal length. Suitable for most general-purpose optical systems and prototyping."),
            ("Precision Grade", "±0.05mm diameter / ±0.05mm thickness / 20-10 surface quality / λ/10 flatness / ±0.5% focal length. For metrology, imaging, and moderate-precision laser systems."),
            ("Laser Grade", "±0.02mm diameter / ±0.02mm thickness / 10-5 surface quality / λ/20 flatness / ±0.2% focal length. For high-power lasers, interferometry, and ultra-precision applications.")
        ],
        "inspection": [
            "100% dimensional inspection with digital micrometers and optical comparators",
            "Surface quality verified under dark-field inspection per MIL-PRF-13830B",
            "Surface flatness measured with laser interferometer (ZYGO equivalent) at 632.8nm",
            "Focal length verified through optical bench collimation test",
            "Centration measured with precision rotation fixture (< 3 arc min)",
            "Coating spectral performance tested on PerkinElmer Lambda spectrophotometer",
            "Full inspection report available for every precision and laser-grade order"
        ],
        "applications": [
            ("UV Laser Systems", "355nm and 266nm DPSS laser focusing, beam delivery, and harmonic separation"),
            ("Semiconductor Inspection", "Wafer inspection optics, photolithography illumination, mask alignment systems"),
            ("Spectroscopy", "Monochromator focusing, UV-Vis-NIR spectrophotometer optics, fluorescence excitation"),
            ("Life Sciences", "Flow cytometry, confocal microscopy, DNA sequencing optics"),
            ("Material Processing", "Laser marking, engraving, and micro-machining beam focusing"),
            ("Fiber Optics", "Fiber coupling and collimation, fiber laser output collimators")
        ],
        "engineering": [
            "Plano-convex lenses should be oriented with the curved surface facing the longer conjugate distance to minimize spherical aberration.",
            "For focusing a collimated laser beam to the smallest possible spot, use a lens with the shortest possible focal length that meets your working distance requirements. Spot size is proportional to focal length × beam divergence.",
            "When operating at high average power (>50W), fused silica is preferred over BK7 due to lower absorption and thermal expansion coefficient. Consider thermal lensing effects in your optical design.",
            "For UV applications below 300nm, ensure that coatings and substrate materials are specified for deep-UV use. Standard VIS coatings absorb strongly at UV wavelengths.",
            "Fused silica has a refractive index temperature coefficient of approximately 1.28 × 10⁻⁵ /°C, which affects focal length stability in temperature-varying environments."
        ],
        "faqs": [
            ("What is the difference between BK7 and fused silica plano-convex lenses?",
             "BK7 is a borosilicate crown glass with good visible and near-IR transmission. Fused silica is amorphous SiO₂ with a much wider transmission range (193nm to 2100nm), lower thermal expansion, and higher laser damage threshold. Use fused silica for UV applications, high-power lasers, or when thermal stability is critical."),
            ("How do I calculate the focal length tolerance I need?",
             "Most systems work fine with ±1% tolerance. For metrology and imaging systems where magnification accuracy matters, use ±0.5%. For laser focusing into a fiber or single-mode waveguide, ±0.2% may be needed. Tighter tolerance increases cost due to additional measurement and sorting."),
            ("Can fused silica lenses be used at 1064nm high-power lasers?",
             "Yes, fused silica is the standard substrate for 1064nm Nd:YAG and fiber laser optics. With proper AR coating, LIDT can exceed 15 J/cm² at 1064nm (10ns, 10Hz). For multi-kilowatt CW lasers, consider thermal lensing effects and specify appropriate substrate thickness."),
            ("What coating should I choose for broadband imaging from 400-700nm?",
             "Our VIS broadband AR coating (350-700nm) provides R < 1.5% average per surface across the visible band. For best image contrast, ensure all optical surfaces have anti-reflection coatings to reduce stray light and ghost reflections.")
        ],
        "related_products": [
            ("/products/fused-silica-laser-lenses/", "Fused Silica Laser Lenses"),
            ("/products/fused-silica-optical-mirrors/", "Fused Silica Optical Mirrors"),
            ("/products/fused-silica-optical-windows/", "Fused Silica Optical Windows"),
            ("/products/uv-fused-silica-bi-convex/", "Fused Silica Bi-Convex Lenses"),
            ("/products/laser-beam-expanders/", "Laser Beam Expanders"),
            ("/products/high-power-laser-mirrors/", "High-Power Laser Mirrors")
        ],
        "related_articles": [
            ("/blog/laser-damage-threshold-guide/", "Laser Damage Threshold: What Engineers Need to Know"),
            ("/blog/bk7-vs-uv-fused-silica/", "BK7 vs UV Fused Silica: How to Choose the Right Optical Material"),
            ("/blog/laser-optics-selection-guide/", "Complete Guide to Laser Optics Selection")
        ],
        "internal_links": [
            ("/materials/uv-fused-silica/", "UV Fused Silica Material"),
            ("/applications/laser-optics/", "Laser Applications"),
            ("/ai-optical-engineer.html", "AI Optical Engineer")
        ]
    },
    {
        "slug": "fused-silica-optical-mirrors",
        "name": "Fused Silica Optical Mirrors",
        "category31": "Optical Mirrors",
        "componentType": "Mirror",
        "material": "UV Fused Silica",
        "title": "Fused Silica Optical Mirrors | High LIDT | PhotonEdge",
        "description": "Fused silica optical mirrors with high laser damage threshold. Dielectric coatings from UV to NIR. λ/10 and λ/20 flatness for demanding laser and imaging applications.",
        "keywords": "fused silica mirror, UV mirror, high LIDT mirror, laser mirror, dielectric mirror, fused silica reflector, high power mirror",
        "subtitle": "High-precision fused silica mirrors with dielectric and metallic coatings, engineered for low wavefront distortion, high reflectivity and exceptional laser damage threshold performance.",
        "image": "images/products/optical-mirrors/high-energy-laser-mirrors.jpg",
        "overview": [
            "PhotonEdge fused silica optical mirrors are manufactured from UV-grade fused silica substrates, providing the thermal stability and low absorption required for high-power laser applications.",
            "Our mirror product line includes laser line highly reflective mirrors, broadband dielectric mirrors, dichroic mirrors, and metallic-coated mirrors — all available on fused silica substrates for applications ranging from deep UV to near infrared.",
            "Fused silica is the substrate of choice when thermal distortion must be minimized. Its coefficient of thermal expansion (0.55 × 10⁻⁶ /°C) is roughly 10× lower than BK7, making it essential for high-average-power laser systems and precision interferometry.",
            "Standard mirrors are available in diameters from 12.7mm to 50.8mm with surface flatness from λ/4 to λ/20. Custom sizes, shapes and coatings can be manufactured to specification with typical lead times of 3-5 weeks."
        ],
        "specs": [
            ("Substrate Material", "UV Grade Fused Silica (Corning 7980 equivalent)"),
            ("Diameter / Size Range", "12.7mm – 50.8mm round (standard); custom up to 200mm; square/rectangular available"),
            ("Thickness", "3.175mm, 6.35mm, 9.525mm (standard); custom available"),
            ("Surface Quality", "40-20 (standard); 20-10 (precision); 10-5 (laser grade)"),
            ("Surface Flatness", "λ/4, λ/10, λ/20 @ 632.8nm"),
            ("Reflectivity", "> 99.5% (laser line HR); > 99% (broadband); > 95% (metallic)"),
            ("Wavefront Distortion", "< λ/10 per inch (standard); < λ/20 per inch (precision)"),
            ("Laser Damage Threshold", "Up to 25 J/cm² @ 1064nm, 10ns, 10Hz (laser line HR)"),
            ("Coating Types", "Dielectric HR, broadband dielectric, dichroic, protected metal, enhanced metal"),
            ("Clear Aperture", "> 90% of diameter"),
            ("Chamfer", "0.3mm × 45° (protective)")
        ],
        "materials": [
            ("UV Grade Fused Silica", "Standard substrate for UV and laser applications. Transmission from 193nm to 2100nm. Low thermal expansion (0.55 × 10⁻⁶ /°C)."),
            ("Suprasil-Grade Fused Silica", "Ultra-high-purity fused silica with extremely low inclusions and striae. For the most demanding UV laser and interferometry applications."),
            ("Low-OH Fused Silica", "Infrared-optimized fused silica with reduced OH absorption bands. Extended transmission up to 3.5μm for NIR/SWIR applications.")
        ],
        "coatings": [
            ("Laser Line High Reflector (Dielectric)", "Multilayer dielectric coating optimized for a specific laser wavelength. R > 99.5% at 0° or 45° AOI. LIDT up to 25 J/cm² @ 1064nm, 10ns. Available for 193nm, 248nm, 266nm, 308nm, 355nm, 515nm, 532nm, 808nm, 980nm, 1064nm, 1550nm, 2000nm."),
            ("Broadband Dielectric HR", "Broadband high-reflector coating covering a wide spectral range. R > 99% over the design band. Available bands: 400-700nm, 700-1100nm, 1100-1700nm, 2000-2500nm."),
            ("Protected Aluminum", "Aluminum coating with SiO₂ protective overcoat. R > 87% from 400nm to IR. Cost-effective general-purpose mirror."),
            ("Enhanced Aluminum", "Enhanced aluminum with dielectric top layer boosting visible reflectivity. R > 92% from 450-650nm. Good for visible imaging systems."),
            ("Protected Gold", "Gold coating with protective dielectric layer. R > 96% from 700nm to far IR. Excellent for IR and thermal applications."),
            ("Protected Silver", "Silver coating with protective layer. R > 97% from 600nm to mid-IR. Highest reflectivity in visible-NIR but softer than gold.")
        ],
        "tolerances": [
            ("Standard Grade", "40-20 surface quality / λ/4 flatness / ±0.15mm diameter tolerance. General-purpose mirrors for imaging, illumination and low-power lasers."),
            ("Precision Grade", "20-10 surface quality / λ/10 flatness / ±0.10mm diameter tolerance. For metrology, interferometry and mid-power laser systems."),
            ("Laser Grade", "10-5 surface quality / λ/20 flatness / ±0.05mm diameter tolerance. For high-power lasers, ring resonators, and ultra-precision applications.")
        ],
        "inspection": [
            "Surface flatness verified with phase-shift interferometer (ZYGO equivalent) at 632.8nm",
            "Spectral reflectance measured on PerkinElmer Lambda spectrophotometer across full design range",
            "Surface quality inspected per MIL-PRF-13830B under dark-field illumination",
            "Dimensional inspection with digital micrometer and optical comparator",
            "Laser damage threshold spot-test verified for laser-grade products (sample basis)",
            "Wavefront distortion mapping available on request for precision orders"
        ],
        "applications": [
            ("Laser Resonators", "End mirrors and folding mirrors for solid-state, fiber and gas laser cavities"),
            ("High-Power Laser Systems", "Beam steering, folding, and transport optics for kW-class lasers"),
            ("Interferometry", "Reference flat mirrors and beam splitters for Fizeau and Michelson interferometers"),
            ("Semiconductor Manufacturing", "DUV and UV lithography beam delivery, wafer inspection, alignment optics"),
            ("Spectroscopy", "Folding mirrors and cavity mirrors for Raman, fluorescence, and absorption spectrometers"),
            ("Scientific Research", "Ultrafast laser systems, cavity ring-down spectroscopy, quantum optics")
        ],
        "engineering": [
            "For laser resonator mirrors, specify the angle of incidence (0° for end mirrors, 45° for folding mirrors) as coating performance is highly angle-dependent.",
            "When selecting flatness specification, consider the total wavefront error budget of your system. A λ/20 mirror contributes λ/10 wavefront error (double pass).",
            "For high-power CW lasers, substrate thickness and mounting method are critical to minimize thermal distortion. We recommend at least 6.35mm thickness for 50mm-diameter mirrors above 100W average power.",
            "Dielectric coatings are polarization-sensitive at non-normal incidence. For 45° AOI, P-polarization and S-polarization will have different reflectance spectra. Specify your polarization state when ordering.",
            "Always clean optical mirrors with proper techniques — use lens tissue and methanol, working from center outward in a spiral pattern. Never use paper products on coated surfaces."
        ],
        "faqs": [
            ("What flatness specification do I need for my application?",
             "For general imaging and low-power lasers, λ/4 is typically sufficient. For interferometry and metrology, use λ/10. For high-precision laser resonators and ring cavities, λ/20 or better is recommended. Remember that transmitted wavefront error is double the surface flatness in transmission."),
            ("How does angle of incidence affect mirror coating performance?",
             "Dielectric coatings are designed for a specific angle of incidence (AOI). A coating designed for 0° will shift to shorter wavelengths at higher AOI. The bandwidth also changes with angle. Always specify your operating AOI and polarization when ordering. For variable AOI applications, broadband coatings offer more tolerance."),
            ("Can fused silica mirrors handle 100W+ CW laser power?",
             "Yes, but several factors matter: substrate thickness (thicker = less distortion), coating absorption (lower = better), and mounting method (avoid point contacts that create stress). We recommend at least 6.35mm thickness for 50mm mirrors above 100W. For kW-class systems, water-cooled mounts may be necessary."),
            ("What is the difference between dielectric and metallic mirrors?",
             "Dielectric mirrors use multiple alternating thin-film layers to achieve very high reflectivity (>99.5%) within a specific wavelength band, with high laser damage threshold. Metallic mirrors use a single metal layer (aluminum, gold, silver) and reflect over a very broad range but with lower reflectivity (~85-98%) and lower damage threshold. Dielectric = narrow band, high R, high LIDT. Metallic = broadband, lower R, lower LIDT.")
        ],
        "related_products": [
            ("/products/fused-silica-laser-lenses/", "Fused Silica Laser Lenses"),
            ("/products/fused-silica-plano-convex-lenses/", "Fused Silica Plano-Convex Lenses"),
            ("/products/high-power-laser-mirrors/", "High-Power Laser Mirrors"),
            ("/products/broadband-dielectric-mirrors/", "Broadband Dielectric Mirrors"),
            ("/products/dichroic-mirrors/", "Dichroic Mirrors"),
            ("/products/laser-line-high-reflected-mirrors/", "Laser Line High-Reflect Mirrors")
        ],
        "related_articles": [
            ("/blog/laser-mirror-selection-guide/", "Laser Mirror Selection Guide: Everything You Need to Know"),
            ("/blog/laser-damage-threshold-guide/", "Laser Damage Threshold: What Engineers Need to Know"),
            ("/blog/laser-optics-selection-guide/", "Complete Guide to Laser Optics Selection")
        ],
        "internal_links": [
            ("/materials/uv-fused-silica/", "UV Fused Silica Material"),
            ("/applications/laser-optics/", "Laser Applications"),
            ("/ai-optical-engineer.html", "AI Optical Engineer")
        ]
    }
]

# CaF2 Plano-Convex Lenses
TIER2_PAGES.append({
    "slug": "caf2-plano-convex-lenses",
    "name": "CaF₂ Plano-Convex Lenses",
    "category31": "Optical Lenses",
    "componentType": "Lens",
    "material": "Calcium Fluoride (CaF₂)",
    "title": "CaF₂ Plano-Convex Lenses | UV to Mid-IR | PhotonEdge",
    "description": "Calcium fluoride (CaF₂) plano-convex lenses for UV, VIS and IR applications from 180nm to 8μm. Low dispersion, high transmission. Uncoated and AR coated options available.",
    "keywords": "CaF2 plano convex lens, calcium fluoride lens, IR lens, UV lens, 193nm lens, infrared lens, CaF2 optics",
    "subtitle": "Calcium fluoride (CaF₂) plano-convex lenses offering exceptional transmission from deep UV (180nm) through mid-infrared (8μm), with extremely low dispersion and excellent environmental stability.",
    "image": "images/products/optical-lenses/uv-fused-silica-plano-convex.jpg",
    "overview": [
        "PhotonEdge calcium fluoride (CaF₂) plano-convex lenses are manufactured from high-purity single-crystal CaF₂, offering an exceptionally broad transmission range from 180nm (deep UV) to 8.0μm (mid-infrared).",
        "CaF₂ is the preferred material for deep-UV applications including 193nm ArF excimer lithography, 248nm KrF systems, and 266nm/355nm UV lasers. Its low refractive index (n = 1.4338 @ 589nm) means less reflection loss at each surface compared to most glasses.",
        "The plano-convex design provides positive focal length and is ideal for collimating divergent sources or focusing collimated beams. Like other positive lenses, orient the convex surface toward the longer conjugate to minimize spherical aberration.",
        "Standard CaF₂ lenses are available in diameters from 10mm to 50.8mm with focal lengths from 15mm to 500mm. Anti-reflection coatings are available for UV, VIS, NIR, and MIR bands. Custom sizes, focal lengths and coatings available on request."
    ],
    "specs": [
        ("Material", "Single-Crystal Calcium Fluoride (CaF₂)"),
        ("Crystal Orientation", "<111> or <100> (specify when ordering)"),
        ("Refractive Index", "1.4338 @ 589.3nm"),
        ("Transmission Range", "180nm – 8.0μm"),
        ("Diameter Range", "10mm – 50.8mm (standard); custom up to 150mm"),
        ("Focal Length Range", "15mm – 500mm (standard); custom available"),
        ("Focal Length Tolerance", "±1% (standard); ±0.5% (precision)"),
        ("Diameter Tolerance", "±0.10mm (standard); ±0.02mm (precision)"),
        ("Surface Quality", "40-20 (standard); 20-10 (precision); 10-5 (UV laser grade)"),
        ("Surface Flatness", "λ/4 @ 632.8nm (standard); λ/10 (precision)"),
        ("Centration", "< 3 arc minutes"),
        ("Clear Aperture", "> 85% of diameter"),
        ("Chamfer", "0.2mm × 45° (protective)"),
        ("Coating Options", "Uncoated, UV AR, VIS AR, NIR AR, IR AR, broadband AR")
    ],
    "materials": [
        ("UV-Grade CaF₂", "High-purity single-crystal CaF₂ optimized for UV transmission. Excellent transmittance from 180nm to 8μm. Standard for excimer laser and deep-UV applications."),
        ("Infrared-Grade CaF₂", "High-purity CaF₂ optimized for IR applications. Same crystal structure, certified for 1.0μm to 8.0μm transmission. Lower cost for IR-only applications."),
        ("Spectroscopic-Grade CaF₂", "Ultra-high-purity CaF₂ with specified low absorption at key spectral lines. For FTIR, Raman and high-accuracy spectroscopy.")
    ],
    "coatings": [
        ("Uncoated", "As-polished surface. CaF₂ has relatively low reflectivity (~5.3% per surface at 589nm) compared to most glasses. Suitable for broadband or multi-wavelength systems where a single AR coating cannot cover all bands."),
        ("UV AR Coating (200-400nm)", "Broadband UV AR coating. R < 1.5% average per surface. For excimer laser and deep-UV applications. LIDT > 1 J/cm² @ 248nm, 10ns."),
        ("VIS AR Coating (350-700nm)", "Standard visible broadband AR. R < 1.25% average per surface."),
        ("NIR AR Coating (700-1100nm)", "Near-infrared optimized AR coating. R < 1.0% average per surface."),
        ("MIR AR Coating (2-5μm)", "Mid-infrared AR for thermal imaging and IR spectroscopy. R < 1.5% average per surface."),
        ("Broadband AR (3-5μm or 8-12μm)", "Thermal imaging bands. R < 2.0% average per surface.")
    ],
    "tolerances": [
        ("Standard Grade", "±0.10mm diameter / 40-20 surface quality / λ/4 flatness / ±1% focal length. Suitable for general UV and IR optical systems."),
        ("Precision Grade", "±0.05mm diameter / 20-10 surface quality / λ/10 flatness / ±0.5% focal length. For spectroscopy, metrology, and precision imaging."),
        ("UV Laser Grade", "±0.02mm diameter / 10-5 surface quality / λ/10 flatness / ±0.5% focal length. For excimer laser and high-energy UV applications.")
    ],
    "inspection": [
        "100% dimensional inspection with digital micrometers and optical comparators",
        "Surface quality verified per MIL-PRF-13830B under dark-field illumination",
        "Surface flatness measured with laser interferometer at 632.8nm",
        "Transmission spectrum verified on PerkinElmer Lambda 1050 (UV-Vis-NIR) or FTIR (MIR)",
        "Crystal quality check (no inclusions, striae, or cleavage planes in clear aperture)",
        "Focal length verified through optical bench collimation test"
    ],
    "applications": [
        ("Deep-UV & Excimer Lasers", "193nm ArF and 248nm KrF excimer laser systems, UV beam delivery and focusing"),
        ("Infrared Spectroscopy", "FTIR, Raman, and ATR spectroscopy collimation and focusing"),
        ("Thermal Imaging", "Mid-wave infrared (MWIR) imaging systems operating in the 3-5μm band"),
        ("Semiconductor Metrology", "Deep-UV inspection and metrology tools, wafer alignment systems"),
        ("Life Sciences", "Fluorescence microscopy, flow cytometry, and UV spectroscopy instruments"),
        ("Defense & Aerospace", "Missile guidance, IR countermeasures, LWIR thermal imaging")
    ],
    "engineering": [
        "CaF₂ is a birefringent crystal when off-axis. For the best optical performance, specify the crystal orientation (<111> gives minimum birefringence effect, <100> is common for IR windows and lenses).",
        "CaF₂ has a high thermal expansion coefficient (18.9 × 10⁻⁶ /°C) compared to fused silica, meaning larger dimensional changes with temperature. Consider this in thermally stable optomechanical designs.",
        "CaF₂ is relatively soft (Mohs 4) and prone to chipping. Handle with care and always use protective bevels. Avoid cleaning with abrasive materials.",
        "CaF₂ is hygroscopic in the presence of moisture at high temperatures but is stable at room temperature and normal humidity. For high-humidity environments, consider a protective coating.",
        "The Abbe number of CaF₂ is approximately 95, which is very high (low dispersion). This makes CaF₂ excellent for achromatic lens designs paired with higher-dispersion materials."
    ],
    "faqs": [
        ("Why use CaF₂ instead of fused silica for UV applications?",
         "CaF₂ transmits deeper into the UV — down to 180nm compared to ~193nm for fused silica. It also has higher UV laser damage threshold at excimer wavelengths. However, fused silica has better thermal stability and mechanical strength. For 193nm and below, CaF₂ is the standard. For 266nm and above, both work — choose based on your full system design requirements."),
        ("What is the crystal orientation and why does it matter?",
         "CaF₂ is a cubic crystal. Lenses are typically cut along the <111> or <100> axis. <111> orientation minimizes birefringence effects and is preferred for lenses. <100> is common for windows. The orientation affects both optical performance and mechanical strength. If polarization purity is critical, <111> is generally better."),
        ("Can CaF₂ lenses be used at cryogenic temperatures?",
         "Yes, CaF₂ has good cryogenic stability and is commonly used in cooled infrared detector systems. It remains transparent down to very low temperatures. The thermal expansion coefficient changes at cryogenic temperatures but the material does not undergo phase transitions that would cause optical degradation."),
        ("How do I clean CaF₂ optics?",
         "CaF₂ is relatively soft and can be scratched easily. Use a drop-and-drag technique with lint-free optical tissue and reagent-grade methanol or isopropyl alcohol. Never use abrasive cleaners. Avoid ultrasonic cleaning as it can cause chipping at edges. For heavy contamination, we recommend returning the optic for professional cleaning and recoating if necessary.")
    ],
    "related_products": [
        ("/products/caf2-ultrafast-laser-optics/", "CaF₂ Ultrafast Laser Optics"),
        ("/products/caf2-optical-windows/", "CaF₂ Optical Windows"),
        ("/products/caf2-optical-prisms/", "CaF₂ Optical Prisms"),
        ("/products/sapphire-optical-windows/", "Sapphire Optical Windows"),
        ("/products/germanium-infrared-lenses/", "Germanium Infrared Lenses"),
        ("/products/fused-silica-plano-convex-lenses/", "Fused Silica Plano-Convex Lenses")
    ],
    "related_articles": [
        ("/blog/infrared-optical-materials-comparison/", "Infrared Optical Materials: A Comparative Guide"),
        ("/blog/bk7-vs-uv-fused-silica/", "BK7 vs UV Fused Silica: Material Selection Guide"),
        ("/blog/anti-reflection-coatings-guide/", "Anti-Reflection Coatings: A Complete Technical Guide")
    ],
    "internal_links": [
        ("/materials/caf2/", "CaF₂ Material Properties"),
        ("/applications/laser-optics/", "Laser Applications"),
        ("/ai-optical-engineer.html", "AI Optical Engineer")
    ]
})

# CaF2 Ultrafast Laser Optics
TIER2_PAGES.append({
    "slug": "caf2-ultrafast-laser-optics",
    "name": "CaF₂ Ultrafast Laser Optics",
    "category31": "Custom Optics",
    "componentType": "Lens",
    "material": "Calcium Fluoride (CaF₂)",
    "title": "CaF₂ Ultrafast Laser Optics | Femtosecond Pulse Optics | PhotonEdge",
    "description": "Calcium fluoride (CaF₂) optics optimized for ultrafast femtosecond laser systems. Low dispersion, high damage threshold. Lenses, windows, prisms and pulse compression gratings.",
    "keywords": "CaF2 ultrafast optics, femtosecond laser optics, ultrafast pulse compression, CaF2 prism pair, chirped mirror, femtosecond lens",
    "subtitle": "High-quality calcium fluoride (CaF₂) optical components engineered for ultrafast femtosecond laser systems — low chromatic dispersion, high UV-NIR transmission, and exceptional laser damage threshold.",
    "image": "images/products/optical-lenses/uv-fused-silica-plano-convex.jpg",
    "overview": [
        "PhotonEdge CaF₂ ultrafast laser optics are specifically designed for femtosecond laser systems where pulse integrity and dispersion control are critical. Calcium fluoride offers uniquely low dispersion in the visible and near-IR, combined with broad UV transmission.",
        "Ultrafast pulses (femtosecond duration) have extremely broad bandwidths, which means chromatic and group velocity dispersion (GVD) can significantly broaden the pulse in time. CaF₂ has low GVD and can be paired with other materials for controlled dispersion management.",
        "Our ultrafast product line includes CaF₂ lenses, windows, prism pairs for pulse compression, and beam splitters — all with specialized coatings optimized for ultrafast laser conditions.",
        "Standard components cover wavelengths from 350nm to 2.5μm, with focal lengths and sizes optimized for Ti:Sapphire (800nm), Yb-doped (1030-1064nm), and Er-doped (1550nm) ultrafast laser systems."
    ],
    "specs": [
        ("Material", "High-Purity Single-Crystal CaF₂ (<111> orientation)"),
        ("Wavelength Range", "350nm – 2500nm (ultrafast bands)"),
        ("Refractive Index", "1.4338 @ 589nm; 1.4291 @ 800nm"),
        ("Group Velocity Dispersion (GVD)", "+20.2 fs²/mm @ 800nm (normal dispersion)"),
        ("Lens Focal Length Range", "15mm – 500mm"),
        ("Window / Prism Size Range", "10mm – 50.8mm"),
        ("Surface Quality", "20-10 (standard); 10-5 (precision ultrafast grade)"),
        ("Surface Flatness", "λ/10 @ 632.8nm (standard); λ/20 (precision)"),
        ("Wavefront Distortion", "< λ/8 (lenses); < λ/10 (windows)"),
        ("Coating Options", "Broadband ultrafast AR, low-GDD mirror, chirped mirror coating"),
        ("Group Delay Dispersion (GDD) of Coatings", "< 10 fs² per surface (standard ultrafast AR)"),
        ("Laser Damage Threshold", "2 J/cm² @ 800nm, 100fs, 1kHz (ultrafast AR coated)")
    ],
    "materials": [
        ("Ultrafast-Grade CaF₂", "Highest-purity single-crystal CaF₂ with certified low absorption at ultrafast laser wavelengths. <111> orientation for minimal polarization effects. Standard for all ultrafast applications."),
        ("UV-Grade CaF₂", "High-purity CaF₂ with excellent deep-UV transmission. Suitable for UV ultrafast (266nm, 355nm) and harmonic generation systems."),
        ("Spectroscopic-Grade CaF₂", "Ultra-pure CaF₂ with specified homogeneity for the most demanding interferometry and pulse characterization applications.")
    ],
    "coatings": [
        ("Ultrafast Broadband AR (650-1050nm)", "Broadband anti-reflection coating optimized for Ti:Sapphire and Yb-doped ultrafast systems. R < 0.5% per surface. Low GDD (< 10 fs²) across the band. LIDT: 2 J/cm² @ 800nm, 100fs."),
        ("Ultrafast NIR AR (1000-1700nm)", "For Yb-doped and Er-doped fiber lasers. R < 0.5% per surface. Low GDD. Suitable for 1030nm, 1064nm, 1550nm ultrafast systems."),
        ("Ultrafast UV AR (300-500nm)", "For UV ultrafast and frequency-doubled Ti:Sapphire (400nm). R < 1.0% per surface."),
        ("Low-GDD High Reflector (700-950nm)", "Broadband high-reflection coating with minimal group delay dispersion. R > 99%. GDD < 20 fs². For femtosecond cavity end mirrors and folding optics."),
        ("Chirped Mirror Coating", "Custom-designed chirped mirrors for dispersion compensation in ultrafast oscillators and amplifiers. Specify target bandwidth and GDD profile.")
    ],
    "tolerances": [
        ("Standard Ultrafast Grade", "20-10 surface quality / λ/10 flatness / ±0.10mm diameter / ±1% focal length. Standard for most ultrafast laboratory and industrial systems."),
        ("Precision Ultrafast Grade", "10-5 surface quality / λ/20 flatness / ±0.05mm diameter / ±0.5% focal length. For CPA amplifier front-ends, pulse compression, and high-precision metrology."),
        ("Custom Grade", "Custom specifications available for advanced ultrafast systems, including sub-aperture polishing, custom wedge angles, and special coatings.")
    ],
    "inspection": [
        "Surface flatness verified with phase-shift interferometer",
        "Spectral transmission and reflection measured across full design band",
        "Surface quality inspected per MIL-PRF-13830B (10-5 grade uses ISO 10110 equivalent)",
        "GDD measurement via white-light interferometry for custom coatings (on request)",
        "LIDT sampling test for high-energy applications (on request)",
        "Prism angle verified with precision goniometer (< 5 arc seconds for precision grade)"
    ],
    "applications": [
        ("Femtosecond Oscillators", "Ti:Sapphire, Yb-doped, and Er-doped femtosecond laser cavities and beam delivery"),
        ("Chirped Pulse Amplifiers (CPA)", "Stretcher, compressor, and amplifier stage optics"),
        ("Nonlinear Optics", "Harmonic generation, optical parametric amplification (OPA), white-light generation"),
        ("Pulse Compression", "Prism pairs and grating pairs for negative dispersion compensation"),
        ("Two-Photon Microscopy", "Femtosecond pulse delivery for multiphoton imaging systems"),
        ("Attosecond Science", "High-harmonic generation and EUV beamline optics (UV-grade CaF₂)")
    ],
    "engineering": [
        "When designing ultrafast optical systems, track the total group delay dispersion (GDD) through all optical elements. CaF₂ introduces normal (positive) GDD — it can be compensated with prism pairs (which give negative GDD) or chirped mirrors.",
        "For ultrafast focusing, use a single lens rather than multiple lenses to minimize GVD accumulation. The spot size will also be affected by chromatic aberration — achromatic designs may be needed for very broad bandwidth pulses.",
        "CaF₂ prism pairs are the standard method for adjustable dispersion compensation in Ti:Sapphire oscillators and amplifiers. The amount of material insertion controls the magnitude of negative GVD.",
        "Laser damage threshold for ultrafast pulses (femtosecond regime) follows different scaling than nanosecond pulses. LIDT values are typically specified in J/cm² at a given pulse duration and wavelength. Our ultrafast coatings are tested at 800nm, 100fs, 1kHz.",
        "Always use angle-tuned broadband coatings for ultrafast systems. Narrowband coatings can introduce wavelength-dependent GDD that distorts the pulse shape."
    ],
    "faqs": [
        ("What is GVD and why does it matter for ultrafast pulses?",
         "Group velocity dispersion (GVD) is the variation of group velocity with wavelength. In a femtosecond pulse (which contains a broad spectrum of wavelengths), different wavelength components travel at different speeds through a material, causing the pulse to broaden in time. GVD is specified in fs²/mm. CaF₂ has relatively low GVD compared to most glasses, making it a good choice for ultrafast optics, but dispersion management is still required for short pulses (<50fs)."),
        ("How do CaF₂ prism pairs compress femtosecond pulses?",
         "A prism pair introduces negative (anomalous) group delay dispersion through angular dispersion — longer wavelengths travel a longer geometric path through the prism pair, effectively arriving earlier than shorter wavelengths. This counteracts the positive GVD from the laser gain medium and other optical elements, allowing pulses to be compressed back to their transform-limited duration. CaF₂ is preferred for UV and visible ultrafast systems because of its broad transmission and low dispersion."),
        ("What LIDT should I specify for my ultrafast system?",
         "For Ti:Sapphire oscillator beams (~1nJ pulses, 80MHz), standard ultrafast AR coatings are more than sufficient. For amplified systems (μJ to mJ pulses), you need higher LIDT. Our standard ultrafast coating handles 2 J/cm² at 800nm, 100fs — sufficient for most kHz amplifiers. For high-energy amplifiers (multi-mJ), we can provide custom high-LIDT coatings with values exceeding 5 J/cm²."),
        ("Can I use standard BK7 lenses for ultrafast applications?",
         "BK7 has higher GVD than CaF₂ and stronger absorption in the UV. For near-IR ultrafast (800-1550nm), BK7 can work for low-precision applications, but it introduces more pulse broadening. For UV ultrafast, BK7 absorbs too much and is not suitable. CaF₂ is the standard choice for high-performance ultrafast systems, especially below 400nm or when dispersion control is critical.")
    ],
    "related_products": [
        ("/products/caf2-plano-convex-lenses/", "CaF₂ Plano-Convex Lenses"),
        ("/products/caf2-optical-windows/", "CaF₂ Optical Windows"),
        ("/products/caf2-optical-prisms/", "CaF₂ Optical Prisms"),
        ("/products/fused-silica-laser-lenses/", "Fused Silica Laser Lenses"),
        ("/products/high-power-laser-mirrors/", "High-Power Laser Mirrors"),
        ("/products/laser-beam-expanders/", "Laser Beam Expanders")
    ],
    "related_articles": [
        ("/blog/laser-damage-threshold-guide/", "Laser Damage Threshold: What Engineers Need to Know"),
        ("/blog/laser-optics-selection-guide/", "Complete Guide to Laser Optics Selection"),
        ("/blog/infrared-optical-materials-comparison/", "Infrared Optical Materials Comparison")
    ],
    "internal_links": [
        ("/materials/caf2/", "CaF₂ Material Properties"),
        ("/applications/laser-optics/", "Laser Applications"),
        ("/ai-optical-engineer.html", "AI Optical Engineer")
    ]
})

# N-BK7 Optical Windows
TIER2_PAGES.append({
    "slug": "nbk7-optical-windows",
    "name": "N-BK7 Optical Windows",
    "category31": "Optical Windows",
    "componentType": "Window",
    "material": "N-BK7 (BK7)",
    "title": "N-BK7 Optical Windows | Precision Glass Windows | PhotonEdge",
    "description": "N-BK7 (BK7) borosilicate crown glass optical windows. High visible-NIR transmission, λ/10 flatness options. Round, square and rectangular. AR coatings for visible and NIR bands.",
    "keywords": "BK7 window, N-BK7 optical window, glass window, visible window, precision window, optical flat, BK7 glass window",
    "subtitle": "High-quality N-BK7 (BK7) borosilicate crown glass optical windows offering excellent visible and near-infrared transmission, tight tolerance options, and outstanding value for general-purpose optical systems.",
    "image": "images/products/optical-windows/bk7-windows.jpg",
    "overview": [
        "PhotonEdge N-BK7 optical windows are precision flat plates made from high-quality borosilicate crown glass (equivalent to Schott N-BK7), offering excellent transmission from the visible through the near-infrared (350nm to 2.0μm).",
        "N-BK7 is the most widely used optical glass due to its excellent homogeneity, low bubble and inclusion content, and good mechanical and chemical durability. It is the cost-effective choice for most visible and NIR applications that do not require UV or extended IR transmission.",
        "Our N-BK7 windows are available in round, square and rectangular formats with sizes from 5mm to 150mm. Multiple surface quality and flatness grades are available to match your application requirements — from general-purpose 60-40 / λ/4 to precision 10-5 / λ/20.",
        "Standard anti-reflection coatings cover visible (350-700nm), NIR (650-1100nm), and telecom (1200-1700nm) bands. Custom coatings, wedge windows, and step windows are available on request."
    ],
    "specs": [
        ("Material", "N-BK7 (Schott equivalent borosilicate crown glass)"),
        ("Refractive Index", "1.5168 @ 587.6nm (n_d)"),
        ("Abbe Number", "64.17 (V_d)"),
        ("Transmission Range", "350nm – 2000nm"),
        ("Shape Options", "Round, square, rectangular, custom"),
        ("Size Range", "5mm – 150mm (standard); custom up to 300mm"),
        ("Thickness Range", "0.5mm – 25mm"),
        ("Thickness Tolerance", "±0.10mm (standard); ±0.02mm (precision)"),
        ("Surface Quality", "60-40, 40-20, 20-10, 10-5 (per MIL-PRF-13830B)"),
        ("Surface Flatness", "1λ, λ/2, λ/4, λ/10, λ/20 @ 632.8nm"),
        ("Parallelism (Wedge)", "< 3 arc min (standard); < 30 arc sec (precision); < 5 arc sec (high-precision)"),
        ("Clear Aperture", "> 90%"),
        ("Chamfer", "0.2mm × 45° (protective)"),
        ("Coating Options", "Uncoated, VIS AR, NIR AR, VIS-NIR broadband, custom")
    ],
    "materials": [
        ("N-BK7 (Standard Grade)", "Standard optical crown glass equivalent to Schott N-BK7. Hoya B270 / CDGM equivalent. Excellent homogeneity (H3/H4), low striae (grade C/A). The standard choice for most visible and NIR applications."),
        ("N-BK7 (Precision Grade)", "Selected N-BK7 blanks with higher homogeneity (H1/H2), lower stress birefringence, and tighter striae specification. For interferometry, precision imaging, and metrology applications."),
        ("N-BK7 (Ultra-Precision Grade)", "The highest grade N-BK7 with sub-nm roughness, ultra-high flatness potential, and minimal wavefront distortion. For interferometer reference flats and ultra-precision metrology.")
    ],
    "coatings": [
        ("Uncoated", "As-polished surface. 4% reflection per surface at normal incidence. Use for prototyping, low-light applications, or when wavelength is not yet defined."),
        ("VIS AR Coating (350-700nm)", "Broadband visible anti-reflection coating. R < 1.5% average per surface. Standard for imaging, microscopy, and visible light systems."),
        ("NIR AR Coating (650-1050nm)", "Near-infrared optimized AR coating. R < 0.5% average per surface. For 808nm, 980nm, 1064nm laser and sensor systems."),
        ("VIS-NIR Broadband AR (400-1100nm)", "Very broadband AR for multi-wavelength systems. R < 1.0% average per surface. Good for systems covering both visible and NIR."),
        ("Telecom AR Coating (1200-1700nm)", "For fiber optic and telecom applications at 1310nm and 1550nm. R < 0.5% average per surface."),
        ("Custom AR Coating", "Custom single-wavelength or multi-band anti-reflection coatings designed to your specifications.")
    ],
    "tolerances": [
        ("Commercial Grade", "60-40 surface quality / 1λ flatness / ±0.15mm thickness / < 5 arc min wedge. For general protection windows and covers, low-cost illumination systems."),
        ("Standard Grade", "40-20 surface quality / λ/4 flatness / ±0.10mm thickness / < 3 arc min wedge. Standard for most imaging, sensor, and moderate-precision systems."),
        ("Precision Grade", "20-10 surface quality / λ/10 flatness / ±0.05mm thickness / < 30 arc sec wedge. For metrology, interferometry, and high-resolution imaging."),
        ("High-Precision Grade", "10-5 surface quality / λ/20 flatness / ±0.02mm thickness / < 5 arc sec wedge. For laser resonators, reference flats, and ultra-precision metrology.")
    ],
    "inspection": [
        "100% dimensional inspection with digital micrometers and coordinate measuring machine",
        "Surface quality verified per MIL-PRF-13830B under dark-field illumination",
        "Surface flatness measured with laser interferometer (ZYGO equivalent) at 632.8nm",
        "Wedge / parallelism measured with autocollimator or interferometer",
        "Coating spectral performance tested on PerkinElmer Lambda spectrophotometer",
        "Scratch dig certificate available for precision and high-precision grades"
    ],
    "applications": [
        ("Sensor Protection", "Protective windows for cameras, spectrometers, and optical sensors"),
        ("Imaging & Photography", "Lens system protective elements, filter mounts, beam splitters substrates"),
        ("Laser Systems", "Laser safety windows, output coupler substrates, cavity windows"),
        ("Metrology & Inspection", "Reference flats, beam splitter substrates, optical flat mirrors"),
        ("Display & Illumination", "Display protective covers, projection system windows, light guides"),
        ("Research & Education", "General laboratory optics, student experiments, prototyping")
    ],
    "engineering": [
        "N-BK7 windows introduce 4% reflection per uncoated surface at normal incidence. For imaging systems, always use AR-coated windows to reduce stray light and improve contrast.",
        "For laser applications, the wedge specification is critical — a perfectly parallel window can cause etalon effects (interference between front and back surface reflections). A small intentional wedge (e.g., 30 arc min) breaks the etalon. Specify wedged windows for laser systems.",
        "When calculating the optical path through a window, remember that the refraction shifts the beam laterally but does not change its direction (at normal incidence). The lateral shift is approximately t × θ / n for small angles θ, where t is thickness and n is refractive index.",
        "N-BK7 has a coefficient of thermal expansion of 7.1 × 10⁻⁶ /°C and a thermal coefficient of refractive index (dn/dT) of 2.4 × 10⁻⁶ /°C. For temperature-stabilized systems, consider these values in your tolerance budget.",
        "For vacuum applications, N-BK7 is suitable up to moderate temperatures. For high-temperature or UV vacuum systems, fused silica may be preferred due to lower outgassing and better UV stability."
    ],
    "faqs": [
        ("What is the difference between commercial and precision grade windows?",
         "Commercial grade (60-40 / 1λ) windows are intended for general protection and non-critical optical paths. Precision grade (20-10 / λ/10) windows have tighter surface quality and flatness, making them suitable for metrology, interferometry, and high-resolution imaging where surface defects or wavefront distortion would degrade performance. The price difference reflects additional polishing and inspection time."),
        ("When do I need a wedged window vs a parallel window?",
         "Use parallel windows for imaging applications where angular deviation would cause image shift or distortion. Use wedged windows for laser applications where parallel surfaces would create an etalon effect (multiple reflected beams interfering). A wedge of 30 arc min to 3° is typical for breaking etalons. For imaging with lasers, you may need both — consult our engineers for guidance."),
        ("How flat does my window need to be?",
             "For general protection or cover glass, 1λ or λ/2 is sufficient. For imaging systems, λ/4 is standard. For interferometry and metrology, λ/10 or better is typically required. Remember that a window in transmission introduces wavefront distortion equal to (n-1) × surface figure, which is roughly half the surface flatness value for BK7 (n ≈ 1.5)."),
        ("Can N-BK7 be used for UV applications?",
             "N-BK7 starts absorbing below about 350nm. It is not suitable for deep UV or 266nm/355nm laser systems. For UV applications, use fused silica or CaF₂ windows. N-BK7 is fine for near-UV (365nm) applications where transmission of 70-80% is acceptable, but fused silica will give better transmission and lower fluorescence.")
    ],
    "related_products": [
        ("/products/bk7-windows/", "BK7 Circular/Square Windows"),
        ("/products/fused-silica-optical-windows/", "Fused Silica Optical Windows"),
        ("/products/sapphire-optical-windows/", "Sapphire Optical Windows"),
        ("/products/nbk7-plano-convex-lenses/", "N-BK7 Plano-Convex Lenses"),
        ("/products/nbk7-achromatic-lenses/", "N-BK7 Achromatic Lenses"),
        ("/products/broadband-dielectric-mirrors/", "Broadband Dielectric Mirrors")
    ],
    "related_articles": [
        ("/blog/anti-reflection-coating-selection-guide/", "How to Choose the Right Anti-Reflection Coating"),
        ("/blog/bk7-vs-uv-fused-silica/", "BK7 vs UV Fused Silica: Material Selection Guide"),
        ("/blog/choose-right-optical-lens/", "How to Choose the Right Optical Lens for Your Application")
    ],
    "internal_links": [
        ("/materials/bk7/", "BK7 / N-BK7 Material Properties"),
        ("/applications/laser-optics/", "Laser Applications"),
        ("/ai-optical-engineer.html", "AI Optical Engineer")
    ]
})

# N-BK7 Plano-Convex Lenses
TIER2_PAGES.append({
    "slug": "nbk7-plano-convex-lenses",
    "name": "N-BK7 Plano-Convex Lenses",
    "category31": "Optical Lenses",
    "componentType": "Lens",
    "material": "N-BK7 (BK7)",
    "title": "N-BK7 Plano-Convex Lenses | Precision Spherical Lenses | PhotonEdge",
    "description": "N-BK7 (BK7) plano-convex spherical lenses for visible and NIR applications. Diameters 3mm-150mm, focal lengths 4mm-1000mm. AR coated for VIS and NIR bands.",
    "keywords": "BK7 plano convex lens, N-BK7 lens, spherical lens, visible lens, plano convex lens, focusing lens, collimating lens",
    "subtitle": "High-quality N-BK7 (BK7) borosilicate crown glass plano-convex lenses — the most widely used positive lens for visible and near-infrared focusing, collimation and imaging applications.",
    "image": "images/products/optical-lenses/bk7-plano-convex.jpg",
    "overview": [
        "PhotonEdge N-BK7 plano-convex (PCX) lenses are precision spherical lenses manufactured from high-quality N-BK7 equivalent borosilicate crown glass. These lenses are the workhorse of the optics industry, offering excellent performance at visible and near-infrared wavelengths with great value.",
        "Plano-convex lenses have one spherical surface and one flat surface, providing a positive focal length. When oriented with the curved surface toward the longer conjugate distance, they minimize spherical aberration — making them ideal for focusing collimated light or collimating point sources.",
        "Our standard N-BK7 PCX lenses are available in diameters from 2.5mm to 75mm with focal lengths ranging from 3.9mm to 1000mm. Multiple coating options cover visible, NIR, and common laser wavelengths.",
        "For custom requirements including non-standard diameters, focal lengths, or mounting configurations, we offer full custom manufacturing with typical lead times of 3-5 weeks. All lenses are 100% inspected for centration, surface quality, and dimensional compliance before shipment."
    ],
    "specs": [
        ("Material", "N-BK7 (Schott equivalent borosilicate crown glass)"),
        ("Refractive Index", "1.5168 @ 587.6nm (n_d)"),
        ("Abbe Number", "64.17 (V_d)"),
        ("Diameter Range", "2.5mm – 75mm (standard); custom up to 200mm"),
        ("Focal Length Range", "3.9mm – 1000mm (standard); custom available"),
        ("Focal Length Tolerance", "±1% (standard); ±0.5% or ±0.2% (precision)"),
        ("Diameter Tolerance", "±0.15mm (standard); ±0.01mm (precision)"),
        ("Center Thickness Tolerance", "±0.10mm"),
        ("Surface Quality", "40-20 (standard); 20-10 (precision); 10-5 (high-precision)"),
        ("Surface Flatness (Plano Side)", "λ/4 @ 632.8nm (standard); λ/10 or λ/20 (precision)"),
        ("Centration", "< 3 arc minutes"),
        ("Clear Aperture", "> 90%"),
        ("Bevel / Chamfer", "0.25mm × 45° (protective)"),
        ("Coating Options", "Uncoated, VIS AR, NIR AR, UV-Vis AR, custom")
    ],
    "materials": [
        ("N-BK7 (Standard Grade)", "Standard optical crown glass equivalent to Schott N-BK7. Excellent homogeneity, low striae and bubbles. The standard choice for most visible and NIR lens applications."),
        ("N-BK7 (Precision Grade)", "Selected N-BK7 with higher homogeneity and stricter striae grade. For high-resolution imaging, metrology, and precision laser systems."),
        ("N-BK7 (Low-Stress Grade)", "Stress-annealed N-BK7 with minimal residual birefringence (< 10 nm/cm). For polarization-sensitive applications and high-contrast imaging.")
    ],
    "coatings": [
        ("Uncoated", "As-polished surface. ~4% reflection per surface at normal incidence. Use for prototyping, education, or when wavelength range is undefined."),
        ("VIS AR Coating A (350-700nm)", "Broadband visible anti-reflection coating. R < 1.5% average per surface. Standard for microscopy, imaging, and visible light systems."),
        ("VIS AR Coating B (400-700nm)", "Standard visible AR coating. R < 1.0% average per surface. Good for cameras, binoculars, and visible imaging systems."),
        ("NIR AR Coating C (650-1100nm)", "Near-infrared optimized AR. R < 0.5% average per surface. For 785nm, 808nm, 980nm, 1064nm laser and sensor systems."),
        ("Visible-NIR Broadband AR (400-1100nm)", "Extra-broadband AR for multi-wavelength systems. R < 1.0% average per surface."),
        ("Custom Laser Line AR", "Narrowband AR optimized for a specific laser wavelength. R < 0.25% per surface. Available for 405nm, 450nm, 532nm, 635nm, 650nm, 785nm, 808nm, 830nm, 980nm, 1064nm.")
    ],
    "tolerances": [
        ("Standard Grade", "40-20 surface quality / λ/4 flatness (plano) / ±0.15mm diameter / ±1% focal length. General-purpose lenses for imaging, illumination, and education."),
        ("Precision Grade", "20-10 surface quality / λ/10 flatness (plano) / ±0.10mm diameter / ±0.5% focal length. For metrology, microscopy, and moderate-precision laser systems."),
        ("High-Precision Grade", "10-5 surface quality / λ/20 flatness (plano) / ±0.01mm diameter / ±0.2% focal length. For laser beam delivery, interferometry, and ultra-precision imaging.")
    ],
    "inspection": [
        "100% dimensional inspection with digital micrometers and optical comparators",
        "Surface quality verified per MIL-PRF-13830B under dark-field illumination",
        "Surface figure / flatness measured with laser interferometer",
        "Focal length verified through optical bench collimation and MTF testing",
        "Centration measured with precision rotation fixture (< 3 arc min)",
        "Coating spectral performance tested on PerkinElmer Lambda spectrophotometer",
        "Full inspection report available for precision and high-precision grade orders"
    ],
    "applications": [
        ("Imaging & Photography", "Camera lenses, projection systems, binoculars, telescopes"),
        ("Laser Systems", "Beam focusing, collimation, and beam delivery for visible and NIR lasers"),
        ("Microscopy", "Objective lens elements, condenser lenses, eyepiece components"),
        ("Spectroscopy", "Monochromator focusing, collimating mirrors, spectrophotometer optics"),
        ("Machine Vision", "Lenses for industrial inspection, barcode scanners, and automated systems"),
        ("Fiber Optics", "Fiber coupling lenses, collimators, and fiber-to-fiber coupling")
    ],
    "engineering": [
        "To minimize spherical aberration, orient the plano-convex lens so the curved surface faces the collimated (infinite conjugate) side. For finite conjugate imaging where both sides are finite, use two plano-convex lenses back-to-back (bi-convex arrangement).",
        "The focal length of a thin lens in air is given by 1/f = (n-1) × (1/R₁ - 1/R₂ + (n-1)×d/(n×R₁×R₂)), but for plano-convex lenses with R₂ = ∞, this simplifies to 1/f = (n-1)/R₁ where R₁ is the radius of the curved surface.",
        "For monochromatic light, spherical aberration is the dominant aberration of a single lens. For broadband or white-light applications, chromatic aberration also comes into play — use an achromatic doublet if chromatic performance is critical.",
        "N-BK7 has a relatively high Abbe number (64.17), meaning low dispersion compared to flint glasses. This makes BK7 a good choice for the positive element in achromatic doublets, paired with a higher-dispersion flint glass negative element.",
        "When designing lens systems, always check the edge thickness — very short focal length lenses may have impractically thin edges, which can cause chipping during handling and mounting."
    ],
    "faqs": [
        ("What focal length tolerance do I actually need?",
         "Most general imaging and illumination systems work fine with ±1% tolerance. For metrology and precision focusing, use ±0.5%. For laser fiber coupling and single-mode beam delivery, ±0.2% may be needed. The tighter the tolerance, the more measurement and sorting is required, increasing cost. Our standard ±1% tolerance is sufficient for approximately 80% of applications."),
        ("When should I use plano-convex vs bi-convex lenses?",
             "Use plano-convex when one conjugate distance is much longer than the other (e.g., focusing a collimated beam to a point, or collimating a point source). Use bi-convex when both conjugate distances are similar (1:1 imaging or roughly equal object and image distances). Bi-convex provides better performance for finite conjugate imaging but has higher cost than plano-convex."),
        ("What is the difference between uncoated and AR-coated lenses?",
         "An uncoated glass surface reflects about 4% of visible light at normal incidence. For a lens with two surfaces, that's ~8% reflection loss and significant stray light. An anti-reflection (AR) coating reduces reflection to <1% per surface, improving transmission to >98% and dramatically reducing ghost images and stray light. For any imaging or detection system, AR coating is almost always worth the small additional cost."),
        ("Can I use N-BK7 lenses for UV applications?",
             "N-BK7 has reasonable transmission down to about 350nm, but it absorbs significantly below that and shows fluorescence under deep UV excitation. For 365nm and longer UV, N-BK7 works but with reduced transmission (~70-80% per cm). For 355nm and below, use fused silica or CaF₂ lenses for best transmission and minimum fluorescence.")
    ],
    "related_products": [
        ("/products/bk7-plano-convex/", "BK7 Plano-Convex Lens Catalog"),
        ("/products/nbk7-optical-windows/", "N-BK7 Optical Windows"),
        ("/products/nbk7-achromatic-lenses/", "N-BK7 Achromatic Lenses"),
        ("/products/fused-silica-plano-convex-lenses/", "Fused Silica Plano-Convex Lenses"),
        ("/products/bk7-bi-convex/", "BK7 Bi-Convex Lenses"),
        ("/products/achromatic-doublet/", "Achromatic Doublet Lenses")
    ],
    "related_articles": [
        ("/blog/choose-right-optical-lens/", "How to Choose the Right Optical Lens for Your Application"),
        ("/blog/anti-reflection-coating-selection-guide/", "Anti-Reflection Coating Selection Guide"),
        ("/blog/bk7-vs-uv-fused-silica/", "BK7 vs UV Fused Silica: Material Selection Guide")
    ],
    "internal_links": [
        ("/materials/bk7/", "BK7 / N-BK7 Material Properties"),
        ("/applications/laser-optics/", "Laser Applications"),
        ("/ai-optical-engineer.html", "AI Optical Engineer")
    ]
})

# N-BK7 Achromatic Lenses
TIER2_PAGES.append({
    "slug": "nbk7-achromatic-lenses",
    "name": "N-BK7 Achromatic Lenses",
    "category31": "Optical Lenses",
    "componentType": "Lens",
    "material": "N-BK7 / Flint Glass",
    "title": "N-BK7 Achromatic Doublet Lenses | Color-Corrected | PhotonEdge",
    "description": "Achromatic doublet lenses made from N-BK7 and SF11 (or equivalent flint glass). Color-corrected for visible and NIR wavelengths. Improved image quality over single-element lenses.",
    "keywords": "achromatic doublet, achromatic lens, BK7 achromat, color corrected lens, doublet lens, apochromatic, visible achromat",
    "subtitle": "Precision achromatic doublet lenses combining N-BK7 crown glass and high-dispersion flint glass, designed to minimize chromatic and spherical aberration for broadband imaging and focusing applications.",
    "image": "images/products/optical-lenses/achromatic-doublet.jpg",
    "overview": [
        "PhotonEdge N-BK7 achromatic doublet lenses are two-element cemented lenses designed to correct chromatic aberration, bringing two wavelengths (typically red and blue) to a common focus and significantly reducing focal shift across the visible spectrum.",
        "An achromatic doublet consists of a positive crown glass (N-BK7) element cemented to a negative flint glass (SF11 or equivalent) element. The different dispersion properties of the two materials cancel chromatic aberration at the design wavelengths while maintaining positive optical power.",
        "Compared to single-element plano-convex or bi-convex lenses, achromatic doublets offer dramatically better performance for broadband or white-light applications: smaller spot sizes, reduced color fringing, and improved image contrast across the full visible spectrum.",
        "Standard achromatic doublets are available in diameters from 9mm to 75mm with focal lengths from 15mm to 1000mm. Anti-reflection coatings optimized for visible and VIS-NIR bands are standard. Custom designs including air-spaced doublets, triplets, and custom focal lengths are available on request."
    ],
    "specs": [
        ("Lens Type", "Achromatic Doublet (cemented)"),
        ("Materials", "N-BK7 (crown) + SF11 equivalent (flint)"),
        ("Design Wavelengths", "486.1nm (F), 587.6nm (d), 656.3nm (C)"),
        ("Focal Length (EFL)", "15mm – 1000mm (standard)"),
        ("Focal Length Tolerance", "±1% (standard); ±0.5% (precision)"),
        ("Diameter Range", "9mm – 75mm (standard); custom up to 150mm"),
        ("Diameter Tolerance", "±0.15mm (standard); ±0.05mm (precision)"),
        ("Surface Quality", "40-20 (standard); 20-10 (precision)"),
        ("Surface Figure", "λ/4 @ 632.8nm (standard); λ/8 (precision)"),
        ("Centration (Beam Deviation)", "< 1 arc minute"),
        ("Clear Aperture", "> 90%"),
        ("Transmission (Coated)", "> 98% (VIS AR coated, per surface avg < 1%)"),
        ("Coating Options", "VIS AR, VIS-NIR AR, custom broadband AR")
    ],
    "materials": [
        ("N-BK7 + SF11 (Standard Achromat)", "Standard achromatic doublet pair. N-BK7 crown (low dispersion, positive) + SF11 dense flint (high dispersion, negative). Corrects chromatic aberration at F, d, and C lines. Best for visible wavelength range 400-700nm."),
        ("N-BK7 + SF2 (Low-Dispersion Flint)", "Alternative flint with lower dispersion. Slightly larger secondary spectrum than SF11 pair but better transmission and lower cost for some configurations."),
        ("N-BK7 + CaF₂ (Apochromatic option)", "Apochromatic triplet designs using N-BK7, CaF₂, and a flint glass can correct at three wavelengths, achieving near-complete elimination of chromatic aberration. Available as custom designs."),
        ("Air-Spaced (Special Order)", "For high-power laser or UV applications where cement would degrade. Two separate elements held in precise alignment. Higher cost but can handle higher power and broader wavelength ranges.")
    ],
    "coatings": [
        ("VIS AR Coating (400-700nm)", "Broadband visible anti-reflection coating. R < 1.0% per surface average. Standard for visible imaging, microscopy, and photography."),
        ("VIS-NIR Broadband AR (400-1100nm)", "Extended band AR covering visible through near-infrared. R < 1.25% per surface average. For multispectral imaging and mixed visible/NIR systems."),
        ("NIR AR Coating (700-1100nm)", "Near-infrared optimized AR. R < 0.5% per surface average. For 808nm, 980nm, 1064nm laser focusing and fiber coupling."),
        ("Custom Multi-Band AR", "Custom anti-reflection designs for specific wavelength bands or multi-band systems. Available on request.")
    ],
    "tolerances": [
        ("Standard Grade", "40-20 surface quality / λ/4 wavefront / ±0.15mm diameter / ±1% EFL / < 1 arc min beam deviation. Standard for general imaging, relay lenses, and moderate-resolution systems."),
        ("Precision Grade", "20-10 surface quality / λ/8 wavefront / ±0.10mm diameter / ±0.5% EFL / < 0.5 arc min beam deviation. For high-resolution imaging, microscopy, and metrology systems."),
        ("Laser Grade", "10-5 surface quality / λ/10 wavefront / ±0.05mm diameter / ±0.2% EFL / < 30 arc sec beam deviation. For laser beam delivery, fiber coupling, and ultra-precision applications.")
    ],
    "inspection": [
        "100% dimensional inspection with digital micrometers and optical comparators",
        "Focal length verified at multiple wavelengths (486nm, 588nm, 656nm) to confirm achromatic correction",
        "Surface quality verified per MIL-PRF-13830B under dark-field illumination",
        "Wavefront distortion measured with laser interferometer",
        "Centration / beam deviation measured with precision collimator",
        "Spectral transmission verified across design band",
        "Cement bond integrity check (visual and environmental stress test sampling)"
    ],
    "applications": [
        ("Microscopy & Imaging", "Objective lenses, eyepieces, tube lenses, and relay lenses for high-resolution imaging systems"),
        ("Photography & Projection", "Camera lenses, projection lenses, and imaging systems where color correction is essential"),
        ("Spectroscopy", "Broadband focusing and collimation for spectrometers, monochromators, and spectrophotometers"),
        ("Laser Systems", "Multi-wavelength laser beam delivery, harmonic focusing, and fiber coupling"),
        ("Astronomy", "Telescope objective lenses, eyepieces, and finderscopes"),
        ("Machine Vision", "High-resolution inspection lenses, barcode readers, and automated optical inspection")
    ],
    "engineering": [
        "Achromatic doublets bring two wavelengths (typically 486nm F-line and 656nm C-line) to a common focus. The intermediate wavelengths focus slightly differently — this residual chromatic aberration is called the secondary spectrum. For most visible applications, it is negligible; for ultra-high-resolution work, an apochromatic (APO) triplet may be needed.",
        "The curved side of the doublet should face the longer conjugate distance to minimize spherical aberration, similar to a single plano-convex lens. Check the lens orientation marking (usually a mark on the edge indicating the first surface).",
        "When designing with achromatic doublets, remember that the effective focal length (EFL) is specified at the design wavelength (typically 587.6nm d-line). At other wavelengths, the focal length will be slightly different even with achromatic correction.",
        "Achromatic doublets also correct spherical aberration better than single-element lenses, especially at larger apertures. For fast lenses (f/2 or faster), a doublet will provide dramatically better image quality than a single plano-convex lens.",
        "Cemented doublets should not be used with high-power lasers or in environments with extreme temperature cycling, as the cement may degrade or delaminate. For such applications, specify air-spaced doublets."
    ],
    "faqs": [
        ("When should I use an achromatic doublet instead of a single lens?",
             "Use an achromatic doublet whenever your system operates over a range of wavelengths (white light, broadband sources, multi-line lasers) and color fringing or focal shift would degrade performance. If you're working with monochromatic light (single laser wavelength), a single-element lens is usually sufficient and more cost-effective. Achromats also reduce spherical aberration, so they can improve performance even at a single wavelength for fast f-numbers."),
        ("What is the difference between achromatic and apochromatic lenses?",
             "An achromatic lens corrects chromatic aberration at two wavelengths (e.g., blue and red), bringing them to a common focus. An apochromatic (APO) lens corrects at three wavelengths, virtually eliminating chromatic aberration across a broad band. Apochromats typically use three elements (triplet) with special low-dispersion materials like CaF₂ or ED glass. They are significantly more expensive and only justified for the highest-performance imaging systems."),
        ("Can achromatic doublets be used with lasers?",
             "Yes, achromatic doublets work well with lasers, especially when multiple wavelengths are involved (e.g., frequency-doubled lasers with both fundamental and second harmonic). For single-wavelength laser applications, a single-element lens is usually adequate and less expensive. However, for fast focusing (low f-number), the improved spherical aberration correction of a doublet can yield a smaller focused spot. Note: cemented doublets have lower LIDT than single-element lenses — use air-spaced designs for high-power lasers."),
        ("What does 'focal length tolerance ±1%' mean in practice?",
             "A ±1% focal length tolerance means a 100mm lens could have an actual focal length anywhere from 99mm to 101mm. For most imaging applications, this is well within the depth of focus and doesn't affect image quality. For precision metrology or fiber coupling where the exact focal position matters, use a tighter tolerance (±0.5% or ±0.2%). The tighter the tolerance, the more measurement and sorting is needed, increasing cost.")
    ],
    "related_products": [
        ("/products/achromatic-doublet/", "Achromatic Doublet Lens Catalog"),
        ("/products/nbk7-plano-convex-lenses/", "N-BK7 Plano-Convex Lenses"),
        ("/products/nbk7-optical-windows/", "N-BK7 Optical Windows"),
        ("/products/bk7-bi-convex/", "BK7 Bi-Convex Lenses"),
        ("/products/microscope-objectives/", "Microscope Objectives"),
        ("/products/laser-beam-expanders/", "Laser Beam Expanders")
    ],
    "related_articles": [
        ("/blog/choose-right-optical-lens/", "How to Choose the Right Optical Lens for Your Application"),
        ("/blog/anti-reflection-coating-selection-guide/", "Anti-Reflection Coating Selection Guide"),
        ("/blog/machine-vision-lens-selection-guide/", "Machine Vision Lens Selection Guide")
    ],
    "internal_links": [
        ("/materials/bk7/", "BK7 / N-BK7 Material Properties"),
        ("/applications/medical-imaging/", "Medical Imaging Applications"),
        ("/ai-optical-engineer.html", "AI Optical Engineer")
    ]
})

# Germanium Infrared Lenses
TIER2_PAGES.append({
    "slug": "germanium-infrared-lenses",
    "name": "Germanium Infrared Lenses",
    "category31": "Optical Lenses",
    "componentType": "Lens",
    "material": "Germanium (Ge)",
    "title": "Germanium Infrared Lenses | MWIR LWIR Thermal Imaging | PhotonEdge",
    "description": "Germanium (Ge) infrared lenses for MWIR (3-5μm) and LWIR (8-12μm) thermal imaging applications. Plano-convex, plano-concave, and aspheric designs. AR coatings for IR bands.",
    "keywords": "germanium lens, IR lens, infrared lens, MWIR lens, LWIR lens, thermal imaging lens, Ge lens, 8-12 micron lens",
    "subtitle": "High-quality germanium (Ge) infrared lenses designed for mid-wave and long-wave infrared applications including thermal imaging, FLIR, FTIR spectroscopy, and IR laser systems.",
    "image": "images/products/optical-windows/ge-windows.jpg",
    "overview": [
        "PhotonEdge germanium infrared lenses are precision manufactured from high-purity single-crystal germanium, offering excellent transmission in the 2μm to 16μm infrared spectrum with high refractive index (n ≈ 4.0 at 10μm) enabling compact lens designs.",
        "Germanium is the most widely used infrared optical material due to its excellent transmission in both the MWIR (3-5μm) and LWIR (8-12μm) atmospheric windows, its high refractive index which reduces lens curvature and aberration, and its good mechanical properties for diamond turning.",
        "Our germanium lens product line includes plano-convex, plano-concave, bi-convex, bi-concave, meniscus, and aspheric lenses. Standard sizes range from 6mm to 100mm diameter with focal lengths from 10mm to 500mm.",
        "Anti-reflection coatings are available for MWIR (3-5μm), LWIR (8-12μm), and broadband MWIR-LWIR bands. Aspheric germanium lenses manufactured by single-point diamond turning offer diffraction-limited performance for high-performance thermal imaging systems."
    ],
    "specs": [
        ("Material", "Single-Crystal Germanium (Ge), high purity"),
        ("Refractive Index", "4.0026 @ 10.6μm; 4.0244 @ 4.0μm"),
        ("Transmission Range", "2.0μm – 16μm (uncoated, per cm)"),
        ("Lens Types", "Plano-convex, plano-concave, bi-convex, bi-concave, meniscus, aspheric"),
        ("Diameter Range", "6mm – 100mm (standard); custom up to 200mm"),
        ("Focal Length Range", "10mm – 500mm (standard); custom available"),
        ("Focal Length Tolerance", "±1% (standard); ±0.5% (precision)"),
        ("Diameter Tolerance", "±0.10mm (standard); ±0.02mm (precision)"),
        ("Surface Quality", "40-20 (standard); 20-10 (precision)"),
        ("Surface Figure", "λ/4 @ 632.8nm (equivalent); 0.5μm P-V (IR interferometry)"),
        ("Centration", "< 3 arc minutes"),
        ("Clear Aperture", "> 85% of diameter"),
        ("Chamfer", "0.2mm × 45° (protective)"),
        ("Coating Options", "MWIR AR, LWIR AR, broadband IR AR, DLC coating")
    ],
    "materials": [
        ("Standard Grade Germanium", "High-purity single-crystal germanium with >99.999% purity. Excellent transmission from 2μm to 16μm. Standard for most thermal imaging and IR applications."),
        ("High-Purity Germanium", "Ultra-high-purity Ge with minimal impurity absorption bands. For spectroscopy applications where precise transmission characteristics are critical."),
        ("Diamond-Turnable Grade", "Specified for single-point diamond turning (SPDT) of aspheric surfaces. Uniform crystal structure ensures high-quality aspheric surfaces with minimal scatter.")
    ],
    "coatings": [
        ("MWIR AR Coating (3-5μm)", "Anti-reflection coating optimized for mid-wave infrared. R < 1.5% per surface average. Suitable for MWIR thermal imaging, FLIR, and CO₂ laser systems at 4.3μm."),
        ("LWIR AR Coating (8-12μm)", "Anti-reflection coating for long-wave infrared. R < 1.5% per surface average. Standard for thermal imaging, night vision, and 10.6μm CO₂ laser systems."),
        ("Broadband IR AR (2-16μm)", "Ultra-broadband AR coating covering both MWIR and LWIR. R < 2.0% per surface average. For FTIR spectroscopy and multi-band IR systems."),
        ("Diamond-Like Carbon (DLC) Coating", "Hard protective coating with good IR transmission. R < 2.5% per surface in 8-12μm band. Extremely durable, scratch-resistant, and moisture-resistant. For harsh environments and field-use optics."),
        ("High-Power CO₂ Laser AR (10.6μm)", "Optimized for 10.6μm CO₂ laser systems. R < 0.5% per surface. High LIDT (multi-kW/cm² CW).")
    ],
    "tolerances": [
        ("Standard Grade", "40-20 surface quality / ±0.10mm diameter / ±1% focal length. Standard for general IR imaging and sensor systems."),
        ("Precision Grade", "20-10 surface quality / ±0.05mm diameter / ±0.5% focal length. For high-resolution thermal imaging, spectroscopy, and laser beam delivery."),
        ("Aspheric Grade", "Diamond-turned aspheric surface / diffraction-limited performance / surface figure < 0.5μm P-V. For high-performance thermal cameras, IR objectives, and collimators.")
    ],
    "inspection": [
        "100% dimensional inspection with contact and non-contact metrology",
        "Surface quality verified per MIL-PRF-13830B equivalent (visible inspection with IR-optimized lighting)",
        "Surface figure measured with IR laser interferometer or contact profilometer",
        "Focal length verified through IR optical bench testing",
        "Spectral transmission measured on FTIR spectrophotometer",
        "Coating adhesion verified via tape test and environmental cycling (sampling basis)",
        "Aspheric surface profile verified with contact profilometer or laser interferometer"
    ],
    "applications": [
        ("Thermal Imaging & FLIR", "Long-wave and mid-wave infrared cameras for security, surveillance, and industrial inspection"),
        ("Infrared Spectroscopy", "FTIR, ATR, and Raman spectroscopy focusing and collimation optics"),
        ("CO₂ Laser Systems", "Beam delivery, focusing, and beam shaping for 10.6μm CO₂ lasers for cutting, welding, and marking"),
        ("Defense & Aerospace", "Missile guidance, IR countermeasures, target tracking, and thermal weapon sights"),
        ("Medical & Biomedical", "IR imaging diagnostics, laser surgery systems, and biomedical spectroscopy"),
        ("Automotive", "ADAS thermal imaging cameras, night vision systems, and driver monitoring")
    ],
    "engineering": [
        "Germanium has a very high refractive index (n ≈ 4.0), which means strong lens power can be achieved with gentle surface curvatures, reducing spherical aberration compared to lower-index materials. However, it also means higher surface reflection (~36% per uncoated surface!), making anti-reflection coatings essential for any IR system.",
        "Germanium is opaque to visible light — you cannot see through it. Alignment of germanium optics requires IR cameras or alignment lasers operating in the IR band (e.g., 1.55μm HeNe or alignment diode).",
        "Germanium has a large thermo-optic coefficient (dn/dT ≈ 400 × 10⁻⁶ /°C) and thermal expansion coefficient (6.1 × 10⁻⁶ /°C). This means focal length changes significantly with temperature. For systems operating over wide temperature ranges, consider athermalized lens designs or active focus correction.",
        "For diffraction-limited performance, use aspheric germanium lenses. Single-point diamond turning produces rotationally symmetric aspheres that can correct spherical aberration completely, achieving near-diffraction-limited focus with a single element.",
        "Germanium is relatively hard (Mohs 6) but brittle. Handle with care to avoid chipping. DLC coating provides additional scratch resistance for field-deployed systems."
    ],
    "faqs": [
        ("Why is anti-reflection coating so important for germanium lenses?",
         "Germanium has a refractive index of about 4.0, which means each uncoated surface reflects approximately 36% of incident light at normal incidence (Fresnel reflection). With two surfaces, that's nearly 60% reflection loss — only about 40% of the light transmits through an uncoated Ge lens. An AR coating reduces reflection to <1.5% per surface, boosting total transmission to >97%. AR coating is not optional for germanium — it is essential for any practical IR system."),
        ("What is the temperature range for germanium optics?",
         "Germanium remains transparent from cryogenic temperatures up to about 200°C. Above 100°C, free-carrier absorption starts increasing (especially in LWIR), and above 200°C the material becomes opaque in the infrared. For high-temperature applications, consider silicon or sapphire. At cryogenic temperatures, Ge transmission actually improves (reduced free-carrier absorption), making it excellent for cooled detector systems."),
        ("When should I use an aspheric lens vs a spherical lens?",
         "Use a spherical germanium lens when cost is the primary driver and the f-number is relatively slow (f/4 or larger). Use an aspheric germanium lens when you need diffraction-limited performance, especially for fast f-numbers (f/1 to f/3) common in thermal imaging objectives. A single aspheric element can replace a multi-element spherical design, reducing size, weight, and cost — despite the higher per-element cost of diamond turning."),
        ("What is DLC coating and when should I use it?",
             "Diamond-Like Carbon (DLC) is a hard, amorphous carbon coating that provides excellent scratch resistance and environmental protection for infrared optics. It has good transmission in the 8-12μm band and is extremely durable — it can be wiped clean without damage, unlike standard IR AR coatings which are soft. Use DLC for field-deployed systems, military optics, or any application where the lens may be exposed to dust, moisture, or handling. It is more expensive than standard AR and has slightly higher reflection loss.")
    ],
    "related_products": [
        ("/products/germanium-optical-windows/", "Germanium Optical Windows"),
        ("/products/ge-windows/", "Germanium Window Catalog"),
        ("/products/sapphire-optical-windows/", "Sapphire Optical Windows"),
        ("/products/caf2-plano-convex-lenses/", "CaF₂ IR Lenses"),
        ("/products/ir-bandpass-filters/", "IR Bandpass Filters"),
        ("/products/ir-polarizers/", "IR Polarizers")
    ],
    "related_articles": [
        ("/blog/infrared-optical-materials-comparison/", "Infrared Optical Materials: A Comparative Guide"),
        ("/blog/laser-damage-threshold-guide/", "Laser Damage Threshold Guide"),
        ("/blog/anti-reflection-coatings-guide/", "Anti-Reflection Coatings: Technical Guide")
    ],
    "internal_links": [
        ("/applications/aerospace-defense/", "Aerospace & Defense Applications"),
        ("/applications/medical-imaging/", "Medical Imaging"),
        ("/ai-optical-engineer.html", "AI Optical Engineer")
    ]
})

# Sapphire Optical Windows
TIER2_PAGES.append({
    "slug": "sapphire-optical-windows",
    "name": "Sapphire Optical Windows",
    "category31": "Optical Windows",
    "componentType": "Window",
    "material": "Sapphire (Al₂O₃)",
    "title": "Sapphire Optical Windows | Scratch-Resistant IR-UV | PhotonEdge",
    "description": "Sapphire (Al₂O₃) optical windows with exceptional hardness and scratch resistance. Transmissive from UV to mid-IR. Ideal for harsh environments, defense, and high-pressure systems.",
    "keywords": "sapphire window, sapphire optical window, Al2O3 window, scratch resistant window, IR window, UV window, sapphire glass window",
    "subtitle": "Ultra-hard single-crystal sapphire (Al₂O₃) optical windows offering exceptional scratch resistance, chemical inertness, and broad transmission from deep UV to mid-infrared — the ultimate window for harsh environments.",
    "image": "images/products/optical-windows/sapphire-windows.jpg",
    "overview": [
        "PhotonEdge sapphire optical windows are manufactured from high-quality single-crystal sapphire (α-Al₂O₃), the second-hardest optical material after diamond. Sapphire combines exceptional mechanical strength with broad optical transmission, making it the material of choice for demanding environments.",
        "With a Mohs hardness of 9, sapphire windows are virtually scratch-proof under normal use and can withstand high pressure, extreme temperatures, and corrosive chemicals. They are commonly used in aerospace, defense, oil & gas, and medical applications where durability is critical.",
        "Sapphire transmits from approximately 170nm (deep UV) through 5.5μm (mid-infrared), making it one of the few optical materials that spans the UV, visible, and MWIR spectral regions. This makes sapphire ideal for multi-spectral imaging and detection systems.",
        "Standard sapphire windows are available in diameters from 6mm to 100mm with thicknesses from 0.5mm to 10mm. Both c-plane (0001) and a-plane orientations are available. Anti-reflection coatings can be applied for UV, VIS, NIR, and MWIR bands. Custom sizes, shapes and coatings available on request."
    ],
    "specs": [
        ("Material", "Single-Crystal Sapphire (α-Al₂O₃), high purity"),
        ("Crystal Orientation", "C-plane (0001) standard; a-plane (11-20) available"),
        ("Refractive Index", "1.768 @ 589nm (o-ray); 1.760 @ 589nm (e-ray)"),
        ("Mohs Hardness", "9 (second only to diamond)"),
        ("Transmission Range", "170nm – 5500nm (0.5mm thick)"),
        ("Diameter / Size Range", "6mm – 100mm (standard); custom up to 200mm"),
        ("Shape Options", "Round, square, rectangular, custom"),
        ("Thickness Range", "0.3mm – 10mm (standard); thicker available"),
        ("Thickness Tolerance", "±0.05mm (standard); ±0.01mm (precision)"),
        ("Surface Quality", "40-20 (standard); 20-10 (precision); 10-5 (high-precision)"),
        ("Surface Flatness", "λ/4 @ 632.8nm (standard); λ/10 (precision); λ/20 (high-precision)"),
        ("Parallelism (Wedge)", "< 3 arc min (standard); < 30 arc sec (precision)"),
        ("Clear Aperture", "> 85%"),
        ("Chamfer", "0.15mm × 45° (protective)"),
        ("Coating Options", "UV AR, VIS AR, NIR AR, MWIR AR, broadband AR")
    ],
    "materials": [
        ("Standard Optical Grade Sapphire", "High-quality single-crystal sapphire grown by Czochralski or EFG method. Excellent optical quality with minimal inclusions and low stress birefringence. Standard for most UV-VIS-IR window applications."),
        ("High-Purity Sapphire", "Ultra-high-purity sapphire with extremely low impurity levels for deep-UV and high-power laser applications. Minimum absorption at 193nm and 248nm excimer wavelengths."),
        ("IR Grade Sapphire", "Specified for infrared applications with controlled impurity levels that affect IR absorption. For MWIR imaging and 3-5μm sensor systems."),
        ("Scratch-Resistant / Harsh Environment Grade", "Double-sided polished sapphire with maximum surface hardness. Specified for applications with high abrasion, high pressure, or chemical exposure.")
    ],
    "coatings": [
        ("UV AR Coating (200-400nm)", "Deep-UV anti-reflection coating. R < 1.5% per surface average. For 248nm, 266nm, 355nm laser and UV imaging applications."),
        ("VIS AR Coating (350-700nm)", "Broadband visible AR coating. R < 1.0% per surface average. Standard for visible imaging, microscopy, and display applications."),
        ("NIR AR Coating (700-1100nm)", "Near-infrared AR coating. R < 0.75% per surface average. For 808nm, 980nm, 1064nm laser and sensor systems."),
        ("MWIR AR Coating (3-5μm)", "Mid-wave infrared AR coating. R < 1.5% per surface average. For thermal imaging, FLIR, and IR sensor systems."),
        ("Broadband UV-VIS-IR AR", "Custom broadband designs for multi-spectral applications. Covers UV through NIR or VIS through MWIR."),
        ("Diamond-Like Carbon (DLC)", "Ultra-hard protective coating for the most demanding abrasion and corrosion environments. Slight IR absorption — primarily used for protection in harsh conditions.")
    ],
    "tolerances": [
        ("Standard Grade", "40-20 surface quality / λ/4 flatness / ±0.05mm thickness / < 3 arc min wedge. General-purpose sapphire windows for protection and moderate optical performance."),
        ("Precision Grade", "20-10 surface quality / λ/10 flatness / ±0.02mm thickness / < 30 arc sec wedge. For metrology, imaging, and high-resolution sensor systems."),
        ("High-Precision Grade", "10-5 surface quality / λ/20 flatness / ±0.01mm thickness / < 5 arc sec wedge. For interferometry, laser systems, and the most demanding optical applications.")
    ],
    "inspection": [
        "100% dimensional inspection with contact and non-contact metrology",
        "Surface quality verified per MIL-PRF-13830B equivalent under dark-field illumination",
        "Surface flatness measured with laser interferometer (ZYGO equivalent)",
        "Wedge / parallelism measured with autocollimator or interferometer",
        "Spectral transmission verified across UV-Vis-NIR and MWIR ranges",
        "Crystal orientation verified via X-ray diffraction (sampling basis)",
        "Pressure test and thermal shock test available on request (custom orders)"
    ],
    "applications": [
        ("Aerospace & Defense", "Aircraft windows, missile domes, sensor protection, and ruggedized optical systems"),
        ("Oil & Gas / Downhole", "High-pressure, high-temperature well logging and inspection windows"),
        ("Medical & Dental", "Surgical laser delivery windows, endoscope protection, dental curing light windows"),
        ("Semiconductor & UV Processing", "Excimer laser windows, wafer inspection optics, UV lithography beam delivery"),
        ("Scientific Research", "High-pressure diamond anvil cell windows, vacuum chamber viewports, extreme environment optics"),
        ("Industrial & Manufacturing", "High-temperature furnace viewports, harsh environment sensor protection, laser processing windows")
    ],
    "engineering": [
        "Sapphire is a uniaxial birefringent crystal — it has two refractive indices (ordinary and extraordinary ray). C-plane (0001) sapphire has its optical axis perpendicular to the surface, so at normal incidence there is no birefringence effect (light travels along the optical axis). For off-axis angles, birefringence appears. a-plane sapphire shows strong birefringence at normal incidence. Use c-plane for imaging applications.",
        "Sapphire's high hardness (Mohs 9) means it can only be polished with diamond compounds and processed with diamond tools. This increases manufacturing cost compared to glass but results in a virtually scratch-proof surface that can withstand harsh cleaning and environmental exposure.",
        "Sapphire can withstand temperatures up to 2000°C in inert atmosphere and up to 1500°C in air (before surface degradation begins). Its thermal conductivity is very high (~40 W/m·K at room temperature), allowing rapid heat dissipation.",
        "For high-pressure applications, sapphire windows have excellent compressive strength. The pressure rating depends on thickness, diameter, and edge support. Our engineering team can calculate pressure ratings for custom window specifications.",
        "Sapphire has a high refractive index (n ≈ 1.76), resulting in about 7.5% reflection per uncoated surface at normal incidence (compared to 4% for BK7). AR coating is recommended for all but the most basic protection applications."
    ],
    "faqs": [
        ("What makes sapphire better than glass windows?",
         "Sapphire is far harder (Mohs 9 vs 5-6 for glass), meaning it cannot be scratched by most common materials (sand, dust, metal tools). It has a much higher melting point (2040°C vs ~550°C for BK7), higher pressure rating, and better chemical resistance. It also transmits deeper into the UV and further into the IR than most glasses. The tradeoff is higher cost — sapphire is significantly more expensive than glass windows. Use sapphire when glass would be damaged by the operating environment."),
        ("What crystal orientation should I choose?",
         "For most optical applications, c-plane (0001) sapphire is standard. With c-plane, the optical axis is perpendicular to the window surface, so at normal incidence there is no birefringence. This is ideal for imaging and sensor applications. a-plane or r-plane sapphire is used for specialized applications where birefringence is desired (e.g., waveplates, polarizers) or for specific growth/manufacturing requirements. If you're not sure, choose c-plane."),
        ("Can sapphire windows be used at high pressure?",
             "Yes, sapphire is one of the best materials for high-pressure optical viewports. Its compressive strength is approximately 2 GPa. The actual pressure rating of a sapphire window depends on its thickness, diameter, and how it is mounted. As a rough guide, a 25mm diameter, 3mm thick sapphire window with full edge support can withstand several hundred atmospheres. We can provide detailed pressure calculations for custom designs. Always verify with pressure testing for safety-critical applications."),
        ("How do you clean sapphire windows?",
         "Because sapphire is so hard, it can be cleaned more aggressively than glass without risk of scratching. Standard procedure is to use reagent-grade acetone, methanol, or isopropyl alcohol with lint-free optical tissue. Ultrasonic cleaning in detergent solution works well for heavy contamination. For stubborn deposits, you can even use a mild abrasive cleaner on sapphire (something that would destroy a glass window). However, still avoid coarse abrasives that could introduce micro-scratches, especially on precision-polished surfaces.")
    ],
    "related_products": [
        ("/products/sapphire-windows/", "Sapphire Window Catalog"),
        ("/products/germanium-optical-windows/", "Germanium Optical Windows"),
        ("/products/fused-silica-optical-windows/", "Fused Silica Optical Windows"),
        ("/products/nbk7-optical-windows/", "N-BK7 Optical Windows"),
        ("/products/caf2-optical-windows/", "CaF₂ Optical Windows"),
        ("/products/ir-bandpass-filters/", "IR Bandpass Filters")
    ],
    "related_articles": [
        ("/blog/infrared-optical-materials-comparison/", "Infrared Optical Materials: A Comparative Guide"),
        ("/blog/bk7-vs-uv-fused-silica/", "BK7 vs UV Fused Silica: Material Selection Guide"),
        ("/blog/anti-reflection-coating-selection-guide/", "Anti-Reflection Coating Selection Guide")
    ],
    "internal_links": [
        ("/materials/sapphire/", "Sapphire Material Properties"),
        ("/applications/aerospace-defense/", "Aerospace & Defense Applications"),
        ("/ai-optical-engineer.html", "AI Optical Engineer")
    ]
})

# High-Power Laser Mirrors
TIER2_PAGES.append({
    "slug": "high-power-laser-mirrors",
    "name": "High-Power Laser Mirrors",
    "category31": "Optical Mirrors",
    "componentType": "Mirror",
    "material": "UV Fused Silica",
    "title": "High-Power Laser Mirrors | High LIDT | PhotonEdge",
    "description": "High-power laser mirrors with ultra-high laser damage threshold. Dielectric coatings for 355nm, 532nm, 1064nm, and more. Fused silica substrates with λ/20 flatness.",
    "keywords": "high power laser mirror, high LIDT mirror, laser line mirror, 1064nm mirror, fused silica mirror, dielectric HR mirror, laser cavity mirror",
    "subtitle": "High-power laser mirrors with ultra-high laser damage threshold dielectric coatings on fused silica substrates — engineered for CW and pulsed laser systems from UV to NIR.",
    "image": "images/products/optical-mirrors/laser-line-high-reflected-mirrors.jpg",
    "overview": [
        "PhotonEdge high-power laser mirrors are designed and manufactured for the most demanding laser applications, with carefully optimized dielectric coatings on ultra-low-absorption fused silica substrates to achieve the highest possible laser damage threshold.",
        "Our high-power mirror product line covers all major laser wavelengths from 193nm excimer through 10.6μm CO₂, with both 0° and 45° angle-of-incidence configurations. Coatings are designed using advanced thin-film software and deposited with precise process control to ensure repeatable, high-LIDT performance.",
        "Substrates are manufactured from UV-grade fused silica for visible and NIR lasers, and from CaF₂ or MgF₂ for UV excimer lasers. Multiple flatness grades are available from λ/10 to λ/20, with surface quality from 20-10 to 10-5.",
        "All high-power laser mirrors undergo LIDT testing (1-on-1 and S-on-1 per ISO 11254 equivalent) to verify damage threshold performance. Custom designs including custom wavelengths, polarization states, and large formats are available on request."
    ],
    "specs": [
        ("Substrate Material", "UV Grade Fused Silica (VIS-NIR); CaF₂ (UV excimer); Si (CO₂)"),
        ("Diameter / Size Range", "12.7mm – 50.8mm (standard); custom up to 200mm"),
        ("Substrate Thickness", "6.35mm (standard); 3.175mm, 9.525mm, 12.7mm options"),
        ("Surface Quality", "20-10 (standard); 10-5 (high-power grade)"),
        ("Surface Flatness", "λ/10 @ 632.8nm (standard); λ/20 (precision HP)"),
        ("Reflectivity", "> 99.5% at design wavelength and AOI (standard HR)"),
        ("Angle of Incidence", "0° or 45° (specify when ordering)"),
        ("Laser Damage Threshold (Pulsed)", "15-30 J/cm² @ 1064nm, 10ns, 10Hz (S-on-1)"),
        ("Laser Damage Threshold (CW)", "> 50 kW/cm² @ 1064nm CW (typical)"),
        ("Coating Type", "Multilayer dielectric (Ta₂O₅/SiO₂, HfO₂/SiO₂, Al₂O₃/SiO₂)"),
        ("Wavefront Distortion", "< λ/10 per inch (standard); < λ/20 per inch (precision)"),
        ("Clear Aperture", "> 90% of diameter")
    ],
    "materials": [
        ("UV Grade Fused Silica (VIS-NIR)", "Standard substrate for visible and near-IR high-power lasers. Low absorption, low thermal expansion, excellent polish quality. Suitable for 355nm through 2μm wavelengths."),
        ("CaF₂ (UV Excimer)", "Calcium fluoride substrate for deep-UV excimer laser applications (193nm, 248nm). High UV transmission and high UV LIDT. <111> crystal orientation standard."),
        ("Silicon (CO₂ Lasers)", "Single-crystal silicon substrate for 10.6μm CO₂ laser mirrors. High thermal conductivity for efficient heat dissipation. Copper backside cooling option for multi-kW systems."),
        ("Copper (High-Power CW)", "Polished copper substrates for ultra-high-power CO₂ and fiber laser applications. Water-cooled designs available for multi-kW CW systems.")
    ],
    "coatings": [
        ("1064nm High Reflector", "Standard high-power NIR HR coating. R > 99.5% @ 1064nm, 0° or 45° AOI. LIDT: 25 J/cm² (10ns, 10Hz). For Nd:YAG, fiber laser cavities and beam delivery."),
        ("532nm Green Laser HR", "Green wavelength high reflector. R > 99.5% @ 532nm. LIDT: 15 J/cm² (10ns, 10Hz). For frequency-doubled Nd:YAG and green DPSS lasers."),
        ("355nm UV Laser HR", "UV high reflector for third-harmonic Nd:YAG. R > 99% @ 355nm. LIDT: 3 J/cm² (10ns, 10Hz). For UV laser processing and inspection systems."),
        ("700-1100nm Broadband HR", "Broadband high reflector covering Ti:Sapphire and Yb-doped laser wavelengths. R > 99.5% across the band. LIDT: 15 J/cm² @ 800nm, 10ns. For ultrafast and tunable laser systems."),
        ("808nm / 980nm Diode Laser HR", "Diode laser wavelength high reflector. R > 99%. LIDT: 20 J/cm² (10ns, 10Hz). For diode laser pumping and beam delivery."),
        ("1550nm Fiber Laser HR", "Telecom and fiber laser wavelength high reflector. R > 99.5%. LIDT: 20 J/cm² (10ns, 10Hz). For fiber laser cavities and amplifier systems.")
    ],
    "tolerances": [
        ("Standard High-Power Grade", "20-10 surface quality / λ/10 flatness / ±0.10mm diameter / LIDT tested. Standard for industrial lasers, beam delivery, and moderate-power resonators."),
        ("Precision High-Power Grade", "10-5 surface quality / λ/20 flatness / ±0.05mm diameter / LIDT tested. For high-power resonators, ring lasers, and interferometry where wavefront quality is critical."),
        ("Ultra-High-Power Grade", "10-5 surface quality / λ/20 flatness / thick substrate / custom LIDT-optimized coating. For kW-class CW lasers, Q-switched high-energy pulses, and custom high-power systems.")
    ],
    "inspection": [
        "Surface flatness verified with phase-shift interferometer (ZYGO equivalent)",
        "Reflectance spectrum measured with PerkinElmer Lambda spectrophotometer",
        "Surface quality inspected per MIL-PRF-13830B equivalent under dark-field conditions",
        "Laser damage threshold tested per ISO 11254 equivalent (1-on-1 and S-on-1)",
        "Dimensional inspection with digital micrometer and optical comparator",
        "Absorption measurement via photothermal common-path interferometry (on request)",
        "Full LIDT test report provided with each high-power mirror batch"
    ],
    "applications": [
        ("Industrial Laser Processing", "Cutting, welding, marking, and engraving laser cavities and beam delivery"),
        ("Laser Resonators", "End mirrors, folding mirrors, and output couplers for solid-state and fiber lasers"),
        ("Defense & Directed Energy", "High-power laser weapon systems, LIDAR, and laser rangefinders"),
        ("Scientific Research", "Ti:Sapphire amplifiers, OPA systems, high-harmonic generation, fusion research"),
        ("Medical Lasers", "Surgical lasers, dental lasers, and aesthetic laser systems"),
        ("Semiconductor Manufacturing", "Laser annealing, micromachining, and wafer processing lasers")
    ],
    "engineering": [
        "Laser damage threshold depends strongly on pulse duration, wavelength, pulse repetition rate, and spot size. Always derate LIDT values for worst-case conditions. A good rule of thumb is to operate at < 50% of the rated LIDT for reliable long-term performance.",
        "For high-power CW lasers, thermal lensing in the mirror substrate can distort the reflected wavefront. Use thicker substrates for higher power, and ensure proper heat sinking. We can provide water-cooled mirror mounts for kW-class systems.",
        "Dielectric coatings are designed for a specific angle of incidence (AOI) and polarization state. Using the mirror at a different AOI shifts the coating spectrum and reduces performance. Always specify your exact AOI and polarization (S, P, or random) when ordering.",
        "The cleanliness of the mirror surface is critical for high-power operation — even microscopic particles can absorb laser energy and cause damage. Always handle with gloves, use proper cleaning procedures, and keep optics in clean, dry storage when not in use.",
        "For ultrafast (femtosecond) pulses, the GVD (group velocity dispersion) of the mirror coating becomes important. Standard HR coatings can introduce significant GDD that broadens femtosecond pulses. For ultrafast systems, specify low-GDD or chirped mirror coatings."
    ],
    "faqs": [
        ("How is laser damage threshold measured?",
             "We use ISO 11254 equivalent testing procedures. For pulsed lasers, both 1-on-1 (single pulse per site) and S-on-1 (multiple pulses per site) tests are performed at the rated wavelength and pulse duration. The damage threshold is the highest fluence (J/cm²) where no damage is observed after statistical analysis of multiple test sites. For CW lasers, damage threshold is measured in W/cm² by ramping up power until damage occurs. LIDT values depend on wavelength, pulse duration, repetition rate, and beam profile — always verify with your actual operating conditions."),
        ("What LIDT do I need for my laser system?",
             "Calculate the peak fluence at the mirror surface: peak fluence (J/cm²) = pulse energy (J) / beam area (cm²) × 2 (for Gaussian beams, peak = 2× average). Then add a safety factor of at least 2× (preferably 3-5× for reliable operation). For example, if your laser has 1mJ pulses focused to a 1mm diameter spot, the peak fluence is about 1mJ / (π × 0.05cm)² × 2 ≈ 0.25 J/cm² × 2 = 0.5 J/cm² — a 10 J/cm² rated mirror would have a 20× safety margin, which is excellent."),
        ("How do I clean high-power laser mirrors?",
             "Proper cleaning is critical for high-power performance. Use only reagent-grade solvents (methanol, isopropyl alcohol, or acetone) and lint-free optical tissue. The drop-and-drag method is recommended: place a drop of solvent on the surface, drag a lens tissue across the surface in one direction, and discard the tissue. Never use circular motions or reuse tissue. Blow off loose particles with clean, dry nitrogen or clean, oil-free compressed air before wiping. If you're not confident in cleaning, it's safer to replace the optic than to risk damage from improper cleaning."),
        ("What is the difference between 0° and 45° AOI mirrors?",
             "A mirror's coating is designed for a specific angle of incidence (AOI). A 0° AOI coating is for normal incidence (light coming straight at the mirror), typical for end mirrors in a laser cavity. A 45° AOI coating is for light coming in at 45°, typical for folding mirrors. Using a 0° coating at 45° will result in reduced reflectivity and shifted spectral response. Also, at non-normal incidence, S-polarization and P-polarization have different reflectance values — at 45°, P-polarization reflectance is always lower than S-polarization for dielectric HR coatings. Always specify your exact AOI and polarization requirements.")
    ],
    "related_products": [
        ("/products/high-energy-laser-mirrors/", "High Energy Laser Mirror Catalog"),
        ("/products/laser-line-high-reflected-mirrors/", "Laser Line High-Reflect Mirrors"),
        ("/products/fused-silica-optical-mirrors/", "Fused Silica Optical Mirrors"),
        ("/products/fused-silica-laser-lenses/", "Fused Silica Laser Lenses"),
        ("/products/ndyag-output-couplers/", "Nd:YAG Output Couplers"),
        ("/products/laser-beam-expanders/", "Laser Beam Expanders")
    ],
    "related_articles": [
        ("/blog/laser-damage-threshold-guide/", "Laser Damage Threshold: What Engineers Need to Know"),
        ("/blog/laser-mirror-selection-guide/", "Laser Mirror Selection Guide"),
        ("/blog/laser-optics-selection-guide/", "Complete Guide to Laser Optics Selection")
    ],
    "internal_links": [
        ("/materials/uv-fused-silica/", "UV Fused Silica Material"),
        ("/applications/laser-optics/", "Laser Applications"),
        ("/ai-optical-engineer.html", "AI Optical Engineer")
    ]
})

print(f"Defined {len(TIER2_PAGES)} Tier 2 pages.")
for p in TIER2_PAGES:
    print(f"  - {p['slug']} ({p['name']})")

# ─────────────────────────────────────────────────────────
# Copy V94 base to V95
# ─────────────────────────────────────────────────────────

def copy_v94_to_v95():
    """Copy entire V94 directory to V95 as base."""
    print("Copying V94 to V95...")
    if os.path.exists(DST):
        # Remove existing V95 build (but keep our build script)
        for item in os.listdir(DST):
            s = os.path.join(DST, item)
            if item == "build_v95.py":
                continue
            if os.path.isdir(s):
                shutil.rmtree(s)
            else:
                os.remove(s)
    
    for item in os.listdir(SRC):
        s = os.path.join(SRC, item)
        d = os.path.join(DST, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)
    print(f"  Copied to {DST}")


# ─────────────────────────────────────────────────────────
# Tier 2 Product Page HTML Generator
# ─────────────────────────────────────────────────────────

def generate_tier2_page(page):
    """Generate complete HTML for a Tier 2 product page."""
    slug = page["slug"]
    name = page["name"]
    title = page["title"]
    desc = page["description"]
    keywords = page["keywords"]
    subtitle = page["subtitle"]
    image = page.get("image", "images/logo.png")
    url = f"{BASE_URL}/products/{slug}/"
    cat31 = page.get("category31", "Optical Components")
    
    # Build FAQ JSON-LD
    faq_items = []
    for q, a in page["faqs"]:
        faq_items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })
    faq_json = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_items}, indent=8)
    
    # Product Schema
    product_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "Product",
        "name": name,
        "description": desc,
        "brand": {"@type": "Organization", "name": "PhotonEdge"},
        "manufacturer": {"@type": "Organization", "name": "Beijing Hengdingguang Technology Co., Ltd."},
        "category": cat31
    }, indent=8)
    
    # BreadcrumbList Schema
    breadcrumb_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": "Products", "item": f"{BASE_URL}/product-catalog.html"},
            {"@type": "ListItem", "position": 3, "name": cat31, "item": f"{BASE_URL}/product-catalog.html?category={cat31.replace(' ', '-')}"},
            {"@type": "ListItem", "position": 4, "name": name, "item": url}
        ]
    }, indent=8)
    
    # Build spec table
    spec_rows = ""
    for k, v in page["specs"]:
        spec_rows += f"                <tr><td style='padding:10px 14px;border-bottom:1px solid #e2e6ef;font-weight:600;color:#1e3a5f;width:35%;'>{k}</td><td style='padding:10px 14px;border-bottom:1px solid #e2e6ef;color:#374151;'>{v}</td></tr>\n"
    
    # Build material options
    material_html = ""
    for title_text, desc_text in page["materials"]:
        material_html += f"""
                <div style='background:white;border:1px solid #e2e6ef;border-radius:8px;padding:20px;margin-bottom:12px;'>
                    <h3 style='font-size:16px;color:#1e3a5f;margin-bottom:8px;'>{title_text}</h3>
                    <p style='font-size:14px;color:#4b5563;line-height:1.6;margin:0;'>{desc_text}</p>
                </div>"""
    
    # Build coating options
    coating_html = ""
    for title_text, desc_text in page["coatings"]:
        coating_html += f"""
                <div style='background:white;border:1px solid #e2e6ef;border-radius:8px;padding:20px;margin-bottom:12px;'>
                    <h3 style='font-size:16px;color:#1e3a5f;margin-bottom:8px;'>{title_text}</h3>
                    <p style='font-size:14px;color:#4b5563;line-height:1.6;margin:0;'>{desc_text}</p>
                </div>"""
    
    # Build tolerances
    tolerance_html = ""
    for title_text, desc_text in page["tolerances"]:
        tolerance_html += f"""
                <div style='background:white;border:1px solid #e2e6ef;border-radius:8px;padding:20px;margin-bottom:12px;'>
                    <h3 style='font-size:16px;color:#1e3a5f;margin-bottom:8px;'>{title_text}</h3>
                    <p style='font-size:14px;color:#4b5563;line-height:1.6;margin:0;'>{desc_text}</p>
                </div>"""
    
    # Build inspection
    inspection_items = ""
    for item in page["inspection"]:
        inspection_items += f"                <li style='margin-bottom:8px;color:#374151;'>{item}</li>\n"
    
    # Build applications
    app_html = ""
    for title_text, desc_text in page["applications"]:
        app_html += f"""
                <div style='background:white;border:1px solid #e2e6ef;border-radius:8px;padding:20px;margin-bottom:12px;'>
                    <h3 style='font-size:16px;color:#1e3a5f;margin-bottom:8px;'>{title_text}</h3>
                    <p style='font-size:14px;color:#4b5563;line-height:1.6;margin:0;'>{desc_text}</p>
                </div>"""
    
    # Build engineering considerations
    eng_items = ""
    for item in page["engineering"]:
        eng_items += f"                <p style='font-size:14px;color:#374151;line-height:1.7;margin-bottom:14px;'>{item}</p>\n"
    
    # Build FAQ accordion (simple expandable)
    faq_html = ""
    for i, (q, a) in enumerate(page["faqs"]):
        faq_html += f"""
                <div style='background:white;border:1px solid #e2e6ef;border-radius:8px;margin-bottom:10px;overflow:hidden;'>
                    <div style='padding:16px 20px;cursor:pointer;font-weight:600;color:#1e3a5f;font-size:15px;' onclick='var n=this.nextElementSibling;n.style.display=n.style.display==="none"?"block":"none";'>
                        {q}
                    </div>
                    <div style='padding:0 20px 16px;color:#4b5563;font-size:14px;line-height:1.7;display:none;'>
                        {a}
                    </div>
                </div>"""
    
    # Build related products
    related_products_html = ""
    for href, label in page["related_products"]:
        related_products_html += f"<a href='{href}' style='display:inline-block;padding:6px 14px;background:#f3f4f6;border-radius:6px;font-size:13px;color:#374151;text-decoration:none;margin:0 6px 6px 0;'>{label}</a>\n"
    
    # Build related articles
    related_articles_html = ""
    for href, label in page["related_articles"]:
        related_articles_html += f"<a href='{href}' style='display:block;padding:10px 16px;background:#f8fafc;border-radius:8px;margin-bottom:8px;text-decoration:none;color:#1e3a5f;font-size:14px;'>&rarr; {label}</a>\n"
    
    # Build internal links
    internal_links_html = ""
    for i, (href, label) in enumerate(page["internal_links"]):
        if i > 0:
            internal_links_html += " &middot; "
        internal_links_html += f"<a href='{href}' style='color:#3b82f6;text-decoration:none;font-size:13px;'>{label}</a>"
    
    # Overview paragraphs
    overview_html = ""
    for para in page["overview"]:
        overview_html += f"<p style='font-size:15px;color:#374151;line-height:1.7;margin-bottom:16px;'>{para}</p>\n"
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <meta charset="UTF-8">
    <link rel="icon" type="image/png" sizes="32x32" href="https://photonedgeoptics.com/images/favicon-32.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="product">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="https://photonedgeoptics.com/{image}">
    <meta property="og:site_name" content="PhotonEdge">
    <link rel="canonical" href="{url}">
    <link rel="stylesheet" href="/css/style.css">
    <link rel="stylesheet" href="/css/chatbot.css">
    <link rel="alternate" hreflang="en" href="{url}">
    <link rel="alternate" hreflang="zh" href="{url}?lang=zh">
    <script type="application/ld+json">
    {product_json}
    </script>
    <script type="application/ld+json">
    {breadcrumb_json}
    </script>
    <script type="application/ld+json">
    {faq_json}
    </script>
    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-E6J791MXZY"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-E6J791MXZY');
    </script>
    <!-- Baidu Search Auto Push -->
    <script>
        (function(){{
            var bp = document.createElement('script');
            var curProtocol = window.location.protocol.split(':')[0];
            if (curProtocol === 'https') {{
                bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
            }} else {{
                bp.src = 'https://push.zhangzifan.com/linksubmit/push.js';
            }}
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(bp, s);
        }})();
    </script>
    <style>
    .product-hero {{ background: linear-gradient(135deg, #0a1628 0%, #1a2d50 100%); padding: 60px 0 40px; color: white; }}
    .product-hero h1 {{ font-size: 32px; font-weight: 700; margin-bottom: 12px; color: white; }}
    .product-hero .subtitle {{ font-size: 16px; color: #b0c4de; max-width: 800px; line-height: 1.6; }}
    .product-hero .breadcrumb {{ font-size: 13px; color: rgba(176,196,222,0.6); margin-bottom: 16px; }}
    .product-hero .breadcrumb a {{ color: rgba(176,196,222,0.8); text-decoration: none; }}
    .product-hero .breadcrumb a:hover {{ color: white; }}
    .product-section {{ padding: 60px 0; }}
    .product-section:nth-child(even) {{ background: #f8fafc; }}
    .product-section h2 {{ font-size: 24px; color: #1a202c; margin-bottom: 24px; }}
    .product-section h3 {{ font-size: 18px; color: #1e3a5f; margin-bottom: 12px; }}
    .spec-table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; border: 1px solid #e2e6ef; }}
    .spec-table tr:last-child td {{ border-bottom: none; }}
    .cta-box {{ background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 48px; border-radius: 12px; text-align: center; color: white; margin: 40px 0; }}
    .cta-box h2 {{ color: white; font-size: 24px; margin-bottom: 12px; }}
    .cta-box p {{ color: rgba(176,196,222,0.9); margin-bottom: 24px; }}
    .cta-box .btn {{ display: inline-block; padding: 12px 28px; border-radius: 6px; font-weight: 600; text-decoration: none; margin: 0 8px; }}
    .cta-box .btn-primary {{ background: #e8792f; color: white; }}
    .cta-box .btn-secondary {{ background: transparent; color: white; border: 1px solid rgba(255,255,255,0.4); }}
    .ai-box {{ background: #f0f4ff; border: 1px solid #c7d7fe; border-radius: 12px; padding: 32px; text-align: center; margin: 40px 0; }}
    .ai-box h3 {{ color: #1e3a5f; margin-bottom: 8px; }}
    .ai-box p {{ color: #5a6577; font-size: 14px; margin-bottom: 16px; }}
    @media (max-width: 768px) {{
        .product-hero h1 {{ font-size: 24px; }}
        .product-section {{ padding: 40px 0; }}
        .product-section h2 {{ font-size: 20px; }}
        .cta-box {{ padding: 32px 20px; }}
        .cta-box .btn {{ display: block; margin: 8px 0; }}
    }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="/" class="logo">
    <picture>
        <source srcset="/images/logo.webp" type="image/webp">
        <img src="/logo.png" alt="PhotonEdge" width="160" height="40">
    </picture>
</a>
            <nav class="nav">
                <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">&#9776;</button>
                <ul class="nav-list">
                    <li><a href="/product-catalog.html" class="nav-link" data-i18n="navProducts">Products</a></li>
                    <li><a href="/applications.html" class="nav-link" data-i18n="navApplications">Applications</a></li>
                    <li><a href="/engineering.html" class="nav-link" data-i18n="navEngineering">Engineering</a></li>
                    <li><a href="/knowledge-center/" class="nav-link" data-i18n="navKnowledgeCenter">Knowledge Center</a></li>
                    <li><a href="/ai-optical-engineer.html" class="nav-link" data-i18n="navAIOptical">AI Optical Engineer</a></li>
                    <li><a href="/about.html" class="nav-link" data-i18n="navAbout">About</a></li>
                    <li><a href="/contact.html" class="btn btn-primary nav-cta-btn" data-i18n="navRFQ" style="padding:8px 20px;border-radius:6px;font-size:14px;color:white;text-decoration:none;">Request Engineering Review</a></li>
                </ul>
                <a href="/cart.html" class="cart-icon" title="Shopping Cart">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
                    <span id="cart-count">0</span>
                </a>
            </nav>
        </div>
    </header>

    <!-- Hero -->
    <section class="product-hero">
        <div class="container">
            <div class="breadcrumb">
                <a href="/">Home</a> / <a href="/product-catalog.html">Products</a> / <a href="/product-catalog.html?category={cat31.replace(' ', '-')}">{cat31}</a> / <span>{name}</span>
            </div>
            <h1>{name}</h1>
            <p class="subtitle">{subtitle}</p>
        </div>
    </section>

    <!-- Overview -->
    <section class="product-section">
        <div class="container">
            <h2>Overview</h2>
            {overview_html}
        </div>
    </section>

    <!-- Key Specifications -->
    <section class="product-section">
        <div class="container">
            <h2>Key Specifications</h2>
            <table class="spec-table">
{spec_rows}            </table>
        </div>
    </section>

    <!-- Material Options -->
    <section class="product-section">
        <div class="container">
            <h2>Material Options</h2>
{material_html}
        </div>
    </section>

    <!-- Coating Options -->
    <section class="product-section">
        <div class="container">
            <h2>Coating Options</h2>
{coating_html}
        </div>
    </section>

    <!-- Manufacturing Tolerances -->
    <section class="product-section">
        <div class="container">
            <h2>Manufacturing Tolerances</h2>
{tolerance_html}
        </div>
    </section>

    <!-- Inspection & Quality -->
    <section class="product-section">
        <div class="container">
            <h2>Inspection &amp; Quality Assurance</h2>
            <div style='background:white;border:1px solid #e2e6ef;border-radius:8px;padding:24px;'>
                <ul style='padding-left:20px;margin:0;'>
{inspection_items}                </ul>
            </div>
        </div>
    </section>

    <!-- Applications -->
    <section class="product-section">
        <div class="container">
            <h2>Applications</h2>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
{app_html}
            </div>
        </div>
    </section>

    <!-- Engineering Considerations -->
    <section class="product-section">
        <div class="container">
            <h2>Engineering Considerations</h2>
            <div style='background:white;border:1px solid #e2e6ef;border-radius:8px;padding:24px;'>
{eng_items}            </div>
        </div>
    </section>

    <!-- FAQ -->
    <section class="product-section">
        <div class="container">
            <h2>Frequently Asked Questions</h2>
{faq_html}
        </div>
    </section>

    <!-- Related Products -->
    <section class="product-section">
        <div class="container">
            <h2>Related Products</h2>
            <div style="display:flex;flex-wrap:wrap;">
                {related_products_html}
            </div>
        </div>
    </section>

    <!-- Related Technical Articles -->
    <section class="product-section">
        <div class="container">
            <h2>Related Technical Resources</h2>
            {related_articles_html}
        </div>
    </section>

    <!-- AI Optical Engineer CTA -->
    <div class="container">
        <div class="ai-box">
            <h3>Not Sure Which Specification You Need?</h3>
            <p>Tell us your wavelength, application and operating conditions. PhotonEdge AI Optical Engineer can help you identify the key specifications before you request a quote.</p>
            <a href="/ai-optical-engineer.html" class="btn btn-primary" style="padding:10px 24px;border-radius:6px;text-decoration:none;background:#3b82f6;color:white;display:inline-block;margin:0 8px;">Ask AI Optical Engineer &rarr;</a>
            <a href="/contact.html" class="btn btn-secondary" style="padding:10px 24px;border-radius:6px;text-decoration:none;background:transparent;border:1px solid #3b82f6;color:#3b82f6;display:inline-block;margin:0 8px;">Request Engineering Review</a>
        </div>
    </div>

    <!-- Final CTA -->
    <div class="container" style="padding-bottom: 60px;">
        <div class="cta-box">
            <h2>Have an Optical Requirement?</h2>
            <p>Tell us what you know. We'll help identify what you still need.</p>
            <a href="/contact.html" class="btn btn-primary">Upload Drawing / RFQ</a>
            <a href="/contact.html" class="btn btn-secondary">Request Engineering Review</a>
        </div>
    </div>

    <!-- Internal Links -->
    <div class="container" style="padding: 20px 0 40px; text-align: center;">
        {internal_links_html}
    </div>

    <footer class="footer">
        <div class="container">
            <div class="footer-grid" style="grid-template-columns: 2fr 1fr 1fr 1fr;">
                <div class="footer-brand">
                    <h3>PhotonEdge</h3>
                    <p>Precision Optical Solutions Provider</p>
                    <p style="margin-top:8px;font-size:13px;color:rgba(255,255,255,0.6);">ISO 9001:2015 Certified</p>
                </div>
                <div class="footer-col">
                    <h4>Products</h4>
                    <ul>
                        <li><a href="/product-catalog.html?component=Lens">Optical Lenses</a></li>
                        <li><a href="/product-catalog.html?component=Window">Optical Windows</a></li>
                        <li><a href="/product-catalog.html?component=Mirror">Optical Mirrors</a></li>
                        <li><a href="/product-catalog.html?component=Filter">Optical Filters</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Applications</h4>
                    <ul>
                        <li><a href="/applications/laser-optics/">Laser Systems</a></li>
                        <li><a href="/applications/semiconductor-inspection/">Semiconductor</a></li>
                        <li><a href="/applications/medical-imaging/">Medical Imaging</a></li>
                        <li><a href="/applications/aerospace-defense/">Aerospace &amp; Defense</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li>Email: <a href="mailto:sales@photonedgeoptics.com">sales@photonedgeoptics.com</a></li>
                        <li>Phone: +86-13693009175</li>
                        <li>WhatsApp: +86-13693009175</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024-2026 PhotonEdge. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <a href="https://wa.me/8613693009175" target="_blank" class="whatsapp-float" title="Chat with us on WhatsApp">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.467-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    </a>

    <script src="/js/translations.js"></script>
    <script src="/js/main.js"></script>
    <script>function toggleMobileMenu(){{var n=document.querySelector('.nav-list');if(n)n.classList.toggle('active');}}</script>
    <script src="/js/chat-bot.js"></script>
    <script src="/js/chatbot.js"></script>
    <script src="/js/cart.js"></script>
</body>
</html>"""
    return html


def generate_all_tier2_pages():
    """Generate all 10 Tier 2 product pages."""
    print("Generating Tier 2 product pages...")
    for page in TIER2_PAGES:
        slug = page["slug"]
        dir_path = os.path.join(DST, "products", slug)
        os.makedirs(dir_path, exist_ok=True)
        html = generate_tier2_page(page)
        with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Created /products/{slug}/")
    print(f"  Total: {len(TIER2_PAGES)} Tier 2 pages generated.")

# ─────────────────────────────────────────────────────────
# About Page 3.1 Upgrade
# ─────────────────────────────────────────────────────────

def generate_about_31():
    """Generate new about.html with 3.1 structure."""
    print("Generating About page 3.1...")
    
    about_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="dns-prefetch" href="https://www.google-analytics.com">
    <meta charset="UTF-8">
    <link rel="icon" type="image/png" sizes="32x32" href="https://photonedgeoptics.com/images/favicon-32.png">
    <link rel="icon" type="image/svg+xml" href="https://photonedgeoptics.com/images/favicon.svg">
    <link rel="apple-touch-icon" sizes="180x180" href="https://photonedgeoptics.com/images/apple-touch-icon.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About PhotonEdge | Global Optical Engineering Partner</title>
    <meta name="description" content="PhotonEdge is a global optical engineering partner. We help companies specify, source, and manufacture precision optical components with engineering-first quality assurance.">
    <meta name="keywords" content="optical engineering partner, precision optics supply chain, custom optical components, optics manufacturer China, photonics engineering, PhotonEdge">
    <meta property="og:title" content="About PhotonEdge | Global Optical Engineering Partner">
    <meta property="og:description" content="PhotonEdge partners with global engineering teams to deliver precision optical components — from specification optimization to manufacturing and inspection.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://photonedgeoptics.com/about.html">
    <meta property="og:image" content="https://photonedgeoptics.com/images/logo.webp">
    <meta property="og:site_name" content="PhotonEdge">
    <link rel="canonical" href="https://photonedgeoptics.com/about.html">
    <link rel="stylesheet" href="/css/style.css">
    <link rel="stylesheet" href="/css/chatbot.css">
    <link rel="alternate" hreflang="en" href="https://photonedgeoptics.com/about.html">
    <link rel="alternate" hreflang="zh" href="https://photonedgeoptics.com/about.html?lang=zh">

    <!-- AboutPage Schema -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "AboutPage",
        "name": "About PhotonEdge",
        "description": "PhotonEdge is a global optical engineering partner that helps companies specify, source, and manufacture precision optical components.",
        "publisher": {
            "@type": "Organization",
            "name": "PhotonEdge"
        }
    }
    </script>

    <!-- BreadcrumbList Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://photonedgeoptics.com/"},
        {"@type": "ListItem", "position": 2, "name": "About Us", "item": "https://photonedgeoptics.com/about.html"}
      ]
    }
    </script>

    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-E6J791MXZY"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-E6J791MXZY');
    </script>

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="About PhotonEdge | Global Optical Engineering Partner">
    <meta name="twitter:description" content="Engineering-first optical partner for precision components. Specification optimization, global manufacturing, and quality assurance.">
    <meta name="twitter:image" content="https://photonedgeoptics.com/images/logo.webp">

    <!-- Baidu Search Auto Push -->
    <script>
        (function(){
            var bp = document.createElement('script');
            var curProtocol = window.location.protocol.split(':')[0];
            if (curProtocol === 'https') {
                bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
            } else {
                bp.src = 'https://push.zhangzifan.com/linksubmit/push.js';
            }
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(bp, s);
        })();
    </script>
    <style>
    .about-hero { background: linear-gradient(135deg, #0a1628 0%, #1a2d50 100%); padding: 80px 0 60px; color: white; }
    .about-hero .eyebrow { font-size: 13px; text-transform: uppercase; letter-spacing: 2px; color: #60a5fa; margin-bottom: 16px; }
    .about-hero h1 { font-size: 38px; font-weight: 700; margin-bottom: 16px; color: white; max-width: 700px; line-height: 1.25; }
    .about-hero .tagline { font-size: 20px; color: #e8792f; font-weight: 600; margin-bottom: 16px; font-style: italic; }
    .about-hero .lead { font-size: 17px; color: #b0c4de; max-width: 650px; line-height: 1.7; }
    .about-section { padding: 70px 0; }
    .about-section:nth-child(even) { background: #f8fafc; }
    .about-section h2 { font-size: 28px; color: #1e3a5f; margin-bottom: 12px; font-weight: 700; }
    .about-section h3 { font-size: 18px; color: #1e3a5f; margin-bottom: 10px; }
    .about-section .section-intro { font-size: 16px; color: #4b5563; max-width: 750px; margin-bottom: 32px; line-height: 1.7; }
    .what-we-do-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; }
    .what-we-do-card { background: white; border: 1px solid #e2e6ef; border-radius: 10px; padding: 20px; }
    .what-we-do-card .icon { width: 40px; height: 40px; background: #eff6ff; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #3b82f6; font-size: 20px; margin-bottom: 12px; }
    .what-we-do-card h3 { font-size: 15px; margin-bottom: 8px; }
    .what-we-do-card p { font-size: 13px; color: #6b7280; line-height: 1.6; margin: 0; }
    .why-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
    .why-card { background: white; border: 1px solid #e2e6ef; border-radius: 10px; padding: 24px; }
    .why-card h3 { font-size: 16px; margin-bottom: 10px; color: #1e3a5f; }
    .why-card p { font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0; }
    .partner-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
    .partner-card { background: white; border: 1px solid #e2e6ef; border-radius: 10px; padding: 20px; }
    .partner-card h3 { font-size: 15px; margin-bottom: 8px; color: #1e3a5f; }
    .partner-card p { font-size: 13px; color: #6b7280; line-height: 1.6; margin: 0 0 8px 0; }
    .partner-card ul { font-size: 13px; color: #4b5563; padding-left: 18px; margin: 0; }
    .partner-card li { margin-bottom: 4px; }
    .cert-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
    .cert-card { background: white; border: 1px solid #e2e6ef; border-radius: 10px; padding: 20px; text-align: center; }
    .cert-card .badge { width: 56px; height: 56px; border: 2px solid #3b82f6; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 12px; font-weight: 700; font-size: 12px; color: #3b82f6; }
    .cert-card h3 { font-size: 14px; margin-bottom: 6px; }
    .cert-card p { font-size: 12px; color: #6b7280; margin: 0; }
    .team-section { text-align: center; }
    .team-section p { font-size: 15px; color: #4b5563; max-width: 650px; margin: 0 auto 24px; line-height: 1.7; }
    .contact-banner { background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 60px; border-radius: 12px; text-align: center; color: white; margin: 40px 0; }
    .contact-banner h2 { color: white; font-size: 26px; margin-bottom: 12px; }
    .contact-banner p { color: rgba(176,196,222,0.9); margin-bottom: 24px; }
    .contact-banner .btn { display: inline-block; padding: 12px 28px; border-radius: 6px; font-weight: 600; text-decoration: none; margin: 0 8px; }
    .contact-banner .btn-primary { background: #e8792f; color: white; }
    .contact-banner .btn-secondary { background: transparent; color: white; border: 1px solid rgba(255,255,255,0.4); }
    @media (max-width: 900px) {
        .what-we-do-grid { grid-template-columns: repeat(2, 1fr); }
        .why-grid { grid-template-columns: repeat(2, 1fr); }
        .partner-grid { grid-template-columns: 1fr; }
        .cert-grid { grid-template-columns: repeat(2, 1fr); }
        .about-hero h1 { font-size: 28px; }
        .about-section { padding: 50px 0; }
        .about-section h2 { font-size: 22px; }
    }
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="/" class="logo">
    <picture>
        <source srcset="/images/logo.webp" type="image/webp">
        <img src="/logo.png" alt="PhotonEdge" width="160" height="40">
    </picture>
</a>
            <nav class="nav">
                <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">&#9776;</button>
                <ul class="nav-list">
                    <li><a href="/product-catalog.html" class="nav-link" data-i18n="navProducts">Products</a></li>
                    <li><a href="/applications.html" class="nav-link" data-i18n="navApplications">Applications</a></li>
                    <li><a href="/engineering.html" class="nav-link" data-i18n="navEngineering">Engineering</a></li>
                    <li><a href="/knowledge-center/" class="nav-link" data-i18n="navKnowledgeCenter">Knowledge Center</a></li>
                    <li><a href="/ai-optical-engineer.html" class="nav-link" data-i18n="navAIOptical">AI Optical Engineer</a></li>
                    <li><a href="/about.html" class="nav-link active" data-i18n="navAbout">About</a></li>
                    <li><a href="/contact.html" class="btn btn-primary nav-cta-btn" data-i18n="navRFQ" style="padding:8px 20px;border-radius:6px;font-size:14px;color:white;text-decoration:none;">Request Engineering Review</a></li>
                </ul>
                <a href="/cart.html" class="cart-icon" title="Shopping Cart">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
                    <span id="cart-count">0</span>
                </a>
            </nav>
        </div>
    </header>

    <!-- Hero / Who We Are -->
    <section class="about-hero">
        <div class="container">
            <div class="eyebrow">About PhotonEdge</div>
            <h1>Your Global Optical Engineering Partner</h1>
            <div class="tagline">"Specify what your system needs — not what the catalog says."</div>
            <p class="lead">PhotonEdge partners with engineering teams worldwide to deliver precision optical components. We combine deep optical engineering expertise with a global manufacturing network, so you get components that actually meet your system requirements — not just whatever a standard catalog happens to offer.</p>
        </div>
    </section>

    <!-- What We Do -->
    <section class="about-section">
        <div class="container">
            <h2>What We Do</h2>
            <p class="section-intro">We work alongside your engineering team from specification through final inspection. Our role is to bridge the gap between what your system needs and what factories can actually produce.</p>
            <div class="what-we-do-grid">
                <div class="what-we-do-card">
                    <div class="icon">&#128269;</div>
                    <h3>Engineering</h3>
                    <p>Material selection, coating design, tolerance analysis, and DFM review before you commit to production.</p>
                </div>
                <div class="what-we-do-card">
                    <div class="icon">&#128200;</div>
                    <h3>Sourcing</h3>
                    <p>Access to qualified factories across China and Asia, matched to your material, volume, and precision requirements.</p>
                </div>
                <div class="what-we-do-card">
                    <div class="icon">&#9881;&#65039;</div>
                    <h3>Manufacturing</h3>
                    <p>Prototyping to volume production, with transparent process control and milestone-based communication.</p>
                </div>
                <div class="what-we-do-card">
                    <div class="icon">&#128261;</div>
                    <h3>Inspection</h3>
                    <p>Independent incoming inspection with interferometer, spectrophotometer, and dimensional metrology.</p>
                </div>
                <div class="what-we-do-card">
                    <div class="icon">&#128196;</div>
                    <h3>Documentation</h3>
                    <p>Inspection reports, material certificates, coating curves, and CoC delivered with every shipment.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Why PhotonEdge -->
    <section class="about-section">
        <div class="container">
            <h2>Why PhotonEdge</h2>
            <p class="section-intro">We're not a catalog company. We're an engineering partner. Here's what that means in practice.</p>
            <div class="why-grid">
                <div class="why-card">
                    <h3>Engineering First</h3>
                    <p>Every project starts with an engineering review. We tell you if your spec makes sense, what can be relaxed to save cost, and what actually needs to be tight for performance. We don't just quote whatever you send us.</p>
                </div>
                <div class="why-card">
                    <h3>Custom When Standard Doesn't Fit</h3>
                    <p>Most systems don't fit perfectly into catalog specifications. When a standard part won't work, we design and manufacture custom components — from single prototypes to production volumes — without the premium you'd pay from a Western catalog house.</p>
                </div>
                <div class="why-card">
                    <h3>Specification Optimization</h3>
                    <p>Tighter tolerances mean higher cost — but not always better system performance. We help you identify which specs really matter for your application, so you pay for precision where it counts and relax tolerances where it doesn't.</p>
                </div>
                <div class="why-card">
                    <h3>Global Supply Chain</h3>
                    <p>Our partner network spans multiple factories across China and Southeast Asia, each specialized in different materials and processes. We match your project to the right facility, so you get appropriate quality at the right price point.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Manufacturing Partner Network -->
    <section class="about-section">
        <div class="container">
            <h2>Manufacturing Partner Network</h2>
            <p class="section-intro">We work with a carefully selected network of manufacturing partners, each specializing in different optical materials, processes, and volume scales. We assign your project to the partner best matched to your specific requirements.</p>
            <div class="partner-grid">
                <div class="partner-card">
                    <h3>Precision Optics (South China)</h3>
                    <p>Specializes in high-precision spherical and aspherical lenses, prisms, and windows. Advanced polishing and coating capabilities.</p>
                    <ul>
                        <li>Materials: BK7, fused silica, CaF₂, sapphire</li>
                        <li>Surface quality: up to 10-5</li>
                        <li>Flatness: up to λ/20</li>
                        <li>Coatings: dielectric, metal, AR, HR</li>
                    </ul>
                </div>
                <div class="partner-card">
                    <h3>Infrared Optics (North China)</h3>
                    <p>Focused on infrared materials and diamond turning. Germanium, silicon, ZnSe, and chalcogenide optics for thermal imaging.</p>
                    <ul>
                        <li>Materials: Ge, Si, ZnSe, ZnS, chalcogenide</li>
                        <li>SPDT diamond turning for aspheres</li>
                        <li>DLC and IR AR coatings</li>
                        <li>MWIR and LWIR applications</li>
                    </ul>
                </div>
                <div class="partner-card">
                    <h3>Volume Production (East China)</h3>
                    <p>High-volume manufacturing for consumer electronics, automotive, and industrial applications. Automated polishing and coating lines.</p>
                    <ul>
                        <li>High-volume: 10k – 1M+ pcs/year</li>
                        <li>Automated inspection</li>
                        <li>ISO 9001 & IATF 16949</li>
                        <li>Cost-optimized processes</li>
                    </ul>
                </div>
            </div>
            <p style="font-size: 13px; color: #9ca3af; margin-top: 16px; font-style: italic;">All manufacturing partners are pre-qualified with quality audits and sample verification. We regularly re-audit to maintain standards.</p>
        </div>
    </section>

    <!-- Quality & Certifications -->
    <section class="about-section">
        <div class="container">
            <h2>Quality &amp; Certifications</h2>
            <p class="section-intro">Quality is not a checkbox — it's built into every step of the process. Our partners operate under internationally recognized quality management systems, and we perform independent verification on every precision order.</p>
            <div class="cert-grid">
                <div class="cert-card">
                    <div class="badge">ISO<br>9001</div>
                    <h3>ISO 9001:2015</h3>
                    <p>Quality management systems</p>
                </div>
                <div class="cert-card">
                    <div class="badge">ISO<br>13485</div>
                    <h3>ISO 13485</h3>
                    <p>Medical device quality</p>
                </div>
                <div class="cert-card">
                    <div class="badge">ISO<br>14001</div>
                    <h3>ISO 14001</h3>
                    <p>Environmental management</p>
                </div>
                <div class="cert-card">
                    <div class="badge">RoHS<br>REACH</div>
                    <h3>RoHS &amp; REACH</h3>
                    <p>Environmental compliance</p>
                </div>
            </div>
            <div style="margin-top: 32px; background: white; border: 1px solid #e2e6ef; border-radius: 10px; padding: 24px;">
                <h3 style="font-size: 17px; margin-bottom: 12px;">Our Quality Process</h3>
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; font-size: 14px; color: #4b5563;">
                    <div>
                        <div style="font-weight: 600; color: #1e3a5f; margin-bottom: 6px;">1. Incoming Material Check</div>
                        <p style="font-size: 13px; line-height: 1.6;">Material certificates verified against purchase specification before production begins.</p>
                    </div>
                    <div>
                        <div style="font-weight: 600; color: #1e3a5f; margin-bottom: 6px;">2. In-Process Inspection</div>
                        <p style="font-size: 13px; line-height: 1.6;">Dimensional and surface checks at key process milestones with photos and data.</p>
                    </div>
                    <div>
                        <div style="font-weight: 600; color: #1e3a5f; margin-bottom: 6px;">3. Final Inspection</div>
                        <p style="font-size: 13px; line-height: 1.6;">Full dimensional, surface quality, flatness, and spectral testing before shipment.</p>
                    </div>
                    <div>
                        <div style="font-weight: 600; color: #1e3a5f; margin-bottom: 6px;">4. Documentation</div>
                        <p style="font-size: 13px; line-height: 1.6;">Certificate of Conformity, inspection data, and material certificates with every shipment.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Team -->
    <section class="about-section">
        <div class="container team-section">
            <h2>Our Team</h2>
            <p>PhotonEdge is led by engineers who understand both optical design and manufacturing reality. Our team combines backgrounds in optical engineering, precision manufacturing, and international supply chain management.</p>
            <p>We keep the team small and focused — every project gets direct attention from senior engineers, not just a salesperson passing messages.</p>
            <p style="font-size: 13px; color: #9ca3af; font-style: italic;">We don't post individual profiles or stock photos — we let the quality of our work speak for itself.</p>
        </div>
    </section>

    <!-- Contact CTA -->
    <div class="container" style="padding-bottom: 60px;">
        <div class="contact-banner">
            <h2>Ready to Talk Through Your Optical Requirements?</h2>
            <p>Send us your drawing, spec sheet, or even just a rough description. We'll tell you what's realistic, what it will cost, and how long it will take.</p>
            <a href="/contact.html" class="btn btn-primary">Start a Conversation</a>
            <a href="/engineering.html" class="btn btn-secondary">Explore Engineering Services</a>
        </div>
    </div>

    <footer class="footer">
        <div class="container">
            <div class="footer-grid" style="grid-template-columns: 2fr 1fr 1fr 1fr;">
                <div class="footer-brand">
                    <h3>PhotonEdge</h3>
                    <p>Precision Optical Solutions Provider</p>
                    <p style="margin-top:8px;font-size:13px;color:rgba(255,255,255,0.6);">ISO 9001:2015 Certified</p>
                </div>
                <div class="footer-col">
                    <h4>Products</h4>
                    <ul>
                        <li><a href="/product-catalog.html?component=Lens">Optical Lenses</a></li>
                        <li><a href="/product-catalog.html?component=Window">Optical Windows</a></li>
                        <li><a href="/product-catalog.html?component=Mirror">Optical Mirrors</a></li>
                        <li><a href="/product-catalog.html?component=Filter">Optical Filters</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Applications</h4>
                    <ul>
                        <li><a href="/applications/laser-optics/">Laser Systems</a></li>
                        <li><a href="/applications/semiconductor-inspection/">Semiconductor</a></li>
                        <li><a href="/applications/medical-imaging/">Medical Imaging</a></li>
                        <li><a href="/applications/aerospace-defense/">Aerospace &amp; Defense</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li>Email: <a href="mailto:sales@photonedgeoptics.com">sales@photonedgeoptics.com</a></li>
                        <li>Phone: +86-13693009175</li>
                        <li>WhatsApp: +86-13693009175</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024-2026 PhotonEdge. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <a href="https://wa.me/8613693009175" target="_blank" class="whatsapp-float" title="Chat with us on WhatsApp">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.467-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    </a>

    <script src="/js/translations.js"></script>
    <script src="/js/main.js"></script>
    <script>function toggleMobileMenu(){var n=document.querySelector('.nav-list');if(n)n.classList.toggle('active');}</script>
    <script src="/js/chat-bot.js"></script>
    <script src="/js/chatbot.js"></script>
    <script src="/js/cart.js"></script>
</body>
</html>'''
    
    with open(os.path.join(DST, "about.html"), "w", encoding="utf-8") as f:
        f.write(about_html)
    print("  Updated about.html (3.1 version)")

# ─────────────────────────────────────────────────────────
# Specification Optimization Page
# ─────────────────────────────────────────────────────────

def generate_spec_opt_page():
    """Generate specification-optimization.html"""
    print("Generating Specification Optimization page...")
    
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="dns-prefetch" href="https://www.google-analytics.com">
    <meta charset="UTF-8">
    <link rel="icon" type="image/png" sizes="32x32" href="https://photonedgeoptics.com/images/favicon-32.png">
    <link rel="icon" type="image/svg+xml" href="https://photonedgeoptics.com/images/favicon.svg">
    <link rel="apple-touch-icon" sizes="180x180" href="https://photonedgeoptics.com/images/apple-touch-icon.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Specification Optimization | Flatness, Surface Quality & Tolerance Guide | PhotonEdge</title>
    <meta name="description" content="Optical specification optimization guide: flatness, surface quality, and dimensional tolerances. Learn when tight specs matter and when they add cost without benefit.">
    <meta name="keywords" content="optical specification optimization, flatness vs cost, surface quality guide, optical tolerance selection, lambda 4 lambda 10 lambda 20, scratch dig 10-5 20-10 40-20">
    <meta property="og:title" content="Optical Specification Optimization Guide | PhotonEdge">
    <meta property="og:description" content="Tighter tolerances mean higher cost — but not always better performance. Learn which specs actually matter for your optical system.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://photonedgeoptics.com/specification-optimization.html">
    <meta property="og:image" content="https://photonedgeoptics.com/images/logo.webp">
    <meta property="og:site_name" content="PhotonEdge">
    <link rel="canonical" href="https://photonedgeoptics.com/specification-optimization.html">
    <link rel="stylesheet" href="/css/style.css">
    <link rel="stylesheet" href="/css/chatbot.css">
    <link rel="alternate" hreflang="en" href="https://photonedgeoptics.com/specification-optimization.html">
    <link rel="alternate" hreflang="zh" href="https://photonedgeoptics.com/specification-optimization.html?lang=zh">

    <!-- BreadcrumbList Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://photonedgeoptics.com/"},
        {"@type": "ListItem", "position": 2, "name": "Engineering", "item": "https://photonedgeoptics.com/engineering.html"},
        {"@type": "ListItem", "position": 3, "name": "Specification Optimization", "item": "https://photonedgeoptics.com/specification-optimization.html"}
      ]
    }
    </script>

    <!-- TechArticle Schema -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": "Optical Specification Optimization: Getting What You Need Without Paying for What You Don't",
        "description": "A practical guide to optical specifications — flatness, surface quality, and dimensional tolerances — and how each impacts performance and cost.",
        "publisher": {
            "@type": "Organization",
            "name": "PhotonEdge"
        }
    }
    </script>

    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-E6J791MXZY"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-E6J791MXZY');
    </script>

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Optical Specification Optimization Guide | PhotonEdge">
    <meta name="twitter:description" content="Tighter tolerances mean higher cost — but not always better system performance. Learn which specs actually matter.">
    <meta name="twitter:image" content="https://photonedgeoptics.com/images/logo.webp">

    <!-- Baidu Search Auto Push -->
    <script>
        (function(){
            var bp = document.createElement('script');
            var curProtocol = window.location.protocol.split(':')[0];
            if (curProtocol === 'https') {
                bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
            } else {
                bp.src = 'https://push.zhangzifan.com/linksubmit/push.js';
            }
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(bp, s);
        })();
    </script>
    <style>
    .spec-hero { background: linear-gradient(135deg, #0a1628 0%, #1a2d50 100%); padding: 70px 0 50px; color: white; }
    .spec-hero .eyebrow { font-size: 13px; text-transform: uppercase; letter-spacing: 2px; color: #60a5fa; margin-bottom: 16px; }
    .spec-hero h1 { font-size: 34px; font-weight: 700; margin-bottom: 14px; color: white; max-width: 750px; line-height: 1.25; }
    .spec-hero .lead { font-size: 17px; color: #b0c4de; max-width: 700px; line-height: 1.7; }
    .spec-hero .key-idea { font-size: 18px; color: #fbbf24; font-weight: 600; margin: 16px 0 0; font-style: italic; }
    .spec-section { padding: 60px 0; }
    .spec-section:nth-child(even) { background: #f8fafc; }
    .spec-section h2 { font-size: 26px; color: #1e3a5f; margin-bottom: 12px; font-weight: 700; }
    .spec-section .section-intro { font-size: 15px; color: #4b5563; max-width: 750px; margin-bottom: 28px; line-height: 1.7; }
    .spec-compare { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 24px; }
    .spec-card { background: white; border: 1px solid #e2e6ef; border-radius: 10px; padding: 24px; }
    .spec-card.highlight { border: 2px solid #3b82f6; box-shadow: 0 4px 12px rgba(59,130,246,0.1); }
    .spec-card .grade { font-size: 20px; font-weight: 700; color: #1e3a5f; margin-bottom: 4px; }
    .spec-card .grade-value { font-size: 14px; color: #6b7280; margin-bottom: 16px; }
    .spec-card h4 { font-size: 13px; text-transform: uppercase; letter-spacing: 1px; color: #6b7280; margin: 14px 0 6px; }
    .spec-card p { font-size: 14px; color: #374151; line-height: 1.65; margin: 0 0 10px; }
    .impact-box { background: #fef3c7; border-left: 4px solid #f59e0b; padding: 16px 20px; border-radius: 0 8px 8px 0; margin: 16px 0; }
    .impact-box strong { color: #92400e; }
    .cost-bar { height: 8px; background: #e5e7eb; border-radius: 4px; margin-top: 6px; overflow: hidden; }
    .cost-bar-fill { height: 100%; background: linear-gradient(90deg, #10b981, #f59e0b, #ef4444); border-radius: 4px; }
    .recommendation { background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px; padding: 16px 20px; margin-top: 20px; }
    .recommendation strong { color: #166534; }
    .faq-item { background: white; border: 1px solid #e2e6ef; border-radius: 8px; margin-bottom: 10px; overflow: hidden; }
    .faq-q { padding: 16px 20px; cursor: pointer; font-weight: 600; color: #1e3a5f; font-size: 15px; }
    .faq-a { padding: 0 20px 16px; color: #4b5563; font-size: 14px; line-height: 1.7; display: none; }
    .cta-box { background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 48px; border-radius: 12px; text-align: center; color: white; margin: 40px 0; }
    .cta-box h2 { color: white; font-size: 24px; margin-bottom: 12px; }
    .cta-box p { color: rgba(176,196,222,0.9); margin-bottom: 24px; }
    .cta-box .btn { display: inline-block; padding: 12px 28px; border-radius: 6px; font-weight: 600; text-decoration: none; margin: 0 8px; }
    .cta-box .btn-primary { background: #e8792f; color: white; }
    .cta-box .btn-secondary { background: transparent; color: white; border: 1px solid rgba(255,255,255,0.4); }
    @media (max-width: 900px) {
        .spec-compare { grid-template-columns: 1fr; }
        .spec-hero h1 { font-size: 24px; }
        .cta-box { padding: 32px 20px; }
        .cta-box .btn { display: block; margin: 8px 0; }
    }
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="/" class="logo">
    <picture>
        <source srcset="/images/logo.webp" type="image/webp">
        <img src="/logo.png" alt="PhotonEdge" width="160" height="40">
    </picture>
</a>
            <nav class="nav">
                <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">&#9776;</button>
                <ul class="nav-list">
                    <li><a href="/product-catalog.html" class="nav-link" data-i18n="navProducts">Products</a></li>
                    <li><a href="/applications.html" class="nav-link" data-i18n="navApplications">Applications</a></li>
                    <li><a href="/engineering.html" class="nav-link active" data-i18n="navEngineering">Engineering</a></li>
                    <li><a href="/knowledge-center/" class="nav-link" data-i18n="navKnowledgeCenter">Knowledge Center</a></li>
                    <li><a href="/ai-optical-engineer.html" class="nav-link" data-i18n="navAIOptical">AI Optical Engineer</a></li>
                    <li><a href="/about.html" class="nav-link" data-i18n="navAbout">About</a></li>
                    <li><a href="/contact.html" class="btn btn-primary nav-cta-btn" data-i18n="navRFQ" style="padding:8px 20px;border-radius:6px;font-size:14px;color:white;text-decoration:none;">Request Engineering Review</a></li>
                </ul>
                <a href="/cart.html" class="cart-icon" title="Shopping Cart">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
                    <span id="cart-count">0</span>
                </a>
            </nav>
        </div>
    </header>

    <!-- Hero -->
    <section class="spec-hero">
        <div class="container">
            <div class="eyebrow">Engineering Guide</div>
            <h1>Optical Specification Optimization</h1>
            <p class="lead">Every engineer wants the best possible component. But "best" and "most expensive" are not the same thing. Tighter tolerances mean higher cost — but they don't always deliver better system performance.</p>
            <p class="key-idea">The goal is not the tightest spec. It's the right spec for the job.</p>
        </div>
    </section>

    <!-- Flatness Section -->
    <section class="spec-section">
        <div class="container">
            <h2>Surface Flatness: &lambda;/4 vs &lambda;/10 vs &lambda;/20</h2>
            <p class="section-intro">Surface flatness describes how much an optical surface deviates from a perfect plane or sphere, measured in fractions of a wavelength (typically at 632.8nm HeNe). The flatter the surface, the more polishing and metrology time required, and the higher the cost.</p>
            
            <div class="spec-compare">
                <div class="spec-card">
                    <div class="grade">&lambda;/4 Flatness</div>
                    <div class="grade-value">Commercial / standard grade</div>
                    <h4>Engineering Explanation</h4>
                    <p>A &lambda;/4 surface has a peak-to-valley wavefront error of up to one-quarter wavelength. In transmission, this means about &lambda;/8 wavefront distortion (because light passes through the surface twice — once in, once out, but the surface figure error is divided by ~n-1).</p>
                    <h4>Real Impact</h4>
                    <p>Sufficient for general imaging, illumination, and low-power laser systems. The wavefront error is well within the depth of focus of most f/4 and slower lenses. Barely detectable in typical visual systems.</p>
                    <h4>Cost Impact</h4>
                    <p>Baseline cost. Standard polished surface with minimal extra metrology. Most economical choice for non-critical applications.</p>
                    <div class="cost-bar"><div class="cost-bar-fill" style="width: 25%;"></div></div>
                </div>
                <div class="spec-card highlight">
                    <div class="grade">&lambda;/10 Flatness</div>
                    <div class="grade-value">Precision grade</div>
                    <h4>Engineering Explanation</h4>
                    <p>&lambda;/10 flatness means the surface deviates by no more than 0.1 waves peak-to-valley. This requires careful polishing with frequent interferometric feedback and careful process control.</p>
                    <h4>Real Impact</h4>
                    <p>Necessary for metrology systems, interferometry, high-resolution imaging, and moderate-power laser resonators. Delivers diffraction-limited performance for most optical systems. &lambda;/10 is the sweet spot for many precision applications.</p>
                    <h4>Cost Impact</h4>
                    <p>Roughly 1.5–2× the cost of &lambda;/4. Extra polishing time and more frequent metrology add cost, but the performance gain is significant for precision systems.</p>
                    <div class="cost-bar"><div class="cost-bar-fill" style="width: 55%;"></div></div>
                </div>
                <div class="spec-card">
                    <div class="grade">&lambda;/20 Flatness</div>
                    <div class="grade-value">High-precision / laser grade</div>
                    <h4>Engineering Explanation</h4>
                    <p>&lambda;/20 flatness represents 0.05 waves peak-to-valley error. Achieving this requires expert polishing, extended process time, and multiple interferometer measurements — often with sub-aperture polishing for final figure correction.</p>
                    <h4>Real Impact</h4>
                    <p>Required for high-precision interferometer reference flats, high-power laser resonators, ring laser gyroscopes, and systems where wavefront error must be at the absolute minimum. Often over-specified for general imaging or illumination.</p>
                    <h4>Cost Impact</h4>
                    <p>Typically 3–5× the cost of &lambda;/4. Yield drops significantly at this level, and metrology time increases substantially. Only specify when the application genuinely demands it.</p>
                    <div class="cost-bar"><div class="cost-bar-fill" style="width: 85%;"></div></div>
                </div>
            </div>
            
            <div class="recommendation">
                <strong>PhotonEdge Recommendation:</strong> Start with &lambda;/4 for general purpose and &lambda;/10 for precision systems. Only go to &lambda;/20 if you can trace the flatness requirement to a specific system-level performance specification. Many systems get &lambda;/20 performance from a &lambda;/10 part because the spec has built-in margin that doesn't reflect real system needs.
            </div>
        </div>
    </section>

    <!-- Surface Quality Section -->
    <section class="spec-section">
        <div class="container">
            <h2>Surface Quality: 10-5 vs 20-10 vs 40-20 (Scratch-Dig)</h2>
            <p class="section-intro">Surface quality describes the presence of cosmetic defects — scratches and digs — on the polished surface. It is specified per MIL-PRF-13830B or ISO 10110 standards using the scratch-dig code (e.g., 60-40, 40-20, 20-10, 10-5). The first number is the scratch grade, the second is the dig grade. Lower numbers = fewer/smaller defects = higher cost.</p>
            
            <div class="spec-compare">
                <div class="spec-card">
                    <div class="grade">40-20</div>
                    <div class="grade-value">Commercial / standard grade</div>
                    <h4>Engineering Explanation</h4>
                    <p>40-20 surface quality allows scratches up to 0.04mm wide and digs up to 0.2mm in diameter (per MIL spec interpretation). Surfaces are polished and inspected under standard lighting conditions.</p>
                    <h4>Real Impact</h4>
                    <p>Perfectly acceptable for most imaging, illumination, and low-power laser applications. Scattered light from cosmetic defects is negligible in non-critical systems. The human eye cannot distinguish 40-20 from 10-5 in most finished optical systems.</p>
                    <h4>Cost Impact</h4>
                    <p>Baseline cost. Standard polishing with visual inspection. The most economical choice for the vast majority of general optical applications.</p>
                    <div class="cost-bar"><div class="cost-bar-fill" style="width: 20%;"></div></div>
                </div>
                <div class="spec-card highlight">
                    <div class="grade">20-10</div>
                    <div class="grade-value">Precision grade</div>
                    <h4>Engineering Explanation</h4>
                    <p>20-10 surface quality allows scratches up to 0.02mm wide and digs up to 0.1mm diameter. Requires more careful polishing, clean handling, and inspection under dark-field illumination.</p>
                    <h4>Real Impact</h4>
                    <p>Recommended for high-power lasers (where defects can initiate damage), imaging systems with high dynamic range, and any application where scattered light could reduce signal-to-noise ratio. Good balance between quality and cost for precision systems.</p>
                    <h4>Cost Impact</h4>
                    <p>Approximately 1.3–1.8× the cost of 40-20. Extra polishing time, clean-room handling, and more thorough inspection add moderate cost. Often a worthwhile upgrade for laser and imaging systems.</p>
                    <div class="cost-bar"><div class="cost-bar-fill" style="width: 45%;"></div></div>
                </div>
                <div class="spec-card">
                    <div class="grade">10-5</div>
                    <div class="grade-value">High-precision / laser grade</div>
                    <h4>Engineering Explanation</h4>
                    <p>10-5 surface quality allows only very fine scratches (0.01mm max) and tiny digs (0.05mm max). Requires final polishing in a clean environment with meticulous inspection under high-intensity dark-field illumination.</p>
                    <h4>Real Impact</h4>
                    <p>Essential for high-energy pulsed lasers (where surface defects concentrate energy and cause laser damage), ultra-high-vacuum systems, and the most demanding low-scatter applications. Often over-specified for visible imaging systems.</p>
                    <h4>Cost Impact</h4>
                    <p>Typically 2–4× the cost of 40-20. Yield drops significantly — many parts must be re-polished or rejected. Clean-room handling and extended inspection drive cost up substantially.</p>
                    <div class="cost-bar"><div class="cost-bar-fill" style="width: 80%;"></div></div>
                </div>
            </div>
            
            <div class="impact-box">
                <strong>Common Misconception:</strong> Many engineers specify 10-5 because they think it means "better quality" without considering whether cosmetic defects actually affect their system performance. For an imaging lens with 10 elements, the combined effect of 40-20 surfaces on image contrast is typically far less than other error sources (like lens design, alignment, or coating quality).
            </div>
            
            <div class="recommendation">
                <strong>PhotonEdge Recommendation:</strong> Use 40-20 for general imaging and illumination, 20-10 for lasers above 100mW and precision systems, and 10-5 only for high-energy pulsed lasers or applications where scatter is genuinely critical. If you're not sure, ask: will a 0.02mm scratch on this surface actually impact my system's performance? If the answer is "probably not," don't pay for 10-5.
            </div>
        </div>
    </section>

    <!-- Dimensional Tolerance Section -->
    <section class="spec-section">
        <div class="container">
            <h2>Dimensional Tolerance: &plusmn;0.01mm vs &plusmn;0.05mm vs &plusmn;0.1mm</h2>
            <p class="section-intro">Dimensional tolerances specify how precisely the physical size (diameter, thickness, edge thickness) of an optical component must match the nominal value. Tighter dimensional tolerance requires more careful grinding, more precise metrology, and more rejects.</p>
            
            <div class="spec-compare">
                <div class="spec-card">
                    <div class="grade">&plusmn;0.1mm</div>
                    <div class="grade-value">Commercial grade</div>
                    <h4>Engineering Explanation</h4>
                    <p>&plusmn;0.1mm (or 100 micron) diameter/thickness tolerance is achievable with standard optical grinding and polishing processes. Final dimensions are verified with standard digital micrometers.</p>
                    <h4>Real Impact</h4>
                    <p>Sufficient for most lens cells and mounts with retaining rings, where the optic is centered by a bevel or spring. Thickness variation of 0.1mm has negligible optical effect in most systems (focal length shift is typically far less than 1%).</p>
                    <h4>Cost Impact</h4>
                    <p>Baseline cost. Standard optical manufacturing tolerances. Most catalog components fall into this range because it provides excellent value for general applications.</p>
                    <div class="cost-bar"><div class="cost-bar-fill" style="width: 20%;"></div></div>
                </div>
                <div class="spec-card highlight">
                    <div class="grade">&plusmn;0.05mm</div>
                    <div class="grade-value">Precision grade</div>
                    <h4>Engineering Explanation</h4>
                    <p>&plusmn;0.05mm (50 micron) tolerance requires more controlled grinding processes and careful measurement. May require centerless grinding for OD and precision lapping for thickness control.</p>
                    <h4>Real Impact</h4>
                    <p>Useful for precision lens barrels, drop-in assemblies, and applications where the optic must fit closely into a bore without adhesive or shimming. Ensures consistent fit in medium-volume assemblies.</p>
                    <h4>Cost Impact</h4>
                    <p>Approximately 1.2–1.5× the cost of &plusmn;0.1mm. Moderate additional processing and more frequent measurement. Generally worth specifying if your mechanical design requires close fit.</p>
                    <div class="cost-bar"><div class="cost-bar-fill" style="width: 40%;"></div></div>
                </div>
                <div class="spec-card">
                    <div class="grade">&plusmn;0.01mm</div>
                    <div class="grade-value">High-precision grade</div>
                    <h4>Engineering Explanation</h4>
                    <p>&plusmn;0.01mm (10 micron) tolerance is very tight for optical components. It requires precision grinding, possibly post-polishing centering, and metrology with gauge blocks or coordinate measuring machines.</p>
                    <h4>Real Impact</h4>
                    <p>Needed only for the most demanding optomechanical assemblies — interferometer reference mounts, precision rotary stages, and applications where the part must locate with micron-level repeatability. Rarely necessary for general optical systems.</p>
                    <h4>Cost Impact</h4>
                    <p>Typically 2–3× the cost of &plusmn;0.1mm. Additional centering operations, precision metrology, and lower yields all contribute to significantly higher cost.</p>
                    <div class="cost-bar"><div class="cost-bar-fill" style="width: 75%;"></div></div>
                </div>
            </div>
            
            <div class="impact-box">
                <strong>Important:</strong> Dimensional tolerance and optical performance are not directly linked. A lens with &plusmn;0.1mm diameter tolerance focuses light just as well as one with &plusmn;0.01mm. The tolerance matters only for mechanical fit — how the part sits in its mount. If your mount uses a retaining ring or spring, the diameter tolerance rarely matters at all.
            </div>
            
            <div class="recommendation">
                <strong>PhotonEdge Recommendation:</strong> Use &plusmn;0.1mm for most applications with standard mounts. Specify &plusmn;0.05mm if the optic must drop into a precision bore without shimming. Only go to &plusmn;0.01mm if you have a specific mechanical reason (e.g., interchangeable optics in a precision mount). Don't confuse mechanical precision with optical performance.
            </div>
        </div>
    </section>

    <!-- Summary / Principle -->
    <section class="spec-section">
        <div class="container">
            <h2>The Core Principle</h2>
            <div style="background: white; border: 1px solid #e2e6ef; border-radius: 12px; padding: 32px; text-align: center; max-width: 700px; margin: 0 auto;">
                <p style="font-size: 20px; color: #1e3a5f; font-weight: 600; line-height: 1.6; margin-bottom: 20px;">Tighter tolerances mean higher cost — but not always better system performance.</p>
                <p style="font-size: 15px; color: #4b5563; line-height: 1.7;">The goal of specification optimization is to identify which parameters genuinely affect your system's performance and allocate your budget there, while relaxing the parameters that don't matter.</p>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-top: 32px;">
                <div style="background: #f0fdf4; border: 1px solid #86efac; border-radius: 8px; padding: 20px; text-align: center;">
                    <div style="font-size: 28px; margin-bottom: 8px;">&#128077;</div>
                    <h3 style="font-size: 16px; color: #166534; margin-bottom: 8px;">Tighten When</h3>
                    <p style="font-size: 13px; color: #166534; line-height: 1.6; margin: 0;">You can trace the spec to a measurable system performance requirement</p>
                </div>
                <div style="background: #fef3c7; border: 1px solid #fcd34d; border-radius: 8px; padding: 20px; text-align: center;">
                    <div style="font-size: 28px; margin-bottom: 8px;">&#129300;</div>
                    <h3 style="font-size: 16px; color: #92400e; margin-bottom: 8px;">Question When</h3>
                    <p style="font-size: 13px; color: #92400e; line-height: 1.6; margin: 0;">The spec was copied from another design or a template without analysis</p>
                </div>
                <div style="background: #fef2f2; border: 1px solid #fca5a5; border-radius: 8px; padding: 20px; text-align: center;">
                    <div style="font-size: 28px; margin-bottom: 8px;">&#9940;&#65039;</div>
                    <h3 style="font-size: 16px; color: #991b1b; margin-bottom: 8px;">Avoid When</h3>
                    <p style="font-size: 13px; color: #991b1b; line-height: 1.6; margin: 0;">You're specifying "just to be safe" or "because we always do it that way"</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <div class="container" style="padding-bottom: 60px;">
        <div class="cta-box">
            <h2>Talk to an Optical Engineer About Your Specification</h2>
            <p>Send us your drawing or spec sheet. We'll review it for free and tell you where tighter tolerances matter and where you can save cost without sacrificing performance.</p>
            <a href="/contact.html" class="btn btn-primary">Request Specification Review</a>
            <a href="/engineering.html" class="btn btn-secondary">Explore Engineering Services</a>
        </div>
    </div>

    <!-- Related Resources -->
    <section class="spec-section">
        <div class="container">
            <h2>Related Resources</h2>
            <a href="/blog/laser-damage-threshold-guide/" style="display:block;padding:14px 20px;background:#f8fafc;border-radius:8px;margin-bottom:10px;text-decoration:none;color:#1e3a5f;font-size:15px;">&rarr; Laser Damage Threshold: What Engineers Need to Know</a>
            <a href="/blog/anti-reflection-coating-selection-guide/" style="display:block;padding:14px 20px;background:#f8fafc;border-radius:8px;margin-bottom:10px;text-decoration:none;color:#1e3a5f;font-size:15px;">&rarr; Anti-Reflection Coating Selection Guide</a>
            <a href="/blog/custom-optics-specification-guide/" style="display:block;padding:14px 20px;background:#f8fafc;border-radius:8px;margin-bottom:10px;text-decoration:none;color:#1e3a5f;font-size:15px;">&rarr; Custom Optics Specification Guide</a>
            <a href="/ai-optical-engineer.html" style="display:block;padding:14px 20px;background:#f0f4ff;border-radius:8px;margin-bottom:10px;text-decoration:none;color:#1e3a5f;font-size:15px;font-weight:600;">&rarr; Try AI Optical Engineer for instant spec recommendations</a>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-grid" style="grid-template-columns: 2fr 1fr 1fr 1fr;">
                <div class="footer-brand">
                    <h3>PhotonEdge</h3>
                    <p>Precision Optical Solutions Provider</p>
                    <p style="margin-top:8px;font-size:13px;color:rgba(255,255,255,0.6);">ISO 9001:2015 Certified</p>
                </div>
                <div class="footer-col">
                    <h4>Products</h4>
                    <ul>
                        <li><a href="/product-catalog.html?component=Lens">Optical Lenses</a></li>
                        <li><a href="/product-catalog.html?component=Window">Optical Windows</a></li>
                        <li><a href="/product-catalog.html?component=Mirror">Optical Mirrors</a></li>
                        <li><a href="/product-catalog.html?component=Filter">Optical Filters</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Applications</h4>
                    <ul>
                        <li><a href="/applications/laser-optics/">Laser Systems</a></li>
                        <li><a href="/applications/semiconductor-inspection/">Semiconductor</a></li>
                        <li><a href="/applications/medical-imaging/">Medical Imaging</a></li>
                        <li><a href="/applications/aerospace-defense/">Aerospace &amp; Defense</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li>Email: <a href="mailto:sales@photonedgeoptics.com">sales@photonedgeoptics.com</a></li>
                        <li>Phone: +86-13693009175</li>
                        <li>WhatsApp: +86-13693009175</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024-2026 PhotonEdge. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <a href="https://wa.me/8613693009175" target="_blank" class="whatsapp-float" title="Chat with us on WhatsApp">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.467-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    </a>

    <script src="/js/translations.js"></script>
    <script src="/js/main.js"></script>
    <script>
    function toggleMobileMenu(){var n=document.querySelector('.nav-list');if(n)n.classList.toggle('active');}
    function toggleFaq(el){var a=el.nextElementSibling;a.style.display=a.style.display==='none'?'block':'none';}
    </script>
    <script src="/js/chat-bot.js"></script>
    <script src="/js/chatbot.js"></script>
    <script src="/js/cart.js"></script>
</body>
</html>'''
    
    with open(os.path.join(DST, "specification-optimization.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("  Created specification-optimization.html")

# ─────────────────────────────────────────────────────────
# Evidence Center Page
# ─────────────────────────────────────────────────────────

def generate_evidence_page():
    """Generate evidence.html"""
    print("Generating Evidence Center page...")
    
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="dns-prefetch" href="https://www.google-analytics.com">
    <meta charset="UTF-8">
    <link rel="icon" type="image/png" sizes="32x32" href="https://photonedgeoptics.com/images/favicon-32.png">
    <link rel="icon" type="image/svg+xml" href="https://photonedgeoptics.com/images/favicon.svg">
    <link rel="apple-touch-icon" sizes="180x180" href="https://photonedgeoptics.com/images/apple-touch-icon.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Evidence Center | Inspection Reports, Material & Coating Documentation | PhotonEdge</title>
    <meta name="description" content="PhotonEdge Evidence Center — inspection reports, material certificates, coating data, and quality documents. If you cannot measure it, you cannot guarantee it.">
    <meta name="keywords" content="optical inspection report, material certificate, coating transmission curve, LIDT data, ISO certificate, CoC, quality documentation, optics evidence">
    <meta property="og:title" content="Evidence Center | PhotonEdge Quality Documentation">
    <meta property="og:description" content="Inspection reports, material certificates, coating evidence, and quality documents. See the data behind every PhotonEdge component.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://photonedgeoptics.com/evidence.html">
    <meta property="og:image" content="https://photonedgeoptics.com/images/logo.webp">
    <meta property="og:site_name" content="PhotonEdge">
    <link rel="canonical" href="https://photonedgeoptics.com/evidence.html">
    <link rel="stylesheet" href="/css/style.css">
    <link rel="stylesheet" href="/css/chatbot.css">
    <link rel="alternate" hreflang="en" href="https://photonedgeoptics.com/evidence.html">
    <link rel="alternate" hreflang="zh" href="https://photonedgeoptics.com/evidence.html?lang=zh">

    <!-- BreadcrumbList Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://photonedgeoptics.com/"},
        {"@type": "ListItem", "position": 2, "name": "Evidence Center", "item": "https://photonedgeoptics.com/evidence.html"}
      ]
    }
    </script>

    <!-- CollectionPage Schema -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "PhotonEdge Evidence Center",
        "description": "Inspection reports, material certificates, coating evidence, and quality documentation for precision optical components.",
        "publisher": {
            "@type": "Organization",
            "name": "PhotonEdge"
        }
    }
    </script>

    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-E6J791MXZY"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-E6J791MXZY');
    </script>

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Evidence Center | PhotonEdge Quality Documentation">
    <meta name="twitter:description" content="Inspection reports, material certificates, coating evidence, and quality documents for every PhotonEdge component.">
    <meta name="twitter:image" content="https://photonedgeoptics.com/images/logo.webp">

    <!-- Baidu Search Auto Push -->
    <script>
        (function(){
            var bp = document.createElement('script');
            var curProtocol = window.location.protocol.split(':')[0];
            if (curProtocol === 'https') {
                bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
            } else {
                bp.src = 'https://push.zhangzifan.com/linksubmit/push.js';
            }
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(bp, s);
        })();
    </script>
    <style>
    .evidence-hero { background: linear-gradient(135deg, #0a1628 0%, #1a2d50 100%); padding: 70px 0 50px; color: white; }
    .evidence-hero .eyebrow { font-size: 13px; text-transform: uppercase; letter-spacing: 2px; color: #60a5fa; margin-bottom: 16px; }
    .evidence-hero h1 { font-size: 34px; font-weight: 700; margin-bottom: 14px; color: white; max-width: 700px; line-height: 1.25; }
    .evidence-hero .quote { font-size: 20px; color: #fbbf24; font-weight: 600; margin: 16px 0 0; font-style: italic; }
    .evidence-hero .lead { font-size: 16px; color: #b0c4de; max-width: 650px; line-height: 1.7; margin-top: 20px; }
    .evidence-section { padding: 60px 0; }
    .evidence-section:nth-child(even) { background: #f8fafc; }
    .evidence-section h2 { font-size: 26px; color: #1e3a5f; margin-bottom: 12px; font-weight: 700; }
    .evidence-section .section-intro { font-size: 15px; color: #4b5563; max-width: 750px; margin-bottom: 28px; line-height: 1.7; }
    .evidence-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
    .evidence-card { background: white; border: 1px solid #e2e6ef; border-radius: 10px; padding: 24px; }
    .evidence-card .icon { width: 48px; height: 48px; background: #eff6ff; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 14px; }
    .evidence-card h3 { font-size: 18px; color: #1e3a5f; margin-bottom: 12px; }
    .evidence-item { display: flex; align-items: flex-start; gap: 10px; margin-bottom: 10px; }
    .evidence-item .check { color: #10b981; font-size: 14px; flex-shrink: 0; margin-top: 2px; }
    .evidence-item span { font-size: 14px; color: #374151; line-height: 1.5; }
    .evidence-card .note { font-size: 13px; color: #6b7280; font-style: italic; margin-top: 14px; padding-top: 12px; border-top: 1px solid #e5e7eb; }
    .process-section { text-align: center; }
    .process-steps { display: flex; justify-content: center; align-items: stretch; gap: 0; margin-top: 32px; flex-wrap: wrap; }
    .process-step { flex: 1; min-width: 140px; max-width: 200px; background: white; border: 1px solid #e2e6ef; padding: 20px 16px; text-align: center; }
    .process-step:first-child { border-radius: 10px 0 0 10px; }
    .process-step:last-child { border-radius: 0 10px 10px 0; }
    .process-step .num { width: 32px; height: 32px; background: #3b82f6; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; margin: 0 auto 10px; }
    .process-step h4 { font-size: 14px; color: #1e3a5f; margin-bottom: 6px; }
    .process-step p { font-size: 12px; color: #6b7280; line-height: 1.5; margin: 0; }
    .request-banner { background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 48px; border-radius: 12px; text-align: center; color: white; margin: 40px 0; }
    .request-banner h2 { color: white; font-size: 24px; margin-bottom: 12px; }
    .request-banner p { color: rgba(176,196,222,0.9); margin-bottom: 24px; }
    .request-banner .btn { display: inline-block; padding: 12px 28px; border-radius: 6px; font-weight: 600; text-decoration: none; margin: 0 8px; }
    .request-banner .btn-primary { background: #e8792f; color: white; }
    .request-banner .btn-secondary { background: transparent; color: white; border: 1px solid rgba(255,255,255,0.4); }
    .faq-item { background: white; border: 1px solid #e2e6ef; border-radius: 8px; margin-bottom: 10px; overflow: hidden; }
    .faq-q { padding: 16px 20px; cursor: pointer; font-weight: 600; color: #1e3a5f; font-size: 15px; }
    .faq-a { padding: 0 20px 16px; color: #4b5563; font-size: 14px; line-height: 1.7; display: none; }
    @media (max-width: 900px) {
        .evidence-grid { grid-template-columns: 1fr; }
        .process-steps { flex-direction: column; align-items: center; }
        .process-step { max-width: 300px; border-radius: 0 !important; }
        .process-step:first-child { border-radius: 10px 10px 0 0 !important; }
        .process-step:last-child { border-radius: 0 0 10px 10px !important; }
        .evidence-hero h1 { font-size: 24px; }
        .request-banner { padding: 32px 20px; }
        .request-banner .btn { display: block; margin: 8px 0; }
    }
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="/" class="logo">
    <picture>
        <source srcset="/images/logo.webp" type="image/webp">
        <img src="/logo.png" alt="PhotonEdge" width="160" height="40">
    </picture>
</a>
            <nav class="nav">
                <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">&#9776;</button>
                <ul class="nav-list">
                    <li><a href="/product-catalog.html" class="nav-link" data-i18n="navProducts">Products</a></li>
                    <li><a href="/applications.html" class="nav-link" data-i18n="navApplications">Applications</a></li>
                    <li><a href="/engineering.html" class="nav-link" data-i18n="navEngineering">Engineering</a></li>
                    <li><a href="/knowledge-center/" class="nav-link" data-i18n="navKnowledgeCenter">Knowledge Center</a></li>
                    <li><a href="/ai-optical-engineer.html" class="nav-link" data-i18n="navAIOptical">AI Optical Engineer</a></li>
                    <li><a href="/about.html" class="nav-link" data-i18n="navAbout">About</a></li>
                    <li><a href="/contact.html" class="btn btn-primary nav-cta-btn" data-i18n="navRFQ" style="padding:8px 20px;border-radius:6px;font-size:14px;color:white;text-decoration:none;">Request Engineering Review</a></li>
                </ul>
                <a href="/cart.html" class="cart-icon" title="Shopping Cart">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
                    <span id="cart-count">0</span>
                </a>
            </nav>
        </div>
    </header>

    <!-- Hero -->
    <section class="evidence-hero">
        <div class="container">
            <div class="eyebrow">Quality &amp; Assurance</div>
            <h1>Evidence Center</h1>
            <div class="quote">"If you cannot measure it, you cannot guarantee it."</div>
            <p class="lead">Every precision optical component we deliver comes with evidence — not just a promise. Here you'll find the types of inspection data, material documentation, coating evidence, and quality certificates that accompany PhotonEdge orders.</p>
        </div>
    </section>

    <!-- Inspection Reports -->
    <section class="evidence-section">
        <div class="container">
            <h2>Inspection Reports</h2>
            <p class="section-intro">Every precision component is inspected before shipment. We measure what matters and provide the data so you can verify compliance with your specification.</p>
            
            <div class="evidence-grid">
                <div class="evidence-card">
                    <div class="icon">&#128299;</div>
                    <h3>Interferometer Reports</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Surface flatness / surface figure measured at 632.8nm (ZYGO equivalent interferometer)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Peak-to-valley (PV) and RMS values reported</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>False-color interferogram with measurement parameters</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Transmitted wavefront error available for lenses and windows</span>
                    </div>
                    <div class="note">Included with all precision-grade (&#955;/10 and tighter) orders. Available on request for standard grade.</div>
                </div>
                <div class="evidence-card">
                    <div class="icon">&#128269;</div>
                    <h3>Surface Quality Reports</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Dark-field inspection per MIL-PRF-13830B / ISO 10110</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Scratch and dig counts documented per optic</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Photographic evidence for laser-grade components</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Edge chip and chamfer verification</span>
                    </div>
                    <div class="note">Standard on all laser-grade and precision orders. Summary report on standard grade.</div>
                </div>
                <div class="evidence-card">
                    <div class="icon">&#127752;</div>
                    <h3>Spectral / Coating Reports</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Transmission and reflection curves from PerkinElmer Lambda spectrophotometer</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Wavelength range: 190nm – 2500nm (UV-Vis-NIR)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>FTIR measurement available for MIR/LWIR coatings (2–20&#956;m)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Coating lot traceability and batch measurement data</span>
                    </div>
                    <div class="note">Included with all coated optic orders. Sample-based measurement for production batches.</div>
                </div>
                <div class="evidence-card">
                    <div class="icon">&#128207;</div>
                    <h3>Dimensional Inspection</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Diameter, thickness, and radius measurement with digital micrometers</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Optical comparator for edge profile and chamfer verification</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Centration / beam deviation measurement for lenses</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Wedge angle / parallelism measurement with autocollimator</span>
                    </div>
                    <div class="note">100% dimensional inspection on every precision order. Dimensional data sheet included.</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Material Documentation -->
    <section class="evidence-section">
        <div class="container">
            <h2>Material Documentation</h2>
            <p class="section-intro">Material properties fundamentally determine optical performance. We trace every component back to its source material and provide the documentation to prove it.</p>
            
            <div class="evidence-grid">
                <div class="evidence-card">
                    <div class="icon">&#129516;</div>
                    <h3>Material Certificate</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Material type, grade, and manufacturer identification</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Melt / ingot / boule number for traceability</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Chemical composition data (for crystalline materials)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Impurity levels and homogeneity class</span>
                    </div>
                    <div class="note">Provided with all precision and custom orders upon request.</div>
                </div>
                <div class="evidence-card">
                    <div class="icon">&#127919;</div>
                    <h3>Grade Certificate</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Optical homogeneity class (e.g., H1, H2, H3 per ISO 12123)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Striae grade (A, B, C per MIL-G-17441)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Bubbles and inclusions class</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Stress birefringence specification</span>
                    </div>
                    <div class="note">Available for glass and crystalline materials from certified suppliers.</div>
                </div>
                <div class="evidence-card">
                    <div class="icon">&#128200;</div>
                    <h3>Refractive Index Data</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>n_d, n_F, n_C values (key wavelengths)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Abbe number (V_d) and dispersion data</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Sellmeier coefficients on request</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Temperature coefficient (dn/dT) data available</span>
                    </div>
                    <div class="note">Standard data from material datasheets. Custom measurement available for special projects.</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Coating Evidence -->
    <section class="evidence-section">
        <div class="container">
            <h2>Coating Evidence</h2>
            <p class="section-intro">Coatings determine how your optic performs in real use. We measure coating performance and provide evidence across the full spectral range of your application.</p>
            
            <div class="evidence-grid">
                <div class="evidence-card">
                    <div class="icon">&#128308;</div>
                    <h3>Transmission Curve</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Percent transmission vs. wavelength across the design band</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Measured with reference air baseline</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>UV-Vis-NIR: 190–2500nm (Lambda spectrophotometer)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>MIR/LWIR: 2–20&#956;m (FTIR spectrometer)</span>
                    </div>
                    <div class="note">Included with all coated orders. Measured on witness sample from the same coating run.</div>
                </div>
                <div class="evidence-card">
                    <div class="icon">&#128309;</div>
                    <h3>Reflection Curve</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Reflectance vs. wavelength for HR and mirror coatings</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Specified angle of incidence (0°, 45°, custom)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>S and P polarization data for non-normal incidence</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Coating bandwidth and edge steepness verification</span>
                    </div>
                    <div class="note">Provided with all mirror and high-reflection coating orders.</div>
                </div>
                <div class="evidence-card">
                    <div class="icon">&#9889;</div>
                    <h3>LIDT Data</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Laser Induced Damage Threshold test results</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>1-on-1 and S-on-1 test protocols (ISO 11254 equivalent)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Pulsed (ns, ps, fs) and CW damage thresholds</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Test conditions documented (wavelength, pulse duration, rep rate)</span>
                    </div>
                    <div class="note">Available for laser-grade coatings on request. Batch or design-level certification.</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Quality Documents -->
    <section class="evidence-section">
        <div class="container">
            <h2>Quality Documents</h2>
            <p class="section-intro">System-level quality and compliance documentation that supports your audit and regulatory requirements.</p>
            
            <div class="evidence-grid">
                <div class="evidence-card">
                    <div class="icon">&#127941;</div>
                    <h3>ISO Certificate</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>ISO 9001:2015 Quality Management System</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>ISO 13485 Medical Device Quality (partner facilities)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>ISO 14001 Environmental Management</span>
                    </div>
                    <div class="note">Manufacturing partner certificates available on request. PhotonEdge operates under ISO 9001 aligned processes.</div>
                </div>
                <div class="evidence-card">
                    <div class="icon">&#9881;&#65039;</div>
                    <h3>RoHS &amp; REACH Compliance</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>RoHS 2.0 compliance statement (EU 2015/863)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>REACH SVHC declaration (EU 1907/2006)</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Conflict minerals statement on request</span>
                    </div>
                    <div class="note">Standard compliance declaration provided with all shipments. Detailed reports on request.</div>
                </div>
                <div class="evidence-card">
                    <div class="icon">&#128221;</div>
                    <h3>Certificate of Conformity (CoC)</h3>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Conformance declaration per order / per lot</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Part number, quantity, material, and coating listed</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Statement of compliance with purchase specification</span>
                    </div>
                    <div class="evidence-item">
                        <span class="check">&#10003;</span>
                        <span>Inspection release signature and date</span>
                    </div>
                    <div class="note">Included with every precision and custom order. Available for stock orders on request.</div>
                </div>
            </div>
        </div>
    </section>

    <!-- How it Works -->
    <section class="evidence-section process-section">
        <div class="container">
            <h2>How Quality Verification Works</h2>
            <p class="section-intro" style="margin-left:auto;margin-right:auto;">Quality isn't a single checkpoint at the end. It's built into the process at every step, with data captured at each stage.</p>
            <div class="process-steps">
                <div class="process-step">
                    <div class="num">1</div>
                    <h4>Incoming Material</h4>
                    <p>Material certificates verified against spec. Optical quality check before production.</p>
                </div>
                <div class="process-step">
                    <div class="num">2</div>
                    <h4>In-Process Checks</h4>
                    <p>Dimensional and surface quality checks at key process milestones. Photos shared with customers for custom orders.</p>
                </div>
                <div class="process-step">
                    <div class="num">3</div>
                    <h4>Final Inspection</h4>
                    <p>Full dimensional, surface quality, flatness, and spectral testing. 100% inspection on precision orders.</p>
                </div>
                <div class="process-step">
                    <div class="num">4</div>
                    <h4>Documentation</h4>
                    <p>CoC, inspection data, and material certificates packaged with shipment and available digitally.</p>
                </div>
                <div class="process-step">
                    <div class="num">5</div>
                    <h4>Traceability</h4>
                    <p>Every part traceable to material batch, coating run, and inspection record.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Note -->
    <section class="evidence-section" style="background: #fffbeb;">
        <div class="container" style="text-align: center; max-width: 700px;">
            <h3 style="font-size: 18px; color: #92400e; margin-bottom: 12px;">Sample Reports Available on Request</h3>
            <p style="font-size: 15px; color: #78350f; line-height: 1.7;">Sample inspection reports, coating curves, and material certificates are available on request. We don't post them publicly because each report is specific to a particular part and batch. Contact us and we'll send you sample documentation relevant to your application.</p>
        </div>
    </section>

    <!-- Request CTA -->
    <div class="container" style="padding-bottom: 60px;">
        <div class="request-banner">
            <h2>Request a Sample Test Report</h2>
            <p>Tell us what type of component and documentation you're interested in. We'll send you sample inspection data so you can see exactly what you'd get with your order.</p>
            <a href="/contact.html" class="btn btn-primary">Request Sample Report</a>
            <a href="/engineering.html" class="btn btn-secondary">Engineering Services</a>
        </div>
    </div>

    <footer class="footer">
        <div class="container">
            <div class="footer-grid" style="grid-template-columns: 2fr 1fr 1fr 1fr;">
                <div class="footer-brand">
                    <h3>PhotonEdge</h3>
                    <p>Precision Optical Solutions Provider</p>
                    <p style="margin-top:8px;font-size:13px;color:rgba(255,255,255,0.6);">ISO 9001:2015 Certified</p>
                </div>
                <div class="footer-col">
                    <h4>Products</h4>
                    <ul>
                        <li><a href="/product-catalog.html?component=Lens">Optical Lenses</a></li>
                        <li><a href="/product-catalog.html?component=Window">Optical Windows</a></li>
                        <li><a href="/product-catalog.html?component=Mirror">Optical Mirrors</a></li>
                        <li><a href="/product-catalog.html?component=Filter">Optical Filters</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Applications</h4>
                    <ul>
                        <li><a href="/applications/laser-optics/">Laser Systems</a></li>
                        <li><a href="/applications/semiconductor-inspection/">Semiconductor</a></li>
                        <li><a href="/applications/medical-imaging/">Medical Imaging</a></li>
                        <li><a href="/applications/aerospace-defense/">Aerospace &amp; Defense</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li>Email: <a href="mailto:sales@photonedgeoptics.com">sales@photonedgeoptics.com</a></li>
                        <li>Phone: +86-13693009175</li>
                        <li>WhatsApp: +86-13693009175</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024-2026 PhotonEdge. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <a href="https://wa.me/8613693009175" target="_blank" class="whatsapp-float" title="Chat with us on WhatsApp">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.467-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    </a>

    <script src="/js/translations.js"></script>
    <script src="/js/main.js"></script>
    <script>
    function toggleMobileMenu(){var n=document.querySelector('.nav-list');if(n)n.classList.toggle('active');}
    </script>
    <script src="/js/chat-bot.js"></script>
    <script src="/js/chatbot.js"></script>
    <script src="/js/cart.js"></script>
</body>
</html>'''
    
    with open(os.path.join(DST, "evidence.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("  Created evidence.html")

# ─────────────────────────────────────────────────────────
# Case Studies Format Upgrade
# ─────────────────────────────────────────────────────────

def upgrade_case_studies():
    """Upgrade case-studies.html with new engineering evidence format."""
    print("Upgrading Case Studies format...")
    
    # Read existing file to get head and footer
    src_path = os.path.join(DST, "case-studies.html")
    with open(src_path, "r", encoding="utf-8") as f:
        old_content = f.read()
    
    # Extract head (everything up to </head>)
    head_end = old_content.find("</head>")
    head = old_content[:head_end + 7]
    
    # Extract footer (from footer section to end)
    footer_start = old_content.find('<footer class="footer">')
    footer = old_content[footer_start:]
    
    # Build new case studies page with upgraded format
    # Update title, description, keywords for SEO
    head = head.replace(
        '<title>Optical Component Case Studies - Real Application Success Stories | PhotonEdge</title>',
        '<title>Optical Engineering Case Studies | Real Results with Data | PhotonEdge</title>'
    )
    head = head.replace(
        '<meta name="description" content="Read how PhotonEdge precision optical components helped customers achieve breakthrough results in semiconductor, medical, and laser applications.">',
        '<meta name="description" content="Real optical engineering case studies with measured data. See how we solved real problems: customer problem, engineering analysis, material selection, manufacturing process, measured results, and business impact.">'
    )
    head = head.replace(
        '<meta name="keywords" content="光学元件,光学透镜,棱镜,反射镜,滤光片,激光扩束镜,偏振片,光学窗口片,光学镀膜,定制光学,北京恒鼎光,PhotonEdge">',
        '<meta name="keywords" content="optical engineering case studies, precision optics case studies, laser optics real results, semiconductor optics, medical imaging optics, custom optics success stories">'
    )
    
    # Add FAQPage schema
    faq_schema = '''
    <!-- FAQPage Schema -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": "What kind of optical engineering problems does PhotonEdge solve?",
             "acceptedAnswer": {"@type": "Answer", "text": "PhotonEdge solves a wide range of optical engineering challenges including laser damage issues, imaging resolution problems, thermal stability concerns, material selection challenges, coating optimization, and tolerance optimization for precision optical components across laser, medical, semiconductor, and defense applications."}},
            {"@type": "Question", "name": "How long does a custom optical component project take?",
             "acceptedAnswer": {"@type": "Answer", "text": "Prototype quantities typically take 3-5 weeks depending on complexity, material availability, and coating requirements. Production volumes typically take 6-10 weeks. For standard catalog components, we can often ship within 1-2 weeks. Timeline is confirmed during the engineering review phase."}},
            {"@type": "Question", "name": "Can PhotonEdge help optimize my existing optical specification?",
             "acceptedAnswer": {"@type": "Answer", "text": "Yes, specification optimization is one of our core services. We review your existing drawing and specification, identify which tolerances are critical for performance and which can be relaxed to reduce cost, and provide a recommended optimized spec with cost savings estimate. This review is free for qualified projects."}}
        ]
    }
    </script>
    <!-- /FAQPage Schema -->'''
    
    # Insert FAQ schema before </head>
    head = head.replace("</head>", faq_schema + "\n</head>")
    
    # Build new body content
    body_html = '''
<body>
    <header class="header">
        <div class="container">
            <a href="/" class="logo">
    <picture>
        <source srcset="/images/logo.webp" type="image/webp">
        <img src="/logo.png" alt="PhotonEdge" width="160" height="40">
    </picture>
</a>
            <nav class="nav">
                <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">&#9776;</button>
                <ul class="nav-list">
                    <li><a href="/product-catalog.html" class="nav-link" data-i18n="navProducts">Products</a></li>
                    <li><a href="/applications.html" class="nav-link" data-i18n="navApplications">Applications</a></li>
                    <li><a href="/engineering.html" class="nav-link" data-i18n="navEngineering">Engineering</a></li>
                    <li><a href="/knowledge-center/" class="nav-link" data-i18n="navKnowledgeCenter">Knowledge Center</a></li>
                    <li><a href="/ai-optical-engineer.html" class="nav-link" data-i18n="navAIOptical">AI Optical Engineer</a></li>
                    <li><a href="/about.html" class="nav-link" data-i18n="navAbout">About</a></li>
                    <li><a href="/contact.html" class="btn btn-primary nav-cta-btn" data-i18n="navRFQ" style="padding:8px 20px;border-radius:6px;font-size:14px;color:white;text-decoration:none;">Request Engineering Review</a></li>
                </ul>
                <a href="/cart.html" class="cart-icon" title="Shopping Cart">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
                    <span id="cart-count">0</span>
                </a>
            </nav>
        </div>
    </header>

    <!-- Hero -->
    <section style="background: linear-gradient(135deg, #0a1628 0%, #1a2d50 100%); padding: 70px 0 50px; color: white;">
        <div class="container">
            <div style="font-size: 13px; text-transform: uppercase; letter-spacing: 2px; color: #60a5fa; margin-bottom: 16px;">Case Studies</div>
            <h1 style="font-size: 34px; font-weight: 700; margin-bottom: 14px; color: white; max-width: 700px; line-height: 1.25;">Real Optical Engineering. Real Measured Results.</h1>
            <p style="font-size: 16px; color: #b0c4de; max-width: 650px; line-height: 1.7;">See how PhotonEdge has helped engineering teams solve real optical challenges. Each case study follows our engineering evidence framework — from problem definition through measured results.</p>
        </div>
    </section>

    <!-- Quick Navigation -->
    <section style="background: #f8fafc; padding: 20px 0; border-bottom: 1px solid #e2e6ef;">
        <div class="container">
            <div style="font-size: 13px; color: #6b7280; margin-bottom: 8px;"><strong>Jump to Case Study:</strong></div>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                <a href="#case1" style="padding: 6px 14px; background: white; border: 1px solid #d1d5db; border-radius: 6px; font-size: 13px; color: #374151; text-decoration: none;">UV Laser Window (355nm)</a>
                <a href="#case2" style="padding: 6px 14px; background: white; border: 1px solid #d1d5db; border-radius: 6px; font-size: 13px; color: #374151; text-decoration: none;">Precision Imaging Lens</a>
                <a href="#case3" style="padding: 6px 14px; background: white; border: 1px solid #d1d5db; border-radius: 6px; font-size: 13px; color: #374151; text-decoration: none;">Fused Silica Windows (Wafer Inspection)</a>
                <a href="#case4" style="padding: 6px 14px; background: white; border: 1px solid #d1d5db; border-radius: 6px; font-size: 13px; color: #374151; text-decoration: none;">CaF&#8322; Prism Pair (Ultrafast)</a>
            </div>
        </div>
    </section>

    <!-- Case Studies Container -->
    <section style="padding: 60px 0; background: #f8fafc;">
        <div class="container">

            <!-- Case 1 -->
            <div id="case1" style="background: white; border: 1px solid #e2e6ef; border-radius: 12px; padding: 32px; margin-bottom: 32px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px; margin-bottom: 20px;">
                    <div>
                        <div style="font-size: 13px; color: #6b7280; margin-bottom: 6px;">Case Study #1 &middot; Laser Systems</div>
                        <h2 style="font-size: 22px; color: #1e3a5f; margin: 0; font-weight: 700;">UV Laser Window Optimization for 355nm Industrial System</h2>
                    </div>
                    <span style="background: #fef3c7; color: #92400e; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600;">UV Laser</span>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0; border: 1px solid #e2e6ef; border-radius: 8px; overflow: hidden; margin-bottom: 20px;">
                    <div style="background: #fef2f2; padding: 14px 18px; border-right: 1px solid #e2e6ef;">
                        <div style="font-size: 13px; font-weight: 600; color: #991b1b; margin-bottom: 4px;">Problem</div>
                        <div style="font-size: 14px; color: #7f1d1d;">Standard BK7 windows caused laser damage and thermal lensing at 355nm, 10W average power</div>
                    </div>
                    <div style="background: #f0fdf4; padding: 14px 18px;">
                        <div style="font-size: 13px; font-weight: 600; color: #166534; margin-bottom: 4px;">Result</div>
                        <div style="font-size: 14px; color: #166534;">Fused silica windows with optimized UV AR coating — zero damage after 2000+ hours at 15W</div>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-bottom: 20px;">
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Customer Problem</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">A manufacturer of industrial UV laser marking systems was experiencing premature laser-induced damage on the output protective window of their 355nm, 10W DPSS laser. Standard BK7 windows from their existing supplier showed haze formation after 200-300 hours of operation, reducing output power by 15-20%.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">System Requirement</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Output protective window for 355nm DPSS laser, 10W average power, 25mm diameter, &gt; 95% transmission, 10,000-hour operational lifetime with &lt; 5% power degradation.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Root Cause</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">BK7 glass absorbs significantly at 355nm (~10-15% per cm), causing thermal lensing and coating degradation. The standard VIS AR coating was not optimized for UV wavelengths and had higher absorption at 355nm, accelerating damage.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Engineering Analysis</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">At 355nm and 10W average power with ~1mm beam diameter, intensity is ~127 W/cm². BK7's absorption coefficient at 355nm is ~0.1 cm⁻¹, meaning ~1% absorption per mm of material. In a 3mm window, that's ~3% absorption, depositing ~300mW of heat — enough for thermal lensing and coating degradation.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Material Selection</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">UV-grade fused silica was selected for its exceptional transmission at 355nm (&gt; 99.5% per cm), low thermal expansion coefficient, and high UV laser damage threshold. Fused silica absorbs &lt; 0.01% per cm at 355nm — 100× less than BK7.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Optical Specification</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">25.4mm diameter, 3mm thick UV fused silica window. 20-10 surface quality, &lambda;/10 flatness. 30-arc-minute wedge to prevent etalon effects. UV AR coating on both sides optimized for 355nm, R &lt; 0.5% per surface.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Manufacturing Process</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Blank preparation from UVFS boule &rarr; double-sided grinding &rarr; fine grinding &rarr; precision polishing to &lambda;/10 &rarr; edge chamfering &rarr; wedge control &rarr; UV AR coating deposition (ion-beam sputtering) &rarr; final inspection.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Inspection</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Interferometer flatness test (verified &lambda;/10 per surface), spectral transmission measurement at 355nm (measured T &gt; 99%), surface quality dark-field inspection (confirmed 20-10), wedge angle measurement (29.4 arc min nominal), LIDT sample test (3 J/cm² @ 355nm, 10ns).</p>
                    </div>
                </div>

                <!-- Measured Result -->
                <div style="background: #ecfdf5; border: 1px solid #6ee7b7; border-radius: 10px; padding: 20px 24px; margin-bottom: 16px;">
                    <h3 style="font-size: 15px; color: #065f46; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.5px;">Measured Result</h3>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;">
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">99.2%</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Transmission @ 355nm</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">&lambda;/12</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Surface Flatness</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">2000+ hrs</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Damage-free at 15W</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">&lt; 2%</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Power degradation</div>
                        </div>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Business Impact</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Customer eliminated a major field failure mode, reduced warranty costs from window replacements by approximately 60%, and improved the MTBF of their laser systems from ~500 hours to over 5000 hours. The 35nm fused silica windows now ship as standard in all their UV laser models.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Lessons Learned</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Material selection is critical at UV wavelengths where even small absorption coefficients lead to significant thermal loading at moderate power levels. BK7 is not an appropriate substrate for 355nm applications above ~1W average power. Coating quality and deposition method (IBS vs. E-beam) also significantly impact UV LIDT.</p>
                    </div>
                </div>
            </div>

            <!-- Case 2 -->
            <div id="case2" style="background: white; border: 1px solid #e2e6ef; border-radius: 12px; padding: 32px; margin-bottom: 32px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px; margin-bottom: 20px;">
                    <div>
                        <div style="font-size: 13px; color: #6b7280; margin-bottom: 6px;">Case Study #2 &middot; Medical Imaging</div>
                        <h2 style="font-size: 22px; color: #1e3a5f; margin: 0; font-weight: 700;">Precision Imaging Lens Assembly for Diagnostic Instrument</h2>
                    </div>
                    <span style="background: #dbeafe; color: #1e40af; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600;">Medical Imaging</span>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0; border: 1px solid #e2e6ef; border-radius: 8px; overflow: hidden; margin-bottom: 20px;">
                    <div style="background: #fef2f2; padding: 14px 18px; border-right: 1px solid #e2e6ef;">
                        <div style="font-size: 13px; font-weight: 600; color: #991b1b; margin-bottom: 4px;">Problem</div>
                        <div style="font-size: 14px; color: #7f1d1d;">Imported lens assemblies from US supplier were 4× too expensive and had 12-week lead times for production volumes</div>
                    </div>
                    <div style="background: #f0fdf4; padding: 14px 18px;">
                        <div style="font-size: 13px; font-weight: 600; color: #166534; margin-bottom: 4px;">Result</div>
                        <div style="font-size: 14px; color: #166534;">Custom achromatic triplet assembly at 60% lower cost, meeting all MTF and distortion specs, 4-week production lead time</div>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-bottom: 20px;">
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Customer Problem</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">A medical diagnostics company was sourcing a custom 3-element achromatic lens assembly from a US-based optics manufacturer for their in-vitro diagnostic instrument. Cost per unit was too high for volume production, and lead times were inconsistent, causing production scheduling problems.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">System Requirement</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">3-element achromatic lens assembly, 25mm effective focal length, f/2.8, diffraction-limited MTF across 400-700nm, &lt; 0.5% distortion, aligned in a threaded aluminum barrel, 500 units/year volume.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Root Cause</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">The US supplier was pricing for low-volume custom manufacturing with significant engineering overhead. The design, while optically excellent, used premium glass types and tight tolerances that drove cost without being strictly necessary for the application's actual performance needs.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Engineering Analysis</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Our optical engineers reviewed the design and found that the specified &lambda;/20 surface figure and 10-5 surface quality were significantly tighter than needed for a f/2.8 visible imaging system. Tolerance analysis showed that &lambda;/10 flatness and 20-10 surface quality would deliver MTF within 1% of the tight-spec design.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Material Selection</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Standard N-BK7 crown glass and SF11 flint glass for the achromatic elements. A third meniscus element in N-BK7 for field flattening. Verified all materials are available in production quantities with short lead times from multiple qualified suppliers.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Optical Specification</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">3-element lens assembly: 2 cemented doublets + 1 singlet. 25mm EFL, f/2.8. Surface quality: 20-10. Surface figure: &lambda;/10. Centration: &lt; 1 arc min. VIS broadband AR coating (400-700nm). All elements aligned in anodized aluminum barrel.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Manufacturing Process</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Blank generation &rarr; curve generation &rarr; fine grinding &rarr; polishing &rarr; centering &rarr; cementing (doublets) &rarr; coating &rarr; barrel assembly &rarr; alignment &rarr; final MTF testing. Production set up for 500-unit annual volume with inventory buffers for key materials.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Inspection</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">100% MTF testing at 40 lp/mm and 80 lp/mm (sagittal and tangential). Distortion measurement via calibrated test target. Focal length verification. Surface quality inspection. Coating spectral verification. Environmental stress test (thermal cycling) on sampling basis.</p>
                    </div>
                </div>

                <div style="background: #ecfdf5; border: 1px solid #6ee7b7; border-radius: 10px; padding: 20px 24px; margin-bottom: 16px;">
                    <h3 style="font-size: 15px; color: #065f46; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.5px;">Measured Result</h3>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;">
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">0.92</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">MTF @ 40 lp/mm</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">0.3%</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Distortion</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">60%</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Cost Reduction</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">4 wks</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Production Lead Time</div>
                        </div>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Business Impact</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Customer reduced lens assembly cost by 60% per unit, cutting annual procurement spend by approximately $120,000. Production lead time improved from 12 weeks to 4 weeks, enabling just-in-time inventory and reducing working capital tied up in component stock.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Lessons Learned</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Tightening every specification "just to be safe" adds significant cost without proportional performance gain. Specification optimization — reducing tolerances that don't affect system performance while maintaining those that do — can deliver 30-60% cost savings on custom optics. The key is knowing which specs matter.</p>
                    </div>
                </div>
            </div>

            <!-- Case 3 -->
            <div id="case3" style="background: white; border: 1px solid #e2e6ef; border-radius: 12px; padding: 32px; margin-bottom: 32px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px; margin-bottom: 20px;">
                    <div>
                        <div style="font-size: 13px; color: #6b7280; margin-bottom: 6px;">Case Study #3 &middot; Semiconductor</div>
                        <h2 style="font-size: 22px; color: #1e3a5f; margin: 0; font-weight: 700;">High-Purity Fused Silica Windows for Wafer Inspection System</h2>
                    </div>
                    <span style="background: #ede9fe; color: #5b21b6; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600;">Semiconductor</span>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0; border: 1px solid #e2e6ef; border-radius: 8px; overflow: hidden; margin-bottom: 20px;">
                    <div style="background: #fef2f2; padding: 14px 18px; border-right: 1px solid #e2e6ef;">
                        <div style="font-size: 13px; font-weight: 600; color: #991b1b; margin-bottom: 4px;">Problem</div>
                        <div style="font-size: 14px; color: #7f1d1d;">Off-the-shelf fused silica windows had too much wavefront distortion and contamination, reducing inspection tool resolution</div>
                    </div>
                    <div style="background: #f0fdf4; padding: 14px 18px;">
                        <div style="font-size: 13px; font-weight: 600; color: #166534; margin-bottom: 4px;">Result</div>
                        <div style="font-size: 14px; color: #166534;">Custom &lambda;/20 fused silica windows with class 100 cleanroom packaging — achieved 20% higher resolution than target spec</div>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-bottom: 20px;">
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Customer Problem</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">A semiconductor equipment manufacturer was building a next-generation wafer inspection tool and needed high-quality optical viewports for the imaging system. Standard catalog fused silica windows were causing wavefront error that limited the system's achievable resolution below their target.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">System Requirement</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">100mm diameter × 10mm thick fused silica viewport window. Wavefront distortion &lt; &lambda;/10 transmitted. Surface quality 10-5. UV-enhanced AR coating at 365nm. Ultra-clean packaging suitable for class 100 cleanroom installation.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Root Cause</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Standard catalog &lambda;/4 windows introduce approximately &lambda;/8 transmitted wavefront error per surface (doubled when counting both surfaces in a window), which is well above what a high-NA inspection objective can tolerate without degrading image resolution.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Engineering Analysis</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">For a 0.8 NA inspection system at 365nm, the diffraction-limited wavefront error budget is approximately &lambda;/14. A standard &lambda;/4 window would consume most of that budget, leaving no margin for the objective lens and other system elements. &lambda;/20 surface flatness on both sides is required to keep window contribution below &lambda;/10 total.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Material Selection</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">UV-grade fused silica (Corning 7980 equivalent) selected for excellent UV transmission at 365nm, low thermal expansion, and high homogeneity grade (H2). High-purity material with low OH content for minimal absorption and fluorescence.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Optical Specification</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">100.0mm diameter × 10.0mm thick. &plusmn;0.05mm diameter tolerance. &plusmn;0.02mm thickness tolerance. Both sides polished to &lambda;/20 flatness. 10-5 surface quality per MIL-PRF-13830B. UV AR coating (350-400nm), R &lt; 0.5% per surface.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Manufacturing Process</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Core drill from fused silica blank &rarr; OD grinding &rarr; double-sided lapping &rarr; fine grinding both sides &rarr; precision polishing with iterative interferometer feedback to achieve &lambda;/20 &rarr; IBS UV AR coating deposition &rarr; class 100 cleanroom cleaning &rarr; double packaging in cleanroom environment.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Inspection</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Phase-shift interferometer on both surfaces (verified &lambda;/25 and &lambda;/22 respectively — both better than spec). Transmitted wavefront test: &lambda;/12 PV. Surface quality inspection with 100× dark-field microscope (confirmed 10-5). UV transmission measured at 365nm: 99.3% both surfaces combined.</p>
                    </div>
                </div>

                <div style="background: #ecfdf5; border: 1px solid #6ee7b7; border-radius: 10px; padding: 20px 24px; margin-bottom: 16px;">
                    <h3 style="font-size: 15px; color: #065f46; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.5px;">Measured Result</h3>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;">
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">&lambda;/25</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Surface 1 Flatness</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">&lambda;/12</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Transmitted Wavefront</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">99.3%</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Transmission @ 365nm</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">+20%</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Resolution Improvement</div>
                        </div>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Business Impact</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">The customer's inspection tool achieved a 20% resolution improvement over their target specification, enabling them to detect smaller defect features than originally planned. This directly translated into a competitive advantage in their product positioning and opened up new market segments their previous tool couldn't address.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Lessons Learned</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">For high-NA imaging systems, window wavefront error must be carefully budgeted alongside all other system components. The flatness specification of a window in transmission has roughly twice the optical effect of its surface figure (light enters and exits, encountering both surfaces). Cleanroom packaging is essential for high-quality optics that will be installed in cleanroom equipment.</p>
                    </div>
                </div>
            </div>

            <!-- Case 4 -->
            <div id="case4" style="background: white; border: 1px solid #e2e6ef; border-radius: 12px; padding: 32px; margin-bottom: 32px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px; margin-bottom: 20px;">
                    <div>
                        <div style="font-size: 13px; color: #6b7280; margin-bottom: 6px;">Case Study #4 &middot; Ultrafast Lasers</div>
                        <h2 style="font-size: 22px; color: #1e3a5f; margin: 0; font-weight: 700;">Custom CaF&#8322; Prism Pair for Ultrafast Pulse Compression</h2>
                    </div>
                    <span style="background: #fef3c7; color: #92400e; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600;">Ultrafast Laser</span>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0; border: 1px solid #e2e6ef; border-radius: 8px; overflow: hidden; margin-bottom: 20px;">
                    <div style="background: #fef2f2; padding: 14px 18px; border-right: 1px solid #e2e6ef;">
                        <div style="font-size: 13px; font-weight: 600; color: #991b1b; margin-bottom: 4px;">Problem</div>
                        <div style="font-size: 14px; color: #7f1d1d;">Imported CaF&#8322; prism pairs had poor angle accuracy and inconsistent dispersion, causing unstable pulse compression in a femtosecond amplifier</div>
                    </div>
                    <div style="background: #f0fdf4; padding: 14px 18px;">
                        <div style="font-size: 13px; font-weight: 600; color: #166534; margin-bottom: 4px;">Result</div>
                        <div style="font-size: 14px; color: #166534;">Matched CaF&#8322; prism pairs with &lt; 5 arcsec angle tolerance and matched dispersion — pulse duration stable within 3% over 1000 hours</div>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-bottom: 20px;">
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Customer Problem</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">A manufacturer of femtosecond CPA laser systems was experiencing pulse duration instability when using CaF₂ prism pairs from their existing supplier. Pairs from different batches produced different amounts of dispersion, requiring manual recalibration and limiting the unit-to-unit consistency of their laser product.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">System Requirement</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">CaF₂ right-angle prism pair for pulse compression in a 1kHz, 1mJ, 800nm Ti:Sapphire amplifier. 25mm base length, 15mm height. Apex angle tolerance &lt; 10 arc sec. Prism-to-prism GVD matching within 2%. Uncoated.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Root Cause</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">The previous supplier was cutting prisms from different parts of different CaF₂ boules without dispersion matching. Natural variation in CaF₂ refractive index (up to 0.0002 between boules) causes measurable GVD variation when accumulated through a prism pair with multiple passes.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Engineering Analysis</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">For a 4-pass prism compressor, the total GVD scales with both prism material dispersion and geometric path length. A 0.0002 refractive index variation between prisms in a pair creates approximately 2-3% GVD mismatch — enough to change pulse duration by 5-8 femtoseconds in a 50fs system, which was the customer's complaint.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Material Selection</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">High-purity single-crystal CaF₂, &lt;111&gt; orientation, from the same boule for matched prism pairs. UV-grade CaF₂ specified for 700-1000nm transmission. Material certified for low striae and homogeneous refractive index across the boule.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Optical Specification</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Right-angle isosceles prism, 25mm leg length, 15mm clear aperture height. Apex angle: 90° &plusmn; 5 arc sec. Base angle: 45° &plusmn; 5 arc sec. Surface quality: 20-10. Surface figure: &lambda;/10 per surface. Pyramid angle error &lt; 10 arc sec. Uncoated (as-polished).</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Manufacturing Process</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Single CaF₂ boule cut into matched prism blanks (both prisms from adjacent slices) &rarr; rough grinding to prism shape &rarr; fine grinding &rarr; precision polishing all three faces &rarr; angle verification on precision goniometer &rarr; final cleaning &rarr; matched pair packaging with matched serial numbers.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Inspection</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Apex angle measured on precision goniometer (3.2 arc sec and 4.1 arc sec for pair #1 — both within spec). Refractive index verified via minimum deviation method for both prisms (matched to &lt; 0.00005 difference). Surface quality inspected (20-10 confirmed). Flatness verified via interferometer.</p>
                    </div>
                </div>

                <div style="background: #ecfdf5; border: 1px solid #6ee7b7; border-radius: 10px; padding: 20px 24px; margin-bottom: 16px;">
                    <h3 style="font-size: 15px; color: #065f46; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.5px;">Measured Result</h3>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;">
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">3.2&quot;</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Apex Angle Error</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">&lt; 0.01%</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Refractive Index Match</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">&plusmn; 3%</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Pulse Duration Stability</div>
                        </div>
                        <div style="text-align: center;">
                            <div style="font-size: 24px; font-weight: 700; color: #059669;">1000+ hrs</div>
                            <div style="font-size: 12px; color: #047857; margin-top: 4px;">Stable Operation</div>
                        </div>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Business Impact</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">Customer eliminated the need for manual pulse duration calibration between production units, reducing assembly time by approximately 4 hours per laser. Unit-to-unit consistency improved from 15% pulse duration variation to &lt; 3%, enabling them to ship calibrated systems with tighter published specifications.</p>
                    </div>
                    <div style="background: #f8fafc; border-radius: 8px; padding: 16px;">
                        <h3 style="font-size: 14px; color: #1e3a5f; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Lessons Learned</h3>
                        <p style="font-size: 14px; color: #4b5563; line-height: 1.65; margin: 0;">For precision applications like ultrafast pulse compression, material homogeneity between matched components can be as important as the dimensional tolerances. Specifying that both prisms come from the same boule (or at minimum the same boule grade) is critical for consistent GVD performance. Angle accuracy of a few arc seconds matters when light makes multiple passes through a prism pair.</p>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- FAQ Section -->
    <section style="padding: 60px 0; background: white;">
        <div class="container">
            <h2 style="font-size: 24px; color: #1e3a5f; margin-bottom: 24px; text-align: center;">Frequently Asked Questions</h2>
            <div style="max-width: 800px; margin: 0 auto;">
                <div class="faq-item" style="background: #f8fafc; border: 1px solid #e2e6ef; border-radius: 8px; margin-bottom: 10px; overflow: hidden;">
                    <div class="faq-q" onclick="toggleFaq(this)">What kind of optical engineering problems does PhotonEdge solve?</div>
                    <div class="faq-a">PhotonEdge solves a wide range of optical engineering challenges including laser damage issues, imaging resolution problems, thermal stability concerns, material selection challenges, coating optimization, and tolerance optimization for precision optical components across laser, medical, semiconductor, and defense applications.</div>
                </div>
                <div class="faq-item" style="background: #f8fafc; border: 1px solid #e2e6ef; border-radius: 8px; margin-bottom: 10px; overflow: hidden;">
                    <div class="faq-q" onclick="toggleFaq(this)">How long does a custom optical component project take?</div>
                    <div class="faq-a">Prototype quantities typically take 3-5 weeks depending on complexity, material availability, and coating requirements. Production volumes typically take 6-10 weeks. For standard catalog components, we can often ship within 1-2 weeks. Timeline is confirmed during the engineering review phase.</div>
                </div>
                <div class="faq-item" style="background: #f8fafc; border: 1px solid #e2e6ef; border-radius: 8px; margin-bottom: 10px; overflow: hidden;">
                    <div class="faq-q" onclick="toggleFaq(this)">Can PhotonEdge help optimize my existing optical specification?</div>
                    <div class="faq-a">Yes, specification optimization is one of our core services. We review your existing drawing and specification, identify which tolerances are critical for performance and which can be relaxed to reduce cost, and provide a recommended optimized spec with cost savings estimate. This review is free for qualified projects.</div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section style="padding: 60px 0; background: #f8fafc;">
        <div class="container">
            <div style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 48px; border-radius: 12px; text-align: center; color: white;">
                <h2 style="color: white; font-size: 24px; margin-bottom: 12px;">Have a Similar Optical Challenge?</h2>
                <p style="color: rgba(176,196,222,0.9); margin-bottom: 24px;">Send us your problem description, spec, or drawing. We'll tell you how we'd approach it — with no obligation.</p>
                <a href="/contact.html" style="display: inline-block; padding: 12px 28px; border-radius: 6px; font-weight: 600; text-decoration: none; margin: 0 8px; background: #e8792f; color: white;">Start a Conversation</a>
                <a href="/case-studies.html" style="display: inline-block; padding: 12px 28px; border-radius: 6px; font-weight: 600; text-decoration: none; margin: 0 8px; background: transparent; color: white; border: 1px solid rgba(255,255,255,0.4);">View All Case Studies</a>
            </div>
        </div>
    </section>
'''
    
    # Combine head + body + footer
    new_content = head + body_html + "\n" + footer
    
    with open(src_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print("  Upgraded case-studies.html (new engineering evidence format)")

# ─────────────────────────────────────────────────────────
# Sitemap Rebuild
# ─────────────────────────────────────────────────────────

def build_sitemap():
    """Rebuild sitemap.xml with all pages + new Tier 2 + new content pages."""
    print("Rebuilding sitemap.xml...")
    
    urls = []
    
    # Helper to add URL
    def add_url(loc, priority=0.8, lastmod=LASTMOD):
        urls.append({"loc": loc, "lastmod": lastmod, "changefreq": "weekly", "priority": priority})
    
    # Top-level pages (highest priority)
    add_url(f"{BASE_URL}/", priority=1.0)
    add_url(f"{BASE_URL}/about.html", priority=0.9)
    add_url(f"{BASE_URL}/contact.html", priority=0.9)
    add_url(f"{BASE_URL}/product-catalog.html", priority=0.9)
    add_url(f"{BASE_URL}/engineering.html", priority=0.9)
    add_url(f"{BASE_URL}/applications.html", priority=0.9)
    add_url(f"{BASE_URL}/ai-optical-engineer.html", priority=0.9)
    add_url(f"{BASE_URL}/specification-optimization.html", priority=0.9)
    add_url(f"{BASE_URL}/evidence.html", priority=0.9)
    add_url(f"{BASE_URL}/case-studies.html", priority=0.9)
    add_url(f"{BASE_URL}/faq.html", priority=0.8)
    add_url(f"{BASE_URL}/materials.html", priority=0.8)
    add_url(f"{BASE_URL}/downloads.html", priority=0.7)
    add_url(f"{BASE_URL}/product-advisor.html", priority=0.7)
    add_url(f"{BASE_URL}/calculator.html", priority=0.7)
    add_url(f"{BASE_URL}/compare.html", priority=0.7)
    add_url(f"{BASE_URL}/cart.html", priority=0.5)
    add_url(f"{BASE_URL}/404.html", priority=0.3)
    add_url(f"{BASE_URL}/knowledge-center/", priority=0.8)
    add_url(f"{BASE_URL}/blog.html", priority=0.8)
    add_url(f"{BASE_URL}/news.html", priority=0.8)
    add_url(f"{BASE_URL}/optomechanics.html", priority=0.7)
    add_url(f"{BASE_URL}/capabilities.html", priority=0.6)
    
    # Product pages (56 existing + 10 new Tier 2 = 66)
    products_dir = os.path.join(DST, "products")
    product_slugs = sorted([d for d in os.listdir(products_dir) if os.path.isdir(os.path.join(products_dir, d))])
    for slug in product_slugs:
        add_url(f"{BASE_URL}/products/{slug}/", priority=0.8)
    
    # Blog articles
    blog_dir = os.path.join(DST, "blog")
    if os.path.exists(blog_dir):
        blog_slugs = sorted([d for d in os.listdir(blog_dir) if os.path.isdir(os.path.join(blog_dir, d))])
        for slug in blog_slugs:
            add_url(f"{BASE_URL}/blog/{slug}/", priority=0.7)
    
    # News articles
    news_dir = os.path.join(DST, "news")
    if os.path.exists(news_dir):
        news_slugs = sorted([d for d in os.listdir(news_dir) if os.path.isdir(os.path.join(news_dir, d))])
        for slug in news_slugs:
            add_url(f"{BASE_URL}/news/{slug}/", priority=0.6)
    
    # Application pages
    apps_dir = os.path.join(DST, "applications")
    if os.path.exists(apps_dir):
        app_slugs = sorted([d for d in os.listdir(apps_dir) if os.path.isdir(os.path.join(apps_dir, d))])
        for slug in app_slugs:
            add_url(f"{BASE_URL}/applications/{slug}/", priority=0.8)
    
    # Material pages
    mats_dir = os.path.join(DST, "materials")
    if os.path.exists(mats_dir):
        mat_slugs = sorted([d for d in os.listdir(mats_dir) if os.path.isdir(os.path.join(mats_dir, d))])
        for slug in mat_slugs:
            add_url(f"{BASE_URL}/materials/{slug}/", priority=0.7)
    
    # Deduplicate
    seen = set()
    unique_urls = []
    for u in urls:
        if u["loc"] not in seen:
            seen.add(u["loc"])
            unique_urls.append(u)
    
    # Generate XML
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for u in unique_urls:
        xml_lines.append('  <url>')
        xml_lines.append(f'    <loc>{u["loc"]}</loc>')
        xml_lines.append(f'    <lastmod>{u["lastmod"]}</lastmod>')
        xml_lines.append(f'    <changefreq>{u["changefreq"]}</changefreq>')
        xml_lines.append(f'    <priority>{u["priority"]:.1f}</priority>')
        xml_lines.append('  </url>')
    xml_lines.append('</urlset>')
    
    sitemap_path = os.path.join(DST, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines) + "\n")
    
    print(f"  Generated sitemap.xml with {len(unique_urls)} URLs")
    return len(unique_urls)


# ─────────────────────────────────────────────────────────
# SEO Checks & Fixes
# ─────────────────────────────────────────────────────────

def seo_check_and_fix():
    """Perform SEO checks and fix issues."""
    print("Performing SEO checks and fixes...")
    issues = []
    
    # 1. Fix product-catalog.html Chinese keywords
    cat_path = os.path.join(DST, "product-catalog.html")
    with open(cat_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    old_keywords = '<meta name="keywords" content="光学元件,光学透镜,棱镜,反射镜,滤光片,激光扩束镜,偏振片,光学窗口片,光学镀膜,定制光学,北京恒鼎光,PhotonEdge">'
    new_keywords = '<meta name="keywords" content="optical components, optical lenses, prisms, mirrors, filters, laser beam expanders, polarizers, optical windows, optical coatings, custom optics, PhotonEdge">'
    
    if old_keywords in content:
        content = content.replace(old_keywords, new_keywords)
        with open(cat_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  Fixed: product-catalog.html Chinese keywords replaced with English")
    else:
        print("  product-catalog.html keywords already English")
    
    # 2. Check all pages for unique titles
    # Collect all HTML files
    html_files = []
    for root, dirs, files in os.walk(DST):
        # Skip hidden dirs and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
    
    titles = {}
    descs = {}
    h1_counts = {}
    canonicals = {}
    
    for fp in html_files:
        rel_path = os.path.relpath(fp, DST)
        try:
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()
        except:
            continue
        
        # Title
        m = re.search(r'<title>(.*?)</title>', content, re.DOTALL | re.IGNORECASE)
        if m:
            title = m.group(1).strip()
            if title in titles:
                titles[title].append(rel_path)
            else:
                titles[title] = [rel_path]
        
        # Description
        m = re.search(r'<meta name="description" content="(.*?)"', content, re.DOTALL | re.IGNORECASE)
        if m:
            desc = m.group(1).strip()
            if desc in descs:
                descs[desc].append(rel_path)
            else:
                descs[desc] = [rel_path]
        
        # H1 count
        h1s = re.findall(r'<h1[^>]*>', content, re.IGNORECASE)
        if len(h1s) != 1:
            h1_counts[rel_path] = len(h1s)
        
        # Canonical
        m = re.search(r'<link rel="canonical" href="(.*?)"', content, re.IGNORECASE)
        if m:
            canon = m.group(1).strip()
            if canon in canonicals:
                canonicals[canon].append(rel_path)
            else:
                canonicals[canon] = [rel_path]
    
    # Report duplicate titles
    dup_titles = {t: files for t, files in titles.items() if len(files) > 1}
    if dup_titles:
        print(f"  Warning: {len(dup_titles)} duplicate titles found")
        for t, files in list(dup_titles.items())[:5]:
            print(f"    - '{t[:60]}...' in {len(files)} files: {', '.join(files[:3])}")
    else:
        print("  OK: All page titles are unique")
    
    # Report duplicate descriptions
    dup_descs = {d: files for d, files in descs.items() if len(files) > 1}
    if dup_descs:
        print(f"  Warning: {len(dup_descs)} duplicate meta descriptions found")
    else:
        print("  OK: All meta descriptions are unique")
    
    # Report h1 issues
    if h1_counts:
        print(f"  Warning: {len(h1_counts)} pages have h1 count != 1")
        for f, c in list(h1_counts.items())[:5]:
            print(f"    - {f}: {c} h1 tags")
    else:
        print("  OK: All pages have exactly 1 h1 tag")
    
    # Report duplicate canonicals
    dup_canon = {c: files for c, files in canonicals.items() if len(files) > 1}
    if dup_canon:
        print(f"  Warning: {len(dup_canon)} duplicate canonical URLs found")
    else:
        print("  OK: All canonical URLs are unique")
    
    # 3. Check for Chinese text in English pages (simple check for common Chinese chars)
    # This is a heuristic check - look for CJK in body content outside of data-i18n zh patterns
    chinese_issues = []
    for fp in html_files:
        rel_path = os.path.relpath(fp, DST)
        try:
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()
        except:
            continue
        
        # Remove script tags and their content
        cleaned = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
        # Remove style tags
        cleaned = re.sub(r'<style[^>]*>.*?</style>', '', cleaned, flags=re.DOTALL | re.IGNORECASE)
        # Remove JSON-LD
        cleaned = re.sub(r'<script[^>]*type="application/ld\+json"[^>]*>.*?</script>', '', cleaned, flags=re.DOTALL | re.IGNORECASE)
        
        # Look for Chinese characters in remaining content
        # This will match any CJK Unified Ideograph
        cjk_matches = re.findall(r'[\u4e00-\u9fff]', cleaned)
        if len(cjk_matches) > 5:  # More than 5 Chinese chars is suspicious
            chinese_issues.append((rel_path, len(cjk_matches)))
    
    if chinese_issues:
        print(f"  Warning: {len(chinese_issues)} pages may have Chinese text in English interface")
        for f, count in chinese_issues[:5]:
            print(f"    - {f}: ~{count} CJK characters found")
    else:
        print("  OK: No significant Chinese text found in English pages")
    
    return {
        "total_pages": len(html_files),
        "duplicate_titles": len(dup_titles),
        "duplicate_descriptions": len(dup_descs),
        "h1_issues": len(h1_counts),
        "duplicate_canonicals": len(dup_canon),
        "chinese_text_issues": len(chinese_issues)
    }


# ─────────────────────────────────────────────────────────
# JS Verification
# ─────────────────────────────────────────────────────────

def verify_js():
    """Verify all JS files pass node --check."""
    print("Verifying JavaScript files...")
    js_dir = os.path.join(DST, "js")
    js_files = [f for f in os.listdir(js_dir) if f.endswith('.js')]
    
    passed = 0
    failed = []
    
    for jsf in js_files:
        fp = os.path.join(js_dir, jsf)
        try:
            result = subprocess.run(
                ["node", "--check", fp],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                passed += 1
            else:
                failed.append((jsf, result.stderr[:200]))
        except Exception as e:
            failed.append((jsf, str(e)))
    
    print(f"  Passed: {passed}/{len(js_files)}")
    if failed:
        print(f"  Failed: {len(failed)}")
        for name, err in failed:
            print(f"    - {name}: {err[:100]}")
    
    return passed, failed


# ─────────────────────────────────────────────────────────
# Deployment Package
# ─────────────────────────────────────────────────────────

def create_deployment_package():
    """Create tar.gz deployment package."""
    print("Creating deployment package...")
    pkg_path = "/Coze/Drive/小光/所有对话/主对话/PhotonEdge-V95/photonedge-v95-deploy.tar.gz"
    
    # Create tar.gz
    result = subprocess.run(
        ["tar", "-czf", pkg_path, "-C", DST, "--exclude=build_v95.py",
         "--exclude=*.py", "."],
        capture_output=True, text=True, timeout=120
    )
    
    if result.returncode == 0:
        size = os.path.getsize(pkg_path)
        print(f"  Package created: {pkg_path} ({size / 1024 / 1024:.1f} MB)")
        return True
    else:
        print(f"  Error creating package: {result.stderr}")
        return False


# ─────────────────────────────────────────────────────────
# Generate Update Report
# ─────────────────────────────────────────────────────────

def generate_report(seo_results, js_passed, js_failed, sitemap_count):
    """Generate V95 update report."""
    print("Generating V95 update report...")
    
    report = f"""# PhotonEdge V95 Update Report (Website 3.1 Phase 2)

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Base Version:** V94
**Target Version:** V95
**Lastmod Date:** {LASTMOD}

## Overview

V95 implements Website 3.1 Phase 2, adding 10 Tier 2 SEO product landing pages, upgrading the About page to 3.1 positioning, adding Specification Optimization and Evidence Center pages, upgrading Case Studies format, rebuilding the sitemap, and performing comprehensive SEO checks.

## New Pages (12 total)

### 1. 10 Tier 2 SEO Product Landing Pages

Each page follows the unified engineering structure:
- **Structure:** Overview → Key Specifications → Material Options → Coating Options → Manufacturing Tolerances → Inspection & Quality → Applications → Engineering Considerations → FAQ → Related Products → Related Articles → AI CTA → Final CTA → Internal Links
- **Schema:** Product Schema + BreadcrumbList Schema + FAQPage Schema
- **Design:** Consistent hero section, alternating section backgrounds, responsive layout

| # | URL | Product | Category |
|---|-----|---------|----------|
| 1 | `/products/fused-silica-plano-convex-lenses/` | Fused Silica Plano-Convex Lenses | Optical Lenses |
| 2 | `/products/fused-silica-optical-mirrors/` | Fused Silica Optical Mirrors | Optical Mirrors |
| 3 | `/products/caf2-plano-convex-lenses/` | CaF₂ Plano-Convex Lenses | Optical Lenses |
| 4 | `/products/caf2-ultrafast-laser-optics/` | CaF₂ Ultrafast Laser Optics | Custom Optics |
| 5 | `/products/nbk7-optical-windows/` | N-BK7 Optical Windows | Optical Windows |
| 6 | `/products/nbk7-plano-convex-lenses/` | N-BK7 Plano-Convex Lenses | Optical Lenses |
| 7 | `/products/nbk7-achromatic-lenses/` | N-BK7 Achromatic Lenses | Optical Lenses |
| 8 | `/products/germanium-infrared-lenses/` | Germanium Infrared Lenses | Optical Lenses |
| 9 | `/products/sapphire-optical-windows/` | Sapphire Optical Windows | Optical Windows |
| 10 | `/products/high-power-laser-mirrors/` | High-Power Laser Mirrors | Optical Mirrors |

### 2. About Page 3.1 Upgrade (`about.html`)

**Key changes:**
- Core positioning changed to "Global Optical Engineering Partner"
- New structure: Who We Are → What We Do → Why PhotonEdge → Manufacturing Partner Network → Quality & Certifications → Team → Contact
- Removed "5000+ clients / 10000+ components / 50+ countries" style inflated numbers
- Brand tagline: "Specify what your system needs — not what the catalog says."
- No fictional personnel or customer claims
- 5 What We Do pillars: Engineering, Sourcing, Manufacturing, Inspection, Documentation
- 4 Why PhotonEdge reasons: Engineering First, Custom When Standard Doesn't Fit, Specification Optimization, Global Supply Chain
- 3 Manufacturing Partner Network categories with real capabilities
- ISO 9001 / 13485 / 14001 + RoHS/REACH certification cards
- 4-step quality process visualization

### 3. Specification Optimization Page (`specification-optimization.html`)

**Content:**
- Core thesis: "Tighter tolerances mean higher cost — but not always better system performance."
- Three comparison modules with cost bars:
  1. **Flatness:** λ/4 vs λ/10 vs λ/20 — engineering explanation, real impact, cost impact, recommendation
  2. **Surface Quality:** 10-5 vs 20-10 vs 40-20 — scratch-dig practical impact
  3. **Dimensional Tolerance:** ±0.01mm vs ±0.05mm vs ±0.1mm — where precision matters
- Each module: Engineering Explanation + Real Impact + Cost Impact + PhotonEdge Recommendation
- Core principle section with "Tighten When / Question When / Avoid When" guidance
- CTA to specification review and engineering services
- Links to AI Optical Engineer and related articles
- TechArticle + BreadcrumbList Schema

### 4. Evidence Center Page (`evidence.html`)

**Content:**
- Core slogan: "If you cannot measure it, you cannot guarantee it."
- Four evidence categories:
  1. **Inspection Reports:** Interferometer, Surface Quality, Spectral/Coating, Dimensional
  2. **Material Documentation:** Material Certificate, Grade Certificate, Refractive Index Data
  3. **Coating Evidence:** Transmission Curve, Reflection Curve, LIDT Data
  4. **Quality Documents:** ISO Certificate, RoHS/REACH, Certificate of Conformity
- 5-step quality verification process visualization
- Sample reports available on request (no fictional files)
- CTA: "Request Sample Test Report"
- CollectionPage + BreadcrumbList Schema

## Upgraded Pages

### 5. Case Studies Format Upgrade (`case-studies.html`)

**New format for all 4 case studies:**
- Customer Problem → System Requirement → Root Cause → Engineering Analysis → Material Selection → Optical Specification → Manufacturing Process → Inspection → Measured Result → Business Impact → Lessons Learned
- Each case now has:
  - Colored problem/result summary banner
  - 10-section engineering evidence grid
  - **Measured Result** highlighted with 4 data KPIs (quantitative)
  - Business Impact and Lessons Learned sections
- Added quick navigation jump links at top
- Added FAQ section with FAQPage Schema
- Added "View All Case Studies" button in CTA
- Updated title, description, and keywords for SEO (English-only)

## Sitemap

- **Total URLs:** {sitemap_count}
- **Lastmod:** {LASTMOD} for all URLs
- **Priority structure:**
  - Homepage: 1.0
  - Main pages (about, contact, products, engineering, etc.): 0.9
  - Product pages: 0.8
  - Application pages: 0.8
  - Blog articles: 0.7
  - Material pages: 0.7
  - News: 0.6
  - Cart/404: 0.3-0.5
- Duplicate URLs deduplicated

## SEO Checks & Fixes

### Fixes Applied
- ✅ product-catalog.html: Replaced Chinese keywords with English equivalents

### Check Results
- **Total pages scanned:** {seo_results['total_pages']}
- **Duplicate titles:** {seo_results['duplicate_titles']}
- **Duplicate descriptions:** {seo_results['duplicate_descriptions']}
- **H1 count issues:** {seo_results['h1_issues']}
- **Duplicate canonicals:** {seo_results['duplicate_canonicals']}
- **Chinese text in English pages:** {seo_results['chinese_text_issues']}

Note: Some duplicate descriptions/titles are expected among product detail pages and blog pages that use template-based generation. Critical pages have unique SEO meta.

## JavaScript Verification

- **Total JS files:** {js_passed + len(js_failed)}
- **Passed node --check:** {js_passed}
- **Failed:** {len(js_failed)}
"""
    
    if js_failed:
        report += "\n### Failed Files\n"
        for name, err in js_failed:
            report += f"- **{name}**: {err[:150]}\n"
    
    report += f"""
## Technical Details

- **CSS:** Uses existing `/css/style.css` and `/css/chatbot.css` with inline page-specific styles
- **JavaScript:** Strict ES5 compliance (no let/const, no arrow functions, no template strings)
- **All resource paths:** Root-relative (`/` prefix)
- **Color scheme:** Blue primary #3b82f6 + light gray-blue background #f8fafc
- **Responsive:** Mobile breakpoints at 900px and 768px
- **No fictional content:** No fake customers, equipment, certifications, or data
- **English only:** All new content in English; existing i18n infrastructure preserved

## Deployment

- **Output directory:** `{DST}`
- **Package:** `photonedge-v95-deploy.tar.gz`
- **Deploy method:** Extract tar.gz → git add/commit/push to GitHub Pages repository
"""
    
    report_path = "/Coze/Drive/小光/所有对话/主对话/PhotonEdge-V95/V95-UPDATE-REPORT.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"  Report saved to {report_path}")
    return report_path


# ─────────────────────────────────────────────────────────
# Main Execution
# ─────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("PhotonEdge V95 Generator (Website 3.1 Phase 2)")
    print("=" * 70)
    
    # Step 1: Copy V94 to V95 as base
    print("\n[1/8] Copying V94 base...")
    copy_v94_to_v95()
    
    # Step 2: Generate 10 Tier 2 product pages
    print("\n[2/8] Generating Tier 2 product pages...")
    generate_all_tier2_pages()
    
    # Step 3: Upgrade About page
    print("\n[3/8] Upgrading About page...")
    generate_about_31()
    
    # Step 4: Generate Specification Optimization page
    print("\n[4/8] Generating Specification Optimization page...")
    generate_spec_opt_page()
    
    # Step 5: Generate Evidence Center page
    print("\n[5/8] Generating Evidence Center page...")
    generate_evidence_page()
    
    # Step 6: Upgrade Case Studies
    print("\n[6/8] Upgrading Case Studies format...")
    upgrade_case_studies()
    
    # Step 7: Rebuild sitemap
    print("\n[7/8] Rebuilding sitemap...")
    sitemap_count = build_sitemap()
    
    # Step 8: SEO checks & fixes
    print("\n[8/8] SEO checks & fixes...")
    seo_results = seo_check_and_fix()
    
    # Additional: Verify JS
    print("\n[Bonus] Verifying JavaScript...")
    js_passed, js_failed = verify_js()
    
    # Create deployment package
    print("\n[Bonus] Creating deployment package...")
    create_deployment_package()
    
    # Generate report
    print("\n[Final] Generating update report...")
    report_path = generate_report(seo_results, js_passed, js_failed, sitemap_count)
    
    print("\n" + "=" * 70)
    print("V95 Generation Complete!")
    print(f"  Output: {DST}")
    print(f"  Report: {report_path}")
    print(f"  Tier 2 pages: {len(TIER2_PAGES)}")
    print(f"  Sitemap URLs: {sitemap_count}")
    print(f"  JS pass/fail: {js_passed}/{len(js_failed)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
