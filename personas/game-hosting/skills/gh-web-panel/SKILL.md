---
name: gh-web-panel
description: Security and scope rules for the bundled web control panel of a game-hosting project — fail-closed authentication, mandatory TLS, reverse proxy (Caddy default), exposure hygiene, the container-control allowlist, many-server views, and keeping game servers independent of the panel. Use this whenever you touch panel code, its proxy config, login/session/credential handling, what the panel may run against the container runtime, resource or port views, or the user asks about exposing the panel to the internet.
---

# Web control panel

Assume a stranger can reach every default, whether the operator keeps the panel on the LAN or
not. The panel is also the stack's most dangerous component: it can stop, start and rewrite
game servers. Hence: fail closed, encrypt always, allowlist everything.

## Scope
- The panel ships bundled in the same compose project; no standalone or external-proxy setup is
  supported.
- Exposure is the operator's one choice: local-only by default; internet exposure goes through
  the public-exposure procedure.
- Game servers never depend on the panel. Stopping, crashing or upgrading it never stops or
  recreates a running server. Prove it by test: stop the panel, the game still answers its
  query port.
- Everything the panel does can be done by hand with the runtime CLI; README documents those
  commands for the day the panel is the problem.

## Authentication — fail closed
- The panel refuses to boot when the admin credential is missing, default or placeholder (or
  the quickstart forces setup first). No "change this later".
- Credentials arrive via env only, with strong-generation steps in the quickstart.
- No registration, no anonymous write access, no debug/dev mode on any published port.

## TLS
- TLS on every listener, LAN included. Self-signed is acceptable and documented (how to
  generate, expected browser warning); a real certificate is the upgrade path for exposure.
- HTTP only as an immediate redirect. Never disable verification anywhere in the stack.

## Exposure hygiene
- Nothing else is re-proxied through the panel. RCON/admin ports and save-data paths are never
  reachable through it — enforce the proxy allowlist by test.
- Container control goes through a fixed allowlist of operations, never an operator-supplied
  command string; enforced by test.
- Before public exposure: auth on, real TLS (or the user's certified proxy), login rate
  limiting, admin surface not enumerable, base-image patch cadence documented — kept as a
  procedure in `docs/procedures/` and walked through with the user.

## Many servers
- Show per-server CPU, memory, network and data-disk usage from the runtime's own stats;
  unmeasurable is shown as unmeasured, never zero.
- Every action names its server; bulk actions list targets and confirm first.
- Show host ports per server so collisions are visible before they fail.

## Proxy
Caddy by default (`tls internal` gives self-signed with no ceremony); nginx where the user
already knows it, with complete TLS config. Pin by digest.

## DR triggers
Frontend technology (always), any widening of what the panel may do without confirmation.
