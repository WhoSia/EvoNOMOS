# P40-P3 — Strong Architectural Rival Court: Source-Edit Permission Reversals, Nominal Observations & Single-Cut Repair Geometry

**EvoNOMOS Generation VIII LAW-R1-P40 · 2026-10-10 KST · MATHEMATICS-FIRST + ACTUAL GO SOURCE REVISION TESTS · DIP49 NEW-LAW IDENTIFICATION HOLD · LAW-R2 NOT_AUTHORIZED.**

[P40 P0 authorized scientific contract](P40_P0_AUTHORIZED_OPENING_COMPOSITIONAL_REPAIR_AND_ARCHITECTURE_LAW_CONTRACT.md) · [P40 P1 old-interface method-set court](P40_P1_GUARDED_SOURCE_REPAIR_COMPOSITION_AND_GO_INTERFACE_COURT.md) · [P40 P2 endpoint-versus-path theorem](P40_P2_ENDPOINT_SEQUENCE_OBSTRUCTION_AND_ATOMIC_SOURCE_EDIT_COURT.md) · [P39 Math-H exact cyclic-order work](../g8-law-r1-p39/P39_MATH_H_EXACT_SEVEN_SHATTERING_TWO_ANCHOR_AMALGAMATION_AND_INFINITE_BOUNDS.md).

## P3-A. Matched original source architecture world

The three architecture competitors are genuine **Go source constructs**, not abstract names:

**C — Coupled original-interface widening:** edit T adds \`Next() int\` to the existing \`Port{Run() int}\`; edit X adds \`Fast.Next\`; edit F publishes the new \`OpenAdvanced() Advanced\` factory where \`Advanced\` aliases the widened \`Port\`.

**D — Direct capability interface:** edit T declares \`Advanced interface{Port; Next() int}\` while **leaving Port unchanged**; edit X adds \`Fast.Next\`; edit F publishes \`OpenAdvanced() Advanced\` returning actual concrete \`Fast\`.

**W — Versioned interface plus adapter/wrapper:** edit T publishes \`PortV2 interface{Port; Next() int}\` and alias \`Advanced = PortV2\` while keeping \`Port\` unchanged; edit X defines a **NEW** \`FastAdapter struct{Fast}\` with \`Next\`; edit F publishes \`OpenAdvanced() Advanced\` returning \`FastAdapter{Fast{}}\). **The original Fast implementation is not modified**. \`PortV2\` here names a versioned interface contract, not a semver release.

All initial program worlds contain original \`Fast.Run()==7\` and \`Legacy.Run()==9\`, with the same \`Old(p Port)=p.Run()\`. When \`Legacy\` is protected, an original client continues to call \`Old(Legacy{})\` and a static \`var _ Port = Legacy{}\` check is kept. The future *structural* contract \(Q_s\) is the same in all three architectures: call \`OpenAdvanced()\`, observe \`Run()==7\`, \`Next()==42\`, and \`New(p)==49\). No client is allowed to observe the representation type under \(Q_s\).

A separate stronger future contract \(Q_n\) adds a **concrete dynamic Go type assertion** that \`OpenAdvanced()\` must contain precisely \`Fast\`. This contract discriminates D from W; this is a *different, stronger client observation grammar*, not a hidden violation of Q_s.

The allowed source edit grammar is exactly three **single** edits T, X, F, where the source revision MUST compile and preserve its own old-client tests after each authorized edit. Those operations are package-local and synthetic; actual maintainer permission and source-edit costs have not been measured.

## P3-B. Actual Go source acceptance and edit paths

[Go code revision generator and test harness](../../tools/p40-p3/architectural_rival_source_court.py) executes actual \`go test -count=1 ./...\` with no external dependencies on:
- 3 architectures × 2 protected-Legacy settings × 8 source states (T,X,F) = **48 distinct source-state test cases**;
- plus 3 architectures × 2 protected settings = **6 terminal type-identity client tests**, for **54 go test invocations** in total.

For \(Q_s\) after all three edits, every valid C/D/W implementation returns the same old and new numeric output; deliberately invalid source states fail the compiler or new contract as specified. The identity-sensitive \(Q_n\) actual Go test rejects W's \`FastAdapter\` dynamic type even though it fulfills the same \`Advanced\` method set.

| Architecture | Protected Legacy | Compile-and-old-client-safe states of 000,100(T),010(X),110(TX),111(TXF) and others | Sequential safe orders to 111 |
| --- | --- | --- | ---: |
| C coupled | no | 000,010,110,111 | **1**: X→T→F |
| C coupled | yes | 000,010 | **0** |
| D direct \`Advanced\` | no or yes | 000,100,010,110,111 | **2**: T→X→F and X→T→F |
| W versioned wrapper | no or yes | 000,100,010,110,111 | **2**: T→X→F and X→T→F |

All F-before-T or F-before-X source states are intentionally invalid; a future factory requires both a named declared interface and a compatible provider/wrapper. \`Legacy\`-protected coupled terminal is invalid regardless of update order because widening \`Port\` invalidates the frozen old implementer. In the unprotected coupled case, adding the method before widening \`Port\` is required.

**Notice the three architectures do not have different values of the common functional goal \(Q_s\) when they compile. Their contextual ranking is about feasibility under owner source-edit permissions and client-visible type observations, not fabricated runtime performance or design aesthetics.**

## P3-C. Exact conditional rival theorem — 3 architecture source/owner guards

Define Boolean inputs:

- \(p\): permission to publish contract T;
- \(f\): permission to publish factory/new client F;
- \(m\): permission to modify original Fast by adding Next;
- \(w\): permission to introduce a separate FastAdapter;
- \(L\): protected original Legacy must continue satisfying original Port;
- \(q\): future client insists on dynamic type Fast (the stronger Q_n);
- \(t\): sequential X-before-T forbidden by owner/release policy, i.e. T-first-only;
- \(a\): **separately permitted** atomic T+X joint edit. This edit *still requires* both affected source rights, so atomicity never grants a missing permission.

Under the three exact source grammars, **the necessary and sufficient guarded safe repair predicates** are

\[
\boxed{
R_C=p f m\;\neg L\;(\neg t\lor a),\qquad
R_D=p f m,\qquad
R_W=p f w\;\neg q.
}
\]

Juxtaposition is Boolean AND. The formula is derived from the compilation-safe cube, terminal contract and owner guard conditions. In C, T-only source fails Go type checking and X must precede T unless the separate authorized atomic T+X edge exists. When L is true, C's completed source violates the old interface and no atomic edit rescues it. D and W admit BOTH T/X staging orders for Q_s; D returns concrete Fast, W returns concrete FastAdapter and fails Q_n.

**Exact source-grounded model court:** [independent BFS versus formula checker](../../tools/p40-p3/architectural_permission_theorem_court.py) tests **all 2^8=256 owner/contract contexts × 3 architectures = 768 verdicts** and all match. Its six distinct architecture-feasibility signatures across the 256 contexts are:

| Viability (C,D,W) | Number of contexts |
| --- | ---: |
| 000 — none | 216 |
| 001 — wrapper only | 8 |
| 010 — direct only | 15 |
| 011 — direct and wrapper | 5 |
| 110 — coupled and direct | 9 |
| 111 — all three | 3 |

**Conditional architecture-reversal theorem within this grammar:** with p=f=L=1, q=0, t=a=0:
- if m=1,w=0, only **D** is reachable;
- if m=0,w=1, only **W** is reachable.
With m=w=1, both D/W satisfy Q_s, but enabling q=1 disqualifies W while D survives. If L=0 and t=1, C fails unless the independently authorized atomic T+X change is enabled.

**Partial order, NOT universal ranking:** for every one of these contexts, \(R_C\Rightarrow R_D\); D weakly dominates C **only for this specific source grammar and definition of repair reachability**. D and W are incomparable when the domain of possible owner rights varies. There is no evidence of a universal performance, development cost, code quality or maintainability rank.

## P3-D. Minimal owner-permission obstruction sets

Under the protected-Legacy old contract \(L=1\) and structural future demand \(q=0\), allowing a choice between D and W yields

\[
\boxed{R_{\mathrm{any}}=p f(m\lor w).}
\]

Thus the exact **minimal owner-permission denial families** blocking both design alternatives are:
- deny contract publication \(p\);
- deny future factory publication \(f\);
- simultaneously deny **both** Fast modification \(m\) and wrapper addition \(w\).

The joint failure criterion follows from the two prime implicants \(\{p,f,m\}\) and \(\{p,f,w\}\). Under stronger client demand \(q=1\), W's endpoint ceases to satisfy the observation contract, so the formula reduces to \(p f m\).

These are a **classical monotone Boolean DNF and minimal hitting-set theorem**, not a novel natural-science law. They do, however, produce an explicit conditional architecture-facing *permission minimal cut* instead of a vague SOLID slogan.

## P3-E. Important geometric correction: two edit-order paths can have ONE vertex cut

With D/W and full edit rights, the two valid sequences are T→X→F and X→T→F. BOTH pass through the same safe pre-factory state \((T,X,F)=(1,1,0)\). Therefore they have **two distinct linear edit orders but only one internally vertex-disjoint terminal repair route**; deleting source state 110 blocks ALL allowed paths.

\[
\boxed{\text{Safe edit order count}=2,\quad \kappa_{\rm internal}=1.}
\]

More generally, in the three-edit grammar F must occur after both T and X to compile. Even if the authorized atomic T+X edge is used, **every successful repair path** still passes 110 before final F. The BFS checker explicitly removes 110 for each of the **60 feasible architecture/context cases** out of all 768 and verifies no route survives. No claim is made for grammars admitting an atomic joint T+X+F terminal edit, arbitrary source rollback or an alternate factory mechanism.

This separates **path cardinality** from **Menger structural robustness** and is a sharper bridge from P39 minimum repair obstructions to genuine Go source states. Still classical reachability/cut theory under a declared grammar.

## P3-F. Strongest classical rivals and prior art

- [Go specification — interface type sets and embedded interfaces](https://go.dev/ref/spec) directly predicts method-set satisfaction; Go compiler provides actual independent type checks.
- [Official Go blog, *Keeping Your Modules Compatible*](https://go.dev/blog/module-compatibility) **explicitly identifies** that adding public interface methods breaks outside implementations, and recommends a new interface and capability type check. This is a **particularly strong prior-art defeat of a standalone new ISP/OCP law claim**.
- Go concrete type assertions and dynamic type identity explain why W fails a stronger client \(Q_n\). Representation independence holds **only under an explicitly restricted client observation grammar**; it is not full Go contextual equivalence.
- Guarded transition systems, classic reachability/Boolean prime implicants, Menger source-edit cuts, optional atomic commits and versioned adapters explain all mathematical claims.
- No original third-party Go repository or actual maintainer authorization was changed or measured. Protected edit rights and client observation scope are declared hypotheses; source-typing checks are real, but not a natural prevalence study.

**Novel-law judgment:** P40-P3 identifies an exact **conditional architecture-repair feasibility partial order** and original-Go-compiler-grounded countercontexts. Both the source behavior and mathematical classification are already anticipated by Go compatibility advice and finite labeled transition logic. **DIP49 NEW LAW IDENTIFICATION HOLD; no LAW-R2 permission.**

## P3-G. Next real scientific direction

Try **architecture alternatives that can defeat or reverse D/W under fixed old-client/future-client contracts without simply toggling edit rights**, such as a compatibility facade with independent interface versions, public API identity promises, plugin-style provider factories, source-level linked ownership and atomic migration protocols. Derive the smallest source-realistic cross-owner invariant that breaks a classical two-module gluing theorem. Compare strong Go compatibility/module-versioning and refinement/event-structure theories before claiming new mathematics; an already-classical result should be recorded as a useful negative novelty finding, not inflated as a fresh law.

**Status: P40 OPEN · P3 ACTUAL GO SOURCE + COMPLETE RIVAL MODEL · CLASSICAL PRIOR ART UNDEFEATED · DIP49 HOLD · LAW-R2 NOT_AUTHORIZED.**


## P3-H. Independent hosted Go-and-formal court receipt (2026-10-10)

[GitHub Actions #38041320962](https://github.com/WhoSia/EvoNOMOS/actions/runs/38041320962) **COMPLETED SUCCESS** for the *tested code/workflow* head \`528a48de7196c0ef25b0fb100d2bb6e5e7da16be\`. The job \`source-and-formal-rivals\` ran both independent steps successfully:
1. **Actual Go compiler/tests:** 48 distinct source-revision cases plus 6 independent terminal concrete-type future-contract test variants = 54 \`go test\` invocations, with intentional type/contract failures audited rather than silently bypassed.
2. **Separate mathematical court:** 256 permission/context assignments × 3 architecture versions = 768 BFS-versus-closed-form verdicts, including the stronger 60 feasible model-cases' shared internal vertex-cut proof.

Hosted artifact \`11666366140\`; artifact digest SHA-256 \`1d85d12d520e652961451cdd78d1fa309ec4cae6f55a4e30149c70375c709533\`. The tested head includes the **shared pre-factory state 110 cut check**, unlike preceding [#38041271814](https://github.com/WhoSia/EvoNOMOS/actions/runs/38041271814). Subsequent Markdown edits/README/Notion updates are NOT in that source-tested head, and the synthetic code does not establish real external maintainer permissions.

**Classification after hosted verification:** typed source behavior PASS, 768 finite model decisions PASS, classical Go compatibility guidance and standard CSP/graph reachability still fully explain the bounded conditional architecture outcome. No newly identified architecture law or independent pure-mathematical priority.
