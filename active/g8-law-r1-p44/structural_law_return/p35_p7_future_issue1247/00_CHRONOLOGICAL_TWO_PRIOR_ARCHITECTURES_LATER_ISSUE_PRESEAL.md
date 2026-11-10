# EvoNOMOS — Prior P35-P7 architectures crossed with later independent external issue #1247

**2026-11-10 KST — PREEXECUTION TREATMENT CONTRACT.** Historical chronological distinction: two real research-owned source treatments LIVE and SNAPSHOT were committed **Oct 9 2026** and tested on real go-chi v5.1.0 with common initial routing contract D0. Independent external maintainer [go-chi issue #1247](https://github.com/go-chi/chi/issues/1247) filed **Nov 1 2026** reports RouteHeaders fails an identical mixed-case exact pattern. So source structural variants predate issue publication. However the analyst read issue description before creating these tests and subsequent repair, so this is *historically time-split, outcome-aware*, NOT a genuinely blind prediction nor new maintenance-agent replication.

Frozen authentic old source: go-chi/chi original v5.1.0 commit `67be7d9cafdaeb4e04e887ff78d09e030ee43b00`, replace only `middleware/route_headers.go` in separate ephemeral Go checkouts by existing P35-P7 arm full source files. Never edit the already committed arm snapshots: derive repaired file as separate temporary source patch.

## Both arms, old contract parity
- original P35-P7 D0 accepted route priority and exactly-once default, existing native Go tests.
- original P35-P7 D8 identical demand may also be rerun; no broader time-mode universal contract is possible since D-LIVE and D-FROZEN contradict one another.
- route original patterns lower-case: matching `gold` with incoming `Gold` succeeds.
- wildcard lower-case `g*` with incoming `Gold` succeeds.
- suffix/prefix lower-case wildcard too.

## Independent later #1247 requirement
- `Route("X-Tier","Gold",...)` must match incoming `X-Tier: Gold`.
- `RouteAny("X-Tier",[]string{"Silver","Gold"},...)` matches incoming Gold.
- configured mixed-case wildcard patterns `Go*` and `*OlD` must behave consistently with lowercased incoming value. These wildcard cases extend the report and are RESEARCHER-authored from original pattern interface, not independently stated in #1247. Classify separately.
- unrelated headers and fallback remain unaffected, no transformation of header **names** beyond existing HTTP normalizations.

## Two source repair strategies constrained to SAME original source API
- Proposed common MINIMAL classical fix: normalize `match`/pattern text at the point of `NewPattern` construction by `value=strings.ToLower(value)`. This is one source-level edit, shared across both architecture arms, because both P35-P7 variants use common `NewPattern` representation. It is an ordinary source-aware normalization repair, not a novel law or a separate owner interaction.
- Both arms must FIRST demonstrably fail the independent new customer contract prior to repair, then pass after repairing the exact same construction point. The test harness must preserve a negative-red result, not count overall expected-red green as customer compliance.
- Require original full `go test -count=1 ./...`, `go vet ./...`, original middleware race tests and existing P35-P7 D0 and D8 tests on the repaired source; keep all other upstream production source unchanged.

**Falsification:** If one original historical arm already meets #1247, or the proposed one-line normalization fails old/native/new tests, record the difference and do not claim a tie. No real independent maintainer actors executed and no measured actual maintenance labor. If both satisfy same old and new requirements with one identical source patch, this supports a *bounded cross-architecture tie*: the LIVE/SNAPSHOT structural moderator did not affect this new requirement's test or source file touched, NOT general architecture equivalence, no novel conditional law.

P44 G1–G7 OPEN. LAW-R2 HOLD.
