# P36 — O2/O3 Native Source Closure, Structural Order Counterexample and MATH-4 Continuation

**2026-10-10 KST · P36 OPEN / P35 CLOSED.** This is a source-backed update of *verified* experiments and a labeled *pre-result* O4 hypothesis. No LAW-R2 authority.

## 1. O2 — Gorilla original independent-source semantics and time/allocations

[Original independent upstream Gorilla native Go/race/vet #37958339620](https://github.com/WhoSia/EvoNOMOS/actions/runs/37958339620): final **SUCCESS**, two jobs EAGER and LAZY; upstream `gorilla/mux@b4617d0b9670ad14039b2739167fd35a60f557c5`. Artifacts downloaded and inspected:
- EAGER id `11632646402`, ZIP SHA256 `4818fca629f36b27c9c8713d72cb0316017255d5c972965482e6c1f329caa006`;
- LAZY id `11631472349`, SHA256 `6d6c9ec24387e2e2d250607600eb2d3fda065e02af1a887464e3a3a145d5578f`.
All common post-baseline 16U+16R behavioral contract tests including source registration priority, fallback and finite race PASS. This is an *independently evolved software package*, but both EAGER/LAZY publication strategies were project-added; do not call them independent naturally occurring implementations.

[Same-runner original Gorilla audit #37959460386](https://github.com/WhoSia/EvoNOMOS/actions/runs/37959460386): **SUCCESS** for reversed benchmark ordering, five repeats each, raw logs archived:
- EAGER→LAZY job artifact id `11632696540`, ZIP SHA256 `483626198377bdc571c169f114c71b34700bc05eadd15258cb51d6d4a6de848f`. Runner EPYC 9V45. Burst median ns/op EAGER **215501**, LAZY **79308**. Alternating EAGER **220930**, LAZY **242888**.
- LAZY→EAGER job artifact id `11632726359`, ZIP SHA256 `19585604bcfab4764a572ed48d6a31bea29239f34d46885e107a331d58bd5175`. Runner EPYC 7763. Burst EAGER **380193**, LAZY **129513**. Alternating EAGER **377731**, LAZY **375193**. CPU and treatment order changed between the two jobs; **do not attribute interleaved sign difference solely to either factor**, and the latter gap is tiny with overlapping raw repeats.

Gorilla burst allocations per workload op EAGER ~518194 B/4449 allocs, LAZY ~144120 B/714 allocs, difference ~374074 B. Alternating both ~517936 B/4433 allocs, as both publish 16 times. Original Chi isolated-benchmark burst EAGER ~160014 vs LAZY ~107962 B (difference ~52052 B); **different underlying router rebuilding mechanisms** produce radically different conditional allocation magnitudes under the *same abstract 16U/16R and snapshot publication counts*. Per-package source-specific cost remains a strong classical rival. The initial Chi-local EAGER-wins-alternating sign does NOT robustly transport as an environment-independent inequality, even though it appeared in one paired Gorilla runner. `H_unconditional_sign_transport` **unsupported**, and universal semantics-only implication is analytically refuted by standard cost countermodels. No new law identified.

## 2. O3 — authentic future-option divergence under two currently matched Chi source repairs

[Native original Chi #37961233537](https://github.com/WhoSia/EvoNOMOS/actions/runs/37961233537) final **SUCCESS**, two jobs. Both original v5.1.0 `go vet ./middleware`, `go test -race ./middleware`, full original Go, frozen D14 and old O6 pass, with future D15 separately tested:
- `RETAIN`: artifact id `11632012939`, ZIP SHA256 `dc98cc87b213a9df430f27a822d3586d857076e54db321e27eede728650b8db5`. Original source SHA256 `5979f53437008c490b78d2b664b2f47d9ca94fba`. D15 `alpha` and `beta` both PASS restoring the original closure and priority.
- `ERASE`: artifact id `11633012192`, ZIP SHA256 `1a41241693801e4dad2dbfde03101e6a8ae814fef6029b655b5a8364849d6caa`. Original source SHA256 `05316703f30a9d595112801aa2b9c62669164d89`. Frozen future D15 fails twice with declared `P36_O3_D15_RESTORE_EXPECTED_NEGATIVE_OR_BUG` because no original closure is retained; treated as **expected scientific negative** and not masked by workflow failure.
- The exact previous D14 source valid repair set is `Γ_obs={RETAIN,ERASE}`, so `May(Surv_0(D15))` true and `Must(Surv_0(D15))` false **only relative to Γ_obs**, not across all legal source edits.

[O3 classical erasure Lean checker #37961481644](https://github.com/WhoSia/EvoNOMOS/actions/runs/37961481644) final **SUCCESS** with `leanprover/lean-action@v1` build and independent `leanchecker=true`. Source theorem: if two histories become literally identical *permitted states* but require different restore answers, no state-only deterministic restore function solves both. This is a classical non-injectivity result; no source-level Go pointer-state equality theorem implied. Repo source explicitly separates permission-limited state equality from full physical state.

## 3. New prospective O4 — retained values, failed RELATIONAL position identity (not merely erased data)

The existing O3 RETAIN [source](../../tools/p36-o3/arms/chi/retain/p35_epoch_router.go) stores original closure and **dynamic index-at-deletion**. With A,B,C same-key priority, first two disables remove A then B, and both save index 0 after earlier indices collapse. A FIFO restoration by saved positions inserts A at 0 then B at 0, so future D16 expects A but B shadows it. A new future D16 challenge was **presealed before O4 treatment code**:
- [D16 independent preseal](P36_O4_D16_STABLE_REGISTRATION_IDENTITY_PRESEAL.md), commit `87e9693`.
- [D16 future test](../../tools/p36-o4/tests/chi/p36_o4_d16_future_test.go), commit `83ca4aa`, tests two consecutive disables, FIFO restores, later Register interleaving, old prefix revisions, and one more disable.
- [new STABLE_ORDER original Chi source treatment](../../tools/p36-o4/arms/chi/stable-order/p35_epoch_router.go), commit `daba1b0`: immutable unique per-registration ordinal across `Register`, `RegisterAny`, `RegisterDefault`; removes and restores routes in sorted ordinal order while retaining middleware closures. **NO OLD D14/D15/trace oracles altered.**
- [original Go two-arm native CI #37964693435](https://github.com/WhoSia/EvoNOMOS/actions/runs/37964693435), last observed **IN_PROGRESS**, matrix old POS_INDEX (expected negative D16) versus STABLE_ORDER (expected positive), both need full Go, vet, race and frozen old D14/D15. D16 verdict is **not yet confirmed** in this phase.

**Scientific novelty limit:** the mechanism is a concrete real-source vulnerability of unstable deletion-time coordinates, and is explained by classical stable identity / order-maintenance and relational provenance. Original closures **were retained** in both O3 RETAIN and new STABLE_ORDER; the failure hypothesis is not loss of middleware value, but source representation and restoration algorithm not respecting an order invariant across successive changes. There is not a new universal design law from this single route scenario.

## 4. Mathematical backbone (MATH-4)

[Mathematical program](P36_MATH_4_MAINTENANCE_CONTEXTUAL_EQUIVALENCE_AND_FORGETFUL_SIMULATION.md) distinguishes:
- equivalence of current runtime output `~_d`;
- equivalence of legal future source-repair possibility sets `≈_{Γ,E}`;
- comparable conditional lifecycle cost `≍_{Γ,E,c}`.

`~_d` need not entail either stronger relation. A **classical forgetful simulation** demands `π∘δ_R=δ_E∘π` and `O_R=O_E∘π`, from which trace preservation follows by induction; it cannot be assumed from finite current tests. Lean source [P36Math4.lean](../../tools/p36-math4/lean/P36Math4.lean), [CI #37964349042](https://github.com/WhoSia/EvoNOMOS/actions/runs/37964349042) was still RUNNING at this phase. Knowledge-rich architectures can simulate erasure **only when Γ permits the requisite forgetting transition and resource constraints allow it**. A future-demand inversion engineered by adding 'you must have erased in the past' retroactively is an invalid test.

P36 next scientifically strong test should compare two real source representations with the *same retained information* but differing repair topology, under fresh order-sensitive demands, and test a preregistered strong classical rival with genuinely different predictions rather than measuring arbitrary Go test pass counts. O4 moves in this direction but the stable-ID explanation remains classical.

**Court:** `GORILLA_ORIGINAL_GO_SUCCESS__GORILLA_PAIRED_SUCCESS__O3_NATIVE_GO_MAY_NOTMUST_BOUNDED_SUCCESS__O3_LEAN_CLASSICAL_SUCCESS__O4_D16_SOURCE_TEST_PENDING__MATH4_LEAN_PENDING__DIP49_LAW_PAIR_HOLD__LAW_R2_NOT_AUTHORIZED`.
