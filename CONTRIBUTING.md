# Contributing to Ordnung!

So you want to bring order to a new kind of agent? Exactly who we are looking for. 🧹

A **persona** is one contract folder under `contracts/persona/<name>/`: the shared Ordnung core
plus your specialist rules for a domain (infrastructure, administration, data science,
homelab — whatever you have tamed). The framework handles boot protocol, memory files and
continuity; you write the part only you know.

## Five-minute quickstart

```sh
git clone https://github.com/pv-whoogsteder/Ordnung-The-AI-Agent-Contract-Repository.git
cd Ordnung-The-AI-Agent-Contract-Repository
python3 tools/new_persona <your-persona>     # scaffolds contracts/persona/<your-persona>/
# 1. edit rules/base.md: fill the slot sections (slot: role, slot: state-history),
#    leave <!-- core --> sections untouched
# 2. keep/adapt/delete the optional modules; add your own with <!-- persona --> markers
# 3. write your rationale in docs/agent-contract/
python3 tools/check_sync                     # must say OK before you commit
uv run --with pytest --no-project python -m pytest tests/ -q
```

Then open a pull request — small and focused beats big and sweeping.

## What a contribution should be

- **Generic**: rules describe behavior, not your project. No client names, paths, record
  numbers — those live in each user project's `agent/REPO-MAP.md` / `agent/STATUS.md`.
- **Honest seams**: every top-level heading carries `<!-- core -->`, `<!-- slot: name -->` or
  `<!-- persona -->`. Only touch `core` sections repo-wide (all personas + root copy, one
  commit) when the change truly is shared behavior — `tools/check_sync` will hold you to it.
  See [docs/authoring/core-sync.md](docs/authoring/core-sync.md).
- **Short**: `base.md` says what every session needs; modules are imperative checklists for
  their domain; the *why* goes in `docs/agent-contract/`, never in boot material.
- **Tested**: `check_sync` OK and pytest green in your branch. If you changed tooling, add a
  test.

## The guides

- [docs/authoring/persona-anatomy.md](docs/authoring/persona-anatomy.md) — folder shape, step
  by step, rules of thumb.
- [docs/authoring/core-sync.md](docs/authoring/core-sync.md) — the seam-marker convention and
  why copies-plus-checker beat shared files.

## Ways to help beyond a new persona

- Fix wording in a `core` section (yes, that means all personas at once — the tool tells you).
- Write or sharpen rationale pages under a persona's `docs/agent-contract/`.
- Report where an agent followed the contract and still made a mess — that is a rule bug, and
  the most valuable kind.

This repository runs its own contract (the root folder is the `repo-maintainer` persona), so
maintainers review contributions the same way agents work: boot via `AGENTS.md`, state in
`agent/STATUS.md`. Your PR will get an honest, rule-bound read. Ordnung!
