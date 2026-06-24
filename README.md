# UAP Manuscript: A Disciplined Assessment

A rigorous, evidence-bounded analysis of Unidentified Anomalous Phenomena (UAP) claims, separating credible anomalies from verified origins, classified allegations from evidence, and physics vocabulary from engineering reality.

## Structure

```text
uap/
├── README.md                          ← you are here
├── CHANGELOG.md                       ← revision history
├── LICENSE                            ← CC BY-ND 4.0
├── Makefile                           ← lint, check-refs, check-stale, build
├── package.json                       ← markdownlint-cli dependency
├── .markdownlint.json                 ← lint configuration
├── manuscript/
│   └── uap-comprehensive.md           ← main manuscript (4 parts)
├── appendices/
│   ├── a-evidence-cases.md            ← case summaries & evidentiary analysis
│   ├── b-physics-boundaries.md        ← the five real physics gaps
│   └── c-speculative-framework.md     ← conditional speculative framework
├── style/
│   └── editorial-principles.md        ← 12 principles, forbidden phrases, razor checklist
├── references/
│   ├── references.md                  ← consolidated bibliography with URLs/DOIs
│   └── source-anchors.md              ← high-risk reference facts for verification
├── scripts/
│   ├── check_footnotes.py             ← verify footnote definitions match references
│   └── check_stale_claims.py          ← scan for forbidden/stale strings
└── archive/
    ├── README.md                      ← non-canonical warning
    ├── uap-physics-map-bridge.md      ← original physics deep dive (superseded)
    ├── uap-speculative-framework.md   ← original speculative framework (superseded)
    ├── uap-missing-floor.md           ← original missing-floor essay (superseded)
    ├── uap-evidence-rebuttal.md       ← original evidence rebuttal (superseded)
    └── evidence-problem-stitched-draft.md  ← early stitched draft (superseded)
```

## Archive (Non-Canonical)

The `archive/` directory contains superseded drafts retained for development history. These files are **not canonical** and contain known factual defects that have been corrected in the canonical versions. See `archive/README.md` for the full warning and file-to-successor mapping.

**For public release:** move `archive/` to a separate branch (e.g. `git checkout -b archive-history && git push origin archive-history`) and remove it from `main`. This prevents search engines and readers from landing on stale drafts. The `make lint` and `make check-stale` commands already exclude `archive/`.

## Reading Guide

- **New to the manuscript?** Start with `manuscript/uap-comprehensive.md` — it is self-contained and covers all four parts: the evidence record, the physics gaps, the conditional speculative framework, and the editorial principles.
- **Want the case details?** See `appendices/a-evidence-cases.md` for standalone summaries of Aguadilla, GoFast, Nimitz, the Grusch/ICIG process, and AARO's SAP authority.
- **Want the physics?** See `appendices/b-physics-boundaries.md` for the five genuine open problems in physics that any UAP explanation would need to address, plus the experimental frontier and decoherence dynamics.
- **Want the speculative framework?** See `appendices/c-speculative-framework.md` for the conditional exploration of what physics would need to permit — clearly marked as speculation with warning blocks.
- **Writing about UAP?** See `style/editorial-principles.md` for the 12 editorial principles, forbidden phrases, and the razor checklist.

## Core Thesis

1. **Credible anomaly ≠ verified origin.** A witness seeing something unexplained is a starting point for investigation, not a conclusion.
2. **Classified allegation ≠ evidence.** A claim made in a secure compartment is still a claim. Without independent verification, it cannot be treated as fact.
3. **Physics vocabulary ≠ engineering reality.** The existence of Casimir forces or vacuum fluctuations does not imply that anyone has built an inertia-cancellation drive.

The public record does not contain verified evidence of extraterrestrial technology, exotic propulsion, or recovered craft. The only honest demand is for the raw sensor data, platform logs, radar tapes, and reconstruction methodology that would allow independent scientific assessment.

## Setup

```bash
npm install         # install markdownlint-cli
# For PDF builds also: brew install pandoc && brew install --cask mactex-no-gui
# (or on Debian/Ubuntu: apt install pandoc texlive-xetex)
```

## Lint & Checks

```bash
make install-deps   # install markdownlint-cli via npm
make lint           # run markdownlint on all canonical .md files
make check-refs     # verify footnote definitions match references
make check-stale    # scan canonical files for forbidden/stale strings
make check          # run all checks (lint, check-refs, check-stale)
make pdf            # build PDF (requires pandoc + xelatex)
make html           # build HTML (requires pandoc)
make help           # list all targets
```

See the [Makefile](Makefile) for details.

## License

This manuscript is licensed under [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/). See the [LICENSE](LICENSE) file for the full legal text. You may share the material with attribution but may not distribute modified versions. All factual claims are sourced to publicly available documents and peer-reviewed literature. Speculative sections are explicitly marked as conditional.
