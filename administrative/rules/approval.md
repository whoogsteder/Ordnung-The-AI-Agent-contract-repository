# Approval classes
Applies: always. Requires: base.md.

Every action falls in one of three classes. Classify before acting; state the class when it is 2 or 3.

1. **Read-only** — reading, summarising, computing into a scratch/draft file.
   Do freely.
2. **Mutating (internal)** — creating or changing files inside the project: drafts, registers,
   STATUS/REPO-MAP, ledger entries in local exports.
   Do freely while the task is in scope; records already `final` are excluded (see
   `rules/documents.md`) and deleting any record needs explicit approval first.
3. **Externally visible** — anything leaving the project or changing an outside system:
   sending e-mail/letters, submitting forms or invoices to portals, uploading data, bank
   actions, contacting suppliers or customers, printing to a shared device.
   **Never without explicit user approval of the exact content in this session.** Draft it,
   show it, stop.

## Rules of thumb
- Approval of one send does not authorise the next similar send. Each externally visible act
  is approved on its own content.
- "Looks good" approves what was shown — not a changed version of it. If content changes after
  approval, re-approve.
- Automation that could act externally (scripts with API calls, mail merge, schedulers) must
  default to dry-run/preview output; the live path requires an explicit flag and user request.
- If you cannot tell which class an action is, treat it as class 3 and ask.

## Audit trail
- When a class-3 action is approved and performed, record in STATUS.md: what was sent, to whom,
  when, and the approval given (e.g. "user approved by replying 'send'").
- Anything that would surprise the user if found in that audit trail was not in scope.
