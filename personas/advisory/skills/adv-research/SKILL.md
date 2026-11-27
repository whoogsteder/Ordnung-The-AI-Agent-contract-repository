---
name: adv-research
description: Product and technology research for an advisory document — the research question, a search plan, primary sources first, a longlist from current portfolios, a must-have screen with a source per cell, lifecycle status from the vendor's own record, triangulating load-bearing facts, and the research pack (question, answer in short, findings, facts table, options, contradictions, sources) that the writer drafts from. Use this whenever a document will state a fact about a product, version, price, date, standard or compatibility, whenever options or vendors are being compared or picked, and when the user asks for product research, a market scan or a shortlist. Also use it to brief research workers.
---

# Research

Getting the answer right comes before presenting it well. A well-written document that recommends
the wrong product is worse than no document. Memory tells you *where to look*, never *what is
true*. Model names, editions, port layouts and dates are exactly what memory gets wrong.

## Before searching
- **The question.** Take the question and its must-haves from the confirmed brief
  (`adv-grilling`); don't ask the user again. A product or feature name that can be read two ways
  is named, with the reading you will search for, and the user confirms it.
- **The search plan.** Write it into the HANDOFF `## Plan`: the sub-questions, where each answer is
  most likely to be found, and what counts as enough. This doubles as the checkpoint before a long
  run.
- **Delegate wide searches** (`ordnung-delegate`). One worker per vendor or sub-question is a good
  split. The brief carries the must-haves verbatim, the source rules below, the pack's table shapes,
  and the line "search the generic question; never paste confidential details" (kernel rule 11).

## Which sources to trust, in order
1. Primary: the standard itself, the vendor's datasheet, lifecycle or end-of-sale pages, release
   notes, compatibility lists, and documentation for the version in use.
2. Reference designs and validated configurations from the vendor of the system it attaches to.
3. Independent measurement with a stated method.
4. Practitioner sources (forums, issue trackers). Mark them as such; they need confirming when
   load-bearing.
5. Marketing material is a claim to be checked, never evidence on its own.

## Options: longlist, screen, shortlist
1. **Longlist from current sources:**
   - each allowed vendor's current portfolio;
   - the compatibility lists and reference designs of the systems the option must attach to;
   - the incumbent's named successor;
   - the preferred supplier's current equivalent.
   Record where each candidate came from.
2. **Screen** every candidate against every must-have, with a source per cell. A candidate is out
   if it fails a must-have or is end-of-sale; give a one-line reason.
   - **Lifecycle status comes from the vendor's lifecycle record.** A fresh datasheet is not
     evidence, and neither is "no notice found".
   - If no record is found, the status is `not established`, and the candidate cannot be
     shortlisted on it.
3. **Shortlist** only the candidates that pass every must-have on checked facts. Nothing goes on it
   "pending verification".
   - Is an obvious candidate missing?
   - An empty or one-item shortlist is a finding to report, not a gap to fill with weaker
     candidates.

## Facts
- A **load-bearing fact** decides a must-have, puts an option in or out, or drives the
  recommendation. Check it at the primary source. When the primary source is unclear, confirm it
  with an independent second source.
- When sources disagree, record both and say which you trust and why. Never average them and never
  pick one silently.
- Check that the source covers the right version, edition, hardware revision and date.
- If a needed source can't be reached (login, paywall, no web access), ask the user to supply it.
  Don't guess.
- "No public source states X" is a finding.

## The research pack, `research/<topic>/pack.md`
Put a `version` and `date` line at the top, then these sections in order:
1. **Question**: its scope, must-haves and term readings, and the brief it came from.
2. **Answer in short**: five to ten plain lines covering the answer, the confidence and the main
   caveat.
3. **Findings**, by sub-question, each with source IDs. Conclusions are marked as conclusions.
4. **Facts table**:
   `F-NN | fact | applies to (product, version) | sources | checked: primary / second source / single`
5. **Options**:
   - the longlist: `candidate | origin | in/out | reason`;
   - the must-have check: `option | must-have | pass/fail | sources`;
   - the shortlist comparison.
6. **Contradictions and gaps.** A question only a person can answer becomes a Q-NN in PROJECT.md.
7. **Limits**: the date the pack is valid to, and what would make it stale (a new generation, an
   end-of-sale notice, a changed must-have).
8. **Sources**:
   `S-NN | what | publisher | product and version | URL | retrieved | type (primary, reference-design, measurement, practitioner, vendor-claim, user)`

IDs are fine in the pack, because the pack is a dataset; the writer turns it into prose. Save a copy
of every source a load-bearing fact rests on under `research/<topic>/sources/S-NN_<date>.<ext>`.
Links rot, and a reviewer must be able to check a fact without searching again.

## Handing over
The pack goes to drafting only after the fact check in `adv-review` passes. Report in chat in this
order: the answer, what is uncertain, then what you need from the user.
