# Contract manifest — game-hosting persona

persona: game-hosting
version: 2.0.0

Self-contained drop-in contract for hosting dedicated game servers: user-configurable Docker
Compose projects with a bundled (auth + TLS enforced) web panel that manages one or more game
servers, local-only or internet-exposed by the operator's choice.
Modules: base.md, verification.md, usability.md, web_frontend.md (always); docker_compose.md
(almost always); steamcmd.md, python.md (when in use). Third-party licensing & distribution rules live in
steamcmd.md.
Boot pointer: AGENTS.md.
