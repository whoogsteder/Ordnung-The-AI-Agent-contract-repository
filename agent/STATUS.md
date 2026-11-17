# Agent Status

## HANDOFF
phase: contracts 1.3.0 - core checkpoint rule + digest, then new personas document-writing and research (branch feat_core-checkpoint-and-doc-personas)
status: IN_PROGRESS
next_action: User reviews branch feat_core-checkpoint-and-doc-personas (2 commits, local only); on approval push and open a PR. Then field-test document-writing + research on the LAN switch selection.
files: contracts/persona/document-writing/, contracts/persona/research/, contracts/persona/*/AGENTS.md, contracts/persona/*/rules/base.md, CHANGELOG.md, README.md, agent/REPO-MAP.md
notes: Commit 53494d2 = core checkpoint rule + digests (manifests 1.3.0). Second commit = the two new personas (1.0.0). tech-writing stays as the 1.x reference persona (core-synced only); its 2.0 rework lives on feat_tech-writing-v2 (0477e3e) and is not to be merged. Nothing pushed. Gates 2026-11-17: check_sync OK, pytest 14 passed. Previous release record (contracts-v1.2.0) is in STATUS.archive.md.
last_update: 2026-11-17T21:00

## Active Tasks
- [x] document-writing persona 1.0.0
- [x] research persona 1.0.0
- [x] README table, REPO-MAP, CHANGELOG; check_sync + pytest
- [ ] User review, push, PR

## Notes
- Never rewrite a repo file's content through PowerShell: a Get-Content/Set-Content round trip decodes UTF-8 as the ANSI code page and mangles every em dash and emoji (hit agent/STATUS.md on 2026-11-10; repaired by `git checkout HEAD -- agent/STATUS.md` plus a re-edit). Edit content with the editor tool; stamp the memory file by setting LastWriteTime only, never by rewriting it.
- check_sync gates contract edits (OK 2026-11-10); pytest gates tools/ and tests/ edits and is not runnable in this environment (no uv, no pytest on system python 3.15.1).
- Run python tools/status_fresh to check this file's freshness; exit 0 means current. Stamp last_update at minute granularity, then set the file's LastWriteTime to that same minute: the probe compares at second precision, so a minute-granularity stamp only passes when the mtime sits on the boundary. A branch switch or checkout rewrites the mtime, so re-stamp after one.
- gh CLI 2.103.3 is installed and authenticated as whoogsteder (repo scope): push, PR create, PR edit --body-file, PR view and PR merge all worked this session.
- Release discipline is documented for contributors: the README "Editing a contract" bullet and CONTRIBUTING.md - contributors bump the manifests they touched, the maintainer writes the CHANGELOG.md entry and pushes the tag.
- Shell transport in this environment: only the last command of a run_commands batch reliably runs, so git steps go one per call and every gate run goes to a log file that is read afterwards.
- Branch cleanup 2026-11-10: the five merged branches (feat_core-memory-guard-hardening, feat_persona-tech-writing, chore_release-contracts-v1.1.0, chore_memory_record-the-v1.1.0-tag, chore_memory_restamp-last-update) are deleted from origin and locally; git ls-remote --heads origin lists refs/heads/main only. Expect no old branch names on the remote.
- Transport hazard with the editor tool: text that looks like tool markup (an angle-bracket tag naming a parameter) inside an edit payload can leak into the file. A CHANGELOG.md link-block edit once injected two such lines plus a duplicated link row; repaired by a stdlib Python script that deleted the rows by index and asserted the expected counts, reading and writing with newline='' so CRLF survived and no BOM was added. Keep markup-shaped strings out of edit payloads, and verify a tail edit with git diff.
- main is not branch-protected (gh api repos/whoogsteder/Ordnung-The-AI-Agent-contract-repository/branches/main -> "protected": false, protection endpoint HTTP 404). By the user's choice this cleanup's memory commit was pushed straight to main; every earlier memory commit rode a <type>_<topic> branch through a PR.
