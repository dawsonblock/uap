---
name: update-documentation-file
description: Workflow command scaffold for update-documentation-file in uap.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /update-documentation-file

Use this workflow when working on **update-documentation-file** in `uap`.

## Goal

Update or align existing documentation files with new information or corrections.

## Common Files

- `README.md`
- `REFERENCES.md`
- `CHANGELOG.md`
- `*.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Edit the relevant documentation file (e.g., README.md, REFERENCES.md, CHANGELOG.md, or other .md files).
- Commit the changes with a descriptive message.

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.