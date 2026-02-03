#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], *, cwd: Path = REPO_ROOT) -> str:
    p = subprocess.run(cmd, cwd=str(cwd), text=True, capture_output=True)
    if p.returncode != 0:
        raise SystemExit((p.stdout + "\n" + p.stderr).strip() or f"Command failed: {' '.join(cmd)}")
    return p.stdout.strip()


def has_changes() -> bool:
    out = run(["git", "status", "--porcelain"])  # empty means clean
    return bool(out.strip())


def main() -> None:
    ap = argparse.ArgumentParser(
        description=(
            "Optional helper: create a branch, rebuild index, validate, commit, and optionally push / open a PR."
        )
    )
    ap.add_argument(
        "--paper-dir",
        action="append",
        default=[],
        help="Paper folder(s) to stage (e.g., papers/2024/MICRO/reed-chiplet-accelerator). Can be repeated.",
    )
    ap.add_argument("--branch", type=str, help="Branch name to create/use")
    ap.add_argument("--message", type=str, help="Commit message")
    ap.add_argument("--push", action="store_true", help="Push branch to origin")
    ap.add_argument("--pr", action="store_true", help="Create PR using GitHub CLI (gh)")
    ap.add_argument("--pr-title", type=str, help="PR title (used with --pr)")
    ap.add_argument("--pr-body", type=str, help="PR body (used with --pr)")
    args = ap.parse_args()

    if not (REPO_ROOT / ".git").exists():
        raise SystemExit("Not a git repo (.git not found). Clone the repo normally to use this helper.")

    if shutil.which("git") is None:
        raise SystemExit("git is not available in PATH")

    # Create/switch branch
    if args.branch:
        branch = args.branch.strip()
    else:
        branch = "update-papers"

    current_branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    if current_branch != branch:
        # If branch exists, checkout; otherwise create
        existing = run(["git", "branch", "--list", branch])
        if existing.strip():
            run(["git", "checkout", branch])
        else:
            run(["git", "checkout", "-b", branch])

    if not has_changes():
        raise SystemExit("No changes detected. Add your paper files first.")

    # Validate and rebuild index
    run(["python3", "scripts/rebuild.py"])

    # Stage files
    stage_paths: list[str] = []
    if args.paper_dir:
        stage_paths.extend([p.strip() for p in args.paper_dir if p.strip()])
    else:
        stage_paths.append("papers")
    stage_paths.append("README.md")

    run(["git", "add", "--"] + stage_paths)

    msg = args.message.strip() if args.message else "Update papers and index"
    run(["git", "commit", "-m", msg])

    if args.push:
        run(["git", "push", "-u", "origin", branch])

    if args.pr:
        if shutil.which("gh") is None:
            raise SystemExit("GitHub CLI (gh) not found. Install it or create the PR manually.")
        title = args.pr_title or msg
        body = args.pr_body or "Automated update: add/update paper entries and rebuild index."
        # Ensure auth/remote config handled by user's environment.
        run(["gh", "pr", "create", "--title", title, "--body", body])

    # Print next steps for users
    if not args.push:
        print(f"Branch ready: {branch}\nNext: git push -u origin {branch}")
    elif not args.pr:
        print("Pushed. Next: open a PR on GitHub (or rerun with --pr if you have gh installed).")


if __name__ == "__main__":
    main()
