# P44 F16 — actual native Go shared heap and BFS reset, verified 2026-11-05

## Real execution evidence

[GitHub Actions run 41967827718](https://github.com/WhoSia/EvoNOMOS/actions/runs/41967827718) on exact tested commit f6ca5842c8641d8f78867eb47d6e0b4c02e8df2d; original job 127048832664, go1.23.2 Linux amd64. Raw job logs inspected, five named tests PASS, go vet PASS, go test -race PASS.

Original logs:
- SHARED_ALIAS_WRITE legacy=new future=new old_client_regressed=true
- DISJOINT_WRITE legacy=stable future=new safe=true
- SHARED_SPLIT_WRITE legacy=stable future=new safe=true
- ALIAS_COST initial_observations_equal=true shared_safe=2 separate_safe=1 naive_shared=1 classical_exact_tie=true

The native Go part uses actual pointers and heap cells. The finite model has exactly two AUTHORIZED DECLARED operations (split and write future) each assigned synthetic unit cost. An initial aliased pair with joint visible outputs (stable,stable) costs 2 to reach (stable,new) safely: split then write. Two disjoint pointers with same initial observed outputs cost 1. A naive local-only estimator incorrectly assigns 1 to the alias case. Exact classical source-aware BFS knows the alias bit and correctly returns 2/1.

## What was actually proved / what was not

The source code's Go runtime behavior empirically demonstrates alias propagation and the witness repair. The cost lower and upper conclusions follow by complete case analysis of the FINITE declared operation graph. The permitted operation relation was *not extracted from parsed Go source* and is not an exact model of all source patches or owner-authorized modifications. No actual software developer time was measured. The test is not a source-level universal alias correctness theorem, performance improvement, or new engineering law.

This is specifically a decisive negative control on the premise 'source-local edits imply observational independence'; the classical separation-logic frame rule requires disjointness/ownership constraints. Reynolds 2002 and O'Hearn/Yang/Reynolds 2009 already account for this mechanism.

## BFS return to original EvoNOMOS ambition

After F12/F13 artificially supplied finite graphs and traces, F14/F15 AST source grammar enumerators, and F16 native heap reference effects, all validated positive claims remain CLASSICAL and narrow. Return to:
> Given two currently observationally equivalent maintained code structures and genuinely comparable actor edit rights, which structural features predict differing future *safe* repair capacities, and can we verify them from actual source more compactly or usefully than existing methods?

Five complementary research branches:
- SOURCE: derive real-authorized edit rights (trusted repository/app-owner scope, parser/typechecked transformation language) with a completeness statement.
- OBSERVER: source-sound old-client joint trace and schedule coverage (not one pointer test).
- THEORETICAL: compare separation logic + bi-abduction, alias analysis, CEGAR, contextual refinement and exact graph/model checking with identical source input and rights.
- EMPIRICAL: preseal independent real future maintenance tasks; evaluate correctness, proof complexity, source transport and actual effort.
- STRATEGIC: information timing/nonanticipation only when historical release commitment before request disclosure can be verified.

Stop rule: no promotion from more toy states, cosmetic graph complexity, or trivial rederivation of classical frame/alias facts. Preserve source-vs-graph distinction and issue honest PASS/FAIL/UNKNOWN. P44 stays open; G1-G7 and LAW-R2 remain HOLD.
