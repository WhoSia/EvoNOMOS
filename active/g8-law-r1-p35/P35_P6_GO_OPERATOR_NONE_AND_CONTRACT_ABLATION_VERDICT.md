# EvoNOMOS Generation VIII LAW-R1-P35-P6 — Go Source-Operator Change Prediction, Explicit NONE and Contract-Level Ablation

**Date:** 2026-10-09. **Bounded phase verdict:** `P35_P6_GO_NATIVE_SOURCE_OPERATOR_PASS__COCHANGE_LABEL_POLLUTION_DETECTED__B1_NO_UNQUALIFIED_VICTORY__PATCH_RELATIVE_CONTRACT_ABLATION_PASS__P35_OPEN__LAW_R2_NOT_AUTHORIZED`.

**Core scientific question:** when does a source change activate an obligation to modify another component, and when is that component a safe **NO-EDIT** despite source linkage? This is about **Go program structure, change-operator semantics, information hiding, contracts and evidence**, not econometric cost estimation, scalar SOLID points or a universal law.

## 1. Reproducibility and seal chronology

### Independent genuine Go historical source: Cobra

- Public [spf13/cobra](https://github.com/spf13/cobra) `v1.8.1` pinned **`e94f6d0dd9a5e5738dca6bce03c4b1207ffbc0ec`** (2024-06-01), disjoint from earlier Restic and chi source families.
- Additional untouched native original-module verification [read-only Actions **#37906172605**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37906172605) **SUCCESS**: `go test -count=1 ./...` across Cobra and `go test -race -count=1 .` in its root package, Go 1.23.12; original source is not modified. Artifact **11604845582**, SHA256 `ce8ed71c27993ab458da5aa378182cce4de556a9f1a4039b8312f662f0c44fdd`.
- Prespecified historical train/heldout boundary **2021-01-01T00:00:00Z**. Training: nonmerge commits older than 2021. Heldout: 2021–2024 through pinned 2024-06-01. Event is a Git commit editing ≥1 target; given input for each seed is the actual Go file before/after **for that seed only**, not the future or other files. Task: predict a companion changed file, **NONE**, or **ABSTAIN**. Therefore this is historical **seed-patch completion**, not a prediction from a user demand before any code has changed.
- [Original v1 prehistory protocol](P35_P6_COBRA_OPERATOR_NONE_PREHISTORY_SEAL.md) named `command.go`, `completions.go`, `args.go`. [Train CI #37904355177](https://github.com/WhoSia/EvoNOMOS/actions/runs/37904355177) **FAILED before model generation**, because `completions.go` was absent from actual pre-2021 source SHA `a4ab3fa09e3d6c4ac3fb7deece97a910957305ab`. This is a **historical source eligibility**, not a predictive, failure.
- [Human-authored v2 cohort eligibility correction](P35_P6_COBRA_COHORT_ELIGIBILITY_V2.md) preserves original protocol and replaces only target triad with files **verified to exist at cutoff**: `command.go`, `args.go`, `cobra.go`. Original B2 mapping accordingly adjusted before scoring. No heldout cochange labels inspected. [Second train CI #37904565320](https://github.com/WhoSia/EvoNOMOS/actions/runs/37904565320) failed on Go printer's unsupported `*ast.FieldList`, repaired by formatting the receiver's `Type`; dedicated Go receiver regression added, no theory-rule change.
- [Read-only successful train-only CI #37904751015](https://github.com/WhoSia/EvoNOMOS/actions/runs/37904751015) **SUCCESS** (Go 1.23.12 `go vet`, unit tests, source/history analysis). Training 223 nonmerge events, 20 multi-target events, source revision `a4ab3fa...`. Artifact **11603439629**, SHA256 `2b4b3877403968a41cbfb0c3004899dd3b964efe0d872a55f8a7fd1f40172253`.
- Human `WhoSia` [commit `4b18d1c`](https://github.com/WhoSia/EvoNOMOS/commit/4b18d1c44f5f7f6cd996027a74e8511c64f465d5) freezes the exact [Go-generated training JSON](../../tools/p35-p6/seals/cobra-v2-training-predictions.json) **before** original holdout evaluation.
- [First scorer #37905067809](https://github.com/WhoSia/EvoNOMOS/actions/runs/37905067809) failed **before opening heldout labels**, because the external Chi 405 test fixture was also in the P6 Go module as a separate package and `go vet ./...` tried to type-check it against Cobra. [Human runner correction `30c97cb`](https://github.com/WhoSia/EvoNOMOS/commit/30c97cbcd97497bf70de4ccc730168f448d26dd1) limits `go vet` and `go test` to the actual P6 predictor package; it changes neither predictor model nor frozen oracle.
- [Successful read-only heldout CI **#37905258309**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37905258309) re-creates old training JSON from the original Git history and rejects **any byte mismatch with the committed seal before reading later multi-file labels**. Go test/vet/build PASS; evaluation artifact **11604475851**, SHA256 `161df656b694bb5b8bba7ab41408f87a44cbac814e8037f92c4aeebdb0691509`.

**All commits to EvoNOMOS are authenticated human `WhoSia` author/committer; Actions `contents: read` and never push code or Git refs.** Earlier failure workflows remain visible rather than hidden.

## 2. Formal distinctions and registered fair rival interfaces

Let `S={command.go,args.go,cobra.go}`. A heldout commit `c` exposes a changed seed file `f`, along with **only that seed's before/after Go AST**. Define observed companion existence:

`Y_path(c,f)=1` iff at least one other file `g∈S\\{f}` is in the same commit's diff.

`Y_AST(c,f)=1` iff at least one other file has a non-equivalent normalized Go AST.

`Y_required(d,f,g;Q,G)=1` only if every admissible repair in declared grammar `G` satisfying behavior `Q` and requirement `d` requires editing `g`. **No Git or Go AST historical label certifies this last quantification.** A single-file ablation of a chosen patch is a narrower counterfactual witness, not a theorem about every repair.

The fixed Go `go/parser`/`go/ast` encoder extracts three seed-side operators from actual seed changes: `TYPE_SHAPE` if a Go type spec changes, `FUNCTION_ONLY` if declarations/methods change without a type-spec change, and `NO_DECL_CHANGE` otherwise. Last category includes documentation, package globals, imports and other declarations. This is intentionally coarse and need not imply behavioral contract change.

All predeclared rivals see the same seed patch/operator and old training source/history, not heldout companion changes:

| Method | Frozen decision rule |
| --- | --- |
| B0+ Go AST operator | Syntactic cross-file symbol neighborhood selects top companion only for `TYPE_SHAPE` with nonzero static score; otherwise `NONE` |
| B1 history + operator | For each seed/operator stratum, train conditional multi-file rate; at least five old events and rate ≥0.5 gives top prior cochange partner, lower rate gives `NONE`, fewer than five gives **`ABSTAIN`** |
| B1 seed-only | Same historical threshold but pooled across operator classes, to test if operator improves over unconditioned cochange |
| B2 qualitative information hiding | On `TYPE_SHAPE` use fixed command/args/cobra responsibility map, otherwise `NONE`; **not** full Design Rule Spaces/CSDG |
| Always NONE | Explicit class-imbalance/singleton control; predicts no companions on every seed |

No new EvoNOMOS H win is asserted; strong `go/types`/SSA and full CSDG plus independently curated contract-aware baselines remain to be implemented and defeated.

## 3. Heldout observable result: real Git prediction with NONE and abstention

42 original nonmerge commits, 8 multi-target commits, 53 seed-patch queries: **19 observed companion-positive**, **34 singleton-negative**. Source-side operator categories: `FUNCTION_ONLY 29`, `NO_DECL_CHANGE 18`, `TYPE_SHAPE 6`. Methods disagree on 17 seed-patch queries.

| Fixed model | Correct companion among 19 positive queries | Correct NONE among 34 singleton queries | Unnecessary singleton alerts | ABSTAIN |
| --- | ---: | ---: | ---: | ---: |
| B0+ Go AST + operator | **0** | 29 | 5 | 0 |
| **B1 old Git cochange + operator** | **4** | **31** | **1** | **6** |
| B1 old Git cochange, seed only | **4** | 32 | 2 | 0 |
| B2 conditional Parnas mapping | **0** | 29 | 5 | 0 |
| Always NONE | 0 | **34** | 0 | 0 |

B1 operator-specific model on positives also issued `NONE` 11 times, one false singleton alert, and six total abstentions across both classes. B1 old seed-only achieved the **same positive hit count** without abstaining and with one additional false alert; therefore no clear operator-conditioned superiority at matched coverage. ALWAYS_NONE wins singleton specificity by design but fails every true observed companion. No scalar accuracy number turns this into a universal architecture ranking. The observations concern **coedited paths**, not a necessary patch graph. Related seed queries inside one commit are correlated.

## 4. Stronger Go source-truth audit — 3 of 8 paired commits are not code changes

After the entire prediction score was frozen, read-only [Cobra Go AST audit **#37905630361**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37905630361) replays all 42 original heldout commits. Actual `go/parser` with comments excluded and normalized `go/format` shows:

- **8 / 42 commits** change multiple target paths.
- **Only 5 / 8** change non-comment Go AST in at least two target files.
- **3 / 8 multi-target commits** change **zero target Go ASTs**: [copyright year #1927](https://github.com/spf13/cobra/commit/9e6b58afc70c60a6b3c8a0138fb25acc734d47e3), [license headers #1809](https://github.com/spf13/cobra/commit/6d978a911e7fff69b1ca2a873dd91d78ebca44cf), [doc-string name corrections #1885](https://github.com/spf13/cobra/commit/bf11ab6321f2831be5390fdd71ab0bb2edbd9ed5). They account for **8 of 19** positive per-seed *path-level* labels. These are legitimate maintenance commits, but not joint program-structure edits.
- At least **two** of B1 operator's **four** path-level hits arise from such administrative change labels: the two triple-file header/year revisions have a `cobra.go` `NO_DECL_CHANGE` seed, whose human-sealed B1 operator predicts `command.go` due earlier coediting. An observed top-1 hit need not signify any actual joint Go behavior change.
- [Cobra micro-optimization #1957](https://github.com/spf13/cobra/commit/3d8ac432bdad89db04ab0890754b2444d7b4e1cf) touches all three ASTs but changes unrelated optimization opportunities; even an AST-mutating multi-file commit does **not** certify necessary coupling.
- [Persistent parent hook feature #2044](https://github.com/spf13/cobra/commit/4cafa37bc4bb85633b4245aa118280fe5a9edcd5), [OnFinalize #1788](https://github.com/spf13/cobra/commit/93d1913fb03362f97e95aeacc7d1541764cafc2f), and [case-insensitive names #1802](https://github.com/spf13/cobra/commit/d689184a421607457a18131e0a2b602fec22e3b4) show genuine cross-file feature/representation contact in the original source, without uniquely identifying minimal repairs.

Audit code: [Go original-source AST auditor](../../tools/p35-p6/sourceaudit/main.go). Artifact **11604790346**, SHA256 `87efb53b266b719a18a2294b7b4082d18c6f2555c81d2d28c5f7edf7642a0d27`. This is **post-score exploratory explanation**, and must not be re-scored as if it were the initial blind prediction.

## 5. Actual-Go behavioral counterfactual, separate truth tier

[Read-only original Chi **405 contract ablation Actions #37904876755**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37904876755) compiles and runs the real [2023-07-13 HTTP 405 `Allow` header commit](https://github.com/go-chi/chi/commit/4b14b832d53cef6c77fdcf852876a34f46bc84a2). The exact original source runs its full Go test suite and a dedicated native Go HTTP public-contract regression [`allow_405_test.go`](../../tools/p35-p6/contract/allow_405_test.go).

With original target source intact: whole-suite + `go test -race` public 405 contract **PASS**. Revert *one* touched Go production file to its original parent's bytes while retaining the other two and the new test:

| Ablated file | Observed |
| --- | --- |
| `mux.go` | compile or public-contract test **FAIL** |
| `tree.go` | compile or public-contract test **FAIL** |
| `context.go` | compile or public-contract test **FAIL** |

Evidence artifact **11603762816**, SHA256 `bc72123c52034cbda11f2041a3339e292ed91c087567c2cf8743f096dd22ae80`.

This is stronger than path-level cochange: it demonstrates **for this exact implementation and fixed HTTP behavior test**, each chosen source file participates in satisfying that contract. **But it does not prove that all possible Go implementations under all admissible repair grammars must edit those three files**. A refactor might relocate or substitute responsibilities. It is **retrospective source intervention**, not heldout predictive performance.

## 6. Scientific interpretation and next expansion gate

A corrected evidence ladder for EvoNOMOS:

1. **Git path cochange**: evidence of joint commit bookkeeping, sometimes documentation-only.
2. **Go AST cochange**: evidence of simultaneous syntax changes, often stronger but can include unrelated batch edits.
3. **Go executable behavioral ablation**: evidence that a particular historical implementation depends on particular modified source sites for a fixed contract.
4. **Grammar-complete repair necessity**: proof that *every* admissible repair satisfying `Q,d,G` requires a source responsibility; not established here.

The next Go-native investigation should build a **source-level contract propagation graph** with `go/types` or SSA, allow `NONE`/`ABSTAIN`, and distinguish raw Git cochange from semantic coupling **before selecting the next heldout sample**. Predeclare contract witnesses, independent Go source worlds, and an equally informed implementation of strong Design Rule Spaces/CSDG alongside B1, rather than comparing with a deliberately weak heuristic. Perform actual native test and file-ablation interventions on prospectively chosen changes. Do not tune decision thresholds to these scored 42 commits.

**Bounded P35-P6 phase CLOSED.** Parent P35 **OPEN**, persistent research continues, no LAW-R2 authorization. The retained failures, negative labels and competing classical explanations are productive science rather than a reason to abandon the problem.
