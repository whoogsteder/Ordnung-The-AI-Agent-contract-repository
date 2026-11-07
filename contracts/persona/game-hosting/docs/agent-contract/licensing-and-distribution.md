# Licensing & distribution — why the rules draw the line where they do

Content acquired with SteamCMD is licensed game content; the wrapper around it is our own code.
The rules keep those two categories strictly apart, and the seams are where legal risk actually
lives. Verified against the current texts on 2026-11-07 — re-check when this page ages.

## Self-hosting is the intended use, not a gray zone

Publishers ship dedicated-server app ids on Steam precisely so players host their own servers;
SteamCMD is Valve's free tool for exactly that. A persona that treated self-hosting as legally
doubtful would refuse the user's core request and mislead them. The one tier that *is* per-game
gray: charging third parties for hosted slots — some publishers bless it, some forbid it — hence
"flag, don't silently assist."

## Distribution is the real seam — and Docker naturally stays on the right side

Game EULAs restrict redistributing server binaries. A thin compose stack sidesteps this by
construction: the image ships tooling, the game content is fetched at runtime on the operator's
machine, and what we publish is config only (compose file, env examples, docs). The rules freeze
that construction so no future "convenience" (pre-baked image, mirrored depot in a registry)
quietly crosses the line. Real-world precedent: the Enshrouded reference project is MIT-licensed
*wrapper* code on GitHub with 291 stars — nobody has taken it down, because it distributes no
game content.

## Runtime platform licensing belongs to the operator

Docker Engine/Compose on Linux is Apache-2.0 — free for any use at any company size. Docker
Desktop (Windows/macOS) sits under the Docker Subscription Service Agreement: free Personal tier
for personal/hobby use and businesses under both 250 employees and $10M revenue; paid above that.
The agent states this once in the delivered README and stops there — policing the operator's
platform choice is not the deliverable, and hiding the thresholds helps no one.

## Why Docker stays the documented default (and Podman costs nothing)

Docker was chosen for recognition and the `docker compose up` one-shot that collapses setup
complexity for inexperienced operators — not for runtime supremacy. The 2026 Podman-on-Windows
story is genuinely closer than its reputation: installer, machine abstraction, GUI, compose
provider; near-drop-in CLI. But it is still the community-supported path: fresh install, real
machine-init bug reports open against current releases, and troubleshooting content that assumes
sysadmin comfort — a bigger ask for exactly the audience this persona serves. The insight that
keeps both: **the compose file is the portable artifact**. Staying Compose-spec-clean means a
Podman operator runs the same stack at zero authoring cost, so the persona recommends without
locking in.

## "OS-agnostic" needs one honest asterisk

Compose files are OS-agnostic; Windows *runtimes* are not really — Docker Desktop and Podman
machine both put containers inside a WSL2/Hyper-V Linux VM, and Wine/Proton-based servers are
more fragile under nested virtualization than on bare Linux. The rule therefore says: portable
artifact, Linux-first runtime, loudly marked platform quirks — which is what the reference
project's own kernel-device (`/dev/ntsync`) caveat already proved in practice.