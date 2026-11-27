---
tags: [skill-creator, ordnung-zwei]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

I want every hard-coded port number in this repo (compose, scripts, panel code, docs) found and replaced by the env variable, but the repo is big and I don't want your context wasted on it. Write the exact brief you'd hand to a subagent for this job and save it as brief.md. Don't launch the subagent yet, I want to read the brief first.

Input files: AGENTS.md, agent/PROJECT.md, agent/STATUS.md, agent/ordnung_check
