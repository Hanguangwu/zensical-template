# Zensical 中文教程

<p align="center">
  <a href="https://zensical.org/"><img src="https://img.shields.io/badge/Built_with-Zensical-4051B5?style=for-the-badge" alt="Built with Zensical" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge" alt="Python 3.11+" /></a>
  <a href="https://github.com/Wcowin/Zensical-Chinese-Tutorial"><img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License" /></a>
</p>

<p align="center">最详细、最便捷、最前沿的 Zensical 中文教程</p>

本项目是一个使用 [Zensical](https://zensical.org/) 构建的中文教程站，内容整理自 [Wcowin/Zensical-Chinese-Tutorial](https://github.com/Wcowin/Zensical-Chinese-Tutorial)。教程覆盖安装与迁移、配置、主题定制、Markdown 写作、博客系统、插件、部署和高级优化，适合第一次接触 Zensical 的读者，也适合从 MkDocs 迁移的维护者。

> 上游在线阅读站点：<https://wcowin.work/Zensical-Chinese-Tutorial/>

## 为什么使用 Zensical

- **官方后继**：Material for MkDocs 已进入维护模式，Zensical 由原团队打造并推荐使用。
- **开箱即用**：即时导航、内置博客、搜索、RSS、标签等功能无需额外插件。
- **高性能**：Rust 运行时（ZRX）负责构建与增量处理。
- **双主题**：Modern 主题面向新项目，Classic 主题兼容 Material for MkDocs 外观。
- **兼容 MkDocs**：可以读取 `mkdocs.yml`，并沿用 Python Markdown 方言。

## 内容导航

| 板块 | 入口 | 主要内容 |
| --- | --- | --- |
| 快速开始 | [5 分钟快速开始](docs/getting-started/quick-start.md) | 安装、创建项目、本地预览 |
| 快速开始 | [命令行接口 (CLI)](docs/getting-started/cli.md) | `serve`、`build`、`new` 与 MkDocs 差异 |
| 快速开始 | [从 MkDocs 迁移](docs/getting-started/migration.md) | 配置迁移、兼容性与部署 |
| 核心教程 | [配置详解](docs/tutorials/configuration.md) | `zensical.toml` 全部主要配置项 |
| 核心教程 | [主题定制](docs/tutorials/theme-customization.md) | 配色、字体、Logo、自定义样式 |
| 核心教程 | [Markdown 扩展](docs/tutorials/markdown-extensions.md) | Admonition、代码块、Mermaid、数学公式等 |
| 核心教程 | [博客系统](docs/tutorials/blog-tutorial.md) | 文章、分类、作者、草稿与阅读时间 |
| 插件系统 | [插件概览](docs/blog/plugins/overview.md) | 博客、搜索、标签、RSS 与第三方插件规划 |
| 部署指南 | [GitHub Pages](docs/blog/deployment/github-pages.md) | 推荐的免费部署方式 |
| 部署指南 | [其他部署方式](docs/blog/deployment/self-hosted.md) | Cloudflare、Netlify、EdgeOne、GitLab、自托管 |
| 高级主题 | [性能优化](docs/blog/advanced/performance.md) | 构建与加载性能 |
| 高级主题 | [SEO 优化](docs/blog/advanced/seo.md) | 站点地图、元数据、结构化数据 |
| 高级主题 | [链接与脚注验证](docs/blog/advanced/validation.md) | 构建期断链检查与修复 |
| 其他 | [关于](docs/about.md) · [FAQ](docs/faq.md) · [案例展示](docs/showcase.md) | 项目说明、常见问题、使用案例 |

## 快速开始

环境要求：**Python 3.11+**（Zensical 0.0.74 的 `Requires-Python` 为 `>=3.11`）。

```powershell
# 1. 创建并激活虚拟环境
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. 安装依赖
python -m pip install -r requirements.txt

# 3. 本地预览（默认 http://localhost:8000）
zensical serve

# 4. 清理并构建到 site/
zensical build --clean
```

也可以使用仓库脚本，在构建前自动刷新导航：

```powershell
# 先生成 docs/SUMMARY.md，再运行 zensical serve
python scripts/docs.py serve

# 先生成 docs/SUMMARY.md，再运行 zensical build --clean
python scripts/docs.py build --clean
```

如果 PowerShell 禁止执行激活脚本，可以只对当前会话放行：

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\.venv\Scripts\Activate.ps1
```

## 项目结构

```text
zensical-template/
├─ zensical.toml                  # 站点配置：主题、Markdown 扩展、literate-nav
├─ requirements.txt               # Python 依赖
├─ scripts/
│  ├─ generate_summary.py         # 扫描 docs/ 生成 docs/SUMMARY.md
│  ├─ docs.py                     # 先生成 SUMMARY，再运行 zensical
│  └─ configure_site_url.py       # CI 中推导 GitHub Pages 的 site_url
├─ docs/
│  ├─ SUMMARY.md                  # literate-nav 导航（自动生成，不要手改）
│  ├─ index.md                    # 首页
│  ├─ about.md / faq.md           # 关于与常见问题
│  ├─ showcase.md                 # 案例展示
│  ├─ OFFICIAL_ALIGNMENT.md       # 维护者文档（不进入侧栏）
│  ├─ getting-started/            # 安装、CLI、迁移
│  ├─ tutorials/                  # 配置、主题、Markdown、博客
│  ├─ blog/
│  │  ├─ deployment/              # GitHub Pages、Cloudflare、Netlify 等
│  │  ├─ plugins/                 # 博客、搜索、标签、RSS
│  │  └─ advanced/                # 性能、SEO、i18n、评论、404 等
│  ├─ javascripts/                # 可选脚本（GitHub 卡片、KaTeX 等）
│  ├─ stylesheets/                # 可选样式
│  └─ overrides/                  # 主题模板覆盖（404、评论、页脚等）
├─ .github/workflows/docs.yml     # GitHub Actions 构建与 GitHub Pages 部署
└─ site/                          # 构建产物（自动生成，已被忽略）
```

## 导航：literate-nav + SUMMARY.md

侧边栏导航不在 `zensical.toml` 中手写，而是由 Zensical 内置的 `literate-nav` 插件读取 `docs/SUMMARY.md`：

```toml
[project.plugins.literate-nav]
nav_file = "SUMMARY.md"
```

`SUMMARY.md` 是普通 Markdown 列表，列表顺序就是侧栏顺序；嵌套层级每级使用 **4 个空格**。该文件由 `scripts/generate_summary.py` 扫描 `docs/` 自动生成，并在 `zensical.toml` 中通过 `exclude_docs` 排除，避免被构建成内容页。

生成规则：

1. 每个目录先输出 `index.md`（如果存在）；
2. 再输出子目录，按 `DIR_ORDER` 与自然排序排列；
3. 最后输出其余 Markdown 文件。

脚本中的几个配置：

- `DIR_TITLES`：目录在侧栏中的显示名，例如 `blog/deployment` → `部署指南`。
- `DIR_ORDER`：目录顺序，数字越小越靠前。
- `TITLE_OVERRIDES`：单个页面的导航标题。
- `NAV_EXCLUDE`：仍然构建、但不进入侧栏的维护者页面，例如 `OFFICIAL_ALIGNMENT.md`。

日常命令：

```powershell
# 生成或更新 docs/SUMMARY.md
python scripts/generate_summary.py

# 只检查是否与当前目录结构一致（过期时退出码为 1）
python scripts/generate_summary.py --check
```

新增页面后重新运行生成脚本即可；新增一级目录时，按需把它加入 `DIR_TITLES` / `DIR_ORDER`。

### 相对链接规则

`docs/` 子目录之间互相引用时，必须先用 `../` 回到 `docs/` 根，再定位目标：

```markdown
<!-- docs/blog/advanced/feature-parity.md 引用 docs/tutorials/configuration.md -->
[配置详解](../../tutorials/configuration.md)
```

错误写法（会变成断链）：

```markdown
[配置详解](../tutorials/configuration.md)
```

构建时 Zensical 会报告 `page does not exist` 或 `anchor does not exist`，提交前应确保构建零警告。

## 部署到 GitHub Pages

工作流文件：`.github/workflows/docs.yml`。推送到 `main` / `master`、创建 Pull Request 或手动触发 `workflow_dispatch` 时运行。

构建流程：

1. Checkout 仓库并安装 Python 依赖；
2. 运行 `python scripts/generate_summary.py`；
3. 运行 `python scripts/configure_site_url.py` 设置 `site_url`；
4. 配置 GitHub Pages；
5. 运行 `python -m zensical build --clean`；
6. 上传 `site/` 并发布到 `github-pages` 环境。

首次启用：

1. 打开仓库 **Settings → Pages**；
2. 将 **Build and deployment → Source** 设为 **GitHub Actions**；
3. 推送到 `main` / `master`，或在 Actions 页面手动运行 **Deploy Docs**。

`site_url` 的解析顺序：

1. 仓库变量 `SITE_URL`（适合自定义域名）；
2. 从 `GITHUB_REPOSITORY` 自动推导：
   - 普通仓库：`https://<owner>.github.io/<repo>/`
   - 用户/组织主页仓库：`https://<owner>.github.io/`
3. 两者都没有时保持 `zensical.toml` 原值。

使用自定义域名时，在 **Settings → Secrets and variables → Actions → Variables** 中添加 `SITE_URL`，例如：

```text
https://docs.example.com/
```

本地模拟 CI：

```powershell
$env:GITHUB_REPOSITORY = "owner/zensical-template"
python scripts/generate_summary.py
python scripts/configure_site_url.py
zensical build --clean
Remove-Item Env:GITHUB_REPOSITORY
```

> `configure_site_url.py` 会直接改写 `zensical.toml` 的 `site_url`；本地模拟后请恢复该文件或改回默认值。

## 常用配置

站点基础信息与主题在 `zensical.toml` 中设置：

```toml
[project]
site_name = "Zensical 中文教程"
site_url = "https://www.example.com/"
site_description = "最详细、最便捷、最前沿的 Zensical 中文教程"

[project.theme]
language = "zh"
```

已启用的常用能力：

- 即时导航与悬停预取；
- 侧栏分组、面包屑、返回顶部、上一页/下一页；
- 搜索结果高亮、右侧目录跟随滚动；
- 代码复制、代码注释、内容标签页；
- Admonition、Details、脚注、定义列表、任务列表；
- Mermaid 图表、数学公式、图标与 emoji。

配置项的完整说明见 [配置详解](docs/tutorials/configuration.md)，主题调整见 [主题定制](docs/tutorials/theme-customization.md)。

## 常见问题

### 构建时提示 `page does not exist`

检查相对链接是否正确。`docs/` 子目录中的页面必须先 `../` 回到 `docs/` 根，再定位目标页面。

### `SUMMARY.md` 被构建成了页面

确认 `zensical.toml` 中包含：

```toml
[project]
exclude_docs = """
SUMMARY.md
"""
```

### 新增页面后侧栏没有变化

运行 `python scripts/generate_summary.py`。如果正在预览，刷新页面；必要时重启 `zensical serve`。

### 手动修改 `SUMMARY.md` 后又被覆盖

这是预期行为。需要长期保留的顺序或标题，请修改 `scripts/generate_summary.py` 中的 `DIR_ORDER`、`DIR_TITLES` 或 `TITLE_OVERRIDES`。

### 嵌套列表没有生效

`literate-nav` 默认每级缩进 4 个空格，不要使用 2 个空格或 Tab。

更多问题见 [FAQ](docs/faq.md)。

## 内容来源与许可

- 教程内容整理自 [Wcowin/Zensical-Chinese-Tutorial](https://github.com/Wcowin/Zensical-Chinese-Tutorial)，上游项目以 MIT 许可发布。
- 官方文档：<https://zensical.org/docs/>
- 官方兼容性说明：<https://zensical.org/compatibility/>
- Zensical 路线图：<https://zensical.org/about/roadmap/>

欢迎提交 Issue 或 Pull Request 补充教程内容。
