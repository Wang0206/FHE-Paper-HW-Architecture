# Contributing Guide

This repository tracks important papers on **FHE hardware acceleration**, organized by **year** and **venue**.

## What to add in a PR

Each paper should have:

1. A folder under `papers/<year>/<venue>/<slug>/`
2. `meta.json` with consistent metadata
3. A per-paper `README.md` summarizing the paper (see required sections below)
4. The root index in `README.md` updated via script

## Folder naming conventions

- `year`: 4-digit year, e.g., `2024`
- `venue`: one of `ISCA`, `MICRO`, `HPCA`, `ASPLOS`, `DAC`, `DATE`, `FPGA` (case-sensitive)
- `slug`: lowercase kebab-case, e.g., `reed-chiplet-accelerator`

Example:

`papers/2024/MICRO/reed-chiplet-accelerator/`

## Metadata format (`meta.json`)

Required keys:

- `title`
- `authors`
- `year`
- `venue`
- `url` (DOI URL or publisher page)
- `key_innovation` (1–2 sentence)

Recommended keys:

- `doi`
- `pdf_url`
- `hardware` (e.g., `["ASIC", "FPGA", "GPU", "PIM", "Chiplet"]`)
- `schemes` (e.g., `["TFHE", "CKKS", "BFV", "FV"]`)
- `tags` (free-form keywords)

## Per-paper README requirements

The per-paper `README.md` should include at minimum:

- Paper info block (title, authors, venue/year, links)
- `Key Innovation` (from metadata)
- `Repo Summary` (short, bullet-based)
- `Method / Architecture` (what the accelerator does, how it maps to FHE ops)
- `Highlights` (what’s new vs prior work)
- `Results` (numbers if available; otherwise leave TODO)

Notes:

- If you **quote the original abstract verbatim**, ensure it is publicly available and keep it clearly labeled as “Original Abstract (verbatim)”.
- Otherwise, write your own summary.

## Recommended workflow (scripts)

### Step 1: Draft files using templates (recommended)

We intentionally keep generation **manual + transparent**:

1. Use a web-based LLM (ChatGPT/Claude/etc.) and upload the paper PDF.
2. Ask it to fill in our templates:

- Template A: `templates/meta.json.template`
- Template B: `templates/paper_readme.md`

The root `README.md` contains a ready-to-copy prompt example.

### Step 2: Put the files into the repo

Create a folder:

`papers/<year>/<venue>/<slug>/`

Then add:

- `meta.json`
- `README.md`

### Step 3: Validate + rebuild the root index

```bash
python3 scripts/validate_repo.py
python3 scripts/build_index.py
```

## Optional: submit a PR via script

If you have the repo cloned locally (with `.git`) you can use:

```bash
python3 scripts/submit_pr.py \
  --paper-dir papers/<year>/<venue>/<slug> \
  --branch add-<slug> \
  --message "Add <slug>" \
  --push
```

If you also have GitHub CLI (`gh`) installed and authenticated:

```bash
python3 scripts/submit_pr.py \
  --paper-dir papers/<year>/<venue>/<slug> \
  --branch add-<slug> \
  --message "Add <slug>" \
  --push --pr --pr-title "Add <paper title>" \
  --pr-body "Adds meta.json + per-paper README; rebuilds index."
```

## Pre-PR checks

Run:

```bash
python3 scripts/validate_repo.py
python3 scripts/build_index.py --check
```
