# Financial records, documents and approval: the integrity contract

Companions to `rules/financial.md`, `rules/documents.md`, `rules/approval.md`,
`rules/python.md`. Start at [index.md](index.md). This is the administrative set's core:
everything else exists to support it.

## The asymmetry that drives all of it

In code, a wrong value is a bug you find in testing or production. In administration, a wrong
value is a *sent* invoice, a filed return, a number a client relied on — discovered months
later, during an audit, when it is no longer fixable by an agent. The contract therefore
assumes the agent will eventually produce a plausible wrong number, and surrounds that failure
with three barriers: **provenance** (where did this figure come from), **immutability** (can we
still see what was actually sent), and **approval** (does a human stand between the record and
the world).

## Provenance: why every number needs an ancestor

"Financial figures never hardcoded; always trace to source" exists because agents fill gaps.
Ask for a summary and an agent that cannot find one figure will *estimate* one — fluently,
without flagging it. The provenance rules close that path: every amount names its source file
or register, totals are recomputed from line items rather than copied (a copied total
inherits the original's error silently; a recomputed one disagrees loudly), and the Python
module makes data loss visible by requiring row-count and per-currency summaries on every
transformation. The rule "halt and ask, never silently balance a discrepancy" is the same
principle at decision time: an agent that plugs a €12 difference with a rounding note has
destroyed the only evidence that something is wrong.

## Money-specific mechanics

- **Decimal/cents, never floats** — `0.1 + 0.2 ≠ 0.3` is a curiosity in a demo and a
  reconciliation nightmare in an invoice pipeline; agents default to floats unless told.
- **Explicit currency and VAT rate on every figure** — "total: 1200" is ambiguous in exactly
  the way that generates real invoices with the wrong tax.
- **ISO dates, timezone-aware timestamps** — date formats are locale landmines when files
  cross between systems; ISO 8601 is the one format every tool agrees on.

## Immutability: why finals are frozen and corrections are new documents

A sent quote that can be edited in place is a liability: nobody can prove what the counterparty
actually received. The draft → final → superseded lifecycle makes history the default —
corrections create `...-v2` files or credit records, and the old artifact stays exactly as it
was issued. This also protects against agent behaviour specifically: an in-place "fix" is the
most tempting action for an agent that spots an error, and the most destructive one here. The
numbering rules (gapless sequences, gap log with reason) come from the same audit logic: a
missing invoice number must be explainable, so agents may never fill gaps or create documents
to make references line up.

## Approval classes: why "externally visible" is its own tier

Read-only and internal work fail small and privately; externally visible acts (sending mail,
submitting forms, issuing invoices) fail publicly and irreversibly. Hence the three-class model
and its two sharp edges: approval is **per content, per session** — approving one email is not
a license to send others — and automation defaults to dry-run with written output until a
human approves the real run. The audit-trail requirement (who approved what, when) exists
because an unlogged human approval is indistinguishable from an agent acting on its own.

## Data handling: why privacy rules sit in the base contract

Administrative projects hold third-party personal data the user may not even own. The
base.md data-handling section assumes leakage is permanent (pasted data can never be recalled)
and therefore keeps real records git-ignored by default, commits only redacted samples of the
same shape, and forbids IBAN/tax numbers in any agent-readable file — STATUS and REPO-MAP
included, because those files are written every session and read by every tool.

## Reading order

`base.md` (data handling) → `financial.md` (figures) → `documents.md` (artifacts) →
`approval.md` (the human boundary) → `python.md` (how to touch data safely). Verification ties
them together: see [verification.md](verification.md).