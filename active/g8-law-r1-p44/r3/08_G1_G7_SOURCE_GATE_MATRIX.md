# Source certification gate matrix

G1 receiver/capability resolution: exact middleware.RequestID and router handlers are pinned, not a complete dynamic Go call graph.
G2 alias and concurrency: explicit shared pointer, mutex locks, request-local string and deterministic ordering; bounded evidence, not general concurrency proof.
G3 bounded source call graph: manually inspected names and partial AST schema only, no sound whole-source analysis.
G4 protected client effects: sequential GET/POST/GET and one temporal interleaving with response status/body and injected RequestID, not all possible effects.
G5 observation completeness: one fixed old-client family and one future demand; arbitrary HTTP contexts not covered.
G6 permission provenance: app-owned fixture editing, no independent upstream maintenance rights.
G7 actual repair cost: one synthetic middleware-copy edit; no human time, infrastructure burden or lifecycle cost estimate.

Current R3 aims to materially probe G2 and G4 under a clearly bounded source model. All seven remain OPEN as general software claims; LAW-R2 HOLD.
