# DR-004: PROJECT.md lists only open decisions

## Context
The operator asked whether storing every decision in PROJECT.md would bloat the context of large
projects (2026-11-26). It would: the file is read in full at every resume.

## Decision
1. PROJECT.md lists only PROPOSED decisions, because those gate work.
2. ACCEPTED decisions live in their records and in the REPO-MAP documentation index, where an
   agent finds them by topic when the work touches them.
3. PROJECT.md does not replace decision records. Most entries pass through it and leave it: once
   accepted, answered, met or finished.
4. The decision scheme (prefix and directory) is set per project in `agent/ordnung.toml`. The
   default is DR in `docs/decisions`; the iac persona uses ADR in `docs/adr`. The checker rejects
   an entry under Decisions that uses any other ID.

## Consequences
- Enforced by: `tools/ordnung_check` (cap; Decisions IDs) and
  `tests/test_tools.py::test_decisions_list_rejects_ids_without_a_record_scheme`.
- Open gap, not yet decided: met or dropped REQs can linger in PROJECT.md (see
  docs/field-tests/feedback.md).

## Status
ACCEPTED (2026-11-26, operator)
