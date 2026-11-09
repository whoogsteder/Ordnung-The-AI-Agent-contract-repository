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
`sensitivity:` field, material above `internal` is git-ignored by default, and nothing confidential
is pasted into a web search, a translation service or a summariser. The rule that costs the agent
the least is the one that protects the reader the most.