# Interfaces <!-- persona -->
Applies: when changing the CLI or the tools exposed to clients. Requires: base.md.

- Tool names, arguments and CLI flags are a public surface consumed by agents that will not read a
  changelog. Changes follow SemVer and the changelog records them.
- Additive first: prefer a new tool or flag over changing the meaning of an existing one.
- Read-only surfaces ship before write surfaces. A caller can retry a read; a mistaken write is
  someone else's cleanup.
- Every tool documents what it returns, what it does when a backend is unavailable, and what it
  never does — for example, never writes to the index.
- Errors distinguish "not found" from "backend unavailable" from "not authorised". A caller
  branches on these; it cannot recover from one generic failure string.
- An interface change that breaks a documented behaviour needs a decision record, not just a commit
  message.
