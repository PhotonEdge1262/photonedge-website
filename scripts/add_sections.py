#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Add Specification Checklist and Critical Parameters sections to all V146 product pages.
"""

import os
import re
import sys

BASE_DIR = "/tmp/v146-work/products"

CRITICAL_PARAMS = {
    "Lenses": ["Wavelength", "Focal Length", "Diameter", "Surface Quality", "Coating"],
    "Mirrors": ["Wavelength", "Reflectivity", "Surface Quality", "Flatness", "Damage Threshold"],
    "Windows": ["Wavelength", "Transmission", "Parallelism", "Surface Quality", "Material"],
    "Prisms": ["Wavelength", "Deviation Angle", "Material Dispersion", "Surface Quality"],
    "Filters": ["Center Wavelength", "Bandwidth", "OD", "Transmission", "Angle of Incidence"],
    "Beamsplitters": ["Split Ratio", "Wavelength", "Wavefront Distortion", "Surface Quality"],
    "Waveplates": ["Wavelength", "Retardance Accuracy", "Clear Aperture", "Damage Threshold"],
    "Polarizers": ["Extinction Ratio", "Wavelength", "Clear Aperture", "Damage Threshold"],
    "Laser Safety": ["OD Rating", "Wavelength Range", "Visible Light Transmission", "Comfort"],
    "Beam Expanders": ["Wavelength", "Expansion Ratio", "Beam Quality", "Input Beam Diameter"],
    "Optomechanics": ["Material", "Dimensional Accuracy", "Surface Flatness", "Thermal Stability"],
    "Custom Optics": ["Application", "Wavelength", "Geometry", "Surface Quality", "Coating"],
}

PRODUCT_TYPE_MAP = {
    "achromatic-doublet": "Lenses", "aspherical-lenses": "Lenses", "ball-lenses": "Lenses",
    "bi-concave-lenses": "Lenses", "bi-convex-lenses": "Lenses", "bk7-bi-concave": "Lenses",
    "bk7-bi-convex": "Lenses", "bk7-c-lenses": "Lenses", "bk7-negative-meniscus": "Lenses",
    "bk7-plano-concave": "Lenses", "bk7-plano-concave-cylindrical": "Lenses",
    "bk7-plano-convex": "Lenses", "bk7-plano-convex-cylindrical": "Lenses",
    "bk7-positive-meniscus": "Lenses", "bk7-rod-lenses": "Lenses", "bk7-ball-lenses": "Lenses",
    "c-mount-lenses": "Lenses", "caf2-plano-convex-lenses": "Lenses",
    "caf2-ultrafast-laser-optics": "Lenses", "cylindrical-lenses": "Lenses",
    "fused-silica-laser-lenses": "Lenses", "fused-silica-plano-convex-lenses": "Lenses",
    "germanium-infrared-lenses": "Lenses", "laser-beam-expanders": "Beam Expanders",
    "1064nm-laser-line-mirrors": "Mirrors", "bk7-optical-mirrors": "Mirrors",
    "broadband-dielectric-mirrors": "Mirrors", "dielectric-mirrors": "Mirrors",
    "enhanced-aluminum-mirrors": "Mirrors", "fused-silica-optical-mirrors": "Mirrors",
    "high-energy-laser-mirrors": "Mirrors", "high-power-laser-mirrors": "Mirrors",
    "laser-line-high-reflected-mirrors": "Mirrors", "dichroic-mirrors": "Mirrors",
    "concentric-mirror-frame": "Optomechanics",
    "bk7-windows": "Windows", "caf2-optical-windows": "Windows", "caf2-windows": "Windows",
    "custom-optical-windows": "Windows", "fused-silica-optical-windows": "Windows",
    "germanium-optical-windows": "Windows", "ge-windows": "Windows",
    "bk7-optical-prisms": "Prisms", "bk7-right-angle-prisms": "Prisms",
    "caf2-optical-prisms": "Prisms", "corner-cube-prisms": "Prisms",
    "corner-cube-retroreflectors": "Prisms", "dispersing-prisms": "Prisms",
    "dove-prisms": "Prisms", "equilateral-dispersing-prisms": "Prisms",
    "dichroic-filters": "Filters", "fixed-neutral-density-filters": "Filters",
    "ir-bandpass-filters": "Filters", "laser-line-filters": "Filters",
    "beamsplitter-plates": "Beamsplitters", "cube-beamsplitters": "Beamsplitters",
    "achromatic-waveplates": "Waveplates", "air-spaced-zero-order-waveplates": "Waveplates",
    "cemented-zero-order-waveplates": "Waveplates", "dual-wavelength-waveplates": "Waveplates",
    "glan-laser-prisms": "Polarizers", "glan-taylor-prisms": "Polarizers",
    "glan-thompson-prisms": "Polarizers", "glan-type-polarizers": "Polarizers",
    "ir-polarizers": "Polarizers", "laser-safety-goggles": "Laser Safety",
    "custom-optical-components": "Custom Optics",
}


def get_product_type(slug):
    return PRODUCT_TYPE_MAP.get(slug, "Custom Optics")


def build_spec_checklist_html():
    return """<section id="specification-checklist" style="padding:60px 0;background:#f8fafc;">
    <div style="max-width:900px;margin:0 auto;padding:0 24px;">
        <h2 style="font-size:28px;font-weight:700;color:#1e293b;margin-bottom:12px;">Before Requesting a Quote</h2>
        <p style="color:#64748b;font-size:16px;line-height:1.7;margin-bottom:32px;">To help us provide an accurate quotation, please prepare the following information. Not all fields are required &#x2014; send what you have, and our engineering team can help identify missing parameters.</p>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;">
            <div style="background:white;padding:20px;border-radius:8px;border:1px solid #e2e8f0;">
                <div style="font-size:14px;font-weight:600;color:#1e293b;margin-bottom:4px;">&#10003; Material</div>
                <div style="font-size:13px;color:#64748b;">BK7, fused silica, CaF&#x2082;, etc.</div>
            </div>
            <div style="background:white;padding:20px;border-radius:8px;border:1px solid #e2e8f0;">
                <div style="font-size:14px;font-weight:600;color:#1e293b;margin-bottom:4px;">&#10003; Dimensions</div>
                <div style="font-size:13px;color:#64748b;">Diameter, thickness, focal length</div>
            </div>
            <div style="background:white;padding:20px;border-radius:8px;border:1px solid #e2e8f0;">
                <div style="font-size:14px;font-weight:600;color:#1e293b;margin-bottom:4px;">&#10003; Wavelength</div>
                <div style="font-size:13px;color:#64748b;">Operating wavelength or range</div>
            </div>
            <div style="background:white;padding:20px;border-radius:8px;border:1px solid #e2e8f0;">
                <div style="font-size:14px;font-weight:600;color:#1e293b;margin-bottom:4px;">&#10003; Coating</div>
                <div style="font-size:13px;color:#64748b;">AR, HR, metallic, or uncoated</div>
            </div>
            <div style="background:white;padding:20px;border-radius:8px;border:1px solid #e2e8f0;">
                <div style="font-size:14px;font-weight:600;color:#1e293b;margin-bottom:4px;">&#10003; Surface Quality</div>
                <div style="font-size:13px;color:#64748b;">Scratch-dig, roughness</div>
            </div>
            <div style="background:white;padding:20px;border-radius:8px;border:1px solid #e2e8f0;">
                <div style="font-size:14px;font-weight:600;color:#1e293b;margin-bottom:4px;">&#10003; Quantity</div>
                <div style="font-size:13px;color:#64748b;">Prototype, low volume, or production</div>
            </div>
            <div style="background:white;padding:20px;border-radius:8px;border:1px solid #e2e8f0;">
                <div style="font-size:14px;font-weight:600;color:#1e293b;margin-bottom:4px;">&#10003; Application</div>
                <div style="font-size:13px;color:#64748b;">Laser, imaging, spectroscopy, etc.</div>
            </div>
            <div style="background:white;padding:20px;border-radius:8px;border:1px solid #e2e8f0;">
                <div style="font-size:14px;font-weight:600;color:#1e293b;margin-bottom:4px;">&#10003; Operating Environment</div>
                <div style="font-size:13px;color:#64748b;">Temperature, vacuum, cleanroom</div>
            </div>
        </div>
        <p style="color:#64748b;font-size:14px;line-height:1.7;margin-top:24px;font-style:italic;">Not sure about some specifications? Send what you have &#x2014; our engineering team will help identify the missing parameters and recommend appropriate values for your application.</p>
    </div>
</section>"""


def build_critical_params_html(product_type):
    params = CRITICAL_PARAMS.get(product_type, CRITICAL_PARAMS["Custom Optics"])
    spans = ""
    for p in params:
        spans += '<span style="background:white;padding:6px 12px;border-radius:4px;font-size:13px;color:#1e3a5f;border:1px solid #bfdbfe;">' + p + '</span>\n        '
    return """<div style="background:#eff6ff;border-left:4px solid #2563eb;padding:20px;margin-bottom:24px;border-radius:0 8px 8px 0;">
    <h3 style="font-size:16px;font-weight:700;color:#1e293b;margin-bottom:8px;">Critical Parameters for """ + product_type + """</h3>
    <p style="font-size:14px;color:#475569;line-height:1.7;margin-bottom:12px;">When specifying this product, these parameters most directly impact performance and cost:</p>
    <div style="display:flex;flex-wrap:wrap;gap:8px;">
        """ + spans.strip() + """
    </div>
</div>"""


def build_critical_params_js(product_type):
    params = CRITICAL_PARAMS.get(product_type, CRITICAL_PARAMS["Custom Optics"])
    type_zh_map = {
        "Lenses": "\u900f\u955c", "Mirrors": "\u53cd\u5c04\u955c", "Windows": "\u7a97\u53e3\u7247",
        "Prisms": "\u68f1\u955c", "Filters": "\u6ee4\u5149\u7247", "Beamsplitters": "\u5206\u5149\u955c",
        "Waveplates": "\u6ce2\u7247", "Polarizers": "\u504f\u632f\u5668", "Laser Safety": "\u6fc0\u5149\u9632\u62a4",
        "Beam Expanders": "\u6269\u675f\u955c", "Optomechanics": "\u5149\u673a\u4ef6", "Custom Optics": "\u5b9a\u5236\u5149\u5b66",
    }
    type_zh = type_zh_map.get(product_type, "\u5b9a\u5236\u5149\u5b66")

    lines = []
    lines.append('            // Critical Parameters callout')
    lines.append("            specsHtml += '<div style=\"background:#eff6ff;border-left:4px solid #2563eb;padding:20px;margin-bottom:24px;border-radius:0 8px 8px 0;\">';")
    lines.append("            specsHtml += '<h3 style=\"font-size:16px;font-weight:700;color:#1e293b;margin-bottom:8px;\">' + (lang === 'zh' ? '" + type_zh + " \u7684\u5173\u952e\u53c2\u6570' : 'Critical Parameters for " + product_type + "') + '</h3>';")
    lines.append("            specsHtml += '<p style=\"font-size:14px;color:#475569;line-height:1.7;margin-bottom:12px;\">' + (lang === 'zh' ? '\u6307\u5b9a\u8be5\u4ea7\u54c1\u65f6\uff0c\u8fd9\u4e9b\u53c2\u6570\u5bf9\u6027\u80fd\u548c\u6210\u672c\u5f71\u54cd\u6700\u5927\uff1a' : 'When specifying this product, these parameters most directly impact performance and cost:') + '</p>';")
    lines.append("            specsHtml += '<div style=\"display:flex;flex-wrap:wrap;gap:8px;\">';")
    for p in params:
        lines.append("            specsHtml += '<span style=\"background:white;padding:6px 12px;border-radius:4px;font-size:13px;color:#1e3a5f;border:1px solid #bfdbfe;\">' + '" + p + "' + '</span>';")
    lines.append("            specsHtml += '</div></div>';")
    return "\n".join(lines)


def classify_page(content):
    has_keys_comment = "<!-- Key Specifications -->" in content
    has_rfq_comment = "<!-- RFQ -->" in content
    has_specsHtml = "var specsHtml" in content
    has_inquiry_form = 'class="product-inquiry-form"' in content
    has_keys_text = "Key Specifications" in content
    # Check for actual RFQ section in HTML body (not just CSS)
    has_rfq_body = bool(re.search(r'class="[^"]*rfq-section-31[^"]*"[^>]*>.*?Request', content, re.DOTALL))
    has_rfq_h2 = "Request an Engineering Quote" in content
    has_faq_comment = "<!-- FAQ -->" in content
    has_faq_text = "Frequently Asked Questions" in content

    if has_keys_comment and has_rfq_comment:
        return "A"
    elif has_keys_comment and not has_rfq_comment:
        return "C"
    elif has_specsHtml and has_inquiry_form:
        return "D"
    elif has_keys_text and not has_keys_comment and not has_specsHtml:
        return "B"
    else:
        return "E"


def insert_checklist_a(content, checklist_html):
    if 'id="specification-checklist"' in content:
        return content, False
    marker = "    <!-- RFQ -->"
    if marker in content:
        content = content.replace(marker, checklist_html + "\n\n" + marker, 1)
        return content, True
    return content, False


def insert_checklist_b(content, checklist_html):
    if 'id="specification-checklist"' in content:
        return content, False
    # Insert before FAQ section (look for "Frequently Asked Questions" heading)
    pattern = r'(    <section style="padding:60px 0;background:white;">\s*\n\s*<div class="container" style="max-width:1200px;margin:0 auto;padding:0 20px;">\s*\n\s*<h2 class="section-title-31">Frequently Asked Questions</h2>)'
    match = re.search(pattern, content)
    if match:
        content = content.replace(match.group(0), checklist_html + "\n\n" + match.group(0), 1)
        return content, True
    # Fallback: insert before footer
    footer_marker = '        <footer class="footer">'
    if footer_marker in content:
        content = content.replace(footer_marker, checklist_html + "\n\n" + footer_marker, 1)
        return content, True
    return content, False


def insert_checklist_c(content, checklist_html):
    if 'id="specification-checklist"' in content:
        return content, False
    marker = "    <!-- FAQ -->"
    if marker in content:
        content = content.replace(marker, checklist_html + "\n\n" + marker, 1)
        return content, True
    return content, False


def insert_checklist_d(content, checklist_html):
    if 'id="specification-checklist"' in content:
        return content, False
    marker = '    <section class="product-inquiry-form" id="productInquiryForm"'
    if marker in content:
        content = content.replace(marker, checklist_html + "\n\n" + marker, 1)
        return content, True
    return content, False


def insert_params_a(content, callout_html):
    if "Critical Parameters for" in content:
        return content, False
    pattern = r'(<!-- Key Specifications -->\s*\n\s*<section class="product-section-31">\s*\n\s*<h2 class="section-title-31">Key Specifications</h2>\s*\n)'
    match = re.search(pattern, content)
    if match:
        pos = match.end()
        content = content[:pos] + "\n" + callout_html + "\n" + content[pos:]
        return content, True
    return content, False


def insert_params_b(content, callout_html):
    if "Critical Parameters for" in content:
        return content, False
    # These pages have <h2 class="section-title-31">Key Specifications</h2>
    pattern = r'(<h2 class="section-title-31">Key Specifications</h2>\s*\n)'
    match = re.search(pattern, content)
    if match:
        pos = match.end()
        content = content[:pos] + "\n" + callout_html + "\n" + content[pos:]
        return content, True
    return content, False


def insert_params_c(content, callout_html):
    if "Critical Parameters for" in content:
        return content, False
    pattern = r'(<!-- Key Specifications -->\s*\n\s*<section[^>]*>\s*\n\s*<h2>Key Specifications</h2>\s*\n)'
    match = re.search(pattern, content)
    if match:
        pos = match.end()
        content = content[:pos] + "\n" + callout_html + "\n" + content[pos:]
        return content, True
    # Fallback: just after <h2>Key Specifications</h2>
    pattern2 = r'(<h2>Key Specifications</h2>\s*\n)'
    match2 = re.search(pattern2, content)
    if match2:
        pos = match2.end()
        content = content[:pos] + "\n" + callout_html + "\n" + content[pos:]
        return content, True
    return content, False


def insert_params_d(content, js_code):
    if "Critical Parameters for" in content:
        return content, False
    pattern = r"(specsHtml \+= '<h3 class=\"specs-title\">' \+ \(lang === 'zh' \? '[^']*' : 'Technical Specifications'\) \+ '</h3>';\s*\n)"
    match = re.search(pattern, content)
    if match:
        pos = match.end()
        content = content[:pos] + "\n" + js_code + "\n" + content[pos:]
        return content, True
    return content, False


def process_all():
    results = {"A": [], "B": [], "C": [], "D": [], "E": []}
    errors = []
    checklist_html = build_spec_checklist_html()

    for slug in sorted(os.listdir(BASE_DIR)):
        filepath = os.path.join(BASE_DIR, slug, "index.html")
        if not os.path.isfile(filepath):
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        product_type = get_product_type(slug)
        group = classify_page(content)
        callout_html = build_critical_params_html(product_type)
        callout_js = build_critical_params_js(product_type)

        checklist_ok = False
        params_ok = False

        try:
            if group == "A":
                content, checklist_ok = insert_checklist_a(content, checklist_html)
                content, params_ok = insert_params_a(content, callout_html)
            elif group == "B":
                content, checklist_ok = insert_checklist_b(content, checklist_html)
                content, params_ok = insert_params_b(content, callout_html)
            elif group == "C":
                content, checklist_ok = insert_checklist_c(content, checklist_html)
                content, params_ok = insert_params_c(content, callout_html)
            elif group == "D":
                content, checklist_ok = insert_checklist_d(content, checklist_html)
                content, params_ok = insert_params_d(content, callout_js)
            else:
                # Group E - try best effort
                if 'id="specification-checklist"' not in content:
                    footer_marker = '        <footer class="footer">'
                    if footer_marker in content:
                        content = content.replace(footer_marker, checklist_html + "\n\n" + footer_marker, 1)
                        checklist_ok = True

            if checklist_ok or params_ok:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)

            results[group].append({
                "slug": slug, "type": product_type,
                "chk": checklist_ok, "prm": params_ok
            })

        except Exception as e:
            errors.append(slug + ": " + str(e))

    return results, errors


def main():
    print("=" * 70)
    print("V146: Adding Specification Checklist & Critical Parameters")
    print("=" * 70)

    results, errors = process_all()

    labels = {
        "A": "Full template (RFQ+KeySpec comments)",
        "B": "KeySpec text, no comments (static)",
        "C": "KeySpec comment, no RFQ",
        "D": "Dynamic JS template",
        "E": "Minimal/incomplete pages",
    }

    for grp in ["A", "B", "C", "D", "E"]:
        items = results[grp]
        print("\n--- GROUP %s: %s (%d pages) ---" % (grp, labels[grp], len(items)))
        for s in items:
            print("  %-40s | %-15s | chk:%s prm:%s" % (s["slug"], s["type"], s["chk"], s["prm"]))

    if errors:
        print("\n--- ERRORS ---")
        for e in errors:
            print("  " + e)

    total_pages = sum(len(results[g]) for g in ["A","B","C","D","E"])
    total_chk = sum(1 for g in ["A","B","C","D","E"] for s in results[g] if s["chk"])
    total_prm = sum(1 for g in ["A","B","C","D","E"] for s in results[g] if s["prm"])

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("Total pages: %d" % total_pages)
    print("  A:%d  B:%d  C:%d  D:%d  E:%d" % (
        len(results["A"]), len(results["B"]), len(results["C"]),
        len(results["D"]), len(results["E"])))
    print("Checklist inserted: %d / %d" % (total_chk, total_pages))
    print("Critical Params inserted: %d / %d" % (total_prm, total_pages))
    print("Errors: %d" % len(errors))


if __name__ == "__main__":
    main()
