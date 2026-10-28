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
