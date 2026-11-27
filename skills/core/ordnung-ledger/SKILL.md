---
name: ordnung-ledger
description: Maintains the strategic memory of an Ordnung-contract project — agent/PROJECT.md (standing requirements, decision index, questions waiting on the user, tracks), decision records (DR-NNN in docs/decisions/ by default, or the project's own scheme such as ADR-NNN in docs/adr/), and the file index agent/REPO-MAP.md. Use this whenever the user states a requirement or preference that should hold beyond the current task, a design or tooling decision is made or needs making, a question only the user can answer comes up, a task finishes or a new one is queued, the user asks about project direction or "what's left", or files are created, moved or deleted. Also use it when a checkpoint finds a note that would matter after the current task closes.
---

# Ledger

The tactical layer (STATUS.md) answers "what am I doing?". The ledger answers "what must
stay true while I do it, and what comes next?" It is the reason an agent deep in one task does
not silently break a requirement agreed three tasks ago.

PROJECT.md is read in full at every resume, so it stays small: **one line per entry, detail
behind a link.** Size cap 80 lines — when it is reached, the fix is to move detail out to
`docs/`, never to drop an active entry.

## Entries

| Section | ID | One line holds | Detail lives in |
|---|---|---|---|
| Standing requirements | `REQ-NN` | requirement — source (who, date) — active/met/dropped | `docs/requirements/` when longer than a line |
| Decisions | `DR-NNN`, or the project's prefix | **open decisions only**: decision — PROPOSED — what it gates | `<dir>/NNN-<topic>.md` |
| Waiting on the user | `Q-NN` | question — options — what it blocks — since date | the question itself; ask it in chat too |
| Tracks | — | strand of work — state — task range — link | `docs/design/` |

**Why only the open ones:** PROJECT.md is read in full at every resume, so each line costs
context in every session. An ACCEPTED decision is needed only when work touches its subject, and
then you read that record. So it belongs in the decision directory and in the REPO-MAP
documentation index, with a status marker, where an agent finds it by topic. A PROPOSED decision
is different: it gates work (nothing that depends on it is claimable), so it must be in view at
every resume. When a record is accepted, remove its line here in the same change, and update its
REPO-MAP marker.

The open tasks themselves live on the board (`agent/TASKS.md`, `ordnung-board`), never in
PROJECT.md.

**The decision scheme is set once per project, in `agent/ordnung.toml`:**
```
[decisions]
prefix = "DR"
dir = "docs/decisions"
```
The default is DR in `docs/decisions`; an IaC project typically uses ADR in `docs/adr`. Use
exactly that prefix. Never invent another one (`D-01`, `DEC-1`): the checker rejects an entry
under Decisions that has no record behind it.

IDs are never reused. A dropped requirement stays with `dropped` and a reason until the next
review, so nobody re-adds it unknowingly.

## When the user says something durable

"From now on…", "always…", "never…", "we decided…", a preference about the deliverable, a
correction of your approach that applies beyond this step → add or update a `REQ-NN` in the same
response, citing the user and the date. Do not paraphrase it into a weaker form.

## Decision records

Use a DR for choices that outlive a task (technology, data layout, interfaces, security stance).

- File: `<dir>/NNN-<topic>.md` with **Context / Decision / Consequences / Status**. Cite a
  numbered decision inside a record as `<prefix>-NNN decision N` (short form: `dN`).
- Status: `PROPOSED` (open), `ACCEPTED` (safe to build on), `CLOSED` (rejected or superseded,
  say why and by what).
- Consequences name how the decision is kept true: a test, a pin, a config line — or
  `Enforced by (planned, <task>): <what>`. An ACCEPTED record without one is debt.
- Work that *depends* on a PROPOSED record stops until it is decided. Raise it as a `Q-NN`.
- Changing an ACCEPTED decision changes its enforcement and everything citing it in the same
  change.

## Waiting on the user

When the next step is the user's call, write the `Q-NN` *before* asking in chat. The chat
question can be lost to a compaction or a closed window; the ledger entry cannot. Remove the
entry when answered, recording the answer where it belongs (a REQ, a DR, or the task).

## REPO-MAP

`agent/REPO-MAP.md` says where things live, so reads can be targeted instead of searches.
- Update it in the same change that adds, moves or deletes a file another agent would need to
  know about. Leave out build output, caches and anything git-ignored.
- Cap 120 lines. Past that, split an area into `agent/maps/<area>.md` and leave one line in
  the top map saying when to read it.
- Documentation entries carry a status marker: ✅ IMPLEMENTED, 🟡 PARTIAL, 📋 PLANNED,
  🗄️ ARCHIVED. Read PLANNED only when working on that design; never read ARCHIVED.

## Review

When the board's NEXT runs dry, or the user asks about direction: walk PROJECT.md top to bottom,
mark met requirements, close stale questions with the user, update `last_reviewed`.
