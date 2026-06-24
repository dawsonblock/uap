# Changelog

All notable changes to this manuscript bundle are documented in this file.

## [2.0.0] — 2026-06-24

### Restructured

- Reorganized the repository into a publishable structure: `manuscript/`, `appendices/`, `style/`, `references/`, `archive/`.
- Moved main manuscript to `manuscript/uap-comprehensive.md`.
- Moved editorial principles to `style/editorial-principles.md`.
- Archived original source documents in `archive/` (physics-map-bridge, speculative-framework, missing-floor, evidence-rebuttal, stitched draft).

### Added

- `appendices/a-evidence-cases.md` — standalone case summaries extracted from evidence-rebuttal.
- `appendices/b-physics-boundaries.md` — the five real physics gaps, decoherence dynamics, and experimental frontier extracted from physics-map-bridge and missing-floor.
- `appendices/c-speculative-framework.md` — conditional speculative framework with warning blocks, extracted from speculative-framework.
- `references/references.md` — consolidated bibliography with full citations, URLs, and DOIs.
- `README.md` — repository overview, reading guide, and structure documentation.
- `CHANGELOG.md` — this file.
- Freshness section (Part IIIb) to the manuscript covering AARO case releases, 2025 workshop, and post-2025 public releases.

### Fixed (P0)

- Corrected BridgeQG COST Action number: CA23140 → CA23130 across all files.
- Added missing `[^30^]` footnote definition in physics-map-bridge.
- Resolved Aguadilla April 25/26 date discrepancy with parenthetical: "April 25–26, 2013 (local time/UTC discrepancy in source materials)".
- Updated Pedalino et al. citation with full reference: *Nature* 649, 866–870 (2026).

### Hardened (P2)

- Labeled power estimate as "punitive order-of-magnitude heuristic, not a physical requirement derived from a concrete control model."
- Rewrote QEC sentence: "No quantum error correction has been demonstrated for the relevant macroscopic degrees of freedom of a room-temperature extended object, let alone a vehicle interacting with atmosphere or water."
- Added ⚠️ warning blocks before every speculative subsection in the manuscript and appendices.
- Applied warning blocks and heuristic labels to the speculative framework appendix.

### Updated

- `.markdownlint.json` — added MD053 suppression for appendix files with reference-style footnotes.

## [1.0.0] — 2026-06-23

### Initial compilation

- Created `uap-comprehensive.md` synthesizing all source documents into a four-part manuscript.
- Created `uap-physics-map-bridge.md` as a standalone physics deep dive.
- Created `uap-speculative-framework.md` as a shorter conditional framework.
- Created `uap-evidence-rebuttal.md` as a disciplined rebuttal to common UAP claims.
- Created `uap-missing-floor.md` as a speculative placeholder essay.
- Created `uap-editorial-principles.md` with 12 principles, forbidden phrases, and razor checklist.
- Created `.markdownlint.json` disabling MD025 (multiple H1) and MD013 (line length).
- Added footnote definitions across all documents to resolve MD052 warnings.
- Applied content fixes: Levin (2009) critique, AARO FY2024 statistics, NASA data quality quotes, SCU resolution, ICIG process, thermal de Broglie wavelength.
