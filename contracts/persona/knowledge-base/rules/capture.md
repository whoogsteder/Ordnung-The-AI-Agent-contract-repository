# Capture <!-- persona -->
Applies: when knowledge is proposed or approved. Requires: base.md, provenance.md.

- Propose, then approve. An agent writes drafts into the proposal area and never commits to the
  curated store. A human moves a proposal into the curated store or rejects it.
- A proposal states the claim, the evidence, the source, the confidence, and what it supersedes.
  A lint check rejects a proposal missing a required field — evidence is the gate, not prose
  quality.
- Worth capturing: a verified fix that cost real time to find; a decision that refines or
  contradicts an existing document; a dead end worth not retrying; a fact a future session would
  otherwise rediscover the hard way.
- Not worth capturing: what the source documents already state. Duplication is rot, not coverage.
- Supersede rather than duplicate: a new note names the note it replaces, and the replaced note is
  retired by the project's archiving rule, not deleted.
- Triggers are written down, so capture is a habit the contract carries rather than a mood the
  agent happens to be in.

## Project layout (additive, when the project keeps a curated store)

```
[project root]/
├── knowledge/
│   ├── proposals/     # Agent-drafted items awaiting approval — never indexed as knowledge
│   └── notes/         # Approved items — the only curated path that counts as current truth
```

The split is the control: writing to `proposals/` is ordinary agent work, writing to `notes/` is
an approval event. An agent that cannot tell which one it is about to write to has not read this
module.
