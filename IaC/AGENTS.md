# Agent rules — MANDATORY first step, every session, no exceptions

Before you do ANYTHING else, in this exact order:
1. List the `rules/` directory.
2. Read EVERY `.md` file in `rules/` — `base.md` first, then each module. Do not skip any file in `rules/`.

The files in `rules/` are the project's rules and the single source of truth for every
agent (Copilot, Continue, Cline, and any other). `base.md` always applies; the other
`rules/*.md` files apply when that language/tool is in use.