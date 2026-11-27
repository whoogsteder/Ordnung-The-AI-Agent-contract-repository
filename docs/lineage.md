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

## knowledge-base persona ([v1 1.0.0](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base) → `personas/knowledge-base/`)

The v1 persona was authored but never installed in a field project, so there is no hardened copy to
prefer over the v1 text. Its rules were always-loaded `rules/*.md`, which is the boot load this
layout exists to remove, so each module is recast as a triggered skill rather than copied.

| v1 | Zwei location | |
|---|---|---|
| [base.md](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base/rules/base.md) Role, State & change history, Documentation | `persona.md` role + kernel rules 9–11 | condensed to what survives a compaction |
| [provenance.md](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base/rules/provenance.md) | `kb-provenance` | kept: source/evidence/date as schema, citation on every result, staleness and superseding |
| [corpus.md](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base/rules/corpus.md), [scope.md](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base/rules/scope.md) | `kb-corpus`, `kb-scope` | split: what is indexed and rebuilt vs what a caller may read |
| [retrieval.md](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base/rules/retrieval.md) | `kb-retrieval` | kept, with the re-ranker audit told in the skill so the failure mode stays concrete |
| [eval.md](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base/rules/eval.md) | `kb-eval` | kept, plus the evidence tiers v1 put in verification.md |
| [capture.md](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base/rules/capture.md) | `kb-capture` | kept, including the anti-trigger for restating what the sources already say |
| [interfaces.md](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base/rules/interfaces.md) | `kb-interfaces` | kept: the tool and flag surface is public API |
| [resource_discipline.md](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base/rules/resource_discipline.md) | `kb-resource-discipline` | kept: batching, content-hash caching, bounded retries |
| [python.md](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base/rules/python.md) | `kb-python` | generic Python rules, plus determinism for anything that reaches an index; device/TLS specifics stay with `iac-python` |
| [verification.md](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base/rules/verification.md) | folded into `kb-eval` | no `kb-verification`: the KB-specific evidence rules are eval rules |
| [adr.md](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0/contracts/persona/knowledge-base/rules/adr.md) | `ordnung-ledger` with `agent/ordnung.toml` (`ADR` / `docs/adr`) | same scheme as iac |

Eval cases were not written with the port; they are board T-13, the same order advisory and iac
shipped in before T-04 and T-05.
