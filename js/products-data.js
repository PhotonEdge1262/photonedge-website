// PhotonEdge Products Data
// Total: 66 products - Enhanced with detailed specifications

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
    }
  },
  {
    "id": 2,
    "name": "Beamsplitter Plate",
    "nameZh": "分光板",
    "category": "Optical Beamsplitters",
    "categoryZh": "光学分光镜",
    "description": "Precision plate beamsplitters for splitting or combining optical beams. Available in various splitting ratios for laboratory and industrial applications. Anti-reflection coated surfaces minimize unwanted reflections.",
    "image": "images/products/optical-beamsplitters/beamsplitter-plate.jpg",
    "parameters": {
      "material": "N-BK7 / K9",
      "diameter": "12.7-50.8mm",
      "thickness": "1-5mm",
      "split_ratio": "50:50 / 70:30 / 90:10",
      "wavelength_range": "400-700nm (VIS) / 700-1100nm (NIR)",
      "surface_quality": "40-20",
      "surface_flatness": "λ/4@632.8nm"
    }
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
    }
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
    }
  },
  {
    "id": 5,
    "name": "Optical Cube Beamsplitters",
    "nameZh": "光学立方体分光镜",
    "category": "Optical Beamsplitters",
    "categoryZh": "光学分光镜",
    "description": "Premium cube beamsplitters with precision-aligned dielectric coating. Zero wedge design eliminates beam deviation. Perfect for OEM integration in optical instruments.",
    "image": "images/products/optical-beamsplitters/optical-cube-beamsplitters.jpg",
    "parameters": {
      "material": "N-BK7",
      "size": "10-50mm",
      "split_ratio": "50:50 (±3%)",
      "wavelength_range": "400-700nm / 650-1050nm",
      "surface_quality": "40-20",
      "extinction_ratio": "<100:1"
    }
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
    }
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
    }
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
    }
  },
  {
    "id": 9,
    "name": "Circular Variable ND(neutral density) Filters",
    "nameZh": "圆形可变中性密度滤光片",
    "category": "Optical Filters",
    "categoryZh": "光学滤光片",
    "description": "Continuously variable neutral density filters with rotary adjustment. Perfect for fine-tuning laser power, balancing illumination in microscopy, and photographic applications.",
    "image": "images/products/optical-filters/circular-variable-ndneutral-density-filters.jpg",
    "parameters": {
      "material": "Schott Glass / Dielectric",
      "diameter": "25-50mm",
      "od_range": "0.04-2.5",
      "wavelength_range": "400-700nm / 650-1050nm",
      "surface_quality": "40-20"
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
  },
  {
    "id": 18,
    "name": "BK7 & UV Fused Silica Double Concave Lenses",
    "nameZh": "BK7与UV熔融石英双凹透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "High-performance double concave lenses for beam expansion and light divergence. Available in both standard BK7 and UV-grade fused silica for UV applications.",
    "image": "images/products/optical-lenses/bk7-and-uv-fused-silica-double-concave-lenses.jpg",
    "parameters": {
      "material": "K9/BK7 / Fused Silica",
      "diameter": "6-100mm",
      "focal_length": "-20 to -200mm",
      "coating": "Uncoated / AR coating",
      "surface_quality": "40-20",
      "center_thickness": "2-10mm"
    }
  },
  {
    "id": 19,
    "name": "BK7 Double Convex Lenses",
    "nameZh": "BK7双凸透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Versatile biconvex lenses with positive focal length for focusing and collimating light beams. Symmetric design minimizes spherical aberration for improved image quality.",
    "image": "images/products/optical-lenses/bk7-double-convex-lenses.jpg",
    "parameters": {
      "material": "K9/BK7",
      "diameter": "6-100mm",
      "focal_length": "20-300mm",
      "coating": "Uncoated / AR coating",
      "surface_quality": "40-20",
      "center_thickness": "2-15mm"
    }
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
    }
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
    }
  },
  {
    "id": 22,
    "name": "BK7 Plano Concave Lenses",
    "nameZh": "BK7平凹透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Standard plano-concave lenses with negative focal length for diverging parallel light beams and forming virtual images. Ideal for beam expanders and light projection systems.",
    "image": "images/products/optical-lenses/bk7-plano-concave-lenses.jpg",
    "parameters": {
      "material": "K9/BK7",
      "diameter": "6-100mm",
      "focal_length": "-20 to -300mm",
      "coating": "Uncoated / AR coating",
      "surface_quality": "40-20",
      "center_thickness": "2-10mm"
    }
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
    }
  },
  {
    "id": 24,
    "name": "BK7 Plano Convex Lenses",
    "nameZh": "BK7平凸透镜",
    "category": "Optical Lenses",
    "categoryZh": "光学透镜",
    "description": "Versatile plano-convex lenses with positive focal length for focusing and collimating light beams. Curved surface minimizes spherical aberration for better beam quality.",
    "image": "images/products/optical-lenses/bk7-plano-convex-lenses.jpg",
    "parameters": {
      "material": "K9/BK7",
      "diameter": "6-200mm",
      "focal_length": "10-500mm",
      "coating": "Uncoated / AR coating",
      "surface_quality": "40-20",
      "center_thickness": "2-20mm"
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
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
    }
  }
];

// Category to first product image mapping for homepage categories
const CATEGORY_IMAGES = {
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
    "Optical Windows": "images/products/optical-windows/bk7-optical-windows.jpg"
};
