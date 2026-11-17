# Agent contract - rationale

This directory explains **why** the rules in `rules/` exist. The rule files are the contract agents
must follow. These pages give the reasoning, for the humans who maintain the contract and review agent
output, and for agents only when explicitly asked.

> Not agent boot material. Nothing here is read during the session-start protocol. `AGENTS.md` sends
> agents to `rules/`, never here.

## How the contract fits together

```
agent starts
  |-- entry point: CLAUDE.md / .github/copilot-instructions.md -> AGENTS.md (boot protocol + digest)
  |-- boot: list rules/ -> read every rules/*.md, base.md first
       |-- no REPO-MAP, or STATUS is the empty template -> agent/bootstrap.md
       |-- exists -> read STATUS.md HANDOFF, scope via REPO-MAP
            |-- per document: questioning -> brief (user confirms) -> facts (research pack
            |   or lookups) -> outline -> draft -> review -> hand over
            |-- checkpoint STATUS at the moments in base.md; archive DONE items -> loop
```

## Where this persona sits
`document-writing` is the writing half of what the `tech-writing` persona tried to do alone. The
`research` persona does the deep research (longlists, screening, landscape studies) and hands over a
research pack. This persona questions the user, writes, and reviews. The two can run in separate
sessions or projects, or the research step can run as a sub-agent where the tool supports one. The
research pack is the contract between them. The `review` persona checks briefs, packs and drafts independently and returns a review
report; it is the portable form of the reviewer role.

## Rationale pages

| Page | Rules it explains |
|---|---|
| [design.md](design.md) | `rules/requirements.md`, `rules/facts.md`, `rules/writing.md`, `rules/doc_types.md`, the review in `rules/verification.md`. Covers what the `tech-writing` field test showed, why facts are checked before they are written, why the brief is a gate, and why the body has a page budget and no internal ids. **Read this first.** |
| [classification-and-distribution.md](classification-and-distribution.md) | `rules/classification.md`: the four tiers, the TLP:2022 mapping, and why a widening is recorded before it acts. Written for `tech-writing` 1.x. This persona applies the same ladder with fewer header fields, and the full checks only at release. |
| [comparisons-and-advisories.md](comparisons-and-advisories.md) | `rules/comparisons.md`, the advisory profile in `rules/doc_types.md`: fairness, and why a tick matrix is not a verdict. Written for `tech-writing` 1.x. Candidate sourcing has since moved to `rules/facts.md` and the research persona. |
| [format-and-visuals.md](format-and-visuals.md) | `rules/output_formats.md`, `rules/visuals.md`: why the agent may not pick a format, why generated output is code, and when a figure beats a sentence. |

## Reading order for a new colleague
1. `AGENTS.md` (the boot protocol and the digest).
2. `rules/base.md`, then `rules/requirements.md` and `rules/writing.md`.
3. `design.md` on this page.
4. `rules/doc_types.md` for the document types you expect to write.
5. Copy the whole directory into a fresh project, open it with any agent, and run bootstrap.
