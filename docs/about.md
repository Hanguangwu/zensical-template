---
title: 关于
date: 2025-01-22
---

# 关于 Zensical-Chinese-Tutorial

## 项目简介

Zensical-Chinese-Tutorial 是最详细、最便捷、最前沿的 Zensical 中文教程。

## 与官方文档对齐

本站教程在结构上与 [Zensical 官方](https://zensical.org/) 对齐，便于与官方文档互查。维护者可参考 [与官方文档对齐说明](OFFICIAL_ALIGNMENT.md)（仓库内文档）进行颗粒度同步。

### 兼容性策略摘要

Zensical 由 Material for MkDocs 原班团队打造，目标是**完整兼容**并超越 Material for MkDocs。本站就官方 Compatibility 区提供了两篇中文综述：

- **[功能对照表（与 Material for MkDocs）](blog/advanced/feature-parity.md)**：逐类列出已支持的核心、外观、Markdown 扩展、导航、优化等功能，一眼看清能力边界。
- **[第三方插件规划](blog/plugins/third-party-plugins.md)**：说明 mkdocstrings、macros、minify 等 MkDocs 插件未来如何以 Zensical「模块」形式无缝替换。

迁移相关内容另见 [从 MkDocs 迁移](getting-started/migration.md)。

## 路线图与愿景 {#roadmap}

Zensical 由 Material for MkDocs 原班团队开发，目前处于 **Alpha 阶段**，正在快速迭代。以下是官方路线图要点摘要，完整内容以官方为准。

### 已实现的基础

- **Rust 运行时 (ZRX)**：全新的底层引擎，支持增量构建、任务调度和并发处理
- **Modern / Classic 双主题**：Modern 是全新的现代设计，Classic 完全兼容 Material for MkDocs 外观
- **向后兼容**：原生读取 `mkdocs.yml`，使用 Python Markdown 解析器保证方言一致，内置 MiniJinja 模板引擎实现并行渲染
- **Studio 编辑器**：专属写作环境，支持实时链接检测和智能提示
- **即时导航**：无刷新页面切换，开箱即用

### 即将到来的能力

- **模块化架构**：将构建管线拆分为可组合、可扩展的模块，支持显式依赖和智能缓存，提供 Python 连接器
- **Disco 搜索引擎**：全新搜索内核，支持倒排索引、向量查询和联邦搜索，未来将作为独立开源项目发布
- **UI 组件框架**：用独立组件替代传统模板，每个组件自包含数据获取、渲染、样式和交互逻辑
- **配置管理革新**：支持零配置默认值、代码化配置、Monorepo 支持和可复用预设
- **灵活导航系统**：从单体导航转向内容驱动的可扩展导航，配合智能缓存
- **嵌套项目**：支持多层级目录结构、跨项目链接、统一搜索和灵活部署
- **全球化本地化**：灵活的内容组织方式、机器学习辅助翻译草稿、完整的界面和代码片段翻译
- **发布追踪**：支持基于 Git 或文件夹的版本管理，增量重建只处理变更内容
- **主题导向写作**：支持内容复用、DITA 兼容、多变体发布，以及为 LLM/AI 助手优化的上下文生成

### 官方链接

- **[Roadmap](https://zensical.org/about/roadmap/)**：完整路线图与进展追踪
- **[Vision](https://zensical.org/about/vision/)**：产品愿景与社区协作方式
- **[Newsletter](https://zensical.org/about/newsletter/)**：月度进展与动态
- **[Zensical Spark](https://zensical.org/about/)**：高级支持与早期功能访问

