# STATUS — the task in hand (≤ 40 lines; strategic facts go to PROJECT.md)

## HANDOFF
task: T-07 — port the knowledge-base persona from v1
status: IN_PROGRESS
next_action: Extract `contracts/persona/knowledge-base/rules/*.md` from the frozen v1 tag and condense each module into a persona skill.
skills: [ordnung-checkpoint, ordnung-board, ca-skill-authoring, ca-release, ca-evals]
constraints:
  - Public repository: no field-project names, hostnames or account names in anything committed; the reranker anecdote stays generic (ca-release, kernel rule 11).
  - Link v1 material by tag URL at `contracts-v1.4.0`, never by branch (DR-006).
  - Pushing, PRs and tags need the operator's go for that release (kernel rule 7).
files: personas/knowledge-base/, docs/lineage.md, README.md, CHANGELOG.md
evidence: `agent/ordnung_check` ok; `pytest tests/ -q` 44 passed; PR #20 open (2026-11-27)
last_update: 2026-11-27T13:06

## Plan
- [x] Claimed T-07, split the remaining ports to T-12, eval cases to T-13
- [x] persona.md + 9 kb-* skills under `personas/knowledge-base/`
- [x] lineage rows with v1 tag links, README persona row, CHANGELOG [Unreleased]
- [x] `pytest tests/` 44 passed, `agent/ordnung_check` ok, committed on this branch
- [x] Pushed; PR #20 open, awaiting the operator's review and merge

## Notes for the next action
A drafted port exists in a retired local checkout (branch `feat_knowledge-base-persona`, commit
`4eb9e5c` in `~/development/Ordnung-Zwei_old`): persona.md plus nine kb-* skills, written against the
pre-rc.1 layout. Treat it as a draft to review against `ca-skill-authoring`, not to cherry-pick —
that checkout is superseded and must never be pushed.
Kernel rule 9 wants an eval case per behaviour change; the port ships with T-13 filed for the cases,
the same way advisory and iac shipped before T-04/T-05. Say that plainly in the PR rather than
implying the skills are proven.
