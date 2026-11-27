---
name: ca-evals
description: Evaluating Ordnung-Zwei skills — eval case layout (prompt.md, case.yaml, graders, files, place-files.sh), paired with-skill and baseline runs in subagents, scripted grading into grading.json, benchmarks and the review viewer, spotting non-discriminating assertions, and turning field-test feedback into new cases. Use this whenever you test a skill, claim a skill change is an improvement, write or rerun eval cases, grade runs, compare iterations, or record operator feedback from a field project.
---

# Evals and field feedback

A skill change is a hypothesis until a run shows the behaviour changed. Kernel rule 9 makes this
a gate, not a nicety.

## Cases
- **Where they live:** `<skill-dir>/evals/<case>/`:
  - `prompt.md`: the user's message, written as a real user would send it;
  - `case.yaml`: what a good result looks like;
  - `graders/NN-*.md`: one assertion each;
  - `files/`: a small project fixture, with a rendered `AGENTS.md`, `agent/ordnung_check` and the
    memory files;
  - `place-files.sh`: sets the file times the freshness checks need.

  The format follows `skill-creator`'s `references/schemas.md`. Read that before writing a case.
- **Fixtures match today's contract.** When a template changes (a new file such as `TASKS.md`, a
  changed `PROJECT.md` section), update every fixture in the same change, or the case tests a
  project that no longer exists.
- **Install the companion skills a case needs** into its fixture. A skill that hands off to
  another (checkpoint → ledger) behaves differently when the other one is missing.

## Runs
- **Run each case twice, in parallel:** once with the skill, once without it as the baseline.
  When improving an existing skill, the baseline is a snapshot of the old version instead. Launch
  all the runs in the same turn.
- **Workspaces** go under `<skill>-workspace/iteration-N/<case>/{with_skill,without_skill}/`, which
  `.gitignore` excludes. Record `timing.json` from each run's completion notice straight away,
  because it is not stored anywhere else.

## Grading
- **Grade by script wherever possible:** parse the files the run produced, and the `tool_use`
  blocks in its transcript. Never string-search the whole transcript, because it contains the
  tool listing too. Write `grading.json` with `text`, `passed` and `evidence` for each assertion.
- **A non-discriminating assertion** passes with and without the skill. It is either already
  covered by the kernel, which is good news, or too easy. Either way, the next iteration needs a
  harder case that only the skill can pass.
- **Read the runs yourself**, not just the scores. Iteration 1's most useful finding (an invented
  decision ID) was not in any assertion.
- **Small samples:** with one run per configuration, timing differences are noise. Say so.

## Field feedback becomes cases
- **Record each operator report** in `docs/field-tests/feedback.md`, with what was observed and
  its outcome (a DR, a board task, or "watch"). Use generic project names (kernel rule 11).
- **A failure seen in the field** gets a case that reproduces it with a generic fixture, before
  the skill is changed to fix it.
- **`agent/estimates.md` lines** from field projects (DR-005, once accepted) are input for cases
  about estimating effort and stopping when a task proves bigger than predicted.
