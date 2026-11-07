# Project Layout Guide

## Agent Memory Files

Use these files to externalize memory from your context. These exist in every project using this ruleset.

| File | Purpose | When to Update |
|------|---------|----------------|
| `STATUS.md` | Forward-looking session state + HANDOFF block | After file creation, command verification, feature completion, or topic switch |
| `REPO-MAP.md` | Stable file index for locating anything | Use it and update it any time a file is added/moved/removed |
| `project_layout.md` | Directory structure guide (this file) | Use it and update it when core directory layout changes |

## Universal Structure (All Projects)

```
[project root]/
├── agent/                 # AI agent externalized memory
│   ├── STATUS.md          # Session handoff + state (single source for continuity)
│   ├── REPO-MAP.md        # Stable file index — scopes the agent's reads/searches
│   └── bootstrap.md       # New project bootstrap protocol
├── rules/                 # Agent rules: base.md always; one module per tool/workflow in use
├── docs/                  # Documentation
│   ├── architecture/      # Topic specific architecture designs (read on demand)
│   │   └── adr/           # Architecture Decision Records: NNN-<topic>.md
│   ├── guides/            # How-to documentation (read on demand)
│   └── runbooks/          # Operational procedures per scenario (backup, updates, triage)
├── docker-compose.yml     # The delivery vehicle — thin: image pins, ports, volumes, env_file
├── <name>.env.example     # Full documented config surface (real *.env are git-ignored)
├── .gitignore             # Guards: secrets, save/data dirs, local artefacts
└── README.md              # Operator landing page: quickstart, settings, troubleshooting
```

## Tool-Specific Layouts

Tool-specific directory structures are defined in their respective rules modules and apply only when that tool is in use. See the "Project layout" section of each applicable module for details. Save/data directories created at runtime stay git-ignored and are listed in REPO-MAP, not committed.
