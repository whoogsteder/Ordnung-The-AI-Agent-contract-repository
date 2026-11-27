# Resource discipline <!-- persona -->
Applies: when calling embedding, re-ranking or other shared model services. Requires: base.md.

- Assume the backend is shared, slow and CPU-bound unless proven otherwise. Batch requests; never
  make one call per document when one call can take many.
- Cache by content hash. Unchanged content is never embedded twice.
- Fail fast with a clear error rather than retry-storming a backend that is down or saturated.
  Retries are bounded and reserved for errors that can plausibly succeed on a second attempt.
- Long jobs checkpoint progress, so an interrupted rebuild resumes instead of restarting.
- Measure before optimising and after: record the wall-clock and volume a run took, so "slow" is a
  number and an improvement is demonstrable.
