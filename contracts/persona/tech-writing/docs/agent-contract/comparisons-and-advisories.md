# Comparisons, advisories and the evidence ladder

Companion to `rules/comparisons.md`, `rules/advisories.md`, `rules/verification.md` and
`rules/dr.md`. Start at [index.md](index.md).

## The failure this pair exists for
A model can produce a confident, well-structured comparison of two products where half the feature
rows describe capabilities neither product has. Structure hides it: a tidy table reads as research.
The rules that counter it are boring - every cell cites a source, `unknown` is a legal value, every
row names its version - and they are the most valuable rules in this persona.

## Why "unknown" is a legal cell value
A rule that forbids guessing without offering a legal alternative produces confident guessing.
Naming `unknown` admissible removes the temptation and makes the gap actionable: it says what work is
left, and on a must-have criterion it stops the comparison being decision-ready, which is the honest
status of that document.

## Why sources are snapshots, not links
Vendor documentation changes without notice; price pages vary by region and session. A URL cited in
a comparison released in March is unverifiable in June. `sources/` keeps the retrieved page, export
or release note, named `<src-id>_<YYYY-MM-DD>`, so a claim can be re-checked and so "the vendor
changed it" becomes a dated fact rather than an argument.

## Why vendor claims are labelled
Vendor-authored material is not false by default; it is unaudited. One cell note lets the reader
weight the row. Mixing a vendor claim and an independent measurement in one sentence makes the
measurement borrow the vendor's credibility, which is how a comparison becomes marketing.

## Why the fairness pass is a rule, not a virtue
Asymmetry is the default: the familiar product gets the deep read, the unfamiliar one gets the
summary. The pass is written as a check - same depth, steelman each option, name what would change
the recommendation - because its outcome is visible in the text. An option that wins on nothing is
usually a criteria problem, and saying so is what makes a close recommendation trustworthy.

## Why a tick matrix is not a verdict
Managers decide on consequences: who operates it, what it costs to run, how to leave. A 40-row
feature grid answers "what does it have", which is rarely the binding constraint. The module
requires the narrative - fit for purpose, operational burden, licensing and exit path, migration
effort, risks, cost shape - because that is the part a reader can act on.

## Why the advisory skeleton front-loads the answer
Executives read the first screen and stop. A recommendation on page six was not read. Bottom line up
front is a reader-protection rule; the rest of the skeleton exists so the summary can be traced -
options, rationale, risks, costs, next steps with owners, open items, sources.

## Why urgency labels are a fixed set
"Critical" means "stop everything" to one reader and "noted" to another. A fixed set with a window
(`Action required by <date>`, `Advisory - next maintenance window`, `Notice - no action`) is
auditable, and it forces the writer to commit to the window they mean.

## Why the validation plan is mandatory in designs
"It should work" is where designs die. Naming the test, pilot or check that will prove the design,
and who runs it, turns a design into something an administrator can accept - and gives the document a
completion criterion, which is what `rules/verification.md` is for.