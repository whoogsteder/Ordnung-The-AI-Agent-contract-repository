# Core sync — seam markers and the one-commit rule

Status: ✅ IMPLEMENTED. Applies to: everyone editing files under `contracts/persona/*/rules/`
or the root `rules/` (the repo-maintainer dogfood contract).

## Why

Persona contracts share a behavioral core (context discipline, HANDOFF, archiving, session
continuity…). Without a mechanism, fixing a bug in one persona's core silently leaves the
others wrong. The mechanism is **copy-with-markers + checker**, not shared source files:
each persona stays a self-contained drop-in folder, and `tools/check_sync` enforces that
copies of shared sections do not drift.

## Seam markers

Every top-level (`# `) heading in a contract rule file carries exactly one marker:

| Marker | Meaning | Checker rule |
|---|---|---|
| `<!-- core -->` | Shared behavior, must be identical | Bodies (whitespace-normalized, markers stripped) equal across all personas that ship the file — and equal to the root dogfood copy if it ships the same file |
| `<!-- slot: name -->` | Same section intent, persona-specific wording | Heading must exist in every persona shipping the file; bodies may differ |
| `<!-- persona -->` or `<!-- persona: note -->` | Owned by one persona | No cross-persona obligation |

Example:

```markdown
# Session continuity <!-- core -->
- If agent/STATUS.md exists: read its HANDOFF block before acting.

# State & change history <!-- slot: state-history -->
- IaC: SemVer + git branches. / Administrative: versioned records + audit trail.
```

## Section map (base.md)

| Section | Seam |
|---|---|
| Role | `slot: role` |
| Context discipline, REPO-MAP maintenance, Session continuity, Session conclusion, HANDOFF block format, Archiving | `core` |
| State & change history | `slot: state-history` |
| Documentation | `slot: documentation` |
| Document archiving | `slot: documentation` (second section carrying the same slot name; heading text must stay identical across personas, bodies differ per persona's document tree) |
| Rule files | `core` |
| Versioning & branches / Versioning & history | `persona` |
| Security / Data handling & privacy | folded into `slot: state-history` (iac / administrative) |

verification.md: module header and Claims are `persona` (evidence vocabulary is
persona-specific); persona modules carry their own markers. adr.md / dr.md share
`slot: decision-records`.

## The one-commit rule

A commit that changes a `<!-- core -->` section must change the same section in **all**
personas shipping that file — and in the root dogfood copy — in the same commit. Bump the
`version:` in every touched persona's `agent/ruleset.md`:

- patch (x.y.Z): wording fix inside a core/slot section
- minor (x.Y.0): new rule, new section, new module
- major (X.0.0): incompatible workflow change (breaking for installed copies)

## Verifying

```sh
python3 tools/check_sync            # structure + drift across personas and root copy
uv run --with pytest --no-project python -m pytest tests/ -q   # checker self-tests
```

Both must pass before committing contract changes. `check_sync` also fails on unmarked
headings and missing/malformed manifests, so a new persona cannot silently skip the seam.
