# Project Layout Guide

## Agent Memory Files

Use these files to externalize memory from your context. They exist in every project using this ruleset.

| File | Purpose | When to update |
|------|---------|----------------|
| `STATUS.md` | Forward-looking session state, the HANDOFF block, and the current search plan | At the checkpoint moments in `rules/base.md` |
| `REPO-MAP.md` | File index plus the registers: topics and pack versions, open questions | Any time a file is added, moved or removed, or a question moves |
| `project_layout.md` | Directory structure guide (this file) | When the directory layout changes |
| `intake.md` | The user's opening brief, verbatim (only when one was given) | Once, at bootstrap; never edited afterwards |

## Universal Structure (research projects)

```
[project root]/
|-- agent/                 # AI agent externalized memory
|   |-- STATUS.md          # Session handoff + state + search plan
|   |-- REPO-MAP.md        # Index + registers: topics and pack versions, open questions
|   |-- intake.md          # Optional: the user's opening brief, verbatim
|   `-- bootstrap.md       # New project bootstrap protocol
|-- rules/                 # Agent rules: base.md always; modules per rules/ listing
|-- topics/                # One directory per research topic
|   |-- <topic>/
|   |   |-- pack.md        # The research pack (rules/research_pack.md), versioned
|   |   |-- brief.md       # Optional research brief for a person (rules/reporting.md)
|   |   `-- sources/       # Saved evidence: S-NN_<YYYY-MM-DD>.<ext>, read-only
|   `-- archive/           # Superseded packs, mirrored by topic; never read at task time
|-- docs/
|   |-- decisions/         # Decision Records: NNN-<topic>.md (rules/dr.md)
|   `-- scripts/           # docs/scripts/X.md pairs with scripts/X.py
|-- scripts/               # Optional helpers: extractors, link checkers
|-- .env.example           # Placeholders for portal/API credentials (real .env git-ignored)
|-- .gitignore             # Guards: secrets, material narrower than Internal
`-- README.md              # Topics, pack versions, status, classification
```

## Guards
- `topics/<topic>/sources/` is evidence: never edited in place. A newer copy of a source is a new
  file with a new date.
- A pack that was handed over is not edited. A re-check produces a new pack version.
- `topics/archive/` is frozen history, never read during task work.
- Material narrower than `Internal` is git-ignored unless the repository is declared private.

## Hand-over to a writer
The receiving `document-writing` project copies or links `topics/<topic>/` into its own
`research/<topic>/`. The pack is read-only on the receiving side. Corrections go back to the research
project as a new pack version.
