# A vital proof-boundary distinction — source repair witness vs minimum cost

Date 2026-11-04. This is a mathematical validity gate, not a novel result or a newly run source test.

## Feasibility is not optimality

Let E_pi be *all and only* authorized source edit transitions according to the declared application permission model. Let O_C encode protected old-client observations, D the new demand, and c >= 0 the cost.

Finding a real sequence p of permitted changes whose every intermediate state passes the **declared bounded** client observer and whose final state satisfies D certifies *existence of a path relative to the tested observer* and upper-bounds the optimal synthetic cost:

  K_E_pi(A,D|C) <= c(p)

But this does not certify that the minimum is exactly c(p). A lower bound K >= L requires exhausting every cheaper authorized path OR a sound abstraction / simulation argument excluding all such paths. A finite three-switch search only proves a minimum among its eight configurations.

## Under-specification of edit relation

If E_small subset E_large, then K(E_large) <= K(E_small), with infinity for infeasible. Restricting the repair grammar can artificially raise reported minimum cost and render a generally possible repair 'impossible'. Likewise restricting the client observer can certify a false 'safe' path.

Therefore a pair of opposing monotonicities matters:
- extending permissions/edits cannot increase minimum scalar cost (when changes preserve existing costs and outcomes);
- extending protected client observations cannot enlarge the set of admissible safe paths.

The second statement presupposes a fixed transition semantics and observer-satisfaction predicate; it is a classical set-inclusion theorem, not proprietary EAC novelty.

## Necessary certificate metadata

1. Frozen source revision, dependency hashes and fixture vs maintained-source distinction.
2. Observational scope and evidence that each certified path prefix passed it; note unobserved client contexts.
3. Permission/right semantics, edit granularity and all excluded classes of actions.
4. A constructive repair path with per-step source patches, tests and costs for upper bounds.
5. A lower-bound witness: exhaustive finite search with completeness of repair grammar OR a separately verified sound symbolic proof.
6. Competing classical exact/overapproximate analysis on equal source/rights/observer information and computational budget.
7. Cost units separately for synthetic edit count, CI/tests, changes, human effort (missing unless observed).

No general lower-bound/minimum maintainability claim until (5) is discharged. P44-R1's minimum cost=3 is valid ONLY within the named three-bit grammar; P44-R3's one-unit bridge is an exhibited repair, NOT a global one-change optimum.
