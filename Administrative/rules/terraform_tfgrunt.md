### Terraform / Terragrunt

## General principles
- Infrastructure changes must be reproducible and idempotent.
- Prefer modifying existing modules over duplicating logic.
- Reuse variables and locals before introducing new inputs.
- Every resource must have a clear purpose and ownership.
- Follow least-privilege principles for IAM/RBAC resources.
- Avoid hardcoded IDs, ARNs, subscription IDs, account IDs, IPs, and secrets.
- Use data sources where appropriate.

## Terraform quality
- Use the latest supported Terraform/OpenTofu version already defined by the project.
- Use explicit provider version constraints.
- Every variable requires: description, type, sensible default or justification for omission.
- Every output requires: description, explicit value.
- Prefer `for_each` over `count` when resources have stable identities.
- Use locals for repeated expressions.
- No unused variables, locals, outputs, providers, or data sources.
- Avoid excessive nesting in expressions.
- Avoid large monolithic .tf files.

## File organization
Prefer:
module/
├── main.tf
├── variables.tf
├── outputs.tf
├── versions.tf
├── providers.tf
├── locals.tf
└── README.md

Split resources into dedicated files once main.tf becomes difficult to navigate.

Examples:
- network.tf
- compute.tf
- iam.tf
- monitoring.tf

## State
- Remote backends only for shared environments.
- State files must never be committed.
- State locking must be enabled where supported.
- Backend configuration must be documented.

## Terragrunt
- Follow DRY principles using include blocks and shared configuration.
- Centralize provider and backend configuration whenever practical.
- Use dependency blocks instead of manually copying outputs.
- Keep environment-specific values in environment folders.
- Avoid duplicating module source definitions across environments.

Preferred structure:
live/
├── prod/
├── test/
├── dev/
└── common/

modules/
├── network/
├── compute/
└── monitoring/

## Planning and changes
Before applying infrastructure changes:
1. Validate formatting.
2. Validate configuration.
3. Review the plan.
4. Document expected impact.

Preferred command sequence:
```bash
terraform fmt -check && terraform validate && terraform plan
```
or
```bash
terragrunt hclfmt && terragrunt validate && terragrunt plan
```

## Security
Follow base.md security rules. Secrets in Vault/Key Vault/SSM/etc., never in *.tf, *.tfvars, or terragrunt.hcl. Mark sensitive outputs `sensitive = true`. Encryption where supported. Public access must be explicitly justified.

## Documentation
Follow documentation.md structure. Module docs: purpose, inputs, outputs, dependencies, example usage, operational considerations, breaking-change notes. Infrastructure changes document resources created/modified/removed, manual actions, rollback approach.

## ADR trigger
Create ADRs for provider selection, state backend choice, module structure changes, networking/IAM architecture changes, shared Terragrunt patterns (see rules/adr.md).

## Paired docs
```
modules/<path>/X/          → docs/modules/<path>/X.md
live/<env>/<stack>/terragrunt.hcl → docs/environments/<env>/<stack>.md
```
