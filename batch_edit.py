import re

# Material data
thermal_data = {
    'bk7': {
        'cte': '7.1 × 10⁻⁶ /K',
        'conductivity': '1.13 W/m·K',
        'dndt': '3 × 10⁻⁶ /K',
        'maxtemp': '~450°C (annealing point 557°C)',
        'note': 'BK7 has relatively low thermal conductivity and moderate thermal expansion. Avoid rapid temperature changes to prevent thermal shock cracking.'
    },
    'uv-fused-silica': {
        'cte': '0.55 × 10⁻⁶ /K',
        'conductivity': '1.38 W/m·K',
        'dndt': '12.8 × 10⁻⁶ /K at 633 nm',
        'maxtemp': '~1000°C (strain point 1070°C)',
        'note': 'UV fused silica has the lowest thermal expansion among common optical materials, making it ideal for precision optics in varying thermal environments.'
    },
    'caf2': {
        'cte': '18.9 × 10⁻⁶ /K',
        'conductivity': '9.71 W/m·K',
        'dndt': '-10.4 × 10⁻⁶ /K at 633 nm',
        'maxtemp': '~600°C',
        'note': 'CaF₂ has a negative dn/dT, meaning its refractive index decreases with temperature. High thermal conductivity helps dissipate heat in laser applications.'
    },
    'sapphire': {
        'cte': '5.0 × 10⁻⁶ /K (⊥), 5.3 × 10⁻⁶ /K (∥)',
        'conductivity': '35 W/m·K',
        'dndt': '13.8 × 10⁻⁶ /K',
        'maxtemp': '~1800°C (melting point 2050°C)',
        'note': 'Sapphire exhibits excellent thermal shock resistance due to high thermal conductivity and moderate CTE. Suitable for extreme temperature environments.'
    },
    'silicon': {
        'cte': '2.6 × 10⁻⁶ /K',
        'conductivity': '149 W/m·K',
        'dndt': '164 × 10⁻⁶ /K at 1.3 μm',
        'maxtemp': '~400°C (in optical applications)',
        'note': 'Silicon has very high thermal conductivity and low CTE, but a very large dn/dT in the IR. Thermal management is critical for stable optical performance.'
    },
    'germanium': {
        'cte': '6.1 × 10⁻⁶ /K',
        'conductivity': '60 W/m·K',
        'dndt': '396 × 10⁻⁶ /K at 10.6 μm',
        'maxtemp': '~100°C (in optical applications due to high dn/dT)',
        'note': 'Germanium has the highest dn/dT among common IR materials. Temperature stabilization or athermalization is essential for precision IR optics.'
    },
    'zinc-sulfide': {
        'cte': '6.6 × 10⁻⁶ /K',
        'conductivity': '17 W/m·K',
        'dndt': '-0.4 × 10⁻⁶ /K at 10.6 μm',
        'maxtemp': '~200°C',
        'note': 'Cleartran ZnS has a near-zero dn/dT, making it thermally stable for broadband IR applications without significant focus shift.'
    },
    'znse': {
        'cte': '7.1 × 10⁻⁶ /K',
        'conductivity': '18 W/m·K',
        'dndt': '61 × 10⁻⁶ /K at 10.6 μm',
        'maxtemp': '~150°C',
        'note': 'ZnSe has moderate thermal properties. The relatively high dn/dT requires thermal consideration in high-power CO₂ laser applications.'
    },
    'magnesium-fluoride': {
        'cte': '8.4 × 10⁻⁶ /K (⊥), 13.7 × 10⁻⁶ /K (∥)',
        'conductivity': '~15 W/m·K',
        'dndt': '-2.0 × 10⁻⁶ /K (⊥)',
        'maxtemp': '~500°C',
        'note': 'MgF₂ is birefringent, so thermal properties vary with crystal axis orientation. Moderate thermal expansion requires consideration in precision mounts.'
    },
    'borosilicate': {
        'cte': '8.3 × 10⁻⁶ /K',
        'conductivity': '1.14 W/m·K',
        'dndt': '3 × 10⁻⁶ /K',
        'maxtemp': '~500°C (annealing point 525°C)',
        'note': 'Borosilicate glass (B270) has thermal properties similar to BK7 with slightly higher CTE. Suitable for general-purpose optics at moderate temperatures.'
    }
}

mfg_data = {
    'bk7': {
        'machinability': 'Easy to machine, good for complex geometries. Standard optical grinding and machining methods apply.',
        'polishing': 'Excellent polishability, achieves low scatter surfaces. Standard optical polishing compounds work well.',
        'environmental': 'Low moisture absorption, stable in normal laboratory and industrial environments. Avoid prolonged high humidity.',
        'cost': 'Low cost, widely available in large blanks and standard sizes. Short lead times from stock.'
    },
    'uv-fused-silica': {
        'machinability': 'Harder than BK7, requires diamond tooling. Slower machining speed due to high hardness.',
        'polishing': 'Good polishability but slower process than BK7. Achieves excellent UV-grade surface finish.',
        'environmental': 'Excellent chemical resistance and UV stability. Virtually unaffected by moisture and most solvents.',
        'cost': 'Moderate cost, available in large ingots. Higher than BK7 but justified by superior UV and thermal performance.'
    },
    'caf2': {
        'machinability': 'Soft material, relatively easy to machine but prone to cleavage along crystal planes. Handle with care during fabrication.',
        'polishing': 'Requires care to avoid subsurface damage. Can achieve excellent optical surfaces with proper technique.',
        'environmental': 'Slightly hygroscopic — store in dry conditions. Prolonged exposure to moisture may degrade surface quality.',
        'cost': 'Moderate to high cost. Size limited by crystal growth process. Larger blanks command premium pricing.'
    },
    'sapphire': {
        'machinability': 'Very hard (9 Mohs), requires diamond tooling throughout. Slow machining rate increases fabrication time.',
        'polishing': 'Excellent polish achievable but time-consuming process. Requires specialized polishing methods for hard materials.',
        'environmental': 'Excellent chemical and scratch resistance. Virtually inert in most environments. Ideal for harsh conditions.',
        'cost': 'High cost, especially for large apertures. Crystal growth limitations affect maximum available size.'
    },
    'silicon': {
        'machinability': 'Very hard and brittle, diamond machining required. Care needed to avoid chipping and cracking during fabrication.',
        'polishing': 'Can achieve optical quality surfaces with diamond polishing. Single-point diamond turning is also effective.',
        'environmental': 'Stable at room temperature. Oxidation occurs above 300°C, limiting high-temperature optical use.',
        'cost': 'Moderate cost, readily available from semiconductor industry supply chains. Good value for IR applications.'
    },
    'germanium': {
        'machinability': 'Can be single-point diamond turned efficiently. Relatively straightforward to machine to shape.',
        'polishing': 'Standard optical polishing methods apply. Achieves good surface quality for IR applications.',
        'environmental': 'High dn/dT requires strict temperature control in use. Oxidation above 100°C limits operating range.',
        'cost': 'High cost due to expensive raw germanium material. Price fluctuates with semiconductor industry demand.'
    },
    'zinc-sulfide': {
        'machinability': 'Relatively soft material, easy to machine. CVD-grown Cleartran grade machines cleanly.',
        'polishing': 'Good polishability. Standard optical polishing methods produce high-quality IR surfaces.',
        'environmental': 'Low moisture absorption, chemically stable in most environments. Good durability for field-deployed IR optics.',
        'cost': 'Moderate cost. CVD process limits maximum blank size. Multi-spectral grade costs more than standard.'
    },
    'znse': {
        'machinability': 'Soft material, easy to machine and diamond turn. One of the easiest IR materials to fabricate.',
        'polishing': 'Good polishability with standard methods. Achieves excellent surface finish for CO₂ laser optics.',
        'environmental': 'Slight moisture absorption over time. Handle with clean gloves to avoid surface contamination.',
        'cost': 'High cost due to expensive raw material. Premium pricing for large-aperture and high-purity grades.'
    },
    'magnesium-fluoride': {
        'machinability': 'Relatively soft material. Careful handling needed to avoid chipping, especially along cleavage planes.',
        'polishing': 'Good polish achievable with standard optical methods. Orientation must be maintained during processing.',
        'environmental': 'Birefringent crystal — orientation must be specified and maintained. Moderate moisture resistance.',
        'cost': 'Moderate cost. Available in standard sizes. Crystal orientation requirements add to procurement complexity.'
    },
    'borosilicate': {
        'machinability': 'Easy to machine, similar behavior to BK7. Standard optical fabrication methods apply.',
        'polishing': 'Good polishability with conventional optical polishing techniques.',
        'environmental': 'Good chemical resistance, stable in normal environments. Resists most common laboratory chemicals.',
        'cost': 'Low cost, widely available from multiple suppliers. Excellent value for general-purpose optics.'
    }
}

def make_thermal_section(d):
    return '''
    <!-- Thermal Properties -->
    <section style="padding:40px 0;background:white;">
        <div class="container">
            <h2 style="font-size:1.5rem;color:#0f172a;margin-bottom:20px;">Thermal Properties</h2>
            <div style="overflow-x:auto;">
                <table style="width:100%;border-collapse:collapse;font-size:14px;">
                    <thead>
                        <tr style="background:#f1f5f9;">
                            <th style="padding:10px 12px;text-align:left;border-bottom:2px solid #e2e8f0;color:#1e3a5f;font-weight:600;">Property</th>
                            <th style="padding:10px 12px;text-align:left;border-bottom:2px solid #e2e8f0;color:#1e3a5f;font-weight:600;">Value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="padding:8px 12px;border-bottom:1px solid #f1f5f9;font-weight:500;">Coefficient of Thermal Expansion (CTE)</td>
                            <td style="padding:8px 12px;border-bottom:1px solid #f1f5f9;">''' + d['cte'] + '''</td>
                        </tr>
                        <tr style="background:#fafbfc;">
                            <td style="padding:8px 12px;border-bottom:1px solid #f1f5f9;font-weight:500;">Thermal Conductivity</td>
                            <td style="padding:8px 12px;border-bottom:1px solid #f1f5f9;">''' + d['conductivity'] + '''</td>
                        </tr>
                        <tr>
                            <td style="padding:8px 12px;border-bottom:1px solid #f1f5f9;font-weight:500;">dn/dT (Thermo-optic Coefficient)</td>
                            <td style="padding:8px 12px;border-bottom:1px solid #f1f5f9;">''' + d['dndt'] + '''</td>
                        </tr>
                        <tr style="background:#fafbfc;">
                            <td style="padding:8px 12px;border-bottom:1px solid #f1f5f9;font-weight:500;">Maximum Operating Temperature</td>
                            <td style="padding:8px 12px;border-bottom:1px solid #f1f5f9;">''' + d['maxtemp'] + '''</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <p style="font-size:13px;color:#64748b;margin-top:12px;line-height:1.6;">''' + d['note'] + '''</p>
        </div>
    </section>
'''

def make_mfg_section(d):
    return '''
    <!-- Manufacturing Considerations -->
    <section style="padding:40px 0;background:#f8fafc;">
        <div class="container">
            <h2 style="font-size:1.5rem;color:#0f172a;margin-bottom:20px;">Manufacturing Considerations</h2>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;">
                <div style="background:white;padding:16px;border-radius:8px;border:1px solid #e2e8f0;">
                    <h3 style="font-size:15px;font-weight:600;color:#1e3a5f;margin-bottom:6px;">Machinability</h3>
                    <p style="font-size:13px;color:#64748b;line-height:1.5;">''' + d['machinability'] + '''</p>
                </div>
                <div style="background:white;padding:16px;border-radius:8px;border:1px solid #e2e8f0;">
                    <h3 style="font-size:15px;font-weight:600;color:#1e3a5f;margin-bottom:6px;">Polishing</h3>
                    <p style="font-size:13px;color:#64748b;line-height:1.5;">''' + d['polishing'] + '''</p>
                </div>
                <div style="background:white;padding:16px;border-radius:8px;border:1px solid #e2e8f0;">
                    <h3 style="font-size:15px;font-weight:600;color:#1e3a5f;margin-bottom:6px;">Environmental Sensitivity</h3>
                    <p style="font-size:13px;color:#64748b;line-height:1.5;">''' + d['environmental'] + '''</p>
                </div>
                <div style="background:white;padding:16px;border-radius:8px;border:1px solid #e2e8f0;">
                    <h3 style="font-size:15px;font-weight:600;color:#1e3a5f;margin-bottom:6px;">Cost &amp; Availability</h3>
                    <p style="font-size:13px;color:#64748b;line-height:1.5;">''' + d['cost'] + '''</p>
                </div>
            </div>
        </div>
    </section>
'''

# Structure A pages: BK7, CaF2, Sapphire, UV Fused Silica, ZnSe
# Thermal: after <!-- Typical Applications --> section closing, before <!-- Common Coating Options -->
# Mfg: after <!-- Common Coating Options --> section closing, before <!-- Products Using This Material -->

# Structure B pages: Borosilicate, Germanium, Silicon, Magnesium Fluoride, Zinc Sulfide
# Thermal: after <!-- Applications --> section, before <!-- Coating Options -->
# Mfg: after <!-- Engineering Considerations --> section, before <!-- Material Comparison -->

import os

structure_a = ['bk7', 'caf2', 'sapphire', 'uv-fused-silica', 'znse']
structure_b = ['borosilicate', 'germanium', 'silicon', 'magnesium-fluoride', 'zinc-sulfide']

all_materials = structure_a + structure_b

for mat in all_materials:
    fpath = '/tmp/v151-work/materials/' + mat + '/index.html'
    if not os.path.exists(fpath):
        print(f"SKIP: {fpath} does not exist")
        continue
    
    with open(fpath, 'r') as f:
        content = f.read()
    
    thermal_html = make_thermal_section(thermal_data[mat])
    mfg_html = make_mfg_section(mfg_data[mat])
    
    modified = False
    
    if mat in structure_a:
        # Insert Thermal Properties: before <!-- Common Coating Options -->
        if 'Thermal Properties' not in content:
            anchor = '<!-- Common Coating Options -->'
            if anchor in content:
                content = content.replace(anchor, thermal_html + '\n    ' + anchor, 1)
                modified = True
                print(f"  [A] Inserted Thermal Properties in {mat}")
            else:
                print(f"  [A] WARNING: Could not find anchor for Thermal in {mat}")
        
        # Insert Manufacturing Considerations: before <!-- Products Using This Material -->
        if 'Manufacturing Considerations' not in content:
            anchor = '<!-- Products Using This Material -->'
            if anchor in content:
                content = content.replace(anchor, mfg_html + '\n    ' + anchor, 1)
                modified = True
                print(f"  [A] Inserted Manufacturing Considerations in {mat}")
            else:
                print(f"  [A] WARNING: Could not find anchor for Mfg in {mat}")
    
    elif mat in structure_b:
        # Insert Thermal Properties: before <!-- Coating Options -->
        if 'Thermal Properties' not in content:
            anchor = '    <!-- Coating Options -->'
            if anchor in content:
                content = content.replace(anchor, thermal_html + '\n' + anchor, 1)
                modified = True
                print(f"  [B] Inserted Thermal Properties in {mat}")
            else:
                print(f"  [B] WARNING: Could not find anchor for Thermal in {mat}")
        
        # Insert Manufacturing Considerations: before <!-- Material Comparison -->
        if 'Manufacturing Considerations' not in content:
            anchor = '    <!-- Material Comparison -->'
            if anchor in content:
                content = content.replace(anchor, mfg_html + '\n' + anchor, 1)
                modified = True
                print(f"  [B] Inserted Manufacturing Considerations in {mat}")
            else:
                print(f"  [B] WARNING: Could not find anchor for Mfg in {mat}")
    
    if modified:
        with open(fpath, 'w') as f:
            f.write(content)
        print(f"  SAVED: {mat}")
    else:
        print(f"  NO CHANGE: {mat}")

print("\nDone!")
