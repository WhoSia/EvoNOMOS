# P44 F15 — joint input/output source semantics and complete two-literal edit graph

Research date 2026-11-05. The user wants continual research, falsifying backward audit, and source results rather than renaming known theory.

## Strict source language

Single comment-free Go source file, exactly `package fixture`, declarations `func Legacy() string { return "stable" }` and `func Future(flag bool) string { if flag { return "t" }; return "f" }`, where t,f are valid Go string literals in a FIXED finite policy domain D of cardinality m. No imports, free variables, additional declarations, function calls, control effects beyond this if, comments, build tags, runtime environment, goroutines or hidden build context. Source actor can only replace either Future branch's string-literal return with a declared alternative. Cost: 1 per nonidentity branch edit; unchanged source costs 0. A separate policy must specify the initial source state, build context and approved client flags.

Define source state (t,f), joint legacy+future observation for input flag true as (stable,t) and for flag false as (stable,f).

**Classical relative edit completeness:** There are exactly m^2 distinct output-semantic states (some text formatting differences intentionally identified), and 2m²(m−1) authorized nonidentity directed edit transitions, each changing exactly one of the two literal positions. Proof: m choices per position; from each pair, m−1 destinations on the true branch and m−1 on the false branch. `go/parser` AST pattern matching and `go/format` reserialization together construct each syntactically permitted transformed source, then reparse to check grammar closure. Native Go runtime tests are required separately to corroborate the denotational input-output interpretation for all enumerated source values in the TEST domain.

For D={off,on,beta}: 9 source states, 36 directed transitions, each with cost 1. Exact conventional BFS graph oracle finds cost 2 to move (off,on)→(beta,off); an EAC certificate has not improved accuracy, proof size, or CPU over the exact classical method.

## Critical observer counterexample

States (off,on) and (on,off) have the SAME marginal set of outputs {off,on}. But the joint input-output relation differs:
  flag=true: off vs on,
  flag=false: on vs off.
Therefore a model preserving only the OUTPUT SET can falsely certify backward compatibility when an input-conditioned customer contract was broken. This countermodel is independent of multi-stage CSP and does not establish novelty over standard relational/contextual equivalence. It is a useful necessary observer-granularity test for any P44 source certification.

## Limits

The observer is exact only for this single conditional return grammar. It cannot reason about aliasing, HTTP routers, concurrency, callbacks, imports, multiple packages, reflection, interactions or full-go code modifications. The legal source-edit universe is declared by hand and may omit what real human developers can modify. Tests of native compilation/observations do NOT themselves prove the compiler semantically correct for ALL possible Go texts; they establish empirical consistency on the enumerated chosen finite domain. The theorem's completeness follows from a deliberately total grammar; it is NOT a whole-program automatic source completeness theorem.

## Scientific gates and prior art

White et al. 2009 base MUSCLE/SPLC multi-step feature configuration; 2012 submitted manuscript; White et al. 2014 JSS drift/constraints; exact graph search/CSP and O'Hearn correctness/incorrectness remain strong alternatives.

**CI execution**: initial GitHub workflow run #41961920487 FAILED due to malformed Go test fixture string escaping, not due to mathematical counterexample. The failed original CI remains part of audit provenance. Fixed in a separate source commit; a later successful CI run (if verified) must be recorded with exact SHA and raw logs. No arbitrary Go source soundness or LAW-R2.
