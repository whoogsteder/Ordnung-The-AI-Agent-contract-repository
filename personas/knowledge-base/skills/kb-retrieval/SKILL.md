---
name: kb-retrieval
description: Rules for the query path — scores and citations on every result, "no result" as a first-class typed answer instead of a synthesised one, degradation announced rather than a silent fallback, health checks that assert output quality rather than an endpoint returning 200, ranking changes made only against the golden question set, and mandatory filters enforced in the interface. Use this whenever you write or change search or retrieval code, a re-ranking, keyword or expansion stage, a health or readiness check, a query response shape or score threshold, when a search returns nothing or returns something that looks wrong, or before you trust a retrieval result enough to act on it.
---

# Retrieval

A retrieval system can be fully operational and wrong. In a real audit of a deployed re-ranker, the
endpoint was healthy, fast and schema-valid — and the *correct* document scored `4.1e-12` while an
irrelevant one scored `1.7e-09`. A working cross-encoder puts a relevant document near `1.0`, so the
ordering was effectively random. The cause was a model file missing a template the reranker needs
before its classification token can be read: invisible from the API surface. No ordinary health
check would have noticed. Every rule here exists so that "it answered" does not count as "it works".

## Every result carries
- Its **score** and its **citation** (source plus location). A bare list of passages is not an
  answer: the caller cannot tell a confident hit from a near-miss without the score.
- The score's meaning: the range, and the hit threshold, both declared in configuration. A result
  below the threshold is reported as *no result*, not as a weak hit.

## "No result" is an answer
- A first-class, documented, well-typed outcome, distinct from *backend unavailable* and *not
  authorised* (`kb-interfaces`).
- Never synthesise a plausible hit to fill an empty set. An agent rewarded for producing an answer
  will produce one from nothing; the typed empty outcome is what lets it behave correctly instead
  of improvising.

## Degradation is announced
- If an optional stage (re-ranking, keyword fallback, query expansion) did not run, the **response**
  says so, not only the log. A silent fallback teaches callers to trust a weaker answer than they got.
- An optional stage is never load-bearing: the system is correct with it absent.

## Health checks assert quality
- **A stage that answered is not a stage that works.** A health check runs a known query and asserts
  output quality: scores inside the declared range, the known document inside the top-k, ordering
  sane on a known relevant/irrelevant pair. Endpoint-up is a precondition, not a result.
- Check the shape of the scores, not only their presence. All scores near zero, or the same score for
  unrelated documents, or scores that do not change when the query changes, is a broken stage — not a
  bad day.
- A stage that cannot produce meaningful scores (missing template, wrong head, unloaded weights) fails
  loudly at load time, not silently at query time.

## Changing ranking
- Any change that can move a ranking is evaluated against the golden question set (`kb-eval`), never
  against one anecdote. That includes preprocessing, filters and chunking, not only "search code".
- A quality regression accepted deliberately is recorded as a decision in the same change.
- A retrieval claim in a report or a doc names the run that backs it: the committed eval report, not
  this paragraph.
