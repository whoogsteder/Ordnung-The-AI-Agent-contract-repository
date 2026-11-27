# Evaluation <!-- persona -->
Applies: always. Requires: base.md.

- A golden question set ships with the tool: real questions, each with the source it must
  retrieve. It is committed, and it grows.
- No change that can affect retrieval merges while the evaluation fails. That includes chunking,
  embedding model, ranking, filtering and preprocessing changes — not only "search code".
- Every new failure mode adds a question, so the same mistake cannot recur unnoticed.
- The evaluation report is committed. "It got better" is a claim; the diff between two reports is
  the evidence.
- State the metric and its threshold (recall@k, and what k means for the caller). A number without
  a threshold cannot be passed or failed.
- When a quality regression is accepted deliberately, record it as a decision with its reason, in
  the same change that accepts it.

## Project layout (additive)

```
[project root]/
└── eval/
    ├── questions/     # Golden question set: each question names the source it must retrieve
    └── reports/       # Committed reports, one per kept run — the diff is the evidence
```
