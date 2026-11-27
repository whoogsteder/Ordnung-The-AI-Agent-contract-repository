# DR-003: The task board is core

## Context
The draft put a task queue inside PROJECT.md. A field project with about 50 open tasks showed
that this cannot fit within 80 lines. That project's own board format (NOW, NEXT, LATER, WAITING;
`[T-NN]`; owner, `after:`, `done:`) was the part the operator called "working very well".

## Decision
1. `agent/TASKS.md` is a core file, with the `ordnung-board` skill. It is the only place open
   work lives.
2. NOW holds at most **2** tasks with `owner: agent` or `both`. This is the operator's choice
   (2026-11-26), matched to the capacity of self-hosted inference. Owner tasks in NOW don't count
   towards the cap.
3. On resume, the agent reads only NOW and WAITING. PROJECT.md tracks point at task ranges.

## Consequences
- Enforced by: `tools/ordnung_check` (`check_board`) and the board tests in `tests/test_tools.py`.

## Status
ACCEPTED (2026-11-26, operator)
