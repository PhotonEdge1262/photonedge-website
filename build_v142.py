#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""V142 Build Script - Phase 1: Homepage restructure + Navigation + CTA + AI page repositioning"""

import os
import re
import shutil

BASE = '/tmp/v142-build'

# ============================================================
# STEP 1: Create ai-optical-assistant.html from ai-optical-engineer.html
# ============================================================
print("Step 1: Creating ai-optical-assistant.html...")

with open(os.path.join(BASE, 'ai-optical-engineer.html'), 'r') as f:
    ai_content = f.read()

# Create new ai-optical-assistant.html
new_ai = ai_content

# Title and meta
new_ai = new_ai.replace(
    '<title>Optical Engineering Consultation | Describe Your Requirement | PhotonEdge</title>',
    '<title>AI Optical Assistant | PhotonEdge</title>'
)
new_ai = new_ai.replace(
    '<meta name="description" content="Describe your optical requirement and our engineering team will provide component recommendations, material suggestions, and coating guidance. Free consultation from PhotonEdge.">',
    '<meta name="description" content="Get preliminary optical component recommendations based on your application. AI Optical Assistant helps identify materials, coatings and specifications for review.">'
)
new_ai = new_ai.replace(
    '<meta name="keywords" content="optical component advisor, lens recommendation, optical material selector, coating advisor, free optical tool, optical consultation">',
    '<meta name="keywords" content="AI optical assistant, optical component recommendation, optical material selector, coating advisor, optical specification tool">'
)
new_ai = new_ai.replace(
    '<meta property="og:title" content="Optical Engineering Consultation | Describe Your Requirement | PhotonEdge">',
    '<meta property="og:title" content="AI Optical Assistant | PhotonEdge">'
)
new_ai = new_ai.replace(
    '<meta property="og:description" content="Describe your optical requirement and our engineering team will provide component recommendations, material suggestions, and coating guidance.">',
    '<meta property="og:description" content="Get preliminary optical component recommendations based on your application requirements. AI-powered tool for material and coating selection.">'
)
new_ai = new_ai.replace(
    '<meta property="og:url" content="https://photonedgeoptics.com/ai-optical-engineer.html">',
    '<meta property="og:url" content="https://photonedgeoptics.com/ai-optical-assistant.html">'
)
new_ai = new_ai.replace(
    '<link rel="canonical" href="https://photonedgeoptics.com/ai-optical-engineer.html">',
    '<link rel="canonical" href="https://photonedgeoptics.com/ai-optical-assistant.html">'
)
new_ai = new_ai.replace(
    '<link rel="alternate" hreflang="en" href="https://photonedgeoptics.com/ai-optical-engineer.html">',
    '<link rel="alternate" hreflang="en" href="https://photonedgeoptics.com/ai-optical-assistant.html">'
)

# Schema.org update
new_ai = new_ai.replace(
    '"name": "Optical Engineering Consultation"',
    '"name": "AI Optical Assistant"'
)
new_ai = new_ai.replace(
    '"description": "Describe your optical application and get professional component recommendations for materials, coatings, and specifications."',
    '"description": "Get preliminary optical component recommendations based on your application. This tool provides suggestions for materials, coatings and specifications for engineering review."'
)
new_ai = new_ai.replace(
    '"url": "https://photonedgeoptics.com/ai-optical-engineer.html"',
    '"url": "https://photonedgeoptics.com/ai-optical-assistant.html"'
)

# Hero section
new_ai = new_ai.replace(
    '<h1>Tell Us Your Optical Requirement</h1>',
    '<h1 data-i18n="v142aiHeroTitle">AI Optical Assistant</h1>'
)
new_ai = new_ai.replace(
    '<p>Describe your optical application. Get recommendations for materials, components, coatings, and specifications.</p>',
    '<p data-i18n="v142aiHeroDesc">Get preliminary component and material suggestions based on your application requirements. This tool provides starting-point recommendations for engineering review.</p>'
)

# Form heading
new_ai = new_ai.replace(
    '<h2>Tell Us About Your Application</h2>',
    '<h2 data-i18n="v142aiFormTitle">Describe Your Application</h2>'
)

# Submit button
new_ai = new_ai.replace(
    '>Get Optical Recommendation \xe2\x86\x92</button>',
    ' data-i18n="v142aiSubmitBtn">Get Preliminary Recommendation \xe2\x86\x92</button>'
)

# Features section
new_ai = new_ai.replace(
    '<h3>Material Selection</h3>',
    '<h3 data-i18n="v142aiFeat1Title">Material Suggestions</h3>'
)
new_ai = new_ai.replace(
    '<p>30+ optical materials matched to your wavelength, power, and environmental requirements</p>',
    '<p data-i18n="v142aiFeat1Desc">Preliminary material suggestions based on wavelength, power and environment. Final selection requires engineering review.</p>'
)
new_ai = new_ai.replace(
    '<h3>Coating Recommendation</h3>',
    '<h3 data-i18n="v142aiFeat2Title">Coating Guidance</h3>'
)
new_ai = new_ai.replace(
    '<p>AR, HR, bandpass, and specialty coating designs optimized for your application</p>',
    '<p data-i18n="v142aiFeat2Desc">General coating type recommendations for common application requirements. Specific designs require detailed specification review.</p>'
)
new_ai = new_ai.replace(
    '<h3>Specification Review</h3>',
    '<h3 data-i18n="v142aiFeat3Title">Specification Guidance</h3>'
)
new_ai = new_ai.replace(
    '<p>Tolerance analysis and DFM feedback to optimize performance vs. cost</p>',
    '<p data-i18n="v142aiFeat3Desc">General guidance on specification parameters. Detailed tolerance analysis is available through our engineering review process.</p>'
)

# Add disclaimer after features
disclaimer_html = '''
        <!-- Disclaimer -->
        <div style="max-width:900px;margin:0 auto 20px;padding:0 20px;">
            <div style="background:#fffbeb;border:1px solid #fde68a;border-radius:10px;padding:16px 20px;">
                <p style="color:#92400e;font-size:13px;line-height:1.6;margin:0;" data-i18n="v142aiDisclaimer">&#9888; This tool provides preliminary suggestions only. Final specifications and production decisions require professional engineering review. Contact us for detailed technical consultation.</p>
            </div>
        </div>
'''
# Insert before the examples section
new_ai = new_ai.replace(
    '        <!-- Example Queries -->',
    disclaimer_html + '\n        <!-- Example Queries -->'
)

# "Prefer Guided Selection?" section
new_ai = new_ai.replace(
    '<h2>Prefer Guided Selection?</h2>',
    '<h2 data-i18n="v142aiAdvisorTitle">Prefer Guided Selection?</h2>'
)
new_ai = new_ai.replace(
    '<p style="color:#6b7280;margin-bottom:20px;">Use our step-by-step Smart Product Advisor for component-by-component selection from our catalog.</p>',
    '<p style="color:#6b7280;margin-bottom:20px;" data-i18n="v142aiAdvisorDesc">Use our step-by-step Smart Product Advisor for component-by-component selection from our catalog.</p>'
)
new_ai = new_ai.replace(
    '>Open Smart Product Advisor \xe2\x86\x92</a>',
    ' data-i18n="v142aiAdvisorCTA">Open Smart Product Advisor \xe2\x86\x92</a>'
)

# Result section
new_ai = new_ai.replace(
    '<h3>\xf0\x9f\x93\x8b Recommended Optical Solution</h3>',
    '<h3 data-i18n="v142aiResultTitle">\xf0\x9f\x93\x8b Preliminary Recommendation</h3>'
)
new_ai = new_ai.replace(
    '<p style="font-size:15px;color:#374151;margin-bottom:16px;font-weight:600;">Get Detailed Engineering Review</p>',
    '<p style="font-size:15px;color:#374151;margin-bottom:16px;font-weight:600;" data-i18n="v142aiResultReviewTitle">Get Detailed Engineering Review</p>'
)
new_ai = new_ai.replace(
    '<p style="font-size:14px;color:#6b7280;margin-bottom:16px;">Our engineering team can provide a detailed specification review, material selection analysis, and custom quote for your application.</p>',
    '<p style="font-size:14px;color:#6b7280;margin-bottom:16px;" data-i18n="v142aiResultReviewDesc">For detailed specification review, material analysis and custom quotes, contact our team directly.</p>'
)

with open(os.path.join(BASE, 'ai-optical-assistant.html'), 'w') as f:
    f.write(new_ai)

print("  ai-optical-assistant.html created.")

# ============================================================
# STEP 2: Add canonical to old ai-optical-engineer.html
# ============================================================
print("Step 2: Adding canonical to ai-optical-engineer.html...")

with open(os.path.join(BASE, 'ai-optical-engineer.html'), 'r') as f:
    old_ai = f.read()

# Replace canonical to point to new page
old_ai = old_ai.replace(
    '<link rel="canonical" href="https://photonedgeoptics.com/ai-optical-engineer.html">',
    '<link rel="canonical" href="https://photonedgeoptics.com/ai-optical-assistant.html">'
)

with open(os.path.join(BASE, 'ai-optical-engineer.html'), 'w') as f:
    f.write(old_ai)

print("  ai-optical-engineer.html canonical updated.")

# ============================================================
# STEP 3: Site-wide link replacement (ai-optical-engineer -> ai-optical-assistant)
# ============================================================
print("Step 3: Replacing ai-optical-engineer.html links site-wide...")

count = 0
for root, dirs, files in os.walk(BASE):
    # Skip hidden dirs and js/css
    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('js', 'css', 'images')]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        if fname == 'ai-optical-engineer.html':
            continue  # Already handled
        with open(fpath, 'r') as f:
            content = f.read()
        if 'ai-optical-engineer.html' in content:
            new_content = content.replace('ai-optical-engineer.html', 'ai-optical-assistant.html')
            with open(fpath, 'w') as f:
                f.write(new_content)
            count += 1

print("  Replaced links in %d files." % count)

# ============================================================
# STEP 4: Update sitemap.xml
# ============================================================
print("Step 4: Updating sitemap.xml...")

with open(os.path.join(BASE, 'sitemap.xml'), 'r') as f:
    sitemap = f.read()

# Replace ai-optical-engineer with ai-optical-assistant
sitemap = sitemap.replace(
    '<url><loc>https://photonedgeoptics.com/ai-optical-engineer.html</loc><lastmod>2026-09-16</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>',
    '<url><loc>https://photonedgeoptics.com/ai-optical-assistant.html</loc><lastmod>2026-09-17</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>'
)

# Update lastmod for index.html
sitemap = sitemap.replace(
    '<url><loc>https://photonedgeoptics.com/</loc><lastmod>2026-09-16</lastmod>',
    '<url><loc>https://photonedgeoptics.com/</loc><lastmod>2026-09-17</lastmod>'
)

with open(os.path.join(BASE, 'sitemap.xml'), 'w') as f:
    f.write(sitemap)

print("  sitemap.xml updated.")

# ============================================================
# STEP 5: Update Navigation in all HTML files
# ============================================================
print("Step 5: Updating navigation (Resources dropdown)...")

# We need to add AI Optical Assistant link and Materials link to Resources dropdown
# The current Resources dropdown in index.html has: Knowledge Center, Application Notes, Materials Guide, Coating Database, FAQ, Blog
# We need to add: AI Optical Assistant (before FAQ)
# Materials Guide is already there as "Materials Guide"

nav_addition = '''                            <a href="/ai-optical-assistant.html" class="dropdown-item" data-i18n="navAIAssistant"><span class="dropdown-icon">&#129302;</span> AI Optical Assistant</a>
'''

# Find all HTML files and update nav
nav_count = 0
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('js', 'css', 'images')]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, 'r') as f:
            content = f.read()
        
        # Check if nav already has AI Optical Assistant
        if 'navAIAssistant' in content or 'AI Optical Assistant' in content:
            continue
        
        # Add AI Optical Assistant before FAQ in Resources dropdown
        if 'data-i18n="navFAQ"' in content:
            # Insert before FAQ line
            content = content.replace(
                '                            <a href="/faq.html" class="dropdown-item" data-i18n="navFAQ">',
                nav_addition.rstrip('\n') + '\n                            <a href="/faq.html" class="dropdown-item" data-i18n="navFAQ">'
            )
            with open(fpath, 'w') as f:
                f.write(content)
            nav_count += 1

print("  Updated navigation in %d files." % nav_count)

print("\nSteps 1-5 complete. Now generating new index.html...")
