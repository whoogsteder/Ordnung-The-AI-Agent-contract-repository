#!/usr/bin/env bash
set -eu
cp -R "$(dirname "$0")/files/." .
# STATUS was written at its own stamp, so the freshness check passes at the start.
touch -t 202611270900.00 agent/STATUS.md
