# Agent Status

## HANDOFF
phase: security-advisories drive — discarded by user; lessons landed on main
status: DONE
next_action: None required. Optional: push to origin (old remote URL redirects fine), tag contracts-v1.0.0, or start the real security persona with our own team using tools/new_persona.
files: tools/new_persona, CONTRIBUTING.md
notes: Evidence 2026-10-28 — branch feat_security-advisories-persona deleted (throwaway proven, user chose to discard; own security team will author the real one). Fix kept on main: new_persona now strips ALL template persona blocks + genericized slot hints; smoke test in throwaway copy shows clean scaffold (core+slots+stub only) and check_sync OK. pytest 8 passed.

## Active Tasks
- [ ] Own security team: author the real security persona via tools/new_persona
- [ ] Decide: keep or remove contracts/persona/iac/rules/zoo-dcg-bug.md (untracked user file)
- [ ] Optional: tag contracts-v1.0.0 now that v1.0.0 manifests are public
