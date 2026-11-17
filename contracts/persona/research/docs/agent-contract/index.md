# Agent contract - rationale

This directory explains **why** the rules in `rules/` exist, for the humans who maintain the contract
and review agent output, and for agents only when explicitly asked.

> Not agent boot material. Nothing here is read during the session-start protocol.

## How the contract fits together

```
agent starts
  |-- entry point: CLAUDE.md / .github/copilot-instructions.md -> AGENTS.md (boot protocol + digest)
  |-- boot: list rules/ -> read every rules/*.md, base.md first
       |-- no REPO-MAP, or STATUS is the empty template -> agent/bootstrap.md
       |-- exists -> read STATUS.md HANDOFF, scope via REPO-MAP
            |-- per topic: question (user confirms) -> search plan -> research -> screen and
            |   compare -> review -> research pack (+ brief) -> hand over
            |-- checkpoint STATUS at the moments in base.md; archive DONE items -> loop
```

## Where this persona sits
`research` hands its pack to `document-writing`. The `review` persona checks the pack before
hand-over, against the question record and the sources.

## Rationale pages

| Page | Rules it explains |
|---|---|
| [design.md](design.md) | All persona modules. Covers why research is a persona of its own, why memory may decide where to look but never what is true, why the pack has a fixed shape, and why the missing-candidate check exists. |

## Reading order for a new colleague
1. `AGENTS.md` (the boot protocol and the digest).
2. `rules/base.md`, then `rules/question.md`, `rules/method.md` and `rules/research_pack.md`.
3. `design.md` on this page.
4. Copy the whole directory into a fresh project, open it with any agent, and run bootstrap.
