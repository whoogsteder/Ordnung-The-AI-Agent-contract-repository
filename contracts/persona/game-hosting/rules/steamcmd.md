# SteamCMD & dedicated server acquisition <!-- persona -->
Applies: when the server binary is distributed through Steam (steamcmd or a prebuilt image
that wraps it). Requires: base.md, docker_compose.md.

## Acquisition
- Prefer a maintained upstream image that owns steamcmd handling; build your own only with a
  recorded reason (DR — see `rules/base.md` → Decision Records). Where you do drive steamcmd:
  anonymous login first — credentialed Steam logins are the user's own secret, supplied via env,
  never baked or committed.
- Record the game's app id and any beta/depot branch in the compose or docs; those change when
  the publisher moves branches and break silent `latest` assumptions.

## Runtime dependencies
- Windows-built server binaries on Linux containers run under Wine/Proton layers. When an image
  variant choice matters (Wine vs Proton, bundled runtime versions), pin the working variant by
  digest and document the failure signature it avoids — including the upstream issue link — so
  the next agent does not "modernize" to a broken variant.
- Optional performance devices (e.g. kernel sync devices) stay commented-out defaults with the
  kernel version they need; never hard requirements unless proven on the target platforms.

## Updates
- Game updates land without notice and can break configs or protocols. Update flow: bump pin →
  back up saves → recreate → verify ready-state logs → only then call it done. Keep a documented
  rollback to the previous digest.
- New game-version settings: diff generated config against the pinned version's documented key
  set; adopt deliberately into the env example, don't auto-merge.

## Third-party licensing & distribution
- Hosting for your own players is permitted, normal use: dedicated server app ids exist on Steam
  precisely so players self-host. Do not treat or present self-hosting as legally doubtful.
- Never redistribute fetched game/server binaries: no baking content into a distributable image,
  no mirroring steamcmd-fetched files to any registry or repository. The runtime pull happens on
  the operator's machine; what ships is thin config only (compose file, env examples, docs).
- Steam credentials are the operator's own account secret (only when a game requires a paid game
  ownership login): env-supplied, never committed, never collected.
- Monetized hosting (charging others for slots) is governed per-game — some publishers allow it,
  some forbid it. Flag "check this game's EULA / publisher hosting policy" whenever the user's
  stated goal includes charging; do not silently assist.
- Runtime platform licensing: Docker Engine/Compose on Linux is Apache-2.0 with no usage or
  company-size restriction; Docker Desktop (Windows/macOS) is governed by the Docker
  Subscription Service Agreement — free Personal tier covers personal/hobby use and small
  businesses (<250 employees AND <$10M annual revenue), larger organizations need a paid
  subscription. Podman (Apache-2.0) is the license-clean alternative; keep delivered stacks
  Compose-spec-compatible so either runtime works. State this once in the project README for
  operators; the agent does not police their platform choice.

## Future platforms
- Servers from other distribution platforms (GOG, Epic, itch) follow the same rules — separate
  section here when one enters use: acquisition path, credential handling as env, pinning,
  update flow. No platform-specific assumption leaks into `docker_compose.md`.