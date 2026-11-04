# Conditional path commutation — mathematical lemma, not novelty claim

Assume three application edit operations e_i:
(1) are authorized at every relevant state,
(2) preserve the protected customer contract at each prefix,
(3) operate on disjoint route registrations without shared-state side effects,
(4) commute modulo the declared observation and preserve each previously achieved independent demand,
(5) have fixed additive unit costs.

Then every permutation of e_1,e_2,e_3 leads to a state satisfying all three demands; the total synthetic expense is three units. Proof: prefix preservation by assumptions (2),(4), reachability by applying each operation once, and total cost by (5).

The native source experiment only probes the named cases and cannot establish these assumptions for all Go code or the entire Chi routing API. A classical LTS with commuting transitions proves the same result without EAC novelty.
