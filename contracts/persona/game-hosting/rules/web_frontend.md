# Web control frontend <!-- persona -->
Applies: when the project includes the optional web frontend for server control and
configuration. Requires: base.md, docker_compose.md. The user may expose this frontend to the
public internet — treat every default as reachable by a stranger.

## Scope
- The frontend is always an **addition** to the compose project, never the default delivery,
  and ships bundled in the same project. There is no supported way to run it outside the
  project: no standalone compose file, no external reverse-proxy instructions.
- The game server must remain fully usable with the frontend service removed.

## Authentication — fail closed
- Never deliver a frontend that can start without authentication configured. The container
  must refuse to boot (or the quickstart must force setup before first start) when the admin
  credential is missing, default or placeholder — no "change this later" defaults.
- Admin credentials arrive via env file only; strong-generation instructions in the quickstart.
- No account registration, no anonymous write access, no debug/dev mode reachable through any
  published port.

## Transport security (TLS)
- TLS is mandatory on every frontend listener — LAN use included. Self-signed is acceptable and
  documented as such (how to generate, expected browser warning); a real certificate via the
  user's own DNS-challenge or reverse proxy is the documented upgrade path for public exposure.
- No plain-HTTP fallback "for convenience"; an HTTP listener only as an immediate redirect.
  Never terminate TLS with verification disabled anywhere in the stack.

## Exposure hygiene
- The frontend publishes its port itself; nothing else in the project gets re-proxied through
  it. Game RCON/admin ports and save-data paths are never reachable via the web service —
  validate the allowlist of what the proxy forwards, by test, not by comment.
- Before any public exposure: authentication on, TLS real (not self-signed) or fronted by the
  user's own certified proxy, rate limiting on login, admin surface not enumerable, base image
  patch cadence documented. Record this checklist as a runbook step in the project docs and
  walk the user through it — do not assume LAN-only forever.

## Proxy choice <!-- persona: recommendation -->
- Prefer an auto-TLS-capable proxy — Caddy is the default (`tls internal` gives self-signed
  with zero ceremony). nginx is acceptable where already known to the user, with TLS config
  explicit and complete in the shipped file. Pin either by digest like any other image.