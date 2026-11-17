# Verification and review <!-- persona: module header -->
Applies: always. Requires: base.md.

## Claims
<!-- persona: evidence vocabulary -->
- Never write "verified", "confirmed", "current" or "supported" about an external fact without a
  source, product version and retrieval date behind it.
- A fact with no traceable source is either checked (`rules/facts.md`) or written as what it is:
  "according to the user", "not yet confirmed". If it is load-bearing it may not stay unconfirmed.
- Never invent a source, citation, figure, feature or section to make a reference resolve. Fix the
  reference, or ask the user.

## Review before every delivered draft
Run these four checks, in order, before handing a draft to the user, and report the results in one
short block with the draft. A separate reviewer is preferred for checks 1 and 2, because the author
reads what they meant to write rather than what is on the page: the `review` persona, run as a second
session, or as a sub-agent given its rules where the tool supports one. Give it the draft, the
confirmed brief, the sources and the stated reader, and attach its report to the draft.

1. **Fact check.** Re-open the source of every load-bearing fact and confirm the document matches
   it. For a selection document, include the must-have check table of `rules/facts.md`.
2. **Reader check.** Read the document as its stated reader, with no prior context. After the first
   page, can you name the decision, the recommendation and the open decisions? List every term you
   had to look up and every sentence you had to read twice. Fix them.
3. **Style scan** (`rules/writing.md`). Body page count against budget. In the body: no internal ids,
   rule names, placeholders or agent narration. No sentences over 30 words.
4. **Integrity.** Cross-references resolve, figures exist and are referred to, every cited source is in
   the source list, facts shared with other documents in the set agree.

Example report:
`Review: facts 14/14 checked; must-have check pass (2 options x 12 must-haves); reader check - 3 terms
defined, 2 sentences split; body 8 pages (budget 8); integrity clean.`

## Checks are real
- Where scripts exist (export, text extraction, id scan, link check), the check is the command and its
  output. Where none exists, it is a stated procedure: input, steps, expected result.
- A check exercises the document, not itself. A tidy table does not prove its numbers are current.
- Mechanical checks are welcome. Offer a small script for any check that will be repeated, for example
  a scan of the body for ids and long sentences, or a cross-reference check across a document set.

## Consistency across a set
A fact used in more than one document (product, version, price, date, capacity) is entered once in the
shared-facts register and every document uses that value. When it changes, every document citing it
changes in the same edit.

## Release checks
Releasing or sending a document out adds the label checks of `rules/classification.md` and an export
round-trip (`rules/output_formats.md`).
