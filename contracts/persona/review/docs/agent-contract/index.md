# Agent contract - rationale

This directory explains **why** the rules in `rules/` exist, for the humans who maintain the contract
and review agent output, and for agents only when explicitly asked.

> Not agent boot material. Nothing here is read during the session-start protocol.

## How the contract fits together

```
review request
  |-- as a separate session/project: AGENTS.md -> read rules/ -> bootstrap -> review
  |-- as a sub-agent: the calling agent passes rules/ + inputs -> review -> report returned
       |-- inputs: artefact + yardstick (brief or question) + sources + stated reader
       |-- checklists A-F as applicable -> findings (blocking / should fix / note)
       |-- report: verdict, scope, must-have table, reader summary, findings, not checked
```

## Where this persona sits
`research` produces packs, `document-writing` produces briefs and documents, and `review` checks both.
It is the portable form of the reviewer role. Agents with sub-agents can run it inside the author's
session. Agents without sub-agents run it as a second session. Either way the report has the same
shape.

## Rationale pages

| Page | Rules it explains |
|---|---|
| [design.md](design.md) | All modules. Covers why review is a persona, why independence is defined by what the reviewer may *not* read, why the reviewer builds its own must-have table, and why memory may not judge facts in either direction. |

## Reading order for a new colleague
1. `AGENTS.md` (the boot protocol and the digest).
2. `rules/base.md`, then `rules/review_setup.md`, `rules/checklists.md` and `rules/findings.md`.
3. `design.md` on this page.
