#!/usr/bin/env python3
"""
Generate 5 blog articles (EN+ZH), update blog-data.js, and update 5 blog HTML pages.
"""

import json
import re
import os

BASE_DIR = "/app/data/所有对话/主对话/PhotonEdge-V64"

# ============================================================
# Article 1: How to Choose the Right Optical Lens
# ============================================================
article1_en = '''<h2>Introduction</h2>
<p>Selecting the right optical lens is one of the most critical decisions in optical system design. Whether you are building a laser beam expander, a machine vision system, or a fiber coupling assembly, the lens type, material, focal length, and coating directly determine system performance. This guide walks you through the key factors to consider and provides practical recommendations for common applications.</p>

<h2>Understanding Lens Types</h2>
<p>Optical lenses come in several fundamental geometries, each optimized for different functions. Understanding these types is the first step toward making the right selection.</p>

<h3>Plano-Convex Lenses</h3>
<p>A plano-convex lens has one flat surface and one spherical convex surface. This is the most commonly used positive lens in optical systems because it minimizes spherical aberration when the curved surface faces the longer conjugate (the side with the greater object or image distance). For collimating a point source or focusing collimated light, orient the curved side toward the collimated beam.</p>
<ul>
<li>Best for: Collimation, light focusing, and simple imaging</li>
<li>Typical focal length range: 5 mm to 1000 mm</li>
<li>Aberration performance: Good for on-axis applications with proper orientation</li>
</ul>
<p>PhotonEdge offers a comprehensive range of <a href="/products/bk7-plano-convex/">BK7 Plano-Convex Lenses</a> with focal lengths from 6 mm to 1000 mm, all available with anti-reflection coatings.</p>

<h3>Bi-Convex Lenses</h3>
<p>A bi-convex (or double-convex) lens has two convex spherical surfaces. It provides a shorter focal length than a plano-convex lens of the same diameter and is symmetric, making it ideal for 1:1 imaging and relay systems. However, for non-symmetric conjugate ratios, a plano-convex lens typically delivers better aberration performance.</p>
<ul>
<li>Best for: 1:1 imaging, relay optics, and short-focal-length applications</li>
<li>Advantage: Symmetric design reduces coma in near-unit-magnification setups</li>
</ul>
<p>Explore our <a href="/products/bk7-bi-convex/">BK7 Bi-Convex Lenses</a> for symmetric imaging applications.</p>

<h3>Plano-Concave Lenses</h3>
<p>A plano-concave lens has one flat and one concave spherical surface, producing a negative focal length. It diverges incident collimated light and is commonly used to expand laser beams or increase system focal length in Galilean beam expanders.</p>
<ul>
<li>Best for: Beam expansion, diverging light, and Galilean telescope designs</li>
<li>Key consideration: Orient the curved surface toward the collimated input to minimize aberration</li>
</ul>
<p>See our <a href="/products/bk7-plano-concave/">BK7 Plano-Concave Lenses</a> for beam expansion applications.</p>

<h3>Achromatic Lenses</h3>
<p>An achromatic doublet consists of a positive and a negative element cemented together, made from glasses with different dispersions (e.g., crown and flint). This design brings two wavelengths to a common focus, dramatically reducing chromatic aberration compared to singlet lenses. Achromatic lenses are the workhorse of broadband imaging systems.</p>
<ul>
<li>Best for: Broadband imaging, microscopy, and photographic objectives</li>
<li>Chromatic correction: Axial color corrected at two wavelengths; lateral color significantly reduced</li>
</ul>

<h2>Key Selection Parameters</h2>
<p>Beyond lens type, several parameters govern lens selection. Here are the most important ones:</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">Parameter</th><th style="border:1px solid #e2e8f0;padding:8px;">What It Affects</th><th style="border:1px solid #e2e8f0;padding:8px;">Typical Specification</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Focal Length (f)</td><td style="border:1px solid #e2e8f0;padding:8px;">Image distance, magnification, NA</td><td style="border:1px solid #e2e8f0;padding:8px;">5 mm – 1000 mm (&plusmn;1%)</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Material</td><td style="border:1px solid #e2e8f0;padding:8px;">Transmission range, refractive index, cost</td><td style="border:1px solid #e2e8f0;padding:8px;">BK7, UV Fused Silica, CaF2</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Diameter</td><td style="border:1px solid #e2e8f0;padding:8px;">Light gathering, f-number</td><td style="border:1px solid #e2e8f0;padding:8px;">3 mm – 100 mm</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Surface Quality</td><td style="border:1px solid #e2e8f0;padding:8px;">Scatter, image contrast</td><td style="border:1px solid #e2e8f0;padding:8px;">40-20 scratch-dig (precision) to 60-40</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Coating</td><td style="border:1px solid #e2e8f0;padding:8px;">Reflection loss, transmission efficiency</td><td style="border:1px solid #e2e8f0;padding:8px;">BBAR, V-coat, or uncoated</td></tr>
</table>

<h2>Application-Specific Recommendations</h2>

<h3>Imaging and Machine Vision</h3>
<p>For imaging systems operating over the visible spectrum (400–700 nm), achromatic doublets are strongly preferred over singlets. They correct both spherical and chromatic aberration, delivering sharper images across the field. For monochromatic laser-based vision (e.g., structured light 3D scanning), a plano-convex singlet with a V-coat AR coating can be more cost-effective while delivering excellent on-axis performance.</p>

<h3>Laser Collimation and Focusing</h3>
<p>Laser applications demand lenses with low absorption and high laser damage threshold. UV fused silica plano-convex lenses are the top choice for UV and high-power lasers due to their low absorption and high LIDT. For visible and near-IR lasers, BK7 plano-convex lenses with V-coat AR coatings provide excellent performance at lower cost. Always orient the curved surface toward the collimated beam to minimize spherical aberration.</p>

<h3>Fiber Optic Coupling</h3>
<p>Fiber coupling requires aspheric lenses to achieve the tight focus needed for efficient coupling into single-mode fibers. Ball lenses and GRIN lenses are also used for compact coupling assemblies. For multimode fibers, a well-designed plano-convex or achromatic lens can achieve acceptable coupling efficiency. The NA of the lens must match or exceed the NA of the fiber for optimal coupling.</p>

<h2>PhotonEdge Lens Products</h2>
<p>PhotonEdge manufactures precision optical lenses with tight focal length tolerances and surface quality up to 20-10 scratch-dig. Our standard catalog includes:</p>
<ul>
<li><a href="/products/bk7-plano-convex/">BK7 Plano-Convex Lenses</a> — The most versatile positive lens, available from 6 mm to 1000 mm EFL</li>
<li><a href="/products/bk7-bi-convex/">BK7 Bi-Convex Lenses</a> — Symmetric positive lenses ideal for relay optics</li>
<li><a href="/products/bk7-plano-concave/">BK7 Plano-Concave Lenses</a> — Negative lenses for beam expansion</li>
<li>UV Fused Silica variants for UV and high-power laser applications</li>
<li>All lenses available with MgF2, BBAR, or V-coat anti-reflection coatings</li>
</ul>

<h2>Conclusion</h2>
<p>Choosing the right optical lens requires balancing lens type, material, focal length, and coating against your application requirements and budget. For most imaging applications, achromatic doublets provide the best balance of performance and cost. For monochromatic laser applications, a properly oriented plano-convex singlet with the right AR coating is often the optimal choice. PhotonEdge offers both catalog and custom lenses to meet your exact specifications — contact our technical team for personalized guidance.</p>'''

article1_zh = '''<h2>引言</h2>
<p>选择合适的光学透镜是光学系统设计中最关键的决策之一。无论您是在构建激光扩束器、机器视觉系统还是光纤耦合组件，透镜类型、材料、焦距和镀膜都直接决定系统性能。本指南将引导您了解关键因素，并为常见应用提供实用建议。</p>

<h2>了解透镜类型</h2>
<p>光学透镜有几种基本几何形状，每种都针对不同功能进行了优化。了解这些类型是做出正确选择的第一步。</p>

<h3>平凸透镜</h3>
<p>平凸透镜有一个平面和一个凸球面。这是光学系统中最常用的正透镜，因为当曲面朝向较长的共轭距离时，它能最小化球差。对于准直点光源或聚焦准直光，应将曲面朝向准直光束。</p>
<ul>
<li>最佳用途：准直、光聚焦和简单成像</li>
<li>典型焦距范围：5 mm 至 1000 mm</li>
<li>像差表现：正确朝向时，轴上应用表现良好</li>
</ul>
<p>恒鼎光提供全面的<a href="/products/bk7-plano-convex/">BK7平凸透镜</a>系列，焦距从6 mm到1000 mm，均可配备减反射镀膜。</p>

<h3>双凸透镜</h3>
<p>双凸透镜有两个凸球面，在相同直径下比平凸透镜提供更短的焦距，且对称设计使其非常适合1:1成像和中继系统。但在非对称共轭比的情况下，平凸透镜通常具有更好的像差表现。</p>
<ul>
<li>最佳用途：1:1成像、中继光学和短焦距应用</li>
<li>优势：对称设计减少了近单位放大倍率设置中的彗差</li>
</ul>
<p>浏览我们的<a href="/products/bk7-bi-convex/">BK7双凸透镜</a>，适用于对称成像应用。</p>

<h3>平凹透镜</h3>
<p>平凹透镜有一个平面和一个凹球面，产生负焦距。它使入射准直光发散，常用于扩展激光束或在伽利略扩束器中增加系统焦距。</p>
<ul>
<li>最佳用途：扩束、光发散和伽利略望远镜设计</li>
<li>关键考虑：将曲面朝向准直输入以最小化像差</li>
</ul>
<p>查看我们的<a href="/products/bk7-plano-concave/">BK7平凹透镜</a>，用于扩束应用。</p>

<h3>消色差透镜</h3>
<p>消色差双合透镜由一个正元件和一个负元件胶合而成，由不同色散的玻璃制成（如冕牌和火石玻璃）。该设计使两个波长会聚于同一焦点，与单透镜相比大大减少了色差。消色差透镜是宽带成像系统的主力元件。</p>
<ul>
<li>最佳用途：宽带成像、显微镜和摄影物镜</li>
<li>色差校正：在两个波长处校正轴向色差；横向色差显著降低</li>
</ul>

<h2>关键选择参数</h2>
<p>除了透镜类型，还有几个参数决定透镜选择。以下是最重要的参数：</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">参数</th><th style="border:1px solid #e2e8f0;padding:8px;">影响</th><th style="border:1px solid #e2e8f0;padding:8px;">典型规格</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">焦距 (f)</td><td style="border:1px solid #e2e8f0;padding:8px;">像距、放大倍率、NA</td><td style="border:1px solid #e2e8f0;padding:8px;">5 mm – 1000 mm (±1%)</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">材料</td><td style="border:1px solid #e2e8f0;padding:8px;">透过范围、折射率、成本</td><td style="border:1px solid #e2e8f0;padding:8px;">BK7、紫外熔融石英、CaF2</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">直径</td><td style="border:1px solid #e2e8f0;padding:8px;">集光能力、f数</td><td style="border:1px solid #e2e8f0;padding:8px;">3 mm – 100 mm</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">表面质量</td><td style="border:1px solid #e2e8f0;padding:8px;">散射、图像对比度</td><td style="border:1px solid #e2e8f0;padding:8px;">40-20 划痕-麻点（精密级）至 60-40</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">镀膜</td><td style="border:1px solid #e2e8f0;padding:8px;">反射损耗、透过效率</td><td style="border:1px solid #e2e8f0;padding:8px;">BBAR、V涂层或无镀膜</td></tr>
</table>

<h2>应用场景推荐</h2>

<h3>成像与机器视觉</h3>
<p>对于在可见光谱（400–700 nm）下工作的成像系统，消色差双合透镜比单透镜更受推荐。它们同时校正球差和色差，在整个视场提供更锐利的图像。对于基于单色激光的视觉系统（如结构光3D扫描），配备V涂层AR镀膜的平凸单透镜更具成本效益，同时提供出色的轴上性能。</p>

<h3>激光准直与聚焦</h3>
<p>激光应用要求透镜具有低吸收和高激光损伤阈值。紫外熔融石英平凸透镜是紫外和高功率激光的首选，因为其低吸收和高LIDT。对于可见光和近红外激光，配备V涂层AR镀膜的BK7平凸透镜以较低成本提供出色性能。始终将曲面朝向准直光束以最小化球差。</p>

<h3>光纤耦合</h3>
<p>光纤耦合需要非球面透镜来实现高效耦合进单模光纤所需的紧密聚焦。球透镜和GRIN透镜也用于紧凑耦合组件。对于多模光纤，设计良好的平凸或消色差透镜可达到可接受的耦合效率。透镜的NA必须等于或超过光纤的NA才能实现最佳耦合。</p>

<h2>恒鼎光透镜产品</h2>
<p>恒鼎光制造精密光学透镜，焦距公差严格，表面质量最高可达20-10划痕-麻点。我们的标准目录包括：</p>
<ul>
<li><a href="/products/bk7-plano-convex/">BK7平凸透镜</a> — 最通用的正透镜，EFL从6 mm到1000 mm</li>
<li><a href="/products/bk7-bi-convex/">BK7双凸透镜</a> — 适用于中继光学的对称正透镜</li>
<li><a href="/products/bk7-plano-concave/">BK7平凹透镜</a> — 用于扩束的负透镜</li>
<li>紫外熔融石英变体，用于紫外和高功率激光应用</li>
<li>所有透镜均可配备MgF2、BBAR或V涂层减反射镀膜</li>
</ul>

<h2>结论</h2>
<p>选择合适的光学透镜需要在透镜类型、材料、焦距和镀膜之间进行平衡，同时考虑应用需求和预算。对于大多数成像应用，消色差双合透镜提供了性能和成本的最佳平衡。对于单色激光应用，正确朝向并配备合适AR镀膜的平凸单透镜通常是最佳选择。恒鼎光提供目录和定制透镜以满足您的精确规格——请联系我们的技术团队获取个性化指导。</p>'''


# ============================================================
# Article 2: Understanding Anti-Reflection Coatings
# ============================================================
article2_en = '''<h2>Introduction</h2>
<p>Every air-glass interface in an optical system reflects approximately 4% of incident light at normal incidence (for n ≈ 1.5). In a multi-element system with 10 surfaces, this amounts to a total transmission loss of about 34% — before accounting for absorption. Anti-reflection (AR) coatings are thin-film coatings designed to reduce this Fresnel reflection, maximizing transmission and eliminating ghost images. Understanding AR coating types and their specifications is essential for optimizing any optical system.</p>

<h2>How AR Coatings Work</h2>
<p>AR coatings operate on the principle of destructive interference. A thin film of controlled thickness and refractive index is deposited on the glass surface. Light reflected from the film-air interface and light reflected from the film-glass interface interfere destructively, canceling the reflected beam and transmitting more light into the optic.</p>
<p>For a single-layer quarter-wave coating at design wavelength &lambda;<sub>0</sub>, the film thickness is &lambda;<sub>0</sub>/4n<sub>f</sub>, where n<sub>f</sub> is the film refractive index. Perfect cancellation occurs when n<sub>f</sub> = &radic;(n<sub>s</sub>), where n<sub>s</sub> is the substrate index. For BK7 (n = 1.517), the ideal film index is 1.233 — lower than any practical deposition material.</p>

<h2>Single-Layer AR Coatings</h2>
<p>The most common single-layer AR coating is magnesium fluoride (MgF<sub>2</sub>), with a refractive index of approximately 1.38. While this does not achieve perfect index matching, it reduces single-surface reflection from 4.0% to about 1.5% at the design wavelength for BK7. MgF<sub>2</sub> coatings are inexpensive, durable, and widely available.</p>
<ul>
<li>Material: MgF<sub>2</sub> (n &asymp; 1.38)</li>
<li>Reflection per surface: ~1.5% at design wavelength for BK7</li>
<li>Effective bandwidth: Narrow (R increases rapidly away from design wavelength)</li>
<li>Best for: Cost-sensitive applications, single-wavelength systems</li>
<li>Laser damage threshold: High (>10 J/cm<sup>2</sup> at 1064 nm, 10 ns)</li>
</ul>

<h2>Multi-Layer Broadband AR Coatings</h2>
<p>Multi-layer AR coatings use two or more thin films of alternating high and low refractive index materials (e.g., TiO<sub>2</sub>/SiO<sub>2</sub> or ZrO<sub>2</sub>/MgF<sub>2</sub>) to achieve low reflectance over a broad wavelength range. A typical broadband AR (BBAR) coating for the visible spectrum (400–700 nm) achieves less than 0.5% reflectance per surface across the entire range.</p>
<ul>
<li>Typical layers: 2–5 per surface</li>
<li>Reflectance: &lt;0.5% per surface across the specified bandwidth</li>
<li>Common broadband ranges: VIS (400–700 nm), NIR (650–1050 nm), SWIR (900–1700 nm)</li>
<li>Best for: Imaging systems, broadband sources, white-light applications</li>
</ul>

<h2>V-Coat vs Broadband AR</h2>
<p>The choice between V-coat and broadband AR coatings depends on the spectral characteristics of your light source:</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">Feature</th><th style="border:1px solid #e2e8f0;padding:8px;">V-Coat</th><th style="border:1px solid #e2e8f0;padding:8px;">Broadband AR</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Shape</td><td style="border:1px solid #e2e8f0;padding:8px;">V-shaped R(&lambda;) curve</td><td style="border:1px solid #e2e8f0;padding:8px;">Flat, low R over broad range</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Min. reflectance</td><td style="border:1px solid #e2e8f0;padding:8px;">&lt;0.1% at design wavelength</td><td style="border:1px solid #e2e8f0;padding:8px;">&lt;0.5% across bandwidth</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Effective bandwidth</td><td style="border:1px solid #e2e8f0;padding:8px;">Narrow (~&plusmn;5% of &lambda;<sub>0</sub>)</td><td style="border:1px solid #e2e8f0;padding:8px;">Broad (hundreds of nm)</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Laser damage threshold</td><td style="border:1px solid #e2e8f0;padding:8px;">Highest (fewer interfaces)</td><td style="border:1px solid #e2e8f0;padding:8px;">Good (more layers)</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Cost</td><td style="border:1px solid #e2e8f0;padding:8px;">Moderate</td><td style="border:1px solid #e2e8f0;padding:8px;">Moderate to High</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Best application</td><td style="border:1px solid #e2e8f0;padding:8px;">Single-wavelength lasers</td><td style="border:1px solid #e2e8f0;padding:8px;">Imaging, broadband sources</td></tr>
</table>

<h2>Selecting AR Coatings by Wavelength</h2>

<h3>UV Applications (190–400 nm)</h3>
<p>UV applications require coatings on UV-grade fused silica substrates with UV-transparent materials. Standard MgF<sub>2</sub>/LiF coatings work down to about 200 nm. For deep UV (below 200 nm), special coating designs and ultra-high-vacuum deposition processes are needed. Avoid epoxy cements in UV beam paths, as they yellow and absorb.</p>

<h3>Visible Applications (400–700 nm)</h3>
<p>The visible range is the easiest to coat effectively. MgF<sub>2</sub> single-layer coatings work for monochromatic visible lasers. For broadband visible applications (microscopy, photography), multi-layer BBAR coatings (400–700 nm or 350–700 nm) are standard. These achieve less than 0.5% reflectance per surface.</p>

<h3>NIR and IR Applications (700 nm – 20 &mu;m)</h3>
<p>NIR coatings typically use SiO<sub>2</sub>/TiO<sub>2</sub> or SiO<sub>2</sub>/Ta<sub>2</sub>O<sub>5</sub> layer pairs. For mid-IR applications on ZnSe or Ge substrates, different material systems (e.g., ThF<sub>4</sub>/ZnSe) are required. IR coatings must also consider absorption in the coating layers, which can cause thermal lensing in high-power CO<sub>2</sub> laser systems.</p>

<h2>Impact on System Performance</h2>
<p>AR coatings affect system performance in several ways beyond simple transmission improvement:</p>
<ul>
<li><strong>Ghost image suppression:</strong> Uncoated surfaces create parasitic reflections (ghost images) that reduce image contrast. AR coatings minimize these reflections, improving MTF and signal-to-noise ratio.</li>
<li><strong>Laser damage threshold:</strong> The coating is typically the weakest link in a laser optics chain. V-coats generally offer higher LIDT than broadband coatings at their design wavelength.</li>
<li><strong>Environmental durability:</strong> Coatings must survive humidity, temperature cycling, and cleaning. MgF<sub>2</sub> single-layer coatings pass MIL-C-675 adhesion and abrasion tests; multi-layer coatings should meet similar durability standards.</li>
<li><strong>Cosmetic inspection:</strong> Coating defects (pinholes, spatter, uncoated spots) can create localized high-reflection zones. Specify acceptable defect density for critical applications.</li>
</ul>

<h2>PhotonEdge Coated Optics</h2>
<p>PhotonEdge offers a full range of AR-coated optical components with coating options to match your application:</p>
<ul>
<li><a href="/products/laser-line-high-reflected-mirrors/">Laser Line Mirrors</a> — With precision V-coat AR on the rear surface</li>
<li><a href="/products/broadband-dielectric-mirrors/">Broadband Dielectric Mirrors</a> — With BBAR coating options on transmissive optics</li>
<li>Custom AR coatings for any wavelength range from 193 nm to 10.6 &mu;m</li>
<li>Coating quality verified by spectrophotometry with certificates of conformance</li>
</ul>

<h2>Conclusion</h2>
<p>AR coatings are a small but crucial part of optical system design. For single-wavelength laser applications, V-coats provide the lowest reflection and highest damage threshold. For broadband imaging, multi-layer BBAR coatings deliver consistent performance across the spectrum. Even a simple MgF<sub>2</sub> coating can reduce reflection from 4% to 1.5%, a meaningful improvement in multi-element systems. When specifying AR coatings, always match the coating bandwidth to your source spectrum and verify LIDT for laser applications. PhotonEdge can help you select and specify the right coating for any application.</p>'''

article2_zh = '''<h2>引言</h2>
<p>光学系统中每个空气-玻璃界面在垂直入射时反射约4%的入射光（n ≈ 1.5时）。在具有10个表面的多元件系统中，总透过损失约达34%——这还未计入吸收。减反射（AR）镀膜是旨在减少这种菲涅尔反射的薄膜镀层，最大化透过率并消除鬼像。了解AR镀膜类型及其规格对优化任何光学系统都至关重要。</p>

<h2>AR镀膜的工作原理</h2>
<p>AR镀膜基于相消干涉原理工作。在玻璃表面沉积一层受控厚度和折射率的薄膜。从膜-空气界面反射的光和从膜-玻璃界面反射的光发生相消干涉，抵消反射光束，使更多光透入光学元件。</p>
<p>对于设计波长&lambda;<sub>0</sub>处的单层四分之一波长镀膜，膜厚为&lambda;<sub>0</sub>/4n<sub>f</sub>，其中n<sub>f</sub>是薄膜折射率。当n<sub>f</sub> = &radic;(n<sub>s</sub>)时实现完美抵消，其中n<sub>s</sub>是基底折射率。对于BK7（n = 1.517），理想膜层折射率为1.233——低于任何实际沉积材料。</p>

<h2>单层AR镀膜</h2>
<p>最常见的单层AR镀膜是氟化镁（MgF<sub>2</sub>），折射率约1.38。虽然这不能实现完美的折射率匹配，但它将BK7在设计波长处的单面反射从4.0%降至约1.5%。MgF<sub>2</sub>镀膜价格低廉、耐用且广泛可用。</p>
<ul>
<li>材料：MgF<sub>2</sub>（n ≈ 1.38）</li>
<li>每面反射：BK7设计波长处约1.5%</li>
<li>有效带宽：窄（偏离设计波长后R快速增加）</li>
<li>最佳用途：成本敏感应用、单波长系统</li>
<li>激光损伤阈值：高（>10 J/cm²，1064 nm，10 ns）</li>
</ul>

<h2>多层宽带AR镀膜</h2>
<p>多层AR镀膜使用两层或更多交替高低折射率材料薄膜（如TiO<sub>2</sub>/SiO<sub>2</sub>或ZrO<sub>2</sub>/MgF<sub>2</sub>），在宽波长范围内实现低反射率。典型的可见光谱（400–700 nm）宽带AR（BBAR）镀膜在整个范围内实现每面低于0.5%的反射率。</p>
<ul>
<li>典型层数：每面2–5层</li>
<li>反射率：指定带宽内每面&lt;0.5%</li>
<li>常见宽带范围：VIS（400–700 nm）、NIR（650–1050 nm）、SWIR（900–1700 nm）</li>
<li>最佳用途：成像系统、宽带光源、白光应用</li>
</ul>

<h2>V涂层与宽带AR对比</h2>
<p>V涂层和宽带AR镀膜的选择取决于光源的光谱特性：</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">特性</th><th style="border:1px solid #e2e8f0;padding:8px;">V涂层</th><th style="border:1px solid #e2e8f0;padding:8px;">宽带AR</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">形状</td><td style="border:1px solid #e2e8f0;padding:8px;">V形R(λ)曲线</td><td style="border:1px solid #e2e8f0;padding:8px;">宽带范围内平坦低R</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">最低反射率</td><td style="border:1px solid #e2e8f0;padding:8px;">设计波长处&lt;0.1%</td><td style="border:1px solid #e2e8f0;padding:8px;">带宽内&lt;0.5%</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">有效带宽</td><td style="border:1px solid #e2e8f0;padding:8px;">窄（约±5% &lambda;<sub>0</sub>）</td><td style="border:1px solid #e2e8f0;padding:8px;">宽（数百nm）</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">激光损伤阈值</td><td style="border:1px solid #e2e8f0;padding:8px;">最高（界面较少）</td><td style="border:1px solid #e2e8f0;padding:8px;">良好（层数更多）</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">成本</td><td style="border:1px solid #e2e8f0;padding:8px;">中等</td><td style="border:1px solid #e2e8f0;padding:8px;">中等到高</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">最佳应用</td><td style="border:1px solid #e2e8f0;padding:8px;">单波长激光</td><td style="border:1px solid #e2e8f0;padding:8px;">成像、宽带光源</td></tr>
</table>

<h2>按波长选择AR镀膜</h2>

<h3>紫外应用（190–400 nm）</h3>
<p>紫外应用需要紫外级熔融石英基底上的紫外透明材料镀膜。标准MgF<sub>2</sub>/LiF镀膜可工作至约200 nm。对于深紫外（200 nm以下），需要特殊镀膜设计和超高真空沉积工艺。避免在紫外光路中使用环氧胶，它们会变黄并吸收。</p>

<h3>可见光应用（400–700 nm）</h3>
<p>可见光范围最容易有效镀膜。MgF<sub>2</sub>单层镀膜适用于单色可见激光。对于宽带可见光应用（显微镜、摄影），多层BBAR镀膜（400–700 nm或350–700 nm）是标准选择，每面反射率低于0.5%。</p>

<h3>近红外和红外应用（700 nm – 20 μm）</h3>
<p>近红外镀膜通常使用SiO<sub>2</sub>/TiO<sub>2</sub>或SiO<sub>2</sub>/Ta<sub>2</sub>O<sub>5</sub>层对。对于ZnSe或Ge基底上的中红外应用，需要不同的材料系统（如ThF<sub>4</sub>/ZnSe）。红外镀膜还必须考虑膜层吸收，这会在高功率CO<sub>2</sub>激光系统中引起热透镜效应。</p>

<h2>对系统性能的影响</h2>
<p>AR镀膜以多种方式影响系统性能，不仅限于透过率提升：</p>
<ul>
<li><strong>鬼像抑制：</strong>未镀膜表面产生寄生反射（鬼像），降低图像对比度。AR镀膜最小化这些反射，改善MTF和信噪比。</li>
<li><strong>激光损伤阈值：</strong>镀膜通常是激光光学链中最薄弱的环节。V涂层在其设计波长处通常提供比宽带镀膜更高的LIDT。</li>
<li><strong>环境耐久性：</strong>镀膜必须经受湿度、温度循环和清洁。MgF<sub>2</sub>单层镀膜通过MIL-C-675附着和磨损测试；多层镀膜应满足类似的耐久性标准。</li>
<li><strong>外观检查：</strong>镀膜缺陷（针孔、飞溅、未镀膜斑点）会产生局部高反射区。对于关键应用，应规定可接受的缺陷密度。</li>
</ul>

<h2>恒鼎光镀膜光学元件</h2>
<p>恒鼎光提供全系列AR镀膜光学元件，镀膜选项匹配您的应用：</p>
<ul>
<li><a href="/products/laser-line-high-reflected-mirrors/">激光线反射镜</a> — 后表面配有精密V涂层AR镀膜</li>
<li><a href="/products/broadband-dielectric-mirrors/">宽带介质反射镜</a> — 透射光学元件配有BBAR镀膜选项</li>
<li>定制AR镀膜，覆盖193 nm至10.6 μm的任何波长范围</li>
<li>镀膜质量通过分光光度法验证，附合格证书</li>
</ul>

<h2>结论</h2>
<p>AR镀膜是光学系统设计中虽小但关键的部分。对于单波长激光应用，V涂层提供最低反射率和最高损伤阈值。对于宽带成像，多层BBAR镀膜在整个光谱范围内提供一致的性能。即使简单的MgF<sub>2</sub>镀膜也能将反射率从4%降至1.5%，在多元件系统中这是显著的改善。指定AR镀膜时，务必将镀膜带宽与光源光谱匹配，并验证激光应用的LIDT。恒鼎光可以帮助您为任何应用选择和指定合适的镀膜。</p>'''


# ============================================================
# Article 3: BK7 vs UV Fused Silica
# ============================================================
article3_en = '''<h2>Introduction</h2>
<p>BK7 and UV fused silica are the two most widely used optical glass materials in precision optics manufacturing. While both are excellent choices for many applications, they have fundamentally different optical, thermal, and mechanical properties that make each material better suited for specific use cases. Understanding these differences is essential for making cost-effective and performance-optimal material selections.</p>

<h2>Material Properties Comparison</h2>
<p>The table below summarizes the key optical and physical properties of BK7 and UV fused silica:</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">Property</th><th style="border:1px solid #e2e8f0;padding:8px;">BK7 (SCHOTT N-BK7)</th><th style="border:1px solid #e2e8f0;padding:8px;">UV Fused Silica</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Transmission Range</td><td style="border:1px solid #e2e8f0;padding:8px;">350 nm – 2.0 &mu;m</td><td style="border:1px solid #e2e8f0;padding:8px;">185 nm – 2.5 &mu;m</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Refractive Index (n<sub>d</sub>)</td><td style="border:1px solid #e2e8f0;padding:8px;">1.5168</td><td style="border:1px solid #e2e8f0;padding:8px;">1.4585</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Abbe Number (V<sub>d</sub>)</td><td style="border:1px solid #e2e8f0;padding:8px;">64.17</td><td style="border:1px solid #e2e8f0;padding:8px;">67.82</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Density (g/cm&sup3;)</td><td style="border:1px solid #e2e8f0;padding:8px;">2.51</td><td style="border:1px solid #e2e8f0;padding:8px;">2.20</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">CTE (10<sup>-6</sup>/&deg;C, 20–100&deg;C)</td><td style="border:1px solid #e2e8f0;padding:8px;">7.1</td><td style="border:1px solid #e2e8f0;padding:8px;">0.55</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Knoop Hardness</td><td style="border:1px solid #e2e8f0;padding:8px;">610</td><td style="border:1px solid #e2e8f0;padding:8px;">480</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">LIDT (1064 nm, 10 ns)</td><td style="border:1px solid #e2e8f0;padding:8px;">~10 J/cm&sup2;</td><td style="border:1px solid #e2e8f0;padding:8px;">~20 J/cm&sup2;</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Homogeneity (typical)</td><td style="border:1px solid #e2e8f0;padding:8px;">&plusmn;2 &times; 10<sup>-6</sup></td><td style="border:1px solid #e2e8f0;padding:8px;">&plusmn;1 &times; 10<sup>-6</sup></td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Relative Cost (same geometry)</td><td style="border:1px solid #e2e8f0;padding:8px;">1&times; (baseline)</td><td style="border:1px solid #e2e8f0;padding:8px;">2–4&times;</td></tr>
</table>

<h2>Transmission Characteristics</h2>

<h3>BK7 Transmission</h3>
<p>BK7 transmits well from about 350 nm in the near-UV through the visible and into the near-IR to approximately 2.0 &mu;m. Internal transmission exceeds 99.5% per 10 mm path length from 400 nm to 1.8 &mu;m. Below 350 nm, absorption increases rapidly due to the iron oxide content in BK7. BK7 is not suitable for excimer laser applications (193 nm ArF, 248 nm KrF) or deep-UV lithography.</p>

<h3>UV Fused Silica Transmission</h3>
<p>UV fused silica transmits from approximately 185 nm in the deep-UV through the visible and near-IR to about 2.5 &mu;m. The extended UV transmission comes from the amorphous SiO<sub>2</sub> structure without metallic impurities. This makes UV fused silica the standard material for UV laser optics, excimer laser applications, and UV spectroscopy. In the IR, fused silica has an OH absorption band near 2.7 &mu;m, so for IR applications beyond 2.2 &mu;m, IR-grade fused silica (low-OH) should be used instead.</p>

<h2>Thermal Properties</h2>
<p>The most dramatic difference between these materials is the coefficient of thermal expansion (CTE). BK7 has a CTE of 7.1 &times; 10<sup>-6</sup>/&deg;C, while UV fused silica has a CTE of only 0.55 &times; 10<sup>-6</sup>/&deg;C — roughly 13 times lower. This has profound implications:</p>
<ul>
<li><strong>Thermal lensing:</strong> In high-power laser applications, absorbed power causes local heating and refractive index change (dn/dT). Fused silica's low CTE means less thermal deformation of the optical surface, maintaining wavefront quality under high thermal load.</li>
<li><strong>Temperature stability:</strong> In environments with large temperature swings (outdoor optics, space applications), fused silica maintains its shape and optical performance far better than BK7.</li>
<li><strong>Thermal shock resistance:</strong> Fused silica can withstand rapid temperature changes without cracking, making it suitable for high-temperature processes and cryogenic applications.</li>
</ul>

<h2>Laser Damage Threshold</h2>
<p>Laser-induced damage threshold (LIDT) is a critical specification for high-power laser optics. UV fused silica consistently outperforms BK7 by a factor of approximately 2&times; at common laser wavelengths. This is due to fused silica's higher purity, lack of metallic impurities, and better UV absorption characteristics. For pulsed laser applications at 1064 nm (Nd:YAG), bulk damage thresholds are approximately 10 J/cm<sup>2</sup> for BK7 and 20 J/cm<sup>2</sup> for UV fused silica (10 ns pulse, single shot). The actual LIDT of a coated optic depends heavily on the coating quality and design.</p>

<h2>When to Choose BK7</h2>
<ul>
<li>Visible and near-IR imaging systems (400 nm – 1.8 &mu;m) where cost is a primary concern</li>
<li>Low-to-moderate power laser applications (CW or low-energy pulsed)</li>
<li>Large optics where the cost difference becomes substantial (diameters > 50 mm)</li>
<li>Applications not exposed to significant thermal loads or temperature extremes</li>
<li>Standard catalog optics where BK7 is the default substrate</li>
</ul>
<p>PhotonEdge's <a href="/products/bk7-plano-convex/">BK7 Plano-Convex Lenses</a> and <a href="/products/bk7-windows/">BK7 Optical Windows</a> offer excellent value for these applications.</p>

<h2>When to Choose UV Fused Silica</h2>
<ul>
<li>UV laser applications (excimer lasers at 193 nm, 248 nm, 355 nm frequency-doubled Nd:YAG)</li>
<li>High-power pulsed laser systems where LIDT is critical</li>
<li>Applications requiring thermal stability (space optics, outdoor systems, interferometry)</li>
<li>Any application below 350 nm wavelength</li>
<li>Fluorescence microscopy where UV excitation is used</li>
</ul>
<p>For these demanding applications, choose PhotonEdge's <a href="/products/uv-fused-silica-plano-convex/">UV Fused Silica Plano-Convex Lenses</a> and <a href="/products/uv-fused-silica-windows/">UV Fused Silica Optical Windows</a>.</p>

<h2>Cost Considerations</h2>
<p>BK7 is significantly less expensive than UV fused silica for equivalent geometries. The raw material cost difference is approximately 2–4&times;, and this ratio increases for larger apertures where UV fused silica blanks are harder to source in high homogeneity grades. For a typical 25 mm diameter, 5 mm thick plano-convex lens, a BK7 version costs roughly one-third to one-half of the UV fused silica equivalent. This cost difference means BK7 should always be the default choice unless your application specifically requires the UV transmission, thermal stability, or higher LIDT of fused silica.</p>

<h2>Conclusion</h2>
<p>BK7 and UV fused silica are both excellent optical materials, but they serve different application spaces. BK7 is the cost-effective workhorse for visible and near-IR applications with moderate power levels. UV fused silica is the premium choice for UV transmission, high-power lasers, and thermally demanding environments. By matching material selection to your specific wavelength, power, and environmental requirements, you can optimize both performance and cost. PhotonEdge offers precision optics in both materials with full coating options — contact us for guidance on your next project.</p>'''

article3_zh = '''<h2>引言</h2>
<p>BK7和紫外熔融石英是精密光学制造中最广泛使用的两种光学玻璃材料。虽然两者都是许多应用的优秀选择，但它们具有根本不同的光学、热学和机械特性，使每种材料更适合特定用途。了解这些差异对于做出具有成本效益和性能最优的材料选择至关重要。</p>

<h2>材料特性对比</h2>
<p>下表总结了BK7和紫外熔融石英的关键光学和物理特性：</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">特性</th><th style="border:1px solid #e2e8f0;padding:8px;">BK7（SCHOTT N-BK7）</th><th style="border:1px solid #e2e8f0;padding:8px;">紫外熔融石英</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">透过范围</td><td style="border:1px solid #e2e8f0;padding:8px;">350 nm – 2.0 μm</td><td style="border:1px solid #e2e8f0;padding:8px;">185 nm – 2.5 μm</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">折射率 (n<sub>d</sub>)</td><td style="border:1px solid #e2e8f0;padding:8px;">1.5168</td><td style="border:1px solid #e2e8f0;padding:8px;">1.4585</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">阿贝数 (V<sub>d</sub>)</td><td style="border:1px solid #e2e8f0;padding:8px;">64.17</td><td style="border:1px solid #e2e8f0;padding:8px;">67.82</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">密度 (g/cm³)</td><td style="border:1px solid #e2e8f0;padding:8px;">2.51</td><td style="border:1px solid #e2e8f0;padding:8px;">2.20</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">CTE (10⁻⁶/°C, 20–100°C)</td><td style="border:1px solid #e2e8f0;padding:8px;">7.1</td><td style="border:1px solid #e2e8f0;padding:8px;">0.55</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">努氏硬度</td><td style="border:1px solid #e2e8f0;padding:8px;">610</td><td style="border:1px solid #e2e8f0;padding:8px;">480</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">LIDT (1064 nm, 10 ns)</td><td style="border:1px solid #e2e8f0;padding:8px;">~10 J/cm²</td><td style="border:1px solid #e2e8f0;padding:8px;">~20 J/cm²</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">均匀性（典型值）</td><td style="border:1px solid #e2e8f0;padding:8px;">±2 × 10⁻⁶</td><td style="border:1px solid #e2e8f0;padding:8px;">±1 × 10⁻⁶</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">相对成本（相同几何）</td><td style="border:1px solid #e2e8f0;padding:8px;">1×（基准）</td><td style="border:1px solid #e2e8f0;padding:8px;">2–4×</td></tr>
</table>

<h2>透过特性</h2>

<h3>BK7透过率</h3>
<p>BK7从近紫外约350 nm透过可见光到近红外约2.0 μm具有良好的透过率。在400 nm至1.8 μm范围内，10 mm光程的内部透过率超过99.5%。在350 nm以下，由于BK7中的氧化铁含量，吸收迅速增加。BK7不适用于准分子激光应用（193 nm ArF、248 nm KrF）或深紫外光刻。</p>

<h3>紫外熔融石英透过率</h3>
<p>紫外熔融石英从深紫外约185 nm透过可见光和近红外到约2.5 μm。延展的紫外透过率来自不含金属杂质的非晶SiO<sub>2</sub>结构。这使紫外熔融石英成为紫外激光光学、准分子激光应用和紫外光谱的标准材料。在红外区域，熔融石英在2.7 μm附近有OH吸收带，因此对于2.2 μm以上的红外应用，应使用红外级熔融石英（低OH）。</p>

<h2>热学特性</h2>
<p>这两种材料最显著的差异是热膨胀系数（CTE）。BK7的CTE为7.1 × 10⁻⁶/°C，而紫外熔融石英仅为0.55 × 10⁻⁶/°C——低约13倍。这具有深远影响：</p>
<ul>
<li><strong>热透镜效应：</strong>在高功率激光应用中，吸收的功率引起局部加热和折射率变化（dn/dT）。熔融石英的低CTE意味着光学表面热变形更小，在高热负荷下保持波前质量。</li>
<li><strong>温度稳定性：</strong>在温度波动大的环境中（户外光学、太空应用），熔融石英比BK7更好地保持形状和光学性能。</li>
<li><strong>抗热冲击性：</strong>熔融石英能承受快速温度变化而不开裂，适用于高温工艺和低温应用。</li>
</ul>

<h2>激光损伤阈值</h2>
<p>激光损伤阈值（LIDT）是高功率激光光学的关键规格。紫外熔融石英在常见激光波长下始终优于BK7约2倍。这是因为熔融石英纯度更高、不含金属杂质且紫外吸收特性更好。对于1064 nm（Nd:YAG）脉冲激光应用，体损伤阈值BK7约10 J/cm²，紫外熔融石英约20 J/cm²（10 ns脉冲，单次发射）。镀膜光学的实际LIDT在很大程度上取决于镀膜质量和设计。</p>

<h2>何时选择BK7</h2>
<ul>
<li>可见光和近红外成像系统（400 nm – 1.8 μm），成本是主要考虑因素</li>
<li>低到中等功率激光应用（连续或低能量脉冲）</li>
<li>大口径光学，成本差异显著（直径 > 50 mm）</li>
<li>不受显著热负荷或温度极端影响的应用</li>
<li>BK7作为默认基材的标准目录光学元件</li>
</ul>
<p>恒鼎光的<a href="/products/bk7-plano-convex/">BK7平凸透镜</a>和<a href="/products/bk7-windows/">BK7光学窗口</a>为这些应用提供出色价值。</p>

<h2>何时选择紫外熔融石英</h2>
<ul>
<li>紫外激光应用（193 nm、248 nm准分子激光、355 nm三倍频Nd:YAG）</li>
<li>LIDT关键的高功率脉冲激光系统</li>
<li>需要热稳定性的应用（太空光学、户外系统、干涉测量）</li>
<li>350 nm波长以下的任何应用</li>
<li>使用紫外激发的荧光显微镜</li>
</ul>
<p>对于这些苛刻应用，选择恒鼎光的<a href="/products/uv-fused-silica-plano-convex/">紫外熔融石英平凸透镜</a>和<a href="/products/uv-fused-silica-windows/">紫外熔融石英光学窗口</a>。</p>

<h2>成本考量</h2>
<p>对于相同几何尺寸，BK7比紫外熔融石英便宜得多。原材料成本差异约2–4倍，对于大口径高均匀性级别的紫外熔融石英毛坯更难采购，该比例更大。对于典型的25 mm直径、5 mm厚平凸透镜，BK7版本的成本约为紫外熔融石英等效产品的三分之一到一半。这种成本差异意味着BK7应始终作为默认选择，除非您的应用特别需要熔融石英的紫外透过率、热稳定性或更高LIDT。</p>

<h2>结论</h2>
<p>BK7和紫外熔融石英都是优秀的光学材料，但服务于不同的应用领域。BK7是可见光和近红外中低功率应用的成本效益型主力材料。紫外熔融石英是紫外透过、高功率激光和热苛刻环境的优选材料。通过将材料选择与您的特定波长、功率和环境要求匹配，您可以同时优化性能和成本。恒鼎光提供两种材料的精密光学元件及完整镀膜选项——请联系我们获取项目指导。</p>'''


# ============================================================
# Article 4: 5 Key Specifications for Optical Windows
# ============================================================
article4_en = '''<h2>Introduction</h2>
<p>Optical windows are flat, parallel-sided optical components that allow light to pass through while protecting internal components or separating environments. Despite their apparent simplicity, selecting the right optical window requires careful evaluation of several specifications that directly affect system performance. Overlooking any one of these five key specifications can lead to wavefront distortion, transmission loss, or even component failure. This guide covers the five most critical parameters to check before purchasing optical windows.</p>

<h2>1. Surface Flatness</h2>
<p>Surface flatness measures how closely a window surface approximates a perfect plane. It is specified in fractions of a wavelength (&lambda;) at 633 nm (HeNe laser test wavelength). Flatness directly determines the wavefront distortion a window introduces into the optical path.</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">Flatness</th><th style="border:1px solid #e2e8f0;padding:8px;">Wavefront Distortion</th><th style="border:1px solid #e2e8f0;padding:8px;">Typical Application</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">&lambda;/2</td><td style="border:1px solid #e2e8f0;padding:8px;">~316 nm PV</td><td style="border:1px solid #e2e8f0;padding:8px;">General purpose, non-imaging</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">&lambda;/4</td><td style="border:1px solid #e2e8f0;padding:8px;">~158 nm PV</td><td style="border:1px solid #e2e8f0;padding:8px;">Standard imaging, moderate precision</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">&lambda;/10</td><td style="border:1px solid #e2e8f0;padding:8px;">~63 nm PV</td><td style="border:1px solid #e2e8f0;padding:8px;">Interferometry, laser cavities</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">&lambda;/20</td><td style="border:1px solid #e2e8f0;padding:8px;">~32 nm PV</td><td style="border:1px solid #e2e8f0;padding:8px;">Extreme precision, reference flats</td></tr>
</table>

<p>For imaging applications, a flatness of &lambda;/4 is typically sufficient. For interferometry or laser cavity windows, &lambda;/10 or better is recommended. Surface flatness is measured using a Fizeau interferometer and reported as peak-to-valley (PV) or root-mean-square (RMS) deviation from a reference plane.</p>

<h2>2. Parallelism (Wedge Angle)</h2>
<p>Parallelism measures the angular deviation between the two surfaces of a window. Non-parallel surfaces create a wedge that deviates the transmitted beam and can introduce ghost reflections. Parallelism is typically specified in arcminutes or arcseconds.</p>
<ul>
<li><strong>&lt;3 arcmin:</strong> Standard quality, acceptable for most imaging and illumination applications</li>
<li><strong>&lt;1 arcmin:</strong> Precision quality, recommended for laser applications and beam paths</li>
<li><strong>&lt;10 arcsec:</strong> Ultra-precision, required for interferometry and critical alignment applications</li>
</ul>
<p>A window with 1 arcmin of wedge deviates a collimated beam by approximately (n-1) &times; wedge &asymp; 0.517 &times; 1 arcmin &asymp; 31 arcsec for BK7. In multi-window systems, this deviation accumulates and can misalign the optical path.</p>

<h2>3. Material Transmission</h2>
<p>The window material must transmit efficiently at your operating wavelength. Transmission depends on both bulk absorption and surface reflections. Key material choices include:</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">Material</th><th style="border:1px solid #e2e8f0;padding:8px;">Transmission Range</th><th style="border:1px solid #e2e8f0;padding:8px;">Best Application</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/bk7-windows/">BK7</a></td><td style="border:1px solid #e2e8f0;padding:8px;">350 nm – 2.0 &mu;m</td><td style="border:1px solid #e2e8f0;padding:8px;">Visible/NIR, cost-effective</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/uv-fused-silica-windows/">UV Fused Silica</a></td><td style="border:1px solid #e2e8f0;padding:8px;">185 nm – 2.5 &mu;m</td><td style="border:1px solid #e2e8f0;padding:8px;">UV lasers, high power, thermal stability</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/sapphire-windows/">Sapphire</a></td><td style="border:1px solid #e2e8f0;padding:8px;">150 nm – 5.0 &mu;m</td><td style="border:1px solid #e2e8f0;padding:8px;">Harsh environments, high pressure, wide band</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">CaF2</td><td style="border:1px solid #e2e8f0;padding:8px;">130 nm – 8.0 &mu;m</td><td style="border:1px solid #e2e8f0;padding:8px;">Deep UV, mid-IR, low dispersion</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">ZnSe</td><td style="border:1px solid #e2e8f0;padding:8px;">600 nm – 18 &mu;m</td><td style="border:1px solid #e2e8f0;padding:8px;">CO2 laser (10.6 &mu;m), thermal imaging</td></tr>
</table>

<p>Always verify the internal transmission grade of the material. BK7 is available in fine annealed grade with homogeneity of &plusmn;2 &times; 10<sup>-6</sup>, while UV fused silica offers &plusmn;1 &times; 10<sup>-6</sup> homogeneity. For laser cavity windows, specify the highest homogeneity grade available.</p>

<h2>4. Clear Aperture</h2>
<p>The clear aperture defines the central area of the window that meets all specified tolerances (flatness, parallelism, surface quality). Edge effects from polishing mean the outer rim of a window typically does not meet the same quality as the center. The clear aperture is usually specified as a percentage of the physical diameter.</p>
<ul>
<li><strong>85% of diameter:</strong> Standard specification for most commercial optics</li>
<li><strong>90% of diameter:</strong> Precision specification, common for laser and imaging applications</li>
<li><strong>95% of diameter:</strong> Ultra-precision, required for large-field imaging where edge performance matters</li>
</ul>
<p>For a 25 mm diameter window with 85% clear aperture, the central 21.25 mm meets specification. When designing your system, ensure that the full beam fits within the clear aperture, not just the physical diameter.</p>

<h2>5. Surface Quality (Scratch-Dig)</h2>
<p>Surface quality is specified using the scratch-dig notation per MIL-PRF-13830B or ISO 10110. The scratch number approximates the maximum width of a scratch in tenths of a micron (e.g., 40-scratch &asymp; 4 &mu;m width). The dig number approximates the maximum diameter of a pit or dig in hundredths of a millimeter (e.g., 20-dig &asymp; 0.20 mm diameter).</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">Scratch-Dig</th><th style="border:1px solid #e2e8f0;padding:8px;">Quality Level</th><th style="border:1px solid #e2e8f0;padding:8px;">Typical Application</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">80-50</td><td style="border:1px solid #e2e8f0;padding:8px;">Commercial</td><td style="border:1px solid #e2e8f0;padding:8px;">Illumination, non-critical</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">60-40</td><td style="border:1px solid #e2e8f0;padding:8px;">Standard</td><td style="border:1px solid #e2e8f0;padding:8px;">General imaging</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">40-20</td><td style="border:1px solid #e2e8f0;padding:8px;">Precision</td><td style="border:1px solid #e2e8f0;padding:8px;">Laser applications, microscopy</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">20-10</td><td style="border:1px solid #e2e8f0;padding:8px;">High precision</td><td style="border:1px solid #e2e8f0;padding:8px;">High-power laser, interferometry</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">10-5</td><td style="border:1px solid #e2e8f0;padding:8px;">Ultra-precision</td><td style="border:1px solid #e2e8f0;padding:8px;">Laser cavity, reference standards</td></tr>
</table>

<p>Surface defects scatter light and reduce system contrast. In high-power laser systems, scratches and digs can act as nucleation sites for laser-induced damage, dramatically reducing LIDT. For laser applications, always specify 40-20 or better surface quality.</p>

<h2>PhotonEdge Optical Windows</h2>
<p>PhotonEdge manufactures precision optical windows with tight flatness and parallelism tolerances:</p>
<ul>
<li><a href="/products/bk7-windows/">BK7 Optical Windows</a> — &lambda;/4 to &lambda;/20 flatness, cost-effective for visible/NIR</li>
<li><a href="/products/uv-fused-silica-windows/">UV Fused Silica Optical Windows</a> — Superior UV transmission and thermal stability</li>
<li><a href="/products/sapphire-windows/">Sapphire Windows</a> — Extreme hardness and chemical resistance for harsh environments</li>
<li>All windows available with AR, BBAR, or custom coatings</li>
<li>Diameters from 5 mm to 200 mm, thicknesses from 1 mm to 30 mm</li>
</ul>

<h2>Conclusion</h2>
<p>When purchasing optical windows, do not simply select the cheapest option that matches your diameter. Evaluate all five key specifications — surface flatness, parallelism, material transmission, clear aperture, and surface quality — against your application requirements. For imaging systems, &lambda;/4 flatness and &lt;3 arcmin parallelism are typically sufficient. For laser and interferometric applications, specify &lambda;/10 or better flatness, &lt;1 arcmin parallelism, and 40-20 or better surface quality. PhotonEdge offers optical windows in BK7, UV fused silica, and sapphire with full specification options and coating capabilities.</p>'''

article4_zh = '''<h2>引言</h2>
<p>光学窗口是平坦的平行面光学元件，允许光通过的同时保护内部元件或隔离环境。尽管看似简单，选择合适的光学窗口需要仔细评估几个直接影响系统性能的规格。忽视这五个关键规格中的任何一个都可能导致波前畸变、透过损失甚至元件失效。本指南涵盖购买光学窗口前需要检查的五个最关键参数。</p>

<h2>1. 表面平整度</h2>
<p>表面平整度衡量窗口表面与理想平面的接近程度。以633 nm（HeNe激光测试波长）处波长的分数（&lambda;）指定。平整度直接决定窗口在光路中引入的波前畸变。</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">平整度</th><th style="border:1px solid #e2e8f0;padding:8px;">波前畸变</th><th style="border:1px solid #e2e8f0;padding:8px;">典型应用</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">&lambda;/2</td><td style="border:1px solid #e2e8f0;padding:8px;">~316 nm PV</td><td style="border:1px solid #e2e8f0;padding:8px;">通用、非成像</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">&lambda;/4</td><td style="border:1px solid #e2e8f0;padding:8px;">~158 nm PV</td><td style="border:1px solid #e2e8f0;padding:8px;">标准成像、中等精度</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">&lambda;/10</td><td style="border:1px solid #e2e8f0;padding:8px;">~63 nm PV</td><td style="border:1px solid #e2e8f0;padding:8px;">干涉测量、激光谐振腔</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">&lambda;/20</td><td style="border:1px solid #e2e8f0;padding:8px;">~32 nm PV</td><td style="border:1px solid #e2e8f0;padding:8px;">超高精度、参考平面</td></tr>
</table>

<p>对于成像应用，&lambda;/4平整度通常足够。对于干涉测量或激光谐振腔窗口，推荐&lambda;/10或更好。表面平整度使用Fizeau干涉仪测量，以峰谷值（PV）或均方根值（RMS）偏差报告。</p>

<h2>2. 平行度（楔角）</h2>
<p>平行度衡量窗口两表面之间的角度偏差。不平行的表面产生楔角，偏折透射光束并可能引入鬼反射。平行度通常以角分或角秒指定。</p>
<ul>
<li><strong>&lt;3角分：</strong>标准质量，适用于大多数成像和照明应用</li>
<li><strong>&lt;1角分：</strong>精密质量，推荐用于激光应用和光路</li>
<li><strong>&lt;10角秒：</strong>超精密，干涉测量和关键对准应用所需</li>
</ul>
<p>具有1角分楔角的窗口将准直光束偏折约(n-1) × 楔角 ≈ 0.517 × 1角分 ≈ 31角秒（BK7）。在多窗口系统中，此偏折累积，可能使光路错位。</p>

<h2>3. 材料透过率</h2>
<p>窗口材料必须在您的工作波长处高效透过。透过率取决于体吸收和表面反射。关键材料选择包括：</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">材料</th><th style="border:1px solid #e2e8f0;padding:8px;">透过范围</th><th style="border:1px solid #e2e8f0;padding:8px;">最佳应用</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/bk7-windows/">BK7</a></td><td style="border:1px solid #e2e8f0;padding:8px;">350 nm – 2.0 μm</td><td style="border:1px solid #e2e8f0;padding:8px;">可见光/近红外，成本效益</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/uv-fused-silica-windows/">紫外熔融石英</a></td><td style="border:1px solid #e2e8f0;padding:8px;">185 nm – 2.5 μm</td><td style="border:1px solid #e2e8f0;padding:8px;">紫外激光、高功率、热稳定</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;"><a href="/products/sapphire-windows/">蓝宝石</a></td><td style="border:1px solid #e2e8f0;padding:8px;">150 nm – 5.0 μm</td><td style="border:1px solid #e2e8f0;padding:8px;">恶劣环境、高压、宽波段</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">CaF2</td><td style="border:1px solid #e2e8f0;padding:8px;">130 nm – 8.0 μm</td><td style="border:1px solid #e2e8f0;padding:8px;">深紫外、中红外、低色散</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">ZnSe</td><td style="border:1px solid #e2e8f0;padding:8px;">600 nm – 18 μm</td><td style="border:1px solid #e2e8f0;padding:8px;">CO2激光（10.6 μm）、热成像</td></tr>
</table>

<p>始终验证材料的内部透过率等级。BK7提供精细退火级，均匀性±2 × 10⁻⁶；紫外熔融石英提供±1 × 10⁻⁶均匀性。对于激光谐振腔窗口，指定最高可用均匀性等级。</p>

<h2>4. 通光孔径</h2>
<p>通光孔径定义窗口满足所有规定公差（平整度、平行度、表面质量）的中心区域。抛光的边缘效应意味着窗口外缘通常达不到与中心相同的质量。通光孔径通常以物理直径的百分比指定。</p>
<ul>
<li><strong>直径的85%：</strong>大多数商业光学的标准规格</li>
<li><strong>直径的90%：</strong>精密规格，激光和成像应用常用</li>
<li><strong>直径的95%：</strong>超精密，大视场成像所需，边缘性能重要</li>
</ul>
<p>对于25 mm直径、85%通光孔径的窗口，中心21.25 mm满足规格。设计系统时，确保整个光束在通光孔径内，而不仅是物理直径。</p>

<h2>5. 表面质量（划痕-麻点）</h2>
<p>表面质量使用MIL-PRF-13830B或ISO 10110的划痕-麻点标记指定。划痕数字近似最大划痕宽度（微米的十分之一，如40-划痕 ≈ 4 μm宽）。麻点数字近似最大麻点直径（毫米的百分之一，如20-麻点 ≈ 0.20 mm直径）。</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">划痕-麻点</th><th style="border:1px solid #e2e8f0;padding:8px;">质量等级</th><th style="border:1px solid #e2e8f0;padding:8px;">典型应用</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">80-50</td><td style="border:1px solid #e2e8f0;padding:8px;">商业级</td><td style="border:1px solid #e2e8f0;padding:8px;">照明、非关键</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">60-40</td><td style="border:1px solid #e2e8f0;padding:8px;">标准级</td><td style="border:1px solid #e2e8f0;padding:8px;">通用成像</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">40-20</td><td style="border:1px solid #e2e8f0;padding:8px;">精密级</td><td style="border:1px solid #e2e8f0;padding:8px;">激光应用、显微镜</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">20-10</td><td style="border:1px solid #e2e8f0;padding:8px;">高精密级</td><td style="border:1px solid #e2e8f0;padding:8px;">高功率激光、干涉测量</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">10-5</td><td style="border:1px solid #e2e8f0;padding:8px;">超精密级</td><td style="border:1px solid #e2e8f0;padding:8px;">激光谐振腔、参考标准</td></tr>
</table>

<p>表面缺陷散射光并降低系统对比度。在高功率激光系统中，划痕和麻点可作为激光诱发损伤的成核点，大幅降低LIDT。对于激光应用，始终指定40-20或更好的表面质量。</p>

<h2>恒鼎光光学窗口</h2>
<p>恒鼎光制造具有严格平整度和平行度公差的精密光学窗口：</p>
<ul>
<li><a href="/products/bk7-windows/">BK7光学窗口</a> — &lambda;/4至&lambda;/20平整度，可见光/近红外性价比高</li>
<li><a href="/products/uv-fused-silica-windows/">紫外熔融石英光学窗口</a> — 卓越的紫外透过率和热稳定性</li>
<li><a href="/products/sapphire-windows/">蓝宝石窗口</a> — 极高硬度和耐化学性，适用于恶劣环境</li>
<li>所有窗口可配备AR、BBAR或定制镀膜</li>
<li>直径从5 mm到200 mm，厚度从1 mm到30 mm</li>
</ul>

<h2>结论</h2>
<p>购买光学窗口时，不要简单选择匹配直径的最低价选项。根据应用要求评估所有五个关键规格——表面平整度、平行度、材料透过率、通光孔径和表面质量。对于成像系统，&lambda;/4平整度和&lt;3角分平行度通常足够。对于激光和干涉测量应用，指定&lambda;/10或更好的平整度、&lt;1角分平行度以及40-20或更好的表面质量。恒鼎光提供BK7、紫外熔融石英和蓝宝石材质的光学窗口，具有完整规格选项和镀膜能力。</p>'''


# ============================================================
# Article 5: Optical Prism Types and Applications
# ============================================================
article5_en = '''<h2>Introduction</h2>
<p>Optical prisms are transparent solid geometric elements with flat polished faces that redirect, deviate, or disperse light through refraction and total internal reflection (TIR). Unlike mirrors, prisms can perform complex beam manipulation without reflective coatings, making them robust and alignment-stable components in optical systems. This guide covers the four most common prism types, their working principles, and practical applications.</p>

<h2>Right-Angle Prisms</h2>
<p>The right-angle prism is the most fundamental and widely used prism type. It has a 90&deg; angle between two perpendicular faces and 45&deg; angles to the hypotenuse. When light enters one of the perpendicular faces and strikes the hypotenuse at 45&deg; (beyond the critical angle for typical glass), it undergoes total internal reflection and exits through the other perpendicular face, deviating the beam by exactly 90&deg;.</p>

<h3>Working Principle</h3>
<p>For BK7 (n = 1.517), the critical angle for TIR is arcsin(1/1.517) &asymp; 41.2&deg;. Since the 45&deg; incidence angle at the hypotenuse exceeds the critical angle, TIR occurs with 100% reflectivity — no metallic or dielectric coating is needed. This makes right-angle prisms more efficient and durable than 90&deg; turning mirrors in many applications.</p>

<h3>Applications</h3>
<ul>
<li>Beam deviation by 90&deg; in periscope and viewfinder assemblies</li>
<li>Image inversion and reversion in optical viewfinders</li>
<li>Porro prism pairs for image erection in binoculars</li>
<li>Compact beam folding in laser cavities and optical delay lines</li>
</ul>

<p>When used in reverse (light entering the hypotenuse), a right-angle prism can split a beam into two outputs — functioning as a beamsplitter. PhotonEdge offers <a href="/products/bk7-right-angle-prisms/">BK7 Right-Angle Prisms</a> in sizes from 5 mm to 50 mm with &lambda;/4 surface flatness and 40-20 surface quality.</p>

<h2>Penta Prisms</h2>
<p>A penta prism has two reflecting surfaces at 45&deg; to each other, which deviates the beam by exactly 90&deg; regardless of the incidence angle (within the acceptance range). This angle-constant property is the defining characteristic of penta prisms and distinguishes them from right-angle prisms.</p>

<h3>Working Principle</h3>
<p>The two internal reflections are at 22.5&deg; each to the prism faces. Because the two reflecting surfaces are fixed at 45&deg;, the deviation is always 2 &times; 45&deg; = 90&deg; by geometry, independent of the input beam angle. Unlike TIR-based prisms, the 22.5&deg; incidence angle is below the critical angle, so the reflecting surfaces must be coated with a metallic or dielectric reflective coating.</p>

<h3>Applications</h3>
<ul>
<li><strong>SLR camera viewfinders:</strong> The angle-constant deviation ensures the viewfinder image does not shift when the camera is tilted slightly</li>
<li><strong>Optical tooling and alignment:</strong> Used in autocollimators and alignment telescopes where precise 90&deg; deviation must be maintained regardless of small angular errors</li>
<li><strong>Laser beam steering:</strong> When a beam must be turned exactly 90&deg; even if the input angle varies</li>
</ul>

<p>PhotonEdge manufactures <a href="/products/penta-prisms/">Penta Prisms</a> with precise 90&deg; deviation tolerance (&plusmn;5 arcsec or better) and protected Al or dielectric coatings on the reflecting surfaces.</p>

<h2>Dove Prisms</h2>
<p>A dove prism is a truncated right-angle prism with an apex angle typically of 45&deg;. Light enters and exits at an angle, traveling through the prism along the length of the base. The key property of a dove prism is that it rotates the image by twice the rotation angle of the prism about its longitudinal axis.</p>

<h3>Working Principle</h3>
<p>When a dove prism is rotated by angle &theta; about its long axis (the axis parallel to the base), the transmitted image rotates by 2&theta;. This 2&times; image rotation property makes dove prisms ideal as image rotators in optical systems. The beam undergoes one TIR at the base, so the prism inverts the image in one axis even at zero rotation.</p>

<h3>Applications</h3>
<ul>
<li><strong>Image rotation:</strong> Compensating for image rotation in scanning systems (e.g., aerial reconnaissance cameras where the aircraft heading changes)</li>
<li><strong>Interferometry:</strong> Rotating the fringe pattern in Twyman-Green and Fizeau interferometers for alignment</li>
<li><strong>Polarization optics:</strong> In conjunction with waveplates, dove prisms can create complex polarization transformations</li>
</ul>

<p>Note that dove prisms introduce significant chromatic dispersion because the beam enters and exits at non-normal angles. They are best used with monochromatic or narrowband sources. PhotonEdge offers <a href="/products/dove-prisms/">Dove Prisms</a> optimized for visible and NIR wavelengths.</p>

<h2>Corner Cube (Retroreflector) Prisms</h2>
<p>A corner cube prism (also called a retroreflector or cat's eye retroreflector) has three mutually perpendicular reflecting surfaces. Any beam entering the prism is reflected off all three surfaces and exits parallel to the input beam, traveling in the opposite direction — regardless of the incidence angle (within the acceptance cone).</p>

<h3>Working Principle</h3>
<p>Each of the three TIR reflections reverses one component of the beam direction. After three reflections, all components are reversed, and the beam exits anti-parallel to the input. The retroreflected beam is laterally displaced but always parallel to the input, making corner cubes self-aligning retroreflectors.</p>

<h3>Applications</h3>
<ul>
<li><strong>Laser ranging:</strong> Corner cubes are placed on satellites (e.g., lunar laser ranging retroreflectors on the Moon) and spacecraft for precise distance measurement by time-of-flight</li>
<li><strong>Optical interferometry:</strong> Used in Michelson interferometers where self-alignment eliminates mirror tilt errors</li>
<li><strong>Autocollimators:</strong> Corner cube retroreflectors return the beam to the source regardless of tilt, used for alignment verification</li>
<li><strong>Road reflectors:</strong> Mass-produced plastic corner cubes in road reflectors and safety markers</li>
</ul>

<p>PhotonEdge's <a href="/products/corner-cube-prisms/">Corner Cube Prisms</a> are available in BK7 and UV fused silica with angular deviation less than 3 arcsec, suitable for precision metrology and laser ranging applications.</p>

<h2>Prism Selection Considerations</h2>
<p>When selecting a prism for your application, consider these factors:</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">Factor</th><th style="border:1px solid #e2e8f0;padding:8px;">Consideration</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Material</td><td style="border:1px solid #e2e8f0;padding:8px;">BK7 for visible/NIR; UV fused silica for UV/high-power; CaF2 for IR</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Surface flatness</td><td style="border:1px solid #e2e8f0;padding:8px;">&lambda;/4 for general use; &lambda;/10 for interferometry and metrology</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Angular tolerance</td><td style="border:1px solid #e2e8f0;padding:8px;">Tight angles (&plusmn;3 arcmin or better) are critical for penta and corner cube prisms</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Coating</td><td style="border:1px solid #e2e8f0;padding:8px;">TIR surfaces need no coating; other surfaces may need AR or reflective coatings</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Beam aperture</td><td style="border:1px solid #e2e8f0;padding:8px;">Ensure prism aperture accommodates full beam diameter with margin</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">Dispersion</td><td style="border:1px solid #e2e8f0;padding:8px;">Dove and wedge prisms introduce dispersion; limit to narrowband sources</td></tr>
</table>

<h2>Conclusion</h2>
<p>Optical prisms are versatile components that perform beam deviation, image rotation, and retroreflection through TIR and refraction, often without requiring reflective coatings. Right-angle prisms provide efficient 90&deg; beam turning via TIR. Penta prisms deliver angle-constant 90&deg; deviation for alignment-critical applications. Dove prisms rotate images at twice the prism rotation angle. Corner cube prisms retroreflect beams regardless of incidence angle, enabling self-aligning interferometry and laser ranging. By understanding each prism type's unique properties, you can select the right component for your optical system. PhotonEdge offers all four prism types in multiple materials with precision angular and surface specifications.</p>'''

article5_zh = '''<h2>引言</h2>
<p>光学棱镜是具有平坦抛光面的透明固体几何元件，通过折射和全内反射（TIR）重定向、偏折或色散光。与反射镜不同，棱镜无需反射镀膜即可执行复杂的光束操作，使其成为光学系统中稳健且对准稳定的元件。本指南涵盖四种最常用的棱镜类型、工作原理和实际应用。</p>

<h2>直角棱镜</h2>
<p>直角棱镜是最基本且最广泛使用的棱镜类型。两个垂直面之间有90&deg;角，与斜面成45&deg;角。当光从垂直面之一入射并以45&deg;角照射斜面时（超过典型玻璃的临界角），发生全内反射，光从另一垂直面出射，光束精确偏折90&deg;。</p>

<h3>工作原理</h3>
<p>对于BK7（n = 1.517），TIR的临界角为arcsin(1/1.517) ≈ 41.2&deg;。由于斜面上的45&deg;入射角超过临界角，发生100%反射率的TIR——不需要金属或介质镀膜。这使得直角棱镜在许多应用中比90&deg;转折反射镜更高效、更耐用。</p>

<h3>应用</h3>
<ul>
<li>潜望镜和取景器组件中的90&deg;光束偏折</li>
<li>光学取景器中的图像倒转和翻转</li>
<li>双筒望远镜中用于图像正立的Porro棱镜对</li>
<li>激光谐振腔和光学延迟线中的紧凑光束折叠</li>
</ul>

<p>反向使用时（光从斜面入射），直角棱镜可将光束分成两个输出——起到分光片的作用。恒鼎光提供<a href="/products/bk7-right-angle-prisms/">BK7直角棱镜</a>，尺寸从5 mm到50 mm，表面平整度&lambda;/4，表面质量40-20。</p>

<h2>五棱镜</h2>
<p>五棱镜有两个成45&deg;角的反射面，无论入射角如何（在接收范围内），光束都精确偏折90&deg;。这种恒角特性是五棱镜的定义特征，也是与直角棱镜的区别。</p>

<h3>工作原理</h3>
<p>两次内部反射各以22.5&deg;角入射到棱镜面。由于两个反射面固定成45&deg;，偏折始终为2 × 45&deg; = 90&deg;（几何决定），与输入光束角度无关。与基于TIR的棱镜不同，22.5&deg;入射角低于临界角，因此反射面必须镀金属或介质反射膜。</p>

<h3>应用</h3>
<ul>
<li><strong>单反相机取景器：</strong>恒角偏折确保相机轻微倾斜时取景器图像不移位</li>
<li><strong>光学工具和对准：</strong>用于自准直仪和对准望远镜，即使存在小角度误差也能保持精确90&deg;偏折</li>
<li><strong>激光光束导向：</strong>当输入角度变化时仍需精确90&deg;转折的光束</li>
</ul>

<p>恒鼎光制造<a href="/products/penta-prisms/">五棱镜</a>，90&deg;偏折公差精密（±5角秒或更好），反射面镀保护铝或介质膜。</p>

<h2>道威棱镜</h2>
<p>道威棱镜是截顶直角棱镜，顶角通常为45&deg;。光以一定角度入射和出射，沿底面长度穿过棱镜。道威棱镜的关键特性是图像旋转角度为棱镜绕纵轴旋转角度的两倍。</p>

<h3>工作原理</h3>
<p>当道威棱镜绕长轴（平行于底面的轴）旋转角度&theta;时，透射图像旋转2&theta;。这种2倍图像旋转特性使道威棱镜成为光学系统中的理想图像旋转器。光束在底面发生一次TIR，因此即使在零旋转时棱镜也在一个轴上翻转图像。</p>

<h3>应用</h3>
<ul>
<li><strong>图像旋转：</strong>补偿扫描系统中的图像旋转（如航向变化的航空侦察相机）</li>
<li><strong>干涉测量：</strong>在Twyman-Green和Fizeau干涉仪中旋转条纹图样以进行对准</li>
<li><strong>偏振光学：</strong>与波片配合使用，道威棱镜可创建复杂的偏振变换</li>
</ul>

<p>注意，道威棱镜由于光束以非垂直角度入射和出射而引入显著色散，最适合单色或窄带光源使用。恒鼎光提供优化用于可见光和近红外波长的<a href="/products/dove-prisms/">道威棱镜</a>。</p>

<h2>角锥棱镜（逆反射器）</h2>
<p>角锥棱镜（也称逆反射器或猫眼逆反射器）有三个互相垂直的反射面。任何进入棱镜的光束经过三个面反射后，以平行于输入光束的方向出射——与入射角无关（在接收锥内）。</p>

<h3>工作原理</h3>
<p>三次TIR反射各反转光束方向的一个分量。三次反射后，所有分量反转，光束以反平行于输入的方向出射。逆反射光束有横向位移但始终平行于输入，使角锥棱镜成为自对准逆反射器。</p>

<h3>应用</h3>
<ul>
<li><strong>激光测距：</strong>角锥棱镜放置在卫星（如月球上的激光测距逆反射器）和航天器上，用于飞行时间精确距离测量</li>
<li><strong>光学干涉测量：</strong>用于Michelson干涉仪，自对准消除了反射镜倾斜误差</li>
<li><strong>自准直仪：</strong>角锥逆反射器无论倾斜如何都将光束返回光源，用于对准验证</li>
<li><strong>道路反光标志：</strong>大量生产的塑料角锥棱镜用于道路反光标志和安全标记</li>
</ul>

<p>恒鼎光的<a href="/products/corner-cube-prisms/">角锥棱镜</a>有BK7和紫外熔融石英可选，角度偏差小于3角秒，适用于精密计量和激光测距应用。</p>

<h2>棱镜选型考虑</h2>
<p>为应用选择棱镜时，考虑以下因素：</p>

<table style="width:100%;border-collapse:collapse;">
<tr style="background:#f1f5f9;"><th style="border:1px solid #e2e8f0;padding:8px;">因素</th><th style="border:1px solid #e2e8f0;padding:8px;">考虑要点</th></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">材料</td><td style="border:1px solid #e2e8f0;padding:8px;">可见光/近红外用BK7；紫外/高功率用紫外熔融石英；红外用CaF2</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">表面平整度</td><td style="border:1px solid #e2e8f0;padding:8px;">通用&lambda;/4；干涉测量和计量用&lambda;/10</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">角度公差</td><td style="border:1px solid #e2e8f0;padding:8px;">紧公差（±3角分或更好）对五棱镜和角锥棱镜至关重要</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">镀膜</td><td style="border:1px solid #e2e8f0;padding:8px;">TIR面无需镀膜；其他面可能需要AR或反射镀膜</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">光束孔径</td><td style="border:1px solid #e2e8f0;padding:8px;">确保棱镜孔径容纳全光束直径并留余量</td></tr>
<tr><td style="border:1px solid #e2e8f0;padding:8px;">色散</td><td style="border:1px solid #e2e8f0;padding:8px;">道威和楔形棱镜引入色散；限于窄带光源</td></tr>
</table>

<h2>结论</h2>
<p>光学棱镜是通过TIR和折射执行光束偏折、图像旋转和逆反射的通用元件，通常无需反射镀膜。直角棱镜通过TIR提供高效的90&deg;光束转折。五棱镜为对准关键应用提供恒角90&deg;偏折。道威棱镜以棱镜旋转角度的两倍旋转图像。角锥棱镜无论入射角如何都逆反射光束，实现自对准干涉测量和激光测距。通过了解每种棱镜类型的独特属性，您可以为光学系统选择合适的元件。恒鼎光提供四种棱镜类型，多种材料可选，具有精密角度和表面规格。</p>'''


# ============================================================
# Now update blog-data.js and HTML pages
# ============================================================

articles = [
    {"slug": "choose-right-optical-lens", "content": article1_en, "contentZh": article1_zh},
    {"slug": "anti-reflection-coatings-guide", "content": article2_en, "contentZh": article2_zh},
    {"slug": "bk7-vs-uv-fused-silica", "content": article3_en, "contentZh": article3_zh},
    {"slug": "optical-windows-buying-guide", "content": article4_en, "contentZh": article4_zh},
    {"slug": "optical-prism-types-applications", "content": article5_en, "contentZh": article5_zh},
]

# Build a lookup by slug
articles_by_slug = {a["slug"]: a for a in articles}

# === Task 2: Update blog-data.js ===
print("=== Updating blog-data.js ===")

blog_data_path = os.path.join(BASE_DIR, "js", "blog-data.js")

with open(blog_data_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the JSON array from the JS file
# Pattern: var BLOG_POSTS = [...] ;
match = re.search(r'var BLOG_POSTS\s*=\s*(\[[\s\S]*?\]);\s*$', content)
if not match:
    raise ValueError("Could not find BLOG_POSTS array in blog-data.js")

json_str = match.group(1)
posts = json.loads(json_str)

# Update first 5 posts with content and contentZh
for i in range(5):
    slug = posts[i]["slug"]
    if slug in articles_by_slug:
        posts[i]["content"] = articles_by_slug[slug]["content"]
        posts[i]["contentZh"] = articles_by_slug[slug]["contentZh"]
        print(f"  Added content for post {i+1}: {slug}")
    else:
        print(f"  WARNING: No article content for slug: {slug}")

# Re-serialize with proper formatting
# We need to write it back as JS: var BLOG_POSTS = [...];
# Use json.dumps with ensure_ascii=False to preserve Chinese characters
json_output = json.dumps(posts, indent=2, ensure_ascii=False)

# Escape any issues - the JSON should be valid JS since we use double quotes
new_content = "// PhotonEdge Blog Posts Data - Updated with Chinese translations and full content\n\nvar BLOG_POSTS = " + json_output + ";\n"

with open(blog_data_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("  blog-data.js updated successfully")


# === Task 3: Update HTML pages ===
print("\n=== Updating HTML pages ===")

# Language switching script to add
lang_switch_script = '''<script>
(function() {
    var enDiv = document.getElementById('articleContentEn');
    var zhDiv = document.getElementById('articleContentZh');
    if (!enDiv || !zhDiv) return;
    // Check current language
    if (typeof getCurrentLanguage === 'function' && getCurrentLanguage() === 'zh') {
        enDiv.style.display = 'none';
        zhDiv.style.display = 'block';
    }
    // Listen for language switch
    var origSetLang = (typeof setLanguage === 'function') ? setLanguage : null;
    if (origSetLang) {
        window.setLanguage = function(lang) {
            origSetLang(lang);
            if (lang === 'zh') {
                enDiv.style.display = 'none';
                zhDiv.style.display = 'block';
            } else {
                enDiv.style.display = 'block';
                zhDiv.style.display = 'none';
            }
        };
    }
})();
</script>'''

for article in articles:
    slug = article["slug"]
    html_path = os.path.join(BASE_DIR, "blog", slug, "index.html")
    
    print(f"  Processing: blog/{slug}/index.html")
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Find the article-body div and replace its content
    # Pattern: <div class="article-body" id="articleBody">...content...</div>
    # We need to find the opening tag and the matching closing div
    
    # Strategy: Find the article-body div, replace everything between opening and closing
    body_start_pattern = r'<div class="article-body" id="articleBody">'
    body_start_match = re.search(body_start_pattern, html_content)
    
    if not body_start_match:
        print(f"    WARNING: Could not find article-body div in {slug}")
        continue
    
    start_pos = body_start_match.end()
    
    # Find the closing </div> that matches the article-body opening
    # Count nesting level
    depth = 1
    pos = start_pos
    while depth > 0 and pos < len(html_content):
        next_open = html_content.find('<div', pos)
        next_close = html_content.find('</div>', pos)
        
        if next_close == -1:
            print(f"    WARNING: Could not find closing div in {slug}")
            break
        
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                end_pos = next_close
            pos = next_close + 6
    
    if depth != 0:
        print(f"    WARNING: Unmatched divs in {slug}")
        continue
    
    # Build new body content
    new_body_content = '\n    <div id="articleContentEn">\n        ' + article["content"] + '\n    </div>\n    <div id="articleContentZh" style="display:none;">\n        ' + article["contentZh"] + '\n    </div>\n'
    
    # Replace the body content
    new_html = html_content[:start_pos] + new_body_content + html_content[end_pos:]
    
    # Now add the language switching script before </body>
    # But after <script src="/js/translations.js"></script>
    # Check if it already exists
    if 'articleContentEn' in new_html and 'id="articleContentZh"' in new_html:
        # Add the language switch script before </body>
        # First remove any existing article lang switch that might conflict
        # Find the position of </body>
        body_end_pos = new_html.rfind('</body>')
        if body_end_pos == -1:
            print(f"    WARNING: Could not find </body> in {slug}")
            continue
        
        # Insert the language switch script before </body>
        new_html = new_html[:body_end_pos] + lang_switch_script + '\n' + new_html[body_end_pos:]
    
    # Also update the existing article language switching script
    # The existing script uses data-en-content/data-zh-content attributes on the <p> tag
    # We need to update or remove that script since we now use divs
    # Find the existing blog article language switching script block
    old_script_pattern = r'<script>\s*// Blog article language switching[\s\S]*?window\.setLanguage = wrappedSetLanguage;\s*\}\s*</script>'
    old_script_match = re.search(old_script_pattern, new_html)
    
    if old_script_match:
        # Replace with a simplified version that works with our new structure
        simplified_script = '''<script>
// Blog article language switching (enhanced for full content)
document.addEventListener('DOMContentLoaded', function() {
    var lang = getCurrentLanguage();
    updateArticleMetaLang(lang);
});

function updateArticleMetaLang(lang) {
    var title = document.getElementById('articleTitle');
    var category = document.getElementById('articleCategory');
    var readTime = document.getElementById('articleReadTime');
    
    if (lang === 'zh') {
        if (title && title.getAttribute('data-zh-title')) title.textContent = title.getAttribute('data-zh-title');
        if (category && category.getAttribute('data-zh-category')) category.textContent = category.getAttribute('data-zh-category');
        if (readTime && readTime.getAttribute('data-zh-time')) readTime.textContent = readTime.getAttribute('data-zh-time');
    } else {
        if (title && title.getAttribute('data-en-title')) title.textContent = title.getAttribute('data-en-title');
        if (category && category.getAttribute('data-en-category')) category.textContent = category.getAttribute('data-en-category');
        if (readTime && readTime.getAttribute('data-en-time')) readTime.textContent = readTime.getAttribute('data-en-time');
    }
}
</script>'''
        new_html = new_html[:old_script_match.start()] + simplified_script + new_html[old_script_match.end():]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    file_size = os.path.getsize(html_path)
    print(f"    Updated: {slug} (file size: {file_size} bytes)")

print("\n=== Verification ===")

# Verify blog-data.js
with open(blog_data_path, 'r', encoding='utf-8') as f:
    verify_content = f.read()

verify_match = re.search(r'var BLOG_POSTS\s*=\s*(\[[\s\S]*?\]);\s*$', verify_content)
verify_posts = json.loads(verify_match.group(1))

for i in range(5):
    has_content = 'content' in verify_posts[i] and len(verify_posts[i]['content']) > 100
    has_content_zh = 'contentZh' in verify_posts[i] and len(verify_posts[i]['contentZh']) > 100
    print(f"  Post {i+1} ({verify_posts[i]['slug']}): content={'YES' if has_content else 'NO'}, contentZh={'YES' if has_content_zh else 'NO'}")

# Verify HTML pages
for article in articles:
    slug = article["slug"]
    html_path = os.path.join(BASE_DIR, "blog", slug, "index.html")
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    has_en_div = 'id="articleContentEn"' in html
    has_zh_div = 'id="articleContentZh"' in html
    has_lang_script = 'articleContentEn' in html and 'articleContentZh' in html and 'setLanguage' in html
    file_size = os.path.getsize(html_path)
    
    print(f"  HTML {slug}: enDiv={'YES' if has_en_div else 'NO'}, zhDiv={'YES' if has_zh_div else 'NO'}, langScript={'YES' if has_lang_script else 'NO'}, size={file_size}")

print("\n=== All done! ===")
