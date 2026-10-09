# EvoNOMOS P35-MATH-1 — Trace-Depth Filtration and Composition Congruence: Pre-Implementation Seal

**2026-10-09 · strict phase:** conjecture/definitions frozen BEFORE MATH-1 Lean/Go/Prolog code or outcome. **P35 OPEN; LAW-R2 NOT_AUTHORIZED.** This is mathematical METHOD and a probe for future theory, not a promotion of "responsibility" or patch predictors.

## Precise domain

A deterministic **total** state machine with internal state set S, shared action alphabet I and output set O is a pair of functions `step:S×I→S` and `out:S→O`. Its run on finite word `w∈I*` starts from state s and executes one step per symbol. Define terminal observation `Out(M,s,w)=out(run(M,s,w))`; this does NOT include an execution trace of intermediate outputs (though all prefixes can be queried). Compare two different state representations M and N with the same I and O.

`M,s ≈ₖ N,t` iff for every action word of **length ≤k**, terminal outputs agree. k begins at 0, and the empty word is included. A *separating word* of length ℓ witnesses inequality at depth ℓ. This is **classical finite-trace state-machine equivalence**, explicitly not novel.

A structural product with an **independent** environment E has state S×T, receives the same external action in both factors, steps independently and exposes the **ordered pair of both outputs**. This output-factorization is part of the theorem's premise, NOT a theorem derived from arbitrary software composition.

A **non-factorizing context** may inspect internal state that the original out-function hides. It is intentionally a different composition operator: contextual probing of private state. A claim about independent products must not be extrapolated to such contexts.

## Frozen mathematical claims, expected results

**T1 FILTRATION (expected theorem):** if 0≤j≤k and `M,s≈ₖN,t`, then `M,s≈ⱼN,t`. No finiteness of S is necessary.

**T2 PRODUCT CONGRUENCE (expected theorem):** if `M,s≈ₖN,t`, then `(M×E,(s,e))≈ₖ(N×E,(t,e))` for every independent E and initial environment state e, with paired visible outputs. Proof requires actual product run factorization, not a vacuous rewriting of the definition.

**C1 DEPTH ZERO NOT ENOUGH (expected finite counterexample):** machine A and B both start at Bool false and have output equal to current state; A toggles state on each Unit action and B stutters. `A,false≈₀B,false`, but the one-action trace distinguishes; `A,false ≉₁ B,false`. Go and Prolog shall independently find shortest distinguishing word of length 1.

**C2 OVERGENERALIZED CONTEXTUAL COMPOSITION (expected counterexample):** a machine whose visible output is the constant false, with two hidden initial states false/true, is equivalent at EVERY finite depth under its original output. A context that directly reads the hidden state distinguishes **with empty input word**. This is NOT an independently factored product. This falsifies "all source contexts preserve observational equivalence" if arbitrary state-probing contexts are admitted. A result dependent on private-state access cannot automatically be inferred about encapsulated real Go APIs.

**T3 HIDING-INSENSITIVE SCORES (expected corollary only):** any score function of the publicly observed terminal output of a bounded trace cannot distinguish A and B when A≈ₖB at that trace. This is not proof of economic or global architectural ranking.

## Attack protocol / negative controls

1. Create human-authored preseal commit for definitions, expected outcomes and scope BEFORE code.
2. Make native Lean 4.34.1 `Machine`, `run`, `eqUpTo`, independent `product` and proofs. No proof holes, introduced axioms or masked assumptions. Fix Lean toolchain and Lake manifest in repo.
3. Implement a distinct bounded **Go enumerator** generating traces up to 3, searching shortest distinction (0 for leaky context, 1 for toggle/stutter), with negative checks for independent product preservation of depth-zero/one equivalence. Do not copy Lean proof outputs.
4. Independent **SWI-Prolog search** enumerates the same counterexamples with queries and `plunit` assertions; no claim that finite enumeration proves T1/T2.
5. Read-only GitHub Actions builds Lean and uses independent leanchecker; Go vet, race tests and Prolog unit tests run in a separate job. Tests enforce expected counterexample lengths, not merely existence.
6. Preserve first technical failures and correction commits; compare proof statement with source-world premise and classical rivals. A proof of this **expected classical theorem** is `METHOD_PASS`, not a new software-design law.

## Existing mathematical competitors (LIVE, undefeated)

- Lean/Mathlib standard [Deterministic Finite Automata](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Computability/DFA.lean) and [ctchou/AutomataTheory](https://github.com/ctchou/AutomataTheory) formalize finite-automata/language results. Our tiny implementation is not a novelty claim.
- Davide Sangiorgi, [*Introduction to Bisimulation and Coinduction*](https://www.cs.unibo.it/~sangio/IntroBook.html) directly anticipates behavioral equivalence and congruence restrictions.
- Broy (2010), [*Synchronous message passing: On the relation between bisimulation and refusal equivalence*](https://doi.org/10.1007/978-3-642-11512-7_8) distinguishes composition operators for which familiar equivalences fail. Do not wrongly transfer trace congruence to an arbitrary synchronous, shared-state or state-probing composition.

**Scientific exit gate:** one correct theorem + one countermodel is a *proof technique*, not a theory. Return to actual Go A/B with matched evolving demands before any LAW promotion; do not rebrand the work as responsibility engineering.
