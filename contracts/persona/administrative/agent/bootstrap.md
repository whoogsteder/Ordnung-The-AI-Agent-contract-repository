# Bootstrap protocol (new project — no agent/REPO-MAP.md and no project-written agent/STATUS.md yet)

The contract ships `agent/STATUS.md` as an empty template (headers only, no HANDOFF). If the
file still has no HANDOFF block, bootstrap has not run in this project — run it. A STATUS.md
containing a written HANDOFF means the project is already bootstrapped: skip to normal
session continuity instead.

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
   - `docs/` and `docs/decisions/` directories
   - Does the open project use git?
     - add `.gitignore`, add .env and obvious secrects to gitignore.
     - Create `.env.example` clone keys from .env file if present. Replace secrets with template example values.
     - `git init` + initial commit

4. **If the project involves design decisions or research:**
   - Create DRs under `docs/decisions/` and follow the process in `rules/dr.md`.

5. **Offer a memory-freshness check (optional, project-written).** The frequency guard in
   `rules/base.md` is enforceable from the `last_update` field alone; this step only makes it
   one command instead of one judgment. Ask the user whether to add it, and build it only on a
   yes: write a small script that prints whether `agent/STATUS.md` was written after the
   `last_update:` timestamp in its HANDOFF block — exit 0 when current, non-zero plus a one-line
   warning when it is older or the field is missing. Choose the language and location for the
   tooling this project actually has (shell with `stat`, Python, PowerShell); register the script
   in `agent/REPO-MAP.md` and record its run command in `agent/STATUS.md` notes. If the user
   declines, or the environment makes a file-timestamp check awkward, record that decision as a
   note and move on: declining is a completed step, and the textual guard still applies.

6. **Set the first real `next_action`** in `agent/STATUS.md` to the first implementation step. Then proceed as normal.

After this, the standard session-continuity protocol applies.
