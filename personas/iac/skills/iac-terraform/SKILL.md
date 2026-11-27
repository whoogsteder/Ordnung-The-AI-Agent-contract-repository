---
name: iac-terraform
description: Terraform, OpenTofu and Terragrunt rules — module structure and file split, variables and outputs, provider pinning, remote state with locking, environment layout and DRY Terragrunt includes, the fmt/validate/plan sequence before any apply, security (no secrets in tf or tfvars, least privilege, sensitive outputs) and module docs. Use this whenever you write or change .tf or terragrunt.hcl files, add a provider or module, touch state or backends, or plan or apply infrastructure.
---

# Terraform / OpenTofu / Terragrunt

## Principles
- Changes are reproducible and idempotent. Change an existing module before you duplicate one.
- Every resource has a clear purpose and owner. IAM and RBAC follow least privilege.
- Never hard-code IDs, ARNs, subscription or account IDs, IPs or secrets. Use variables or data
  sources instead.

## Quality
- Use the Terraform/OpenTofu version the project already pins, and give every provider an
  explicit version constraint.
- Every variable has a description, a type, and a sensible default or a stated reason it has
  none. Every output has a description.
- Prefer `for_each` over `count` when items have stable identities. Put repeated expressions in
  locals. Leave nothing unused.
- Split files as `main.tf`, `variables.tf`, `outputs.tf`, `versions.tf`, `providers.tf`,
  `locals.tf`, plus area files (`network.tf`, `iam.tf`, ...) once `main.tf` gets hard to read.

## State
- Shared environments use a remote backend with locking. Document the backend configuration.
- **Never commit a state file.** Never edit state by hand without the owner's go; `terraform
  state` operations count as destructive (kernel rule 7).

## Terragrunt
- Keep it DRY with `include` blocks, and centralise the provider and backend settings. Use
  `dependency` blocks instead of copying outputs across.
- Layout: `live/<env>/<stack>/`, where `<env>` is dev, test, prod or common, plus `modules/<area>/`.

## Before any apply
1. `fmt -check`, then `validate`, then `plan` (or `hclfmt`, `validate`, `plan` with Terragrunt).
2. Review the plan: resources created, changed and destroyed. Write the expected impact into the
   PR or HANDOFF.
3. Apply only with the owner's go, against the environment the task names, from a tagged release
   for anything shared (kernel rules 10 and 12).

## Security and docs
- Secrets live in Vault, Key Vault, SSM or similar, never in `*.tf`, `*.tfvars` or
  `terragrunt.hcl`. Mark sensitive outputs `sensitive = true`. Turn on encryption wherever the
  service supports it. Public exposure needs a written reason.
- `modules/<path>/X/` → `docs/modules/<path>/X.md`, covering purpose, inputs, outputs,
  dependencies, an example, operational notes and breaking changes.
- Provider choice, the state backend, module structure, and network or IAM architecture are
  decisions that need an ADR (`ordnung-ledger`).
