---
name: iac-release
description: Branching, versioning and release rules for infrastructure-as-code projects — SemVer with one version source, short-lived typed branches off an always-releasable main, one change batch per branch and PR, squash merge, Keep a Changelog, annotated tags and pre-release tags, bundles built from tags, environments upgraded from tags in order (acceptance then production), declared stable surfaces and live-smoke rules. Use this whenever you create a branch, commit, open or update a PR, bump a version, edit CHANGELOG.md, tag, build a release bundle, or upgrade an environment.
---

# Branches and releases

## Branches
- `main` is always releasable. Work happens on short-lived branches off `main`, named
  `<type>_<topic>` with type `feat`, `fix`, `docs` or `chore` and a snake_case topic.
- One change batch per branch, which is one PR. Unrelated work found on the way goes on the
  board (`ordnung-board`), not into this branch.
- Before you branch, pull `main` and delete merged local branches only with the owner's go.
- Commit only when the user or the release flow asks for it. Push only to your own branch. Never
  force-push a shared branch.

## Versions
- SemVer 2.0. The version string lives in exactly one file (`iac-python`: `pyproject.toml`).
- MAJOR is a breaking change to a stable surface; MINOR is a backward-compatible feature batch;
  PATCH is a fix or docs only. While the version is `0.y.z`, MINOR may break things.
- The project declares, in one place the REPO-MAP names, its stable surfaces, what `v1.0.0`
  means, and when a live smoke test is required.

## Release flow (the default; a project's PROJECT.md may record its own variant as a REQ)
1. **The PR.** The tests are green, plus a live smoke test where the project requires one. The PR
   description says what changed, how it was tested (the tiers), and any upgrade step.
2. **The merge** is a squash into `main`, done by the owner, or by whoever PROJECT.md says. After
   the merge, delete the branch.
3. **The changelog.** Update `CHANGELOG.md` in Keep a Changelog format with every release. If a
   generated artefact is derived from it (a "what's new" page), regenerate it in the same change.
4. **The tag.** An annotated `vX.Y.Z` on the merge commit. During a live smoke test, use
   pre-release tags `vX.Y.Z-rc.N` on the branch tip.
5. **Bundles and environments.** Build the bundle from tags only, never from a branch tip.
   Upgrade in order, acceptance and then production, each with the owner's go. Record the result
   per environment in the HANDOFF `evidence:` field, and in the project's operations notes.

## Upgrade steps
A release that needs a one-time step on an environment (a schema migration, a config key, a
restart) documents that step in the admin or upgrade docs before the tag. The steps per
environment are:
1. read-only check;
2. backup;
3. the step itself;
4. a re-check, with the result recorded.

A step that changes data counts as destructive (kernel rule 7).
