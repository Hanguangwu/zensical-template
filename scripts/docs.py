#!/usr/bin/env python3
"""Run Zensical after regenerating docs/SUMMARY.md.

Usage:
    python scripts/docs.py serve
    python scripts/docs.py build --clean
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] not in {"serve", "build"}:
        print("Usage: python scripts/docs.py {serve|build} [zensical arguments...]")
        return 2

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_summary.py")],
        check=True,
        cwd=ROOT,
    )
    return subprocess.call(
        [sys.executable, "-m", "zensical", *sys.argv[1:]],
        cwd=ROOT,
    )


if __name__ == "__main__":
    raise SystemExit(main())
