---
name: adv-grilling
description: Runs the requirements session for a technical or advisory document — asks the questions in batches, challenges answers that conflict, separates facts from wishes and from open decisions, finds the gaps the user did not mention, and writes the requirements brief that gates all drafting. Use this whenever a new document or research question starts, when the user asks to be grilled or questioned, when a requirement or fact changes mid-project, and before anyone writes an outline or a draft. Also use it to resume an interrupted question session.
---

# Requirements session and the brief

Most of a document's value is created here. A document can only be as good as the requirements
it answers, and the brief is what stops those requirements from drifting once drafting starts.

## Files
- The brief lives in `briefs/NNN-<topic>.md`. Number it from the documents list in
  `agent/REPO-MAP.md`.
- **Write each round of answers into the brief as soon as you have them, before asking the next
  round.** A session can be compacted at any point, and an answer that exists only in the chat is
  lost. Set the HANDOFF `next_action` to the next round ("Ask round 3: operating model and
  sign-off").
- A requirement that outlives this document becomes a REQ-NN in PROJECT.md (`ordnung-ledger`).
  Examples: "everything must run on-premises", "vendor X is excluded". The musts of a single
  document stay in its brief.

## How to question
- **Batch the questions**, at most about seven per round, grouped by theme. When the reason for a
  question is not obvious, say why it matters ("this decides whether cloud options stay on the
  list").
- **Start from the document type's checklist** (`adv-advisory`, "Document types"). Ask about every
  item the user has not already answered.
- **Challenge; don't just take notes.** When an answer conflicts with an earlier one, with the
  current state as the user described it, or with how the technology works, say so and ask which
  holds.
- **Separate three kinds of statement**, and record each as what it is:
  - a fact: "we run X today";
  - a requirement: "it must do Y";
  - an open decision: "Y depends on the board meeting in March".
- **Hunt for the gaps the user hasn't mentioned:** dependencies on other systems, who operates it
  and with what skills, migration and rollback, lifecycle dates, licensing and exit, physical
  limits, and who signs off.
- **Implementation impact needs its own questions:** what has to change around the chosen option
  (people, processes, integrations, data migration, downtime), and what must not change.
- **Find the reader and their time.** That sets the page budget.
- **Ask about research:** whether it needs a screened longlist (`adv-research`), whether web
  searches are allowed, and which material is confidential.
- **Don't ask what you can look up.** A datasheet fact is research, not a question for the user.

## The brief (one to two pages, plain language)
1. **Decision or purpose**: what the reader must be able to decide or do, in one or two sentences.
2. **Reader and budget**: who reads it, the language, and the body's page budget.
3. **Current state**: each fact with its origin (the user, an export, a document).
4. **Requirements** grouped as must, should and not required. A must is something whose failure
   rules an option out. Must-haves are never assumed.
5. **Constraints**: budget, vendors, timeline, skills, policy.
6. **Implementation context**: what the choice touches, and what must stay as it is.
7. **Research plan**: a research pack at `research/<topic>/`, or a few lookups by the writer.
8. **Open decisions**: only questions a person must answer, each with its owner and what changes
   with the answer. Each one is also a Q-NN in PROJECT.md.

## The gate
Show the brief and ask for confirmation. Confirmation counts when the user either:
- says so in words, or
- answers every open item and objects to nothing else.

Don't ask a second time when the second form applies. Record the date and the user's words, quoted,
in the brief and in the PROJECT.md track. Until then the HANDOFF stays at the brief, and no outline
or draft is written. That is kernel rule 9.

When a should-have or a scoring weight was left unsettled, it may go ahead as ASSUMED, named in the
brief. A must-have may not.

## When something changes later
- Update the brief first, with the date. Then rewrite every affected section of the document, so
  that it reads as if the new fact had always been true. The change note records what changed.
- If the change touches a must-have or an open decision, the screening (`adv-research`) is void
  until it is re-run.
- If the same fact changes twice, stop and ask the user to settle it.
- If an open decision changes which options qualify, either get it answered before drafting, or
  write the recommendation as branches ("if 10GbE: A; if 25GbE: B"). Never blend the two into one
  hedged answer.
