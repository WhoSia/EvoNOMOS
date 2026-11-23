# P44 alternating abstraction polarity — proof gate

Date 2026-11-05. This is a classical game/synthesis observation, NOT a new EvoNOMOS theorem.

## Existential source paths versus alternating games

In the finite repair game, the environment universally chooses later demands and the editor existentially selects authorized edits, without knowledge of future demands when making the first release. Therefore a plain existential repair-path overapproximation, suitable for the lower cost bound of one fixed demand, does not automatically prove a winning *strategy*.

### False WIN

Original graph: two early commitments a,b. Only a can later serve x; only b can serve y. Concrete OnlineWinning=false. An abstract system graph inventing a permitted source edit a→by now claims OnlineWinning=true. The abstract extra existential system move creates a **false positive** winning strategy. It is not source-sound simply because it overapproximates reachable paths.

### False LOSS

Original graph with a→ax and a→by offers online-winning commitment a for legal futures {x,y}. An abstract environment includes an additional spurious future z with no feasible goal. Abstract OnlineWinning=false, although concrete OnlineWinning=true. Overapproximating universal environment choices can generate false losses, even if this challenge makes proof of abstract winning conservatively stronger.

## Sufficient strategy-lifting obligations (not yet proved for source code)

1. A relation between abstract and real versioned source release states preserving activated client contracts and demand satisfaction.
2. Every **real** allowable environment future demand is represented by a matching abstract environmental move (do not omit adversary cases).
3. Every **abstract chosen system move** is implemented by a real authorized, all-prefix contract-safe source edit path from any related concrete state (no phantom repairs).
4. Inductively maintain state relation and the appropriate time-indexed contract, including release/checkpoint progress.
5. Concrete editor's observable information suffices to implement the abstract policy without anticipating hidden future demands.
6. Cost and temporal trace claims have separately certified mapping and environment/fairness conditions.

Under these premises, an abstract winning policy can be lifted to a concrete one on the named finite game. Full Go source extraction and universal source checker remain OPEN.

## Prior literature

Pnueli & Rosner (1989), On the Synthesis of a Reactive Module, POPL, DOI 10.1145/75277.75293; Borodin & El-Yaniv (1998), Online Computation and Competitive Analysis. Public bibliographic records and abstracts checked; full proofs not read. Google Drive name/author lookups yielded no named copies; ownership still not byte-certified.

## Finite evidence only

See online/game_test.go for negative-control graph tests; CI receipt must be independently read before asserting pass. This proof note is a design requirement, not source-level verification.
