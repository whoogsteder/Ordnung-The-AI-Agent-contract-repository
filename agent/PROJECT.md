# PROJECT — what must stay true across tasks (≤ 80 lines; one line per entry, detail in docs/)

## Purpose
Ordnung-Zwei: a drop-in agent contract (a kernel plus skills plus a checker) for projects run by
AI coding agents. It keeps agents steered through compaction, across harnesses, and across
tactical and strategic work. Personas specialise it; this repository runs its own (DR-006).

## Standing requirements
<!-- REQ-NN: requirement — source (who, date) — status: active | met | dropped -->
- REQ-01: Survive context compaction: the steering rules are never lost — operator, 2026-11-25 — active
- REQ-02: Agent-agnostic; no lock-in to one harness (Claude Code, OpenCode, Codex, Copilot, ...) — operator, 2026-11-25 — active
- REQ-03: Assume the agent supports subagents/workers and skills; no fallback design for agents without them — operator, 2026-11-25 — active
- REQ-04: Serve tactical work (the task in hand) and strategic work (larger project scope, requirements) — operator, 2026-11-25 — active
- REQ-05: v1 personas stay available as reference, at tag contracts-v1.4.0 (DR-006) — operator, 2026-11-25 / 2026-11-27 — active
- REQ-06: Create and change skills with the skill-creator workflow (draft, evals, iterate) — operator, 2026-11-25 — active
- REQ-07: Field tests run on self-hosted models too (Qwen3.8-flash via OpenCode); keep context cost low — operator, 2026-11-26 — active

## Decisions
<!-- Open decisions only (DR-NNN in docs/decisions/, DR-004). Accepted ones: REPO-MAP index. -->
- DR-005: Batching low-effort development tasks + agent/estimates.md — PROPOSED — gates T-09

## Waiting on the user
<!-- Q-NN: the question — options — blocking what — since YYYY-MM-DD -->
- none

## Tracks
<!-- name — state — tasks — detail -->
- 2.0.0 release — rc.1 published 2026-11-27; final after field feedback — T-10 — CHANGELOG.md
- Evals — iteration 1 done for resume/checkpoint/delegate (only resume discriminates) — T-02, T-04, T-05 — skills/core/*/evals/
- Harness support — desk research done, nothing tested yet — T-03 — docs/harness-matrix.md
- Field tests — A (advisory), B (iac); feedback log — T-04, T-05, T-09 — docs/field-tests/feedback.md
- Persona ports from v1 — game-hosting, advisory, iac done; others not — T-06, T-07 — docs/lineage.md

last_reviewed: 2026-11-27
