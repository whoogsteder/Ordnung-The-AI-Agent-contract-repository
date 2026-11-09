# Verification <!-- persona: module header -->
Applies: always. Requires: base.md.

## Checks
- A check exercises something outside the check file. Never assert a figure, table or claim that
  is defined only inside the check.
- Where generators exist, checks are commands (render, extract text, compare). Where none exists
  yet, the check is a stated procedure: input document, steps or command, expected result.
- A task with a checkable completion criterion is done when its check passes.

## Claims <!-- persona: evidence vocabulary -->
- Never write "verified", "current", "confirmed" or "supported" about an external fact (a product
  feature, a version, a price, a benchmark, a clause of a standard) without the evidence record:
  source, product and version, retrieval date, result.
- Prefer a committed source snapshot (saved page, release note, exported table) over a bare URL:
  links rot, snapshots do not. Keep snapshots under `sources/` and cite the file, not only the URL.
- A figure, number or quotation with no traceable source is labelled `unverified` in the body text,
  not softened into an adjective.
- Vendor-authored material is cited as a vendor claim; independent measurement is cited as
  measurement. Never mix the two in one sentence, and never let a marketing page stand in for a
  measurement.

## References
- Never create a source, citation, figure, product feature or chapter to make a dangling reference
  resolve. Fix the reference, or ask the user.
- Before changing a documented decision, re-check everything that cites it (documents, comparison
  matrices, registers, templates).
- Keep a document-integrity pass: cross-references and anchors resolve, figure files exist, every
  citation appears in the Sources list, shared facts match across the set, terminology follows the
  register.

## Consistency across the set
- A fact used in more than one document (product name, version, price, date, capacity figure,
  acronym) is a shared fact: it has one register entry, and a change to it updates every document
  citing it in the same change.
- Restating a figure for a new document is a computation from the register, never a copy of an
  earlier document's summary.

## Verification ladder, cheapest first
Static (header, naming, structure, links present) -> internal consistency (tables match the prose,
contents match the headings, shared facts agree across documents) -> source spot-check (each
load-bearing claim traced to its cited source) -> render round-trip (exported .docx/.pdf text
matches the source) -> external confirmation (vendor, lab, pilot: opt-in, never inferred). A tier
never certifies what only a higher tier can show: a tidy table does not prove the numbers are
current.