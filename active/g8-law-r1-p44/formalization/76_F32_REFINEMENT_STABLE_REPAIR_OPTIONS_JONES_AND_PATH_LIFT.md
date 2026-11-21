# P44-F32 — Refinement-Stable Repair Options: Exact Finite Path-Lifting Lemma and a Failure Witness

**2026-11-09. Research branch only. C3-MODEL, NOT a new theorem of programming languages, NOT a source extraction result, NOT LAW-R2.**

## A. Revisited original Jones 1983, precise source and chronology

Verified primary original held at [central Drive 10_PAPERS](https://drive.google.com/file/d/1bXdGFS9dqgBPWtJWEjcjzWH_lXJUsm94/view). C. B. Jones, *Tentative Steps Toward a Development Method for Interfering Programs*, ACM TOPLAS 5(4) 596–619 (1983). Specifically §3.3 printed p.612 eq (3.39)-(3.40): an abstract minimum \`min(et,ot)\` may be nonincreasing while the more restrictive refined rely clause \`et'=et AND ot'<=ot\` is not implied. Counterexample \`(et,ot)=(5,5)\`, \`(et',ot')=(4,5)\`: min changes 5→4 so abstract monotonicity holds, but et changes, refuting the refined reliance. The text explicitly says the proof of coexistence must be repeated after refinement because representation-dependent properties could not be formulated at the abstract level.

At printed p.606 §3.2 eq (3.7), Jones already demands guarantee-to-rely compatibility, plus the dynamic invariant, environmental stability and postcondition rules (3.9)-(3.13). §3.4 printed pp.614–615 partitions changes between root/body effects; all of these are PRIOR ART against a newly invented 'SOLID's first mathematical modularity theory' story.

Further Jones monograph **not yet held in central Drive exact-title search**: C. B. Jones (1981), *Development Methods for Computer Programs Including a Notion of Interference*, Oxford Computing Laboratory Technical Monograph **PRG-25**, 257 pages (Oxford catalogue https://www.cs.ox.ac.uk/publications/publication3768-abstract.html), official open [full original PDF](https://www.cs.ox.ac.uk/files/9025/PRG-25.pdf). This pre-dates the 1983 article and is especially important for mathematical and semantic priority. Merely locating the PDF publicly is NOT a Drive-held original or completed 257-page reading.

## B. The research object, with all quantifiers

Let \`A=(S_A,E_A,O_A,s_A)\` be a **complete declared finite** abstract version graph. Let \`C=(S_C,E_C,O_C,s_C)\` be a **complete declared finite** concrete version graph. Each directed edge is labelled \`(actor, demand_event, nonnegative_integer_cost)\`, and each state has an old-client observation string. Fix a total representation map \`α:S_C→S_A\` mapping initial states.

Required certificate conditions:
1. Old-client observation fidelity: for all c, \`O_C(c)=O_A(α(c))\`.
2. **Projection (forward):** each concrete edit \`c --(actor,d,cost)--> c'\` projects to an abstract edit \`α(c) --(same label)--> α(c')\`.
3. **Universal concrete path lifting (backward):** for **every** concrete representative c and **every** abstract edit \`α(c) --label--> a'\`, some admitted concrete edit \`c --same label--> c'\` exists with \`α(c')=a'\`. This is an existence condition for each concrete representative, not merely one representative per abstract state.
4. Every edge in both graphs is assumed correctly enumerated. Actor claims, completeness, source/build identity and cost semantics are **external unproved premises**, not established by a caller-supplied graph.

### F32 two-way cost preservation (classical result)

For every finite word w of **demand event labels**, the shortest exact-labelled edit-event path cost starting at initial states is equal:

\`\`\`
Cost_C(s_C,w) = Cost_A(s_A,w)
\`\`\`

where both sides are infinity if impossible (the executable court uses a sentinel). The result preserves actor labels at matched edges and per-edge prices; the public query currently fixes demand labels only, so it computes the least over permissible actors in each declared graph. It does **NOT** by itself prove that previously satisfied *state predicates* remain true: F27's stagewise persistent-goal condition must be added before using the equation for sequentially durable customer demands.

**Proof:** For any concrete w-path, forward projection produces an abstract w-path of identical edge costs; taking minima gives \`Cost_A <= Cost_C\`. Conversely take an abstract w-path and initial concrete representative. Inductively apply condition 3 for each abstract edge, obtaining a concrete w-path of identical prices; hence \`Cost_C <= Cost_A\`. An absent abstract or concrete path yields absence in the other by respective projection/lifting. Both inequalities yield equality; infinite/nonnegative-cost search is exact on finite tables. This is classical strong labelled bisimulation / a graph bounded-morphism lifting argument, not a new categorical discovery.

### Why 'source build passes, client observer unchanged' is insufficient

In synthetic countermodel \`A\` costs 1 and changes an invisible right/permission flag from open to closed, while old-client observable \`old\` remains identical and the abstraction maps both to \`x0\`. The abstract graph has \`A:x0→x0 cost1\`, \`B:x0→x1 cost2\`, so \`[A,B]\` costs 3. Concretely B is available from open, not closed. After A, B cannot be performed: concrete \`[A,B]\` cost infinity despite matching observations and individually possible A/B edits. The forward projection is valid, yet the backward **representative-specific** B-lifting obligation fails at \`closed\`. There is an exact diagnostic \`CounterWitness{ConcreteState:"closed",AbstractState:"x0",AbstractEdge:(b-owner,B,2,x1)}\`.

This is a synthetic rights-state counterexample, not an observed repository permission revocation, not a claim that real maintainers' rights changed.

## C. Executed reproducibility and hard controls

Module [\`f32_refinement_lift\`](f32_refinement_lift/README.md), Go1.23.2, \`go test -count=1 -v ./...\`, \`go vet ./...\`, \`go test -race -count=1 ./...\`. Local results **11 top-level tests pass**. Check rejects absent/incomplete finite state tables, invalid/negative cost, absent abstraction mappings, observation mismatch, wrong actor or price, cost overflow. It returns HOLD for unverifiable two-way claims, not "no repair possible."

**Exhaustive court:** all \`2^8=256\` edge subsets over two concrete states, two possible edit labels, two targets; abstract baseline has one state with both self-loops. Exactly **81 graphs** satisfy strong two-way obligations. For those 81 models, both concrete starting states and all \`1+2+4+8=15\` event words of length 0–3 were checked against the abstract model: **81×2×15=2,430 comparisons**, all equal. This is a finite test, not mathematical proof of all graphs (the paper lemma supplies that proof); the exhaustive distribution also depends on the explicitly defined finite test universe.

**GitHub original-source CI** [#42563037683](https://github.com/WhoSia/EvoNOMOS/actions/runs/42563037683) completed SUCCESS, original logs inspected: 11 top-level PASS lines, including witness and exhaustive court, vet and race. No original Go implementation source analysis is performed by this checker.

## D. Relation to original SOLID superstructure ambition

Proposed *research mathematical representation* is a projection of the category/graph of concrete, actor-authorized, costed, client-preserving source edits onto a graph of abstract interface-level changes. **Safe abstract future edit options must lift in EVERY concrete implementation of that abstract state.** A one-way abstraction is insufficient. This suggests a fiber-indexed *repair option lifting* requirement.

It is **not automatically a Grothendieck (op)fibration**: that term requires additional opcartesian/universal properties beyond mere existence of graph-edge lifts. A standard two-way simulation / p-morphism already proves the finite theorem. The genuine unsolved research opportunity is a small sound certificate that demonstrates these lifts from actual source edits and independently authenticated rights, and whether this improves prospective reasoning against equally informed conventional bisimulation, CEGAR, effect, alias and rely-guarantee baselines.

Conditional connections:
- SRP: if edits lift and independently commute, responsibility decomposition is stable; lifting ALONE does not prove commutation.
- OCP: an abstract extension option is actionable for a concrete codebase only if its protected, legal source edit can be lifted.
- LSP: runtime contextual refinement is separate from whether future source-version edits can lift.
- ISP: an observer projection can preserve current observations but erase repair-relevant permissions; projection adequacy is relative to the future question.
- DIP: abstraction through a port requires source-level realizability of the port's anticipated modifications; its existence does not follow from static interface types.

## E. Promotion gates

The needed experiment is **actual source/build/right/observer/cost evidence for concrete graphs** plus a held-out customer demand stream with the prediction sealed before independent outcomes. This research has no such C5. Traditional weighted bisimulation receives the *same complete graphs* and must tie exactly. A source-aware CEGAR tool would detect the counterexample if it knew the hidden permission state. Therefore: **METHOD/FORMAL COURT progress only, no novel theorem priority, G1–G7 OPEN, LAW-R2 HOLD; PR #13 Draft/unmerged.**
