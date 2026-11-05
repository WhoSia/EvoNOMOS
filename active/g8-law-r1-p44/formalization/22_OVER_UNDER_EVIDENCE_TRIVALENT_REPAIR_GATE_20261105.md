# F13 candidate: separate correct-safety proofs, incorrectness witnesses, and unknown states

2026-11-05. This is a **classical logical refinement for the P44 problem**, motivated by direct reading of O'Hearn 2020, Incorrectness Logic and the earlier CEGAR, separation logic and source alias courts. Not claimed novel.

## Finite source-release execution semantics

For a fixed source release p, environment e and declared joint observer O, let T(p,e) be the set of feasible source traces. Let C(t) mean protected client contract holds on trace t.

- Universal SAFE(p) means for all relevant e,t in T(p,e), C(t).
- Existential BAD(p) means exists relevant e,t in T(p,e) with not C(t).

Construct a sound **overapproximation** U_p such that T(p,e) subset U_p for every declared environment. If every trace in U_p satisfies C, then SAFE(p) is PROVED.

Construct a sound **underapproximation** W_p of realizable traces such that W_p subset T(p,e) for a valid declared environment. If a trace in W_p violates C, then BAD(p) is PROVED.

If neither source-sound proof exists, verdict UNKNOWN. A sample of good executions yields neither general SAFE nor proof of absence of errors. A spurious abstract bad trace in U_p is not a genuine incorrectness witness. Conversely, a sample of bad executions must be source-reproducible and belong to the declared client observer domain before claiming a repair failure.

SAFE and BAD are mutually exclusive only if the sources and environments are fixed, C is total and trace semantics is consistent. A checker receiving both genuine proofs must reject the inconsistency, not silently prefer the latest result.

## Effect on staged repair certificates

For a proposed authorized source-edit sequence h=(p0,...,pn), all protected release/checkpoint states require SAFE under already activated contracts before calling the **whole path** certified safe. One BAD checkpoint refutes safety of that path, but does NOT prove that no other authorized safe repair exists. One UNKNOWN checkpoint forces the safe-path certification UNKNOWN; it is not a failed source edit.

For impossibility / minimum cost across all possible source edits, this runtime trace logic is NOT enough. Separately require completeness of allowed source-edit grammar and sound coverage of every cheaper candidate path. Source-soundness of observed trace overapproximation (all schedules/contexts) and source graph completeness are different proof obligations.

## Finite model and limitations

The Go finite reference checker [evidence/oracle.go](evidence/oracle.go) accepts explicit UnderCertified and OverCertified booleans whose evidence must come from **outside this tool**. Its VerifyFiniteCoverage routine can check those assumptions only because a tiny supplied full ground-truth trace set exists for the toy fixture. For real Go source, a flag set to true is NOT proof that the trace universe has been covered. Go test green = finite reference logic correct, not source-complete audit. Explicit negative controls: phantom bad trace, missed bad runtime trace, success-only underapprox cannot prove universal safety, unauthorized edit, unsafe intermediate checkpoint, conflicting proof badges.

## Highest-priority scientific next step

Construct a genuinely **source-sound bounded observer semantics**, e.g. a small typed Go subset with closed finite input/scheduler and fully specified edit policy, then derive U_p and W_p with machine-checkable inclusion proofs. Couple it with F12 edge-local source-edit certificate only after both (A) source edit completeness and (B) runtime trace coverage are separately shown. Benchmark with classical abstract interpretation, incorrectness logic, model checking and exact finite search. G1-G7 OPEN, LAW-R2 HOLD.
