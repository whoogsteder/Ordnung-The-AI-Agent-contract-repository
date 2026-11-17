# Document types <!-- persona: module header -->
Applies: choosing the structure, the questions to ask and the page budget for a document. Requires:
base.md, `rules/requirements.md`, `rules/writing.md`.

Each profile gives the purpose, the reader, the questions to ask during the questioning session, the
skeleton of the body, the default page budget for the body, and the checks before delivery. The
skeleton is a starting point: merge or drop sections that have nothing to say. Annexes are always
allowed and do not count towards the budget.

## Architecture document
- **Purpose:** describe how a system is built and why, so it can be operated, changed and reviewed.
- **Reader:** architects and administrators; a manager reads the summary.
- **Ask about:** scope and boundaries, the requirements each part answers, interfaces and dependencies,
  security zones, operations (backup, monitoring, patching, support), growth, the alternatives that were
  rejected.
- **Body:** Summary - Context and scope - Requirements and constraints - Design (with one overview
  diagram) - Key decisions and alternatives rejected - Operations - Risks and open questions.
- **Budget:** 8-15 pages.
- **Checks:** every design element traces to a requirement; every interface is named on the diagram;
  the operations section names an owner for each task.

## Integration how-to
- **Purpose:** let an administrator connect system A to system B, start to finish, without help.
- **Reader:** an administrator doing the work.
- **Ask about:** versions on both sides, prerequisites and access rights, the environment (lab or
  production), how success is tested, how to roll back.
- **Body:** What this achieves - Prerequisites - Steps (numbered, one action each, with the expected
  result) - Test - Rollback - Troubleshooting (symptom, cause, fix).
- **Budget:** as short as the steps allow, typically 3-8 pages.
- **Checks:** every command or setting is copied from a tested run or a cited vendor document, with
  the product version; every step has an expected result; nothing is "as needed".

## Change or implementation plan
- **Purpose:** get a change approved and carried out safely.
- **Reader:** change board and manager (approval), engineers (execution).
- **Ask about:** what changes and why, impact and downtime, dependencies, the schedule and change
  windows, who does what, the test and rollback criteria, communication.
- **Body:** Summary (what, why, when, impact) - Scope - Approach and phases - Schedule - Roles - Risks
  and mitigations - Test and acceptance - Rollback - Communication.
- **Budget:** 4-10 pages. Runbook-level steps go in an annex.
- **Checks:** every phase has an entry and exit criterion; rollback has a decision point and a time
  limit; every task has an owner and a date.

## Lifecycle advisory and product selection
- **Purpose:** decide what replaces an ageing or end-of-life platform, and when.
- **Reader:** IT manager or team deciding. Engineers read the annexes.
- **Ask about:** the estate (models, counts, sites, how this is known), the lifecycle dates and their
  source, what the platform actually does today (roles, protocols, dependencies), what must change and
  what must not, growth expectations, physical constraints, vendor and supplier constraints, the
  operating model and skills, budget and timeline, and who decides.
- **Body:** Summary and recommendation - Why now (lifecycle facts) - What the replacement must do
  (must-haves in plain words) - Options considered and how they were screened - Shortlist compared -
  Recommendation, cost shape and risks - Next steps and open decisions.
- **Budget:** 6-10 pages for a single-platform selection.
- **Checks:** the must-have check of `rules/facts.md` passes for every recommended option; every
  candidate is current (not end-of-sale); the longlist includes the vendors' own reference designs
  and the compatibility lists of attached systems.

## Research brief
- **Purpose:** answer a question about a topic so the reader can form a view or decide what to
  explore.
- **Reader:** the person who asked, usually a manager or architect.
- **Ask about:** the exact question, why it is asked, the depth wanted, sources to include or avoid,
  the deadline.
- **Body:** Answer in short - Background - Findings (grouped by theme, each with sources) - What is
  uncertain or contested - Implications and suggested next steps.
- **Budget:** 3-8 pages.
- **Checks:** every finding cites a source; vendor claims are marked as such; uncertainty is named,
  not smoothed over.

## End-user guide
- **Purpose:** help a non-technical user complete a task.
- **Reader:** end users with no IT background.
- **Ask about:** who the users are, which tasks they need, the devices and versions, the language,
  where they will read it (printed, intranet, phone), who they contact for help.
- **Body:** What you can do with this - Before you start - Task sections (numbered steps with a
  screenshot where it helps) - If something goes wrong - Who to contact.
- **Budget:** 1-2 pages per task.
- **Checks:** no jargon left unexplained; every step is one action; screenshots match the current
  version; a reader can follow it without prior knowledge.

## Advisory, memo or briefing
- **Purpose:** tell a reader something they must act on: a deprecation, a patch, a licensing
  change, a capacity warning.
- **Reader:** IT manager, with an administrator as second reader where action is technical.
- **Ask about:** what happened or is coming, who is affected, the deadline, the action, the cost.
- **Body:** Bottom line and urgency - What is happening - Who is affected - What to do, by whom, by
  when - Risks of not acting - Sources.
- **Budget:** 1-2 pages.
- **Checks:** the urgency is one of `Action required by <date>`, `Advisory - next maintenance
  window`, `Notice - no action`; every action names an owner and a date; the advisory states how long
  it is valid.

## Other types
For a type not listed here (minutes, runbook, policy), agree the purpose, reader, skeleton and budget
with the user during the questioning session, and record them in the brief.
