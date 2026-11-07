# Verification & upstream truth — why evidence looks like this here

## "It's running" is not evidence

`restart: unless-stopped` plus a crashing entrypoint produces a container that is *running* and
dead at the same time. A restart loop looks healthy to `ps` and invisible until someone tries
to join. So verification in this persona is defined as the artifact of liveness: log lines
showing the server reached its ready state, and where the protocol allows, an external query
answer. The cheapest tier that can prove the claim is the tier you owe — `compose config`
proves the file parses, nothing more.

## Never against live saves without a go-ahead

The verification ladder creates and destroys containers. Tested against a user's real save
directory, a mistake during "just checking" becomes their worst day. Throwaway directories are
nearly free; deleted worlds are not.

## Upstream documentation is trusted last

Game publishers document server settings well and update those pages late or wrong: keys go
missing, ranges drift from what the binary enforces, out-of-range numbers get silently clamped
so a wrong doc fails quietly while invalid text stops the boot. The only source that cannot lie
about itself is the artifact the server produces — its generated config and its console output.
Hence: trust the artifact, record disagreements with URLs and dates so the next agent inherits
the finding instead of rediscovering it, and diff before adopting new settings rather than
auto-merging whatever an update writes.

This rule exists because agents are fluent summarizers of confident-sounding wrong documents.
The clamp-on-error behavior in particular means a doc-following agent can produce a config that
"looks configured" while the server quietly ignored it — only the generated file reveals that.
