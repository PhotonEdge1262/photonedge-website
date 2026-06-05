# PhotonEdge V31 发布说明

## 🔴 P0 修复（严重问题）

### 1. 产品描述翻译修复
- 修复75个产品 `descriptionZh` 中英混杂问题
- 全部产品描述现在为纯中文

### 2. 首页翻译补全
- 为计算器区域标题和描述添加 `data-i18n`
- 为8个产品分类副标题添加 `data-i18n`
- 为 "Industries We Serve" 和底部 "Company" 链接添加翻译

## 📝 新增翻译键（中英文）
- `calcTitle` / `calcDesc` - 计算器区域标题和描述
- `calcFocal` / `calcCoating` / `calcMagnification` - 3个计算器标题
- `industriesTitle` - 服务行业标题
- `catLensesDesc` ~ `catBallLensesDesc` (8个) - 产品分类描述
- `footerCompany` - 底部公司链接

## 其他更新
- sitemap.xml 更新日期为 2026-06-05

## 部署命令
```bash
tar -xzf PhotonEdge-V31.tar.gz
git add .
git commit -m "V31: 产品描述全部汉化 + 首页翻译补全"
git push origin main
```
