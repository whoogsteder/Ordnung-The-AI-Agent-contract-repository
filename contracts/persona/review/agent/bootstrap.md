# Bootstrap protocol (new project - no agent/REPO-MAP.md and no project-written agent/STATUS.md yet)

The contract ships `agent/STATUS.md` as an empty template (headers only, no HANDOFF block). If the
file still has no HANDOFF block, bootstrap has not run in this project, so run it. A HANDOFF with
`phase: bootstrap` means bootstrap started and did not finish: resume it at its `next_action`. Any
other written HANDOFF means the project is bootstrapped: skip to normal session continuity instead.

Until step 3 creates the skeleton, checkpoint with `phase: bootstrap` (`rules/base.md`, Session
continuity). If the user opens with a brief or requirements, save them verbatim to
`agent/intake.md` before your first reply: a compaction during bootstrap must not lose them.

When this persona runs as a sub-agent, skip bootstrap entirely (`agent/project_layout.md`).

1. **Confirm the job.** In one or two sentences, name the artefact you are asked to review, its
   version, and what you will judge it against. Ask for whatever is missing of: the artefact, its
   yardstick (confirmed brief or question record), access to its sources, and the stated reader.
   If the opening message already states the artefact, its yardstick and its reader, do steps 1 and
   2 in one message.

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
   `agent/STATUS.md` was written after its `last_update:` time, and that flags a `last_update`
   later than the write (an estimated stamp). Build it only on a yes. Declining is
   fine; the checkpoint fallback in `rules/base.md` still applies.

5. **Agree the scope** (`rules/review_setup.md`) and start.

After this, the standard session-continuity protocol applies.
