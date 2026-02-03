#!/usr/bin/env python3

from __future__ import annotations

import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = REPO_ROOT / "papers"


def fail(msg: str) -> None:
    raise SystemExit(msg)


def validate_meta(meta_path: Path) -> None:
    data = json.loads(meta_path.read_text(encoding="utf-8"))
    required = ["title", "authors", "year", "venue", "url", "key_innovation", "slug"]
    missing = [k for k in required if not data.get(k)]
    if missing:
        fail(f"Missing keys {missing} in {meta_path}")

    slug = str(data["slug"])
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        fail(f"Invalid slug in {meta_path}: {slug}")

    year = int(data["year"])
    parts = meta_path.parent.relative_to(PAPERS_DIR).parts
    if len(parts) < 3:
        fail(f"Invalid folder structure for {meta_path}. Expected papers/<year>/<venue>/<slug>/")
    year_dir, venue_dir, slug_dir = parts[0], parts[1], parts[2]
    if str(year) != year_dir:
        fail(f"Year mismatch: meta has {year}, folder is {year_dir} ({meta_path})")
    if slug != slug_dir:
        fail(f"Slug mismatch: meta has {slug}, folder is {slug_dir} ({meta_path})")
    if str(data["venue"]).strip() != venue_dir:
        fail(f"Venue mismatch: meta has {data['venue']}, folder is {venue_dir} ({meta_path})")


def main() -> None:
    if not PAPERS_DIR.exists():
        return
    for meta in PAPERS_DIR.glob("**/meta.json"):
        validate_meta(meta)
        readme = meta.parent / "README.md"
        if not readme.exists():
            fail(f"Missing README.md for {meta.parent}")


if __name__ == "__main__":
    main()
