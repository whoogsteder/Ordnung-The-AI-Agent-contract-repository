# Agent Status

## HANDOFF
phase: field-test fixes (branch feat_field-test-fixes, off main 1c397b2)
status: IN_PROGRESS
next_action: Wait for the user to review and merge the field-test-fixes PR; then field-test round 2 (corrected pack v0.6, then document-writing).
files: rules/base.md + contracts/persona/*/rules/base.md (core), contracts/persona/{research,review,document-writing}/, tools/status_fresh, tests/test_check_sync.py, CHANGELOG.md
notes: Source of the fixes: F-001..F-014 in the user's field-test log (outside this repo) plus two research gaps (lifecycle from vendor lifecycle record; ambiguous must-have terms). Rejected: F-013 item 5 (two-round bound) and F-014 reviewer error-rate counting. research bumped to 2.0.0 (pack dir research/ -> topics/).
last_update: 2026-11-18T13:07

## Active Tasks
- [ ] Field-test round 1 done (research + review); fixes on feat_field-test-fixes. Round 2: corrected pack v0.6, then document-writing
- [ ] Decide the fate of feat_tech-writing-v2 (0477e3e): rework it, merge it, or drop it
- [ ] Next release act: turn ## [Unreleased] (review persona + field-test fixes) into ## [1.4.0] and tag it
- [ ] Optional, declined for now: delete the six merged branches still on origin

## Notes
- Git config hazard: `remote.origin.fetch` had been narrowed to main only, which made this clone look like it had lost its git tracking data. It now reads `+refs/heads/*:refs/remotes/origin/*`; do not narrow it again.
- The 2026-11-10 claim that `git ls-remote --heads origin` lists refs/heads/main only is no longer true: PRs #6-#11 left six merged branches on origin (chore_memory_record-the-v1.2.0-tag, chore_release-contracts-v1.2.0, chore_release-contracts-v1.3.0, feat_core-checkpoint-and-doc-personas, feat_docs-archiving-rule, feat_persona-review).
- Environment moved to linux/bash: commands chain normally, so the old run_commands one-command-per-call workaround does not apply. `python3 tools/check_sync` and `python3 tools/status_fresh` both run here.
- Never rewrite a repo file's content through PowerShell: a Get-Content/Set-Content round trip decodes UTF-8 as the ANSI code page and mangles every em dash and emoji (hit agent/STATUS.md on 2026-11-10). Edit content with the editor tool; stamp the memory file by setting LastWriteTime only, never by rewriting it.
- Transport hazard with the editor tool: text that looks like tool markup (an angle-bracket tag naming a parameter) inside an edit payload can leak into the file. Keep markup-shaped strings out of edit payloads, and verify a tail edit with git diff.
- Stamp discipline: `python3 tools/status_fresh`, exit 0 means current. Write `last_update` at minute granularity, then set the file's mtime to that same minute — the probe fails when mtime is newer than the stamp, and a checkout rewrites mtime, so re-stamp after one.
- gh CLI is authenticated as whoogsteder (repo scope): push, PR create, PR edit --body-file, PR view and PR merge all work. main is not branch-protected, but memory commits ride a `chore_<topic>` branch through a PR by default.
- Release discipline (README "Editing a contract" bullet and CONTRIBUTING.md): contributors bump the manifests they touched, the maintainer writes the CHANGELOG.md entry and pushes the tag.
