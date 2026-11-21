# Chat 26 — From 25.md's 2/3/p Distinction to History-Aware Repair Fibers

## Statement reconstructed from 25.md

For a source state \`s\`, chosen observer projection \`o\`, abstraction \`q(s)\`, and enabled source edit \`a\`, the requirement for updating a compact state *without rereading source* is \`q(a(s))=F_a(q(s))\`. Every fiber of \`q\` must be stable under \`a\`: two concrete states mapped together cannot split into different next q-values.

The cycle construction in the archive uses an odd-prime regular rotation action and only two adjacent constrained old observations:
- current observation can be represented with two abstract states;
- direct observation after a known rotation (no need to update q) requires a proper 3-coloring of the odd cycle;
- sequentially maintaining deterministic q under the edit action requires p distinct states (no nontrivial rotation congruence can respect the distinguishable adjacent pair).

The lower bound has **specific** premises: fixed deterministic abstract update, full rotation grammar, no external source reread and stated partial observation. It is NOT a lower bound on generic software architecture cost or human cognition, and the 2/3/p phenomenon has strong automata-prior-art ties.

## Extend to permissions and source history

Let \`H\` be an enriched labelled transition system of \`h=(source,contract,rights,resources,history)\`. A quotient \`q:H→Q\` is sufficient for *all declared finite action words and their old/new observations* if:
1. current declared observation and goal flags are constant on q-fibers;
2. each labelled authorized/editable action's enabledness is constant on q-fibers;
3. each defined labelled successor has a q-value determined by the old q-value.

This is the classical history-erasure congruence theorem already documented in P42-R11-P2. A one-way abstraction can instead give conditional lower/upper certificates, F32. Without sound source extraction and rights evidence, no global Go proof follows.

## Important distinction: knowledge vs state refinement

- **Epistemic filtering** (Paper B): add legitimate information to *reduce candidate worlds*. Once a robust accept/reject is derived within a fixed world set, this decision survives evidence filtering.
- **Source evolution** (P44): apply an actual edit to *change the world*. A previously acceptable patch/architecture may cease to be acceptable; a right may be revoked; the epistemic monotonicity theorem does not constrain these transitions.
- **Observation-language refinement**: add new protected queries. Previously observationally equivalent architectures may become distinguishable, as the P35 absent-header negative control shows.
- **Repair grammar enlargement**: adding genuinely conservative authorized options can expand feasible future goals, but need not preserve old minimal quotient block counts (P42-P13-R6).

## Prior-art collision

Ordinary state-congruence, Myhill–Nerode, weighted bisimulation, rely–guarantee, separation logic and Abadi–Lamport auxiliary/history-variable refinement mappings already handle much of the abstract theory. A true EvoNOMOS contribution would require (i) a reproducible source/right extractor, (ii) independently tested forecasts under fixed information, or (iii) identified regime changes in real causal architecture effects that do not follow from equal-information conventional models. A Grothendieck opfibration claim requires opcartesian/universal factorization data, not just some concrete lift witnesses.

## Reusable falsifiers

1. Same q(s) but different enabledness for a documented actor/edit: failure of abstract repair admissibility.
2. Same q(s) but different q(next) under equal edit: failure of no-reread update.
3. Same protected old responses but different newly protected response: failure of observational sufficiency for enlarged contract.
4. Same observed function but differing source-repair rights or admissible edits: failure of static architecture ranking.
5. Same initial behavior/rights but costs reverse under independent future demands: potential conditional law candidate, **only** if actually measured and conventional models compared.
