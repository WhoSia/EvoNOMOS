# P36-O2 — Independent Gorilla Mux Transport of Chi EAGER/LAZY Demand-Sequence Preferences

**2026-10-10 KST, prospective PRE-SOURCE seal.** P36 sole active version; P35 CLOSED; LAW-R2 NOT_AUTHORIZED. This research reuses original Chi P35-O6 SUCCESS [native run #37951885323](https://github.com/WhoSia/EvoNOMOS/actions/runs/37951885323), but original Chi's post-baseline cost experiment [#37954396262](https://github.com/WhoSia/EvoNOMOS/actions/runs/37954396262) remains unverified as of this seal. The Chi local cost signs are exploratory prior, NOT native-hosted transport evidence. Gorilla independent source v1.8.1 `b4617d0b9670ad14039b2739167fd35a60f557c5` is a **separately evolved real repository**, not a second fork of Chi; all Gorilla source additions and tests must compile in its pinned original module.

## Same authorized semantic intersection, different source structures

Gorilla original `NewRouter()`, `(*Router).NewRoute().Headers`, `(*Router).NotFoundHandler`, and `ServeHTTP` form the actual source-backed substrate. Publish immutable routers by constructing fresh `*Router` from the synchronized route-registration list. The project-owned wrapper exports the same research API shape as Chi `NewP35EpochRouter(next)`, `Register(header,match,wrap)`, `RegisterAny(header,matches,wrap)`, `RegisterDefault(wrap)`, `ServeHTTP`, `Stats`, with one logical update per public registration. The shared cross-repository contract is **only** single-header exact-name lower-case token matching on `X-P35-Epoch`, first-registered duplicate priority, default fallback, and completed registration visibility. No claim of equal regex/wildcard behavior across Chi and Gorilla, nor equal source line count, CPU instruction count, method behavior outside this intersection, or comprehensive concurrent linearizability. API mapping is pre-outcome and fixed; direct external router writes forbidden.

Both additions independently sync `Register` and snapshot selection through `mu`, and do not hold lock inside user-provided middleware. Each request sees all updates completed before its snapshot selection critical section. EAGER publishes on every registration; LAZY publishes only at first request after one or more unseen updates. The initial registry is 32 routes, and 16 subsequent updates plus 16 requests yield an exact prospective *mechanism* signature:

| Frozen trace | EAGER extra publishes | LAZY extra publishes |
| --- | ---: | ---: |
| `U^16 R^16` | 16 | 1 |
| `(UR)^16` | 16 | 16 |

The two original module native Go packages require original full Go `go test -count=1 ./...`, race `go test -race -count=1 ./...`, vet `go vet ./...`; frozen route fidelity, duplicate first precedence, default, concurrent-completed visibility, and 16/16 trace counts. Host artifact provides source SHAs and raw benchmark repetitions on exact frozen host in each arm. Both arms use identical pinned Gorilla module and identical frozen tests.

## Prospective strong classical opposition (do not weaken after outcomes)

**H-transport-sign (overstrong falsifiable candidate):** carrying the Chi *local*, baseline-excluded preferred arm across repositories is justified by shared 16U/16R order and semantics alone: under `U^16R^16` LAZY is faster than EAGER, under `(UR)^16` EAGER is faster than LAZY. This has a real predicted sign pair, but was derived after observing Chi locally. It is a **fresh out-of-repository prediction**, not a blind discovery or general law.

**B-source-aware classical caching/architecture prior:** both exact rebuild-count predictions transfer, but the **sign of measured time differences is not entailed** by correct trace semantics. Compiling Gorilla routes vs Chi registries, matcher evaluation, allocations, internal representations and load conditions change the size-specific `b_i`, `m_i`, `h_j` and residual; a priori an architecture may win both, split or tie. The classical rival therefore allows **all sign outcomes**, not a sharp counter-forecast. B cannot be "defeated" by a match with H; it does provide a complete existing conceptual explanation of any discovered mechanism. A Gorilla sign contrary to H falsifies the overstrong cross-repo sign-transport claim but does not discover a new structural law.

**DIP-49/50 qualification:** match intervention prefixes and projected common routing decisions; do not pretend conditional source-specific runtime ranks satisfy a common hardware/implementation-invariant query, and never infer a new law from source-specific benchmark magnitude. If original Gorilla matching differs on the frozen common contract, treat `REALIZATION_HOLD` and repair the *implementation* without changing the acceptance test or rewriting history. Do not replace an unfavorable sign with chosen post-hoc workloads. A new beyond-classical pair remains **HOLD**; this deliberately adversarial O2 tests a tempting but unsupported transfer shortcut.

## Gates

- Frozen acceptance source must precede arm implementation commits.
- Full original upstream test + race + vet before declaring native correctness.
- Benchmark repeated raw numbers, no forced PASS condition on benchmark *sign* or skipped outliers, no unsupported cross-VM causal comparison. Prefer interleaved paired within-run arm repeats / independent GitHub runners if feasible.
- Source-author human `WhoSia`, CI read-only.
- Strong repair-option law candidate beyond classical needs separately frozen semantic repair grammar `Gamma` and non-overlapping `sigma_q(H)` vs `sigma_q(B)`; O2 alone not enough.

**At preseal:** `P36_O2_FROZEN_NOT_EXECUTED__DIP49_IDENTIFICATION_HOLD__LAW_R2_NOT_AUTHORIZED`.
