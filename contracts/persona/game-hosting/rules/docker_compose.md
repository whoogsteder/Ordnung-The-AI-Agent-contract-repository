# Docker Compose delivery <!-- persona -->
Applies: always — compose is this persona's delivery vehicle. Requires: base.md.

## Composition rules
- The compose file ships the platform: the panel, its proxy and any control-plane helper. Game
  servers are either compose services or containers the panel creates and owns (see
  Panel-owned game containers) — choose per project and record the choice as a DR.
- Keep `docker-compose.yml` thin — image, ports, volumes, restart policy, `env_file`. Stack
  tunables live in the env file, not the compose file.
- Pin every image by tag **and** digest. Record where and when the digest was verified.
- Name a generous `stop_grace_period` for servers that need to flush saves on shutdown;
  set `restart: unless-stopped` unless there is a documented reason not to.
- Publish only the ports the game protocol actually needs (some servers serve game and query
  traffic on one port); state in a comment why each published port exists.
- Save data lives in a host-mounted directory or named volume declared in the compose file —
  never inside the container filesystem, which an image bump throws away.

## Panel-owned game containers
Applies: when the panel creates game-server containers itself instead of compose.
- Every composition rule above binds a panel-created container too: image pinned by tag and
  digest, restart policy, stop grace period, only the needed ports published, save data outside
  the container filesystem. The panel's container spec is the compose file's equivalent and is
  reviewed like one.
- Ownership is exclusive. Compose never manages a panel-created container and the panel never
  adopts a compose service: compose recreates any container it did not create itself.
- Label every created container with the project and the server it belongs to, so the operator
  can find, inspect and stop them with the container runtime's CLI and no panel
  (`web_frontend.md` → Scope).
- The panel keeps the desired state of every server (image, ports, volumes, limits) in a file
  under the project's data directory. On start it reconciles against what is running; it never
  recreates a running server only because the panel itself restarted.
- Host ports come from a range declared in the env file; the panel refuses a collision with a
  plain-language error instead of letting the runtime fail.
- Tearing down the platform stack (`docker compose down`) never deletes game containers or their
  data. Removing a server is a panel action with explicit confirmation, after a backup
  (`base.md` → destructive operations).

## Env-file config model
- The env file is the **stack's** configuration surface — ports and port ranges, paths, exposure,
  credentials, resource limits. Every variable appears in `<name>.env.example`, grouped and
  annotated with allowed values, defaults and source.
- Game settings are not env variables: they live in each game's native config (JSON, INI, XML,
  launch arguments) and the panel writes them through its per-game definition. Tell the operator,
  per game, which file is authoritative and whether a hand-edit survives the panel's next write.
- Compose `env_file` values are taken literally — quotes become part of the value, types come
  from the text. Document these traps in the example file itself where they bite.
- State what applying each change needs: a restart, a recreate (`up -d`), or nothing.

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
