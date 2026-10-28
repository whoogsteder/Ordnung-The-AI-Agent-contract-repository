# Tooling modules: why per-language rules read as checklists

Companions to `rules/python.md`, `rules/terraform_tfgrunt.md`, `rules/ansible.md`,
`rules/web.md`. Start at [index.md](index.md).

## Why the modules are short and imperative

Module rules fire during work, when the agent's context is already busy. A paragraph of
reasoning per rule costs attention that the task needs; a one-line imperative does not. The
modules are therefore written as checklists — each line is testable behaviour, not advice —
and the explanations live here, where they are read by humans reviewing the contract or
agents explicitly asked "why this rule?".

The same reasoning sets the module scope: a module loads only when its language/tool is in
use (declared in REPO-MAP), so each file can assume full attention rather than compete with
the other five. That is also why modules never restate `base.md` — the base contract is
already loaded, and duplicated rules drift apart.

## Why these rules and not others

Each module concentrates on the failure modes agents actually produce in this stack:

- **Python** — agents write notebooks-style code when unconstrained: no typing, prints instead
  of logging, silent `except Exception`. The module's core is "explicit at boundaries": type
  hints, structured errors, tests co-located so a refactor cannot silently strand them.
  Virtualenv and `requirements.txt` pinning exist because an agent that pip-installs into the
  system Python poisons the next session's environment — an unreproducible environment makes
  every "it works" claim unverifiable (see verification.md).
- **Terraform/Terragrunt** — agents copy plausible HCL; without a pinning rule they also pick
  provider versions at random. Module version pins and `terragrunt.hcl` hygiene are the two
  places where a plausible-but-wrong line becomes an outage three applies later, so the module
  puts its weight there and defers style to the formatter — a machine can own what a linter
  can check.
- **Ansible** — agent-written playbooks fail in one signature way: they half-apply, then the
  next run compounds it. Hence idempotency-first rules (state not shell, `changed_when`,
  handlers over restart-tasks) and the serial/canary rollout rule: an agent cannot feel blast
  radius, so the contract feels it for them.
- **Web** — accessibility and state-management choices are exactly what agents skip under
  deadline pressure because nothing breaks visibly. Listing them as required (semantic HTML,
  keyboard paths, central store) makes omission a checkable violation instead of a silent debt.

## The shared pattern underneath all four

1. **Pin everything** (versions, dependencies, module refs) — reproducibility is the
   precondition for every other rule.
2. **Declare intent explicitly** (types, state, `changed_when`, a11y semantics) — implicit
   intent is where plausible-but-wrong output hides.
3. **Fail loudly at boundaries** (errors not swallowed, lint gates CI, plan diffs reviewed) —
   an agent's environment must reject bad work even when the agent does not notice it.

Those three are the module-level echo of the verification contract: reality gets a vote at
every boundary the agent crosses.