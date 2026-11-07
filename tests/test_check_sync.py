"""Tests for tools/check_sync. Includes negative fixtures (planted drift)."""
import importlib.util
import os
import shutil
import subprocess
import sys
from importlib.machinery import SourceFileLoader
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
loader = SourceFileLoader("check_sync", str(ROOT / "tools" / "check_sync"))
check_spec = importlib.util.spec_from_loader("check_sync", loader)
check_sync = importlib.util.module_from_spec(check_spec)
loader.exec_module(check_sync)

IAC_CORE = """# Context discipline <!-- core -->
- shared rule line one
- shared rule line two

# Role <!-- slot: role -->
- iac role text
"""

ADM_CORE = """# Context discipline <!-- core -->
- shared rule line one
- shared rule line two

# Role <!-- slot: role -->
- admin role text
"""


def make_repo(tmp_path, iac_base=IAC_CORE, adm_base=ADM_CORE, root_rules=True, root_base=None):
    personas = tmp_path / "contracts" / "persona"
    for name, body in (("iac", iac_base), ("administrative", adm_base)):
        rules = personas / name / "rules"
        rules.mkdir(parents=True)
        (rules / "base.md").write_text(body)
        manifest = personas / name / "agent"
        manifest.mkdir()
        (manifest / "ruleset.md").write_text(f"persona: {name}\nversion: 1.0.0\n")
    if root_rules:
        rules = tmp_path / "rules"
        rules.mkdir()
        (rules / "base.md").write_text(root_base if root_base is not None else iac_base)
    return tmp_path


def problems(repo):
    return check_sync.check(repo)


def test_clean_repo_passes(tmp_path):
    assert problems(make_repo(tmp_path)) == []


def test_planted_core_drift_between_personas(tmp_path):
    drifted = IAC_CORE.replace("- shared rule line two", "- shared rule line TWO-CHANGED")
    repo = make_repo(tmp_path, adm_base=drifted)
    msgs = problems(repo)
    assert any("Context discipline" in m and "differs" in m for m in msgs), msgs


def test_planted_core_drift_root_vs_persona(tmp_path):
    root_drift = IAC_CORE.replace("- shared rule line one", "- shared rule line ONE-CHANGED")
    repo = make_repo(tmp_path, root_base=root_drift)
    msgs = problems(repo)
    assert any("root" in m and "Context discipline" in m for m in msgs), msgs


def test_unmarked_heading_detected(tmp_path):
    unmarked = IAC_CORE.replace("# Context discipline <!-- core -->", "# Context discipline")
    repo = make_repo(tmp_path, adm_base=unmarked)
    msgs = problems(repo)
    assert any("unmarked top-level heading" in m for m in msgs), msgs


def test_marker_kind_mismatch_detected(tmp_path):
    mismatched = ADM_CORE.replace("# Context discipline <!-- core -->",
                                  "# Context discipline <!-- persona -->")
    repo = make_repo(tmp_path, adm_base=mismatched, root_rules=False)
    msgs = problems(repo)
    assert any("marked differently" in m for m in msgs), msgs


def test_slot_content_may_differ(tmp_path):
    varied = ADM_CORE.replace("- admin role text", "- totally different admin role")
    repo = make_repo(tmp_path, adm_base=varied)
    assert problems(repo) == []


def test_missing_manifest_detected(tmp_path):
    repo = make_repo(tmp_path)
    shutil.rmtree(repo / "contracts" / "persona" / "iac" / "agent")
    msgs = problems(repo)
    assert any("missing manifest" in m for m in msgs), msgs


STATUS_TOOL = ROOT / "tools" / "status_fresh"


def run_status_fresh(path):
    return subprocess.run(
        [sys.executable, str(STATUS_TOOL), str(path)], capture_output=True, text=True
    )


def set_mtime(path, epoch):
    os.utime(path, (epoch, epoch))


def test_status_fresh_ok_when_mtime_not_after_stamp(tmp_path):
    status = tmp_path / "STATUS.md"
    status.write_text("## HANDOFF\nlast_update: 2099-01-01T00:00\n")
    set_mtime(status, 0)
    result = run_status_fresh(status)
    assert result.returncode == 0, result.stdout


def test_status_fresh_flags_write_that_missed_the_stamp(tmp_path):
    status = tmp_path / "STATUS.md"
    status.write_text("## HANDOFF\nlast_update: 2000-01-01T00:00\n")
    set_mtime(status, 1_700_000_000)
    result = run_status_fresh(status)
    assert result.returncode == 1
    assert "STALE" in result.stdout


def test_status_fresh_flags_missing_field(tmp_path):
    status = tmp_path / "STATUS.md"
    status.write_text("## HANDOFF\nnext_action: do the thing\n")
    result = run_status_fresh(status)
    assert result.returncode == 1
    assert "no last_update field" in result.stdout


def test_status_fresh_flags_unparseable_stamp(tmp_path):
    status = tmp_path / "STATUS.md"
    status.write_text("## HANDOFF\nlast_update: soon-ish\n")
    result = run_status_fresh(status)
    assert result.returncode == 1
    assert "unparseable" in result.stdout


def test_status_fresh_flags_absent_file(tmp_path):
    result = run_status_fresh(tmp_path / "nope.md")
    assert result.returncode == 1
    assert "not found" in result.stdout


def test_real_repo_status_is_fresh():
    """The repo runs its own contract: agent/STATUS.md must pass its own probe."""
    result = run_status_fresh(ROOT / "agent" / "STATUS.md")
    assert result.returncode == 0, result.stdout


def test_real_repo_passes():
    assert check_sync.check(ROOT) == []
