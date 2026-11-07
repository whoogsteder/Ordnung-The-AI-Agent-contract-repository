# Verification <!-- persona: module header -->
Applies: always. Requires: base.md.

## Tests
- A test exercises something outside the test file. Never assert a value or table
  defined only inside the test.
- Not built yet: mark the test expected-to-fail, strict, limited to the not-built error
  (pytest: `xfail(strict=True, raises=ModuleNotFoundError, reason="<task-id>")`).
  Remove the marker when it passes.
- A task with a testable completion criterion is done when its test passes.

## Claims <!-- persona: evidence vocabulary -->
- Never write "verified", "proven" or "confirmed" without the command that reproduces
  it, or an evidence record: what, command, environment, date, result.
- Prefer a committed script over a prose recipe.
- For container work the evidence is the container's own output: `docker compose ps`
  status, log lines showing the server reached its ready state, and — where the game
  protocol allows — an external query response. "The container is running" alone proves
  nothing: crashed-and-restarting containers run too.

## References
- Never create a document, record or test to make a dangling reference resolve. Fix
  the reference, or ask the user.
- Before changing a documented decision, change and run the tests that enforce it.
- Keep a docs-integrity test: ID references resolve, index paths exist, index status
  markers match the documents. Generate tables from their source where one exists.

## Upstream truth <!-- persona -->
- Game servers move fast and vendor docs lag or contradict each other. When sources
  disagree, trust the artifact the server itself produces (generated config, runtime
  log) over any page or readme; record the disagreement in the project docs with
  source URLs and dates.
- Adopting upstream changes (new settings, image bumps): diff against the pinned
  version first, document what changed, then bump — never blind-pull `latest`.

## Test tiers, cheapest first <!-- persona -->
Static lint (`docker compose config` renders; env example covers every variable the
compose file reads) → bring up in a throwaway directory → container healthy + logs reach
ready state → join/query from outside the host → restore-from-backup drill. A tier never
certifies what only a higher tier can show. Never run this ladder against the user's live
save data without their explicit go-ahead.
