# Verification: why documents become tests

Companion to `rules/verification.md` (and the Enforcement section of `rules/adr.md`).
The rule files tell agents what to do; this page explains why, for the people who
maintain the rules and review the work.

## The problem

Design work with agents produces a lot of prose: decisions, task lists, status notes,
"verified" claims. Prose is never executed, so nothing notices when it goes wrong.
Every time a topic is revisited, some documents get updated and some do not, and the
stale ones still read as authoritative. Smaller models make this worse: they write
fluent, plausible text whether or not it is true.

The fix is to move every claim that *can* be checked into something that is checked
on every run, and leave prose only for the reasons behind decisions.

## Four kinds of statement

| Kind | Example | Becomes |
|---|---|---|
| Requirement | "Dry run never marks configuration deployed" | A spec test that exercises real code, a rendered config, a plan or a playbook in check mode |
| Decision / constraint | "Domain code never imports vendor code" | A constraint test over the source tree, config or built artifacts |
| Fact about the outside world | "The vendor API rejects field X on VLAN interfaces" | An evidence record that can be re-run, or a fixture recorded from a real device |
| Rationale | "Reliability before speed" | Stays prose |

## Tests as the task list

A requirement that is not built yet is still written as a test now, marked as an
expected failure. Two settings make that marker trustworthy:

- **Limited to "not built yet"** (pytest `raises=ModuleNotFoundError`). If the code
  exists but behaves wrongly, the test fails loudly instead of hiding behind the marker.
- **Strict.** When the code lands and the test unexpectedly passes, the run fails until
  someone removes the marker, so the backlog can never silently drift out of date.

The set of expected-failure tests is then the backlog of testable requirements, and a
task closes when its test passes rather than when a status line says so.

## Decisions name their enforcement

Where a project uses ADRs, each one lists what enforces it (`Enforced by:` entries). A
meta-test fails when an accepted decision enforces nothing, or points at a test that
no longer exists. Older decisions without enforcement sit on a debt list that may
only shrink: the test fails when a listed decision gains enforcement, forcing the
list to be updated.

The payoff comes when a decision changes. Change its tests first and the failures show
everything the change touches; update the prose afterwards.

## What link checks cannot catch

A docs-integrity test catches references to things that do not exist. It cannot catch
a record that was **invented to fit its references**. This happened in practice: a
renumbering left old citations behind, and an agent wrote a new record matching what
the citations seemed to expect, along with a test that only checked a table defined
inside itself. Every structural check passed. That is why the rules forbid creating a
target to resolve a dangling reference, and why a test must exercise something outside
the test file.

## Ports and existing code

When code is migrated or consolidated, intent documents (change logs, READMEs) and
the code itself can disagree. The code is what actually ran, so it wins, and the
disagreement is recorded. Golden-file (characterization) tests capture what the old
code produces for a matrix of inputs. The new code must reproduce it, and every
intended change is its own commit with its own test, so behaviour never shifts
unnoticed inside a "port".

## The test ladder for infrastructure as code

Run the cheapest checks first; each tier gates the next.

1. **Static**: lint; schema-validate inventory, variables and data files.
2. **Rendered**: templates, plans and API payloads compared against golden files.
3. **Check mode / dry run** against fixtures: non-mutation is asserted, not assumed.
4. **Idempotency**: a second run reports zero changes.
5. **Lab / live**: opt-in, against an explicitly allowlisted target, never in default CI.
6. **Canary / production**: approval-gated.

A lower tier never certifies what only a higher one can show: fixtures do not prove
device ordering, and one test VM does not prove fleet throughput.
