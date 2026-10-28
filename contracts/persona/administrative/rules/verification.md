# Verification <!-- persona: module header -->
Applies: always. Requires: base.md.

## Checks
- A check exercises something outside the check file. Never assert a value or table
  defined only inside the check.
- Where scripts exist, checks are pytest tests (see `rules/python.md`). Where no script
  exists yet, the check is a stated procedure: input file, command or steps, expected output.
- A task with a checkable completion criterion is done when its check passes.

## Claims <!-- persona: evidence vocabulary -->
- Never write "verified", "correct", "reconciled" or "confirmed" without the command or
  evidence record that reproduces it: what, source document, how checked, date, result.
- Prefer a committed script over a prose recipe.
- Figures quoted from an external system (bank export, accounting portal, supplier price list)
  state the system, export date and file — or are labelled unverified.

## References
- Never create a document, record or entry to make a dangling reference resolve. Fix
  the reference, or ask the user.
- Before changing a documented decision, re-check everything that cites it (REPO-MAP,
  registers, dependent records).
- Keep a register-integrity pass: sequence numbers listed in REPO-MAP match the files on
  disk, document cross-references resolve, counterparty names match master data.

## Corrections and restatements
- When a report or export disagrees with its source documents, the source documents are the
  truth; record the disagreement (see `rules/financial.md`, Reconciliation).
- Restating figures for a new purpose (summary, dashboard, e-mail) is a computation from the
  records — never a copy of an earlier summary's numbers.

## Verification ladder, cheapest first
Static (file exists, naming and metadata correct) → recomputation (line items sum to totals,
cross-document figures match) → round-trip (re-export/re-render matches a saved expected
output) → spot-check against the original source document → confirmation from the outside
system (opt-in, requires approval per `rules/approval.md`). A lower tier never certifies what
only a higher tier can show: a matching total does not prove the counterparty or period is right.

