# Ordnung-Zwei — design

Status: 🟡 DRAFT (2026-11-25). Nothing here has been field-tested yet; see "Test plan".

## The four requirements

| # | Requirement | Mechanism in Zwei |
|---|---|---|
| R1 | Survive context compaction; steering rules never get lost | A tiny **kernel** in `AGENTS.md` (the one file harnesses re-inject); everything else is a skill re-loaded on demand; the HANDOFF names the skills and constraints the current task needs, so `ordnung-resume` restores *exactly* that after a summary |
| R2 | Agent-agnostic, no lock-in | Plain files only: `AGENTS.md`, Agent Skills (`SKILL.md` + frontmatter), Markdown memory, a stdlib-Python checker, a git hook. Harness-specific hooks are optional adapters, never load-bearing |
| R3 | Assume subagents and skills exist | Rules ship as skills (progressive disclosure); long or wide work is delegated through a fixed brief template that carries the kernel into the subagent |
| R4 | Tactical *and* strategic use | Two memory layers with hard size limits: `agent/STATUS.md` = one task, `agent/PROJECT.md` = the project's standing requirements, decisions and operator-pending questions. A checkpoint **promotes** anything that outlives the task from STATUS to PROJECT |

## What went wrong in v1 (measured, not guessed)

Field data from a v1 game-hosting project (field project C, a dedicated game-server stack, 2026-11-25):

- Boot load ≈ 900 lines (rules 454 + REPO-MAP 207 + STATUS 220) before the first task read.
  The contract itself fills the context that compaction then summarizes away.
- STATUS.md was 220 lines against a 40-line size guard; `next_action` was multi-paragraph
  against a "single sentence" schema. Self-policed limits were not kept under pressure.
- Strategic facts (operator decisions, cross-task prerequisites) lived in the tactical HANDOFF,
  because there was no other short, always-read place for them. The strategic sources that did
  exist (a 122 KB roadmap) cannot be loaded at all.
- "Re-read base.md at pressure points" depends on the agent knowing it is at one; after a
  summary it does not.

What worked and is kept: the file-based memory idea, the HANDOFF schema, the contract digest
in `AGENTS.md` (Ordnung 2.0), decision records, evidence-backed claims, `status_fresh`,
"checkpoint at moments, not on a count" (Ordnung 2.0). See `lineage.md`.

## Layer model

```
always in context        AGENTS.md (kernel, ≤ 60 lines)  ── re-injected by the harness
read at every resume     agent/PROJECT.md (≤ 80)  +  agent/STATUS.md (≤ 40)
read when scoping        agent/REPO-MAP.md (≤ 120, area maps below it)
loaded on trigger        .agents/skills/*/SKILL.md   (core ordnung-* + persona skills)
loaded on demand         skill references/, docs/decisions/, docs/design/
never read at task time  agent/STATUS.archive.md, docs/archive/, docs/agent-contract/
```

Size limits are enforced by `tools/ordnung_check`, run by the pre-commit hook and by
`ordnung-resume` — not by the agent's memory. A project adds its own pre-commit commands under
`[hook] run` in `agent/ordnung.toml`; `--install-hook` writes them into the hook, and the check
reports an installed hook that lags that list.

## Compaction strategy

1. **Re-injection** — the kernel is in `AGENTS.md` because that is the file harnesses
   reload. It says one thing above all: *after any summary, run `ordnung-resume`.*
2. **Re-hydration** — `ordnung-resume` reads PROJECT + STATUS, runs the check, re-loads the
   skills listed in the HANDOFF `skills:` field and echoes the HANDOFF `constraints:`.
3. **Avoidance** — the coordinator stays light: wide reading, debugging and long edit runs go
   to subagents, whose context burns instead. The coordinator holds the plan and integrates
   ≤ 15-line reports.
4. **Checkpoint before risk** — STATUS is written *before* a long run, so a compaction
   mid-run loses nothing that matters.

## Tactical vs strategic

- **Tactical** (`STATUS.md`): one task — plan, next action, task-scoped constraints, last
  evidence. Disposable when the task ends (archived).
- **Strategic** (`PROJECT.md`): what must stay true across tasks — standing requirements
  (`REQ-NN`), decision index (`DR-NNN`), questions waiting on the operator (`Q-NN`), active
  tracks. Each entry is one line plus a link; detail lives in `docs/`.
- **Promotion rule** (in `ordnung-checkpoint`): before writing STATUS, ask of every note
  "would this matter after this task is closed?" Yes → it goes to PROJECT (or a DR), not
  STATUS.

## Skill discovery (to verify per harness)

Canonical location in an installed project: `.agents/skills/<name>/SKILL.md`. The installer
also links `.claude/skills → .agents/skills`. Which harnesses discover `.agents/skills`
natively is a test item, not an assumption — record results in `docs/harness-matrix.md`.
Fallback that always works: the kernel lists every skill with its trigger and path, so an agent
whose harness does not auto-load skills reads the `SKILL.md` itself.

## Test plan

1. `pytest tests/` — checker and installer behave as specified.
2. Skill evals (skill-creator format, `evals/` in each core skill) — with-skill vs baseline.
3. Field test: install into a throwaway copy of a v1 project, migrate its STATUS/REPO-MAP,
   run a multi-session task across at least one forced compaction per harness
   (Claude Code, OpenCode, one more), record in `docs/harness-matrix.md`:
   did the kernel survive, did resume restore skills + constraints, did limits hold.

## Open questions

- Q1: Should the persona kernel lines be rendered into `AGENTS.md` at install (current draft)
  or kept in a separate always-read file? Rendering keeps one re-injected file.
- Q2: Keep REPO-MAP at all, or replace with area maps only? Draft keeps a ≤ 120-line top map.
- Q3: Seam markers / `check_sync` from v1 — needed once there are several Zwei personas sharing
  core skills? Draft: core skills are shared *files*, not copies, so no drift check is needed
  until a persona forks one.
