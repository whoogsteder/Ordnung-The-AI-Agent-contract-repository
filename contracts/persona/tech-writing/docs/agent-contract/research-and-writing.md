# Research, the brief and writing for the reader - rationale

Explains: `rules/requirements.md`, `rules/research.md`, `rules/writing.md`, `rules/doc_types.md`, the
review step in `rules/verification.md`, and the 2.0.0 rebalancing of the persona.

## What happened with 1.x
Version 1.x was tested on a real product selection: replacing a top-of-rack switch pair at a few dozen
sites. The contract did its governance job: classification, registers, open items, decision records
and a mechanical cross-reference check. The questioning session with the user was valuable and the
overall framework was sound. The document still failed in three ways:

1. **Wrong answer.** Candidate specifications were written from the model's memory, tagged
   `unverified`, and parked as open items. Both recommended models failed the document's own
   must-haves (wrong port type and count), and the vendor's own reference switch for the attached
   server platform was never considered. The agent had flagged its doubt about the port layouts as an
   open item and recommended them anyway.
2. **Unusable length.** Around 50 pages for a decision a team should be able to take after a short
   read. A reviewer will not work through that, so the document cannot do its job as decision support.
3. **Hard to read.** Internal ids in running text, references to rule files, compliance statements,
   stacked qualifications, and sentences that read like the agent's reasoning.

## Why the 1.x rules produced that
- **Recording counted as handling.** "Ambiguity is allowed when named, numbered and owned" let the
  agent turn its own research tasks into open items for the reader. 2.0 splits gaps into ones a
  person must close (open decisions) and ones research can close (agent work), and forbids
  recommending on unchecked facts.
- **No longlist method.** 1.x said how to score a comparison but not where candidates come from.
  Memory filled the gap. 2.0 starts the longlist from current portfolios, compatibility lists and
  vendor reference designs.
- **Auditable rules leak into the text.** Rules phrased as "X is a finding" make the agent prove
  compliance on the page. 2.0 keeps the machinery (ids, registers, rule references) out of the body.
- **Length rules covered only advisories.** 2.0 sets a page budget per document type and agrees it in
  the brief.
- **Amend-in-place.** Corrections piled up as dated remarks and stale tables. 2.0 rewrites affected
  sections when inputs change. The change note is the only history in the document.
- **Requirements drifted.** Facts were scattered across registers and changed during drafting. 2.0
  adds a one-to-two-page brief that the user confirms before drafting starts.

## Why "right, usable, traceable", in that order
Traceability is what makes the work checkable, but it is a means. A document that is perfectly traced
and wrong, or traced and unread, has failed. The order tells the agent what to give up first when the
rules pull against each other: detail moves to an annex before readability suffers, and nothing ships
before the facts are right.

## Why a separate reviewer
An author re-reads what they meant to write. A reviewer with no prior context, playing the stated
reader, finds undefined terms, buried decisions and overlong passages that the author cannot see. That
is why the reader check and fact check are preferably run by a subagent or a second session.

## What was kept
The questioning session, the open-decisions and assumptions register, decision records, the
classification ladder, the output-format menu, the visual pass, and mechanical checks. They are
shorter, and the release-only parts of governance are applied at release rather than from the first
draft.
