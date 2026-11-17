# Writing for the reader <!-- persona: module header -->
Applies: every document, every draft. Requires: base.md.

The reader is a busy person who must decide or act. If they will not read the document, it has
failed, however complete it is.

## Two layers
- **Body:** readable chapters and paragraphs that a reader can get through in one sitting. It
  explains the situation, the options, the recommendation and what is still open, in plain prose with
  a few tables where tables are clearer.
- **Annexes:** the dataset. Requirement lists, full comparison matrices, inventories, the open-items
  and assumptions register, the source list. Detail moves here, it is not deleted.
- The body must stand on its own. A reader who never opens an annex still understands the decision,
  the reasons and the risks.

## Page budget
- Agree the body's page budget in the brief (`rules/requirements.md`), proportional to the stakes and
  the reader's time. Defaults per type are in `rules/doc_types.md`.
- Stay inside it. If the content does not fit, cut or move to an annex. If it genuinely cannot fit, ask
  the user before going over.
- Report the body length with every draft: "Body: 7 pages (budget 8). Annexes: 4 pages."

## First page
The first page answers, in plain words: what is being decided or done, the recommendation or outcome,
the two or three reasons for it, and what is still open and who must answer it. No document-control
tables, confidence-tag legends or reading instructions ahead of it. Metadata goes in a compact header
block or at the end.

## Sentences
- One point per sentence. Split a sentence that carries two decisions or two qualifications.
- Short sentences. Aim for an average under 20 words. A sentence over 30 words gets rewritten.
- Active voice and concrete subjects: "Dell's S5248F-ON supports PFC" rather than "PFC support is
  provided".
- Define a term or acronym the first time it is used, in the sentence itself. Do not rely on a
  glossary.
- Numbers instead of adjectives: "48 × 25G ports", not "high-density".
- Use the reader's vocabulary. Prefer the name people use in the room to a formal identifier.
- No rhetorical or editorial voice ("the thing that should worry the reader", "stated plainly",
  "the honest answer"). State the point.

## Nothing from the machinery
The body never contains:
- internal ids (OQ-, SF-, DR-, TBD-, requirement ids) in running text. Refer to things by name
  ("the storage question, annex B"). Ids may appear in annex tables.
- rule-file names, contract terms or compliance statements ("as required by…", "this is a finding").
- narration of the agent's own process or reasoning ("this draft would defend…", "the instruction
  behind this draft…").
- placeholders such as FIG-nn, TODO or TBD. Track those in the working notes or the register, not in
  the text.
- more than one confidence marker per claim. Prefer a plain phrase ("according to the vendor",
  "not yet confirmed") over tag systems.

## Rewrite, do not amend
A draft is rewritten whole when its inputs change. It never accumulates corrections, "conditional
since" remarks, withdrawn options left in tables, or stale scores with warnings. Corrections belong in
the change note at the end, one line each.

## Self-check before handing over
- Can the stated reader name the decision, the recommendation and the open questions after reading
  only the first page?
- Is the body within budget?
- Search the body for ids, rule names, placeholders and sentences over 30 words, and fix every hit.
- Read each section's first sentence alone: together they should tell the story.
