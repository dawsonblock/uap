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
- Freshness section (Part IIIb) to the manuscript covering AARO case releases and post-2025 public releases.

### Fixed (P0)

- Corrected BridgeQG COST Action number: CA23140 → CA23130 across all files.
- Added missing `[^30^]` footnote definition in physics-map-bridge.
- Corrected Aguadilla date to AARO-first language: "AARO lists April 26, 2013; some third-party analyses use April 25." Removed "April 25–26" compromise from case titles and body text.
- Corrected AARO FY2024 wording: "444 cases archived for lack of sufficient data" → "444 cases remained unresolved or lacked sufficient data for closure."
- Verified Pedalino et al. citation against Nature: title, volume 649, pages 866–870 (2026) all confirmed. Added DOI 10.1038/s41586-025-09917-9.
- Removed uncited "2025 AARO Workshop" section (no primary source available).
- Replaced "ICIG process remains ongoing in classified channels" with "No public ICIG conclusion validating the existence of non-human craft, biologics, or recovered technology has been released."
- Replaced false-precision "archived June 2026" labels with "accessed June 2026" in references.
- Qualified decoherence-rate estimates as order-of-magnitude and geometry-dependent (depends on separation scale, scattering environment, temperature, object geometry, and degree of freedom).
- Added explicit assumptions to the ~10^25 molecules-per-second interaction claim (meter-scale cross-section, ~300 m/s, sea-level air density).
- Expanded source-anchors.md with AARO FY2024, Pedalino verification, ICIG, and decoherence-rate anchor entries.

### Hardened (P2)

- Labeled power estimate as "punitive order-of-magnitude heuristic, not a physical requirement derived from a concrete control model."
- Rewrote QEC sentence: "No quantum error correction has been demonstrated for the relevant macroscopic degrees of freedom of a room-temperature extended object, let alone a vehicle interacting with atmosphere or water."
- Added warning blocks before speculative subsections in the manuscript and appendices.
- Applied warning blocks and heuristic labels to the speculative framework appendix.

### Trimmed (P2 — Publication Quality)

- Added one-page executive summary at the top of the manuscript.
- Moved speculative equations (ZPF force, toy parameterization, semiclassical Einstein, power estimate) out of the main body and into Appendix C only. Main body references them verbally.
- Condensed Part II (physics gaps) by referencing Appendix B for detailed treatment. Merged sections II.2-II.7 into four tighter sections.
- Condensed Part III sections III.7-III.11 by merging overlapping content and referencing Appendix C.
- Replaced Part IV (12 editorial principles, fully duplicated in style/editorial-principles.md) with a summary and reference to the style file. Kept the Honest Bottom Line conclusion.
- Removed redundant per-subsection warning blocks in Part III (kept one at the top).
- Net result: manuscript reduced from ~434 lines / ~8,800 words to ~308 lines / ~6,400 words (27% reduction).

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
