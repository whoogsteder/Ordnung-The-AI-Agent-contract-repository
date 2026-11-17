# Decision Records <!-- slot: decision-records -->
Applies: when the project records decisions in `docs/decisions/`. Requires: base.md.

A decision record captures a choice that outlives one research topic, so later research does not reopen
it by accident.

## When to write one
- Standing constraints across topics: the allowed vendors or suppliers, regions, licensing models.
- Source policy: sources to prefer or exclude, whether web search is allowed, what counts as
  confidential.
- An assumption the user signs off as standing policy.
- Every widening of a classification, written before the wider label is applied
  (`rules/classification.md`).
A conclusion of one research topic belongs in its pack, not in a record.

## Shape
- Location: `docs/decisions/NNN-<topic>.md`, zero-padded.
- Sections: Context / Decision / Consequences / Status. Keep it under a page.
- Status: `PROPOSED`, `ACCEPTED` (safe to build on), `CLOSED` (rejected or superseded; say by what).

## Rules
- A pack that depends on a `PROPOSED` record may be drafted, but it says so in "Limits" and is not
  handed over as final.
- Research that contradicts an `ACCEPTED` record is reported to the user. Do not silently follow either
  one. Superseding the record is the user's decision.
- Changing an accepted decision triggers a re-check of every pack that relies on it.
