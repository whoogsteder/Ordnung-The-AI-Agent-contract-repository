"""Tests for tools/ordnung_check and tools/install — they exercise the real scripts and templates."""
from __future__ import annotations

import importlib.machinery
import importlib.util
import os
import time
from datetime import datetime
from pathlib import Path

import pytest

ZWEI = Path(__file__).resolve().parent.parent


def load(name: str):
    loader = importlib.machinery.SourceFileLoader(name, str(ZWEI / "tools" / name))
    spec = importlib.util.spec_from_loader(name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


check_mod = load("ordnung_check")
install_mod = load("install")

NOW = datetime(2026, 11, 25, 12, 0)


def handoff(**over: str) -> str:
    f = {
        "task": "T-1 add backup cron",
        "status": "IN_PROGRESS",
        "next_action": "Run docker compose config in the throwaway dir.",
        "skills": "[ordnung-checkpoint, gh-compose]",
        "constraints": "\n  - do not touch live saves",
        "files": "docker-compose.yml",
        "evidence": "none",
        "last_update": "2026-11-25T12:00",
    }
    f.update(over)
    return "# STATUS\n\n## HANDOFF\n" + "".join(f"{k}: {v}\n" for k, v in f.items()) + "\n## Plan\n- [ ] x\n"


def project(extra: str = "") -> str:
    return ("# PROJECT\n\n## Standing requirements\n- REQ-01: quickstart works on Linux and Windows — user\n"
            "\n## Decisions\n- none yet\n\n## Waiting on the user\n" + (extra or "- none\n"))


def make(tmp: Path, status: str, proj: str | None = None, mtime: datetime = NOW) -> Path:
    (tmp / "agent").mkdir(parents=True, exist_ok=True)
    if proj is not None:
        (tmp / "agent/PROJECT.md").write_text(proj)
    s = tmp / "agent/STATUS.md"
    s.write_text(status)
    os.utime(s, (time.mktime(mtime.timetuple()),) * 2)
    return tmp


def run(tmp: Path) -> tuple[int, list[str]]:
    return check_mod.check(tmp, now=NOW)


def test_well_formed_project_passes(tmp_path):
    assert run(make(tmp_path, handoff(), project())) == (0, [])


def test_missing_project_means_not_bootstrapped(tmp_path):
    code, out = run(make(tmp_path, handoff()))
    assert code == 2 and "not bootstrapped" in out[0]


def test_shipped_templates_are_flagged_as_unfilled(tmp_path):
    status = (ZWEI / "templates/agent/STATUS.md").read_text()
    code, out = run(make(tmp_path, status, (ZWEI / "templates/agent/PROJECT.md").read_text()))
    assert code == 1 and any("placeholder" in o for o in out)


def test_oversize_status_fails(tmp_path):
    code, out = run(make(tmp_path, handoff() + "- [ ] step\n" * 40, project()))
    assert code == 1 and any("STATUS.md: " in o and "cap 40" in o for o in out)


@pytest.mark.parametrize("na", [
    "Fix the cron. Then deploy it.",
    ">\n  multi-line narrative",
])
def test_next_action_must_be_one_sentence_on_one_line(tmp_path, na):
    code, out = run(make(tmp_path, handoff(next_action=na), project()))
    assert code == 1 and any("next_action" in o for o in out)


def test_next_action_with_file_names_is_one_sentence(tmp_path):
    assert run(make(tmp_path, handoff(next_action="Edit docker-compose.yml and .env.example."), project()))[0] == 0


def test_stale_status_is_reported(tmp_path):
    code, out = run(make(tmp_path, handoff(last_update="2026-11-25T11:00"), project()))
    assert code == 1 and any("stale" in o for o in out)


def test_future_stamp_is_reported(tmp_path):
    code, out = run(make(tmp_path, handoff(last_update="2026-11-25T15:00"), project()))
    assert code == 1 and any("future" in o for o in out)


def test_blocked_requires_open_question(tmp_path):
    code, out = run(make(tmp_path, handoff(status="BLOCKED"), project()))
    assert code == 1 and any("BLOCKED" in o for o in out)
    ok = make(tmp_path, handoff(status="BLOCKED"), project("- Q-01: monitor-only or wait? — blocks T-1\n"))
    assert run(ok)[0] == 0


def test_cited_ids_must_resolve(tmp_path):
    code, out = run(make(tmp_path, handoff(constraints="\n  - honour REQ-07 and DR-004"), project()))
    assert code == 1
    assert any("REQ-07" in o for o in out) and any("DR-004" in o for o in out)
    (tmp_path / "docs/decisions").mkdir(parents=True)
    (tmp_path / "docs/decisions/004-ports.md").write_text("x")
    code, out = run(make(tmp_path, handoff(constraints="\n  - honour REQ-01 and DR-004"), project()))
    assert (code, out) == (0, [])


def test_checkpoint_skill_must_be_listed(tmp_path):
    code, out = run(make(tmp_path, handoff(skills="[gh-compose]"), project()))
    assert code == 1 and any("ordnung-checkpoint" in o for o in out)


def test_install_renders_kernel_and_skills(tmp_path):
    install_mod.install(tmp_path, "game-hosting", [".claude/skills"], force=False)
    agents = (tmp_path / "AGENTS.md").read_text()
    assert "{{" not in agents
    assert "Save data is the user's crown jewel" in agents
    assert "| `gh-compose` |" in agents and "| `ordnung-resume` |" in agents
    assert len(agents.splitlines()) <= check_mod.CAPS["AGENTS.md"]
    names = {p.name for p in (tmp_path / ".agents/skills").iterdir()}
    assert {"ordnung-resume", "ordnung-checkpoint", "gh-compose"} <= names
    assert (tmp_path / ".claude/skills/ordnung-resume/SKILL.md").is_file()
    assert not (tmp_path / ".agents/skills/ordnung-resume/evals").exists()
    assert (tmp_path / "licenses").is_dir()


def test_install_never_overwrites_existing_agents_md(tmp_path):
    (tmp_path / "AGENTS.md").write_text("mine")
    install_mod.install(tmp_path, "game-hosting", [], force=False)
    assert (tmp_path / "AGENTS.md").read_text() == "mine"
    assert (tmp_path / "AGENTS.md.ordnung-new").is_file()


PERSONAS = sorted(p.parent.name for p in ZWEI.glob("personas/*/persona.md"))


@pytest.mark.parametrize("persona", PERSONAS)
def test_every_skill_listed_in_kernel_exists(persona):
    import re
    tmpl = (ZWEI / "kernel/AGENTS.md.tmpl").read_text()
    text = (ZWEI / "personas" / persona / "persona.md").read_text()
    listed = set(re.findall(r"^\| `([a-z-]+)` \|", tmpl + text, re.M))
    shipped = {p.parent.name for p in [*ZWEI.glob("skills/core/*/SKILL.md"),
                                       *ZWEI.glob(f"personas/{persona}/skills/*/SKILL.md")]}
    assert listed == shipped


@pytest.mark.parametrize("persona", PERSONAS)
def test_every_persona_installs_within_cap(tmp_path, persona):
    install_mod.install(tmp_path, persona, [".claude/skills"], force=False)
    agents = (tmp_path / "AGENTS.md").read_text()
    assert "{{" not in agents
    assert "9. " in agents and "12. " in agents
    assert len(agents.splitlines()) <= check_mod.CAPS["AGENTS.md"]


# ---- task board (agent/TASKS.md) and decision settings ------------------------------------------
BOARD = """# TASKS

## NOW

- [T-1] Add backup cron — owner: agent — ref: REQ-01
    done: compose config renders with BACKUP_CRON set.

## NEXT

- [T-2] Restore drill — owner: agent
    after: T-1

## LATER

- [T-3] Panel TLS — owner: both

## WAITING

- [T-4] Pick the time zone — owner: owner — decision: UTC or local
"""


def with_board(tmp: Path, board: str = BOARD, archive: str | None = None, **over: str) -> Path:
    make(tmp, handoff(**over), project())
    (tmp / "agent/TASKS.md").write_text(board)
    if archive is not None:
        (tmp / "agent/TASKS.archive.md").write_text(archive)
    return tmp


def test_well_formed_board_passes(tmp_path):
    assert run(with_board(tmp_path)) == (0, [])


@pytest.mark.parametrize("board, expect", [
    (BOARD.replace("- [T-3] Panel TLS — owner: both", "- [T-1] Panel TLS — owner: both"), "appears in"),
    (BOARD.replace("Panel TLS — owner: both", "Panel TLS"), "no 'owner"),
    (BOARD.replace(" — decision: UTC or local", ""), "WAITING but"),
    (BOARD.replace("after: T-1", "after: T-9"), "neither on the board"),
    (BOARD.replace("## NEXT\n", "- [T-5] a — owner: agent\n- [T-6] b — owner: both\n"
                   "\n## NEXT\n"), "agent tasks in NOW > 2"),
])
def test_board_findings(tmp_path, board, expect):
    code, out = run(with_board(tmp_path, board))
    assert code == 1 and any(expect in o for o in out), out


def test_board_ids_are_never_reused_from_the_archive(tmp_path):
    code, out = run(with_board(tmp_path, archive="- 2026-11-01 · [T-3] old outcome\n"))
    assert code == 1 and any("never reused" in o for o in out)


def test_handoff_task_must_be_claimed_into_now(tmp_path):
    code, out = run(with_board(tmp_path, task="T-2 restore drill"))
    assert code == 1 and any("claim it into NOW" in o for o in out)
    assert run(with_board(tmp_path, task="T-2 restore drill", status="DONE"))[0] == 0


def test_decision_prefix_and_dir_come_from_settings(tmp_path):
    with_board(tmp_path, BOARD.replace("ref: REQ-01", "ref: ADR-019 d2"))
    (tmp_path / "agent/ordnung.toml").write_text('[decisions]\nprefix = "ADR"\ndir = "docs/adr"\n')
    code, out = run(tmp_path)
    assert code == 1 and any("docs/adr/019-*.md does not exist" in o for o in out)
    (tmp_path / "docs/adr").mkdir(parents=True)
    (tmp_path / "docs/adr/019-engine-owns-desired-state.md").write_text("Status: ACCEPTED\n")
    assert run(tmp_path) == (0, [])


def test_decisions_list_rejects_ids_without_a_record_scheme(tmp_path):
    make(tmp_path, handoff(), project().replace("## Decisions\n- none yet",
                                                 "## Decisions\n- D-01: monitor-only — ACCEPTED"))
    code, out = run(tmp_path)
    assert code == 1 and any("decision IDs here are DR-NNN" in o for o in out)


def test_owner_tasks_in_now_do_not_count_against_the_cap(tmp_path):
    board = BOARD.replace("## NEXT\n", "- [T-5] a — owner: owner\n- [T-6] b — owner: owner\n"
                          "- [T-7] c — owner: agent\n\n## NEXT\n")
    assert run(with_board(tmp_path, board)) == (0, [])


def hooked(tmp: Path, run_cmds: str | None) -> Path:
    with_board(tmp)
    (tmp / ".git/hooks").mkdir(parents=True)
    if run_cmds is not None:
        (tmp / "agent/ordnung.toml").write_text(f"[hook]\nrun = {run_cmds}\n")
    return tmp


def test_install_hook_without_settings_runs_only_the_check(tmp_path):
    hooked(tmp_path, None)
    assert check_mod.install_hook(tmp_path) == 0
    text = (tmp_path / ".git/hooks/pre-commit").read_text()
    assert text.endswith("exec python3 agent/ordnung_check\n")
    assert run(tmp_path) == (0, [])


def test_install_hook_appends_the_run_commands_in_order(tmp_path):
    hooked(tmp_path, '["uv lock --check", "true"]')
    assert check_mod.install_hook(tmp_path) == 0
    lines = (tmp_path / ".git/hooks/pre-commit").read_text().splitlines()
    assert lines[2:] == ["set -e", "python3 agent/ordnung_check", "uv lock --check", "true"]
    assert run(tmp_path) == (0, [])


def test_hook_that_lags_its_settings_is_reported(tmp_path):
    hooked(tmp_path, None)
    check_mod.install_hook(tmp_path)
    (tmp_path / "agent/ordnung.toml").write_text('[hook]\nrun = ["uv lock --check"]\n')
    code, out = run(tmp_path)
    assert code == 1 and any("rerun python3 agent/ordnung_check --install-hook" in o for o in out)


def test_a_foreign_hook_is_left_alone(tmp_path):
    hooked(tmp_path, '["uv lock --check"]')
    (tmp_path / ".git/hooks/pre-commit").write_text("#!/bin/sh\nmake lint\n")
    assert check_mod.install_hook(tmp_path) == 1
    assert run(tmp_path) == (0, [])


# ---- this repository's own contract (DR-006) -----------------------------------------------------
def test_root_agents_md_is_the_rendered_kernel():
    """The repo runs its own contract; re-render after kernel or persona changes:
    tools/install . --persona contract-authoring --dev --force"""
    assert (ZWEI / "AGENTS.md").read_text() == install_mod.render_agents("contract-authoring")


def test_dev_install_links_every_shipped_skill():
    skills = ZWEI / ".agents/skills"
    expected = {p.parent.name for p in [*ZWEI.glob("skills/core/*/SKILL.md"),
                                        *ZWEI.glob("personas/contract-authoring/skills/*/SKILL.md")]}
    assert {p.name for p in skills.iterdir()} == expected
    assert all((skills / n).is_symlink() for n in expected)
    assert (ZWEI / "agent/ordnung_check").resolve() == (ZWEI / "tools/ordnung_check").resolve()


def test_lineage_links_point_at_tags():
    import re
    text = "\n".join(p.read_text() for p in [ZWEI / "docs/lineage.md", ZWEI / "README.md"])
    refs = re.findall(r"Ordnung-The-AI-Agent-contract-repository/(?:tree|blob)/([^/)\s>]+)", text)
    assert refs, "lineage must link into the v1 tag"
    assert all(r.startswith(("contracts-v", "archive/")) for r in refs), refs
    assert "../Ordnung-The-AI-Agent-contract-repository" not in text


# Kernel rule 11: this repository is public. These are sha256 prefixes of lower-cased words
# (adjacent word pairs are also checked joined) that identify field projects and their owners;
# the words themselves stay out of the repo. Field projects are A, B, C in docs/field-tests/.
FIELD_NAME_HASHES = frozenset({
    "a3a4842197f85682",
    "ad0fc66325596c00",
    "c50ef369a6b8046e",
    "e2eb61c564491a57",
    "e93d5d59ccd9a517",
})


def _field_name_hits(text: str) -> bool:
    import hashlib
    import re
    words = re.findall(r"[a-z0-9]+", text.lower())
    for token in [*words, *(a + b for a, b in zip(words, words[1:]))]:
        if hashlib.sha256(token.encode()).hexdigest()[:16] in FIELD_NAME_HASHES:
            return True
    return False


def test_shipped_text_names_no_field_project():
    hits = [str(p.relative_to(ZWEI)) for p in ZWEI.rglob("*")
            if p.is_file() and not p.is_symlink() and ".git" not in p.parts
            and not any(part.endswith("-workspace") or part == "__pycache__" for part in p.parts)
            and p.suffix in {".md", ".py", ".yaml", ".yml", ".toml", ".tmpl", ".sh", ""}
            and _field_name_hits(p.read_text(errors="ignore"))]
    assert hits == []


def test_field_name_guard_catches_a_planted_name():
    import hashlib
    assert not _field_name_hits("an IaC firewall-management tool, project B")
    planted = "".join(chr(c) for c in (100, 107, 102, 109))  # a banned word, never spelled out
    assert _field_name_hits(f"notes about {planted} go here")
