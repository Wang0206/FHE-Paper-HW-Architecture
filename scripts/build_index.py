#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = REPO_ROOT / "papers"
ROOT_README = REPO_ROOT / "README.md"

INDEX_START = "<!-- INDEX:START -->"
INDEX_END = "<!-- INDEX:END -->"

TOC_HEADER = "## Table of Contents"


@dataclass(frozen=True)
class Paper:
    title: str
    authors: str
    year: int
    venue: str
    url: str
    key_innovation: str
    slug: str
    path: Path
    doi: str | None = None


def iter_meta_files() -> Iterable[Path]:
    if not PAPERS_DIR.exists():
        return []
    return PAPERS_DIR.glob("**/meta.json")


def load_paper(meta_path: Path) -> Paper:
    data = json.loads(meta_path.read_text(encoding="utf-8"))
    required = ["title", "authors", "year", "venue", "url", "key_innovation", "slug"]
    missing = [k for k in required if not data.get(k)]
    if missing:
        raise ValueError(f"Missing required keys in {meta_path}: {missing}")

    year = int(data["year"])
    venue = str(data["venue"]).strip()
    slug = str(data["slug"]).strip()

    return Paper(
        title=str(data["title"]).strip(),
        authors=str(data["authors"]).strip(),
        year=year,
        venue=venue,
        url=str(data["url"]).strip(),
        key_innovation=str(data["key_innovation"]).strip(),
        slug=slug,
        doi=str(data.get("doi")).strip() if data.get("doi") else None,
        path=meta_path.parent,
    )


def collect_papers() -> List[Paper]:
    papers: List[Paper] = []
    for meta in iter_meta_files():
        papers.append(load_paper(meta))
    return papers


def paper_rel_link(p: Paper) -> str:
    rel = p.path.relative_to(REPO_ROOT).as_posix()
    return f"{rel}/README.md"


def render_by_year(papers: List[Paper]) -> str:
    by_year: Dict[int, List[Paper]] = {}
    for p in papers:
        by_year.setdefault(p.year, []).append(p)

    lines: List[str] = []
    for year in sorted(by_year.keys(), reverse=True):
        lines.append(f"\n## {year}\n")
        year_papers = by_year[year]
        by_venue: Dict[str, List[Paper]] = {}
        for p in year_papers:
            by_venue.setdefault(p.venue, []).append(p)

        for venue in sorted(by_venue.keys()):
            lines.append(f"### {venue} {year}")
            venue_papers = sorted(by_venue[venue], key=lambda x: x.title.lower())
            for p in venue_papers:
                link = paper_rel_link(p)
                lines.append(
                    f"- **Title:** [{p.title}]({link})  \n"
                    f"  **Authors:** {p.authors}  \n"
                    f"  **Link:** {p.url}  \n"
                    f"  **Key Innovation:** {p.key_innovation}"
                )
            lines.append("")

    lines.append("\n")
    return "\n".join(lines).lstrip("\n")


def render_by_venue(papers: List[Paper]) -> str:
    by_venue: Dict[str, List[Paper]] = {}
    for p in papers:
        by_venue.setdefault(p.venue, []).append(p)

    lines: List[str] = []
    for venue in sorted(by_venue.keys()):
        lines.append(f"\n## {venue}\n")
        venue_papers = by_venue[venue]
        by_year: Dict[int, List[Paper]] = {}
        for p in venue_papers:
            by_year.setdefault(p.year, []).append(p)

        for year in sorted(by_year.keys(), reverse=True):
            lines.append(f"### {venue} {year}")
            year_papers = sorted(by_year[year], key=lambda x: x.title.lower())
            for p in year_papers:
                link = paper_rel_link(p)
                lines.append(
                    f"- **Title:** [{p.title}]({link})  \n"
                    f"  **Authors:** {p.authors}  \n"
                    f"  **Link:** {p.url}  \n"
                    f"  **Key Innovation:** {p.key_innovation}"
                )
            lines.append("")

    lines.append("\n")
    return "\n".join(lines).lstrip("\n")


def render_index(papers: List[Paper]) -> str:
    if not papers:
        return "(No papers yet. Add one under `papers/<year>/<venue>/<slug>/`.)\n"

    parts = [
        "# Index (by Year)\n",
        render_by_year(papers).rstrip() + "\n",
        "# Index (by Venue)\n",
        render_by_venue(papers).rstrip() + "\n",
    ]
    return "\n".join(parts).rstrip() + "\n"


def render_toc(papers: List[Paper]) -> str:
    years = sorted({p.year for p in papers}, reverse=True)
    venues = sorted({p.venue for p in papers})

    lines: List[str] = []
    lines.append("- [Repository Layout](#repository-layout)")

    lines.append("- [Index (by Year)](#index-by-year)")
    for y in years:
        lines.append(f"  - [{y}](#{y})")

    lines.append("- [Index (by Venue)](#index-by-venue)")
    for v in venues:
        lines.append(f"  - [{v}](#{slugify_anchor(v)})")

    lines.append("- [Contributing](#contributing)")
    lines.append("- [License](#license)")

    return "\n".join(lines).rstrip() + "\n"


def slugify_anchor(text: str) -> str:
    # Best-effort GitHub-style anchor slug for typical venue strings.
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s


def replace_index_block(readme_text: str, new_block: str) -> str:
    if INDEX_START not in readme_text or INDEX_END not in readme_text:
        raise RuntimeError("Root README is missing INDEX markers.")
    pattern = re.compile(
        re.escape(INDEX_START) + r".*?" + re.escape(INDEX_END),
        flags=re.DOTALL,
    )
    replacement = f"{INDEX_START}\n\n{new_block.rstrip()}\n\n{INDEX_END}"
    return pattern.sub(replacement, readme_text, count=1)


def replace_toc_section(readme_text: str, new_toc: str) -> str:
    if TOC_HEADER not in readme_text:
        raise RuntimeError("Root README is missing the Table of Contents header.")

    # Replace everything between the TOC header and the next H2 header.
    pattern = re.compile(
        r"(^## Table of Contents[ \t]*\n)(.*?)(?=^##\s)",
        flags=re.DOTALL | re.MULTILINE,
    )
    m = pattern.search(readme_text)
    if not m:
        raise RuntimeError("Failed to locate the Table of Contents section to replace.")

    replacement = f"{m.group(1)}\n{new_toc.rstrip()}\n\n"
    return pattern.sub(replacement, readme_text, count=1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="Do not write; fail if README would change")
    args = ap.parse_args()

    papers = collect_papers()
    new_block = render_index(papers)
    new_toc = render_toc(papers)

    current = ROOT_README.read_text(encoding="utf-8")
    updated = replace_index_block(current, new_block)
    updated = replace_toc_section(updated, new_toc)

    if args.check:
        if updated != current:
            raise SystemExit(
                "README.md (TOC and/or index) is out of date. Run: python3 scripts/build_index.py"
            )
        return

    ROOT_README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
