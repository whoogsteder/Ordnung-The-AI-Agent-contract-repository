# Requirements and the brief <!-- persona: module header -->
Applies: before drafting any document, and whenever a requirement changes. Requires: base.md.

A document is only as good as the requirements it answers. The questioning session with the user is
where most of the value is created, and the brief is what stops the requirements from drifting
afterwards.

## The questioning session
- Ask before you write. Work through the checklist for the document type (`rules/doc_types.md`) and
  ask about every item the user has not already answered. Batch related questions, at most about seven per
  round, and say why each one matters when the reason is not obvious.
- Challenge, do not transcribe. When an answer conflicts with an earlier one, with the estate as
  described, or with how the technology works, say so and ask which holds.
- Separate facts from wishes and from strategy. "We run X today" is a fact. "We want Y" is a
  requirement. "Y depends on a client meeting next month" is an open decision. Record each as what it
  is.
- Look for gaps the user has not mentioned: dependencies on other systems, the operating model,
  physical constraints, lifecycle dates, licensing, and who signs off. Ask about these as well.
- Find out who reads the document and how long they will spend on it. That sets the page budget
  (`rules/writing.md`).

## The requirements brief (gate)
After the questioning session, write the brief: one to two pages, plain language, no internal ids in
the body. It holds:
1. **The decision or purpose.** One or two sentences: what the reader must be able to decide or do.
2. **Reader and budget.** Who reads it, the language, and the agreed page budget for the body.
3. **Current state.** The facts the document stands on, each with where it came from (user
   statement, inventory export, document).
4. **Requirements.** Grouped as must, should and not required. A must is something whose failure
   rules an option out.
5. **Constraints.** Budget, vendors, timeline, skills, policy.
6. **Open decisions.** Only questions a human must answer, each with who answers it and what changes
   with the answer.

**Show the brief to the user and get it confirmed before drafting.** Record the confirmation (date,
and any changes) in `agent/STATUS.md`. An unconfirmed brief means drafting has not started.

## When something changes
- A changed requirement or fact goes into the brief first, with the date. Then rewrite every section
  it affects so that the document reads as if the new fact had always been true. The change note
  records what changed. The body does not carry "since <date>" remarks, stale columns or amendment
  paragraphs.
- If the change touches a must-have or an open decision, redo the screening of options
  (`rules/research.md`). A recommendation made under the old requirements is void until it is
  re-checked.
- If the same fact has changed twice, stop and ask the user to settle it before writing further.

## Open decisions are not a substitute for work
- An open decision belongs to a person: the user, a client, a manager. Questions the agent can answer
  itself by reading a datasheet, a lifecycle page or a compatibility list are research tasks, not open
  items (`rules/research.md`).
- If an open decision changes which options qualify, either get it answered before drafting, or
  write the document as branches ("if 10GbE: A or B; if 25GbE: C or D") and keep each branch
  complete. Do not draft one blended answer that hedges across both.
