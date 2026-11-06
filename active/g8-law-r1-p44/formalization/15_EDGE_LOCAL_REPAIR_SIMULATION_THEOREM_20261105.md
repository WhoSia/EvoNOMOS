# P44 edge-local path-simulation theorem — scoped classical result

Research unit dated 2026-11-05. CLASSICAL graph simulation and weighted shortest-path lemma, not original EvoNOMOS mathematical priority.

## Finite closed-world premises
Let C=(V_C,E_C,s_C,G_C) be a finite concrete authorized source-edit graph. Every vertex carries an already-declared client-contract predicate Safe, a disclosure stage k, and a demand-goal predicate Goal. Every actual graph edge is a bounded, authorized source edit with fixed nonnegative scalar synthetic cost and rights label.

**Source-completeness is assumed, not inferred from the graph.** To claim a result about actual Go source, one must independently prove that all relevant authorized source edits, client outcomes, source dependencies and environments are faithfully represented. Otherwise this theorem covers only the enumerated graph.

Define admissible paths as finite paths from s_C consisting only of authorized, contract-safe edges with unchanged stage k, ending at a goal state. Let K_C be their minimum cost (infinity if none).

Construct an abstract graph A=(V_A,E_A,s_A,G_A) and a total map alpha from every concrete safe vertex to an abstract safe vertex. Require:
1. alpha(s_C)=s_A;
2. stage(alpha(v))=stage(v) for all safe v;
3. v∈G_C implies alpha(v)∈G_A;
4. for every authorized concrete edge v --(right,c)--> v' whose endpoints are safe at the same stage, there exists an authorized abstract edge alpha(v) --(right,c')--> alpha(v') with c'≤c.

Then every concrete admissible finite path is projected to a stagewise-safe abstract path of no greater cost. Proof by concatenating matching abstract edges and summing the edge-local inequality. Thus L_A≤K_C, where L_A is the abstract minimum over its safe authorized paths. An independently checked concrete path h of cost U proves K_C≤U. Hence L_A≤K_C≤U.

If L_A=U<infinity, this yields exact minimum cost **only within the finite complete concrete edit graph**. This is standard weighted forward simulation / conservative abstraction, not novel software-maintenance physics.

## Important domains excluded

The checker enforces unchanged stage along source edit transitions. It is not yet a proof about demand-disclosure edges, rollback, adversarial future information, nondeterministic Go runtime semantics, continuous code-diff edit keystrokes, concurrency, arbitrary full contextual traces, or vector-valued actual maintenance costs.

The rights label is a string in the finite fixture; actual rights enforcement needs a source ownership/type/provenance proof. Safe flags are supplied predicates rather than dynamically computed true contractual properties.

## Countermodels

1. Omitted permitted safe concrete edit: an abstract graph lacking its cost-refining match must be rejected.
2. Abstract cost exceeds concrete cost on all matching transitions: reject.
3. Abstract image of a concrete goal is not a goal: reject.
4. Mapped stage mismatch or unsafe abstract image: reject.
5. Unknown source edit can break a previously claimed lower bound. Example closed enumerated graph K=4; a subsequently discovered permitted direct cost-1 edit changes the actual K to 1. The previous abstract graph certifies only the old incomplete source-edit universe; extending the finite graph and rerunning the verifier catches the unrepresented edit.
6. Unauthorized upstream shortcut and contract-unsafe intermediate states must not lower a protected source-edit cost.

## Next genuinely open problem

Build a sound *source-derived* transition enumeration or structural proof certificate that satisfies conditions (1)–(4) for real maintained code and its actual permitted edit universe. This is much more difficult than verifying a supplied graph and must be compared against classical separation logic, bi-abduction, CEGAR and program-repair search.

File links: edgecert/graph.go and edgecert/graph_test.go. CI should be checked at the tested source commit; local Go1.23.2 tests/vet/race had PASSED prior to GitHub commit, but the published source CI requires independent receipt.
