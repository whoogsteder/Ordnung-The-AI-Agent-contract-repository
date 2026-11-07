# Bootstrap protocol — repo-maintainer persona

Status: ✅ IMPLEMENTED. Trigger: `agent/REPO-MAP.md` missing, or `agent/STATUS.md` missing /
still the empty template (see base.md → Context discipline).

## Steps (one session, in order)

1. **Survey**: list the repository tree (skip `.git`, ignored dirs). One pass, no deep reads.
2. **Write `agent/REPO-MAP.md`**: sections for root, contracts/persona/*, tools/, tests/,
   docs/. Mark each entry ✅ IMPLEMENTED, 🟡 PARTIAL or 📋 PLANNED based on what you saw.
   Exclude anything .gitignore'd and generated artifacts.
3. **Write the first HANDOFF block** in `agent/STATUS.md` per the base.md schema:
   phase = current workstream, next_action = the single most valuable next step derived from
   REPO-MAP gaps (PLANNED entries, failing checks), files = what the next session must open.
4. **Run the health checks** and record results in the HANDOFF notes line:
   `python3 tools/check_sync` and
   `uv run --with pytest --no-project python -m pytest tests/ -q`.
5. Continue with the task the user actually asked for; do not "fix" PLANNED items unprompted.

## Dogfood note: the memory-freshness probe lives here, not in the personas

Persona bootstraps offer the agent to author a project-local freshness probe for STATUS.md
(see `contracts/persona/*/agent/bootstrap.md` step 5). This repository takes that offer on its own
contract: `tools/status_fresh` compares the HANDOFF `last_update:` against `agent/STATUS.md`'s
mtime (run: `python3 tools/status_fresh`).

What stays deliberately unshipped is a probe inside the persona folders. A script cannot travel
with a drop-in persona copy, so it would be unshippable enforcement — the contract ships the
*instruction*, and each project writes the probe that fits its own tooling. The textual guard
(`last_update:` plus the frequency rule in `rules/base.md`) remains the baseline; this script is
this project's opt-in upgrade to one command instead of one judgment.

## Authoring-work specifics

- When bootstrapping after a structural change (new persona, moved folder), update
  REPO-MAP and README in the same response, then run `tools/check_sync` before committing —
  it catches stale paths only via structure, so eyeball README links too.
- If check_sync reports drift you did not cause, surface it as a finding; do not silently
  rewrite another persona's slot content.
