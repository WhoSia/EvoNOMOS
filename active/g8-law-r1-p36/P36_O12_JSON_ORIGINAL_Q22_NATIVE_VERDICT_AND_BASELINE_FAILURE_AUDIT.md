# P36-O12 — Genuine Independent Non-Router JSON Source, Same Q22: Native Verdict and Baseline-Failure Isolation

**2026-10-10 KST · POST-NATIVE Q22 READBACK · P36 OPEN / P37 NAME PROPOSED ONLY / DIP49 IDENTIFICATION HOLD / LAW-R2 NOT_AUTHORIZED**

## Frozen originals and experiment chronology

- Independently evolved original `tidwall/gjson@690362d6edf4bcbde1e9f54d552d3814f1cd5bcb`: `Result`, `Raw`, `ForEach`; [exact original source](https://github.com/tidwall/gjson/blob/690362d6edf4bcbde1e9f54d552d3814f1cd5bcb/gjson.go).
- Independently evolved original `buger/jsonparser@36a686d11807c62cd5a30d41b294d66969ea25d8`: raw byte `ObjectEach` and `ValueType`; [exact original source](https://github.com/buger/jsonparser/blob/36a686d11807c62cd5a30d41b294d66969ea25d8/parser.go).
- [Q22 prospective seal](P36_O12_INDEPENDENT_JSON_PROVENANCE_Q22_PRESEAL.md), commit `244442a4`; then **two identical** [source tests](../../tools/p36-o12/tests/) committed `fdb2ffb9` and `6f31e06f`, then [research authored opt-in source extensions](../../tools/p36-o12/arms/) committed `7db0ad6d` and `11bf1795`. No original upstream code file was edited.
- Both implementations under fixed Q22 select `first` or `last` duplicate `meta.id` numeric JSON member and return **original numeric spelling**, not a normalized floating-point representation. No claim duplicate-object-key selection is mandated by JSON standard. Invalid policy, type mismatch, empty input, no matching member, source immutability, concurrency separately tested.

## Initial native workflow failures were NOT Q22 results

The first [original CI #37973487549](https://github.com/WhoSia/EvoNOMOS/actions/runs/37973487549) FAILED on pre-existing `buger/jsonparser` **Go vet** warnings in upstream `parser.go:2023:2` unreachable code and `bytes_unsafe_test.go:29:35` unsafe reflect.StringHeader use. An initial workflow-only script amendment `4a6abbf` mistakenly expanded replacement `$'` in a JS string expression, corrupting YAML and producing a separate no-jobs failure [#37973851920](https://github.com/WhoSia/EvoNOMOS/actions/runs/37973851920). This script was fixed without modifying Q22. Next [#37973952915](https://github.com/WhoSia/EvoNOMOS/actions/runs/37973952915) found original package full tests' **two existing** `TestOracleSetPr286Regression` subcases failing due top-level out-of-bounds/far array `Set` and later `Get` mismatch. The scientific method requires proving these existed before the research addon, not erasing them.

The final workflow explicitly captured the **BEFORE-addon original upstream vet and full test logs**, then compared WITH-addon original full/vet logs and separately ran qualified other tests/race. Both JSONParser pre- and post-addon full test logs show the same two PR286 failing subcases and both pre/post full vet logs the same two warnings. Other qualified upstream tests and full race excluding *that exact historical test* PASS. The upstream issues are **NOT fixed** and are not Q22 negative observations. Never claim unqualified `go vet ./...` or `go test ./...` PASS for pinned jsonparser.

## Final original CI and immutable ZIP receipt

[Native original packages read-only Go and same-runner benchmark #37974374859](https://github.com/WhoSia/EvoNOMOS/actions/runs/37974374859) completed **SUCCESS**. Artifact `p36-o12-independent-original-json-q22-source`, ID **11638590284**, ZIP SHA256 **`9de45316db2eda6d1db8076fa74208a9dd70f8f2528028f2e0fcb1a29ab7d0b1`**, 35 raw audit/log/bench records, verified by direct ZIP inspection.

- `tidwall/gjson`: unqualified old/full original Go tests, race and vet PASS; independent Q22 all **13 specified cases** plus concurrent read-only test PASS.
- `buger/jsonparser`: original full Go & vet **qualified** with exactly the two upstream findings each captured pre/post; full other Go tests and qualified race PASS; the **identical Q22 13 cases and concurrent read-only test PASS**, no new Q22 failing case. Historical upstream original PR286 failure persists, classified separately.
- Both pinned modules ran Go `1.23.12 linux/amd64` on same Intel Xeon Platinum 8573C host; each source run in two counterbalanced library-order blocks, `GOMAXPROCS=1`, 5 Go benchmark repetitions per block = **10 measurements per query variant/source**. Caller JSON document built **outside** timed loop. Request to method returns original lexeme; allocations include wrapper's policy evaluation but not caller doc construction.

**SHA256 immutable exact Q22 source/test:**
- gjson addon `67b4c4e9758c749d5f10f84a0ba9f870a105491738e3ca70d783f997e9a79e21`; test `29b38b4ff8e8b12c51a892f7d466ff9f716bc2216a6f0e2505c47a9e095862b2`.
- jsonparser addon `b8ce93b28d16b684442a938fbba4add5640a3d5b9f0755020c2d96041f586630`; test `843aa159692d151c92a2602567a00251b8f3f948dd4dcbd80976ced7d5206ff2`.

## Same Q22 fixed-workload original Go measurements

All rows are **the same declared Q22** and positive original source code tests. `padding064` adds 64 irrelevant scalar fields to object `meta`; `front/back` is where the unique matching key appears relative to padding. `first/last` coincide for the unique key in benchmarking, but distinct duplicate cases were tested in native functional suite. **Costs of arbitrary duplicate-rich documents are not measured here**.

| Q22 data/policy | gjson ns/op median | jsonparser ns/op median | gjson B/op, alloc/op | jsonparser B/op, alloc/op |
| --- | ---: | ---: | ---: | ---: |
| first/front/padding000 | 238.75 | **104.75** | 32 B,1 | 4 B,1 |
| first/back/padding000 | 239.9 | **104.65** | 32 B,1 | 4 B,1 |
| first/front/padding064 | 3974.0 | **2068.0** | 1152 B,1 | 4 B,1 |
| first/back/padding064 | 3951.0 | **2065.5** | 1152 B,1 | 4 B,1 |
| last/front/padding000 | 240.3 | **104.7** | 32 B,1 | 4 B,1 |
| last/back/padding064 | 3949.0 | **2063.0** | 1152 B,1 | 4 B,1 |

Observed source-adapter allocation differences suggest extra richer `Result`/string processing vs raw byte iteration; **do not causally attribute 1152B allocation only to one internal data structure without allocation profiles**. The policies and workloads are finite, and no cross-runner replication was done for this non-router source yet.

## Strongest rival and DIP-49

Source-aware classical **data provenance, raw JSON token parsing, schema/value distinction and lexical normalization**, with source-specific scan/allocation cost, predicts both can satisfy Q22. The two original sources differ in public API and cost, not in Q22 feasibility under one additive-file edit grammar. This is a valuable independent-domain **positive transport** of bounded source repair to lexeme provenance, **not** an identification of a beyond-classical structural law or formal proof any future repair is possible.

For independent future requirement Q23, the API distinction is sharper: gjson `Result.ForEach` retains both `key.Str` (semantic key) and `key.Raw` (original JSON quoted spelling), while jsonparser `ObjectEach` returns the **decoded** key byte string and value offset but no direct raw key spelling; its original full input buffer could still allow reconstruction via additional code, so **no information-theoretic impossibility** under Γ_add. See [prepped P37 program and strong rival court](P37_FLOWING_HANDOFF_REPAIR_GRAPH_GEOMETRY_PROPOSAL.md).

**Final verdict:** `P36_O12_TWO_ORIGINAL_INDEPENDENT_NONROUTER_JSON_Q22_NATIVE_PASS__JSONPARSER_UPSTREAM_VET_AND_PR286_HISTORICAL_QUALIFIED__PAIRED_COST_MEASURED__STRONG_CLASSICAL_RIVAL_PREDICTS_BOTH__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.


## Independent isolated-Q22 / race confirmation (post-original full experiment)

[Q22-only original independent matrix #37974852391](https://github.com/WhoSia/EvoNOMOS/actions/runs/37974852391) also completed **SUCCESS 2/2 original-package jobs**, `GJSON` and `JSONPARSER`, with the **same pinned exact upstream source SHA and the same frozen Q22 source/tests**. This isolated `go test -vet=off -race -v -run '^TestP36O12' .` from the pre-existing `jsonparser` unrelated PR286 original full-test failure, and independently performed Go vet with only the *historically existing* unreachable and unsafe-pointer analyzers disabled. Both scientific Q22 feature and concurrent read-only test PASS. This is an **independent CI workflow** but not an independent *source treatment* or separate model: no new sample of naturally evolved parsers was added. Upstream PR286 and unconditional full vet remain FAIL as recorded above.

[Strong-classical competitor scoring code's **synthetic-only** CI #37974481371](https://github.com/WhoSia/EvoNOMOS/actions/runs/37974481371) also ended **SUCCESS** after fixing a CI-only false positive that matched `NOT_AUTHORIZED` as `AUTHORIZED`. The five evaluator tests are not real predictive evidence. For any future holdout, code presently validates dataset shape/grouping and scores predictions but **cannot itself prove that predictions were committed before future outcome labels existed**: enforce separate hash-timestamped prediction manifests, repo holdout locks, and independent outcome provenance. No scientific-law change.

**Final readback scope:** `O12_FULL_NATIVE_WITH_EXPLICIT_UPSTREAM_QUALIFICATIONS_PASS__O12S_Q22_ISOLATED_RACE_2_OF_2_PASS__P37_PREDICTIVE_COURT_SYNTHETIC_1_OF_1_PASS__DIP49_HOLD`.
