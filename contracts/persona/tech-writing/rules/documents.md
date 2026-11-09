# Documents and the document set <!-- persona: module header -->
Applies: when creating, editing, releasing or tracking documents. Requires: base.md.

## Lifecycle states
Every document sits in exactly one state, visible in its header and its path:
- `outline` - structure agreed, content not written.
- `draft` - being written; freely editable.
- `in-review` - complete, awaiting a named reviewer; content frozen except review fixes.
- `released` - accepted by its owner; **immutable**. Corrections create a new version citing the
  original, never an in-place edit.
- `superseded` - kept for history; never edited, never used as input to new work.
Moving a document between states is an explicit action recorded in STATUS.md, not a silent rename.

## Header block
Every document opens with: id, title, version, status, date, audience, owner, sensitivity, format,
sources (the source ids it relies on), open-items (count). A missing header field is a finding, not
a formatting detail: the header is what makes a document safe to cite.

## Naming
`NNN-<type>-<topic>-v<major.minor>.md`, e.g. `014-design-network-segmentation-v1.0.md`.
`<type>` in {design, advisory, comparison, brief, runbook, minutes, memo}. Numbers come from the
document register in `agent/REPO-MAP.md`, never invented per document. Minor version: content
changed. Major version: the recommendation changed.

## The document set (multi-chapter work)
Complex work spans chapters and documents, and context is not the memory. These registers live in
`agent/REPO-MAP.md` and are the single source of truth:
- **Document map:** every document with version, status, owner, dependencies, and the open items it
  blocks or is blocked by.
- **Shared facts:** each figure, product version, price, date and capacity number used in more than
  one place, with its value, source id, and the documents citing it.
- **Terminology:** approved term, banned synonyms, acronym expanded at first use.
- **Sources:** source id, what it is, product and version, retrieval date, snapshot location.
A chapter is not finished while a register entry it depends on is missing: write the entry, then the
chapter. Register updates follow the REPO-MAP triggers in `rules/base.md`.
- Before releasing any document in a set, run the consistency pass of `rules/verification.md` across
  the whole set, not only the document in hand.

## Structure
- First screen carries the decision or finding, and what is still open. Detail comes after.
- Scope and non-goals stated; audience stated; acronyms expanded at first use and listed.
- Headings numbered with stable anchors; cross-references cite `<doc-id> section <n>`, never "the
  section above".
- Closes with: Open items, Sources, Change note (what changed in this version, and why).

## Templates and generators
- Templates live in `templates/`; a generated document states which template produced it.
- Generated output is never hand-edited into truth: fix the template, the register or the generator,
  then regenerate (see `rules/output_formats.md`).
- `templates/X` pairs with `docs/templates/X.md`; `scripts/X.py` pairs with `docs/scripts/X.md`.