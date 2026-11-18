# Bootstrap protocol (new project - no agent/REPO-MAP.md and no project-written agent/STATUS.md yet)

The contract ships `agent/STATUS.md` as an empty template (headers only, no HANDOFF block). If the
file still has no HANDOFF block, bootstrap has not run in this project, so run it. A HANDOFF with
`phase: bootstrap` means bootstrap started and did not finish: resume it at its `next_action`. Any
other written HANDOFF means the project is bootstrapped: skip to normal session continuity instead.

Until step 3 creates the skeleton, checkpoint with `phase: bootstrap` (`rules/base.md`, Session
continuity). If the user opens with a brief or requirements, save them verbatim to
`agent/intake.md` before your first reply: a compaction during bootstrap must not lose them.

Keep bootstrap short. The value is in the questioning session, not in the scaffolding.

1. **Confirm the job.** In two or three sentences, restate what you understand: the document(s), the
   type (`rules/doc_types.md`), the reader, and what the reader must be able to decide or do. Ask
   whether anything is missing, and wait for the answer.
   If the opening message already states the document, its reader and what the reader must decide or
   do, do steps 1 and 2 in one message.

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

4. **Offer a freshness check (optional).** Ask whether to add a small script that reports whether
   `agent/STATUS.md` was written after its `last_update:` time, and that flags a `last_update`
   later than the write (an estimated stamp). Build it only on a yes, in whatever
   language the environment has, and record its run command in STATUS notes. Declining is fine; the
   checkpoint fallback in `rules/base.md` still applies.

5. **Start the questioning session** (`rules/requirements.md`) and work towards the brief. Agree
   whether the document needs a research pack from the `research` persona (`rules/facts.md`).
   Drafting starts only after the user has confirmed the brief.

After this, the standard session-continuity protocol applies.
