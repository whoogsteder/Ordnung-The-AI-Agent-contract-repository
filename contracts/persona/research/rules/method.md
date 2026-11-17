# Research method <!-- persona: module header -->
Applies: every research task. Requires: base.md, `rules/question.md`, `rules/sources.md`.

## Plan before searching
Write a short search plan into `agent/STATUS.md` before a long run of searching: the sub-questions,
where each answer is most likely to be found, and what will count as enough. Update it when the plan
changes. This also serves as the checkpoint the base contract asks for.

## Go to the source most likely to be right
Prefer, in this order:
1. **Primary sources**: the standard itself, the vendor's datasheet, lifecycle or end-of-sale page,
   release notes, compatibility or validated-device lists, official documentation for the version in
   use.
2. **Reference designs and validated configurations** from the vendor of the system the answer must
   attach to.
3. **Independent measurement or analysis** with a stated method.
4. **Practitioner sources** (forums, blogs, issue trackers): useful for problems and real-world
   behaviour. Mark them as such, and confirm them elsewhere when they are load-bearing.
5. **Marketing material**: a claim to be checked, never evidence on its own.
Never answer from memory. Memory is useful for deciding *where to look*, never for *what is true*.
Model names, editions, port layouts and dates are exactly what memory gets wrong.

## Options: longlist, screen, shortlist
When the question asks for options (products, approaches, suppliers):
1. **Longlist from current sources**: each allowed vendor's current portfolio, the compatibility lists
   and reference designs of the systems the option must work with, the incumbent's named successor,
   and the preferred supplier's current equivalent. Record where each candidate came from.
2. **Screen** every candidate against every must-have, with a source per cell. A candidate that fails
   a must-have, or is end-of-sale or announced end-of-sale, is out, with a one-line reason.
3. **Shortlist**: only candidates that pass every must-have on checked facts. A candidate whose status
   cannot be established stays on the longlist with the reason. It is never shortlisted "pending
   verification".
4. **Compare** the shortlist (`rules/comparisons.md`).
Ask yourself: is an obvious candidate missing? An empty or one-item shortlist is a finding to report,
not something to fill with weaker candidates.

## Triangulate what matters
- A **load-bearing fact** is one that decides a must-have, puts an option in or out, or drives a
  conclusion. Check it against the primary source. Where the primary source is unclear, confirm it with a
  second, independent source.
- When sources disagree, record both, say which you trust and why, and flag it in the pack. Never
  average them, and never silently pick one.
- Check that the source covers the right version, edition and date. A datasheet for the wrong
  hardware revision is the wrong source.

## Know when to stop
Stop when every sub-question has an answer at the agreed depth, every load-bearing fact is checked, and
new searches return what is already known. Report what was not found as plainly as what was. "No public
source states X" is a finding.

## Access limits
If a needed source is unreachable (no web access, login, paywall, internal system), say so to the user
and ask them to supply it. Do not substitute a guess.
