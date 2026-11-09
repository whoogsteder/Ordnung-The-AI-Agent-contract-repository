# Bootstrap protocol (new project - no agent/REPO-MAP.md and no project-written agent/STATUS.md yet)

The contract ships `agent/STATUS.md` as an empty template (headers only, no HANDOFF). If the
file still has no HANDOFF block, bootstrap has not run in this project - run it. A STATUS.md
containing a written HANDOFF means the project is already bootstrapped: skip to normal
session continuity instead.

You are starting from scratch. Do the following IN ORDER before any implementation:

1. **Confirm scope.** Restate in 2-3 sentences what you understand the document set to be: the
   audience (IT manager, IT administrator, or both), the documents expected, and the decision the
   set supports. Ask if anything is missing. Wait for confirmation.

2. **Set project license.** Present the three available license templates under `licenses/` and have the user choose one, or state they do not want a LICENSE file:
   - Generic permissive (`licenses/LICENSE_permissive.txt`)
   - Generic unpermissive (`licenses/LICENSE_unpermissive.txt`)
   - Standard MIT (`licenses/LICENSE_MIT-license.txt`)

   When a choice is made, copy the selected template to `LICENSE` at project root. If no license is wanted, skip this step. Delete the `licenses/` directory when done. Modify the copied file and follow instructions in the files` comment (#) lines.
   Ask separately about the deliverables and the templates: documents meant for redistribution can
   carry different terms from the generator scripts (see `rules/dr.md`).

3. **Ask the format question.** Offer the menu from `rules/output_formats.md` - Markdown, Word or
   LibreOffice rich text, or a user-specified target - and record the answer in `agent/STATUS.md`
   and the document map. If a rich-text target is chosen, ask whether to set up the export path
   (pandoc with a reference document, or python-docx/docxtpl) and record what is installed.

4. **Create the project skeleton.**
   - `README.md` (title, one-paragraph purpose, audience, "Status: scaffolding")
   - `agent/STATUS.md` with initial HANDOFF:
       phase: 0 - Scaffolding
       status: IN_PROGRESS
       next_action: Create project structure per the layout in agent/project_layout.md
       files: (none yet)
   - `agent/REPO-MAP.md` (directory guide, plus the register headings started empty: documents,
     shared facts, terminology, sources, open items)
   - `documents/` by type, `docs/` and `docs/decisions/`, `templates/`, `assets/figures/`, `sources/`
   - Does the open project use git?
     - add `.gitignore`, add .env, build output and obvious secrets to gitignore.
     - Create `.env.example` clone keys from .env file if present. Replace secrets with template example values.
     - `git init` + initial commit

5. **If the project involves design decisions, comparisons or research:**
   - Create DRs under `docs/decisions/` and follow the process in `rules/dr.md`.
   - Put every gap and undecided choice into the open-items register per `rules/open_questions.md`.

6. **Offer a memory-freshness check (optional, project-written).** The frequency guard in
   `rules/base.md` is enforceable from the `last_update` field alone; this step only makes it
   one command instead of one judgment. Ask the user whether to add it, and build it only on a
   yes: write a small script that prints whether `agent/STATUS.md` was written after the
   `last_update:` timestamp in its HANDOFF block - exit 0 when current, non-zero plus a one-line
   warning when it is older or the field is missing. Choose the language and location for the
   tooling this project actually has (shell with `stat`, Python, PowerShell); register the script
   in `agent/REPO-MAP.md` and record its run command in `agent/STATUS.md` notes. If the user
   declines, or the environment makes a file-timestamp check awkward, record that decision as a
   note and move on: declining is a completed step, and the textual guard still applies.

7. **Set the first real `next_action`** in `agent/STATUS.md` to the first drafting step. Then proceed as normal.

After this, the standard session-continuity protocol applies.