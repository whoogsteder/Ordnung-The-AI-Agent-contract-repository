# Documents and the document set <!-- persona: module header -->
Applies: when creating, editing, releasing or tracking documents. Requires: base.md.

## Workflow
Every document goes through the same steps. Do not skip ahead.
1. **Questioning session and brief** (`rules/requirements.md`). The user confirms the brief.
2. **Facts** (`rules/facts.md`): a research pack from the `research` persona, or lookups by the writer
   for smaller documents; options screened on checked facts before any are recommended.
3. **Outline**: the skeleton from `rules/doc_types.md` with one line per section saying what it will
   say, and the page budget. Show it to the user. A short confirmation is enough.
4. **Draft** (`rules/writing.md`).
5. **Review** (`rules/verification.md`), then hand over with the review report.
6. **Release** when the owner accepts it (`rules/classification.md` checks apply).

## Lifecycle states
`brief` - `outline` - `draft` - `in-review` - `released` - `superseded`.
- Up to `in-review`, a document is rewritten freely.
- `released` is immutable. A correction is a new version that names the one it replaces.
- `superseded` documents are kept for history and never used as input to new work.
Record each state change in `agent/STATUS.md`.

## Header
Keep it compact, at the top or end of the document:
`id | title | version | status | date | owner | audience | classification`.
Advisories add `tlp:` and the urgency label. Sources and open decisions are annexes, not header fields.

## Naming
`NNN-<type>-<topic>-v<major.minor>.<ext>`, for example `014-selection-lan-switch-v1.0.md`. `<type>` is
one of: architecture, howto, change-plan, selection, advisory, research, guide, memo, minutes.
Numbers come from the document map in `agent/REPO-MAP.md`. Minor version: content changed. Major
version: the recommendation changed.

## Registers
Kept in `agent/REPO-MAP.md` and cited by the documents, never duplicated inside them:
- **Document map:** id, title, version, status, owner, classification, depends on.
- **Sources:** id, what it is, product and version, retrieval date, file under `sources/`.
- **Open decisions and assumptions** (`rules/open_questions.md`).
- **Shared facts** (only for a set of two or more documents): value, source, documents using it.
- **Distribution** (once anything has been sent out, `rules/classification.md`).
- **Terminology** (only when the set has terms that must be used consistently).
Start a register when it is first needed, not empty in advance.

## Ending a document
The body ends with the next steps and open decisions. After that come the annexes: detail tables, open
decisions and assumptions register, sources, and a change note with one line per version.

## Templates and generators
- Templates live in `templates/`. A generated document states which template produced it.
- Never hand-edit generated output into the truth: fix the source, template or generator and
  regenerate (`rules/output_formats.md`).
- `templates/X` pairs with `docs/templates/X.md`. `scripts/X.py` pairs with `docs/scripts/X.md`.
