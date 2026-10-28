## Python for administrative data work (Additive if project uses Python)
Applies: scripts that read/write CSV, spreadsheets, PDFs or accounting exports.

## Code quality
- <= 100 chars/line. Double quotes. 4-space indent. One trailing newline at EOF.
- Imports: std → third-party → local. No unused imports/vars/params.
- Small functions. Cyclomatic complexity <= 10. Nesting <= 3 levels.
- `open(..., encoding="utf-8")`. `csv` module over hand-split lines. `datetime.date` for dates.
- Money is `decimal.Decimal` or integer cents — never `float`. No magic numbers: rate, VAT and
  rounding rules are named constants sourced from project config.
- `yaml.safe_load` only. `secrets` module for tokens/IDs (not `random`).

## Data-file discipline
- Source exports (bank CSV, accounting dumps) are read-only inputs. Scripts write to new files;
  never modify an export in place — it is the evidence record others reconcile against.
- Every script that produces financial output prints or writes a summary: row counts in/out,
  sum per currency, and any skipped rows with reasons. Silent skips are forbidden.
- Generated files are deterministic where possible (sorted keys/rows) so reruns diff cleanly.

## Project layout (Additive if project uses Python)
  repo-root/
  ├── scripts/         # Data-processing and document-generation scripts
  ├── tests/           # Unit tests (pytest)
  └── requirements.txt

## Testing Strategy
- pytest in `tests/`, using small fixture exports that mirror the real export columns with
  redacted/synthetic values (label them synthetic; record real column layout and date).
- Minimum checks per script: totals recomputed match output; VAT math on a known case;
  empty-input and unknown-counterparty cases fail loudly.

## Dependency management
- Always create `requirements.txt` (or `pyproject.toml`) to manage dependencies. Pin versions.

## Paired docs
- `scripts/<path>/X.py` → `docs/scripts/<path>/X.md` (input file expected, command, output produced).

