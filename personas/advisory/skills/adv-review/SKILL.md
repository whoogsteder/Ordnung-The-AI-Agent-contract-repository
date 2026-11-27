---
name: adv-review
description: Review, release and export for advisory and design documents — the four checks before any draft is handed over (fact check against sources, cold reader check, style scan, integrity), using an independent reviewer worker, the review block reported with the draft, classification labels and the content scan at release, choosing and round-tripping the output format (Markdown source, docx, PDF via pandoc). Use this before handing any draft or research pack to the user, before writing that a document or fact is checked, when exporting, and when releasing or sending a document out.
---

# Review, release and export

The author reads what they meant to write, not what is on the page. So a separate reviewer does
the fact check and the reader check whenever the harness can run a worker.

## The four checks, before every draft goes to the user
1. **Fact check.** Re-open the source of every load-bearing fact and confirm that the document
   matches it. For a selection, include the must-have check table.
2. **Reader check.** Read the document as its stated reader would, with no prior context.
   - After the first page, can you name the decision, the recommendation and the open decisions?
   - List every term you had to look up and every sentence you had to read twice, then fix them.
3. **Style scan.** Count the body's pages against the budget. Look for IDs, rule names,
   placeholders, agent narration and sentences over 30 words in the body.
4. **Integrity.** Cross-references resolve, figures exist and are referred to, every cited source
   is in the source list, and facts shared with other documents agree.

## Using a reviewer worker
Use `ordnung-delegate`. Give the reviewer:
- the draft, the confirmed brief, the research pack and its sources, and the stated reader;
- these four checks, verbatim;
- the fence "do not edit the document; report findings only".

Integrate what it finds and fix the draft. Re-run any check whose result changed.

## The review block
Report it with the draft, and put the same line in the HANDOFF `evidence:` field. For example:

`Review: facts 14/14 checked; must-have check pass (2 options x 12 must-haves); reader check: 3 terms defined, 2 sentences split; body 8 pages (budget 8); integrity clean.`

Also say how many decisions are still open: "Open decisions: 3 (1 changes the recommendation).
Assumptions: 2."

Releasing while a decision that changes the recommendation is still open needs the user's explicit
acceptance, recorded in PROJECT.md.

A pack or draft whose review failed is not used. Fix it, issue a new version, and review it again.

## Classification
The labels, from most open to most restrictive:
- `Public`
- `Client-shareable`
- `Internal` (the default for every draft)
- `Restricted`

The label goes in the header line and on page one.
- Narrowing a label is free.
- Widening one needs a DR first (`ordnung-ledger`): the new tier, the recipient, the basis, the date
  and who decided.
- Excerpts and figures inherit their parent's label.

**At release:**
- Check the label is present everywhere, including the export footers.
- Run the content scan for the tier:
  - for every tier: no credentials, keys or personal ID numbers;
  - for `Public`: also no client names, internal hostnames, contract amounts, NDA material or
    personal data.
- Log the distribution in PROJECT.md: `document + version | recipient | date | channel | label`.

A label never authorises sending. Sending or uploading happens only on the user's explicit yes
(kernel rule 7).

## Output format
- Never choose the format silently. Ask once per document set (Markdown source; docx or odt; PDF;
  other), and record the answer as a DR.
- Keep one source, Markdown by default, and one recorded export recipe per target. For example:
  `pandoc doc.md -o doc.docx --reference-doc templates/reference.docx --toc`
  Give the install command if a tool is missing.
- **Round-trip every export.** Extract the text (`pandoc out.docx -t plain`, or `pdftotext`), then
  confirm that the headings, tables, figures and classification footer survived. Report the command
  and its result.
- Never fake an export, and never ship a file whose extension doesn't match its content.
