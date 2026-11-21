# Joint observer is strictly stronger than equality of marginal observer ranges

Date 2026-11-04; pure finite formal countermodel, no original Go execution and no novelty claim.

Let Trace={0,1}×{0,1}, and observer coordinates o1(x,y)=x, o2(x,y)=y.

- Program A permits trace set T_A={(0,0),(1,1)}.
- Program B permits trace set T_B={(0,1),(1,0)}.

For both A and B, the marginal value set of o1 is {0,1}; the marginal value set of o2 is {0,1}. Therefore individual-coordinate marginal set equality cannot distinguish A and B.

But joint observed sets:
  JObs(A)={(0,0),(1,1)}
  JObs(B)={(0,1),(1,0)}
are unequal. A satisfies the relational client contract C(x,y): x=y for all its traces, B violates it on every trace.

Therefore the definition of observational equivalence must preserve **within-execution correlations**, explicit client contexts and timing. Source tests that compare only status histograms and body histograms separately can report false equivalence even when actual response tuples differ.

The corrected F2 definition in 00_P44_MATHEMATICAL_PROBLEM_CONTRACT.md uses a jointly indexed vecO(t), not unioned or separate marginal sets.

A full contextual observer must also preserve correlation across multiple requests and interleavings, not just fields inside one response. Data-race freedom does not remove these relational obligations.

Status: VALIDATED BY DIRECT FINITE ENUMERATION/PROOF; no empirical claim about all real source programs.
