# Bootstrap protocol (new project - no agent/REPO-MAP.md and no project-written agent/STATUS.md yet)

The contract ships `agent/STATUS.md` as an empty template (headers only, no HANDOFF block). If the
file still has no HANDOFF block, bootstrap has not run in this project, so run it. A STATUS.md that
already contains a written HANDOFF means the project is bootstrapped: skip to normal session
continuity instead.

Keep bootstrap short. The value is in agreeing the question, not in the scaffolding.

1. **Confirm the job.** In two or three sentences, restate the research question as you understand
   it, what it feeds (a decision, a document, understanding) and who receives the result. Ask whether
   anything is missing, and wait for the answer.

2. **Three set-up questions, asked together in one message:**
   - Tools and access: may you search the web, and are there portals or internal documents the user
     will open or supply?
   - Confidential material: what must never go into a search (customer names, internal prices,
     configurations)?
   - Classification of the results: "default is Internal. Tell me if this is meant to go wider."
     Do not block on the answer (`rules/classification.md`).

3. **Create the skeleton.**
   - `README.md` (purpose, receiver, classification, "Status: question")
   - `agent/STATUS.md` with a HANDOFF block: phase `0 - Question`, status IN_PROGRESS,
     next_action "Agree the research question for <topic>".
   - `agent/REPO-MAP.md` with the directory guide, the `classification:` line, and a topics register.
   - `research/<topic>/sources/`.
   - If the project uses git: `.gitignore` (`.env`, material narrower than Internal), `git init` and an
     initial commit.

4. **Offer a freshness check (optional).** Ask whether to add a small script that reports whether
   `agent/STATUS.md` was written after its `last_update:` time. Build it only on a yes, in whatever
   language the environment has, and record its run command in STATUS notes. Declining is fine; the
   checkpoint fallback in `rules/base.md` still applies.

5. **Agree the question** (`rules/question.md`). Searching starts only after the user has confirmed
   it.

After this, the standard session-continuity protocol applies.
