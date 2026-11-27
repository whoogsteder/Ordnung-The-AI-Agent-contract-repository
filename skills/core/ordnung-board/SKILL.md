---
name: ordnung-board
description: Keeps the task board agent/TASKS.md — the one place open work lives in an Ordnung-contract project. Covers claiming a task into NOW, writing a task line with owner, refs, after-dependencies and a checkable done criterion, splitting a task that grew, parking new work discovered mid-task, WAITING on an owner decision, closing and archiving a task, and choosing what comes next. Use this whenever work is picked up or finished, when new work or a follow-up turns up during a task, when a task turns out bigger than its line, when the user asks "what's next", "what's open" or adds work, when several small tasks could ship together (proposing a batch), when a batched task turns out bigger than predicted, and when ordnung_check reports a TASKS or estimates finding.
---

# The task board

A project with many open tasks needs a queue that a resuming agent can read in seconds and that
no session can quietly rewrite. The board is that queue. STATUS.md says what you are doing now,
PROJECT.md says what must stay true, and the board says what is open and in what order.

Without a board, follow-ups get parked in STATUS notes or in chat, where the next compaction
drops them.

## The line
```
- [T-NN] <title, imperative> — owner: agent|owner|both — ref: <REQ-NN, ADR/DR-NNN dN, T-NN>
    after: T-NN, T-NN            (only when it really cannot start before them)
    done: <a criterion someone else can check: a test passes, a PR merged, the owner confirms X>
    <at most ~3 lines of context the next person needs; detail goes to a design doc>
```
- **IDs.** Take the next number above every ID on the board and in `agent/TASKS.archive.md`. An
  ID is never reused, even for a scrapped task.
- **`owner:`** says who must act for the task to move. An agent never moves an `owner` task, and
  never resolves a WAITING decision on the owner's behalf.
- **`done:`** is written when the task is claimed at the latest. If you can't state it, ask the
  owner as you claim the task. "Done" that nobody can check is how tasks reopen.
- **The section is the status.** NOW holds at most 2 *slots* for work the agent does (`owner:
  agent` or `both`). A slot is one task, or one batch the operator approved (below). Owner tasks
  in NOW don't count against that limit, since they are the owner's work in progress. NEXT holds
  ready tasks, in order.
  LATER is real but not ready. WAITING says `decision: ...` or `waits: <event, date>`.

## Claim
1. Take the top of NEXT, unless the user names another task. Check that its `after:` tasks are
   archived.
2. Move the line into NOW, and add the `done:` criterion if it is missing.
3. Write the HANDOFF with `task: T-NN <title>` (`ordnung-checkpoint`). The checker refuses a
   HANDOFF whose task is not in NOW.
4. A task that depends on a PROPOSED decision is not claimable. Raise the decision with the user,
   or claim the task that decides it.

## Batches (DR-005)
Each delivered change costs a merge, and on some setups every merge needs a second reviewer.
When several small tasks are ready, they can ship as **one batch: one branch, one PR, one review,
one merge**. Each task still keeps its own line, `done:` and evidence, and gets its own archive
line.

**Propose, never decide.** At claim time, a batch may be proposed when every candidate task:
- is low effort (a few files, well understood);
- is low risk (no stable surface, easy to revert);
- needs no decision, and depends on no PROPOSED one;
- is not excluded by the persona (iac: no ops work, and nothing that touches a live system —
  `iac-release`).

Put the proposal to the operator, and wait:
```
Batch proposal: <branch name>
| Task | Effort | Impact | Risk | How it will be checked |
| T-63 | low: one script + its doc | dev tooling only | low: env var with the old default | unit test + doc |
| ...  |
Why these fit together: <one line>
```
The operator decides each proposal. There is no fixed size, and tasks are never labelled as
batchable in advance: the judgement is made fresh, at claim time.

**On a yes:** move the tasks into NOW, each with `batch: <branch> (operator YYYY-MM-DD)` in its
detail. The checker counts that batch as one slot. The HANDOFF names every task:
`task: T-63, T-05, T-06 (batch <branch>)`.

**While the batch runs:** one commit per task, with its ID in the message. Each task's `done:` is
checked and its evidence recorded before you move to the next one.

**A task turns out bigger than predicted** (more files, a decision appears, a live system comes
into scope, a test you cannot make pass): **stop**.
1. Take the task out of the batch: remove its `batch:` line and move it back to NEXT with one
   line saying what you found. Drop or revert its commit on the batch branch.
2. Append one line to `agent/estimates.md`. Create the file from `agent/templates/estimates.md`
   if it doesn't exist yet. The format:
   `- YYYY-MM-DD · T-NN · <agent>/<model> · predicted: <effort, risk> · found: <what> · why: <cause> · then: <what happened to the task>`
   The checker enforces it. The file is read by the operator to improve the process, so be
   specific about *why* the estimate was wrong.
3. Report to the operator, then go on with the rest of the batch, unless the operator says
   otherwise.

**Review and merge:** a rejected item holds the whole merge. Fix it on the batch branch and ask
for the re-review. Never merge part of a batch: a partial merge leaves the rejected item
dangling, with nothing pushing anyone to fix it.

**Close:** after the merge, archive every task of the batch, each with its own line citing its
commit.

## While working
- **New work turns up:** add it to the board in the same response, in NEXT if it is ready,
  LATER if not, or WAITING with its blocker named. Never leave it in STATUS notes or in chat.
- **The task grew:** split it. Keep the part you are finishing, and file the rest as new IDs
  with `after:` links. Say so in the HANDOFF notes ("split from T-26").
- **Blocked on the owner:** move the task to WAITING with `decision: ...`. If the decision
  outlives the task, also write it as a Q-NN in PROJECT.md (`ordnung-ledger`). Claim the next
  task instead of waiting idle.
- **Many related tasks** (a phase, an epic) form a *track* in PROJECT.md, one line pointing at
  the range ("ADR-019 phase A: T-28…T-39"). The board holds the tasks; PROJECT holds the
  direction.

## Close
In the same response:
1. Check the `done:` criterion and put its evidence in the HANDOFF `evidence:` field.
2. Append to `agent/TASKS.archive.md`:
   `- YYYY-MM-DD · [T-NN] <title>: <one-line outcome, with the PR/commit/evidence>`
   Then remove the line from the board. The archive is append-only, and nobody reads it unless
   the user asks; scripts may grep it.
3. Run `ordnung-checkpoint`'s DONE step, then claim the next task.

## Review (when NEXT runs dry, or the user asks "what's left")
- Walk LATER and WAITING with the user. Move what has become ready to NEXT.
- Scrap tasks that no longer apply: archive them with "scrapped: <reason>".
- Check that every PROJECT.md track still points at open tasks.

## Do not
- Copy a task into STATUS, PROJECT or a design doc. Refer to it by ID.
- Edit a task's meaning silently. If the scope changes, say so in the line and in the HANDOFF.
- Read the whole archive to find an ID. Use `grep -o 'T-[0-9]*' agent/TASKS*.md | sort -V | tail -1`.
