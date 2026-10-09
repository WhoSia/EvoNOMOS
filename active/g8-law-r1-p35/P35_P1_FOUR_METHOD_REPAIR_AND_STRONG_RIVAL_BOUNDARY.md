# P35-P1 — Four-Method Composed Repair and Strong-Rival Boundary

**2026-10-09. Updated scientific status:** `LOCAL_SOURCE_REPAIR_FAMILY_EXPANDED__PINNED_RESTIC_PACKAGE_PASS__ARCHITECTURE_ADMISSIBILITY_BOUNDARY_OPEN__LAW_R2_NOT_AUTHORIZED`. Local DNS was superseded by [hosted original Restic #37895607800](https://github.com/WhoSia/EvoNOMOS/actions/runs/37895607800). This is a same-stage extension, **not** P36, LAW-R2 or a new Lab.

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

The four-method candidate modifies `newPayloadStore`, `payloadStore.put`, `payloadStore.get`, `payloadStore.clear`; `readEngine.decode`, `composed.Save`, `composed.Load`, `Stat` and `List` remain byte-identical to P0. **Critical architectural correction:** `readEngine.decode` is only a forwarded call while the payload store performs the version interpretation, violating P35's frozen *independent read-decoder* responsibility. Its behavior PASS is not admissible as a fixed-architecture C repair. The lowest observed C repair that preserves independent decode is **five modified methods (tagged variant)**, not four. The difference is a test of the architectural repair grammar, not proof of a global minimum. Typed payload state and codec helpers add costs even in the four-method arm.

**Verification:** Go 1.23.2 shim `go vet` PASS; `go test -race -count=10` PASS for the selected tests; P34 public behavior replay `18/18`; expected unedited new-demand baseline FAIL. Does **not** imply Restic full upstream conformance or developer time.

## Set-valued repair observation, not abstract-law victory

For architecture A and requirement d, `R_A(d; T,G)` denotes the admissible repair candidates under frozen test oracle T and patch grammar G, while `S_A(r)` is a particular source-edit support. Observing U=2 and C=6 initially **does not** establish `min_{r∈R_U}|S_U(r)| < min_{r∈R_C}|S_C(r)|`. After alternative C repairs, the observed method count falls to 4. The C four-method support is contained in several larger observed C supports under the chosen grammar, but no exhaustive grammar proof or cross-architecture minimum exists.

The information-cut constraint for overlapping old/new byte encodings is classical deterministic factorization, not a new mathematical theorem. The implementation has to preserve a trusted distinguishing context. The location of that context can affect code edit propagation, but is not prescribed by SOLID alone.

## Source-aware strong rivals

Existing syntactic B0+ reachability seeds include `unified.Save/Load/Stat/List/Remove/Delete` (six candidate methods) and twelve source-neighborhood C candidates. The candidates contain every observed modified method in U2 and C4; U: 2/6 precision and 1.0 recall, C4: 4/12 precision and 1.0 recall. A stricter, whole-program, context-sensitive CSDG is **not** implemented here; B1 genuine source history and B2 Parnas/DRSpaces/CSDG/repair-synthesis baselines remain scientifically undefeated. This evidence supports a bounded **repair-choice dependence**, not a new predictor.

## Authentic upstream attempt / reproducibility

The earlier read-only *local* original-source attempt exited 40 during GitHub DNS resolution. Subsequently, [read-only GitHub Actions #37895607800](https://github.com/WhoSia/EvoNOMOS/actions/runs/37895607800) checked out the pinned **actual Restic** commit, compiled, vetted and race-tested all eight Go source worlds, replayed the P34 18-step history in each, and demonstrated both untouched-baseline expected failures. The source and runner are now [human-authored browser-readable files](../../tools/p35-p1/worlds/baseline/backend.go); artifact 11599942843 SHA256 `49d38c9c60a7415c9b9395cb7c52db5e33cdf25e55297de6888d5f52fa89f85b`. No full upstream Restic suite or strong-rival win is claimed.

**Next legitimate action:** architecture-admissible repair family comparison under matched information and source-aware B0+/B1/B2; separate a test-passing decoder relocation from a genuinely fixed COMPOSED read contract. Maintain persistence in seeking better independent worlds without indefinitely retesting the same null contrast.

Authorship: GitHub commit author and committer must be authenticated `WhoSia`; Actions must remain read-only. No bot-authored repository history.
