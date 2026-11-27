# Ordnung-Zwei

Status: 🟡 release candidate `contracts-v2.0.0-rc.1`, in field test. The successor to Ordnung v1.

> **Looking for v1?** It is frozen at tag
> [`contracts-v1.4.0`](https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/tree/contracts-v1.4.0)
> (the `contracts/persona/*` folders, `rules/`, `tools/check_sync`). Where each v1 piece went:
> [docs/lineage.md](docs/lineage.md).

Same idea as v1: **durable state lives in files, not in conversation history.** What changes is
how much of the contract sits in context at any moment, and what happens after a compaction.

- A **kernel** of 50–60 lines in `AGENTS.md`: the only text guaranteed to survive a summary,
  because harnesses re-inject it. It tells the agent to run `ordnung-resume` after any summary.
- Everything else is an **Agent Skill**, loaded when the work needs it.
- Three memory files: `agent/PROJECT.md` (strategic: requirements, open decisions, questions for
  the user, tracks), `agent/TASKS.md` (the task board) and `agent/STATUS.md` (tactical: the one
  task in hand). Hard size limits and board rules, enforced by a script and a pre-commit hook.
- Long or wide work is **delegated** with a brief that carries the kernel into the subagent.

Why, and what v1 taught us: [docs/design.md](docs/design.md) and the decision records in
[docs/decisions/](docs/decisions/). How each agent finds skills: [docs/harness-matrix.md](docs/harness-matrix.md).
Field-test reports: [docs/field-tests/feedback.md](docs/field-tests/feedback.md).
Where every v1 piece went: [docs/lineage.md](docs/lineage.md).

## Layout

```
kernel/AGENTS.md.tmpl          kernel template (persona lines are rendered in)
kernel/licenses/               license picker texts for bootstrap
skills/core/ordnung-*/         shared skills: resume, checkpoint, board, ledger, delegate, bootstrap
personas/<name>/persona.md     role, kernel lines, skill table, bootstrap questions
personas/<name>/skills/        persona skills (gh-*, adv-*, iac-*, ca-* for this repo)
templates/agent/               PROJECT.md, TASKS.md, STATUS.md, REPO-MAP.md
tools/install                  install a persona into a project
tools/ordnung_check            size / schema / freshness / ID checks (stdlib Python)
tests/                         tests for the tools
skills/core/*/evals/           skill-creator eval cases
```

## Install into a project

```bash
tools/install /path/to/project --persona iac      # or game-hosting, advisory
```

It writes `AGENTS.md` (or `AGENTS.md.ordnung-new` if one exists), pointer files, skills under
`.agents/skills/` with a `.claude/skills` symlink, and `agent/ordnung_check`. It never touches
existing memory files. The first agent session then runs `ordnung-bootstrap`, which also
covers migrating from v1.

## Checks

```bash
uv run --with pytest --no-project python -m pytest tests/ -q
```

## Personas

| Persona | Status | Ported from |
|---|---|---|
| game-hosting | 0.1.0-draft | Ordnung v1 game-hosting 2.0.0 |
| advisory | 0.1.0-draft | Ordnung v1 document-writing 1.2.0 + research |
| iac | 0.1.0-draft | Ordnung v1 iac 1.5.0 + field project B's rule set and task board |
| contract-authoring | 0.1.0-draft | v1's repo-maintainer contract; runs this repository |

## Eat your own dogfood

This repository runs its own contract, as v1 did: the `contract-authoring` persona, installed with
`tools/install . --persona contract-authoring --dev --force`. In dev mode the skills, checker and
templates are symlinks into the source tree, so the contract the repo works under is always the one
it ships. Its memory lives in `agent/` like any project's; `python3 agent/ordnung_check` runs as the
pre-commit hook.
