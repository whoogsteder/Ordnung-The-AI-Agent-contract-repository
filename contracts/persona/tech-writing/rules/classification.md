# Classification and distribution <!-- persona: module header -->
Applies: every document, from first draft to last export, and every figure and export derived from it.
Requires: base.md.

Documents carry a classification and a distribution statement, not a license. The label is what makes
a document safe to hand over: it says who may read it, and on what basis.

## The ladder (most open to most restrictive)
- `Public` - `Classification: Public -- approved for public release, distribution is unlimited`
- `Client-shareable` - `Classification: Client-shareable -- may be shared with <client> and its
  advisers; not for wider distribution`
- `Internal` - `Classification: Internal -- intended for use by <org> only`
- `Restricted` - `Classification: Restricted -- named recipients only (<list>); no further
  distribution`

The tier name is the vocabulary; the sentence after it is the distribution statement and is printed
verbatim in the document - one canonical sentence on page one, the pattern taken from the US
distribution statements. The words `<client>` and `<org>` are filled from the project, never left as
placeholders.

Advisories, security notes and patch guidance add the traffic-light marking from FIRST TLP:2022:
`TLP:CLEAR`, `TLP:GREEN`, `TLP:AMBER`, `TLP:AMBER+STRICT`, `TLP:RED`. The ladder maps onto it as
`Public` = CLEAR, `Client-shareable` = AMBER, `Internal` = AMBER+STRICT, `Restricted` = RED. Where a
document is handed to a CSIRT-style recipient, the TLP line is the one the recipient reads.

## Default and direction of travel
- A draft is `Internal`. `Internal` is the safe default: a document starts narrow and is widened on
  purpose, never by accident.
- Widening (towards `Public`) is recorded **before** it is applied: a decision record naming the new
  tier, the recipient and its basis, what the content scan checked, the date, and who widened it.
  Then apply the label. There is no approval step - the author owns the decision, and the record is
  the accountability.
- Narrowing (towards `Restricted`) is free: header line only, no record.
- The header records the move: `label: Internal -> Client-shareable (DR-07, 2026-11-09)`.

## Header fields
`classification`, `distribution` (the canonical sentence), `distribution-basis` (contract clause, NDA
dated, user statement dated, or `-`), `label-review` (date), and for advisories `tlp:`. The block is
specified in `rules/documents.md`.

## Rules
- One label per document. A document set carries the most restrictive label of any of its members; a
  document may sit lower only when it demonstrably contains nothing above it.
- Derivatives inherit the parent's tier: excerpts, slide cut-outs, executive summaries, standalone
  figure exports, and quotations landing inside a comparison cell. Record the parent and its tier in
  the source register.
- The label travels into every export: header line one plus a footer on every page for rich text and
  PDF, a banner at the top for Markdown and HTML. The export round-trip of `rules/output_formats.md`
  checks that the label arrived.
- `Client-shareable` names the client and records a basis; `Restricted` names the recipients. A
  missing basis is an open item (`OQ-NNN`), never a silent assumption, and never a block.
- Releasing a document (`released`) requires: an explicit label, a clean content scan for that tier,
  and - where the label was widened - the record. `Public` is permanent, so write the record first.
- `label-review` expiry: reconfirm or narrow, and record it. A released document is immutable, so
  declassification produces a new revision; it never edits a released document.
- Distribution register in `agent/REPO-MAP.md`:
  `DIST-NN | document + version | recipient | date | channel | label`
  Re-issuing a document to a recipient outside that register is a leak; check the register before the
  send, not after.
- Memory inherits the set's tier: `agent/REPO-MAP.md` and `agent/STATUS.md` carry a `classification:`
  field. For a `Restricted` set the registers hold titles and pointers only, never facts. If the
  memory files cannot carry that tier, say so - that is a hard stop, not a workaround.
- A label never authorises transmission. Publishing, sending, uploading and sharing stay actions the
  user asked for (base.md, State & change history). The label says who may receive a document once it
  goes; it never decides that it goes.

## Content scan (what each tier forbids)
Run before widening, and before every release, over the whole document including figures, tables and
captions:
- Every tier: credentials, tokens, private keys, personal ID numbers - never in a document, never in
  memory files (base.md).
- `Public`: client names, internal hostnames and IP addresses, contract amounts, salaries, unreleased
  roadmap items, NDA'd vendor material, personal data.
- Anything wider than a single client's tier: that client's identifying material.
Report it with the release: `Content scan for <tier>: clean` or the list of hits.

## Third-party rights (the remnant of licensing)
Documents are not licensed; third-party material inside them is. Every copied code snippet, figure,
screenshot, quotation or logo gets a `rights:` entry in the source register (`MIT, (c) <author>`,
`own screenshot`, `NDA'd vendor document, quoted with permission`). Attribution obligations travel
with the document at every tier. The license picker under `licenses/` applies to code a project ships,
never to its documents.

## Export control (asked once, never applied silently)
Ask once, and only when a document describes cryptography, interception or surveillance-capable
technology, whether it needs an export-control marker. Record the answer in the header and the
document map. Never apply a marker silently, and never assume one is needed.

## Enforcement
- A document header without `classification:` is a finding.
- Widening without a record is a finding: write the record, then the label.
- The verification pass (`rules/verification.md`) checks label presence, label consistency across the
  set, the label inside every export, and the content scan for the release tier.
- Naming a file `-INTERNAL` or `-CLIENT` is an optional set-level convenience, and never the only
  marker: the label must be readable inside the document.
