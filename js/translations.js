// PhotonEdge Translations
// 中英文翻译文件

const translations = {
  // 页面标题
  "page_title": {
    "en": "PhotonEdge - Optical Components & Precision Optics",
    "zh": "北京恒鼎光科技 - 光学元件与精密光学"
  },
  
  // 导航
  "nav": {
    "home": { "en": "Home", "zh": "首页" },
    "products": { "en": "Products", "zh": "产品中心" },
    "about": { "en": "About Us", "zh": "关于我们" },
    "contact": { "en": "Contact", "zh": "联系我们" }
  },
  
  // 产品页面
  "products": {
    "all_products": { "en": "All Products", "zh": "全部产品" },
    "category": { "en": "Category", "zh": "产品分类" },
    "part_number": { "en": "Part Number", "zh": "型号" },
    "description": { "en": "Description", "zh": "产品描述" },
    "specifications": { "en": "Specifications", "zh": "技术规格" },
    "applications": { "en": "Applications", "zh": "应用领域" },
    "related_products": { "en": "Related Products", "zh": "相关产品" },
    "inquiry": { "en": "Request Quote", "zh": "询价" },
    "download": { "en": "Download Specs", "zh": "下载规格" }
  },
  
  // 参数标签
  "params": {
    "material": { "en": "Material", "zh": "材料" },
    "diameter": { "en": "Diameter", "zh": "直径" },
    "focal_length": { "en": "Focal Length", "zh": "焦距" },
    "thickness": { "en": "Thickness", "zh": "厚度" },
    "wavelength": { "en": "Wavelength", "zh": "波长" },
    "reflectivity": { "en": "Reflectivity", "zh": "反射率" },
    "transmittance": { "en": "Transmittance", "zh": "透过率" },
    "surface_quality": { "en": "Surface Quality", "zh": "光洁度" },
    "surface_flatness": { "en": "Surface Flatness", "zh": "面型" },
    "centration": { "en": "Centration", "zh": "偏心" },
    "clear_aperture": { "en": "Clear Aperture", "zh": "有效孔径" },
    "coating": { "en": "Coating", "zh": "镀膜" },
    "phase_delay": { "en": "Phase Delay", "zh": "相位延迟" },
    "extinction_ratio": { "en": "Extinction Ratio", "zh": "消光比" },
    "numerical_aperture": { "en": "Numerical Aperture", "zh": "数值孔径" },
    "working_distance": { "en": "Working Distance", "zh": "工作距离" },
    "magnification": { "en": "Magnification", "zh": "放大倍率" }
  },
  
  // 按钮和操作
  "actions": {
    "view_details": { "en": "View Details", "zh": "查看详情" },
    "add_to_cart": { "en": "Add to Cart", "zh": "加入购物车" },
    "request_quote": { "en": "Request Quote", "zh": "询价" },
    "download_pdf": { "en": "Download PDF", "zh": "下载PDF" },
    "back_to_list": { "en": "Back to List", "zh": "返回列表" },
    "contact_us": { "en": "Contact Us", "zh": "联系我们" },
    "search": { "en": "Search", "zh": "搜索" },
    "filter": { "en": "Filter", "zh": "筛选" },
    "clear": { "en": "Clear", "zh": "清除" }
  },
  
  // 分类名称
  "categories": {
    "optical-materials": { "en": "Optical Materials", "zh": "光学材料简介" },
    "plano-convex-lenses": { "en": "Plano-Convex Lenses", "zh": "K9平凸透镜" },
    "bi-convex-lenses": { "en": "Bi-Convex Lenses", "zh": "K9双凸透镜" },
    "optical-windows": { "en": "Optical Windows", "zh": "光学窗口" },
    "optical-mirrors": { "en": "Optical Mirrors", "zh": "光学反射镜" },
    "optical-prisms": { "en": "Optical Prisms", "zh": "光学棱镜" },
    "optical-filters": { "en": "Optical Filters", "zh": "光学滤光片" },
    "wave-plates-polarizers": { "en": "Wave Plates & Polarizers", "zh": "光学波片和偏振片" },
    "beamsplitters": { "en": "Beamsplitters", "zh": "光学分光镜片" },
    "other-optical-components": { "en": "Other Optical Components", "zh": "其他光学元件" },
    "optical-coatings": { "en": "Optical Coatings", "zh": "光学镀膜" },
    "opto-mechanical-products": { "en": "Opto-Mechanical Products", "zh": "光机产品" }
  },
  
  // 错误和提示信息
  "messages": {
    "no_products": { "en": "No products found", "zh": "未找到相关产品" },
    "loading": { "en": "Loading...", "zh": "加载中..." },
    "error": { "en": "An error occurred", "zh": "发生错误" },
    "success": { "en": "Success", "zh": "成功" }
  },
  
  // 页脚
  "footer": {
    "company_name": { "en": "Beijing Hengding Optical Technology Co., Ltd.", "zh": "北京恒鼎光科技有限公司" },
    "tagline": { "en": "Your Trusted Optical Components Partner", "zh": "您值得信赖的光学元件合作伙伴" },
    "copyright": { "en": "© 2024 PhotonEdge. All rights reserved.", "zh": "© 2024 北京恒鼎光科技. 保留所有权利." }
  }
};

// 语言切换函数
function setLanguage(lang) {
  if (lang !== 'en' && lang !== 'zh') return;
  
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    const keys = key.split('.');
    let value = translations;
    
    for (const k of keys) {
      if (value && value[k]) {
        value = value[k];
      } else {
        return;
      }
    }
    
    if (value && value[lang]) {
      element.textContent = value[lang];
    }
  });
  
  // 存储语言选择
  localStorage.setItem('language', lang);
}

// 获取当前语言
function getCurrentLanguage() {
  return localStorage.getItem('language') || 'en';
}

// 导出
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { translations, setLanguage, getCurrentLanguage };
}
