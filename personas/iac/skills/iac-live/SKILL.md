---
name: iac-live
description: Rules for touching real infrastructure — lab and live devices, acceptance and production environments, deployment hosts, read-only probes, write experiments on scratch devices, recording fixtures, certificate pinning, the git-ignored LAB notes file for lab facts, customer data handling, and read-only reference repositories. Use this before any command that reaches a device, host, API or environment outside the local machine, before running a lab script, when recording device answers, when loading credentials from env files, and when reading a legacy or reference repository.
---

# Lab and live work

A unit test that is wrong costs a rerun. A write to the wrong firewall costs an outage. Every
command that leaves the machine is either read-only, or a write the task and the owner allowed,
against a target on the allowlist.

## Before you connect
- **Name the target and the environment.** Which device or host, whether it is lab, acceptance
  or production, and whether the action is read-only or a write.
- **Read the lab notes.** Use the project's git-ignored lab file (for example `agent/LAB.md`,
  named in the REPO-MAP) for addresses, pins and the firmware in use. Keep it current, as you do
  STATUS. Credentials never go in it: they stay in `.env` or the vault.
- **Credentials** come from env files through a runner script, so they never appear on a command
  line, in a log or in the transcript. Map the env keys onto the tool's variables inside the
  runner.
- **TLS.** Verify the peer, or pin its certificate. A pin is recorded with where it came from
  ("owner-confirmed in the UI, date").

## Read-only by default
- Probes use `GET` or the equivalent read calls. Their raw output goes outside the repository
  (scratch or state directories); only redacted extracts come in.
- A write experiment runs only against a scratch or factory-default lab device the owner has
  designated for writes. It touches only objects it created itself (a name prefix it owns), and
  cleans up after itself.
- Production and acceptance change only through the project's reviewed apply path, run from a
  tagged release, with the owner's go for that change (kernel rules 7, 10 and 12).

## Evidence from devices
Record what you ran, against what (model, firmware, environment), when, and what came back. Put
the short form in the HANDOFF `evidence:` field, and the detail in the lab notes or a design
doc. When the device contradicts the vendor documentation, the device wins: record both.

## Customer data
- Customer configurations, database dumps and exports stay outside git. Only aggregates and
  redacted, labelled fixtures come in.
- A local copy of customer data (a dump in a throwaway database container) is listed in the lab
  notes, and removed when the task is done. Removing it is a board task with the owner, if the
  owner holds it.

## Reference repositories
Legacy or sibling repositories named as read-only in the REPO-MAP are read-only: never commit
or push to them. Never copy code across a repository boundary that a decision record draws:
read it, then write it anew on this side.

## Hosts
SSH and remote commands follow the same rules. Name the host. Run read commands freely, but
writes, restarts and `docker`/`systemctl` actions on a shared host need the go for that action.
Before an action that can't be undone, show the exact command first.
