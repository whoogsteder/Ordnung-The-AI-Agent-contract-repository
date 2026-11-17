# Decision Records <!-- slot: decision-records -->
Applies: when the project records decisions in `docs/decisions/`. Requires: base.md.

A decision record captures a choice that outlives one document, so that later documents and agents
do not reopen it by accident.

## When to write one
- Choices about the document set: output format and toolchain, naming, templates, set classification.
- Choices that several documents depend on: a vendor shortlist constraint, comparison weights used
  across documents, a standing assumption the user signed off as policy.
- Every widening of a classification, written before the wider label is applied
  (`rules/classification.md`).
A decision that lives inside one document (the recommendation itself, a choice between two designs)
belongs in that document, not in a record.

## Shape
- Location: `docs/decisions/NNN-<topic>.md`, zero-padded.
- Sections: Context / Decision / Consequences / Status. Keep it under a page.
- Status: `PROPOSED` (not yet decided), `ACCEPTED` (safe to build on), `CLOSED` (rejected or
  superseded; say by what).
- Consequences name where the decision is applied (template, register, generator) so it can be kept
  true.

## Rules
- A document that depends on a `PROPOSED` record may be drafted, but not released.
- A document that contradicts an `ACCEPTED` record is wrong: fix the document, or supersede the
  record. Never leave both standing.
- Changing an accepted decision updates every document that relies on it, in the same change.
- In a document body, refer to a decision by what it says ("the agreed four-vendor shortlist"), not by
  its number (`rules/writing.md`).
