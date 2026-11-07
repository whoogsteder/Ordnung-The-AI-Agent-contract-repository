# Frontend security — why auth and TLS are defaults, not options

## The exposure assumption

The web frontend controls a game server: read and change settings, restart processes, browse
save-adjacent state. It is built for a LAN, but the user who grows confident will eventually
port-forward it — often after reading one forum thread about "opening your server." A contract
that hardens only for LAN quietly sets that user up: the moment of public exposure is exactly
when weak defaults get exploited, and game-server hosting has a long history of scanner-driven
compromise of exposed admin panels and RCON ports.

So the rules assume **the frontend may be public** and make the safe configuration the only
configuration:

- **Fail-closed auth.** The container refuses to serve with missing or placeholder credentials.
  A warning in a README is read once, if ever; a boot failure is impossible to ignore. This is
  the difference between "we told them" and "they cannot get it wrong."
- **TLS always, self-signed acceptable.** Encryption without a trusted chain still stops
  credential sniffing on LANs and café Wi-Fi. Accepting self-signed removes the excuse to run
  plain HTTP; the upgrade path (real certificates) is documented so the warning never becomes
  "just click through, it's normal."
- **No re-proxying of game admin surfaces.** RCON and save paths are the crown jewels behind
  the crown jewels. What the proxy forwards is validated by test, not asserted in a comment —
  comments rot, tests don't.

## Why bundled-only

Support surface is effort. A frontend supported standalone multiplies every install question by
two platforms and every reverse-proxy recipe by however many nginx configs exist in the wild —
and each hand-rolled proxy setup is a chance to strip out the auth or TLS the contract just
enforced. Bundling keeps one tested path: `docker compose up`, security intact.

## Why Caddy-preferred, nginx-allowed

Caddy's default behavior (HTTPS on, `tls internal` for local names) aligns with the contract
without configuration; nginx requires every directive to be written correctly by hand, and each
hand-written TLS block is a fresh chance at a subtle miss. Users who know nginx are not forced
to learn Caddy — but the shipped config must be complete and explicit, because nobody gets to
run the frontend outside this project where "it works on my proxy" would apply.
