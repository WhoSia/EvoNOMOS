# Chat 26 — Evidence-Relative Fixed-Patch Judgement: Exact Bounded Court

## Scope and source grounding

Paper B v16 §5 examines a *fixed* library patch. Its observed behavior supports technical reports, still rejects errata, and changes the historical book-output prefix from \`book\` to \`BOOK\`. The research authors stipulate two prospective requests and two old-client protection scopes. It does **not** record real reviewers accepting this patch.

Worlds \`w=(E,B)\`, where E=1 iff errata support is required and B=1 iff the old book prefix is a protected contract. **Within this four-world stipulated court only**, a candidate is acceptable exactly when \`¬E ∧ ¬B\`. No source-level general OCP checker or actual human acceptance observation follows.

## Information-state judgment

Let \`W\` be the four finite worlds; evidence \`e\` selects the compatible version space \`V(e)⊆W\`. A fixed patch predicate \`A(w)\` returns one accepted/rejected outcome in a *fully specified* world. Define

- \`ACCEPT(e)\` if \`V(e)≠∅\` and \`A(w)\` is true for every \`w∈V(e)\`;
- \`REJECT(e)\` if \`V(e)≠∅\` and \`A(w)\` is false for every \`w∈V(e)\`;
- \`HOLD(e)\` if \`V(e)\` contains both labels;
- \`INCONSISTENT(e)\` if \`V(e)=∅\`.

These are epistemically robust verdicts **relative to a declared finite candidate specification set**, not an estimate of actual review behavior.

### Complete finite court

| Known errata required? | Known book protection? | Verdict |
|---|---|---|
| unknown | unknown | HOLD |
| unknown | yes | REJECT |
| unknown | no | HOLD |
| yes | unknown | REJECT |
| yes | yes | REJECT |
| yes | no | REJECT |
| no | unknown | HOLD |
| no | yes | REJECT |
| no | no | ACCEPT |

Thus 9 disclosure states yield exactly **1 ACCEPT / 5 REJECT / 3 HOLD**, matching the fixed authored example. A contradictory disclosure must **not** be vacuously accepted/rejected.

## Classical theorem: evidence-refinement stability

If new evidence is consistent and only eliminates candidate worlds, \`V(e')⊆V(e)\`, an existing ACCEPT or REJECT verdict is stable: the universal truth value cannot reverse over a subset. A HOLD may become ACCEPT, REJECT or stay HOLD. Proof is immediate from subset inclusion. If the *normative contract itself is changed* (rather than learned), or the patch changes, this theorem does not apply. It does not justify unsafe real-world approval when \`W\` omitted plausible contracts.

## Classical theorem: one-question decision sufficiency

A binary question \`q\` settles a HOLD under every possible answer iff every nonempty answer fiber is uniform in \`A\`. At no disclosure, asking only whether errata are required leaves the report-only branch in HOLD; asking whether books are protected leaves the unprotected branch in HOLD. After confirming report-only, the book-protection question splits ACCEPT/REJECT. The algorithm \`reveal\` yields exact conditional verdicts, not a new discovery in decision theory.

## Independent executable fixture

\`contract_judgment.py\` implements these semantics; \`test_contract_judgment.py\` encodes the 4-world truth table, all 9 states, contradictory evidence, one-question outcomes and exhaustive evidence-monotonicity. Until CI actually runs, code commit is **not** test evidence.

## Why this matters to EvoNOMOS

The same missing-contract distinction that forces HOLD on fixed-patch approval can force ABSTAIN on an architecture ranking if initial behavior is unmatched under a candidate customer observation. Unlike Paper B's authored four worlds, P44 must ground feasible versions and their contracts in *real source, authorized edits and an independent task*. Source semantics and the prior-art limits are not replaced by the truth table.
