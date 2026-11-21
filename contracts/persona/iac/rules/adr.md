# ADRs (Architecture Decision Records) <!-- slot: decision-records -->
Applies: when the project records decisions in `docs/adr/`. Requires: base.md.

- Location: `docs/adr/NNN-<topic>.md` (zero-padded, e.g. `001-model-gateway-litellm.md`). This is the
  only place ADRs live: `docs/architecture/` holds design write-ups and links to the ADRs that record
  its choices, it never contains them.
- Each record has: Context / Decision / Consequences / Status.
- Statuses:
  - `PROPOSED` — open, not yet decided.
  - `ACCEPTED` — decided; safe to build on.
  - `CLOSED` — rejected or superseded (state why).

## Rule
- A record may stay `PROPOSED` while work proceeds, as long as the current task does not depend on it.
- If a task depends on a `PROPOSED` record: drive it to a decision (`ACCEPTED`/`CLOSED`) first, or halt that work until it is resolved. Never implement against an undecided decision.
- Cite decisions as `ADR-NNN decision N`; both must exist. A `CLOSED` ADR is cited only
  by other ADRs and history files.
- An architecture document in `docs/architecture/` describes the design and points at the records that
  decided it: cite `ADR-NNN decision N` and link the file (`../adr/NNN-<topic>.md`). It never restates
  or holds a decision — the ADR is the record, so a design doc that copies one is a second source of
  truth that goes stale on the next decision.

## Enforcement (if verification.md is present)
- Consequences list `- Enforced by: \`path\`` or `` `path::test_name` `` plus what it checks,
  or `- Enforced by (planned, <task-id>): <what>` while the subject does not exist.
- An `ACCEPTED` ADR needs at least one concrete entry. ADRs without one go in a debt
  list in the docs-integrity test; the list may only shrink.
- The docs-integrity test also checks that entries resolve and that the index status
  of each ADR matches its Status line.
