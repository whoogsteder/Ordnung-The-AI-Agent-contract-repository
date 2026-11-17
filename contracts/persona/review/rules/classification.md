# Classification and distribution <!-- persona: module header -->
Applies: every document carries a label from the first draft. The full release checks apply when a
document is released or sent out. Review reports are documents for this module and carry the most
restrictive label of what they quote. Requires: base.md.

A label says who may read a document. It is one line in the header while drafting, and a gate only at
release.

## The ladder (most open to most restrictive)
- `Public` - approved for public release.
- `Client-shareable` - may be shared with a named client and its advisers.
- `Internal` - for the authoring organisation only. **The default for every draft.**
- `Restricted` - named recipients only.

Print one distribution sentence on page one and in every export footer, for example:
`Classification: Internal - intended for use by <org> only`, with `<org>`, `<client>` or the
recipient list filled in from the project.

Advisories and security notes also carry a TLP:2022 marking (`TLP:CLEAR`, `TLP:GREEN`, `TLP:AMBER`,
`TLP:AMBER+STRICT`, `TLP:RED`). A pre-patch advisory is at least `TLP:AMBER`.

## While drafting
- Default `Internal`. Ask once during the questioning session whether the set is meant to go wider. Do
  not block on the answer.
- Narrowing is free. Widening is recorded first (a decision record naming the new tier, recipient,
  basis, date and who decided), then applied.
- Derivatives (excerpts, summaries, exported figures) inherit the parent's label.
- Material narrower than `Internal` stays out of git unless the repository is declared private.
- Confidential material never goes into web searches or external tools (base.md, State & change history).

## At release or send-out
Before a document is released or sent:
1. **Label present** in the header, on page one and in every export page footer or banner.
2. **Content scan for the tier.** Every tier: no credentials, tokens, keys or personal id numbers.
   `Public`: no client names, internal hostnames or addresses, contract amounts, unreleased roadmap
   items, NDA material or personal data. Wider than one client: no other client's identifying
   material. Report: `Content scan for <tier>: clean`, or the hits.
3. **Basis recorded** for `Client-shareable` (contract clause, NDA, dated user statement) and the
   named recipients for `Restricted`.
4. **Distribution logged** in the register in `agent/REPO-MAP.md`:
   `document + version | recipient | date | channel | label`.

A label never authorises sending. Publishing, sending and uploading happen only when the user asks for
that action in the session.

## Third-party material
Copied code, figures, screenshots, quotations and logos get a `rights:` note in the source list. The
licence texts under `licenses/` apply to code a project ships, not to its documents. Ask once about an
export-control marker only when a document describes cryptography or surveillance-capable technology.
