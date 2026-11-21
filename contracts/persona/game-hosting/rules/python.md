# Python <!-- persona: module header -->
Applies: when the project contains Python code (the panel, a probe or generator, helper tooling).
Requires: base.md, verification.md. Most of the code may be AI-written and reviewed by an operator
who reads Python but did not write it: optimize for reading, and let the type checker and the
gate below carry what a reviewer cannot hold in their head.

## Toolchain & dependency discipline
- Declare the Python version in `pyproject.toml` (`requires-python`) and pin the base image to that
  same minor version by tag **and** digest; a Python bump is its own commit (see `base.md` → State &
  change history).
- `uv` manages dependencies: `pyproject.toml` plus a committed `uv.lock`. Images install with
  `uv sync --frozen --no-dev`, so the lock's hashes decide what is installed. Never `pip install` an
  unpinned package in a Dockerfile.
- Keep the dependency graph small and stdlib-first. Every third-party package has a stated reason
  to exist; prefer ~10 lines of code over a new dependency. No framework whose dev server, reload
  mode or debug routes can be reached through a published port (`web_frontend.md`).
- The committed `uv.lock` is reviewed as supply-chain surface, like any image digest.

## Project layout
```
<service>/
├── pyproject.toml / uv.lock   # one project per deployable image
├── src/<package>/
│   ├── __main__.py            # wiring only: load config, construct deps, serve
│   ├── config.py              # env parsed and validated once, at start
│   └── <domain>/              # one module or package per responsibility
├── tests/                     # pytest, mirroring src/<package>/
└── Dockerfile                 # multi-stage: pinned builder → slim pinned runtime
```
- Modules are named for what they provide, not what they contain (`backups`, not `utils`). A
  `utils` or `helpers` module is a finding: move each symbol to the module that owns it.
- A tool that is not part of the runtime (probe, generator, linter) is its own entry point. It is
  never reachable through a published port, and what it produces is a file a human reviews and
  commits before the runtime reads it.

## Language rules
- Type hints on every function and attribute; the type checker runs in strict mode and is clean.
  `Any` does not cross a module boundary. Every `# type: ignore` / `# pyright: ignore` names the
  error code and carries a one-line reason.
- Data crossing a boundary — env, files, HTTP bodies, per-game definitions, container-runtime API
  responses — is parsed into typed, validated models at the edge. Inside, only typed objects move.
- Raise specific exceptions with context (`raise BackupError(f"archive {name}: {exc}") from exc`).
  No bare `except:`, no `except Exception: pass`. Only the entry point decides to log and exit.
  `assert` is for tests, never for runtime checks.
- Async code never runs blocking I/O on the event loop (`asyncio.to_thread` or a sync worker).
  Every task has an owner and a cancellation path (`asyncio.TaskGroup`); no fire-and-forget
  `create_task`.
- `subprocess` takes an argument list, never `shell=True`, never an operator-supplied string as
  the program, and always a timeout.
- `pathlib` for paths. Any path built from input is resolved and checked against its allowed root
  (`resolve()` + `is_relative_to()`) before use. `open(..., encoding="utf-8")`. `yaml.safe_load`
  only. `secrets` for tokens, never `random`.
- ≤ 100 characters per line, formatted by the formatter, not by hand.

## Configuration & secrets
- All configuration arrives via env (`docker_compose.md` → Env-file config model); parse and
  validate it once at start into a typed settings object, and fail fast with a plain-language
  message naming the variable and the file to edit (`usability.md`). No env reads scattered through
  handlers.
- Secrets are held in a secret type (e.g. `SecretStr`), never logged, never returned in an HTTP
  response, never written to an audit line or error message. Logging redacts known secret keys on
  purpose.
- Fail-closed defaults follow `web_frontend.md`: a missing, default or placeholder admin credential
  means refuse to boot, not warn-and-serve.

## HTTP & runtime hygiene
- Serve with a production server; reload and debug off. Interactive API docs and schema routes are
  disabled on published ports unless they sit behind authentication by decision.
- Limit and validate every request body and every path segment used for file access. The auth,
  CSRF, rate-limit and security-header layers `web_frontend.md` requires wrap every route.
- Container-runtime access lives in one module that exposes only the allowlisted operations; a test
  fails when any other module imports the runtime client.
- Structured JSON logs to stdout at the request boundary: method, route template (not the raw
  path), status, duration. No `print` debugging left in shipped code.
- Durations, cron expressions and ports are parsed explicitly and parse errors surfaced; never
  fall back silently to a default that hides a typo in the env file.

## Testing
- pytest; test names state behaviour, not the function name. Parametrize table-like cases.
- Container-runtime and filesystem side effects sit behind an interface (`typing.Protocol`) so unit
  tests never need Docker. Real-Docker checks belong to the higher tiers in `verification.md`.
- A fix ships with a regression test that fails without it (`verification.md` → Tests).

## Verification gate — commit-blocking
Definition of done for any Python change. Run from the project root with the tool versions pinned
in the lock's dev group, in this order; **all** must pass before committing:
```
uv run ruff format --check .    # no diff
uv run ruff check .             # clean
uv run pyright                  # strict, 0 errors
uv run pytest -q                # pass
uv run pip-audit                # no known-vulnerable package in the locked set
docker build .                  # image builds; runs non-root with a read-only rootfs
```
- Suppressions (`# noqa`, `# type: ignore`) need an inline reason and stay on a debt list to remove;
  no rule switched off project-wide.
- CI runs exactly these commands, so nobody holds a private definition of "clean". If a scanner
  cannot reach its database in the current environment, say so — never imply a clean scan that did
  not run.

## Documentation & comments
- Every module starts with a docstring stating its purpose; every public function documents purpose,
  arguments, return value and the exceptions it raises. Comments explain *why*, per `base.md` →
  Documentation.
- Behaviour an operator can trip over (refuse-to-boot conditions, what a panel action actually runs)
  is documented in README or `docs/procedures/`, not only in code.

## DR triggers (this module)
- The web framework, the validation library, a database or ORM, a code generator, and any dependency
  without a prebuilt wheel for the target platforms — record each in `docs/decisions/` per `base.md`
  → Decision Records.
