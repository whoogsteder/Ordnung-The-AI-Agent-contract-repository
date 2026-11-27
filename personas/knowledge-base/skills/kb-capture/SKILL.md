---
name: kb-capture
description: The propose-then-approve path for knowledge the agent discovers — the proposals area versus the curated store as the approval control, a proposal's required fields (claim, evidence, source, confidence, supersedes) rejected by a lint check, what is and is not worth capturing, superseding instead of duplicating, the written triggers that make capture a habit rather than a mood, and the end-of-task question that catches what a session learned. Use this whenever knowledge is proposed, approved or rejected, after a hard-won fix or a dead end, when you learn something a later session would otherwise rediscover, and before writing anywhere near the curated store.
---

# Capture

An agent is good at writing a confident summary of what it just did, and that summary is exactly the
kind of item that poisons a knowledge base: plausible, unsourced, and permanently available to every
later session. Bad code fails loudly; a bad memory item silently shapes every answer after it. So
capture is propose-then-approve — code review's reasoning, applied to memory.

## The split is the control
```
knowledge/proposals/     # agent-drafted items awaiting approval — never indexed as knowledge
knowledge/notes/         # approved items — the only curated path that counts as current truth
```
- An agent writes drafts into the proposal area and **never commits to the curated store**. A human
  moves a proposal into the curated store, or rejects it.
- Silence is not approval. Neither is "the tests pass".
- If you cannot say which of the two you are about to write to, you have not read this skill.

## A proposal states
- The **claim**, the **evidence**, the **source**, the **confidence**, and **what it supersedes**
  (`kb-provenance`).
- A lint check rejects a proposal missing a required field. Evidence is the gate, not prose quality:
  a well-written unsourced item is exactly what the check exists for.

## Worth capturing
- A verified fix that cost real time to find.
- A decision that refines or contradicts an existing document.
- A dead end worth not retrying, with what was tried.
- A fact a future session would otherwise rediscover the hard way.

## Not worth capturing
- What the source documents already state. Duplication is rot, not coverage: it doubles the surface
  that can go stale while looking like coverage.
- Anything you cannot cite. That is a draft, and it stays one.
- Project state that belongs in `agent/PROJECT.md` or a decision record, not in the corpus
  (`ordnung-ledger`).

## Supersede, don't restate
A new note names the note it replaces; the replaced note is retired by the project's archiving rule,
not deleted. Two notes on one subject is two chances to be stale.

## Triggers are written down
Capture is a habit the contract carries, not a mood the agent happens to be in. The project declares
its triggers — in configuration or `agent/PROJECT.md` — for example: a fix that cost more than the
declared threshold, a contradiction found between two sources, a dead end, an owner decision that
narrows a requirement. Add a trigger when you notice a class of learning that keeps going missing.
- **End of task, ask once:** what did this session learn that no document says? Propose it, or write
  "nothing" and mean it.
