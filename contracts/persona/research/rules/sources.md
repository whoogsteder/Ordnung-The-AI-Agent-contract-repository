# Sources and evidence <!-- persona: module header -->
Applies: every fact the research records. Requires: base.md.

## Every fact has a source
- Each fact in the pack carries a source id, and each source id resolves to an entry in the source list:
  `S-NN | what it is | publisher | product and version covered | URL or location | retrieval date |
  type | file`.
- `type` is one of: `primary`, `reference-design`, `measurement`, `practitioner`, `vendor-claim`,
  `user`, `internal`.
- A statement with no source is either sourced or removed. Inferences are allowed, but they are
  written as conclusions ("so the S5248F-ON meets the 25G must-have"), with the facts they rest on, and
  never stored in the facts table as facts.

## Keep a copy
- Save each source that a load-bearing fact rests on under `sources/` as `S-NN_<YYYY-MM-DD>.<ext>`:
  the PDF, a saved page, or a text extract with the URL and retrieval date at the top. Links rot, and a
  reviewer must be able to check the fact without searching again.
- Quote only the passage that is needed, and record third-party rights where material will be reused
  in a document (`rules/classification.md`).

## Say what kind of evidence it is
- A vendor's statement about its own product is a vendor claim. An independent test is a measurement.
  Do not mix the two in one sentence.
- Practitioner reports are anecdotes until confirmed. Record how many independent reports there are, and
  how recent they are.
- Record the date the source applies to, not only the retrieval date. A 2021 compatibility list is not
  current because it was retrieved today.

## Confidentiality
- Confidential material (customer names, internal prices, unreleased roadmaps, configurations, live
  security findings) never goes into a web search, a translation service or any external tool. Search
  for the generic question ("48-port 25G switch with PFC"), not for the customer's situation.
- Material the user supplies keeps its classification inside the pack (`rules/classification.md`).
