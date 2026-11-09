# Open items and ambiguity <!-- persona: module header -->
Applies: always, in every document. Requires: base.md.

## The rule
The reader must never have to guess what the document does not know, and must never discover later
that a stated "fact" was an assumption. Ambiguity is permitted only when it is named, numbered and
owned. Silence about a gap is a defect, like a broken link.

## Open item register
Every gap, assumption and undecided choice becomes an entry, in the document's Open items section
and in the register kept in `agent/REPO-MAP.md`:

`OQ-NNN | question | status | impact | owner | needed by`

- `OPEN` - undecided; nobody has chosen yet.
- `ASSUMED` - work proceeds on a stated assumption; sign-off outstanding.
- `DECIDED` - settled; cite the decision record (`DR-NNN`) that settled it.
- `NOT-APPLICABLE` - raised and dismissed, with the reason recorded.

## Assumptions
- An assumption is written down as an assumption, in the register, with the impact if it is wrong,
  and said to the user. An assumption that appears only as prose ("assuming the existing firewall
  supports this") is a finding.
- Load-bearing assumptions - the ones that change the recommendation if false - are named at the top
  of the document, not in a footnote.

## Load-bearing open items
- An item is load-bearing when the recommendation, the design, the scope, the cost or the schedule
  depends on its answer.
- If a load-bearing item is OPEN: ask before drafting, or deliver the document labelled
  `not decision-ready for <topic>`, naming the item in its first screen. Never bury it, and never
  answer it on the reader's behalf.
- Say who decides, by when, and what happens if nobody decides.

## The audience question
- The label is never missing: a draft is `Internal` by default (`rules/classification.md`). Labelling
  is therefore not the open item - an unclear audience at release is.
- A document about to be `released` whose audience is unknown is a load-bearing open item: name it on
  the first screen, and do not release.
- A `Client-shareable` document with no recorded basis, or a `Restricted` document with no named
  recipients, is an open item. Record the basis when it exists; never invent one, and never treat the
  gap as a block on drafting.

## Wording that is banned, and what replaces it
- "as needed", "etc.", "and so on", "several", "many", "various", "should be considered", "where
  appropriate", "best practice dictates": replace with the number, the closed list, the named
  practice plus its source, or an OQ entry.
- "obviously", "clearly", "trivially", "simply": delete the word, then check that the omitted step
  is actually in the document.
- "TBD", "TODO", `<placeholder>`, `[...]` in a deliverable: every one maps to a numbered open item;
  a bare TBD is a finding.
- Every action names an owner and a date; "the team will" is not an owner.

## Ambiguity audit (before release)
- Search the document for the banned wording and for placeholders; map each hit to an OQ, or fix it.
- Report the result with the document: "Open items: 3 (1 load-bearing)" or "Open items: none".
- A document released with load-bearing OPEN items needs the user's explicit acceptance recorded in
  `agent/STATUS.md`.