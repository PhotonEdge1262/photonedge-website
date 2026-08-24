// ============================================================
// PhotonEdge V84 - Product Enhanced Render
// ES5 compatible: var/function only, no let/const/arrow/template
// Renders Application Scenarios, Selection Guide, FAQs,
// Materials & Coatings, Related Products, Related Articles
// ============================================================

var ProductEnhancedRender = (function() {

    // Get current language
    function getLang() {
        var lang = localStorage.getItem('lang');
        if (!lang) lang = 'en';
        return lang;
    }

    // Get enhancement data for a product slug
    function getEnhancement(slug) {
        if (typeof PRODUCT_ENHANCEMENTS === 'undefined' || !PRODUCT_ENHANCEMENTS[slug]) {
            return null;
        }
        return PRODUCT_ENHANCEMENTS[slug];
    }

    // Get field value with language suffix
    function getField(enh, baseField, lang) {
        if (!enh) return null;
        if (lang === 'zh') {
            var zhField = baseField + 'Zh';
            if (enh[zhField] !== undefined) return enh[zhField];
        }
        return enh[baseField];
    }

    // ============================================================
    // Applications Section
    // ============================================================
    function renderApplications(enh, lang) {
        if (!enh) return '';
        var apps = getField(enh, 'applications', lang);
        if (!apps || !apps.length) return '';

        var title = lang === 'zh' ? '应用场景' : 'Application Scenarios';
        var html = '<section class="enh-section enh-applications">' +
            '<div class="container">' +
            '<h2 class="enh-section-title">' + title + '</h2>' +
            '<div class="enh-app-tags">';

        for (var i = 0; i < apps.length; i++) {
            html += '<span class="enh-app-tag">' + apps[i] + '</span>';
        }
        html += '</div></div></section>';
        return html;
    }

    // ============================================================
    // Application Details Section
    // ============================================================
    function renderApplicationDetails(enh, lang) {
        if (!enh) return '';
        var details = getField(enh, 'applicationDetails', lang);
        if (!details || !details.length) return '';

        var title = lang === 'zh' ? '应用详情' : 'Application Details';
        var html = '<section class="enh-section enh-app-details">' +
            '<div class="container">' +
            '<h2 class="enh-section-title">' + title + '</h2>' +
            '<div class="enh-app-detail-grid">';

        for (var i = 0; i < details.length; i++) {
            var d = details[i];
            html += '<div class="enh-app-detail-card">' +
                '<h3 class="enh-app-detail-title">' + d.title + '</h3>' +
                '<p class="enh-app-detail-desc">' + d.description + '</p>' +
                '</div>';
        }
        html += '</div></div></section>';
        return html;
    }

    // ============================================================
    // Selection Guide Section
    // ============================================================
    function renderSelectionGuide(enh, lang) {
        if (!enh) return '';
        var guide = getField(enh, 'selectionGuide', lang);
        if (!guide) return '';

        var title = lang === 'zh' ? '选型指南' : 'Selection Guide';
        var paragraphs = guide.split('\n\n');
        var bodyHtml = '';
        for (var i = 0; i < paragraphs.length; i++) {
            if (paragraphs[i].trim()) {
                bodyHtml += '<p class="enh-guide-paragraph">' + paragraphs[i].trim() + '</p>';
            }
        }

        var html = '<section class="enh-section enh-selection-guide">' +
            '<div class="container">' +
            '<h2 class="enh-section-title">' + title + '</h2>' +
            '<div class="enh-guide-content">' + bodyHtml + '</div>' +
            '</div></section>';
        return html;
    }

    // ============================================================
    // ============================================================
    // Materials Section - Knowledge Graph Edition
    // Shows available materials with descriptions and links to material pages
    // ============================================================
    function renderMaterials(enh, lang, componentType) {
        if (!enh) return '';
        
        // Material database with descriptions and links
        var MATERIAL_DB = {
            "BK7": {
                slug: "bk7",
                desc: { en: "General-purpose visible/NIR glass, excellent homogeneity, cost-effective.", zh: "通用可见/近红外玻璃，均匀性好，性价比高。" }
            },
            "UV Fused Silica": {
                slug: "uv-fused-silica",
                desc: { en: "Superb UV transmission, high laser damage threshold, low thermal expansion.", zh: "优异的紫外透过率，高激光损伤阈值，低热膨胀。" }
            },
            "CaF2": {
                slug: "caf2",
                desc: { en: "Deep UV to mid-IR transmission, low dispersion, ideal for broadband.", zh: "深紫外到中红外透过，低色散，适合宽带应用。" }
            },
            "Sapphire": {
                slug: "sapphire",
                desc: { en: "Extremely hard and durable, UV to mid-IR, scratch resistant.", zh: "极高硬度和耐用性，紫外到中红外，耐刮擦。" }
            },
            "ZnSe": {
                slug: "znse",
                desc: { en: "Excellent IR transmission, ideal for CO2 laser and thermal imaging.", zh: "优异的红外透过，理想用于CO2激光和热成像。" }
            },
            "Germanium": {
                slug: "germanium",
                desc: { en: "High refractive index IR material, ideal for MWIR/LWIR imaging.", zh: "高折射率红外材料，理想用于中波/长波红外成像。" }
            },
            "Silicon": {
                slug: "silicon",
                desc: { en: "Lightweight NIR/SWIR material, good thermal conductivity.", zh: "轻质近红外/短波红外材料，良好的导热性。" }
            },
            "Quartz": {
                slug: "uv-fused-silica",
                desc: { en: "Birefringent crystal for waveplates and polarization optics.", zh: "双折射晶体，用于波片和偏振光学。" }
            }
        };
        
        // Default materials by component type
        var DEFAULT_MATERIALS = {
            "Lens": ["BK7", "UV Fused Silica", "CaF2", "Sapphire"],
            "Window": ["BK7", "UV Fused Silica", "Sapphire", "ZnSe"],
            "Mirror": ["UV Fused Silica", "BK7", "Silicon"],
            "Filter": ["BK7", "UV Fused Silica", "Sapphire"],
            "Prism": ["BK7", "UV Fused Silica", "CaF2"],
            "Beamsplitter": ["BK7", "UV Fused Silica"],
            "Waveplate": ["UV Fused Silica", "Quartz"],
            "Polarizer": ["UV Fused Silica", "Quartz"],
            "Accessory": ["BK7", "UV Fused Silica"],
            "Mount": ["BK7"]
        };
        
        // Determine materials list
        var materials = getField(enh, 'materials', lang);
        if (!materials || !materials.length) {
            materials = DEFAULT_MATERIALS[componentType] || ["BK7", "UV Fused Silica"];
        }
        
        var title = lang === 'zh' ? '可选光学材料' : 'Available Optical Materials';
        var html = '<section class="enh-section enh-materials" style="background: #f8fafc;">' +
            '<div class="container">' +
            '<h2 class="enh-section-title">' + title + '</h2>' +
            '<p style="color:#64748b;text-align:center;max-width:600px;margin:0 auto 24px;font-size:14px;">' +
            (lang === 'zh' ? '根据您的波长、环境和预算要求选择最佳基底材料。' : 'Select the optimal substrate material based on your wavelength, environment, and budget requirements.') +
            '</p>' +
            '<div class="enh-materials-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px;">';
        
        for (var i = 0; i < materials.length; i++) {
            var matName = materials[i];
            var matInfo = MATERIAL_DB[matName];
            var matSlug = matInfo ? matInfo.slug : 'bk7';
            var matDesc = matInfo && matInfo.desc ? matInfo.desc[lang] || matInfo.desc.en : '';
            
            html += '<a href="/materials/' + matSlug + '/" class="enh-material-item" style="display:block;text-decoration:none;color:inherit;background:white;border:1px solid #e2e8f0;border-radius:10px;padding:18px;transition:all 0.3s;">' +
                '<div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">' +
                '<span class="enh-material-icon" style="font-size:20px;">◈</span>' +
                '<span class="enh-material-name" style="font-weight:600;color:#1e3a5f;font-size:15px;">' + matName + '</span>' +
                '</div>' +
                '<p style="color:#64748b;font-size:12px;line-height:1.5;margin:0;">' + matDesc + '</p>' +
                '</a>';
        }
        html += '</div>';
        
        // AI Engineer CTA
        html += '<div style="margin-top:28px;text-align:center;">' +
            '<p style="color:#64748b;margin-bottom:12px;font-size:14px;">' +
            (lang === 'zh' ? '不确定选择哪种材料？' : 'Not sure which material to choose?') +
            '</p>' +
            '<a href="/ai-optical-engineer.html" style="display:inline-block;padding:10px 24px;background:#3b82f6;color:white;border-radius:6px;font-weight:600;text-decoration:none;font-size:14px;">' +
            (lang === 'zh' ? '咨询AI光学工程师' : 'Ask AI Optical Engineer') +
            ' →</a>' +
            '</div>';
        
        html += '</div></section>';
        return html;
    }
    // Coatings Section
    // ============================================================
    function renderCoatings(enh, lang) {
        if (!enh) return '';
        var coatings = getField(enh, 'coatings', lang);
        if (!coatings || !coatings.length) return '';

        var title = lang === 'zh' ? '镀膜选项' : 'Coating Options';
        var html = '<section class="enh-section enh-coatings">' +
            '<div class="container">' +
            '<h2 class="enh-section-title">' + title + '</h2>' +
            '<div class="enh-coatings-list">';

        for (var i = 0; i < coatings.length; i++) {
            html += '<div class="enh-coating-item">' +
                '<span class="enh-coating-check">✓</span>' +
                '<span class="enh-coating-text">' + coatings[i] + '</span>' +
                '</div>';
        }
        html += '</div></div></section>';
        return html;
    }

    // ============================================================
    // FAQ Section
    // ============================================================
    function renderFAQ(enh, lang) {
        if (!enh) return '';
        var faqs = getField(enh, 'faq', lang);
        if (!faqs || !faqs.length) return '';

        var title = lang === 'zh' ? '常见问题' : 'Frequently Asked Questions';
        var html = '<section class="enh-section enh-faq">' +
            '<div class="container">' +
            '<h2 class="enh-section-title">' + title + '</h2>' +
            '<div class="enh-faq-list">';

        for (var i = 0; i < faqs.length; i++) {
            var faq = faqs[i];
            var qId = 'enh-faq-' + i;
            html += '<div class="enh-faq-item">' +
                '<button class="enh-faq-question" onclick="ProductEnhancedRender.toggleFaq(\'' + qId + '\')">' +
                '<span class="enh-faq-q-text">' + faq.question + '</span>' +
                '<span class="enh-faq-icon" id="' + qId + '-icon">+</span>' +
                '</button>' +
                '<div class="enh-faq-answer" id="' + qId + '">' +
                '<p>' + faq.answer + '</p>' +
                '</div>' +
                '</div>';
        }
        html += '</div></div></section>';

        // Add FAQ schema JSON-LD
        var schema = {
            '@context': 'https://schema.org',
            '@type': 'FAQPage',
            'mainEntity': []
        };
        for (var j = 0; j < faqs.length; j++) {
            schema.mainEntity.push({
                '@type': 'Question',
                'name': faqs[j].question,
                'acceptedAnswer': {
                    '@type': 'Answer',
                    'text': faqs[j].answer
                }
            });
        }
        html += '<script type="application/ld+json">' + JSON.stringify(schema) + '</script>';

        return html;
    }

    // Toggle FAQ answer
    function toggleFaq(id) {
        var answer = document.getElementById(id);
        var icon = document.getElementById(id + '-icon');
        if (!answer) return;
        if (answer.classList.contains('open')) {
            answer.classList.remove('open');
            if (icon) icon.textContent = '+';
        } else {
            answer.classList.add('open');
            if (icon) icon.textContent = '−';
        }
    }

    // ============================================================
    // Related Products Section
    // ============================================================
    function renderRelatedProducts(enh, lang) {
        if (!enh) return '';
        var related = enh.relatedProducts;
        if (!related || !related.length) return '';

        var title = lang === 'zh' ? '相关产品' : 'Related Components';
        var subtitle = lang === 'zh'
            ? '探索我们的配套光学元件，为您的系统找到完整解决方案'
            : 'Explore our complementary optical components to find a complete solution for your system';

        var html = '<section class="enh-section enh-related-products">' +
            '<div class="container">' +
            '<h2 class="enh-section-title">' + title + '</h2>' +
            '<p class="enh-section-subtitle">' + subtitle + '</p>' +
            '<div class="enh-related-grid">';

        for (var i = 0; i < related.length && i < 5; i++) {
            var rp = related[i];
            var prodName = lang === 'zh' && rp.nameZh ? rp.nameZh : rp.name;
            var imgSrc = getProductImage(rp.slug);
            html += '<a href="/products/' + rp.slug + '/" class="enh-related-card">' +
                '<div class="enh-related-img-wrap">' +
                '<img src="' + imgSrc + '" alt="' + prodName + '" loading="lazy" onerror="this.style.display=\'none\'">' +
                '</div>' +
                '<div class="enh-related-info">' +
                '<h3 class="enh-related-name">' + prodName + '</h3>' +
                '<span class="enh-related-link">' + (lang === 'zh' ? '查看详情 →' : 'Learn More →') + '</span>' +
                '</div>' +
                '</a>';
        }
        html += '</div></div></section>';
        return html;
    }

    // Helper: get product image from PRODUCTS array
    function getProductImage(slug) {
        if (typeof PRODUCTS === 'undefined') return '/images/logo.png';
        for (var i = 0; i < PRODUCTS.length; i++) {
            if (PRODUCTS[i].slug === slug) {
                return '/' + PRODUCTS[i].image;
            }
        }
        return '/images/logo.png';
    }

    // ============================================================
    // Related Articles Section
    // ============================================================
    function renderRelatedArticles(enh, lang) {
        if (!enh) return '';
        var articles = getField(enh, 'relatedArticles', lang);
        if (!articles || !articles.length) return '';

        var title = lang === 'zh' ? '相关文章' : 'Related Articles';
        var subtitle = lang === 'zh'
            ? '深入了解光学技术知识，助您做出更好的选型决策'
            : 'Deepen your optical knowledge to make better component selection decisions';

        var html = '<section class="enh-section enh-related-articles">' +
            '<div class="container">' +
            '<h2 class="enh-section-title">' + title + '</h2>' +
            '<p class="enh-section-subtitle">' + subtitle + '</p>' +
            '<div class="enh-articles-grid">';

        for (var i = 0; i < articles.length && i < 3; i++) {
            var article = articles[i];
            var artTitle = article.title;
            var url = article.slug;
            if (url.indexOf('http') !== 0 && url.indexOf('/') !== 0) {
                url = '/' + url;
            }
            html += '<a href="' + url + '" class="enh-article-card">' +
                '<div class="enh-article-icon">📄</div>' +
                '<h3 class="enh-article-title">' + artTitle + '</h3>' +
                '<span class="enh-article-link">' + (lang === 'zh' ? '阅读文章 →' : 'Read Article →') + '</span>' +
                '</a>';
        }
        html += '</div></div></section>';
        return html;
    }

    // ============================================================
    // Main render function: injects all enhanced sections
    // ============================================================
    function renderAll(slug, containerSelector) {
        var enh = getEnhancement(slug);
        if (!enh) {
            console.log('No enhancement data for:', slug);
            return;
        }

        var lang = getLang();
        var container = document.querySelector(containerSelector);
        if (!container) {
            console.log('Container not found:', containerSelector);
            return;
        }

        // Build sections in order
        var sectionsHtml = '';
        sectionsHtml += renderApplications(enh, lang);
        sectionsHtml += renderApplicationDetails(enh, lang);
        sectionsHtml += renderSelectionGuide(enh, lang);
        sectionsHtml += renderMaterials(enh, lang, currentProduct.componentType);
        sectionsHtml += renderCoatings(enh, lang);
        sectionsHtml += renderFAQ(enh, lang);
        sectionsHtml += renderRelatedProducts(enh, lang);
        sectionsHtml += renderRelatedArticles(enh, lang);

        // Insert before the existing relatedSection (or at end of container)
        var existingRelated = document.getElementById('relatedSection');
        if (existingRelated) {
            var tempDiv = document.createElement('div');
            tempDiv.innerHTML = sectionsHtml;
            // Insert each section before relatedSection
            while (tempDiv.firstChild) {
                existingRelated.parentNode.insertBefore(tempDiv.firstChild, existingRelated);
            }
        } else {
            container.innerHTML += sectionsHtml;
        }
    }

    // ============================================================
    // Public API
    // ============================================================
    return {
        renderAll: renderAll,
        renderApplications: renderApplications,
        renderApplicationDetails: renderApplicationDetails,
        renderSelectionGuide: renderSelectionGuide,
        renderMaterials: renderMaterials,
        renderCoatings: renderCoatings,
        renderFAQ: renderFAQ,
        renderRelatedProducts: renderRelatedProducts,
        renderRelatedArticles: renderRelatedArticles,
        toggleFaq: toggleFaq,
        getEnhancement: getEnhancement
    };
})();
