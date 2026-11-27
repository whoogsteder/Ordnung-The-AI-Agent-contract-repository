---
name: iac-verification
description: Evidence and testing rules for infrastructure-as-code work — what counts as proof, the cheapest-first test tiers (static, golden files, check mode, idempotency, lab or live, canary), tests that exercise real code, strict expected-to-fail spec tests for unbuilt work, golden-file locking before porting legacy code, fixtures recorded from real devices, decision enforcement and the docs-integrity test, and docs shipping with every change. Use this before writing that anything works, passes, is fixed, verified or confirmed, when writing or changing tests, when deciding how far to test, when porting existing code, and when adding or changing a decision record or a documented reference.
---

# Verification

A claim without the command behind it is a guess. The next agent will build on it, and the owner
will release it.

## Claims
- Never write "verified", "proven", "confirmed" or "works" without one of these behind it:
  - the command that reproduces it;
  - an evidence record: what, command, environment, date, result.

  Put the latest one in the HANDOFF `evidence:` field.
- If a check could not run here (no device, no network, no credentials), say so plainly. Don't
  substitute a weaker check under the same word.
- Prefer a committed script over a prose recipe.

## Test tiers: cheapest first
1. Static: lint, type check, `validate`, rendering.
2. Rendered output compared against golden files.
3. Check mode or dry run, asserting that nothing changed.
4. Idempotency: a second run changes nothing.
5. Lab or live. This tier is opt-in, allowlisted, never in default CI, and run under `iac-live`.
6. Canary: a small chosen set first, then the rest.

A tier never certifies what only a higher tier can show. Say which tier a claim rests on ("unit
tests pass; not run on a device").

## Tests
- **A test exercises something outside the test file.** Never assert on a value or table that is
  defined only inside the test.
- **Work that isn't built yet** gets a spec test. Mark it expected-to-fail, strict, limited to the
  not-built error, and cite the board task, for example
  `xfail(strict=True, raises=ModuleNotFoundError, reason="T-28")`. Remove the marker when it passes.
- **A fix ships with a regression test** that fails without the fix.
- **A task with a testable `done:` criterion** is done when that test passes.
- **The unit tier needs no network and no device.** Anything that does needs them carries a marker
  (e.g. `integration`), and CI excludes it.

## Fixtures
A device or vendor response in a fixture is either:
- recorded from a real device, with its model, firmware and date, and redacted; or
- labelled synthetic.

Provenance goes in a README next to the fixtures.

## Porting existing code
- Port the code, not the intent documents. Where they disagree, the code is the behaviour;
  record the disagreement.
- Before porting, lock the current behaviour with golden-file tests. Each intended change of
  behaviour is its own commit: the updated golden file plus a test that names the reason.

## Decisions and references
- An ACCEPTED decision record lists how it is kept true: ``- Enforced by: `path::test` `` plus
  what it checks. While the subject does not exist yet, use `- Enforced by (planned, T-NN): ...`.
- Before changing a documented decision, change and run the tests that enforce it.
- Keep a docs-integrity test that checks:
  - ID references resolve;
  - index paths exist;
  - status markers match the documents;
  - CLOSED records are cited only by other records.
- Generate a table from its source wherever a source exists.
- Never create a document, record or test just to make a dangling reference resolve. Fix the
  reference, or ask.

## Docs ship with the change
- Every deliverable comes with its docs: no docs, not done.
- The README is the landing page.
- Paired docs are per language (`iac-python`, `iac-ansible`, `iac-terraform`). Update the
  REPO-MAP documentation index and its status markers (✅ 🟡 📋 🗄️) in the same change.
