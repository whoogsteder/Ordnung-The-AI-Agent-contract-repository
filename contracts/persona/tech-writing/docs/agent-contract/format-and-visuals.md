# Format choice, generation, and the visual pass

Companion to `rules/output_formats.md` and `rules/visuals.md`. Start at [index.md](index.md).

## Why the agent may not choose the format
Format is not a style preference, it is an infrastructure decision. It fixes the toolchain (pandoc,
python-docx, a style reference), the figure format (Mermaid source versus rendered image), the table
widths, the review channel (pull request versus Word comments) and the archival target. The user's
organisation usually already has a standard the agent cannot see. Choosing silently also produces the
worst state in document work: the same content in two formats, maintained twice, drifting.

The menu exists so the question takes one line, and so the answer is recorded once in the document
map instead of being re-litigated per document.

## Why generation beats hand-shaping
A `.docx` assembled by copy-paste is not reproducible: styles are local, numbering is manual, and
the next revision is a fresh act of copy-paste. A generator (pandoc with a reference document, or
python-docx/docxtpl over a template) makes the format a reviewable artifact: styles live in one
reference file, export is one command, a style change is a diff. Reproducibility is also honesty -
the export recipe in the change note is what lets someone else prove what shipped.

"Offer the code path" is an offer, not a mandate. For a one-off memo, hand-shaping is fine; the rule
is that the agent says which tool it would use, and names the install command when it is missing.

## Why "never fake an export"
A file named `.docx` that is renamed text opens as corrupt in Word and is unreadable to a compliance
archive. An extension is a claim about bytes, and the check (extract the text, count the figures) is
cheap, so the rule is cheap.

## Why figures are named in the draft, not invented at the end
The visual pass runs on the draft, and unmet needs become `FIG-NN: <what> -- <why> -- to-make`
placeholders, which are open items. Two reasons: the author is the one who can feel where prose is
doing the work of a table, and a named gap is visible to the user, who may decide it is not worth
making. Silent omission is invisible, and invisibility is the whole problem.

## Why one sentence must point at every figure
A figure nothing references is decoration: it costs a page, a caption and a licence check. The
reference rule proves the figure is load-bearing, which is what justifies maintaining it.

## Why diagrams are kept as text
A PNG cannot be reviewed in a diff; a Mermaid, PlantUML or Graphviz source can, and it re-renders
when the architecture changes. Architecture diagrams go stale fastest in exactly the documents that
live longest, so the source is committed beside the image and the render command is recorded.

## Why ASCII art is Markdown-only
ASCII art inside Word is a formatting accident waiting for a font change: Markdown is read in a
monospace context, rich text is not. That is a rendering fact, written as a rule so it is applied
before the export instead of after the complaint.

## Why screenshots get a redaction rule
Screenshots carry what the document does not intend to disclose: real hostnames, user handles,
tokens, internal chat panes, salary tables. Redaction before commit is the only point at which it is
cheap.