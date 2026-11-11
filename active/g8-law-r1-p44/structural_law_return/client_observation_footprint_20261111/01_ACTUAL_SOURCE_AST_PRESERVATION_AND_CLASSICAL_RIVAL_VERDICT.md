# EvoNOMOS — First Source-Derived Restricted Client-Observation Preservation Certificate

**2026-11-11 KST · original P35-P7 Go AST source verified / ten source actions evaluated / conservative global-dependence negative control PASSED / classical code-slicing novelty NOT established / LAW-R2 HOLD**

## 0. Research object, exact scope, and why we ran it

Previous [source-to-repair execution](../source_to_repair_20261111/02_ALL_TEN_NATIVE_GO_REPAIR_ACTION_VERDICT.md) tested five source edits against prior LIVE/SNAPSHOT architecture alternatives. Later [direct-client scope sensitivity](../source_to_repair_20261111/04_DIRECT_CLIENT_SCOPE_SENSITIVE_REPAIR_CONE_VERDICT.md) verified that preserving the *researcher-proposed*, not officially promised, historical case sensitivity of direct \`NewPattern(pattern).Match(value)\` clients narrowed the tested repair options from three to one per original architecture. However, that result was obtained by adding a new Go test, **not by a source-derived predictive observation-footprint analysis**.

This investigation instead asks whether an AST-derived, deliberately restricted **definitely-preserved** finding can be constructed in the actual source, and compares it with a weak classical baseline (any modified production source file may affect any client in that file). The results of previous native direct Go tests are ALREADY KNOWN. Neither the baseline nor the Go AST analyzer is novel; this is in-sample calibration to define a credible source-to-client abstraction target.

### Frozen source and repairs

- Original genuine upstream go-chi/chi v5.1.0 application/library source used in earlier trials.
- Original 2026-10-09 research-owned source architecture variants, Git blobs **LIVE \`ad9a2fbc0a30a39475f746068e74e2d3e6c93999\` and SNAPSHOT \`e9ca2c3863d5aa06ef0f0b9d168ddcf184713d75\`**.
- Same five *previously frozen and source-native executed* operators: \`none\`, \`constructor\`, \`route_both\`, \`remove_lookup_lower\`, \`match_lower\`.
- Public direct microclient boundary **specified by researcher**, not automatically discovered: the composed expression \`NewPattern(pattern).Match(value)\`. Its narrow semantics require only the locally allocated \`Pattern\` struct fields and standard Go \`strings.IndexByte\`, \`strings.HasPrefix\`, \`strings.HasSuffix\`, and builtin \`len\`, with \`strings.ToLower\` admitted in the *changed* repair variants.

[Pre-execution frozen analysis rule and explicitly acknowledged known-test outcomes](00_AST_CLIENT_PRESERVATION_PRESEAL.md) was committed BEFORE running the new AST analyzer. It anticipated 8 modified files across 10 arm×patch rows, 4 truly changed direct old-client cases, and an analysis able to certify no direct change for the remaining six. No new Go customer test was written, no direct Go result newly observed, and no claim of blind prediction is made.

## 1. Executed static extraction

[Go AST analyzer](source_client_footprint.go) parses the two source revisions with the standard \`go/parser\`, normalizes the exact declarations' AST printing and identifies modified function and type declarations. It records:

1. **File baseline MAY-AFFECT** whenever any source declaration in \`route_headers.go\` is modified; this deliberately coarse source-file baseline cannot distinguish protected direct consumers from route-only consumers.
2. **Direct-client MAY-AFFECT** if either \`NewPattern\`, receiver \`Pattern.Match\`, or the \`Pattern\` struct type AST changed, or the analyzer fails its strict limited source-body purity check.
3. **Restricted DEFINITELY-PRESERVED** iff none of those three declarations changed and the original and patched direct-only function bodies satisfy the syntactic whitelist of allowed standard string operations, local receiver fields and identifier names. It must refuse preservation on unfamiliar calls/selectors or identifiers that could read hidden mutable global state.

**Justification of the bounded certificate:** Under fixed original Go import binding/build environment, the source-microclient evaluates exclusively two unchanged local definitions and the unchanged Pattern type. Both functions in these exact source revisions have no other application call, mutable global read, reflection or externally observable side effect. Therefore the expression's value is identical at equal inputs for the pinned source pair. This is a simple **closed pure subprogram framing argument**, NOT full Go contextual equivalence or a general static-analysis soundness theorem. No claim is made about callers using different methods/fields, package initialization, interface dispatch, cgo, concurrency, external code that was not within this identified direct microclient, or arbitrary Go repositories.

**Adversarial fail-closed test:** [test_fail_closed_global.py](test_fail_closed_global.py) creates a synthetic source revision where the direct \`Pattern.Match\` body reads a package global \`sharedGate\`, while an ostensibly unrelated \`RouteHeaders\` function changes that global. The direct function's text itself does NOT change between before/after; a pure unchanged-method checksum would falsely certify preservation. The AST conservative identifier check flags the unexpected global read and REFUSES certification. This demonstrates why a file-function checksum alone is **not a sound general client-preservation proof**. It does NOT establish handling of all possible Go aliasing/global effects.

## 2. Actually verified results

[Final GitHub Actions **#42937640036 SUCCESS**](https://github.com/WhoSia/EvoNOMOS/actions/runs/42937640036) compiled the Go AST tool, checked both original blobs, applied the same five guarded source operators separately to each ephemeral source, compared every declaration change with pre-specified expected grammar sites, and cross-tabulated against **previously measured, known** native Go direct legacy customer cases in [#42932257551](https://github.com/WhoSia/EvoNOMOS/actions/runs/42932257551). Original GitHub job logs were read back including ten SOURCE_FOOTPRINT rows and ADVERSARIAL_HIDDEN_GLOBAL_PASS.

| Source repair action | File-level baseline MAY-AFFECT | AST microclient MAY-AFFECT | AST restricted direct client definitely preserved | Earlier native Go direct client behavior changed |
|---|---|---|---|---|
| \`none\` | NO | NO | YES | NO |
| \`constructor\` | YES | YES | NO | YES |
| \`route_both\` | YES | NO | YES | NO |
| \`remove_lookup_lower\` | YES | NO | YES | NO |
| \`match_lower\` | YES | YES | NO | YES |

These five rows **repeat identically for LIVE and SNAPSHOT**. Aggregates from 10 arm×operation cases:

- File-level coarse MAY-AFFECT flags **8/10** (all four edits per architecture, two \`none\` unchanged).
- Restricted AST MAY-AFFECT flags **4/10**, with **6/10 restricted preservation certificates** (including the two unedited \`none\`).
- Previously native Go direct-client observed behavior changed in **4/10**, matching the four MAY-AFFECT flags in this already-known finite grammar.
- Among the **8 actual source edits**, 4 were classified direct-client MAY-AFFECT and 4 were direct-client definitely preserved under the restricted pure microcontract.
- **0 independently unseen future client demands; 0 independent new test execution** in this latest AST workflow. This is source-based retrospective consistency only, not estimation of precision/recall on a realistic task distribution.

There were earlier failing harness runs:
- [#42937012746](https://github.com/WhoSia/EvoNOMOS/actions/runs/42937012746) Go compile failed due to unused import in research analyzer; corrected without touching the source arms.
- [#42937091304](https://github.com/WhoSia/EvoNOMOS/actions/runs/42937091304) original whitelist rejected the newly authored \`strings.ToLower\` candidate even though it is a standard string operation; fixed and reran.
Final run includes stricter **unknown-identifier rejection** and adversarial hidden-global negative control; all PASS. Do not conflate these harness failures with tested architecture repair failures.

CI source code and machine-readable receipt generator: [run_impact_court.py](run_impact_court.py); receipt artifact \`p44-source-client-observation-footprint\`.

## 3. What this adds to the mathematical program — and what it does not

Previously \(\mathcal P_A(Q)\) was the set of finite repair actions passing explicit customer tests. Now obtain a *three-valued conservative client impact* of a source edit \(e\), client \(c\):
- \(\operatorname{Preserve}(e,c)\): certified within a **verified closed/pure source microcontext**;
- \(\operatorname{MayAffect}(e,c)\): uncertainty or observed direct-code modification, not necessarily breakage;
- \(\operatorname{Break}(e,c)\): an actual old-client counterexample from a native test, not inferred from an AST difference.

This prevents the invalid conflation \(\text{changed AST}\Rightarrow\text{contract broken}\), and the invalid converse \(\text{same changed production file}\Rightarrow\text{all clients affected}\).

Within a defined repair grammar and source/client semantics, a candidate client-preserving source-repair set can be narrowed by **safe exclusions** and certified inclusions:
\[
\mathcal R^{\rm verified}_{A}(Q)\ \subseteq\ 
\mathcal R^{\rm possible}_{A}(Q)\ \subseteq\ \mathcal E,
\]
where certified preservation of a client constitutes only ONE required contract obligation, and unknown impacts cannot be treated as passing. This is standard may/must reasoning and frame-like modular semantics; **not a new theorem**. Actual current client-specific direct contract was hand-specified and the oracle was previously seen. Computing a source-extracted client map and true owner-permission-aware action feasibility remains open.

### Classical strong rival, explicitly not beaten

A source-file-level impact test is a deliberately weak strawman. A standard interprocedural program slicer, symbolic executor or accurate change-impact analyzer can also identify this trivial pure direct subprogram and reach the same conclusion given identical source and client roots. Accordingly, the 8→4 reduction is **not evidence that EvoNOMOS outperforms existing static analysis**. A credible next trial requires equal-information direct comparison to existing Go tooling, unknown consumers, dynamic dispatch, mutable aliases and independently authored future changes.

## 4. What is actually distinctive at the project level

**Useful connected research chain** (not yet a novel law): authenticated old Go source and patch candidates → AST-certified *local* customer-preservation facts → finite native Go tests for new requirements and possible unsafe edits → explicit repair action options → minimal decision-conflict hypergraph for different inaccessible future contexts → cost of source observation/coordination/owner rights.

In the current known Chi issue, \`route_both\` has **two syntax edits** but preserves direct clients, while \`constructor\` has **one syntax edit** but potentially breaks protected direct clients; a larger edit can be safer under a broader customer contract. This is a legitimate architectural tradeoff within a specified observation boundary, not universal economic superiority of local fixes or OCP/ISP/SRP derivation.

**Next falsifier:** Can the analysis *automatically discover real customer roots* and compute a provably safe may-affect region for Go programs with package globals, pointers/interfaces and callbacks, as opposed to manually naming \`NewPattern.Match\`? Can it outperform or add a meaningful certificate to a same-information standard Go call graph/slicer or model checker on independent source revisions? Could it provide a useful Pareto frontier for old-client safety vs repair labor and runtime cost? These tasks are still open.

**Research disposition:** bounded static Go client preservation result accepted as calibration; STOP adding known #1247 regex variants; leave \`LAW-R2 HOLD\` and G1–G7 OPEN. Real source-derived client-observation footprint remains the research objective, not an achieved broad theorem.
