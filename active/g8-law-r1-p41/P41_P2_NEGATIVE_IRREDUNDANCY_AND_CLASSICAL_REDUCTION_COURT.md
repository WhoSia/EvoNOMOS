# EvoNOMOS G8 LAW-R1-P41-P2 — Noncircular Axiom Irredundancy, Source-Realized Projection Countermodels & Classical Reduction Court

**2026-10-11 KST · P41-P2 FIRST BOUNDED NEGATIVE COURT · full A–F independent axiom basis OPEN · LAW-R1 · LAW-R2 NOT_AUTHORIZED.**

## 0. Decision first — the six-field “foundation” cannot be promoted

P41-P0 proved that A–F *can be separately falsified in a deliberately unconstrained finite product*, but that syntactic result does not establish independent axioms of object-oriented software evolution.

P41-P1 now independently finds:
- original Echo **route-identity hidden by equal HTTP status/body** in two source-admitted router worlds: [native Go #38063086233 PASS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38063086233);
- original Echo **two same-interface, different-behavior providers**, and **a third provider missing a real interface port fails Go compilation**: [original Go #38063852776 PASS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38063852776);
- authenticated GitHub current role `admin` on `WhoSia/EvoNOMOS` PLUS an independently re-fetched, timestamped **actual upstream Echo PR #3132 merge actor/commit**; historical branch-policy/normatively legitimate permission STILL UNKNOWN: [C/F provenance document](P41_P1_AUTHENTICATED_PERMISSION_AND_NATIVE_PROVIDER_EVIDENCE.md).

**Verdict: no claim of six necessary, sufficient, pairwise independent, source-realized OO axioms is currently defensible.** However, selected **information/observer lower bounds** are noncircular and source-supported.

## 1. Three distinct levels of “independence”

| Level | Proof obligation | Current result |
| --- | --- | --- |
| (I) **Syntactic model independence** | independent field valuations in a free product `EditWorld` | P0 Lean PASS, **synthetic only** |
| (II) **Source-realized information insufficiency** | same admissible coarse evidence with different external trace/dispatch/contract verdict | route identity and provider behavior original Go **PASS** in chosen cases |
| (III) **Semantically independent and irredundant OO axioms** | each candidate premise independently observable and necessary in a domain-restricted, noncircular theorem with a source-realized (N-1) refutation and no stronger classical equivalent | **NOT_PROVED** |

An (N-1) Boolean assignment is a theorem of an unconstrained product only; it does not satisfy Level III. A target defined as `SafeGlue := A∧B∧C∧D∧E∧F` makes “necessity” trivial and is excluded.

## 2. Concrete classical nonfactorization witnesses (sources versus proofs)

### 2.1 Source registration + status/body are not sufficient for handler identity

Let `q` retain program compilation, accepted route registration, old HTTP output, requested method/URL, new status and new body; discard the actually selected route ID. The two original Echo router instances constructed in P41-P1 satisfy identical `q` but dispatch `TAGS` versus `UPLOADS`. Thus **no** decision function from just `q` can return actual route identity for every world in the declared source family.

Formal proof of the generic factorization obstruction is an elementary classical theorem already present in [P41SemanticP0.lean](../../tools/p41/lean/P41SemanticP0.lean), not a proof of the complete Go semantics.

### 2.2 Structural port compatibility does not determine semantic provider behavior

The original [Echo `Router` API](https://github.com/labstack/echo/blob/3882266a3641a36fc2111b48cd597adab1c1ecea/router.go) declares four interface methods. Both the forwarding provider and diverted provider implement `echo.Router`, are admitted to `NewWithConfig` and run. One returns `CONTRACT_OK` and the other returns `WRONG_PROVIDER` for identical user input. The selected *client contract verdict* differs despite equal static port compatibility and source acceptance.

Therefore there is no universal correct classifier of the selected provider behavior using only these two Boolean facts. When the actual method body (including a purposely diverted `Route`) is available, ordinary source-aware data refinement/contextual analysis can distinguish them. No claim is made that **all** source-based semantics fail.

### 2.3 A current platform role cannot establish historical permission

The authenticated current-role record is now complemented by a genuine historically timestamped platform event: original [Echo PR #3132](https://github.com/labstack/echo/pull/3132) was merged by account `vishr` into `v4` at `2026-09-30T01:00:17Z`, merge SHA `f085ffbe8f99de165bd920746920000ab56bd6bc`. An [independent GitHub REST re-fetch #38064380066 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38064380066) compared PR metadata, timeline's `merged` event and the two actual `COMMENTED` review records. This establishes an actual version/time-indexed **platform merge operation**. It does **not** show which protection/approval policy was in force or the right to make unrelated edits. Two histories can have the same current administrator status and agree on this merge event yet disagree about rights for another earlier edit. The Lean historical nonfactorization witness is still a **synthetic model**; actual rights changes for any named account were NOT demonstrated. No impropriety or wrongful editing is inferred.

## 3. Noncircular axiom *minimality* rejection: the A/F overlap

For the **original Go provider fixture with explicit interface assertions**, let:
- (A_{mathrm{build}}(p)) be successful compilation of the *whole assembled module*, including `var _ echo.Router = (*Provider)(nil)`;
- (F_{mathrm{shape}}(p)) be provider satisfaction of the original four-method `echo.Router` structural port.

The Go compiler's successful type check of that assertion **entails** `F_shape`, hence:
[
A_{mathrm{build}}(p) Rightarrow F_{mathrm{shape}}(p).
]
Adding `F_shape` as another premise of an implication already requiring this specific `A_build` does not strengthen it. **Therefore this naive pair is redundant in the scoped fixture.** This does *not* mean F is universally redundant, because a weaker compilation predicate or other dependency graph may not include the provider assertion.

Trying to repair this by defining (F_{mathrm{semantic}}) as “the provider produces the demanded output” risks **duplicating D**, the independent new-client goal fulfillment predicate. A legitimate future F must be framed with independent, testable **provider capabilities and dependency choices that are not a mere renaming of D**.

Likewise `C_currentAdmin` or one observed historical merge event is not a substitute for `C_permittedAtRevision` on arbitrary edits; the branch-protection policy applicable at other revisions is unavailable. This fails the time-indexing and legitimate-authority obligations and cannot support a broad conditional SOLID theorem.

[P41InformationMinimality.lean](../../tools/p41/lean/P41InformationMinimality.lean) implements a direct adversary to artificially long premise lists: a seventh guard defined to duplicate A is logically eliminable. The file also encodes provider source/type projection and current-admin-versus-past-rights countermodels. **These are classical, restricted proof models; none is a kernel-verified implementation of actual Go or GitHub’s complete permissions engine.**

## 4. A–F elimination matrix, with forced missing-evidence labels

| Candidate | One bounded necessary-information result | Obstacle to Level III irredundancy |
| --- | --- | --- |
| A: type/compile | missing Echo `Route` interface method fails original compilation | defining F as interface shape makes it redundant with strong A |
| B: old-client observation | headers/hidden effects can differ despite accepted source | all-context observational preservation untested |
| C: revisioned edit rights | current authenticated admin and one independently verified real historical merge actor/commit | historical protected-branch policy and edit-specific normative legitimacy unobserved |
| D: goal/route identity | same coarse HTTP response hides wrong selected Echo route | full goal compatibility and context population not fixed |
| E: source admission | real chi mount and httprouter structural collisions absent from type-only theory | source admission alone not sufficient for B/D; minimal model of E still context-dependent |
| F: capability/provider | original Echo ports enforce typed structure, but two conforming providers behave differently | (A_{m build}) subsumes (F_{m shape}); (F_{m semantic}) risks collapsing into D |

**No entry in this table qualifies as a universal independent OO axiom merely by having a source example.**

## 5. Strongest classical contender remains adequate

- Standard **structural typing** explains the rejection of incomplete Echo provider.
- **Behavioral refinement and contextual equivalence with an appropriately rich observer** explain why a type-correct substitute can fail the client contract.
- **Information-theoretic factorization and state abstraction** explain why lost route identity and versioned authority cannot be recovered from smaller views.
- **Parnas 1972 information hiding** motivates stable change boundaries.
- **Liskov–Wing 1994 behavioral subtyping**, **Reynolds/Separation Logic**, **capability-based authorization** and **rely/guarantee** remain applicable.
- **CSP terminology:** P40’s admission scorer uses *constraint satisfaction problem* source conditions, not automatically Hoare's *Communicating Sequential Processes*.

**The best classical explanation survives every independently checked P41-P1 counterexample.** Existing source evidence discriminates against weak baselines (type-only/response-only) but does not falsify the strongest contextual, source-aware classical model.

### 5A. Verified primary classical rivals

- [Liskov & Wing, *A Behavioral Notion of Subtyping* (TOPLAS, 1994)](https://doi.org/10.1145/197320.197383) already defines subtype adequacy by preserving the properties visible to appropriately typed clients. Type shape alone is a deliberately weak straw competitor.
- [Abadi & Lamport, *Conjoining Specifications* (TOPLAS, 1995)](https://www.microsoft.com/en-us/research/publication/conjoining-specifications/) emphasizes how an environment assumption and a system guarantee must be coordinated across temporal behaviors. Our present GitHub role snapshot is NOT a temporal rights logic and cannot defeat such a competitor.
- [Krebbers, Timany & Birkedal, *Interactive Proofs in Higher-Order Concurrent Separation Logic* (POPL, 2017)](https://doi.org/10.1145/3093333.3009855) reinforces that classical higher-order separation-logic proof systems can express rich resource/ownership reasoning. P41 cannot present an independent “authority coordinate” as proof that prior ownership logics lack expressive capacity.

These are **competing established theories**, not citations proving P41's empirical outcomes. The original Go and GitHub source cases are the outcomes.

## 6. Next irreversible scientific gate

1. Obtain **historically versioned, authentic permission/approval evidence** for a real edit, not current repository role alone. Privacy and third-party rights must be respected, and lack of access must remain UNKNOWN, not false.
2. Develop source-realized **dependency graph countercases** with a provider capability tested independently of output-D, optionally compare bound import/export contracts against call-time behavior.
3. Specify the observer class and source edit grammar **before** obtaining new test outcomes; compare conditional OO theory with source-aware classical CSP/frame/refinement using exactly the same information budget.
4. For each proposed minimal axiom, demand a **noncircular external outcome** not definitionally identical to the conjunction of premises, a kernel proof, and a genuine original-source omission witness. Record nonidentifiability and classical collapses as valid negative outcomes.

**P41-P1: bounded independent C platform/F source evidence completed, broader C/F OPEN. P41-P2: first negative irredundancy/observer sufficiency court complete only after standalone Lean kernel PASS at a tested HEAD; comprehensive A–F axiom minimality OPEN. Historical SOLID total reconstruction OPEN. New fundamental OO law HOLD. LAW-R2 NOT_AUTHORIZED.**
