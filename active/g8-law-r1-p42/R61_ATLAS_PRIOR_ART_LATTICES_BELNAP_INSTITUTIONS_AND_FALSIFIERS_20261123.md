# EvoNOMOS R61 — Atlas Prior Art and Exact Mathematical Boundaries

2026-11-23 | Companion to R60, Paper B v37 and EvoNOMOS 27.md. Literature comparison, not a novelty verdict.

## Three pre-existing mathematical alternatives

1. Ganter & Wille (1999), *Formal Concept Analysis: Mathematical Foundations* (book), original PDF in Research OS 11_BOOKS. Formal contexts and closure systems already support concept lattices. The mathematical novelty cannot be 'putting sets of contexts in inclusion order'. Confirmed publisher: https://link.springer.com/book/10.1007/978-3-642-59830-2
2. Dunn (1976) / Belnap (1977): four values (neither, true only, false only, both) and separate orders for information and truth pre-exist the atlas. Useful for preserving *conflicting* versus *missing* engineering evidence; not a new semantics claimed by EvoNOMOS. Reference: https://plato.stanford.edu/entries/truth-values/
3. Goguen & Burstall (1992), *Institutions: Abstract Model Theory for Specification and Programming*, considers satisfaction that remains coherent through signature change and mathematical gluing of theories under conditions. Any alleged atlas 'gluing law' must compete with these known constructions. Reference: https://www.lfcs.inf.ed.ac.uk/reports/90/ECS-LFCS-90-106/

## A sharper distinction

An engineering principle's SUPPORT in the atlas is not identical to truth of a logical sentence in a model. A policy's binding force depends on authorization; a contract's satisfaction depends on semantic traces; a cost heuristic depends on a conditional comparator, causal assumptions, and an objective chosen by someone. Mixing these sorts creates invalid deductions.

Define evidence for proposition p in context c as e(p,c)=(s,d) in {0,1}². The information order is componentwise: (s,d) <=_k (s',d') if s<=s' and d<=d'. Its meet is bitwise AND and join is bitwise OR. The four elements form a distributive lattice under this information order. Existing logic; *not* evidence that design principles themselves form a complete lattice of semantics.

Even if finite contexts C generate the powerset lattice 2^C, the actual images {S+(p):p in P} are generally not closed under intersections or unions. For example, C={a,b,c}, S+(p)={a,b}, S+(q)={b,c}, and no principle has support set {b}. Therefore the observed principles do not form a sublattice without adding derived concepts. 'An atlas exists' needs a specified family of observations and transitions, rather than an assumption of a single smooth space.

## Nontrivial question for publication

Can one map design arguments to typed context-dependent warrants so that a change in D, T, G, A or J produces a documented recommendation revision *without silently promoting heuristics into contracts*? Would independent reviewers using the same evidence and declared costs produce better-calibrated abstentions or more consistent decision records than a baseline of ordinary design-review checklists?

## Falsifiers

- Two independent raters cannot agree on what counts as the same context or warrant.
- The atlas degenerates into old formal concept analysis without incremental explanatory/predictive benefit.
- It fails to represent policy supersession or conflicting evidence without forcing a false single verdict.
- A general, source-aware design baseline makes at least as accurate and less expensive decisions.

## Evidence hygiene

The R60 code tests 4 evidence states across 64 ordered triples, plus a 3/7 expected-cost crossover and a local-gluing counterexample; these are exhaustive for that toy state set, not software-system validation. Literature and toy mathematical demonstrations do not substantiate claimed societal prevalence of SOLID dogmatism or universal OOP principles.

## LIRA

0.98 preserve typed distinctions; 0.95 put independent raters and falsifiers into research plan; 0.90 retain context-indexed atlas as exploratory construct; 0.15 reject unqualified claim of original bilattice/concept lattice/sheaf theorem.

Paper B v37 untouched; LAW-R2 still HOLD.