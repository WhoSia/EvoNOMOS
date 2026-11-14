# P44-F33 — Source-Backed Repair-Lift Certificate: Proof Obligations and Adversarial Court (protocol v0.1)

Status: DESIGN / NOT EXECUTED / LAW-R2 HOLD. Date: 2026-11-09.
Parent: F30 local effects, F31 frozen Go build closure, F32 weighted finite graph lift checker. This note adds **no new validated source claim**. All thresholds are prospective and must be frozen prior to outcome inspection.

## 1. Question and epistemic separation

Can a certificate derived from a **fixed, complete Go source/build snapshot**, plus explicitly sourced edit permissions, soundly establish that a future contract-preserving edit path is realizable at no greater than a stated cost, for all concrete versions in a specified abstraction fiber?

Evidence tiers must not be conflated:
- mathematical implication under stated transition completeness: a theorem;
- bounded model and synthetic adversarial fixtures: tests of an implementation;
- original Go source and actual compilation: source evidence only;
- historical maintainer record: retrospective evidence, not permission authentication;
- prospective demand, held-out outcome and matched baseline: predictive evidence.

## 2. Formal bounded claim

Let C be concrete states (source tree, frozen build closure, ownership evidence, current client contract), A abstract interface/contract states, and α:C→A. For actor o and demand d let E_C(o,d) and E_A(o,d) be *declared* allowed directed edits with nonnegative costs w_C,w_A. Let H_C and H_A be corresponding demand-satisfaction predicates.

**Conditional upper-bound lifting obligation** for every reachable concrete c in the declared domain and every abstract edge α(c)=a → a' allowed by (o,d): find c' such that c → c' is permitted, α(c')=a', w_C(c,c') ≤ w_A(a,a'); additionally ensure H_A(α(c)) implies H_C(c) when accepting terminal nodes. This is a total forward edge-lifting condition over the **enumerated domain**, not over arbitrary Go programs.

**Lemma (bounded abstract-path realizability).** Under the edge-lifting obligation and accepting-node implication, each finite abstract path a0→…→ak starting at a0=α(c0) admits a concrete path c0→…→ck with α(ci)=ai and sum w_C ≤ sum w_A. Proof: induction on path length. The terminal predicate transfers by the accepting-node implication. Consequently K_C(c0,d) ≤ K_A(α(c0),d) when K_A is attained and feasible, for the same fixed actor/demand and matching target predicate. If K_A=∞ this comparison carries no feasibility information. This upper bound fails if the edge relation is an incomplete approximation, the ownership assumption is false, or labels/acceptance change along the path.

**Do not invert this implication.** The reverse lower-bound K_A≤K_C needs projection of concrete steps (including any stuttering/cost accounting) and compatible acceptance, as independently addressed in F32.

## 3. Minimal falsification cases, all pre-declared

C1 — Fiber loss: two versions open/closed map to the same abstract API; after edit A, B remains abstractly available but is absent from closed. Expect upper lift REJECT with precise missing edge.

C2 — Rights mismatch: the concrete edit exists but the named actor lacks authenticated permission. Expect HOLD unless rights evidence is present, then REJECT when denied. A Git author field alone does not authenticate rights.

C3 — Cost mismatch: witness exists but concrete cost exceeds abstract bound. Expect upper lift REJECT with cost witness.

C4 — Build-scope drift: Go build tags, symlink, hidden source or changes to go.mod invalidate the frozen closure. Expect HOLD/REJECT according to declared admissible language; never PASS solely on go test.

C5 — Aliasing: a nominally local edit mutates client-visible shared state through an alias. Expect source effect certificate to fail or abstain.

C6 — Demand persistence: a later edit satisfies demand B but destroys previously protected contract A. Expect REJECT when cumulative contracts are part of the frozen demand predicate.

C7 — Partial source: missing dependency/revision/CI provenance. Expect HOLD, not a proof of impossibility.

C8 — Baseline parity: classic SSA/alias, CEGAR, rely–guarantee or bounded model checking with identical evidence reaches the same claims at equal/lower cost. Expect TIE/LOSS; novelty remains HOLD.

## 4. Source-evidence protocol

1. Freeze repository URL, branch, full commit SHA, submodules, Go version/toolchain, build tags/environment, source-tree hashes and dependency lock/sums. Record a byte-complete manifest of the admitted build closure; mark external undeclared sources as HOLD.
2. Preseal an edit grammar, actors/permissions source with timestamp, protected clients and demand predicate. Treat rights that are merely self-reported as an explicit assumption, not independently validated authorization.
3. Derive candidate alpha, edits and costs from the snapshot, marking every inferred edge and every missing/unknown edge separately. **Never assume all real edits have been enumerated without a completeness proof.**
4. Produce local source facts (type/SSA/alias/effects), link to edit witness source diffs and compile/test each witness when admissible. Compilation/testing provides only bounded evidence, not universal semantic safety.
5. Run the F32 checker only on the finite domain actually enumerated. Each outcome must contain PASS_WITH_ASSUMPTIONS, COUNTEREXAMPLE, or HOLD, with precise boundary and a checkable replay script.
6. Independently reproduce using matched-information conventional baselines and blind held-out future demands. Publish counts of abstentions, cost and counterexamples; do not remove failures.

## 5. Pre-registered evaluation table (not yet measured)

Fields: cohort_id, frozen_commit, source_manifest_SHA256, actor_rights_source, client_observer, demand_preseal_time, edit_grammar, candidate_claim, proof_grade, compilation_result, regression_result, baseline_claim, baseline_cost, certificate_cost, witness_or_counterexample, leakage_audit, decision.

Primary endpoints: calibrated soundness on the admitted source/demand domain, demand-level coverage (including abstentions), matched baseline advantage, and end-to-end cost with failure/triage included. All empirical results are pending.

## 6. Novelty gate

The induction lemma and weighted transition matching are classical. Novelty would require a nontrivial **sound extraction** theorem for useful real source families, an independently reproducible prospective advantage over equal-information classical tools, or both. No upgrade to categorical (op)fibration is warranted without universal opcartesian factorization. No upgrade to LAW-R2 from synthetic or retrospective successes.

NEXT: construct the source-derived C1/C2/C5 fixtures from immutable original Go trees, freeze baseline tool versions, then run falsifiers before positive examples.
