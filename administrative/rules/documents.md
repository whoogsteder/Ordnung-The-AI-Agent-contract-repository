# Documents and records
Applies: when creating or managing quotes, invoices, offers, receipts, contracts or
correspondence. Requires: base.md.

## Lifecycle states
Every record file is in exactly one state, visible from its location or name:
- `draft` — being prepared; freely editable.
- `final` — approved and issued (sent/printed/filed); **immutable**. Corrections create a new
  document (credit note, revised quote `-r2`, amended letter) that cites the original.
- `superseded` — kept for the audit trail; never deleted, never used as input to new work.
Moving a file between states is an explicit action recorded in STATUS.md, not a silent rename.

## Naming and numbering
- Records: `YYYY-MM-DD_<type>_<counterparty>_<number>` (e.g. `2026-03-14_quote_acme_q-0042.pdf`).
  `<type>` ∈ {quote, invoice, credit, receipt, letter, contract}. `<number>` is the legal or
  project sequence number once assigned; use `draft` until then.
- Number sequences are declared once in `agent/REPO-MAP.md` (which sequences exist, their
  format, next free number). The next number is taken from there — never invented per document.
- Templates live in `templates/`; a generated record always states which template it came from.

## Integrity checks
- Before issuing: line items sum to the stated total; VAT rate and currency present; counterparty
  name/address matches the master record; document number unique within its sequence.
- A cross-reference that does not resolve (a quote number, a contract clause) is fixed at the
  reference or raised with the user — never by inventing a document to point at
  (same rule as `rules/verification.md`, References).

## Master data
- Counterparty details have one authoritative location (`data/counterparties/` or the accounting
  system named in REPO-MAP). Documents cite it; they do not fork it. If two records disagree,
  halt and ask — do not pick a winner silently.

## Paired docs
- `templates/X` → `docs/templates/X.md` (placeholders, when to use, what must be checked before sending).
- `scripts/<path>/X.py` → `docs/scripts/<path>/X.md`.
- Records themselves need no companion doc; their metadata lives in REPO-MAP's registers section.
