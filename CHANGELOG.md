# Changelog

All notable changes to the Ordnung! agent-contract set are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html). The version string
lives in each persona manifest (`contracts/persona/*/agent/ruleset.md`) and in the root
repo-maintainer manifest (`agent/ruleset.md`). A release of the contract set is an annotated tag
`contracts-vX.Y.Z` on `main`. Bumps follow the rule in
[docs/authoring/core-sync.md](docs/authoring/core-sync.md): patch for wording inside a core/slot
section, minor for a new rule, section or module, major for an incompatible workflow change.

## [Unreleased]

The next entry starts when the next contract change lands on `main`.

## [1.2.0] - 2026-11-10

Tagged `contracts-v1.2.0`. All four persona manifests and the root dogfood manifest read
`version: 1.2.0`.

### Added

- **Document archiving rule** (all four personas + root dogfood copy, 2026-11-10) — a new
  `# Document archiving (mandatory)` section in every `rules/base.md`, marked
  `<!-- slot: documentation -->` so each persona names its own document tree while the heading stays
  identical across personas. The rule treats archiving as a **reference-graph operation, not a file
  move**: the operator decides, the agent only proposes; `git mv` into `docs/archive/<same subpath>/` in
  a commit of its own so rename detection keeps `git log --follow` intact; an
  `ARCHIVED <date> — read-only history; superseded by <path>; <reason>` banner freezing the file; a
  repo-wide `git grep` for the old path *and* the bare filename, re-pointing every citation except
  history files; instructions that tell a reader to write into the archived file re-pointed to a
  writable location; both REPO-MAP rows (directory guide + documentation index) moved with the file;
  🗄️ **ARCHIVED** added as a fourth documentation status marker; the archive is never read during task
  work, the same exclusion as `STATUS.archive.md` and `docs/agent-contract/`.
- **Persona-specific slot bodies** (the reason the section is a slot, not core):
  - `iac` archives `docs/architecture/`, `docs/guides/`, `docs/runbooks/`; **ADRs are not archived** —
    `ADR-NNN` is the citation and the sequence is the index, so retirement stays `Status: CLOSED`
    (`rules/adr.md`).
  - `administrative` archives `docs/guides/`, `docs/procedures/` and superseded template/script paired
    docs; **`records/` is never archived** — it is the audit trail and retention is a legal clock
    (`rules/documents.md`); Decision Records retire by `Status: CLOSED`.
  - `game-hosting` archives superseded `docs/procedures/` and `docs/guides/`; **live operator material
    is never archived** (`docker-compose.yml`, `*.env.example`, `README.md`) — a retired setting is
    removed in a commit naming its decision record, so an operator is never pointed at a setting that no
    longer exists.
  - `tech-writing` splits the tree: `docs/archive/<subpath>/` for project documents and
    `documents/archive/<type>/` for superseded deliverables; the document id and number are never
    reused; the `classification:` label and git-ignore rules travel with the file; **a `released`
    deliverable gets no banner**, because `rules/documents.md` makes it immutable — the document-map row
    with the 🗄️ marker plus the superseding document's change note carry the record.
- **Layout guides carry the archive**: `docs/archive/` in all four `agent/project_layout.md` trees
  (`documents/archive/` in tech-writing), each with a frozen-history guard; the four
  `docs/agent-contract/base-contract.md` pages gained a "Document archiving" rationale section, and
  `docs/authoring/core-sync.md`'s section map names the new slot section.

Manifests (four personas + root) go `1.1.0 → 1.2.0`: a new section is a minor bump. `tools/check_sync`
passes: the section is a slot, its heading text is identical in all five copies, and no `core` section
moved.

The next entry starts when the next contract change lands on `main`.

## [1.1.0] - 2026-11-10

Tagged `contracts-v1.1.0`. All four persona manifests and the root dogfood manifest read
`version: 1.1.0`.

### Added

- **Core: mechanical session-continuity triggers** (all personas + root copy, 2026-11-07). The
  `Session continuity` section stops relying on judgment: any verified command run (pass *or*
  fail), any file created, rewritten or substantially edited, any completed feature and any topic
  switch is an update trigger for `agent/STATUS.md`; a frequency guard forces the write-up after
  five tool calls without one. "Too small to record" is explicitly closed off, and a milestone is
  no longer the unit of work.
- **Core: observable stamp.** The HANDOFF block gains a `last_update:` field, so staleness has a
  value to compare against instead of a hunch.
- **`tools/status_fresh`** (2026-11-07) — the memory-freshness probe: compares the HANDOFF
  `last_update:` against `agent/STATUS.md`'s modification time; exit 0 when current, warning and
  non-zero exit when the stamp is stale, in the future, or missing. Stdlib Python, covered by the
  pytest suite, and run by this repo's own contract at session start and before session end.
- **`game-hosting` persona** (2026-11-07) — dedicated game server hosting: base contract with
  version pinning and save-data protection, `docker_compose.md`, `steamcmd.md`, `web_frontend.md`
  with fail-closed authentication and TLS, and verification against upstream truth.
- **`tech-writing` persona** (2026-11-09) — professional document authoring for IT managers and IT
  administrators: technical designs, advisories, product and feature comparisons, and the briefing
  material around them. Modules: base, verification, classification, documents, open_questions,
  output_formats, comparisons, advisories, visuals, dr.
- **`rules/classification.md`** (tech-writing, always-on, 2026-11-09) — the document license
  picker is replaced by a four-tier distribution ladder, each tier with a canonical statement
  printed on page one and mapped to FIRST TLP:2022 for security recipients: `Public` (CLEAR),
  `Client-shareable` (AMBER), `Internal` (AMBER+STRICT, the default), `Restricted` (RED). The
  three named leaks are closed: derivatives inherit the parent's tier (excerpts, slide cut-outs,
  standalone figure exports, quotations landing in a comparison cell); a document set takes its
  most restrictive label; agent memory (`REPO-MAP.md`, `STATUS.md`) inherits the tier, so a
  `Restricted` set keeps titles and pointers in it, never the facts. Widening a label is recorded
  in a Decision Record *before* the label is applied — no approval gate.
- **Rationale pages**: `classification-and-distribution.md` (tech-writing) and the memory-guard
  sections in the iac / administrative rationale pages.

### Changed

- Licensing is demoted to what it is actually for: rights in third-party material (`rights:`
  entries, travel at every tier) and the code a project ships (`licenses/` stays for generator and
  export scripts). Documents carry a classification tier and a distribution statement, not a
  license.
- The tech-writing `sensitivity:` field is folded into `classification:`; the persona's bootstrap
  step 2 asks the classification question (default `Internal`, non-blocking) in place of the
  license question, and `agent/project_layout.md` gains `distribution/` and `restricted/`.
- README, `agent/REPO-MAP.md` and `CONTRIBUTING.md` registries cover the added personas and tools.

### Removed

- The license question as a document decision in the tech-writing contract (replaced by the
  classification question). Licensing stays in the iac, administrative and game-hosting personas,
  where it was never about documents.

## [1.0.0] - 2026-10-28

Backfilled: no `contracts-v1.0.0` tag exists. Tagging that release was proposed on 2026-11-07 and
canceled by the maintainer (recorded in `agent/STATUS.archive.md`), so the 1.0.0 entry describes the
state of the contract set as published on 2026-10-28.

### Added

- The contract set itself: self-contained drop-in agent contracts, each a folder an agent can be
  pointed at — boot pointer (`AGENTS.md` / `CLAUDE.md`), `rules/`, `agent/` boot material,
  `docs/agent-contract/` rationale. The chat is disposable; durable state lives in files.
- **`iac` persona** — infrastructure-as-code authoring: base contract, verification/test ladder,
  bootstrap lifecycle, `python.md`, `terraform_tfgrunt.md`, `ansible.md`, `web.md`, ADRs.
- **`administrative` persona** — administrative work: base contract, verification/records ladder,
  bootstrap lifecycle, `python.md`, `documents.md`, `financial.md` (audit trail), `approval.md`
  (advice-only and actable classes), Decision Records.
- **Repo-maintainer dogfood contract at the root** — this repository runs its own contract: root
  `AGENTS.md` / `CLAUDE.md`, `rules/base.md`, `rules/verification.md` and `agent/` (manifest,
  bootstrap protocol, STATUS templates). The sync problems the contracts police are the ones the
  repo would otherwise suffer itself.
- **Seam markers** (`<!-- core -->`, `<!-- slot: name -->`, `<!-- persona -->`) in every rule file,
  making shared behavior machine-checkable: core sections must be identical across personas and the
  root copy, slot headings must exist in every persona shipping the file, persona sections are free.
- **`tools/check_sync`** — the seam checker: structure, cross-persona core drift, root-copy drift,
  manifest presence and SemVer shape. Stdlib Python, self-tested by `tests/test_check_sync.py`
  including planted-drift fixtures and a real-repo pass test.
- **`tools/new_persona`** — scaffolds a contributor persona from a template with slot headings
  reset to a TODO line, a fresh manifest and a rationale stub.
- Authoring docs: `docs/authoring/core-sync.md` (marker convention, section map, one-commit rule,
  release and version policy) and `docs/authoring/persona-anatomy.md`; `CONTRIBUTING.md`; the
  README landing page; the `agent/REPO-MAP.md` + `agent/STATUS.md` memory pair with the archiving
  rule.

[Unreleased]: https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/compare/contracts-v1.2.0...HEAD
[1.2.0]: https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/compare/contracts-v1.1.0...contracts-v1.2.0
[1.1.0]: https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/compare/03851d8...contracts-v1.1.0
[1.0.0]: https://github.com/whoogsteder/Ordnung-The-AI-Agent-contract-repository/commits/03851d8
