# Agent contract — rationale

This directory explains **why** the rules in `rules/` exist. The rule files are the contract
agents must follow; these pages are the reasoning behind it, written for the humans who
maintain this contract and review agent output — and for agents only when explicitly asked.

> Not agent boot material. Nothing here is read during the session-start protocol.

## Pages

- [base-contract.md](base-contract.md) — why an inexperienced-operator audience shapes every
  rule: pinning, save-data protection, marked OS dependencies, confirmation before destruction.
- [frontend-security.md](frontend-security.md) — why auth and TLS are non-negotiable defaults on
  the web frontend: the public-exposure assumption and the fail-closed stance.
- [verification-and-upstream.md](verification-and-upstream.md) — why container evidence is log-
  and query-based, and why upstream (vendor/game) documentation is trusted last.
- [licensing-and-distribution.md](licensing-and-distribution.md) — why self-hosting is permitted
  use while redistribution of fetched game content is the real line; Docker vs Desktop licensing;
  why Docker stays the documented default with Podman-compatible artifacts.

## Writing rationale pages

One page per rule area. Explain the decisions a newcomer would question: why digests, why no
standalone frontend support, why self-signed TLS beats plain HTTP. Cite the real failure each
rule prevents where one exists.
