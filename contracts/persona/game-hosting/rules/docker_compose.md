# Docker Compose delivery <!-- persona -->
Applies: always — compose is this persona's delivery vehicle. Requires: base.md.

## Composition rules
- One service per dedicated server; keep `docker-compose.yml` thin — image, ports, volumes,
  restart policy, `env_file`. All tunables live in the env file, not the compose file.
- Pin every image by tag **and** digest. Record where and when the digest was verified.
- Name a generous `stop_grace_period` for servers that need to flush saves on shutdown;
  set `restart: unless-stopped` unless there is a documented reason not to.
- Publish only the ports the game protocol actually needs (some servers serve game and query
  traffic on one port); state in a comment why each published port exists.
- Save data lives in a host-mounted directory or named volume declared in the compose file —
  never inside the container filesystem, which an image bump throws away.

## Env-file config model
- The env file is the product's configuration surface: every supported setting appears in
  `<name>.env.example`, grouped and annotated with allowed values, defaults and source.
- Compose `env_file` values are taken literally — quotes become part of the value, types come
  from the text. Document these traps in the example file itself where they bite.
- The container regenerates its native config (JSON/INI) from env at start: tell the user which
  file is authoritative and that hand-edits to generated files are transient unless a key is
  left unmanaged. Applying changes usually needs recreate (`up -d`), not just `restart`.

## Portability
- The portable artifact is the **compose file**, not a vendor product: any Compose-spec runtime
  (Docker Engine/Compose, Podman + compose provider) runs the delivered stack. Docker is the
  documented default because it is the best-known platform and `docker compose up` is the
  one-shot that lowers the complexity bar; Podman-compatible syntax is free to keep.
- Docker Desktop is never a requirement in instructions — its licensing is the operator's
  platform concern (see `steamcmd.md` → Third-party licensing), and any Desktop-specific setup
  step is written as optional convenience, never as the only path.
- Linux is the primary, best-supported runtime target. On Windows the container runtime is a
  Linux VM either way (WSL2/Hyper-V under Docker Desktop or Podman machine), so nested
  virtualization and its quirks are shared; Wine/Proton-based servers are more fragile there.
  A server that cannot meet the Windows target is still deliverable — mark it loudly in README
  and compose comments, name the reason (Wine/Proton runtime, kernel device, driver), and
  document the platform-specific step instead of dropping support silently.

## Verification
- `docker compose config` renders before any commit; env example and compose variables stay in
  sync (every variable read has an example entry, every example entry is read).
- Full ladder per `rules/verification.md`; never test against live save data uninvited.