# Design of the research persona - rationale

## Why research is a persona of its own
The `tech-writing` 1.x persona did questioning, research, writing and governance in one contract. In
its first real use, a product selection, the research was the part that failed. Candidate
specifications were written from the model's memory and tagged "unverified". Both recommended models
failed the document's own must-haves, and the vendor's reference switch for the attached platform was
never considered. The writing and the bookkeeping had taken the attention.

Splitting research out gives it a contract that is about nothing else: a sharp question, primary
sources, screening on checked facts, and a hand-over in a fixed shape. The `document-writing` persona
consumes that hand-over.

## Memory decides where to look, sources decide what is true
A language model is good at knowing that a vendor has a datacentre switch line, and bad at knowing
which model has 48 SFP28 ports and which has 48 copper ports. The method module lets memory steer
the search and forbids it from supplying facts. The cost is a few more lookups. The saving is a wrong
recommendation that would otherwise surface after the purchase.

## Why the longlist starts from compatibility lists and reference designs
The candidates that failed in the field test came from the model's sense of each vendor's portfolio.
The candidate that should have been there came from the vendor of the attached server platform, which
publishes the switch it validates for exactly that use. Starting from the systems the option must work
with surfaces those candidates first.

## Why the pack has a fixed shape
A writer, another agent or a reviewer must be able to find the answer, the facts, the screening and
the gaps without reading the whole thing. Fixed sections, fact ids and source ids make the pack a
dataset that can be checked line by line. The prose belongs in the writer's document or the research
brief.

## Why "no public source states X" is a finding
Agents tend to fill a gap with something plausible. Making "not found" a legitimate result, reported
as plainly as a found fact, removes the pressure to guess.

## Why a separate reviewer
A researcher who has just searched for something remembers what they meant to find. A reviewer with
no prior context re-opens the sources and spots a missing candidate or a mismatched version. Where the
tool supports sub-agents, the review runs as one. Otherwise it runs as a second session.

## Lessons from the first field test (2.0.0)
The first run, a top-of-rack switch selection, produced a pack whose shortlist held up on ports,
standards and the attached system's compatibility list. An independent review still failed it, for two
reasons the rules now cover:
- **Lifecycle status was read from a datasheet.** A spec sheet revised last month says nothing about
  whether the product can still be bought, and one vendor dated its OS options on the same hardware
  apart. Lifecycle status now comes from the vendor's lifecycle record, per hardware and OS
  combination, or is `not established`.
- **A must-have term had two readings.** The pack picked one without saying so. Ambiguous terms are now
  pinned down while the question is agreed.
The same run showed the question gate costing about as much as a quick scan: five rounds before the
first search. Confirmation is now defined, so it is not asked for twice. For a quick scan the gate
takes one round, and only should-haves may go ahead as assumptions. Must-haves never do. The pack
directory moved from `research/` to `topics/`, because a project root called `research` produced
`research/research/<topic>`.
