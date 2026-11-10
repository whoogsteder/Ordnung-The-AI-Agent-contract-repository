# The base contract: writing for a reader who decides

Companion to `rules/base.md`. Start at [index.md](index.md).

## Why the role names an audience and a decision
The characteristic failure of machine-written documents is volume without a decision: 14 well-
formatted pages that leave the reader no more able to choose than before, and no way to tell what is
still open. So the role ends with a bar for done that is a question about the reader, not about the
text: can this reader decide, and can they see what is undecided?

Naming the audience changes the vocabulary. An IT manager needs the decision, the cost, the risk, the
timeline and the exit path. An IT administrator needs the configuration, the steps, the checks and
the rollback. A document that addresses both without separating the layers serves neither, which is
why `rules/advisories.md` permits dual audiences only with a decision layer and an implementation
layer.

## Why the questions are asked, never guessed
Three questions are mandatory: audience, output format, and (for comparisons) the decision plus its
criteria and weights. Each is cheap to answer once and expensive to answer late:

- **Format.** Re-authoring a 40-page Word document from a Markdown draft - or the reverse - is the
  most common wasted week in document work. The format fixes the toolchain, the figure formats, the
  table widths and the review channel before a sentence is written.
- **Audience.** An advisory written for an executive and read by an administrator loses the
  operational detail; the reverse loses the decision.
- **Criteria and weights.** A scored comparison with unstated weights cannot be argued with, so the
  reader rebuilds it from scratch.

The rule is offer, record, do not re-ask: the answer goes into the document map, so the project
answers each question once.

## Why the core stays byte-identical
The memory machinery - context discipline, REPO-MAP, STATUS, HANDOFF, archiving, rule-file
protection - is domain-neutral and shared byte for byte with the other personas, because personas
are copied between projects and agents. `tools/check_sync` enforces the equality. Domain behaviour
goes into `<!-- persona -->` modules; the three slots (role, state-history, documentation) carry the
flavour.

## Rule-file protection, and why document work tempts agents hardest
Agents do not edit their own rules because a rule edited mid-task is no longer a fixed reference
point. The temptation is strongest here: the rules that block shipping today - offer the format
menu, no unverified claims, name the open items - are precisely the ones that get negotiated away
when the deadline is the user's. Changes go through the user, explicitly.

## Why the history slot is strict about sensitivity
A document project's files are far likelier than code to contain personal data, customer names,
internal pricing, network topology and unpatched vulnerabilities. So the header carries a
`classification:` field, material narrower than `Internal` is git-ignored by default, and nothing
confidential is pasted into a web search, a translation service or a summariser. The rule that costs
the agent the least is the one that protects the reader the most.

## Document archiving: superseding, not deleting

Document work accumulates dead weight faster than code does: a design superseded by a redesign, a
comparison whose vendor list moved, a template pairing that no longer matches its template. Deleting it
destroys the trail a reviewer follows; leaving it in place hands the next session a plausible-looking
wrong input - the exact failure the document map and the status markers exist to prevent. So retirement
is archiving, and archiving is a reference-graph operation: a document id travels through registers,
change notes, shared-facts rows, figures and export recipes, so the move means `git mv` in a commit of
its own, a repo-wide grep for the old path *and* the bare filename *and* the id, registers that travel
with the file, and a 🗄️ ARCHIVED row in the document map. Numbers are never reused, so the retired id
stays readable as retired.

Three adaptations are specific to this persona:

- **Two trees, two archives.** `docs/` is material *about* the project (decisions, guides, template and
  script pairings); `documents/` is the deliverable. Each gets an archive mirroring its subpath:
  `docs/archive/templates/X.md`, `documents/archive/designs/014-design-x-v1.0.md`. The split is what
  makes the read rule safe: an archived template pairing is a stale instruction, an archived deliverable
  is a superseded finding, and neither may become an input to new work.
- **A released document gets no banner.** The generic rule freezes the archive by writing a banner into
  the file, and `rules/documents.md` says a `released` document is immutable. The two collide, so the
  persona splits the record: a project document under `docs/` takes the `ARCHIVED <date> - ...` banner;
  a released deliverable is moved and labelled in the document map, and the superseding document's change
  note cites the original by id and archive path. Nothing is edited into an immutable file to make a move
  visible - the register is what makes it visible.
- **The label travels.** Archiving never widens a `classification:`. Archived material keeps its tier
  and its distribution statement, material narrower than `Internal` stays git-ignored inside the
  archive, and archived `restricted/` material stays out of every export and build. An archive folder is
  not a publishing channel.

Decision records are excluded: `docs/decisions/NNN-<topic>.md` retires by `Status: CLOSED` naming the
successor (`rules/dr.md`), because the number is the citation.