# Agent rules — MANDATORY first step, every session, no exceptions

Before you do ANYTHING else, in this exact order:
1. List the `rules/` directory.
2. Read EVERY `.md` file in `rules/` — `base.md` first, then each module. Do not skip any file in `rules/`.

The files in `rules/` are the project's rules and the single source of truth for every
agent (Copilot, Continue, Cline, and any other). `base.md` always applies; the other
`rules/*.md` files apply when that language/tool is in use.

`docs/agent-contract/` explains *why* these rules exist. It is background for humans and
for agents only on request — do NOT read it during the boot sequence or as part of task work.

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
6. The operator is inexperienced: the quickstart works as written, and defaults are safe.
7. A bundled web frontend fails closed: authentication and TLS are never optional.
