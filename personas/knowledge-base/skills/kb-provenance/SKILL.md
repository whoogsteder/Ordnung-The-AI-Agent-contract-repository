---
name: kb-provenance
description: Provenance rules for anything entering or leaving a knowledge base — source, evidence and date on every item, items without evidence kept as drafts and never served, a citation on every retrieved result, shelf life and staleness caveats, superseding instead of restating, secrets and personal data excluded by the indexer, recorded model output labelled as a fixture, and git as the truth with the index as a rebuildable derivative. Use this whenever you write, edit or approve a knowledge item, serve or justify an answer from the knowledge base, decide whether a fact is still current, discuss an index rebuild or migration, or wonder whether something is knowledge or only a draft.
---

# Provenance

An item that cannot say where it came from is a guess with permanent storage: it will be cited by
every later answer and contradicted by none. Provenance is a schema requirement, not a field that
nice notes have.

## Every item carries it
- **Source** (where it came from), **evidence** (what shows it is true: command, environment, date,
  result) and **the date it was last true** — in the item itself, not in a sidecar nobody reads.
- No evidence → it is a **draft**: not indexed as knowledge, never served as an answer. Send it to
  the proposal area (`kb-capture`); do not soften it into a weaker note to get it in.
- The evidence is a command or a record, not an adjective. "Confirmed" with no command behind it is
  the same item with a hat on.

## Every answer carries a citation
- Source **plus the location within it** (path and heading, line, page or chunk id). A result with no
  citation did not come from the knowledge base — say so out loud rather than serving it.
- Never present a synthesised passage as a retrieved one. If the answer is your inference, label it
  as inference and name the items it stands on.

## Facts age
- Each claim type has a shelf life declared in configuration. An item older than its shelf life is
  served **with that caveat attached**, never silently.
- Supersede rather than restate: a new item names what it replaces, and the replaced item is retired
  by the project's archiving rule, not deleted. Duplication doubles the surface that can go stale.

## Never indexed
- Secrets, credentials, tokens and personal-data items — **even when a source document contains
  one**. Exclusion is enforced by the indexer and proved by a test (`kb-corpus`), never left to
  judgment at query time.
- Recorded model output used as a fixture (embeddings, scores, generated text) is labelled with the
  model, its version and the capture date, or marked synthetic. A score recorded from a different
  model certifies nothing about this one.

## The index is a derivative
- Information that exists only in the index is a defect, not a design choice. Everything the
  knowledge base knows must be rebuildable from committed files.
- Record the recipe with the index — embedding model and version, chunking version — because a
  derivative built by a different recipe is a different index (`kb-corpus`).
- The point of a disposable index: while a rebuild is always available, changing an embedding model
  is a routine reversible operation. When it is not, every model change becomes a risky migration
  and people stop making the change they should make.
