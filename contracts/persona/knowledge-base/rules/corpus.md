# Corpus <!-- persona -->
Applies: when indexing, or changing what gets indexed. Requires: base.md.

- Inclusion is declared in configuration — source roots, document types, exclusions. An agent
  never decides at runtime what belongs in the corpus.
- The indexer excludes by construction: frozen/archived material, ignored paths, and anything the
  source project marks as not current. A project that forbids reading archived material is
  honoured by never indexing it, so a search cannot smuggle it back into a caller's context.
- Re-indexing is idempotent. Content-hashed, so unchanged content is never re-embedded and a second
  run changes nothing.
- Chunk boundaries are a documented, versioned choice. Changing them changes the index identity:
  rebuild and evaluate, do not patch a live index piecemeal.
- The index records the recipe that built it (embedding model and version, chunking version).
  Writing vectors from a different recipe into the same index is refused, not warned about.
- Exclusion is tested. A corpus test proves an excluded document cannot be retrieved, because an
  exclusion nobody exercises silently stops working.
