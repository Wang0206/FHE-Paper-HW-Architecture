#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = REPO_ROOT / "papers"


def validate_slug(slug: str) -> None:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise SystemExit("Invalid --slug. Use lowercase kebab-case, e.g., reed-chiplet-accelerator")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--venue", type=str, required=True)
    ap.add_argument("--slug", type=str, required=True)
    ap.add_argument("--title", type=str, required=True)
    ap.add_argument("--authors", type=str, required=True)
    ap.add_argument("--url", type=str, required=True)
    ap.add_argument("--key-innovation", type=str, required=True)
    ap.add_argument("--doi", type=str)
    ap.add_argument("--pdf-url", type=str)
    ap.add_argument("--llm", action="store_true", help="Generate README via LLM (requires OPENAI_API_KEY)")
    args = ap.parse_args()

    validate_slug(args.slug)

    paper_dir = PAPERS_DIR / str(args.year) / args.venue.strip() / args.slug.strip()
    paper_dir.mkdir(parents=True, exist_ok=False)

    meta = {
        "title": args.title.strip(),
        "authors": args.authors.strip(),
        "year": args.year,
        "venue": args.venue.strip(),
        "slug": args.slug.strip(),
        "url": args.url.strip(),
        "key_innovation": args.key_innovation.strip(),
        "doi": args.doi.strip() if args.doi else None,
        "pdf_url": args.pdf_url.strip() if args.pdf_url else None,
        "date_added": str(date.today()),
    }
    meta_path = paper_dir / "meta.json"
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Generate README (template by default)
    import subprocess

    cmd = [
        "python3",
        str(REPO_ROOT / "scripts" / "generate_paper_readme.py"),
        str(paper_dir.relative_to(REPO_ROOT)),
    ]
    if args.llm:
        cmd.append("--llm")
    subprocess.check_call(cmd)

    # Update root index
    subprocess.check_call(["python3", str(REPO_ROOT / "scripts" / "build_index.py")])


if __name__ == "__main__":
    main()
