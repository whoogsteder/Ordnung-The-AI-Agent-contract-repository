# Why retrieval and capture are gated the way they are

Status: ✅ IMPLEMENTED. Explains `rules/retrieval.md`, `rules/eval.md`, `rules/capture.md`,
`rules/provenance.md`.

## A retrieval system can be up and useless at the same time

The failure this persona is written around: a re-ranking stage returns HTTP 200, fast, with a
result list — and the scores are garbage. In a real audit of a deployed reranker, the *correct*
document scored `4.1e-12` while an irrelevant one scored `1.7e-09`. A working cross-encoder scores
a relevant document near `1.0`, so the ordering was effectively random. Nothing in a health check
would have noticed: the endpoint was healthy, the schema was valid, the latency was fine.

The cause was a model file missing the chat template a causal reranker needs before its classification
token can be read. That is invisible from the API surface.

Three rules follow directly:

- **A stage that answered is not a stage that works** (`retrieval.md`). Health checks assert output
  quality on a known case, not just a 200. This is the cheapest rule in the persona and the one
  that would have caught the above on day one.
- **Degradation is announced** (`retrieval.md`). If a system silently drops to keyword search, the
  caller keeps believing they got ranked results. Announcing it is what makes a fallback safe to
  have.
- **Reranking is optional and off by default** in practice, not just in configuration. A component
  that is usually absent should never be load-bearing.

## Why "no result" has to be a first-class answer

An agent that is rewarded for producing an answer will produce one from an empty result set. Making
"nothing found" an explicit, documented, well-typed outcome — with an error that distinguishes it
from *backend unavailable* and *not authorised* — is what lets a calling agent behave correctly
instead of improvising.

## Why the golden question set is the contract's teeth

`rules/eval.md` exists because retrieval quality is otherwise unfalsifiable. Every other kind of
change in this codebase has an obvious test; a chunking change does not, until a question that used
to retrieve the right document stops retrieving it.

The rules are deliberately strict about scope: *any* change that can affect retrieval must pass the
evaluation, including preprocessing and filter changes, because those are exactly the changes people
do not think of as retrieval changes. Adding a question per failure mode is what stops the same
regression recurring — the set is a memory of mistakes.

## Why capture is propose-then-approve

Agents are good at writing a confident summary of something they just did, and that summary is
exactly the kind of item that poisons a knowledge base: plausible, unsourced, and permanently
available to future sessions. Two mechanisms close that gap:

- **Provenance is a schema requirement** (`provenance.md`), so an item without source, evidence and
  date cannot be indexed at all. A draft with no evidence is not a weak note; it is not a note.
- **Approval is a human act** (`capture.md`). An agent writes to a proposal area; a human moves it
  into the curated store. This is not a comment on agent competence — it is the same reasoning as
  code review, applied to memory. Bad code fails loudly; a bad memory item silently shapes every
  later answer.

The anti-trigger matters as much as the triggers. The most common bad capture is restating what a
source document already says, which doubles the surface that can go stale while looking like
coverage.
