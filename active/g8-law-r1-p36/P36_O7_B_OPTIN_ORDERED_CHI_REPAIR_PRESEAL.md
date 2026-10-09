# P36-O7-B — Additive Registration-Order Repair Surface in Original Chi and Source-Relative Cost

**2026-10-10 KST, supplementary prospective pre-source acceptance.** P36-O7 primary D18 comparison is already presealed with original source Chi map vs original Gorilla route slice. This is **a separately frozen repair option**, not a retroactive modification of original Chi's contract. Existing `type HeaderRouter map[string][]HeaderRoute` and all public external Go map writes remain legal and unmodified in the old API.

## Repair target and exact allowed edit grammar

Original Go module `go-chi/chi@67be7d9cafdaeb4e04e887ff78d09e030ee43b00`. Allowed: **one newly authored extra file** `middleware/p36_o7_ordered_headers.go`; **no changes** to upstream route_headers.go or any other upstream source; original `HeaderRouter` remains accessible and stays functionally identical. The NEW opt-in constructor and methods:
```
func P36O7NewOrderedHeaderRouter() *P36O7OrderedHeaderRouter
func (*P36O7OrderedHeaderRouter).Route(header, value string, middleware func(http.Handler)http.Handler) *P36O7OrderedHeaderRouter
func (*P36O7OrderedHeaderRouter).RouteAny(header string, match []string, middleware func(http.Handler)http.Handler) *P36O7OrderedHeaderRouter
func (*P36O7OrderedHeaderRouter).RouteDefault(middleware func(http.Handler)http.Handler) *P36O7OrderedHeaderRouter
func (*P36O7OrderedHeaderRouter).Handler(next http.Handler) http.Handler
```
Within this surface registration uses an ordered slice of independent `HeaderRoute` entries, preserving the existing original Chi `NewPattern`, `IsMatch` and middleware semantics. The new API may be used by a client electing D18, while no old direct-map caller gains historical chronology automatically.

## Frozen acceptance Q0 and D18, extra case

Q0 unique header matches must dispatch correctly for both orderings. D18 both headers match and earliest **chronologically registered** must always win for both AB, BA across 128 repeated requests. Additional **same-header tie**: two routes of same header and identical values must dispatch earliest. Another `RouteDefault` when no registered predicate matches must dispatch fallback middleware without polluting when a match exists. MatchAny must preserve original Chi pattern behavior for same header when accessed through opt-in type. The new type is mutable during registration but **not** safe for concurrent calls with mutation; frozen tests register *before* serving. The old public mutable map similarly does not promise race-safe concurrent mutation. The exact absence of concurrency support is disclosed.

## Cost hypotheses and meaningful comparisons

- `B_classical_api_representation`: stable chronological priority is impossible from a source state that contains only final cross-header bucket maps of AB/BA and no log. A migration to new logging/order data or altered public interface can meet D18. This is a classical indistinguishability argument; no law identification.
- Since original Chi `HeaderRouter.Handler` scans per-request map buckets while new ordered surface scans per-request registration entries, `Q0` matching calls and source costs may differ depending how many entries, buckets and positive/negative matches exist. Freeze two workloads: (i) only one matching header, (ii) both matching headers. But **cost numbers are not comparable architecture rank** when the legacy map doesn't satisfy the new chronological priority contract under (ii). Benchmark within module `GOMAXPROCS=1`, five repeats, report `ns/op`, `B/op`, `allocs/op`, and cost of registration separately if useful. Never interpret an unpaired cross-package timing as intrinsic structural advantage.
- No fabricated novel structure law if original Gorilla and opt-in Chi both satisfy new client contract with different costs. Cross-repo evidence isolates representational information and API authority, while standard data structure semantics already explains it.

**At pre-source** `O7B_NEW_OPTIN_CHI_API_TEST_FROZEN__IMPLEMENTATION_NOT_YET_AUTHORIZED_AS_PASS__DIP49_HOLD`.
