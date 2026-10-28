# Financial data
Applies: whenever money is calculated, quoted, invoiced or reported. Requires: base.md.

## Provenance
- Every amount traces to a source: an invoice, quote, bank export, price list or contract.
  Record which one next to the figure (file path or document number), not in your head.
- No source found? The figure does not exist yet. Ask; do not estimate into a record.
- Never copy a total from one document into another — recompute it from the line items and
  compare. A mismatch is a finding: report it, never silently reconcile to make numbers meet.

## Arithmetic discipline
- Currency and VAT/sales-tax rate are explicit on every figure; no implicit defaults.
- Amounts are stored in minor units (cents) or exact decimals — never binary floats.
- Rounding happens once, at the stated step (per line or per total), with the rule written down.
- Percentages state their base (net vs gross, incl/excl shipping).
- Dates are ISO-8601 (`YYYY-MM-DD`) everywhere; fiscal period stated when relevant.

## Sequences and registers
- Invoice/quote numbers follow the project's declared sequence (`rules/documents.md`). Gaps in
  a legal sequence are recorded and explained, never filled retroactively.
- Payments, credits and corrections are separate records against the original — not edits of it.

## Reconciliation
- Reconcile by matching both sides of a transaction (export vs ledger), not by adjusting one
  side until totals agree.
- Unexplained difference after reconciliation: halt that task, write it into STATUS.md with
  both figures and their sources, and ask the user. An agent never "balances" a discrepancy.

## Verification hooks
- A computed figure is "verified" only with the recomputation command or evidence record —
  see `rules/verification.md` (Claims).
- Where scripts produce financial output, the checks in `rules/python.md` apply: totals tests,
  fixture exports, no in-place edits of source files.
