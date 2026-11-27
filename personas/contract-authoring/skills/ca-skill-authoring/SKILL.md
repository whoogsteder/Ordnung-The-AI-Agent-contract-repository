---
name: ca-skill-authoring
description: Authoring rules for the Ordnung-Zwei contract itself — SKILL.md anatomy and frontmatter, descriptions that route well (triggers named, slightly pushy, no unquoted colon-space), the kernel's line budget, persona.md anatomy (frontmatter, Kernel rules 9-12, Skills rows, Bootstrap questions), keeping skills generic and agent-agnostic, and keeping the checker, installer and templates backward compatible for installed projects. Use this whenever you create, edit, rename or split a skill or persona, touch kernel/AGENTS.md.tmpl, templates/, tools/ordnung_check or tools/install, or port a piece of the v1 contract.
---

# Authoring the contract

Every line here ends up in someone else's context window, often after a compaction, often on a
small self-hosted model. So write less, route precisely, and prove behaviour.

## Creating or changing a skill
- Use the `skill-creator` skill where the harness has it, because it carries the draft, test and
  iterate loop (REQ in PROJECT.md). Without it, follow `ca-evals` by hand.
- **The format:** `skills/core/<name>/SKILL.md` or `personas/<p>/skills/<name>/SKILL.md`. The
  YAML frontmatter holds `name`, which equals the folder name, and `description`.
  - Validate the frontmatter. An unquoted `: ` inside the description breaks the YAML: use an
    em dash or quote the value.
  - Keep the body under about 150 lines. Push detail into `references/` files that the body
    names, saying when to read each one.
- **The description is the only thing a model sees before it decides to load the skill.** It
  says what the skill does and lists its triggers: the files, situations and user phrases.
  Write it slightly pushy, because models under-trigger skills.
- **Explain why, not only must.** A model that knows the failure a rule prevents applies it
  better than one obeying a capitalised MUST.
- **Generic only.** No project names, paths or numbers in skills. Project facts belong in that
  project's PROJECT.md or REPO-MAP.
- **Agent-agnostic.** Name actions, not tools ("delegate to a worker", not one harness's tool
  name). Check every claim about a harness against `docs/harness-matrix.md`.

## The kernel (`kernel/AGENTS.md.tmpl`)
- The cap is 80 lines, rendered with the largest persona. Each line costs context in every
  session of every installed project.
- Only rules that must hold when the kernel is all the agent remembers belong here. Everything
  else is a skill.
- Changing the kernel means re-rendering this repo's own `AGENTS.md` (`tools/install . --persona
  contract-authoring --dev --force`). The root-kernel test fails until you do.

## Personas (`personas/<p>/persona.md`)
- **The frontmatter** holds `persona`, `version`, `title`, `role`, and optionally
  `decisions: <PREFIX> <dir>`.
- **`## Kernel rules`** holds rules 9 to 12: the few things the persona must never get wrong.
- **`## Skills`** has one table row per persona skill: `` | `name` | trigger | ``.
- **`## Bootstrap questions`** holds the questions `ordnung-bootstrap` asks.
- **When porting from v1,** take the field-hardened wording, then condense it. Record the move
  in `docs/lineage.md`, with a link to the v1 tag.

## Checker, installer, templates: installed projects depend on them
- Every check the checker adds must pass on a well-formed existing project. A new strictness is
  optional, or comes with a migration step in CHANGELOG.md (kernel rule 12).
- Every new check gets a passing test and a failing test in `tests/test_tools.py`. Run it against
  a real field project's board or memory files, using a copy in scratch, before you trust it.
- The installer never overwrites a project's `PROJECT.md`, `TASKS.md`, `STATUS.md` or
  `REPO-MAP.md`, or an existing `agent/ordnung.toml`.
- Stdlib-only Python, so the tools run under any agent and in any CI.
