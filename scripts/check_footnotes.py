#!/usr/bin/env python3
"""Check footnote integrity across canonical Markdown files.

For each .md file under the canonical directories (manuscript/, appendices/,
references/, style/), this script verifies that every footnote reference
of the form [^N^] used in the body has a corresponding definition line
of the form [^N^]: ... at the bottom of the file.

It also reports definitions that are never referenced (potential dead refs),
unless --allow-unused is passed.

Exit code is non-zero if any mismatch is found.
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_DIRS = ["manuscript", "appendices", "references", "style"]

# Matches footnote references like [^2^] or [^69^]
REF_RE = re.compile(r"\[\^(\d+)\^\]")
# Matches footnote definitions like [^2^]: at start of a line
DEF_RE = re.compile(r"^\[\^(\d+)\^\]:")


def check_file(filepath: Path) -> list[str]:
    """Return a list of error messages for the given file (empty if OK)."""
    text = filepath.read_text(encoding="utf-8")
    errors = []

    # Collect referenced footnote IDs from the entire text,
    # but exclude lines that are definitions themselves.
    referenced: set[str] = set()
    for line in text.splitlines():
        if DEF_RE.match(line):
            continue
        for m in REF_RE.finditer(line):
            referenced.add(m.group(1))

    # Collect defined footnote IDs
    defined: set[str] = set()
    for line in text.splitlines():
        m = DEF_RE.match(line)
        if m:
            defined.add(m.group(1))

    # Undefined references
    undefined = referenced - defined
    for fn_id in sorted(undefined, key=int):
        errors.append(f"  undefined: [^{fn_id}^] is referenced but never defined")

    # Unused definitions (reported as warnings, not errors, unless --strict)
    unused = defined - referenced
    for fn_id in sorted(unused, key=int):
        errors.append(f"  unused:    [^{fn_id}^] is defined but never referenced")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check footnote integrity.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat unused definitions as errors (default: warnings).",
    )
    args = parser.parse_args()

    all_files: list[Path] = []
    for d in CANONICAL_DIRS:
        dirpath = REPO_ROOT / d
        if dirpath.is_dir():
            all_files.extend(sorted(dirpath.rglob("*.md")))

    total_errors = 0
    total_warnings = 0

    for f in all_files:
        rel = f.relative_to(REPO_ROOT)
        errors = check_file(f)
        if not errors:
            continue
        print(f"{rel}:")
        for e in errors:
            if e.strip().startswith("undefined:"):
                total_errors += 1
                print(f"  ERROR {e.strip()}")
            else:
                total_warnings += 1
                level = "ERROR" if args.strict else "WARN"
                print(f"  {level} {e.strip()}")

    print(f"\n{total_errors} error(s), {total_warnings} warning(s)")

    if total_errors > 0 or (args.strict and total_warnings > 0):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
