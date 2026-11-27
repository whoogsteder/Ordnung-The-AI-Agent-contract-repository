---
name: kb-interfaces
description: The public surface a knowledge base exposes — CLI subcommands and flags, tool names and arguments given to clients, response shapes and typed error kinds — treated as an API that calling agents will not read a changelog for. Additive-first changes, SemVer and the changelog, read-only surfaces shipping before write surfaces, documenting what a tool returns, what it does when a backend is unavailable and what it never does, and distinguishing not-found from backend-unavailable from not-authorised. Use this whenever you add or change a CLI command or flag, a tool schema exposed to a client, a response or error shape, when a caller reports a break, or before a write surface is proposed at all.
---

# Interfaces

The callers are agents, and agents make confident mistakes. A mistaken read costs a retry; a
mistaken write contaminates the corpus that every later session trusts.

## Treat the surface as public
- Tool names, arguments and CLI flags are a public surface consumed by agents that will not read a
  changelog. Changes follow SemVer and the changelog records them.
- **Additive first:** prefer a new tool or flag over changing the meaning of an existing one.
- A change that breaks a documented behaviour needs a decision record, not just a commit message.

## Read-only ships before write
- Read-only surfaces ship first. A caller can retry a read; a mistaken write is someone else's
  cleanup.
- Every tool documents what it returns, what it does when a backend is unavailable, and **what it
  never does** — for example, never writes to the index (`kb-scope`).
- A write surface states who authorises it and what it refuses. Anything that can destroy the corpus
  or switch a live index needs the owner's go for that action (kernel rule 7 and 13).

## Errors are typed, not prose
- Distinguish *not found*, *backend unavailable* and *not authorised*. A caller branches on these; it
  cannot recover from one generic failure string, and guessing is how an agent retries an
  authorisation failure forever.
- *No result* is a documented outcome, not an error (`kb-retrieval`).
- An error never carries a secret, a credential or corpus content it should not show (kernel rule 12).

## The description is part of the interface
- A tool's own description text is what a calling agent reads instead of a manual. It says when to
  use the tool, what it returns, and what it never does.
- Keep argument names self-describing and their defaults the safe choice: the narrowest scope, the
  read-only path, the smallest result set.

## Prove the surface
- Each subcommand and each exposed tool has a document stating what it returns and the command that
  proves it. Retrieval behaviour is documented by its evaluation, not by adjectives (`kb-eval`).
- A test per error kind: the caller's branch is the behaviour under test.
