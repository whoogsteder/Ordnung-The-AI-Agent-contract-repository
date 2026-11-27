---
name: ordnung-bootstrap
description: Sets up agent memory for a new project under an Ordnung contract — confirms scope with the user, picks a license, and creates agent/PROJECT.md, agent/TASKS.md, agent/STATUS.md and agent/REPO-MAP.md from the templates. Use this when agent/PROJECT.md does not exist, when ordnung-resume or ordnung_check reports the project as not bootstrapped, or when the HANDOFF task is bootstrap. Also use it when migrating a project from Ordnung v1 (agent/STATUS.md exists but agent/PROJECT.md does not).
---

# Bootstrap

A project without PROJECT.md has no strategic memory yet, and every later session would
rebuild it from chat. Build it once, with the user, before implementation.

Checkpoint as you go: the very first file you write is a STATUS.md with `task: bootstrap`,
so an interrupted bootstrap resumes instead of restarting.

## New project

1. **Confirm scope.** Restate in 2–3 sentences what the project is. Ask what is missing and
   wait. Then settle the persona's scope questions, listed under *Bootstrap questions* in
   `agent/persona.md`. Each answer that must hold for the project's life becomes a `REQ-NN`.
2. **License.** Offer the templates in `licenses/` (or "no LICENSE file"). Copy the choice to
   `LICENSE`, follow its comment lines, delete `licenses/`.
3. **Memory files.** Copy `agent/templates/{PROJECT,TASKS,STATUS,REPO-MAP}.md` into `agent/`
   and fill them in: the Purpose, the REQs from step 1, and the first tasks on the board
   (`ordnung-board`). Check the decision scheme in `agent/ordnung.toml` (the installer writes the
   persona's default) with the user.
4. **Repository hygiene.** If git is used: `.gitignore` covering env/secret files and data
   directories; `<name>.example` for every config file with placeholder values. List the
   project's own pre-commit commands (a lock check, a linter) under `[hook] run` in
   `agent/ordnung.toml`, then install the hook: `python3 agent/ordnung_check --install-hook`.
   Ask before `git init` or the first commit.
5. **Decisions.** Open choices that outlive a task become PROPOSED DRs (`ordnung-ledger`).
6. **Hand off.** Set the HANDOFF to the first real task and run `python3 agent/ordnung_check`.

## Migrating from Ordnung v1

The v1 STATUS.md usually mixes the task with strategy. Do not copy it whole.

1. Read v1 `agent/STATUS.md` (not the archive).
2. Sort each item:
   - a requirement that still binds → `REQ-NN`;
   - a decision → a line in the decision index. The records stay where they are; set
     `agent/ordnung.toml` to their existing prefix and directory, and never renumber them;
   - something waiting on the user → `Q-NN`;
   - future work → the board;
   - the current task → the new HANDOFF;
   - everything else → append to `agent/STATUS.archive.md` under `## <date> — v1 migration`.
3. **An existing `agent/TASKS.md` board** (NOW/NEXT/LATER/WAITING with `[T-NN]` lines) is
   already in Zwei format. Keep it and its archive, and fix whatever `ordnung_check` reports.
   Anything the board's header text explains is now in `ordnung-board`, so shorten the header
   to the template's.
4. Trim REPO-MAP to 120 lines by splitting areas into `agent/maps/`. Before you move anything,
   check whether a project test reads REPO-MAP.
5. Show the user the new PROJECT.md and ask what is wrong or missing before continuing.
