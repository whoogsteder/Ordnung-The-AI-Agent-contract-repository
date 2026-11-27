# Why the corpus, scope and interfaces are rigid

Status: ✅ IMPLEMENTED. Explains `rules/corpus.md`, `rules/scope.md`, `rules/interfaces.md`,
`rules/resource_discipline.md`.

## Exclusion belongs in the indexer, not in judgment

A source project may forbid reading archived or superseded material during task work — the point
being that stale decisions should not quietly steer current ones. A knowledge base is a very
efficient way to break that rule by accident: index everything, and the archived design comes back
into a caller's context wearing the costume of a search result.

So exclusion is enforced **by construction** (`corpus.md`): the indexer never reads those paths, and
a test proves an excluded document cannot be retrieved. The alternative — asking the query layer, or
the agent, to filter it out — depends on every future caller remembering, which is not a guarantee.

The same reasoning puts inclusion in configuration rather than in agent judgment. What is in the
corpus is a decision with a diff, not a runtime opinion.

## Why the index refuses mismatched vectors

Two embedding models that happen to emit the same dimension produce vectors that are shape-compatible
and semantically unrelated. Cosine similarity between them still returns a number, and that number
looks like a score. Nothing errors. Retrieval just gets worse, invisibly.

Hence: the recipe that built an index (embedding model and version, chunking version) is recorded
with the index, and writing vectors from a different recipe into the same index is **refused rather
than warned** (`corpus.md`). A warning is a message nobody reads at 2 a.m.; a refusal is a bug report
with the cause in the title.

This is also why the index stays disposable. If a rebuild from committed files is always available,
changing the embedding model is a routine, reversible operation — build the new index alongside,
measure it, switch, drop the old. If it is not, every model change becomes a risky migration, and
people stop making the change they should make.

## Why read-only ships before write

The tools in this persona are consumed by agents, and agents make confident mistakes. A mistaken
read costs a retry; a mistaken write contaminates the corpus that every later session trusts. So
`interfaces.md` puts read-only surfaces first, keeps changes additive, and treats tool names and
flags as a public API — because a calling agent will not read a changelog before it breaks.

Distinguishing error kinds is part of the same idea. "Not found", "backend unavailable" and "not
authorised" require different behaviour from a caller; a single generic failure string forces it to
guess, and guessing is how an agent ends up retrying an authorisation failure forever.

## Why resource discipline is a rule and not a suggestion

Embedding and re-ranking backends in a personal system are usually shared, CPU-bound, and slow. The
failure mode is a retry storm: a client hammers an already saturated service, and a rebuild that
would have taken ten minutes takes an hour and degrades everyone else using the host. Batching,
content-hash caching, bounded retries and checkpointed rebuilds are cheap to write down and expensive
to retrofit into a rebuild that is already running.
