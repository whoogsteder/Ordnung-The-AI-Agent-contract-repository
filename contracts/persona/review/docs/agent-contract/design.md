# Design of the review persona - rationale

## Why review is a persona
The `tech-writing` 1.x field test produced a document whose own open-items list suspected that the two
recommended switches had the wrong port layout, and it recommended them anyway. The author had all the
information. What was missing was someone whose only job was to say "this fails a must-have" and who had
no stake in the draft.

`document-writing` and `research` each tell their agent to prefer a separate reviewer. Not every agent
can start a sub-agent, so the reviewer needs a form that works everywhere: a persona that can run as a
second session, and whose rules double as sub-agent instructions where sub-agents exist.

## Independence is defined by what the reviewer may not read
A reviewer that reads the author's notes and reasoning inherits the author's blind spots. The rule is
therefore about inputs: the artefact, its yardstick, its sources and the stated reader, and nothing
else. A missing yardstick is asked for, never reconstructed from the artefact, because that would let
the artefact grade itself.

## Why the reviewer builds its own must-have table
Copying the author's table checks only that the table is internally consistent. Building it from the
sources is what would have caught the 1G-copper switch in the field test.

## Why memory may not judge facts in either direction
"That port count looks wrong" from memory is as unreliable as "that port count looks right". Both
produce confident findings without evidence. The reviewer opens the source, or marks the fact "not
checked".

## Why the missing-candidate check
The most damaging error in the field test was an absence: the vendor reference switch for the attached
server platform was never on the list. Absences do not show up in a line-by-line check of what is on
the page. They need a deliberate look at where candidates should come from.

## Why three severities and a verdict
The owner needs to know in one line whether the artefact may be used. "Fail" is reserved for blocking
findings, so a pile of style notes cannot sink a sound document, and a single wrong must-have cannot
hide among them.
