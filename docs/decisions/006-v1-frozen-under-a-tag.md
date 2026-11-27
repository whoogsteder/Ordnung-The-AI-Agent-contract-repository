# DR-006: v1 frozen under a tag, Zwei is main from 2.0.0

## Context
The operator wants to keep v1 as a reference and make Zwei the leading content (2026-11-27). v1
ships 16 `AGENTS.md`/`CLAUDE.md` files in its persona folders. Claude Code, Codex, OpenCode and
Cursor load nested pointer files of that kind, so a v1 copy inside the tree would quietly feed
old rules to an agent working on Zwei.

## Decision
1. v1 is released one last time as `contracts-v1.4.0`, and is browsed at that tag. No part of it
   stays in the tree. The unmerged tech-writing 2.0.0 rework is kept as the tag
   `archive/tech-writing-v2`.
2. `docs/lineage.md` links into the v1 tag, never to a moving branch.
3. Zwei is released as `contracts-v2.0.0-rc.N` while the field tests run, and as 2.0.0 once their
   feedback is in. It keeps the `contracts-v` tag scheme. Personas carry their own versions.
4. This repository runs its own contract (the `contract-authoring` persona), as v1 did:
   eat your own dogfood.

## Consequences
- Enforced by: `tests/test_tools.py::test_lineage_links_point_at_tags` and
  `tests/test_tools.py::test_root_agents_md_is_the_rendered_kernel`.

## Status
ACCEPTED (2026-11-27, operator)
