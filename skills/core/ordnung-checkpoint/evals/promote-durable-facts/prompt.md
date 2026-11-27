---
tags: [skill-creator, ordnung-zwei]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Quick update before we move on. I've decided: 7D2D gets deployed monitor-only (logs, status, version) with no restore and no scheduled restart until there's a wrapper that forwards SIGTERM, and that goes for any future image that can't flush on stop. Also I ran `go test ./internal/dockerctl/...` and it printed `ok  panel/internal/dockerctl 0.41s`. Next thing I want is the 7D2D game definition in the panel. Please bring the agent memory up to date.

Input files: AGENTS.md, agent/PROJECT.md, agent/STATUS.md, agent/ordnung_check
