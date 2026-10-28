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

## Authoring-work specifics

- When bootstrapping after a structural change (new persona, moved folder), update
  REPO-MAP and README in the same response, then run `tools/check_sync` before committing —
  it catches stale paths only via structure, so eyeball README links too.
- If check_sync reports drift you did not cause, surface it as a finding; do not silently
  rewrite another persona's slot content.
