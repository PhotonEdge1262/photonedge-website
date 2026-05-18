# PhotonEdge Products Data

北京恒鼎光科技有限公司 (Beijing Hengding Optical Technology Co., Ltd.) 完整产品数据

## 产品分类 (Product Categories)

| 分类 ID | 英文分类名 | 中文分类名 | 图片目录 |
|---------|-----------|-----------|----------|
| optical-lenses | Optical Lenses | 光学透镜 | optical-lenses/ |
| optical-windows | Optical Windows | 光学窗口 | optical-windows/ |
| optical-mirrors | Optical Mirrors | 光学反射镜 | optical-mirrors/ |
| optical-prisms | Optical Prisms | 光学棱镜 | optical-prisms/ |
| optical-filters | Optical Filters | 光学滤光片 | optical-filters/ |
| optical-beamsplitters | Optical Beamsplitters | 光学分光片 | optical-beamsplitters/ |
| optical-waveplates | Optical Waveplates | 光学波片 | optical-waveplates/ |
| optical-polarizers | Optical Polarizers | 光学偏振片 | optical-polarizers/ |

## 包含产品数量

- **光学透镜**: 平凸透镜、弯月透镜、石英透镜、柱面透镜、消色差透镜、C透镜、球透镜、棒镜、非球面透镜
- **光学窗口**: K9窗口、UV石英窗口、蓝宝石窗口、CaF2窗口、Ge窗口、Si窗口、ZnSe窗口
- **光学反射镜**: 介质反射镜、金属反射镜
- **光学棱镜**: 直角棱镜、五角棱镜、角锥棱镜、道威棱镜、色散棱镜、屋脊棱镜
- **光学滤光片**: 窄带滤光片、ND中性密度滤光片
- **光学分光片**: 平板分光片、立方体分光片、消偏振分光片、偏振分光片
- **光学波片**: 多级波片、双波长波片、胶合零级波片、空气隙零级波片
- **光学偏振片**: 线偏振片、圆偏振片、红外偏振片、格兰泰勒棱镜、格兰激光棱镜、格兰汤普生棱镜、渥拉斯通棱镜

## 数据文件格式

```javascript
// products-data.js
const PRODUCTS = [
  {
    id: "lens-k9-plano-convex-001",
    name: "K9 Plano-Convex Lens",
    nameZh: "K9平凸透镜",
    category: "optical-lenses",
    categoryZh: "光学透镜",
    description: "High-quality K9 glass plano-convex lens for general laser and imaging applications...",
    image: "images/products/optical-lenses/k9-plano-convex.jpg",
    parameters: {
      material: "K9",
      type: "Plano-Convex",
      diameter: "6mm, 10mm, 12.7mm, 25mm, 50mm",
      focalLength: "10mm, 20mm, 30mm, 50mm, 100mm, 200mm",
      coating: "Uncoated, AR coating"
    },
    partNumbers: ["PCX-K9-6-10", "PCX-K9-6-20", "PCX-K9-10-20", "..."],
    price: 8,
    priceUnit: "USD",
    priceNote: "Price varies by specification",
    priceNoteZh: "价格根据规格不同",
    slug: "k9-plano-convex"
  }
];
```

## 图片路径规范

所有产品图片应放置在 `images/products/` 目录下：

```
images/products/
├── optical-lenses/
│   ├── k9-plano-convex.jpg
│   ├── bk7-plano-convex.jpg
│   ├── ...
├── optical-windows/
├── optical-mirrors/
├── optical-prisms/
├── optical-filters/
├── optical-beamsplitters/
├── optical-waveplates/
└── optical-polarizers/
```

## 使用方法

### 在 Node.js 项目中

```javascript
// 方式1: ES Module
import { PRODUCTS } from './products-data.js';

// 方式2: CommonJS
const { PRODUCTS } = require('./products-data.js');

// 获取所有产品
console.log(PRODUCTS.length, 'products');

// 按分类筛选
const lenses = PRODUCTS.filter(p => p.category === 'optical-lenses');

// 按ID查找
const product = PRODUCTS.find(p => p.id === 'lens-k9-plano-convex-001');
```

### 在浏览器中

```html
<script src="./products-data.js"></script>
<script>
  console.log(PRODUCTS);
</script>
```

## 数据字段说明

| 字段 | 类型 | 描述 |
|------|------|------|
| `id` | string | 产品唯一标识符 |
| `name` | string | 产品英文名称 |
| `nameZh` | string | 产品中文名称 |
| `category` | string | 分类ID |
| `categoryZh` | string | 分类中文名称 |
| `description` | string | 英文SEO描述 |
| `image` | string | 产品图片相对路径 |
| `parameters` | object | 技术规格参数 |
| `partNumbers` | array | 规格型号列表 |
| `price` | number | 参考价格 |
| `priceUnit` | string | 价格单位 (USD) |
| `priceNote` | string | 价格说明（英文） |
| `priceNoteZh` | string | 价格说明（中文） |
| `slug` | string | URL友好标识符 |

## 联系信息

- **公司**: 北京恒鼎光科技有限公司 (PhotonEdge)
- **网址**: https://www.photonedgeoptics.com
- **邮箱**: sales@photonedgeoptics.com
- **电话**: +86-13693009175

## 许可证

本产品数据仅供内部使用。价格和信息如有变更，恕不另行通知。

---

*最后更新: 2025年*
