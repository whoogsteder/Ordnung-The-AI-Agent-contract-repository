---
name: ordnung-checkpoint
description: Writes the tactical session memory of an Ordnung-contract project — the HANDOFF block and plan in agent/STATUS.md — and archives finished tasks. Use this before starting a long run of tool work (research, debugging, a batch of edits), after any test, build or check runs (pass or fail), after creating or substantially changing a file, when a decision is made, before switching topic, before reporting back to the user, when a task is done, and whenever agent/ordnung_check reports STATUS as stale or oversize. Checkpoint early rather than late — a compaction mid-run loses everything not yet written.
---

# Checkpoint

STATUS.md is what survives when your context does not. Write it at *moments of risk*, not on
a count: the moment before a long run (so an interruption loses nothing), and the moment after
you learned something (so the result outlives you).

## 1. Promote first

Before writing STATUS, look at every fact you are about to put in it and ask:
**"Would this still matter after this task is closed?"**

- A requirement the user stated, a decision taken, a prerequisite another task will hit, or a
  question only the user can answer, is strategic. Load `ordnung-ledger` and put it in
  `agent/PROJECT.md` (or a decision record). In STATUS, at most refer to its ID.
- Follow-up work you found is a board task (`ordnung-board`), not a note.
- Everything else (the step you are on, the probe result, the file you will edit next) →
  STATUS.

This is the step that keeps STATUS short. Without it, STATUS becomes the project's diary and
outgrows every limit — which is the failure this contract was redesigned to stop.

## 2. Write the HANDOFF

Exactly this schema (the checker parses it):

```
## HANDOFF
task: <T-NN title — the board task in NOW; or a short name if the project has no board>
status: IN_PROGRESS | PAUSED | BLOCKED | DONE
next_action: <one sentence: exactly what to do first>
skills: [<skills the next action needs, ordnung-checkpoint always included>]
constraints:
  - <task-scoped must / must-not that a summary would lose; ≤ 3, or "none">
files: <paths the next action touches, or "none">
evidence: <last check: command → result, or "none">
last_update: <YYYY-MM-DDThh:mm — read it from the clock (e.g. `date +%FT%R`), never estimate>
```

Field guidance:
- `next_action` is one sentence because a resuming agent must be able to act on it without
  interpretation. If you need a paragraph, the paragraph is either a plan (→ `## Plan`) or
  strategy (→ PROJECT.md).
- `skills:` is how the next session — or you, after a compaction — gets the right rules back.
  List the persona skills governing this work.
- `constraints:` is for steering that is true *for this task only* ("do not touch live save
  data", "user wants monitor-only, not restorable"). Standing constraints belong in PROJECT.md.
- `BLOCKED` means waiting on the user: the matching `Q-NN` must exist in PROJECT.md. Usually
  it is better to move the task to WAITING on the board and claim another.

Below the HANDOFF: `## Plan` (`[ ]` steps) and `## Notes for the next action` (delete notes once
used). Total ≤ 40 lines.

## 3. Check

Run `python3 agent/ordnung_check`. It verifies size, schema, freshness and that every ID you
cite resolves. Fix what it reports before continuing.

## 4. When a task reaches DONE

1. Append the finished plan items, the final HANDOFF and its evidence to
   `agent/STATUS.archive.md` under `## YYYY-MM-DD — <task>` (append only; never read it later
   unless the user asks).
2. Close the task on the board: archive it to `agent/TASKS.archive.md` and remove its line
   (`ordnung-board`). Mark any requirements it met in PROJECT.md.
3. Reset STATUS.md. The next claimed task becomes the new HANDOFF with `status: IN_PROGRESS`.
   If nothing is ready, write `status: DONE` with `task: none`.

## 5. Interrupted

If you are about to be stopped or the context is near its limit, write the HANDOFF now with the
best `next_action` you have — a rough handoff beats none.
