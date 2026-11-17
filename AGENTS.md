# Agent rules — MANDATORY first step, every session, no exceptions

Before you do ANYTHING else, in this exact order:
1. List the `rules/` directory.
2. Read EVERY `.md` file in `rules/` — `base.md` first, then each module. Do not skip any file in `rules/`.

The files in `rules/` are this repository's own agent contract (the repo-maintainer persona)
and the single source of truth for every agent working on this repository. `base.md` always
applies; the other `rules/*.md` files apply when that language/tool is in use.

When your work touches a contract under `contracts/persona/`, load and honor that contract's
rules for the duration of that work, in addition to these.

`docs/agent-contract/` inside each persona folder explains *why* those rules exist. It is
background for humans and for agents only on request — do NOT read it during the boot
sequence or as part of task work.

## Contract digest - the non-negotiables, kept here because this file is reloaded

If this list is all you remember of the contract (after a context summary or compaction, or deep
into a long session), stop and re-read `rules/base.md` and `agent/STATUS.md` before your next action.
The full rules in `rules/` win over this digest wherever they say more.

1. Read the HANDOFF block in `agent/STATUS.md` before acting. Checkpoint STATUS.md before a long run
   of tool work, after files and checks, and before reporting back. If you cannot say when you last
   updated it, update it now.
2. Scope reads and searches with `agent/REPO-MAP.md`, and keep it current when files are added, moved
   or removed.
3. Never edit `rules/`, `AGENTS.md`, `CLAUDE.md` or other agent pointer files unless the user asks for
   that specific change.
4. Never write "verified", "confirmed" or "current" without the command or source that shows it.
5. If a task is ambiguous or a rule blocks it, say so and ask. Never work around a rule.

Persona:
6. A commit that changes a `<!-- core -->` section changes it in every persona and the root copy, and `tools/check_sync` passes before any commit that touches contract files.
7. Contract changes bump the touched persona manifests; `CHANGELOG.md` is updated with every release.
