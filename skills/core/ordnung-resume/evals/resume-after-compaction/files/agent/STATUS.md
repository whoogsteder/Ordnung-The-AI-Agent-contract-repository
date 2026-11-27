# STATUS — the task in hand

## HANDOFF
task: T-7 scheduled backups via BACKUP_CRON
status: IN_PROGRESS
next_action: Write the chosen schedule into enshrouded.env.example and deploy with docker compose up -d.
skills: [ordnung-checkpoint, gh-compose]
constraints:
  - only BACKUP_CRON may change in the env file
files: enshrouded.env.example, docker-compose.yml
evidence: docker compose config → renders (2026-11-24T16:40)
last_update: 2026-11-24T16:40

## Plan
- [x] add BACKUP_CRON to the env example
- [ ] write the chosen schedule
- [ ] deploy and check crontab in the container
