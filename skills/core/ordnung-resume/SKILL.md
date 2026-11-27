---
name: ordnung-resume
description: Restores the working context of an Ordnung-contract project from its files — project memory, the current task's HANDOFF, the skills and constraints that task needs. Use this at the start of every session, immediately after any context summary or compaction, after being handed a conversation summary instead of the full history, when you are unsure what you were doing, or when the user asks "where were we", "continue", "pick up where you left off". Use it even if you think you remember — after a summary you remember the gist, not the rules.
---

# Resume

After a summary or a fresh start you carry a compressed story of the work, and compressed
stories drop exactly the things that steer you: task-scoped constraints, the skill that was
governing the work, the decision the user made three hours ago. This skill rebuilds that from
the files, which do not forget.

## Steps

1. **Run the check.** `python3 agent/ordnung_check`. If it fails on STATUS (stale,
   oversize, schema), fixing STATUS is your first task — load `ordnung-checkpoint` and repair it
   from what you know *before* doing anything else. A stale STATUS is never someone else's debt.
   If `agent/PROJECT.md` does not exist, this is a new project: load `ordnung-bootstrap` instead.

2. **Read project memory in full:** `agent/PROJECT.md`. It is short on purpose. Note anything
   under *Waiting on the user* — work that depends on an open question stays parked.

3. **Read the HANDOFF** in `agent/STATUS.md`, then the **NOW and WAITING sections** of
   `agent/TASKS.md`. Don't read NEXT or LATER now: you need them only when this task closes.

4. **Re-load what the task named.** Load every skill in the HANDOFF `skills:` list. Then
   restate the `constraints:` lines to yourself as rules for this session — they are the
   task-scoped steering that a summary is most likely to have lost.

5. **Echo to the user** in a few lines, then continue:
   ```
   Resuming: <task> — <status>
   Next: <next_action>
   Constraints: <constraints, or "none">
   Waiting on you: <Q-NN lines that block this task, or "nothing">
   ```
   If `next_action` depends on a `Q-NN` that is still open, ask that question instead of
   proceeding.

## Do not

- Do not read `agent/STATUS.archive.md`, `agent/TASKS.archive.md`, `docs/archive/` or
  `docs/agent-contract/`. They are
  history, and loading them is the context bloat this contract exists to prevent.
- Do not walk the repository. Use `agent/REPO-MAP.md` to scope the first targeted read the next
  action needs.
- Do not trust the summary over the files. Where they disagree, the files win; if the files
  look wrong, say so to the user.
