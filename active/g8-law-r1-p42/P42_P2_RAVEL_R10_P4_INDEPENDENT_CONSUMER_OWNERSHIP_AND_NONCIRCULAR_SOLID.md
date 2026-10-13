# EvoNOMOS Gen VIII LAW-R1-P42-P2-R10-P4 — Independent Consumer Ownership Composition & Non-Circular Conditional SOLID

**Status:** SOURCE-REAL CROSS-REPOSITORY BOUNDED PASS · TWO TAG-CONTEXT NATIVE PASS · EQUAL-SOURCE CLASSICAL ADEQUACY PASS · NO NEW-LAW CLAIM. Parent P42 RUNNING; P43 HOLD; LAW-R2 NOT_AUTHORIZED.

## 0. Why this court is needed

The originating EvoNOMOS question was not to take SOLID as a theorem, or to accumulate elaborate proof apparatus. It was to explain **why and under what actual software change and client conditions competing structures are better, worse or incomparable**, with SOLID possibly a restricted useful description. R10-P3 showed history-sensitive repair paths, but the repair provider/root/adapter and demand sequence were all authored in the lab. R10-P4 therefore holds the gRPC implementation fixed, introduces **two genuinely separately maintained consumers' unchanged source**, and asks whether their actual semantic ownership contracts support a non-circular structural explanation.

This court is deliberately **not** a historical 2024 externally maintained consumer cohort. The pinned gRPC source is from 2024; the pinned Thanos and OpenTelemetry source revisions are later. This is a cross-version source-interop experiment. No source or runtime deployment from the independent projects is claimed to be running under the lab experiment's exact version pairing in production.

## 1. Source custody and preregistration

| Surface | Frozen exact source identity | What is original vs authored |
| --- | --- | --- |
| gRPC Go implementation | [grpc/grpc-go 9ab8b62505c85a5e03be1ae97949e960e24b6d4f](https://github.com/grpc/grpc-go/tree/9ab8b62505c85a5e03be1ae97949e960e24b6d4f) (2024) | Native library unchanged: BufferSlice.MaterializeToBuffer, NewBuffer, Free, NopBufferPool |
| Thanos | [thanos-io/thanos f1e0bbc906c54ca138466bd3095c3f61bf31368d](https://github.com/thanos-io/thanos/tree/f1e0bbc906c54ca138466bd3095c3f61bf31368d), `pkg/extgrpc/codec_stringlabels.go` blob `6268c8a351d5b74a362774197602be10debd922c`, and `codec_slicelabels.go` blob `7819a41abc34dbb9983c61882f0883d6dbcef79d` | Both byte-exact imported original files. Only an **extra** authored exported test-only forwarding shim calls the original package-private function |
| OpenTelemetry Collector | [open-telemetry/opentelemetry-collector e838d926f0e018e3503886923a27d42a35c4bdad](https://github.com/open-telemetry/opentelemetry-collector/tree/e838d926f0e018e3503886923a27d42a35c4bdad), `pdata/internal/otelgrpc/encoding.go` blob `4f3bfdb6cccf2fdd845f82e256f74910b084395f` | Byte-exact imported original CodecV2 body. Authored probe implements the codec's expected `otelEncoder` interface; its bytes are **synthetic test inputs**, not a production collector message |

[Immutable R10-P4 test prediction and boundary](../../tools/p42/p2-r10/frozen_p4_independent_consumer_and_noncircular_solid.json) sealed at [WhoSia commit 48b99302](https://github.com/WhoSia/EvoNOMOS/commit/48b9930211b7e9d93bd4b14ab7b5079a190c4a8d) **before** [fixture materialization code](../../tools/p42/p2-r10-native/make_independent_consumer_fixtures.py) and [Actions workflow](../../.github/workflows/g8-p42-r10-p4-independent-consumers.yml) existed. The workflow tests freeze-byte immutability/ancestry; fetches source from exact upstream commit URLs; verifies all three real original Git blob hashes both before and after materialization; and uses read-only CI with no bot-authored Git writes.

## 2. New real-source observation: identical bytes, different obligations

Original 2024 gRPC `mem.BufferSlice.MaterializeToBuffer(pool)` increases the existing original Buffer's reference and returns it **without a copy** when given exactly one Buffer. With multiple Buffers it creates a newly allocated/materialized Buffer via the supplied pool. Original `Buffer.Free()` returns backing to its tracked pool when all references are released.

Two Thanos **real originally authored build-tag** implementations share the same signature `materializeForUnmarshal(data mem.BufferSlice) ([]byte, func())`:

- Default `!slicelabels`: `MaterializeToBuffer(mem.DefaultBufferPool())`, returns both bytes **and a concrete `buf.Free` callback**.
- `slicelabels`: `MaterializeToBuffer(mem.NopBufferPool{})`, returns bytes **and a nil callback**.

For the single-Buffer input case, **the Nop pool setting does not override original gRPC's single-Buffer reference shortcut**. The observed difference is thus the downstream ownership-return interface, not merely a method name or user-written dummy pool.

Original independent OTel codec `codecV2.Marshal` gets byte storage from its private tiered `otelBufferPool`, invokes its `otelEncoder.MarshalProto` input and wraps the resulting storage in original `mem.NewBuffer`. Two concurrently outstanding *synthetic payload* codecs are held alive while the real Thanos materializer is invoked. This physically executes both real consumers within one Go process.

### Actual native receipt

[Original Go independent consumers #38331951042 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38331951042); [same-source classical revalidation #38332093569 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38332093569), tested EvoNOMOS HEAD `6adade5cb1cce84f98db50996d6145e0ca731d8a`, native job `115083901632`, artifact ID `11782703878`, ZIP SHA-256 `fc55624d7d53e4230e00a5deaf0c889cbc7ad240522fb9cbf6ad211ca74a3561`.

| Selected Thanos original build mode | Thanos observed byte | Cleanup supplied? | Research-authored tracking pool Put after freeing original input, then available cleanup | Original OTel first bytes of two simultaneously outstanding outputs |
| --- | ---: | --- | ---: | --- |
| default | `0x41` | yes | `1` | `0x43, 0x44` unchanged |
| `slicelabels` | `0x41` | no | `0` | `0x43, 0x44` unchanged |

Independent Thanos multi-fragment input `2 × 1024` was also tested in both modes: each returned identical 2048-byte contents; the cleanup callback remained nonnil/nil according to the original build choice.

**Interpretation limit:** The 0-count is **not** evidence of an upstream memory leak or defect; it is the bounded observation that the tested single-buffer ownership reference had not been returned to the *lab-authored counting pool* at the end of this particular use sequence. Real caller lifetimes, source version history, GC, workload costs and downstream consumer conventions are not fully represented.

## 3. Non-circular software organization signature

Define the underlying universe without mentioning any SOLID principle. Let

\[
\mathfrak{E}=(P,E,\Gamma,\mathcal C,\mathcal D,\operatorname{Obs},\operatorname{Tr},\operatorname{Own},\partial,\otimes,\mathcal W)
\]

be a family of source states `P`; concrete source-edit relations `E`; time/source-owner qualified permitted transitions `\Gamma`; independent client contexts `\mathcal C`; prospective requirements `\mathcal D`; observer-projected traces `Obs,Tr`; allocation and release/ownership relationships `Own`; module boundaries `\partial` and partial composition operator `\otimes`; plus an explicit workload/lifecycle environment family `\mathcal W`.

These are operational objects with independent semantics: the terms are meaningful whether an engineer has heard of SOLID or not. For a given client population and requirement `d` define

\[
\mathcal F_{\Gamma}(s,d,\mathcal C)=
\{h=(s=s_0\xrightarrow{e_1}\dots\xrightarrow{e_k}s_k):
 \forall i,\ \mathrm{Compile}(s_i)\land
 \mathrm{Preserve}_{\mathcal C}(s_i),\
 \mathrm{Meets}_d(s_k),\
 (s_{i-1},e_i,s_i)\in\Gamma_i\}.
\]

**Time and the existing-client preservation requirement are explicitly part of the semantics.** Current bytes alone are not the predictive structure; retaining the release-ref observable may be necessary for a future source-repair decision.

### A restricted classical frame/composition proposition

Assume for two independently supplied modules A and B:

1. Their **reachable mutable backing regions are disjoint under the evaluated client history**, including any shared global state reachable from either; this is stronger than different package names.
2. An A-local edit does not touch B-owned source and does not change the contract exposed at the A–B boundary as observed by the selected clients.
3. Ownership transfer and reference-release effects at that boundary refine the previously accepted trace contract.
4. Each stage's concrete source edit is permitted and both modules compile.

Then old B-local observational safety is retained when A is edited, and the combined selected observer can be checked from the preserved boundary trace and the two local traces. **Proof method:** standard frame/locality reasoning followed by contextual trace refinement; the B observer's read footprint is unaffected by the A edit, and cross-boundary observations are handled by premise (3).

This is a **sufficient, scoped proposition**, not a newly discovered theorem, and not a proof in Coq/Lean or all Go. Premise (1) fails if a buffer is aliased into another consumer region; premise (3) fails when callers rely on a callback that no longer exists. Separate Go package names alone prove neither.

The **countermodel** is the exact original Thanos/gRPC single-buffer branch: if an abstraction collapses source states by `returned bytes only`, both Thanos variants are observationally equivalent under that abstraction but distinct under the callback/release observer. Therefore byte-output-only equivalence is insufficient for this declared ownership-sensitive client family. This is a classical contextual-distinguishability result with authentic, independently maintained source witnesses.

## 4. SOLID inside the universe: definability is not yet derivation

Only **after** defining source/program/client meanings independently do we propose scoped predicates:

| Conventional principle | Candidate predicate in the independent structure | Current evidence boundary |
| --- | --- | --- |
| SRP | A declared decomposition of independently varying demand families admits local edits whose observable effects do not spread across the other responsibility boundary | Not derived from Thanos/OTel; defining a responsibility partition is itself nontrivial |
| OCP | For a future demand `d` there exists an authorized extension-only source-edit path preserving all original client traces and leaving the declared protected core unchanged at each step | R10-P3 is a finite example of safe extension preparation; no universal OCP deduction |
| LSP | Replacing an interface implementation preserves all **declared relevant client observables**, including resource ownership and eventual release, rather than only satisfying the method set | Thanos/gRPC establishes why byte equality/method compatibility alone is insufficient for this selected lifetime observer; does not settle full LSP |
| ISP | A client's admitted interface and obligations are a sufficient projection of only the capabilities it actually invokes; splitting a composite interface cannot silently lose shared semantic invariants | Candidate formalization only; no native witness proves an ISP advantage |
| DIP | Consumer behavior and future repair availability factor through a stable semantic provider contract across admissible implementation substitutions and ownership transfer | Candidate formalization only; actual provider independence is context-sensitive and cannot be inferred from an interface edge |

A purely set-theoretic inclusion \(\{\mathfrak E:\varphi_{\rm SOLID}(\mathfrak E)\}\subseteq\{\mathfrak E\}\) is **trivial** and cannot be advertised as 'SOLID derived from more fundamental axioms'. Substantive non-circular derivation would require an independently justified set of minimal semantic assumptions, prospective statements about actual source edits, and a demonstration that applying the restricted predicate predicts an outcome that strong classical formalisms cannot predict on the same information.

In particular, the five original English principles need **not** be asserted universally true, mutually consistent in every design, or logically implied by object orientation. This study establishes a useful semantic **interpretation agenda**, not a general inclusion/isomorphism theorem.

## 5. Demand-conditional comparison and the absent winner

With exactly the two unmodified Thanos build alternatives and two deliberately registered client contract families,

- `D_explicit_release`: return a callable cleanup and return the single-buffer underlying authored pool reference after input.Free and callback invocation.
- `D_no_cleanup_api`: return a nil cleanup callback, while preserving bytes.

the observed admissible choices are respectively **default** and **slicelabels**. Both also satisfy the independent OTel byte preservation check.

This is a **scope-limited conditional feasibility polarity**, not a measured causal architecture advantage or performance reversal. The `D_no_cleanup_api` requirement was defined by researchers to test a structural difference, not verified as a fresh independent customer's demand; no genuine workload preference distribution, service time, allocation count or engineering labor cost was measured.

Do **not** write 'Thanos's release mode is better' or 'Nop mode is better'. The strongest adequate equal-input classical rival—original Go reference counting, known build-tag compilation, and memory region/trace contracts—predicts all observations exactly. [Reproduced classical source oracle](../../tools/p42/p2-r10/source_independent_consumer_classical_audit.py) independently reads actual gRPC and consumer source code, predicts before consulting native logs, agrees in both build contexts, and rejects an altered release callback source.

## 6. Next falsifiable research gate

1. Find an **independently demanded, temporally documented real requirement** in one or more consumer repositories where two structurally distinct and similarly qualified *source-repair options* are both feasible *before* observing resolution. Mark any 2024 contemporaneity honestly; never backdate a 2026 source.
2. Pre-register a pair of competing **new** structural predictors and the strongest classical alternatives (ownership logic, contextual refinement, worklist/path planning, change-impact and source diff models) with equal information and a distinguishing test, not merely a feature label.
3. Require an actually measured multi-objective or time-ordered feasibility consequence and a source-grounded path. Test whether ownership/frame contracts predict conditional structural preference or failure on **unseen demands**, including adverse independent consumer contexts.
4. If the strongest classical theory predicts the same result, **retain as classical adequacy**, do not promote to novel SOLID or EvoNOMOS law.

**Closure verdict:** R10-P4 SOURCE-REAL-INDEPENDENT-CONSUMERS PASS; scoped ownership contract difference and cross-module byte noninterference PASS; equal-source classical analyzer PASS; meaningful new mathematical/software-design law remains **UNIDENTIFIED**. P42 RUNNING · P43 HOLD · LAW-R2 NOT_AUTHORIZED.


## 7. R10-P4-MATH-A: an exact minimal observer refinement, not a universal SOLID axiom

**Post-outcome mathematical analysis (not preregistered).** Take the **exact two original Thanos build configurations** \(a_0\) (default) and \(a_1\) (`slicelabels`) under the **single, 2048-byte original gRPC Buffer context** \(c^\*\). A Go counting-pool input, the later original OTel codec outputs, and the declared release sequence are fixed, as described above.

Write \(\beta(a)\) for the returned byte sequence, \(\chi(a)\in\{0,1\}\) for existence of the returned cleanup callback, and \(\rho(a)\in\{0,1\}\) for whether the origin counting pool receives exactly one Put after the specified source-Free-then-if-available-cleanup sequence.

The actual original-Go observations establish

\[
\begin{aligned}
\beta(a_0)&=\beta(a_1),\\
(\chi(a_0),\rho(a_0))&=(1,1),\\
(\chi(a_1),\rho(a_1))&=(0,0).
\end{aligned}
\]

**Proposition — byte-only prediction impossibility on the two-state fixed support.** For this test support \(U=\{a_0,a_1\}\), there exists no function \(g\) satisfying \(\rho(a)=g(\beta(a))\) for all \(a\in U\). Proof: equal input \(\beta(a_0)=\beta(a_1)\) would require equal \(g\) outputs, contradicting the observed unequal \(\rho\). Thus the byte-output quotient is strictly coarser than the quotient sufficient to decide the declared ownership-return requirement. The single extra bit \(\chi\) **does** distinguish these two exact source states, so one additional binary distinction is necessary and sufficient on \(U\) (not for all programs, requirements or ownership policies).

In kernel language,

\[
\ker(\beta,\chi)\ \subsetneq\ \ker(\beta)
\]

on this registered support. The mathematical inference is ordinary factorization/observational equivalence; the contribution is an authentic **cross-repository software consumer witness** with the source and execution identities pinned.

**Guarded composition frame (classical).** Let \(T_A,T_B\) be local trace sets and \(\pi_A,\pi_B\) their projections to the same **ownership-complete shared interface alphabet** \(\Sigma\). Under an explicitly validated compositional semantics
\[
T_{A\otimes B}=\{(x,y)\in T_A\times T_B:\pi_A(x)=\pi_B(y)\},
\]
and refinements \(T'_A\subseteq T_A\), \(T'_B\subseteq T_B\), it follows immediately that \(T'_{A\otimes B}\subseteq T_{A\otimes B}\). Proof: every synchronized pair from the smaller product is already a synchronized pair from the larger product. **But** this implication is only as adequate as the interface trace alphabet and the exact pullback assumption. If \(\Sigma\) omits release/borrow-transfer events that the client can observe later, the premise that \(\pi\) is ownership-complete is false. In our test, \(\beta\) alone is an explicit counterexample to treating that projection as ownership-complete.

This has a precise relevance to LSP and DIP *without assuming either*: a source-level interface or emitted byte trace is not a sufficient abstraction for substitution in a client whose contract observes later release behavior. The proper object of refinement must include such events, or the result must be explicitly scoped to clients that never observe them.

**Non-circularity test:** The predicates \(\chi\), \(\rho\), the trace pullback and preservation rule were defined in the programming semantics without mentioning any SOLID label. LSP/DIP can be interpreted **afterward** as restricted policy families within those semantics. This is a defensible translation and a falsification of output-only sufficiency, **not** a derivation of all five SOLID principles as universal or mutually exhaustive design laws. Classical contextual refinement, reference counting and separation/ownership logic remain sufficient explanations on all verified evidence.

**Decision for next court:** Do not create a new axiomatic framework merely to restate this proposition. Obtain genuinely independent future maintenance demands with two adequate, implementable structural alternatives, preregister a discriminating observable that source-aware classical rivals cannot trivially reproduce, and evaluate actual lifecycle outcomes or repair-option survival under the same information budget.
