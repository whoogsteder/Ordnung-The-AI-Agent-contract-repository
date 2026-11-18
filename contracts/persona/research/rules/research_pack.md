# The research pack <!-- persona: module header -->
Applies: every research task whose result is handed to a writer, another agent or a later session.
Requires: base.md, `rules/sources.md`.

The research pack is the hand-over between this persona and the `document-writing` persona (or a
person). Its shape is fixed so the receiver knows where to look and can trust what it finds.

## Location
`topics/<topic>/pack.md`, with its sources under `topics/<topic>/sources/`. One pack per
question. The receiving project copies or links the whole `topics/<topic>/` directory.

## Sections, in this order
1. **Question.** The agreed question, its purpose, scope, must-haves and constraints, the reading taken
   for any term that can be read two ways, and the confirmation: date and the user's words, quoted.
2. **Answer in short.** Five to ten lines of plain language: the answer, the confidence, and the
   main caveat.
3. **Findings.** Grouped by sub-question. Each finding is one or two sentences with its source ids.
   Conclusions are marked as conclusions.
4. **Facts table.** One row per load-bearing fact:
   `F-NN | fact | applies to (product, version, edition) | source ids | checked (primary / second
   source / single source)`.
5. **Options** (when options were sought):
   - longlist: `candidate | where it came from | in/out | reason`
   - must-have check for every shortlisted option: `option | must-have | pass/fail | source ids`.
     Shortlisted means any option the pack tells the reader to buy, quote, test or deploy, including
     a secondary or reference list. A secondary list may use a shorter table, with `not established`
     as a value, but never none.
   - shortlist comparison (`rules/comparisons.md`)
6. **Contradictions and gaps.** Where sources disagree and what was trusted, what could not be found,
   and what only a person can supply. Each human question gets an owner (`rules/open_questions.md`).
7. **Limits.** What was out of scope, the date the pack is valid for, and what would make it stale (a
   new product generation, an end-of-sale notice, a changed must-have).
8. **Sources.** The source list from `rules/sources.md`.

## Rules for the pack
- The pack contains no recommendation the question did not ask for. When asked, it gives the
  recommendation with its conditions, per branch if an open decision splits it.
- Ids (F-, S-) are fine here. The pack is a dataset. The writer turns it into prose.
- A pack is versioned like a document: `pack.md` carries a `version` and `date` line at the top, and a
  change note at the end. A re-check after new information produces a new version, and the change note says
  which facts changed.
- Hand the pack over only after the review in `rules/verification.md` has passed. Hand it over with
  the review report. When a separate review (`review` persona) returns `fail`, the hand-over is
  blocked: fix, issue a new version, and have it re-reviewed. A pack already handed over is recalled
  by telling its receiver which version is blocked and why.
