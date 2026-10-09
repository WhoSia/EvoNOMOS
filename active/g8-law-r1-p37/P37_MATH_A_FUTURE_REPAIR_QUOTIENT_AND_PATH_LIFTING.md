# P37-MATH-A — When Does a Present Software Abstraction Preserve Future Repair Possibility?

**2026-10-10 KST · P37 OPEN · mathematical derivation (classical factorization). No claim of new law.**

## Formal exact question

Let finite source states `S` have present visible abstraction `q:S→A`. Let `Γ` be a precisely delimited directed source-change graph. For each future demand `d∈D`, let accepting states `Acc_d⊆S` and path-invariant set `I⊆S` be fixed. Say `May(s,d)` iff there is a zero-or-more-edge directed path from s to a state in `Acc_d` whose states all satisfy I (including start). Define `Must(s,d)` iff May(s,d) and every *I-preserving terminal reachable state* lies in `Acc_d`; do not confuse this with universal graph paths or exclude zero-length paths silently.

Define present quotient `s≈_0t↔q(s)=q(t)`. The question is whether one can decide future May from q(s) alone.

## Theorem A1 (factorization, elementary)

There exists `f:A×D→{0,1}` with `f(q(s),d)=May(s,d)` for every s∈S,d∈D **iff** `May(-,d)` is constant within every nonempty fibre `q^{-1}(a)` for all d.

Proof ⇒ choose s,t in same fibre, so f has the same arguments. Proof ⇐ set f(a,d) to that constant on nonempty fibres; arbitrary off-image. This is a finite version of factoring an observer through a quotient. Identical present HTTP response does not imply the premise. **This theorem is familiar quotient theory / continuation equivalence and not beyond SOLID novelty.**

## Theorem A2 (path-raising, carefully limited)

A directed morphism `h:S→T` that preserves **start-state admissibility**, every Γ edge, and acceptance (`Acc_d(s) ⇒ Acc'_d(h(s))`) guarantees **May(s,d)⇒May'(h(s),d)**. It does not guarantee the converse. For equivalence, it suffices in addition that (a) target acceptance is reflected by h, (b) each target edge starting at h(s) can be **lifted** to a source edge from s (for every reachable s), with admissible endpoints, and (c) target successful zero-length starts lift. Then May is equivalent. Nonvacuous Must requires substantially more: reverse lift / coverage of **all** relevant reachable terminal states and preservation/reflection of acceptance. Without these additional assumptions, a single favorable lift does not imply Must.

**Counterexample to converse with one-sided simulation:** source a has no edges and is nonaccepting; target h(a)=x has an edge to accepting y. h trivially forwards every source edge (none); target May true, source May false.

## Smallest noncommuting present quotient

Source `s_1` and `s_2` have q-values both 0 (same present behavior), yet differ in retained provenance. In Γ only s1 has an authorized edge to a future-accepting target a (or no-history s2 cannot produce same stored closure), so May(s1,d)=true and May(s2,d)=false. No q-only future feasibility predictor exists. The statement is meaningful only if Γ forbids reading an external log or a caller re-supplying the lost data. This is the DIP42/49 motif and classical automata distinguishability.

## Crucial negative: path count and structure are not an automatic new law

Consider graphs with states s,a accepting and s→a, versus t,b1,b2 accepting and t→b1,t→b2. q(s)=q(t), May(s,d)=May(t,d)=true; the paths differ (one vs two). Therefore more repair routes or different source cut-size does **not** force different May for a fixed requirement. A graph feature `G` must predict a genuinely *new demand family*, not smuggle a structural difference as a performance or law claim.

## Source-linked research meaning

P36's Chi HeaderRouter and Gorilla original routes instantiate distinct historical information boundaries; O12's two parsers instantiate raw token provenance. Both still admit classical interpretations. P37 should seek graph properties that remain robust under admissible abstraction of real source and that **predict future option survival** under truly independent change sequences. If the strongest classical game/automata/source-refinement model already predicts the exact statement, register the result as a useful bridge, not a new theorem.

### Experimental progression

1. Exhaustively enumerate small labelled finite graphs to check A1 and forward/non-converse A2; preserve explicit negative control with equal future May and different path counts.
2. Define relation-preserving, *not cost-derived*, source annotations (where data was retained, API edges crossed, who can revise invariants) and freeze them before Q23 source editing.
3. Ask a stronger theoretical question: under what restricted **composition of responsibilities** does the future-repair equivalence become a congruence? Prior art: Myhill–Nerode, (bi)simulation, game semantics, modal transition systems and data refinement. Do not assert a congruence under hidden-state-inspecting contexts.
4. DIP49: prospective separating experiment only if H and strongest classical B* actually disagree on same original source, Q and edit authority.

**Verdict**: `P37_MATH_A1_FACTORING_CLASSICAL__MATH_A2_SIMULATION_CLASSICAL__NEGATIVE_PATH_COUNT_COURT__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.
