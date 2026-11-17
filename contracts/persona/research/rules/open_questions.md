# Open questions and assumptions <!-- persona: module header -->
Applies: every research task. Requires: base.md, `rules/question.md`.

The receiver of the research must never have to guess what it does not know, and must never find out
later that a stated fact was an assumption.

## What belongs in the register
Keep one register in `agent/REPO-MAP.md`, copied into the pack's "Contradictions and gaps" section:

`OQ-NNN | question | status | what changes with the answer | owner | needed by`

Statuses: `OPEN`, `ASSUMED` (work proceeds on a stated assumption awaiting sign-off), `DECIDED` (with
date and who decided), `NOT-APPLICABLE` (dismissed, with the reason).

Only two kinds of entry belong here:
- **Decisions a person must take**, such as which speed to standardise on or whether a vendor is
  allowed.
- **Facts only a person can supply**, such as a site survey, an internal price or a configuration
  export.

Anything the researcher can find out is not an open question. Find it out (`rules/method.md`). If it
cannot be found ("no public source states X"), that is a finding, and it goes in the pack as one.

## Assumptions
- Write an assumption down as an assumption, with what happens if it is wrong, and tell the user.
- Load-bearing assumptions, the ones that would change the answer if wrong, appear in the pack's
  "Answer in short".

## When an open decision splits the answer
Do not pick a side on the user's behalf. Research both branches to the depth agreed, and give the
answer per branch (`rules/research_pack.md`). Ask the user first if researching both would double the
work.

## Wording
Replace vague wording ("several", "various", "as needed", "best practice") with the number, the closed
list, the named source, or an open question.
