// PhotonEdge Shopping Cart Logic
// Uses localStorage for persistence

var CART_KEY = 'photonedge_cart';

// Get cart from localStorage
function getCart() {
    var cartData = localStorage.getItem(CART_KEY);
    if (cartData) {
        try {
            return JSON.parse(cartData);
        } catch (e) {
            return [];
        }
    }
    return [];
}

// Save cart to localStorage
function saveCart(cart) {
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
}

// Add item to cart
function addToCart(productId, partNumber, quantity) {
    var cart = getCart();
    var found = false;
    
    for (var i = 0; i < cart.length; i++) {
        if (cart[i].productId === productId && cart[i].partNumber === partNumber) {
            cart[i].quantity = cart[i].quantity + quantity;
            found = true;
            break;
        }
    }
    
    if (!found) {
        cart.push({
            productId: productId,
            partNumber: partNumber || null,
            quantity: quantity || 1,
            addedAt: new Date().toISOString()
        });
    }
    
    saveCart(cart);
    updateCartBadge();
    return true;
}

// Remove item from cart
function removeFromCart(productId, partNumber) {
    var cart = getCart();
    var newCart = [];
    
    for (var i = 0; i < cart.length; i++) {
        if (cart[i].productId !== productId || cart[i].partNumber !== partNumber) {
            newCart.push(cart[i]);
        }
    }
    
    saveCart(newCart);
    updateCartBadge();
}

// Update item quantity
function updateQuantity(productId, partNumber, quantity) {
    var cart = getCart();
    
    for (var i = 0; i < cart.length; i++) {
        if (cart[i].productId === productId && cart[i].partNumber === partNumber) {
            if (quantity <= 0) {
                cart.splice(i, 1);
            } else {
                cart[i].quantity = quantity;
            }
            break;
        }
    }
    
    saveCart(cart);
    updateCartBadge();
}

// Get total item count in cart
function getCartCount() {
    var cart = getCart();
    var count = 0;
    
    for (var i = 0; i < cart.length; i++) {
        count = count + cart[i].quantity;
    }
    
    return count;
}

// Get cart total price
function getCartTotal() {
    var cart = getCart();
    var total = 0;
    
    for (var i = 0; i < cart.length; i++) {
        var productId = cart[i].productId;
        var partNumber = cart[i].partNumber;
        var quantity = cart[i].quantity;
        
        // Find product
        var product = null;
        for (var j = 0; j < PRODUCTS.length; j++) {
            if (PRODUCTS[j].id === productId) {
                product = PRODUCTS[j];
                break;
            }
        }
        
        if (product) {
            var price = product.price;
            
            // Check for part number specific price
            if (partNumber && product.partNumbers) {
                for (var k = 0; k < product.partNumbers.length; k++) {
                    if (product.partNumbers[k].partNumber === partNumber && product.partNumbers[k].price) {
                        price = product.partNumbers[k].price;
                        break;
                    }
                }
            }
            
            total = total + (price * quantity);
        }
    }
    
    return total;
}

// Clear entire cart
function clearCart() {
    localStorage.removeItem(CART_KEY);
    updateCartBadge();
}

// Update cart badge in header
function updateCartBadge() {
    var count = getCartCount();
    var badge = document.getElementById('cartBadge');
    
    if (badge) {
        badge.textContent = count;
        badge.style.display = count > 0 ? 'flex' : 'none';
    }
}

// Show toast notification
function showToast(message) {
    // Remove existing toast if any
    var existingToast = document.querySelector('.toast-notification');
    if (existingToast) {
        existingToast.parentNode.removeChild(existingToast);
    }
    
    // Create toast element
    var toast = document.createElement('div');
    toast.className = 'toast-notification';
    toast.textContent = message;
    
    // Add to body
    document.body.appendChild(toast);
    
    // Trigger animation
    setTimeout(function() {
        toast.classList.add('show');
    }, 10);
    
    // Remove after delay
    setTimeout(function() {
        toast.classList.remove('show');
        setTimeout(function() {
            if (toast.parentNode) {
                toast.parentNode.removeChild(toast);
            }
        }, 300);
    }, 2500);
}

// Get product by ID
function getProductById(productId) {
    for (var i = 0; i < PRODUCTS.length; i++) {
        if (PRODUCTS[i].id === productId) {
            return PRODUCTS[i];
        }
    }
    return null;
}

// Get product price (considering part number)
function getProductPrice(product, partNumber) {
    if (!product) return 0;
    
    if (partNumber && product.partNumbers) {
        for (var i = 0; i < product.partNumbers.length; i++) {
            if (product.partNumbers[i].partNumber === partNumber && product.partNumbers[i].price) {
                return product.partNumbers[i].price;
            }
        }
    }
    
    return product.price || 0;
}

// Format price with currency
function formatPrice(price) {
    return '$' + price.toFixed(2);
}

// Initialize cart badge on page load
document.addEventListener('DOMContentLoaded', function() {
    updateCartBadge();
});
