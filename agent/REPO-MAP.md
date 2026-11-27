# REPO-MAP — where things live (≤ 120 lines; split detail into agent/maps/<area>.md)

## Directory guide
| Path | What it holds |
|---|---|
| `AGENTS.md` | This repo's own kernel, rendered from `kernel/AGENTS.md.tmpl` + `personas/contract-authoring` (`tools/install . --persona contract-authoring --dev --force`); never hand-edited |
| `CLAUDE.md`, `.github/copilot-instructions.md` | Pointers to `AGENTS.md` |
| `.agents/skills/` | Symlinks (dev install) to `skills/core/*` and `personas/contract-authoring/skills/*`; `.claude/skills` links here |
| `kernel/` | `AGENTS.md.tmpl` (the kernel every project gets) and `licenses/` (offered at bootstrap) |
| `skills/core/<name>/` | Core skills shipped to every project: resume, checkpoint, board, ledger, delegate, bootstrap; `evals/<case>/` per skill |
| `personas/<p>/` | `persona.md` (frontmatter, kernel rules 9-12, skills rows, bootstrap questions) + `skills/`: game-hosting (`gh-*`), advisory (`adv-*`), iac (`iac-*`), contract-authoring (`ca-*`, this repo) |
| `templates/agent/` | PROJECT, TASKS, STATUS, REPO-MAP templates copied into projects at bootstrap |
| `tools/` | `ordnung_check` (the contract gate, stdlib) and `install` (puts a contract into a project; `--dev` for this repo) |
| `tests/test_tools.py` | Tests for the checker, the installer and repo integrity (`uv run --with pytest --no-project python -m pytest tests/ -q`) |
| `agent/` | This repo's memory: PROJECT, TASKS, STATUS, REPO-MAP; `ordnung.toml`; symlinks `ordnung_check`, `templates`, `persona.md` |
| `docs/decisions/` | Decision records DR-NNN (`ordnung-ledger`) |
| `*-workspace/` | Eval run outputs (git-ignored); never read them during other work |

## Documentation index
<!-- path — one line — ✅ IMPLEMENTED | 🟡 PARTIAL | 📋 PLANNED | 🗄️ ARCHIVED -->
| Document | Status | Read when |
|---|---|---|
| `README.md` | ✅ | Landing page: what Zwei is, install, personas |
| `CHANGELOG.md` | ✅ | Releasing; what changed since v1 (v1 history below the 2.0 entries) |
| `docs/design.md` | 🟡 PARTIAL — the design as drafted 2026-11-25; DR-001..006 supersede where they differ | Questions about why the contract is shaped this way |
| `docs/harness-matrix.md` | 🟡 PARTIAL — desk research, Tested column empty | Any claim about how a harness loads skills (kernel rule 10) |
| `docs/lineage.md` | ✅ | Porting from v1, or looking up what v1 did; links into tag contracts-v1.4.0 |
| `docs/field-tests/feedback.md` | ✅ | Operator reports from field projects and their outcomes |
| `docs/decisions/001-kernel-plus-skills.md` | ✅ ACCEPTED | Kernel size, what goes in a skill, skill location |
| `docs/decisions/002-three-memory-layers.md` | ✅ ACCEPTED | STATUS/PROJECT/TASKS roles, caps, the checker |
| `docs/decisions/003-task-board-is-core.md` | ✅ ACCEPTED | The board, NOW cap |
| `docs/decisions/004-project-lists-open-decisions-only.md` | ✅ ACCEPTED | What PROJECT.md lists; decision scheme per project |
| `docs/decisions/005-batching-low-effort-development-tasks.md` | 📋 PROPOSED | Batching tasks into one PR; agent/estimates.md |
| `docs/decisions/006-v1-frozen-under-a-tag.md` | ✅ ACCEPTED | v1 reference, versioning, dogfooding |

## Area maps
<!-- agent/maps/<area>.md — when to read it -->
- none yet
