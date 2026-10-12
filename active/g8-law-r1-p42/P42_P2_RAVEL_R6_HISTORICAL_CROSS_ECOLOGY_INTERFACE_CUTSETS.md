# EvoNOMOS Generation VIII LAW-R1-P42-P2-R6 — Cross-Ecology Capability-Propagation Cutsets & Demand-Indexed Program Refinement: Historical Interface Changes, External Consumer Compatibility, Independent Classical Predictors & Minimal Source-Repair Certificates

**2026-10-12 KST · user-confirmed official P42-P2-R6 title · RAVEL discovery → preregistration → source execution → negative counterexamples → independent Lean kernel → external-source challenge → scope-controlled promotion. P42 RUNNING, P43 NOT_STARTED, LAW-R2 NOT_AUTHORIZED.**

## 0. Finding: structural change propagation is an edge- and demand-indexed phenomenon

R5's original Go language fixtures established a deliberately controlled capability/obligation geometry, but **did not** show that historically independent OSS maintainers made such choices. R6 now observes **two real independent original codebases and three distinct interface events** under **four exact historical source revisions**:

1. [go-chi/chi PR #926, merged 2024-06-28](https://github.com/go-chi/chi/pull/926): adds `Discard()` to the **existing** externally implementable `middleware.WrapResponseWriter`. Historical PRE `7957c0d4ddaee560a01110145dbf2809ffdb6663`; POST `67be7d9cafdaeb4e04e887ff78d09e030ee43b00`.
2. [grpc/grpc-go PR #7356, merged 2024-08-21](https://github.com/grpc/grpc-go/pull/7356): preserves old `encoding.Codec` unchanged and adds **parallel** `encoding.CodecV2`, while at the same time replacing the signatures of `mem.BufferPool.Get/Put` from `[]byte` to `*[]byte`. Historical PRE `7e12068baffd8e6328e99d901409cd49d0edebf6`; POST `9ab8b62505c85a5e03be1ae97949e960e24b6d4f`.

These events distinguish three source-level mutation operators: **strengthen an incumbent interface**, **introduce an opt-in parallel boundary**, and **substitute the types of existing methods without changing method count**. A general unqualified claim “smaller interface = fewer edits” cannot classify them. The appropriate classical object is a demand-indexed incidence relation between **exact typed method signatures**, client references, provider method sets and source-edit sites.

**R6 BOUNDED_POSITIVE for real source mechanisms, NEGATIVE for novelty over strong classical typed API compatibility.** These are not new universal axioms. The existing Go team's own [module compatibility guidance](https://go.dev/blog/module-compatibility) explicitly explains that adding methods to an existing public interface is source-breaking; [Go apidiff's original compatibility rules](https://go.googlesource.com/exp/+/master/apidiff) already distinguish method-set and typed-signature changes. R6's gain is **verified historical cross-ecology instances**, independent actually maintained Heroku consumer compilation, and a precise separation of **type repair** from **behaviorally adequate repair**.

## 1. Real historical source provenance and pretest freeze

### Original interfaces at exact commits

| Ecology/event | PRE source | POST source | Native interface effect |
| --- | --- | --- | --- |
| chi WrapResponseWriter | `7957c0d4` | `67be7d9c` | required `Discard()` **added** |
| grpc mem.BufferPool | `7e12068b` | `9ab8b625` | `Get(int) []byte; Put([]byte)` → `Get(int) *[]byte; Put(*[]byte)` |
| grpc encoding.Codec | same pair | same pair | original `Codec` signature **unchanged** |
| grpc encoding.CodecV2 | absent | present | new parallel `CodecV2` contract with `mem.BufferSlice` |

Sources: [chi original interface](https://github.com/go-chi/chi/blob/67be7d9cafdaeb4e04e887ff78d09e030ee43b00/middleware/wrap_writer.go); [gRPC original preexisting Codec](https://github.com/grpc/grpc-go/blob/9ab8b62505c85a5e03be1ae97949e960e24b6d4f/encoding/encoding.go); [new CodecV2](https://github.com/grpc/grpc-go/blob/9ab8b62505c85a5e03be1ae97949e960e24b6d4f/encoding/encoding_v2.go); [postchange typed BufferPool](https://github.com/grpc/grpc-go/blob/9ab8b62505c85a5e03be1ae97949e960e24b6d4f/mem/buffer_pool.go).

[Frozen R6 seven-client matrix](../../tools/p42/p2-r6/frozen_cross_ecology_interface_matrix.json) was written at EvoNOMOS `main` **`096aca61ea7c5f56c0919dfa3a8bb35930128815`**, **before** either R6 Go test-source family existed. An independent [pretest gate #38209588486 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38209588486) checked schema and absence of Go oracle files, HEAD `ae313cd4e5af4399e288cf53beef85e8411a2b1f`, artifact `11729136335`, SHA-256 `d113b2426b8cf6ecf0d51e5dfc52aeddcfa168c08b6cd4fb8306e9d403d82626`.

The final original-Go action independently checks: freeze is a Git ancestor; frozen manifest is byte-for-byte identical to ancestor; named Go test oracle files were absent at freeze; all four upstream checkouts are **exactly pinned** and **read only**. The native consumer programs are **researcher-authored**, exercising unchanged historical package sources and original Go method-set type checking. They are not disguised as original maintainers' clients.

## 2. Native original-Go evidence: 7 cases × 2 source revisions

[GitHub Actions #38209926838 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38209926838), exact tested harness HEAD `746405b2c8db409df5c1f37dc610aeaa5a7ed3d0`, artifact `11729171932`, SHA-256 `f883a3478ff5260a299cb7623824788fa3e17dafcb64c939bb6e0790463f0b9a`. Exact original upstream source and compiler stderr/stdout for every acceptance and rejection are in its artifact, including frozen hash and per-source test hashes.

| Original-source client | Historical PRE | Historical POST | What is and is not proved |
| --- | --- | --- | --- |
| chi old external implementation of `WrapResponseWriter` | **COMPILE** | **REJECT** | Post addition demands missing `Discard` |
| chi old implementation with `Discard(){}` added | COMPILE | COMPILE | **Only structural type repair**; no-op `Discard` does not implement discard semantics |
| chi new `Discard` feature invocation via original factory | REJECT | **COMPILE / RUN** | Original POST factory really drops original response and tees bytes |
| grpc old `mem.BufferPool` provider (`[]byte`) | COMPILE | **REJECT** | `Get` return and `Put` argument must match new exact signatures |
| grpc new pointer-buffer provider (`*[]byte`) | REJECT | COMPILE | Reverse compatibility; no automatic old client adapter |
| grpc original `encoding.Codec` implementation | COMPILE | COMPILE | Parallel CodecV2 does **not** remove legacy `Codec` |
| grpc new `encoding.CodecV2` implementation | REJECT | COMPILE / RUN | New API did not exist before, is opt-in after |

**Compiler acceptance 9, rejected 5, all 14 frozen forecasts matched.** The [verifier](../../tools/p42/p2-r6/audit_native_compiler.py) requires the exact named **Go compiler diagnostic** for every expected failure, not simply any nonzero exit status, and the real Go PASS marker on each success. It also checks a disclosed *source-aware classical method-set predictor*, which matched 14/14.

**Importantly, this comparison does not claim that the classical model is an independent blinded engineering system.** Its method signatures and cases were deliberately constructed after inspecting known 2024 source changes. The conclusion is **classical adequacy**, not novel TCS superiority or unseen forecasting skill.

## 3. Independently maintained external consumer: Heroku source actually compiled

This evidence tier is distinct from the researcher-authored seven clients. A real independent repository, [`heroku/x` at commit `59fc5216`](https://github.com/heroku/x/blob/59fc5216e297df6368fbf4e214bc91c7bb64a8ed/hmiddleware/logger.go), defines its original `hmiddleware` client around `middleware.WrapResponseWriter`: it calls `NewWrapResponseWriter`, `Status`, `BytesWritten`, and `Unwrap`, but does not need to implement the chi interface itself. Its [actual project test file](https://github.com/heroku/x/blob/59fc5216e297df6368fbf4e214bc91c7bb64a8ed/hmiddleware/logger_test.go) was executed unmodified.

A separate [cross-temporal real consumer freeze](../../tools/p42/p2-r6/frozen_heroku_actual_external_consumer.json) predicted that `go test ./hmiddleware` on identical Heroku source would pass against both original chi revisions. The forecast was committed at `90fa41b8cd07666fc731f21e60434f72c928f98c` **before** the external-go test action existed.

[Independent original Heroku Go Actions #38210450426 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38210450426) checked harness HEAD `f7532701f8e8587f399a93b40e352b5a8fd474c4`, artifact **`11728428288`**, SHA-256 **`32af10517de0471b1d23bf77ccfd6f59b5c0c2e6fab88abfdc4599ab35898b5d`**:
- Unmodified Heroku `hmiddleware` original code/test suite compiled and passed with pre-change chi.
- The **same** original Heroku source/test suite compiled and passed with post-change chi.
- The workflow used two isolated Go workspaces outside both projects; **no source or original module files were changed**.

This is a genuine independent-project consumer compatibility witness. **Time limitation:** the pinned Heroku snapshot can postdate the 2024 upstream change; it is a **cross-temporal controlled intervention**, not proof that Heroku's actual code in June 2024 had this exact structure. Two other independently maintained consumer implementations were source-inspected but **not** Go-compiled: [Cortex's `CodecV2` and `mem.BufferPool` integration](https://github.com/cortexproject/cortex/blob/1c18027a4e3ca8aea1a8ffbf2570184db1d4e30d/pkg/cortexpb/codec.go) and [Milvus's pointer-pool implementation](https://github.com/milvus-io/milvus/blob/023e356a8b609057c456cbdba9a84d9fd207a56f/pkg/util/resource/codec_buffer_pool.go). Do **not** count them as successful native external consumer compilation.

## 4. Theoretical structure: typed obligation hypergraph, not a new pseudo-axiom

A provider's ability to satisfy a boundary is determined by the set of **full method signatures**, not merely method names or count. For revision `t`, let `Req_t(I)` be the boundary's set of exact typed requirements and `Methods_t(P)` the provider method set.

[
\operatorname{Conforms}_t(P,I)
\iff
\operatorname{Req}_t(I)\subseteq \operatorname{Methods}_t(P).
]

A source-changing operator transforms both the boundary `I` and external provider or consumer obligations. R6's three actual structures:

**(i) Existing interface method addition** (`go-chi/chi`). Source transition increases the contract by `Discard()`. An external implementation that satisfied the old contract can fail the new contract without changing a single preexisting method. A designated one-site provider-method grammar requires adding `Discard()`. However a no-op implementation can type-check **while failing the new intended semantics**, meaning `Conforms` is not `BehaviorallyRefines`.

**(ii) Nonmonotone typed method substitution** (`grpc` `mem.BufferPool`). Before and after, there are exactly two required method names; nonetheless the exact signatures change, so neither historical provider's typed method set automatically satisfies the other contract. Under **the explicitly fixed source-repair grammar with one edit per existing method declaration**, each mismatched `Get` and `Put` declaration must be fixed, giving a **2-site minimum**. Other repair grammars allowing wrappers, adapters, provider replacement, grouped edits, or redefinitions may have different minima. This is not a global minimum Go patch.

**(iii) Parallel interface/consumer opt-in** (`grpc` `CodecV2`). A new boundary can extend reachable behaviors without invalidating old `Codec` implementations, **when the old contract and dependent callers really stay untouched**. This does not make the entire gRPC PR backward-compatible—its other `BufferPool` change was not. It establishes a scoped component-wise effect rather than blanket compatibility.

Represent each failed typed obligation as an edge incident on the source locations able to repair it. A **cutset/hitting set** intersects all such failure edges. Its minimum is meaningful only relative to: a frozen **edit grammar**, a selected **source/consumer graph**, declared **behavioral obligations**, and an actual **future demand**. A 1-method chi repair, a 2-signature grpc pool repair, and a 0-change legacy Codec client are different demand-indexed cut structures.

This structure is already explainable by classical **structural typing**, [Go API compatibility rules](https://go.googlesource.com/exp/+/master/apidiff), and source-aware constrained hitting sets. Go's own maintainers explicitly contrast method additions with using a new interface in [Keeping Your Modules Compatible](https://go.dev/blog/module-compatibility). No universal nonclassical Pareto reversal was measured. R5's hypothetical demand weights/probabilities remain hypothetical in R6; **actual engineering hours, migration rates and population risks were not estimated**.

## 5. Independent Lean 4.34.1 kernel model and limits

[Lean `P42HistoricalInterfaceCuts.lean`](../../tools/p42/lean/P42HistoricalInterfaceCuts.lean) represents the exact source-identified change classes as separate closed historical **signature-incidence worlds**, proving:
- chi PRE legacy accepted / POST legacy rejected, while adding one signature restores structural acceptance in both;
- gRPC old/new BufferPool provider compatibility **reverses** as exact signatures change;
- gRPC original `Codec` accepted at both revisions while new `CodecV2` is absent PRE and accepted POST;
- gRPC BufferPool's method count is identical in both revisions but the same provider's compatibility is different;
- under the restricted two-signature edit grammar, both `Get` and `Put` edits are necessary, and changing only either one fails;
- an interface-compatible dummy `Discard` repair cannot be used as evidence of required runtime effect.

**[Independent kernel-check Actions #38210179415 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38210179415)** at exact formal HEAD `91dd12b28c59ab5b03e62feb7c22ca37c5fb00f1`, artifact **`11728318536`**, SHA-256 **`264eeb036ba5079badd22185714ebaaa47dc771db4142558d973ed03f07df691`**. All 13 Lake build jobs succeeded, including `P42HistoricalInterfaceCuts`, and independent `leanchecker` succeeded. An initial proof script [#38210039376 failed](https://github.com/WhoSia/EvoNOMOS/actions/runs/38210039376) because a nonexisting Boolean helper lemma was invoked; the repair used explicit case analysis on the two required method-site Boolean values without altering the theorem.

Lean establishes **facts about this declared finite incidence model only**; the independent Go CI attests selected original-source compiler acceptance. A full verified interpreter or simulation proving *all* original Go source and client semantics refine the Lean model **has not been constructed**.

## 6. RAVEL judgement, remaining gates and where genuine TCS novelty could arise

**PROMOTE (bounded):** two real independent original 2024 interface changes; three source mutation mechanisms; four source revisions; 14/14 original Go typecheck forecasts including 5 actual compiler rejections; real Heroku external project source passing both controlled chi checkout substitutions; restrictive cutset/lower-bound observations; independent finite Lean court; direct classical adequacy.

**HOLD:** any inference that interface size alone predicts lifecycle work, that typechecked `Discard` has correct effects, that the pinned external Heroku/Cortex/Milvus snapshots are contemporaneous original 2024 clients, that every actual consumer of the merged PR compiled, that the restricted 1- or 2-site repair minima are globally minimal patches, that Go compiler semantics were mechanically proved in Lean, or that new architecture/TCS axioms or LAW-R2 are warranted.

**NEXT:** a repository-level, date-scoped consumer cohort with real **versioned** external module dependency graphs and source changes, not just pinned modern snapshots; preregister method-level obligations and demand traces before source outcomes; test multiple repair grammars/adapters with **functional behavioral contracts**, not typecheck alone; produce a **source-realized edit-graph minimum cut or unattainability certificate** with an independent classical optimizer given identical inputs. Compare prospective unseen PRs and publish the equally valid **negative** conclusion if established classical methods suffice.

The substantive EvoNOMOS scientific target is **compositional closure of source-resolved obligations under actual library edits**: determine whether typed method-set constraints, behavior constraints, module boundaries and external client histories can yield sound, tractable, genuinely predictive change-impact certificates. That is a TCS / programming-languages research problem, not permission to relabel ordinary interface subtyping as a new law.

**Final R6: BOUNDED VERIFIED, external true consumer PASS with cross-time caveat; P42 RUNNING, P43 NOT_STARTED, LAW-R2 NOT_AUTHORIZED.**
