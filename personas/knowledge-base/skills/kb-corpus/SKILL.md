---
name: kb-corpus
description: Rules for what the corpus contains and how an index is built — inclusion declared in configuration (roots, document types, exclusions), exclusion enforced by construction and proved by a test, idempotent content-hashed re-indexing, chunk boundaries as a documented versioned choice, the build recipe recorded with the index and mismatched vectors refused rather than warned about, and rebuild-then-switch for any recipe change. Use this whenever you index or re-index, change what gets indexed, change chunking or an embedding model, build, migrate or rebuild an index, or when a search returns material that should have been excluded.
---

# Corpus and index builds

What is in the corpus is a decision with a diff, not a runtime opinion. A knowledge base is a very
efficient way to break a project's own rules by accident: index everything, and the superseded
design comes back into a caller's context wearing the costume of a search result.

## Inclusion is configuration
- Source roots, document types and exclusions are declared in configuration. An agent never decides
  at runtime what belongs in the corpus.
- Ignore files are honoured: an ignored path is out of the corpus even when it is on disk.
- A request for data outside the declared roots is a configuration change the owner approves
  (`kb-scope`), not something to widen at runtime.

## Exclusion by construction
- The indexer never reads excluded paths: frozen or archived material, ignored paths, and anything
  the source project marks as not current. Asking the query layer, or the agent, to filter it out
  depends on every future caller remembering, which is not a guarantee.
- **Test the exclusion.** A corpus test asserts that an excluded document cannot be retrieved. An
  exclusion nobody exercises silently stops working.

## Builds are idempotent
- Content-hash each chunk, so unchanged content is never re-embedded and a second run changes
  nothing. Prove it: run the build twice and the second reports zero writes (`kb-resource-discipline`).

## The recipe is part of the index
- The index records the recipe that built it: embedding model and version, chunking version.
- Writing vectors from a different recipe into the same index is **refused, not warned about**. Two
  embedding models of the same dimension produce shape-compatible, semantically unrelated vectors;
  cosine similarity still returns a number, and that number looks like a score. A warning is a
  message nobody reads at 2 a.m.; a refusal is a bug report with the cause in the title.
- Chunk boundaries are a documented, versioned choice. Changing them changes the index identity:
  rebuild and evaluate (`kb-eval`); never patch a live index piecemeal.

## Changing a recipe
1. Build the new index alongside the old one, never over it.
2. Run the golden question set against it and commit the report (`kb-eval`).
3. Switch by pointer or configuration, so the switch is one reversible step.
4. Drop the old index once the owner has given the go for that change (kernel rule 13).

## Layout
```
config            # roots, document types, exclusions, chunking version
index store       # a derivative: rebuildable, disposable, carries its recipe
```
