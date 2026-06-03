// 产品对比功能核心模块
var COMPARE_KEY = 'photonedge_compare';
var MAX_COMPARE = 3;

// 获取对比列表
function getCompareList() {
    try {
        var data = localStorage.getItem(COMPARE_KEY);
        return data ? JSON.parse(data) : [];
    } catch (e) {
        return [];
    }
}

// 保存对比列表
function saveCompareList(list) {
    localStorage.setItem(COMPARE_KEY, JSON.stringify(list));
    updateCompareBadge();
}

// 添加产品到对比
function addToCompare(productId) {
    var list = getCompareList();
    
    // 检查是否已存在
    if (list.indexOf(productId) !== -1) {
        return true; // 已存在，也算成功
    }
    
    // 检查数量限制
    if (list.length >= MAX_COMPARE) {
        alert('最多只能对比 ' + MAX_COMPARE + ' 个产品');
        return false;
    }
    
    list.push(productId);
    saveCompareList(list);
    return true;
}

// 从对比中移除产品
function removeFromCompare(productId) {
    var list = getCompareList();
    var index = list.indexOf(productId);
    if (index !== -1) {
        list.splice(index, 1);
        saveCompareList(list);
    }
    return true;
}

// 检查产品是否在对比中
function isInCompare(productId) {
    var list = getCompareList();
    return list.indexOf(productId) !== -1;
}

// 清空对比列表
function clearCompare() {
    saveCompareList([]);
}

// 获取对比数量
function getCompareCount() {
    return getCompareList().length;
}

// 更新对比按钮badge
function updateCompareBadge() {
    var badge = document.getElementById('compareBadge');
    if (badge) {
        var count = getCompareCount();
        badge.textContent = count;
        badge.style.display = count > 0 ? 'inline-block' : 'none';
    }
    
    // 更新所有产品卡片的对比按钮状态
    updateAllCompareButtons();
}

// 更新所有产品卡片的对比按钮状态
function updateAllCompareButtons() {
    var buttons = document.querySelectorAll('.compare-btn');
    buttons.forEach(function(btn) {
        var productId = parseInt(btn.dataset.productId);
        if (isInCompare(productId)) {
            btn.classList.add('active');
            btn.innerHTML = '✓';
        } else {
            btn.classList.remove('active');
            var lang = getCurrentLang();
            btn.innerHTML = lang === 'zh' ? '对比' : 'Compare';
        }
    });
}

// 切换对比状态
function toggleCompare(productId, name) {
    if (isInCompare(productId)) {
        removeFromCompare(productId);
        return false;
    } else {
        var success = addToCompare(productId);
        if (success) {
            var list = getCompareList();
            if (list.length >= MAX_COMPARE) {
                var lang = getCurrentLang();
                var msg = lang === 'zh' 
                    ? '已选择最多产品，现在就去对比？' 
                    : 'Max products selected. Go to compare now?';
                if (confirm(msg)) {
                    window.location.href = 'compare.html';
                }
            }
        }
        return success;
    }
}

// 页面加载时更新badge
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateCompareBadge);
} else {
    setTimeout(updateCompareBadge, 100);
}
