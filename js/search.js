// PhotonEdge Site Search
// Real-time product search functionality

(function() {
    // Search state
    var searchOverlay = null;
    var searchInput = null;
    var searchResults = null;
    var searchIcon = null;
    var isSearchOpen = false;
    var currentLang = "en";

    // Initialize search when DOM is ready
    function init() {
        createSearchElements();
        bindEvents();
        updateLanguage(window.currentLang || "en");
    }

    // Create search UI elements
    function createSearchElements() {
        // Create overlay
        searchOverlay = document.createElement("div");
        searchOverlay.className = "search-overlay";
        searchOverlay.id = "searchOverlay";
        searchOverlay.innerHTML = '<div class="search-container"><div class="search-header"><input type="text" class="search-input" id="headerSearchInput" placeholder="Search products..." autocomplete="off"><button class="search-close" id="searchCloseBtn">&times;</button></div><div class="search-results" id="headerSearchResults"></div></div>';
        document.body.appendChild(searchOverlay);

        // Get references
        searchInput = document.getElementById("headerSearchInput");
        searchResults = document.getElementById("headerSearchResults");

        // Add search icon to header
        var nav = document.querySelector(".nav");
        if (nav) {
            searchIcon = document.createElement("a");
            searchIcon.href = "javascript:void(0)";
            searchIcon.className = "search-icon";
            searchIcon.id = "headerSearchIcon";
            searchIcon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>';
            searchIcon.onclick = openSearch;
            
            // Insert before cart icon
            var cartIcon = nav.querySelector(".cart-icon");
            if (cartIcon) {
                nav.insertBefore(searchIcon, cartIcon);
            } else {
                nav.appendChild(searchIcon);
            }
        }
    }

    // Bind event listeners
    function bindEvents() {
        // Search overlay click handlers
        searchOverlay.addEventListener("click", function(e) {
            if (e.target === searchOverlay || e.target.classList.contains("search-container")) {
                closeSearch();
            }
        });

        // Close button
        var closeBtn = document.getElementById("searchCloseBtn");
        if (closeBtn) {
            closeBtn.addEventListener("click", closeSearch);
        }

        // Search input handler
        searchInput.addEventListener("input", debounce(handleSearch, 200));

        // Keyboard events
        document.addEventListener("keydown", function(e) {
            if (e.key === "Escape" && isSearchOpen) {
                closeSearch();
            }
            // Open search with Ctrl/Cmd + K
            if ((e.ctrlKey || e.metaKey) && e.key === "k") {
                e.preventDefault();
                openSearch();
            }
        });

        // Language change listener
        document.addEventListener("languageChange", function(e) {
            updateLanguage(e.detail.lang);
        });
    }

    // Open search overlay
    function openSearch() {
        isSearchOpen = true;
        searchOverlay.classList.add("active");
        setTimeout(function() {
            searchInput.focus();
        }, 100);
    }

    // Close search overlay
    function closeSearch() {
        isSearchOpen = false;
        searchOverlay.classList.remove("active");
        if (searchInput) {
            searchInput.value = "";
            searchInput.placeholder = currentLang === "zh" ? "搜索产品..." : "Search products...";
        }
        if (searchResults) {
            searchResults.innerHTML = "";
        }
    }

    // Handle search input
    function handleSearch() {
        var query = searchInput.value.trim();
        
        if (query.length < 3) {
            searchResults.innerHTML = '<div class="search-hint">' + (currentLang === "zh" ? "输入至少3个字符开始搜索" : "Enter at least 3 characters to search") + '</div>';
            return;
        }

        var results = performSearch(query);
        displayResults(results, query);
    }

    // Perform search across products
    function performSearch(query) {
        var results = [];
        var queryLower = query.toLowerCase();
        var maxResults = 8;

        if (typeof PRODUCTS === "undefined" || !PRODUCTS) {
            return results;
        }

        for (var i = 0; i < PRODUCTS.length; i++) {
            var product = PRODUCTS[i];
            var score = 0;

            // Search in name (English)
            if (product.name && product.name.toLowerCase().indexOf(queryLower) !== -1) {
                score += 10;
                if (product.name.toLowerCase().indexOf(queryLower) === 0) {
                    score += 5; // Bonus for starts with
                }
            }

            // Search in name (Chinese)
            if (product.nameZh && product.nameZh.indexOf(query) !== -1) {
                score += 8;
            }

            // Search in category
            if (product.category && product.category.toLowerCase().indexOf(queryLower) !== -1) {
                score += 3;
            }
            if (product.categoryZh && product.categoryZh.indexOf(query) !== -1) {
                score += 3;
            }

            // Search in part numbers
            if (product.partNumbers) {
                for (var j = 0; j < product.partNumbers.length; j++) {
                    var pn = product.partNumbers[j];
                    if (pn.partNumber && pn.partNumber.toLowerCase().indexOf(queryLower) !== -1) {
                        score += 6;
                        break;
                    }
                }
            }

            if (score > 0) {
                results.push({
                    product: product,
                    score: score
                });
            }
        }

        // Sort by score descending
        results.sort(function(a, b) {
            return b.score - a.score;
        });

        // Limit to max results
        return results.slice(0, maxResults);
    }

    // Display search results
    function displayResults(results, query) {
        if (results.length === 0) {
            searchResults.innerHTML = '<div class="search-no-results">' + 
                (currentLang === "zh" ? "未找到产品" : "No products found") + 
                '</div>';
            return;
        }

        var html = "";
        var productUrlBase = window.location.protocol + "//" + window.location.host;

        for (var i = 0; i < results.length; i++) {
            var item = results[i];
            var product = item.product;
            var productUrl = productUrlBase + "/products/" + product.slug;
            var productName = currentLang === "zh" && product.nameZh ? product.nameZh : product.name;
            var categoryName = currentLang === "zh" && product.categoryZh ? product.categoryZh : product.category;

            html += '<a href="' + productUrl + '" class="search-result-item" onclick="closeHeaderSearch()">';
            html += '<div class="search-result-image">';
            if (product.image) {
                html += '<img src="' + product.image + '" alt="' + productName + '">';
            } else {
                html += '<div class="search-result-placeholder">&#128269;</div>';
            }
            html += '</div>';
            html += '<div class="search-result-info">';
            html += '<div class="search-result-name">' + productName + '</div>';
            html += '<div class="search-result-category">' + categoryName + '</div>';
            html += '</div>';
            html += '</a>';
        }

        // Add "View all results" link
        html += '<a href="products.html?search=' + encodeURIComponent(query) + '" class="search-view-all" onclick="closeHeaderSearch()">';
        html += (currentLang === "zh" ? "查看全部结果" : "View all results") + ' &rarr;</a>';

        searchResults.innerHTML = html;
    }

    // Update language strings
    function updateLanguage(lang) {
        currentLang = lang;
        if (searchInput) {
            searchInput.placeholder = lang === "zh" ? "搜索产品..." : "Search products...";
        }
    }

    // Debounce helper
    function debounce(func, wait) {
        var timeout;
        return function() {
            var context = this;
            var args = arguments;
            clearTimeout(timeout);
            timeout = setTimeout(function() {
                func.apply(context, args);
            }, wait);
        };
    }

    // Global function to close search (called from result links)
    window.closeHeaderSearch = closeSearch;

    // Listen for language changes
    if (typeof window.setLanguage === "function") {
        var originalSetLanguage = window.setLanguage;
        window.setLanguage = function(lang) {
            originalSetLanguage(lang);
            document.dispatchEvent(new CustomEvent("languageChange", { detail: { lang: lang } }));
        };
    }

    // Initialize when DOM is ready
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})();
