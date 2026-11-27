# How agents find and load skills

Status: desk research, 2026-11-26. Every row below comes from the vendor's documentation (linked)
unless marked *reported*. None of it has been tested in a real session yet; the "Check" column says
how to test it, and the test results belong in the last column.

## The short version

1. **All the major harnesses now read `SKILL.md`**, the Agent Skills format: a folder with a
   `SKILL.md` that starts with YAML frontmatter holding `name` and `description`.
2. **`.agents/skills/` is the shared project location.** Codex, Copilot, Cursor, Gemini CLI and
   OpenCode read it. **Claude Code does not**: it reads only `.claude/skills/`, and the requests for
   `.agents/skills` are still open. That is why the installer creates the symlink
   `.claude/skills -> .agents/skills`. Codex and Claude Code both document that they follow
   symlinks.
3. **Loading happens in three stages**, and they behave differently:
   - **Discovery** (at session start): only each skill's `name` and `description` enter the context.
     They cost about 100 tokens per skill.
   - **Activation** (when relevant): the full `SKILL.md` body is read in. Either the model decides
     the description matches the task, or someone names the skill explicitly.
   - **Resources** (on demand): files the skill points to are read only when the skill says to.
4. **Activation by the model is a judgement call, and models often skip it.** That is acceptable
   for persona skills (`gh-compose` when editing compose files), but not for the skills the contract
   depends on. The kernel therefore never leaves `ordnung-resume` to chance: AGENTS.md, which every
   harness re-reads, names the skill and its file path. The fallback line ("no skill tool: read
   `.agents/skills/<name>/SKILL.md`") makes it work even in a harness that has no skill tool.

## Per harness

| Harness | Project paths read | Personal paths | How activation works | Check | Tested |
|---|---|---|---|---|---|
| Claude Code | `.claude/skills/`, searching up to the repo root; nested `.claude/skills/` in subdirectories load on demand (one open issue says nested discovery fails) | `~/.claude/skills/` | `Skill` tool, chosen by the model; the user can type `/<name>`. After a compaction, skills already invoked are re-attached to the context: this session showed it happening | `/skills`, or ask "which skills do you have?" | – |
| OpenAI Codex | `.agents/skills/` in every directory from the working directory up to the repo root; follows symlinks | `~/.agents/skills/`, admin `/etc/codex/skills` | Model reads `SKILL.md` when the description matches; the user can invoke one explicitly (`$name`, or the `/skills` picker) | `/skills` | – |
| GitHub Copilot (CLI, cloud agent, VS Code / Visual Studio / JetBrains agent mode) | `.github/skills/`, `.claude/skills/`, `.agents/skills/` | `~/.copilot/skills/`, `~/.agents/skills/` | Agent decides; `SKILL.md` is injected into the context. Support differs by IDE version (*reported*: some VS Code harnesses list only `.github/skills/`) | Ask the agent; `gh skill` (preview) lists installed skills | – |
| Cursor (2.4+) | `.agents/skills/`, `.cursor/skills/`, plus `.claude/skills/` and `.codex/skills/` for compatibility; searches recursively | `~/.agents/skills/` (some pages also give `~/.cursor/skills/`) | Agent decides; a nested folder applies only to the files beneath it | Settings → Rules/Skills | – |
| Gemini CLI | `.gemini/skills/` and the alias `.agents/skills/` (the alias wins on a name clash) | `~/.gemini/skills/`, `~/.agents/skills/` | `activate_skill` tool, chosen by the model; the user is asked to approve | `/skills list` | – |
| OpenCode | `.opencode/skills/`, plus `.claude/skills/` and `.agents/skills/`, walking up to the git worktree root | `~/.config/opencode/skills/`, `~/.claude/skills/`, `~/.agents/skills/` | `skill` tool, chosen by the model. `OPENCODE_DISABLE_EXTERNAL_SKILLS=1` switches off the `.claude`/`.agents` paths, and the Claude path support has changed between versions | `opencode debug skill` | – |

## What this means for Ordnung-Zwei

- **Keep the canonical copy in `.agents/skills/` and keep the symlink.** One copy of the files
  serves all six harnesses. A harness that reads both paths (Copilot, Cursor, OpenCode) may list
  each skill twice. To test: check whether that happens, and whether it does any harm.
- **Do not add `.github/skills` or `.cursor/skills` copies.** Every harness that reads one of those
  also reads `.agents/skills` or `.claude/skills`.
- **Descriptions do the routing.** For persona skills, the `description` is the only thing the model
  sees before choosing, so it has to name the files and situations that should trigger the skill. The
  skill-creator description optimiser can tune this once the skills settle.
- **The kernel's skills table is the fallback for the cases where routing fails.** It lists every
  skill with its trigger, so an agent that has the kernel in context but missed a skill can still
  find it.
- **Compaction:** only Claude Code is documented to re-attach skills after a summary. For every other
  harness the only defence is the kernel instruction "after every summary, load ordnung-resume". That
  is why it is the first line of AGENTS.md.

## To test per harness (one session each, on a throwaway install)

1. `tools/install /tmp/zwei-probe --persona <p>`, then start the harness in that folder.
2. Ask it to list its skills. Record whether every `ordnung-*` and persona skill shows up, once or
   twice.
3. Say "resume". Record whether it loads `ordnung-resume` on its own, or reads the file through the
   fallback.
4. Force a compaction (in Claude Code: `/compact`), then send one more task. Record whether it
   re-runs resume before acting.

## Sources

- Claude Code: https://code.claude.com/docs/en/skills;
  `.agents/skills` request: https://github.com/anthropics/claude-code/issues/31005
- Codex: https://developers.openai.com/codex/skills
- Copilot: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills,
  https://github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills/
- Cursor: https://cursor.com/docs/skills
- Gemini CLI: https://geminicli.com/docs/cli/skills/
- OpenCode: https://opencode.ai/docs/skills
