# Decision Records
Applies: when the project records decisions in `docs/decisions/`. Requires: base.md.

Use for choices that outlive a single task: supplier/tool selection, pricing or rate model,
numbering scheme, document workflow, data-handling policy, recurring-report format.

- Location: `docs/decisions/NNN-<topic>.md` (zero-padded, e.g. `001-invoice-numbering-scheme.md`).
- Each record has: Context / Decision / Consequences / Status.
- Statuses:
  - `PROPOSED` — open, not yet decided.
  - `ACCEPTED` — decided; safe to build on.
  - `CLOSED` — rejected or superseded (state why).

## Rule
- A record may stay `PROPOSED` while work proceeds, as long as the current task does not depend on it.
- If a task depends on a `PROPOSED` record: drive it to a decision (`ACCEPTED`/`CLOSED`) first, or halt that work until it is resolved. Never issue documents against an undecided scheme.
- Cite decisions as `DR-NNN decision N`; both must exist. A `CLOSED` record is cited only
  by other records and history files.

## Enforcement
- Consequences state how the decision is kept true in practice: where it is encoded
  (template, register in REPO-MAP, script check) or `- Enforced by (planned, <task-id>): <what>`
  while that mechanism does not exist yet.
- An `ACCEPTED` record needs at least one concrete entry. Records without one go on a debt
  list in REPO-MAP; the list may only shrink.
- Changing an accepted decision means updating its enforcement points and everything citing
  it in the same change — figures and documents that silently disagree with a DR are findings
  (see `rules/verification.md`).

## DR triggers (per module)
- `rules/documents.md`: numbering scheme, naming convention, template set changes.
- `rules/financial.md`: rounding policy, VAT handling exceptions, reconciliation procedure.
- `rules/approval.md`: any widening of what the agent may do without approval — always a DR
  and explicit user sign-off.

