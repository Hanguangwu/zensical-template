#!/usr/bin/env python3
"""Generate ``docs/SUMMARY.md`` for Zensical's literate-nav plugin.

The ``docs`` directory is the single source of truth. For every directory the
generator emits, in this order:

1. its ``index.md`` (when present), so it can act as the section landing page,
2. subdirectories that contain Markdown pages, sorted naturally,
3. the remaining Markdown files, sorted naturally.

Navigation labels come from front matter ``title``, then the first H1, then the
file or directory name **unchanged** -- ``AI`` stays ``AI``, ``EECS`` stays
``EECS`` and ``cpp`` stays ``cpp``.

Usage::

    python scripts/generate_summary.py            # write docs/SUMMARY.md
    python scripts/generate_summary.py --check    # fail if it is out of date
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DOCS_DIR = ROOT / "docs"
SUMMARY_NAME = "SUMMARY.md"
# Directories that never contain documentation pages.
SKIP_DIRS = {"__pycache__", "node_modules"}

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)
TITLE_RE = re.compile(r"^title\s*:\s*(.+?)\s*$", re.MULTILINE)
H1_RE = re.compile(r"^#\s+(.+?)\s*$")


def natural_key(value: str) -> tuple[tuple[int, object], ...]:
    """Sort ``2-`` before ``10-`` while keeping case-insensitive text order."""
    return tuple(
        (0, int(part)) if part.isdigit() else (1, part.casefold())
        for part in re.split(r"(\d+)", value)
    )


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


def label_for(path: Path, docs_dir: Path) -> str:
    """Label for a page or directory, preserving the name's original spelling."""
    if path.name == "index.md":
        return "Home" if path.parent == docs_dir else path.parent.name
    return path.stem


def title_for(path: Path, docs_dir: Path) -> str:
    return read_title(path) or label_for(path, docs_dir)


def is_visible(path: Path) -> bool:
    return not (path.name.startswith(".") or path.name in SKIP_DIRS)


def is_page(path: Path, exclude: Path) -> bool:
    return (
        path.is_file()
        and path.suffix.lower() == ".md"
        and path.name != SUMMARY_NAME
        and path.resolve() != exclude
    )


def has_pages(directory: Path, exclude: Path) -> bool:
    """Return whether *directory* contains any visible Markdown page."""
    for path in directory.rglob("*"):
        if not is_page(path, exclude):
            continue
        relative = path.relative_to(directory)
        if not any(part.startswith(".") or part in SKIP_DIRS for part in relative.parts):
            return True
    return False


def sorted_children(directory: Path, exclude: Path) -> tuple[list[Path], list[Path]]:
    directories: list[Path] = []
    files: list[Path] = []
    for child in directory.iterdir():
        if not is_visible(child):
            continue
        if child.is_dir():
            if has_pages(child, exclude):
                directories.append(child)
        elif is_page(child, exclude):
            files.append(child)
    directories.sort(key=lambda path: natural_key(path.name))
    files.sort(key=lambda path: natural_key(path.name))
    return directories, files


def page_line(path: Path, docs_dir: Path, depth: int) -> str:
    relative = path.relative_to(docs_dir).as_posix()
    return f"{'    ' * depth}- [{title_for(path, docs_dir)}]({relative})"


def render_directory(
    directory: Path,
    docs_dir: Path,
    exclude: Path,
    depth: int,
    include_index: bool = True,
) -> list[str]:
    lines: list[str] = []
    index = directory / "index.md"
    if include_index and index.is_file() and index.resolve() != exclude:
        lines.append(page_line(index, docs_dir, depth))

    directories, files = sorted_children(directory, exclude)
    for child in directories:
        child_index = child / "index.md"
        if child_index.is_file() and child_index.resolve() != exclude:
            lines.append(page_line(child_index, docs_dir, depth))
            lines.extend(render_directory(child, docs_dir, exclude, depth + 1, include_index=False))
        else:
            lines.append(f"{'    ' * depth}- {label_for(child, docs_dir)}")
            lines.extend(render_directory(child, docs_dir, exclude, depth + 1))

    for child in files:
        if child.name != "index.md":
            lines.append(page_line(child, docs_dir, depth))
    return lines


def build_summary(docs_dir: Path, exclude: Path) -> str:
    lines = render_directory(docs_dir, docs_dir, exclude, 0)
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

    output = args.output.resolve() if args.output else docs_dir / SUMMARY_NAME
    if output.is_dir():
        print(f"output path is a directory: {output}", file=sys.stderr)
        return 2
    if not output.parent.is_dir():
        print(f"output directory not found: {output.parent}", file=sys.stderr)
        return 2

    content = build_summary(docs_dir, output)
    current = output.read_text(encoding="utf-8") if output.is_file() else None

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
