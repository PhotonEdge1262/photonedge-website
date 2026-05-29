// PhotonEdge Enhanced Site Search v2.0
// Advanced search with fuzzy matching, blog search, application search, and search history

(function() {
    // Search state
    var searchOverlay = null;
    var searchInput = null;
    var searchResults = null;
    var searchIcon = null;
    var isSearchOpen = false;
    var currentLang = "en";
    var searchHistory = [];
    var maxHistoryItems = 5;
    
    // Synonym mapping for common optical terms
    var synonyms = {
        "lens": ["lenses", "lens"],
        "lenses": ["lens", "optical lens"],
        "mirror": ["mirrors", "reflector"],
        "mirrors": ["mirror", "reflector"],
        "window": ["windows", "window"],
        "windows": ["window", "optical window"],
        "prism": ["prisms", "prism"],
        "prisms": ["prism", "optical prism"],
        "filter": ["filters", "filtration"],
        "filters": ["filter", "optical filter"],
        "bk7": ["k9", "bk-7", "b-k7"],
        "k9": ["bk7", "bk-7", "b-k7"],
        "uvfs": ["uv fused silica", "jgs1", "jgs2", "sio2"],
        "fused silica": ["uvfs", "quartz", "jgs1"],
        "quartz": ["fused silica", "jgs1", "uvfs"],
        "znse": ["zinc selenide"],
        "ge": ["germanium"],
        "sio2": ["fused silica", "quartz"],
        "caf2": ["calcium fluoride", "fluorite"],
        "laser": ["lasers", "laser system"],
        "beamsplitter": ["beam splitter", "bs", "beam-splitting"],
        "waveplate": ["wave plates", "retarder", "phase retarder"],
        "polarizer": ["polarizer", "polarising"],
        "ar": ["anti-reflection", "antireflection", "ar coating"],
        "hr": ["high reflectance", "high-reflectance", "hr coating"],
        "nd": ["neutral density", "neutral-density", "nd filter"],
        "cylinder": ["cylindrical", "cylinder lens"],
        "cylindrical": ["cylinder", "cylinder lens"],
        "achromatic": ["achromat", "achromatic doublet", "achromatic lens"],
        "aspheric": ["aspherical", "aspheric lens", "non-spherical"],
        "ball lens": ["ball lenses", "sphere lens", "spherical lens"],
        "rod lens": ["rod lenses", "cylindrical rod"]
    };

    // Initialize search when DOM is ready
    function init() {
        loadSearchHistory();
        createSearchElements();
        bindEvents();
        updateLanguage(window.currentLang || "en");
    }

    // Load search history from localStorage
    function loadSearchHistory() {
        try {
            var saved = localStorage.getItem("photonedge_search_history");
            if (saved) {
                searchHistory = JSON.parse(saved);
            }
        } catch (e) {
            searchHistory = [];
        }
    }

    // Save search history to localStorage
    function saveSearchHistory() {
        try {
            localStorage.setItem("photonedge_search_history", JSON.stringify(searchHistory));
        } catch (e) {
            // Ignore storage errors
        }
    }

    // Add term to search history
    function addToHistory(term) {
        if (!term || term.length < 2) return;
        
        // Remove if already exists
        searchHistory = searchHistory.filter(function(h) {
            return h.toLowerCase() !== term.toLowerCase();
        });
        
        // Add to beginning
        searchHistory.unshift(term);
        
        // Limit size
        if (searchHistory.length > maxHistoryItems) {
            searchHistory = searchHistory.slice(0, maxHistoryItems);
        }
        
        saveSearchHistory();
    }

    // Create search UI elements
    function createSearchElements() {
        // Create overlay
        searchOverlay = document.createElement("div");
        searchOverlay.className = "search-overlay";
        searchOverlay.id = "searchOverlay";
        searchOverlay.innerHTML = 
            '<div class="search-container enhanced-search-container">' +
            '<div class="search-header">' +
            '<div class="search-input-wrapper">' +
            '<svg class="search-icon-svg" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>' +
            '<input type="text" class="search-input enhanced-search-input" id="headerSearchInput" placeholder="Search products, blogs, applications..." autocomplete="off">' +
            '</div>' +
            '<button class="search-close" id="searchCloseBtn">&times;</button>' +
            '</div>' +
            '<div class="search-body">' +
            '<div class="search-categories" id="searchCategories"></div>' +
            '<div class="search-results-container">' +
            '<div class="search-results-section" id="searchResultsProducts" style="display:none;"></div>' +
            '<div class="search-results-section" id="searchResultsBlogs" style="display:none;"></div>' +
            '<div class="search-results-section" id="searchResultsApps" style="display:none;"></div>' +
            '</div>' +
            '<div class="search-history-section" id="searchHistorySection" style="display:none;"></div>' +
            '<div class="search-suggestions" id="searchSuggestions"></div>' +
            '</div>' +
            '</div>';
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
        searchInput.addEventListener("input", debounce(handleSearch, 150));
        
        // Focus event - show history
        searchInput.addEventListener("focus", function() {
            if (searchInput.value.length === 0) {
                showSearchHistory();
            }
        });

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

    // Show search history
    function showSearchHistory() {
        var historySection = document.getElementById("searchHistorySection");
        var resultsContainer = document.querySelector(".search-results-container");
        
        if (searchHistory.length === 0) {
            historySection.style.display = "none";
            return;
        }
        
        var html = '<div class="history-header">';
        html += '<span>' + (currentLang === "zh" ? "搜索历史" : "Recent Searches") + '</span>';
        html += '<button class="clear-history" onclick="clearSearchHistory()">' + 
                (currentLang === "zh" ? "清除" : "Clear") + '</button>';
        html += '</div><div class="history-items">';
        
        searchHistory.forEach(function(term) {
            html += '<div class="history-item" onclick="searchFromHistory(\'' + escapeHtml(term) + '\')">';
            html += '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>';
            html += '<span>' + escapeHtml(term) + '</span></div>';
        });
        
        html += '</div>';
        historySection.innerHTML = html;
        historySection.style.display = "block";
        
        if (resultsContainer) {
            resultsContainer.style.display = "none";
        }
    }

    // Clear search history
    window.clearSearchHistory = function() {
        searchHistory = [];
        saveSearchHistory();
        showSearchHistory();
    };

    // Search from history
    window.searchFromHistory = function(term) {
        searchInput.value = term;
        handleSearch();
    };

    // Open search overlay
    function openSearch() {
        isSearchOpen = true;
        searchOverlay.classList.add("active");
        setTimeout(function() {
            searchInput.focus();
            showSearchHistory();
        }, 100);
    }

    // Close search overlay
    function closeSearch() {
        isSearchOpen = false;
        searchOverlay.classList.remove("active");
        if (searchInput) {
            searchInput.value = "";
            searchInput.placeholder = currentLang === "zh" ? "搜索产品、博客、应用..." : "Search products, blogs, applications...";
        }
        if (searchResults) {
            searchResults.innerHTML = "";
        }
    }

    // Handle search input
    function handleSearch() {
        var query = searchInput.value.trim();
        var historySection = document.getElementById("searchHistorySection");
        
        if (query.length < 2) {
            if (historySection) {
                showSearchHistory();
            }
            return;
        }
        
        if (historySection) {
            historySection.style.display = "none";
        }
        
        var results = performSearch(query);
        displayResults(results, query);
        showSuggestions(query);
        
        // Add to history if valid search
        if (query.length >= 3) {
            addToHistory(query);
        }
    }

    // Show search suggestions
    function showSuggestions(query) {
        var suggestionsContainer = document.getElementById("searchSuggestions");
        if (!suggestionsContainer) return;
        
        var popularTerms = ["lens", "mirror", "filter", "prism", "beamsplitter", "waveplate", "laser", "AR coating", "BK7", "fused silica"];
        var queryLower = query.toLowerCase();
        
        var matches = popularTerms.filter(function(term) {
            return term.toLowerCase().indexOf(queryLower) !== -1;
        }).slice(0, 4);
        
        if (matches.length === 0) {
            suggestionsContainer.innerHTML = '';
            return;
        }
        
        var html = '<div class="suggestions-label">' + 
                   (currentLang === "zh" ? "热门搜索" : "Popular Searches") + '</div>';
        
        matches.forEach(function(term) {
            html += '<div class="suggestion-item" onclick="applySuggestion(\'' + escapeHtml(term) + '\')">' + 
                    escapeHtml(term) + '</div>';
        });
        
        suggestionsContainer.innerHTML = html;
    }

    window.applySuggestion = function(term) {
        searchInput.value = term;
        handleSearch();
    };

    // Expand query with synonyms
    function expandWithSynonyms(query) {
        var expanded = [query.toLowerCase()];
        var queryLower = query.toLowerCase();
        
        for (var key in synonyms) {
            if (queryLower.indexOf(key) !== -1) {
                synonyms[key].forEach(function(syn) {
                    if (expanded.indexOf(syn) === -1) {
                        expanded.push(syn);
                    }
                });
            }
        }
        
        // Handle common variations
        if (queryLower.endsWith("s")) {
            expanded.push(queryLower.slice(0, -1));
        } else {
            expanded.push(queryLower + "s");
        }
        
        return expanded;
    }

    // Fuzzy match helper - checks if query matches with tolerance
    function fuzzyMatch(text, query) {
        if (!text) return false;
        text = text.toLowerCase();
        query = query.toLowerCase();
        
        // Exact contains
        if (text.indexOf(query) !== -1) return true;
        
        // Fuzzy threshold matching
        var threshold = 0.6;
        var distance = levenshteinDistance(text, query);
        var maxLen = Math.max(text.length, query.length);
        
        return (1 - distance / maxLen) >= threshold;
    }

    // Levenshtein distance calculation
    function levenshteinDistance(a, b) {
        if (a.length === 0) return b.length;
        if (b.length === 0) return a.length;
        
        var matrix = [];
        
        for (var i = 0; i <= b.length; i++) {
            matrix[i] = [i];
        }
        
        for (var j = 0; j <= a.length; j++) {
            matrix[0][j] = j;
        }
        
        for (var i = 1; i <= b.length; i++) {
            for (var j = 1; j <= a.length; j++) {
                if (b.charAt(i - 1) === a.charAt(j - 1)) {
                    matrix[i][j] = matrix[i - 1][j - 1];
                } else {
                    matrix[i][j] = Math.min(
                        matrix[i - 1][j - 1] + 1,
                        matrix[i][j - 1] + 1,
                        matrix[i - 1][j] + 1
                    );
                }
            }
        }
        
        return matrix[b.length][a.length];
    }

    // Perform comprehensive search across products, blogs, and applications
    function performSearch(query) {
        var results = {
            products: [],
            blogs: [],
            applications: []
        };
        
        var expandedQueries = expandWithSynonyms(query);
        var queryLower = query.toLowerCase();
        
        // Search Products
        if (typeof PRODUCTS !== "undefined" && PRODUCTS) {
            results.products = searchProducts(PRODUCTS, expandedQueries, queryLower);
        }
        
        // Search Blogs
        if (typeof BLOG_POSTS !== "undefined" && BLOG_POSTS) {
            results.blogs = searchBlogs(BLOG_POSTS, expandedQueries, queryLower);
        }
        
        // Search Applications
        results.applications = searchApplications(expandedQueries, queryLower);
        
        return results;
    }

    // Search products with enhanced matching
    function searchProducts(products, expandedQueries, queryLower) {
        var results = [];
        var maxResults = 6;
        
        for (var i = 0; i < products.length; i++) {
            var product = products[i];
            var score = 0;
            var matchDetails = [];
            
            // Search in name (English) - highest weight
            if (product.name) {
                var nameLower = product.name.toLowerCase();
                expandedQueries.forEach(function(eq) {
                    if (nameLower.indexOf(eq) !== -1) {
                        score += 10;
                        if (nameLower.indexOf(eq) === 0) {
                            score += 5;
                        }
                        matchDetails.push("name");
                    }
                });
                // Fuzzy match
                if (score === 0 && fuzzyMatch(product.name, queryLower)) {
                    score += 6;
                    matchDetails.push("name_fuzzy");
                }
            }
            
            // Search in name (Chinese)
            if (product.nameZh) {
                expandedQueries.forEach(function(eq) {
                    if (product.nameZh.indexOf(eq) !== -1 || product.nameZh.indexOf(queryLower) !== -1) {
                        score += 8;
                        matchDetails.push("nameZh");
                    }
                });
            }
            
            // Search in category
            if (product.category) {
                expandedQueries.forEach(function(eq) {
                    if (product.category.toLowerCase().indexOf(eq) !== -1) {
                        score += 3;
                        matchDetails.push("category");
                    }
                });
            }
            
            if (product.categoryZh) {
                expandedQueries.forEach(function(eq) {
                    if (product.categoryZh.indexOf(eq) !== -1) {
                        score += 3;
                        matchDetails.push("categoryZh");
                    }
                });
            }
            
            // Search in description
            if (product.description) {
                expandedQueries.forEach(function(eq) {
                    if (product.description.toLowerCase().indexOf(eq) !== -1) {
                        score += 2;
                        matchDetails.push("description");
                    }
                });
            }
            
            // Search in parameters
            if (product.parameters) {
                var paramStr = JSON.stringify(product.parameters).toLowerCase();
                expandedQueries.forEach(function(eq) {
                    if (paramStr.indexOf(eq) !== -1) {
                        score += 2;
                        matchDetails.push("parameters");
                    }
                });
            }
            
            // Search in part numbers
            if (product.partNumbers) {
                for (var j = 0; j < product.partNumbers.length; j++) {
                    var pn = product.partNumbers[j];
                    if (pn.partNumber && pn.partNumber.toLowerCase().indexOf(queryLower) !== -1) {
                        score += 6;
                        matchDetails.push("partNumber");
                        break;
                    }
                }
            }
            
            if (score > 0) {
                results.push({
                    product: product,
                    score: score,
                    matchDetails: matchDetails
                });
            }
        }
        
        // Sort by score descending
        results.sort(function(a, b) {
            return b.score - a.score;
        });
        
        return results.slice(0, maxResults);
    }

    // Search blog posts
    function searchBlogs(blogs, expandedQueries, queryLower) {
        var results = [];
        var maxResults = 4;
        
        for (var i = 0; i < blogs.length; i++) {
            var blog = blogs[i];
            var score = 0;
            
            // Search in title
            if (blog.title) {
                expandedQueries.forEach(function(eq) {
                    if (blog.title.toLowerCase().indexOf(eq) !== -1) {
                        score += 10;
                    }
                });
                if (fuzzyMatch(blog.title, queryLower)) {
                    score += 6;
                }
            }
            
            // Search in excerpt
            if (blog.excerpt) {
                expandedQueries.forEach(function(eq) {
                    if (blog.excerpt.toLowerCase().indexOf(eq) !== -1) {
                        score += 3;
                    }
                });
            }
            
            // Search in category
            if (blog.category) {
                expandedQueries.forEach(function(eq) {
                    if (blog.category.toLowerCase().indexOf(eq) !== -1) {
                        score += 2;
                    }
                });
            }
            
            if (score > 0) {
                results.push({
                    blog: blog,
                    score: score
                });
            }
        }
        
        results.sort(function(a, b) {
            return b.score - a.score;
        });
        
        return results.slice(0, maxResults);
    }

    // Search application scenarios
    function searchApplications(expandedQueries, queryLower) {
        var results = [];
        var maxResults = 3;
        
        // Application data
        var applications = [
            { id: "laser", title: "Laser Systems", titleZh: "激光系统", keywords: ["laser", "laser cutting", "laser marking", "laser welding", "co2 laser", "fiber laser", "nd:yag"] },
            { id: "medical", title: "Medical Devices", titleZh: "医疗设备", keywords: ["medical", "endoscopy", "surgical", "diagnostic", "microscopy", "ophthalmic"] },
            { id: "semiconductor", title: "Semiconductor", titleZh: "半导体", keywords: ["semiconductor", "lithography", "ic", "chip", "wafer", "inspection"] },
            { id: "telecom", title: "Telecommunications", titleZh: "光通信", keywords: ["telecom", "fiber", "optical communication", "datacom", "network"] },
            { id: "defense", title: "Defense & Aerospace", titleZh: "国防航空", keywords: ["defense", "military", "aerospace", "targeting", "surveillance", "navigation"] },
            { id: "research", title: "Research & Education", titleZh: "科研教育", keywords: ["research", "laboratory", "university", "spectroscopy", "interferometry"] },
            { id: "industrial", title: "Industrial Imaging", titleZh: "工业成像", keywords: ["machine vision", "inspection", "quality control", "automation", "robotics"] },
            { id: "imaging", title: "Optical Imaging", titleZh: "光学成像", keywords: ["camera", "lens", "imaging", "photography", "telescope"] }
        ];
        
        for (var i = 0; i < applications.length; i++) {
            var app = applications[i];
            var score = 0;
            
            expandedQueries.forEach(function(eq) {
                if (app.title.toLowerCase().indexOf(eq) !== -1) {
                    score += 8;
                }
                if (app.titleZh.indexOf(eq) !== -1) {
                    score += 8;
                }
                app.keywords.forEach(function(kw) {
                    if (kw.indexOf(eq) !== -1) {
                        score += 3;
                    }
                });
            });
            
            if (fuzzyMatch(app.title, queryLower) || fuzzyMatch(app.keywords.join(" "), queryLower)) {
                score += 5;
            }
            
            if (score > 0) {
                results.push({
                    application: app,
                    score: score
                });
            }
        }
        
        results.sort(function(a, b) {
            return b.score - a.score;
        });
        
        return results.slice(0, maxResults);
    }

    // Display search results with categories
    function displayResults(results, query) {
        var productsSection = document.getElementById("searchResultsProducts");
        var blogsSection = document.getElementById("searchResultsBlogs");
        var appsSection = document.getElementById("searchResultsApps");
        var categoriesSection = document.getElementById("searchCategories");
        var resultsContainer = document.querySelector(".search-results-container");
        var suggestionsSection = document.getElementById("searchSuggestions");
        
        if (suggestionsSection) suggestionsSection.innerHTML = '';
        
        if (!results.products.length && !results.blogs.length && !results.applications.length) {
            resultsContainer.style.display = "none";
            categoriesSection.innerHTML = '<div class="no-results">' + 
                (currentLang === "zh" ? "未找到结果，试试其他关键词？" : "No results found. Try different keywords?") + 
                '</div>';
            categoriesSection.style.display = "block";
            return;
        }
        
        categoriesSection.style.display = "none";
        resultsContainer.style.display = "block";
        
        var html = '';
        
        // Products section
        if (results.products.length > 0) {
            html = '<div class="results-category-header">';
            html += '<span>' + (currentLang === "zh" ? "产品" : "Products") + '</span>';
            html += '<a href="products.html?search=' + encodeURIComponent(query) + '" class="view-all-link" onclick="closeHeaderSearch()">' + 
                    (currentLang === "zh" ? "查看全部" : "View All") + '</a>';
            html += '</div>';
            
            results.products.forEach(function(item) {
                var product = item.product;
                var productName = currentLang === "zh" && product.nameZh ? product.nameZh : product.name;
                var categoryName = currentLang === "zh" && product.categoryZh ? product.categoryZh : product.category;
                
                html += '<a href="products/' + product.slug + '" class="search-result-item" onclick="closeHeaderSearch()">';
                html += '<div class="search-result-image">';
                if (product.image) {
                    html += '<img src="' + product.image + '" alt="' + escapeHtml(productName) + '">';
                } else {
                    html += '<div class="search-result-placeholder">&#128269;</div>';
                }
                html += '</div>';
                html += '<div class="search-result-info">';
                html += '<div class="search-result-name">' + highlightMatch(productName, query) + '</div>';
                html += '<div class="search-result-category">' + escapeHtml(categoryName) + '</div>';
                if (product.price) {
                    html += '<div class="search-result-price">$' + product.price + ' <span class="price-note">' + 
                            (currentLang === "zh" ? "起" : "from") + '</span></div>';
                }
                html += '</div></a>';
            });
            
            productsSection.innerHTML = html;
            productsSection.style.display = "block";
        } else {
            productsSection.style.display = "none";
        }
        
        // Blogs section
        if (results.blogs.length > 0) {
            html = '<div class="results-category-header">';
            html += '<span>' + (currentLang === "zh" ? "技术博客" : "Blog Articles") + '</span>';
            html += '<a href="blog.html?search=' + encodeURIComponent(query) + '" class="view-all-link" onclick="closeHeaderSearch()">' + 
                    (currentLang === "zh" ? "查看全部" : "View All") + '</a>';
            html += '</div>';
            
            results.blogs.forEach(function(item) {
                var blog = item.blog;
                var blogUrl = 'blog/' + blog.slug + '/index.html';
                
                html += '<a href="' + blogUrl + '" class="search-result-item blog-result" onclick="closeHeaderSearch()">';
                html += '<div class="search-result-icon blog-icon">&#128214;</div>';
                html += '<div class="search-result-info">';
                html += '<div class="search-result-name">' + highlightMatch(blog.title, query) + '</div>';
                html += '<div class="search-result-category">' + escapeHtml(blog.category) + ' · ' + blog.readTime + '</div>';
                html += '</div></a>';
            });
            
            blogsSection.innerHTML = html;
            blogsSection.style.display = "block";
        } else {
            blogsSection.style.display = "none";
        }
        
        // Applications section
        if (results.applications.length > 0) {
            html = '<div class="results-category-header">';
            html += '<span>' + (currentLang === "zh" ? "应用领域" : "Applications") + '</span>';
            html += '<a href="applications.html" class="view-all-link" onclick="closeHeaderSearch()">' + 
                    (currentLang === "zh" ? "查看全部" : "View All") + '</a>';
            html += '</div>';
            
            results.applications.forEach(function(item) {
                var app = item.application;
                var appTitle = currentLang === "zh" ? app.titleZh : app.title;
                
                html += '<a href="applications.html#' + app.id + '" class="search-result-item app-result" onclick="closeHeaderSearch()">';
                html += '<div class="search-result-icon app-icon">&#9883;</div>';
                html += '<div class="search-result-info">';
                html += '<div class="search-result-name">' + highlightMatch(appTitle, query) + '</div>';
                html += '<div class="search-result-category">' + (currentLang === "zh" ? "应用领域" : "Application") + '</div>';
                html += '</div></a>';
            });
            
            appsSection.innerHTML = html;
            appsSection.style.display = "block";
        } else {
            appsSection.style.display = "none";
        }
    }

    // Highlight matching text
    function highlightMatch(text, query) {
        if (!text || !query) return escapeHtml(text);
        
        var regex = new RegExp('(' + escapeRegex(query) + ')', 'gi');
        return escapeHtml(text).replace(regex, '<mark class="search-highlight">$1</mark>');
    }

    // Escape HTML
    function escapeHtml(text) {
        if (!text) return '';
        var div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Escape regex special characters
    function escapeRegex(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    // Update language strings
    function updateLanguage(lang) {
        currentLang = lang;
        if (searchInput) {
            searchInput.placeholder = lang === "zh" ? "搜索产品、博客、应用..." : "Search products, blogs, applications...";
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
