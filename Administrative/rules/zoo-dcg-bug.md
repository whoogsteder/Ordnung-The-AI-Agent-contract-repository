# Zoo Code DCG Bug Workaround

**Issue:** `execute_command` fails with "Unable to start DCG: spawn .../dcg ENOENT" when `cwd` is passed as the string `"null"` instead of an actual path.

**Workaround:** Always pass an explicit absolute path for `cwd` in `execute_command`. Never use `"null"` or omit it expecting a default. Use `/home/whoogsteder/development/home_demo_lab` as the standard working directory.

**Example (correct):**
```json
{"command": "echo test", "cwd": "/home/whoogsteder/development/home_demo_lab", "timeout": 5}
```

See `docs/guides/zoo-dcg-bug-details.md` for full analysis and reproduction steps.