# Findings and the review report <!-- persona: module header -->
Applies: every review. Requires: base.md, `rules/checklists.md`.

## Severity
- **Blocking**: the artefact must not be used or handed on until this is fixed. Examples: a
  recommended option fails a must-have, a load-bearing fact is wrong or unsourced, the artefact answers
  the wrong question, an obvious candidate that would pass is missing.
- **Should fix**: the artefact can be used, but this makes it worse for its reader or weaker as
  evidence. Examples: an undefined term on page one, the body over budget, an unconfirmed second-tier
  fact, ids in the body.
- **Note**: a suggestion, or an observation with no defect.
- **A must-have that cannot be scored because a term in the yardstick is ambiguous**: should fix
  when the artefact names the reading it took and the other reading is implausible; blocking when the
  two readings lead to different answers and the artefact does not say which it took.
When unsure between two levels, pick the higher one and say why.

## Each finding
`R-NN | severity | where (section, table row, page) | what is wrong | evidence | suggested fix`

- **Evidence** is a source quote with its id, a contradiction between two places in the artefact, or
  the checklist item that failed. "Seems off" is not evidence.
- **Suggested fix** says what would make the finding go away. It does not rewrite the artefact.

## The report
Write to `reviews/<artefact>/review-<artefact-version>.md`:
1. **Verdict**: `pass`, `pass with fixes` (no blocking findings), `fail` (one or more blocking
   findings), or `blocked - cannot review` (the yardstick is missing, or sources a verdict depends on
   are unreachable), with the reason and what would unblock it. Give it in one line, with counts per
   severity.
2. **Scope**: the artefact and version, the yardstick used, the checklists applied, and whether facts
   were re-checked.
3. **Must-have table** (when list C applied), built by the reviewer from the sources.
4. **Reader summary** (when list D applied): what the reader takes away from page one, in the
   reviewer's words.
5. **Findings**, blocking first.
6. **Not checked**: anything out of scope or unreachable (a source behind a login, for example).

Keep the report short. It lists what is wrong, and leaves out what is fine and the reviewer's own
opinions about style.

## After the verdict
- **Hand the report to the artefact's owner** (the user, or the author's project when the user says
  so), and set the review register row in `agent/REPO-MAP.md` to `awaiting author` or `closed`.
- **A `fail` blocks the hand-over.** Say in the report which hand-over is blocked (to which writer
  or reader) and by which finding ids. If the artefact was already handed on, say so in the report
  so the owner can recall it. The reviewer does not contact the receiver itself.
- **The author may dispute a finding.** A disputed finding is marked `rejected` in the re-review, with
  the author's reason and the reviewer's reply side by side. It stays in every later report until it
  is closed; it never quietly disappears.
- **Closed** means every blocking finding is `fixed`, or the owner has accepted it as a risk in
  writing, with a date. Only a closed review is archived (`rules/base.md`, Document archiving).

## After the author's fixes
A re-review checks every earlier finding (`fixed`, `not fixed`, `partly`, `rejected`). It then
re-runs list B on every changed fact and on every must-have row that cited it. Any changed must-have
re-runs list C for every option. A fix can move a defect into a row that was not touched. If the
re-review shows an earlier finding was wrong, mark it `withdrawn - reviewer error` with the evidence.
Write the re-review as a new report version. Earlier reports are kept.
