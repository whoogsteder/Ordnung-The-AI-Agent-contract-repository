# Agent Status

## HANDOFF
phase: Restructure — self-hosting (step 1 of approved plan)
status: IN_PROGRESS
next_action: Move IaC/ and administrative/ to contracts/persona/{iac,administrative}/ with git mv, then add seam markers to all persona rule files.
files: rules/base.md, rules/verification.md, agent/ruleset.md, agent/REPO-MAP.md
notes: Root core sections verified byte-identical to IaC originals (marker-stripped); core-sync doc not yet written — follow plan in chat history. Leave IaC/rules/zoo-dcg-bug.md untouched (user's file).

## Active Tasks
- [ ] Move personas to contracts/persona/ (git mv, case fix included)
- [ ] Add seam markers + slot headings to persona rule files
- [ ] Write tools/check_sync + tests/test_check_sync.py; green run
- [ ] Persona manifests (agent/ruleset.md), versions 1.0.0
- [ ] docs/authoring/core-sync.md + persona-anatomy.md
- [ ] agent/bootstrap.md for repo-maintainer; update README
