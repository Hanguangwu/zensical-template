#!/usr/bin/env python3
"""Configure zensical.toml site_url for GitHub Pages builds.

Resolution order:
1. SITE_URL environment variable (for custom domains or manual overrides),
2. GitHub repository name from GITHUB_REPOSITORY,
3. no change outside CI if neither is available.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "zensical.toml"


def resolve_site_url() -> str | None:
    explicit = os.environ.get("SITE_URL", "").strip()
    if explicit:
        return explicit.rstrip("/") + "/"

    repository = os.environ.get("GITHUB_REPOSITORY", "").strip()
    if not repository:
        return None

    owner, _, name = repository.partition("/")
    if not owner or not name:
        return None

    if name.lower() == f"{owner.lower()}.github.io":
        return f"https://{owner}.github.io/"
    return f"https://{owner}.github.io/{name}/"


def main() -> int:
    site_url = resolve_site_url()
    if site_url is None:
        print("GITHUB_REPOSITORY/SITE_URL not set; leaving site_url unchanged")
        return 0

    text = CONFIG.read_text(encoding="utf-8")
    updated, count = re.subn(
        r'^site_url = ".*"$',
        f'site_url = "{site_url}"',
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if count != 1:
        print("Could not find site_url in zensical.toml", file=sys.stderr)
        return 1

    if updated != text:
        CONFIG.write_text(updated, encoding="utf-8", newline="\n")
    print(f"site_url = {site_url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
