# Agent Status

## HANDOFF
phase: Restructure — persona move + seam markers (step 2 of approved plan)
status: IN_PROGRESS
next_action: Add seam markers and slot headings to all rule files under contracts/persona/{iac,administrative}/rules/, then write tools/check_sync.
files: agent/REPO-MAP.md, README.md
notes: Personas moved with git mv (history preserved). Root core sections verified byte-identical to iac originals (marker-stripped). Leave contracts/persona/iac/rules/zoo-dcg-bug.md untouched (user's file).

## Active Tasks
- [ ] Add seam markers + slot headings to persona rule files
- [ ] Write tools/check_sync + tests/test_check_sync.py; green run
- [ ] Persona manifests (agent/ruleset.md), versions 1.0.0
- [ ] docs/authoring/core-sync.md + persona-anatomy.md
- [ ] agent/bootstrap.md for repo-maintainer; final README polish
