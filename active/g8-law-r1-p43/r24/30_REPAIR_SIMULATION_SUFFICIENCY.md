# Conditional source-edit simulation — candidate future proof certificate

Let R relate safe source states of A and B. A conditional *cost-refining repair simulation* requires:
(1) R(a0,b0) and matched protected observable customer contract;
(2) whenever R(a,b) and an authorized, stagewise-safe A edit a -> a' costs c, B admits a finite authorized safe path b ->* b' of aggregate cost <= c and R(a',b');
(3) every relevant target demand satisfied at a is satisfied at b for related states;
(4) all comparison rights, cost definitions, old-client constraints, and demand disclosures are fixed before the experiment.

Then each safe A repair path can be converted by concatenation to a safe B path with no greater total cost. Hence minSafeCost(B,d) <= minSafeCost(A,d), provided the B path segments exist for every A step on the claimed domain.

This is a standard forward-simulation-style lifting argument, not a novel theorem. The *new substantive research challenge* is extracting and validating such a certificate from original source with credible ownership and cost, then testing its predictive compression and transfer against classical source analysis.

Counterexample/off-ramp: if even one permitted A step lacks a corresponding B path, this sufficient certificate fails; that alone does not imply B is genuinely worse for every demand.
