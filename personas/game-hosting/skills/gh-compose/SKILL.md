---
name: gh-compose
description: Rules for delivering game servers as a Docker Compose project — thin compose file, env file as the configuration surface, images pinned by tag and digest, published ports, save-data volumes, panel-owned game containers, Linux/Windows/Podman portability. Use this whenever you edit or review docker-compose.yml, a *.env or *.env.example file, a container spec the panel creates, an image tag or digest, a port or volume, or answer how the stack runs on Windows, Docker Desktop or Podman.
---

# Compose delivery

The compose file is the product: it is what the operator runs, and what an image bump or a
typo can break on a night nobody is watching. Everything here is about making changes
deliberate and the safe path the default.

## Composition
- The compose file ships the platform: the panel, its proxy, any control-plane helper. Game
  servers are compose services *or* containers the panel creates and owns — one per project,
  recorded as a DR.
- Keep `docker-compose.yml` thin: image, ports, volumes, restart policy, `env_file`. Tunables
  live in the env file.
- Pin every image by tag **and** digest (`image: name:tag@sha256:…`) and note where/when the
  digest was checked. An image or server-version bump is its own commit with a CHANGELOG entry,
  because it is the change most likely to need rolling back.
- Give servers that flush saves on shutdown a generous `stop_grace_period`; default
  `restart: unless-stopped` unless a reason is documented.
- Publish only the ports the game protocol needs, with a comment saying why each exists.
- Save data lives in a host-mounted directory or named volume — never the container
  filesystem, which an image bump throws away.

## Panel-owned game containers
When the panel creates game containers itself:
- Every rule above binds the panel's container spec too; review it like a compose file.
- Ownership is exclusive: compose never manages a panel container, the panel never adopts a
  compose service (compose recreates any container it did not create).
- Label each container with project and server, so the operator can find and stop it with the
  runtime CLI when the panel is down.
- The panel keeps desired state in a file under the data directory and reconciles on start; it
  never recreates a running server just because the panel restarted.
- Host ports come from an env-declared range; collisions are refused with a plain-language
  error.
- `docker compose down` on the platform never deletes game containers or data. Removing a
  server is a confirmed panel action, after a backup.

## Env-file config model
- The env file is the stack's configuration surface — ports, paths, exposure, credentials,
  limits. Every variable appears in `<name>.env.example`, grouped and annotated with allowed
  values, defaults and source; every example entry is actually read.
- Game settings live in each game's native config; say per game which file is authoritative
  and whether a hand-edit survives the next write.
- Compose `env_file` values are literal — quotes become part of the value. Document the trap
  in the example file where it bites.
- State what applying each change needs: restart, recreate (`up -d`), or nothing.
- Real env files are git-ignored from the first commit; secrets never enter git history.

## Portability
- The portable artifact is the compose file: any Compose-spec runtime (Docker Engine/Compose,
  Podman + compose provider) runs it. Docker is the documented default; keep Podman-compatible
  syntax.
- Never require Docker Desktop; Desktop-specific steps are optional convenience.
- Linux is the primary target. On Windows the runtime is a Linux VM either way, and
  Wine/Proton servers are more fragile there. A server that cannot meet the Windows target is
  still deliverable — mark it loudly in README and compose comments with the reason.

## Before commit
`docker compose config` renders; env example and compose variables are in sync. Higher tiers:
`gh-verification`.

## DR triggers
Image/vendor selection, volume layout, port scheme, compose-vs-panel ownership.
