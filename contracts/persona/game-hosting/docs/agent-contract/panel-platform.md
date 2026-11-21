# Panel platform — why the panel is always bundled, and what it may never become

## Why the panel stopped being optional

The first contract treated plain compose as the delivery and the panel as an add-on. In practice
the panel is what makes a project usable by an operator who has never hosted a server: it is
where a setting is explained, validated and applied, where a backup is restored, and where a
failing server is noticed. Keeping it optional meant every feature had two paths — panel and
hand-edited env file — and the second one was always the less tested. Version 2 makes the panel
part of every delivery and moves the operator's choice to where it actually matters: whether the
panel stays local or faces the internet.

## Why the game must not depend on it

A mandatory panel must not become a single point of failure. A panel crash, a bad panel image or
an upgrade should cost the operator their admin screen, never their players' session. That is why
game servers keep their own restart policy, why a panel restart never recreates a running server,
and why the README carries the plain container-runtime commands for the day the panel is the
problem. The rule asks for a test because "it does not touch the game" is exactly the kind of
claim that is true until a reconcile loop is added.

## Why panel-owned containers, and why ownership is exclusive

One panel managing several servers has to create game containers that the compose file does not
list — otherwise adding a game means editing compose, which is the step the panel exists to
remove. The obvious shortcut, creating containers that compose then "adopts", does not work:
compose decides whether a service is up to date by comparing the live container with its own
freshly resolved project model, and it recreates a container it did not create even when labels,
network and config hash match. So the panel owns its containers outright, compose owns the
platform, and neither touches the other's. Labels keep the panel's containers findable without
the panel; a desired-state file keeps them reproducible after a rebuild.

## Why resource usage is mandatory on a many-server panel

With one server, "the host is slow" has one suspect. With several, the operator needs to see
which server is eating memory or disk before deciding what to stop, and an inexperienced operator
will otherwise guess. Numbers come from the container runtime's own statistics because an
estimate that is wrong is worse than a server shown as unmeasured.

## Why the env file shrank to the stack

When one game was configured entirely through env variables, the env file could be the whole
product surface. Once a panel manages several games, each with its own native config format, env
variables become a lossy translation layer for game settings: types flatten to text, quoting
rules differ per parser, and the image's entrypoint decides what survives. The env file keeps
what the stack needs before any game exists — ports, paths, credentials, exposure — and game
settings go to the file the game itself reads.

## Why a Python module

The panel and its tooling are expected to be largely AI-written and reviewed by an operator. Code
the reviewer cannot read is code they can only trust, so the language should be one they read.
Python's usual cost — dependency trouble on the host — does not reach the operator, because
everything runs in a container. What Python gives up against a compiled language (static checks,
a single binary) the module buys back with strict type checking, a hashed lockfile, and a
commit-blocking gate that runs the same commands everywhere.
