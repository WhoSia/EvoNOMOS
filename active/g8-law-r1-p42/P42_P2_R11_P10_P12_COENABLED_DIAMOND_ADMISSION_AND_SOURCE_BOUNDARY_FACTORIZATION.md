# EvoNOMOS Generation VIII LAW-R1-P42 — R11-P10-P12
# Co-Enabled Diamond Admission: Why Trace Saturation Does Not Certify Source Repair Concurrency

**2026-10-17 | RESEARCH FIRST | Theory, provenance and counterexample recorded BEFORE any P12 formal checker. P42 RUNNING · P43 HOLD · LAW-R2 NOT_AUTHORIZED.**

## 0. Research question and exact genealogy (do not claim rediscovery)

The explanandum is why some real, authorized, stagewise-old-client-safe source edit choices survive combination and why others do not, even when client route languages are disjoint. We reuse established net/trace/CSP and source semantics rather than attempt novel axioms for their own sake.

- **P37-MATH-I:** a minimum sufficient quotient for chosen future requirements was already the right research question.
- **P39-MATH-D:** owner/right histories that reach the same source can require independent future information. **P39-MATH-E/G:** edit interaction graphs and conditional α-acyclic join-tree gluing, with explicit separator incompatibility counterexamples.
- **P40-P4** already has [native ORIGINAL Chi both positive distinct static Mounts and negative equal-route pairs, 6/3 cases](../../tools/p40-p4/original_chi_gluing_test.go), plus a **2-bit lower bound** for 3 static route names in its specifically defined model [source](../../tools/p40-p4/boundary_minimum_certificate_court.py). These are NOT discoveries of P12.
- **P40-MATH-B-P2** has [original Chi disjoint REGEX request languages but both-source-order Mount rejection](../g8-law-r1-p40/P40_MATH_B_P2_AXIOM_INDEPENDENCE_AND_ORIGINAL_CHI_SOURCE_GLUING_COURT.md) with [original Go CI #38047274495 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38047274495), and an independent Lean proof of the scoped no-observation-factorization criterion [#38047101580 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38047101580). The pinned source is Chi 167e1e3bd039d060696b99c8da4e876ae04f42c1.
- **P40-MATH-B** had already defined deterministic source-continuation right-congruence. **P42 P10-P7/P8/P9** refined the demand-language presentation but not a first discovery of history/right obstruction.
- **P10-P10** [source-to-C/E-net admission](P42_P2_R11_P10_P10_SOURCE_TO_CAUSAL_NET_ADMISSION_AND_REPAIR_TRACE_QUOTIENT.md) introduced B1 (forward), B2 (reverse), B3 (owner/resource), B4 (effects/cost), B5 (domain). It applies Aalbersberg & Rozenberg 1988 Theorems 2.23/5.37/5.39 and, only for regular trace language, Theorem 3.35. The original [82-page *Theory of Traces*](https://drive.google.com/file/d/199AH7M4_udvXvRdlkvQTk4uexp1zT5Jb/view) is by **I.J. Aalbersberg and Grzegorz Rozenberg**, NOT Mazurkiewicz. Original [Lipton 1975 ACM 5-page article](https://drive.google.com/file/d/1TmiyB-5qivIY18VxL15t1gio5z8u918e/view) permits specific final-state/progress reductions, not unconstrained event histories.
- **P11**, [real pinned original Gin source/native SUCCESS #39041668694](https://github.com/WhoSia/EvoNOMOS/actions/runs/39041668694), verifies research-owned application edits A=/a and B=/b in 5 independently compiled source states 00,A,B,AB,BA with stagewise tested /old, /a, /b and no recorder Flush event. Actual AB and BA SOURCE BYTES DIFFER, despite equal tested client observations. Exact 4-marking causal quotient on this small declared edit grammar is supported. This is NOT a measured labor claim or real Gin maintainer source-edit authority.

## 1. The overlooked *second* admission condition

Fix a rooted, deterministic partial source-edit system \((S,\delta,s_0,E)\), with edit authorization, executable source change and stagewise old-client contract built into each defined transition. Let \(H\subseteq E^*\) be the prefix-closed set of admitted edit histories. Fix two distinct edits \(a,b\). A symmetric irreflexive candidate independence alphabet \(I\) defines a Mazurkiewicz adjacent-swap congruence \(\equiv_I\).

**Trace saturation**, as in classical trace theory, says:
\[
w\in H,\quad w\equiv_I v\quad\Longrightarrow\quad v\in H.
\]
It says nothing about whether a word of length 2 exists merely because both length-1 prefixes are legal.

**COENABLED SQUARE-FILL (CSF)** is a distinct condition:
\[
\boxed{\forall u\in H:\ 
ua\in H\ \wedge\ ub\in H\ \wedge\ a I b
\quad\Longrightarrow\quad
uab\in H\ \wedge\ uba\in H.}
\]
This is the language-level **joint realizability/enablement** condition which must be separately sourced before treating two locally possible edits as concurrent repair events. CSF does NOT by itself prove equal final source, client effects, future contractual acceptance or actual work cost. Those are additional quotient/observational conditions P9/P10, not consequences of a source-label swap.

### P12-T1: Trace saturation does not imply CSF

Take \(E=\{a,b\}\) and \(I=\{(a,b),(b,a)\}\). Let
\[
H_0=\{\epsilon,a,b\},\qquad
H_1=\{\epsilon,a,b,ab,ba\}.
\]
Both are prefix-closed and saturated under \(\equiv_I\). For \(H_0\), every legal word has length at most one, and swapping adjacent symbols cannot affect it; hence saturation. Both a and b are enabled initially but neither ab nor ba is in \(H_0\); CSF fails. \(H_1\) satisfies CSF (from the initial prefix; no other prefix co-enables two distinct one-shot edits) and is likewise saturated. QED.

**Interpretation:** the original regex-disjoint Chi same-parent Mount pair supports \(H_0\) **relative to the two defined one-shot owned app edits and tested contexts**; original Gin P11 supports \(H_1\) relative to its separately declared edit semantics; P40-P4 already gives a Chi \(H_1\) with distinct *static* Mount names **within the same underlying framework**. These ARE NOT the exact same edit API across Gin and Chi; do not rank frameworks from the comparison.

### P12-T2: A truly independent C/E source/net relation forces square filling

Suppose source \(S\) admits \(sa,sb\), and a candidate C/E system \(N\) has a related initial marking \(n\). Assume:
1. **B1 forward:** each admitted source step has a same-labelled firing with a related successor.
2. **B2 backward:** each enabled firing from any related reachable pair has an actual admitted source step, with a related successor. Both assumptions quantify over *successors*, not just initial state.
3. **Physical net independence:** if firing \(a\) and \(b\) are both enabled at \(n\) and \(a I_N b\), then the resulting firings can occur in **both orders** (usual non-interfering C/E condition/event square). This is net independence from real pre/post conditions, not a post-hoc independence declared from disjoint HTTP request languages.

Then both \(sab\) and \(sba\) exist as source edits. Proof: use B1 to map source a and b to enabled net a and b; net independence gives the two second firings; invoke B2 on each first-step related pair to reflect the second firing into admitted source edits. Hence any concrete Chi \(H_0\) pair **refutes** a proposed net that models the pair as independent co-enabled events while claiming B1+B2 for this source. The pair must be modelled with **some shared structural admission dependency/condition/contact** or the source/net certificate must be HOLD. This is a transfer of standard C/E concurrency, not original net theory.

**Important distinction:** both \(H_0,H_1\) being trace-saturated means even a completely correct proof of Theorem 5.39's LANGUAGE SATURATION property alone cannot distinguish these two source-admission profiles. To claim physical concurrency, the source–net *enabledness* relation and the diamond rule must additionally be established.

### P12-T3: Local-to-global transfer from an exact implementation boundary

Let \(\beta:S\to B\) be a source-derived boundary state map. For each edit e assume an exact guard \(g_e:B\to\mathrm{Bool}\) and boundary update \(U_e:B\rightharpoonup B\) such that, for every *reachable* concrete source state \(s\):

\[
\delta(s,e)\downarrow\quad\Longleftrightarrow\quad
g_e(\beta(s))=\mathrm{true},
\qquad
\beta(\delta(s,e))=U_e(\beta(s)).
\]

Exact guard reflection includes actual source validity, edit rights and stagewise protected old-client legality. In a live system this is a STRONG proof obligation; the existence of a Go AST node alone does not prove it.

For a fixed initial \(b=\beta(s)\), define
\[
D_\beta(b;a,b') =
g_a(b)\land g_{b'}(b)\land
g_{b'}(U_a(b))\land g_a(U_{b'}(b)).
\]
Here \(b'\) denotes the second EDIT LABEL, not a boundary state.

Then a concrete two-edit square with BOTH insertion orders is admitted **iff** \(D_\beta\) holds. Proof: for the forward direction apply necessity of each exact guard at the four source transitions; for the reverse direction use guard reflection successively and update compatibility. This establishes the **existence of two legal paths**, not equivalence of their endpoints. To obtain a client-relative commutation square one must additionally establish compatible projected final observations, cost sums and the chosen history-sensitive client queries. For source/net B1–B5 transfer, the update semantics must be closed and precise in the independently asserted domain.

This is a classical partial-transition homomorphism theorem. It is useful here as a **source certificate specification**, not a new mathematical theorem attributed exclusively to EvoNOMOS.

### P12-T4: Exact boundary admission is necessary information for a faithful net

If a proposed abstraction \(\beta\) merges two reachable source states \(s,t\) yet some legally offered edit e is admitted at s but rejected at t, no single-valued \(g_e\) can factor source admission through \(\beta\). The proof is immediate by substituting \(\beta(s)=\beta(t)\); this is already the classical non-factorization lemma and was **Lean-kernel verified in P40-MATH-B**, not re-discovered here.

This explains why a boundary state that preserves only route LANGUAGE supports, current client outputs, route types or a source edit's nominal file ownership may be insufficient. It does **not** establish that the complete underlying Chi radix tree is the minimal sufficient boundary domain.

## 2. Native source anchors for the BOUNDARY THEORY

[Unmodified Chi mux.go at P40 pinned commit](https://github.com/go-chi/chi/blob/167e1e3bd039d060696b99c8da4e876ae04f42c1/mux.go#L288-L354) implements \`Mount\` with first a \`mx.tree.findPattern(pattern+"*") || mx.tree.findPattern(pattern+"/*")\` reservation guard and later an \`subr.tree == mx.tree\` self-mount alias guard, before installing its stub/wildcard routes. [tree.go original function](https://github.com/go-chi/chi/blob/167e1e3bd039d060696b99c8da4e876ae04f42c1/tree.go#L591-L630) searches **structural node types**; \`ntParam, ntRegexp\` skip to the first closing brace; this procedure does not establish that two regular expression LANGUAGES have empty intersection. [Original Chi middleware source](https://github.com/go-chi/chi/blob/167e1e3bd039d060696b99c8da4e876ae04f42c1/mux.go#L100-L110) separately forbids \`Use\` after handler stack finalization. These are **three distinct kinds of source admission guards**, originally identified at P40; our P12 contribution is their mathematical placement in the B1/B2 source/net admission square.

For the P40 *number vs lowercase* mount patterns:
\[
P_a=/service/\{number:[0-9]+\},\
P_b=/service/\{letter:[a-z]+\}.
\]
Their represented HTTP request segment languages are disjoint, but native source rejects either second \`Mount\` on the same parent with the existing-path guard. This is measured Go behaviour in source CI, not deduced from regex syntax alone. For flat distinct Chi routes \`/service/a\` and \`/service/b\`, already tested at P40, both orders were admitted in its exhaustive \(3\times3\) court (six distinct pairs), whereas equal names rejected three pairs. The original Gin P11 is a separate true producer, with HTTP route registration rather than Chi Mount. **No new native experiment is required to discover these P40/P11 observations**.

### Three distinct proof-gate failures (do not collapse)

- **ADMISSION FAILURE:** a net predicts both source edit orders but Chi accepts only the individual Mounts. B2 source realization fails because the structural route-claim reservation was omitted from the net boundary, even if a/b's HTTP request languages are disjoint.
- **EFFECT/LANGUAGE FAILURE:** even when both orders exist (Gin), a new client's full-history policy such as “A must precede B” need not factor through their observational endpoint equivalence. This was already P8/P9.
- **COST/RIGHTS FAILURE:** the same two source edit orders may use differently priced actions or an externally issued reviewer approval; never infer cost or owner rights from Go interfaces alone. Already P39–P40 and P9.

## 3. Why this moves the P37→P42 central question

The equation “client supports are disjoint ⇒ admissible modular gluing” is false. The weaker but provable source-gluing chain becomes:
\[
\underbrace{\text{implementation boundary guards + rights + old-client prefix safety}}_{\text{B1/B2/B3 admission}}
\quad\Longrightarrow\quad
\underbrace{\text{legal 2-cell (source diamond)}}_{\text{CSF}},
\]
then, ONLY after admitting both paths,
\[
\underbrace{\text{client trace compatibility + exact cost invariance}}_{\text{P8/P9/B4/B5}}
\quad\Longrightarrow\quad
\underbrace{\text{client-relative trace quotient of future repairs}}_{\text{P10 bridge}}.
\]
There are TWO different gluing problems: *existence of the source square*, and *identification of its two executions in the client's future-repair quotient*. P10's trace-saturation theorem addresses the second once the source/net language correspondence has already been certified; it cannot manufacture the missing source square.

For more than two edits, P39-MATH-G has already shown that acyclic overlap structure alone is insufficient under additional owner-invariant precedence; **separator compatibility** is needed. A correct n-way composition would need compatible source boundary states and guards on overlaps, not just pairwise positive examples. This is the natural higher-dimensional challenge, not license to declare new LAW-R2.

## 4. Future falsifiable source work selected by mathematics

**Next source certification gate** is deliberately narrow: choose an action-grammar and client observation family for an original source project; freeze a source boundary map \(\beta\) and guard rules BEFORE new independent edit cases. Then verify exact enabledness, source update and conditional old-client oracle for **all declared reachable states** in that bounded grammar, and compare predicted source two-cell viability with strongest fair classical CSP/guarded LTS theory (which is expected to be competitive or tie). A counterexample to guard reflection must produce a source state + edit with divergent truth, and the abstraction must refine or HOLD; never hide it as a CI success.

No claim that P12 itself certifies B1–B5 for unbounded Go. P11 source stages are real native evidence, P40 source guards are real native evidence, but the complete guard factoring theorem for the chosen original source grammar still requires actual two-way source extraction and independent verification.

**Scientific result:** P12 research question/conditional theorems and the *trace-saturated but non-square-fillable* source obstruction are formalized first; code not yet written. P42 RUNNING, R11-P10-P12 MATHEMATICAL/ORIGINAL-SOURCE SYNTHESIS, B1–B5 source-wide OPEN, P43 HOLD, LAW-R2 NOT_AUTHORIZED.

## 5. POST-FREEZE FORMAL RECEIPT (2026-10-17; does not rewrite the pre-code question)

The independent mathematical kernel was implemented **AFTER** research preseal [d01c1300](https://github.com/WhoSia/EvoNOMOS/commit/d01c1300bd6dc0450286fdfdc91865d2928ac181), as [P12SourceDiamond.lean](../../tools/p42/p2-r11-lean-p12/P12SourceDiamond.lean) in Lean **v4.34.1**, without `axiom`, `sorry` or `admit`. Source theorem `reflect_concurrent_square` proves P12-T2 on *abstract partial transitions* under explicitly assumed B1/B2 matching and net coenabled-square existence; `saturation_does_not_imply_diamond` formally checks the two singletons are admitted and the two ordered 2-step paths are not in the saturated-by-length source language. `admission_requires_boundary_information` restates P40's prior classical no-factorization theorem, not new priority. It proves equality only of the **abstract endpoint marking** via the supplied mapping, not identical source files nor cost/client trace equivalence.

First read-only [Actions #39043142501 FAILED](https://github.com/WhoSia/EvoNOMOS/actions/runs/39043142501) due to missing `lake-manifest.json`, and [#39043293953 FAILED](https://github.com/WhoSia/EvoNOMOS/actions/runs/39043293953) due to missing Lean `Decidable` instances on explicitly defined finite languages. Both failure receipts remain preserved. Configuration and decidability repairs were made without altering mathematical hypotheses. **[Actions #39043394490 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39043394490)**: independent preseal-ancestry gate, Lean 4.34.1 Lake build, bundled `leanchecker` environment/kernel verification, no-proof-hole gate, SHA-256 artifact and precise scope receipt all PASS. This is **a kernel-level mathematical theorem**, and does **not** certify that the Go source/net interpretation is sound for all Go executions or human owner rights; G1–G7/B1–B5 remain OPEN for general source.

**P12 disposition:** mathematical trace-saturation vs square-filling separation AND formal source/net lifting lemma verified; original Chi P40 native negative and Gin P11 native positive remain historically separate source observations. NO new Chi/Gin experiment, no comparative architecture advantage, no new general SOLID law. P42 RUNNING; P43 HOLD; LAW-R2 NOT_AUTHORIZED.
