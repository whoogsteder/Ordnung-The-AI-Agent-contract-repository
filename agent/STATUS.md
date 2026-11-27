# Agent Status

## HANDOFF
phase: final v1 release (contracts-v1.4.0); v1 frozen, Ordnung-Zwei becomes main at 2.0.0-rc.1
status: DONE
next_action: None in v1 — work continues under the Ordnung-Zwei contract on main (its own agent/STATUS.md).
files: CHANGELOG.md
notes: Operator decision 2026-11-27: freeze v1 under a tag and make Ordnung-Zwei the leading content as a 2.0.0 release candidate. knowledge-base 1.0.0 merged (PR #16) before the freeze. feat_tech-writing-v2 (0477e3e) not merged — local only, conflicts with main, superseded by document-writing; kept as tag archive/tech-writing-v2. Checks: `python3 tools/check_sync` OK, pytest 15/15.
last_update: 2026-11-27T11:45

## Active Tasks
- [ ] iac 1.5.0: committed 3aba410, PR #15 open; merge awaits the operator
- [ ] Field-test round 1 done (research + review); fixes on feat_field-test-fixes. Round 2: corrected pack v0.6, then document-writing
- [ ] Optional, declined for now: delete the merged branches still on origin

## Notes
- Git config hazard: `remote.origin.fetch` had been narrowed to main only, which made this clone look like it had lost its git tracking data. It now reads `+refs/heads/*:refs/remotes/origin/*`; do not narrow it again.
- Environment moved to linux/bash: commands chain normally. `python3 tools/check_sync` and `python3 tools/status_fresh` both run here.
- Never rewrite a repo file's content through PowerShell: a Get-Content/Set-Content round trip decodes UTF-8 as the ANSI code page and mangles every em dash and emoji (hit agent/STATUS.md on 2026-11-10). Edit content with the editor tool; stamp the memory file by setting LastWriteTime only, never by rewriting it.
- Stamp discipline: `python3 tools/status_fresh`, exit 0 means current. Write `last_update` at minute granularity, then set the file's mtime to that same minute (`touch -t YYYYMMDDhhmm.00`) — the probe fails when mtime is newer than the stamp, and a checkout rewrites mtime, so re-stamp after one.
- gh CLI is authenticated as whoogsteder (repo scope): push, PR create, PR edit --body-file, PR view and PR merge all work. main is not branch-protected, but contract commits ride a `<type>_<topic>` branch through a PR by default.
- Release discipline (README "Editing a contract" bullet and CONTRIBUTING.md): contributors bump the manifests they touched, the maintainer writes the CHANGELOG.md entry and pushes the tag.
