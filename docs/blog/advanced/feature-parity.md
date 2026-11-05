---
title: 功能对照表（与 Material for MkDocs）
date: 2026-08-11
authors:
  - name: Wcowin
    email: wcowin@qq.com
categories:
  - 高级主题
---

# 功能对照表（与 Material for MkDocs）

> 对应官方：[Feature parity](https://zensical.org/compatibility/features/)
>
> Zensical 由 Material for MkDocs 的原班团队打造，目标是**完整兼容** Material for MkDocs 的全部能力，并在此之上超越。下表列出当前已支持的功能（含原 Insiders 版特性），官方称此页会随功能对齐进展**定期更新**。

!!! note "如何阅读"
    本表按官方分类整理。绝大多数功能在 Zensical 中**开箱即用**或仅需简单配置即可启用，具体用法见本站对应教程页（配置、主题、Markdown 扩展、博客、部署、高级主题等）。

## 1. 核心功能（Core）

| 功能 | 说明 | 本站对应 |
|------|------|----------|
| `pip install` 安装 | 标准 Python 包安装 | [5 分钟快速开始](../../getting-started/quick-start.md) |
| 创建新站点 | `zensical new` | [命令行接口](../../getting-started/cli.md) |
| 从 `mkdocs.yml` 构建 | 原生兼容 MkDocs 配置 | [从 MkDocs 迁移](../../getting-started/migration.md) |
| 内置预览服务器 | `zensical serve` | [命令行接口](../../getting-started/cli.md) |
| 兼容 MkDocs 文件布局 | 目录结构一致 | — |
| Python Markdown 方言 | 解析语法一致 | [Markdown 扩展使用](../../tutorials/markdown-extensions.md) |
| 目录 URL | `use_directory_urls` | [配置详解](../../tutorials/configuration.md) |
| Jinja 模板 | 引擎换为 MiniJinja，结构不变 | [主题定制指南](../../tutorials/theme-customization.md) |
| YAML 页面元数据 | front matter 一致 | — |
| 额外 CSS / JS / 模板 | `extra_css` / `extra_javascript` | [配置详解](../../tutorials/configuration.md) |
| 浏览器兼容 | 与官方一致 | — |
| 链接校验 | 构建期检查断链 | [链接与脚注验证](validation.md) |
| 严格模式（Strict） | 警告即中止构建 | [配置详解](../../tutorials/configuration.md) · [链接与脚注验证](validation.md) |

## 2. 站点与页面结构（Site & page structure）

| 功能 | 说明 |
|------|------|
| 60+ 语言支持 | `language` 配置 |
| 站点语言切换器 | 多语言切换 |
| 页眉（Header） | 顶部导航 |
| 自动隐藏页眉 | 滚动时收起 |
| 公告栏（Announcement） | `announce.dismiss` |
| 仓库图标与链接 | `repo_url` / `repo_name` |
| Code Actions | 代码区操作 |
| 页脚（Footer） | 版权、社交链接 |
| 页脚导航 | 上一页/下一页 |
| 社交链接 | `extra.social` |
| 版权声明 | `copyright` |
| 生成器声明 | `generator` |
| 评论系统 | Waline / Giscus 等 | [添加评论系统](comment-system.md) · [Giscus 明暗同步](giscus-theme-sync.md) |
| 404 页面 | [自定义 404 页面](custom-404.md) |
| 标签（Tags） | [标签插件](../plugins/tags.md) |
| 搜索中的标签 | 标签可被检索 |
| 标签列表页 | 标签归档 |
| 修订信息¹ | 文档日期、作者、贡献者（超越基础仓库集成） | [文档日期插件](../../tutorials/configuration.md) |

## 3. 外观（Appearance）

| 功能 | 说明 | 本站对应 |
|------|------|----------|
| Classic Material 主题 | 经典外观 | [主题定制指南](../../tutorials/theme-customization.md) |
| 资源与定制 | 自定义资源 | 同上 |
| 模板覆盖 | `custom_dir` | 同上 |
| 颜色与调色板切换 | `palette` | 同上 |
| 自动明暗模式 | 跟随系统 | 同上 |
| 自定义颜色与配色 | 主色/强调色 | 同上 |
| 字体 | [自定义字体](custom-fonts.md) |
| 图标、表情、Favicon | `icon` / emoji | [主题定制指南](../../tutorials/theme-customization.md) |
| 社交卡片 | 分享卡片 | — |

## 4. Markdown 扩展（Markdown extensions）

> 以下扩展均基于 Python Markdown + `pymdownx`，本站 [Markdown 扩展使用](../../tutorials/markdown-extensions.md) 已逐类讲解。

Abbreviations · Admonitions · Annotations · Attribute lists · BetterEm · Buttons · Caption · Caret/Mark/Tilde · Code blocks（高亮、复制）· Content tabs · Critic · Data tables · Definition lists · Details · Diagrams（Mermaid）· Footnotes · Grids · Highlight · Icons & Emojis · Images · InlineHighlight · Keys · Markdown in HTML · Math（MathJax、KaTeX）· SmartSymbols · Snippets · Superfences · Tabbed · Table of contents · Tables · Tasklist · Tooltips

## 5. 内容（Content）

| 功能 | 说明 | 本站对应 |
|------|------|----------|
| 评论系统 | 见上 | [添加评论系统](comment-system.md) |
| 仓库集成 | `repo_url` | [配置详解](../../tutorials/configuration.md) |
| 版本管理 | Versioning（路线图中） | — |
| 博客 | 内置博客系统 | [博客系统完全指南](../../tutorials/blog-tutorial.md) |

## 6. 导航（Navigation）

| 功能 | 说明 | 本站对应 |
|------|------|----------|
| `mkdocs.yml` 显式导航 | `nav` | [配置详解](../../tutorials/configuration.md) |
| 即时加载 | `navigation.instant` | 同上 |
| 即时预取 | `navigation.instant.prefetch` | 同上 |
| 进度指示 | 加载进度条 | 同上 |
| 即时预览 | Instant previews | 同上 |
| 锚点跟踪 | `navigation.tracking` | 同上 |
| 导航 Tab / 吸顶 Tab | `navigation.tabs` | 同上 |
| 导航分组 | `navigation.sections` | 同上 |
| 导航展开 | `navigation.expand` | 同上 |
| 导航路径（面包屑） | 面包屑 | 同上 |
| 导航剪枝 | `navigation.prune` | 同上 |
| 章节索引页 | `navigation.indexes` | 同上 |
| 目录（TOC） | `toc` | [配置详解](../../tutorials/configuration.md) |
| 目录跟随滚动 | `toc.follow` | 同上 |
| 返回顶部按钮 | `navigation.top` | 同上 |
| 隐藏侧边栏 | 布局控制 | 同上 |
| 键盘快捷键 | 快捷键 | 同上 |
| 内容区宽度 | 内容宽度 | 同上 |
| 搜索 | [搜索功能配置](../plugins/search.md) |

## 7. 优化（Optimization）

| 功能 | 说明 | 本站对应 |
|------|------|----------|
| 站点分析与反馈组件 | Analytics & feedback | — |
| Cookie 同意 | [Cookie 同意表单](data-privacy.md) |
| 自定义 Cookie | 同上 |
| 搜索引擎优化 | [SEO 优化](seo.md) |
| 离线使用 | `use_directory_urls = false` | [配置详解](../../tutorials/configuration.md) |
| 数据隐私 | [Cookie 同意表单](data-privacy.md) |

## 8. 扩展（Extensions）

| 功能 | 说明 | 状态 |
|------|------|------|
| 模块系统（Module system） | 用于替代 hooks 与 plugins 的下一代扩展机制 | 路线图中（见 [第三方插件规划](../plugins/third-party-plugins.md)） |

---

!!! info "与 MkDocs 插件的对应"
    上表中的模块系统将逐步替代 MkDocs 生态的第三方插件（mkdocstrings、macros、minify 等）。详见 [第三方插件规划](../plugins/third-party-plugins.md)。

**官方链接**：[Feature parity](https://zensical.org/compatibility/features/)（此页随功能对齐进展定期更新）
