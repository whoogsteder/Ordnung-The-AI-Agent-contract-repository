# Review checklists <!-- persona: module header -->
Applies: every review; pick the lists that match the artefact. Requires: base.md,
`rules/review_setup.md`.

Work through each applicable list. Every item produces either "pass" or a finding
(`rules/findings.md`). Do not skip an item because it looks fine. Check it.

## A. Fit to the yardstick (every artefact)
- Does it answer the question, or support the decision, stated in the yardstick? Does it answer a
  different, easier question?
- Is every must-have from the yardstick addressed? Did requirements change without the yardstick being
  updated?
- Is anything the yardstick ruled out back in?
- Can every term in the must-haves be read only one way? If a term has two plausible readings, does the
  artefact name the reading it took, and is that reading the user's?

## B. Facts (every artefact that states facts)
- Re-open the source of every load-bearing fact: a fact that decides a must-have, puts an option in
  or out, or drives a conclusion. Does the source say this, for this product, version, edition and
  date?
- Is any load-bearing fact unsourced, sourced from memory, or resting on a single practitioner report
  or a marketing page?
- Are vendor claims and measurements kept apart?
- Are conclusions presented as facts?

## C. Options and recommendations (selections, comparisons, research packs with options)
- **Must-have check:** for every recommended or shortlisted option, every must-have has a pass and a
  source. Build the table yourself from the sources. Do not copy the author's table. Shortlisted means
  any option the artefact tells the reader to buy, quote, test or deploy, including a secondary or
  "reference only" list. Such a list may carry a shorter table with `not established` as a value; it
  never carries none.
- **Missing candidates:** check the systems the option must work with (compatibility and validated
  lists, vendor reference designs), the incumbent vendor's named successor, and the preferred
  supplier's current equivalent. Name any obvious candidate that is absent, and whether it would pass.
- **Freshness:** is any recommended option end-of-sale, announced end-of-sale, or a previous
  generation? Check the vendor's lifecycle record (end-of-sale notices, lifecycle or warranty dates
  page), not the datasheet, and each hardware and OS combination where the vendor dates them apart.
- **Fairness:** same depth and same kind of source for every option. Is the recommendation conditional
  on an open decision, and if so, is it given per branch?

## D. Reader (documents and research briefs)
Read as the stated reader, with no prior context.
- After the first page, can you name the decision or purpose, the recommendation or outcome, and the
  open decisions? Write down what you would say. A mismatch with the artefact is a finding.
- List every term you had to look up and every sentence you had to read twice.
- Is the body within the agreed page budget? Does detail sit in annexes?
- Does the body contain internal ids, rule or contract references, placeholders, or narration of the
  author's process?
- Does a section read as amended (dated remarks, withdrawn items left in tables) instead of rewritten?

## E. Open decisions and assumptions
- Is every gap that only a person can close named, with an owner and a date?
- Is any "open item" really a lookup the author could have done?
- Are load-bearing assumptions stated where the reader will see them?

## F. Integrity
- Cross-references, figure references and source ids resolve.
- Facts shared with other documents in the set agree.
- The classification label is present. For a release review, also run the content scan of
  `rules/classification.md`.

## Which lists apply
| Artefact | Lists |
|---|---|
| Research pack | A, B, C (when options were sought), E, F |
| Selection or lifecycle document | A, B, C, D, E, F |
| Other document (architecture, how-to, plan, guide) | A, B, D, E, F; C if it recommends |
| Requirements brief | A (against the user's request), E, plus: is it confirmable, with no hidden decisions? |
