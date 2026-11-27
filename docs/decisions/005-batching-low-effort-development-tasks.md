# DR-005: Batching low-effort development tasks

## Context
Operator feedback from the IaC field test (2026-11-27). The one-task, one-branch, one-PR flow
works, but sometimes it "works too well". The pain is the merge, not the review: on the
operator's company GitHub, every merge to main needs a second reviewer, which becomes painful in
a heavy development cycle. The operator has several times told the agent to handle a set of small
tasks in one go and review them afterwards.

## Decision (proposed)
1. The task stays the unit of tracking. Each task keeps its board line, its `done:` criterion, its
   own evidence and its own archive line.
2. At claim time the agent may propose a batch of tasks that are low in both effort and risk, and
   that need no decision. For each task it states the predicted effort, impact and risk. **The
   operator decides** each proposal. There is no fixed size limit, and nothing is labelled as
   batchable ahead of time, because different agents judge differently.
3. A batch is one branch, one PR, one review and one merge.
   - One commit per task, with the task ID in the message.
   - The full suite runs once, on the batch tip.
   - The PR has a checklist with one line per task: impact, risk, and how it was checked.
   - There is one version bump and one changelog entry for the batch.
4. **A rejected item holds the whole merge** until it is fixed. A partial merge leaves things
   dangling and removes the pressure to fix them.
5. A task that proves bigger than predicted stops the work. The agent takes it out of the batch,
   puts it back in NEXT and reports to the operator. It also appends one line to
   `agent/estimates.md`:
   `date · task · agent/model · predicted (effort, risk) · found · why · what happened`.
   The file feeds straight into process improvement.
6. **Never batched:** ops tasks, and anything that touches a live system. A development host, a
   test host, and acceptance systems when the operator says so, are the exceptions. Production
   always gets control task by task.

## Consequences
- This would touch `ordnung-board` (proposing and closing a batch), `iac-release` (the batch PR),
  the templates (`agent/estimates.md`) and the checker (the estimates line format).
- Enforced by (planned, after the operator accepts): a checker rule for the format of
  `agent/estimates.md` lines, and an eval case where a batch member proves bigger than predicted.

## Status
PROPOSED (2026-11-27). The operator asked not to change anything yet: "Actual use will tell."
