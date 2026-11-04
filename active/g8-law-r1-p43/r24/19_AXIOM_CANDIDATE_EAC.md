# R24-EAC: Evolutionary Admissibility Calculus (candidate, NOT a new established theory)

The target is the permitted, source-grounded and old-contract-safe *process* of software change, not SOLID pattern compliance.

Define an evolutionary instance M=(S,s0,O,C,D,E,Pi,c,V):
- S source and runtime configurations; s0 initial configuration.
- O a declared observation operator; C the set of protected client traces.
- D a prospective demand family, independent of source-specific discovered outcomes.
- E allowed source edit transitions; Pi ownership/authorization; c nonnegative cost vectors.
- V provenance and verification predicates for each transition claim.

Candidate foundational obligations:
E0 (Observer specification): every claimed equivalence is indexed by a declared O and finite/complete scope.
E1 (Permission): every transition in a repair path must be in the allowed source edit relation E_Pi.
E2 (Prefix preservation): each intermediate configuration must satisfy protected C under O.
E3 (Demand realization): the final configuration must satisfy the externally fixed future requirement.
E4 (Cost transparency): compare repair paths with an explicit nonnegative cost vector; distinguish synthetic edits and actual labor.
E5 (Evidence provenance): separate proposed, code-reviewed, native-executed and independently reproduced claims.
E6 (Matched comparison): compare two structures only with identical customer oracle, demand family, rights *semantics*, and competing explanation budget.

E0-E6 are protocol axioms / definitional obligations, not automatically true facts about arbitrary software. Source-checkability and feasibility are research problems. None entails that architecture A is uniformly superior to B.
