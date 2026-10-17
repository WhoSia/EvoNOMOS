# EvoNOMOS P42 R11-P10-P7 — F131: Four Original Strong-Preservation & Trace-Semantics Papers — Verified Custody, Deep Reading, and Repair-Language Implications

**2026-10-17 | Source custody: 00_INTAKE → 10_PAPERS COMPLETE for 4/4 | Full source-level reading of all four PDFs | P42 RUNNING · P43 HOLD · LAW-R2 NOT_AUTHORIZED**

## A. What was actually received and preserved?

Four distinct actual PDFs were discovered in the exact Research OS `00_INTAKE — Literature Radar` folder (parent `1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16`) by searching author names and titles. All four were opened through the authenticated Drive connector, identified from their **own title pages**, renamed, moved to `10_PAPERS — Canonical Literature Commons` (parent `1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP`) and re-read through `get_file_metadata` to establish that the new parent is exact and the old parent is absent. Their raw PDF bytes were also retrieved and their genuine local SHA-256 digests and page counts computed; PDFs were inspected at original page-level where equations or notation matter. No PDF was deleted, merged, relabelled as a different edition, or silently replaced.

| Citation and edition | Source Drive file / exact type | Pages / bytes / SHA-256 |
| --- | --- | --- |
| Ranzato & Tapparo, *Strong Preservation as Completeness in Abstract Interpretation*, ESOP 2004, LNCS 2986 pp.18–32, DOI 10.1007/978-3-540-24725-8_3 | [Springer published PDF](https://drive.google.com/file/d/1PZCTvGdxUCF3ivNfO8ObUJcxijqp8iA1/view); renamed `Ranzato & Tapparo (2004) — Strong Preservation as Completeness in Abstract Interpretation — ESOP 2004 — Springer ORIGINAL.pdf` | 15 pp; 240883 bytes; `a177d3f9b8e9e7699bb58a9da8c8d9a1439ef6176e76ce21e4f567fadab46d14` |
| Ranzato & Tapparo, *An Abstract Interpretation-Based Refinement Algorithm for Strong Preservation*, TACAS 2005, LNCS 3440 pp.140–156, DOI 10.1007/978-3-540-31980-1_10 | [Springer published PDF](https://drive.google.com/file/d/1_YR9nnuMRxBN4aX9X4AUzUxtij_txtXT/view); renamed `Ranzato & Tapparo (2005) — An Abstract Interpretation-Based Refinement Algorithm for Strong Preservation — TACAS 2005 — Springer ORIGINAL.pdf` | 17 pp; 282479 bytes; `65f701e2abc3c769bba705a6defbc627e42f2a9961233726929f4382f74548d5` |
| Giacobazzi & Ranzato, *Incompleteness of States w.r.t. Traces in Model Checking*, *Information and Computation* 204(3), 2006 pp.376–407, DOI 10.1016/j.ic.2006.01.001 | [arXiv cs/0404048v2](https://drive.google.com/file/d/1cElDDmsnmA3buF30enPFjJThJ8-YsADv/view); PDF dated **24 Aug 2005**, **NOT** journal typesetting; renamed `Giacobazzi & Ranzato (2006) — Incompleteness of States w.r.t. Traces in Model Checking — arXiv cs-0404048v2 — 2005 PREPRINT.pdf` | 29 pp; 334944 bytes; `79f6c53e3eefba91d6d9e923c857f47c476b9565cb8db3a3ec7db779e7daa047` |
| Ranzato & Tapparo, *Generalized Strong Preservation by Abstract Interpretation*, arXiv cs/0401016v3 **14 Mar 2006**, later revised journal lineage | [arXiv v3 expanded manuscript](https://drive.google.com/file/d/1djiUlkPbgLFpeh4u_HNcHydyKgvWEkAR/view); renamed `Ranzato & Tapparo (2006) — Generalized Strong Preservation by Abstract Interpretation — arXiv cs-0401016v3 — PREPRINT.pdf` | 32 pp; 401143 bytes; `ad2775f0a5871fe60621b9e5540068fdeea077f9bc3359bf77c965d64b9e03a3` |

**Duplicate audit:** Four exact four different bibliographic/title-page identities and four distinct hashes, so none of the four is a byte duplicate of another. Drive title/author searches disclosed these four in 00 before action, rather than additional prior canonical instances in 10. A whole-Drive hash index of all unrelated files has **not** been performed; that wider claim is not made. Cousot & Cousot 1977 retains its two previously audited **distinct** searchable/facsimile original PDFs in 10_PAPERS.

**Edition warning:** ESOP 2004, TACAS 2005, expanded arXiv 2006 are related sequential work by Ranzato–Tapparo, not three independent confirmations. The Giacobazzi–Ranzato preprint may differ in pagination/formulations from its 2006 journal version; the exact journal full PDF is **not** what the Drive copy contains.

## B. Original-paper reading, actual theorem locations, and distinctions

### B1. ESOP 2004 — why a partition is not necessarily the right abstraction

The introduction and §3 contrast **state partitions** with arbitrary upper-closure-operator (uco)/Galois-connection abstract domains. This is a structural enlargement of the search space, not a rhetorical call for finer partitioning. §4 defines generalized strong preservation for the fixed specification language L. **Theorem 4.6** says strong preservation of a closure is characterized by refinement of the particular semantic closure \(\mu_L\), and **Proposition 4.7** identifies \(\mu_L\) as the Moore closure of \(\{\llbracket\varphi\rrbracket:\varphi\in L\}\). It is therefore **language-relative**: changing what clients are permitted to ask changes the minimum required information.

**Proposition 4.9** is a particularly useful caution: under the paper's hypothesis that L is closed under possibly infinite conjunction, the induced \(\mu_L\) is a **partitioning** closure iff the language is closed under logical negation. In Example 4.10 the authors exhibit a non-partitioning strongly preserving abstract domain for a language fragment. Therefore a source-state 'minimal partition' need not be the optimal abstract DOMAIN for an asymmetric query language.

§5 defines **forward completeness** as closure under concrete operator applications. **Lemma 5.2** gives the greatest-fixed-point construction of the complete shell. **Theorem 5.4 and Corollary 5.5** identify the most abstract strongly preserving refinement for conjunctively closed languages as the forward complete shell of an initial atom domain under the specified language operators. **Lemma 5.7** ties partitioning domains to forward completeness for complement. §6 recovers bisimulation/Paige–Tarjan in the appropriate Boolean/Hennessy–Milner setting, explicitly as a special instance of completeness. These are the pre-existing mathematical tools for EvoNOMOS—not discoveries of our P7.

### B2. TACAS 2005 — implementation follows a theorem, with nontrivial correctness gates

§2 formally constructs the \(F\)-complete shell; **Lemma 2.1** expresses it as a greatest fixed point. §4 introduces **CPT** over concrete abstract domains and **GPT** for an abstract representation of domains. **Lemma 4.1** guarantees CPT termination and correct shell on a *finite concrete* state set. The abstract GPT is **not automatically correct or terminating on every chosen domain**. **Theorem 4.3** explicitly assumes that the abstract domain satisfies the descending chain condition (DCC) and at least one of two completeness/representability conditions: backward completeness for the relevant \(F_{uco}\), or stability of the represented domain family under complete-shell computation. Only then does GPT terminate and compute the appropriate abstract image of the complete shell.

§5 explains how classical simulation/stuttering algorithms instantiate GPT; §5.3 develops a reachability-language \(EF\) case and a particular \(O(|Transitions|\,|States|)\)-time partition algorithm. That complexity bound is for this particular EF application and data structure, **not** generic GPT.

**EvoNOMOS effect:** the next 'repair minimizer' should be a direct instance of the GPT/complete-shell framework, but only after the *selected future-repair language* and the abstract domain demonstrate Theorem 4.3's actual hypotheses. Code-before-language was precisely the practice to avoid.

### B3. arXiv cs/0401016v3 — general domain-level proof, not merely a longer ESOP summary

§§2–4 develop Galois connections, completeness and abstract semantics for general inductively defined logical/temporal languages. **Theorem 5.8** formally characterizes strongly preserving abstract domains by refinement against
\[
AD_L=\operatorname{Moore}\{\llbracket\varphi\rrbracket:\varphi\in L\}.
\]
The minimum domain needed for exact responses depends on *which predicates and operators are present in L*; language-relative adequacy is the operative concept. §6.1 **Lemmas 6.1–6.2** show existence and greatest-fixed-point construction of a **forward complete shell** for the specified monotone operator family in this state-domain setting.

**Theorem 6.7 (§6.2.1)** identifies strong preservation for a language closed under infinite conjunction with its forward-complete shell construction. Its proof uses structural induction on formulas and a transfinite/fixed-point argument for shell construction, with the closure and operator hypotheses made explicit. **Theorem 7.2** characterizes bisimulation for appropriate Kripke structures as forward completeness for suitable concrete transformers; §7.2 and §7.3 similarly treat stuttering and simulation.

**Scope:** this paper is not evidence that a useful small complete domain always exists for *every* arbitrary history-sensitive language, and it does not establish rights to edit GitHub source. The P7 9-class finite right-language quotient is one **particular** finite deterministic/receipt-language instance, not this paper's most abstract domain in general.

### B4. arXiv cs/0404048v2 — much stronger limitation than 'save event traces'

§§1–2 construct trace semantics and the universal/existential **state-based model checking abstraction**, distinguishing *soundness* from *completeness*. The authors demonstrate that the state-domain semantics can give a sound answer yet be strictly less expressive than the trace-based answer, **even on a finite transition system**.

The key theoretical surprise is that a blanket "take the complete shell" instruction can fail for the relevant starting trace abstraction and operators. In **Theorem 3.1**, the complete shell for trace negation **does not exist** under the paper's universal model-checking abstraction; **Theorem 3.2** proves the analogous nonexistence for the monotone eventuality/sometime operator \(F\). Their proofs use a single-state looping transition system with distinct present-time indices to separate candidate completions.

The limitation takes a different shape for disjunction: in **Theorem 3.20**, the only disjunction-complete *core* is the trivial uninformative domain; **Theorem 3.21** establishes that the complete *shell* for disjunction is essentially the identity on the actual model trace set \(M\):
\[
\operatorname{Shell}_{\lor}(\rho_M^\forall)(X)=X\cap M.
\]
The original author explicitly states that restoring full precision for disjunction can require **all actual traces** in \(M\), defeating a hoped-for economical 'state-only' abstraction. **Theorem 4.1** transfers operator complete-shell results to temporal-language completeness only when the operator shell exists and additionally satisfies the stated descending-chain/co-continuity condition.

**EvoNOMOS consequence:** A future repair language that admits arbitrary disjunction of mutually incompatible **effect histories or client traces** may compel a genuinely trace-indexed domain, not simply a new Boolean bit in an AST feature vector. This is a research **hypothesis to instantiate**, not a proven transfer of the authors' temporal calculus to our owner-rights/source-edit calculus.

## C. What the four originals jointly settle and what they do NOT

1. **Define the future-repair query language first.** There is no query-independent 'minimum source abstraction' worthy of universal promotion. ESOP §4/§5 and GSP Theorems 5.8/6.7 support a language-relative domain search.
2. **Do not reflexively force a partition.** For languages lacking classical negation closure, the most abstract strongly preserving domain can be non-partitioning (ESOP Proposition 4.9).
3. **Treat algorithm correctness as a separate theorem.** TACAS Theorem 4.3 gives actual termination/representation conditions; an executable finite refinement loop is not proof of validity for arbitrary chosen abstract domain.
4. **Do not assume a useful complete shell always exists.** Distinguish forward complete shell existence in the powerset-state setting from trace-language/universal projection shells for negation or \(F\), where Giacobazzi–Ranzato Theorems 3.1/3.2 prove nonexistence.
5. **Some logics force full trace information.** Theorem 3.21's disjunction result is a particularly severe no-compression warning for certain trace languages.
6. **No paper in this four-file corpus certificates real third-party source edit permission or actual engineering-cost vectors.** EvoNOMOS's G1–G7 source transfer/authority obligations remain OPEN. Rights information is an *external input*, not an AST-inferable property.

## D. Research-first next mathematical question (not an invented result)

We should define at least **two distinct** future-repair query languages before writing another extractor:

- \(L_{\mathrm{reach}}\): externally authorized legal edit steps; terminal safety, reachable goal, fixed client observable predicates and **exact / bounded cost vector**. Suggested operators: Boolean atom predicates, authorized \(\langle e,c\rangle\), and reachability \(EF\) when its semantics are fixed. This may admit a state-based complete-shell/GPT treatment on finite proof-certified state spaces. Need to check closure, non-monotone operators and budget in the state.
- \(L_{\mathrm{trace}}\): the same, but clients may distinguish **ordered event histories, rights consumptions and interleavings**, and the language may support disjunctions over trace histories or past/future modalities. We must first determine whether any state-only quotient strong-preserves this actual language; if not, use a trace- or history-indexed semantic domain. Prior trace-incompleteness theorems motivate this but **do not themselves prove an EvoNOMOS-specific no-go**.

For any declared \(L\), specify the concrete state/trace semantics, atom interpretations (protected clients, permissions, effects, costs), and operator transformers. Prove whether its desired complete domain exists in the chosen abstraction universe. Then *only if applicable* instantiate CPT/GPT, preserve original source-rights certificates, and compare equal-information classical baselines. When a language is too strong, a **mathematically defended expressive restriction** is valid research progress.

**No phase promotion:** R11-P10-P7/F131 ORIGINALS READ AND CANONICALIZED, original third-party Go source/authority G1–G7 still OPEN, P42 RUNNING, P43 HOLD, LAW-R2 NOT_AUTHORIZED.
