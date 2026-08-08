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
    // Materials Section
    // ============================================================
    function renderMaterials(enh, lang) {
        if (!enh) return '';
        var materials = getField(enh, 'materials', lang);
        if (!materials || !materials.length) return '';

        var title = lang === 'zh' ? '材料选项' : 'Available Materials';
        var html = '<section class="enh-section enh-materials">' +
            '<div class="container">' +
            '<h2 class="enh-section-title">' + title + '</h2>' +
            '<div class="enh-materials-grid">';

        for (var i = 0; i < materials.length; i++) {
            html += '<div class="enh-material-item">' +
                '<span class="enh-material-icon">◈</span>' +
                '<span class="enh-material-name">' + materials[i] + '</span>' +
                '</div>';
        }
        html += '</div></div></section>';
        return html;
    }

    // ============================================================
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
        sectionsHtml += renderMaterials(enh, lang);
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
