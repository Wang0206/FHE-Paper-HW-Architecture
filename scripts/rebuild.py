#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> None:
    p = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if p.returncode != 0:
        raise SystemExit(p.returncode)


def main() -> None:
    ap = argparse.ArgumentParser(description="Validate repo and rebuild the root index in one command")
    ap.add_argument("--check", action="store_true", help="Do not write; fail if README index would change")
    args = ap.parse_args()

    py = sys.executable or "python3"

    run([py, str(REPO_ROOT / "scripts" / "validate_repo.py")])

    build_cmd = [py, str(REPO_ROOT / "scripts" / "build_index.py")]
    if args.check:
        build_cmd.append("--check")
    run(build_cmd)


if __name__ == "__main__":
    main()
