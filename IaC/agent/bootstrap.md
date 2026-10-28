# Bootstrap protocol (new project — no agent/STATUS.md exists yet)

You are starting from scratch. Do the following IN ORDER before any implementation:

1. **Confirm scope.** Restate in 2-3 sentences what you understand the project to be.
   Ask if anything is missing. Wait for confirmation.

2. **Set project license.** Present the three available license templates under `licenses/` and have the user choose one, or state they do not want a LICENSE file:
   - Generic permissive (`licenses/LICENSE_permissive.txt`)
   - Generic unpermissive (`licenses/LICENSE_unpermissive.txt`)
   - Standard MIT (`licenses/LICENSE_MIT-license.txt`)

   When a choice is made, copy the selected template to `LICENSE` at project root. If no license is wanted, skip this step. Delete the `licenses/` directory when done. Modify the copied file and follow instructions in the files` comment (#) lines.

3. **Create the project skeleton.**
   - `README.md` (title, one-paragraph purpose, "Status: scaffolding")
   - `agent/STATUS.md` with initial HANDOFF:
       phase: 0 — Scaffolding
       status: IN_PROGRESS
       next_action: Create project structure per the layout in agent/project_layout.md
       files: (none yet)
   - `agent/REPO-MAP.md` (directory guide — start from the core layout, add tool dirs as they appear)
   - `docs/` and `docs/adr/` directories
   - `.gitignore`, `.env.example` (if applicable)
   - `git init` + initial commit

4. **If the project involves design decisions or research:**
   - Create ADRs under `docs/adr/` and follow the process in `rules/adr.md`.

5. **Set the first real `next_action`** in `agent/STATUS.md` to the first implementation step. Then proceed as normal.

After this, the standard session-continuity protocol applies.
