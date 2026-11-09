# Agent Status — archive (append-only history)

## 2026-11-07 — Housekeeping: tasks closed as CANCELED (ownership-transfer phase)

Tasks retired without being carried out. User decision 2026-11-07: "None of the open
tasks in agent/STATUS.md are relevant anymore" — removed or archived as canceled, not
carried forward to a future phase.

- [x] CANCELED — Own security team: author the real security persona via tools/new_persona
- [x] CANCELED — Optional: tag contracts-v1.0.0 now that v1.0.0 manifests are public (listed twice in STATUS.md; both instances retired)
- [x] RESOLVED — Decide: keep or remove `contracts/persona/iac/rules/zoo-dcg-bug.md`
  → Removed. User decision: it was a workaround for a Zoo Code Agent bug and does not belong
  in this repo. Evidence 2026-11-07: file already absent from disk (`find . -name 'zoo*'` empty)
  and never committed (`git log --all -- <path>` empty), so no history purge was required.
  Stale references deleted from `agent/REPO-MAP.md` (index entry) and `agent/STATUS.md`.

Notes relevant to that decision: none outstanding — the file left no trace in git history,
so nothing to scrub on the remote.

## 2026-11-09 - Phase closed: new persona - tech-writing (DONE, branch feat_persona-tech-writing)

- [x] DONE - Scaffolded with tools/new_persona (template iac): contracts/persona/tech-writing/ with AGENTS.md, CLAUDE.md, the .github pointer, agent/, licenses/, rules/base.md and rules/verification.md.
- [x] DONE - base.md slots filled by a temp script reusing the reset_slot regex from tools/new_persona, so the core sections stayed byte-identical to the other personas and to the root copy: slot role (technical writer serving IT managers and IT administrators, decision-support bar for done), slot state-history (source plus retrieval date for external claims, sensitivity header field, drafts are never published, registers live in REPO-MAP), slot documentation (the deliverable IS documentation, README as landing page for the set, template and script doc pairings).
- [x] DONE - Modules authored, every top-level heading persona-marked, 40 to 58 lines each: documents.md (lifecycle outline / draft / in-review / released / superseded, header block, naming NNN-<type>-<topic>-v1.0, and the document map, shared facts, terminology and sources registers that carry multi-chapter work), open_questions.md (OQ-NNN register with OPEN / ASSUMED / DECIDED / NOT-APPLICABLE, the load-bearing rule, the banned wording list, an ambiguity audit that reports a count), output_formats.md (format menu: Markdown, Word and LibreOffice rich text, user-specified; never choose the format silently; one source many targets; offer the code path - pandoc, python-docx, docxtpl, openpyxl, matplotlib; round-trip check on the export), comparisons.md (declare the question, criteria and weights, per-cell sourcing, unknown as a legal cell value, like-for-like units, fairness and steelman pass, verdict as consequences, expiry date), advisories.md (audience split, BLUF skeleton, design skeleton, fixed urgency label set, mandatory validation plan), visuals.md (visual pass with FIG-NN placeholders, table / graph / matrix / diagram taxonomy, caption plus source plus alt text plus an in-body reference rule, diagrams kept as code, screenshot redaction), dr.md (slot decision-records, DR triggers per module).
- [x] DONE - Manifest agent/ruleset.md (persona tech-writing, version 1.0.0); agent/project_layout.md (document-project tree, registers in REPO-MAP, build output kept out of the index); agent/bootstrap.md (scope, license per component, the format question as step 3, skeleton with the registers started empty, the freshness-probe offer kept).
- [x] DONE - Rationale pages under docs/agent-contract/: index.md, base-contract.md, document-set-and-memory.md, comparisons-and-advisories.md, format-and-visuals.md, open-items-and-ideas.md (idea roadmap: style_guide, review, accessibility, localisation, compliance_mapping, release_notes, runbooks, security_advisory, vendor_questionnaires, cost_models, meeting_docs, doc_as_code, content_governance, reader_profiles, notations, source_tiers, export toolkit).
- [x] DONE - Registered in README.md (persona table row, rationale bullet, the wording change to All contracts share, the DR naming note) and in agent/REPO-MAP.md (persona section, plus the tools/new_persona smoke-test note extended to 2026-11-09).
- [x] DONE - Verified: python tools/check_sync printed OK with exit 0 (core equality across four personas plus the root copy, slot headings present, manifest SemVer valid). Every new file is BOM-free and ASCII-only; README.md and agent/REPO-MAP.md were edited through a UTF-8 Python pass that preserved existing line endings, em-dashes and check-mark emoji.

Notes kept for history: pytest was not run - uv is absent from PATH and system python 3.15.1 has no pytest; tests/ and tools/ were untouched, so check_sync is the applicable gate. Transport mechanics worth keeping: JSON decoding of tool input eats single backslashes, so use forward slashes in PowerShell paths; Set-Content with -Encoding utf8 writes a BOM, which hides the first heading of a file from the parser in tools/check_sync; non-ASCII typed into a command arrives mangled, so non-ASCII output is produced with Python unicode escapes.

- [x] DONE - Pushed feat_persona-tech-writing to origin (tracking set) and opened PR #2 against main: the persona, its nine rule files, the check_sync evidence, and the pytest caveat recorded in the body. PR verified with gh pr view 2: state OPEN, mergeable MERGEABLE, 29 changed files, +1149/-12. No tag and no CHANGELOG.md, per the user choice of push-and-PR only.
