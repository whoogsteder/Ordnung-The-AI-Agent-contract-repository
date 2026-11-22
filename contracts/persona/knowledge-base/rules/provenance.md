# Provenance <!-- persona -->
Applies: always. Requires: base.md.

- Every item that enters the knowledge base carries where it came from (source), what shows it is
  true (evidence: command, environment, date, result), and when it was last true.
- An item without evidence is a draft. It is not indexed as knowledge and must not be served as an
  answer.
- Retrieval always returns citations: the source plus the location within it. A result with no
  citation did not come from the knowledge base.
- Facts age. A retrieved item whose date is older than its claim's shelf life is presented with
  that caveat, not silently.
- Never index a secret, credential or personal-data item, even when a source document contains one.
  Exclusion is enforced by the indexer, not left to judgment at query time.
- Recorded model output used as a fixture is labelled with the model, version and date, or marked
  synthetic.
