> **2026-10-17 F131 CUSTODY/READING UPDATE — F130 FOUR-PAPER ACQUISITION DEBT CLOSED.** [Exact four original PDFs, raw SHA256/page audits, theorem-by-theorem reading, edition distinctions and EvoNOMOS implications](P42_P2_R11_P10_P7_F131_FOUR_ORIGINAL_STRONG_PRESERVATION_TRACE_GPT_READING.md). All four files are now **renamed and verified in Research OS 10_PAPERS**. Any older statement below that these PDFs are missing is a **dated F130 snapshot superseded by F131**, not current. **Important mathematical correction:** forward complete-shell existence for the particular state-domain operators in ESOP'04/GSP'06 does **NOT** transfer unconditionally to trace-universal abstractions: Giacobazzi–Ranzato preprint Theorems 3.1/3.2 prove nonexistence for negation/eventuality, while Theorem 3.21 recovers the complete disjunction shell only essentially by keeping all actual traces. For GPT, TACAS'05 Theorem 4.3 requires DCC and representation/completeness assumptions. P7 32→9 is a fixed tiny right-language instance, not a blanket source abstraction. **P42 RUNNING · P43 HOLD · LAW-R2 NOT_AUTHORIZED.**

# EvoNOMOS Generation VIII LAW-R1-P42 — R11-P10-P7
# Rights-Aware Future Repair Languages, Existing Abstract Interpretation, and Research-Led Development

**2026-10-17 · P42 RUNNING · R11-P10-P7 BOUNDED MATH · P43 HOLD · LAW-R2 NOT_AUTHORIZED**

## 1. Operating doctrine: use established mathematics without ownership anxiety

EvoNOMOS's independent research question is not conditional on inventing a completely new proof technique. The aim is to understand which independently observed software source structures, actual owner edit rights, cost vectors, effect traces and future client demands govern legitimate repair paths, then derive scoped consequences for SOLID-like practices. We **reuse** well-tested abstract interpretation, complete shells, trace semantics, right-congruences, automata minimization, weighted transition systems and their algorithms when adequate. It is a valid scientific outcome to give these classical theories a previously unmodeled, verifiably source-grounded repair object. Code implements a source-derived proof obligation; code never invents the research question.

## 2. Four source articles NOT FOUND in Research OS Drive on 2026-10-17

These are **real source links**, not invented DOI addresses. Google Drive was searched by author/title; the two 1977 Cousot editions already present in 10_PAPERS should not be duplicated. The four below were not located. This is a search-based finding, not a claim that unindexed private files cannot exist.

1. **Ranzato & Tapparo, Strong Preservation as Completeness in Abstract Interpretation (ESOP 2004, LNCS 2986, pp.18–32), DOI 10.1007/978-3-540-24725-8_3.** Author's [direct PDF](https://www.math.unipd.it/~ranzato/papers/esop04.pdf), [University of Padua open repository published version PDF](https://www.research.unipd.it/retrieve/e14fb267-6a0f-3de1-e053-1705fe0ac030/published-paper-springer.pdf), [research record](https://research.unipd.it/handle/11577/1365865). Institution site may intermittently block automated downloads; citation and author-hosted PDF references independently indexed.
2. **Giacobazzi & Ranzato, Incompleteness of States w.r.t. Traces in Model Checking (Information and Computation 204(3), 2006, pp.376–407), DOI 10.1016/j.ic.2006.01.001.** [Author pre-publication 39-page PDF](https://www.math.unipd.it/~ranzato/papers/ic06.pdf), [arXiv 29-page preprint v2](https://arxiv.org/pdf/cs/0404048), [published-version repository record](https://research.unipd.it/handle/11577/1564839). Editions differ, do not label 29-page arXiv as identical bytes to 32-page journal.
3. **Ranzato & Tapparo, Generalized Strong Preservation by Abstract Interpretation, expanded working manuscript arXiv cs/0401016 (first 2004, v3 March 2006), later Journal of Logic and Computation 17(1), 2007 pp.157–197.** [arXiv complete extended PDF](https://arxiv.org/pdf/cs/0401016). This expands the ESOP'04 development and must not be merged indiscriminately into the shorter proceedings item.
4. **Ranzato & Tapparo, An Abstract Interpretation-Based Refinement Algorithm for Strong Preservation (TACAS 2005, LNCS 3440, pp.140–156), DOI 10.1007/978-3-540-31980-1_10.** [Author's direct PDF](https://www.math.unipd.it/~ranzato/papers/tacas05.pdf), [repository bibliographic record](https://research.unipd.it/handle/11577/1426807). University published version is restricted; author PDF indexed independently.

**Reading evidence grade:** full original arXiv 0401016v3 (32 pp) and 0404048v2 (29 pp) available and principal theorem/negative example sections consulted; ESOP 2004 authored PDF text and TACAS 2005 authored PDF abstract/main result indexed; DO NOT call either last item exhaustively read until actual full-page inspection.

## 3. Read and apply actual results rather than mere citation laundering

### Ranzato–Tapparo 2004 and expanded arXiv manuscript

Their language-relative **strong preservation**: validity of every specification formula must match between concrete and abstract models. Partition abstractions are only one class of abstract domain; the most abstract strongly preserving domain can be described by logical interpretations. In the expanded manuscript, Theorem 5.8 gives the characterization of strongly preserving domains by the Moore-closure of the concrete semantics of specification formulae. Section 6.1 develops *forward complete shells*, including the greatest fixed-point characterization in Lemma 6.2.

**Adopt:** specify an explicit **future repair query language**, then seek strong preservation relative to its effect/action/rights/goal operators. Do not demand generic all-program/full-Go equivalence if the independently chosen query language does not observe it. Use complete-shell techniques to refine only where a new repair query or authorized edit transformer separates abstract states.

### Giacobazzi–Ranzato 2006

The 2006 work makes a sharper negative claim than 'traces are useful': for a particular past/future-time mu-calculus, state-based abstraction is intrinsically trace-incomplete; refining/abstracting the domain of state sets cannot in general recover trace-completeness. Its minimal two-state example uses a temporal disjunction to distinguish the state- and trace-based interpretations. For some operations the necessary complete shell is effectively trace-level information (not a finite tag count). These claims have an exact specification-language scope.

**Adopt:** treat authorized edits and intermediate protected client effects as **paths with labels**, not endpoint bits. A state-only quotient cannot be presumed sufficient for history-sensitive repair contracts. Test exact observation-language expressiveness before searching for a 'minimal sufficient source feature set'.

### Ranzato–Tapparo 2005 GPT

The Generalized Paige–Tarjan refinement algorithm is a natural computational implementation of theory-relative strong preservation. It already subsumes standard partition-refinement cases for behavioural equivalences.

**Adopt:** when needing a finite P7 quotient checker, start from GPT/partition refinement, not a made-up new 'EvoNOMOS minimal quotient' algorithm. Code only after the chosen future query operators and ownership/cost semantics demand a computational certificate.

## 4. The new P7 mathematical object

Define a deterministic partial, authorized, stagewise protected, cost-and-effect-labelled edit transition system with source-history states s. Let \(\mathcal W\) be finite words in independent edit labels. For each word w define a partial *full receipt* \(R_s(w)\) including blocked/legal status, per-step labelled effect and exact vector cost, and final client observation. Let \(R_s(w)=\bot\) if any edit is forbidden or fails the protected old contract.

\[
s\equiv_R t\quad\Longleftrightarrow\quad
\forall w\in\mathcal W,\;R_s(w)=R_t(w).
\]

**Conditional right-congruence theorem (classical).** For fixed deterministic partial edit semantics and complete per-step receipts, equality of all residual receipt languages implies equivalent existence/labels/costs of any next admissible edit and receipt equivalence of the respective successors. This is the classic right-language (Mealy/Myhill–Nerode-type) quotient, relative to the declared alphabet and observations. Every future terminal client demand definable from those receipts has an identical set of legal repair costs on equivalent states, not necessarily a globally identical unobservable source.

**Proof idea:** choose word a·v for each edit label a and arbitrary suffix v. Equality on all a·v forces equal availability, equal first receipt, and equal continuation receipt languages. Reverse implication from a coinductive bisimulation follows by induction over word length. Weighted cost equality follows by adding identical per-edit cost vectors. There is NO claim that this is the most abstract domain for an unrelated, more expressive, history-sensitive temporal logic.

**State-only/no-rights impossibility:** If two concrete configurations have identical source bytes and protected observations but different externally granted edit rights, then for a demand requiring the distinguishing edit their legal cost sets differ. No predictor using solely source bytes/AST outputs can be simultaneously correct on both. This is an **information-identifiability limit**, not a failure solved by writing a more elaborate parser.

**Premature cost saturation can break right congruence:** If a client only observes accumulated capped costs but the residual-state model does not retain the consumed-budget history, states with equal current capped-cost predictions may have successors whose residual futures differ. Preserve per-step vector receipts or remaining budget in state. A fully selected, strongly preserving domain may be strictly richer than output-only projections.

## 5. P7 computation only after theory freeze

[Research question and negative controls presealed 0e2387fa](https://github.com/WhoSia/EvoNOMOS/commit/0e2387faec0a8fe214c0c72d78eb22d948950f80), before the checker code was written. [P7 finite checker](../../tools/p42/p2-r11/p10_p7_future_repair_right_languages.py); [actual proof-test CI #39023127360 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39023127360).

Under the authored 32-state, 2-action finite source/rights/tag edit semantics:

- **32 abstract source-world states → 9 full future edit-receipt right-equivalence classes**. Independent exhaustive word-signatures and action-labelled partition refinement coincide.
- Source installed-output bits alone produce 4 classes; source+raw rights bits ignoring irrelevant tags produce 16. The 9 classes remove rights bits already exhausted by installed edits and an irrelevant tag, while preserving future repairs for the declared grammar.
- Every one of 16 terminal-goal predicate subsets over installed A/B was checked for constant legal cost sets within the 9 classes.
- Rights differ despite same source output: exact repair possibility differs.
- Premature cumulative-cost saturation has a separate residual non-congruence counterexample.

**Limit:** the 32 source-rights states and associated costs are authored mathematical examples. This is not evidence that arbitrary original Go owner-rights G6, client observations G1–G5, or costs G7 have been certified. Earlier Chi/Gin/Echo real-source evidence remains a separate bounded bridge; external truly unforeseen PR rank still ABSTAIN.

## 6. Research-first execution priorities

1. **Choose a legitimate future query language** before a source extractor: does it ask only terminal reachable capability goals, or order-sensitive protected effect histories, resource use and authority evolution?
2. **Classify theoretical obstruction:** use complete shells/GPT if missing operator closure can be repaired by state refinement, or move to a trace-based domain if the query language defeats every state-set completion route.
3. **Prove source evidence suffices:** include authenticated rights, actual emitted effects and edit-cost ledger. Source hashes alone cannot predict externally governed permissions.
4. **Implement only a witness extractor/certificate for that theorem**, then test on independent maintained source pairs with preregistered matched client demands.
5. **Treat classical theoretical adequacy as an ordinary valuable success.** No rhetorical hunt for originality, no claim that using established methods makes EvoNOMOS dependent or unoriginal as a research program.

**P42 RUNNING · P7 MATHEMATICAL FINITE PASS · SOURCE-CERTIFICATION G1–G7 OPEN · P43 HOLD · LAW-R2 NOT_AUTHORIZED.**
