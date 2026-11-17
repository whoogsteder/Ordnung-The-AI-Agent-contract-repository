# Project Layout Guide

## Agent Memory Files

Use these files to externalize memory from your context. They exist in every project using this ruleset.

| File | Purpose | When to update |
|------|---------|----------------|
| `STATUS.md` | Forward-looking session state, the HANDOFF block, the review in progress | At the checkpoint moments in `rules/base.md` |
| `REPO-MAP.md` | File index plus the review register: artefact, version, verdict, report path | Any time a file is added, moved or removed, or a review completes |
| `project_layout.md` | Directory structure guide (this file) | When the directory layout changes |

## Universal Structure (review projects)

```
[project root]/
|-- agent/                 # AI agent externalized memory
|   |-- STATUS.md
|   |-- REPO-MAP.md        # Index + review register
|   `-- bootstrap.md
|-- rules/                 # Agent rules: base.md first, then every module
|-- reviews/
|   |-- <artefact>/        # One directory per reviewed artefact (document id or research topic)
|   |   |-- inputs/        # Read-only copies or links: artefact, yardstick, sources
|   |   `-- review-<artefact-version>.md   # One report per reviewed version
|   `-- archive/           # Closed reviews, mirrored; never read at task time
|-- docs/scripts/          # docs/scripts/X.md pairs with scripts/X.py
|-- scripts/               # Optional mechanical checks (id scan, link check, sentence length)
|-- .gitignore             # Guards: material narrower than Internal, .env
`-- README.md              # Reviews: artefact, version, verdict, date
```

## Guards
- `inputs/` is read-only. The reviewer never edits an artefact, here or at its origin.
- A report that was handed over is never edited. A re-review is a new report.
- Material narrower than `Internal` is git-ignored unless the repository is declared private.

## Used as a sub-agent
When a `document-writing` or `research` agent runs this persona as a sub-agent, no project is
created. The sub-agent receives the rules and the inputs, returns the report, and the calling agent
saves it next to the artefact (`reviews/review-<version>.md` in the caller's project).
