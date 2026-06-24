---
name: fix-or-rewrite-domain-specific-manuscript
description: Workflow command scaffold for fix-or-rewrite-domain-specific-manuscript in uap.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /fix-or-rewrite-domain-specific-manuscript

Use this workflow when working on **fix-or-rewrite-domain-specific-manuscript** in `uap`.

## Goal

Fix errors or rewrite sections in domain-specific markdown manuscripts.

## Common Files

- `uap-speculative-framework.md`
- `uap-comprehensive.md`
- `uap-physics-map-bridge.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Identify the manuscript file requiring changes (e.g., uap-speculative-framework.md, uap-comprehensive.md, uap-physics-map-bridge.md).
- Edit the file to fix errors or rewrite content.
- Commit the changes with a message indicating the fix or rewrite.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.