# EvoNOMOS P42 R11-P10-P5 — Relative Effect-Repair Abstraction and Genuine Source Proof Obligations

**2026-10-17. P42 RUNNING; R11-P10-P5 BOUNDED. P43 HOLD; LAW-R2 NOT_AUTHORIZED. This is not a new universal SOLID law.**

## Problem and prior art

We want a source-derived mathematical structure in which conditional versions of SRP, OCP, LSP, ISP and DIP are consequences, not axioms. The starting objects are concrete source histories, independently protected client observations, authorized edits, event/resource traces and edit cost vectors. HARC R11-P5 already proves scoped SOLID implications under these premises; P10-P5 addresses the missing source-to-theory proof obligations.

The core may/must structure is **classical abstract interpretation**: Cousot & Cousot (1977), Abstract interpretation: a unified lattice model for static analysis of programs by construction or approximation of fixpoints, POPL, DOI 10.1145/512950.512973, https://doi.org/10.1145/512950.512973 . Costed bisimulation and partition refinement are also classical. Their reuse is not independent theoretical priority.

## 1. Concrete semantics before architecture judgments

Fix a transition system S with state containing source P, dispatch/linking L, runtime resources R, owner-rights evidence G, protected clients C and versioned history H. A client c specifies an admitted trace language over declared observable actions, including optional method assertions or underlying transport events if the client can observe them. A future demand d specifies a goal predicate independently of the repair candidate.

An actual edit path is legitimate only if every transition has proven authority, executable source transformation, stagewise old-client preservation and a declared nonnegative vector cost in R^k_+. Let K(s,d) be the set of costs of all finite legitimate goal-reaching repairs, and F(s,d)=ParetoMin K(s,d). Unknown ownership must yield UNKNOWN rather than authorize a hypothetical source edit. No SOLID axiom or preference is in these definitions.

## 2. Relative soundness theorem P5-R1: may/must repair bounds

Let K_MAY overapproximate concrete authorized repair costs and K_MUST be actual costed repair witnesses. **Hypotheses:** K_MUST is a subset of K, and K is a subset of K_MAY; the same concrete cost units and goal language are used in all three, or declared abstraction inequalities correctly translate them.

**Theorem:** For all nonnegative weight vectors w, with opt_w(K)=inf {w dot c : c in K} and inf empty=positive infinity,

  K_MUST subset K subset K_MAY,
  opt_w(K_MAY) <= opt_w(K) <= opt_w(K_MUST).

**Proof:** Set inclusion reverses the infimum order on the extended nonnegative real numbers. This says nothing false about Pareto-frontier set nesting. QED.

A forward source-to-abstract simulation preserving each legitimate edit and cost suffices for the may inclusion; a certified backward path-lifting/witness mechanism suffices for must inclusion. Exact cost-frontier equality follows if both directions cover the same costed paths. An unverified transition relation or missing source-owner right does not satisfy the hypotheses. A may path can be spurious, and must cannot consist of hypothetical upstream edits.

This is a **classical** theorem, used as a discipline for source extraction, not a new design principle.

## 3. Automatic derivation from authentic Chi #1185 source

[Freeze of extraction contract, before extractor source](https://github.com/WhoSia/EvoNOMOS/commit/43b906a629e0ba8df22ea85a47067453a9d1c2d4). [Source AST extractor](../../tools/p42/p2-r11-go/p10_p5_chi_source_effect_obligations.go). Original Chi at commit b1c9ab47626cc46b34393ad4d35779c4363c4e1e and merged actual contributor source at 9b3e51c349f3fa6cf120ae786a2835e89e81da2e, both original file Git blob IDs pinned.

[Original-source AST CI #39020588686 PASS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39020588686): old source contains four direct underlying Flush implementations, merged source contains four delegate calls to a single helper and the helper tests !b.discard before forwarding the transport Flush event. The typed Go AST and exact source identities are authenticated. This is syntax evidence, NOT an automatically proven whole-Go semantic trace equivalence.

The extractor emits seven required but UNDISCHARGED proof obligations: G1 dynamic receiver and interface type resolution; G2 concurrency/alias stability of discard state; G3 completeness of executable dynamic Flush call graph; G4 effects of maybeWriteHeader and resource/event bookkeeping on clients; G5 completeness of the protected observation language; G6 independent evidence of edit permission over third-party source; G7 staged source validity and real edit-cost certification. No global proof may be labelled PASS while any required G1–G7 is open.

## 4. Relative factorization theorem P5-R2 and actual effect failure

**Theorem:** Suppose q(s)=q(t) but some protected event e distinguishes s from t. Then no function f on quotient states computes this event observation on both states, since e(s)=f(q(s))=f(q(t))=e(t) would contradict the witness. QED.

For Chi #1185, the existing independent actual native source court #39019814512 verifies that before and after the real merged change both expose the same tested outer Go wrapper and http.Flusher method set, the same selected HTTP status/body/byte counters, but with Discard the original forwards underlying Flush and the merged change suppresses it. Thus a method-set-and-selected-HTTP-output abstraction is insufficient for that particular event language. This is ordinary contextual/effect semantics, not a new theorem priority.

## 5. Classical finite relative may/must check

[Finite source/effect model](../../tools/p42/p2-r11/p10_p5_relative_may_must_repair_sandwich.py) uses the eight authentic native-tested Chi source/revision x Discard x invocation observations, doubled with a distinctly **hypothetical** ownership bit to yield 16 model states. That extra bit MUST NOT be interpreted as authorization to edit Chi's maintained upstream repository.

[Finite CI #39020916896 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39020916896): forgetting source revision merges states with distinct transport events; an optimistic may quotient can falsely suggest zero-edit feasibility. A quotient preserving source revision, discard and the synthetic edit-right bit forms a strong cost-labelled bisimulation for THIS finite event model, while the unimportant tested invocation mode is safely omitted. The checker validates the may/must cost-set sandwich in all 16 model states. It does not verify all Go executions or source-owner rights.

## 6. Two independently maintained real source frameworks, identical predeclared new client contract

[Common source-conditioned future-demand freeze 0cbf1b08](https://github.com/WhoSia/EvoNOMOS/commit/0cbf1b080c5dbc9735f67dd81fec35101427e131) predates both new native test implementations.

Actual maintained independent historical sources: Gin commit d3ffc9985281dcf4d3bef604cce4e662b1a327a6; Echo commit 86d0223c7aa39b865a9452de3479897fcb5a3939. Both check their exact originally pinned source blob, and are NOT edited.

The new RESEARCH-AUTHORED client contract (not a previously unseen third-party PR) requires GET /capability -> 200, body probe, header X-EvoNOMOS-Underlying-Flusher=present/absent exactly reflecting whether the unwrapped underlying actual writer implements http.Flusher; it must not actually Flush; old GET /old stays 200/old. Writers include standard Flusher-enabled ResponseRecorder and research-owned basic-interface-only wrapper.

Only author-controlled application handlers are legitimate edit locations. E0=no edit has normalized synthetic cost (0,0); E1=one app handler edit has (1,1), where the second unit is merely a placeholder review token, not measured labor. The predeclared source-conditioned prediction: in both frameworks E0 fails because no /capability route exists, E1 meets the contract and protects tested old clients. Therefore within this exact grammar F={(1,1)} for BOTH.

[Independent source native CI #39020790152 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39020790152): both Gin and Echo with actual historic source passed both writer classes, old-client preservation, no transport Flush, E0 negative and E1 positive controls. This certifies user-owned test/handler mutation, **not** rights to change either upstream framework. The strongest equal-information classical cost-labelled LTS also predicts F={(1,1)}: **2/2 ties**, zero unique HARC advantage. The historical source was read before demand freeze, so this is a pre-native research-authored demand, not unseen external PR forecasting.

## 7. Conditional SOLID implication: what is still mathematically missing

The actual dependency is:

  verified source effect + client observation + stagewise edit rights
     -> simulation/lifting obligations for repair paths
     -> admissible source/port factorization and repair frontier bounds
     -> conditional separation/extension/substitution/segregation/inversion corollaries.

These are the hypotheses under which limited SRP/OCP/LSP/ISP/DIP results already proved by HARC R11-P5 survive. Neither a syntax-only interface boundary nor naming a class an abstraction is a legitimate substitute for rights- and effect-complete source semantics.

**Highest-value mathematics next:** establish a compositional, capability-and-effect-indexed source calculus for a precisely bounded Go subset that discharges G1–G5 from actual source semantics and isolates explicit G6/G7 certificates. Prove a forward simulation composition theorem and a separate backward edit-path lifting theorem under independently stated framing and owner-right rules. Then attempt truly unseen semantically matched third-party requirements against the strongest classical competitor; abstain when contracts/rights differ.

**P42 RUNNING · R11-P10-P5 BOUNDED: AST-OBLIGATION, FINITE MAY/MUST, MATCHED NATIVE CLIENT COURTS PASS; GLOBAL SOURCE-REPAIR SIMULATION AND NOVEL LAW NOT ESTABLISHED · P43 HOLD · LAW-R2 NOT_AUTHORIZED.**
