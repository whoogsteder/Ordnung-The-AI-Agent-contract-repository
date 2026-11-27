---
name: gh-verification
description: Evidence and testing rules for a game-hosting project — what counts as proof that a container or server works, the cheapest-first test ladder (compose lint, throwaway bring-up, ready-state logs, external query, restore drill), test hygiene, docs-integrity checks, and trusting server-produced artifacts over vendor docs. Use this before writing "works", "verified" or "fixed", when writing or changing tests, when deciding how far to test a change, when adopting an upstream image or setting change, and when sources about a game server disagree.
---

# Verification

Crashed-and-restarting containers are "running" too. A claim without the command behind it is
a guess wearing a uniform; the next agent will build on it.

## Claims
- "Verified", "proven", "confirmed", "works" come with the command that reproduces it, or an
  evidence record: what, command, environment, date, result. Put the last one in the HANDOFF
  `evidence:` field.
- For containers, evidence is the container's own output: `docker compose ps` health, log
  lines showing the ready state, and where the protocol allows, an external query response.
- If a check could not run here (no Docker, scanner offline), say so plainly.

## Test ladder — cheapest first
1. Static: `docker compose config` renders; env example covers every variable read.
2. Bring-up in a throwaway directory.
3. Healthy + logs reach ready state.
4. Join/query from outside the host.
5. Restore-from-backup drill.

A tier never certifies what only a higher tier can show. Never run the ladder against live save
data without the user's explicit go-ahead.

## Tests
- A test exercises something outside the test file — never assert a table defined only in the
  test.
- Not built yet: mark expected-to-fail, strict, limited to the not-built error, with the task
  id. Remove the marker when it passes.
- A fix ships with a regression test that fails without it.
- Keep a docs-integrity test: IDs resolve, index paths exist, status markers match.
- Never create a document or test just to make a dangling reference resolve — fix the reference
  or ask.

## Upstream truth
- When sources disagree, trust what the server itself produces (generated config, runtime log)
  over pages and readmes; record the disagreement with URLs and dates.
- Adopting upstream changes: diff against the pinned version, document what changed, then bump.
