# P36 — Four Real-Source Repair Candidates and Their Future-Demand Survival Filtration

**2026-10-10 KST · Research record, P36 OPEN.** This study is a **finite source-candidate filtration**, not a discovery of a universal new law.

## Why this matters for actual software design rather than just Go testing

Earlier P35-MATH-1 studied the filtration of *behavioral equivalence classes* under longer future action words. P35-MATH-2 modeled authorized repair as a **set-valued relation**, with nonvacuous May/Must, and MATH-3 checked **selected** source change-order witnesses rather than claiming confluence. P36 now joins these: how the admissible **finite portfolio of actual Go repair structures** shrinks as new independent demand words and prefix tests are imposed. A patch's old Go PASS is an existential *present* proof, not evidence of universal future survival.

Fix a pinned upstream source A, a frozen finite authored repair portfolio `Γ_obs`, future demand sequence `d_1,...,d_k`, and a growing conjunction of prefix-correctness oracles `Q_{≤j}`. Define
```
V_j(A;Γ_obs) :=
  { B in Γ_obs(A) : Q_≤j(B) = PASS on the pinned original Go world }.
```
If `Q_≤j+1` includes all tests in `Q_≤j`, then `V_{j+1}⊆V_j`. This is **definitionally monotone**, not a new theorem. Strictness `V_{j+1}⊊V_j` needs a specific real Go source survivor and a newly refuted candidate for that step. It does not follow from architecture labels, SOLID compliance or a few selected successes.

## Actual source candidates and the sequential experimental history

All four are separately committed project research extensions to the same pinned original `go-chi/chi v5.1.0@67be7d9cafdaeb4e04e887ff78d09e030ee43b00`. They were **not** randomly sampled from all patch families; later candidates were designed informed by earlier failures, so this is sequential adversarial construction, not prospective blind ex ante prediction of all four.

| Repair variant (literal source path) | Mechanism and retained data | D14 current disable | D15 future single restore | D16 future double restore | D17 cyclic restore |
| --- | --- | --- | --- | --- | --- |
| [ERASE](../../tools/p36-o3/arms/chi/erase/p35_epoch_router.go) | physically discard original middleware closure | native PASS | expected-negative original native | not needed for membership | not needed |
| [POSITION_INDEX](../../tools/p36-o3/arms/chi/retain/p35_epoch_router.go) | retains original middleware closure; records deletion-time *mutable index* | native PASS | native PASS | expected-negative original native (`got B, want A`) | not needed |
| [RELATIVE_REBASE](../../tools/p36-o5/arms/chi/relative-rebase/p35_epoch_router.go) | retains middleware closure and deletion index; rebase remaining disabled indices on restoration | source authored; native PENDING | source authored; native PENDING | source authored; native PENDING | expected-negative native pending |
| [STABLE_ORDER](../../tools/p36-o4/arms/chi/stable-order/p35_epoch_router.go) | retains closure and immutable ordinal; restores by ranked position | native PASS | native PASS | native PASS | native PENDING |

D14 and D15 test source commits predated O3 treatment source. D16 was presealed and test committed before O4 STABLE_ORDER. D17 was presealed and test committed before O5 RELATIVE_REBASE. Previously frozen Go tests remain unchanged across follow-up courts. Later source repairs are post-treatment to prior demands but prospective against the *newly frozen* future demand test.

**Verified original native receipts:**
- [O3 D14/D15 Chi source 2/2 SUCCESS #37961233537](https://github.com/WhoSia/EvoNOMOS/actions/runs/37961233537): ERASE D15 expected failure; RETAIN D15 PASS, with full Go/race/vet.
- [O4 D16 Chi source 2/2 SUCCESS #37964693435](https://github.com/WhoSia/EvoNOMOS/actions/runs/37964693435): original positional source D14/D15 PASS then D16 expected failure in two worlds at second restoration `got B, want A`; stable ordinal source D14/D15/D16 PASS. Artifacts `11632339441` (POS, ZIP SHA256 `c3b4c43da502c1c47293a6273dd49a05db28e3df16f0001866fb00847757d45d`) and `11632764217` (STABLE, ZIP SHA256 `4908cc7db7e8603f2a51025aa38ae520afd26234db7357044c5cf37b9756b0ea`). Frozen D16 test source SHA256 `02c728670dd457c1db042baf629bc115b757497d57812a35226e7542399c5988`. Original Chi full Go/race/vet and previous D14/D15 PASS for both.
- [O5 relative-index vs stable-ordinal native #37965392085](https://github.com/WhoSia/EvoNOMOS/actions/runs/37965392085): **IN_PROGRESS at this inscription**; do not claim D17 native outcomes yet.
- [P36 O3 classical erased-history theorem #37961481644](https://github.com/WhoSia/EvoNOMOS/actions/runs/37961481644) **SUCCESS**, and [MATH-4 classical forgetful simulation #37964349042](https://github.com/WhoSia/EvoNOMOS/actions/runs/37964349042) **SUCCESS** with Lean checker. Neither formally verifies the actual arbitrary Go source representation invariant.

## Mechanism taxonomy from the source, not law inflation

1. **Value erasure:** ERASE loses the original middleware closure; without an authorized log or re-registration, D15 is not recoverable in the narrow current-state-only contract. Existing noninjectivity and program repair theory.
2. **Relational position instability:** POSITION_INDEX retains the closure but maps it to an index whose *referent changes when another entry is deleted*. Two different records both save `index=0`; FIFO reenabling can reverse original precedence. Existing stable-ID/order-maintenance theory.
3. **Incomplete transition coverage:** RELATIVE_REBASE may fix the immediate D16 two-restoration case by shifting suspended indices on **restore** but fail D17's disable/restore **cycle** because it does not preserve a global invariant over both classes of action. This is a **hypothesis until CI readback**; classical representation invariant restoration predicts such risks.
4. **Ordinal invariance:** STABLE_ORDER uses monotonically increasing IDs stable across list mutation. This suffices for the D16 fixed oracle, and hypothesized for D17, but **may have its own failure under a different insertion/priority policy**. It is not proved necessary nor universally correct.

These are increasingly demanding **real source examples** of behaviors that cannot be inferred from present HTTP output alone. They do **not** establish that all repair grammars have the same strict filtration, that a tiny Go test suite gives universal correctness, or that retained information and relational information are exactly equal across candidates.

## Strong established rival and direction beyond it

Program repair overfitting (Qi et al. ISSTA 2015), continuation equivalence (Myhill–Nerode), data structure invariants, stable entity IDs, order maintenance, information refinement and amortization account for all current results. The mature next question is not 'do IDs win?' but:
- Which *specified structural invariants* actually predict the survival set `V_j` on **independent evolved code topologies** and genuinely unseen future demands, better than source-aware classical rivals?
- Does a representation invariant explain multiple independent change generators beyond the one constructed route family? If not, record domain-specific mechanic rather than 'software design law'.
- When cost/resource budgets and edit-authority restrictions are held equal, can two variants *with the same information available* have different reachable future repairs under a real (not contrived) source-edit grammar?
- What is the strongest classical countermodel to each proposed law? Preseal a query for which signatures differ rather than presenting the same standard prediction as novelty.

**P36 stays OPEN, P35 stage CLOSED. DIP49 strong model-pair identification HOLD. LAW-R2 NOT_AUTHORIZED.**
