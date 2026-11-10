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
├── rules/                 # Agent rules: base.md always; one module per record type/tool in use
├── docs/                  # Documentation
│   ├── archive/           # Frozen history of retired docs, mirroring the original subpath (docs/archive/procedures/x.md); never read at task time — see rules/base.md, Document archiving
│   ├── decisions/         # Decision Records: NNN-<topic>.md — retired by Status: CLOSED, never archived
│   ├── guides/            # How-to documentation (read on demand)
│   └── procedures/        # Step-by-step operational procedures per scenario
├── templates/             # Document templates (quotes, invoices, letters) — see rules/documents.md
├── records/               # Working records: drafts and finals by type/year (see rules/documents.md)
│   ├── quotes/
│   ├── invoices/
│   └── correspondence/
├── data/                  # Structured data: exports, ledgers, master data (see rules/python.md)
│   ├── counterparties/    # Master data — single source of truth per counterparty
│   └── imports/           # Read-only source exports (bank CSV, accounting dumps)
├── .env.example           # Secret placeholders (real .env is git-ignored, if applicable)
├── .gitignore             # Guards: secrets, personal data, local artefacts
└── README.md              # Human readable landing page
```

## Record-handling guards
- `data/imports/` files are evidence: read-only inputs, never edited in place.
- `docs/archive/` is frozen history: never edited, never read during task work, cited only with the
  🗄️ ARCHIVED marker (base.md, Document archiving). `records/` is the audit trail and is **never**
  archived — a final record keeps its path for its retention period (`rules/documents.md`).
- Real customer/supplier data is git-ignored unless the project declares the repository private
  (see base.md, Data handling & privacy); commit redacted samples with the same shape instead.
- Registers (number sequences and their next free number) live in `agent/REPO-MAP.md`.

## Tool-Specific Layouts

Tool-specific directory structures are defined in their respective rules modules and apply only when that tool is in use. See the "Project layout" section of each applicable module for details.
