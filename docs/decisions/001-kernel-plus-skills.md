# DR-001: A short kernel in AGENTS.md, everything else as skills

## Context
v1 put the whole contract in `rules/*.md`, read in full at the start of every session. Field data
showed two failures. After a compaction or a summary, the rules were the first thing lost, and
only the `AGENTS.md` digest survived, because harnesses reload that file. And the read cost grew
with every module. The operator's requirements (2026-11-25): survive compaction, stay
agent-agnostic, and assume the agent can use subagents and skills.

## Decision
1. `AGENTS.md` is a kernel of 80 lines or fewer: the non-negotiables, the persona's rules 9 to
   12, and a skills table with triggers. It is the only contract text a harness is guaranteed to
   reload.
2. Everything else is an Agent Skill (`SKILL.md` with frontmatter), canonical in
   `.agents/skills/`. `.claude/skills` is a symlink to it, because Claude Code does not read
   `.agents/skills` (docs/harness-matrix.md).
3. The skills the contract depends on (`ordnung-resume` first of all) are named in the kernel,
   with a file-path fallback, so they never rely on the model choosing to load them.

## Consequences
- An installed project carries no copy of the rules in prose. Changing a rule means changing a
  skill and reinstalling it.
- Enforced by: `tests/test_tools.py::test_every_persona_installs_within_cap` (the kernel stays
  within its cap) and `tests/test_tools.py::test_every_skill_listed_in_kernel_exists`.

## Status
ACCEPTED (2026-11-25, operator: "a draft"; field-tested from 2026-11-26)
