# REPO-MAP — Ordnung! (repo-maintainer persona)

## Root
- `README.md` — landing page: logo banner (`img/ordnung_logo.png`, 800×192), Ordnung! intro, personas, contribution invite, checks ✅
- `CHANGELOG.md` — release history in Keep a Changelog + SemVer form: one entry per `contracts-vX.Y.Z` release with `## [Unreleased]` on top; the release act is an entry here plus an annotated tag on `main` ✅
- `img/` — project assets (logo) ✅
- `CONTRIBUTING.md` — contributor guide: quickstart with tools/new_persona, contribution rules ✅
- `AGENTS.md` / `CLAUDE.md` — this repo's own agent boot pointer (repo-maintainer contract) ✅
- `rules/base.md` — repo-maintainer contract core (marked `<!-- core -->` / `<!-- slot: -->` / `<!-- persona -->`) ✅
- `rules/verification.md` — evidence and checker rules for repo work ✅

## agent/ (this repo's boot material)
- `agent/ruleset.md` — manifest: persona=repo-maintainer, version 1.1.0; core drift against personas checked by tools/check_sync ✅
- `agent/STATUS.md` — session state (HANDOFF lives here) ✅
- `agent/STATUS.archive.md` — append-only history of completed/canceled tasks; do not read unless the user asks ✅
- `agent/bootstrap.md` — new-project bootstrapping protocol adapted for authoring work ✅

## contracts/persona/iac/ (persona: infrastructure-as-code) ✅
- `contracts/persona/iac/rules/` — base, verification, python, terraform_tfgrunt, ansible, web, adr ✅
- `contracts/persona/iac/agent/` — bootstrap, project_layout, STATUS template ✅
- `contracts/persona/iac/docs/agent-contract/` — rationale docs (do not read at boot) ✅
- `contracts/persona/iac/licenses/` — license picker texts ✅

## contracts/persona/administrative/ (persona: administrative work) ✅
- `contracts/persona/administrative/rules/` — base, verification, python, documents, financial, approval, dr ✅
- Same agent/, docs/agent-contract/, licenses/ shape as iac persona ✅

## contracts/persona/game-hosting/ (persona: dedicated game server hosting) ✅
- `contracts/persona/game-hosting/rules/` — base, verification, usability, docker_compose, steamcmd, web_frontend ✅
- Same agent/, docs/agent-contract/, licenses/ shape as iac persona; ADRs kept (image variant/frontend choices warrant records) ✅
- `contracts/persona/game-hosting/docs/agent-contract/` — base-contract, frontend-security, verification-and-upstream ✅

## contracts/persona/tech-writing/ (persona: professional document authoring) ✅
- `contracts/persona/tech-writing/rules/` — base, verification, classification, documents, open_questions, output_formats, comparisons, advisories, visuals, dr ✅
- Same agent/ shape as iac persona (bootstrap, project_layout, STATUS template, ruleset manifest v1.1.0); dr.md carries the shared `slot: decision-records` heading like administrative ✅
- `contracts/persona/tech-writing/licenses/` — kept for the code a project ships (generator/export scripts); documents carry a classification tier and distribution statement instead of a license (v1.1.0, 2026-11-09) ✅
- `contracts/persona/tech-writing/docs/agent-contract/` — base-contract, document-set-and-memory, comparisons-and-advisories, format-and-visuals, open-items-and-ideas, classification-and-distribution ✅

## tools/ ✅
- `tools/check_sync` — core/slot/persona seam checker: structure, cross-persona core drift, root dogfood copy, manifest presence + SemVer (stdlib Python)
- `tools/new_persona` — scaffold a contributor persona from the iac template: slots reset to TODO, fresh manifest + rationale stub (smoke-tested 2026-10-28 and 2026-11-09, used to scaffold tech-writing; not covered by pytest)
- `tools/status_fresh` — memory-freshness probe for this repo's own contract: compares the HANDOFF `last_update:` in `agent/STATUS.md` against that file's mtime, exit 0 current / non-zero + warning when stale or field missing (stdlib Python; smoke-tested 2026-11-07)

## tests/ ✅
- `tests/test_check_sync.py` — pytest incl. planted-drift fixtures and a real-repo pass test (`uv run --with pytest --no-project python -m pytest tests/ -q`)

## docs/authoring/ ✅
- `core-sync.md` — seam marker convention, base.md section-slot map, one-commit rule, release/version policy
- `persona-anatomy.md` — folder shape and steps to add a persona
