# Open decisions and assumptions <!-- persona: module header -->
Applies: every document. Requires: base.md, `rules/requirements.md`.

The reader must never have to guess what the document does not know, and must never find out later
that a stated fact was an assumption. A gap is allowed when it is named and has an owner.

## What belongs in the register
Keep one register in `agent/REPO-MAP.md`, copied into the document's annex:

`OQ-NNN | question | status | what changes with the answer | owner | needed by`

Statuses: `OPEN` (nobody has decided), `ASSUMED` (work proceeds on a stated assumption awaiting
sign-off), `DECIDED` (settled, with date and who decided), `NOT-APPLICABLE` (dismissed, with the
reason).

Only two kinds of entry belong here:
- **Decisions a person must take:** the user, a client, a manager, a supplier.
- **Facts only a person can supply:** a site survey, an internal price, a configuration export.

Lookups the agent can do itself (datasheets, lifecycle pages, compatibility lists, standards) are not
open items. Do them (`rules/research.md`).

## Assumptions
- Write an assumption down as an assumption, with what happens if it is wrong, and tell the user.
- Load-bearing assumptions, the ones that would change the recommendation if wrong, are stated in plain
  words on the first page.

## In the body
- The first page names the open decisions that matter, in plain words, with who answers them and by
  when. Usually that is between one and five. The rest stay in the annex register.
- Refer to an open decision by what it is about ("the 25GbE question"), not by its id.
- If a load-bearing decision is open, either get it answered before drafting, or write the
  recommendation per branch (`rules/requirements.md`). Never answer it on the reader's behalf.

## Wording
- Replace vague wording with the number, the closed list, or an open decision: "as needed", "etc.",
  "several", "various", "where appropriate", "should be considered", "best practice".
- Delete "obviously", "clearly", "simply", then check that the step they hid is written down.
- Every action names an owner and a date. "The team will" is not an owner.

## Before delivery
Report with the draft: "Open decisions: 3 (1 changes the recommendation). Assumptions: 2." A document
released while a decision that changes the recommendation is still open needs the user's explicit
acceptance, recorded in `agent/STATUS.md`.
