#!/usr/bin/env python3
"""Generate docs/SUMMARY.md for Zensical's literate-nav plugin.

The docs directory is the source of truth. For every directory, the generator
emits:

1. ``index.md`` when present (so it can act as the section landing page),
2. child directories sorted naturally,
3. remaining Markdown files sorted naturally.

Titles are resolved from front matter ``title``, then the first H1, then a
humanized file/directory name. ``TITLE_OVERRIDES`` and ``DIR_TITLES`` can be
used for navigation labels that intentionally differ from page headings, and
``NAV_EXCLUDE`` keeps maintainer-only pages out of the sidebar while still
building them.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DOCS_DIR = ROOT / "docs"
DEFAULT_OUTPUT_NAME = "SUMMARY.md"

SKIP_DIRS = {"__pycache__", "node_modules"}
# Pages that are still built (so links work) but intentionally omitted from nav.
NAV_EXCLUDE = {"OFFICIAL_ALIGNMENT.md"}
# Directory order; keys are paths relative to docs/. Lower numbers come first.
DIR_ORDER = {
    "getting-started": 0,
    "tutorials": 1,
    "blog": 2,
    "blog/deployment": 0,
    "blog/plugins": 1,
    "blog/advanced": 2,
}
# Human-friendly navigation group names for directories.
DIR_TITLES = {
    "getting-started": "快速开始",
    "tutorials": "核心教程",
    "blog": "博客",
    "blog/advanced": "高级主题",
    "blog/plugins": "插件系统",
    "blog/deployment": "部署指南",
}
TITLE_OVERRIDES = {
    "index.md": "首页",
    "about.md": "关于",
    "faq.md": "常见问题",
    "showcase.md": "案例展示",
}

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)
TITLE_RE = re.compile(r"^title\s*:\s*(.+?)\s*$", re.MULTILINE)
H1_RE = re.compile(r"^#\s+(.+?)\s*$")


def natural_key(value: str) -> list[object]:
    """Sort ``02-`` before ``10-`` instead of lexicographically."""
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", value)]


def clean_title(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value.strip()


def read_title(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    front_matter = FRONT_MATTER_RE.match(text)
    if front_matter:
        match = TITLE_RE.search(front_matter.group(1))
        if match:
            return clean_title(match.group(1))
        text = text[front_matter.end() :]

    in_fence = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = H1_RE.match(line)
        if match:
            return clean_title(match.group(1))
    return None


def fallback_title(path: Path) -> str:
    name = path.parent.name if path.name == "index.md" else path.stem
    name = name or "Home"
    return name.replace("-", " ").replace("_", " ").strip().title()


def title_for(path: Path, docs_dir: Path) -> str:
    relative = path.relative_to(docs_dir).as_posix()
    return TITLE_OVERRIDES.get(relative) or read_title(path) or fallback_title(path)


def is_markdown(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() == ".md" and path.name != DEFAULT_OUTPUT_NAME


def is_skipped(path: Path) -> bool:
    return any(part.startswith(".") or part in SKIP_DIRS for part in path.parts)


def is_nav_excluded(path: Path, docs_dir: Path) -> bool:
    return path.relative_to(docs_dir).as_posix() in NAV_EXCLUDE


def has_markdown(directory: Path) -> bool:
    for path in directory.rglob("*"):
        if not is_markdown(path):
            continue
        if is_skipped(path.relative_to(directory)):
            continue
        return True
    return False


def sorted_children(directory: Path, docs_dir: Path) -> tuple[list[Path], list[Path]]:
    directories: list[Path] = []
    files: list[Path] = []
    for child in directory.iterdir():
        if child.name.startswith(".") or child.name in SKIP_DIRS:
            continue
        if child.is_dir():
            if has_markdown(child):
                directories.append(child)
        elif is_markdown(child) and not is_nav_excluded(child, docs_dir):
            files.append(child)
    directories.sort(
        key=lambda path: (
            DIR_ORDER.get(path.relative_to(docs_dir).as_posix(), 100),
            natural_key(path.name),
        )
    )
    files.sort(key=lambda path: natural_key(path.name))
    return directories, files


def page_line(path: Path, docs_dir: Path, depth: int) -> str:
    relative = path.relative_to(docs_dir).as_posix()
    return f"{'    ' * depth}- [{title_for(path, docs_dir)}]({relative})"


def render_directory(directory: Path, docs_dir: Path, depth: int, include_index: bool = True) -> list[str]:
    lines: list[str] = []
    index = directory / "index.md"
    if include_index and index.is_file():
        lines.append(page_line(index, docs_dir, depth))

    directories, files = sorted_children(directory, docs_dir)
    for child in directories:
        child_index = child / "index.md"
        if child_index.is_file():
            lines.append(page_line(child_index, docs_dir, depth))
        else:
            relative = child.relative_to(docs_dir).as_posix()
            lines.append(f"{'    ' * depth}- {DIR_TITLES.get(relative, fallback_title(child))}")
        lines.extend(render_directory(child, docs_dir, depth + 1, include_index=False))

    for child in files:
        if child.name != "index.md":
            lines.append(page_line(child, docs_dir, depth))
    return lines


def build_summary(docs_dir: Path) -> str:
    lines = render_directory(docs_dir, docs_dir, 0)
    return "# Summary\n\n" + "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-dir", type=Path, default=DEFAULT_DOCS_DIR, help="Documentation source directory")
    parser.add_argument("--output", type=Path, help="Output file (default: <docs-dir>/SUMMARY.md)")
    parser.add_argument("--check", action="store_true", help="Fail if the output file is not up to date")
    args = parser.parse_args()

    docs_dir = args.docs_dir.resolve()
    if not docs_dir.is_dir():
        print(f"docs directory not found: {docs_dir}", file=sys.stderr)
        return 2

    output = args.output.resolve() if args.output else docs_dir / DEFAULT_OUTPUT_NAME
    content = build_summary(docs_dir)
    current = output.read_text(encoding="utf-8") if output.exists() else None

    if args.check:
        if current != content:
            print(f"{output} is out of date; run: python scripts/generate_summary.py", file=sys.stderr)
            return 1
        print(f"{output} is up to date")
        return 0

    if current == content:
        print(f"{output} is up to date")
        return 0

    output.write_text(content, encoding="utf-8", newline="\n")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
