# P35-MATH-1 — Trace-Depth Filtration, Independent Product Congruence and Non-Factoring Context Countermodel

**2026-10-09 · bounded status:** `MATH1_LEAN_KERNEL_CHECKED__GO_PROLOG_COUNTERMODELS_VERIFIED__CLASSICAL_THEORY_NOT_DEFEATED__REAL_SOURCE_TRANSFER_OPEN__P35_OPEN__LAW_R2_NOT_AUTHORIZED`.

## 0. Keep the founding scientific question distinct from the mathematical tools

EvoNOMOS searches for **nontrivial conditional laws governing the relative behavior and evolution of software structures**. Its ultimate goal is not source cochange, responsibility boundaries, scalar repair cost, nor creating decorative Lean theorems. MATH-1 studies a necessary *semantic instrument*: what it means for two independently implemented programs to be indistinguishable under a bounded repertoire of changes, and what composition assumptions make this indistinguishability stable.

The initial mathematical questions and four expected claims [were human-presealed](P35_MATH_1_TRACE_COMPOSITION_PRESEAL.md) **before the Lean/Go/Prolog sources or CI outcomes**, in authenticated `WhoSia` commit [`9148508`](https://github.com/WhoSia/EvoNOMOS/commit/9148508dbc2b650db2f6b2fd57ac0b17ea2e305e). The separate [implementations](../../tools/p35-math1) were authored in `WhoSia` [`0227d2a`](https://github.com/WhoSia/EvoNOMOS/commit/0227d2a90430fbb9ad44c31e12d0f55c2cdc32aa), followed by a read-only CI workflow `WhoSia` [`fc8ca18`](https://github.com/WhoSia/EvoNOMOS/commit/fc8ca18d58052e7293972e0e4e92ab025a8ae84f). No bot writes or branch-force updates.

## 1. Actual formal definitions, with quantifiers and boundaries

A deterministic *total* state machine over arbitrary (not necessarily finite) internal state `S`, action alphabet `I`, output `O` is `Machine S I O` with `step : S → I → S`, `out : S → O`. The complete state `run(M,s,w)` follows a finite word `w : List I` in order. Observations are **terminal-state outputs**. All prefixes are in the quantified word set, but output traces as a single object are not primitive.

For possibly different state spaces S,T, same I and O:
```
eqUpTo k M s N t :=
  ∀ word : List I, word.length ≤ k →
    M.out (run M s word) = N.out (run N t word)
```
This genuinely allows comparing two implementations whose private representations do not match.

`prodMachine M E` has state `S×U`, identical input actions applied independently to the two factors, and output `(M.out(s),E.out(u))`. It does NOT model synchronized shared-memory mutation, input feedback from partner outputs, nondeterministic external scheduling, or an observer with access to a component's private state.

## 2. Kernel-verified results and false conjectures attacked

Full exact Lean source: [`EvoNOMOSMath1.lean`](../../tools/p35-math1/lean/EvoNOMOSMath1.lean), with no `sorry`, `admit`, or introduced `axiom`, fixed Lean v4.34.1, verified by independent bundled `leanchecker`.

| Identifier | Statement / nature | Outcome |
| --- | --- | --- |
| `depth_antitone` | `j≤k ∧ A≈ₖB ⇒ A≈ⱼB` | **THEOREM, Lean checked**, any state spaces |
| `eqUpTo_refl`, `eqUpTo_symm` | basic properties | **THEOREMS** |
| `runProduct` | `run(M×E,(s,u),w) = (run(M,s,w),run(E,u,w))` | **THEOREM** by induction on every finite word; vital non-vacuous composition step |
| `independent_product_congruence` | `A≈ₖB ⇒ (A×E)≈ₖ(B×E)` with the same E, factored transitions and visible pair outputs | **THEOREM** for every k, E and word |
| `observed_score_equal` | applying any score to the **same observed output** preserves equality for words ≤k | **COROLLARY**, NOT global architectural ranking |
| `toggle_stutter_eq_zero`, `toggle_stutter_separate_one` | depth 0 equivalence but depth 1 failure | **THEOREM AND COUNTEREXAMPLE** |
| `silent_hides_all_depths`, `private_state_probe_counterexample` | constant public output remains indistinguishable for every k; a foreign observer directly probing hidden state distinguishes at empty word | **THEOREM AND COUNTEREXAMPLE TO A DIFFERENT, OVERBROAD CONTEXTUAL CLAIM** |

The important logical correction is **not** “composition universally preserves equivalence.” Instead it specifies a congruence theorem **for an independent product whose outputs factor through the declared public observations**. The hidden-state probe is **not such a product**. A context that accesses hidden state breaks the premise and can distinguish at depth zero, even if the declared outputs never differ. No theorem about unrestricted real-world Go module composition follows.

### Finite attacks as an independent, lower truth tier

[Native Go enumerator](../../tools/p35-math1/go/model.go) and [SWI-Prolog program](../../tools/p35-math1/prolog/countermodels.pl) are separate implementations of the state-transition claims. Both verified first separating action word `[tick]` of length 1 for a toggling vs stuttering Boolean state machine, absence of depth-0 separation, and a private-state probe that distinguishes two silently-outputting states at length 0. Go additionally exhaustively checks independent-product preservation on a finite, **explicitly bounded family of 16 Boolean-state transition/output tables** for traces up to depth 2, with Go native tests and race detection. This is *evidence about that bounded family*, **not a universal proof**; the universal theorem resides in Lean.

## 3. Native machine evidence and exact chronology

[Read-only GitHub Actions **#37914813182**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37914813182) **SUCCESS BOTH JOBS**.

- `lean-formal`: fixed Lean 4.34.1 and Lake manifest; `lake build` **SUCCESS (3 jobs)**; bundled independent `leanchecker` **SUCCESS**; no proof holes/intended axioms. Hosted artifact **11609846892**, ZIP archive SHA256 **`ff253208b59d5e19a78ea1af8243290d4476f756beb5f76965bf59aea190e27b`**.
- `go-prolog-attack`: Go 1.23 native `go vet ./...`, `go test -race -count=1 -v ./...` SUCCESS; JSON receipt explicitly checks `depth_zero_equal=true`, `depth_one_equal=false`, `first_separator=["tick"]`, `first_length=1`, `hidden_output_equal_up_to_three=true`, `state_probe_separates_at_empty=true`, `product_cases>0`, `product_violations=0`; SWI-Prolog `plunit` SUCCESS. Hosted artifact **11609826165**, ZIP archive SHA256 **`d4c769a83483ab865ebbe7a76101a0877e0dafdbcd98fecc42e898d1b01bdc33`**.
- Both artifacts contain source/model receipts; workflows have `contents:read`. No failure concealed, no theorem statement changed to make CI pass.

## 4. Prior art: proper competitors, not ceremonial citations

**This mathematics is classical in substance.** In particular, behavioral equivalence/bisimulation, product automata, equivalence/congruence under specific composition operators, and distinctions between private states and public observations are established areas.

- [Mathlib DFA formalization](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Computability/DFA.lean) models deterministic machines and runs over finite input words.
- [ctchou/AutomataTheory](https://github.com/ctchou/AutomataTheory) formalizes finite/infinite automata and language/congruence machinery in Lean.
- [Davide Sangiorgi, *Introduction to Bisimulation and Coinduction* (2012)](https://www.cs.unibo.it/~sangio/IntroBook.html) treats behavioral equivalence and compositionality as foundational.
- [Manfred Broy, *Synchronous message passing: On the relation between bisimulation and refusal equivalence* (2010)](https://doi.org/10.1007/978-3-642-11512-7_8) directly warns that equivalence preservation depends on the composition operator; a blanket trace-congruence claim fails in some process algebras.

**All these rivals remain undefeated.** This project *checks its own chosen formalization*, not the novelty of the formal statement or its correspondence to every actual Go program. Mathlib is not made a massive dependency for a small kernel-proof seed; its definitions/lemmas should be used when the next theorem genuinely requires finite-state structure, quotients or algebra.

## 5. Next mathematical gate: not more toy theorems for their own sake

**MATH-2 direction:** (a) for arbitrary k, can two finite-state machines first become distinguishable at k+1, and what number of states is required? (b) compare bounded trace equivalence under state-hiding, input-feedback, nondeterministic and shared-state product operators, without slipping into unsupported universal congruence. (c) rigorously map software's *future demand transformations* to action/context families and test whether structural tradeoff/relative rankings are invariant under allowable equivalence and representational choices. (d) require independent *original Go* source A/B competitors and actual future demands; P7 remains the native source substrate, not the proven model's exhaustive semantics.

A genuine possible law would have to **survive classical automata/process theory, countermodel attacks, and two independent original Go software-worlds under matched demand sequences**. So far, **MATH-1 is METHOD PASS, not CORE ADVANCE.** Parent P35 OPEN; LAW-R2 NOT_AUTHORIZED.
