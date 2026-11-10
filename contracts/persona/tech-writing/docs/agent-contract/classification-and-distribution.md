# Classification and distribution - why the ladder replaces the license picker

The persona used to open a new project by asking which LICENSE file to copy. For a code persona that
question is load-bearing: the license is how the artifact may be used. For a document set it is the
wrong question. A network design, a patch advisory and a vendor comparison are not published for
strangers to reuse; they are handed to named people - a client, a management board, an administrator
on a night shift. What governs them is not "what may anyone do with this file" but "who may read this
one, and on what basis". The question the persona must answer at boot is therefore confidentiality and
distribution, and the rules that follow from it live in `rules/classification.md`.

## The ladder, and why these four words

| Tier | Statement printed on page one | TLP:2022 equivalent | Typical object |
|---|---|---|---|
| `Public` | approved for public release, distribution is unlimited | `TLP:CLEAR` | published runbook, public advisory |
| `Client-shareable` | may be shared with a named client and its advisers | `TLP:AMBER` | design handed to the client it describes |
| `Internal` | intended for use by the authoring organisation only | `TLP:AMBER+STRICT` | working design, internal comparison |
| `Restricted` | named recipients only, no further distribution | `TLP:RED` | pre-patch advisory, live vulnerability detail |

Four tiers because that is the granularity a reader can act on: one tier per answer to "who is this
for", and one tier beyond the client for material whose recipients must be named. ISO/IEC 27002:2022
asks for an information-labeling scheme (control 5.12) applied in the environments where information
is handled (5.13), with confidentiality and integrity marked in agreements for information shared
outside the organisation (5.10); a ladder of named tiers with one canonical sentence per tier is that
scheme in the shape a document author can apply on page one.

The statements are canonical and printed verbatim, borrowed in shape from the US distribution
statements ("distribution is unlimited", "distribution authorized only beyond the Department of...").
A canonical sentence is checkable: the verification pass can look for the exact words, and a reader who
receives a printout can still see the label. A tier name alone is not checkable, and a free-form
sentence per document is not comparable.

Advisories and security notes carry the FIRST TLP:2022 marking as well, because their recipients are
CSIRTs and Managed Service Providers who read TLP, not an internal company scheme. TLP is chosen over
MLS (the deprecated predecessor), over ISAN (a national scheme), over the DIN SPEC 16454
"VS-NfD"/"NUR FUER DEN GEBRAUCH" labels (German public-administration specific), and over
`SENSITIVE` (the TLP:2024 proposal, not a ratified standard). The mapping in the module is written as
a convention: it is how this persona's tiers translate for a security recipient, not a claim that the
schemes are equivalent.

## Default narrow, widen deliberately: record before the act

`Internal` is the default for a draft, and widening towards `Public` is recorded **before** the label
is applied. The order is the deliberate heart of the module.

- **Default narrow** is the only safe default. A document that starts `Internal` and is widened leaves
  two records; a document that starts `Public` and turns out to name a client leaves a leak and no
  trail.
- **Record before the act** keeps the trail honest. A record written after the label is applied is a
  justification; written before, it is a decision. So the DR naming the new tier, the recipient and its
  basis, and what the content scan checked, exists before the header line changes.
- **No approval gate.** The persona does not route the widening to a human and wait. The user of this
  contract *is* the accountable author - an IT designer or administrator with the standing to decide
  what their own document may do. An approval step in an agent contract is a step that gets skipped
  under time pressure, and a skipped gate leaves nothing behind. The trust model is complete records
  rather than approvals: the author owns the decision, the record is the accountability, and the
  verification pass calls a widening with no record a finding. Narrowing needs no record at all - a

Two boundaries keep this from reading as permission to send things. First, a label never authorises
transmission: base.md keeps publishing, sending and uploading as actions the user asked for. The label
says who may receive a document once it goes; it never decides that it goes. Second, an unclear
audience is an open item, never a missing label: `Internal` is always available as the safe answer, so
the open-items register tracks "who is this for, at release?" instead of blocking work on a label
question - which is why the license question it replaces was a boot blocker and this one is not.

## Where the label must appear, and the three named leaks

The label goes on the document and into every export: header line one, a footer on every page of rich
text and PDF, a banner at the top of Markdown and HTML. Three leaks get their own rules because they
are how document sets actually fail:

- **Derivatives inherit.** An excerpt, a slide cut-out, an executive summary, a figure exported on its
  own, and a quotation landing inside a comparison cell all carry the parent's tier. The excerpt is the
  leak: nobody re-labels a slide.
- **The set takes the most restrictive label.** A twelve-document set is `Client-shareable` if one
  chapter is, which is why the label is a register entry and not a per-file afterthought.
- **Memory inherits.** `agent/REPO-MAP.md` and `agent/STATUS.md` carry the set's classification, and a
  `Restricted` set keeps facts out of them: titles and pointers only. Registers are written to be read
  by the next agent session, and in a hosted agent that context is shared infrastructure - a register
  that quotes the live vulnerability it is tracking has already leaked it. Where the memory files
  cannot carry the tier, saying so is a hard stop, not a workaround.

The distribution register (`DIST-NN | document + version | recipient | date | channel | label`) exists
for the question asked after an incident: who has this? Without it, "we sent it to the client" is a
memory. With it, it is a query. The content scan runs before a widening and before every release, and
reports as `Content scan for <tier>: clean` - the same reporting discipline as the ambiguity audit,
because "I checked" that is not reportable is not a check.

## What remains of licensing, and what is deliberately absent

Licensing is not deleted, it is demoted to where it applies. Third-party material inside a document -
a code snippet, a vendor figure, a screenshot, a quoted table - carries rights and attribution
obligations, and those obligations travel at every tier, so they get a `rights:` entry in the source
register. The license picker under `licenses/` stays available for the code a project ships (generator
scripts, export tooling): documents are not licensed, code is. That is why the directory is kept
rather than removed - the personas that ship code need it, and this one ships scripts.

Two mechanisms are considered and left out on purpose:

- **Human approval as a gate**, for the reason given above: unenforceable in a prompt-driven contract,
  and it leaves no trace when skipped. The record-before-act rule is the enforceable substitute.
- **Per-document licenses** (the old question of what a recipient may do with a document). The tier
  answers who may read it; adding a license per document would multiply the surface without protecting
  anything the tier does not already cover, so it is not part of the contract.

Export control is the one wider question the module asks rather than answers: it is offered once, and
only when a document describes cryptography, interception or surveillance-capable technology, because a
marker of that kind is a legal statement the author - not the agent - must make.

  stricter label harms nobody.
- `Public` is the one tier treated as permanent, because a public document cannot be unpublished: the
  record is signed by the act of publishing, so write it first.
