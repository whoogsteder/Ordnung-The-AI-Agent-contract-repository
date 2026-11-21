# Web control panel <!-- persona -->
Applies: always — the web panel is part of every delivery. Requires: base.md, docker_compose.md.
Whether the panel stays on the local network or is exposed to the internet is the operator's
choice; treat every default as reachable by a stranger either way.

## Scope
- The panel ships bundled in the same compose project as everything else. There is no supported
  way to run it outside the project: no standalone compose file, no external reverse-proxy
  instructions.
- Exposure is the operator's one choice: local-only is the default; internet exposure is an
  opt-in step that goes through the public-exposure procedure below.
- Game servers never depend on the panel being up. Stopping, crashing, rebuilding or upgrading
  the panel never stops, restarts or recreates a running game server, and every game server
  keeps its own restart policy without it. Prove this by test (stop the panel; the game keeps
  serving and still answers its query port), not by comment.
- Everything the panel does to a game server can also be done by hand with the container
  runtime's own CLI; the README documents those commands (list, logs, stop, start, backup) for
  the day the panel itself is the problem.

## Many-server panel
Applies: when one panel manages more than one game server.
- Show resource usage per game-server container — CPU, memory, network, and the disk used by
  its data — and for the panel's own stack, read from the container runtime's own statistics,
  never estimated. A server the panel cannot measure is shown as unmeasured, not as zero.
- Every action names the server it acts on. No action addresses "all servers" implicitly; a
  bulk action lists the servers it will touch and asks for confirmation first.
- Show the host ports each server holds, so a collision is visible before it is a failure.

## Authentication — fail closed
- Never deliver a panel that can start without authentication configured. The container
  must refuse to boot (or the quickstart must force setup before first start) when the admin
  credential is missing, default or placeholder — no "change this later" defaults.
- Admin credentials arrive via env file only; strong-generation instructions in the quickstart.
- No account registration, no anonymous write access, no debug/dev mode reachable through any
  published port.

## Transport security (TLS)
- TLS is mandatory on every panel listener — LAN use included. Self-signed is acceptable and
  documented as such (how to generate, expected browser warning); a real certificate via the
  user's own DNS-challenge or reverse proxy is the documented upgrade path for public exposure.
- No plain-HTTP fallback "for convenience"; an HTTP listener only as an immediate redirect.
  Never terminate TLS with verification disabled anywhere in the stack.

## Exposure hygiene
- The panel publishes its port itself; nothing else in the project gets re-proxied through
  it. Game RCON/admin ports and save-data paths are never reachable via the web service —
  validate the allowlist of what the proxy forwards, by test, not by comment.
- The panel's access to the container runtime is its most dangerous capability: it acts only
  through a fixed allowlist of operations, never an operator-supplied command string, and the
  allowlist is enforced by test.
- Before any public exposure: authentication on, TLS real (not self-signed) or fronted by the
  user's own certified proxy, rate limiting on login, admin surface not enumerable, base image
  patch cadence documented. Record this checklist as a procedure under `docs/procedures/` and
  walk the user through it — do not assume LAN-only forever.

## Proxy choice <!-- persona: recommendation -->
- Prefer an auto-TLS-capable proxy — Caddy is the default (`tls internal` gives self-signed
  with zero ceremony). nginx is acceptable where already known to the user, with TLS config
  explicit and complete in the shipped file. Pin either by digest like any other image.
