# Field-test feedback

The operator's reports from using Ordnung-Zwei on real projects. Each entry holds what was
observed and what came of it: a decision record, a board task, or "watch". Project names are
generic on purpose: this repository is public. Field projects:
- **A**: an advisory-document repo (advisory persona; run on Qwen3.8-flash via OpenCode,
  self-hosted).
- **B**: an IaC firewall-management tool (iac persona; migrated from v1 on 2026-11-26).

## 2026-11-26: advisory persona, project A
- **Observed:** it spent a good deal of time on research, as it should, and produced a fairly
  brief advisory with detailed decision annexes. The v1 attempt at the same document was about
  28,000 words.
- **Outcome:** a keeper in its current state. No change.

## 2026-11-26: the migration review, project B
- **Decision index.** The operator asked whether storing every decision in PROJECT.md is
  context bloat for large projects. It is.
  - Outcome: DR-004 (only open decisions in PROJECT.md).
- **NOW cap.** The operator reduced it to 2 agent tasks, because "going by the capacity of a
  self-hosted inference engine, more isn't that realistic".
  - Outcome: DR-003.
- **Task processing:** "seems good in this version. Actual use will tell."
  - Outcome: watch.

## 2026-11-26: PROJECT.md growth
- **The question:** can PROJECT.md grow very big, or is it meant to replace ADRs? It is not a
  replacement; most entries pass through and leave it.
- **Gap found:** met or dropped REQs can linger, and nothing forces the review that would remove
  them. A candidate fix: the checker flags met or dropped REQs older than about 14 days, and
  `ordnung-ledger` gains a "promote or retire" step at each board review.
- **Outcome:** the operator chose to use it as it is and report back. Watch.

## 2026-11-27: iac persona, project B
- **Observed:** it is working well, and the task structure works as intended. But "occasionally
  it works too well": low-effort tasks each get their own branch, PR and reviewed merge. The
  operator has instructed the agent several times to do a set in one go.
- **The pain is the merge:** every merge to main needs a second reviewer on the company GitHub.
- **Outcome:** DR-005 (PROPOSED). It includes `agent/estimates.md`, so that misjudged estimates
  leave a record that feeds the improvement process.

## What to watch (from the 2026-11-26 hand-over)
- **Resume after a compaction or a new session.** Does the agent reload the HANDOFF `skills:` and
  restate the `constraints:` before acting?
- **The board.** Does new work land on the board, not in STATUS notes or chat?
- **PROJECT.md.** How fast does it grow towards its cap, and do met REQs get removed?
- **Live safety.** Acceptance before production, and the operator's go before each step.
