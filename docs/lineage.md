# Lineage — where each v1 piece went

v1 reference: tag [`contracts-v1.4.0`](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0),
the final v1 release (DR-006). Every v1 path below is relative to that tag; for example, v1 iac
`verification.md` is
<https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/blob/contracts-v1.4.0/contracts/persona/iac/rules/verification.md>.
Personas there: iac, administrative, game-hosting (2.0.0), document-writing, research, review,
knowledge-base; the unmerged tech-writing 2.0.0 rework is tag `archive/tech-writing-v2`.
Field project used for measurement: field project C, a dedicated game-server stack (game-hosting
1.1.0 + a project-local `go.md`).

Legend: **kept** (same intent, moved), **changed**, **dropped**, **not yet ported**.

## Core (v1 `rules/base.md` + `agent/`)

| v1 piece | Zwei location | Verdict | Why |
|---|---|---|---|
| AGENTS.md boot: "read every rules/*.md" | `AGENTS.md` kernel → `ordnung-resume` | changed | Read-everything at boot was the main context cost |
| Contract digest in AGENTS.md (2.0) | `AGENTS.md` Non-negotiables | kept | Worked: it is the part harnesses re-inject |
| Context discipline | `ordnung-resume`, kernel rule 1 | kept | |
| Read-back at pressure points | `ordnung-resume` "after any summary" | changed | Trigger is now an event the agent can detect, not a judgment |
| REPO-MAP maintenance | `ordnung-ledger` § REPO-MAP | changed | Hard 120-line cap + area maps |
| Session continuity / checkpoint at moments (2.0) | `ordnung-checkpoint` | kept | |
| Frequency guard (5 tool calls) (1.1) | dropped | dropped | 2.0 already replaced it; the count was never kept |
| HANDOFF format | `ordnung-checkpoint` § schema | changed | + `task`, `skills`, `constraints`, `evidence`; `phase` folded into task |
| Archiving | `ordnung-checkpoint` § archive | kept | |
| Size guard 40 lines | `tools/ordnung_check` | changed | Enforced by script + hook, not memory |
| Decision Records | `ordnung-ledger` § decisions | kept | Index line in PROJECT.md, record in docs/decisions |
| Rule files are read-only | kernel rule 5 | kept | Now covers `.agents/skills/` |
| bootstrap.md | `ordnung-bootstrap` | kept | License picker unchanged |
| `tools/status_fresh` | `tools/ordnung_check` (freshness check) | kept | Same logic, one entry point |
| `tools/check_sync` + seam markers | not ported | not yet ported | Shared files instead of copies; see design Q3 |
| `docs/agent-contract/` rationale | `docs/` per skill or `references/` | changed | Skills explain their *why* inline, per skill-creator guidance |
| — (new) | `agent/PROJECT.md`, `ordnung-ledger` | new | Strategic layer was missing |
| — (new) | `ordnung-delegate` | new | v1 assumed no subagents (except review) |

## game-hosting persona (Ordnung 2.0.0 → `personas/game-hosting/`)

| v1 module | Zwei skill | Verdict |
|---|---|---|
| base.md role + state-history slot | `personas/game-hosting/persona.md` (kernel lines) + `gh-compose` | changed |
| docker_compose.md | `gh-compose` | kept, condensed |
| steamcmd.md | `gh-steamcmd` | kept, condensed |
| web_frontend.md (panel always bundled, 2.0) | `gh-web-panel` | kept, condensed |
| verification.md | `gh-verification` | kept |
| usability.md + documentation slot | `gh-operator-docs` | merged |
| python.md | `gh-python` | not yet ported (port when a Python panel is in scope) |
| project C's `go.md` (project-local, never in Ordnung) | — | not yet ported |

## Other v1 personas

Not ported in this draft. The review persona's "independence by inputs" idea is reused in
`ordnung-delegate` § verification subagent. Port others only after the field test.

## advisory persona (v1 document-writing 1.2.0 + research → `personas/advisory/`)

One persona covers the whole flow: grilling, research, then the advisory. In v1 that took two
personas and a hand-over between projects. The research pack stays as the contract between the
stages, and wide searches go to workers (`ordnung-delegate`) instead of to a second project.

| v1 module | Zwei location | |
|---|---|---|
| requirements.md, open_questions.md | `adv-grilling` (brief, gate); open decisions → Q-NN in PROJECT.md | changed: the brief is written round by round, so compaction can't lose answers |
| research question.md, method.md, sources.md, research_pack.md | `adv-research` | condensed |
| facts.md, comparisons.md, doc_types.md, writing.md, documents.md, visuals.md | `adv-advisory` | condensed; new "implementation impact per pick" |
| verification.md, classification.md, output_formats.md | `adv-review` | condensed; reviewer = worker |
| dr.md | `ordnung-ledger` (core) | merged |
| OQ register in REPO-MAP | Q-NN in PROJECT.md | changed |
| research reporting.md | `adv-research` "Handing over" + `adv-advisory` | merged |

## iac persona (v1 iac 1.5.0 + field project B's rule set → `personas/iac/`)

Field project B (an IaC firewall-management tool, docs/field-tests/feedback.md) ran a field-hardened copy of the v1 rules. Where it differs from v1 iac
1.5.0, its wording was used.

| v1 / project B | Zwei location | |
|---|---|---|
| base.md Task board (TASKS.md: NOW/NEXT/LATER/WAITING, T-NN, owner, after, done) | **core**: `ordnung-board`, `templates/agent/TASKS.md`, board checks in `ordnung_check` | promoted from a project habit to core; NOW caps agent tasks only |
| base.md Security | kernel rule 11 + `iac-python` (safe APIs) + `iac-live` (TLS, credentials) | split |
| base.md Versioning & branches, ADR-005 | kernel rule 12 + `iac-release` | condensed |
| base.md Documentation, status markers | `iac-verification` (docs ship with the change) + `ordnung-ledger` (REPO-MAP markers) | split |
| python.md, ansible.md | `iac-python`, `iac-ansible` | kept, with additions (locking, collections, running Ansible from code) |
| terraform_tfgrunt.md | `iac-terraform` | condensed |
| verification.md | `iac-verification` | kept nearly whole |
| adr.md | `ordnung-ledger` with `agent/ordnung.toml` (`ADR` / `docs/adr`) | merged; the prefix is configurable |
| (implicit: LAB.md, read-only repos, customer data) | `iac-live` | new: made explicit |
| web.md | — | not ported yet; port it when project B starts its web scaffold (board T-06) |
