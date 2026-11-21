# Chat 26 — Minimal Evidence Certificates and Question Costs

**Status:** Exact finite and classical Boolean reasoning, based on Paper B v16's researcher-authored four-world fixture. No observed reviewer behavior or new LAW-R2 claim.

## 1. Precise two-fact model

Let E mean “the requested patch must support errata” and B mean “the old book-output prefix is protected.” The fixed patch supports reports, not errata, and changes the book prefix. Its acceptance under these authored obligations is A(E,B) = not E AND not B.

For the evidence-compatible set V of worlds:
- ACCEPT if V is nonempty and every member satisfies A.
- REJECT if V is nonempty and no member satisfies A.
- HOLD if both accepted and rejected worlds remain.
- INCONSISTENT if V is empty, rather than treating a universal quantifier over empty set as safe approval.

## 2. Exact minimal certificates

The unique inclusion-minimal acceptance certificate is {not E, not B}. The two distinct inclusion-minimal rejection certificates are {E} and {B}.

Proof: E alone or B alone makes A false for every value of the other variable. Conversely, neither partial negative observation by itself can force A true: an adverse completion of the unknown fact still rejects. The empty set does not force a verdict. Exhausting four worlds shows no other minimal certificates.

The independently implemented enumeration and ambiguity-countermodel functions in decision_certificates.py check the finite claim. A HOLD is paired with two compatible worlds reaching opposite judgments; contradictory evidence is excluded.

## 3. One-step question sufficiency

From no information, asking whether errata are required yields REJECT if E=true, but HOLD if E=false because B remains unknown. Asking about B behaves symmetrically. Thus neither individual binary question guarantees resolution from the fully unknown state. Once report-only (not E) is known, asking B always settles the decision.

General finite criterion: question q is one-step sufficient iff all its nonempty answer fibers are uniform in the patch predicate. This is familiar decision tree/version-space theory, not a novel theorem.

## 4. Expected query cost (assumed, not observed probabilities)

Let pE and pB be the *investigator-supplied marginal* probabilities of E and B respectively. If a positive answer immediately rejects, asking about E first uses expected 2-pE binary questions; asking about B first uses expected 2-pB. Therefore E-first minimizes question count if pE>=pB, B-first if pB>=pE, both tied at equality. No independence assumption is necessary for these short-circuit question counts. Unequal question costs, unreliable answer sources or actual human inquiry efforts require a different model.

Worst-case acceptance needs two negative facts (hence two yes/no questions) in this stipulated fact vocabulary.

## 5. Three different transitions that must not be conflated

- Evidence update: learn facts while fixed patch, obligations and candidate-world set stay fixed; evidence removes worlds, robust verdict is stable.
- Normative contract revision: changing legitimate obligations changes the actual requirement and can reverse a previous verdict.
- Source repair: changing code alters patch behavior and the evaluation predicate; it is a different transition and needs Go source and owner-right evidence.

These distinctions matter for Paper B and P44 but neither establish industrial over-axiomatization frequency nor source-level architectural superiority.

## 6. Scope gate

The 4-world fixture does not cover every real customer requirement; the computed verdicts are not observations of human code reviewers; these scripts do not run the real example application; no source-aware classical superiority has been tested. Preserve LAW-R2 HOLD. A next valid step would connect authentic externally authored contract facts (with provenance and uncertainty) to an independent source repair, not simply enlarge this toy truth table.
