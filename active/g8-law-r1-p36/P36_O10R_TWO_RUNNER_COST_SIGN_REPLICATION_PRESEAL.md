# P36-O10R — Post-Observed Independent Runner Challenge for a Small Same-Contract Cost-Sign Reversal

**2026-10-10 KST · FOLLOW-UP PRE-REPLICATION SEAL, AFTER O10 FIRST RUN.** First-run raw numbers were already observed from native original Go [#37970800075](https://github.com/WhoSia/EvoNOMOS/actions/runs/37970800075); this study is NOT blind with respect to the sign hypotheses, but native replication environments and their data have not yet been observed.

## Exact original programs and frozen tests

Use the already committed, bit-identical source [Chi](../../tools/p36-o10/arms/chi/p36_o10_selectable.go) and [Gorilla](../../tools/p36-o10/arms/mux/p36_o10_selectable.go), exact pins Chi `67be7d9cafdaeb4e04e887ff78d09e030ee43b00` and Gorilla `b4617d0b9670ad14039b2739167fd35a60f557c5`. Use the already frozen identical Q21 tests; **do not change treatments, test or benchmark source**. The exact same **restricted** two-pattern scope, HTTP response label and immutable Handler contract applies.

Initial O10 run #37970800075: one EPYC 7763 Runner, `GOMAXPROCS=1`, two blocks CHI→MUX and MUX→CHI, 5 bench repetitions/block. For Q21 specificity PS overlap, Chi 1122 vs Gorilla 1346.5 ns/op (Chi faster 16.7%). For specificity PS single generic-only match, Chi 1646 vs Gorilla 1603.5 ns/op (Gorilla faster 2.6%, **small and possibly environmentally unstable**). For chronology PS overlap, Chi 1541.5 vs Gorilla 1558.5 (~1%, essentially tied). For specificity build, Chi 1623.5 vs Gorilla 16726.5 (~10x but source-policy implementation dependent). All Q21 and original Go full/race/vet native PASS.

## Prospective independent-replication plan and criteria

Use **two fresh GitHub Actions VMs**, one each assigned initial library order CHI_FIRST or GORILLA_FIRST. Within each runner, repeat two blocks reversing order: CHI→GORILLA and GORILLA→CHI, so source comparison is paired within physical runner. Same Go setup and pinned packages, with the exact same source/test hash; native `go vet`, `go test -race ./...`, `go test ./...`, `go test -run '^TestP36O10' .` must pass before timing.

`GOMAXPROCS=1 go test -run '^$' -bench '^BenchmarkP36O10' -count=6 -benchtime=150ms -benchmem -cpu=1 .` per original library per block. Baseline first run measured 10 repeats per source/variant; replication gives **12 within-run samples per source/variant per runner**. Save all 4 block logs per runner, CPU model, Go version, source SHA, artifacts. No post hoc filtering of slower/less convenient samples. Descriptive medians per runner and block, not a p-value with independent observations (Go benchmark repeats and shared host are not fully independent). Exact normalizers include httptest recorder allocations; not pure router dispatch.

**Target signs to challenge** (post-first-run, fixed here before replica run):
- `S_overlap`: Chi< Gorilla on Q21 specificity PS overlapping request, reasonably separated baseline;
- `S_single`: Gorilla< Chi on Q21 specificity PS generic-only request, weak baseline; count as **not robust** if either replica has opposite sign or broad overlap, even if grand median favors Gorilla.
- `S_build`: Chi< Gorilla on these specific project-authored adapter constructors, not universal upstream source build efficiency.
- `S_chronology_PS_overlap`: near tie; **do not claim** robust rank from a 1% baseline.

All variants already satisfy the **same Q21** client semantics by native original Go oracle. If a replica differs, preserve discrepancy as valuable negative evidence. No runtime sign itself defeats standard route-matching/Go allocation classical theory. `DIP49_NEW_LAW_PAIR_HOLD` continues.

**Pre-replication status:** `Q21_ORIGINAL_NATIVE_PASS__ONE_RUNNER_CONDITIONAL_MEDIANS_OBSERVED__TWO_NEW_INDEPENDENT_RUNNER_COST_SIGNS_UNTESTED`.
