# P44 conditional two-axis repair source certificate: edit coverage and trace coverage

2026-11-05. Classical weighted simulation, program abstraction and incorrectness-logic synthesis. NOT a newly established universal law.

## Two independent universes

Let P be versioned real source artifacts, E_pi^real the full authorized source-edit relation, Tr(p,e) feasible joint client traces under declared environment/schedules, and C_k the protected contract activated at stage k.

**Axis A: source-edit coverage** — a source-derived edit graph represents EVERY permitted concrete edit path within a declared grammar, with actual rights, costs, protected stage and goal reflection. Missing one permitted cheaper edit invalidates any claimed global lower bound. F12 supplies a finite omission countermodel.

**Axis B: runtime-observation coverage** — for every protected release checkpoint p_i, a sound execution trace overapproximation U(p_i) contains ALL relevant actual joint source traces and all abstract traces in U satisfy C_k. A hidden bad actual trace invalidates a universal safe assertion. A source-realizable underapproximation W(p_i) containing an erroneous trace certifies this path violates its client contract, but says nothing about other source repairs. F13 supplies finite evidence countermodels.

These axes are logically independent. Enumerating all permitted edits does not prove every edited program safe; proving one program safe does not prove cheaper alternative patches have been enumerated.

## Conditional composition theorem

Assume (A1) complete source edit grammar for the explicitly declared source domain; (A2) correct permissions, goals, edit costs and staged client activation; (B1) every SAFE checkpoint is validated with a sound overapproximation of all relevant joint runtime client traces; (C1) a stage- and right-preserving cost-nonincreasing edge-local simulation representing every admissible concrete source edit; and (C2) a separately checked concrete safe authorized repair witness of cost U.

Then the abstract optimum L is no greater than the concrete safe source-edit optimum K within the domain, and K is no greater than U: L <= K <= U. When L=U finite, the domain optimum is proved. The proof follows by including every permitted safe source path (A/B), applying C1 to its edges for L<=K, and C2 for K<=U. This is classical proof composition rather than a new claim of mathematical priority.

For a particular proposed repair path, one source-realizable erroneous trace at a protected checkpoint suffices to reject THAT path. To prove NO safe repair exists, one must quantify across ALL permitted source repairs; a bad witness for just one is insufficient. Missing a sound source graph or runtime overapprox certificate must yield UNKNOWN.

## Evidence and honest limits

The existing F12 edgecert and F13 evidence Go modules are separate finite mathematical fixtures. They do not automatically extract a whole-Go edit graph, prove all possible client context traces, establish rights provenance, or show certificate efficiency vs strong classical methods. Their green GitHub CI results verify toy logic, not a complete original-source certificate.

Next gate: define a small typed source-edit DSL whose allowed edits can be completely enumerated and whose bounded runtime joint trace semantics can be exhaustively checked, and then compare to exact classical search on identical inputs. G1-G7 OPEN; LAW-R2 HOLD.
