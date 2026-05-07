 // PhotonEdge Products Data

const PRODUCTS = [
  {
    "id": 1,
    "name": "UV Fused Silica Ball Lenses",
    "nameZh": "UV熔融石英球透镜",
    "category": "Optical Ball Lenses",
    "categoryZh": "光学球透镜",
    "description": "High-grade UV fused silica ball lenses featuring superior transmittance from UV to near-IR (185-2500nm). Ideal for fiber optic coupling, endoscopy, and laser diode collimation. Low thermal expansion coefficient ensures stability in demanding environments.",
    "image": "images/products/optical-ball-lenses/uv-fused-silica-ball-lenses.jpg",
    "parameters": {
      "material": "Fused Silica (JGS1)",
      "diameter": "0.5-10mm",
      "wavelength_range": "185-2500nm",
      "surface_quality": "40-20",
      "clear_aperture": ">90%"
    },
    "price": 18,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 2,
    "name": "Beamsplitter Plate",
    "nameZh": "分光板",
    "category": "Optical Beamsplitters",
    "categoryZh": "光学分光镜",
    "description": "Optical beamsplitter plates split incident light into transmitted and reflected beams in various ratios such as 50/50, 60/40, 80/20, or 90/10 through dielectric coatings. The default configuration is 50/50 beam splitting. Custom splitting ratios are available upon request.",
    "image": "images/products/optical-beamsplitters/beamsplitter-plate.jpg",
    "parameters": {
      "material": "N-BK7 / K9",
      "diameter_tolerance": "±0.15mm",
      "thickness_tolerance": "±0.10mm",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4 @ 632.8nm",
      "parallelism": "<1 arc min",
      "split_ratio": "50/50 ±2%, T=(Ts+Tp)/2, R=(Rs+Rp)/2",
      "coatings": "One side: dielectric partial reflection; other side: AR coating"
    },
    "partNumbers": [
      {
        "partNumber": "LOBP12.7-450/650",
        "dimension": "Φ12.7×3.0mm",
        "wavelength": "450-650nm",
        "price": 35
      },
      {
        "partNumber": "LOBP20.0-450/650",
        "dimension": "Φ20.0×3.0mm",
        "wavelength": "450-650nm",
        "price": 45
      },
      {
        "partNumber": "LOBP25.4-450/650",
        "dimension": "Φ25.4×3.0mm",
        "wavelength": "450-650nm",
        "price": 55
      },
      {
        "partNumber": "LOBP50.8-450/650",
        "dimension": "Φ50.8×3.0mm",
        "wavelength": "450-650nm",
        "price": 75
      },
      {
        "partNumber": "LOBP12.7-650/900",
        "dimension": "Φ12.7×3.0mm",
        "wavelength": "650-900nm",
        "price": 38
      },
      {
        "partNumber": "LOBP25.4-650/900",
        "dimension": "Φ25.4×3.0mm",
        "wavelength": "650-900nm",
        "price": 58
      },
      {
        "partNumber": "LOBP50.8-650/900",
        "dimension": "Φ50.8×3.0mm",
        "wavelength": "650-900nm",
        "price": 78
      },
      {
        "partNumber": "LOBP12.7-900/1200",
        "dimension": "Φ12.7×3.0mm",
        "wavelength": "900-1200nm",
        "price": 40
      },
      {
        "partNumber": "LOBP25.4-900/1200",
        "dimension": "Φ25.4×3.0mm",
        "wavelength": "900-1200nm",
        "price": 60
      },
      {
        "partNumber": "LOBP50.8-900/1200",
        "dimension": "Φ50.8×3.0mm",
        "wavelength": "900-1200nm",
        "price": 85
      }
    ],
    "price": 35,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 3,
    "name": "Non-Polarising Beamsplitter Cubes",
    "nameZh": "非偏振分光立方体",
    "category": "Optical Beamsplitters",
    "categoryZh": "光学分光镜",
    "description": "Non-polarizing cube beamsplitters provide equal splitting of incident light without affecting polarization state. Ideal for interferometry, microscopy, and optical metrology applications.",
    "image": "images/products/optical-beamsplitters/non-polarising-beamsplitter-cubes.jpg",
    "parameters": {
      "material": "N-BK7",
      "size": "10-50mm",
      "split_ratio": "50:50 (±5%)",
      "wavelength_range": "400-700nm",
      "surface_quality": "40-20",
      "beam_deviation": "<5 arcmin"
    },
    "price": 55,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 4,
    "name": "Non-Polarizing Beamsplitter Plate",
    "nameZh": "非偏振分光板",
    "category": "Optical Beamsplitters",
    "categoryZh": "光学分光镜",
    "description": "Non-polarizing plate beamsplitters designed for uniform beam splitting across a wide wavelength range. Suitable for RGB applications and general-purpose beam splitting needs.",
    "image": "images/products/optical-beamsplitters/non-polarizing-beamsplitter-plate.jpg",
    "parameters": {
      "material": "K9/BK7",
      "diameter": "12.7-50.8mm",
      "thickness": "1-5mm",
      "split_ratio": "50:50 / 70:30",
      "wavelength_range": "400-700nm",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4@632.8nm"
    },
    "price": 45,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LONPB-12.7-532",
        "dimension": "12.7x12.7x12.7mm",
        "wavelength": "532nm",
        "price": 65
      },
      {
        "partNumber": "LONPB-20-532",
        "dimension": "20x20x20mm",
        "wavelength": "532nm",
        "price": 85
      },
      {
        "partNumber": "LONPB-25.4-532",
        "dimension": "25.4x25.4x25.4mm",
        "wavelength": "532nm",
        "price": 105
      },
      {
        "partNumber": "LONPB-12.7-633",
        "dimension": "12.7x12.7x12.7mm",
        "wavelength": "633nm",
        "price": 65
      },
      {
        "partNumber": "LONPB-25.4-633",
        "dimension": "25.4x25.4x25.4mm",
        "wavelength": "633nm",
        "price": 105
      },
      {
        "partNumber": "LONPB-12.7-1064",
        "dimension": "12.7x12.7x12.7mm",
        "wavelength": "1064nm",
        "price": 68
      },
      {
        "partNumber": "LONPB-25.4-1064",
        "dimension": "25.4x25.4x25.4mm",
        "wavelength": "1064nm",
        "price": 108
      }
    ]
  },
  {
    "id": 5,
    "name": "Optical Cube Beamsplitters",
    "nameZh": "光学立方体分光镜",
    "category": "Optical Beamsplitters",
    "categoryZh": "光学分光镜",
    "description": "Multilayer dielectric cube beamsplitters consist of two right-angle prisms cemented together. The beamsplitter divides incident light into reflected and transmitted beams in a 1:2 or 1:3 ratio. Both entry and exit faces are coated with multilayer anti-reflection coatings. Since dielectric coatings have virtually no absorption, incident light loss is minimal. Unlike plate beamsplitters, cube beamsplitters experience almost no optical axis shift or ghost images.",
    "image": "images/products/optical-beamsplitters/optical-cube-beamsplitters.jpg",
    "parameters": {
      "material": "N-BK7",
      "size_tolerance": "±0.15mm",
      "angle_tolerance": "±10 arc sec",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4 @ 632.8nm",
      "parallelism": "<1 arc min",
      "split_ratio": "50/50 ±3%",
      "coatings": "Cemented face: dielectric; entry/exit faces: AR coating"
    },
    "partNumbers": [
      {
        "partNumber": "LOCBS10-532",
        "dimension": "10.0×10.0×10.0mm",
        "wavelength": "532nm",
        "price": 55
      },
      {
        "partNumber": "LOCBS12.7-532",
        "dimension": "12.7×12.7×12.7mm",
        "wavelength": "532nm",
        "price": 65
      },
      {
        "partNumber": "LOCBS20-532",
        "dimension": "20.0×20.0×20.0mm",
        "wavelength": "532nm",
        "price": 85
      },
      {
        "partNumber": "LOCBS10-633",
        "dimension": "10.0×10.0×10.0mm",
        "wavelength": "633nm",
        "price": 55
      },
      {
        "partNumber": "LOCBS12.7-633",
        "dimension": "12.7×12.7×12.7mm",
        "wavelength": "633nm",
        "price": 65
      },
      {
        "partNumber": "LOCBS20-633",
        "dimension": "20.0×20.0×20.0mm",
        "wavelength": "633nm",
        "price": 85
      },
      {
        "partNumber": "LOCBS10-1064",
        "dimension": "10.0×10.0×10.0mm",
        "wavelength": "1064nm",
        "price": 50
      },
      {
        "partNumber": "LOCBS12.7-1064",
        "dimension": "12.7×12.7×12.7mm",
        "wavelength": "1064nm",
        "price": 60
      },
      {
        "partNumber": "LOCBS20-1064",
        "dimension": "20.0×20.0×20.0mm",
        "wavelength": "1064nm",
        "price": 80
      },
      {
        "partNumber": "LOCBS25.4-1064",
        "dimension": "25.4×25.4×25.4mm",
        "wavelength": "1064nm",
        "price": 105
      }
    ],
    "price": 55,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 6,
    "name": "Optical Polarizing Beamsplitter Cubes",
    "nameZh": "偏振分光立方体",
    "category": "Optical Beamsplitters",
    "categoryZh": "光学分光镜",
    "description": "High-performance polarizing cube beamsplitters separating S and P polarizations with extinction ratios exceeding 1000:1. Essential for polarimetry, ellipsometry, and optical communication systems.",
    "image": "images/products/optical-beamsplitters/optical-polarizing-beamsplitter-cubes.jpg",
    "parameters": {
      "material": "N-BK7 / Calcite",
      "size": "10-25mm",
      "extinction_ratio": ">10^5:1",
      "wavelength_range": "400-700nm / 650-1050nm",
      "surface_quality": "40-20",
      "transmittance": ">90% (P-polarized)"
    },
    "price": 120,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 7,
    "name": "UV Fused Silica Plano Concave Cylindrical Lenses",
    "nameZh": "UV熔融石英平凹柱面透镜",
    "category": "Optical Cylindrical Lenses",
    "categoryZh": "光学柱面透镜",
    "description": "UV-grade plano-concave cylindrical lenses for generating line-shaped laser beams or correcting astigmatism. Excellent for semiconductor inspection and laser material processing.",
    "image": "images/products/optical-cylindrical-lenses/uv-fused-silica-plano-concave-cylindrical-lenses.jpg",
    "parameters": {
      "material": "Fused Silica (JGS1)",
      "diameter": "6-50mm",
      "focal_length": "-20 to -200mm",
      "wavelength_range": "185-2500nm",
      "surface_quality": "20-10",
      "coating": "Uncoated / AR coating"
    },
    "price": 35,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 8,
    "name": "UV Fused Silica Plano Convex Cylindrical Lenses",
    "nameZh": "UV熔融石英平凸柱面透镜",
    "category": "Optical Cylindrical Lenses",
    "categoryZh": "光学柱面透镜",
    "description": "UV-grade plano-convex cylindrical lenses for line generation and one-dimensional beam shaping. Ideal for barcode scanning, optical character recognition, and laser projection systems.",
    "image": "images/products/optical-cylindrical-lenses/uv-fused-silica-plano-convex-cylindrical-lenses.jpg",
    "parameters": {
      "material": "Fused Silica (JGS1)",
      "diameter": "6-50mm",
      "focal_length": "20-200mm",
      "wavelength_range": "185-2500nm",
      "surface_quality": "20-10",
      "coating": "Uncoated / AR coating"
    },
    "price": 35,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 9,
    "name": "Circular Variable ND(neutral density) Filters",
    "nameZh": "圆形可变中性密度滤光片",
    "category": "Optical Filters",
    "categoryZh": "光学滤光片",
    "description": "Continuously variable neutral density filters with rotary adjustment for fine-tuning laser power and light attenuation. Perfect for balancing illumination in microscopy, photography, and laser applications. Available in various optical density ranges.",
    "image": "images/products/optical-filters/circular-variable-ndneutral-density-filters.jpg",
    "parameters": {
      "material": "Schott Glass / Dielectric",
      "diameter": "25-50mm",
      "od_range": "0.04-2.5",
      "wavelength_range": "400-700nm / 650-1050nm",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4@632.8nm",
      "angular_tolerance": "±1°"
    },
    "price": 55,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LORVF01",
        "odRange": "0.0-1.0",
        "diameter": "25.00mm",
        "price": 85
      },
      {
        "partNumber": "LORVF03",
        "odRange": "0.0-1.0",
        "diameter": "50.00mm",
        "price": 120
      },
      {
        "partNumber": "LORVF04",
        "odRange": "0.0-1.5",
        "diameter": "25.00mm",
        "price": 90
      },
      {
        "partNumber": "LORVF05",
        "odRange": "0.0-1.5",
        "diameter": "50.00mm",
        "price": 130
      },
      {
        "partNumber": "LORVF06",
        "odRange": "0.0-2.0",
        "diameter": "25.00mm",
        "price": 95
      },
      {
        "partNumber": "LORVF07",
        "odRange": "0.0-2.0",
        "diameter": "50.00mm",
        "price": 140
      },
      {
        "partNumber": "LORVF08",
        "odRange": "0.0-3.0",
        "diameter": "25.00mm",
        "price": 105
      },
      {
        "partNumber": "LORVF09",
        "odRange": "0.0-3.0",
        "diameter": "50.00mm",
        "price": 155
      }
    ]
  },
  {
    "id": 10,
    "name": "Color Glass Filter",
    "nameZh": "颜色玻璃滤光片",
    "category": "Optical Filters",
    "categoryZh": "光学滤光片",
    "description": "High-quality colored glass filters for wavelength selection and color correction. Made from Schott or Hoya glass with excellent spectral characteristics and thermal stability.",
    "image": "images/products/optical-filters/color-glass-filter.jpg",
    "parameters": {
      "material": "Schott / Hoya Glass",
      "diameter": "12.7-50.8mm",
      "thickness": "1-5mm",
      "wavelength_range": "300-2000nm",
      "surface_quality": "40-20"
    },
    "price": 25,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 11,
    "name": "Fixed Neutral Density Filters",
    "nameZh": "固定中性密度滤光片",
    "category": "Optical Filters",
    "categoryZh": "光学滤光片",
    "description": "Precision fixed ND filters providing uniform light attenuation across the visible spectrum. Available in standard OD values from 0.1 to 4.0 for laser power control and imaging applications.",
    "image": "images/products/optical-filters/fixed-neutral-density-filters.jpg",
    "parameters": {
      "material": "Schott Glass / Dielectric",
      "diameter": "12.7-50.8mm",
      "od_value": "0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.9, 1.0, 2.0, 3.0, 4.0",
      "wavelength_range": "400-700nm (VIS) / 250-2500nm (NIR)",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4@632.8nm"
    },
    "price": 20,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOFNF1-12.7",
        "diameter": "12.7mm",
        "od": "1.0",
        "transmittance": "10%",
        "price": 18
      },
      {
        "partNumber": "LOFNF2-12.7",
        "diameter": "12.7mm",
        "od": "2.0",
        "transmittance": "1.0%",
        "price": 20
      },
      {
        "partNumber": "LOFNF3-12.7",
        "diameter": "12.7mm",
        "od": "3.0",
        "transmittance": "0.1%",
        "price": 22
      },
      {
        "partNumber": "LOFNF4-12.7",
        "diameter": "12.7mm",
        "od": "4.0",
        "transmittance": "0.01%",
        "price": 25
      },
      {
        "partNumber": "LOFNF0.1-25.4",
        "diameter": "25.4mm",
        "od": "0.1",
        "transmittance": "79%",
        "price": 22
      },
      {
        "partNumber": "LOFNF0.2-25.4",
        "diameter": "25.4mm",
        "od": "0.2",
        "transmittance": "63%",
        "price": 22
      },
      {
        "partNumber": "LOFNF0.3-25.4",
        "diameter": "25.4mm",
        "od": "0.3",
        "transmittance": "50%",
        "price": 24
      },
      {
        "partNumber": "LOFNF0.4-25.4",
        "diameter": "25.4mm",
        "od": "0.4",
        "transmittance": "39.8%",
        "price": 24
      },
      {
        "partNumber": "LOFNF0.5-25.4",
        "diameter": "25.4mm",
        "od": "0.5",
        "transmittance": "32%",
        "price": 25
      },
      {
        "partNumber": "LOFNF0.8-25.4",
        "diameter": "25.4mm",
        "od": "0.8",
        "transmittance": "15.8%",
        "price": 26
      },
      {
        "partNumber": "LOFNF1-25.4",
        "diameter": "25.4mm",
        "od": "1.0",
        "transmittance": "10%",
        "price": 28
      },
      {
        "partNumber": "LOFNF1.5-25.4",
        "diameter": "25.4mm",
        "od": "1.5",
        "transmittance": "3.2%",
        "price": 30
      },
      {
        "partNumber": "LOFNF2-25.4",
        "diameter": "25.4mm",
        "od": "2.0",
        "transmittance": "1%",
        "price": 32
      },
      {
        "partNumber": "LOFNF3-25.4",
        "diameter": "25.4mm",
        "od": "3.0",
        "transmittance": "0.1%",
        "price": 35
      }
    ]
  },
  {
    "id": 12,
    "name": "Narrow band filter",
    "nameZh": "窄带滤光片",
    "category": "Optical Filters",
    "categoryZh": "光学滤光片",
    "description": "High-performance narrow bandpass filters with steep edges and high transmission. Essential for fluorescence microscopy, Raman spectroscopy, and laser line isolation.",
    "image": "images/products/optical-filters/narrow-band-filter.jpg",
    "parameters": {
      "material": "Dielectric Multilayer",
      "diameter": "12.7-50.8mm",
      "center_wavelength": "400-1600nm (customizable)",
      "bandwidth": "1-40nm (FWHM)",
      "peak_transmittance": ">70%",
      "blocking": ">OD4"
    },
    "price": 75,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 13,
    "name": "Optical Linear Variable neutral density( ND) Filters",
    "nameZh": "线性可变中性密度滤光片",
    "category": "Optical Filters",
    "categoryZh": "光学滤光片",
    "description": "Linear gradient ND filters providing continuous optical density variation across the aperture. Ideal for spectrophotometry, photography, and balanced detection systems.",
    "image": "images/products/optical-filters/optical-linear-variable-neutral-density-nd-filters.jpg",
    "parameters": {
      "material": "Schott Glass / Dielectric",
      "size": "25x50mm / Custom",
      "od_range": "0.1-2.5",
      "wavelength_range": "400-700nm / 650-1050nm",
      "surface_quality": "40-20"
    },
    "price": 45,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 14,
    "name": "Ultraviolet through visible absorption filters",
    "nameZh": "紫外-可见吸收滤光片",
    "category": "Optical Filters",
    "categoryZh": "光学滤光片",
    "description": "Specialized UV to visible absorption filters blocking UV radiation while transmitting visible light. Commonly used in photography, lighting, and safety applications.",
    "image": "images/products/optical-filters/ultraviolet-through-visible-absorption-filters.jpg",
    "parameters": {
      "material": "Schott UG / BG Series",
      "diameter": "12.7-50.8mm",
      "cut_on_wavelength": "300-400nm",
      "peak_transmittance": ">80%",
      "surface_quality": "40-20"
    },
    "price": 30,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 15,
    "name": "UV Fused Silica Half Ball Lenses",
    "nameZh": "UV熔融石英半球透镜",
    "category": "Optical Half Ball Lenses",
    "categoryZh": "光学半球透镜",
    "description": "Half-ball lenses for fiber coupling and endoscopy applications. UV-grade fused silica provides excellent transmission in UV and deep UV applications.",
    "image": "images/products/optical-half-ball-lenses/uv-fused-silica-half-ball-lenses.jpg",
    "parameters": {
      "material": "Fused Silica (JGS1)",
      "diameter": "1-10mm",
      "wavelength_range": "185-2500nm",
      "surface_quality": "40-20",
      "clear_aperture": ">85%"
    },
    "price": 15,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 16,
    "name": "Achromatic Doublet Lenses",
    "nameZh": "消色差双胶合透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Color-corrected achromatic doublets minimizing chromatic aberration across the visible spectrum. Essential for imaging, photometry, and beam collimation in multi-wavelength applications.",
    "image": "images/products/optical-lenses/achromatic-doublet-lenses.jpg",
    "parameters": {
      "material": "N-BK7 + F2",
      "diameter": "6-75mm",
      "focal_length": "20-200mm",
      "coating": "AR coating (400-700nm)",
      "surface_quality": "40-20",
      "back_focal_length": "Customizable"
    },
    "price": 55,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOADL5-7.5",
        "diameter": "5.00mm",
        "focalLength": "7.50mm",
        "centerThickness": "4.50mm",
        "price": 65
      },
      {
        "partNumber": "LOADL5-10",
        "diameter": "5.00mm",
        "focalLength": "10.00mm",
        "centerThickness": "4.40mm",
        "price": 68
      },
      {
        "partNumber": "LOADL5-15",
        "diameter": "5.00mm",
        "focalLength": "15.00mm",
        "centerThickness": "4.80mm",
        "price": 70
      },
      {
        "partNumber": "LOADL6-10",
        "diameter": "6.00mm",
        "focalLength": "10.00mm",
        "centerThickness": "4.00mm",
        "price": 72
      },
      {
        "partNumber": "LOADL6.25-20",
        "diameter": "6.25mm",
        "focalLength": "20.00mm",
        "centerThickness": "3.60mm",
        "price": 75
      },
      {
        "partNumber": "LOADL6.25-25",
        "diameter": "6.25mm",
        "focalLength": "25.00mm",
        "centerThickness": "3.20mm",
        "price": 78
      },
      {
        "partNumber": "LOADL6.25-30",
        "diameter": "6.25mm",
        "focalLength": "30.00mm",
        "centerThickness": "3.20mm",
        "price": 78
      },
      {
        "partNumber": "LOADL8-20",
        "diameter": "8.00mm",
        "focalLength": "20.00mm",
        "centerThickness": "4.00mm",
        "price": 82
      },
      {
        "partNumber": "LOADL9-27",
        "diameter": "9.00mm",
        "focalLength": "27.00mm",
        "centerThickness": "5.19mm",
        "price": 85
      },
      {
        "partNumber": "LOADL9-36",
        "diameter": "9.00mm",
        "focalLength": "36.00mm",
        "centerThickness": "4.00mm",
        "price": 88
      },
      {
        "partNumber": "LOADL9-40",
        "diameter": "9.00mm",
        "focalLength": "40.00mm",
        "centerThickness": "5.06mm",
        "price": 90
      },
      {
        "partNumber": "LOADL9-45",
        "diameter": "9.00mm",
        "focalLength": "45.00mm",
        "centerThickness": "4.30mm",
        "price": 92
      },
      {
        "partNumber": "LOADL9-75",
        "diameter": "9.00mm",
        "focalLength": "75.00mm",
        "centerThickness": "4.60mm",
        "price": 95
      },
      {
        "partNumber": "LOADL12.5-40",
        "diameter": "12.50mm",
        "focalLength": "40.00mm",
        "centerThickness": "5.06mm",
        "price": 98
      },
      {
        "partNumber": "LOADL12.5-45",
        "diameter": "12.50mm",
        "focalLength": "45.00mm",
        "centerThickness": "5.00mm",
        "price": 100
      },
      {
        "partNumber": "LOADL12.5-50",
        "diameter": "12.50mm",
        "focalLength": "50.00mm",
        "centerThickness": "5.00mm",
        "price": 102
      },
      {
        "partNumber": "LOADL12.5-60",
        "diameter": "12.50mm",
        "focalLength": "60.00mm",
        "centerThickness": "5.00mm",
        "price": 105
      },
      {
        "partNumber": "LOADL12.5-75",
        "diameter": "12.50mm",
        "focalLength": "75.00mm",
        "centerThickness": "4.60mm",
        "price": 108
      },
      {
        "partNumber": "LOADL12.5-80",
        "diameter": "12.50mm",
        "focalLength": "80.00mm",
        "centerThickness": "3.70mm",
        "price": 110
      },
      {
        "partNumber": "LOADL12.5-90",
        "diameter": "12.50mm",
        "focalLength": "90.00mm",
        "centerThickness": "3.58mm",
        "price": 115
      },
      {
        "partNumber": "LOADL12.5-100",
        "diameter": "12.50mm",
        "focalLength": "100.00mm",
        "centerThickness": "4.50mm",
        "price": 118
      },
      {
        "partNumber": "LOADL12.7-25",
        "diameter": "12.70mm",
        "focalLength": "25.00mm",
        "centerThickness": "5.60mm",
        "price": 105
      },
      {
        "partNumber": "LOADL12.7-30",
        "diameter": "12.70mm",
        "focalLength": "30.00mm",
        "centerThickness": "5.30mm",
        "price": 108
      },
      {
        "partNumber": "LOADL12.7-40",
        "diameter": "12.70mm",
        "focalLength": "40.00mm",
        "centerThickness": "4.70mm",
        "price": 112
      },
      {
        "partNumber": "LOADL12.7-50",
        "diameter": "12.70mm",
        "focalLength": "50.00mm",
        "centerThickness": "4.40mm",
        "price": 115
      },
      {
        "partNumber": "LOADL12.7-60",
        "diameter": "12.70mm",
        "focalLength": "60.00mm",
        "centerThickness": "4.10mm",
        "price": 118
      },
      {
        "partNumber": "LOADL12.7-75",
        "diameter": "12.70mm",
        "focalLength": "75.00mm",
        "centerThickness": "3.90mm",
        "price": 122
      },
      {
        "partNumber": "LOADL15-50",
        "diameter": "15.00mm",
        "focalLength": "50.00mm",
        "centerThickness": "6.50mm",
        "price": 135
      },
      {
        "partNumber": "LOADL15-75",
        "diameter": "15.00mm",
        "focalLength": "75.00mm",
        "centerThickness": "7.50mm",
        "price": 145
      },
      {
        "partNumber": "LOADL18-80",
        "diameter": "18.00mm",
        "focalLength": "80.00mm",
        "centerThickness": "7.50mm",
        "price": 155
      },
      {
        "partNumber": "LOADL18-125",
        "diameter": "18.00mm",
        "focalLength": "125.00mm",
        "centerThickness": "6.50mm",
        "price": 165
      },
      {
        "partNumber": "LOADL20-60",
        "diameter": "20.00mm",
        "focalLength": "60.00mm",
        "centerThickness": "7.00mm",
        "price": 165
      },
      {
        "partNumber": "LOADL25-75",
        "diameter": "25.00mm",
        "focalLength": "75.00mm",
        "centerThickness": "9.50mm",
        "price": 185
      },
      {
        "partNumber": "LOADL25-100",
        "diameter": "25.00mm",
        "focalLength": "100.00mm",
        "centerThickness": "8.50mm",
        "price": 195
      },
      {
        "partNumber": "LOADL25.4-40",
        "diameter": "25.40mm",
        "focalLength": "40.00mm",
        "centerThickness": "12.50mm",
        "price": 195
      },
      {
        "partNumber": "LOADL25.4-60",
        "diameter": "25.40mm",
        "focalLength": "60.00mm",
        "centerThickness": "10.50mm",
        "price": 205
      },
      {
        "partNumber": "LOADL25.4-75",
        "diameter": "25.40mm",
        "focalLength": "75.00mm",
        "centerThickness": "9.50mm",
        "price": 215
      },
      {
        "partNumber": "LOADL25.4-100",
        "diameter": "25.40mm",
        "focalLength": "100.00mm",
        "centerThickness": "6.50mm",
        "price": 225
      }
    ]
  },
  {
    "id": 17,
    "name": "BK7  Plano Concave Cylindrical Lenses",
    "nameZh": "BK7平凹柱面透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Standard BK7 plano-concave cylindrical lenses for light divergence and beam expansion. Cost-effective solution for general-purpose optical applications.",
    "image": "images/products/optical-lenses/bk7--plano-concave-cylindrical-lenses.jpg",
    "parameters": {
      "material": "K9/BK7",
      "diameter": "6-100mm",
      "focal_length": "-20 to -300mm",
      "coating": "Uncoated / AR coating",
      "surface_quality": "40-20"
    },
    "price": 25,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 18,
    "name": "BK7 Double Concave Lenses",
    "nameZh": "BK7双凹透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Bi-concave lenses made from BK7 glass have a negative focal length and are primarily used for diverging parallel light and forming virtual images. Ideal for visible light applications. Various specifications available.",
    "image": "images/products/optical-lenses/bk7-uv-fused-silica-double-concave-lenses.jpg",
    "parameters": {
      "material": "K9 (BK7)",
      "diameter_tolerance": "±0.15mm",
      "thickness_tolerance": "±0.10mm",
      "focal_length_tolerance": "±1%",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4 @ 632.8nm",
      "centration": "<3 arc min",
      "clear_aperture": ">90%",
      "beveling": "0.25mm × 45°",
      "coatings": "Uncoated / AR coating available",
      "wavelength_range": "400-700nm"
    },
    "partNumbers": [
      {
        "partNumber": "LOBCCB6.35-12.5",
        "diameter": "6.35mm",
        "focalLength": "-12.50mm",
        "centerThickness": "2.50mm",
        "price": 25
      },
      {
        "partNumber": "LOBCCB12.7-15",
        "diameter": "12.70mm",
        "focalLength": "-15.00mm",
        "centerThickness": "2.30mm",
        "price": 28
      },
      {
        "partNumber": "LOBCCB12.7-20",
        "diameter": "12.70mm",
        "focalLength": "-20.00mm",
        "centerThickness": "2.00mm",
        "price": 28
      },
      {
        "partNumber": "LOBCCB12.7-25",
        "diameter": "12.70mm",
        "focalLength": "-25.00mm",
        "centerThickness": "2.50mm",
        "price": 30
      },
      {
        "partNumber": "LOBCCB12.7-30",
        "diameter": "12.70mm",
        "focalLength": "-30.00mm",
        "centerThickness": "2.70mm",
        "price": 30
      },
      {
        "partNumber": "LOBCCB12.7-40",
        "diameter": "12.70mm",
        "focalLength": "-40.00mm",
        "centerThickness": "2.00mm",
        "price": 32
      },
      {
        "partNumber": "LOBCCB12.7-50",
        "diameter": "12.70mm",
        "focalLength": "-50.00mm",
        "centerThickness": "3.50mm",
        "price": 35
      },
      {
        "partNumber": "LOBCCB12.7-75",
        "diameter": "12.70mm",
        "focalLength": "-75.00mm",
        "centerThickness": "2.50mm",
        "price": 38
      },
      {
        "partNumber": "LOBCCB25.4-50",
        "diameter": "25.40mm",
        "focalLength": "-50.00mm",
        "centerThickness": "3.00mm",
        "price": 45
      },
      {
        "partNumber": "LOBCCB25.4-75",
        "diameter": "25.40mm",
        "focalLength": "-75.00mm",
        "centerThickness": "3.50mm",
        "price": 50
      },
      {
        "partNumber": "LOBCCB25.4-100",
        "diameter": "25.40mm",
        "focalLength": "-100.00mm",
        "centerThickness": "4.00mm",
        "price": 55
      },
      {
        "partNumber": "LOBCCB25.4-150",
        "diameter": "25.40mm",
        "focalLength": "-150.00mm",
        "centerThickness": "2.50mm",
        "price": 58
      },
      {
        "partNumber": "LOBCCB25.4-200",
        "diameter": "25.40mm",
        "focalLength": "-200.00mm",
        "centerThickness": "2.50mm",
        "price": 60
      },
      {
        "partNumber": "LOBCCB30-50",
        "diameter": "30.00mm",
        "focalLength": "-50.00mm",
        "centerThickness": "2.00mm",
        "price": 60
      },
      {
        "partNumber": "LOBCCB30-60",
        "diameter": "30.00mm",
        "focalLength": "-60.00mm",
        "centerThickness": "2.00mm",
        "price": 62
      },
      {
        "partNumber": "LOBCCB30-70",
        "diameter": "30.00mm",
        "focalLength": "-70.00mm",
        "centerThickness": "2.00mm",
        "price": 64
      },
      {
        "partNumber": "LOBCCB30-80",
        "diameter": "30.00mm",
        "focalLength": "-80.00mm",
        "centerThickness": "2.00mm",
        "price": 65
      },
      {
        "partNumber": "LOBCCB50.8-75",
        "diameter": "50.80mm",
        "focalLength": "-75.00mm",
        "centerThickness": "2.50mm",
        "price": 80
      },
      {
        "partNumber": "LOBCCB50.8-100",
        "diameter": "50.80mm",
        "focalLength": "-100.00mm",
        "centerThickness": "2.50mm",
        "price": 85
      },
      {
        "partNumber": "LOBCCB50.8-150",
        "diameter": "50.80mm",
        "focalLength": "-150.00mm",
        "centerThickness": "2.50mm",
        "price": 90
      },
      {
        "partNumber": "LOBCCB50.8-200",
        "diameter": "50.80mm",
        "focalLength": "-200.00mm",
        "centerThickness": "2.50mm",
        "price": 95
      }
    ],
    "price": 25,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 67,
    "name": "UV Fused Silica Double Concave Lenses",
    "nameZh": "UV熔融石英双凹透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "UV Fused Silica bi-concave lenses offer superior transmittance from UV to near-IR (185-2500nm) with low thermal expansion coefficient. Ideal for UV and high-power laser applications.",
    "image": "images/products/optical-spherical-lenses/uv-fused-silica-double-concave-lenses.jpg",
    "parameters": {
      "material": "Fused Silica (JGS1)",
      "diameter_tolerance": "±0.15mm",
      "thickness_tolerance": "±0.10mm",
      "focal_length_tolerance": "±1%",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4 @ 632.8nm",
      "centration": "<3 arc min",
      "clear_aperture": ">90%",
      "wavelength_range": "185-2500nm",
      "coatings": "Uncoated / AR coating available"
    },
    "partNumbers": [
      {
        "partNumber": "LOBCCU6.35-12.5",
        "diameter": "6.35mm",
        "focalLength": "-12.50mm",
        "centerThickness": "2.50mm",
        "price": 35
      },
      {
        "partNumber": "LOBCCU12.7-15",
        "diameter": "12.70mm",
        "focalLength": "-15.00mm",
        "centerThickness": "2.30mm",
        "price": 38
      },
      {
        "partNumber": "LOBCCU12.7-20",
        "diameter": "12.70mm",
        "focalLength": "-20.00mm",
        "centerThickness": "2.00mm",
        "price": 38
      },
      {
        "partNumber": "LOBCCU12.7-25",
        "diameter": "12.70mm",
        "focalLength": "-25.00mm",
        "centerThickness": "2.50mm",
        "price": 42
      },
      {
        "partNumber": "LOBCCU12.7-30",
        "diameter": "12.70mm",
        "focalLength": "-30.00mm",
        "centerThickness": "2.70mm",
        "price": 42
      },
      {
        "partNumber": "LOBCCU12.7-40",
        "diameter": "12.70mm",
        "focalLength": "-40.00mm",
        "centerThickness": "2.00mm",
        "price": 45
      },
      {
        "partNumber": "LOBCCU12.7-50",
        "diameter": "12.70mm",
        "focalLength": "-50.00mm",
        "centerThickness": "3.50mm",
        "price": 48
      },
      {
        "partNumber": "LOBCCU25.4-50",
        "diameter": "25.40mm",
        "focalLength": "-50.00mm",
        "centerThickness": "3.00mm",
        "price": 60
      },
      {
        "partNumber": "LOBCCU25.4-75",
        "diameter": "25.40mm",
        "focalLength": "-75.00mm",
        "centerThickness": "3.50mm",
        "price": 68
      },
      {
        "partNumber": "LOBCCU25.4-100",
        "diameter": "25.40mm",
        "focalLength": "-100.00mm",
        "centerThickness": "4.00mm",
        "price": 75
      },
      {
        "partNumber": "LOBCCU50.8-75",
        "diameter": "50.80mm",
        "focalLength": "-75.00mm",
        "centerThickness": "2.50mm",
        "price": 110
      },
      {
        "partNumber": "LOBCCU50.8-100",
        "diameter": "50.80mm",
        "focalLength": "-100.00mm",
        "centerThickness": "2.50mm",
        "price": 118
      },
      {
        "partNumber": "LOBCCU50.8-150",
        "diameter": "50.80mm",
        "focalLength": "-150.00mm",
        "centerThickness": "2.50mm",
        "price": 125
      }
    ],
    "price": 35,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 19,
    "name": "BK7 Double Convex Lenses",
    "nameZh": "BK7双凸透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Bi-convex lenses have a positive focal length and are primarily used for collimating and focusing light. The symmetric design with equal curvature on both surfaces minimizes spherical aberration for improved image quality. Ideal for imaging, photometry, and beam collimation applications.",
    "image": "images/products/optical-lenses/bk7-double-convex-lenses.jpg",
    "parameters": {
      "material": "K9 (BK7)",
      "diameter_tolerance": "±0.15mm",
      "thickness_tolerance": "±0.10mm",
      "focal_length_tolerance": "±1%",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4 @ 632.8nm",
      "centration": "<3 arc min",
      "clear_aperture": ">90%",
      "beveling": "0.25mm × 45°",
      "coatings": "A: AR 350-650nm / B: AR 650-950nm / C: AR 950-1250nm"
    },
    "partNumbers": [
      {
        "partNumber": "LOBCXB6-6",
        "diameter": "6.00mm",
        "focalLength": "6.00mm",
        "centerThickness": "2.50mm",
        "price": 18
      },
      {
        "partNumber": "LOBCXB6-10",
        "diameter": "6.00mm",
        "focalLength": "10.00mm",
        "centerThickness": "2.40mm",
        "price": 18
      },
      {
        "partNumber": "LOBCXB9-12",
        "diameter": "9.00mm",
        "focalLength": "12.00mm",
        "centerThickness": "3.60mm",
        "price": 20
      },
      {
        "partNumber": "LOBCXB10-15",
        "diameter": "10.00mm",
        "focalLength": "15.00mm",
        "centerThickness": "4.10mm",
        "price": 22
      },
      {
        "partNumber": "LOBCXB12.7-15",
        "diameter": "12.70mm",
        "focalLength": "15.00mm",
        "centerThickness": "4.70mm",
        "price": 25
      },
      {
        "partNumber": "LOBCXB12.7-20",
        "diameter": "12.70mm",
        "focalLength": "20.00mm",
        "centerThickness": "3.88mm",
        "price": 25
      },
      {
        "partNumber": "LOBCXB12.7-30",
        "diameter": "12.70mm",
        "focalLength": "30.00mm",
        "centerThickness": "3.14mm",
        "price": 25
      },
      {
        "partNumber": "LOBCXB15-25",
        "diameter": "15.00mm",
        "focalLength": "25.00mm",
        "centerThickness": "4.80mm",
        "price": 30
      },
      {
        "partNumber": "LOBCXB20-45",
        "diameter": "20.00mm",
        "focalLength": "45.00mm",
        "centerThickness": "8.00mm",
        "price": 38
      },
      {
        "partNumber": "LOBCXB25.4-50",
        "diameter": "25.40mm",
        "focalLength": "50.00mm",
        "centerThickness": "5.24mm",
        "price": 42
      }
    ],
    "price": 18,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 20,
    "name": "BK7 Half Ball Lenses",
    "nameZh": "BK7半球透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Economical BK7 half-ball lenses for fiber coupling and light homogenization. Suitable for visible light applications with excellent cost-performance ratio.",
    "image": "images/products/optical-lenses/bk7-half-ball-lenses.jpg",
    "parameters": {
      "material": "K9/BK7",
      "diameter": "1-10mm",
      "wavelength_range": "350-2000nm",
      "surface_quality": "40-20",
      "clear_aperture": ">85%"
    },
    "price": 10,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 21,
    "name": "BK7 Optical Ball Lenses",
    "nameZh": "BK7光学球透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Standard BK7 ball lenses for fiber coupling and optical fiber illumination. Available in various diameters for different fiber core sizes.",
    "image": "images/products/optical-lenses/bk7-optical-ball-lenses.jpg",
    "parameters": {
      "material": "K9/BK7",
      "diameter": "0.5-20mm",
      "wavelength_range": "350-2000nm",
      "surface_quality": "40-20",
      "clear_aperture": ">90%"
    },
    "price": 10,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 22,
    "name": "BK7 Plano Concave Lenses",
    "nameZh": "BK7平凹透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Plano-concave lenses have a negative focal length. When parallel light passes through plano-concave lenses, it diverges. Our lenses feature excellent uniformity, no patterns, inclusions, or bubbles. Ideal for beam expanders and light projection systems.",
    "image": "images/products/optical-lenses/bk7-plano-concave-lenses.jpg",
    "parameters": {
      "material": "K9 (BK7)",
      "diameter_tolerance": "±0.15mm",
      "thickness_tolerance": "±0.10mm",
      "focal_length_tolerance": "±1%",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4 @ 632.8nm",
      "centration": "<3 arc min",
      "clear_aperture": ">90%",
      "beveling": "0.25mm × 45°",
      "coatings": "A: AR 350-650nm / B: AR 650-950nm / C: AR 950-1250nm"
    },
    "partNumbers": [
      {
        "partNumber": "LOPCCB6-6",
        "diameter": "6.00mm",
        "focalLength": "-6.00mm",
        "centerThickness": "2.00mm",
        "price": 15
      },
      {
        "partNumber": "LOPCCB6-10",
        "diameter": "6.00mm",
        "focalLength": "-10.00mm",
        "centerThickness": "2.00mm",
        "price": 15
      },
      {
        "partNumber": "LOPCCB10-15",
        "diameter": "10.00mm",
        "focalLength": "-15.00mm",
        "centerThickness": "2.00mm",
        "price": 18
      },
      {
        "partNumber": "LOPCCB10-25",
        "diameter": "10.00mm",
        "focalLength": "-25.00mm",
        "centerThickness": "2.00mm",
        "price": 18
      },
      {
        "partNumber": "LOPCCB12.7-19",
        "diameter": "12.70mm",
        "focalLength": "-19.00mm",
        "centerThickness": "1.70mm",
        "price": 20
      },
      {
        "partNumber": "LOPCCB12.7-25.4",
        "diameter": "12.70mm",
        "focalLength": "-25.40mm",
        "centerThickness": "3.00mm",
        "price": 22
      },
      {
        "partNumber": "LOPCCB12.7-50",
        "diameter": "12.70mm",
        "focalLength": "-50.00mm",
        "centerThickness": "2.50mm",
        "price": 22
      },
      {
        "partNumber": "LOPCCB15-25",
        "diameter": "15.00mm",
        "focalLength": "-25.00mm",
        "centerThickness": "2.00mm",
        "price": 25
      },
      {
        "partNumber": "LOPCCB20-50",
        "diameter": "20.00mm",
        "focalLength": "-50.00mm",
        "centerThickness": "2.00mm",
        "price": 28
      },
      {
        "partNumber": "LOPCCB25.4-25",
        "diameter": "25.40mm",
        "focalLength": "-25.00mm",
        "centerThickness": "2.50mm",
        "price": 32
      }
    ],
    "price": 15,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 23,
    "name": "BK7 Plano Convex Cylindrical Lenses",
    "nameZh": "BK7平凸柱面透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Standard plano-convex cylindrical lenses for generating line-shaped beams and one-dimensional focusing. Widely used in laser scanning, spectroscopy, and optical metrology.",
    "image": "images/products/optical-lenses/bk7-plano-convex-cylindrical-lenses.jpg",
    "parameters": {
      "material": "K9/BK7",
      "diameter": "6-100mm",
      "focal_length": "20-300mm",
      "coating": "Uncoated / AR coating",
      "surface_quality": "40-20"
    },
    "price": 22,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 24,
    "name": "BK7 Plano Convex Lenses",
    "nameZh": "BK7平凸透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Plano-convex lenses have a positive focal length and are widely used for focusing and collimating light beams. The curved surface minimizes spherical aberration for better beam quality. Our BK7 Plano Convex Lenses feature excellent uniformity, no patterns, inclusions, or bubbles. Custom coatings available upon request.",
    "image": "images/products/optical-lenses/bk7-plano-convex-lenses.jpg",
    "parameters": {
      "material": "K9 (BK7)",
      "diameter_tolerance": "±0.15mm",
      "thickness_tolerance": "±0.10mm",
      "focal_length_tolerance": "±1%",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4 @ 632.8nm",
      "centration": "<3 arc min",
      "clear_aperture": ">90%",
      "beveling": "0.25mm × 45°",
      "coatings": "A: AR 350-650nm / B: AR 650-950nm / C: AR 950-1250nm"
    },
    "partNumbers": [
      {
        "partNumber": "LOPCXB2.5-3.9",
        "diameter": "2.50mm",
        "focalLength": "3.90mm",
        "centerThickness": "1.95mm",
        "price": 18
      },
      {
        "partNumber": "LOPCXB2.8-5.0",
        "diameter": "2.80mm",
        "focalLength": "5.00mm",
        "centerThickness": "1.62mm",
        "price": 18
      },
      {
        "partNumber": "LOPCXB3.0-8.0",
        "diameter": "3.00mm",
        "focalLength": "8.00mm",
        "centerThickness": "2.00mm",
        "price": 18
      },
      {
        "partNumber": "LOPCXB4.0-8.0",
        "diameter": "4.00mm",
        "focalLength": "8.00mm",
        "centerThickness": "2.00mm",
        "price": 20
      },
      {
        "partNumber": "LOPCXB5.0-10",
        "diameter": "5.00mm",
        "focalLength": "10.00mm",
        "centerThickness": "2.00mm",
        "price": 20
      },
      {
        "partNumber": "LOPCXB6.0-8.0",
        "diameter": "6.00mm",
        "focalLength": "8.00mm",
        "centerThickness": "2.30mm",
        "price": 22
      },
      {
        "partNumber": "LOPCXB6.0-12",
        "diameter": "6.00mm",
        "focalLength": "12.00mm",
        "centerThickness": "2.28mm",
        "price": 22
      },
      {
        "partNumber": "LOPCXB8.0-15",
        "diameter": "8.00mm",
        "focalLength": "15.00mm",
        "centerThickness": "3.00mm",
        "price": 25
      },
      {
        "partNumber": "LOPCXB10-15",
        "diameter": "10.00mm",
        "focalLength": "15.00mm",
        "centerThickness": "3.80mm",
        "price": 28
      },
      {
        "partNumber": "LOPCXB12.7-19",
        "diameter": "12.70mm",
        "focalLength": "19.00mm",
        "centerThickness": "4.80mm",
        "price": 35
      }
    ],
    "price": 18,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 25,
    "name": "Laser beam extender",
    "nameZh": "激光扩束器",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Precision laser beam expanders for increasing beam diameter while maintaining collimation. Available in Galilean and Keplerian designs with various magnification ratios.",
    "image": "images/products/optical-lenses/laser-beam-extender.jpg",
    "parameters": {
      "material": "N-BK7 / Fused Silica",
      "magnification": "2X, 3X, 5X, 10X, 20X",
      "wavelength_range": "532nm / 632.8nm / 1064nm / Custom",
      "input_aperture": "5-30mm",
      "surface_quality": "20-10",
      "damage_threshold": ">10 J/cm² (10ns)"
    },
    "price": 250,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOLLM20-532",
        "wavelength": "532nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 55
      },
      {
        "partNumber": "LOLLM25.4-532",
        "wavelength": "532nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 68
      },
      {
        "partNumber": "LOLLM30-532",
        "wavelength": "532nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 78
      },
      {
        "partNumber": "LOLLM20-1064",
        "wavelength": "1064nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 55
      },
      {
        "partNumber": "LOLLM25.4-1064",
        "wavelength": "1064nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 68
      },
      {
        "partNumber": "LOLLM30-1064",
        "wavelength": "1064nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 78
      },
      {
        "partNumber": "LOLLM35-1064",
        "wavelength": "1064nm",
        "diameter": "35mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 88
      },
      {
        "partNumber": "LOLLM50-1064",
        "wavelength": "1064nm",
        "diameter": "50mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 110
      },
      {
        "partNumber": "LOLLM20-355",
        "wavelength": "355nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 65
      },
      {
        "partNumber": "LOLLM30-355",
        "wavelength": "355nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 85
      },
      {
        "partNumber": "LOLLM25.4-1550",
        "wavelength": "1550nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 85
      }
    ]
  },
  {
    "id": 26,
    "name": "Micro Objectives",
    "nameZh": "显微物镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Precision microscope objectives for biological and industrial microscopy applications. Available in various magnification powers and correction levels.",
    "image": "images/products/optical-lenses/micro-objectives.jpg",
    "parameters": {
      "magnification": "4X, 10X, 20X, 40X, 60X, 100X",
      "numerical_aperture": "0.10-1.25",
      "working_distance": "0.1-10mm",
      "thread": "RMS / M25 / Custom",
      "correction": "Achromatic / Plan Achromatic"
    },
    "price": 180,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOOL-X4",
        "magnification": "4x",
        "na": "0.10",
        "workingDistance": "15.5mm",
        "price": 85
      },
      {
        "partNumber": "LOOL-X10",
        "magnification": "10x",
        "na": "0.25",
        "workingDistance": "6.3mm",
        "price": 95
      },
      {
        "partNumber": "LOOL-X20",
        "magnification": "20x",
        "na": "0.40",
        "workingDistance": "1.2mm",
        "price": 115
      },
      {
        "partNumber": "LOOL-X40",
        "magnification": "40x",
        "na": "0.65",
        "workingDistance": "0.44mm",
        "price": 135
      },
      {
        "partNumber": "LOOL-X60",
        "magnification": "60x",
        "na": "0.85",
        "workingDistance": "0.185mm",
        "price": 165
      },
      {
        "partNumber": "LOOL-X100",
        "magnification": "100x",
        "na": "1.25",
        "workingDistance": "0.198mm",
        "price": 195
      }
    ]
  },
  {
    "id": 27,
    "name": "Optical Aspheric Lenses",
    "nameZh": "非球面透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Precision molded aspheric lenses eliminating spherical aberration for superior focusing performance. Ideal for laser diode collimation, LED coupling, and imaging systems.",
    "image": "images/products/optical-lenses/optical-aspheric-lenses.jpg",
    "parameters": {
      "material": "N-BK7 / Fused Silica / PMMA",
      "diameter": "3-50mm",
      "focal_length": "3-100mm",
      "numerical_aperture": "Up to 0.80",
      "surface_quality": "40-20",
      "coating": "AR coating available"
    },
    "price": 40,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 28,
    "name": "Broadband Dielectric Coated Mirrors",
    "nameZh": "宽带介电镀膜反射镜",
    "category": "Optical Mirrors",
    "categoryZh": "光学反射镜",
    "description": "High-reflectivity dielectric mirrors with broad spectral bandwidth. Multi-layer coating technology provides >99% reflectivity across visible and near-infrared regions.",
    "image": "images/products/optical-mirrors/broadband-dielectric-coated-mirrors.jpg",
    "parameters": {
      "substrate": "N-BK7 / Fused Silica",
      "diameter": "12.7-50.8mm",
      "reflectivity": ">99% (400-700nm) / >98% (650-1050nm)",
      "surface_flatness": "λ/4@632.8nm",
      "surface_quality": "40-20",
      "damage_threshold": ">20 J/cm² (10ns)"
    },
    "price": 45,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LODM12.7-3A1",
        "wavelength": "400-700nm",
        "diameter": "12.70mm",
        "thickness": "3mm",
        "price": 45
      },
      {
        "partNumber": "LODM20-3A1",
        "wavelength": "400-700nm",
        "diameter": "20.00mm",
        "thickness": "3mm",
        "price": 55
      },
      {
        "partNumber": "LODM25.4-3A1",
        "wavelength": "400-700nm",
        "diameter": "25.40mm",
        "thickness": "3mm",
        "price": 65
      },
      {
        "partNumber": "LODM30-5A1",
        "wavelength": "400-700nm",
        "diameter": "30.00mm",
        "thickness": "5mm",
        "price": 78
      },
      {
        "partNumber": "LODM40-5A1",
        "wavelength": "400-700nm",
        "diameter": "40.00mm",
        "thickness": "5mm",
        "price": 95
      },
      {
        "partNumber": "LODM50-5A1",
        "wavelength": "400-700nm",
        "diameter": "50.00mm",
        "thickness": "5mm",
        "price": 115
      },
      {
        "partNumber": "LODM12.7-31A2",
        "wavelength": "650-1050nm",
        "diameter": "12.70mm",
        "thickness": "3mm",
        "price": 48
      },
      {
        "partNumber": "LODM25.4-31A2",
        "wavelength": "650-1050nm",
        "diameter": "25.40mm",
        "thickness": "3mm",
        "price": 68
      },
      {
        "partNumber": "LODM12.7-3A3",
        "wavelength": "400-1100nm",
        "diameter": "12.70mm",
        "thickness": "3mm",
        "price": 48
      },
      {
        "partNumber": "LODM25.4-4A3",
        "wavelength": "400-1100nm",
        "diameter": "25.40mm",
        "thickness": "5mm",
        "price": 72
      }
    ]
  },
  {
    "id": 29,
    "name": "Dielectric Dual Wavelength Laser Line Mirrors",
    "nameZh": "双波长介电激光线反射镜",
    "category": "Optical Mirrors",
    "categoryZh": "光学反射镜",
    "description": "Specialized mirrors optimized for dual wavelength laser systems. Perfect for dual-frequency laser applications, interferometry, and harmonic generation.",
    "image": "images/products/optical-mirrors/dielectric-dual-wavelength-laser-line-mirrors.jpg",
    "parameters": {
      "substrate": "N-BK7 / Fused Silica",
      "diameter": "12.7-50.8mm",
      "wavelength_range": "532nm+1064nm / 1064nm+1550nm / Custom",
      "reflectivity": ">99.5% at each wavelength",
      "surface_flatness": "λ/10@632.8nm",
      "surface_quality": "20-10"
    },
    "price": 65,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOLLM20-532",
        "wavelength": "532nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 55
      },
      {
        "partNumber": "LOLLM25.4-532",
        "wavelength": "532nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 68
      },
      {
        "partNumber": "LOLLM30-532",
        "wavelength": "532nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 78
      },
      {
        "partNumber": "LOLLM20-1064",
        "wavelength": "1064nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 55
      },
      {
        "partNumber": "LOLLM25.4-1064",
        "wavelength": "1064nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 68
      },
      {
        "partNumber": "LOLLM30-1064",
        "wavelength": "1064nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 78
      },
      {
        "partNumber": "LOLLM35-1064",
        "wavelength": "1064nm",
        "diameter": "35mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 88
      },
      {
        "partNumber": "LOLLM50-1064",
        "wavelength": "1064nm",
        "diameter": "50mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 110
      },
      {
        "partNumber": "LOLLM20-355",
        "wavelength": "355nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 65
      },
      {
        "partNumber": "LOLLM30-355",
        "wavelength": "355nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 85
      },
      {
        "partNumber": "LOLLM25.4-1550",
        "wavelength": "1550nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 85
      }
    ]
  },
  {
    "id": 30,
    "name": "Dielectric Laser Line Mirrors",
    "nameZh": "介电激光线反射镜",
    "category": "Optical Mirrors",
    "categoryZh": "光学反射镜",
    "description": "Laser line mirrors optimized for specific wavelengths with high reflectivity and damage threshold. Essential for laser resonator cavities and beam steering.",
    "image": "images/products/optical-mirrors/dielectric-laser-line-mirrors.jpg",
    "parameters": {
      "substrate": "N-BK7 / Fused Silica",
      "diameter": "12.7-50.8mm",
      "wavelength_range": "355nm / 532nm / 633nm / 1064nm / Custom",
      "reflectivity": ">99.5% (R-pol / S-pol)",
      "surface_flatness": "λ/10@632.8nm",
      "surface_quality": "20-10",
      "damage_threshold": ">10 J/cm² (10ns)"
    },
    "price": 40,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOLLM20-532",
        "wavelength": "532nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 55
      },
      {
        "partNumber": "LOLLM25.4-532",
        "wavelength": "532nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 68
      },
      {
        "partNumber": "LOLLM30-532",
        "wavelength": "532nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 78
      },
      {
        "partNumber": "LOLLM20-1064",
        "wavelength": "1064nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 55
      },
      {
        "partNumber": "LOLLM25.4-1064",
        "wavelength": "1064nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 68
      },
      {
        "partNumber": "LOLLM30-1064",
        "wavelength": "1064nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 78
      },
      {
        "partNumber": "LOLLM35-1064",
        "wavelength": "1064nm",
        "diameter": "35mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 88
      },
      {
        "partNumber": "LOLLM50-1064",
        "wavelength": "1064nm",
        "diameter": "50mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 110
      },
      {
        "partNumber": "LOLLM20-355",
        "wavelength": "355nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 65
      },
      {
        "partNumber": "LOLLM30-355",
        "wavelength": "355nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 85
      },
      {
        "partNumber": "LOLLM25.4-1550",
        "wavelength": "1550nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 85
      }
    ]
  },
  {
    "id": 31,
    "name": "Metal Coated  Concave Spherical Reflected Mirrors",
    "nameZh": "金属镀膜凹球面反射镜",
    "category": "Optical Mirrors",
    "categoryZh": "光学反射镜",
    "description": "Precision concave spherical mirrors with metal coatings for broadband reflection. Available with aluminum, silver, or gold coatings for different spectral regions.",
    "image": "images/products/optical-mirrors/metal-coated--concave-spherical-reflected-mirrors.jpg",
    "parameters": {
      "substrate": "N-BK7 / Fused Silica",
      "diameter": "10-200mm",
      "radius_of_curvature": "25-2000mm",
      "coating": "Al + SiO2 / Ag + SiO2 / Au",
      "reflectivity": ">90% (Al) / >95% (Ag) / >98% (Au)",
      "surface_flatness": "λ/4@632.8nm"
    },
    "price": 35,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOAUM12.7-3",
        "wavelength": "800-2000nm",
        "diameter": "12.70mm",
        "thickness": "3mm",
        "reflectance": ">98%",
        "price": 52
      },
      {
        "partNumber": "LOAUM25.4-3",
        "wavelength": "800-2000nm",
        "diameter": "25.40mm",
        "thickness": "3mm",
        "reflectance": ">98%",
        "price": 72
      },
      {
        "partNumber": "LOAUM30-5",
        "wavelength": "800-2000nm",
        "diameter": "30.00mm",
        "thickness": "5mm",
        "reflectance": ">98%",
        "price": 88
      },
      {
        "partNumber": "LOAUM50-5",
        "wavelength": "800-2000nm",
        "diameter": "50.00mm",
        "thickness": "5mm",
        "reflectance": ">98%",
        "price": 115
      }
    ]
  },
  {
    "id": 32,
    "name": "NdYAG Laser Output Coupler",
    "nameZh": "Nd:YAG激光输出耦合器",
    "category": "Optical Mirrors",
    "categoryZh": "光学反射镜",
    "description": "Specialized output couplers for Nd:YAG laser systems with optimized transmission at 1064nm. Partial reflector design balances output power and laser efficiency.",
    "image": "images/products/optical-mirrors/ndyag-laser-output-coupler.jpg",
    "parameters": {
      "substrate": "N-BK7 / Fused Silica",
      "diameter": "12.7-50.8mm",
      "wavelength": "1064nm / 532nm",
      "transmittance": "5-30% (at laser wavelength)",
      "surface_flatness": "λ/10@632.8nm",
      "damage_threshold": ">15 J/cm² (10ns)"
    },
    "price": 85,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOLLM20-532",
        "wavelength": "532nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 55
      },
      {
        "partNumber": "LOLLM25.4-532",
        "wavelength": "532nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 68
      },
      {
        "partNumber": "LOLLM30-532",
        "wavelength": "532nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 78
      },
      {
        "partNumber": "LOLLM20-1064",
        "wavelength": "1064nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 55
      },
      {
        "partNumber": "LOLLM25.4-1064",
        "wavelength": "1064nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 68
      },
      {
        "partNumber": "LOLLM30-1064",
        "wavelength": "1064nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 78
      },
      {
        "partNumber": "LOLLM35-1064",
        "wavelength": "1064nm",
        "diameter": "35mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 88
      },
      {
        "partNumber": "LOLLM50-1064",
        "wavelength": "1064nm",
        "diameter": "50mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 110
      },
      {
        "partNumber": "LOLLM20-355",
        "wavelength": "355nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 65
      },
      {
        "partNumber": "LOLLM30-355",
        "wavelength": "355nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 85
      },
      {
        "partNumber": "LOLLM25.4-1550",
        "wavelength": "1550nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 85
      }
    ]
  },
  {
    "id": 33,
    "name": "Optical Dichroic Mirrors",
    "nameZh": "二向色镜",
    "category": "Optical Mirrors",
    "categoryZh": "光学反射镜",
    "description": "Precision dichroic mirrors for separating or combining beams of different wavelengths. Multi-layer dielectric coating provides sharp cut-off and high transmission.",
    "image": "images/products/optical-mirrors/optical-dichroic-mirrors.jpg",
    "parameters": {
      "substrate": "N-BK7",
      "diameter": "12.7-50.8mm",
      "wavelength_range": "400-1100nm",
      "reflectivity": ">95% (design wavelength)",
      "transmittance": ">90% (other wavelengths)",
      "surface_quality": "40-20"
    },
    "price": 55,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 34,
    "name": "Optical Enhanced Aluminum Coated Mirrors",
    "nameZh": "增强铝镀膜反射镜",
    "category": "Optical Mirrors",
    "categoryZh": "光学反射镜",
    "description": "Enhanced aluminum mirrors with improved reflectivity in the visible spectrum. SiO2 protective coating ensures long-term durability and environmental stability.",
    "image": "images/products/optical-mirrors/optical-enhanced-aluminum-coated-mirrors.jpg",
    "parameters": {
      "substrate": "N-BK7 / Float Glass",
      "diameter": "10-200mm",
      "reflectivity": ">92% (400-700nm)",
      "coating": "Al + SiO2 (enhanced)",
      "surface_flatness": "λ/4@632.8nm",
      "surface_quality": "40-20"
    },
    "price": 28,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOEAM12.7-3",
        "wavelength": "400-700nm",
        "diameter": "12.70mm",
        "thickness": "3mm",
        "reflectance": ">90%",
        "price": 42
      },
      {
        "partNumber": "LOEAM25.4-3",
        "wavelength": "400-700nm",
        "diameter": "25.40mm",
        "thickness": "3mm",
        "reflectance": ">90%",
        "price": 58
      },
      {
        "partNumber": "LOEAM30-5",
        "wavelength": "400-700nm",
        "diameter": "30.00mm",
        "thickness": "5mm",
        "reflectance": ">90%",
        "price": 72
      },
      {
        "partNumber": "LOEAM50-5",
        "wavelength": "400-700nm",
        "diameter": "50.00mm",
        "thickness": "5mm",
        "reflectance": ">90%",
        "price": 98
      }
    ]
  },
  {
    "id": 35,
    "name": "Optical Gold Mirrors",
    "nameZh": "金反射镜",
    "category": "Optical Mirrors",
    "categoryZh": "光学反射镜",
    "description": "High-reflectivity gold mirrors for infrared applications. Protected gold coating provides excellent reflectivity in the 650nm-20μm range with superior durability.",
    "image": "images/products/optical-mirrors/optical-gold-mirrors.jpg",
    "parameters": {
      "substrate": "N-BK7 / Fused Silica",
      "diameter": "10-100mm",
      "reflectivity": ">98% (650-1600nm) / >95% (2-10μm)",
      "coating": "Au + SiO2 protective",
      "surface_flatness": "λ/4@632.8nm",
      "surface_quality": "40-20"
    },
    "price": 60,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOAUM12.7-3",
        "wavelength": "800-2000nm",
        "diameter": "12.70mm",
        "thickness": "3mm",
        "reflectance": ">98%",
        "price": 52
      },
      {
        "partNumber": "LOAUM25.4-3",
        "wavelength": "800-2000nm",
        "diameter": "25.40mm",
        "thickness": "3mm",
        "reflectance": ">98%",
        "price": 72
      },
      {
        "partNumber": "LOAUM30-5",
        "wavelength": "800-2000nm",
        "diameter": "30.00mm",
        "thickness": "5mm",
        "reflectance": ">98%",
        "price": 88
      },
      {
        "partNumber": "LOAUM50-5",
        "wavelength": "800-2000nm",
        "diameter": "50.00mm",
        "thickness": "5mm",
        "reflectance": ">98%",
        "price": 115
      }
    ]
  },
  {
    "id": 36,
    "name": "Optical Protective Aluminum Coated Mirrors",
    "nameZh": "保护铝镀膜反射镜",
    "category": "Optical Mirrors",
    "categoryZh": "光学反射镜",
    "description": "Standard aluminum mirrors with SiO2 protective coating for improved durability. Cost-effective solution for general-purpose beam steering applications.",
    "image": "images/products/optical-mirrors/optical-protective-aluminum-coated-mirrors.jpg",
    "parameters": {
      "substrate": "Float Glass / N-BK7",
      "diameter": "10-200mm",
      "reflectivity": ">90% (400-700nm)",
      "coating": "Al + SiO2 protective",
      "surface_flatness": "λ/4@632.8nm",
      "surface_quality": "40-20"
    },
    "price": 25,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 37,
    "name": "Optical Silver Mirrors",
    "nameZh": "银反射镜",
    "category": "Optical Mirrors",
    "categoryZh": "光学反射镜",
    "description": "High-reflectivity silver mirrors with excellent visible light performance. Protected silver coating prevents tarnishing and ensures long-term stability.",
    "image": "images/products/optical-mirrors/optical-silver-mirrors.jpg",
    "parameters": {
      "substrate": "N-BK7 / Float Glass",
      "diameter": "10-150mm",
      "reflectivity": ">95% (400-800nm) / >90% (400-2000nm)",
      "coating": "Ag + SiO2 protective",
      "surface_flatness": "λ/4@632.8nm",
      "surface_quality": "40-20"
    },
    "price": 35,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOAGM12.7-3",
        "wavelength": "400-2000nm",
        "diameter": "12.70mm",
        "thickness": "3mm",
        "reflectance": ">95%",
        "price": 48
      },
      {
        "partNumber": "LOAGM25.4-3",
        "wavelength": "400-2000nm",
        "diameter": "25.40mm",
        "thickness": "3mm",
        "reflectance": ">95%",
        "price": 65
      },
      {
        "partNumber": "LOAGM30-5",
        "wavelength": "400-2000nm",
        "diameter": "30.00mm",
        "thickness": "5mm",
        "reflectance": ">95%",
        "price": 78
      },
      {
        "partNumber": "LOAGM50-5",
        "wavelength": "400-2000nm",
        "diameter": "50.00mm",
        "thickness": "5mm",
        "reflectance": ">95%",
        "price": 105
      }
    ]
  },
  {
    "id": 38,
    "name": "Air Spaced Zero Order high power Waveplates",
    "nameZh": "气隙零级高功率波片",
    "category": "Optical Polarising Components",
    "categoryZh": "光学偏振组件",
    "description": "Zero-order wave plates with air gap design for high-power laser applications. Superior temperature bandwidth and damage threshold compared to cemented designs.",
    "image": "images/products/optical-polarising-components/air-spaced-zero-order-high-power-waveplates.jpg",
    "parameters": {
      "material": "Crystal Quartz",
      "diameter": "12.7-50.8mm",
      "wavelength_range": "532nm / 633nm / 1064nm / Custom",
      "retardation": "λ/2 / λ/4",
      "surface_quality": "20-10",
      "damage_threshold": ">10 J/cm² (10ns)"
    },
    "price": 95,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOWPZ-10Q-532",
        "diameter": "10.00mm",
        "wavelength": "532nm",
        "phase": "Quarter Wave",
        "price": 95
      },
      {
        "partNumber": "LOWPZ-10H-532",
        "diameter": "10.00mm",
        "wavelength": "532nm",
        "phase": "Half Wave",
        "price": 100
      },
      {
        "partNumber": "LOWPZ-12.7Q-532",
        "diameter": "12.70mm",
        "wavelength": "532nm",
        "phase": "Quarter Wave",
        "price": 115
      },
      {
        "partNumber": "LOWPZ-12.7H-532",
        "diameter": "12.70mm",
        "wavelength": "532nm",
        "phase": "Half Wave",
        "price": 120
      },
      {
        "partNumber": "LOWPZ-20Q-532",
        "diameter": "20.00mm",
        "wavelength": "532nm",
        "phase": "Quarter Wave",
        "price": 145
      },
      {
        "partNumber": "LOWPZ-20H-532",
        "diameter": "20.00mm",
        "wavelength": "532nm",
        "phase": "Half Wave",
        "price": 150
      },
      {
        "partNumber": "LOWPZ-25.4Q-532",
        "diameter": "25.40mm",
        "wavelength": "532nm",
        "phase": "Quarter Wave",
        "price": 175
      },
      {
        "partNumber": "LOWPZ-25.4H-532",
        "diameter": "25.40mm",
        "wavelength": "532nm",
        "phase": "Half Wave",
        "price": 180
      },
      {
        "partNumber": "LOWPZ-10Q-1064",
        "diameter": "10.00mm",
        "wavelength": "1064nm",
        "phase": "Quarter Wave",
        "price": 100
      },
      {
        "partNumber": "LOWPZ-10H-1064",
        "diameter": "10.00mm",
        "wavelength": "1064nm",
        "phase": "Half Wave",
        "price": 105
      },
      {
        "partNumber": "LOWPZ-12.7Q-1064",
        "diameter": "12.70mm",
        "wavelength": "1064nm",
        "phase": "Quarter Wave",
        "price": 120
      },
      {
        "partNumber": "LOWPZ-12.7H-1064",
        "diameter": "12.70mm",
        "wavelength": "1064nm",
        "phase": "Half Wave",
        "price": 125
      },
      {
        "partNumber": "LOWPZ-20Q-1064",
        "diameter": "20.00mm",
        "wavelength": "1064nm",
        "phase": "Quarter Wave",
        "price": 155
      },
      {
        "partNumber": "LOWPZ-20H-1064",
        "diameter": "20.00mm",
        "wavelength": "1064nm",
        "phase": "Half Wave",
        "price": 160
      },
      {
        "partNumber": "LOWPZ-25.4Q-1064",
        "diameter": "25.40mm",
        "wavelength": "1064nm",
        "phase": "Quarter Wave",
        "price": 185
      },
      {
        "partNumber": "LOWPZ-25.4H-1064",
        "diameter": "25.40mm",
        "wavelength": "1064nm",
        "phase": "Half Wave",
        "price": 190
      }
    ]
  },
  {
    "id": 39,
    "name": "Cemented Zero Order Waveplate",
    "nameZh": "胶合零级波片",
    "category": "Optical Polarising Components",
    "categoryZh": "光学偏振组件",
    "description": "Cost-effective zero-order wave plates with optical contact cementing. Suitable for moderate power applications with excellent retardation accuracy.",
    "image": "images/products/optical-polarising-components/cemented-zero-order-waveplate.jpg",
    "parameters": {
      "material": "Crystal Quartz",
      "diameter": "12.7-50.8mm",
      "wavelength_range": "532nm / 633nm / 1064nm / Custom",
      "retardation": "λ/2 / λ/4",
      "surface_quality": "40-20",
      "damage_threshold": ">5 J/cm² (10ns)"
    },
    "price": 65,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOWPZ-10Q-532",
        "diameter": "10.00mm",
        "wavelength": "532nm",
        "phase": "Quarter Wave",
        "price": 95
      },
      {
        "partNumber": "LOWPZ-10H-532",
        "diameter": "10.00mm",
        "wavelength": "532nm",
        "phase": "Half Wave",
        "price": 100
      },
      {
        "partNumber": "LOWPZ-12.7Q-532",
        "diameter": "12.70mm",
        "wavelength": "532nm",
        "phase": "Quarter Wave",
        "price": 115
      },
      {
        "partNumber": "LOWPZ-12.7H-532",
        "diameter": "12.70mm",
        "wavelength": "532nm",
        "phase": "Half Wave",
        "price": 120
      },
      {
        "partNumber": "LOWPZ-20Q-532",
        "diameter": "20.00mm",
        "wavelength": "532nm",
        "phase": "Quarter Wave",
        "price": 145
      },
      {
        "partNumber": "LOWPZ-20H-532",
        "diameter": "20.00mm",
        "wavelength": "532nm",
        "phase": "Half Wave",
        "price": 150
      },
      {
        "partNumber": "LOWPZ-25.4Q-532",
        "diameter": "25.40mm",
        "wavelength": "532nm",
        "phase": "Quarter Wave",
        "price": 175
      },
      {
        "partNumber": "LOWPZ-25.4H-532",
        "diameter": "25.40mm",
        "wavelength": "532nm",
        "phase": "Half Wave",
        "price": 180
      },
      {
        "partNumber": "LOWPZ-10Q-1064",
        "diameter": "10.00mm",
        "wavelength": "1064nm",
        "phase": "Quarter Wave",
        "price": 100
      },
      {
        "partNumber": "LOWPZ-10H-1064",
        "diameter": "10.00mm",
        "wavelength": "1064nm",
        "phase": "Half Wave",
        "price": 105
      },
      {
        "partNumber": "LOWPZ-12.7Q-1064",
        "diameter": "12.70mm",
        "wavelength": "1064nm",
        "phase": "Quarter Wave",
        "price": 120
      },
      {
        "partNumber": "LOWPZ-12.7H-1064",
        "diameter": "12.70mm",
        "wavelength": "1064nm",
        "phase": "Half Wave",
        "price": 125
      },
      {
        "partNumber": "LOWPZ-20Q-1064",
        "diameter": "20.00mm",
        "wavelength": "1064nm",
        "phase": "Quarter Wave",
        "price": 155
      },
      {
        "partNumber": "LOWPZ-20H-1064",
        "diameter": "20.00mm",
        "wavelength": "1064nm",
        "phase": "Half Wave",
        "price": 160
      },
      {
        "partNumber": "LOWPZ-25.4Q-1064",
        "diameter": "25.40mm",
        "wavelength": "1064nm",
        "phase": "Quarter Wave",
        "price": 185
      },
      {
        "partNumber": "LOWPZ-25.4H-1064",
        "diameter": "25.40mm",
        "wavelength": "1064nm",
        "phase": "Half Wave",
        "price": 190
      }
    ]
  },
  {
    "id": 40,
    "name": "Multi Order Waveplate",
    "nameZh": "多级波片",
    "category": "Optical Polarising Components",
    "categoryZh": "光学偏振组件",
    "description": "Multi-order wave plates offering cost-effective polarization control. Lower price with wider temperature and wavelength bandwidth compared to zero-order designs.",
    "image": "images/products/optical-polarising-components/multi-order-waveplate.jpg",
    "parameters": {
      "material": "Crystal Quartz / MgF2",
      "diameter": "12.7-50.8mm",
      "wavelength_range": "400-1600nm",
      "retardation": "λ/2 / λ/4 (multi-order)",
      "surface_quality": "40-20",
      "damage_threshold": ">3 J/cm² (10ns)"
    },
    "price": 35,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOWPM-10Q-532",
        "diameter": "10.00mm",
        "wavelength": "532nm",
        "phase": "Quarter Wave",
        "price": 45
      },
      {
        "partNumber": "LOWPM-10H-532",
        "diameter": "10.00mm",
        "wavelength": "532nm",
        "phase": "Half Wave",
        "price": 48
      },
      {
        "partNumber": "LOWPM-12.7Q-532",
        "diameter": "12.70mm",
        "wavelength": "532nm",
        "phase": "Quarter Wave",
        "price": 55
      },
      {
        "partNumber": "LOWPM-12.7H-532",
        "diameter": "12.70mm",
        "wavelength": "532nm",
        "phase": "Half Wave",
        "price": 58
      },
      {
        "partNumber": "LOWPM-20Q-532",
        "diameter": "20.00mm",
        "wavelength": "532nm",
        "phase": "Quarter Wave",
        "price": 72
      },
      {
        "partNumber": "LOWPM-20H-532",
        "diameter": "20.00mm",
        "wavelength": "532nm",
        "phase": "Half Wave",
        "price": 75
      },
      {
        "partNumber": "LOWPM-25.4Q-532",
        "diameter": "25.40mm",
        "wavelength": "532nm",
        "phase": "Quarter Wave",
        "price": 88
      },
      {
        "partNumber": "LOWPM-25.4H-532",
        "diameter": "25.40mm",
        "wavelength": "532nm",
        "phase": "Half Wave",
        "price": 92
      },
      {
        "partNumber": "LOWPM-10Q-1064",
        "diameter": "10.00mm",
        "wavelength": "1064nm",
        "phase": "Quarter Wave",
        "price": 48
      },
      {
        "partNumber": "LOWPM-10H-1064",
        "diameter": "10.00mm",
        "wavelength": "1064nm",
        "phase": "Half Wave",
        "price": 50
      },
      {
        "partNumber": "LOWPM-12.7Q-1064",
        "diameter": "12.70mm",
        "wavelength": "1064nm",
        "phase": "Quarter Wave",
        "price": 58
      },
      {
        "partNumber": "LOWPM-12.7H-1064",
        "diameter": "12.70mm",
        "wavelength": "1064nm",
        "phase": "Half Wave",
        "price": 62
      },
      {
        "partNumber": "LOWPM-20Q-1064",
        "diameter": "20.00mm",
        "wavelength": "1064nm",
        "phase": "Quarter Wave",
        "price": 78
      },
      {
        "partNumber": "LOWPM-20H-1064",
        "diameter": "20.00mm",
        "wavelength": "1064nm",
        "phase": "Half Wave",
        "price": 82
      },
      {
        "partNumber": "LOWPM-25.4Q-1064",
        "diameter": "25.40mm",
        "wavelength": "1064nm",
        "phase": "Quarter Wave",
        "price": 95
      },
      {
        "partNumber": "LOWPM-25.4H-1064",
        "diameter": "25.40mm",
        "wavelength": "1064nm",
        "phase": "Half Wave",
        "price": 100
      }
    ]
  },
  {
    "id": 41,
    "name": "Optical Circular Polarizer",
    "nameZh": "圆偏振片",
    "category": "Optical Polarising Components",
    "categoryZh": "光学偏振组件",
    "description": "Broadband circular polarizers combining linear polarizers with quarter-wave plates. Essential for glare reduction, 3D displays, and optical isolation.",
    "image": "images/products/optical-polarising-components/optical-circular-polarizer.jpg",
    "parameters": {
      "material": "Polarizing film + Quarter-wave plate",
      "diameter": "12.7-50mm",
      "wavelength_range": "400-700nm / 600-900nm",
      "extinction_ratio": ">100:1",
      "peak_transmittance": ">30% (circular)",
      "surface_quality": "40-20"
    },
    "price": 85,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 42,
    "name": "Optical Glan Laser Prisms",
    "nameZh": "Glan激光棱镜偏振器",
    "category": "Optical Polarising Components",
    "categoryZh": "光学偏振组件",
    "description": "Glan-laser prisms with high extinction ratio and laser-grade surface quality. Air-spaced design for high-power laser applications with excellent damage threshold.",
    "image": "images/products/optical-polarising-components/optical-glan-laser-prisms.jpg",
    "parameters": {
      "material": "Calcite / α-BBO",
      "aperture": "5-15mm",
      "wavelength_range": "400-700nm / 700-1100nm",
      "extinction_ratio": ">10^5:1",
      "surface_quality": "20-10",
      "damage_threshold": ">10 J/cm² (10ns)"
    },
    "price": 120,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOLLM20-532",
        "wavelength": "532nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 55
      },
      {
        "partNumber": "LOLLM25.4-532",
        "wavelength": "532nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 68
      },
      {
        "partNumber": "LOLLM30-532",
        "wavelength": "532nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 78
      },
      {
        "partNumber": "LOLLM20-1064",
        "wavelength": "1064nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 55
      },
      {
        "partNumber": "LOLLM25.4-1064",
        "wavelength": "1064nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 68
      },
      {
        "partNumber": "LOLLM30-1064",
        "wavelength": "1064nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 78
      },
      {
        "partNumber": "LOLLM35-1064",
        "wavelength": "1064nm",
        "diameter": "35mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 88
      },
      {
        "partNumber": "LOLLM50-1064",
        "wavelength": "1064nm",
        "diameter": "50mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 110
      },
      {
        "partNumber": "LOLLM20-355",
        "wavelength": "355nm",
        "diameter": "20mm",
        "thickness": "4mm",
        "reflectance": ">99%",
        "price": 65
      },
      {
        "partNumber": "LOLLM30-355",
        "wavelength": "355nm",
        "diameter": "30mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 85
      },
      {
        "partNumber": "LOLLM25.4-1550",
        "wavelength": "1550nm",
        "diameter": "25.4mm",
        "thickness": "5mm",
        "reflectance": ">99%",
        "price": 85
      }
    ]
  },
  {
    "id": 43,
    "name": "Optical Glan Taylor Prisms",
    "nameZh": "Glan Taylor棱镜偏振器",
    "category": "Optical Polarising Components",
    "categoryZh": "光学偏振组件",
    "description": "Glan-Taylor prisms providing high extinction ratio polarization separation. Standard choice for laboratory and instrumentation applications.",
    "image": "images/products/optical-polarising-components/optical-glan-taylor-prisms.jpg",
    "parameters": {
      "material": "Calcite",
      "aperture": "5-15mm",
      "wavelength_range": "350-700nm",
      "extinction_ratio": ">10^5:1",
      "surface_quality": "40-20",
      "damage_threshold": ">5 J/cm² (10ns)"
    },
    "price": 95,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 44,
    "name": "Optical Isolator",
    "nameZh": "光隔离器",
    "category": "Optical Polarising Components",
    "categoryZh": "光学偏振组件",
    "description": "High-performance optical isolators protecting laser sources from back reflections. Essential for fiber lasers, semiconductor lasers, and precision measurement systems.",
    "image": "images/products/optical-polarising-components/optical-isolator.jpg",
    "parameters": {
      "wavelength_range": "532nm / 633nm / 1064nm / 1550nm",
      "isolation": ">30dB",
      "transmittance": ">85%",
      "aperture": "2-5mm",
      "damage_threshold": ">5 J/cm² (10ns)"
    },
    "price": 350,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 45,
    "name": "Optical Linear Polarizer",
    "nameZh": "线偏振片",
    "category": "Optical Polarising Components",
    "categoryZh": "光学偏振组件",
    "description": "High-quality linear polarizers for producing polarized light. Available in various sizes and wavelength ranges for scientific and industrial applications.",
    "image": "images/products/optical-polarising-components/optical-linear-polarizer.jpg",
    "parameters": {
      "material": "Polarizing film / Glan / Calcite",
      "diameter": "10-50mm",
      "wavelength_range": "400-700nm / 650-1100nm / Custom",
      "extinction_ratio": ">1000:1",
      "peak_transmittance": ">42% (polarized)",
      "surface_quality": "40-20"
    },
    "price": 55,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOLP12.7",
        "size": "12.7mm",
        "wavelength": "400-700nm",
        "transmittance": ">50%",
        "price": 85
      },
      {
        "partNumber": "LOLO25.4",
        "size": "25.4mm",
        "wavelength": "400-700nm",
        "transmittance": ">50%",
        "price": 115
      }
    ]
  },
  {
    "id": 46,
    "name": "Optical Wollaston Prisms",
    "nameZh": "Wollaston棱镜",
    "category": "Optical Polarising Components",
    "categoryZh": "光学偏振组件",
    "description": "Wollaston prisms separating unpolarized light into two orthogonal polarized beams. Perfect for polarimetry, interferometry, and beam splitting applications.",
    "image": "images/products/optical-polarising-components/optical-wollaston-prisms.jpg",
    "parameters": {
      "material": "Calcite",
      "aperture": "2-10mm",
      "wavelength_range": "400-700nm",
      "extinction_ratio": ">10^4:1",
      "beam_separation": "0.5-3°",
      "surface_quality": "40-20"
    },
    "price": 85,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 47,
    "name": "Quartz Polarization Rotator",
    "nameZh": "石英偏振旋转器",
    "category": "Optical Polarising Components",
    "categoryZh": "光学偏振组件",
    "description": "Crystal quartz polarization rotators rotating the plane of polarization without changing beam properties. Rotation angle depends on crystal thickness and wavelength.",
    "image": "images/products/optical-polarising-components/quartz-polarization-rotator.jpg",
    "parameters": {
      "material": "Crystal Quartz",
      "diameter": "10-30mm",
      "wavelength_range": "400-1600nm",
      "rotation_angle": "0-90° (customizable)",
      "extinction_ratio": ">500:1",
      "surface_quality": "40-20"
    },
    "price": 75,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 48,
    "name": "Wide band achromatic wave plate",
    "nameZh": "宽带消色差波片",
    "category": "Optical Polarising Components",
    "categoryZh": "光学偏振组件",
    "description": "Achromatic wave plates with consistent retardation across a broad wavelength range. Ideal for broadband light sources and multi-wavelength laser systems.",
    "image": "images/products/optical-polarising-components/wide-band-achromatic-wave-plate.jpg",
    "parameters": {
      "material": "Crystal Quartz + MgF2",
      "diameter": "12.7-50.8mm",
      "bandwidth": "400-700nm / 600-1100nm",
      "retardation": "λ/2 / λ/4",
      "surface_quality": "40-20",
      "damage_threshold": ">5 J/cm² (10ns)"
    },
    "price": 100,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 49,
    "name": "Corner Cube Prisms",
    "nameZh": "角锥棱镜",
    "category": "Optical Prisms",
    "categoryZh": "光学棱镜",
    "description": "Precision corner cube prisms reflecting incident light back toward the source regardless of orientation. Essential for surveying, laser ranging, and optical alignment.",
    "image": "images/products/optical-prisms/corner-cube-prisms.jpg",
    "parameters": {
      "material": "K9/BK7 / Fused Silica",
      "aperture": "5-50mm",
      "reflectivity": ">90% (all faces)",
      "angle_tolerance": "±30 arcsec",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4@632.8nm"
    },
    "price": 45,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOCCP12.7",
        "diameter": "12.70mm",
        "height": "10.20mm",
        "price": 45
      },
      {
        "partNumber": "LOCCP15",
        "diameter": "15.00mm",
        "height": "11.30mm",
        "price": 55
      },
      {
        "partNumber": "LOCCP25.4",
        "diameter": "25.40mm",
        "height": "19.00mm",
        "price": 75
      },
      {
        "partNumber": "LOCCP38",
        "diameter": "38.00mm",
        "height": "28.50mm",
        "price": 120
      },
      {
        "partNumber": "LOCCP50.8",
        "diameter": "50.80mm",
        "height": "37.50mm",
        "price": 165
      },
      {
        "partNumber": "LOCCP70",
        "diameter": "70.00mm",
        "height": "52.50mm",
        "price": 250
      }
    ]
  },
  {
    "id": 50,
    "name": "Dove Prisms",
    "nameZh": "Dove棱镜",
    "category": "Optical Prisms",
    "categoryZh": "光学棱镜",
    "description": "Dove prisms for image rotation and inversion without deviating the beam path. Widely used in telescopes, optical alignment, and interferometer applications.",
    "image": "images/products/optical-prisms/dove-prisms.jpg",
    "parameters": {
      "material": "K9/BK7",
      "length": "10-100mm",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4@632.8nm",
      "beam_deviation": "<3 arcmin"
    },
    "price": 30,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LODP01",
        "dimension": "9.3x2.6x1.3mm",
        "price": 35
      },
      {
        "partNumber": "LODP02",
        "dimension": "14x5x2.6mm",
        "price": 45
      },
      {
        "partNumber": "LODP03",
        "dimension": "80x20x20mm",
        "price": 120
      },
      {
        "partNumber": "LODP04",
        "dimension": "21.1x5x5mm",
        "price": 55
      },
      {
        "partNumber": "LODP05",
        "dimension": "42.3x10x10mm",
        "price": 85
      },
      {
        "partNumber": "LODP06",
        "dimension": "63.4x15x15mm",
        "price": 115
      }
    ]
  },
  {
    "id": 51,
    "name": "Equilateral Prisms",
    "nameZh": "等边棱镜",
    "category": "Optical Prisms",
    "categoryZh": "光学棱镜",
    "description": "Three-sided prisms for spectral dispersion and wavelength separation. Essential for spectroscopy, color separation, and educational demonstrations.",
    "image": "images/products/optical-prisms/equilateral-prisms.jpg",
    "parameters": {
      "material": "K9/BK7",
      "aperture": "10-50mm",
      "apex_angle": "60° (±30 arcsec)",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4@632.8nm"
    },
    "price": 25,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 52,
    "name": "Half Penta Prisms",
    "nameZh": "半五角棱镜",
    "category": "Optical Prisms",
    "categoryZh": "光学棱镜",
    "description": "Half penta prisms deflecting light by 45° without inverting the image. Commonly used in camera viewfinders and optical sighting systems.",
    "image": "images/products/optical-prisms/half-penta-prisms.jpg",
    "parameters": {
      "material": "K9/BK7",
      "aperture": "10-30mm",
      "angle_tolerance": "±30 arcsec",
      "surface_quality": "40-20"
    },
    "price": 35,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 53,
    "name": "Optical Wedge Prisms",
    "nameZh": "楔形棱镜",
    "category": "Optical Prisms",
    "categoryZh": "光学棱镜",
    "description": "Precision wedge prisms for beam steering and deviation. Multiple wedges can be combined for variable angle adjustment.",
    "image": "images/products/optical-prisms/optical-wedge-prisms.jpg",
    "parameters": {
      "material": "K9/BK7 / Fused Silica",
      "diameter": "10-50mm",
      "wedge_angle": "1-10°",
      "angle_tolerance": "±30 arcsec",
      "surface_quality": "40-20"
    },
    "price": 25,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 54,
    "name": "Penta Prisms",
    "nameZh": "五角棱镜",
    "category": "Optical Prisms",
    "categoryZh": "光学棱镜",
    "description": "Five-sided prisms deflecting light by exactly 90° while maintaining image orientation. Essential for optical alignment, surveying instruments, and camera systems.",
    "image": "images/products/optical-prisms/penta-prisms.jpg",
    "parameters": {
      "material": "K9/BK7",
      "aperture": "10-50mm",
      "angle_tolerance": "±30 arcsec",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4@632.8nm"
    },
    "price": 35,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 55,
    "name": "Right Angle Prisms",
    "nameZh": "直角棱镜",
    "category": "Optical Prisms",
    "categoryZh": "光学棱镜",
    "description": "Versatile right angle prisms for beam deflection and total internal reflection. Used in optical instruments, endoscopy, and laser systems.",
    "image": "images/products/optical-prisms/right-angle-prisms.jpg",
    "parameters": {
      "material": "K9/BK7 / UV Fused Silica",
      "leg_length": "5-50mm",
      "angle_tolerance": "±30 arcsec",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4@632.8nm"
    },
    "price": 22,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LORP3-3",
        "dimension": "3x3x3mm",
        "price": 12
      },
      {
        "partNumber": "LORP3-5",
        "dimension": "3x3x5mm",
        "price": 13
      },
      {
        "partNumber": "LORP5-5",
        "dimension": "5x5x5mm",
        "price": 15
      },
      {
        "partNumber": "LORP10-10",
        "dimension": "10x10x10mm",
        "price": 18
      },
      {
        "partNumber": "LORP15-15",
        "dimension": "15x15x15mm",
        "price": 22
      },
      {
        "partNumber": "LORP20-20",
        "dimension": "20x20x20mm",
        "price": 28
      },
      {
        "partNumber": "LORP25-25",
        "dimension": "25x25x25mm",
        "price": 32
      },
      {
        "partNumber": "LORP25.4-25.4",
        "dimension": "25.4x25.4x25.4mm",
        "price": 35
      },
      {
        "partNumber": "LORP30-30",
        "dimension": "30x30x30mm",
        "price": 42
      },
      {
        "partNumber": "LORP50.8-50.8",
        "dimension": "50.8x50.8x50.8mm",
        "price": 65
      }
    ]
  },
  {
    "id": 56,
    "name": "Optical Rod Lenses",
    "nameZh": "光学棒状透镜",
    "category": "Optical Rod Lenses",
    "categoryZh": "光学棒状透镜",
    "description": "Cylindrical rod lenses for line generation and light homogenization. High numerical aperture design for efficient fiber coupling and illumination systems.",
    "image": "images/products/optical-rod-lenses/optical-rod-lenses.jpg",
    "parameters": {
      "material": "K9/BK7 / Fused Silica",
      "diameter": "1-10mm",
      "length": "10-100mm",
      "surface_quality": "40-20",
      "numerical_aperture": "Up to 0.50"
    },
    "price": 25,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 57,
    "name": "UV Fused Silica Double Convex Lenses",
    "nameZh": "UV熔融石英双凸透镜",
    "category": "Optical Spherical Lenses",
    "categoryZh": "光学球面透镜",
    "description": "UV-grade biconvex lenses for UV and visible light focusing applications. Fused silica provides excellent transmission from 185nm to 2500nm.",
    "image": "images/products/optical-spherical-lenses/uv-fused-silica-double-convex-lenses.jpg",
    "parameters": {
      "material": "Fused Silica (JGS1)",
      "diameter": "6-50mm",
      "focal_length": "20-200mm",
      "wavelength_range": "185-2500nm",
      "surface_quality": "20-10",
      "coating": "Uncoated / AR coating"
    },
    "price": 30,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 58,
    "name": "UV Fused Silica Plano Concave Lenses",
    "nameZh": "UV熔融石英平凹透镜",
    "category": "Optical Spherical Lenses",
    "categoryZh": "光学球面透镜",
    "description": "UV-grade plano-concave lenses for beam expansion and divergence. Ideal for laser pulse stretching and optical path length extension.",
    "image": "images/products/optical-spherical-lenses/uv-fused-silica-plano-concave-lenses.jpg",
    "parameters": {
      "material": "Fused Silica (JGS1)",
      "diameter": "6-50mm",
      "focal_length": "-20 to -150mm",
      "wavelength_range": "185-2500nm",
      "surface_quality": "20-10",
      "coating": "Uncoated / AR coating"
    },
    "price": 28,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 59,
    "name": "UV Fused Silica Plano Convex Lenses",
    "nameZh": "UV熔融石英平凸透镜",
    "category": "Optical Spherical Lenses",
    "categoryZh": "光学球面透镜",
    "description": "UV-grade plano-convex lenses with superior transmission in the UV spectrum. Excellent for UV curing, photolithography, and fluorescence excitation.",
    "image": "images/products/optical-spherical-lenses/uv-fused-silica-plano-convex-lenses.jpg",
    "parameters": {
      "material": "Fused Silica (JGS1)",
      "diameter": "6-100mm",
      "focal_length": "20-300mm",
      "wavelength_range": "185-2500nm",
      "surface_quality": "20-10",
      "coating": "Uncoated / AR coating"
    },
    "price": 28,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 60,
    "name": "BK7 Optical Windows",
    "nameZh": "BK7光学窗口",
    "category": "Optical Windows",
    "categoryZh": "光学窗口",
    "description": "Standard optical windows for sealing and protecting optical systems. BK7 glass provides excellent transmittance in the visible spectrum with good thermal stability.",
    "image": "images/products/optical-windows/bk7-optical-windows.jpg",
    "parameters": {
      "material": "K9/BK7",
      "diameter": "6-100mm",
      "thickness": "1-10mm",
      "surface_flatness": "λ/4@632.8nm",
      "surface_quality": "40-20",
      "parallelism": "<3 arcmin"
    },
    "price": 18,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOWB6-2",
        "diameter": "6.00mm",
        "thickness": "2.00mm",
        "price": 12
      },
      {
        "partNumber": "LOWB10-3",
        "diameter": "10.00mm",
        "thickness": "3.00mm",
        "price": 15
      },
      {
        "partNumber": "LOWB12.7-3",
        "diameter": "12.70mm",
        "thickness": "3.00mm",
        "price": 18
      },
      {
        "partNumber": "LOWB15-3",
        "diameter": "15.00mm",
        "thickness": "3.00mm",
        "price": 20
      },
      {
        "partNumber": "LOWB20-3",
        "diameter": "20.00mm",
        "thickness": "3.00mm",
        "price": 25
      },
      {
        "partNumber": "LOWB25.4-3",
        "diameter": "25.40mm",
        "thickness": "3.00mm",
        "price": 28
      },
      {
        "partNumber": "LOWB30-3",
        "diameter": "30.00mm",
        "thickness": "3.00mm",
        "price": 35
      },
      {
        "partNumber": "LOWB38.1-3",
        "diameter": "38.10mm",
        "thickness": "3.00mm",
        "price": 45
      },
      {
        "partNumber": "LOWB40-5",
        "diameter": "40.00mm",
        "thickness": "5.00mm",
        "price": 52
      },
      {
        "partNumber": "LOWB50.8-5",
        "diameter": "50.80mm",
        "thickness": "5.00mm",
        "price": 65
      },
      {
        "partNumber": "LOWB75-5",
        "diameter": "75.00mm",
        "thickness": "5.00mm",
        "price": 95
      },
      {
        "partNumber": "LOWB100-10",
        "diameter": "100.00mm",
        "thickness": "10.00mm",
        "price": 145
      }
    ]
  },
  {
    "id": 61,
    "name": "Optical Silicon Windows",
    "nameZh": "硅光学窗口",
    "category": "Optical Windows",
    "categoryZh": "光学窗口",
    "description": "Silicon windows for NIR and FIR applications from 1.2μm to 8μm. Lightweight and cost-effective solution for infrared optical systems.",
    "image": "images/products/optical-windows/optical-silicon-windows.jpg",
    "parameters": {
      "material": "Si",
      "diameter": "12.7-50.8mm",
      "thickness": "2-6mm",
      "wavelength_range": "1.2-8000nm",
      "surface_flatness": "λ/2@632.8nm",
      "surface_quality": "40-20"
    },
    "price": 55,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 62,
    "name": "Optical CaF2 Windows",
    "nameZh": "CaF2光学窗口",
    "category": "Optical Windows",
    "categoryZh": "光学窗口",
    "description": "Calcium fluoride windows for UV and mid-infrared applications. Extended transmission from 180nm to 8μm with excellent chemical resistance.",
    "image": "images/products/optical-windows/optical-caf2-windows.jpg",
    "parameters": {
      "material": "CaF2",
      "diameter": "12.7-50.8mm",
      "thickness": "1-5mm",
      "wavelength_range": "180nm-8μm",
      "surface_flatness": "λ/4@632.8nm",
      "surface_quality": "40-20"
    },
    "price": 65,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 63,
    "name": "Optical Germanium Windows",
    "nameZh": "锗光学窗口",
    "category": "Optical Windows",
    "categoryZh": "光学窗口",
    "description": "Germanium windows for thermal imaging and MWIR applications. High refractive index provides excellent performance in the 3-12μm atmospheric window.",
    "image": "images/products/optical-windows/optical-germanium-windows.jpg",
    "parameters": {
      "material": "Ge",
      "diameter": "12.7-50.8mm",
      "thickness": "2-8mm",
      "wavelength_range": "3-12μm",
      "surface_flatness": "λ/2@632.8nm",
      "surface_quality": "40-20",
      "coating": "AR coating available"
    },
    "price": 75,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 64,
    "name": "Optical Sapphire Windows",
    "nameZh": "蓝宝石光学窗口",
    "category": "Optical Windows",
    "categoryZh": "光学窗口",
    "description": "Synthetic sapphire windows for UV to MIR applications. Extremely hard and durable material with excellent scratch resistance and thermal conductivity.",
    "image": "images/products/optical-windows/optical-sapphire-windows.jpg",
    "parameters": {
      "material": "Al2O3 (Sapphire)",
      "diameter": "6-50mm",
      "thickness": "0.5-5mm",
      "wavelength_range": "150nm-4.5μm",
      "surface_flatness": "λ/4@632.8nm",
      "surface_quality": "40-20"
    },
    "price": 55,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOWS6-2",
        "diameter": "6.00mm",
        "thickness": "2.00mm",
        "price": 35
      },
      {
        "partNumber": "LOWS8-1",
        "diameter": "8.00mm",
        "thickness": "1.00mm",
        "price": 38
      },
      {
        "partNumber": "LOWS10-3",
        "diameter": "10.00mm",
        "thickness": "3.00mm",
        "price": 42
      },
      {
        "partNumber": "LOWS12.7-1",
        "diameter": "12.70mm",
        "thickness": "1.00mm",
        "price": 48
      },
      {
        "partNumber": "LOWS15-2",
        "diameter": "15.00mm",
        "thickness": "2.00mm",
        "price": 55
      },
      {
        "partNumber": "LOWS20-2",
        "diameter": "20.00mm",
        "thickness": "2.00mm",
        "price": 68
      },
      {
        "partNumber": "LOWS25.4-2",
        "diameter": "25.40mm",
        "thickness": "2.00mm",
        "price": 78
      },
      {
        "partNumber": "LOWS30-3",
        "diameter": "30.00mm",
        "thickness": "3.00mm",
        "price": 95
      },
      {
        "partNumber": "LOWS38.1-5",
        "diameter": "38.10mm",
        "thickness": "5.00mm",
        "price": 125
      },
      {
        "partNumber": "LOWS50.8-5",
        "diameter": "50.80mm",
        "thickness": "5.00mm",
        "price": 165
      }
    ]
  },
  {
    "id": 65,
    "name": "Optical ZnSe Windows",
    "nameZh": "ZnSe光学窗口",
    "category": "Optical Windows",
    "categoryZh": "光学窗口",
    "description": "Zinc selenide windows for CO2 laser and thermal imaging applications. Low absorption coefficient and high thermal shock resistance make it ideal for high-power laser systems.",
    "image": "images/products/optical-windows/optical-znse-windows.jpg",
    "parameters": {
      "material": "ZnSe",
      "diameter": "12.7-50.8mm",
      "thickness": "2-6mm",
      "wavelength_range": "600nm-16μm",
      "surface_flatness": "λ/4@632.8nm",
      "surface_quality": "40-20",
      "damage_threshold": ">10 J/cm² (10ns, 10.6μm)"
    },
    "price": 85,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 66,
    "name": "UV Fused Silica Windows",
    "nameZh": "UV熔融石英窗口",
    "category": "Optical Windows",
    "categoryZh": "光学窗口",
    "description": "UV-grade fused silica windows for semiconductor and scientific applications. Ultra-low thermal expansion and excellent UV transmission from 185nm.",
    "image": "images/products/optical-windows/uv-fused-silica-windows.jpg",
    "parameters": {
      "material": "Fused Silica (JGS1)",
      "diameter": "6-100mm",
      "thickness": "1-10mm",
      "wavelength_range": "185-2500nm",
      "surface_flatness": "λ/4@632.8nm",
      "surface_quality": "40-20",
      "parallelism": "<3 arcmin"
    },
    "price": 35,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价",
    "partNumbers": [
      {
        "partNumber": "LOWF5-2",
        "diameter": "5.00mm",
        "thickness": "2.00mm",
        "price": 22
      },
      {
        "partNumber": "LOWF6-2",
        "diameter": "6.00mm",
        "thickness": "2.00mm",
        "price": 25
      },
      {
        "partNumber": "LOWF10-3",
        "diameter": "10.00mm",
        "thickness": "3.00mm",
        "price": 28
      },
      {
        "partNumber": "LOWF12.7-2",
        "diameter": "12.70mm",
        "thickness": "2.00mm",
        "price": 32
      },
      {
        "partNumber": "LOWF15-3",
        "diameter": "15.00mm",
        "thickness": "3.00mm",
        "price": 38
      },
      {
        "partNumber": "LOWF20-3",
        "diameter": "20.00mm",
        "thickness": "3.00mm",
        "price": 45
      },
      {
        "partNumber": "LOWF25.4-3",
        "diameter": "25.40mm",
        "thickness": "3.00mm",
        "price": 52
      },
      {
        "partNumber": "LOWF30-5",
        "diameter": "30.00mm",
        "thickness": "5.00mm",
        "price": 65
      },
      {
        "partNumber": "LOWF38.1-5",
        "diameter": "38.10mm",
        "thickness": "5.00mm",
        "price": 85
      },
      {
        "partNumber": "LOWF50.8-5",
        "diameter": "50.80mm",
        "thickness": "5.00mm",
        "price": 105
      },
      {
        "partNumber": "LOWF75-10",
        "diameter": "75.00mm",
        "thickness": "10.00mm",
        "price": 165
      },
      {
        "partNumber": "LOWF100-12",
        "diameter": "100.00mm",
        "thickness": "12.00mm",
        "price": 245
      }
    ]
  },
  {
    "id": 68,
    "name": "Kinematic Mirror Mounts",
    "nameZh": "反射镜调整架",
    "category": "Optical Mounts & Accessories",
    "categoryZh": "光学支架与配件",
    "description": "Precision kinematic mirror mounts with fine adjustment screws for accurate tip/tilt alignment. Compatible with mirrors from 12.7mm to 50.8mm diameter.",
    "image": "images/products/optical-mounts/kinematic-mirror-mounts.jpg",
    "parameters": {
      "material": "Aluminum alloy, black anodized",
      "aperture": "12.7-50.8mm",
      "adjustment_range": "±4°",
      "resolution": "0.003° per click"
    },
    "partNumbers": [
      {
        "partNumber": "LMMK12.7",
        "size": "12.7mm",
        "price": 45
      },
      {
        "partNumber": "LMMK25.4",
        "size": "25.4mm",
        "price": 55
      },
      {
        "partNumber": "LMMK50.8",
        "size": "50.8mm",
        "price": 75
      }
    ],
    "price": 45,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 69,
    "name": "Fixed Lens Mounts",
    "nameZh": "固定透镜架",
    "category": "Optical Mounts & Accessories",
    "categoryZh": "光学支架与配件",
    "description": "SM-threaded fixed lens mounts for securely holding optical lenses. Available in various thread sizes.",
    "image": "images/products/optical-mounts/fixed-lens-mounts.jpg",
    "parameters": {
      "material": "Aluminum alloy, black anodized",
      "thread_standard": "SM (Standard Metric)",
      "clear_aperture": "Up to 90% of thread size"
    },
    "partNumbers": [
      {
        "partNumber": "LFM05",
        "thread": "M5",
        "price": 20
      },
      {
        "partNumber": "LFM1",
        "thread": "M10",
        "price": 22
      },
      {
        "partNumber": "LFM2",
        "thread": "M20",
        "price": 25
      }
    ],
    "price": 20,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 70,
    "name": "Rotation Mounts",
    "nameZh": "旋转调整架",
    "category": "Optical Mounts & Accessories",
    "categoryZh": "光学支架与配件",
    "description": "Precision rotation mounts for waveplates, polarizers and other rotation-sensitive optics. 360° continuous rotation with fine scale adjustment.",
    "image": "images/products/optical-mounts/rotation-mounts.jpg",
    "parameters": {
      "material": "Aluminum alloy, black anodized",
      "aperture": "25.4mm",
      "rotation_range": "360° continuous",
      "resolution": "1° scale, 0.1° vernier"
    },
    "partNumbers": [
      {
        "partNumber": "LRM25.4",
        "aperture": "25.4mm",
        "price": 65
      },
      {
        "partNumber": "LRM50.8",
        "aperture": "50.8mm",
        "price": 85
      }
    ],
    "price": 65,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 71,
    "name": "Optical Post & Base",
    "nameZh": "光学接杆与底座",
    "category": "Optical Mounts & Accessories",
    "categoryZh": "光学支架与配件",
    "description": "Stainless steel optical posts with bases for stable optical mounting. Standard hole patterns compatible with optical tables.",
    "image": "images/products/optical-mounts/optical-post-base.jpg",
    "parameters": {
      "material": "Stainless steel",
      "base_size": "60x60mm",
      "hole_pattern": "25mm grid, M6 threads"
    },
    "partNumbers": [
      {
        "partNumber": "LOP-50",
        "length": "50mm",
        "price": 15
      },
      {
        "partNumber": "LOP-75",
        "length": "75mm",
        "price": 18
      },
      {
        "partNumber": "LOP-100",
        "length": "100mm",
        "price": 20
      },
      {
        "partNumber": "LOP-150",
        "length": "150mm",
        "price": 25
      }
    ],
    "price": 15,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 72,
    "name": "Post Holders",
    "nameZh": "杆座",
    "category": "Optical Mounts & Accessories",
    "categoryZh": "光学支架与配件",
    "description": "Sturdy post holders for securing optical posts to breadboards or optical tables. Quick-release mechanism for easy adjustment.",
    "image": "images/products/optical-mounts/post-holders.jpg",
    "parameters": {
      "material": "Aluminum alloy, black anodized",
      "post_diameter": "12.7mm",
      "clamping": "Knurled thumb screw"
    },
    "partNumbers": [
      {
        "partNumber": "LPH-50",
        "height": "50mm",
        "price": 18
      },
      {
        "partNumber": "LPH-75",
        "height": "75mm",
        "price": 22
      },
      {
        "partNumber": "LPH-100",
        "height": "100mm",
        "price": 25
      }
    ],
    "price": 18,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 73,
    "name": "XY Translation Stages",
    "nameZh": "XY平移台",
    "category": "Optical Mounts & Accessories",
    "categoryZh": "光学支架与配件",
    "description": "Compact XY translation stages for precise two-axis positioning. Micrometer-driven with fine resolution.",
    "image": "images/products/optical-mounts/xy-translation-stages.jpg",
    "parameters": {
      "material": "Aluminum alloy, black anodized",
      "platform_size": "60x60mm",
      "load_capacity": "5kg"
    },
    "partNumbers": [
      {
        "partNumber": "LXY-25",
        "travel": "±12.5mm",
        "price": 120
      },
      {
        "partNumber": "LXY-50",
        "travel": "±25mm",
        "price": 165
      }
    ],
    "price": 120,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 74,
    "name": "Optical Table Breadboards",
    "nameZh": "光学面包板",
    "category": "Optical Mounts & Accessories",
    "categoryZh": "光学支架与配件",
    "description": "Stainless steel optical breadboards with standard hole patterns for flexible optical setup configurations.",
    "image": "images/products/optical-mounts/optical-breadboard.jpg",
    "parameters": {
      "material": "Stainless steel",
      "thickness": "12mm",
      "hole_pattern": "25mm grid, M6 threads"
    },
    "partNumbers": [
      {
        "partNumber": "LBB-300x300",
        "size": "300x300mm",
        "price": 200
      },
      {
        "partNumber": "LBB-450x450",
        "size": "450x450mm",
        "price": 320
      },
      {
        "partNumber": "LBB-600x600",
        "size": "600x600mm",
        "price": 480
      }
    ],
    "price": 200,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  },
  {
    "id": 75,
    "name": "Cage Systems",
    "nameZh": "笼式系统",
    "category": "Optical Mounts & Accessories",
    "categoryZh": "光学支架与配件",
    "description": "Modular cage system components for building compact and stable optical assemblies. Compatible with standard cage system standards.",
    "image": "images/products/optical-mounts/cage-system.jpg",
    "parameters": {
      "material": "Aluminum alloy, black anodized",
      "standard": "30mm / 60mm cage",
      "components": "Plates, rods, mounts"
    },
    "partNumbers": [
      {
        "partNumber": "LCS-30",
        "size": "30mm cage",
        "price": 30
      },
      {
        "partNumber": "LCS-60",
        "size": "60mm cage",
        "price": 45
      }
    ],
    "price": 30,
    "priceUnit": "USD",
    "priceNote": "Starting price, contact for volume discount",
    "priceNoteZh": "起售价，批量询价"
  }
];
// Category to first product image mapping for homepage categories
var CATEGORY_IMAGES = {
    "Optical Ball Lenses": "images/products/optical-ball-lenses/uv-fused-silica-ball-lenses.jpg",
    "Optical Beamsplitters": "images/products/optical-beamsplitters/beamsplitter-plate.jpg",
    "Optical Cylindrical Lenses": "images/products/optical-cylindrical-lenses/uv-fused-silica-plano-concave-cylindrical-lenses.jpg",
    "Optical Filters": "images/products/optical-filters/circular-variable-ndneutral-density-filters.jpg",
    "Optical Half Ball Lenses": "images/products/optical-half-ball-lenses/uv-fused-silica-half-ball-lenses.jpg",
    "Optical Lenses": "images/products/optical-lenses/achromatic-doublet-lenses.jpg",
    "Optical Mirrors": "images/products/optical-mirrors/broadband-dielectric-coated-mirrors.jpg",
    "Optical Polarising Components": "images/products/optical-polarising-components/air-spaced-zero-order-high-power-waveplates.jpg",
    "Optical Prisms": "images/products/optical-prisms/corner-cube-prisms.jpg",
    "Optical Rod Lenses": "images/products/optical-rod-lenses/optical-rod-lenses.jpg",
    "Optical Spherical Lenses": "images/products/optical-spherical-lenses/uv-fused-silica-double-convex-lenses.jpg",
    "Optical Windows": "images/products/optical-windows/bk7-optical-windows.jpg",
    "Optical Mounts & Accessories": "images/products/optical-mounts/kinematic-mirror-mounts.jpg"
};
