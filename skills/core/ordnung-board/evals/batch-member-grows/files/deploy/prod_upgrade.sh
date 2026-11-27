#!/usr/bin/env bash
# Production upgrade: run by the operator from a release tag (REQ-01).
set -eu
docker exec netctl-db pg_dump -U netctl netctl > "backup-$(date +%F).sql"
docker compose -f deploy/compose.prod.yaml up -d
docker exec netctl-db psql -U netctl -c 'SELECT 1'
