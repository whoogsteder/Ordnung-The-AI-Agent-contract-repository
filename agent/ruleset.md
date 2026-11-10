# Contract manifest — repo-maintainer persona

persona: repo-maintainer
version: 1.2.0
core_source: contracts/persona/iac v1.1.0 (core sections), contracts/persona/administrative v1.1.0
  (the 1.2.0 change is the `slot: documentation` Document archiving section; the core sections are
  untouched, so the provenance stays v1.1.0)
bootstrapped: 2026-10-28

This repository runs its own contract. The core sections in `rules/base.md` are copies of the
contract core and follow the same sync rule as personas: a commit that changes a
`<!-- core -->` section here must change it in all contract personas in the same commit
(`tools/check_sync` enforces this across `contracts/persona/`; keep this root copy in step).

Modules: base.md (always), verification.md (always).
