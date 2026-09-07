// ============================================================
// Products 3.1 Filter & Render
// ES5 compatible
// Data structure note: material, wavelength, wavelengthRange,
//   application, coating are arrays in products-data.js (3.1 format)
// ============================================================

(function() {
    var grid = document.getElementById('product-grid');
    var visibleCountEl = document.getElementById('visible-count');
    var totalCountEl = document.getElementById('total-count');
    var noResultsEl = document.getElementById('no-results');
    var totalProducts = typeof PRODUCTS !== 'undefined' ? PRODUCTS.length : 0;

    totalCountEl.textContent = totalProducts;

    function getQueryParam(name) {
        var url = window.location.href;
        name = name.replace(/[\[\]]/g, '\\$&');
        var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)');
        var results = regex.exec(url);
        if (!results) return '';
        if (!results[2]) return '';
        return decodeURIComponent(results[2].replace(/\+/g, ' '));
    }

    function getFilters() {
        return {
            component: document.getElementById('filter-component').value,
            material: document.getElementById('filter-material').value,
            wavelength: document.getElementById('filter-wavelength').value,
            application: document.getElementById('filter-application').value,
            coating: document.getElementById('filter-coating').value,
            search: document.getElementById('filter-search').value.toLowerCase()
        };
    }

    function arrContains(arr, val) {
        if (!arr || !arr.length) return false;
        for (var i = 0; i < arr.length; i++) {
            if (String(arr[i]).indexOf(val) !== -1) return true;
            if (val.indexOf(String(arr[i])) !== -1) return true;
        }
        return false;
    }

    function matchWavelength(wlArr, wlRangeArr, filterWL) {
        if (!filterWL) return true;
        var nmRanges = {
            'UV (190-400nm)': [190, 400],
            'Visible (400-700nm)': [400, 700],
            'NIR (700-1700nm)': [700, 1700],
            'SWIR (1.7-3µm)': [1700, 3000],
            'MWIR (3-5µm)': [3000, 5000],
            'LWIR (8-14µm)': [8000, 14000]
        };

        var bucket = nmRanges[filterWL];
        if (!bucket) return true;

        // Check by wavelength label array (UV, Visible, NIR, etc.)
        if (wlArr && wlArr.length) {
            for (var i = 0; i < wlArr.length; i++) {
                var wl = String(wlArr[i]).toLowerCase();
                if (wl.indexOf('uv') !== -1 && filterWL.indexOf('UV') === 0) return true;
                if (wl.indexOf('visible') !== -1 && filterWL.indexOf('Visible') === 0) return true;
                if (wl.indexOf('nir') !== -1 && filterWL.indexOf('NIR') === 0) return true;
                if (wl.indexOf('swir') !== -1 && filterWL.indexOf('SWIR') === 0) return true;
                if (wl.indexOf('mwir') !== -1 && filterWL.indexOf('MWIR') === 0) return true;
                if (wl.indexOf('lwir') !== -1 && filterWL.indexOf('LWIR') === 0) return true;
            }
        }

        // Check by numeric wavelength range array
        if (wlRangeArr && wlRangeArr.length >= 2) {
            var low = parseFloat(wlRangeArr[0]);
            var high = parseFloat(wlRangeArr[wlRangeArr.length - 1]);
            if (!isNaN(low) && !isNaN(high)) {
                return low <= bucket[1] && high >= bucket[0];
            }
        }

        return true; // don't filter if can't parse
    }

    function matchCoating(coatArr, filterCoating) {
        if (!filterCoating) return true;
        if (!coatArr || !coatArr.length) return false;
        var pc = '';
        for (var i = 0; i < coatArr.length; i++) {
            pc += ' ' + String(coatArr[i]).toLowerCase();
        }
        switch(filterCoating) {
            case 'AR Coating':
                return pc.indexOf('ar ') !== -1 || pc.indexOf('ar,') !== -1 || pc.indexOf('anti-reflection') !== -1 || pc.indexOf('bbar') !== -1;
            case 'HR Coating':
                return pc.indexOf('hr ') !== -1 || pc.indexOf('high ref') !== -1 || pc.indexOf('hr,') !== -1;
            case 'Protected Metal':
                return pc.indexOf('protected') !== -1 || pc.indexOf('enhanced al') !== -1;
            case 'Narrow Band':
                return pc.indexOf('narrow') !== -1 || pc.indexOf('bandpass') !== -1;
            case 'Beamsplitter':
                return pc.indexOf('bs') !== -1 || pc.indexOf('beamsplitter') !== -1 || pc.indexOf('split') !== -1 || pc.indexOf('polarizing') !== -1;
            case 'Uncoated':
                return pc.indexOf('uncoated') !== -1;
            case 'Custom':
                return pc.indexOf('custom') !== -1;
            default:
                return true;
        }
    }

    function filterProducts(filters) {
        if (typeof PRODUCTS === 'undefined') return [];
        var results = [];

        for (var i = 0; i < PRODUCTS.length; i++) {
            var p = PRODUCTS[i];

            if (filters.component) {
                if ((p.componentType || '') !== filters.component) {
                    continue;
                }
            }

            if (filters.material) {
                if (!arrContains(p.material, filters.material)) {
                    continue;
                }
            }

            if (filters.wavelength) {
                if (!matchWavelength(p.wavelength, p.wavelengthRange, filters.wavelength)) {
                    continue;
                }
            }

            if (filters.application) {
                if (!arrContains(p.application, filters.application)) {
                    continue;
                }
            }

            if (filters.coating) {
                if (!matchCoating(p.coating, filters.coating)) {
                    continue;
                }
            }

            if (filters.search) {
                var searchTarget = (p.name + ' ' + (p.description || '') + ' ' + (p.material ? p.material.join(' ') : '') + ' ' + (p.category || '')).toLowerCase();
                if (searchTarget.indexOf(filters.search) === -1) {
                    continue;
                }
            }

            results.push(p);
        }

        return results;
    }

    function displayVal(arrOrStr, maxLen) {
        if (!arrOrStr) return 'N/A';
        if (Array.isArray(arrOrStr)) {
            var s = arrOrStr.join(', ');
        } else {
            s = String(arrOrStr);
        }
        if (maxLen && s.length > maxLen) {
            s = s.substring(0, maxLen) + '...';
        }
        return s;
    }

    function renderProducts(products) {
        var html = '';
        for (var i = 0; i < products.length; i++) {
            var p = products[i];
            var img = '/' + (p.image || 'images/logo.png');
            var mat = displayVal(p.material, 40);
            var wl = displayVal(p.wavelength, 35);
            var coat = displayVal(p.coating, 40);
            var app = displayVal(p.application, 30);

            html += '<div class="p31-product-card" onclick="window.location.href=\'/products/' + p.slug + '/\'">' +
                '<div class="p31-product-img">' +
                    '<img src="' + img + '" alt="' + p.name + '" loading="lazy">' +
                '</div>' +
                '<div class="p31-product-body">' +
                    '<h4 class="p31-product-name">' + p.name + '</h4>' +
                    '<div class="p31-product-specs">' +
                        '<div class="p31-spec-row"><span class="p31-spec-label">Material</span><span class="p31-spec-value">' + mat + '</span></div>' +
                        '<div class="p31-spec-row"><span class="p31-spec-label">Wavelength</span><span class="p31-spec-value">' + wl + '</span></div>' +
                        '<div class="p31-spec-row"><span class="p31-spec-label">Coating</span><span class="p31-spec-value">' + coat + '</span></div>' +
                        '<div class="p31-spec-row"><span class="p31-spec-label">Application</span><span class="p31-spec-value">' + app + '</span></div>' +
                    '</div>' +
                    '<a href="/products/' + p.slug + '/" class="p31-product-btn" onclick="event.stopPropagation()">View Product &rarr;</a>' +
                '</div>' +
            '</div>';
        }
        return html;
    }

    window.applyFilters = function() {
        var filters = getFilters();
        var results = filterProducts(filters);
        visibleCountEl.textContent = results.length;

        if (results.length === 0) {
            grid.innerHTML = '';
            noResultsEl.style.display = 'block';
        } else {
            noResultsEl.style.display = 'none';
            grid.innerHTML = renderProducts(results);
        }
    };

    window.resetFilters = function() {
        document.getElementById('filter-component').value = '';
        document.getElementById('filter-material').value = '';
        document.getElementById('filter-wavelength').value = '';
        document.getElementById('filter-application').value = '';
        document.getElementById('filter-coating').value = '';
        document.getElementById('filter-search').value = '';
        applyFilters();
    };

    function initFromURL() {
        var component = getQueryParam('component');
        var category = getQueryParam('category');

        if (component) {
            document.getElementById('filter-component').value = component;
        } else if (category) {
            var catMap = {
                'Optical Lenses': 'Lens',
                'Optical Windows': 'Window',
                'Optical Mirrors': 'Mirror',
                'Optical Filters': 'Filter',
                'Optical Prisms': 'Prism',
                'Waveplates & Polarizers': 'Waveplate',
                'Optical Beamsplitters': 'Beamsplitter',
                'Optical Wave Plates': 'Waveplate',
                'Optical Polarizers': 'Polarizer'
            };
            if (catMap[category]) {
                document.getElementById('filter-component').value = catMap[category];
            }
        }

        var material = getQueryParam('material');
        if (material) document.getElementById('filter-material').value = material;

        var wavelength = getQueryParam('wavelength');
        if (wavelength) document.getElementById('filter-wavelength').value = wavelength;

        var application = getQueryParam('application');
        if (application) document.getElementById('filter-application').value = application;

        var coating = getQueryParam('coating');
        if (coating) document.getElementById('filter-coating').value = coating;

        var q = getQueryParam('q');
        if (q) document.getElementById('filter-search').value = q;

        applyFilters();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initFromURL);
    } else {
        initFromURL();
    }
})();
