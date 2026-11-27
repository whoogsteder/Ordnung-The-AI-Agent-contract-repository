---
name: kb-resource-discipline
description: Rules for calling shared embedding, re-ranking and other model backends — batching instead of one call per document, caching by content hash so unchanged content is never embedded twice, bounded retries and fail-fast instead of a retry storm, checkpointed rebuilds that resume where they stopped, respecting the declared per-query latency and cost budget, and measuring wall-clock and volume before and after an optimisation. Use this whenever you call an embedding or re-ranking backend, write or run an index rebuild or backfill, when a job is slow or a service looks saturated, when adding a client for a model service, or when a query path makes more than one backend call per query.
---

# Resource discipline

Assume the backend is shared, slow and CPU-bound unless proven otherwise. The failure mode is a retry
storm: a client hammers an already saturated service, a rebuild that would have taken ten minutes
takes an hour, and everyone else on the host pays for it.

## Call it politely
- **Batch.** Never make one call per document when one call can take many.
- **Cache by content hash.** Unchanged content is never embedded twice. The same hash that makes a
  build idempotent (`kb-corpus`) is the cache key.
- **Retries are bounded**, with backoff, and reserved for errors that can plausibly succeed on a
  second attempt. A down or saturated backend gets a fail-fast error with a clear message, not a
  storm. A retry storm turns one outage into a longer one.
- Respect the declared budget: the per-query latency ceiling and cost limit live in configuration.
  A query path that makes more than one backend call per query says so as a declared design choice,
  not an accident.

## Long jobs
- **Checkpoint progress**, so an interrupted rebuild resumes where it stopped instead of restarting.
  A rebuild that cannot be interrupted is a rebuild you cannot debug.
- A rebuild writes to a scratch index and switches by pointer (`kb-corpus`), so an aborted run leaves
  the live index untouched.
- Print progress the operator can read: documents and chunks done, rate, and what remains.

## Concurrency and load
- Parallelism is declared in configuration and never exceeds what the backend declares it can take.
  More workers on a saturated CPU-bound service buys queueing, not throughput.
- Under load, an optional stage sheds first (re-ranking off, keyword path serving) and **says so in
  the response** — shedding is allowed, silent shedding is not (`kb-retrieval`).

## Measure, before and after
- Record wall-clock and volume (documents, chunks, tokens) for a run, so "slow" is a number and an
  improvement is demonstrable. Put the numbers in the HANDOFF `evidence:` field.
- Measure before optimising as well as after: a number nobody recorded before the change cannot be
  beaten by a claim afterwards.
- Where a backend is optional, measure what it costs per query and record it next to the decision to
  keep it (`kb-retrieval`: an optional stage is never load-bearing).
