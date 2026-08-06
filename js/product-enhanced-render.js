// === Product Enhanced Renderer (V79) ===
// Only uses var and function, no ES6

function renderEnhancedSections(product, lang) {
    if (!product) return '';
    var html = '';
    var isZh = lang === 'zh';
    
    // 1. Application Details Section
    if (product.applicationDetails) {
        html += '<div class="enhanced-section app-details-section">';
        html += '<h3 class="enhanced-title">' + (isZh ? '应用场景' : 'Application Scenarios') + '</h3>';
        html += '<div class="app-details-grid">';
        var apps = product.applications || [];
        for (var i = 0; i < apps.length; i++) {
            var appName = apps[i];
            var appDetail = product.applicationDetails[appName] || '';
            html += '<div class="app-detail-card">';
            html += '<div class="app-detail-icon">' + getAppIcon(i) + '</div>';
            html += '<h4 class="app-detail-name">' + appName + '</h4>';
            html += '<p class="app-detail-desc">' + appDetail + '</p>';
            html += '</div>';
        }
        html += '</div></div>';
    }
    
    // 2. Materials & Coatings Section
    if (product.materials && product.materials.length > 0) {
        html += '<div class="enhanced-section material-section">';
        html += '<h3 class="enhanced-title">' + (isZh ? '可用材料与镀膜' : 'Available Materials & Coatings') + '</h3>';
        html += '<div class="mat-coat-grid">';
        html += '<div class="mat-col">';
        html += '<h4 class="mat-label">' + (isZh ? '材料选项' : 'Materials') + '</h4>';
        html += '<div class="tag-list">';
        for (var m = 0; m < product.materials.length; m++) {
            html += '<span class="mat-tag">' + product.materials[m] + '</span>';
        }
        html += '</div></div>';
        if (product.coatings && product.coatings.length > 0) {
            html += '<div class="mat-col">';
            html += '<h4 class="mat-label">' + (isZh ? '镀膜选项' : 'Coating Options') + '</h4>';
            html += '<div class="tag-list">';
            for (var c = 0; c < product.coatings.length; c++) {
                html += '<span class="coat-tag">' + product.coatings[c] + '</span>';
            }
            html += '</div></div>';
        }
        html += '</div></div>';
    }
    
    // 3. Selection Guide Section
    if (product.selectionGuide) {
        html += '<div class="enhanced-section selection-guide-section">';
        html += '<h3 class="enhanced-title">' + (isZh ? '选型指南' : 'Selection Guide') + '</h3>';
        html += '<div class="selection-guide-card">';
        html += '<div class="sg-icon">&#128161;</div>';
        html += '<p class="sg-text">' + product.selectionGuide + '</p>';
        html += '</div></div>';
    }
    
    // 4. Specifications Summary
    if (product.specifications) {
        html += '<div class="enhanced-section spec-summary-section">';
        html += '<h3 class="enhanced-title">' + (isZh ? '规格概述' : 'Specifications Summary') + '</h3>';
        html += '<p class="spec-summary-text">' + product.specifications + '</p>';
        html += '</div>';
    }
    
    // 5. FAQ Section
    if (product.faq && product.faq.length > 0) {
        html += '<div class="enhanced-section faq-section">';
        html += '<h3 class="enhanced-title">' + (isZh ? '常见问题' : 'Frequently Asked Questions') + '</h3>';
        html += '<div class="faq-list">';
        for (var f = 0; f < product.faq.length; f++) {
            html += '<div class="faq-item" onclick="toggleFaq(this)">';
            html += '<div class="faq-question">';
            html += '<span>' + product.faq[f].question + '</span>';
            html += '<span class="faq-arrow">&#9660;</span>';
            html += '</div>';
            html += '<div class="faq-answer" style="display:none;">';
            html += '<p>' + product.faq[f].answer + '</p>';
            html += '</div></div>';
        }
        html += '</div></div>';
    }
    
    // 6. Related Articles (dynamic from data)
    if (product.relatedArticles && product.relatedArticles.length > 0) {
        html += '<div class="enhanced-section related-articles-section">';
        html += '<h3 class="enhanced-title">' + (isZh ? '相关文章' : 'Related Articles') + '</h3>';
        html += '<div class="related-articles-grid">';
        for (var a = 0; a < product.relatedArticles.length; a++) {
            var blogSlug = product.relatedArticles[a];
            html += '<a href="/blog/' + blogSlug + '/" class="related-art-card">';
            html += '<span class="art-tag">' + (isZh ? '技术指南' : 'Technical Guide') + '</span>';
            html += '<span class="art-link">' + (isZh ? '阅读文章 →' : 'Read Article →') + '</span>';
            html += '</a>';
        }
        html += '</div></div>';
    }
    
    // 7. Related Solutions
    if (product.relatedSolutions && product.relatedSolutions.length > 0) {
        var solNames = {laser: 'Laser', semiconductor: 'Semiconductor', medical: 'Medical', research: 'Research'};
        html += '<div class="enhanced-section related-solutions-section">';
        html += '<h3 class="enhanced-title">' + (isZh ? '相关解决方案' : 'Industry Solutions') + '</h3>';
        html += '<div class="sol-links">';
        for (var s = 0; s < product.relatedSolutions.length; s++) {
            var sol = product.relatedSolutions[s];
            var solName = solNames[sol] || sol;
            html += '<a href="/solutions/#' + sol + '" class="sol-link-btn">';
            html += getSolIcon(sol) + ' ' + solName + ' Solutions';
            html += '</a>';
        }
        html += '</div></div>';
    }
    
    return html;
}

function getAppIcon(index) {
    var icons = ['&#128300;', '&#128187;', '&#10084;', '&#128270;', '&#128218;', '&#128161;', '&#9881;', '&#127760;'];
    return icons[index % icons.length];
}

function getSolIcon(sol) {
    var map = {laser: '&#128300;', semiconductor: '&#128187;', medical: '&#10084;', research: '&#128218;'};
    return map[sol] || '&#9881;';
}

function toggleFaq(el) {
    var answer = el.querySelector('.faq-answer');
    var arrow = el.querySelector('.faq-arrow');
    if (answer.style.display === 'none') {
        answer.style.display = 'block';
        arrow.innerHTML = '&#9650;';
    } else {
        answer.style.display = 'none';
        arrow.innerHTML = '&#9660;';
    }
}
