# Agent Status

## HANDOFF
phase: game-hosting platform amendments (branch feat_game-hosting-platform, off main 72c3c28)
status: IN_PROGRESS
next_action: Wait for the operator to review and merge PR #14 (game-hosting 2.0.0); then return to field-test round 2 (corrected pack v0.6, then document-writing).
files: contracts/persona/game-hosting/{rules/base.md,rules/web_frontend.md,rules/docker_compose.md,rules/python.md (new),agent/bootstrap.md,agent/ruleset.md,AGENTS.md,docs/agent-contract/panel-platform.md (new),docs/agent-contract/index.md}, README.md, agent/REPO-MAP.md, CHANGELOG.md. check_sync OK; pytest 15/15 after re-stamp
notes: Operator-approved 2026-11-21 (all four, explicitly): (1) web panel always part of the delivery, optional only local vs internet-exposed, game keeps running when the panel stops; (2) python.md module for panel/probe tooling; (3) env file = stack settings only, game settings in native config files the panel writes via a profile; (4) one panel manages many servers and may create/own game containers itself; the operator added that a many-server panel must show the project containers' resource usage. First consumer: the Game Commons project (/home/whoogsteder/development/Game-Commons). The field-test-fixes PR (#13) is merged.
last_update: 2026-11-21T11:58

## Active Tasks
- [ ] game-hosting 2.0.0: committed 9814b51, PR #14 open; copied to Game-Commons. Merge awaits the operator
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
