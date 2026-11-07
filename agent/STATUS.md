# Agent Status

## HANDOFF
phase: contract adaptation — memory-rule hardening from field feedback
status: IN_PROGRESS
next_action: Commit the feat_core-memory-guard-hardening working tree as one commit (core change touches all 4 base.md copies + 3 persona bootstraps + 4 manifests), then report to the user; release/tagging was explicitly canceled and stays out of scope.
files: rules/base.md, contracts/persona/{iac,administrative,game-hosting}/rules/base.md, contracts/persona/{iac,administrative,game-hosting}/agent/bootstrap.md, agent/bootstrap.md, contracts/persona/*/agent/ruleset.md, agent/ruleset.md, contracts/persona/{iac,administrative}/docs/agent-contract/{base-contract.md,memory-and-bootstrap.md}
notes: Evidence 2026-11-07 — `python3 tools/check_sync` prints OK; `uv run --with pytest --no-project python -m pytest tests/ -q` = 8 passed. Change set: Session continuity core rewritten (mechanical triggers incl. failing tests + probe files, observable frequency guard, resume-from-summary rule, read-back rule), Context discipline gained a read-back bullet, HANDOFF schema gained `last_update:`; all four base.md copies byte-identical in those sections (check_sync enforces). Enforcement decision: no hook/checker shipped in tools/ — unshippable with drop-in personas; instead each persona bootstrap step 5 offers the agent to author a project-local freshness probe, decline = completed step. Root agent/bootstrap.md carries the dogfood note. Versions bumped 1.0.0 → 1.1.0 (minor). Rationale prose added to iac + administrative docs/agent-contract (base-contract.md gained "Why the triggers are spelled out mechanically"; memory-and-bootstrap.md diagram + failure table updated); game-hosting ships no rationale page — it has no memory-and-bootstrap page to extend, deliberate asymmetry.
last_update: 2026-11-07T19:05

## Active Tasks
- [ ] Commit the contract adaptation on branch `feat_core-memory-guard-hardening` (all core edits must land in one commit).

