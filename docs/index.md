---
title: Zensical 中文教程
hide:
  - footer
---

# Zensical 中文教程

> 最详细、最便捷、最前沿的 Zensical 中文教程，与官方文档结构保持同步。

本站系统讲解 Zensical 的安装、配置、主题定制、Markdown 写作、博客系统、插件与部署，适合从 MkDocs 迁移或第一次搭建文档站的读者。

!!! info "当前状态"
    Zensical 目前处于 **Alpha** 阶段，核心功能可用，部分能力仍在开发中。
    功能状态与常见问题见 [FAQ](faq.md)。

## 内容导航

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } __快速开始__

    ---

    - [5 分钟快速开始](getting-started/quick-start.md)
    - [命令行接口 (CLI)](getting-started/cli.md)
    - [从 MkDocs 迁移](getting-started/migration.md)

-   :material-book-open:{ .lg .middle } __核心教程__

    ---

    - [zensical.toml 配置详解](tutorials/configuration.md)
    - [主题定制指南](tutorials/theme-customization.md)
    - [Markdown 扩展使用](tutorials/markdown-extensions.md)
    - [Markdown 高效写作](tutorials/zensical-markdown-tip.md)
    - [博客系统完全指南](tutorials/blog-tutorial.md)

-   :material-puzzle:{ .lg .middle } __插件系统__

    ---

    - [插件概览](blog/plugins/overview.md)
    - [博客插件](blog/plugins/blog.md)
    - [搜索插件](blog/plugins/search.md)
    - [标签插件](blog/plugins/tags.md)
    - [RSS 插件](blog/plugins/rss.md)

-   :material-rocket:{ .lg .middle } __部署指南__

    ---

    - [GitHub Pages（推荐）](blog/deployment/github-pages.md)
    - [Cloudflare Pages](blog/deployment/cloudflare-pages.md)
    - [Netlify](blog/deployment/netlify.md)
    - [EdgeOne Pages](blog/deployment/edgeone-pages.md)
    - [GitLab Pages](blog/deployment/gitlab-pages.md)
    - [自托管](blog/deployment/self-hosted.md)

-   :material-tune-variant:{ .lg .middle } __高级主题__

    ---

    - [性能优化](blog/advanced/performance.md)
    - [SEO 优化](blog/advanced/seo.md)
    - [多语言支持](blog/advanced/i18n.md)
    - [自定义 404](blog/advanced/custom-404.md)
    - [评论系统](blog/advanced/comment-system.md)
    - [链接与脚注验证](blog/advanced/validation.md)

-   :material-account-group:{ .lg .middle } __关于与案例__

    ---

    - [关于本站](about.md)
    - [案例展示](showcase.md)
    - [常见问题](faq.md)

</div>

## 推荐学习路径

- **新手**：[5 分钟快速开始](getting-started/quick-start.md) → [配置详解](tutorials/configuration.md) → [主题定制](tutorials/theme-customization.md) → [GitHub Pages 部署](blog/deployment/github-pages.md)
- **从 MkDocs 迁移**：[迁移指南](getting-started/migration.md) → [配置差异](tutorials/configuration.md) → 本地预览 → 部署
- **进阶**：[性能](blog/advanced/performance.md)、[SEO](blog/advanced/seo.md)、[i18n](blog/advanced/i18n.md)、[评论系统](blog/advanced/comment-system.md)

## 常用命令

```bash
# 本地预览（默认 http://localhost:8000）
zensical serve

# 清理并构建到 site/
zensical build --clean
```

更多用法见 [命令行接口 (CLI)](getting-started/cli.md)；完整配置见 [zensical.toml 配置详解](tutorials/configuration.md)。

## 参与贡献

本站内容整理自 [Wcowin/Zensical-Chinese-Tutorial](https://github.com/Wcowin/Zensical-Chinese-Tutorial)，欢迎提交 Issue 或 Pull Request 补充教程内容。

- **GitHub**：[Wcowin/Zensical-Chinese-Tutorial](https://github.com/Wcowin/Zensical-Chinese-Tutorial)
- **官方文档**：[zensical.org](https://zensical.org/docs/)
