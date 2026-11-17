# Bootstrap protocol (new project - no agent/REPO-MAP.md and no project-written agent/STATUS.md yet)

The contract ships `agent/STATUS.md` as an empty template (headers only, no HANDOFF block). If the
file still has no HANDOFF block, bootstrap has not run in this project, so run it. A STATUS.md that
already contains a written HANDOFF means the project is bootstrapped: skip to normal session
continuity instead.

Keep bootstrap short. The value is in the questioning session, not in the scaffolding.

1. **Confirm the job.** In two or three sentences, restate what you understand: the document(s), the
   type (`rules/doc_types.md`), the reader, and what the reader must be able to decide or do. Ask
   whether anything is missing, and wait for the answer.

2. **Three set-up questions, asked together in one message:**
   - Output format: Markdown, Word/LibreOffice, or something else (`rules/output_formats.md`). If
     rich text is chosen, ask whether to set up the export path (pandoc with a reference document,
     or python-docx).
   - Language(s) of the deliverable.
   - Classification: "default is Internal. Tell me if this is meant to go wider." Do not block on
     the answer (`rules/classification.md`).

3. **Create the skeleton.**
   - `README.md` (title, one-paragraph purpose, reader, classification, "Status: brief")
   - `agent/STATUS.md` with a HANDOFF block: phase `0 - Brief`, status IN_PROGRESS, next_action
     "Run the questioning session for <doc>".
   - `agent/REPO-MAP.md` with the directory guide, the set's `classification:` line, and a document
     map. Other registers are started when they are first needed.
   - `briefs/`, `documents/`, `sources/`. Other directories from `agent/project_layout.md` are created
     when first needed.
   - If the project uses git: `.gitignore` (build output, `.env`, material narrower than Internal),
     `git init` and an initial commit.

4. **Start the questioning session** (`rules/requirements.md`) and work towards the brief. Drafting
   starts only after the user has confirmed the brief.

After this, the standard session-continuity protocol applies.
