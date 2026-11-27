---
name: kb-eval
description: The golden question set and the gate it holds over retrieval changes — real questions each naming the source they must retrieve, a metric and threshold declared in configuration, committed reports whose diff is the evidence, a question added for every failure mode, the gate covering any change that can affect retrieval (chunking, embedding model, preprocessing, filters, ranking, prompts), recorded model output labelled as fixtures, and accepted regressions written as decisions. Use this whenever you change anything that can affect retrieval quality, when asked whether retrieval got better or worse, when a question stops retrieving its source, when writing, extending or running the question set or its reports, and before merging any such change.
---

# Evaluation

Retrieval quality is unfalsifiable without this. Every other change in the codebase has an obvious
test; a chunking change does not — until a question that used to retrieve the right document stops
retrieving it. The question set is the contract's teeth, and it is a memory of mistakes.

## The set
- It ships with the tool, committed: real questions, each naming the source it **must** retrieve.
  It grows; it is never trimmed to make a run green.
- **Every new failure mode adds a question** in the same change that fixes it, so the same mistake
  cannot recur unnoticed.
- Questions come from real usage: written by the owner, or proposed by the agent and approved
  (`kb-capture`). The people with the intent own what counts as a right answer.
- Each question names its expected source, not its expected wording, so a re-chunked corpus does not
  make the set meaningless.

## The gate
- **No change that can affect retrieval merges while the evaluation fails.** That includes chunking,
  embedding model, preprocessing, filtering, ranking and the prompts around them — not only "search
  code", because those are exactly the changes people do not think of as retrieval changes.
- State the metric and its threshold in configuration (for example recall@k, and what k means for the
  caller). A number without a threshold cannot be passed or failed.
- The run is a committed command, not a recipe in prose. Its output goes in the HANDOFF `evidence:`
  field.

## The report
- Commit one report per kept run. "It got better" is a claim; **the diff between two committed
  reports is the evidence.**
- Each report names the recipe it ran against — index identity, embedding model and version,
  chunking version — so two reports are comparable, or visibly are not.
- Retrieval behaviour is documented by its evaluation: the committed report outranks any prose that
  describes what the system finds.

## Layout
```
eval/questions/     # golden set: each question names the source it must retrieve
eval/reports/       # one committed report per kept run — the diff is the evidence
```

## Fixtures and recorded output
- Recorded model output (embeddings, scores, generated text) is labelled with the model, its version
  and the capture date, or marked synthetic. A score recorded from a different model certifies
  nothing about this one.
- A test exercises something outside the test file. Never assert a score table defined only inside
  the test.

## Tiers, cheapest first
static checks → corpus and exclusion tests → the golden question set against a built index →
end-to-end queries against a real deployment. A tier never certifies what only a higher tier can
show: a passing unit test says nothing about ranking quality, and a healthy endpoint says nothing
about either (`kb-retrieval`).

## Accepted regressions
Record a deliberate quality regression as a decision (ADR) in the same change that accepts it: what
dropped, by how much, why it is worth it, and what will restore it.
