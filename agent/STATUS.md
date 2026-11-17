# Agent Status

## HANDOFF
phase: tech-writing persona v2.0.0 rework - branch feat_tech-writing-v2
status: IN_PROGRESS
next_action: User reviews the uncommitted tech-writing 2.0.0 changes on feat_tech-writing-v2; on approval commit, push and open a PR. Then field-test 2.0.0 by rerunning the switch selection from its requirements brief.
files: contracts/persona/tech-writing/ (rules/, agent/, docs/agent-contract/), README.md, CHANGELOG.md, agent/REPO-MAP.md
notes: Driver - the first real document made with v1.2.0 (a LAN switch selection) was 50 pages, hard to read, and recommended two switches that failed its own must-haves (specs written from memory, tagged unverified, recommended anyway). Rework: research/fact-check gate, confirmed requirements brief before drafting, writing style + page budget, document-type profiles, governance demoted to release time. Core sections untouched (one-commit rule); the core frequency guard is raised with the user as a cross-persona proposal, not changed here.
Checks 2026-11-17 on the working tree: check_sync OK; pytest 14 passed (uv run --with pytest). Nothing committed yet.
last_update: 2026-11-17T19:45

## Previous release record
phase: contracts-v1.2.0 released - the Document archiving rule is shipped and tagged
status: DONE
files: agent/STATUS.md
notes: Release record - the annotated tag contracts-v1.2.0 is tag object 0846341 pointing at commit 7a97bef, the merge commit of PR #7 (the release act) on main, pushed to origin. The change it ships is the Document archiving rule: PR #6, merged as 1315da7, branch commit f9abafe. All five manifests read 1.2.0. For comparison, contracts-v1.1.0 is tag object 963dfe8 at commit e848438.
last_update: 2026-11-10T11:52:00

## Active Tasks
- [x] DONE - Document archiving rule shipped: the `slot: documentation` section in all five base.md copies, the ARCHIVED status marker in the core Context discipline bullet, docs/archive/ (and documents/archive/ for tech-writing) in the four layout guides with frozen-history guards, a rationale section in each of the four base-contract.md pages, rationale index rows, the core-sync.md section-map row, README bullets, CHANGELOG entry, manifests 1.1.0 -> 1.2.0. Branch feat_docs-archiving-rule, commit f9abafe, PR #6 merged into main as 1315da7.
- [x] DONE - Release act for contracts-v1.2.0: CHANGELOG entry turned into ## [1.2.0] - 2026-11-10 with the tag/manifest line and the compare links, fresh empty ## [Unreleased] on top (commit 2f302ed), PR #7 merged into main as 7a97bef, annotated tag contracts-v1.2.0 (tag object 0846341) created on that merge commit and pushed. The manifests already read 1.2.0, so the release carried no version change of its own.

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
