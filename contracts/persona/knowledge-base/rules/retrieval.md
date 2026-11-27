# Retrieval <!-- persona -->
Applies: always on the query path. Requires: base.md.

- Report scores and citations with every result. A bare list of passages is not an answer: the
  caller cannot tell a confident hit from a near-miss without the score.
- "No result" is a valid, expected answer. Never synthesise a plausible hit to fill an empty set.
- Degradation is announced. If an optional stage (re-ranking, keyword fallback) did not run, the
  response says so. A silent fallback teaches callers to trust a weaker answer than they got.
- A stage that answered is not a stage that works. Health checks assert output quality — scores in
  range, ordering sane on a known case — not merely that the endpoint returned 200. A service can
  be up, fast, and useless.
- Ranking changes are made against the evaluation set, never against one anecdote.
- Filters that are mandatory are mandatory in the interface, not by convention. A caller must not be
  able to forget a scope filter and get another tenant's results.
