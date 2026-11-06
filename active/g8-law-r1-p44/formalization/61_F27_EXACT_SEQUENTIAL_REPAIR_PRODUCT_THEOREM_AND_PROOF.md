# P44-F27 — Exact Stagewise Repair-Product Factorization (finite closed model)

**2026-11-06 · theorem and proof · classical product argument · NOT a new universal law.**

## Statement, without SOLID axioms

Let A and B be two *complete finite*, nonnegative-cost, actor/permission-labelled edit graphs. Each state x has a set G_A(x) of **already satisfied** local demands from declared alphabet D_A, respectively G_B(y) from D_B. Let D_A and D_B be disjoint. Existing customers' safety and admissibility are assumed checked at EVERY product state/edge; the abstract graph does NOT verify actual Go source. Only edit moves legal in each owner's local policy are present.

Construct asynchronous product A||B:
- state (x,y); initial (x0,y0);
- demand alphabet D_A disjoint union D_B; satisfaction G(x,y)=G_A(x) union G_B(y);
- every A edit changes only x, leaves y unchanged, retaining A's actor/cost; likewise B;
- no global shared capacity, edit, budget, synchronization, joint contract, or cross-component effects;
- path price is the sum of step prices. Existing obligations remain satisfied at EVERY subsequent edit checkpoint.

For a finite word w of future demands, let K_G(w) be the minimum cost of a path that sequentially acknowledges every demand, while all earlier demands remain satisfied at each edit checkpoint; infinity when no such path exists *in this declared complete graph*. Write projections w|A and w|B to respective declared alphabets.

**F27-PRODUCT theorem:**
```
K_(A||B)(w) = K_A(w|A) + K_B(w|B)            for every w in (D_A union D_B)*,
```
using infinity + x = infinity. This covers demand repetitions and interleavings.

## Proof (two inequalities)

**Lower bound.** Take an arbitrary finite, globally admissible staged path for w in A||B. Project all local A edits and acknowledgements onto A, deleting B edits; similarly project onto B. Because each product edit changes exactly one coordinate and its label, cost and local goals are preserved, each projection is a local legal, stagewise persistent repair path for the corresponding projected demand word. Its local price is therefore >= the corresponding local optimum. Global cost is exactly the sum of projected local costs; hence global cost >= K_A(w|A)+K_B(w|B). If a local task is impossible, a global path would project to a contradiction.

**Upper bound.** Suppose both projected words are repairable. Choose locally optimal finite paths (finite graph, nonnegative integer costs; at least one finite minimum exists). Traverse w stage by stage; whenever its next letter belongs to D_A, execute the next segment of A's local optimal staged plan while holding B fixed, then acknowledge it; analogously for B. Local past obligations remain protected by the local plan, and the other coordinate is unchanged. Therefore every stagewise global checkpoint remains protected. The composed global path costs exactly the sum of both local optima. If either optimum is infinity the lower-bound argument already shows global impossibility. QED.

## What it does NOT imply
- No universal or source-level independence certificate is established just because source modules/classes are separate.
- Costs are additive **by premise**, not a conclusion about engineer-hours.
- Current client observations must factor and be jointly safe; correlated traces, resource/alias effects, and common permissions violate the product assumptions.
- This is a classical asynchronous-product/path projection lemma, adjacent to separation logic, frame rules and weighted automata. Naming it does NOT establish new mathematical priority.
- Original P42 RC1 and P42 conditional SRP already cover related facts. F27 specifically fixes the **all-demand-sequences plus price equality** target to stress-test source extraction and reveal exactly where independence fails.

## Executable artifact
[`f27_repair_product/product.py`](f27_repair_product/product.py) + [exhaustive court](f27_repair_product/test_factorization.py) + [negative tests](f27_repair_product/test_safety.py). Local Python unittest court: 11 tests including exhaustive 64 small graph configurations x 31 words (length 0..4) = 1,984 product/projection comparisons; no original GitHub-hosted CI receipt in this output. Treat independently source-certified complete edit graphs as a separate, OPEN gate. G1–G7 OPEN; LAW-R2 HOLD.
