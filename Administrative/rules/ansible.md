## Ansible
- Playbooks in `playbooks/`. Roles in `roles/`.
- Every playbook has a paired doc: `docs/playbooks/<name>.md`.
  Covers: purpose, prerequisites, vars (name/required/default/desc), example run,
  dry-run example, outputs, rollback.
- Idempotent. `check_mode` safe. No `shell:` when a module exists.
- Inventory in `inventory/`. Group vars in `inventory/group_vars/`.

## Project layout (Additive if project uses Ansible)
  repo-root/
  ├── playbooks/          # Ansible playbooks
  ├── roles/              # Ansible roles
  ├── inventory/          # Inventory + group_vars
  └── vault               # Ansible vault file(s)

## Paired docs
- `playbooks/X.yml` → `docs/playbooks/X.md`