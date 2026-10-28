# REPO-MAP — AI Agent Rulesets (repo-maintainer persona)

## Root
- `README.md` — landing page: contract concept, personas, install instructions ✅
- `AGENTS.md` / `CLAUDE.md` — this repo's own agent boot pointer (repo-maintainer contract) ✅
- `rules/base.md` — repo-maintainer contract core (marked `<!-- core -->` / `<!-- slot: -->` / `<!-- persona -->`) ✅
- `rules/verification.md` — evidence and checker rules for repo work ✅

## agent/ (this repo's boot material)
- `agent/ruleset.md` — manifest: persona=repo-maintainer, version 1.0.0, core-source declaration 🟡 (root copy not yet covered by check_sync)
- `agent/STATUS.md` — session state (HANDOFF lives here) ✅
- `agent/bootstrap.md` — PLANNED: bootstrap protocol adapted for authoring work

## contracts/persona/iac/ (persona: infrastructure-as-code) ✅
- `contracts/persona/iac/rules/` — base, verification, python, terraform_tfgrunt, ansible, web, adr ✅
- `contracts/persona/iac/agent/` — bootstrap, project_layout, STATUS template ✅
- `contracts/persona/iac/docs/agent-contract/` — rationale docs (do not read at boot) ✅
- `contracts/persona/iac/licenses/` — license picker texts ✅
- `contracts/persona/iac/rules/zoo-dcg-bug.md` — user's untracked file, leave in place until user decides

## contracts/persona/administrative/ (persona: administrative work) ✅
- `contracts/persona/administrative/rules/` — base, verification, python, documents, financial, approval, dr ✅
- Same agent/, docs/agent-contract/, licenses/ shape as iac persona ✅

## tools/ 📋 PLANNED
- `tools/check_sync` — core-section sync checker across personas (stdlib Python)

## tests/ 📋 PLANNED
- `test_check_sync.py` — pytest incl. planted-drift fixture

## docs/authoring/ 📋 PLANNED
- `core-sync.md` — seam marker convention, section-slot map, release flow
- `persona-anatomy.md` — how to add a persona (fill-the-slots guide)
