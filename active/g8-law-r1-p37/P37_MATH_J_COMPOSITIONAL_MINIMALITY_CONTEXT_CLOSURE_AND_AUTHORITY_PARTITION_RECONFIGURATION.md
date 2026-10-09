# P37-MATH-J — Compositional Minimality of Future-Repair Structures: Context Closure, Information Splitting & Authority-Dependent Congruence

**2026-10-10 KST · Theory-first · Classical conditional results · No novel law identified.** Predecessor: [MATH-I](P37_MATH_I_MINIMAL_FUTURE_SUFFICIENT_QUOTIENTS_AND_CONTEXT_NONCOMMUTATION.md). P37 OPEN / DIP49 IDENTIFICATION HOLD / LAW-R2 NOT_AUTHORIZED.

## Definitions and scope

Fix source-state space \(S\), invariant-preserving admissible edit relation \(\Gamma\), invariant \(I\), and demands \(D\). Define the exact (not search-bounded) reachability signature \(F(s)=\sigma_D(s)=(\operatorname{May}_{\Gamma,I}(s,d))_{d\in D}\) and its kernel \(R=\ker F\). MATH-I showed that \(S/R\) is the coarsest local exactly sufficient partition.

For any admitted **typed** context \(C\), plugging is \(j_C:S\to T_C\). The composition has its own owner-authorized edit relation \(\Gamma_C\), invariant \(I_C\) and translated future demand family \(D_C\). The contextual signature pulled back to the SAME source-state space is \(G_C(s)=\sigma^{C}_{D_C}(j_C(s))\), with \(K_C=\ker G_C\). When plugging is partial, restrict comparisons to a common domain; claims concern \(j_C(S)\), not all of \(T_C\).

## J1 — Contextual sufficiency and minimality are distinct

An abstraction \(q:S\to Q\) permits an exact predictor \(G_C=h_C\circ q\) **if and only if** \(\ker q\subseteq K_C\). Necessity: a fiber of \(q\) cannot contain different contextual answers. Sufficiency: define \(h_C\) on each fiber's common answer. Consequently the OLD quotient \(S/R\) is sufficient under context \(C\) iff \(R\subseteq K_C\), but is **coarsest exact sufficient** iff \(R=K_C\).

- \(R=K_C\): still sufficient and still minimal.
- \(R\subsetneq K_C\): still sufficient but now redundant distinctions survive.
- \(R\nsubseteq K_C\): insufficient; composition requires separating some formerly equivalent states.

This theorem concerns only the named future queries, not source-path bisimulation or the number, costs, or owner labels of repair paths.

## J2 — Context-family closure and relative congruence

For a family \(\mathcal C\) of typed admissible contexts put \(K_{\mathcal C}=\bigcap_{C\in\mathcal C}K_C\).

The abstraction \(q\) is sufficient for **every** such context iff \(\ker q\subseteq K_{\mathcal C}\). The coarsest exact family-sufficient quotient is \(S/K_{\mathcal C}\). The original \(S/R\) is family-minimal iff \(R=K_{\mathcal C}\), while it is *separately minimal for every context* only if \(R=K_C\) individually for all \(C\). The latter is strictly stronger.

If the admitted context grammar and demand translations are closed under typed composition, preservation of the equivalence under every admitted context is a **relative contextual congruence**. Congruence for any enlarged owner/capability grammar is not inherited automatically; neither is graph path lifting.

## Three-state countermodels

Let \(S=\{a,b,c\}\), local \(F=(0,0,1)\), hence \(R=\{\{a,b\},\{c\}\}\).

1. \(G_1=(0,0,1)\): same partition, local quotient sufficient and minimal.
2. \(G_2=(0,0,0)\): a single contextual class, old quotient sufficient but not minimal.
3. \(G_3=(0,1,1)\): contextual classes \(\{a\}\mid\{b,c\}\); old quotient insufficient.
4. For family \(\{G_1,G_3\}\), the combined kernel intersection is discrete, hence three states must be distinguished.

These signatures admit elementary source-edit reachability realizations; they are **synthetic mathematical worlds**, not new Go experiments.

## J3 — Expanding edit authority preserves May but can rearrange quotient classes

Fix \(S,I,D\) and demands' acceptance predicates. If \(\Gamma_0\subseteq\Gamma_1\), every prior safe authorized path remains authorized. Thus \(\operatorname{May}_{\Gamma_0,I}(s,d)\le\operatorname{May}_{\Gamma_1,I}(s,d)\) for each \(s,d\). **But there is no general refinement relation between \(\ker\sigma_{\Gamma_0}\) and \(\ker\sigma_{\Gamma_1}\).**

Witness: goal \(c\), no edits under \(\Gamma_0\), and \(\Gamma_1=\{a\to c\}\). Old signature \((0,0,1)\) groups \(\{a,b\}\mid\{c\}\); new signature \((1,0,1)\) groups \(\{a,c\}\mid\{b\}\). Neither partition refines the other. Statewise May monotonicity permits old classes to **merge and split** simultaneously. This differs from extending \(D\subseteq D'\) under *fixed* \(\Gamma\), where MATH-I showed only refinement.

## Executable bounded check

[Three-state checker](../../tools/p37-math-j/context_minimality.py) enumerates all six possible directed non-loop source-edit edges. Each edge can be absent in both relations, present in both, or newly added: \(3^6=729\) ordered relation pairs \(\Gamma_0\subseteq\Gamma_1\). Across all \(2^3=8\) accepting subsets there are **5,832** configurations. Local Python validation confirms: all cases satisfy pointwise May monotonicity and **162** have incomparable before/after partitions; the sufficiency/minimality/context-family witnesses also pass. The linked workflow checks source under GitHub Actions with read-only permissions, and its result must be inspected before claiming hosted CI success.

## Strong classical rivals and prospective gate

All three results are established by ordinary function-kernel factorization, context/continuation semantics and graph reachability. **These are not a novel EvoNOMOS law.** Myhill–Nerode-style continuation equivalence, contextual equivalence, abstract interpretation/complete abstractions, access-control and bisimulation remain undefeated strong rivals.

Before any further external Go library trial, fix the original source, admissible edit grammar, owner-authority model, invariants, future demands, exact outcome and a maximally informed classical rival \(B_*\). Register an explicit prospective prediction where \(H_{\rm Evo}\) and \(B_*\) differ; otherwise classify observations as classical corroboration. The objective remains an independently falsifiable **conditional software-design structural law** explaining when SOLID-family recommendations work or reverse, not collecting more green infrastructure checks.

**Verdict: MATH-J theoretical conditional distinctions + finite synthetic enumeration PASS; source-grounded novel-law identification HOLD. P37 OPEN / DIP49 HOLD / LAW-R2 NOT_AUTHORIZED.**
