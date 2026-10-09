# G8 LAW-R1-P33 — Demand-Relative Interface Quotients and a Conditional Mathematical Reconstruction of SOLID

**Research mode change (2026-10-09):** Interpretive formalization with rigorous attribution is a **legitimate publication contribution**, even where the mathematical result is classical. Novel universal theorems or H>B0+/B1/B2 forecast wins are *optional enhancements for this interpretive strand*, not prerequisites for recording a coherent P33 theoretical advance. Never misattribute prior results, assert false generality, or promote a toy model to empirical universal law. P33 stays OPEN / LAW-R2 NOT_AUTHORIZED.

## 1. Prior literature and interpretive program

A plausible contribution is the integrated mathematical **reading** of SOLID: its principles as partially independent statements about *observability, behavioral contracts, change authority, and extension costs* for an explicitly chosen **family of future requirements**. This is not a claim that the original acronym was originally expressed in these exact terms.

- [Parnas (1972), modular decomposition and information hiding](https://drive.google.com/file/d/1EcQRy3iehx4lUN7uGsZ1BFXU33HggcEQ/view): dependency boundaries are a response to change, not just file count.
- [Parnas (1979), extension and contraction](https://drive.google.com/file/d/1XGzB9hq_6wk6aXeVojMo1IeKoKCg704j/view): structural extension is an architectural design objective with scope.
- [Sullivan, Griswold, Cai & Hallen (2001), modularity and real options](https://drive.google.com/file/d/1Gyt45QSE3T0RIiivwVIiw4ofxemxLXfr/view): economic valuations of change and a Parnas/KWIC translation predate P33.
- [Tishby, Pereira & Bialek (1999; arXiv version 2000), Information Bottleneck](https://drive.google.com/file/d/1uXpPVCT6VKCtbJITUsMfyPZAOX9odYgj/view): lossy compression preserving task-relevant information is existing information theory. Do not identify deterministic exact quotienting with the stochastic information bottleneck without an explicit probabilistic optimization problem.
- Reiter (1987), SemFix (2013), DirectFix (2015), Angelix (2016), Smith et al. (2015), Guigue (2014) originals are canonical in 10_PAPERS (P33 six-paper court). Repair synthesis, set-valued control and diagnostic antichains are established strong foundations.

The writing contribution is a **faithful conditional map with proofs and counterexamples**, not a new proof of an old function-factorization fact.

## 2. Definitions — finite exact-behavior core

Fix a set X of relevant source/application states, demand index set D, total deterministic requirement functions g_d:X→Y_d, and a chosen module or plugin's accessible observation interface o:X→Z. These assumptions are **not** general OO semantics, which may have nondeterminism, side effects, errors, trace-sensitive effects or concurrent actors.

Define x ~_D y iff for every d∈D, g_d(x)=g_d(y). Let q_D:X→Q_D = X/~_D be the quotient. Let ker(f) = {(x,y):f(x)=f(y)}.

**Theorem 1 — Minimal sufficient demand quotient (classical factorization).**
All requirements in D can be implemented by some deterministic functions h_d of the *existing* observation o alone iff

    ker(o) ⊆ intersection_{d∈D} ker(g_d) = ker(q_D).

When it holds, each g_d=h_d∘o on im(o). Moreover q_D=t∘o for some t defined on im(o). Thus q_D is a **coarsest sufficient** interface representation for exactly the chosen demand family, unique up to relabeling of its image; any sufficient o has at least as many reachable observable equivalence classes as q_D.

Proof. If h_d exists, equality under o forces equality under g_d. Conversely, whenever o(x)=o(y), the kernel containment forces g_d(x)=g_d(y), so define h_d(z)=g_d(x) using any x with o(x)=z. The definition is independent of x. Apply this to every d, including q_D. This is elementary equivalence-relation/function factorization, **not a newly established general theorem**.

**Corollary 2 — Demand enlargement (classical lattice property).**
For D⊆E, ker(q_E)⊆ker(q_D). Adding requirements makes the minimal sufficient contract at least as discriminating, even though its *API declaration count* need not increase. For union E=D∪F, ker(q_E)=ker(q_D)∩ker(q_F).

**Corollary 3 — A bounded, conditional OCP criterion (interpretation).**
Suppose the only permitted change on adding d is a new deterministic downstream decoder h_d operating on *the existing fixed* observation o, with no fresh side channel, data read, retraining, altered contract or changed upstream states. Then the new demand can be added without altering the information boundary iff ker(o)⊆ker(g_d). Failure provides x,y with the same visible input but different required outputs, certifying impossibility **for that restricted extension mode only**. This is *one exact mathematical reading of OCP*, not a universal necessary/sufficient theorem for OCP in arbitrary software.

## 3. SOLID as five conditional design interpretations

| Principle | Proposed P33 formal reading | What this does NOT prove |
|---|---|---|
| S — Single Responsibility | Assign owner modules to **coherent demand-change axes**; identify a 'reason to change' using explicit stakeholder/demand classes and obligation interventions rather than raw method count. | The quotient theorem itself neither determines organizational reasons nor proves one-class-per-module yields lowest lifecycle cost. |
| O — Open/Closed | A fixed boundary o is **open to a demand class** D precisely when all target functions in D factor via o *under a downstream-only decoder extension grammar*. | Real extension may legitimately add upstream information, registry sites, runtime injection, and test changes; an open system need not be closed under all imaginable requirements. |
| L — Liskov Substitution | A replacement must refine/preserve the complete **client-observable behavioral contract** (including specified errors, state transitions, and traces) on D. For deterministic pure subcases this reduces to output equality; for nondeterministic implementations refinement/inclusion requires an explicit trace semantics. | Finite examples or equality of a single output field do not certify universal LSP; demanding literal equality of all implementation internals is too strong. |
| I — Interface Segregation | A consumer's ideal task-relative contract is q_D, the **coarsest sufficient observable distinction**. Avoid exposing or forcing capabilities unrelated to its D. | Not a literal rule about number of interface methods, and not proof that exact minimal interface is always cheapest to implement/maintain. |
| D — Dependency Inversion | Depend on a stable **abstract behavioral quotient/contract**; concrete representations can vary while implementing the same D-relevant observation and maintaining refinement. | Quotient equivalence does not imply dependency direction or compile-time decoupling by itself; inversion requires an actual ownership/port mechanism. |

These readings are **jointly coherent but not all logically equivalent**: S depends on organizational/demand axis assignment, L needs trace/refinement, O/I use factorization, D additionally constrains dependency authority/ports. Treat that separation as intellectual clarity, not a failure of SOLID.

## 3A. Conditional SRP economics: a small, cited model, not a universal commandment

An organizational "reason to change" is not automatically a mathematical independence class. To illustrate *when* separating two responsibility axes can be justified, stipulate change events A and B with marginal probabilities p_A, p_B, and joint probability p_AB, one grouped owner's expected edit touch cost c_g, two separated owners' touch costs c_a,c_b, amortized fixed split cost k≥0, and a **hypothesized** within-module cross-reason interference surcharge λ≥0 paid only when exactly one axis changes.

Then the modeled expected costs are

    C_group = c_g (p_A + p_B - p_AB) + λ(p_A+p_B-2p_AB)
    C_split = c_a p_A + c_b p_B + k.

For q=p_A+p_B−2p_AB>0, the separated design wins in this *specific model* exactly when

    λ > [c_a p_A+c_b p_B+k−c_g(p_A+p_B−p_AB)] / q.

Proof: algebraic rearrangement of C_split<C_group. If q=0, the interference term cannot favor separation at all. This is a **conditional accounting identity** built from assumed costs, not a new optimization theorem and not an experimentally estimated general SRP rule. Its value is to show why "one responsibility per class" may or may not lower expected maintenance cost.

Example: independent change probabilities p_A=p_B=.2, p_AB=.04; normalized edit touch costs all 1, k=.03. Then C_group=.36+.32λ and C_split=.43. Separation is favored iff λ>.21875; at λ=.1 grouping wins; at λ=.3 splitting wins. [Finite checker](../../tools/law-r1-p33-demand-quotient.mjs) asserts both cells.

This connects Parnas information hiding, Sullivan et al. modularity real-options, and the exact-demand interface quotients into a single conditional research story: **SRP depends on change distribution and interference cost; ISP/OCP depend on observation sufficiency.** Neither one subsumes the other, nor does this scalar illustration replace P33's vector/Pareto continuation analysis.

## 4. Source-rooted bridge to P33

Pinned Uptime Kuma certificate context uses an unescaped `[name][url]` message. Different (name,url) states can have identical encoded messages, so the decoder interface violates ker(o)⊆ker(g_name,url) for an exact-context demand. Existing template-message decoder cannot recover distinctions hidden by the encoding alone. The candidate caller-side repair adds a structured context channel, changing o; downstream string parser does not. This **illustrates** the O/I/D interpretation with a real code witness; the issue (#7639) was already known.

Source executable `tools/law-r1-p33-info-cut-repair-world.mjs` and corrected 64-pair execution hosted [37811536823](https://github.com/WhoSia/EvoNOMOS/actions/runs/37811536823) SUCCESS, bounded VM. Caller 64/64 synthetic collision pairs pass; dispatcher 0/64. No full production Q or independent empirical law asserted. The prior hand-labelled cut-site discovery claim remains withdrawn.

## 5. Machine-checked finite sanity tests, not a replacement for proof

`tools/law-r1-p33-demand-quotient.mjs` checks **all 65,536 pairs** of functions g and observation maps o from a four-state domain to a four-label codomain: factorization iff kernel containment. It also checks a two-demand example:

- D={A}: sufficient canonical quotient has 2 reachable classes.
- D={A,B}, independent demands: canonical quotient requires 4 reachable classes.
- Observing only A cannot satisfy B with downstream-only code; observing the joint quotient can.
- Nonidentical interface encodings can have the same demand-relevant kernel.
- An example from the pinned source shows a message collision, and (in hosted workflow) verifies the prior executed repair evidence before computing the finite model.

The theorem is proved mathematically above; 65,536 cases are only test instances, not a proof over arbitrary sets.

## 6. Research conclusion and legitimate writing claim

**Legitimate paper direction:**

*Demand-Relative Interface Quotients: An Information-Theoretic Reconstruction of Conditional SOLID Principles.*

Possible contributions, without a novelty obsession: (1) an explicit shared semantic vocabulary for SOLID that states exactly which assumptions each principle needs; (2) a rigorous classical-factorization derivation of the **ISP–OCP information boundary**, linked to but not identified with stochastic information bottleneck; (3) an account of what remains outside the factorization theorem (SRP institutional change reasons, LSP behavioral refinement, DIP dependency authority); (4) a reproducible real-source case demonstrating why scope and test-domain enrichment matter; (5) a future program for source-guided policy valuation using Guigue/Sullivan, if supported.

A rigorous conceptual/theoretical software-design paper, even one that openly labels its mathematics **known**, is a proper outcome. New mathematical claims and blind predictive wins would strengthen *another sort* of paper; they should not be imposed as universal exit gates on this line. Honest empirical scope and citations are still nonnegotiable.

**P33 RULING:** `P33_CONDITIONAL_SOLID_INTERPRETATION_FORMALIZED__MATH_CLASSICAL__FINITE_SOURCE_BRIDGE__P33_OPEN__LAW_R2_NOT_AUTHORIZED`.
