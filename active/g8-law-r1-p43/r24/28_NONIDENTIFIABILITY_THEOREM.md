# Baseline observation alone does not identify future repair feasibility

Given only one customer-observation relation O on initial states, one cannot in general infer the safe authorized source-edit reachability relation. A and B can agree on all declared initial outputs and still possess different future authorized transitions.

Formal finite countermodel: public observations O(A0)=O(B0)="200/old". A permits A0 -> A1 (app-owned cost 1), while B has no permissible outgoing transition from B0. Both A1 and a hypothetical B1 are declared safe goals. Under the same right {app}, the demand is feasible for A and infeasible for B.

This is an indistinguishability / underidentification counterexample, not a claim to novel logic. Full source-aware labeled transition systems with permissions *do* distinguish A and B; an observer-only method cannot.

Executable independent Go test is identifiability_test.go. Local tests passed on 2026-11-04; the GitHub branch test file's CI status is separate.
