#!/usr/bin/env python3
"""Generate 5 Application Note pages + index + Quality Assurance page for V103"""
import os, json

BUILD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AN_DIR = os.path.join(BUILD, "application-notes")
os.makedirs(AN_DIR, exist_ok=True)

# Load template components
with open(os.path.join(BUILD, "_tpl_head.txt")) as f: HEAD = f.read()
with open(os.path.join(BUILD, "_tpl_nav.txt")) as f: NAV = f.read()
with open(os.path.join(BUILD, "_tpl_footer.txt")) as f: FOOTER = f.read()

def schema_json(schemas):
    return "\n".join(['    <script type="application/ld+json">\n' + json.dumps(s, indent=4) + '\n    </script>' for s in schemas])

def page(title, desc, url, breadcrumb_items, schemas, body_content):
    head = HEAD.replace(
        '<title>Laser Optics Solutions | High-Power Optical Components | PhotonEdge Optics</title>',
        '<title>{}</title>'.format(title)
    ).replace(
        'content="Optical components for laser optics solutions. Custom solutions from PhotonEdge Optics."',
        'content="{}"'.format(desc)
    ).replace(
        'content="Laser Optics Solutions | PhotonEdge Optics"',
        'content="{}"'.format(title), 2
    ).replace(
        'content="Precision optical components engineered for laser optics solutions applications."',
        'content="{}"'.format(desc), 2
    ).replace(
        'content="https://photonedgeoptics.com/applications/laser-optics/"',
        'content="{}"'.format(url), 3
    ).replace(
        'href="https://photonedgeoptics.com/applications/laser-optics/"',
        'href="{}"'.format(url)
    ).replace(
        'href="/applications/laser-optics/"',
        'href="{}"'.format(url)
    )
    # Fix title for twitter
    head = head.replace(
        '<meta name="twitter:title" content="Laser Optics Solutions | PhotonEdge Optics">',
        '<meta name="twitter:title" content="{}">'.format(title)
    ).replace(
        '<meta name="twitter:description" content="Precision optical components engineered for laser optics solutions applications.">',
        '<meta name="twitter:description" content="{}">'.format(desc)
    )
    
    bc = '\n    <div class="breadcrumb-wrapper"><div class="container"><nav class="breadcrumb">\n'
    for label, href in breadcrumb_items:
        if href:
            bc += '        <a href="{}">{}</a>\n        <span class="breadcrumb-separator">/</span>\n'.format(href, label)
        else:
            bc += '        <span>{}</span>\n'.format(label)
    bc += '    </nav></div></div>\n'
    
    quote = '\n    <div class="request-quote-float"><a href="/contact.html" class="quote-btn"><span class="quote-icon">&#9993;</span><span>Request Engineering Review</span></a></div>\n'
    
    return head + "\n" + schema_json(schemas) + "\n" + NAV + bc + quote + body_content + "\n" + FOOTER

def faq_section(faqs):
    h = '\n    <section style="padding:60px 0;background:#f8fafc"><div class="container">\n'
    h += '        <h2 style="text-align:center;font-size:28px;color:#1e3a5f;margin-bottom:12px">Frequently Asked Questions</h2>\n'
    h += '        <p style="text-align:center;color:#64748b;margin-bottom:40px;max-width:600px;margin-left:auto;margin-right:auto">Common questions from optical engineers and procurement teams.</p>\n'
    h += '        <div style="max-width:800px;margin:0 auto">\n'
    for q, a in faqs:
        h += '            <div style="background:white;border-radius:12px;margin-bottom:16px;border:1px solid #e2e8f0;overflow:hidden">\n'
        h += '                <details><summary style="padding:20px 24px;font-weight:600;color:#1e293b;cursor:pointer;font-size:15px;list-style:none;display:flex;justify-content:space-between;align-items:center"><span>{}</span><span style="color:#3b82f6;font-size:20px;flex-shrink:0;margin-left:16px">+</span></summary>\n'.format(q)
        h += '                    <div style="padding:0 24px 20px;color:#475569;font-size:14px;line-height:1.7;border-top:1px solid #f1f5f9">{}</div>\n'.format(a)
        h += '                </details></div>\n'
    h += '        </div></div></section>\n'
    return h

def section(title, body):
    return '\n    <section style="padding:30px 0"><div class="container" style="max-width:800px">\n' + \
           '        <h2 style="font-size:24px;color:#1e3a5f;margin-bottom:20px;padding-bottom:12px;border-bottom:2px solid #e2e8f0">{}</h2>\n'.format(title) + \
           '        <div style="color:#334155;font-size:15px;line-height:1.8">{}</div>\n'.format(body) + \
           '    </div></section>\n'

def h3(t): return '<h3 style="font-size:18px;color:#1e3a5f;margin:28px 0 16px">{}</h3>'.format(t)
def p(t): return '<p>{}</p>'.format(t)
def ul(items): return '<ul style="padding-left:20px;margin:12px 0">' + ''.join('<li style="margin-bottom:8px">{}</li>'.format(i) for i in items) + '</ul>'
def ol(items): return '<ol style="padding-left:20px;margin:12px 0">' + ''.join('<li style="margin-bottom:10px">{}</li>'.format(i) for i in items) + '</ol>'
def callout(color, title, text):
    colors = {'blue': ('#eff6ff','#3b82f6','#1e40af','Key Principle'), 'yellow': ('#fef3c7','#d97706','#92400e','Common Mistake'), 'red': ('#fef2f2','#dc2626','#991b1b','Warning'), 'green': ('#f0fdf4','#16a34a','#166534','Summary')}
    bg, border, tc, default_title = colors.get(color, colors['blue'])
    if not title: title = default_title
    return '<div style="background:{};border-left:4px solid {};padding:20px 24px;border-radius:0 8px 8px 0;margin:24px 0"><strong style="color:{}">{}:</strong> {}</div>'.format(bg, border, tc, title, text)

def cta():
    return '''
    <section style="padding:70px 0;background:linear-gradient(135deg,#1e3a5f 0%,#2d5a87 100%);text-align:center;color:white">
        <div class="container">
            <h2 style="color:white;margin-bottom:14px;font-size:28px">Need Help Selecting Optical Components?</h2>
            <p style="color:rgba(255,255,255,0.9);margin-bottom:30px;font-size:16px;max-width:550px;margin-left:auto;margin-right:auto">Send us your requirements. Our engineers respond within 24 hours.</p>
            <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
                <a href="/contact.html" class="btn btn-primary" style="padding:14px 32px;border-radius:8px;font-size:15px;background:white;color:#1e3a5f;text-decoration:none;font-weight:600">Request Engineering Review</a>
                <a href="/ai-optical-engineer.html" class="btn" style="padding:14px 32px;border-radius:8px;font-size:15px;border:1px solid rgba(255,255,255,0.4);color:white;text-decoration:none">Ask AI Optical Engineer</a>
            </div>
        </div>
    </section>'''

def related(products):
    h = '\n    <section style="padding:50px 0;border-top:1px solid #e2e8f0"><div class="container">\n'
    h += '        <h3 style="font-size:22px;color:#1e3a5f;margin-bottom:24px;text-align:center">Related PhotonEdge Products</h3>\n'
    h += '        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;max-width:900px;margin:0 auto">\n'
    for name, url in products:
        h += '            <a href="{}" style="display:block;background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:20px;text-decoration:none;color:#1e293b"><div style="font-weight:600;font-size:14px;margin-bottom:6px">{}</div><div style="font-size:12px;color:#3b82f6">View Product Details →</div></a>\n'.format(url, name)
    h += '        </div></div></section>\n'
    return h

def article_hero(tags, title, desc):
    h = '\n    <section style="padding:50px 0 30px;background:linear-gradient(to bottom,#f8fafc,white)"><div class="container" style="max-width:800px">\n'
    h += '        <div style="margin-bottom:16px"><span style="background:#1e3a5f;color:white;padding:4px 14px;border-radius:20px;font-size:12px;font-weight:600;letter-spacing:0.5px">APPLICATION NOTE</span></div>\n'
    h += '        <h1 style="font-size:32px;color:#1e3a5f;margin-bottom:16px;line-height:1.3">{}</h1>\n'.format(title)
    h += '        <p style="color:#475569;font-size:17px;line-height:1.7;margin-bottom:20px">{}</p>\n'.format(desc)
    h += '        <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:24px">'
    for t in tags:
        h += '<span style="background:#eff6ff;color:#1d4ed8;padding:4px 12px;border-radius:20px;font-size:12px;font-weight:500">{}</span>'.format(t)
    h += '</div>\n'
    h += '        <div style="display:flex;gap:24px;color:#94a3b8;font-size:13px;padding-bottom:24px;border-bottom:1px solid #e2e8f0">\n'
    h += '            <span>Published: August 23, 2026</span><span>By PhotonEdge Engineering Team</span><span>~8 min read</span>\n'
    h += '        </div>\n    </div></section>\n'
    return h

# ===================== APPLICATION NOTE DEFINITIONS =====================

NOTES = [
    {
        "slug": "ar-coating-specification-multi-wavelength",
        "title": "How to Specify AR Coatings for Multi-Wavelength Laser Systems",
        "desc": "A practical guide to specifying anti-reflection coatings for multi-wavelength laser systems. Covers coating design, material selection, damage thresholds, and verification.",
        "tags": ["Laser Optics", "Coatings", "AR Coating", "Multi-Wavelength"],
        "products": [("UV Fused Silica Windows", "/products/uv-fused-silica-window/"), ("Laser Line Mirrors", "/products/1064nm-laser-line-mirrors/"), ("BK7 Plano-Convex Lenses", "/products/bk7-plano-convex/")],
        "faq": [
            ("What is the difference between single-wavelength and broadband AR coatings?", "Single-wavelength AR coatings are optimized for minimum reflection at one specific wavelength (typically <0.1% R). Broadband coatings maintain low reflectance across a range (e.g., 400-700nm), but achieve higher residual R (typically 0.25-0.5% per surface). For multi-wavelength systems, multi-band coatings combine transmission bands at specific lines."),
            ("What laser damage threshold should I expect from AR coatings?", "Standard IAD coatings on fused silica typically achieve 10-20 J/cm² at 1064nm (10ns pulse). For CW applications, the thermal threshold is typically >10 kW/cm². Always specify wavelength, pulse duration or CW power density, and beam diameter."),
            ("Can AR coatings work at angles other than 0°?", "Yes, but the design must account for the angle. Coatings optimized for 0° shift to shorter wavelengths at oblique angles (~5-15nm at 15°). For fixed-angle optics, specify the AOI in coating requirements."),
            ("How do I verify AR coating performance?", "Use a UV-VIS-NIR spectrophotometer to measure transmission/reflectance. For production, compare incident vs transmitted power at each wavelength with a calibrated power meter."),
            ("What durability can I expect from optical coatings?", "Modern IAD and IBS coatings withstand MIL-PRF-13830B adhesion tests, humidity (95% RH, 48hr), and temperature cycling (-40°C to +85°C). For harsh environments, specify protective overcoats."),
            ("Should I coat both surfaces?", "For windows and intra-cavity optics, coat both surfaces to prevent etalon effects. For beam splitters, typically only the functional surface receives the coating.")
        ],
        "content_fn": None  # Will be generated
    },
    {
        "slug": "optical-window-material-selection-harsh-environments",
        "title": "Optical Window Material Selection for Harsh Environments",
        "desc": "Engineering guide for selecting window materials for extreme temperatures, chemical exposure, high pressure, vacuum, and abrasion. Covers sapphire, ZnSe, CaF2, fused silica.",
        "tags": ["Materials", "Windows", "Harsh Environment", "Sapphire", "ZnSe"],
        "products": [("Sapphire Windows", "/products/sapphire-window/"), ("ZnSe Windows", "/products/znse-window/"), ("UV Fused Silica Windows", "/products/uv-fused-silica-window/")],
        "faq": [
            ("When should I choose sapphire over fused silica?", "Choose sapphire for superior hardness (9 Mohs — 5x harder than silica), better thermal conductivity (35 vs 1.4 W/m·K), or operation above 1000°C. Fused silica is better for UV <200nm, lower cost, or larger sizes."),
            ("What window material works for CO2 lasers at 10.6 μm?", "ZnSe is standard — >68% transmission at 10.6μm uncoated. For lower-power systems, silicon is a cheaper alternative."),
            ("Can windows survive autoclave sterilization?", "Sapphire handles autoclave conditions (121°C, 2 atm) indefinitely. Fused silica also survives. CaF2 is not recommended for repeated autoclave cycling."),
            ("Best window material for vacuum chambers?", "Fused silica and BK7 are standard for vacuum windows. Calculate thickness based on diameter, pressure differential, and safety factor of 4:1 minimum."),
            ("How to specify windows for abrasive environments?", "Sapphire is first choice (9H hardness). For large sizes, use chemically strengthened glass with protective coating."),
            ("What temperature limits for optical windows?", "BK7: ~350°C continuous. Fused silica: >1000°C. Sapphire: to 1800°C. ZnSe: ~150°C. CaF2: ~400°C. Always check coating limits too.")
        ],
        "content_fn": None
    },
    {
        "slug": "surface-quality-scratch-dig-explained",
        "title": "Surface Quality Specifications: Understanding Scratch-Dig and Beyond",
        "desc": "Complete guide to optical surface quality — from MIL-PRF-13830B scratch-dig to ISO 10110-7. Learn to specify the right quality without over-specifying cost.",
        "tags": ["Quality", "Surface Finish", "Scratch-Dig", "ISO 10110"],
        "products": [("Precision Flat Mirrors", "/products/precision-flat-mirrors/"), ("Achromatic Doublet Lenses", "/products/achromatic-doublet/"), ("Right Angle Prisms", "/products/right-angle-prism/")],
        "faq": [
            ("What does '60-40 scratch-dig' mean?", "Per MIL-PRF-13830B: max scratch width = 0.6mm (60 × 0.01), max dig diameter = 0.4mm (40 × 0.01). Lower = finer. 80-50 economy, 60-40 standard, 40-20 precision, 20-10 high precision."),
            ("How is surface quality inspected?", "Visual comparison against calibrated reference standards under dark-field illumination at 45°. Inherently subjective — specify quantitative Ra for critical applications."),
            ("When to use ISO 10110-7 vs MIL-PRF-13830B?", "ISO 10110-7 for European customers or ISO quality systems. MIL-PRF-13830B for US military/aerospace. Many modern specs reference both."),
            ("Does surface quality affect laser performance?", "Yes — scratches reduce laser damage threshold. A 20-10 surface can have 2-3x higher LDT than 60-40 at the same coating."),
            ("How much does tighter surface quality cost?", "80-50 to 60-40: +10-15%. 60-40 to 40-20: +30-50%. 40-20 to 20-10: +100-200%. Always specify the loosest grade your application allows."),
            ("Can I specify surface quality without scratch-dig?", "Yes. ISO 10110-7 offers 'N' classification. You can also specify surface roughness (Ra) or total integrated scatter (TIS) instead.")
        ],
        "content_fn": None
    },
    {
        "slug": "beam-expander-design-considerations",
        "title": "Beam Expander Design Considerations for UV/VIS/NIR Applications",
        "desc": "Engineering considerations for beam expander systems across UV, visible, and near-IR. Covers Galilean vs Keplerian designs, materials, coatings, and alignment.",
        "tags": ["Beam Expanders", "Laser Optics", "UV", "VIS", "NIR"],
        "products": [("BK7 Plano-Convex Lenses", "/products/bk7-plano-convex/"), ("UV Fused Silica PCX", "/products/uv-fused-silica-plano-convex/"), ("Achromatic Doublet Lenses", "/products/achromatic-doublet/")],
        "faq": [
            ("Galilean or Keplerian?", "Galilean (negative+positive): shorter, no internal focus, safer for high-power. Keplerian (positive+positive): has internal focus for spatial filtering but longer. Most industrial applications prefer Galilean."),
            ("What material for beam expander lenses?", "UV (<350nm): UV fused silica. VIS (400-700nm): BK7 is cost-effective. NIR: BK7 works, fused silica for high-power."),
            ("What magnification is typical?", "Common: 2x, 3x, 5x, 10x. Lower (2-3x) easier to align. Higher (5-10x) needs better input beam quality."),
            ("How critical is alignment?", "Very. Typical tolerance: centering ±50μm, tilt ±1 arcmin, spacing ±100μm. Misalignment causes beam walk-off and pointing instability."),
            ("Do I need AR coatings?", "Yes. Without AR: ~15% loss on 4 surfaces. With AR (<0.25%/surface): ~1% loss."),
            ("What input beam quality is needed?", "Output quality = input × magnification. For clean output, input should be M² < 1.3 with circular cross-section.")
        ],
        "content_fn": None
    },
    {
        "slug": "optics-for-vacuum-and-cleanroom",
        "title": "Selecting Optical Components for High-Vacuum and Cleanroom Environments",
        "desc": "Guide to specifying optics for vacuum chambers, cleanrooms, and controlled environments. Covers outgassing, bake-out compatibility, and contamination control.",
        "tags": ["Vacuum", "Cleanroom", "Semiconductor", "Space Optics"],
        "products": [("UV Fused Silica Windows", "/products/uv-fused-silica-window/"), ("CaF2 Windows", "/products/caf2-window/"), ("Sapphire Windows", "/products/sapphire-window/")],
        "faq": [
            ("What makes an optic 'vacuum-compatible'?", "Low outgassing, stable dimensions, vacuum-compatible coatings. Fused silica, sapphire, and most glasses are inherently compatible. Mounting hardware and adhesives must also be vacuum-rated."),
            ("Can standard optics be used in Class 100 cleanrooms?", "Yes, if properly cleaned and packaged. Specify 'cleanroom compatible' for cleanroom-grade cleaning and packaging."),
            ("What is bake-out and which optics survive it?", "Heating to 150-300°C to drive off adsorbed gases. Fused silica, sapphire, CaF2 survive standard bake-out. BK7 survives <200°C."),
            ("How to prevent contamination in vacuum?", "Clean assembly protocols: powder-free gloves, cleanroom wipes, laminar flow hoods. Avoid adhesives near optical surfaces."),
            ("What outgassing spec for space optics?", "ASTM E595: TML < 1.0%, CVCM < 0.10%. Most glasses and oxide coatings meet this. Request lot-specific test data."),
            ("How does vacuum affect optical adhesives?", "Standard epoxies outgas significantly. Use space-qualified epoxies (EPO-TEK 353ND-T), glass frit, or mechanical retention.")
        ],
        "content_fn": None
    }
]

# ===================== CONTENT GENERATORS =====================

def gen_an001():
    return article_hero(NOTES[0]["tags"], NOTES[0]["title"], NOTES[0]["desc"]) + \
    section("Introduction",
        p("Multi-wavelength laser systems require optical components that perform at two or more discrete wavelengths simultaneously. Standard single-wavelength AR coatings cannot meet this requirement.") +
        h3("Understanding the Challenge") +
        p("AR coatings work by destructive interference — thin film layers with precise thicknesses create reflected waves that cancel. A coating for 532nm won't perform at 1064nm. For multi-wavelength systems, you need coatings with 20-40+ layers instead of 4-8 for single-wavelength.") +
        callout("blue", "Key Principle", "The more wavelengths and broader bandwidth needed, the more layers required. More layers = higher cost, longer production, and potentially lower LDT. Specify only the wavelengths your system actually needs.")
    ) + \
    section("Coating Types", 
        '<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:14px"><thead><tr style="background:#f1f5f9"><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">Type</th><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">Best For</th><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">Typical R</th><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">Layers</th></tr></thead><tbody>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0"><strong>Dual-band AR</strong></td><td style="padding:12px;border:1px solid #e2e8f0">2 wavelengths (532+1064nm)</td><td style="padding:12px;border:1px solid #e2e8f0"><0.25% each λ</td><td style="padding:12px;border:1px solid #e2e8f0">15-25</td></tr>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0"><strong>Tri-band AR</strong></td><td style="padding:12px;border:1px solid #e2e8f0">3 wavelengths (355+532+1064nm)</td><td style="padding:12px;border:1px solid #e2e8f0"><0.5% each λ</td><td style="padding:12px;border:1px solid #e2e8f0">25-40</td></tr>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0"><strong>Broadband AR</strong></td><td style="padding:12px;border:1px solid #e2e8f0">Continuous band (400-700nm)</td><td style="padding:12px;border:1px solid #e2e8f0"><0.25% avg</td><td style="padding:12px;border:1px solid #e2e8f0">10-20</td></tr>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0"><strong>Dichroic</strong></td><td style="padding:12px;border:1px solid #e2e8f0">Transmit some λ, reflect others</td><td style="padding:12px;border:1px solid #e2e8f0">T>95% pass, R>99% stop</td><td style="padding:12px;border:1px solid #e2e8f0">40-80+</td></tr>' +
        '</tbody></table>'
    ) + \
    section("Writing a Coating Specification",
        p("Include these elements to prevent costly back-and-forth:") +
        ol([
            "<strong>Wavelengths and bandwidth:</strong> Each wavelength with acceptable bandwidth (e.g., 532nm ±5nm)",
            "<strong>Maximum reflectance:</strong> R% per surface at each wavelength (e.g., <0.25% at 532nm)",
            "<strong>Angle of incidence:</strong> Operating angle (0° or specify exact angle)",
            "<strong>Laser damage threshold:</strong> J/cm² (pulsed) or kW/cm² (CW) at your wavelength and pulse duration",
            "<strong>Environmental requirements:</strong> Lab, industrial, or extreme (outdoor/space)",
            "<strong>Substrate material:</strong> BK7, UV fused silica, CaF2 — affects coating material choices"
        ]) +
        callout("yellow", "Common Mistake", 'Specifying "broadband AR 400-1100nm" when your system uses 3 discrete wavelengths. Instead specify "dual-band AR at 532nm ±10nm and 1064nm ±10nm" for simpler, cheaper, higher-performance results.')
    ) + \
    section("Deposition: IAD vs IBS",
        '<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:14px"><thead><tr style="background:#f1f5f9"><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">Parameter</th><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">IAD</th><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">IBS</th></tr></thead><tbody>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0">Surface roughness</td><td style="padding:12px;border:1px solid #e2e8f0">0.3-0.5nm Ra</td><td style="padding:12px;border:1px solid #e2e8f0"><0.2nm Ra</td></tr>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0">LDT (1064nm)</td><td style="padding:12px;border:1px solid #e2e8f0">10-20 J/cm²</td><td style="padding:12px;border:1px solid #e2e8f0">30-50 J/cm²</td></tr>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0">Cost</td><td style="padding:12px;border:1px solid #e2e8f0">Standard</td><td style="padding:12px;border:1px solid #e2e8f0">2-3x IAD</td></tr>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0">Best for</td><td style="padding:12px;border:1px solid #e2e8f0">Most applications</td><td style="padding:12px;border:1px solid #e2e8f0">High-power lasers, metrology</td></tr>' +
        '</tbody></table>'
    ) + \
    section("Verification",
        p("When receiving coated optics, verify before installation:") +
        ol([
            "<strong>Spectral measurement:</strong> UV-VIS-NIR spectrophotometer to measure transmission at design wavelengths",
            "<strong>Visual inspection:</strong> Under white light at 45°, AR surfaces show characteristic residual color — should be uniform across clear aperture",
            "<strong>Power throughput test:</strong> Measure input vs transmitted power at each wavelength, calculate actual loss per surface",
            "<strong>Laser damage test:</strong> Request witness samples, perform 1-on-1 or R-on-1 testing per ISO 21254"
        ]) +
        callout("green", "Summary", "Multi-wavelength AR coatings are proven technology. Write a clear specification stating exact wavelengths, max reflectance, and power requirements. Don't over-specify — a coating designed for your exact needs will be cheaper, more durable, and higher-performing.")
    )

def gen_an002():
    return article_hero(NOTES[1]["tags"], NOTES[1]["title"], NOTES[1]["desc"]) + \
    section("The Selection Framework",
        p("Window material selection balances five requirements: optical transmission, mechanical strength, thermal performance, chemical resistance, and cost.") +
        p("No single material excels in all five. The decision is about finding the best compromise for your specific application.")
    ) + \
    section("Material Comparison",
        '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:13px;min-width:700px"><thead><tr style="background:#f1f5f9"><th style="padding:10px 12px;border:1px solid #e2e8f0;color:#1e3a5f">Property</th><th style="padding:10px;border:1px solid #e2e8f0;color:#1e3a5f;text-align:center">BK7</th><th style="padding:10px;border:1px solid #e2e8f0;color:#1e3a5f;text-align:center">Fused Silica</th><th style="padding:10px;border:1px solid #e2e8f0;color:#1e3a5f;text-align:center">Sapphire</th><th style="padding:10px;border:1px solid #e2e8f0;color:#1e3a5f;text-align:center">CaF2</th><th style="padding:10px;border:1px solid #e2e8f0;color:#1e3a5f;text-align:center">ZnSe</th></tr></thead><tbody>' +
        '<tr><td style="padding:10px 12px;border:1px solid #e2e8f0"><strong>Transmission</strong></td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">350-2000nm</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">180-2100nm</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">150-5500nm</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">130-9000nm</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">500-20000nm</td></tr>' +
        '<tr><td style="padding:10px 12px;border:1px solid #e2e8f0"><strong>Hardness (Mohs)</strong></td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">~6</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">~6</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">9</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">3</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">~4</td></tr>' +
        '<tr><td style="padding:10px 12px;border:1px solid #e2e8f0"><strong>Max temp</strong></td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">~350°C</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">>1000°C</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">~1800°C</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">~400°C</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">~150°C</td></tr>' +
        '<tr><td style="padding:10px 12px;border:1px solid #e2e8f0"><strong>Thermal shock</strong></td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">Moderate</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">Excellent</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">Excellent</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">Poor</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">Good</td></tr>' +
        '<tr><td style="padding:10px 12px;border:1px solid #e2e8f0"><strong>Chemical resistance</strong></td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">Good</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">Excellent</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">Excellent</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">Poor</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">Good</td></tr>' +
        '<tr><td style="padding:10px 12px;border:1px solid #e2e8f0"><strong>Relative cost</strong></td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">$</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">$$</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">$$$</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">$$$$</td><td style="padding:10px;border:1px solid #e2e8f0;text-align:center">$$$$</td></tr>' +
        '</tbody></table></div>'
    ) + \
    section("Decision Matrix",
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:20px 0">' +
        '<div style="background:#fef3c7;border-radius:10px;padding:20px"><h4 style="color:#92400e;margin-bottom:12px">High Temperature (>500°C)</h4><p style="font-size:13px;margin:0"><strong>Best:</strong> Sapphire. <strong>Good:</strong> Fused silica. <strong>Avoid:</strong> BK7, ZnSe</p></div>' +
        '<div style="background:#dbeafe;border-radius:10px;padding:20px"><h4 style="color:#1e40af;margin-bottom:12px">Hardness / Abrasion</h4><p style="font-size:13px;margin:0"><strong>Best:</strong> Sapphire (Mohs 9). <strong>Good:</strong> Fused silica. <strong>Avoid:</strong> CaF2, ZnSe</p></div>' +
        '<div style="background:#fce7f3;border-radius:10px;padding:20px"><h4 style="color:#9d174d;margin-bottom:12px">Chemical Exposure</h4><p style="font-size:13px;margin:0"><strong>Best:</strong> Sapphire. <strong>Good:</strong> Fused silica (avoid HF). <strong>Special:</strong> CaF2 for HF</p></div>' +
        '<div style="background:#d1fae5;border-radius:10px;padding:20px"><h4 style="color:#065f46;margin-bottom:12px">Thermal Shock</h4><p style="font-size:13px;margin:0"><strong>Best:</strong> Fused silica. <strong>Good:</strong> Sapphire. <strong>Avoid:</strong> CaF2</p></div>' +
        '</div>'
    ) + \
    section("Thickness Calculation",
        p("For flat windows under pressure differential, use: <code style='background:#f1f5f9;padding:2px 8px;border-radius:4px'>t = K × D × √(ΔP / σ)</code>") +
        p("Always apply safety factor ≥ 4:1. For vacuum, atmospheric pressure (101.3 kPa) acts on the window — a 50mm aperture sees ~200N force.") +
        callout("red", "Critical", "This simplified formula assumes uniform pressure on a flat disc. For critical applications, have thickness verified by a qualified engineer and perform proof pressure testing.")
    )

def gen_an003():
    return article_hero(NOTES[2]["tags"], NOTES[2]["title"], NOTES[2]["desc"]) + \
    section("What Are Scratch-Dig Numbers?",
        p("MIL-PRF-13830B uses two numbers: scratch width (× 0.01mm) and dig diameter (× 0.01mm). '60-40' means max scratch width 0.6mm, max dig diameter 0.4mm.") +
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:20px 0"><div style="background:#eff6ff;border-radius:10px;padding:20px"><h4 style="color:#1e40af">First Number: Scratch</h4><p style="font-size:13px;margin:0">Scratch number × 0.01mm = max width. "60" = 0.6mm max width.</p></div><div style="background:#fef3c7;border-radius:10px;padding:20px"><h4 style="color:#92400e">Second Number: Dig</h4><p style="font-size:13px;margin:0">Dig number × 0.01mm = max diameter. "40" = 0.4mm max diameter.</p></div></div>'
    ) + \
    section("Common Grades & Cost Impact",
        '<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:14px"><thead><tr style="background:#f1f5f9"><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">Grade</th><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">Use</th><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">Cost</th><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">Applications</th></tr></thead><tbody>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0"><strong>80-50</strong></td><td style="padding:12px;border:1px solid #e2e8f0">Economy</td><td style="padding:12px;border:1px solid #e2e8f0">Base</td><td style="padding:12px;border:1px solid #e2e8f0">Windows, beam steering</td></tr>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0"><strong>60-40</strong></td><td style="padding:12px;border:1px solid #e2e8f0">Standard</td><td style="padding:12px;border:1px solid #e2e8f0">+10-15%</td><td style="padding:12px;border:1px solid #e2e8f0">Imaging (f/8+), mirrors, prisms</td></tr>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0"><strong>40-20</strong></td><td style="padding:12px;border:1px solid #e2e8f0">Precision</td><td style="padding:12px;border:1px solid #e2e8f0">+30-50%</td><td style="padding:12px;border:1px solid #e2e8f0">Imaging (f/4+), laser optics</td></tr>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0"><strong>20-10</strong></td><td style="padding:12px;border:1px solid #e2e8f0">High precision</td><td style="padding:12px;border:1px solid #e2e8f0">+100-200%</td><td style="padding:12px;border:1px solid #e2e8f0">High-power laser, lithography</td></tr>' +
        '</tbody></table>' +
        callout("blue", "Rule of Thumb", "Every step finer adds 30-100% polishing cost. 60-40 to 40-20 is the most common over-specification trap.")
    ) + \
    section("When Does It Matter?",
        p("<strong>High impact:</strong> High-power laser (scratches reduce LDT), precision imaging at f/2 or faster, interferometric surfaces.") +
        p("<strong>Low impact:</strong> Non-imaging windows, mirrors at f/8+, prisms in fold mirrors, any defect smaller than the Airy disk.")
    ) + \
    section("Beyond Scratch-Dig",
        ul([
            "<strong>Surface roughness (Ra/RMS):</strong> Measured with profilometer. 0.5-2nm standard, <0.2nm superpolish. Directly correlates with scatter.",
            "<strong>Total Integrated Scatter (TIS):</strong> Ratio of scattered to total reflected light. TIS < 0.1% for precision optics.",
            "<strong>ISO 10110-7 'N' count:</strong> Specifies max defects per area. More objective than scratch-dig for production QC."
        ])
    ) + \
    section("Practical Advice",
        callout("green", "Recommendation", "For most commercial applications, 60-40 with visual inspection per MIL-PRF-13830B is sufficient. Only move to tighter grades when your application specifically requires it. For production consistency, add quantitative Ra or TIS alongside scratch-dig.")
    )

def gen_an004():
    return article_hero(NOTES[3]["tags"], NOTES[3]["title"], NOTES[3]["desc"]) + \
    section("Galilean vs. Keplerian",
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin:20px 0">' +
        '<div style="background:#dbeafe;border-radius:10px;padding:20px"><h4 style="color:#1e40af">Galilean (Neg-Pos)</h4><ul style="font-size:13px;padding-left:16px;margin:0"><li>Shorter length</li><li>No internal focus (safer for high-power)</li><li>Inverted image</li><li>Best for: industrial lasers, beam delivery</li></ul></div>' +
        '<div style="background:#fef3c7;border-radius:10px;padding:20px"><h4 style="color:#92400e">Keplerian (Pos-Pos)</h4><ul style="font-size:13px;padding-left:16px;margin:0"><li>Longer length</li><li>Internal focus (spatial filtering)</li><li>Upright image</li><li>Best for: precision, research</li></ul></div></div>'
    ) + \
    section("Material Selection",
        '<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:14px"><thead><tr style="background:#f1f5f9"><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">Range</th><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">Material</th><th style="padding:12px;border:1px solid #e2e8f0;color:#1e3a5f">Why</th></tr></thead><tbody>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0">UV (200-350nm)</td><td style="padding:12px;border:1px solid #e2e8f0"><strong>UV Fused Silica</strong></td><td style="padding:12px;border:1px solid #e2e8f0">High UV transmission, low fluorescence</td></tr>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0">VIS (400-700nm)</td><td style="padding:12px;border:1px solid #e2e8f0"><strong>BK7</strong></td><td style="padding:12px;border:1px solid #e2e8f0">Low cost, good homogeneity</td></tr>' +
        '<tr><td style="padding:12px;border:1px solid #e2e8f0">NIR (700-1100nm)</td><td style="padding:12px;border:1px solid #e2e8f0"><strong>BK7 or Fused Silica</strong></td><td style="padding:12px;border:1px solid #e2e8f0">Silica for high-power, BK7 for economy</td></tr>' +
        '</tbody></table>' +
        callout("red", "UV Warning", "Never use BK7 below 320nm. It has increasing absorption and can solarize under UV. Always use UV-grade fused silica for UV beam expanders.")
    ) + \
    section("Design Parameters",
        ul([
            "<strong>Magnification:</strong> M = f2/f1. Typical: 2x, 3x, 5x, 10x.",
            "<strong>Lens diameter:</strong> Output lens ≥ M × input beam diameter × 1.2.",
            "<strong>Spacing tolerance:</strong> ±100μm for M≤5x, ±50μm for M>5x.",
            "<strong>Wavefront quality:</strong> λ/10 PV for diffraction-limited, λ/4 for non-critical.",
            "<strong>Coatings:</strong> AR on all 4 surfaces. Without AR: ~15% loss. With AR: ~1%."
        ])
    ) + \
    section("Alignment",
        ol([
            "<strong>Coarse alignment:</strong> Both lenses on kinematic mounts, centers on optical axis.",
            "<strong>Spacing adjustment:</strong> Adjust separation while monitoring output diameter. Minimum divergence change = correct spacing.",
            "<strong>Fine tip-tilt:</strong> Adjust input lens while watching beam profile — goal is circular, symmetric beam.",
            "<strong>Verify:</strong> Check diameter at 0.5m and 2m. Consistent = properly collimated.",
            "<strong>Lock:</strong> Lock all mounts after alignment. Mark positions for future reference."
        ])
    )

def gen_an005():
    return article_hero(NOTES[4]["tags"], NOTES[4]["title"], NOTES[4]["desc"]) + \
    section("Why Standard Optics Fail in Vacuum",
        p("Every material contains adsorbed gases. In vacuum, these outgas and become contaminants — raising chamber pressure and depositing volatile condensables on nearby optics.") +
        callout("blue", "Key Insight", "The substrate is rarely the problem — it's coatings, adhesives, markings, cleaning residues, and packaging that introduce contaminants. Specify the entire assembly as vacuum-compatible.")
    ) + \
    section("Vacuum-Compatible Materials",
        '<table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:13px"><thead><tr style="background:#f1f5f9"><th style="padding:10px;border:1px solid #e2e8f0;color:#1e3a5f">Material</th><th style="padding:10px;border:1px solid #e2e8f0;color:#1e3a5f">TML</th><th style="padding:10px;border:1px solid #e2e8f0;color:#1e3a5f">CVCM</th><th style="padding:10px;border:1px solid #e2e8f0;color:#1e3a5f">Bake-out</th><th style="padding:10px;border:1px solid #e2e8f0;color:#1e3a5f">Verdict</th></tr></thead><tbody>' +
        '<tr><td style="padding:10px;border:1px solid #e2e8f0"><strong>Fused Silica</strong></td><td style="padding:10px;border:1px solid #e2e8f0"><0.1%</td><td style="padding:10px;border:1px solid #e2e8f0"><0.01%</td><td style="padding:10px;border:1px solid #e2e8f0">300°C</td><td style="padding:10px;border:1px solid #e2e8f0;color:#16a34a">Excellent</td></tr>' +
        '<tr><td style="padding:10px;border:1px solid #e2e8f0"><strong>Sapphire</strong></td><td style="padding:10px;border:1px solid #e2e8f0"><0.05%</td><td style="padding:10px;border:1px solid #e2e8f0"><0.01%</td><td style="padding:10px;border:1px solid #e2e8f0">400°C</td><td style="padding:10px;border:1px solid #e2e8f0;color:#16a34a">Excellent</td></tr>' +
        '<tr><td style="padding:10px;border:1px solid #e2e8f0"><strong>BK7</strong></td><td style="padding:10px;border:1px solid #e2e8f0">~0.3%</td><td style="padding:10px;border:1px solid #e2e8f0"><0.05%</td><td style="padding:10px;border:1px solid #e2e8f0">200°C</td><td style="padding:10px;border:1px solid #e2e8f0;color:#ca8a04">Good</td></tr>' +
        '<tr><td style="padding:10px;border:1px solid #e2e8f0"><strong>Standard epoxy</strong></td><td style="padding:10px;border:1px solid #e2e8f0">5-20%</td><td style="padding:10px;border:1px solid #e2e8f0">1-5%</td><td style="padding:10px;border:1px solid #e2e8f0">80°C</td><td style="padding:10px;border:1px solid #e2e8f0;color:#dc2626">Not compatible</td></tr>' +
        '<tr><td style="padding:10px;border:1px solid #e2e8f0"><strong>EPO-TEK 353ND-T</strong></td><td style="padding:10px;border:1px solid #e2e8f0"><0.5%</td><td style="padding:10px;border:1px solid #e2e8f0"><0.05%</td><td style="padding:10px;border:1px solid #e2e8f0">150°C</td><td style="padding:10px;border:1px solid #e2e8f0;color:#ca8a04">Space-grade</td></tr>' +
        '</tbody></table>' +
        '<p style="font-size:12px;color:#64748b">TML/CVCM per ASTM E595. Request lot-specific data for critical applications.</p>'
    ) + \
    section("Cleanroom & Coatings",
        p("<strong>Oxide coatings (SiO2, Ta2O5, Al2O3, HfO2):</strong> Excellent vacuum compatibility. Dense, low porosity.") +
        p("<strong>Fluoride coatings (MgF2, CaF2):</strong> Acceptable but more porous. Request post-coating bake-out.") +
        p("<strong>Avoid:</strong> Organic coatings, epoxy edge seals, evaporation-deposited coatings without ion assist.")
    ) + \
    section("Contamination Control",
        ol([
            "Wear powder-free nitrile gloves — never bare hands",
            "Clean with electronic-grade IPA, applied with cleanroom wipes",
            "Avoid adhesives within 5mm of optical clear aperture",
            "Pre-bake optics at max rated temperature before assembly",
            "Install optics last, immediately before system pump-down"
        ]) +
        callout("green", "Summary", "Vacuum optics require attention to the full chain — substrate, coating, cleaning, adhesive, and packaging. Fused silica with oxide coatings is the safest choice. Always specify vacuum level and bake-out temperature.")
    )

CONTENT_FNS = [gen_an001, gen_an002, gen_an003, gen_an004, gen_an005]

# ===================== GENERATE PAGES =====================

for i, note in enumerate(NOTES):
    slug = note["slug"]
    title = note["title"]
    desc = note["desc"]
    url = "https://photonedgeoptics.com/application-notes/{}/".format(slug)
    
    breadcrumbs = [("Home", "/"), ("Application Notes", "/application-notes/"), (title, None)]
    
    schemas = [
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://photonedgeoptics.com/"},
            {"@type": "ListItem", "position": 2, "name": "Application Notes", "item": "https://photonedgeoptics.com/application-notes/"},
            {"@type": "ListItem", "position": 3, "name": title, "item": url}
        ]},
        {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "url": url,
         "author": {"@type": "Organization", "name": "PhotonEdge Optics"},
         "publisher": {"@type": "Organization", "name": "PhotonEdge Optics", "logo": {"@type": "ImageObject", "url": "https://photonedgeoptics.com/images/logo.webp"}},
         "datePublished": "2026-08-23", "dateModified": "2026-08-23"},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in note["faq"]
        ]}
    ]
    
    body = CONTENT_FNS[i]() + faq_section(note["faq"]) + related(note["products"]) + cta()
    
    html = page(title, desc, url, breadcrumbs, schemas, body)
    
    out_path = os.path.join(AN_DIR, slug, "index.html")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        f.write(html)
    print("Generated: {} ({} bytes)".format(out_path, len(html)))

# ===================== INDEX PAGE =====================

index_url = "https://photonedgeoptics.com/application-notes/"
index_schemas = [
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://photonedgeoptics.com/"},
        {"@type": "ListItem", "position": 2, "name": "Application Notes", "item": index_url}
    ]},
    {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Application Notes", "url": index_url,
     "description": "Practical engineering guides for optical component selection and application."}
]

cards = ""
for note in NOTES:
    tags_h = "".join(['<span style="background:#eff6ff;color:#1d4ed8;padding:3px 10px;border-radius:16px;font-size:11px;font-weight:500">{}</span>'.format(t) for t in note["tags"][:3]])
    cards += '<a href="/application-notes/{}/" style="display:block;background:white;border-radius:14px;border:1px solid #e2e8f0;padding:28px;text-decoration:none;color:inherit;box-shadow:0 1px 3px rgba(0,0,0,0.04)"><div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px">{}</div><h3 style="font-size:18px;color:#1e3a5f;margin-bottom:10px;line-height:1.4">{}</h3><p style="color:#64748b;font-size:14px;line-height:1.6;margin-bottom:14px">{}</p><span style="color:#3b82f6;font-size:13px;font-weight:500">Read Application Note →</span></a>\n'.format(
        note["slug"], tags_h, note["title"], note["desc"]
    )

index_body = '\n    <section style="padding:50px 0 30px;background:linear-gradient(to bottom,#f8fafc,white)"><div class="container"><div style="max-width:700px;margin:0 auto;text-align:center"><span style="background:#1e3a5f;color:white;padding:5px 16px;border-radius:20px;font-size:12px;font-weight:600">APPLICATION NOTES</span><h1 style="font-size:34px;color:#1e3a5f;margin:20px 0 14px;line-height:1.3">Practical Optical Engineering Guides</h1><p style="color:#475569;font-size:16px;line-height:1.7">Written by optical engineers for engineers. Real-world decisions about material selection, coating specs, surface quality, and system design.</p></div></div></section>\n'
index_body += '    <section style="padding:30px 0 60px"><div class="container"><div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:24px;max-width:1100px;margin:0 auto">' + cards + '</div></div></section>\n'
index_body += cta()

index_html = page(
    "Application Notes | Optical Engineering Guides | PhotonEdge Optics",
    "Practical engineering guides for selecting, specifying, and applying optical components.",
    index_url,
    [("Home", "/"), ("Application Notes", None)],
    index_schemas,
    index_body
)

index_path = os.path.join(AN_DIR, "index.html")
with open(index_path, 'w') as f:
    f.write(index_html)
print("Generated: {} ({} bytes)".format(index_path, len(index_html)))

print("\n=== All application notes generated ===")
print("Files created:")
for note in NOTES:
    p = os.path.join(AN_DIR, note["slug"], "index.html")
    print("  {} - {} bytes".format(p, os.path.getsize(p)))
print("  {} - {} bytes".format(index_path, os.path.getsize(index_path)))
