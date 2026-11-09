# Figures, graphs and tables <!-- persona: module header -->
Applies: every document that carries data, structure, comparison or flow. Requires: base.md.

## The visual pass
Every document gets one pass that asks: where would a figure, graph or table carry the information
better than the sentence does? Record the answer in the draft as a placeholder line:

`FIG-NN: <what it shows> -- <why it helps> -- <made | to-make>`

A to-make figure is an open item (OQ-NNN) until it exists. Naming the spot is allowed; leaving the
need unnamed is not.

## What suits what
- **Table:** the reader compares more than two items on more than two attributes, or looks values up
  (ports, limits, versions, prices, owners, dates).
- **Matrix:** feature comparison, RACI, risk by likelihood and impact, control-to-standard coverage.
- **Line graph:** change over time - capacity growth, cost over a horizon, latency under load.
- **Bar:** magnitude across a few categories; scored-comparison totals.
- **Pie/donut:** shares of one whole where the parts are mutually exclusive; prefer a table past
  about five slices.
- **Architecture/deployment diagram:** components, boundaries, trust zones, connections; label
  protocols and ports.
- **Sequence diagram:** time-ordered interaction - authentication flow, failover, backup window.
- **Flowchart:** a branching decision including its negative branches.
- **Timeline/roadmap:** sequenced phases with owners and gates.
- **State diagram:** the lifecycle of a document, certificate, device or ticket.
- **Screenshot:** one specific user-interface step, for the administrator audience.
Prose suits reasoning, judgement and caveats. It is the wrong tool for counts, sets and sequences.

## Figure discipline
- Every figure has a number, a caption, a source line (data source and retrieval date for graphs;
  "author's design" for designs), alt text, and at least one body sentence pointing at it ("see
  Figure 2"). A figure nothing refers to is a finding.
- One idea per figure. The caption states the conclusion ("Latency doubles above 400 users"), not
  just the subject ("Latency chart").
- Graphs: axes labelled with units, data source and date range stated; no truncated axis that
  exaggerates a difference; no dual axis without saying so.
- Tables: header row, units in the header, aligned numbers, source note, no merged cells (they break
  exports), at most 7 columns for rich-text targets.
- Colour is never the only carrier of meaning (must read in greyscale); exported text at least 12pt.

## Diagrams as code
- Keep diagrams as text sources (Mermaid, PlantUML, Graphviz) committed beside the rendered image, so
  they diff, review and re-render: `assets/figures/<doc-id>-<nn>.png` with the source next to it.
- ASCII art is acceptable in Markdown-only documents. It is not acceptable in a Word or PDF target:
  render it to an image.
- Record the render command (tool, version, command) with the figure.

## Screenshots
- Redact names, handles, e-mail addresses, tokens, internal hostnames and pricing before committing.
- Label with product, version and date; annotate the step being shown; keep the text legible.
- Check the licence for third-party material before shipping it.