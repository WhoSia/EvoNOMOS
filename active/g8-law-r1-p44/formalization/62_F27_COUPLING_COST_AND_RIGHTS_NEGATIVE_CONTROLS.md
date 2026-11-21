# P44-F27 — Two coupling countermodels

The exact asynchronous product theorem requires completely independent edited coordinates, independent rights, factorized demand satisfaction and **additive costs**. These are hypotheses, not consequences of using classes/interfaces.

### C1: cross-component synergy
Component A can satisfy a at cost 2; B satisfies b at cost 3. Independent product predicts future demand sequence (a,b) costs 5. Add a legal joint edit from initial (0,0) to (1,1), cost 1. The new global optimum is **1**, not 5. An interface crossing can LOWER the repair cost: modular decomposition alone never proves an unconditional optimum advantage.

### C2: shared edit budget
For the same components impose a single globally usable edit opportunity. After the first A or B edit, the other is no longer permitted. The cost of every individual demand remains finite (2 or 3), but sequential demand (a,b) becomes **impossible in this declared complete finite graph**. The independent cost prediction 5 is now *falsely feasible*. This is more serious than a cost-ranking error.

### C3: declared-but-unsatisfiable future demand
Do not project a demand word using only goal labels currently appearing in reachable states. An unachievable demand is still in its declared alphabet, and must yield infinity, not disappear. The F27 first implementation had this pitfall; the corrected version stores declared demand alphabets separately from per-state satisfied goals.

### C4: permission quantifier polarity
Existential safe-repair availability weakly increases when additional legally authorized choices become available. A different **universal** assertion, 'every possible action permitted under the policy is safe', can cease to hold when new risky actions are permitted. These have different quantifiers and different transition universes; never infer universal safety from an existential repair graph.

The examples are classical finite countermodels, not original-Go proofs. Strong matched-information conventional baselines would detect them when supplied the same complete graph. Real source extraction and G1–G7 remain open. LAW-R2 HOLD.
