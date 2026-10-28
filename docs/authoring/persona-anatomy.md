# Persona anatomy — how to add a contract

Status: ✅ IMPLEMENTED. A persona is a self-contained folder under `contracts/persona/<name>/`
that a user can copy into a project root and use as-is. No build step, no shared files.

## Folder shape

```
contracts/persona/<name>/
├── AGENTS.md              # boot pointer: read all of rules/ first (copy verbatim from iac)
├── CLAUDE.md              # one line: @AGENTS.md
├── .github/copilot-instructions.md
├── agent/
│   ├── ruleset.md         # manifest: persona: <name>, version: X.Y.Z  (required by check_sync)
│   ├── bootstrap.md       # new-project bootstrapping protocol
│   ├── project_layout.md  # target layout the bootstrap creates
│   └── STATUS.md          # empty contract template (HANDOFF header only)
├── rules/
│   ├── base.md            # required; every top-level heading seam-marked
│   ├── verification.md    # recommended
│   └── <tool>.md          # optional modules, one per language/tool/workflow
├── docs/agent-contract/   # rationale ("why") — never read at boot
│   └── index.md
└── licenses/              # license-picker texts (copy from iac)
```

## Steps

1. `mkdir -p contracts/persona/<name>/{agent,rules,docs/agent-contract,licenses}` and copy
   the scaffold files from `contracts/persona/iac/`.
2. Edit `rules/base.md`: rewrite the two slot sections (`slot: role`,
   `slot: state-history`) for the new persona; leave `core` sections byte-identical.
3. Keep, adapt or delete optional modules; add persona modules with `<!-- persona -->`
   markers as needed. Every top-level heading gets a marker (see core-sync.md).
4. Write `agent/ruleset.md` with `persona: <name>` and `version: 1.0.0`.
5. Rewrite `docs/agent-contract/index.md` to point at the rationale for this persona's rules.
6. Run `python3 tools/check_sync` — it must pass; unmarked headings or missing manifests fail.
7. Add the persona to the README table and `agent/REPO-MAP.md`.

## Rules of thumb

- Core changes are expensive on purpose (all personas + root copy in one commit). If a rule
  is not truly shared behavior, it belongs in a slot or persona section.
- Rule text stays generic: no project names, paths or record numbers — those live in the
  user project's `agent/REPO-MAP.md` / `agent/STATUS.md`.
- Persona folders must survive being copied alone into an unrelated project root.
