import re

with open('/tmp/v159-work/index.html', 'r') as f:
    html = f.read()

# Split by section comment markers
section_pattern = r'(<!-- ============ (.+?) ============ -->)'
# parts: [pre, comment1, name1, content1, comment2, name2, content2, ...]
raw_parts = re.split(section_pattern, html)

# raw_parts[0] = everything before first section comment
# raw_parts[1] = first comment tag (<!-- ==== ... ==== -->)
# raw_parts[2] = section name
# raw_parts[3] = content until next comment
# etc.

sections = {}
header_html = raw_parts[0]

i = 1
while i < len(raw_parts) - 2:
    comment_tag = raw_parts[i]
    section_name = raw_parts[i+1].strip()
    section_content = raw_parts[i+2]
    sections[section_name] = (comment_tag, section_content)
    i += 3

# Find where footer starts
footer_idx = html.find('\n    <footer class="footer">')
footer_and_end = html[footer_idx:]

print("Header length:", len(header_html))
print("Footer length:", len(footer_and_end))
print("Sections found:", list(sections.keys()))

# ==============================
# BUILD NEW SECTIONS
# ==============================

# --- Merged Custom Optics & Engineering Review Section ---
merged_custom_optics = '''
<!-- ============ SECTION 3: CUSTOM OPTICS & ENGINEERING REVIEW ============ -->
<section style="padding:80px 0;background:#f8fafc;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;" data-i18n="v159CustomSectionTitle">Custom Optics &amp; Engineering Review</h2>
            <p style="color:#64748b;max-width:750px;margin:0 auto;font-size:16px;line-height:1.7;" data-i18n="v159CustomSectionSubtitle">From prototype to volume production &mdash; we coordinate every stage based on your specifications. Every inquiry receives engineering review before quotation.</p>
        </div>

        <!-- Project Flow -->
        <div style="margin-bottom:48px;">
            <h3 style="font-size:18px;font-weight:600;color:#1e293b;text-align:center;margin-bottom:24px;" data-i18n="v159FlowTitle">Project Flow</h3>
            <div style="display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:8px;max-width:1100px;margin:0 auto;">
                <span style="background:white;border:1px solid #e2e8f0;border-radius:8px;padding:10px 18px;color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v159Flow1">Requirement</span>
                <span style="color:#94a3b8;font-size:18px;">&#10132;</span>
                <span style="background:white;border:1px solid #e2e8f0;border-radius:8px;padding:10px 18px;color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v159Flow2">Engineering Review</span>
                <span style="color:#94a3b8;font-size:18px;">&#10132;</span>
                <span style="background:white;border:1px solid #e2e8f0;border-radius:8px;padding:10px 18px;color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v159Flow3">DFM Feedback</span>
                <span style="color:#94a3b8;font-size:18px;">&#10132;</span>
                <span style="background:white;border:1px solid #e2e8f0;border-radius:8px;padding:10px 18px;color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v159Flow4">Quotation</span>
                <span style="color:#94a3b8;font-size:18px;">&#10132;</span>
                <span style="background:white;border:1px solid #e2e8f0;border-radius:8px;padding:10px 18px;color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v159Flow5">Production</span>
                <span style="color:#94a3b8;font-size:18px;">&#10132;</span>
                <span style="background:white;border:1px solid #e2e8f0;border-radius:8px;padding:10px 18px;color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v159Flow6">Inspection</span>
                <span style="color:#94a3b8;font-size:18px;">&#10132;</span>
                <span style="background:white;border:1px solid #e2e8f0;border-radius:8px;padding:10px 18px;color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v159Flow7">Delivery</span>
            </div>
        </div>

        <!-- Engineering Review Checklist -->
        <div style="margin-bottom:40px;">
            <h3 style="font-size:18px;font-weight:600;color:#1e293b;text-align:center;margin-bottom:20px;" data-i18n="v159ReviewTitle">Engineering Review Covers</h3>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;max-width:900px;margin:0 auto;">
                <div style="padding:14px 20px;background:white;border-radius:8px;border:1px solid #e2e8f0;display:flex;align-items:center;gap:10px;">
                    <span style="color:#2563eb;font-size:16px;font-weight:700;">&#10003;</span>
                    <span style="color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v144ReviewItem1">Material selection</span>
                </div>
                <div style="padding:14px 20px;background:white;border-radius:8px;border:1px solid #e2e8f0;display:flex;align-items:center;gap:10px;">
                    <span style="color:#2563eb;font-size:16px;font-weight:700;">&#10003;</span>
                    <span style="color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v144ReviewItem2">Coating requirements</span>
                </div>
                <div style="padding:14px 20px;background:white;border-radius:8px;border:1px solid #e2e8f0;display:flex;align-items:center;gap:10px;">
                    <span style="color:#2563eb;font-size:16px;font-weight:700;">&#10003;</span>
                    <span style="color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v144ReviewItem3">Dimensional tolerances</span>
                </div>
                <div style="padding:14px 20px;background:white;border-radius:8px;border:1px solid #e2e8f0;display:flex;align-items:center;gap:10px;">
                    <span style="color:#2563eb;font-size:16px;font-weight:700;">&#10003;</span>
                    <span style="color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v144ReviewItem4">Surface quality</span>
                </div>
                <div style="padding:14px 20px;background:white;border-radius:8px;border:1px solid #e2e8f0;display:flex;align-items:center;gap:10px;">
                    <span style="color:#2563eb;font-size:16px;font-weight:700;">&#10003;</span>
                    <span style="color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v144ReviewItem5">Flatness</span>
                </div>
                <div style="padding:14px 20px;background:white;border-radius:8px;border:1px solid #e2e8f0;display:flex;align-items:center;gap:10px;">
                    <span style="color:#2563eb;font-size:16px;font-weight:700;">&#10003;</span>
                    <span style="color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v144ReviewItem6">Wavelength requirements</span>
                </div>
                <div style="padding:14px 20px;background:white;border-radius:8px;border:1px solid #e2e8f0;display:flex;align-items:center;gap:10px;">
                    <span style="color:#2563eb;font-size:16px;font-weight:700;">&#10003;</span>
                    <span style="color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v144ReviewItem7">Power handling</span>
                </div>
                <div style="padding:14px 20px;background:white;border-radius:8px;border:1px solid #e2e8f0;display:flex;align-items:center;gap:10px;">
                    <span style="color:#2563eb;font-size:16px;font-weight:700;">&#10003;</span>
                    <span style="color:#1e293b;font-size:14px;font-weight:500;" data-i18n="v144ReviewItem8">Manufacturability (DFM)</span>
                </div>
            </div>
        </div>

        <div style="text-align:center;">
            <a href="/contact.html" style="display:inline-block;background:#2563eb;color:white;padding:14px 32px;border-radius:8px;text-decoration:none;font-weight:600;font-size:16px;" data-i18n="v159UploadCTA">Upload Your Drawing</a>
        </div>
    </div>
</section>

'''

# --- Streamlined Evidence Section with ISO 9001:2015 ---
new_evidence_section = '''
<!-- ============ SECTION 6: EVIDENCE & QUALITY ============ -->
<section style="padding:80px 0;background:#f8fafc;">
    <div class="container">
        <div style="text-align:center;margin-bottom:50px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;" data-i18n="v159EvidenceTitle">Quality &amp; Evidence</h2>
            <p style="color:#64748b;max-width:700px;margin:0 auto;font-size:16px;line-height:1.7;" data-i18n="v159EvidenceSubtitle">Quality system aligned with ISO 9001:2015. Inspection reports and documentation provided per project requirements.</p>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;max-width:1100px;margin:0 auto;">
            <a href="/evidence.html" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128203;</div>
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v159EvCard1Title">Inspection Reports</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v159EvCard1Desc">Dimensional, optical and surface inspection documentation provided with shipments.</p></a>
            <a href="/coatings/" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#128300;</div>
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v159EvCard2Title">Coating Performance Data</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v159EvCard2Desc">Transmission curves, reflectance data and laser damage threshold test results.</p></a>
            <a href="/quality-assurance.html" style="text-decoration:none;padding:28px;background:white;border-radius:12px;border:1px solid #e2e8f0;transition:all 0.3s;display:block;" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 8px 20px rgba(0,0,0,0.08)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
                <div style="font-size:28px;margin-bottom:12px;">&#9989;</div>
                <h3 style="font-size:17px;color:#1e293b;margin-bottom:8px;font-weight:600;" data-i18n="v159EvCard3Title">Quality Documentation</h3>
                <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v159EvCard3Desc">Certificates of conformity, material certificates and quality procedures per project requirements.</p></a>
        </div>
        <div style="text-align:center;margin-top:32px;">
            <a href="/evidence.html" style="color:#2563eb;font-weight:600;text-decoration:none;font-size:15px;" data-i18n="v159ViewAllEvidence">View Evidence Center</a>
        </div>
    </div>
</section>

'''

# --- FAQ Section ---
faq_section = '''
<!-- ============ SECTION 7: FAQ ============ -->
<section style="padding:80px 0;background:#ffffff;">
    <div class="container">
        <div style="text-align:center;margin-bottom:40px;">
            <h2 style="font-size:32px;font-weight:700;color:#1e293b;margin-bottom:12px;" data-i18n="v159FaqTitle">Frequently Asked Questions</h2>
            <p style="color:#64748b;max-width:600px;margin:0 auto;font-size:16px;line-height:1.7;" data-i18n="v159FaqSubtitle">Common questions about working with PhotonEdge.</p>
        </div>
        <div style="max-width:800px;margin:0 auto;">
            <div style="border:1px solid #e2e8f0;border-radius:10px;margin-bottom:12px;overflow:hidden;">
                <button onclick="toggleFaqItem(this)" style="width:100%;padding:20px 24px;background:white;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;text-align:left;">
                    <span style="font-size:15px;font-weight:600;color:#1e293b;" data-i18n="v159Faq1Q">What information do you need for a quotation?</span>
                    <span class="faq-arrow" style="color:#94a3b8;font-size:18px;transition:transform 0.3s;">&#9660;</span>
                </button>
                <div class="faq-accordion-body" style="display:none;padding:0 24px 20px;">
                    <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v159Faq1A">Material, dimensions, tolerances, surface quality, coating requirements, quantity and target delivery date. A drawing is ideal, but a clear specification description also works.</p>
                </div>
            </div>
            <div style="border:1px solid #e2e8f0;border-radius:10px;margin-bottom:12px;overflow:hidden;">
                <button onclick="toggleFaqItem(this)" style="width:100%;padding:20px 24px;background:white;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;text-align:left;">
                    <span style="font-size:15px;font-weight:600;color:#1e293b;" data-i18n="v159Faq2Q">Do you handle both standard and custom components?</span>
                    <span class="faq-arrow" style="color:#94a3b8;font-size:18px;transition:transform 0.3s;">&#9660;</span>
                </button>
                <div class="faq-accordion-body" style="display:none;padding:0 24px 20px;">
                    <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v159Faq2A">Yes. We supply standard catalog optical components as well as custom optics manufactured to your drawings and specifications.</p>
                </div>
            </div>
            <div style="border:1px solid #e2e8f0;border-radius:10px;margin-bottom:12px;overflow:hidden;">
                <button onclick="toggleFaqItem(this)" style="width:100%;padding:20px 24px;background:white;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;text-align:left;">
                    <span style="font-size:15px;font-weight:600;color:#1e293b;" data-i18n="v159Faq3Q">What is the typical lead time?</span>
                    <span class="faq-arrow" style="color:#94a3b8;font-size:18px;transition:transform 0.3s;">&#9660;</span>
                </button>
                <div class="faq-accordion-body" style="display:none;padding:0 24px 20px;">
                    <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v159Faq3A">Standard components ship according to stock availability. Custom components typically require 2&ndash;4 weeks depending on complexity and quantity. We confirm lead time in every quotation.</p>
                </div>
            </div>
            <div style="border:1px solid #e2e8f0;border-radius:10px;margin-bottom:12px;overflow:hidden;">
                <button onclick="toggleFaqItem(this)" style="width:100%;padding:20px 24px;background:white;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;text-align:left;">
                    <span style="font-size:15px;font-weight:600;color:#1e293b;" data-i18n="v159Faq4Q">Do you provide inspection reports and documentation?</span>
                    <span class="faq-arrow" style="color:#94a3b8;font-size:18px;transition:transform 0.3s;">&#9660;</span>
                </button>
                <div class="faq-accordion-body" style="display:none;padding:0 24px 20px;">
                    <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v159Faq4A">Yes. Inspection reports, material certificates and certificates of conformity are provided according to project requirements. Specify documentation needs when requesting a quote.</p>
                </div>
            </div>
            <div style="border:1px solid #e2e8f0;border-radius:10px;margin-bottom:12px;overflow:hidden;">
                <button onclick="toggleFaqItem(this)" style="width:100%;padding:20px 24px;background:white;border:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;text-align:left;">
                    <span style="font-size:15px;font-weight:600;color:#1e293b;" data-i18n="v159Faq5Q">What is the minimum order quantity?</span>
                    <span class="faq-arrow" style="color:#94a3b8;font-size:18px;transition:transform 0.3s;">&#9660;</span>
                </button>
                <div class="faq-accordion-body" style="display:none;padding:0 24px 20px;">
                    <p style="color:#64748b;font-size:14px;line-height:1.7;margin:0;" data-i18n="v159Faq5A">For standard components, there is no minimum. For custom optics, we can produce from 1 piece for prototype evaluation.</p>
                </div>
            </div>
        </div>
    </div>
</section>

'''

# --- New Final CTA ---
new_final_cta = '''
<!-- ============ SECTION 8: FINAL CTA ============ -->
<section style="padding:80px 0;background:linear-gradient(135deg,#1e3a5f 0%,#2563eb 100%);">
    <div class="container" style="text-align:center;">
        <h2 style="font-size:32px;font-weight:700;color:white;margin-bottom:16px;" data-i18n="v159FinalCTATitle">Ready to discuss your project?</h2>
        <p style="color:rgba(255,255,255,0.85);font-size:16px;line-height:1.8;max-width:680px;margin:0 auto 32px;" data-i18n="v159FinalCTADesc">Send your drawing, specification or application requirements. Our engineering team will review your request and respond with the appropriate manufacturing approach and quotation.</p>
        <div style="display:flex;gap:16px;flex-wrap:wrap;justify-content:center;">
            <a href="/contact.html" style="display:inline-block;background:white;color:#2563eb;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600;font-size:16px;" data-i18n="v159FinalCTA1">Request a Quote</a>
            <a href="/contact.html" style="display:inline-block;background:transparent;border:2px solid rgba(255,255,255,0.5);color:white;padding:14px 28px;border-radius:8px;text-decoration:none;font-weight:600;font-size:16px;" data-i18n="v159FinalCTA2">Upload Your Drawing</a>
        </div>
    </div>
</section>

'''

# ==============================
# ASSEMBLE NEW HOMEPAGE
# ==============================

new_html = header_html

# 1. Hero
new_html += sections['SECTION 1: HERO'][0] + sections['SECTION 1: HERO'][1]

# 2. Capability Bar
new_html += sections['CAPABILITY OVERVIEW BAR'][0] + sections['CAPABILITY OVERVIEW BAR'][1]

# 3. Product Categories (moved up)
new_html += sections['SECTION 4: CORE PRODUCT CATEGORIES'][0] + sections['SECTION 4: CORE PRODUCT CATEGORIES'][1]

# 4. Merged Custom Optics & Engineering Review
new_html += merged_custom_optics

# 5. Why PhotonEdge
new_html += sections['SECTION 4B: WHY PHOTONEDGE'][0] + sections['SECTION 4B: WHY PHOTONEDGE'][1]

# 6. Applications
new_html += sections['SECTION 5: APPLICATIONS'][0] + sections['SECTION 5: APPLICATIONS'][1]

# 7. Evidence & Quality (streamlined)
new_html += new_evidence_section

# 8. FAQ
new_html += faq_section

# 9. Final CTA
new_html += new_final_cta

# Footer and end
new_html += footer_and_end

with open('/tmp/v159-work/index.html', 'w') as f:
    f.write(new_html)

print("\nNew homepage written successfully!")
print("New file size:", len(new_html))
print("\nNew section order:")
print("1. Hero")
print("2. Capability Bar")
print("3. Product Categories")
print("4. Custom Optics & Engineering Review (MERGED)")
print("5. Why PhotonEdge")
print("6. Applications")
print("7. Evidence & Quality (streamlined)")
print("8. FAQ (NEW)")
print("9. Final CTA (refreshed)")
