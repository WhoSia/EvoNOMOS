# P35-P1 — Four-Method Composed Repair and Strong-Rival Boundary

**2026-10-09. Scientific status:** `LOCAL_SOURCE_REPAIR_FAMILY_EXPANDED__UPSTREAM_DNS_BLOCK__LAW_R2_NOT_AUTHORIZED`. This is a same-stage extension, **not** P36, LAW-R2 or a new Lab.

## Experimental contact

The pinned real upstream Restic interface is [`restic.Backend` at `495982232cf1af184eac0a97871ef8161e8708ee`](https://github.com/restic/restic/blob/495982232cf1af184eac0a97871ef8161e8708ee/internal/restic/backend.go). The actual local test source uses an explicitly synthetic API-compatible `internal/restic` shim, so **no upstream module build success is claimed**.

The P35 source family retains two distinct mechanisms:
- UNIFIED: one authoritative map whose record owns payload and logical length.
- COMPOSED: payload store + independent metadata index and removal coordinator; read engine delegates through the payload store under consistency lock.

Two requirements: (d_L) KeyFile-only Save limit at 8 bytes with prior contents intact; (d_E) reversible versioned payload storage preserving arbitrary legacy raw bytes, partial loads, Stat/List logical sizes and the P34 18-event public behavior.

## Realized source repair costs

All values are `Go AST diff against exactly the same unedited P35-P0`, counting *changed pre-existing methods*. New codec helpers are listed separately and equivalent across encoded worlds.

| World | Changed pre-existing Go methods | Go source line addition/deletion | Verdict |
| --- | ---: | ---: | --- |
| U local rule | 1 | +3/−0 | Local demand PASS |
| C local rule | 1 | +3/−0 | Local demand PASS |
| U encoded | 2 | +30/−1 | Local demand PASS |
| C encoded, separate map | 6 | +55/−10 | Local demand PASS |
| C encoded, decoder in payload store but separate map | 5 | +50/−8 | Local demand PASS |
| C encoded, tagged payload decoded in read engine | 5 | +55/−9 | Local demand PASS |
| **C encoded, tagged payload decoded in payload store** | **4** | **+50/−7** | **Local demand PASS** |

The four-method candidate modifies `newPayloadStore`, `payloadStore.put`, `payloadStore.get`, `payloadStore.clear`; `readEngine.decode`, `composed.Save`, `composed.Load`, `Stat` and `List` remain byte-identical to P0 in that candidate. This is **not** a zero-cost implementation: typed payload representation and codec helpers are additional structural obligations.

**Verification:** Go 1.23.2 shim `go vet` PASS; `go test -race -count=10` PASS for the selected tests; P34 public behavior replay `18/18`; expected unedited new-demand baseline FAIL. Does **not** imply Restic full upstream conformance or developer time.

## Set-valued repair observation, not abstract-law victory

For architecture A and requirement d, `R_A(d; T,G)` denotes the admissible repair candidates under frozen test oracle T and patch grammar G, while `S_A(r)` is a particular source-edit support. Observing U=2 and C=6 initially **does not** establish `min_{r∈R_U}|S_U(r)| < min_{r∈R_C}|S_C(r)|`. After alternative C repairs, the observed method count falls to 4. The C four-method support is contained in several larger observed C supports under the chosen grammar, but no exhaustive grammar proof or cross-architecture minimum exists.

The information-cut constraint for overlapping old/new byte encodings is classical deterministic factorization, not a new mathematical theorem. The implementation has to preserve a trusted distinguishing context. The location of that context can affect code edit propagation, but is not prescribed by SOLID alone.

## Source-aware strong rivals

Existing syntactic B0+ reachability seeds include `unified.Save/Load/Stat/List/Remove/Delete` (six candidate methods) and twelve source-neighborhood C candidates. The candidates contain every observed modified method in U2 and C4; U: 2/6 precision and 1.0 recall, C4: 4/12 precision and 1.0 recall. A stricter, whole-program, context-sensitive CSDG is **not** implemented here; B1 genuine source history and B2 Parnas/DRSpaces/CSDG/repair-synthesis baselines remain scientifically undefeated. This evidence supports a bounded **repair-choice dependence**, not a new predictor.

## Authentic upstream attempt / reproducibility

A read-only original-source validation driver has been written and syntax-checked and tries to clone the *real* Restic pinned repository in a temporary directory, run `go vet`, `go test -race` on all source worlds and baseline-negative controls. The attempted local run returned **exit 40** before checkout: `fatal: unable to access ... Could not resolve host: github.com`. No original upstream build took place. The script is provided in the local P35-P1 evidence bundle to be executed on a host with network.

**Next legitimate action:** original Restic compile and 18-step tests, then source-aware rival baseline under matched input. If no structural discrimination survives, close P35 with its actual bounded outcome instead of inventing novel names for established theories.

Authorship: GitHub commit author and committer must be authenticated `WhoSia`; Actions must remain read-only. No bot-authored repository history.
