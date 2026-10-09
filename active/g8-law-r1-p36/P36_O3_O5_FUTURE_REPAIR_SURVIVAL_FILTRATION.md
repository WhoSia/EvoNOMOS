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


## 2026-10-10 — O5 Native Post-Preseal Readback and Strict Four-Repair Survival Chain

This section is **after** the O5 source and D17 oracle were frozen. Do not silently change earlier pre-result declarations.

[Original pinned Chi native Go CI #37965392085](https://github.com/WhoSia/EvoNOMOS/actions/runs/37965392085) completed **SUCCESS**, both matrix jobs. Each original-source variant passed existing upstream full Go, race/vet, **and the unmodified old D14/D15/D16 frozen tests**. Then independently presealed D17 was applied:

- **RELATIVE_REBASE**: exact original-source artifact id `11633034916`, ZIP SHA256 `47a447a1fd597835f03cd26b8788d0d41901da5c172ab6b42d3bb339563bc187`. Old D14/D15/D16 PASS. D17 **expected negative** in both worlds, with literal native log `P36_O5_D17_CYCLIC_PRIORITY_FAILURE action=restore_B got="C" want="B"`. Source SHA256 `e377097f669b2edc1037cc9a87e95ed067d365b2602c0f5086c9c195218d16d6`.
- **STABLE_ORDER**: artifact id `11633141469`, ZIP SHA256 `238e2a029395643831b291330afe692ce9526aa06fd81e52cee73c15b81e27ba`. Old D14/D15/D16 PASS and new D17 PASS both worlds. Source SHA256 `0733318f9e18ec2df88d5025783a8d4e3fc18f39d99cf1e80473dd65d54086bc`. Both arms used exactly the same D17 oracle SHA256 `63a87c9f3ad6a3d1bfd9c1bc3fd98e95ed7dcc9b9295eff7a63ae4dd8f38aff3`.

The now-verified **restricted four-source survival filtration**, with frozen cumulative prefix test suites, is strictly nested:
```
V_D14              = {ERASE, POSITION_INDEX, RELATIVE_REBASE, STABLE_ORDER}
V_D14+D15          = {POSITION_INDEX, RELATIVE_REBASE, STABLE_ORDER}
V_D14+D15+D16      = {RELATIVE_REBASE, STABLE_ORDER}
V_D14+D15+D16+D17  = {STABLE_ORDER}.
```
This is actual original-Go native test evidence over *four intentionally constructed source candidates*, **not** a demonstration that all possible edits inhabit this chain. The independent future requirements were created sequentially *after examining earlier source failures*; the test-source chronology was prospective for each respective repair, but the full chain was **not** blind sampled from real future user demands. The eventual stable candidate has not yet passed unbounded traces or an independent reference beyond these selectively constructed tests.

## O6 independent finite maintenance-automaton challenge

To attack source-induced selection, a separate after-source [O6 preseal](P36_O6_FINITE_MAINTENANCE_AUTOMATON_PRESEAL.md) and [standalone reference-model test](../../tools/p36-o6/tests/chi/p36_o6_finite_action_reference_test.go) were committed **after** the O3–O5 implementations, without any new treatment source. All `1+3+9+27+81+243+729=1093` action words of lengths 0..6 over `R=RegisterNew,D=DisableEarliest,E=EnableOldestDisabled` are prospectively fully enumerated, reference uses a logical ordered list+FIFO pending IDs, independently of source indices/ordinals. [Original Chi four-arm CI #37966139703](https://github.com/WhoSia/EvoNOMOS/actions/runs/37966139703) is currently **QUEUED**. A pass here can certify only the declared finite action alphabet and depth, not universal model checking.

**Status now:** `O3_O4_O5_NATIVE_STRICT_FOUR_ARM_FILTRATION_CONFIRMED__O6_EXHAUSTIVE_1093_SOURCE_GO_PENDING__DIP49_NOVEL_PAIR_HOLD__LAW_R2_NOT_AUTHORIZED`.


## 2026-10-10 — O6 complete, original Go finite-depth conformance verified

[O6 original Chi four-arm full Go/race/vet + independent logical reference #37966139703](https://github.com/WhoSia/EvoNOMOS/actions/runs/37966139703) completed **SUCCESS (4/4 jobs)**, with strict historical preservation of all frozen earlier source variants. Reference Go oracle source SHA256 `49c49090ff7c0093f9fa08dea8a19055bf2c60a41eca4a72d1d6e71346319079`. The action alphabet was fixed `Σ={R=register new, D=disable earliest, E=enable oldest pending}`, initial same-header A>B>C, and all 1093 words of length 0–6 enumerated shortest first. The oracle used an independent logical entry-order list and FIFO queue and compared method return, published revision and HTTP response on every prefix.

| Original source treatment | First incorrect word, found shortest-first | Native mismatch | Actual ZIP artifact & SHA256 |
| --- | --- | --- | --- |
| ERASE | `DE` length 2 | `Enable actual=false ref=true` | 11633626650, `352b99751906a5506de6d113397f4464b705fe25ebedc01a432311e87743f56a` |
| POSITION_INDEX | `DDEE` length 4 | `HTTP actual=B reference=A` | 11633831407, `25f8a8180e8bc282c9bbf0787bd7b8ebccfd220e4f77980a3bb08afcc1992e33` |
| RELATIVE_REBASE | `DDEDE` length 5 | `HTTP actual=C reference=B` | 11633741513, `d356e18bb56ad417519f76b829da27d71246a41966caecf6f950a66e46f4e411` |
| STABLE_ORDER | **none at length ≤6** | **all 1093 words and every prefix PASS** | 11633242485, `4d840ab25fbe9a3c919eb10b5aa6250b9bf2e1d681997e7bd6b95d081492c3ea` |

**Crucial distinction**: the three negative arms did NOT execute all 1093 words: the frozen test stops at its first counterexample. Because words are enumerated by increasing length with no prior failures, the counterexample length is a verified **minimal failing length** within the given finite alphabet and initial state. The STABLE_ORDER positive arm alone exhausted the entire 1093-word domain. Nothing proves unbounded behavior, all action alphabets, all initial registries or all real software contexts.

This yields bounded empirical `d_Σ(ERASE)=2`, `d_Σ(POSITION_INDEX)=4`, `d_Σ(RELATIVE_REBASE)=5`, and `d_Σ(STABLE_ORDER)>6`, where `d_Σ(B)=min{|w|:O_w(B) differs from fixed reference}`. **Do not turn this test-relative depth into a universal structural quality score.**

### Two same-current-observer histories separated by a one-step future action

[MATH-5](P36_MATH_5_ONE_STEP_MAINTENANCE_SEPARATING_CONTINUATION.md) originally predeclared a **source-concrete** classical continuation distinction using `h_1=DDRR` and `h_2=DDED`, both length 4 from the same initial A,B,C source. Under observer `O=(current HTTP tag, Stats published revision)`, both output `(C,7)` but after future `E` they output respectively `(A,8)` and `(B,8)`. The passing O6 stable source test covers `DDRRE` and `DDEDE` and every prefix, so this is now a **bounded original-Go-validated observation witness**, not merely symbolic speculation. The observation projection is explicit and does not include private registry metadata or counts. It is classical non-Markovity under a coarse observation and ordinary Nerode distinguishing continuation, not non-Markovity of the full Go state.

**Updated court:** `O3_O4_O5_NESTED_NATIVE_STRICT_FILTRATION_PASS__O6_ORIGINAL_CHI_FINITE_1093_STABLE_ONLY_PASS__MATH5_ONE_ACTION_OBSERVER_SEPARATOR_BOUNDED_VALIDATED__DIP49_CLASSICAL_RIVALS_UNDEFEATED__LAW_R2_NOT_AUTHORIZED`.
