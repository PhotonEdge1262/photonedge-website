# PhotonEdge V13.2 线上问题诊断报告

**诊断日期：** 2025年5月  
**网站：** https://photonedgeoptics.com  
**版本：** V13.2  
**诊断范围：** 全站链接完整性、资源加载、SEO配置

---

## 执行摘要

V13.2 版本存在 **1个阻断性问题** 和 **3个次要问题**。用户反馈"链接有问题了"的原因已确认：产品 slug URL（`/products/:slug`）全部返回 404。

---

## 🔴 P0 — 阻断性问题

### 问题 1：所有 `/products/:slug` URL 返回 404（核心问题）

**影响范围：** 75个产品页面（sitemap中全部产品slug URL）  
**严重程度：** 🔴 阻断 — 搜索引擎和用户直接访问均无法打开产品页  
**检测方法：** `fetch_web` 直接访问 slug URL

**测试结果：**

| URL | 状态 |
|-----|------|
| `https://photonedgeoptics.com/products/bk7-double-convex-lenses` | ❌ 404 "link dead" |
| `https://photonedgeoptics.com/products/uv-fused-silica-ball-lenses` | ❌ 404 "link dead" |
| `https://photonedgeoptics.com/nonexistent` | ❌ 404 "link dead" |
| `https://photonedgeoptics.com/product-detail.html?slug=bk7-double-convex-lenses` | ✅ 正常 |
| `https://photonedgeoptics.com/product-detail.html?code=BK7%20Double%20Convex%20Lenses` | ✅ 正常（旧格式兼容） |

**根本原因分析：**

当前 `vercel.json` 的 rewrite 规则使用了 Vercel v2 的 **命名参数语法**（`:slug`），但目标端也用了 `:slug`：

```json
{
  "rewrites": [
    { "source": "/products/:slug", "destination": "/product-detail.html?slug=:slug" }
  ]
}
```

在 Vercel v2 中，**`:slug` 是 source 端命名捕获，destination 端必须用 `$slug`**（美元符号）来引用捕获的值。使用 `:slug` 在 destination 中不会被 Vercel 解析，会被当作字面字符串处理，导致目标 URL 变成 `/product-detail.html?slug=:slug`，查询参数值是字面量 `":slug"` 而不是实际 slug 值。

**如何修复：**

```json
{
  "rewrites": [
    { "source": "/products/:slug", "destination": "/product-detail.html?slug=$slug" }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" }
      ]
    }
  ]
}
```

---

## 🟡 P1 — SEO/内容质量问题

### 问题 2：sitemap.xml 中 75个产品 URL 全部无效

**影响范围：** 97个 sitemap URL 中 75个产品 URL  
**严重程度：** 🟡 高 — Google 等搜索引擎抓取这些 URL 会得到 404，直接影响搜索排名  
**文件位置：** `photonedge-website/sitemap.xml`

**具体表现：**
sitemap 中所有 `/products/:slug` 格式的 URL 均不可访问，与问题1的 slug URL 404 相同。修复问题1后 sitemap 自然修复，无需额外操作。

**建议：** 修复 vercel.json 后，重新生成 sitemap（已有工具 `generate_website.py`）。

---

### 问题 3：News 页面（news.html）图片显示 `[object Object]`

**影响范围：** news.html 首页展示的 3篇新闻文章  
**严重程度：** 🟡 中 — 图片加载失败，影响页面美观  
**检测方法：** `fetch_web` 抓取 news.html，图片 URL 为 `https://photonedgeoptics.com/[object%20Object]`

**根本原因分析：**

news.html 引用了 AiPexBase BaaS SDK（`aipexbase-js`）来动态加载新闻数据。问题出在 BaaS 数据库中的 `thumbnail` 字段存储格式与前端渲染代码期望的格式不匹配：

```javascript
// news.html 渲染代码（正确）
const thumbnail = article.thumbnail && article.thumbnail.length > 0 
    ? article.thumbnail[0]   // 期望 thumbnail 是一个数组，取第一个元素
    : 'https://images.unsplash.com/...';

// AiPexBase BaaS 中实际存储的可能是
thumbnail: { url: '...', alt: '...' }   // ❌ 对象而非数组
// 或
thumbnail: 'https://...'                 // ❌ 字符串而非数组
```

当 `thumbnail` 是对象时，`article.thumbnail[0]` 返回 `undefined`，BaaS SDK 将其 stringified 为 `[object Object]`。

**如何修复：**

修改 news.html 的 `DOMContentLoaded` 中初始化 AiPexBase 后的数据处理逻辑，对 thumbnail 做类型适配：

```javascript
// 修复后的 thumbnail 处理
function getThumbnailUrl(article) {
    var thumb = article.thumbnail;
    if (!thumb) return 'https://images.unsplash.com/...default...';
    if (typeof thumb === 'string') return thumb;  // 直接是URL字符串
    if (Array.isArray(thumb)) return thumb[0];     // 数组格式
    if (thumb.url) return thumb.url;               // 对象格式 {url, alt}
    return 'https://images.unsplash.com/...default...';
}
```

**备选方案：** 直接在 AiPexBase BaaS 数据库中将 thumbnail 字段改为字符串数组格式。

---

## 🟠 P2 — 配置一致性问题

### 问题 4：sitemap 中 blog-post 页面 URL 缺失

**影响范围：** 10篇技术博客文章未收录 sitemap  
**严重程度：** 🟠 低 — 博客文章不被搜索引擎索引

sitemap 中只有 `blog.html` 列表页，缺少各博客文章详情页的 URL（`/blog-post.html?slug=xxx` 或 `/blog/xxx`）。blog.html 链接到文章详情使用 `?slug=` 格式，这部分功能正常，但未被 sitemap 收录。

**建议：** 生成 sitemap 时遍历 BLOG_POSTS 数据添加博客文章 URL。

---

### 问题 5：旧 URL 格式（`?code=`）仍在工作，但 sitemap 中未体现

**影响范围：** `product-detail.html?code=BK7%20Double%20Convex%20Lenses` 等旧链接  
**严重程度：** 🟠 低 — 旧 URL 兼容，但 sitemap 中不存在

旧格式产品 URL（`?code=xxx`）仍然可用，在 `product-detail.html` 的 JS 中有多级兼容逻辑。这是有益的降级机制，但 sitemap 中只有新 slug 格式 URL（旧 URL 失效时不影响 SEO）。

---

## ✅ 正常工作的部分

以下页面和功能经检测正常：

| 页面/功能 | 状态 |
|-----------|------|
| 首页 `index.html` | ✅ 正常 |
| 产品列表 `products.html` | ✅ 正常 |
| About页面 `about.html` | ✅ 正常 |
| Contact页面 `contact.html` | ✅ 正常 |
| Blog列表 `blog.html` | ✅ 正常 |
| Blog详情 `blog-post.html?slug=xxx` | ✅ 正常 |
| Applications页面 `applications.html` | ✅ 正常 |
| Downloads页面 `downloads.html` | ✅ 正常（含4个PDF下载链接） |
| Cart页面 `cart.html` | ✅ 正常 |
| 产品详情 `product-detail.html?slug=xxx` | ✅ 正常 |
| `robots.txt` | ✅ 正常 |
| `sitemap.xml` | ✅ 结构正常（内容URL无效） |

**CSS/JS 资源：** 静态资源链接（`css/style.css`、GA4、`translations.js`）使用相对路径，经验证在根路径页面均正常加载。

**翻译系统：** `translations.js` 多语言切换功能正常。

---

## 问题严重程度汇总

| # | 问题 | 程度 | 修复难度 |
|---|------|------|----------|
| 1 | `/products/:slug` 全部404（vercel.json rewrite 用错了 `$slug`） | 🔴 P0 | ⭐ 改1个字符 |
| 2 | sitemap.xml 中75个产品URL无效 | 🟡 P1 | 自动修复 |
| 3 | news.html 图片显示 `[object Object]` | 🟡 P1 | 修改JS逻辑 |
| 4 | sitemap 缺少 blog-post 详情页 | 🟠 P2 | 更新生成脚本 |
| 5 | 旧 `?code=` URL 未在 sitemap 中体现 | 🟠 P2 | 可选 |

---

## 修复优先级

### 立即修复（P0）

**文件：** `/app/data/所有对话/主对话/photonedge-website/vercel.json`

将 destination 中的 `:slug` 改为 `$slug`：

```json
{
  "rewrites": [
    { "source": "/products/:slug", "destination": "/product-detail.html?slug=$slug" }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" }
      ]
    }
  ]
}
```

然后重新部署：
```bash
cd /f/deploy/photonedge-website/photonedge-website-v6
git add vercel.json
git commit -m "V13.2 fix: use \$slug in rewrite destination"
git push origin main --force
```

### 其次修复（P1）

**问题3：** 修改 `news.html` 中的 thumbnail 处理逻辑，兼容对象/字符串/数组三种格式。

**问题2：** vercel.json 修复后 sitemap 自然有效，无需额外操作。

---

## 本地代码 vs 线上对比

| 文件 | 本地状态 | 线上状态（推测） |
|------|----------|-----------------|
| `vercel.json` | 有 rewrite 但用了错误的 `:slug` | 可能同本地（导致404） |
| `404.html` | ✅ 存在于 photonedge-website | ❌ 可能不存在于 photonedge-website-new |
| `product-detail.html` | ✅ 正确 | ✅ 正确 |
| `products.html` | 链接到 `/products/:slug` | ❌ slug URL 404 |
| `sitemap.xml` | 75个 slug URL | ❌ 全部404 |
| `news.html` | AiPexBase 动态数据 | ❌ thumbnail 格式不匹配 |

> ⚠️ 注意：`photonedge-website-new` 目录中 `vercel.json` 使用了更旧版本的 rewrite（`/product-detail` → `/product-detail.html`，缺少 `:slug` 参数），且缺少 `404.html`。如果该目录被误部署，会导致更严重的问题（slug URL 完全无法工作）。建议确认 GitHub 推送的源目录是 `photonedge-website` 而非 `photonedge-website-new`。
