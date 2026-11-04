# Source-aware classical rival: a bounded route-disjointness certificate

Unlike the 3-bit mathematical LTS, this analyzer parses the actual Go router.go AST with go/parser and go/ast. It extracts the predeclared FrozenDemands source literal, checks that exactly three source paths appear, and verifies pairwise disjointness of those paths and the original /items/{id} route under a strict grammar: slash-separated literal segments and one-segment {parameter} wildcards, no catch-all, no regexp, no host/method and no middleware.

For the actual R2 source it extracts:
- /ledger/{id}/revisions
- /ledger/{id}/audit
- /ledger/{id}/summary

Under the named limited segment grammar these paths have no pairwise overlap, so route-registration interference is not expected. Deliberate negative controls detect wildcard/wildcard and wildcard/static overlap. Pure Go1.23.2 source parser tests, go vet and race checks PASS locally.

This is a **source-aware classical rival** built from normal Go AST tools and elementary path intersection, not a new EAC theorem. It is narrower than true Chi or stdlib router semantics: route registration order, encoding, method handling, regex, catchall and nested mounts remain native execution obligations.
