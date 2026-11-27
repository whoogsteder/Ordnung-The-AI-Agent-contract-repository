# TASKS

The work board. Every open task lives here and nowhere else (`ordnung-board`). STATUS.md holds
the one task in hand (`task: T-NN`); PROJECT.md holds what must stay true across tasks.

One task per line: `- [T-NN] title — owner: agent|owner|both — ref: <REQ/decision IDs>`, then
indented detail: `after: T-NN`, `done: <checkable criterion>`, at most a few lines of context.
The section is the status: move the line, never copy it. IDs are never reused.

## NOW

- [T-09] Implement batching (DR-005) and agent/estimates.md — owner: both — ref: DR-005
    Operator accepted DR-005 2026-11-27 to field-test in project B today. Branch feat_dr005_batching.
    done: PR merged; checker counts a batch as one NOW slot and checks estimates lines;
    ordnung-board and iac-release describe proposing, shipping and breaking up a batch.
- [T-07] Port the knowledge-base persona from v1 — owner: both — ref: REQ-06
    Operator picked knowledge-base first from the remaining v1 personas (split: the rest are T-12).
    Source: `contracts/persona/knowledge-base/` at tag `contracts-v1.4.0`, condensed into skills.
    done: `personas/knowledge-base/` with persona.md + skills, `docs/lineage.md` and README rows
    added, CHANGELOG entry under [Unreleased], `pytest tests/` and `agent/ordnung_check` green.
    Pushed as PR #20; closes on merge.

## NEXT

- [T-02] Eval iteration 2 for resume/checkpoint/delegate — owner: agent — ref: REQ-06
    Fixtures to the TASKS.md / open-decisions format; companion skills installed; harder
    checkpoint case (a durable fact not phrased "from now on"); delegate report-length assertion.
    done: iteration-2 benchmark with at least one discriminating assertion per case.
- [T-03] Test skill discovery per harness (Claude Code, OpenCode first) — owner: both — ref: REQ-02
    The four-step probe in docs/harness-matrix.md; record results in its Tested column.
    done: Tested column filled for at least two harnesses.
- [T-04] Eval cases for adv-* from field test A — owner: agent — ref: REQ-06
    done: one case per adv skill, run with and without the skill.
- [T-05] Eval cases for ordnung-board and iac-* from field test B — owner: agent — ref: REQ-06
    after: T-02
    done: cases for claim, split and close on a board; one iac-live safety case.

## LATER

- [T-06] Port iac-web from v1 web.md — owner: agent
    When field project B starts its web scaffold.
- [T-12] Port the remaining v1 personas (administrative, review) — owner: both
    Operator picks the order; research and document-writing are already folded into advisory.
    knowledge-base was split out as T-07 and ported first.
- [T-13] Eval cases for the kb-* persona skills — owner: agent — ref: REQ-06
    after: T-07
    One case per kb skill, run with and without the skill; the kb-retrieval case must fail a
    baseline that treats an endpoint answering 200 as proof of quality.
    done: one case per kb skill with a discriminating assertion, graded into grading.json.
- [T-08] Description optimisation for the core skills (skill-creator) — owner: agent
    after: T-02
- [T-11] Retire met/dropped REQs: checker flag after ~14 days, ledger review step — owner: agent
    Watch item from feedback 2026-11-26; build only if field use shows the gap.

## WAITING

- [T-10] Release contracts-v2.0.0 (final) — owner: both — ref: DR-006
    waits: field feedback from A and B on the rc; personas to 1.0.0 at that point.
