# Usability for inexperienced operators <!-- persona -->
Applies: always. Requires: base.md.

## Voice and framing
- Write for someone who has never hosted a server: define each term on first use, explain what
  a command does before telling them to run it, and state expected output ("you should see
  `container healthy` within ~2 minutes").
- Never blame the user; a wrong value they could reasonably enter is a documentation bug — fix
  the docs or add validation with a plain-language error.

## The quickstart is sacred
- README quickstart: copy-pasteable, in order, identical on Linux and Windows (mark the rare
  divergence). It ends with how to confirm the server is up — from inside and from the game.
- Every command shown must exist verbatim in the repo; no implicit `cd`, no assumed editor.

## Failure experience
- Each failure mode you hit during development becomes a README troubleshooting entry: symptom
  (paste the exact log signature), cause in one sentence, fix in steps. Include the
  "container restarts in a loop" triage path (`ps`, `logs --tail 100`).
- Error handling in shipped scripts speaks human: what went wrong, which file to edit, where to
  look if that fails — never a bare stack trace.

## Guardrails over lectures
- Prefer designs that make the dangerous thing hard: sane defaults, validation at start with
  clear messages, `.example` files that refuse nothing but explain everything.
- Destructive paths (reset, delete saves, expose publicly) get an explicit warning block in the
  docs before the steps, per base.md's confirmation rule.