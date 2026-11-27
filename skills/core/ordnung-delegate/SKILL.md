---
name: ordnung-delegate
description: Hands work to a subagent / worker in an Ordnung-contract project with a brief that carries the contract along, and integrates the result without flooding the coordinator's context. Use this whenever a step needs many file reads or searches, a long debugging or probing session, a batch of independent edits, research across sources, an independent review of your own work, or parallel pieces that do not depend on each other. Prefer delegating over doing such work inline — the subagent's context burns instead of yours, so your plan and the project's constraints survive.
---

# Delegate

You are the coordinator. Your context holds the plan, the user's decisions and the contract;
it is the scarcest thing in the session. Work that eats context — wide reads, trial-and-error,
long logs — goes to a worker whose context is disposable.

Subagents start without your conversation and usually without this project's `AGENTS.md`
loaded. Whatever the brief does not carry, the worker does not know. So the brief carries the
contract.

## When to delegate

- More than a handful of reads or searches to answer one question.
- Debugging or probing with an unknown number of iterations.
- Independent pieces that can run in parallel (one worker each; never two workers on the
  same files).
- Verifying your own work: an independent reviewer sees what you are blind to.

Keep inline: one targeted read, one edit, one command whose output you need verbatim.

## Before you dispatch

Checkpoint (`ordnung-checkpoint`): the HANDOFF names the delegated step, so a compaction while
the worker runs loses nothing.

## Brief template

Fill every section; "none" is an answer, a missing section is not.

```
ROLE: <persona role line from AGENTS.md>

NON-NEGOTIABLES (from the project contract, verbatim):
<paste the Non-negotiables list from AGENTS.md>

TASK: <one or two sentences>

DONE MEANS: <the observable result — a passing command, a file, an answer to a question>

CONTEXT: <paths and IDs to read — REQ/DR/Q entries that bind this work — not summaries of
         them; the worker reads the source>

SKILLS TO LOAD: <persona skills governing this work, by name and path>

FENCES: <files not to touch; decisions that are not the worker's to make; no commits/pushes
        unless stated; destructive or outward-facing actions are out of scope>

REPORT (≤ 15 lines, this shape):
  outcome: done | partial | blocked — one line
  evidence: command → result, per claim
  changed: files touched
  decisions needed: anything only the user or coordinator can decide
  durable facts: anything that should outlive this task (coordinator promotes it)
  surprises: what contradicted the brief
```

## Integrating the report

1. Check the evidence, not the prose: re-run or spot-check the commands that matter before
   telling the user it is done.
2. *decisions needed* → a `Q-NN` (or a DR) via `ordnung-ledger`. *durable facts* → PROJECT.md.
3. Checkpoint. Do not paste the worker's full output into your context or into STATUS.

## Independent review worker

For review, independence comes from inputs: give the reviewer the requirement (REQ/DR lines
and the acceptance criterion) and the artifact — not your reasoning or your conclusion. Ask for
findings with severity and evidence, and no edits. You decide what to fix.
