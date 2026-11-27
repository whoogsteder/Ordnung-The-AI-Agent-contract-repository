# Estimates — where a task proved bigger than predicted (DR-005)

Append-only. One line each time a task (in a batch, or on its own) turns out bigger, riskier or
less clear than predicted at claim time. The operator reads this file to improve the process
and to judge future batch proposals per agent. `agent/ordnung_check` enforces the line format:

`- YYYY-MM-DD · T-NN · <agent>/<model> · predicted: <effort, risk> · found: <what> · why: <cause> · then: <what happened to the task>`

Example:
`- 2026-11-27 · T-63 · opencode/qwen3.8-flash · predicted: low effort, low risk · found: the name is also hard-coded in the production upgrade script · why: the search was scoped to scripts/dev/ · then: out of the batch, back to NEXT as live work`

## Entries
