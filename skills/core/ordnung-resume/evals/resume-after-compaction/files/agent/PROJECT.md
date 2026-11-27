# PROJECT — what must stay true across tasks

## Purpose
Docker Compose stack for an Enshrouded dedicated server plus a bundled web panel, for a
non-technical operator.

## Standing requirements
- REQ-01: Quickstart works verbatim on Linux and Windows — user, 2026-11-02 — active
- REQ-02: Never test against the live save in ./data/savegame — user, 2026-11-10 — active

## Decisions
- none yet

## Waiting on the user
- Q-01: Backup schedule in UTC or local time (Europe/Amsterdam)? — blocks T-7 deploy — since 2026-11-24

## Tracks
- Backups — scheduled backups via BACKUP_CRON — docs/procedures/backup.md

## Task queue
- T-8 restore drill procedure

last_reviewed: 2026-11-24
