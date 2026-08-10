#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Blog #36: Optical Beamsplitter Selection Complete Guide
"""

import os
import json
import re

# ========== BLOG CONTENT ==========

blog_id = 36
blog_slug = "optical-beamsplitter-selection-complete-guide"
blog_url = "/blog/" + blog_slug + "/"
blog_date = "2026-08-10"
blog_read_time = "12 min"
blog_category = "Technical Guide"
blog_category_zh = "技术指南"
blog_author = "PhotonEdge Technical Team"

title_en = "Optical Beamsplitters Complete Selection Guide: Plate, Cube, Polarizing & Non-Polarizing"
title_zh = "光学分束器完全选型指南：平板、立方、偏振与非偏振分束器"

excerpt_en = "Complete guide to optical beamsplitters: how to choose between plate beamsplitters, cube beamsplitters, polarizing and non-polarizing cubes. Learn about split ratios, extinction ratio, damage threshold, and application-specific selection for lasers, interferometry, machine vision, and fiber optics."
excerpt_zh = "光学分束器完全选型指南：如何在平板分束器、立方分束器、偏振立方与非偏振立方之间选择。了解分束比、消光比、损伤阈值以及针对激光、干涉测量、机器视觉和光纤通信的应用选型建议。"

keywords_en = "Beamsplitter, Optical Beamsplitter, Cube Beamsplitter, Plate Beamsplitter, Polarizing Beamsplitter, Non-Polarizing Beamsplitter, Beam Splitter Selection, 50/50 Beamsplitter, High Power Beamsplitter"
keywords_zh = "分束器, 光学分束器, 立方分束器, 平板分束器, 偏振分束器, 非偏振分束器, 分束器选型, 50/50分束器, 高功率分束器"

# ========== ENGLISH CONTENT ==========
content_en = """<h2>Introduction</h2>
<p>Every optical system &mdash; from a simple laser power monitor to a complex Mach-Zehnder interferometer &mdash; needs a way to split light into two or more paths. That job belongs to the <strong>beamsplitter</strong>. Choose the wrong type and your polarization gets scrambled. Choose the wrong coating and your high-power laser damages the optic. Choose plate instead of cube, and ghost reflections degrade your signal-to-noise ratio. Yet many engineers treat beamsplitters as a commodity &mdash; ordering any 50/50 part and assuming it will work.</p>
<p>This guide walks through every major beamsplitter type: plate beamsplitters, cube beamsplitters, polarizing cube beamsplitters, and non-polarizing cube beamsplitters. You will learn how beamsplitter coatings work, why polarization matters more than most people realize, how to read extinction ratio specifications, and which beamsplitter type is right for your laser, imaging, interferometry, or fiber optic application.</p>

<h2>What Is an Optical Beamsplitter?</h2>
<p>An optical beamsplitter is an optical component that divides an incident light beam into two (or more) separate beams traveling in different directions. The division can be based on intensity (power), polarization, wavelength, or a combination of these. The most common type splits a single beam into a <strong>transmitted beam</strong> and a <strong>reflected beam</strong>, typically at 90&deg; to each other.</p>
<p>Beamsplitters are defined by their <strong>split ratio</strong> (also called the beam splitting ratio or R/T ratio), which describes how much light is reflected versus transmitted. A 50/50 beamsplitter reflects 50% and transmits 50%. A 70/30 beamsplitter reflects 70% and transmits 30%. The ratio is always specified as <em>R:T</em> (Reflected:Transmitted) unless otherwise noted.</p>

<h3>Key Beamsplitter Parameters</h3>
<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">Parameter</th><th style="border:1px solid #e2e8f0;padding:8px;">Typical Range</th><th style="border:1px solid #e2e8f0;padding:8px;">Why It Matters</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Split Ratio (R:T)</td><td style="border:1px solid #e2e8f0;padding:8px;">10:90, 30:70, 50:50, 70:30, 90:10</td><td style="border:1px solid #e2e8f0;padding:8px;">Determines power distribution between output beams</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Wavelength Range</td><td style="border:1px solid #e2e8f0;padding:8px;">UV, Visible, NIR, SWIR, Broadband</td><td style="border:1px solid #e2e8f0;padding:8px;">Split ratio only holds within specified band</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Polarization Sensitivity</td><td style="border:1px solid #e2e8f0;padding:8px;">Polarizing vs Non-Polarizing</td><td style="border:1px solid #e2e8f0;padding:8px;">Whether S and P polarizations split differently</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Extinction Ratio</td><td style="border:1px solid #e2e8f0;padding:8px;">100:1 to 1000:1 (PBS)</td><td style="border:1px solid #e2e8f0;padding:8px;">Purity of polarization separation in PBS cubes</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Laser Damage Threshold</td><td style="border:1px solid #e2e8f0;padding:8px;">0.5 &ndash; 15 J/cm&sup2; (1064 nm, 10 ns)</td><td style="border:1px solid #e2e8f0;padding:8px;">Critical for high-power laser systems</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Wavefront Distortion</td><td style="border:1px solid #e2e8f0;padding:8px;">&lambda;/4 to &lambda;/10 @ 633 nm</td><td style="border:1px solid #e2e8f0;padding:8px;">Affects beam quality in precision systems</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Substrate Material</td><td style="border:1px solid #e2e8f0;padding:8px;">BK7, UV Fused Silica, ZnSe, CaF2</td><td style="border:1px solid #e2e8f0;padding:8px;">Determines spectral range and thermal properties</td></tr>
</table>

<h2>Four Types of Beamsplitters: How They Compare</h2>
<p>PhotonEdge offers four primary beamsplitter configurations, each with distinct advantages and best-use scenarios. Understanding the differences is the first step toward making the right choice.</p>

<h3>1. Plate Beamsplitters</h3>
<p>A <a href="/products/beamsplitter-plates/">plate beamsplitter</a> is a flat optical window with a partial-reflection coating on one surface and an anti-reflection coating on the other. Light enters through the AR-coated back surface, passes through the substrate, and hits the partially reflecting front coating. Part of the beam reflects off the coating (reflected beam), while the rest transmits through (transmitted beam).</p>
<p><strong>Advantages:</strong></p>
<ul>
<li>Low cost &mdash; simple flat optic, easy to manufacture</li>
<li>Low absorption &mdash; minimal material in the beam path</li>
<li>High damage threshold possible with proper coatings</li>
<li>Available in large sizes for wide beams</li>
<li>Lightweight compared to cube equivalents</li>
</ul>
<p><strong>Disadvantages:</strong></p>
<ul>
<li><strong>Ghost reflection</strong> from the back (AR-coated) surface creates a secondary reflected beam that can interfere with measurements</li>
<li><strong>Beam displacement</strong> &mdash; the transmitted beam shifts laterally due to refraction through the substrate</li>
<li><strong>Strongly polarization-dependent</strong> at 45&deg; incidence (plate beamsplitters are inherently polarization-sensitive due to Fresnel equations at oblique incidence)</li>
<li>Requires precise angular alignment</li>
</ul>
<p><strong>Best for:</strong> Cost-sensitive applications, high-power systems where substrate absorption matters, large beam diameters, and setups where ghost reflections can be tolerated or managed.</p>

<h3>2. Cube Beamsplitters</h3>
<p>A <a href="/products/cube-beamsplitters/">cube beamsplitter</a> is formed by cementing two right-angle prisms together along their hypotenuse faces. The beamsplitter coating is deposited on the hypotenuse of one prism before cementing. Light enters through a face of the cube, hits the diagonal coating, and is split &mdash; transmitted beam continues straight through, reflected beam exits at 90&deg; through the side face.</p>
<p><strong>Advantages:</strong></p>
<ul>
<li>No beam displacement in transmission &mdash; the output beam remains collinear with the input</li>
<li>No ghost reflections &mdash; the back reflection problem of plate beamsplitters is eliminated</li>
<li>Easier alignment &mdash; input and output faces are normal to their respective beams</li>
<li>Compact, robust form factor</li>
<li>Both transmitted and reflected beams have equal optical path length through glass</li>
</ul>
<p><strong>Disadvantages:</strong></p>
<ul>
<li>Higher cost than plate beamsplitters</li>
<li>Heavier and bulkier</li>
<li>More absorption due to longer optical path through substrate</li>
<li>Cemented version has lower damage threshold than all-dielectric plate beamsplitters</li>
<li>Limited to moderate beam sizes (large cubes are very expensive)</li>
</ul>
<p><strong>Best for:</strong> Imaging systems, interferometry, fiber optics, and any application where beam displacement or ghost reflections would be problematic.</p>

<h3>3. Non-Polarizing Cube Beamsplitters</h3>
<p>A <a href="/products/non-polarizing-cube-beamsplitters/">non-polarizing cube beamsplitter</a> is a special type of cube beamsplitter designed to split light <em>regardless of its polarization state</em>. Standard cube beamsplitters use simple dielectric coatings that reflect S-polarized light more efficiently than P-polarized light. Non-polarizing coatings use complex multilayer designs to achieve the same split ratio for both S and P polarizations at the design angle (typically 45&deg;).</p>
<p>The key specification is the <strong>polarization sensitivity</strong> or <strong>Tp/Ts ratio</strong>. A good non-polarizing beamsplitter might have Tp = 50% and Ts = 48%, giving a polarization sensitivity of only 2% &mdash; meaning the transmission varies by just 2% regardless of input polarization.</p>
<p><strong>Advantages:</strong></p>
<ul>
<li>Consistent split ratio regardless of input polarization</li>
<li>No beam displacement</li>
<li>No ghost reflections</li>
<li>Critical for systems with unknown or changing polarization</li>
</ul>
<p><strong>Disadvantages:</strong></p>
<ul>
<li>More expensive than standard polarizing-sensitive cubes</li>
<li>Coatings are more complex, with narrower effective wavelength range</li>
<li>Slightly lower damage threshold than simple dielectric coatings</li>
</ul>
<p><strong>Best for:</strong> Unpolarized light sources, imaging systems, photometry, color splitting, and any system where input polarization varies or is unknown.</p>

<h3>4. Polarizing Cube Beamsplitters (PBS)</h3>
<p>A <a href="/products/polarizing-cube-beamsplitters/">polarizing cube beamsplitter</a> (PBS) is designed to completely separate S-polarized and P-polarized light. P-polarized light (electric field parallel to the plane of incidence) transmits through the cube with minimal loss, while S-polarized light (electric field perpendicular to the plane of incidence) is reflected at 90&deg;. In an ideal PBS, the separation is perfect. In practice, some leakage always occurs.</p>
<p>The critical specification for PBS cubes is the <strong>extinction ratio</strong>, which measures how well the two polarizations are separated:</p>
<ul>
<li><strong>Transmission extinction ratio</strong> (Tp/Ts): How much P-polarized light transmits vs. S-polarized light leaking through in transmission. Typically 1000:1 or higher.</li>
<li><strong>Reflection extinction ratio</strong> (Rs/Rp): How much S-polarized light reflects vs. P-polarized light leaking into reflection. Typically 100:1 to 1000:1.</li>
</ul>
<p><strong>Advantages:</strong></p>
<ul>
<li>Complete polarization separation in a single component</li>
<li>Very high extinction ratio available</li>
<li>No beam displacement in transmission</li>
<li>Essential for polarization-dependent optical systems</li>
</ul>
<p><strong>Disadvantages:</strong></p>
<ul>
<li>Only works for specific wavelength bands (coating design is narrowband)</li>
<li>Damage threshold can be lower than standard dielectric coatings</li>
<li>Performance degrades if angle of incidence deviates from 45&deg;</li>
<li>Higher cost than standard cubes</li>
</ul>
<p><strong>Best for:</strong> Laser systems requiring polarization control, interferometry, optical isolation, Q-switching, and polarization-based measurements.</p>

<h2>Beamsplitter Type Comparison Table</h2>
<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">Feature</th><th style="border:1px solid #e2e8f0;padding:8px;">Plate Beamsplitter</th><th style="border:1px solid #e2e8f0;padding:8px;">Cube Beamsplitter</th><th style="border:1px solid #e2e8f0;padding:8px;">Non-Polarizing Cube</th><th style="border:1px solid #e2e8f0;padding:8px;">Polarizing Cube (PBS)</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>Beam displacement</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">Yes (significant)</td><td style="border:1px solid #e2e8f0;padding:8px;">None</td><td style="border:1px solid #e2e8f0;padding:8px;">None</td><td style="border:1px solid #e2e8f0;padding:8px;">None</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>Ghost reflections</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">Yes (from back surface)</td><td style="border:1px solid #e2e8f0;padding:8px;">No</td><td style="border:1px solid #e2e8f0;padding:8px;">No</td><td style="border:1px solid #e2e8f0;padding:8px;">No</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>Polarization sensitivity</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">High (inherent)</td><td style="border:1px solid #e2e8f0;padding:8px;">Medium</td><td style="border:1px solid #e2e8f0;padding:8px;">Low (&lt; 2%)</td><td style="border:1px solid #e2e8f0;padding:8px;">Very high (by design)</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>Damage threshold</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">Highest</td><td style="border:1px solid #e2e8f0;padding:8px;">Medium</td><td style="border:1px solid #e2e8f0;padding:8px;">Medium-Low</td><td style="border:1px solid #e2e8f0;padding:8px;">Low-Medium</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>Relative cost</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">Lowest</td><td style="border:1px solid #e2e8f0;padding:8px;">Medium</td><td style="border:1px solid #e2e8f0;padding:8px;">High</td><td style="border:1px solid #e2e8f0;padding:8px;">High</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>Wavelength range</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">Broadband available</td><td style="border:1px solid #e2e8f0;padding:8px;">Medium-Broadband</td><td style="border:1px solid #e2e8f0;padding:8px;">Narrower (coating-limited)</td><td style="border:1px solid #e2e8f0;padding:8px;">Narrowband (V-coating)</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>Best application</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">High-power lasers, large beams</td><td style="border:1px solid #e2e8f0;padding:8px;">General use, imaging</td><td style="border:1px solid #e2e8f0;padding:8px;">Unpolarized light, photometry</td><td style="border:1px solid #e2e8f0;padding:8px;">Polarization control, isolators</td></tr>
</table>

<h2>How to Select the Right Beamsplitter</h2>

<h3>Step 1: Define Your Application</h3>
<p>The application dictates everything. Start by answering these questions:</p>
<ul>
<li>Is the light source polarized or unpolarized?</li>
<li>What is the wavelength (or wavelength range)?</li>
<li>What power level are you working with?</li>
<li>How critical is beam alignment and displacement?</li>
<li>What split ratio do you need?</li>
<li>Is wavefront quality (beam distortion) important?</li>
</ul>

<h3>Step 2: Choose the Configuration</h3>
<p>Based on your application requirements:</p>
<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">If you need&hellip;</th><th style="border:1px solid #e2e8f0;padding:8px;">Choose&hellip;</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Lowest cost and can tolerate ghost reflections and beam displacement</td><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/beamsplitter-plates/">Plate beamsplitter</a></td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">No beam displacement, clean single reflected beam</td><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/cube-beamsplitters/">Cube beamsplitter</a></td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Consistent split ratio with unpolarized or randomly polarized light</td><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/non-polarizing-cube-beamsplitters/">Non-polarizing cube</a></td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Complete separation of S and P polarizations</td><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/polarizing-cube-beamsplitters/">Polarizing cube (PBS)</a></td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Highest possible laser damage threshold</td><td style="border:1px solid #e2e8f0;padding:8px;">Plate beamsplitter with all-dielectric coating</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Ultra-broadband splitting (e.g., visible + NIR)</td><td style="border:1px solid #e2e8f0;padding:8px;">Plate beamsplitter (broader coating range)</td></tr>
</table>

<h3>Step 3: Select the Wavelength Range</h3>
<p>Beamsplitter coatings are designed for specific wavelength bands. Using a beamsplitter outside its design range will result in incorrect split ratios and potentially high loss. Common bands include:</p>
<ul>
<li><strong>UV (250&ndash;400 nm):</strong> UV fused silica substrate, specialty dielectric coatings</li>
<li><strong>Visible (400&ndash;700 nm):</strong> BK7 substrate, standard dielectric coatings</li>
<li><strong>Visible-NIR (400&ndash;900 nm):</strong> Broadband visible + near IR</li>
<li><strong>NIR (700&ndash;1100 nm):</strong> For fiber optics and telecom</li>
<li><strong>SWIR (1100&ndash;1700 nm):</strong> For telecom C+L bands</li>
<li><strong>Laser line:</strong> Single wavelength (e.g., 532 nm, 633 nm, 1064 nm) with optimized split ratio</li>
</ul>
<p>For the most accurate split ratio, always choose a laser-line coating matched to your specific wavelength, not a broadband coating. Broadband coatings trade precision for range.</p>

<h3>Step 4: Determine the Split Ratio</h3>
<p>Common standard split ratios:</p>
<ul>
<li><strong>50/50 (R/T):</strong> Most common. Equal split for monitoring, interferometry, and dividing power.</li>
<li><strong>70/30 (R/T):</strong> More power in reflection. Useful when the reflected beam goes to a low-sensitivity detector.</li>
<li><strong>90/10 (R/T):</strong> Sampling configuration. Most power transmits, small fraction reflected for monitoring.</li>
<li><strong>10/90 (R/T):</strong> Reverse sampling. Most power reflects, small fraction transmits for monitoring.</li>
<li><strong>80/20, 30/70, etc.:</strong> Custom ratios available on request.</li>
</ul>
<p><strong>Pro tip:</strong> If you need a precise power ratio, specify it clearly. The split ratio tolerance on standard beamsplitters is typically &plusmn;5% or worse. For precision applications, request tight tolerance specification.</p>

<h2>Common Applications &amp; Recommended Configurations</h2>

<h3>Laser Systems</h3>
<p>In laser systems, beamsplitters serve as pick-off mirrors for power monitoring, beam sampling for diagnostics, and in cavity configurations such as interferometers. For high-power lasers, plate beamsplitters are often preferred because the cement in cube beamsplitters can fail at high intensities. For low-power laser diodes and fiber lasers, cube beamsplitters offer cleaner performance.</p>
<p><strong>Recommendation:</strong> Use <a href="/products/beamsplitter-plates/">plate beamsplitters</a> for high-power (&gt; 10 W CW), <a href="/products/cube-beamsplitters/">cube beamsplitters</a> for low-to-medium power.</p>

<h3>Interferometry</h3>
<p>Interferometers (Michelson, Mach-Zehnder, Fizeau) rely on precise 50/50 splitting with minimal wavefront distortion. Cube beamsplitters are preferred because they eliminate beam displacement and ghost reflections that would create spurious interference fringes. Non-polarizing cubes are used when polarization state must be preserved.</p>
<p><strong>Recommendation:</strong> <a href="/products/cube-beamsplitters/">High-quality cube beamsplitters</a> with &lambda;/10 wavefront specification, preferably non-polarizing for unpolarized sources.</p>

<h3>Machine Vision &amp; Imaging</h3>
<p>In machine vision, beamsplitters are used in beam splitters for coaxial illumination, fluorescence microscopy, and multi-camera setups. Non-polarizing cube beamsplitters are preferred because the light from most imaging sources is unpolarized, and polarization-dependent splitting would create inaccurate color or intensity reproduction.</p>
<p><strong>Recommendation:</strong> <a href="/products/non-polarizing-cube-beamsplitters/">Non-polarizing cube beamsplitters</a> for visible-range imaging applications.</p>

<h3>Fiber Optics &amp; Telecommunications</h3>
<p>In fiber optic systems, beamsplitters (often called "couplers" in fiber form) divide optical signals for monitoring, testing, and distribution. Free-space beamsplitters are used in fiber bench-top setups and fiber-to-free-space interfaces. Polarizing beamsplitters are critical for polarization diversity receivers and coherent communications.</p>
<p><strong>Recommendation:</strong> <a href="/products/polarizing-cube-beamsplitters/">Polarizing cube beamsplitters</a> for polarization-sensitive systems; <a href="/products/cube-beamsplitters/">standard cubes</a> for power splitting.</p>

<h3>Spectroscopy &amp; Analytical Instruments</h3>
<p>Spectrometers, fluorometers, and absorbance instruments use beamsplitters for reference channels, beam splitting for dual detectors, and wavelength calibration. Broadband coverage is essential, and non-polarizing performance is often required since many sample types depolarize light.</p>
<p><strong>Recommendation:</strong> Broadband non-polarizing plate or cube beamsplitters, depending on space and alignment constraints.</p>

<h2>5 Common Beamsplitter Mistakes &amp; How to Avoid Them</h2>

<h3>1. Ignoring Polarization Dependence</h3>
<p>This is the #1 mistake. Most standard beamsplitters (both plate and cube) have significantly different split ratios for S and P polarized light at 45&deg; incidence. If your input beam polarization changes &mdash; due to fiber bending, rotation, or a depolarizing sample &mdash; your split ratio changes too. In photometry and imaging systems, this causes measurement errors and intensity fluctuations.</p>
<p><strong>Solution:</strong> If you have unpolarized or randomly polarized light, use a <a href="/products/non-polarizing-cube-beamsplitters/">non-polarizing beamsplitter</a>. Verify the polarization sensitivity specification &mdash; look for &lt; 2% variation between S and P. If your system is polarization-controlled, standard cubes work fine.</p>

<h3>2. Forgetting About Ghost Reflections with Plate Beamsplitters</h3>
<p>Every plate beamsplitter has two reflecting surfaces: the front (coated) surface and the back (AR-coated) surface. Even a good AR coating leaves about 0.25% reflection per surface. That means you get a primary reflected beam (from the front coating) and a weaker "ghost" beam (from the back surface) that is displaced by a distance proportional to the plate thickness. In imaging systems, this creates double images. In interferometry, it creates spurious fringe patterns.</p>
<p><strong>Solution:</strong> Use a <a href="/products/cube-beamsplitters/">cube beamsplitter</a> if ghost reflections are unacceptable. If you must use a plate, choose a wedge-shaped plate to spatially separate the ghost beam from the primary beam, or tilt the plate so the ghost beam misses your detector.</p>

<h3>3. Choosing the Wrong Wavelength Band</h3>
<p>Beamsplitter coatings are precisely engineered for specific wavelength ranges. A "50/50" beamsplitter designed for 1064 nm might be 30/70 at 532 nm and 80/20 at 1550 nm. Using a broadband beamsplitter when you only need a single wavelength gives you worse precision than a laser-line coating. Using a laser-line coating for broadband use gives you wrong split ratios.</p>
<p><strong>Solution:</strong> Match the beamsplitter coating band to your actual operating wavelength. For monochromatic sources (lasers), use laser-line coatings for the most accurate split ratio. For broadband sources, use broadband coatings and accept the &plusmn;10% typical variation across the band.</p>

<h3>4. Underestimating Power Handling Requirements</h3>
<p>Beamsplitters have lower damage thresholds than mirrors because the coating is designed to partially transmit &mdash; more layers are exposed to the light, and the electric field distribution in the coating can create hot spots. Cemented cube beamsplitters are especially vulnerable because the cement layer can absorb light and fail at relatively low power levels.</p>
<p><strong>Solution:</strong> For powers above ~5 W CW or pulse energies above ~0.1 J/cm&sup2;, use <a href="/products/beamsplitter-plates/">all-dielectric plate beamsplitters</a> instead of cemented cubes. For high-power pulsed lasers, specify a laser-line coating with verified damage threshold. Always derate &mdash; use a beamsplitter rated for at least 2&ndash;3&times; your actual power.</p>

<h3>5. Overlooking Beam Displacement in Transmission</h3>
<p>Plate beamsplitters cause the transmitted beam to shift laterally because of refraction through the tilted substrate. The displacement depends on the plate thickness and refractive index. For a 3 mm thick BK7 plate at 45&deg;, the displacement is roughly 1 mm &mdash; enough to throw off alignment in precision systems. If you have multiple plate beamsplitters in a system, the displacements add up.</p>
<p><strong>Solution:</strong> Use <a href="/products/cube-beamsplitters/">cube beamsplitters</a> when alignment precision is critical &mdash; they produce zero transmitted beam displacement. If you must use a plate, account for the displacement in your optical design, or use a thinner plate to minimize it.</p>

<h2>Product Selection Guide</h2>

<h3>Cube Beamsplitters</h3>
<ul>
<li><a href="/products/cube-beamsplitters/">Standard Cube Beamsplitters</a> &mdash; Visible and NIR range; 50/50 and 70/30 ratios; BK7 substrate; ideal for general imaging and laser setups</li>
<li><a href="/products/non-polarizing-cube-beamsplitters/">Non-Polarizing Cube Beamsplitters</a> &mdash; Consistent split ratio for unpolarized light; low polarization sensitivity (&lt; 2%); best for photometry and imaging</li>
<li><a href="/products/polarizing-cube-beamsplitters/">Polarizing Cube Beamsplitters (PBS)</a> &mdash; High extinction ratio (1000:1 transmission); 532 nm, 633 nm, 808 nm, 1064 nm laser-line versions available</li>
</ul>

<h3>Plate Beamsplitters</h3>
<ul>
<li><a href="/products/beamsplitter-plates/">Plate Beamsplitters</a> &mdash; All-dielectric coatings; higher damage threshold than cemented cubes; available in 25.4 mm and 50 mm sizes; 50/50 and 90/10 standard ratios</li>
</ul>

<h3>Complementary Polarization Optics</h3>
<ul>
<li><a href="/products/visible-linear-polarizers/">Visible Linear Polarizers</a> &mdash; Pair with PBS cubes for polarization control setups; high extinction ratio polarizing film on BK7 substrate</li>
<li><a href="/products/ir-polarizers/">IR Polarizers</a> &mdash; For NIR and SWIR applications; wire-grid or dichroic polarizer options</li>
<li><a href="/products/cemented-zero-order-waveplates/">Zero-Order Waveplates</a> &mdash; Use with PBS cubes to rotate polarization and adjust split ratio; 1/2 wave for rotation, 1/4 wave for circular polarization</li>
<li><a href="/products/glan-taylor-prisms/">Glan Taylor Prisms</a> &mdash; Ultra-high extinction ratio (&gt; 100,000:1) for demanding polarization applications</li>
</ul>

<h3>Related Optics</h3>
<ul>
<li><a href="/products/bk7-right-angle-prisms/">BK7 Right Angle Prisms</a> &mdash; Basic building blocks for beamsplitter and turning mirror assemblies</li>
<li><a href="/products/broadband-dielectric-mirrors/">Broadband Dielectric Mirrors</a> &mdash; High-reflection mirrors to pair with beamsplitters for fold mirrors</li>
<li><a href="/products/laser-line-high-reflected-mirrors/">Laser Line High Reflectors</a> &mdash; High-reflector mirrors for laser-line beamsplitter setups</li>
</ul>

<h2>Conclusion</h2>
<p>Choosing the right beamsplitter is more nuanced than just picking a 50/50 ratio and adding it to your optical train. The configuration &mdash; plate vs. cube, polarizing vs. non-polarizing &mdash; determines everything from beam alignment to polarization purity to power handling. Plate beamsplitters offer the highest damage threshold and lowest cost but bring ghost reflections and beam displacement. Cube beamsplitters eliminate those problems at the cost of lower power handling and higher price. Non-polarizing cubes handle unpolarized light accurately, while polarizing cubes deliver clean S/P separation essential for polarization-sensitive systems.</p>
<p>At PhotonEdge, we manufacture all four beamsplitter types with standard and custom coatings across UV, visible, and infrared wavelengths. Our technical team can help you specify the right beamsplitter &mdash; including coating design, substrate material, split ratio tolerance, and damage threshold &mdash; for your specific application. Whether you need a single 50/50 cube for a prototype or custom beamsplitter arrays for a production instrument, we can support your design from concept through delivery.</p>"""

# ========== CHINESE CONTENT ==========
content_zh = """<h2>引言</h2>
<p>每一个光学系统——从简单的激光功率监测器到复杂的马赫-曾德尔干涉仪——都需要将光分成两条或更多路径的方法。这个任务由<strong>分束器</strong>来完成。选择错误的类型，您的偏振状态会被打乱；选择错误的镀膜，高功率激光器会损坏光学元件；选择平板而不是立方，鬼像反射会降低信噪比。然而，许多工程师把分束器当成标准件——随便订购一个50/50的零件，然后假设它能正常工作。</p>
<p>本指南全面介绍每一种主要的分束器类型：平板分束器、立方分束器、偏振立方分束器和非偏振立方分束器。您将了解分束器镀膜的工作原理、为什么偏振比大多数人认为的更重要、如何解读消光比规格，以及哪种分束器类型适合您的激光、成像、干涉测量或光纤应用。</p>

<h2>什么是光学分束器？</h2>
<p>光学分束器是一种将入射光束分成两束（或多束）沿不同方向传播的独立光束的光学元件。分光的依据可以是强度（功率）、偏振、波长，或这些因素的组合。最常见的类型将单束光分成<strong>透射光束</strong>和<strong>反射光束</strong>，两者通常成90度角。</p>
<p>分束器由其<strong>分束比</strong>（也称为分束比例或R/T比）来定义，它描述了反射光与透射光的比例。50/50分束器反射50%并透射50%。70/30分束器反射70%并透射30%。除非另有说明，比例始终指定为<em>R:T</em>（反射:透射）。</p>

<h3>分束器的关键参数</h3>
<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">参数</th><th style="border:1px solid #e2e8f0;padding:8px;">典型范围</th><th style="border:1px solid #e2e8f0;padding:8px;">重要性</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">分束比（R:T）</td><td style="border:1px solid #e2e8f0;padding:8px;">10:90、30:70、50:50、70:30、90:10</td><td style="border:1px solid #e2e8f0;padding:8px;">决定输出光束之间的功率分配</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">波长范围</td><td style="border:1px solid #e2e8f0;padding:8px;">紫外、可见光、近红外、短波红外、宽带</td><td style="border:1px solid #e2e8f0;padding:8px;">分束比仅在指定波段内有效</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">偏振灵敏度</td><td style="border:1px solid #e2e8f0;padding:8px;">偏振型 vs 非偏振型</td><td style="border:1px solid #e2e8f0;padding:8px;">S和P偏振是否有不同的分束比</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">消光比</td><td style="border:1px solid #e2e8f0;padding:8px;">100:1 至 1000:1（偏振分束器）</td><td style="border:1px solid #e2e8f0;padding:8px;">偏振立方中偏振分离的纯度</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">激光损伤阈值</td><td style="border:1px solid #e2e8f0;padding:8px;">0.5 – 15 J/cm²（1064 nm，10 ns）</td><td style="border:1px solid #e2e8f0;padding:8px;">对高功率激光系统至关重要</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">波前畸变</td><td style="border:1px solid #e2e8f0;padding:8px;">λ/4 至 λ/10 @ 633 nm</td><td style="border:1px solid #e2e8f0;padding:8px;">影响精密系统中的光束质量</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">基底材料</td><td style="border:1px solid #e2e8f0;padding:8px;">BK7、紫外熔融石英、ZnSe、CaF2</td><td style="border:1px solid #e2e8f0;padding:8px;">决定光谱范围和热性能</td></tr>
</table>

<h2>四种分束器类型：如何比较</h2>
<p>恒鼎光提供四种主要分束器结构，每种都有独特的优势和最佳适用场景。了解差异是做出正确选择的第一步。</p>

<h3>1. 平板分束器</h3>
<p><a href="/products/beamsplitter-plates/">平板分束器</a>是一种平面光学窗口，一面镀有部分反射膜，另一面镀有增透膜。光从增透膜背面入射，穿过基底，照射到部分反射的正面镀膜上。部分光束从镀膜上反射（反射光束），其余部分透射通过（透射光束）。</p>
<p><strong>优点：</strong></p>
<ul>
<li>成本低——简单的平面光学元件，易于制造</li>
<li>吸收低——光路中的材料最少</li>
<li>配合适当镀膜可实现高损伤阈值</li>
<li>有大尺寸可选，适用于宽光束</li>
<li>与立方分束器相比重量轻</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>背面（增透膜面）产生的<strong>鬼像反射</strong>会形成二次反射光束，干扰测量</li>
<li><strong>光束位移</strong>——透射光束因通过基底折射而横向偏移</li>
<li>45度入射时<strong>偏振依赖性强</strong>（由于斜入射下的菲涅耳方程，平板分束器本质上是偏振敏感的）</li>
<li>需要精确角度对准</li>
</ul>
<p><strong>最适合：</strong>对成本敏感的应用、基底吸收很重要的高功率系统、大光束直径、以及可以容忍或控制鬼像反射的装置。</p>

<h3>2. 立方分束器</h3>
<p><a href="/products/cube-beamsplitters/">立方分束器</a>是将两个直角棱镜沿斜面胶合在一起形成的。在胶合之前，分束膜镀在其中一个棱镜的斜面上。光从立方的一个面入射，碰到对角镀膜后被分开——透射光束继续直线传播，反射光束从侧面成90度射出。</p>
<p><strong>优点：</strong></p>
<ul>
<li>透射方向无光束位移——输出光束与输入保持共线</li>
<li>无鬼像反射——消除了平板分束器的背反射问题</li>
<li>更容易对准——入射面和出射面都与各自的光束垂直</li>
<li>结构紧凑、坚固</li>
<li>透射和反射光束在玻璃中的光程长度相等</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>比平板分束器成本高</li>
<li>更重、体积更大</li>
<li>由于通过基底的光程更长，吸收更多</li>
<li>胶合版的损伤阈值低于全介质平板分束器</li>
<li>限于中等光束尺寸（大立方非常昂贵）</li>
</ul>
<p><strong>最适合：</strong>成像系统、干涉测量、光纤光学，以及任何光束位移或鬼像反射会造成问题的应用。</p>

<h3>3. 非偏振立方分束器</h3>
<p><a href="/products/non-polarizing-cube-beamsplitters/">非偏振立方分束器</a>是一种特殊类型的立方分束器，设计用于<strong>无论偏振状态如何</strong>都能分光。标准立方分束器使用简单的介质膜，对S偏振光的反射效率高于P偏振光。非偏振镀膜使用复杂的多层膜设计，在设计角度（通常为45度）下对S和P偏振都实现相同的分束比。</p>
<p>关键规格是<strong>偏振灵敏度</strong>或<strong>Tp/Ts比</strong>。一个好的非偏振分束器可能有Tp = 50%和Ts = 48%，偏振灵敏度仅为2%——意味着无论输入偏振如何，透射率的变化只有2%。</p>
<p><strong>优点：</strong></p>
<ul>
<li>分束比稳定，不受输入偏振影响</li>
<li>无光束位移</li>
<li>无鬼像反射</li>
<li>对于偏振未知或变化的系统至关重要</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>比标准偏振敏感立方更贵</li>
<li>镀膜更复杂，有效波长范围更窄</li>
<li>损伤阈值略低于简单介质膜</li>
</ul>
<p><strong>最适合：</strong>非偏振光源、成像系统、光度测量、彩色分光，以及任何输入偏振变化或未知的系统。</p>

<h3>4. 偏振立方分束器（PBS）</h3>
<p><a href="/products/polarizing-cube-beamsplitters/">偏振立方分束器</a>（PBS）设计用于完全分离S偏振光和P偏振光。P偏振光（电场平行于入射面）以最小损耗透射通过立方，而S偏振光（电场垂直于入射面）被反射90度。在理想的PBS中，分离是完美的。实际上，总会有一些泄漏。</p>
<p>PBS立方的关键指标是<strong>消光比</strong>，它衡量两种偏振被分离的程度：</p>
<ul>
<li><strong>透射消光比</strong>（Tp/Ts）：透射的P偏振光与泄漏的S偏振光之比。通常为1000:1或更高。</li>
<li><strong>反射消光比</strong>（Rs/Rp）：反射的S偏振光与泄漏的P偏振光之比。通常为100:1到1000:1。</li>
</ul>
<p><strong>优点：</strong></p>
<ul>
<li>单个元件实现完全偏振分离</li>
<li>可提供非常高的消光比</li>
<li>透射方向无光束位移</li>
<li>偏振相关光学系统不可或缺</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>仅适用于特定波段（镀膜设计为窄带）</li>
<li>损伤阈值可能低于标准介质膜</li>
<li>如果入射角偏离45度，性能会下降</li>
<li>成本高于标准立方</li>
</ul>
<p><strong>最适合：</strong>需要偏振控制的激光系统、干涉测量、光隔离、Q开关和基于偏振的测量。</p>

<h2>分束器类型对比表</h2>
<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">特性</th><th style="border:1px solid #e2e8f0;padding:8px;">平板分束器</th><th style="border:1px solid #e2e8f0;padding:8px;">立方分束器</th><th style="border:1px solid #e2e8f0;padding:8px;">非偏振立方</th><th style="border:1px solid #e2e8f0;padding:8px;">偏振立方（PBS）</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>光束位移</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">有（明显）</td><td style="border:1px solid #e2e8f0;padding:8px;">无</td><td style="border:1px solid #e2e8f0;padding:8px;">无</td><td style="border:1px solid #e2e8f0;padding:8px;">无</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>鬼像反射</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">有（来自背面）</td><td style="border:1px solid #e2e8f0;padding:8px;">无</td><td style="border:1px solid #e2e8f0;padding:8px;">无</td><td style="border:1px solid #e2e8f0;padding:8px;">无</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>偏振灵敏度</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">高（固有）</td><td style="border:1px solid #e2e8f0;padding:8px;">中</td><td style="border:1px solid #e2e8f0;padding:8px;">低（&lt; 2%）</td><td style="border:1px solid #e2e8f0;padding:8px;">非常高（设计使然）</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>损伤阈值</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">最高</td><td style="border:1px solid #e2e8f0;padding:8px;">中</td><td style="border:1px solid #e2e8f0;padding:8px;">中低</td><td style="border:1px solid #e2e8f0;padding:8px;">低中</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>相对成本</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">最低</td><td style="border:1px solid #e2e8f0;padding:8px;">中</td><td style="border:1px solid #e2e8f0;padding:8px;">高</td><td style="border:1px solid #e2e8f0;padding:8px;">高</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>波长范围</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">可提供宽带</td><td style="border:1px solid #e2e8f0;padding:8px;">中-宽带</td><td style="border:1px solid #e2e8f0;padding:8px;">较窄（镀膜限制）</td><td style="border:1px solid #e2e8f0;padding:8px;">窄带（V型膜）</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><strong>最佳应用</strong></td><td style="border:1px solid #e2e8f0;padding:8px;">高功率激光、大光束</td><td style="border:1px solid #e2e8f0;padding:8px;">通用、成像</td><td style="border:1px solid #e2e8f0;padding:8px;">非偏振光、光度测量</td><td style="border:1px solid #e2e8f0;padding:8px;">偏振控制、隔离器</td></tr>
</table>

<h2>如何选择合适的分束器</h2>

<h3>第一步：明确您的应用</h3>
<p>应用决定一切。首先回答以下问题：</p>
<ul>
<li>光源是偏振的还是非偏振的？</li>
<li>波长（或波长范围）是多少？</li>
<li>您使用的功率水平是多少？</li>
<li>光束对准和位移有多关键？</li>
<li>您需要什么分束比？</li>
<li>波前质量（光束畸变）是否重要？</li>
</ul>

<h3>第二步：选择结构形式</h3>
<p>根据您的应用需求：</p>
<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">如果您需要……</th><th style="border:1px solid #e2e8f0;padding:8px;">请选择……</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">最低成本，且可以容忍鬼像反射和光束位移</td><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/beamsplitter-plates/">平板分束器</a></td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">无光束位移，干净的单反射光束</td><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/cube-beamsplitters/">立方分束器</a></td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">对非偏振或随机偏振光具有稳定的分束比</td><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/non-polarizing-cube-beamsplitters/">非偏振立方分束器</a></td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">S和P偏振完全分离</td><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/polarizing-cube-beamsplitters/">偏振立方分束器（PBS）</a></td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">尽可能高的激光损伤阈值</td><td style="border:1px solid #e2e8f0;padding:8px;">全介质镀膜平板分束器</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">超宽带分光（例如可见光+近红外）</td><td style="border:1px solid #e2e8f0;padding:8px;">平板分束器（镀膜范围更宽）</td></tr>
</table>

<h3>第三步：选择波长范围</h3>
<p>分束器镀膜是为特定波段设计的。在设计范围之外使用分束器会导致分束比不正确和潜在的高损耗。常见波段包括：</p>
<ul>
<li><strong>紫外（250–400 nm）：</strong>紫外熔融石英基底，特殊介质膜</li>
<li><strong>可见光（400–700 nm）：</strong>BK7基底，标准介质膜</li>
<li><strong>可见-近红外（400–900 nm）：</strong>宽带可见光+近红外</li>
<li><strong>近红外（700–1100 nm）：</strong>用于光纤和电信</li>
<li><strong>短波红外（1100–1700 nm）：</strong>用于电信C+L波段</li>
<li><strong>激光线：</strong>单波长（如532 nm、633 nm、1064 nm），优化分束比</li>
</ul>
<p>为了获得最精确的分束比，请始终选择与您特定波长相匹配的激光线镀膜，而不是宽带镀膜。宽带镀膜是以精度换取范围。</p>

<h3>第四步：确定分束比</h3>
<p>常见的标准分束比：</p>
<ul>
<li><strong>50/50（R/T）：</strong>最常见。平均分配用于监测、干涉测量和功率分配。</li>
<li><strong>70/30（R/T）：</strong>反射方向功率更多。当反射光束进入低灵敏度探测器时很有用。</li>
<li><strong>90/10（R/T）：</strong>采样配置。大部分功率透射，小部分反射用于监测。</li>
<li><strong>10/90（R/T）：</strong>反向采样。大部分功率反射，小部分透射用于监测。</li>
<li><strong>80/20、30/70等：</strong>可按需提供定制比例。</li>
</ul>
<p><strong>专业提示：</strong>如果您需要精确的功率比例，请明确指定。标准分束器的分束比容差通常为±5%或更差。对于精密应用，请要求严格的容差规格。</p>

<h2>常见应用与推荐配置</h2>

<h3>激光系统</h3>
<p>在激光系统中，分束器用作功率监测的采样镜、用于诊断的光束采样器，以及在干涉仪等腔结构中使用。对于高功率激光器，平板分束器通常是首选，因为立方分束器中的胶合剂在高强度下可能失效。对于低功率激光二极管和光纤激光器，立方分束器提供更干净的性能。</p>
<p><strong>推荐：</strong>高功率（&gt; 10 W连续）使用<a href="/products/beamsplitter-plates/">平板分束器</a>，中低功率使用<a href="/products/cube-beamsplitters/">立方分束器</a>。</p>

<h3>干涉测量</h3>
<p>干涉仪（迈克尔逊、马赫-曾德尔、菲索）依赖于精确的50/50分光和最小的波前畸变。立方分束器是首选，因为它们消除了光束位移和会产生虚假干涉条纹的鬼像反射。当必须保持偏振状态时，使用非偏振立方。</p>
<p><strong>推荐：</strong>波前规格为λ/10的高品质<a href="/products/cube-beamsplitters/">立方分束器</a>，对于非偏振光源优选非偏振型。</p>

<h3>机器视觉与成像</h3>
<p>在机器视觉中，分束器用于同轴照明分光、荧光显微镜和多相机设置。非偏振立方分束器是首选，因为大多数成像光源的光是非偏振的，偏振相关的分束会造成不准确的颜色或强度再现。</p>
<p><strong>推荐：</strong>可见光范围成像应用使用<a href="/products/non-polarizing-cube-beamsplitters/">非偏振立方分束器</a>。</p>

<h3>光纤与电信</h3>
<p>在光纤系统中，分束器（在光纤形式中通常称为"耦合器"）将光信号分配用于监测、测试和分发。自由空间分束器用于光纤台式装置和光纤-自由空间接口。偏振分束器对于偏振分集接收机和相干通信至关重要。</p>
<p><strong>推荐：</strong>偏振敏感系统使用<a href="/products/polarizing-cube-beamsplitters/">偏振立方分束器</a>；功率分配使用<a href="/products/cube-beamsplitters/">标准立方分束器</a>。</p>

<h3>光谱与分析仪器</h3>
<p>光谱仪、荧光计和吸光度仪器使用分束器用于参考通道、双探测器光束分光和波长校准。宽带覆盖至关重要，而且通常需要非偏振性能，因为许多样品类型会使光退偏。</p>
<p><strong>推荐：</strong>宽带非偏振平板或立方分束器，具体取决于空间和对准限制。</p>

<h2>5个常见分束器错误及避免方法</h2>

<h3>1. 忽略偏振依赖性</h3>
<p>这是排名第一的错误。大多数标准分束器（平板和立方）在45度入射时对S和P偏振光有显著不同的分束比。如果您的输入光束偏振发生变化——由于光纤弯曲、旋转或退偏样品——您的分束比也会变化。在光度测量和成像系统中，这会导致测量误差和强度波动。</p>
<p><strong>解决方法：</strong>如果您有非偏振或随机偏振光，请使用<a href="/products/non-polarizing-cube-beamsplitters/">非偏振分束器</a>。验证偏振灵敏度规格——寻找S和P之间变化小于2%的产品。如果您的系统是偏振受控的，标准立方就可以正常工作。</p>

<h3>2. 忘记平板分束器的鬼像反射</h3>
<p>每个平板分束器都有两个反射面：正面（镀膜）和背面（增透膜）。即使是好的增透膜每面也会留下约0.25%的反射。这意味着您会得到一个主反射光束（来自正面镀膜）和一个较弱的"鬼像"光束（来自背面），后者的偏移距离与平板厚度成正比。在成像系统中，这会产生重影。在干涉测量中，它会产生虚假的条纹图案。</p>
<p><strong>解决方法：</strong>如果鬼像反射不可接受，请使用<a href="/products/cube-beamsplitters/">立方分束器</a>。如果必须使用平板，请选择楔形平板将鬼像光束与主光束空间分开，或倾斜平板使鬼像光束偏离您的探测器。</p>

<h3>3. 选择错误的波段</h3>
<p>分束器镀膜是针对特定波长范围精确设计的。为1064 nm设计的"50/50"分束器在532 nm时可能是30/70，在1550 nm时可能是80/20。当您只需要单一波长时使用宽带分束器，精度会比激光线镀膜差。当用于宽带用途时使用激光线镀膜，分束比会不正确。</p>
<p><strong>解决方法：</strong>将分束器镀膜波段与您的实际工作波长相匹配。对于单色光源（激光器），使用激光线镀膜以获得最精确的分束比。对于宽带光源，使用宽带镀膜，并接受整个波段内典型的±10%变化。</p>

<h3>4. 低估功率处理要求</h3>
<p>分束器的损伤阈值低于反射镜，因为镀膜设计为部分透射——更多的膜层暴露在光下，镀膜中的电场分布会产生热点。胶合立方分束器尤其脆弱，因为胶合层会吸收光并在相对较低的功率水平下失效。</p>
<p><strong>解决方法：</strong>对于功率高于约5 W连续波或脉冲能量高于约0.1 J/cm²的情况，使用<a href="/products/beamsplitter-plates/">全介质平板分束器</a>而不是胶合立方。对于高功率脉冲激光器，请指定带有已验证损伤阈值的激光线镀膜。始终降额使用——选择额定功率至少是您实际功率2-3倍的分束器。</p>

<h3>5. 忽视透射中的光束位移</h3>
<p>平板分束器会导致透射光束横向偏移，因为光通过倾斜的基底时发生折射。位移大小取决于平板厚度和折射率。对于3毫米厚的BK7平板，45度入射时位移约为1毫米——这足以在精密系统中打乱对准。如果您的系统中有多个平板分束器，位移会叠加。</p>
<p><strong>解决方法：</strong>当对准精度至关重要时，使用<a href="/products/cube-beamsplitters/">立方分束器</a>——它们产生的透射光束位移为零。如果必须使用平板，请在您的光学设计中考虑位移，或使用更薄的平板来最小化位移。</p>

<h2>产品选型指南</h2>

<h3>立方分束器</h3>
<ul>
<li><a href="/products/cube-beamsplitters/">标准立方分束器</a> — 可见光和近红外范围；50/50和70/30比例；BK7基底；适用于一般成像和激光装置</li>
<li><a href="/products/non-polarizing-cube-beamsplitters/">非偏振立方分束器</a> — 对非偏振光具有稳定分束比；低偏振灵敏度（&lt; 2%）；最适合光度测量和成像</li>
<li><a href="/products/polarizing-cube-beamsplitters/">偏振立方分束器（PBS）</a> — 高消光比（透射1000:1）；提供532 nm、633 nm、808 nm、1064 nm激光线版本</li>
</ul>

<h3>平板分束器</h3>
<ul>
<li><a href="/products/beamsplitter-plates/">平板分束器</a> — 全介质镀膜；损伤阈值高于胶合立方；提供25.4 mm和50 mm尺寸；50/50和90/10标准比例</li>
</ul>

<h3>配套偏振光学元件</h3>
<ul>
<li><a href="/products/visible-linear-polarizers/">可见光线性偏振片</a> — 与PBS立方配对用于偏振控制装置；BK7基底上的高消光比偏振膜</li>
<li><a href="/products/ir-polarizers/">红外偏振片</a> — 用于近红外和短波红外应用；线栅或二向色偏振片选项</li>
<li><a href="/products/cemented-zero-order-waveplates/">零级波片</a> — 与PBS立方配合使用旋转偏振和调整分束比；1/2波片用于旋转，1/4波片用于圆偏振</li>
<li><a href="/products/glan-taylor-prisms/">格兰泰勒棱镜</a> — 用于要求苛刻的偏振应用的超高消光比（&gt; 100,000:1）</li>
</ul>

<h3>相关光学元件</h3>
<ul>
<li><a href="/products/bk7-right-angle-prisms/">BK7直角棱镜</a> — 分束器和转向镜组件的基础构建块</li>
<li><a href="/products/broadband-dielectric-mirrors/">宽带介质反射镜</a> — 与分束器配合用作折叠镜的高反射镜</li>
<li><a href="/products/laser-line-high-reflected-mirrors/">激光线高反射镜</a> — 用于激光线分束器装置的高反射镜</li>
</ul>

<h2>结论</h2>
<p>选择合适的分束器比仅仅选择50/50比例然后添加到您的光学系统中要复杂得多。结构形式——平板还是立方，偏振型还是非偏振型——决定了从光束对准则偏振纯度再到功率处理的一切。平板分束器提供最高的损伤阈值和最低的成本，但会带来鬼像反射和光束位移。立方分束器消除了这些问题，代价是功率处理能力较低和价格较高。非偏振立方能准确处理非偏振光，而偏振立方则提供对偏振敏感系统必不可少的干净S/P分离。</p>
<p>在恒鼎光，我们制造全部四种分束器类型，提供覆盖紫外、可见光和红外波长的标准和定制镀膜。我们的技术团队可以帮助您为特定应用指定合适的分束器——包括镀膜设计、基底材料、分束比容差和损伤阈值。无论您需要用于原型的单个50/50立方，还是用于生产仪器的定制分束器阵列，我们都可以从概念到交付为您的设计提供支持。</p>"""

print("Blog #36 content generated successfully.")
print(f"English content length: {len(content_en)} chars")
print(f"Chinese content length: {len(content_zh)} chars")
