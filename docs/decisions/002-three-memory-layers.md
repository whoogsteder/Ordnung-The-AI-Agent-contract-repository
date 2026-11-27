# DR-002: Three memory layers, kept by script

## Context
v1's STATUS.md mixed the task in hand with project strategy, and grew past every limit (a v1
field project measured a multi-paragraph `next_action`). The operator asked for both a tactical
and a strategic layer (2026-11-25).

## Decision
1. `agent/STATUS.md` is the task in hand: a HANDOFF with `task`, `status`, `next_action` (one
   sentence), `skills`, `constraints`, `files`, `evidence` and `last_update`. Capped at 40 lines.
2. `agent/PROJECT.md` is what must stay true across tasks: requirements (REQ), open decisions,
   questions for the operator (Q) and tracks. Capped at 80 lines, one line per entry, with detail
   behind a link.
3. `agent/TASKS.md` holds all open work (DR-003).
4. The promotion rule: a fact that would still matter after the task closes goes to PROJECT.md,
   never only to STATUS.
5. `agent/ordnung_check` enforces the caps, the schema, freshness and ID resolution, and runs as
   the pre-commit hook.

## Consequences
- Enforced by: `tools/ordnung_check` and `tests/test_tools.py`.

## Status
ACCEPTED (2026-11-25)
