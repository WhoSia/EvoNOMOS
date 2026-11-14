# P44-F32 — Directional Cost Certificates, Refined Permission Countermodel and Source-Versus-Theory Prior Art

**Date 2026-11-09. This is a proof-contract improvement to an elementary classical finite graph model, NOT a newly discovered law and NOT source-level rights verification.**

## 1. Two proof directions are not interchangeable

Let C be a finite complete graph of legally admitted **concrete** version-edit events and A a complete abstract graph. Each edit has a named actor, a demand **event label**, and nonnegative integer cost; observation is checked at each state; α:C.states→A.states is total and preserves the initial state. Let K_C(w), K_A(w) be minimum cost of the EXACT event sequence w, NOT yet persistent state-goal satisfaction.

- **Forward projection**: every concrete edge projects to an abstract edge with IDENTICAL actor/demand/cost label. Thus every concrete w-path maps to an abstract w-path of the same cost. Consequently **K_A(w) ≤ K_C(w)**; K_A is a certified *lower bound*. If no abstract w-path exists, no concrete one can exist under the declared complete graph. An abstract path's existence **does not** prove concrete feasibility.
- **Backward representative-wise lifting**: for every concrete state c and every abstract edge outgoing from α(c), a concrete edge outgoing from c with identical actor/demand/cost exists and maps to the same abstract destination. Inductively an abstract w-path lifts from ANY relevant concrete representative; hence **K_C(w) ≤ K_A(w)**, giving a constructible *upper bound* under the declared graph. It says nothing about concrete paths absent from the abstraction, so not generally a lower bound.
- **Both directions** yield equality **K_C(w)=K_A(w)** for every finite word w, a standard weighted bisimulation/bounded-morphism argument.
- **Neither** → HOLD. A failed check is neither proof that a real repo has no safe edit nor proof of a missing permission; only the supplied graph contract is being examined.

## 2. Operational classification (real execution)

The executable \`f32_refinement_lift/lift/polarity.go\` reports one of:
\`SOUND_COST_LOWER_BOUND_ONLY\`,
\`CONSTRUCTIVE_COST_UPPER_BOUND_ONLY\`,
\`EXACT_COST_EQUALITY\`,
\`HOLD_INSUFFICIENT_PATH_RELATION\`.

Receipt grade is deliberately \`FINITE_GRAPH_POLICY_AND_SOURCE_UNATTESTED\`. Both directions separately verify total map, same original client observation and complete declared graph tables. \`BoundForWord\` returns the abstract cost and boolean claims **LowerCertified/UpperCertified**. Its result is NOT a promise that full real-world rights and all Go source transitions have been enumerated. The finite engine uses \`math.MaxInt\` as an unreachability sentinel, so any route whose true total cost equals that extreme needs an amended representation before claiming full generality; ordinary unit-cost court stays well below the sentinel.

### Four independent tests, not a fake empirical lift
- **Lower only:** hidden-right countermodel. Abstract \`[A,B]\` cost 3; concrete implementation with A closing a hidden editor gate has no B after A (infinite cost). Projection holds, lifting fails.
- **Upper only:** concrete graph contains A and additional B edit, abstract graph contains only A. Every abstract edit lifts, but the concrete B has no abstract image. This demonstrates that no abstract B-path **does not** imply real B-impossibility under upper-only evidence.
- **Exact:** both graphs contain matched A edit and no extra edits.
- **HOLD:** missing abstract representation of a concrete additional event *and* missing concrete witness of an abstract event.

Local Go 1.23.2 tests pass, including 256 enumerated 2-state graph cases (81 two-way-certified models, 2,430 word comparisons). Current original GitHub CI requires independent completion/readback; DO NOT propagate an older pre-polarity run as the new test receipt.

## 3. Why this matters to SOLID without inflating novelty

Design principles are not axioms that uniquely determine all future edit paths. Different levels of available evidence authorize **different types of claims**. In particular:
- An ISP-style observable projection may be adequate for today's clients and yet erase the future editor capability/rights state. One cannot infer OCP-style future extensibility from runtime equivalence.
- A source/port abstraction may supply a safe lower estimate, but **not a repair construction**; to claim extendibility requires a concrete edit witness. This distinction is useful for auditable maintenance decisions.
- SRP-like noninterference/commutation is stronger still; neither a one-way simulation nor exact event-path cost equality ALONE proves independent edit commutation or persistent state-goal preservation.
- LSP's contextual execution refinement remains separate from maintenance edit-graph lifting; DIP's stable type boundary similarly does not establish source edit realizability.

The mathematics of simulations/abstract interpretations, automata bounded morphisms, refinement and CEGAR already provides these proof polarities. **Novelty is at most a proposed integrated software maintenance certificate:** source+build exact closure, independently authenticated editor rights, prospective staged demands, exact repair witnesses and matched-information verification-economy study. C3 model court, NOT law.

## 4. Central primary literature and a newly exposed original

**HELD** Jones (1983), *Tentative Steps Toward a Development Method for Interfering Programs*, 24 pages, central Drive ID \`1bXdGFS9dqgBPWtJWEjcjzWH_lXJUsm94\`; direct pp.605–615 reading verifies (3.7) rely–guarantee and critical (3.40) nonimplication on representation refinement. Jones's historical example is about runtime interference under data refinement, NOT about modern owners of source-version edits; analogy must be explicit.

**NEW MISSING SOURCE:** C. B. Jones (June 1981), *Development Methods for Computer Programs Including a Notion of Interference*, Oxford University Computing Laboratory technical monograph **PRG-25**, **257 pages**. Exact Oxford institutional record https://www.cs.ox.ac.uk/publications/publication3768-abstract.html; freely discoverable original PDF https://www.cs.ox.ac.uk/files/9025/PRG-25.pdf. Exact title searched in central Drive; only the distinct 1983 article returned. Thus official full text FOUND ONLINE but original **NOT HELD** in central Drive. This source predates the 1983 paper and must be read before a priority claim for a formal theory above SOLID. Do not infer complete reading from the Oxford catalogue.

Other current missing exact originals unchanged:
- O'Hearn, Yang & Reynolds 2009, *Separation and information hiding*, DOI 10.1145/1498926.1498929; note a separate earlier 2004 conference version exists, DOI 10.1145/982962.964024. They must NOT be automatically recorded as the same edition/document.
- Stephen Brookes 2004, *A Semantics for Concurrent Separation Logic*, DOI 10.1007/978-3-540-28644-8_2.
- Baldwin & Clark 2000, *Design Rules, Vol. 1: The Power of Modularity*, DOI 10.7551/mitpress/2366.001.0001.

## 5. Exact research stop and next promotion test

Candidate next experiment: independently frozen real repository/source tree; authentic maintainer edit authority and matching target build; extract complete bounded edit witnesses and compute conservative forward/lifting polarities against equal-information classical SSA, source slicing, context-based rely–guarantee and CEGAR. Hold out future independently authored demand and outcome, freeze model and comparison baselines prior to outcome. Neither F32 graph results nor Jones 1983 constitute prospective source prediction or classical-baseline superiority.

**G1–G7 OPEN · LAW-R2 HOLD · PR #13 Draft/unmerged.**
