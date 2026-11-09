# Product and feature comparisons <!-- persona: module header -->
Applies: when comparing products, editions, features, standards or vendors. Requires: base.md,
`rules/verification.md`.

## Declare the question first
Before any matrix, state in the first screen: the decision being supported, who decides it, by when,
and the constraints that bind (budget, existing stack, skills, licensing, compliance, timeline). A
comparison without a question is a catalogue.

## Criteria
- List the criteria before scoring them, and say where each came from: the reader's question, a
  standard, the RFP, a stated constraint.
- Give every criterion a weight, or state "all criteria equal". When weights drive the
  recommendation, the weights are a decision record (`rules/dr.md`).
- Keep criteria countable: "supports S/MIME", not "good security". Split composite criteria
  ("management interface") into rows that can be checked.
- Separate must-have from nice-to-have. A product failing a must-have is out, and the table says so.

## Cells
- Every cell cites a source id and names the product edition, version and retrieval date; a shared
  table note may cover one date for the whole table.
- `unknown` is a legal cell value. Blank, guessed and "probably" are not. An `unknown` on a
  must-have criterion is a finding to close, not a footnote.
- Cells resting on vendor marketing are marked `vendor claim`.

## Compare like for like
- Same edition, same deployment model (on-premises, cloud, hybrid), same unit (per user, per core,
  per GB, per instance), same price basis (list or street, with or without support, first year or
  steady state, currency and exchange date).
- When editions differ across options, state the assumption and the reason in the table note.

## Fairness pass
- Same depth for every option: no option described from its marketing and another from its bug
  tracker.
- Steelman each option: state the conditions under which it wins. If an option wins on nothing, the
  criteria are wrong before the writing is.
- Name what would change the recommendation.

## Verdict for the reader
- Answer fit-for-purpose, not "best": what it costs to run, who operates it, the licensing and exit
  path, the migration effort, the risks, and the shape of total cost over the stated horizon.
- A tick matrix with no narrative is a finding; a verdict with no conditions is a finding.
- A recommendation that reverses an accepted DR needs a new DR superseding it.

## Expiry
- Every comparison carries "valid as of <date>" and its version basis. Re-check the sources before
  reissuing: a stale comparison is superseded, never edited in place.
- Benchmarks: state harness, workload, hardware and who ran it. Never compare numbers from two
  harnesses in one row.

## Visuals
Feature matrix as a table; scored comparison as a weighted table plus a bar summary with the axes
and weights named beside the figure; price over time as a graph; deployment-shape differences as a
diagram. See `rules/visuals.md`.

## Legal hygiene
Product and vendor names as registered; no fabricated benchmarks; confirm the licence for
third-party screenshots, logos and quoted tables before shipping them.