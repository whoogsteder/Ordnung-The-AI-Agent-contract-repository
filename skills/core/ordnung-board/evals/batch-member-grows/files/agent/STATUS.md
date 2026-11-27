# STATUS

## HANDOFF
task: T-3, T-4, T-5 (batch chore_dev_tooling)
status: IN_PROGRESS
next_action: Start T-3 by replacing the hard-coded container name in scripts/dev/local_db.sh with NETCTL_DB_CONTAINER.
skills: [ordnung-checkpoint, ordnung-board, iac-release, iac-python]
constraints:
  - Batch approved by the operator as development-only work: nothing that touches production.
files: scripts/dev/local_db.sh, docs/dev/setup.md, scripts/dev/render_preview.py
evidence: none
last_update: 2026-11-27T09:00

## Plan
- [ ] T-3 (commit), T-4 (commit), T-5 (commit); full suite on the tip; PR with checklist
