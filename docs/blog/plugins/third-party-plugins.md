---
title: 第三方插件规划（与 MkDocs 插件对应）
date: 2026-08-11
authors:
  - name: Wcowin
    email: wcowin@qq.com
categories:
  - 插件系统
---

# 第三方插件规划（与 MkDocs 插件对应）

> 对应官方：[Plugins](https://zensical.org/compatibility/plugins/)
>
> Zensical 基于对 GitHub 上使用 Material for MkDocs 的 Top 1000 仓库及插件目录的定量分析，将需要迁移的 MkDocs 插件分为两级优先级，全部放入官方 Backlog。

## 支持策略

- **兼容方式**：在 `mkdocs.yml` 或 `zensical.toml` 的 `project` 域中，把原插件配置映射到 Zensical 正在开发的**模块（modules）**，用户**无需修改配置或内容**即可构建。
- **Tier 1（最高优先级）**：确保无缝迁移的核心插件。
- **Tier 2（次高优先级）**：次高优先级插件。

## MkDocs 插件对应清单

| MkDocs 插件 | 分类 | Zensical 对应 | Backlog |
|-------------|------|---------------|---------|
| mkdocstrings | Tier 1 | 映射为 Zensical 模块（文档指向 `/docs/setup/extensions/mkdocstrings`） | [#4](https://github.com/zensical/backlog/issues/4) |
| macros（mkdocs-macros-plugin） | Tier 1 | 对应模块开发中 | [#16](https://github.com/zensical/backlog/issues/16) |
| minify（mkdocs-minify-plugin） | Tier 1 | 对应模块 | [#15](https://github.com/zensical/backlog/issues/15) |
| mike | Tier 1 | 对应模块 | [#14](https://github.com/zensical/backlog/issues/14) |
| awesome-nav（mkdocs-awesome-nav） | Tier 1 | 对应模块 | [#12](https://github.com/zensical/backlog/issues/12) |
| static-i18n（mkdocs-static-i18n） | Tier 2 | 对应模块 | [#1](https://github.com/zensical/backlog/issues/1) |
| git-authors | Tier 2 | 对应模块 | [#19](https://github.com/zensical/backlog/issues/19) |
| git-committers | Tier 2 | 对应模块 | [#17](https://github.com/zensical/backlog/issues/17) |
| git-revision-date-localized | Tier 2 | 对应模块 | [#18](https://github.com/zensical/backlog/issues/18) |

> `git` 泛指上述三个 `git-*` 插件，Zensical 将其全数纳入 Tier 2 支持。

## 当前限制与未来开放

1. **当前限制**：Zensical 先以自带模块替代上表中的 MkDocs 插件，用于测试模块系统；目前**暂未发布公共 API**，刻意暂缓第三方接入以免破坏变更。
2. **未来开放**：待 API 稳定后，在 **Zensical Spark** 中发布公共 API，并邀请关键生态维护者参与，培育第三方模块生态。
3. **开发优势**：第三方开发者只需写业务逻辑，运行时负责编排、并行化、缓存；模块可用 Rust 编写（Python 支持也在推进）。
4. **替换自由**：即使官方提供默认模块，用户仍可用第三方模块替换，保持灵活性。

## 功能重构提示

- `literate-nav` 与 `awesome-nav`（Tier 1）当前为兼容而映射，但 Phase 4 后 Zensical 将用**模块化导航**原生支持"导航即内容"，超越原插件约束。
- `typeset` 等因 MkDocs 设计局限产生的插件在 Zensical 中已废弃（不在上表）。

!!! tip "与本站内置插件的关系"
    本站已覆盖 Zensical 的**内置**插件：博客（[博客系统完全指南](../../tutorials/blog-tutorial.md)）、搜索（[搜索功能配置](search.md)）、标签（[标签插件](tags.md)）、RSS（[RSS 插件](rss.md)）。上表所列是**未来以模块形式替代的 MkDocs 第三方插件**，目前尚在 Backlog 中。

**官方链接**：[Plugins](https://zensical.org/compatibility/plugins/)
