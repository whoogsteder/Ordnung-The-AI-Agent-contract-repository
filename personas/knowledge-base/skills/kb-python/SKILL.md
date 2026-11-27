---
name: kb-python
description: Python rules for knowledge-base tooling — style and complexity limits, safe-by-default APIs (yaml.safe_load, subprocess argument lists, no eval or pickle, sha256 content hashes, utf-8 everywhere), docstrings, deterministic behaviour so an index rebuild is reproducible, src/tests layout, pyproject as the single version source, dependency locking, a unit tier with no network and no live backend, and the paired doc for every script. Use this whenever you write, change or review Python in the project (indexer, query path, CLI, eval and capture scripts, tests), add a dependency, bump a version, or add a script that needs its doc.
---

# Python

The indexer's output is a derivative that everything else trusts, so the code that builds it is held
to two things: it is safe with other people's files, and it is reproducible.

## Style
- Lines are at most 100 characters. Use double quotes, a 4-space indent and one trailing newline.
- Order imports standard library, then third-party, then local. Leave no unused imports, variables
  or parameters. The project's linter (ruff) and type checker (mypy) are the judges; run both.
- Use f-strings. A `# type: ignore` needs a reason on the same line.
- Keep functions small: cyclomatic complexity at most 10 and nesting at most 3 levels.
- Name your constants; no magic numbers — including score thresholds and batch sizes, which are also
  declared in configuration (`kb-retrieval`). No dead code and no commented-out code.
- Docstrings: one per module, and one per public function saying its purpose, args, returns and
  raises.

## Safe by default
- `yaml.safe_load` only. Never `eval`, `exec` or `pickle` — including for cached embeddings: a cache
  file is parsed as data, never unpickled.
- Run `subprocess` with an argument list. Never `shell=True`.
- Resolve every path against a declared root before opening it (`kb-scope`); corpus content is data,
  never a path to follow or a command to run.
- Use `secrets` for tokens and IDs, never `random`. Hash content with `sha256`, never `md5`: the hash
  is the chunk identity and the cache key, so it must be stable and collision-resistant.
- Open files with `open(..., encoding="utf-8")`.
- No bare `except:`. Raise specific exceptions — the caller branches on error kind (`kb-interfaces`) —
  and never use `assert` in production paths.
- Read secrets from the environment or a vault at the point of use. Never put one in a log line, an
  exception message, a default value or a fixture (kernel rule 12).

## Reproducible
- A rebuild from the same committed files produces the same index. Sort before hashing or emitting;
  no wall-clock timestamp, locale or dict-order dependence in anything that lands in the index.
- Anything that varies the result — model, version, chunking version — is recorded with the output,
  not remembered (`kb-corpus`).

## Layout
```
src/<package>/     indexer, query path, tooling
scripts/<area>/    standalone helpers (rebuild, backfill, eval runs, capture lint)
tests/             pytest; the unit tier runs with no network and no live backend
pyproject.toml     the version and dependencies (single source), plus a lock file
```
Put a directory in place only together with the code that needs it. Anything that needs a backend
carries a marker (e.g. `integration`), and default CI excludes it. Recorded backend responses used as
fixtures carry their provenance (`kb-eval`).

## Versions and dependencies
- The version lives only in `pyproject.toml`. After bumping it, reinstall any editable install,
  because editable installs cache the version.
- Lock dependencies. The lock file is a reviewed input: commit it and review it in the PR. A new
  dependency needs a reason in the PR, and its licence must fit the project's licence.

## Paired docs
`scripts/<path>/X.py` → `docs/scripts/<path>/X.md`. The doc covers purpose, prerequisites,
arguments, an example run, outputs and failure modes. A script without its doc is not done.
