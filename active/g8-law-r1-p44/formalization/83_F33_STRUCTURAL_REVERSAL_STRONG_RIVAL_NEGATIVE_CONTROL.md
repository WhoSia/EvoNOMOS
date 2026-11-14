# P44-F33 R3 — Structural Design-Reversal Pilot with a Post-Hoc Strong Rival

**2026-11-09 · CONTROLLED GENERATED GO SOURCE / LOCAL NATIVE TESTS / NO LAW-R2 PROMOTION**

## Why this experiment was done
The founding object of EvoNOMOS is a conditional structural-design law, not progressively more elaborate certificates. An initial DIRECT-versus-PORT comparison seemed to suggest that interface-based design is cheaper for provider replacement but more expensive for interface-contract extension. A third **direct_refactored** architecture was then deliberately introduced *after seeing the first eight results* to test whether this was merely the effect of duplicated provider strings.

## Experimental construction and honesty
- Go 1.23.2 linux/amd64, 3 architectures × provider swap yes/no × backend-derived `Mode()` extension yes/no = **12 independent compilable module snapshots**.
- `direct`: three service methods each duplicate a provider-version literal.
- `port`: service delegates through `Backend` interface, with contract and concrete backend in separate source files.
- `direct_refactored`: same service methods delegate to one private local helper but **no interface**.
- All snapshots require `Legacy() == "old"` plus case-specific `Lookup/Label/Describe` checks and `Mode()` when requested. Old-client testing is narrow and deliberately not equivalent to all-client contextual safety.
- Each snapshot independently passed `go test -count=1 ./...`, `go vet ./...`, `go test -race -count=1 ./...` = **36 successful local commands**. No GitHub-hosted run is claimed.
- Source edit metric: GNU-style line insertions plus deletions relative to that architecture's baseline, excluding generated tests. Files touched and baseline source LOC are separately counted. These are **not measured developer effort**.

| Outcome | DIRECT duplicated | PORT interface | DIRECT refactored |
|---|---:|---:|---:|
| Baseline source lines | 5 | 13 | 6 |
| Provider replacement changed source lines (added+deleted) | 6 | 2 | 2 |
| Adding Mode changed source lines | 1 | 3 | 1 |
| Adding Mode touched source files | 1 | 3 | 1 |

The strong rival **eliminates the supposed PORT replacement advantage** while retaining its lower contract-change footprint and simpler baseline. Therefore, apparent DIP-specific improvement in the initial DIRECT-vs-PORT pair is **confounded by duplicate literals**. The strong rival was POST-HOC, so this is a negative diagnostic, not a confirmatory outcome.

## Scientific interpretation
This synthetic study distinguishes superficial architecture rankings from a minimum-information rival. It does NOT identify a general source-level law; it is the same known issue emphasized by the Baldwin–Clark/Sullivan real-options and Parnas modularization lineage: comparisons require appropriate design alternatives and declared change environments. Within our narrow source grammar, a helper can match a port on provider-change cost without carrying an interface-extension cost.

No genuine independent upstream source, editor authorization, independent future demand, randomly assigned developer, timed human effort, realistic jointly protected contracts, full static-analysis baseline, or source-extracted graph is established. There is no C5 prospective prediction.

## Source custody
A self-contained source/testing ZIP was generated locally at `/mnt/data/EvoNOMOS_Structural_Reversal_Strong_Rival_Pilot_v0.1.zip`, **19,303 bytes, local SHA-256 `561979a701d7e1fa2f4c7474e0d01bccb0c5b344c17913cc6e75eb7a9e66a81b`**. Contains generator `generate.py`, independent checker `evaluate.py`, all 12 Go source snapshots, exact `preseal_initial_8.json`, checks and README. The initial preseal was retained and the rival identified as post-hoc. This report does NOT claim that ZIP was uploaded to Drive or committed to GitHub, nor that a GitHub workflow ran. Local sandbox custody is temporary and not a substitute for durable byte custody.

## Next scientifically worthwhile test
(1) Eliminate duplicate-code confounding and compare genuinely distinct *capabilities*, e.g. independent runtime provider injection, concurrent edits, cross-module trust/rights, and stable-vs-unstable contract changes. (2) Repeat in original independently pinned Go repos, not researcher-generated toy programs, with a frozen independent demand selector and matched conventional source-aware baselines. (3) Estimate context-conditional sign reversals with multi-objective Pareto judgments, not one metric or synthetic line counts.

**No new theorem, no predictive advantage, no LAW-R2. G1–G7 OPEN / PR #13 DRAFT.**
