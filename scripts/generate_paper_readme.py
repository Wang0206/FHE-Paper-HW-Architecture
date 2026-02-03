#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import textwrap
import urllib.request
from pathlib import Path
from typing import Any, Dict


REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = (REPO_ROOT / "templates" / "paper_readme.md").read_text(encoding="utf-8")


def render_template(meta: Dict[str, Any]) -> str:
    doi_line = f"**DOI:** {meta.get('doi')}  \\n+" if meta.get("doi") else ""
    pdf_line = f"**PDF:** {meta.get('pdf_url')}  \\n+" if meta.get("pdf_url") else ""
    out = TEMPLATE
    out = out.replace("{{title}}", str(meta.get("title", "")))
    out = out.replace("{{authors}}", str(meta.get("authors", "")))
    out = out.replace("{{venue}}", str(meta.get("venue", "")))
    out = out.replace("{{year}}", str(meta.get("year", "")))
    out = out.replace("{{url}}", str(meta.get("url", "")))
    out = out.replace("{{key_innovation}}", str(meta.get("key_innovation", "")))
    out = out.replace("{{doi_line}}", doi_line)
    out = out.replace("{{pdf_line}}", pdf_line)
    return out


def call_openai(prompt: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")

    url = f"{base_url}/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You write concise, factual paper summaries for an FHE hardware accelerator paper repository."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        body = resp.read().decode("utf-8")
    parsed = json.loads(body)
    return parsed["choices"][0]["message"]["content"]


def llm_prompt(meta: Dict[str, Any]) -> str:
    title = meta.get("title", "")
    venue = meta.get("venue", "")
    year = meta.get("year", "")
    url = meta.get("url", "")
    key = meta.get("key_innovation", "")

    return textwrap.dedent(
        f"""
        Generate a per-paper README in Markdown for a repository about FHE hardware accelerators.

        Constraints:
        - Be careful: do NOT invent numeric results. If not known, write TODO.
        - Use short bullets and clear section headings.
        - Keep it neutral and technical.

        Paper metadata:
        - Title: {title}
        - Venue/Year: {venue} {year}
        - URL: {url}
        - Key innovation: {key}

        Required sections:
        - Key Innovation
        - Repo Summary (3–6 bullets)
        - Method / Architecture
        - Highlights
        - Results (TODO if unknown)
        - Notes
        - BibTeX (TODO)
        """
    ).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("paper_dir", help="Paper folder containing meta.json")
    ap.add_argument("--llm", action="store_true", help="Use OpenAI-compatible API to draft the README")
    args = ap.parse_args()

    paper_dir = (REPO_ROOT / args.paper_dir).resolve() if not args.paper_dir.startswith("/") else Path(args.paper_dir)
    meta_path = paper_dir / "meta.json"
    if not meta_path.exists():
        raise SystemExit(f"meta.json not found: {meta_path}")

    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    readme_path = paper_dir / "README.md"

    if args.llm:
        content = call_openai(llm_prompt(meta))
    else:
        content = render_template(meta)

    readme_path.write_text(content.rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
