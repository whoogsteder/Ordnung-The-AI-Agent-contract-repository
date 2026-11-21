# Agent Status

## HANDOFF
phase: iac ADR location fix (branch fix_iac-adr-location, off main b53958f)
status: DONE
next_action: Push `fix_iac-adr-location` and open the PR for the iac ADR-location fix (commit 3aba410), then return to field-test round 2 (corrected pack v0.6, then document-writing).
files: contracts/persona/iac/{agent/project_layout.md,rules/adr.md,rules/base.md,docs/agent-contract/base-contract.md,agent/ruleset.md}, CHANGELOG.md
notes: Operator-reported conflict, fixed on their explicit request. `agent/project_layout.md` had nested ADRs at `docs/architecture/adr/` while `rules/adr.md`, `rules/base.md`, `agent/bootstrap.md` and `AGENTS.md` all said `docs/adr/`. End state the operator chose: ADRs land in `docs/adr/` and stay there; `docs/architecture/` remains for design write-ups, which cite `ADR-NNN decision N` and link `../adr/NNN-<topic>.md` instead of holding records; an archived design keeps its citations and the records never travel into `docs/archive/`. iac manifest 1.4.0 -> 1.5.0. Other personas audited: administrative, document-writing, game-hosting and research use `docs/decisions/` consistently across layout guide, rules and bootstrap; `review` ships no decision records — no change needed there. Checks: `python3 tools/check_sync` OK, `python3 tools/status_fresh` OK, pytest 15/15.
last_update: 2026-11-21T13:44

## Active Tasks
- [ ] Push `fix_iac-adr-location` + open PR (iac 1.5.0, commit 3aba410); merge awaits the operator
- [ ] Field-test round 1 done (research + review); fixes on feat_field-test-fixes. Round 2: corrected pack v0.6, then document-writing
- [ ] Decide the fate of feat_tech-writing-v2 (0477e3e): rework it, merge it, or drop it
- [ ] Next release act: turn ## [Unreleased] (review persona + field-test fixes + game-hosting 2.0.0 + iac 1.5.0) into ## [1.5.0] and tag it
- [ ] Optional, declined for now: delete the merged branches still on origin

## Notes
- Git config hazard: `remote.origin.fetch` had been narrowed to main only, which made this clone look like it had lost its git tracking data. It now reads `+refs/heads/*:refs/remotes/origin/*`; do not narrow it again.
- Environment moved to linux/bash: commands chain normally. `python3 tools/check_sync` and `python3 tools/status_fresh` both run here.
- Never rewrite a repo file's content through PowerShell: a Get-Content/Set-Content round trip decodes UTF-8 as the ANSI code page and mangles every em dash and emoji (hit agent/STATUS.md on 2026-11-10). Edit content with the editor tool; stamp the memory file by setting LastWriteTime only, never by rewriting it.
- Stamp discipline: `python3 tools/status_fresh`, exit 0 means current. Write `last_update` at minute granularity, then set the file's mtime to that same minute (`touch -t YYYYMMDDhhmm.00`) — the probe fails when mtime is newer than the stamp, and a checkout rewrites mtime, so re-stamp after one.
- gh CLI is authenticated as whoogsteder (repo scope): push, PR create, PR edit --body-file, PR view and PR merge all work. main is not branch-protected, but contract commits ride a `<type>_<topic>` branch through a PR by default.
- Release discipline (README "Editing a contract" bullet and CONTRIBUTING.md): contributors bump the manifests they touched, the maintainer writes the CHANGELOG.md entry and pushes the tag.
