# P44 source-repair lower/upper certification through abstraction

2026-11-04. A CLASSICAL abstraction/optimization lemma adapted to P44's formal objects. No novel mathematical priority asserted.

## Fixed semantics and proof obligations

Fix a real source program p, environment/scheduler family E, *joint* observation family O, staged customer contracts C, external demand d, and a fixed COMPLETE permitted source-edit relation E_pi within the claimed domain. Let R_c be all permitted, staged contract-safe concrete edit paths satisfying d. Costs c(h) are nonnegative scalar values with a fixed measurement unit. K_c=inf{c(h):h in R_c}, inf(empty)=infinity.

An abstraction has candidate paths R_a, projected costs c_a and an abstraction map alpha defined **for every concrete admissible path** such that alpha(h) belongs to R_a and c_a(alpha(h)) <= c(h).

Then L=inf{c_a(a):a in R_a} <= K_c. A separately validated concrete source-edit witness h_w in R_c of cost U proves K_c <= U. Therefore L<=K_c<=U. If L=U finite, optimum is proved **for the defined domain**.

Proof: all concrete admissible paths map into candidate abstract paths with cost no larger, so every concrete path costs at least L. Take infimum. Concrete witness upper bound follows since U is attainable.

It is NOT sufficient that the abstract ordinary program transition graph overapproximates execution traces if the abstraction's safety filter discards a genuinely safe concrete edit path. Sound lower bounds require the *admissible repair-path* inclusion above, including source rights, staged contract, costs, and observation quantifiers.

## Counterexample-guided refinement

Let R_a(0) contain sound images of every concrete admissible path plus spurious cheap paths of costs 1 and 2. An observed legitimate concrete witness has cost U=4. Then L0=1, while the true optimum in this toy model is 4. If a checker soundly excludes the nonconcretizable 1-path and 2-path without excluding concrete images, the nested abstract path sets give L1=2, L2=4=U. Thus source optimum becomes proved within the complete grammar.

In general if R_a(i+1) subset R_a(i), the valid source-path images remain included, and the abstract cost rule does not change, then L_i are nondecreasing lower bounds. If refinement changes abstract costs or mappings, monotonicity does not automatically hold. Heuristic inability to find a realization is not proof that a cheap abstract edit path is spurious.

## Where the actual research begins

This bounds argument is inherited from abstract interpretation / CEGAR and optimization dual bounding. What is unsolved in P44 is extracting a sound source/edit-rights/old-client-preserving abstraction from real Go source, efficiently refining it with checked counterexamples, and proving that cheaper alternatives are excluded *without* a hand-picked edit grammar. Benchmark against separation logic, bi-abduction, CEGAR and an equal-information exact bounded classical search. No whole-Go source soundness, all-context equivalence or novel LAW-R2 is claimed.
