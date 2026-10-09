# P36-O3 — Post-Treatment Local Smoke and the Unverified Original-Source Court

**2026-10-10 KST.** This is AFTER both original Chi D14 source treatments were committed, not part of the original [pre-source seal](P36_O3_D14_D15_REPAIR_OPTION_SURVIVAL_PRESEAL.md). P36 sole active stage.

## Actual original-source source files and chronology

Human WhoSia commits:
- [pre-source D14+D15 research seal](P36_O3_D14_D15_REPAIR_OPTION_SURVIVAL_PRESEAL.md) `2e257ec`;
- [frozen D14 Go acceptance](../../tools/p36-o3/tests/chi/p36_o3_d14_test.go) `74406e9` and independently frozen [future D15 test](../../tools/p36-o3/tests/chi/p36_o3_d15_future_test.go) `f0c164c`;
- [RETAIN original Chi source addition](../../tools/p36-o3/arms/chi/retain/p35_epoch_router.go) `f5e247c` and [ERASE source addition](../../tools/p36-o3/arms/chi/erase/p35_epoch_router.go) `cb17602`;
- [read-only native original Chi full/race/vet and future negative court](https://github.com/WhoSia/EvoNOMOS/actions/runs/37961233537) `81224ec`; last readback **QUEUED**.

After those commits, a separate local **method-level approximation** of the original Chi HeaderRouter API and same D14 retained-versus-erased route manipulation was built in a local Go test project. It is not checked-out immutable `go-chi/chi` source and is not a replacement for the hosted native run. Executed:
- RETAIN `go test -race -count=1 -run TestD14 ./...`: **PASS**; `TestD15`: **PASS**.
- ERASE `go test -race -count=1 -run TestD14 ./...`: **PASS**; `TestD15`: **EXPECTED NEGATIVE** with "no restore".

The first local reproduction script contained **its own text-template replacement ordering error**, causing *local source-generation build failures* for both arms; correcting the local text substitution (without any edits to GitHub original-source treatments or frozen acceptance tests) gave the results above. This was a harness mishap, not evidence that the real GitHub source compiled or failed. Original Go CI remains authoritative. Avoid disguising local replicas as native original code.

## Quantifier and semantic cautions

The considered finite grammar `Γ_obs` has exactly **two constructed candidate repairs**. Even if both pass D14 and one fails D15, this proves `May` and not-`Must` of **zero-edit future survival only in Γ_obs**, not across arbitrary Go repairs. D15 has two independent closure-tag worlds `alpha` and `beta`, and fixed duplicate priority; it cannot identify arbitrary HTTP routing semantics or all future changes.

The analytic Lean lemma in [P36O3Survival.lean](../../tools/p36-o3/lean/P36O3Survival.lean) assumes literally equal erased snapshots and unequal required answers. Distinct Go closure allocations and HTTP handler pointers can remain unequal as raw runtime objects even if their permitted routing behavior is indistinguishable. To apply the lemma to actual code, specify a **restricted observation/reconstruction interface** and show erasure under *that interface*, not pointer identity. The preliminary code plausibly discards the target closure via authorized registry fields, but finite native tests do not prove an unrestricted Go impossibility theorem.

The entire theoretical mechanism has classic explanations in information loss, nondeterministic repair/refinement and test-suite underspecification (Qi et al., ISSTA 2015; Smith et al., FSE 2015). **NO NOVEL LAW**.

**Verdict:** `P36_O3_LOCAL_METHOD_SMOKE_PASS__SOURCE_CI_PENDING__LEAN_KERNEL_PENDING__MAY_NOT_MUST_IS_RELATIVE_TO_GAMMA_OBS__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.
