# STATUS

## HANDOFF
task: T-9 second managed instance (7 Days to Die)
status: IN_PROGRESS
next_action: >
  The measurement spike is done. The 7D2D image does not honour stop: PID 1 is the shell
  wrapper, so docker stop -t 20 took 21 s and SIGKILLed, and with --init it stopped in 1 s
  but wrote no final save. That means restore cannot be offered for it. Also games.Target
  needs a file field before any game with no env layer can be written for, because 7D2D has
  no env layer and the panel would own serverconfig.xml outright. Next, decide with the
  user how to deploy it, then write the panel game definition.
skills: [ordnung-checkpoint]
constraints: none
files: panel/internal/games/sevendays.go
evidence: none
last_update: 2026-11-25T09:10
