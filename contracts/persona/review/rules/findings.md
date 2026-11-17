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
When unsure between two levels, pick the higher one and say why.

## Each finding
`R-NN | severity | where (section, table row, page) | what is wrong | evidence | suggested fix`

- **Evidence** is a source quote with its id, a contradiction between two places in the artefact, or
  the checklist item that failed. "Seems off" is not evidence.
- **Suggested fix** says what would make the finding go away. It does not rewrite the artefact.

## The report
Write to `reviews/<artefact>/review-<artefact-version>.md`:
1. **Verdict**: `pass`, `pass with fixes` (no blocking findings), or `fail` (one or more blocking
   findings). Give it in one line, with counts per severity.
2. **Scope**: the artefact and version, the yardstick used, the checklists applied, and whether facts
   were re-checked.
3. **Must-have table** (when list C applied), built by the reviewer from the sources.
4. **Reader summary** (when list D applied): what the reader takes away from page one, in the
   reviewer's words.
5. **Findings**, blocking first.
6. **Not checked**: anything out of scope or unreachable (a source behind a login, for example).

Keep the report short. It lists what is wrong, and leaves out what is fine and the reviewer's own
opinions about style.

## After the author's fixes
A re-review checks every earlier finding (`fixed`, `not fixed`, `partly`) and runs list B again on any
changed fact. Write it as a new report version. Earlier reports are kept.
