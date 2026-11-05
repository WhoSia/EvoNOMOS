# Adversarial review of the P44 finite online/offline repair game

## A. Fix the stage semantics before proving anything

The first implementation draft accidentally evaluated later goals without also enforcing the previously accepted stage-one contract. This was corrected BEFORE claiming a verified result: the game now has separate fields Stage1 (contract on all later nodes) and Checkpoint (eligible early commitment nodes). Reach(s,d,true) refuses paths that exit Stage1 after the first release; Safe preserves the original C0 at all nodes. The intentionally unsafe path a→u→by is a negative control.

Concretely, d1 is not required at the initial source s0 before it is implemented, but once a stage-one checkpoint a/b is committed, every subsequent permitted revision must preserve d1; ax and by both satisfy d1 as well as their corresponding future demand. Keep these time indices explicit in any formal paper.

## B. Real game boundary

The comparison OfflineCover vs OnlineCommitWin is a toy two-round **information game**. It says nothing about actual behavior in a company unless a first release is forced before the next demand, an adversary may choose either x or y, no valid rollback or cross repair exists, and stage-one release endpoints are restricted to H1. With a new authorized cross edit a→by or with delayed commitment until future disclosure, the conclusion changes. This dependency is the scientific point; it is not evidence of universal inevitability of nonanticipation costs.

## C. Critical external novelty audit

Classical online algorithms and reactive synthesis already study foresight and game strategies. The novelty cannot be simply that "for all futures exists a path" differs from "exists one strategy for all futures." An original source-verified application could distinguish architecture future robustness only if the observer/rights/release checkpoint mapping and demand generator are independently validated and stronger classical synthesis comparisons given equal input/CPU.

## D. Future dynamic soundness

Static cost-bounds theorem L≤K≤U from the earlier P44 text has a fixed revealed demand. An online game needs a different certificate target, e.g. a strategy that is sound against all legal demand sequences, or a sound lower bound on minimax expected/worst cost under an explicit environment model. A CEGAR-style abstraction preserving only existential reachability is not automatically sound for alternating quantifiers; both existential system choices and universal environment branches must be treated with correct abstraction polarity.

Do not reuse P44's existential path cost lower-bound argument as an online strategy winning proof. Need alternating-simulation or appropriate abstract-game winning certificates, explicit abstraction of demand availability, and schedule-independent client-safety proof obligations.

## E. Proof and reading checklist

1. Quantified demand-history language and acceptance/deadline timing.
2. Source-level edit ownership, rollback possibilities, release checkpoint granularity.
3. Asynchronous temporal trace and joint observer preserved under any purported abstract-game equivalence.
4. Source-derived strategy representation with checker verdict PROVED/REFUTED/UNKNOWN.
5. Classical competitive-online or reactive-synthesis rival.
6. Source-based external demand/commitment evidence; no artificial selection of adversarial branch.
7. Limit on claims when finite checks pass.
