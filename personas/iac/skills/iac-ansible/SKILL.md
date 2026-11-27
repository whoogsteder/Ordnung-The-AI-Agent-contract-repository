---
name: iac-ansible
description: Ansible rules for infrastructure-as-code projects — playbook and role layout, idempotency and check-mode safety, modules over shell, inventory and group_vars, vault for secrets, collections (pinned, vendored or forked), running playbooks from Python as child processes, and the paired doc for every playbook. Use this whenever you write or change a playbook, role, inventory, vault reference or collection dependency, wrap Ansible in a CLI or form, or debug an Ansible run against a device.
---

# Ansible

## Layout
```
playbooks/            playbooks (or package data, if the application ships them)
roles/                roles
inventory/            inventory and inventory/group_vars/
vault files           encrypted; their keys come from env or a key file, never from git
```
A layout deviation, such as playbooks shipped inside a Python package, is recorded once in the
REPO-MAP.

## Rules
- **Idempotent and check-mode safe.** A second run reports no change. `--check` mutates
  nothing; a task that cannot honour check mode says so, and is skipped in check mode.
- **Use a module whenever one exists.** `shell:` and `command:` need `changed_when` and
  `failed_when`, plus a comment saying why no module fits.
- **No secrets in playbooks, defaults or vars files.** Use vault references or environment
  lookups. Use `no_log: true` on every task that handles one.
- **Pin collections and roles by version** in a requirements file. A forked or vendored collection
  records its upstream and the commit it was forked from, and is changed only in its own
  repository. Never copy collection code across the repository boundary.
- **Running Ansible from code:** run one playbook as a child process, with an argument list and
  an explicit inventory and limit. Read back a structured result, not scraped output.

## Debugging against a device
Read before you write. Record what the device answered (model, firmware, date) and what the
module sent. A difference between the module's documentation and the device's real answer is a
finding: record it, and code to the device (`iac-live`, `iac-verification`).

## Paired docs
`playbooks/X.yml` → `docs/playbooks/X.md`. The doc covers purpose, prerequisites, vars (name,
required, default, description), an example run, a dry-run example, outputs and rollback.
