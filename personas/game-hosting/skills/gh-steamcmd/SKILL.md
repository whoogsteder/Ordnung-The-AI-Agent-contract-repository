---
name: gh-steamcmd
description: Rules for acquiring, running and updating Steam-distributed dedicated servers — upstream image vs own steamcmd build, app ids and beta branches, Wine/Proton image variants, game update flow and rollback, and third-party licensing (self-hosting, redistribution, monetized hosting, Docker Desktop licensing). Use this whenever you choose or bump a game-server image, touch steamcmd, handle a game update, pick a Wine/Proton variant, or the user asks whether hosting, charging for slots or distributing an image is allowed.
---

# SteamCMD & server acquisition

Game updates land without notice, and vendor docs lag the binaries. These rules exist so that
the next agent does not "modernize" to a broken variant or pull a breaking update unattended.

## Acquisition
- Prefer a maintained upstream image that owns steamcmd handling. Building your own is always a
  DR with the reason.
- Where you drive steamcmd: anonymous login first. A credentialed Steam login is the
  operator's own secret — env-supplied, never baked, committed or collected.
- Record the app id and any beta/depot branch in compose or docs; branch moves break `latest`
  assumptions.

## Runtime variants
- Windows-built servers on Linux run under Wine/Proton. When the variant matters, pin the
  working one by digest and document the failure signature it avoids, with the upstream issue
  link.
- Optional performance devices (e.g. kernel sync devices) stay commented-out defaults with the
  kernel version they need.

## Updates
1. Bump the pin. 2. Back up saves. 3. Recreate. 4. Check ready-state logs (`gh-verification`).
5. Only then call it done. Keep the rollback to the previous digest documented.
- New settings in a game version: diff the generated config against the pinned version's key
  set and adopt deliberately into the env example — never auto-merge.

## Licensing & distribution
- Hosting for your own players is normal, permitted use — that is why dedicated-server app ids
  exist. Do not present it as legally doubtful.
- Never redistribute fetched game/server binaries: no baking content into a distributable
  image, no mirroring to a registry. What ships is config only.
- Charging others for slots is governed per game. When the user's goal includes charging, flag
  "check this game's EULA / publisher hosting policy"; do not silently assist.
- Docker Engine on Linux is Apache-2.0; Docker Desktop is under Docker's subscription terms
  (free for personal use and small businesses, paid above that); Podman is the license-clean
  alternative. State this once in README; the platform choice is the operator's.

## Other platforms
GOG, Epic, itch follow the same shape (acquisition, env credentials, pinning, update flow) —
add a section here when one enters use.
