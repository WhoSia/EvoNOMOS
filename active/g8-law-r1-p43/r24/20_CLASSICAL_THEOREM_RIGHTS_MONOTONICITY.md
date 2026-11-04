# Conditional rights monotonicity — classical finite transition-system theorem

Let Q(pi) be the set of *stagewise-safe* paths admitted by rights pi in a fixed state graph, fixed observations, fixed demands, fixed nonnegative edge costs.
If pi subset pi' and the transition relation is conservative (all old admissible edits remain executable with unchanged outcomes and costs), then Q(pi) subset Q(pi').

Therefore F(pi') subset-or-equal F(pi) for minimum scalar repair cost; with infinity for infeasible. The set of attainable cost vectors can expand, while its Pareto frontier changes non-monotonically as a *set*, so never assert simple inclusion of ParetoMin fronts.

Proof: each old path remains legal. The infimum over a superset cannot increase. Empty paths retain infinity.

Failure boundary: adding a permission that changes authority semantics or deletes an existing transition is not a conservative rights extension. Cost scalars cannot be substituted for real engineer hours without measurement.

Locally executed Go Dijkstra verifier checks 27 ordered right-set inclusions (including equality) for 3 symbolic rights and four source states; result PASS. This is a bounded test of a classical proposition, not an original universal software law.
