# Agent contract — rationale

This directory explains **why** the rules in `rules/` exist. The rule files are the contract
agents must follow; these pages are the reasoning behind it, written for the humans who maintain
this contract and review agent output — and for agents only when explicitly asked.

> Not agent boot material. Nothing here is read during the session-start protocol; `AGENTS.md`
> sends agents to `rules/`, never here.

## What this persona is for

A knowledge-base project fails in a way most projects do not: it can be **fully operational and
wrong**. A search endpoint that returns plausible passages with meaningless scores looks healthy in
a log, passes an HTTP-200 health check, and quietly degrades every answer built on it. There is no
stack trace for a bad ranking.

So the persona is organised around three refusals, in order of how expensive they are to learn late:

1. **Refuse to trust an index.** The repository is the source of truth; the index is a cache that
   must be rebuildable. This is what makes every other mistake recoverable.
2. **Refuse to trust a retrieval claim.** Quality is a committed evaluation with a threshold, not
   an impression from a few queries.
3. **Refuse to trust an unsourced item.** Provenance is a schema requirement, so "the model said
   so" cannot enter the corpus.

Compared with the `iac` persona this one borrows the verification vocabulary from — *claims become
checks* — the difference is what a check looks like. Infrastructure has plan/dry-run/idempotency
tiers; a knowledge base has a golden question set and a score distribution. Both refuse the same
thing: an unbacked "it works".

## Rationale pages

| Page | Rules it explains |
|---|---|
| [retrieval-and-capture.md](retrieval-and-capture.md) | `rules/retrieval.md`, `rules/eval.md`, `rules/capture.md`, `rules/provenance.md` — why silent fallback is treated as a defect, why "no result" must be a first-class answer, and why capture is propose-then-approve rather than agent-committed |
| [corpus-and-interfaces.md](corpus-and-interfaces.md) | `rules/corpus.md`, `rules/scope.md`, `rules/interfaces.md`, `rules/resource_discipline.md` — why exclusion lives in the indexer, why the index refuses mismatched vectors, and why read-only ships first |

## Reading order for a new colleague

1. `AGENTS.md` (30 seconds — the boot protocol and the three persona non-negotiables).
2. `rules/base.md` — the always-on contract.
3. This page, then the two rationale pages.
4. The persona modules: they are short, and each one exists because of a specific failure.
5. Copy the whole directory into a fresh project, open it with any agent, and run bootstrap.
