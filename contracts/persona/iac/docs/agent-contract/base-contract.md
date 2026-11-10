# The base contract: why it is shaped this way

Companion to `rules/base.md`. Start at [index.md](index.md). This page explains the design
decisions behind the always-on rules, for people maintaining the contract or wondering why an
agent is behaving this way.

## The one problem this contract solves

Agents lose context: sessions end, windows fill, models change mid-project. Everything the
contract does is a variation of one idea — **durable state lives in files, not in conversation
history**. REPO-MAP and STATUS are the agent's memory; the rules are its personality; the
conversation is disposable.

## Context discipline: why "do not explore at session start"

The natural agent instinct — walk the repo first to "understand the project" — is the main
source of context bloat: it spends the window on files this task will never touch, and every
token spent there is a token less for actual work. The contract inverts the default: the
REPO-MAP index answers "where do things live", so orientation costs one small file read, and
anything unknown mid-task gets *one targeted* lookup. The documentation status markers
(✅/🟡/📋) exist for the same reason on the `docs/` side: five plausible-looking design docs
about unbuilt features are five invitations to implement the wrong thing.

## Two memory files, not one

REPO-MAP is **stable** (what exists and where); STATUS is **volatile** (what is happening
now). Merging them means every session-state update rewrites the index and every index edit
pollutes the handoff — and it drags the agent into re-reading stale task noise. Separating
them keeps both small enough to read at boot without cost.

## HANDOFF: a schema, not prose

A free-form "notes for next time" block degrades into narrative an agent half-reads. The
fixed schema (`phase / status / next_action / files / notes`) forces exactly one answerable
question — *what should the next session do first?* — and makes the handoff checkable: the
agent echoes `next_action` back, so a missing or vague handoff fails visibly at boot instead
of silently misdirecting the session.

## Update triggers and frequency guards: why rules repeat themselves

"You should keep STATUS.md current" fails because recency wins: after ten tool calls, the
instruction that fired early is far away and the agent "forgets". The contract therefore
attaches updates to **events** (file created, command or test run, topic switch) plus a
**frequency guard** (5+ tool calls since last update → update now). Redundant by design: an
event trigger missed in the noise gets caught by the counter.

## Why the triggers are spelled out mechanically

Both halves of that redundancy failed in practice, in a long debugging session on a Go project.
The event half starved because the agent read the list as *achievements*: throwaway probe files
and failing test runs did not feel like "a file created" or "a command verified", so no trigger
seemed owed until a milestone — and a milestone never arrives in a session that ends stuck. The
counter half starved because nothing was counted: under context pressure the queue-depth check
lost to "one more probe", and an agent arriving through a compacted summary inherited a stale
STATUS it treated as somebody else's debt.

The rule text now removes the judgment instead of repeating the exhortation: any test/build/check
run is a verified command, pass or fail; any file created or rewritten counts, probes included;
milestones are explicitly not the unit of work. Two additions close the other holes — a resume
rule (stale STATUS is your first task, never inherited debt) and a read-back rule (re-read
`rules/base.md` on topic switch, on conflict, and on every resume), because reading the contract
once at boot governs the calm start and not the pressurized middle.

The counter also became observable: the HANDOFF schema carries `last_update`, so an agent that
lost count can compare it against STATUS.md's modification date with one cheap command instead of
relying on memory. Deliberately **not** shipped is a hook or checker script in this repository: a
file under `tools/` cannot travel with a drop-in persona folder, which would make enforcement
unshippable. The contract ships the *instruction* and each project's bootstrap offers to have the
agent author a probe that fits its own tooling — same reasoning bootstrap already applies to
project skeletons: generated scaffolding reflects the generator's assumptions, not the project's.

## Archiving: forward-only STATUS

An agent reads its whole STATUS at boot. If that file carries three phases of completed work,
the session starts with stale context it cannot distinguish from live context — the exact
staleness problem `verification.md` describes for docs, one level up. Hence: STATUS is
forward-looking, `STATUS.archive.md` is append-only history, and the archive trigger moves
`[x]` items out *in the same response* that marks them done. The 40-line size guard is the
backstop when triggers are missed.

## Document archiving: a reference-graph operation

The STATUS archive has a twin problem one level down. A design doc quietly `mv`-ed into
`docs/archive/` leaves every citation of its old path dangling, and leaves a workflow step that tells
the next agent to "record your decision in `docs/design/x.md`" writing into frozen history. A move
invalidates a reference graph, so the contract treats archiving as a graph operation: `git mv` in a
commit of its own (rename detection keeps `git log --follow`), a banner naming what supersedes it, a
repo-wide `git grep` for the old path *and* the bare filename, and index rows that travel with the
file.

Three decisions in that rule are deliberate:

- **The operator decides; the agent proposes.** Archiving changes what future sessions read, which is a
  change of behaviour — the same reason agents may not edit their own rules.
- **Archive is not a delete.** An agent that wants a secret, a wrong fact or a retired setting gone is
  answered by a normal commit that removes it and says why. Routing that through `docs/archive/` keeps
  the content in the repository while making it harder to see.
- **The archive is never read at task time.** Same exclusion as `STATUS.archive.md` and
  `docs/agent-contract/`: a superseded design doc is a plausible-looking wrong answer, exactly the
  failure the documentation status markers exist to prevent. Hence a fourth REPO-MAP marker,
  🗄️ ARCHIVED, so the index can name the file without inviting a read.

In this persona the archive candidates are `docs/architecture/`, `docs/guides/` and `docs/runbooks/`.
ADRs are excluded on purpose: `ADR-NNN` *is* the citation and the sequence is the index, so a moved ADR
breaks every reference to it and the docs-integrity test's index check. Retirement there is
`Status: CLOSED` naming the successor (`rules/adr.md`).

## Rule-file protection: why agents may not edit the rules

Left unsupervised, an agent that hits a conflicting rule will "fix" the rule — silently
changing its own contract and every future session's behaviour. The Rule-files section makes
rules read-only to agents and routes the energy through the human: report the conflict, ask,
never work around it. It pairs with the genericity rule (no project-specific facts in rules):
the moment one project's paths or record numbers leak into a shared rule, the contract stops
being reusable — and edits made under session pressure are exactly how that happens.

## "Approval of one change does not cover others"

Agents generalise approvals: approving one rules edit reads as license to tidy the whole
directory. The contract states the opposite default explicitly because the failure is
invisible — the extra edits look like helpfulness until the next session boots under a
silently changed contract.

## Documentation and versioning in one line each

"No docs = not done" exists because agents reliably stop at working code; the paired-docs
convention in the tool modules makes documentation a completion criterion rather than an
afterthought. SemVer + short-lived branches exist so that "the agent committed directly to
main" is always a visible contract violation — the branch discipline doubles as an audit
mechanism for agent work.
