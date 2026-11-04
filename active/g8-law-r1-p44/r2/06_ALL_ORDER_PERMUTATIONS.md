# Six non-overlapping demand insertion orders

The code enumerates all 3! permutations of the three frozen requirements. For each insertion order it checks stage 0,1,2,3 under both original backed routers; after each prefix it verifies old contract and all demands already inserted.

The request paths are disjoint and the routers' registration interfaces are assumed not to conflict here. Classical commuting independent edits predict success for every order, with synthetic cost 3 after all route insertions.

This is a robustness extension selected after the primary sequence was predeclared, so it is not a separate independent blinded holdout. Any failure must be preserved and analyzed rather than silently dropped.
