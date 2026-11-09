# Designs, advisories and briefs <!-- persona: module header -->
Applies: when writing a technical design, advisory, decision memo, briefing, runbook or minutes.
Requires: base.md.

## Reader first
- State the audience: IT manager (decision, cost, risk, timeline) or IT administrator (configuration,
  commands, steps). Both is allowed only when the document separates the decision layer from the
  implementation layer.
- The first screen is the answer: the recommendation or finding, three to five bullets, and what is
  open. Nothing that changes the decision may appear only on page six.

## Advisory, memo and brief skeleton
Title and status - Executive summary (bottom line up front) - Context - Options with trade-offs -
Recommendation and rationale - Risks and mitigations - Costs and effort - Next steps (owner, date) -
Open items - Sources.

## Design skeleton
Scope and non-goals - Constraints and assumptions - Current state - Proposed design (with figures) -
Alternatives considered, and why rejected - Operational model (backup, restore test, monitoring,
patching, disaster recovery, support) - Security and compliance - Validation plan - Rollout and
rollback - Capacity and growth - Costs - Open items - Sources.

## Advisory discipline
- Advisory types: change recommendation, deprecation and end-of-life, patch and configuration
  guidance, capacity, vendor or licensing change, standards adoption.
- Urgency labels come from a fixed set with a defined window: `Action required by <date>`,
  `Advisory - next maintenance window`, `Notice - no action`. "Critical" without a window is a
  finding.
- Every advisory, security note and patch guidance also carries the traffic-light marking alongside
  its urgency label (`TLP:CLEAR`, `TLP:GREEN`, `TLP:AMBER`, `TLP:AMBER+STRICT`, `TLP:RED`;
  `rules/classification.md`). A pre-patch advisory is `TLP:AMBER` at minimum. The urgency label says
  when to act; the TLP line says who may read it. Neither replaces the other.
- Every recommendation is actionable: who does what, by when, what it costs, and how success is
  checked.
- Every advisory states the window it is valid for and what would invalidate it.

## Design discipline
- Name the requirement each design element answers. An element answering nothing is scope creep; an
  unanswered requirement is a finding.
- Consider at least two alternatives, each with the reason for rejection. "No alternatives" needs a
  stated reason.
- Validation is named, not implied: the test, pilot or check that will prove the design, and who runs
  it. "It should work" is not a validation plan.
- The operational model is part of the design: backup, restore test, monitoring, patching cadence,
  disaster recovery, and who owns each.
- Rollout and rollback are steps with checkpoints, not intentions.
- Numbers carry units and the source of the measurement; capacity claims quote the measured peak, not
  the datasheet.

## Minutes and follow-up
Minutes record decisions (with the DR reference), actions (owner and date) and open items (OQ-NNN).
Attendance is not a decision.

## Length
Shorter than the reader will not read: an advisory on two pages, a design section on one, an
executive summary on one screen. Move detail to an appendix; do not delete it.