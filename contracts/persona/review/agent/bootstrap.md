# Bootstrap protocol (new project - no agent/REPO-MAP.md and no project-written agent/STATUS.md yet)

The contract ships `agent/STATUS.md` as an empty template (headers only, no HANDOFF block). If the
file still has no HANDOFF block, bootstrap has not run in this project, so run it. A STATUS.md that
already contains a written HANDOFF means the project is bootstrapped: skip to normal session
continuity instead.

When this persona runs as a sub-agent, skip bootstrap entirely (`agent/project_layout.md`).

1. **Confirm the job.** In one or two sentences, name the artefact you are asked to review, its
   version, and what you will judge it against. Ask for whatever is missing of: the artefact, its
   yardstick (confirmed brief or question record), access to its sources, and the stated reader.

2. **Two set-up questions, asked together:**
   - May you re-check facts on the web, and what in the artefact is confidential and must never go
     into a search?
   - Classification of the report: "default is Internal, or the label of the artefact if that is
     narrower".

3. **Create the skeleton.** `README.md`, `agent/STATUS.md` with a HANDOFF block (phase
   `0 - Review setup`, next_action "Agree the review scope for <artefact>"), `agent/REPO-MAP.md` with a
   review register, and `reviews/<artefact>/inputs/`. If the project uses git: `.gitignore`,
   `git init` and an initial commit.

4. **Offer a freshness check (optional).** Ask whether to add a small script that reports whether
   `agent/STATUS.md` was written after its `last_update:` time. Build it only on a yes. Declining is
   fine; the checkpoint fallback in `rules/base.md` still applies.

5. **Agree the scope** (`rules/review_setup.md`) and start.

After this, the standard session-continuity protocol applies.
