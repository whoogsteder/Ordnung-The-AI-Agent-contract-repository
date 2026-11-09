# Open items, and where this persona could grow

Companion to `rules/open_questions.md`. Start at [index.md](index.md).

## Why the no-silent-assumptions rule is the persona's spine
Document work is asymmetric: the writer knows exactly what is missing, and the reader cannot see it.
A fluent advisory transfers the writer's confidence to the reader - including confidence about the
parts that were guessed. So the rule converts a feeling (uncertainty) into an artifact (a numbered
register) that survives compaction, review and handover. It is the same move the core makes for agent
memory: do not remember it, write it where the next reader must find it.

Three properties make the register work:
- **Numbered** - referenceable as `OQ-07` in review, in STATUS.md, and in the next session.
- **Statused** - OPEN / ASSUMED / DECIDED / NOT-APPLICABLE, so an assumption is visible as an
  assumption and a settled question stops being argued.
- **Impact-bearing** - each entry says what changes if the answer is no, which is what tells the
  reader whether to stop work.

## Why the banned wording is listed explicitly
"etc.", "as needed", "where appropriate", "several" are how a writer defers a decision without
recording it. Naming the phrases makes the audit mechanical: it is a search, not a mood. Removing one
forces the count, the closed list, the owner, or an OQ entry.

## Why the audit reports a count
"Open items: 3 (1 load-bearing)" is something the user can close in a sentence. A paragraph of
caveats invites skimming; a count invites a decision. The count also makes the honest status visible:
a design with a load-bearing OPEN item is `not decision-ready`, and saying so early is cheaper than
being found out at the steering meeting.

## Ideas this persona should hold

Built in at 1.0.0: format menu with a code-generation offer; open-items register with banned wording
and an ambiguity audit; visual pass with a figure taxonomy and diagrams-as-code; comparison discipline
(criteria, weights, sources, fairness, expiry); design and advisory skeletons with an urgency label
set and a validation plan; document lifecycle with immutability and the registers for multi-chapter
work; a decision-records slot for format, criteria and architecture choices.

Not built - candidates, each with its own trigger and DR:

| Idea | Module | Why it is worth having |
|---|---|---|
| House style + linter | `style_guide.md` | Active voice, sentence-length cap, spelling variant, product-name casing table; enforceable with Vale/markdownlint |
| Review workflow | `review.md` | Reviewer roles, finding classes (blocking/nit), sign-off record, review comments turned into OQs and DRs |
| Accessibility | `accessibility.md` | Heading hierarchy, table headers, alt text, contrast, reading order, PDF tagging |
| Multilingual sets | `localisation.md` | Term base, translation memory, do-not-translate list, locale formats |
| Compliance mapping | `compliance_mapping.md` | ISO 27001 / BSI C5 / NIS2 / SOC 2 / GDPR: required document types, evidence pointers, review cadence |
| Release notes | `release_notes.md` | Change records for administrators: blast radius, action needed, rollback |
| Runbooks | `runbooks.md` | Trigger, prerequisites, steps with commands, expected output, verification, rollback, escalation |
| Security advisories | `security_advisory.md` | CVE/CVSS fields, affected version ranges, workarounds, disclosure timing |
| Questionnaires | `vendor_questionnaires.md` | RFP/RFI/security/TPA answer library with source and date, consistent across questionnaires |
| Cost and capacity models | `cost_models.md` | TCO and capacity as a small script with inputs in one file: computed, not typed |
| Meetings | `meeting_docs.md` | Agenda, decision log, actions with owners and dates (grows out of advisories.md) |
| Docs-as-code gates | `doc_as_code.md` | CI: style lints, link and anchor checks, header-field checks, figure-exists, export build |
| Content governance | `content_governance.md` | Owner per document, review and expiry dates, sign-off matrix, deprecation policy |
| Reader profiles | `reader_profiles.md` | Named personas (IT manager, sysadmin, CISO, procurement): their questions, vocabulary, what they skip |
| Notation register | `notations.md` | C4 levels, sequence and ERD conventions, network-topology notation (layers, ranges, boundaries) |
| Source tiers | `source_tiers.md` | Tier 1 standard, tier 2 vendor doc, tier 3 independent lab, tier 4 community - and what each may prove |
| Export toolkit | `scripts/export.py` | pandoc reference.docx builder, python-docx exporter, style-name checker, one-command build |

Adding one is a normal authoring step: a `<!-- persona -->` file of 40-60 lines, a DR for the choice,
a manifest line, a rationale page, and a minor version bump.