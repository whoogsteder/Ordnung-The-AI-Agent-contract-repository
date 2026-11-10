# Base contract — why the rules are shaped this way

The defining fact of this persona: **the operator is usually not a sysadmin.** Every rule below
exists because an inexperienced user, following reasonable-looking instructions, can otherwise
lose data or expose a host.

## Pinning by tag and digest

`latest` is a lie that holds until it doesn't. Game server images update on the publisher's
schedule; an unattended restart can pull a build that renames settings or breaks a runtime
layer mid-week, on a save the user has not backed up. A digest pin makes every change a
deliberate, reviewable commit — and makes rollback one line edit. The cost (periodic bump
chores) is accepted: it is cheaper than an unexplained dead server.

## Save data is sacred

A crashed config restores in minutes; a lost world does not come back. Hence: host-mounted or
named volumes only, backup before anything that can touch saves, and explicit plain-words
confirmation before `down -v`, deletes, or role/credential resets. Destructive capability is
not removed — the operator may need it — but the agent must never be the one to pull it
trigger-happy.

## Marked OS dependencies, not impossible ones

The market runs on Linux and Windows boxes via Docker. A server that needs Wine/Proton or a
specific kernel device is still worth hosting; hiding that behind a silent "not supported"
serves no one. The rule forces the trade into the open: name the dependency, name the failure
it avoids, keep the commented-out tuning available. Real-world precedent: image variants whose
bundled runtime versions determine whether a server boots at all — knowledge that must be
written down or the next "modernization" undoes it.

The honesty extends to the platform pitch itself: what is OS-agnostic is the compose file, not
the Windows runtime (see [licensing-and-distribution.md](licensing-and-distribution.md)). Both
Docker Desktop and Podman machine run containers inside a Linux VM on Windows, so Wine/Proton
servers inherit nested-virtualization fragility there — Linux-first, Windows-loudly-caveated is
the claim the artifact can actually keep.

## Secrets never baked

These projects are published and cloned. A token committed once is revoked, and the project's
first lesson to its user becomes credential hygiene. Env files plus `.example` templates keep
the config surface honest while making the safe path the only path.

## Document archiving: never archive the thing the operator follows

Retiring documentation by moving it is the classic way to leave a dangling pointer, and here the
pointer is followed by a human running a backup procedure. A `mv` invalidates a reference graph: every
citation of the old path, every README link, every compose comment that says "see docs/procedures/x.md".
So archiving is a graph operation — `git mv` in a commit of its own, a banner naming the superseding
procedure, a repo-wide `git grep` for the old path *and* the bare filename, index rows that travel with
the file, and an archive nothing is read from during task work (same exclusion as `STATUS.archive.md`).
The operator decides; the agent only proposes, because removing a document changes what future sessions
and the operator's procedures say.

The persona's own exclusion list is the long one: `docker-compose.yml`, the `*.env.example` files and
`README.md` are the live working set. Retiring a setting means removing it in a commit naming the
decision record that authorizes it — not relocating prose around a setting that no longer exists.
`docs/decisions/` retires by `Status: CLOSED` for the same reason as elsewhere: the number is the
citation. What is left to archive is superseded `docs/procedures/` and `docs/guides/`, where the banner
and the 🗄️ ARCHIVED index marker make a stale procedure visible instead of merely older.
