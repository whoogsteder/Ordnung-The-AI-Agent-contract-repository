---
name: iac-python
description: Python rules for infrastructure-as-code tooling — style and complexity limits, safe-by-default APIs (yaml.safe_load, subprocess arg lists, no eval or pickle, TLS on), docstrings, src/scripts/tests layout, pyproject as the single version source, dependency locking, and the paired doc for every script. Use this whenever you write, change or review Python in the project (engine code, CLI, helper scripts called by Ansible, deploy scripts, tests), add a dependency, bump a version, or add a script that needs its doc.
---

# Python

## Style
- Lines are at most 100 characters. Use double quotes, a 4-space indent and one trailing newline.
- Order imports standard library, then third-party, then local. Leave no unused imports, variables
  or parameters. The project's linter (ruff) and type checker (mypy) are the judges; run both.
- Use f-strings. A `# type: ignore` needs a reason on the same line.
- Keep functions small: cyclomatic complexity at most 10 and nesting at most 3 levels.
- Name your constants; no magic numbers. No dead code and no commented-out code.
- Docstrings: one per module, and one per public function saying its purpose, args, returns and
  raises.

## Safe by default
- `yaml.safe_load` only. Never `eval`, `exec` or `pickle`.
- Run `subprocess` with an argument list. Never `shell=True`.
- Use `secrets` for tokens and IDs, never `random`. Hash with `sha256`, never `md5`.
- Open files with `open(..., encoding="utf-8")`.
- No bare `except:`. Raise specific exceptions, and never use `assert` in production paths.
- Default to HTTPS, and never turn off TLS verification without a documented reason. Prefer
  pinning a certificate over disabling the check.
- Read secrets from the environment or a vault at the point of use. Never put one in a log line,
  an exception message, a default value or a fixture.

## Layout
```
src/<package>/     application code
scripts/<area>/    standalone helpers (e.g. called by Ansible, deploy or lab scripts)
tests/             pytest; the unit tier runs with no network and no device
pyproject.toml     the version and dependencies (single source), plus a lock file
```
Put a directory in place only together with the code that needs it.

## Versions and dependencies
- The version lives only in `pyproject.toml`. After bumping it, re-lock (`uv lock`) in the same
  commit, because the lock records the project's own version, and reinstall any editable install,
  because editable installs cache the version.
- A unit test asserts the lock records the `pyproject.toml` version. `agent/ordnung.toml` lists the
  lock tool's check under `[hook] run` (e.g. `uv lock --check`), so the pre-commit hook runs it.
- Lock dependencies. The lock file is a reviewed input, so commit it and review it in the PR. A
  new dependency needs a reason in the PR, and its licence must fit the project's licence.

## Paired docs
`scripts/<path>/X.py` → `docs/scripts/<path>/X.md`. The doc covers purpose, prerequisites,
arguments, an example run, outputs and failure modes. Code comments explain how a line works;
docs explain what to run and what it means. A script without its doc is not done.
