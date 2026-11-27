# STATUS — the task in hand (≤ 40 lines; strategic facts go to PROJECT.md)

## HANDOFF
task: T-09 Implement batching (DR-005) and agent/estimates.md
status: IN_PROGRESS
next_action: Open the PR for feat_dr005_batching and merge it on the operator's go, then archive T-09.
skills: [ordnung-checkpoint, ordnung-board, ca-skill-authoring, ca-release]
constraints:
  - A parallel session works in the main checkout (T-07, PR #20); this work lives in the ../Ordnung-batching worktree.
  - The operator field-tests batching in project B today: keep the change additive for installed projects.
files: tools/ordnung_check, skills/core/ordnung-board/SKILL.md, personas/iac/skills/iac-release/SKILL.md
evidence: pytest tests/ (see the PR) and agent/ordnung_check
last_update: 2026-11-27T15:07

## Plan
- [x] DR-005 accepted; T-09 into NOW
- [x] Checker: batch slots, HANDOFF batch tasks, estimates format; tests
- [x] ordnung-board Batches, iac-release batch PR, iac rule 12, estimates template, eval case
- [ ] PR, merge, archive T-09

## Notes for the next action
- The eval case batch-member-grows is written but not yet run (T-05 runs the board cases).
