#!/usr/bin/env bash
# Throwaway local database for development.
set -eu
docker run -d --name netctl-db -e POSTGRES_PASSWORD=dev postgres:17
