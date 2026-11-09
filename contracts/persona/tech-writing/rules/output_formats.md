# Output format <!-- persona: module header -->
Applies: whenever a document is produced, exported or published. Requires: base.md.

## Never choose the format silently
Offer the menu and ask for a choice before the first substantial draft, then record the choice in
the document header and in the document map:
- **Markdown** - the source of record: repository diffs, review, agent-editable, portable.
- **Rich text / word processor** - Word `.docx`, LibreOffice `.odt` (`.rtf` for legacy readers):
  real styles, table of contents, captions, comments for review.
- **User-specified** - PDF (fixed layout, sign-off), HTML, AsciiDoc, reStructuredText, LaTeX,
  Confluence/Wiki, Google Docs, plain text.
Ask once per document set, and again when the target reader changes. When the user names a format,
use it. When the user has already answered this question in this project, the recorded answer stands
- do not re-ask.

## One source, many targets
- Keep one canonical source (Markdown by default) plus a documented export path per target, so the
  same source yields every format. Never maintain the same content twice in two formats.
- Record the export recipe with the document: exact command, tool and version, template used.
- Rich-text targets: headings map to real paragraph styles (Heading 1..3), tables to table styles,
  numbering to list styles - no bold text posing as a heading. ASCII-art diagrams belong in Markdown
  only; in rich text use the rendered image.
- Markdown targets: no raw HTML unless the renderer is known to accept it.

## Offer the code path
When the target is a binary format (`.docx`, `.odt`, `.pdf`, `.xlsx`, `.pptx`), or the same document
is produced repeatedly, offer to generate it with a small committed script rather than hand-shaping,
and name the tool:
- `pandoc` with `--reference-doc templates/reference.docx` and `--toc` for md -> docx/odt/pdf/html.
- `python-docx` or `docxtpl` for Word templates with placeholders, tables and styles.
- `openpyxl` for matrix workbooks; `matplotlib` for graphs; `mermaid`/`plantuml`/`graphviz` for
  diagrams; `weasyprint`/`reportlab` for PDF.
Give the install command when a tool is missing. Never fake an export, and never ship a file whose
extension does not match its content.

## Check what you shipped
- Round-trip the export: extract the text (`pandoc out.docx -t plain`, a `python-docx` walk, or
  `pdftotext`) and confirm headings, tables, captions and numbering survived. Report command, result.
- Figures must exist in the exported file, not only in the source; count them.
- The classification label survived the export: header line one, a footer on every page of rich text
  and PDF, the banner at the top of Markdown and HTML. Count the pages carrying it; an export without
  the label is not shippable (`rules/classification.md`).
- Units, date format (ISO `YYYY-MM-DD`) and capitalisation follow the project style register.
- Name outputs `<doc-id>-v<version>.<ext>` beside the source. Generated artifacts are build output:
  not indexed in REPO-MAP.