# Verification: why claims become checks

Companion to `rules/verification.md` (and the Enforcement section of `rules/dr.md`).
Start at [index.md](index.md) for the map of all rationale pages.
The rule files tell agents what to do; this page explains why, for the people who
maintain the rules and review the work.

## The problem

Administrative work with agents produces prose *and* numbers: status notes, "reconciled"
claims, summaries of figures, corrections that were "applied". Prose is never executed, so
nothing notices when it goes wrong. Worse, in administrative work a fluent, plausible
sentence can carry a fabricated number, and smaller models make this likelier: they write
confident text whether or not it is true. A wrong total that reads certain is more dangerous
than an open question.

The fix is the same as in engineering: move every claim that *can* be checked into something
that is checked, and leave prose only for the reasons behind decisions.

## Four kinds of statement

| Kind | Example | Becomes |
|---|---|---|
| Requirement | "Invoice totals equal the sum of their line items" | A recomputation script or stated check procedure that runs on the real records |
| Decision / constraint | "All quotes use the hourly rate model from rate card v2" | A decision record with a named enforcement point (template, register, script check) |
| Fact about the outside world | "Supplier X quoted €4,200 for phase 1" | An evidence record: source document, date received, file path — or labelled unverified |
| Rationale | "We prefer annual prepayment with this supplier" | Stays prose |

## Checks as the task list

A check that cannot run yet is still written now, as a stated procedure or an
expected-to-fail test, so the backlog of open verification items is visible and a task closes
when its check passes rather than when a status line says so.

## Decisions name their enforcement

Where a project uses decision records, each one states what keeps it true (a template, a
register entry, a script check). A decision that enforces nothing drifts: the first document
produced under a slightly different habit quietly changes policy. Naming the enforcement point
makes drift visible at the next check instead of at the next audit.

## What link checks cannot catch

A register-integrity pass catches references to things that do not exist. It cannot catch
a record that was **invented to fit its references**. This happens in practice: a summary
cites quote number Q-0137, the file is missing, and an agent creates a plausible Q-0137 to
make everything line up. Every structural check passes. That is why the rules forbid creating
a target to resolve a dangling reference — in administrative work the invented target is an
invoice that never existed, which is not a documentation bug but a liability.

The same reasoning drives "recompute, never copy": a copied total inherits whatever error sat
in the original; a recomputed one at least agrees with the line items you can inspect.

## The verification ladder for records

Run the cheapest checks first; each tier gates the next.

1. **Static**: file exists, naming and metadata correct, required fields present.
2. **Recomputation**: line items sum to totals; cross-document figures match; VAT math holds.
3. **Round-trip**: re-export/re-render matches a saved expected output.
4. **Spot-check against source**: open the original invoice/contract/export and compare.
5. **Outside confirmation**: query the bank, portal or supplier — opt-in, approval-gated.

A lower tier never certifies what only a higher one can show: totals that add up do not prove
the counterparty, period, or price is right — only tiers 4 and 5 touch reality.
