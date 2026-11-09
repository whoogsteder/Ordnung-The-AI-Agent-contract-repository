# Decision Records <!-- slot: decision-records -->
Applies: when the project records decisions in `docs/decisions/`. Requires: base.md.

Use for choices that outlive a single task: architecture and product choices inside a design, the
output format and toolchain, comparison criteria and their weights, terminology, the structure of the
document set, the template set, the classification of the set and every widening of a document's
classification, and any widening of what the agent may do without asking.

- Location: `docs/decisions/NNN-<topic>.md` (zero-padded, e.g. `001-output-format-and-toolchain.md`).
- Each record has: Context / Decision / Consequences / Status.
- Statuses:
  - `PROPOSED` - open, not yet decided.
  - `ACCEPTED` - decided; safe to build on.
  - `CLOSED` - rejected or superseded (state why, and by what).

## Rule
- A record may stay `PROPOSED` while work proceeds, as long as no document depends on it.
- If a document depends on a `PROPOSED` record: drive it to `ACCEPTED`/`CLOSED` first, or halt that
  document. Never release a design against an undecided architecture choice, and never release a
  comparison against undecided criteria.
- Cite decisions as `DR-NNN decision N`; both must exist. A `CLOSED` record is cited only by other
  records and history files.
- A document that contradicts an `ACCEPTED` record is a finding: fix the document, or supersede the
  record. Never leave both standing.

## Enforcement
- Consequences state how the decision is kept true in practice: where it is encoded (template,
  register in REPO-MAP, generator script, style guide) or `- Enforced by (planned, <task-id>): <what>`
  while that mechanism does not exist yet.
- An `ACCEPTED` record needs at least one concrete entry. Records without one go on a debt list in
  REPO-MAP; the list may only shrink.
- Changing an accepted decision means updating its enforcement points and every document citing it,
  in the same change; documents that silently disagree with a DR are findings (see
  `rules/verification.md`).
- A widening of a classification is written as a record **before** the wider label is applied
  (`rules/classification.md`). The record names the new tier, the recipient and its basis, what the
  content scan checked, the date and who widened it. There is no approval gate: the record is the
  accountability, and a widening with no record is the finding.

## DR triggers (per module)
- `rules/documents.md`: naming scheme, document-set structure, template set, lifecycle states.
- `rules/output_formats.md`: output format, export toolchain, style reference document.
- `rules/comparisons.md`: criteria list and weights, price basis, benchmark harness.
- `rules/advisories.md`: the basis of a recommendation, the urgency label set.
- `rules/open_questions.md`: any assumption the user signs off as standing policy.
- `rules/classification.md`: widening a classification (recorded before the label is applied), the
  named-recipient list for `Restricted`, the basis for a `Client-shareable` set, an export-control
  marker.