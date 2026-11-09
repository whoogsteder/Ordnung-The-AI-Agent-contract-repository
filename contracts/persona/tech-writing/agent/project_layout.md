# Project Layout Guide

## Agent Memory Files

Use these files to externalize memory from your context. These exist in every project using this ruleset.

| File | Purpose | When to Update |
|------|---------|----------------|
| `STATUS.md` | Forward-looking session state + HANDOFF block | After file creation, command verification, feature completion, or topic switch |
| `REPO-MAP.md` | Stable file index, plus the registers: document map, shared facts, terminology, sources, open items | Use it and update it any time a file is added/moved/removed, a fact changes, or an open item moves |
| `project_layout.md` | Directory structure guide (this file) | Use it and update it when core directory layout changes |

## Universal Structure (document projects)

```
[project root]/
|-- agent/                 # AI agent externalized memory
|   |-- STATUS.md          # Session handoff + state (single source for continuity)
|   |-- REPO-MAP.md        # Index + registers: documents, shared facts, terminology, sources, open items
|   `-- bootstrap.md       # New project bootstrap protocol
|-- rules/                 # Agent rules: base.md always; one module per document type in use
|-- docs/                  # Human-facing documentation about the project
|   |-- decisions/         # Decision Records: NNN-<topic>.md (see rules/dr.md)
|   |-- guides/            # How-to documentation (read on demand)
|   |-- templates/         # docs/templates/X.md pairs with templates/X
|   `-- scripts/           # docs/scripts/X.md pairs with scripts/X.py
|-- documents/             # The deliverables, by type (see rules/documents.md)
|   |-- designs/
|   |-- advisories/
|   |-- comparisons/
|   `-- briefs/
|-- distribution/          # Per-recipient release packages, one dir per recipient (not indexed)
|-- restricted/            # Restricted-tier material: never exported, git-ignored by default
|-- templates/             # Document skeletons and style references (reference.docx, md skeletons)
|-- assets/figures/        # Figure sources (mermaid/plantuml/dot) + rendered images, named <doc-id>-<nn>
|-- sources/               # Evidence: saved vendor pages, release notes, exports, benchmark runs
|-- scripts/               # Generators and exporters (pandoc wrappers, python-docx, matplotlib)
|-- build/                 # Exported .docx/.odt/.pdf: generated output, git-ignored
|-- .env.example           # Publishing-token placeholders (real .env git-ignored)
|-- .gitignore             # Guards: secrets, narrower-than-Internal material, build output
`-- README.md              # Landing page for the document set, with the set's classification
```

## Document-handling guards
- `sources/` is evidence: read-only inputs, never edited in place. Name each file
  `<src-id>_<YYYY-MM-DD>.<ext>` so a source id in a document resolves to a file.
- Material whose `classification:` is narrower than `Internal` - that is `Client-shareable` and
  `Restricted` - is git-ignored unless the project declares the repository private; commit a redacted
  sample with the same shape (base.md, State & change history).
- `restricted/` holds `Restricted`-tier material and is kept out of every export and build.
  `distribution/` holds the per-recipient release packages, one directory per recipient; it is not
  indexed in REPO-MAP beyond the distribution register.
- `build/` and exported rich-text files are build output: generated, never hand-edited, not indexed
  in REPO-MAP.
- Registers (document numbers, shared facts, terminology, sources, open items, distribution) live in
  `agent/REPO-MAP.md`; documents cite them, they do not fork them. The registers carry the set's
  `classification:`, and for a `Restricted` set they hold titles and pointers only, never facts
  (`rules/classification.md`).

## Tool-Specific Layouts
Directory structures for specific tools are named by the module that owns them: `rules/documents.md`
(document tree and naming), `rules/visuals.md` (figures), `rules/output_formats.md` (exports and
generators), `rules/dr.md` (decision records).