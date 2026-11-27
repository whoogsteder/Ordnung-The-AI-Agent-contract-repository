# STATUS — the task in hand (≤ 40 lines; strategic facts go to PROJECT.md)

## HANDOFF
task: T-01 Release contracts-v2.0.0-rc.1: Zwei replaces v1 on main
status: IN_PROGRESS
next_action: Merge the replacement PR, then tag contracts-v2.0.0-rc.1 on the merge commit and publish it as a pre-release.
skills: [ordnung-checkpoint, ordnung-board, ca-release]
constraints:
  - The repo is public: nothing from field project B's internals goes out, history included (kernel rule 11).
  - The local ~/development/Ordnung-Zwei checkout is superseded by this repo from the merge on.
  - v1 stays frozen at contracts-v1.4.0; nothing from it returns to the tree (DR-006).
files: CHANGELOG.md, README.md, docs/lineage.md, docs/field-tests/
evidence: on branch chore_ordnung_zwei_main — pytest tests/ and agent/ordnung_check (see PR)
last_update: 2026-11-27T12:24

## Plan
- [x] Freeze v1 (contracts-v1.4.0, GitHub release)
- [x] Decision records DR-001..006, feedback log, dogfood persona and self-install
- [x] CHANGELOG 2.0.0-rc.1, README, lineage links to the tag; public-name guard test
- [x] Field-test drafts dropped; Zwei brought in as one squashed commit (operator, 2026-11-27)
- [ ] Replacement PR on the public repo; merge; tag; pre-release

## Notes for the next action
- Zwei's local commits stay local (they hold the dropped drafts); never push that checkout.
