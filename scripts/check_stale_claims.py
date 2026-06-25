#!/usr/bin/env python3
"""Scan canonical Markdown files for forbidden/stale strings.

This script enforces the editorial discipline of the manuscript by checking
that known-bad or stale phrasings do not reappear in canonical files
(manuscript/, appendices/, references/, style/, README.md, CHANGELOG.md).

Archive files are NOT scanned -- they are superseded drafts and are
expected to contain old language. They are non-canonical.

Exit code is non-zero if any forbidden string is found.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Files/directories to scan (canonical only)
# CHANGELOG.md is excluded because it legitimately references old/stale strings
# to document what was fixed.
CANONICAL_PATHS = [
    "manuscript",
    "appendices",
    "references",
    "style",
    "README.md",
]

# Forbidden strings: (pattern, reason)
# Each pattern is matched case-insensitively as a substring.
FORBIDDEN = [
    ("CA23140", "Wrong COST Action number -- should be CA23130"),
    ("April 25\u201326", "Aguadilla date compromise -- use AARO date April 26, 2013"),
    ("April 25-26", "Aguadilla date compromise -- use AARO date April 26, 2013"),
    ("few kilograms", "Misleading QEC mass threshold -- use 'macroscopic degrees of freedom' framing"),
    ("archived for lack", "Imprecise AARO FY2024 wording -- use 'lacked sufficient data and were placed in the Active Archive'"),
    ("444 cases archived", "Imprecise AARO FY2024 wording -- use 'lacked sufficient data and were placed in the Active Archive'"),
    ("444 archived", "Imprecise AARO FY2024 wording -- use 'lacked sufficient data and were placed in the Active Archive'"),
    ("AARO-GOFAST-2024", "Wrong Go Fast citation key -- use AARO-GOFAST-2025"),
    ("GoFast (2024)", "Wrong Go Fast case-resolution year -- use February 6, 2025"),
    ("GoFast (2015)*, 2024", "Wrong Go Fast reference -- use Case Resolution: “Go Fast”, February 6, 2025"),
    ("Case Resolution: GoFast (2015)", "Wrong Go Fast title/date -- use Case Resolution: “Go Fast”, February 6, 2025"),
    ("ICIG process remains ongoing", "Stale/stale-process claim -- use 'no public ICIG conclusion has been released'"),
    ("2025 AARO Workshop", "Uncited freshness claim -- cite or remove"),
    ("archived June 2026", "False precision -- use 'accessed June 2026' unless a real archive URL exists"),
]


def scan_file(filepath: Path) -> list[tuple[int, str, str]]:
    """Return list of (line_number, matched_text, reason) for forbidden strings."""
    hits = []
    text = filepath.read_text(encoding="utf-8")
    for i, line in enumerate(text.splitlines(), start=1):
        for pattern, reason in FORBIDDEN:
            if pattern.lower() in line.lower():
                hits.append((i, pattern, reason))
    return hits


def main() -> int:
    all_files: list[Path] = []
    for p in CANONICAL_PATHS:
        full = REPO_ROOT / p
        if full.is_dir():
            all_files.extend(sorted(full.rglob("*.md")))
        elif full.is_file() and full.suffix == ".md":
            all_files.append(full)

    total_hits = 0
    for f in all_files:
        rel = f.relative_to(REPO_ROOT)
        hits = scan_file(f)
        if not hits:
            continue
        print(f"{rel}:")
        for lineno, matched, reason in hits:
            total_hits += 1
            print(f"  line {lineno}: '{matched}' -- {reason}")

    if total_hits > 0:
        print(f"\n{total_hits} forbidden string(s) found in canonical files.")
        return 1

    print("No forbidden strings found in canonical files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
