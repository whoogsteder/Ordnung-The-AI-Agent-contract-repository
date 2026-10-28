## Python Code quality
- <= 100 chars/line. Double quotes. 4-space indent. One trailing newline at EOF.
- Imports: std → third-party → local. No unused imports/vars/params.
- f-strings over `%`/`.format`. No `# type: ignore` without justification.
- Small functions. Cyclomatic complexity <= 10. Nesting <= 3 levels.
- No magic numbers (name constants). No dead code. No commented-out code.
- No `assert` in production paths. Raise specific exceptions.
- `yaml.safe_load` only. `secrets` module for tokens/IDs (not `random`).
- `open(..., encoding="utf-8")`. `sha256` not `md5`.

## Docstrings
- Module docstring. Public functions: purpose / args / returns / raises.

## Project layout (Additive if project uses Python)
  repo-root/
  ├── src/             # Python application code
  ├── scripts/         # Stand alone or helper python scripts (e.g. a script called by Ansible)
  ├── tests/           # Unit tests
  └── requirements.txt
  
### Testing Strategy
- Unit tests with pytest in `tests/` directory

## Dependency management
- Always create `requirements.txt` (or `pyproject.toml`) to manage depencies

## Versioning
- The version lives only in `pyproject.toml`. After a version bump, re-run
  `pip install -e .` (editable installs cache the version).

## Paired docs
- `scripts/<path>/X.py` → `docs/scripts/<path>/X.md`
