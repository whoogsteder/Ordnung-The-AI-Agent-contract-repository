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
attaches updates to **events** (file created, command verified, topic switch) plus a
**frequency guard** (5+ tool calls since last update → update now). Redundant by design: an
event trigger missed in the noise gets caught by the counter.

## Archiving: forward-only STATUS

An agent reads its whole STATUS at boot. If that file carries three phases of completed work,
the session starts with stale context it cannot distinguish from live context — the exact
staleness problem `verification.md` describes for docs, one level up. Hence: STATUS is
forward-looking, `STATUS.archive.md` is append-only history, and the archive trigger moves
`[x]` items out *in the same response* that marks them done. The 40-line size guard is the
backstop when triggers are missed.

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
