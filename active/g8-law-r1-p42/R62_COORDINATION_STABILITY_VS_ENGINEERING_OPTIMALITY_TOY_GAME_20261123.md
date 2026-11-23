# EvoNOMOS R62 — Coordination Stability Is Not Engineering Optimality

2026-11-23 | Exact finite game-theoretic illustrative counterexample. Existing Nash/Pareto theory, not a newly discovered law.

## Motivation
The contextual atlas should map *how a team habit gets authority* separately from *whether the habit improves change costs*. Social stability and engineering benefit are different predicates. This is a conceptual caution, not empirical evidence that any team follows SOLID as dogma.

## Two-agent coordination game
Two collaborating developers each choose an architectural convention A or B. Illustration-only symmetric payoff table:
| First / second | A | B |
| --- | --- | --- |
| A | (2,2) | (0,0) |
| B | (0,0) | (3,3) |

At (A,A), neither player can improve by changing alone, since deviation gives payoff 0 instead of 2; thus it is a Nash equilibrium. At (B,B), neither can improve by changing alone either, because deviation gives payoff 0 instead of 3. Yet B,B Pareto-dominates A,A since 3>2 for both. A convention can therefore be stable without being Pareto optimal. The statement is elementary and conditional on the chosen payoff table; neither payoff corresponds to measured software teams.

## Atlas type separation
Record policy authorization as one variable, behavioral contract admissibility as another, and cost/benefit conditional on incentives as a third. Even an observed coordination equilibrium does not establish an actual team governance obligation. For any game model used empirically, specify agents, action space, payoffs, information and switching friction, then search for institutional and observational rivals.

## Falsifiable research questions
- Is explicit design-rule language predictive of reviewer behavior after holding code change demand and quality concerns constant?
- If developers coordinate on an incumbent rule, can experimentally supplied change-cost evidence revise that choice?
- Do teams with different switching costs show different persistence even if a design-quality baseline predicts the opposite?
- Can a much simpler norm-conformity model explain any observations as well as the contextual atlas?

Negative control: a mandated behavior contract cannot be evaluated as mere payoff preference. Historical author claims about prevalence remain unverified. No automatic LAW-R2 promotion.

## Local mechanical verification
Enumerate four strategy profiles (A,A), (A,B), (B,A), (B,B) and unilateral deviations for each player. Results: exactly two pure Nash equilibria (A,A), (B,B); A,A is Pareto dominated by B,B. Local exhaustive toy check performed with Python on 2026-11-23.

## LIRA 0.1
0.96 for keeping stable convention separate from engineering value; 0.83 for inclusion in a supporting theory note; 0.36 for inserting the entire payoff table into the short Paper B body; 0.05 for claiming empirical design norms have already been demonstrated.