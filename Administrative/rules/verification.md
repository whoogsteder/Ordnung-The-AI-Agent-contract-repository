# Verification
Applies: always. Requires: base.md.

## Tests
- A test exercises something outside the test file. Never assert a value or table
  defined only inside the test.
- Not built yet: mark the test expected-to-fail, strict, limited to the not-built error
  (pytest: `xfail(strict=True, raises=ModuleNotFoundError, reason="<task-id>")`).
  Remove the marker when it passes.
- A task with a testable completion criterion is done when its test passes.

## Claims
- Never write "verified", "proven" or "confirmed" without the command that reproduces
  it, or an evidence record: what, command, environment, date, result.
- Prefer a committed script over a prose recipe.
- Device or vendor responses in fixtures are recorded from a real device (model,
  firmware, date) or labelled synthetic.

## References
- Never create a document, record or test to make a dangling reference resolve. Fix
  the reference, or ask the user.
- Before changing a documented decision, change and run the tests that enforce it.
- Keep a docs-integrity test: ID references resolve, index paths exist, index status
  markers match the documents. Generate tables from their source where one exists.

## Ports and existing code
- Port the code, not intent documents. When they disagree, the code is the behaviour;
  record the disagreement.
- Before porting, lock current behaviour with golden-file tests. Each intended change
  is its own commit: updated golden file plus a test naming the reason.

## Test tiers, cheapest first
Static → rendered output vs golden files → check mode / dry run (assert no mutation)
→ idempotency (second run changes nothing) → lab/live (opt-in, allowlisted, never in
default CI) → canary. A tier never certifies what only a higher tier can show.
