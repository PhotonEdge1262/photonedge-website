/**
 * PhotonEdge AI Product Selector
 * Rule-based optical component recommendation engine
 * ES5 only - no const, let, arrow functions, template literals
 */

var AISelector = (function() {

    /* ===== Knowledge Base ===== */

    var applicationMap = {
        'laser-processing': {
            en: 'Laser Processing',
            zh: '激光加工',
            categories: ['Optical Mirrors', 'Optical Lenses', 'Optical Windows', 'Optical Beamsplitters'],
            prioritySlugs: ['laser-line-high-reflected-mirrors', 'high-energy-laser-mirrors', 'ndyag-output-couplers', 'bk7-plano-convex', 'bk7-bi-convex', 'bk7-plano-concave', 'laser-beam-expanders', 'bk7-windows', 'uv-fused-silica-windows', 'sapphire-windows', 'cube-beamsplitters', 'beamsplitter-plates', 'broadband-dielectric-mirrors', 'protected-aluminum-mirrors'],
            reason: {
                en: 'Laser processing demands high damage thresholds, precise beam control, and wavelength-specific coatings.',
                zh: '激光加工需要高损伤阈值、精确光束控制和特定波长镀膜。'
            }
        },
        'medical-imaging': {
            en: 'Medical Imaging',
            zh: '医疗成像',
            categories: ['Optical Lenses', 'Optical Windows', 'Optical Filters', 'Optical Prisms'],
            prioritySlugs: ['achromatic-doublet', 'aspherical-lenses', 'microscope-objectives', 'bk7-plano-convex', 'bk7-bi-convex', 'uv-fused-silica-windows', 'sapphire-windows', 'caf2-windows', 'narrow-band-interference-filters', 'uv-bandpass-filters', 'dichroic-mirrors', 'bk7-right-angle-prisms', 'cube-beamsplitters'],
            reason: {
                en: 'Medical imaging requires high transmission, biocompatible materials, and precise spectral filtering.',
                zh: '医疗成像需要高透过率、生物相容性材料和精确的光谱过滤。'
            }
        },
        'spectroscopy': {
            en: 'Spectroscopy',
            zh: '光谱分析',
            categories: ['Optical Prisms', 'Optical Windows', 'Optical Filters', 'Optical Lenses'],
            prioritySlugs: ['equilateral-dispersing-prisms', 'penta-prisms', 'bk7-right-angle-prisms', 'caf2-windows', 'uv-fused-silica-windows', 'sapphire-windows', 'znse-windows', 'narrow-band-interference-filters', 'uv-bandpass-filters', 'ir-bandpass-filters', 'uv-fused-silica-plano-convex', 'uv-fused-silica-bi-convex', 'bk7-plano-convex', 'achromatic-doublet'],
            reason: {
                en: 'Spectroscopy applications need broadband UV transmission, dispersion elements, and precise wavelength selection.',
                zh: '光谱分析需要宽带紫外透过、色散元件和精确的波长选择。'
            }
        },
        'research-lab': {
            en: 'Research & Laboratory',
            zh: '科研实验',
            categories: ['Optical Lenses', 'Optical Mirrors', 'Optical Windows', 'Optical Prisms', 'Optical Wave Plates', 'Optical Polarizers'],
            prioritySlugs: ['bk7-plano-convex', 'uv-fused-silica-plano-convex', 'protected-silver-mirrors', 'broadband-dielectric-mirrors', 'bk7-windows', 'uv-fused-silica-windows', 'multiple-order-waveplates', 'air-spaced-zero-order-waveplates', 'visible-linear-polarizers', 'glan-taylor-prisms'],
            reason: {
                en: 'Research labs need versatile, high-precision components across the full optical spectrum.',
                zh: '科研实验室需要全光谱范围内多功能、高精度的光学元件。'
            }
        },
        'defense-aerospace': {
            en: 'Defense & Aerospace',
            zh: '国防航天',
            categories: ['Optical Windows', 'Optical Mirrors', 'Optical Prisms', 'Optical Polarizers'],
            prioritySlugs: ['ge-windows', 'znse-windows', 'sapphire-windows', 'si-windows', 'protected-gold-mirrors', 'corner-cube-prisms', 'penta-prisms', 'ir-polarizers'],
            reason: {
                en: 'Defense applications demand IR materials (Ge, ZnSe, Si), environmental durability, and MIL-SPEC compliance.',
                zh: '国防应用需要红外材料（Ge、ZnSe、Si）、环境耐久性和军标合规。'
            }
        },
        'fiber-optic': {
            en: 'Fiber Optic Communication',
            zh: '光纤通信',
            categories: ['Optical Lenses', 'Optical Filters', 'Optical Polarizers'],
            prioritySlugs: ['bk7-c-lenses', 'bk7-ball-lenses', 'uv-fused-silica-ball-lenses', 'bk7-rod-lenses', 'narrow-band-interference-filters', 'visible-linear-polarizers', 'glan-laser-prisms'],
            reason: {
                en: 'Fiber optics requires compact coupling lenses, narrowband filtering, and polarization control.',
                zh: '光纤通信需要紧凑的耦合透镜、窄带滤波和偏振控制。'
            }
        },
        'industrial-metrology': {
            en: 'Industrial Metrology',
            zh: '工业计量',
            categories: ['Optical Prisms', 'Optical Mirrors', 'Optical Lenses', 'Optical Windows'],
            prioritySlugs: ['penta-prisms', 'corner-cube-prisms', 'roof-prisms', 'protected-silver-mirrors', 'retroreflector-prisms', 'bk7-plano-convex', 'bk7-windows'],
            reason: {
                en: 'Metrology relies on precise angle reference, beam steering, and interferometric-quality surfaces.',
                zh: '工业计量依赖精确的角度基准、光束导向和干涉级面型。'
            }
        },
        'fluorescence': {
            en: 'Fluorescence Microscopy',
            zh: '荧光显微',
            categories: ['Optical Filters', 'Optical Mirrors', 'Optical Lenses'],
            prioritySlugs: ['narrow-band-interference-filters', 'dichroic-mirrors', 'uv-bandpass-filters', 'uv-fused-silica-plano-convex', 'achromatic-doublet', 'broadband-dielectric-mirrors'],
            reason: {
                en: 'Fluorescence requires precise excitation/emission filtering, dichroic beam splitting, and UV-compatible optics.',
                zh: '荧光显微需要精确的激发/发射滤波、二向色分光和紫外兼容光学。'
            }
        }
    };

    var wavelengthMap = {
        'uv': {
            en: 'UV (200-400nm)',
            zh: '紫外 (200-400nm)',
            materials: ['UV Fused Silica(JGS1)', 'UV Fused Silica', 'CaF2', 'Al2O3 (Sapphire)'],
            mirrorSlugs: ['protected-aluminum-mirrors', 'enhanced-aluminum-mirrors', 'broadband-dielectric-mirrors'],
            filterSlugs: ['uv-bandpass-filters'],
            lensSlugs: ['uv-fused-silica-plano-convex', 'uv-fused-silica-bi-convex', 'uv-fused-silica-plano-concave', 'uv-fused-silica-ball-lenses', 'uv-fused-silica-rod-lenses'],
            windowSlugs: ['uv-fused-silica-windows', 'caf2-windows', 'sapphire-windows'],
            reason: {
                en: 'UV wavelengths require high-purity fused silica or CaF2 for optimal transmission.',
                zh: '紫外波长需要高纯度熔石英或氟化钙以获得最佳透过率。'
            }
        },
        'visible': {
            en: 'Visible (400-700nm)',
            zh: '可见光 (400-700nm)',
            materials: ['K9(BK7)', 'H-K9L(BK7)', 'UV Fused Silica(JGS1)', 'N-BK7/K9'],
            mirrorSlugs: ['protected-aluminum-mirrors', 'enhanced-aluminum-mirrors', 'protected-silver-mirrors', 'broadband-dielectric-mirrors'],
            filterSlugs: ['narrow-band-interference-filters', 'fixed-neutral-density-filters', 'variable-neutral-density-filters'],
            lensSlugs: ['bk7-plano-convex', 'bk7-bi-convex', 'bk7-plano-concave', 'achromatic-doublet', 'aspherical-lenses', 'microscope-objectives'],
            windowSlugs: ['bk7-windows', 'uv-fused-silica-windows', 'sapphire-windows'],
            reason: {
                en: 'Visible range is well-served by BK7 and fused silica with standard AR coatings.',
                zh: '可见光范围可由BK7和熔石英配合标准增透膜完美覆盖。'
            }
        },
        'nir': {
            en: 'NIR (700-1100nm)',
            zh: '近红外 (700-1100nm)',
            materials: ['K9(BK7)', 'H-K9L(BK7)', 'UV Fused Silica(JGS1)', 'N-BK7/K9'],
            mirrorSlugs: ['protected-silver-mirrors', 'protected-gold-mirrors', 'laser-line-high-reflected-mirrors', 'ndyag-output-couplers', 'high-energy-laser-mirrors', 'broadband-dielectric-mirrors'],
            filterSlugs: ['narrow-band-interference-filters', 'fixed-neutral-density-filters'],
            lensSlugs: ['bk7-plano-convex', 'bk7-bi-convex', 'uv-fused-silica-plano-convex', 'laser-beam-expanders'],
            windowSlugs: ['bk7-windows', 'uv-fused-silica-windows'],
            reason: {
                en: 'NIR applications benefit from protected silver/gold mirrors and standard AR coatings.',
                zh: '近红外应用适合使用保护银/金膜反射镜和标准增透膜。'
            }
        },
        'swir': {
            en: 'SWIR (1.1-2.5μm)',
            zh: '短波红外 (1.1-2.5μm)',
            materials: ['UV Fused Silica(JGS1)', 'CaF2', 'Al2O3 (Sapphire)', 'N-BK7/K9'],
            mirrorSlugs: ['protected-gold-mirrors', 'protected-silver-mirrors'],
            filterSlugs: ['narrow-band-interference-filters'],
            lensSlugs: ['uv-fused-silica-plano-convex', 'caf2-windows'],
            windowSlugs: ['uv-fused-silica-windows', 'caf2-windows', 'sapphire-windows'],
            reason: {
                en: 'SWIR requires fused silica or CaF2 for transmission; gold mirrors for reflection.',
                zh: '短波红外需要熔石英或氟化钙透过；金膜反射镜用于反射。'
            }
        },
        'mwir': {
            en: 'MWIR (3-5μm)',
            zh: '中波红外 (3-5μm)',
            materials: ['CaF2', 'Si', 'Al2O3 (Sapphire)'],
            mirrorSlugs: ['protected-gold-mirrors'],
            filterSlugs: [],
            lensSlugs: [],
            windowSlugs: ['caf2-windows', 'si-windows', 'sapphire-windows'],
            reason: {
                en: 'MWIR thermal imaging uses Si windows, CaF2 optics, and gold-coated mirrors.',
                zh: '中波红外热成像使用硅窗口、氟化钙光学件和金膜反射镜。'
            }
        },
        'lwir': {
            en: 'LWIR (8-14μm)',
            zh: '长波红外 (8-14μm)',
            materials: ['Ge', 'ZnSe'],
            mirrorSlugs: ['protected-gold-mirrors'],
            filterSlugs: [],
            lensSlugs: [],
            windowSlugs: ['ge-windows', 'znse-windows'],
            reason: {
                en: 'LWIR requires Germanium and ZnSe — the only practical transmitting materials in this band.',
                zh: '长波红外需要锗和硒化锌——该波段唯一实用的透射材料。'
            }
        },
        'broadband': {
            en: 'Broadband / Multi-wavelength',
            zh: '宽带 / 多波长',
            materials: ['UV Fused Silica(JGS1)', 'CaF2', 'Al2O3 (Sapphire)', 'H-K9L(BK7)'],
            mirrorSlugs: ['protected-silver-mirrors', 'broadband-dielectric-mirrors', 'protected-aluminum-mirrors'],
            filterSlugs: ['variable-neutral-density-filters', 'narrow-band-interference-filters'],
            lensSlugs: ['uv-fused-silica-plano-convex', 'achromatic-doublet', 'bk7-plano-convex'],
            windowSlugs: ['uv-fused-silica-windows', 'caf2-windows', 'sapphire-windows'],
            reason: {
                en: 'Broadband setups need materials with wide transmission ranges and versatile coatings.',
                zh: '宽带设置需要宽透过率范围的材料和通用镀膜。'
            }
        }
    };

    var componentTypeMap = {
        'auto': { en: 'Auto-detect (Recommended)', zh: '自动推荐（推荐）', category: null },
        'lenses': { en: 'Lenses', zh: '透镜', category: 'Optical Lenses' },
        'mirrors': { en: 'Mirrors', zh: '反射镜', category: 'Optical Mirrors' },
        'windows': { en: 'Windows', zh: '窗口片', category: 'Optical Windows' },
        'prisms': { en: 'Prisms', zh: '棱镜', category: 'Optical Prisms' },
        'filters': { en: 'Filters', zh: '滤光片', category: 'Optical Filters' },
        'beamsplitters': { en: 'Beamsplitters', zh: '分光镜', category: 'Optical Beamsplitters' },
        'waveplates': { en: 'Wave Plates', zh: '波片', category: 'Optical Wave Plates' },
        'polarizers': { en: 'Polarizers', zh: '偏振片', category: 'Optical Polarizers' }
    };

    /* ===== Scoring Engine ===== */

    function scoreProduct(product, application, wavelength, componentType) {
        var score = 0;
        var reasons = [];
        var lang = getCurrentLang();
        var appData = applicationMap[application];
        var wlData = wavelengthMap[wavelength];

        if (!appData || !wlData) return { score: 0, reasons: [] };

        var params = product.parameters || {};
        var material = params.material || params.substrate || '';

        // 1. Application priority match (0-40 points)
        var priorityIdx = appData.prioritySlugs.indexOf(product.slug);
        if (priorityIdx !== -1) {
            score += 40 - (priorityIdx * 3);
            reasons.push(appData.reason[lang] || appData.reason.en);
        }

        // 2. Application category match (0-30 points)
        if (appData.categories.indexOf(product.category) !== -1) {
            score += 30;
        }

        // 3. Wavelength material match (0-25 points)
        var matMatch = false;
        for (var i = 0; i < wlData.materials.length; i++) {
            if (material.indexOf(wlData.materials[i].split('(')[0]) !== -1 || material === wlData.materials[i]) {
                matMatch = true;
                break;
            }
        }
        if (matMatch) {
            score += 25;
            reasons.push(wlData.reason[lang] || wlData.reason.en);
        }

        // 4. Wavelength-specific product match (0-15 points)
        var wlSlugs = [].concat(
            wlData.mirrorSlugs || [],
            wlData.filterSlugs || [],
            wlData.lensSlugs || [],
            wlData.windowSlugs || []
        );
        if (wlSlugs.indexOf(product.slug) !== -1) {
            score += 15;
        }

        // 5. Component type filter
        if (componentType && componentType !== 'auto') {
            var typeData = componentTypeMap[componentType];
            if (typeData && typeData.category && product.category !== typeData.category) {
                score = Math.floor(score * 0.15); // Heavy penalty but don't eliminate completely
            }
        }

        // 6. Deduplicate reasons
        var uniqueReasons = [];
        var seenReasons = {};
        for (var j = 0; j < reasons.length; j++) {
            if (!seenReasons[reasons[j]]) {
                uniqueReasons.push(reasons[j]);
                seenReasons[reasons[j]] = true;
            }
        }

        return { score: score, reasons: uniqueReasons };
    }

    function recommend(application, wavelength, componentType, maxResults) {
        if (typeof PRODUCTS === 'undefined' || !PRODUCTS.length) return [];
        maxResults = maxResults || 5;

        var results = [];
        for (var i = 0; i < PRODUCTS.length; i++) {
            var scored = scoreProduct(PRODUCTS[i], application, wavelength, componentType);
            if (scored.score > 5) {
                results.push({
                    product: PRODUCTS[i],
                    score: scored.score,
                    reasons: scored.reasons
                });
            }
        }

        results.sort(function(a, b) { return b.score - a.score; });
        return results.slice(0, maxResults);
    }

    /* ===== UI Rendering ===== */

    var currentStep = 1;
    var selectedApp = '';
    var selectedWavelength = '';
    var selectedComponent = '';

    function init() {
        currentStep = 1;
        selectedApp = '';
        selectedWavelength = '';
        selectedComponent = '';
        renderWizard();
    }

    function renderWizard() {
        var container = document.getElementById('aiSelectorContent');
        if (!container) return;

        var lang = getCurrentLang();
        var html = '';

        // Progress bar
        html += '<div class="ai-progress">';
        html += '<div class="ai-progress-bar" style="width:' + (currentStep * 33.33) + '%"></div>';
        html += '</div>';
        html += '<div class="ai-progress-steps">';
        html += '<span class="ai-step' + (currentStep >= 1 ? ' active' : '') + '">' + (lang === 'zh' ? '应用场景' : 'Application') + '</span>';
        html += '<span class="ai-step' + (currentStep >= 2 ? ' active' : '') + '">' + (lang === 'zh' ? '工作波长' : 'Wavelength') + '</span>';
        html += '<span class="ai-step' + (currentStep >= 3 ? ' active' : '') + '">' + (lang === 'zh' ? '元件类型' : 'Component') + '</span>';
        html += '</div>';

        if (currentStep === 1) {
            html += renderStep1();
        } else if (currentStep === 2) {
            html += renderStep2();
        } else if (currentStep === 3) {
            html += renderStep3();
        } else if (currentStep === 4) {
            html += renderResults();
        }

        container.innerHTML = html;
    }

    function renderStep1() {
        var lang = getCurrentLang();
        var html = '<h3 class="ai-step-title">' + (lang === 'zh' ? '选择您的应用场景' : 'Select Your Application') + '</h3>';
        html += '<p class="ai-step-desc">' + (lang === 'zh' ? '告诉我们您的使用场景，我们将推荐最合适的光学元件' : 'Tell us your application and we will recommend the most suitable optical components') + '</p>';
        html += '<div class="ai-options-grid">';

        var appKeys = Object.keys(applicationMap);
        var icons = ['⚡', '🏥', '🔬', '🧪', '🛡️', '📡', '📐', '🔬'];
        for (var i = 0; i < appKeys.length; i++) {
            var key = appKeys[i];
            var app = applicationMap[key];
            var icon = icons[i] || '💡';
            var isSelected = selectedApp === key ? ' selected' : '';
            html += '<div class="ai-option-card' + isSelected + '" onclick="AISelector.selectApp(\'' + key + '\')">';
            html += '<div class="ai-option-icon">' + icon + '</div>';
            html += '<div class="ai-option-label">' + (lang === 'zh' ? app.zh : app.en) + '</div>';
            html += '</div>';
        }

        html += '</div>';
        html += '<div class="ai-nav">';
        html += '<button class="ai-btn ai-btn-next' + (!selectedApp ? ' disabled' : '') + '" onclick="AISelector.nextStep()"' + (!selectedApp ? ' disabled' : '') + '>' + (lang === 'zh' ? '下一步' : 'Next') + ' →</button>';
        html += '</div>';
        return html;
    }

    function renderStep2() {
        var lang = getCurrentLang();
        var html = '<h3 class="ai-step-title">' + (lang === 'zh' ? '选择工作波长范围' : 'Select Wavelength Range') + '</h3>';
        html += '<p class="ai-step-desc">' + (lang === 'zh' ? '不同波长需要不同的光学材料和镀膜' : 'Different wavelengths require different optical materials and coatings') + '</p>';
        html += '<div class="ai-options-grid ai-wavelength-grid">';

        var wlKeys = Object.keys(wavelengthMap);
        var wlIcons = ['☄️', '🌈', '🔴', '🟤', '🌡️', '🔥', '📡'];
        for (var i = 0; i < wlKeys.length; i++) {
            var key = wlKeys[i];
            var wl = wavelengthMap[key];
            var icon = wlIcons[i] || '💡';
            var isSelected = selectedWavelength === key ? ' selected' : '';
            html += '<div class="ai-option-card' + isSelected + '" onclick="AISelector.selectWavelength(\'' + key + '\')">';
            html += '<div class="ai-option-icon">' + icon + '</div>';
            html += '<div class="ai-option-label">' + (lang === 'zh' ? wl.zh : wl.en) + '</div>';
            html += '</div>';
        }

        html += '</div>';
        html += '<div class="ai-nav">';
        html += '<button class="ai-btn ai-btn-back" onclick="AISelector.prevStep()">← ' + (lang === 'zh' ? '上一步' : 'Back') + '</button>';
        html += '<button class="ai-btn ai-btn-next' + (!selectedWavelength ? ' disabled' : '') + '" onclick="AISelector.nextStep()"' + (!selectedWavelength ? ' disabled' : '') + '">' + (lang === 'zh' ? '下一步' : 'Next') + ' →</button>';
        html += '</div>';
        return html;
    }

    function renderStep3() {
        var lang = getCurrentLang();
        var html = '<h3 class="ai-step-title">' + (lang === 'zh' ? '选择元件类型' : 'Select Component Type') + '</h3>';
        html += '<p class="ai-step-desc">' + (lang === 'zh' ? '可选择自动推荐，或指定需要的元件类别' : 'Choose auto-detect or specify a component category') + '</p>';
        html += '<div class="ai-options-grid ai-component-grid">';

        var compKeys = Object.keys(componentTypeMap);
        var compIcons = ['🤖', '🔭', '🪞', '🪟', '🔺', '🎨', '🔀', '🌊', '🔲'];
        for (var i = 0; i < compKeys.length; i++) {
            var key = compKeys[i];
            var comp = componentTypeMap[key];
            var icon = compIcons[i] || '💡';
            var isSelected = selectedComponent === key ? ' selected' : '';
            html += '<div class="ai-option-card' + isSelected + '" onclick="AISelector.selectComponent(\'' + key + '\')">';
            html += '<div class="ai-option-icon">' + icon + '</div>';
            html += '<div class="ai-option-label">' + (lang === 'zh' ? comp.zh : comp.en) + '</div>';
            html += '</div>';
        }

        html += '</div>';
        html += '<div class="ai-nav">';
        html += '<button class="ai-btn ai-btn-back" onclick="AISelector.prevStep()">← ' + (lang === 'zh' ? '上一步' : 'Back') + '</button>';
        html += '<button class="ai-btn ai-btn-recommend" onclick="AISelector.showResults()">✨ ' + (lang === 'zh' ? '获取推荐' : 'Get Recommendations') + '</button>';
        html += '</div>';
        return html;
    }

    function renderResults() {
        var lang = getCurrentLang();
        var results = recommend(selectedApp, selectedWavelength, selectedComponent, 5);

        var html = '<h3 class="ai-step-title">' + (lang === 'zh' ? '🎯 为您推荐' : '🎯 Recommendations for You') + '</h3>';

        var appLabel = applicationMap[selectedApp] ? (lang === 'zh' ? applicationMap[selectedApp].zh : applicationMap[selectedApp].en) : '';
        var wlLabel = wavelengthMap[selectedWavelength] ? (lang === 'zh' ? wavelengthMap[selectedWavelength].zh : wavelengthMap[selectedWavelength].en) : '';
        html += '<p class="ai-results-summary">' + (lang === 'zh' ? '应用：' : 'Application: ') + appLabel + ' | ' + (lang === 'zh' ? '波长：' : 'Wavelength: ') + wlLabel + '</p>';

        if (results.length === 0) {
            html += '<div class="ai-no-results">';
            html += '<p>' + (lang === 'zh' ? '未找到完全匹配的产品，请联系我们获取定制方案。' : 'No exact matches found. Please contact us for custom solutions.') + '</p>';
            html += '<a href="/contact.html" class="ai-btn ai-btn-recommend">' + (lang === 'zh' ? '联系工程师' : 'Contact Engineer') + '</a>';
            html += '</div>';
        } else {
            html += '<div class="ai-results-grid">';
            for (var i = 0; i < results.length; i++) {
                var r = results[i];
                var p = r.product;
                var displayName = lang === 'zh' && p.nameZh ? p.nameZh : p.name;
                var displayCategory = lang === 'zh' && p.categoryZh ? p.categoryZh : p.category;
                var displayDesc = lang === 'zh' && p.descriptionZh ? p.descriptionZh : p.description;
                var matchPct = Math.min(99, Math.round(r.score * 1.1));

                html += '<div class="ai-result-card">';
                html += '<div class="ai-result-rank">#' + (i + 1) + '</div>';
                html += '<div class="ai-result-match">' + matchPct + '% ' + (lang === 'zh' ? '匹配' : 'Match') + '</div>';
                html += '<div class="ai-result-img-wrap">';
                html += '<img src="/' + p.image + '" alt="' + displayName + '" loading="lazy">';
                html += '</div>';
                html += '<div class="ai-result-info">';
                html += '<div class="ai-result-category">' + displayCategory + '</div>';
                html += '<h4 class="ai-result-name">' + displayName + '</h4>';
                html += '<p class="ai-result-desc">' + displayDesc.substring(0, 100) + (displayDesc.length > 100 ? '...' : '') + '</p>';

                if (r.reasons.length > 0) {
                    html += '<div class="ai-result-reasons">';
                    for (var j = 0; j < r.reasons.length; j++) {
                        html += '<div class="ai-result-reason">✓ ' + r.reasons[j] + '</div>';
                    }
                    html += '</div>';
                }

                html += '<div class="ai-result-actions">';
                html += '<a href="/products/' + p.slug + '/" class="ai-btn ai-btn-outline">' + (lang === 'zh' ? '查看详情' : 'View Details') + '</a>';
                html += '<a href="/contact.html?product=' + p.slug + '" class="ai-btn ai-btn-primary">' + (lang === 'zh' ? '询价' : 'Request Quote') + '</a>';
                html += '</div>';
                html += '</div></div>';
            }
            html += '</div>';
        }

        html += '<div class="ai-nav ai-nav-results">';
        html += '<button class="ai-btn ai-btn-back" onclick="AISelector.reset()">← ' + (lang === 'zh' ? '重新选择' : 'Start Over') + '</button>';
        html += '<a href="/products.html" class="ai-btn ai-btn-outline">' + (lang === 'zh' ? '浏览全部产品' : 'Browse All Products') + '</a>';
        html += '<a href="/contact.html" class="ai-btn ai-btn-primary">' + (lang === 'zh' ? '联系工程师' : 'Contact Engineer') + '</a>';
        html += '</div>';
        return html;
    }

    /* ===== Event Handlers ===== */

    function selectApp(app) {
        selectedApp = app;
        renderWizard();
    }

    function selectWavelength(wl) {
        selectedWavelength = wl;
        renderWizard();
    }

    function selectComponent(comp) {
        selectedComponent = comp;
        renderWizard();
    }

    function nextStep() {
        if (currentStep === 1 && !selectedApp) return;
        if (currentStep === 2 && !selectedWavelength) return;
        currentStep++;
        renderWizard();
    }

    function prevStep() {
        if (currentStep > 1) {
            currentStep--;
            renderWizard();
        }
    }

    function showResults() {
        currentStep = 4;
        renderWizard();
    }

    function reset() {
        currentStep = 1;
        selectedApp = '';
        selectedWavelength = '';
        selectedComponent = '';
        renderWizard();
    }

    /* ===== Public API ===== */
    return {
        init: init,
        selectApp: selectApp,
        selectWavelength: selectWavelength,
        selectComponent: selectComponent,
        nextStep: nextStep,
        prevStep: prevStep,
        showResults: showResults,
        reset: reset,
        recommend: recommend
    };

})();

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
        if (typeof AISelector !== 'undefined') AISelector.init();
    });
} else {
    if (typeof AISelector !== 'undefined') AISelector.init();
}
