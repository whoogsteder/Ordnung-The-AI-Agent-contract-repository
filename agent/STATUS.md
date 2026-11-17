# Agent Status

## HANDOFF
phase: post-PR #11 hygiene (main == origin/main == 224c4df)
status: IN_PROGRESS
next_action: Field-test the research -> document-writing -> review chain on the LAN switch selection; the review persona is merged and waits under ## [Unreleased] for the next release act.
files: contracts/persona/review/, contracts/persona/document-writing/, contracts/persona/research/, feat_tech-writing-v2 (unmerged, 0477e3e)
notes: contracts-v1.3.0 is the newest tag (tag object b022339 on d26ce72). Working tree is byte-identical to GitHub: `git diff origin/main` is empty. Gates run locally; the repo has no CI.
last_update: 2026-11-17T20:15

## Active Tasks
- [ ] Field-test research -> document-writing -> review on the LAN switch selection
- [ ] Decide the fate of feat_tech-writing-v2 (0477e3e): rework it, merge it, or drop it
- [ ] Next release act: turn the ## [Unreleased] review-persona entry into ## [1.4.0] and tag it
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
