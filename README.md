# PhotonEdge Website

## 产品中心网站 - 静态版本

本目录包含 PhotonEdge 官网的产品展示页面，**无需后端数据库**，可直接部署到任何静态托管平台。

### 文件结构

```
photonedge-website/
├── index.html              # 首页
├── products.html           # 产品中心页（动态加载）
├── product-detail.html     # 产品详情页（动态加载）
├── about.html              # 关于我们
├── applications.html       # 应用领域
├── news.html               # 新闻动态
├── downloads.html          # 下载中心
├── contact.html            # 联系我们
├── logo.png                # Logo
├── vercel.json             # Vercel 部署配置
├── images/
│   └── products/           # 产品图片（按分类组织）
│       ├── optical-lenses/
│       ├── optical-windows/
│       ├── optical-mirrors/
│       ├── optical-prisms/
│       ├── optical-filters/
│       ├── optical-beamsplitters/
│       └── optical-polarizing-components/
└── js/
    └── products-data.js    # 产品数据（66个产品）
```

### 产品数据

- **总产品数**: 66 个
- **总分类数**: 12 个

#### 分类列表

| 分类ID | 英文名 | 中文名 | 产品数 |
|--------|--------|--------|--------|
| optical-lenses | Optical Lenses | 光学透镜 | 12 |
| optical-spherical-lenses | Optical Spherical Lenses | 球面透镜 | 3 |
| optical-cylindrical-lenses | Optical Cylindrical Lenses | 柱面透镜 | 2 |
| optical-rod-lenses | Optical Rod Lenses | 棒状透镜 | 1 |
| optical-half-ball-lenses | Optical Half Ball Lenses | 半球透镜 | 1 |
| optical-ball-lenses | Optical Ball Lenses | 球面透镜 | 1 |
| optical-windows | Optical Windows | 光学窗口 | 7 |
| optical-mirrors | Optical Mirrors | 光学反射镜 | 10 |
| optical-prisms | Optical Prisms | 光学棱镜 | 7 |
| optical-filters | Optical Filters | 光学滤光片 | 5 |
| optical-beamsplitters | Optical Beamsplitters | 光学分束器 | 5 |
| optical-polarizing-components | Optical Polarising Components | 偏振光学组件 | 11 |

### 使用说明

#### 本地预览

1. 直接用浏览器打开 `index.html`
2. 或使用任意静态服务器：
   ```bash
   npx serve .
   # 或
   python -m http.server 8080
   ```

#### 部署到 Vercel

1. 将此目录上传到 GitHub
2. 在 Vercel 导入项目
3. 点击 Deploy

#### 部署到其他平台

由于使用纯静态文件，可部署到：
- GitHub Pages
- Netlify
- Cloudflare Pages
- 任意 Web 服务器

### 产品页面功能

#### 产品列表页 (products.html)
- ✅ 按分类筛选
- ✅ 搜索产品
- ✅ 响应式布局
- ✅ 产品卡片展示
- ✅ 无限滚动/分页

#### 产品详情页 (product-detail.html)
- ✅ 产品大图展示
- ✅ 技术参数表
- ✅ 相关产品推荐
- ✅ 面包屑导航
- ✅ 询价按钮

### 技术特点

- 🎨 **Tailwind CSS** - 现代 CSS 框架
- 📱 **完全响应式** - 适配所有设备
- ⚡ **无后端依赖** - 纯静态网站
- 🔄 **动态加载** - JS 按需渲染
- 🖼️ **图片优化** - WebP 格式支持

### 数据来源

产品数据来源于 `ltoptic.com` 爬取数据，已整合到 `js/products-data.js` 中。

### 许可证

© 2024 PhotonEdge. All rights reserved.
