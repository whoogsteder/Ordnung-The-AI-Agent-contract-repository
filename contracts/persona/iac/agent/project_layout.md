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
├── rules/                 # Agent rules: base.md always; one module per language/tool in use
├── docs/                  # Documentation
│   ├── archive/           # Frozen history of retired docs, mirroring the original subpath (docs/archive/guides/x.md); never read at task time — see rules/base.md, Document archiving
│   ├── architecture/      # Topic specific architecture designs (read on demand)
│   │   └── adr/           # Architecture Decision Records: NNN-<topic>.md — retired by Status: CLOSED, never archived
│   ├── guides/            # How-to documentation (read on demand)
│   └── runbooks/          # Operational procedures per scenario
├── .env.example           # Secret placeholders (real .env is git-ignored, if applicable)
├── .gitignore             # Guards: secrets, local artefacts, dev/runtime outputs
└── README.md              # Human readable landing page
```

## Tool-Specific Layouts

Tool-specific directory structures are defined in their respective rules modules and apply only when that tool is in use. See the "Project layout" section of each applicable module for details.
