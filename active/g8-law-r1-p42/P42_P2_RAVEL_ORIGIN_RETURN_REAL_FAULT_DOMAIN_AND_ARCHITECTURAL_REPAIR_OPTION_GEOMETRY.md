# EvoNOMOS Generation VIII LAW-R1-P42 — Origin Return RAVEL-R2/R3: Source-Indexed Repair Option Geometry, Actual-History Fault Domains & Demand-Conditional Architecture Tradeoffs

**2026-10-12 KST · continuation of officially approved P42-P2 · SOURCE_REALIZED_BOUNDED_PASS · TCS/OO research direction corrected · P42 RUNNING · LAW-R2 NOT_AUTHORIZED.**

## 0. Founding explanandum recovered, not rewritten

The foundational [P31 origin-return correction](../g8-law-r1-p31/P31_ORIGIN_RETURN_STRUCTURAL_EXPLANANDUM.md), [LawKit charter](../../lawkit/README.md) and [LAW-R1 constitutional envelope](../g8-law-r1-p0/LAW_SURFACE_CONSTITUTION.json) explicitly say that **program state distinguishability is a METHOD, not EvoNOMOS's scientific explanandum**. The explanandum is:

> For rival source-realized OO architectures satisfying the same present demand, under what structural boundaries, obligation correlations and changing future requirements does one design require more edits, impose larger capability/conformance demands, fail an old client or acquire an advantage that is absent or reversed in other demand environments?

A useful mechanism must name real OO source boundaries and *predict* the effect/vector under future demands; eventually SOLID can only be a contingent reduct. S/L/C/A/Q must remain a **vector**, not an uncalibrated combined score. P42-P2's earlier rich-vs-coarse contextual observation witness was correct, but extending its test suite indefinitely would again displace the founding explanandum.

This continuation intentionally uses TCS for two subordinate steps: (1) finite original-program observational quotient and a source-defined separating suite, and (2) **future edit-obligation spectrum** of initially behaviorally equal rival architectures. The latter is much closer to actual evolvability than simply discovering another response-code distinction.

## 1. RAVEL-R2 — real historical fault domain, not researcher-created fake mutants

**Original upstream:** [labstack/echo PR #3132](https://github.com/labstack/echo/pull/3132), v4 actual router grammar backport. Instead of a made-up third-world program, preserve its **real upstream original source progression**: PRE commit, C1 through C10 original developer commits, and the actual merged result (12 source snapshots). All are *original source bytes*, not synthetic rewritten router implementations.

**Frozen prior to harness:** [original 12-source × 16-client manifest](../../tools/p42/p2-r2/frozen_real_pr3132_fault_domain.json), commit **`b3711fbbbc30f128a6e5d2eedd42f723458aebcc`**, [standalone freeze gate #38200794862 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38200794862) at commit `04845477905f52c43c2bcd0d210f46d79201f833`. Client contexts include literal escaped-colon routes, generic fallback, registration order reversal, backtracking, wildcard, complex escaped parameter, leaf-rest path, encoded colon, POST method fallback and 405. The freeze did not specify individual per-version outcomes; it committed the version/context population and method **before native source testing**.

### Important source-provenance erratum (RAVEL failure repaired transparently)

Initial frozen C3 Git locator was mistyped as **39 hexadecimal characters**: `358c2e8c9efd52ed18e0a7fc91332e2f3cb9b05`. The actual original C3 SHA is **`358c2e8c9efd52ed18e0a7fc91332e2f3fcb9b05`** (40 characters, an additional `f` in the suffix). The frozen erroneous string was not changed. The first historical Git-source CI correctly rejected the source identity; the initial inference that a historical commit object was lost was **wrong**, and subsequently corrected using the authoritative actual C4 first-parent SHA and a separate successful original GitHub commit API read.

The independent [post-freeze source locator erratum](../../tools/p42/p2-r2/source_locator_errata.json) records exact bad/good strings, the source Git parent/child check and the **post-freeze timing**. The native runner applies this erratum only to the source locator; the original **16 observer contexts and behavioral hypotheses remain byte-for-byte frozen**. Never represent the full source-locator set as error-free at prereg time. Other RAVEL CI failures from the parent-integrity assertion were retained, and the final source gate accepts only actual accessible original commits.

### Source execution

[Original source Go Action #38201312245 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38201312245), checked EvoNOMOS harness HEAD **`e9d796b12b54665a6be76a8c91b5b80e0e3270d8`**, artifact **`11725127049`**, SHA-256 **`65a00d57a23585e8eb3ebd40ac8a2c490df962ecac97f0f5e4ec49f7960ae494`**. Run source: [Go 16-context fixture](../../tools/p42/p2-r2-native/fault_domain_source_test.go), [source-aware finite partition grader](../../tools/p42/p2-r2/exact_original_fault_domain_court.py). The workflow verified the frozen manifest ancestor, byte identity and pre-test absence, corrected C3 source revision Git identity, and ran **192 original native Go client queries** = 12 original programs × 16 frozen contexts.

**Observed quotient structure:**

| Property | Verified result |
| --- | --- |
| Original source SHA snapshots | 12 |
| Fine-grained selected source-implementation observational classes | **6** |
| Coarse HTTP-only selected classes | **6** |
| Smallest subset of the 16 frozen client contexts preserving either six-class quotient | **4** |
| Number of distinct cardinality-4 minimum context sets | **7** |
| Historically sourced revision pairs non-dominated under frozen five-demand Boolean vector | **20** |

The six classes are:
`{PRE,C1}`, `{C2}`, `{C3,C4}`, `{C5}`, `{C6,C7,C8}`, `{C9,C10,MERGED}`.

For both full handler-accessible observations and HTTP status/body/headers, a lexicographically first minimal distinguishing suite is:
`inline_basic`, `complex_param`, `leaf_path`, `wildcard_backtrack`.

**NEGATIVE result:** In this particular 12-source/16-client domain, HTTP and enriched handler traces induce **the same six-class partition**. P42-P2's earlier masked-client strictness witness was valid in a different fixture but does not imply a class-count increase for every hypothesis domain. Equating “more observation fields” with “more distinguishable programs” would be an unjustified universal principle.

### Independent cross-check, not self-grading

[Independent source-geometry and minimum certificate Actions #38201574238 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38201574238), independent checker HEAD **`ef45b26ad89064a89d9fab1fdc0c14b4c0cac730`**, artifact **`11725368020`**, SHA-256 **`2de9673d3f9c4a0dfcf9418d1959bde5869cdf864a3636ac536ab34167f3bd98`**. This workflow **reused the immutable earlier actual source Go artifact**, independently recomputed complete behavioral equivalence partitions and all minimum test sets by a different, direct subset/partition algorithm, and analyzed the original Git source diffs with `git diff --numstat`.

All **2,517** context subsets of sizes 0–4 were examined for each observer view. Exactly **seven** size-4 suites preserve the full six-class partition; none of size 0–3 do. Therefore 4 is a sharp cardinality minimum **for this frozen finite domain**. This is a classical minimum hitting-set / test characterization result, not a new generalized theorem about all router programs.

Original source geometry provides a useful control against observation reduction: **C3 and C4 were indistinguishable under all 16 frozen client contexts**, yet the actual original C3→C4 `perf(router)` stage changed **three implementation source files and 264 implementation lines** (count of inserted plus deleted lines), **zero test lines**. This does **not** prove a performance improvement (no benchmark), but confirms that complete **selected runtime behavior** does not recover source-edit structure. P31's origin warning applies: source structure is an independent variable, not replaceable by the observed HTTP vector.

## 2. Noncollapsed demand reversal in the real source history

The independently checked demand vector for the actual PRE and MERGED source revisions includes:

| Declared requirement | PRE | MERGED |
| --- | --- | --- |
| Legacy `GET /r/foo` accepted | **YES** | NO |
| Correct new inline-verb binding `Param("name")="foo"` | NO | **YES** |
| Selected backtracking old client | YES | YES |
| Selected leaf-rest path old client | NO | **YES** |
| Stable `/health` | YES | YES |

This is a true **bounded demand-conditioned preference reversal**: PRE satisfies a named legacy requirement absent from MERGED, while MERGED satisfies two other named requirements absent from PRE. Neither satisfies a superset of the other's named obligations. Twenty original-version pairs have such incomparable selected-demand vectors.

**What it is not:** The two historical versions are not a clean controlled test of alternative responsibility/dependency architectures meeting an identical full initial goal. They differ in runtime semantics and have other source history confounds. Calling their Pareto incomparability a universal SOLID or ISP/DIP structural reversal would violate [P31 origin rules](../g8-law-r1-p31/P31_ORIGIN_RETURN_STRUCTURAL_EXPLANANDUM.md).

## 3. RAVEL-R3 — the first founding-question-oriented structural rivalry

To correct that gap, construct **two controlled source-authored rival architectures using the exact SAME untouched original Echo v4 router** at `f085ffbe8f99de165bd920746920000ab56bd6bc`:

- `SINGLE`: install **one** source route `GET /r/:name\\:cancel`.
- `SPLIT`: install that same inline-verb route **plus a distinct client-specific generic fallback** `GET /r/:name`.
- `SPLIT_REVERSE`: same two structural routes registered in reverse order, testing the source-order moderator.
- `SINGLE_REPAIRED`: after late demand appears, install the missing generic fallback as one additional local source registration intervention.

Here the architecture choice is **actual registration/handler boundary structure**, not a relabeled same transducer. The **initial client functionality is deliberately identical**: `GET /health → 200/health`, `GET /r/foo:cancel → 200/new:foo`. The **possible later demand** is frozen separately: legacy `GET /r/foo → 200/legacy:foo` and `GET /r/foo:other → 200/legacy:foo:other`.

Original [frozen rival/D0/D1 specification](../../tools/p42/p2-r3/frozen_initially_matched_rival_architectures.json) committed **`3a1bac88d9cb4668b6dd5f7c41152e8de36f0d29`** before the source rival Go test file existed.

[Original Echo architecture rivalry Actions #38201810713 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38201810713), exact harness HEAD **`5516956ed79d1c7a861dc1295fb7de5b79688d1b`**, artifact **`11726082056`**, SHA-256 **`430aa9faefcbc9bb707ac6c50a2399c428e26e7585a8dabdf8cf83ecaec6fb69`**. [Native Go fixture](../../tools/p42/p2-r3-native/structural_rivals_source_test.go) and [strict temporal/source audit](../../tools/p42/p2-r3/verify_architecture_rivals.py) verify **16 named source-architecture/runtime observations** (four architecture source states × two initial plus two late clients):

| Structural source architecture | Initial client D0 | New late legacy D1 without further edit | Initial non-health route registrations | Later source registration edit required |
| --- | --- | --- | ---: | ---: |
| SINGLE | PASS | FAIL (404) | **1** | **1** |
| SPLIT | PASS | PASS | 2 | **0** |
| SPLIT_REVERSE | PASS | PASS | 2 | **0** |
| SINGLE_REPAIRED (post-edit state) | PASS | PASS | 2 after repair | 1 in its actual history |

The reverse-order source assembly gave identical selected results, but **only for these named contexts**. The extra route is an actual, verifiable source-boundary decision. A second original Go route registration is sufficient to satisfy the late legacy demand, and the original unedited SINGLE version fails both late requests. Hence, **relative to this specified edit grammar**, zero further edits is impossible for SINGLE, one extra source registration suffices, and SPLIT needs none.

This yields the meaningful source-grounded obstruction:
[
mathrm{Obs}_{D_0}(mathrm{SINGLE})
=
mathrm{Obs}_{D_0}(mathrm{SPLIT})
quad	ext{but}quad
operatorname{AdditionalRouteEdits}_{D_1}(mathrm{SINGLE})=1
\neq0=
operatorname{AdditionalRouteEdits}_{D_1}(mathrm{SPLIT}).
]

Therefore **no classifier using only present named-client observations D0** can recover the subsequent **edit burden** for both original-Echo-based rival assemblies. It needs an architecture/source dimension, a future-demand dimension, or both. This is the **origin-consistent part of P42**: present behavioral equivalence is insufficient to explain later source evolution of distinct architectural structures.

### Honest source-lifecycle and decision boundary

If the late demand **never occurs**, SINGLE has strictly less birth-time route-registration surface (1 vs 2). If the late demand **occurs**, SPLIT requires 0 new source-registration edits at that moment, SINGLE requires 1, and the repaired source eventually has **the same total 2 route registrations** as SPLIT. Hence:
- Initial creation burden favors SINGLE.
- Conditional future *incremental* modification burden favors SPLIT.
- In this measured setting there is **no demonstrated strict overall full-lifecycle cost superiority under D1**; the recorded route-count totals converge. Do NOT invent team hours, quantified failure rates, runtime overhead or a single positive/negative design score to force a net winner.
- This controlled **source structural intervention** is authored by the researchers, **not a historical alternative considered by the Echo maintainers**. Original Echo *upstream runtime/router code* is completely unchanged.

This is a bounded example of **design option value / deferred change burden**, explainable by existing real-options reasoning, information hiding (Parnas 1972), contextual refinement and source-edit distance. Its mathematical observation-kernel obstruction is classical and does **not** create new priority for a foundational TCS result.

## 4. Better fundamental TCS object for EvoNOMOS

Instead of treating source versions as static programs only, define a *demand-indexed edit game* on real source states. It has:
- A typed partial source-edit relation (s\xrightarrow{e}s'), with separately verified compilation, ownership and source-namespace admission.
- Present clients (D_0), later requirement sequences (d_1,d_2,\ldots), and admissible contexts (C_d).
- A non-scalar lifecycle vector (V(s,e,d)=(S,L,C,A,Q)), each coordinate with independently described units and epistemic status.
- A residual **repair-option correspondence** (\mathcal R_s(d)), the set of **source-realizable edit sequences that achieve d while preserving declared old-client contracts**. A meaningful cost object is not a single arbitrary metric but the Pareto frontier (\mathrm{PF}(\{V(h):h\in\mathcal R_s(d)\})).

The central object should be **the conditional reachability/future edit options of source structures under a demand environment**, not an unbounded syntax of quasi-SOLID axioms.

An exact mathematical question becomes: under what real source-boundary/composition conditions can (\mathcal R_s(d)) or its Pareto frontier **be factored through modular dependency/capability geometry**, and what minimal source or history information is necessary when it cannot? This connects existing P39 source-graph memory and P40 source-join findings to P31's actual mechanism-and-reversal ambition.

**New-theory viability gate:** first find a genuine independently evidenced effect (or impossibility) not already predicted by classical contextual equivalence, information hiding, automata characterization, guarded constraint satisfaction, source-edit reachability, formal concept analysis or ordinary real-options economics. Until then **the terminology is a proposed common research object, not a newly discovered theorem or new law**.

## 5. Scientifically binding next gates

1. **True multi-demand structural rivalry:** repeat both architecture choices under the same initial client contract and *multiple distinct future demand streams* (including co-requiring and disjoint client subsets), with actual original source interface/capability obligations; prospectively measure S/L/C/A/Q and find a genuine *whole-lifecycle* Pareto-sign or feasibility reversal. Ordinary registration-count shifting is not enough.
2. **Nontrivial repair graph:** add alternative edit paths (interface widening vs segregation; direct concrete provider vs injected port; shared authority vs dispersed membership). A source-edit option must be an actual admissible Go program transition, not an invented label; retain source compilers and caller histories.
3. **Source-to-theory bridge:** obtain a sound abstraction for a typed, documented subset of real Go source/route grammar and runtime contexts with either a simulation theorem or explicit completeness failure; do not imply Lean has verified full Echo by reflecting a static dataset into a toy theorem.
4. **Demand-indexed observability and rights:** audit which distinctions actually change the engineering decision (including absent/unknown historical ownership), not every distinction visible to a sophisticated tracer.
5. **Strong classical competition:** compare real source-aware guarded constraint/refinement and established modularity/change-propagation mechanisms with the **same source, demands and provenance budget**, preregistered before unseen future outcomes. Classical adequacy is a valid negative scientific result.
6. **No rank inflation:** P42-P2/R2/R3 = **BOUNDED_SOURCE_AND_STRUCTURAL_MECHANISM_PASS**; P42 overall RUNNING. Historic rights remain UNKNOWN, general architecture law HOLD, LAW-R2 NOT_AUTHORIZED.

## Receipts

- [Original P31 founding return](../g8-law-r1-p31/P31_ORIGIN_RETURN_STRUCTURAL_EXPLANANDUM.md)
- [EvoNOMOS LawKit founding method](../../lawkit/README.md)
- [R2 original frozen revision/context contract](../../tools/p42/p2-r2/frozen_real_pr3132_fault_domain.json) and [separate post-freeze SHA erratum](../../tools/p42/p2-r2/source_locator_errata.json)
- [R2 192 native original Go source traces Actions #38201312245](https://github.com/WhoSia/EvoNOMOS/actions/runs/38201312245)
- [R2 independent 2,517-context-subset minimum and source geometry Actions #38201574238](https://github.com/WhoSia/EvoNOMOS/actions/runs/38201574238)
- [R3 frozen rival demand/source specification](../../tools/p42/p2-r3/frozen_initially_matched_rival_architectures.json)
- [R3 original Echo code 16 rival-client observations Actions #38201810713](https://github.com/WhoSia/EvoNOMOS/actions/runs/38201810713)
- [Prior P42-P2 original real version and TCS Lean kernel](P42_P2_HISTORICAL_ROUTER_CONTEXTUAL_QUOTIENTS_AND_TCS_SEPARATION_COURT.md)

**Final judgment:** SOURCE-WITNESSED PRESENT-EQUIVALENCE / FUTURE-REPAIR-BURDEN NONFACTORABILITY, WITH EXPLICIT INITIAL-VS-LATE REGISTRATION TRADEOFF AND NO EVIDENCE OF NET LIFETIME SUPERIORITY. Its underlying mathematics is classical; a truly new general structural law remains an explicit future hypothesis subject to stronger evidence.
