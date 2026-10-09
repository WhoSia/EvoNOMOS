# P36-O5 — Relative-Position Repair, Cyclic Restore and the Boundary of Local Index Rebasing

**2026-10-10 KST · PRE-SOURCE SEAL.** P36 active. O4 original Chi native [#37964693435](https://github.com/WhoSia/EvoNOMOS/actions/runs/37964693435) ended 2/2 SUCCESS: old O3 RETAIN position-index source kept all frozen D14/D15 but failed D16 exactly at second restore, `got B / want A`; source with permanent per-registration ordinal passed D14/D15 and both D16 scenarios. All original Chi full/race/vet PASS. This is a **post-O4, pre-O5** adversarial extension, not a newly blind prediction about O4.

## Competing source-level repairs to D16

An immutable registration ID is a sufficient repair in O4, but a code change might preserve the D16 2-disable-2-restore contract **without permanent identity tokens**:
- `RELATIVE_REBASE`: retain original O3 disabled middleware closures plus per-route deletion-time `index`, but whenever a route is restored at index i, increment the stored indices of *remaining disabled routes from that header* at or after i. Predict this simple local coordinate update passes D14/D15/D16, but the next cyclic action can still break the global historical priority relation.
- `STABLE_ORDER`: immutable increasing registration order as in [O4 source](../../tools/p36-o4/arms/chi/stable-order/p35_epoch_router.go). Predict D14/D15/D16 and the new D17 PASS.

Both treatment sources are *project-authored additions to original pinned Chi*, not independently evolved historical OSS choices.

## New, separately predeclared **D17** future sequence

Same exact header match and initial three handler registrations A,B,C with priority A>B>C. All middleware values/closures are retained by BOTH implementations; this neutralizes O3 ERASE's trivial lost-data mechanism. With exact-match `DisableRoute` removing the first currently enabled rule, and `EnableRoute` restoring the **earliest disabled still pending**:
1. Disable A, now B serves.
2. Disable B, now C serves.
3. Enable A, now A serves. This is the earlier D16 **prefix**. Index-rebase strategy is expected to have updated B's stored index from 0 to 1.
4. Disable A **again**, now C serves. The pending disabled queue is B(index=1), A(index=0). These are the same logical records but from different disable eras.
5. Enable B, require B serves (before original C): this is the **new D17 discriminating observation**. Naive local rebase instead inserts B at current index 1 after C, so C incorrectly serves.
6. Enable A, require original priority A again. Repeat with an optional new handler D appended between steps 2 and 3, confirming that a later registration does not take over an earlier route.

Each step has completed-registration visibility and publication/revision checks; new field/handler APIs not introduced. Freeze tests BEFORE writing any O5 treatment. This is a repair option survival problem under a cyclic **source-development action word**, not a new unrelated grammar or retrospective D16 alteration.

## Mathematical target and classical rival

The shift in index bases after deletion and reinsertion is not a stable equivariant group action on the old priority order when pending disabled records span several deletion/restoration epochs. Rebasing only on **one type of transition** (restore) may be enough for one D16 trace but fail a D17 cyclic trace. This is classical order-maintenance/invariant restoration; a comprehensive local rebase algorithm could maintain the order without global IDs. **Do not claim stable unique IDs are necessary** or that the candidate RELATIVE_REBASE exhausts no-ID repairs.

Hypotheses preregistered:
- `H_local_simple` (deliberately fragile): adjusting deferred indices after each restore suffices even under D17 cycles.
- `B_action_invariant` (strong classical): each update operation must preserve an invariant relating current slice, pending disabled records and original priority; one-sided updates can lose coherence after cycles. Predict RELATIVE_REBASE D17 FAIL, STABLE_ORDER D17 PASS. Unlike a straw null, B is a standard representation-invariant explanation and is favored by source inspection before measurement. Successful B confirms classical knowledge, not a beyond-SOLID law.

`DIP49` *novel* rival pair still not separated. O5's valuable result is an actual composed-action counterexample that rejects a simplistic sufficient-condition candidate while establishing provenance of multiple genuine repairs, not a slogan.

## Test and CI gate

Use original `go-chi/chi v5.1.0@67be7d9cafdaeb4e04e887ff78d09e030ee43b00`, unchanged O6 frozen traces and unchanged D14/D15/D16 tests. Before D17, both candidates must native PASS D14/D15/D16, `go vet ./...`, `go test -race -count=1 ./middleware`, full upstream `go test -count=1 ./...`. After adding frozen D17 test, expected:
- RELATIVE_REBASE deliberate D17 test failure identified by `P36_O5_D17_CYCLIC_PRIORITY_FAILURE`;
- STABLE_ORDER D17 PASS in all frozen worlds.
Record raw job logs and hashes, do not change any frozen test after seeing results. Failure on D16 is a **source defect** in RELATIVE_REBASE requiring repair; never relabel it as the planned D17 negative.
 
**Pre-source verdict**: `P36_O5_D17_PRESEALED__TWO_INFORMATION_RETAINING_REPAIR_STRUCTURES__EXPECTED_LOCAL_REBASE_COUNTEREXAMPLE__NATIVE_UNVERIFIED__LAW_R2_NOT_AUTHORIZED`.
