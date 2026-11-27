---
name: gh-operator-docs
description: Documentation and usability rules for game-hosting projects whose operators are often inexperienced — README landing page, the copy-paste quickstart for Linux and Windows, per-setting env documentation, troubleshooting entries from real failure signatures, numbered procedures, plain-language error messages and destructive-action warnings. Use this whenever you write or change README, docs/procedures, docs/guides, an env example comment, a script's error output, or finish any deliverable (no docs = not done).
---

# Operator docs & usability

The operator has often never hosted a server. A wrong value they could reasonably enter is a
documentation bug, not user error — fix the docs or add validation.

## README (the landing page)
Minimum: prerequisites, a copy-paste quickstart for Linux **and** Windows, per-setting
documentation of the env example, troubleshooting for every known failure mode, and the
runtime licensing note (`gh-steamcmd`). Every deliverable ships with docs.

## Quickstart is sacred
- Copy-pasteable, in order, identical on Linux and Windows (mark the rare divergence).
- Every command exists verbatim in the repo; no implicit `cd`, no assumed editor.
- Ends with how to confirm the server is up — from the host and from the game.

## Voice
Define each term on first use, say what a command does before asking them to run it, state the
expected output ("you should see `healthy` within ~2 minutes").

## Failure experience
- Each failure mode hit during development becomes a troubleshooting entry: exact log
  signature, cause in one sentence, fix in steps. Include the restart-loop triage
  (`docker compose ps`, `docker compose logs --tail 100`).
- Shipped scripts fail in human: what went wrong, which file to edit, where to look next.

## Procedures and guides
- `docs/procedures/`: backup/restore, updates, log inspection, public exposure — numbered steps
  with expected output, for someone who has never done it.
- `docs/guides/`: how-to material.
- Destructive paths (reset, delete saves, expose publicly) get a warning block before the steps.

## Guardrails over lectures
Sane defaults, validation at start with clear messages, `.example` files that explain
everything. Code comments explain how a line works; docs explain what to run and what it means.
