# Verification <!-- persona: module header -->
Applies: always. Requires: base.md.

## Claims
<!-- persona: evidence vocabulary — this repo's evidence is checker/test output -->
- Never write "verified", "proven" or "confirmed" without the command that reproduces it, or an evidence record: what, command, environment, date, result.
- Prefer a committed script over a prose recipe.

## References
<!-- core -->
- Never create a document, record or test to make a dangling reference resolve. Fix the reference, or ask the user.
- Before changing a documented decision, change and run the tests that enforce it.
- Keep a docs-integrity check: ID references resolve, index paths exist, index status markers match the documents.

## Tooling checks <!-- persona -->
- `tools/check_sync` must pass before any commit that touches contract files; `pytest tests/` must pass before any commit that touches `tools/` or `tests/`.
- Contract changes bump the affected persona manifest version in the same commit (see `docs/authoring/core-sync.md`).
