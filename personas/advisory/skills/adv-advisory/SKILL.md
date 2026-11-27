---
name: adv-advisory
description: Outlining and drafting technical documents a busy reader decides from — advisory and product-selection documents with implementation impact and considerations, design and architecture documents, how-tos, change plans and memos. Covers the document-type profiles (questions, skeleton, page budget, checks), the first-page rule, body versus annexes, fair comparisons and a verdict per branch, plain sentences, and keeping agent machinery out of the text. Use this whenever you outline, draft, restructure or rewrite a document, write up options or "potential picks", or describe what a choice means for implementation, even when the user just says "write it up".
---

# Writing the document

The reader is a busy person who has to decide or act. If they don't read the document, it has
failed, however complete it is.

## Workflow (do not skip ahead)
1. Confirmed brief (`adv-grilling`).
2. Facts from a research pack or checked lookups (`adv-research`).
3. **Outline.** Use the type's skeleton below, with one line per section saying what it will say,
   plus the page budget. Show it to the user; a short yes is enough.
4. Draft, in `documents/NNN-<type>-<topic>-v<major.minor>.md`.
5. Review (`adv-review`), then hand over with the review block.

Record each step in the HANDOFF. When a document moves through `brief`, `outline`, `draft`,
`in-review`, `released` or `superseded`, update its line in the PROJECT.md track. Once a document
is released it is never edited: a correction is a new version.

## Document types
Each profile gives what to ask about (feed this to `adv-grilling`), the body's skeleton, the page
budget and the checks.

**Advisory with picks and implementation impact.** This is the selection document, extended with
what each choice sets in motion.
- **Ask about:** the current state and how it is known; what must and must not change; growth;
  vendor and supplier limits; the operating model and skills; budget and timeline; who decides.
- **Body:**
  - summary and recommendation;
  - why now;
  - what the solution must do (the must-haves, in plain words);
  - the options considered and how they were screened;
  - the shortlist compared;
  - implementation impact per pick (see below);
  - risks;
  - next steps and open decisions.
- **Budget:** 6 to 10 pages.
- **Checks:** the must-have check passes for every recommended option; every candidate is
  current; every pick has its impact written out.

**Design or architecture document.**
- **Ask about:** scope and boundaries; the requirement each part answers; interfaces; security
  zones; operations; growth; the alternatives that were rejected.
- **Body:** summary; context and scope; requirements; the design (with one overview diagram); key
  decisions and the alternatives rejected; operations; risks.
- **Budget:** 8 to 15 pages.
- **Checks:** every element traces to a requirement; every interface appears on the diagram; every
  operations task has an owner.

**Integration how-to.**
- **Body:** what it achieves; prerequisites; numbered steps, one action each, with the expected
  result; test; rollback; troubleshooting.
- **Budget:** 3 to 8 pages.
- **Checks:** every command comes from a tested run or a cited vendor document, with its version.

**Change or implementation plan.**
- **Body:** summary; scope; phases with entry and exit criteria; schedule; roles; risks; test and
  acceptance; rollback, with a decision point and a time limit; communication.
- **Budget:** 4 to 10 pages.

**Memo or notice.**
- **Body:** the bottom line and its urgency, worded as one of:
  - `Action required by <date>`
  - `Advisory - next maintenance window`
  - `Notice - no action`

  Then: what is happening; who is affected; what to do, by whom and by when; the risk of not acting.
- **Budget:** 1 to 2 pages.

For any other type, agree its purpose, reader, skeleton and budget in the brief.

## Implementation impact, per pick
For each shortlisted option, write these in prose, with a table where it compares better:
- **What changes:** systems, integrations, data migration, network or hardware, licences.
- **Effort and sequence:** the phases, the rough effort, the dependencies, and the downtime or
  change windows.
- **People and operations:** the skills needed, the training, who runs it day to day, and the
  support model.
- **Cost shape over the horizon:** one-off costs versus recurring ones, on the same price basis for
  every option.
- **Risks and exit:** what could go wrong, how it is reversed, and lock-in.
- **When this pick is the right one.** An option that wins on nothing doesn't belong on the
  shortlist.

## Comparing fairly
- Must-haves come from the brief and work as a screen. They are not scored.
- Score only what separates the shortlist: three to six countable criteria. Agree the weights with
  the user before scoring.
- Compare like for like: the same edition, deployment model and price basis. Note any difference.
- Describe every option at the same depth, and from the same kind of source.
- **Make a recommendation.** If an open decision changes it, give the recommendation per branch.
  Name what would change it. A matrix with no narrative is not a verdict.
- State the date the comparison is valid to: "valid as of <date>".

## The page
- **The first page answers four things:**
  - what is being decided;
  - the recommendation;
  - the two or three reasons for it;
  - what is still open, and who must answer it.

  Nothing comes before it except a one-line header (`id | title | version | status | date | owner |
  audience | classification`).
- **The body stands on its own.** Detail goes into annexes and is never deleted: the full longlist,
  the must-have check with its sources, the matrices, the open-decision register, the sources and a
  change note.
- **Stay within the page budget.** Report with every draft, for example: "Body: 7 pages (budget
  8). Annexes: 4."
- **Sentences:**
  - one point per sentence, averaging under 20 words; rewrite any sentence over 30;
  - active voice, with a concrete subject;
  - define each term in the sentence where it first appears;
  - use numbers, not adjectives ("48 × 25G ports", not "high-density").
- **Nothing from the machinery:**
  - no REQ, DR, Q, F or S IDs in running text; refer to things by name ("the storage question,
    annex B");
  - no rule names;
  - no TODO or TBD;
  - no narration of your own reasoning.
- **Load-bearing assumptions** are stated in plain words on the first page, with what happens if
  they are wrong.
- **Look for visuals.** Ask where a table or diagram would carry the point better. Tables suit
  lookups and comparisons. Diagrams suit components and flows: keep them as Mermaid or PlantUML
  source next to the rendered image. Every figure gets a caption that states its conclusion, and
  the text refers to it.
- **Rewrite; don't amend.** When an input changes, rewrite the affected sections whole. One line in
  the change note records the change.

## Before you hand it to review
Check the draft yourself first:
- Read each section's first sentence on its own. Together, those sentences should tell the story.
- Grep the body for IDs, TODO and sentences over 30 words, and fix every hit.
