---
name: ca-release
description: Releasing Ordnung-Zwei — SemVer for the contract set with contracts-vX.Y.Z annotated tags and release candidates, persona versions in persona.md frontmatter, Keep a Changelog entries with breaking changes and migration steps, GitHub releases, links into the frozen v1 tag, branch-and-PR flow on main, and the public-repository check before anything is pushed. Use this whenever you bump a version, edit CHANGELOG.md, tag, cut a release candidate, open or merge a PR here, link to v1 material, or push anything to the public remote.
---

# Releasing the contract set

## Versions
- **The contract set uses SemVer, with annotated tags `contracts-vX.Y.Z`.** MAJOR breaks
  installed projects (memory-file format, kernel shape, the installer's behaviour). MINOR adds a
  persona, skill or check that existing projects pass. PATCH is wording.
- **Release candidates** (`contracts-vX.Y.Z-rc.N`) cover the field-test period. The final tag
  waits until the field feedback named in PROJECT.md is in.
- **Each persona carries its own `version` in `persona.md`.** A change bumps every persona it
  touches, core skills included, since every persona ships those.
- **v1 is frozen at `contracts-v1.4.0`.** Link to it by tag URL
  (`…/tree/contracts-v1.4.0/contracts/persona/<p>/rules/<file>.md`), never by branch. Nothing from
  v1 comes back into the tree (DR-006).

## CHANGELOG.md
Use Keep a Changelog format, with an `[Unreleased]` section that is kept current. Each release
lists:
- Added, Changed and Removed;
- **Breaking**, with a migration step for installed projects. For example: "add
  `agent/TASKS.md`, move the *Task queue* entries onto it".

## Flow
- **`main` is always releasable.** Work happens on `<type>_<topic>` branches, each going through
  a PR. Before the PR: `pytest tests/` passes, `python3 agent/ordnung_check` passes, and the root
  `AGENTS.md` is re-rendered if the kernel or this persona changed.
- **Releasing:**
  1. Turn `[Unreleased]` into the version section.
  2. Merge.
  3. Put an annotated tag on the merge commit, with a message summarising the release.
  4. Push the tag.
  5. Create the GitHub release. Mark an RC as a pre-release.
- Tags, releases and merges to the public remote are outward-facing (kernel rule 7). Do them on
  the operator's go for that release.

## Before anything is pushed: the public check
This repository is public (kernel rule 11). Before pushing, grep the diff for:
- names of field projects, employers, customers or sites;
- hostnames, IP addresses, account or repository names that belong to a field project;
- secrets, tokens and keys.

Material from a field project is made generic first ("project B, an IaC firewall-management
tool"). Remember that history is public too: a file deleted in a later commit is still published
if an earlier commit holds it.
