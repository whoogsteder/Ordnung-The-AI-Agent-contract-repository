# Scope <!-- persona -->
Applies: always. Requires: base.md.

- Read only the source roots declared in configuration. Never walk outside them, and never follow
  a link or path that escapes them.
- Respect ignore files. An ignored path is out of the corpus even when it is on disk.
- The tool does not write to the index store on behalf of a client. Writes happen through the
  indexer, from committed files, so provenance cannot be bypassed by whoever is holding the
  credential.
- Credentials come from the environment or the operator's secret store — never from a document in
  the corpus, and never echoed into logs, errors or evaluation output.
- A request that needs data outside the declared roots is a configuration change the operator
  approves, not something to widen at runtime.
