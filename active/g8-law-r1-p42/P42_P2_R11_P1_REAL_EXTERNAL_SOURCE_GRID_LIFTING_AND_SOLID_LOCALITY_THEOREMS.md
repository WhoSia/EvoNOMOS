# EvoNOMOS Generation VIII LAW-R1-P42-P2-R11-P1 — Independent Go Ownership Source, Interleaving-Grid Repair Theorems, Contextual Refinement and Non-Circular SOLID Interpretability

> **CURRENT SOURCE/LITERATURE CORRECTION (2026-10-13):** The four original CCR 2.0, Simuliris, Iris and DimSum PDFs formerly marked missing below were acquired, independently inspected and normalized to Research OS Drive 10_PAPERS; [R11-P2 canonical revised rival audit](P42_P2_R11_P2_HISTORY_SENSITIVE_AUTHORITY_RUBY_GO_PRIMARY_RIVAL_COURT.md) supersedes the historical missing-paper ledger. F2 iff statement below has a newly explicit stepwise-refinement premise; plain safety requires a weaker F_e^safe predicate. P43 HOLD, LAW-R2 NOT_AUTHORIZED.

**Status:** P42 RUNNING; R11-P1 BOUNDED NATIVE ORIGINAL GO PASS; mathematical results below are explicit conditional theorems and classical constructions, not general-Go mechanized proofs or novel software design laws. P43 HOLD, LAW-R2 NOT_AUTHORIZED.

## I. Scientific result and independent source custody

The test is anchored to **two independent software projects**, and to a frozen research package:

- Actual 2024 grpc-go original at commit \`9ab8b62505c85a5e03be1ae97949e960e24b6d4f\`, including original \`mem.Copy\`, \`mem.BufferPool\`, \`Buffer.Free\`.
- Actual third-party \`milvus-io/milvus\` source \`pkg/util/resource/codec_buffer_pool.go\` at commit \`4610a590c49ee5d15b81d8d10d3ef15853458745\`. The Go file was copied **byte-identically** into all staged programs without changing a single byte.
- Pre-result prediction freeze \`tools/p42/p2-r11/frozen_p1_independent_milvus_provider_typed_source_paths.json\` at commit \`2ebb6644b4ad8409050baff99f12a3af998f786e\`, recorded before staged source generator, checker or CI source.
- [Live original Go workflow SUCCESS #38333768692](https://github.com/WhoSia/EvoNOMOS/actions/runs/38333768692): job \`115089152988\`; artifact \`11783677841\`; ZIP SHA-256 \`a3f922472925203d23ebc59347133dccb3cfd03b78fa2ecbc339596188132857\`.

**Identity boundary.** The original Milvus file is source maintained separately from grpc-go, but its queried file path did not show a commit dated on or before December 31, 2024. A December 2024 snapshot of \`googleapis/google-cloud-go/storage/client_test.go\` likewise lacks the current \`testBufferPool\` and \`WithBufferPool\` test. Cortex's selected contemporary codec file was not found in its before-2025 file history either. Therefore **the original-file version-matched execution today is NOT evidence of a 2024 contemporaneous independent third-party client or maintained change sequence**.

**Truthful test role separation:** original 2024 grpc-go implementation and original third-party Milvus provider were imported into new Go test packages; the two consumer implementations, full-overwrite and partial-write demands, a deterministic dirty-provider adversary, and edit rights are **research-authored**. These distinguish interface obligations without alleging a Milvus production bug or independently running Milvus's own test suite.

| Frozen source stage | Old full-overwrite client | New partial-write / zero suffix on any admissible pool | Authentic original external source | Compile |
| --- | --- | --- | --- | --- |
| direct | PASS | FAIL against deterministic dirty pool | exactly preserved | PASS |
| guard_prepared | PASS | FAIL (adapter not selected) | exactly preserved | PASS |
| guard_selected | PASS | PASS | exactly preserved | PASS |
| root_first | ineligible | ineligible | exactly preserved | **FAIL**: undefined \`writeZeroed\` |

The two-file typed patch path \`direct → guard_prepared → guard_selected\` is valid at each stage. \`direct → root_first → guard_selected\` reaches the same endpoint but violates intermediate compiler validity. The path \`direct\` alone fails the new demand. The original gRPC and original independent Milvus provider did compile and execute together for all three buildable stages. Classical finite source-edit invariants recover the complete court.

## II. Read the full CCR 1.0, not only the abstract

Actual PDF: Song, Cho, Lee, Hur, Sammler, Dreyer (2023), *Conditional Contextual Refinement*, Proc. ACM Program. Lang. 7 (POPL), article 39, 31 pages, DOI \`10.1145/3571232\`. Verified original PDF SHA-256 \`e41b6418faffbe1b7666727eaa53abf849138300fa9e600914721cc08d5e3828\`. [Canonical owned PDF in Drive 10_PAPERS](https://drive.google.com/file/d/13Ghr7KUsITAJnkDngPoh2tT2jn5JbkMy/view).

Important actual internal claims in the full paper:

1. §1.2 distinguishes **horizontal composition** (linking different modules satisfying matched separation-logic conditional specifications) from **vertical composition** (transitive incremental replacement/refinement of a module). Neither is a new EvoNOMOS theorem.
2. §1.2, pp. 5–6 introduces a separation-logic wrapper that enforces preconditions and postconditions operationally and defines a conditional refinement by ordinary contextual refinement against the wrapped specification.
3. §3.1 states ordinary contextual refinement supports both horizontal and vertical composition. This is a stronger competitor than mere points-to analysis and covers precisely many naïve "ownership composition" claims.
4. §8 explicitly notes CCR 1.0's lack of concurrency and higher-order concurrency features. This is a limitation of **the 2023 version**; it is not evidence that future work lacks these features.
5. **CCR 2.0**, Song & Cho (2025), arXiv \`2507.04298\`, adds more powerful reasoning, relational logic and model changes motivated by counterexamples, with Rocq mechanization. Source metadata verified online; original full PDF currently **not found in Drive**. Mathematical novelty against 1.0 alone is thus insufficient.

## III. A precise typed source-evolution system

Let a module's states form a labelled transition system \((S_i,E_i,\rightarrow_i)\) whose states include the **typed, buildable source tree**, not only runtime heap state. Labels record an authorized owner and an actual source edit, \((o_i,e_i)\). Rights \(Γ_i(s,o,e)\), dependencies and compilation validity may change with history: if so, the state must include the relevant histories, not silently identify them.

Let \(S_1\otimes_B S_2\) be a **partial linking operator** defined only for compatible interfaces, shared resources and authority boundaries \(B\). For a linked state \(u\), let \(I_C(u)\) mean **all declared existing clients' observational/ownership contracts hold**. We deliberately do **not** define \(I_C\) by "satisfies SOLID"; its semantics are external code-level oracles or verified traces. Let \(\operatorname{Goal}_d(u)\) represent an independently specified future demand.

A valid repair path from \(s\) to \(t\) must take actual authorized, buildable source transitions, stay in \(I_C\) at **every prefix**, and satisfy \(\operatorname{Goal}_d(t)\) at the endpoint. Both path quantifiers matter:

\[
\operatorname{May}_{Γ,I}(s,d)\equiv \exists H,\;\operatorname{SafePrefix}_{Γ,I}(H)\land \operatorname{Goal}_d(\mathrm{last}(H)).
\]

\[
\operatorname{AllSafe}_{Γ,I}(\mathcal H)\equiv \forall H\in\mathcal H,\;\operatorname{SafePrefix}_{Γ,I}(H).
\]

The second is not logically interchangeable with the first; the endpoint may be identical.

## IV. Exact finite interleaving-grid theorem for two prescribed edit chains

Take two separately frozen finite local source edit chains \(a_0 \to a_1 \to\dots\to a_m\) and \(b_0\to b_1\to\dots\to b_n\). **Assume a genuine path-independent decomposition**: the linked state after the first \(i\) edits of A and the first \(j\) of B is exactly \((a_i,b_j)\), regardless of order. (Do not use this grid if cross-module edits change each other's patch semantics or rights; in that case move to the enriched history-state graph.)

Define a finite rectangle grid \(G=\{0,\ldots,m\}\times\{0,\ldots,n\}\). Its cell predicate \(\mathrm{Good}(i,j)\) holds iff \(a_i\otimes_B b_j\) is defined, compile-valid and satisfies \(I_C\). Each right/up edge is enabled only if the corresponding actual owner/source edit remains admissible in that linked context. An *interleaving* is a monotone directed lattice path from \((0,0)\) to \((m,n)\).

**Theorem G1 (May exactness):** With fixed final goal true at \((m,n)\), there exists a fully valid interleaving iff the following backward recurrence returns true at \((0,0)\):

\[
M(i,j)=\mathrm{Good}(i,j)\land\left[
(i=m\land j=n)\lor
\bigl(\mathrm{Edge}_A(i,j)\land M(i+1,j)\bigr)\lor
\bigl(\mathrm{Edge}_B(i,j)\land M(i,j+1)\bigr)
\right].
\]

Terms outside the grid are false. Without the final goal the base terminal term is replaced by \(\operatorname{Goal}_d(a_m\otimes b_n)\).

**Proof:** Backwards induction on \(m+n-i-j\). At the terminal cell an admissible path exists iff Good and the endpoint goal hold. For any other cell every complete monotone edit sequence starts with either an A step or B step. That step must be enabled and lead to a suffix whose May recurrence is true by induction. Conversely choose a true disjunct, perform its enabled step and append the inductively admissible suffix. QED.

**Theorem G2 (universal-source-interleaving criterion):** Every *syntactically possible shuffle* is buildable, authorized and preserves existing clients iff **all grid cells are Good and every right/up grid edge is enabled**. Here "every syntactic shuffle is safe" includes execution feasibility for each prescribed edit order; it is not the vacuous statement that every *already-valid* shuffle is safe.

**Proof:** Every cell \((i,j)\) and edge on the rectangle lies on at least one monotone origin-to-terminal shuffle: prepend \(i+j\) edits and append the remaining \(m+n-i-j\). If all shuffles are valid, every cell/edge on such a shuffle is good/enabled. For sufficiency each shuffle consists entirely of precisely these cells/edges. QED.

**Interpretation:** G1 tests *some valid repair schedule*, G2 tests *all schedules*. Both results are standard dynamic programming and transition-system invariants, **not new mathematics**. Their new value for EvoNOMOS must be a prospective source-grounded prediction that a particular interface boundary gives a smaller obstruction set or a valid schedule under real maintainers' edit rights, not the abstract recurrence.

**Further classical connection:** A blocked-source-edit cut that intersects every path from origin to endpoint is a certificate for failed May-repair. This is a standard directed graph reachability / vertex-edge cut property, not a novel repair law.

## V. General conditional lifting theorem beyond commuting edit rectangles

Real owner edits may not commute or retain their permissions, so a single cell \((i,j)\) may fail to represent the state: a history-sensitive \(\widehat s=(s,\mathrm{trace},\mathrm{rights},\mathrm{resources})\) is necessary. Let \(L\subseteq \widehat S_1\times\widehat S_2\) be a proposed linked-state relation preserving boundary ownership and client observations.

**Theorem L (conditional safe path lifting).** Suppose initial linked state lies in \(L\) and satisfies \(I_C\). Suppose for every state \(u\in L\) reachable by the declared owner edit grammar and for every selected owner-local next edit \(e_i\):

1. The edit has a **linked, authorized, compilable successor** \(u\xrightarrow{e_i}u'\).
2. Its successor remains in \(L\), its boundary resource postcondition establishes the next rely/precondition, and \(I_C(u')\) holds.
3. The link witnesses an observational conditional refinement for all declared clients, with ownership transfer, publication/aliasing and rights transitions reflected correctly.

Then **every finite sequence** of those selected owner edits is defined and remains in \(I_C\) after every prefix. If its terminal source additionally satisfies \(\operatorname{Goal}_d\), it is a valid repair path.

**Proof:** Induction on length \(k\). Base \(k=0\) is the initial-link assumption. At the induction step the prefix endpoint belongs to \(L\) and satisfies \(I_C\), so the universally quantified local lifting hypotheses provide an admissible linked successor in \(L\cap I_C\). Trace and conditional refinement side conditions transport all existing client contracts. Endpoint success requires the separate goal assumption. QED.

**Claim boundary:** This is a valid *conditional induction schema*. Its assumptions are demanding, and finding them from actual Go source is the hard problem. It does not prove that two locally valid edits automatically compose, that CCR 2.0 is beaten, or that arbitrary Go ownership/alias properties are decidable. If history-dependent permissions or shared state violate (1)–(3), the theorem offers **no** safety promise. Unlike an ad hoc new axiom, this states precisely the existing frame, rely-guarantee and contextual refinement commitments that must be discharged.

## VI. Why SOLID-style finite locality alone cannot close unbounded contexts

**Theorem K (bounded-radius indistinguishability; classical locality obstruction).** Fix \(k\ge0\) and any architecture predicate \(f\) determined only by the radius-\(k\) marked neighborhood of an edited module. There exist finite dependency/source-resource graphs \(G^0_k,G^1_k\) with isomorphic such neighborhoods, but opposite safe-repair feasibility for a declared global demand.

**Construction:** Both worlds have identical directed dependency chains of length \(k+1\) from edited component \(v_0\) to boundary \(v_{k+1}\). In \(G^0_k\), the far boundary resource name needed for the new requirement is unreserved. In \(G^1_k\), the same name is held by a separate owner. The two marked radius-\(k\) neighborhoods coincide, since only \(v_{k+1}\)'s remote reservation differs. The new requirement forces a change propagated to \(v_{k+1}\) and reserves that name. The repair is admitted in world 0 and rejected in world 1. Yet \(f(G^0_k)=f(G^1_k)\). QED.

**Corollary:** No family of SOLID-like predicates whose interpretations are all restricted to a fixed finite-radius local footprint can be sufficient for **all unbounded shared-boundary future repair demands**. Any exact predictor of this pair must retain at least one distinguishing bit or request an observation revealing the remote reservation. This **does not imply** that canonical SRP/OCP/LSP/ISP/DIP must always be local, nor that a general global SOLID formalization could not see the difference. It proves strict inadequacy **only for the specified bounded-local interpretations**. There is no novelty claim: this is a straightforward locality/indistinguishability argument, consistent with classical graph and program semantics.

Earlier source-confirmed \`go-chi/chi\` mount name collisions provide a real, restricted counterpart: two modules locally valid become globally incompatible when joined at the same reserved mount route. The formal \(k\)-unbounded family is a mathematical extrapolation, NOT a Go benchmark.

## VII. Non-circular SOLID partial semantics, without deriving the desired answer

Introduce separate primitive predicates based on independently selected source evolution contracts:

- **SRP fragment:** responsibility-domain partitioning and edit support locality relative to an explicit demand family \(D_R\).
- **OCP fragment:** authorized source extension that preserves a protected implementation region and all old clients.
- **LSP fragment:** context-indexed behavioral/trace refinement under a stated substitution and precondition.
- **ISP fragment:** client demand footprints and observational capabilities that need not expose unrelated operations.
- **DIP fragment:** typed dependency factoring through an explicitly stable interface contract, rather than a concrete implementation identity.

These are five **chosen interpretations** \(\llbracket\mathrm{SRP}\rrbracket,\ldots,\llbracket\mathrm{DIP}\rrbracket\) within the ambient typed source/observer/owner model, which is defined **without mentioning SOLID**. They need not hold at every program; they need not be jointly satisfiable; they do not follow from the existence of objects, types or interfaces alone.

Strictness against a **bounded-local SOLID signature** follows from Theorem K once the chosen signature depends only on the \(k\)-neighborhood. Whether a richer, context-sensitive SOLID formalization can account for a specified repair phenomenon must be separately attacked. No canonical uniqueness or equivalence between original five philosophical/engineering slogans is assumed.

## VIII. Independent experiments required to turn these theorems into EvoNOMOS science

1. **Historicity:** discover a genuinely contemporaneous independently maintained consumer with a version-compatible original producer; the three R11-P0 files do not meet this older 2024 requirement. Older Google Cloud commit \`d49263b2...\` lacks the later \`WithBufferPool/testBufferPool\` passage; selected Cortex and Milvus files were not found in their 2024 file histories.
2. **Real source semantics:** check original client tests, then a first actual cross-owner change path with code version custody, not merely a laboratory dirty-pool adversary.
3. **Formal strengthening:** design a **checkable weakest sufficient ownership/authority boundary** for real source patches, with semantic preservation and edit-grammar completeness assumptions exposed. Prove an interface-local certificate transports along all live source edits, or construct a counterexample proving an unavoidable dependence on global history.
4. **Classical priority:** test G1/G2/L/K against CCR 1.0 **and CCR 2.0**, Iris's higher-order separation logic, Simuliris's relational proofs, and DimSum's modular event synchronization. Equal-source classical explanation is preferred when adequate. No novel law without a prospectively differing prediction.
5. **Conditional design reversal:** choose two genuinely matched real source architectures implementing the same old clients and then disclose two independent new demands only after experimental design freeze; predict under what demand/owner/boundary worlds DIRECT vs ADAPTER flips, without replacing semantic correctness by an arbitrary LOC scalar.

## IX. Literature acquisition ledger, actual Drive inventory checked

**CONFIRMED and reviewed original complete PDF:** Song et al. (2023) CCR 1.0, DOI \`10.1145/3571232\`, transferred to canonical Drive \`10_PAPERS\` under normalized scholarly filename. **Duplicate bytes identified:** An additional same-title original `3571232.pdf` was subsequently discovered in Drive `00_INTAKE` at file ID `16x-GJJkXiXljEbO3SD0wL8L_S0Zxzj5u`. Its complete 31-page PDF has the **same SHA-256 `e41b6418faffbe1b7666727eaa53abf849138300fa9e600914721cc08d5e3828`** as canonical 10_PAPERS file `13Ghr7KUsITAJnkDngPoh2tT2jn5JbkMy`. The extra copy was preserved in 00_INTAKE and renamed `DUPLICATE_NOT_CANONICAL`; it was not deleted or promoted.

**NOT FOUND as separately stored original PDF by title/DOI search** (web discoverability is not Drive ownership or proof of reading):

- Song & Cho (2025), *CCR 2.0: High-level Reasoning for Conditional Refinements*, [arXiv 2507.04298](https://arxiv.org/abs/2507.04298) — urgent; counterexamples against 1.0 and Rocq model amendments.
- Gäher et al. (2022), *Simuliris: A Separation Logic Framework for Verifying Concurrent Program Optimizations*, DOI [10.1145/3498689](https://doi.org/10.1145/3498689) — concurrent relational classical rival.
- Jung et al. (2018), *Iris from the Ground Up: A Modular Foundation for Higher-Order Concurrent Separation Logic*, DOI [10.1017/S0956796818000151](https://doi.org/10.1017/S0956796818000151) — higher-order resource model, available [open PDF](https://pure.mpg.de/pubman/item/item_3033720_3/component/file_3331878/iris-from-the-ground-up-a-modular-foundation-for-higher-order-concurrent-separation-logic.pdf).
- Sammler et al. (2023), *DimSum: A Decentralized Approach to Multi-language Semantics and Verification*, DOI [10.1145/3571220](https://doi.org/10.1145/3571220), [open paper PDF](https://plv.mpi-sws.org/dimsum/paper.pdf) — source module/linking semantics comparator.

**Different available material:** Sangiorgi lecture notes on bisimulation are indexed in Drive, but they do not replace a full original concurrency/ownership paper. Other software architecture papers may already be in Drive; no universal absence is claimed without searching them by their titles/DOIs.

**Scientific disposition:** R11-P1 exact-source Go test **PASS**; G1/G2/L/K have explicit conditional proofs and finite model checks, but their mechanism is **CLASSICALLY ADEQUATE**, not a new derived OO law. Genuine real-world architecture-value reversal and general Go source-to-formal-semantics certification remain OPEN. P42 RUNNING; P43 HOLD; LAW-R2 NOT_AUTHORIZED.


## X. P1B update: genuine independently maintained 2024 consumer source executed

Earlier R11-P0 historical negatives apply only to the selected contemporary Cortex, Google Cloud Storage and Milvus files. A *different* independent historical source cohort was subsequently found and tested successfully:

- [moby/buildkit 2024-10-03 original source](https://github.com/moby/buildkit/blob/41a0a0c37d0bd66d97203d3895750ff96c015548/util/grpcutil/encoding/proto/proto.go), ref 41a0a0c37d0bd66d97203d3895750ff96c015548, source blob 9aa156cf27e9ed004e1899c803fe86442409b902.
- [authzed/spicedb 2024-09-18 original source](https://github.com/authzed/spicedb/blob/44372c1c020b9ce7e40b704951b59f1529f6fe1a/pkg/proto/dispatch/v1/01_codec.go), ref 44372c1c020b9ce7e40b704951b59f1529f6fe1a, source blob d72e4e4feb59d46379d06e86053881deae124665.
- Same unmodified original grpc-go producer ref 9ab8b62505c85a5e03be1ae97949e960e24b6d4f.

P1B independent prediction/source freeze commit b30daf54aa11916e7b21df037114355a55740569, preceding generator or CI. [Frozen P1B contract](../../tools/p42/p2-r11/frozen_p1b_two_real_2024_independent_grpc_consumers.json), [byte-exact original-source materializer](../../tools/p42/p2-r11-native/make_two_original_2024_codec_clients.py), [hosted Actions #38334505205 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38334505205), job 115091455208, artifact 11783888662, ZIP SHA256 f5bf2453e1810a5196cac87a075d91e5714df85a6978c4319234a398800dbaaa.

Both real 2024 CodecV2 source files were imported byte-identically and successfully compiled against exactly the original 2024 grpc-go source. Original source implementations each successfully marshalled and unmarshalled research-authored 1,024-byte and 2,048-byte vtproto-compatible message instances, four native roundtrips total, PASS. The tests use authentic maintained *consumer implementations* but research-authored test messages and an isolated Go module. The full original projects' suites and any real owner-separated production patch were NOT tested.

The older claim that *no contemporaneous independently maintained consumer exists* is now **superseded for this new BuildKit/SpiceDB cohort**. The older selected Cortex/Storage/Milvus cohort's exact-2024 limitation remains in effect.

## XI. Theorem F: greatest rely-frame support and polynomial grid verification

Let A be one owner's state, B the context/partner owner's state, and e:a -> a' be a genuine authorized source edit. Consider a partial linking operation and an independently specified set of existing client trace contracts I. Define the full contextual safe rely support:

\[
F_e(a) := \{b \mid
\operatorname{Linked}(a,b) \land I(a \otimes b)
\land \operatorname{AuthorizedBuildable}(e,a,b)
\land \operatorname{Linked}(a',b) \land I(a'\otimes b)
\land \operatorname{TraceRefines}_C(a'\otimes b,a\otimes b)\}.
\]

**F1 (greatest permissible environment / weakest sufficient rely assumption).** A partner-state set R guarantees this edit is enabled, preserves the interface/client contract and satisfies the selected trace refinement for every partner b in R **if and only if** R is a subset of F_e(a).

**Proof.** Expand the definition of F_e(a) and the universal condition over R. Every b in R must have all the defining properties, precisely expressing R subset F_e(a). Any strict extension outside F_e(a) contains a direct failing frame witness. QED.

This gives an exact greatest rely-support set under the powerset order; it does not guarantee that the set is source-locally inferable, decidable for arbitrary Go, unique under changing semantics, or novel against weakest preconditions, separation-logic frames and relational residuals.

**F2 (exact safe all-shuffle source-edit criterion).** Given owner A's fixed source chain a0 -> ... -> am and owner B's fixed chain b0 -> ... -> bn, assume the source state after i A-edits and j B-edits is independent of the chosen interleaving (the rectangular path-independence hypothesis). Suppose the initial link is safe. Then *every syntactically possible source-edit shuffle* is permitted, buildable and old-client-safe **AND each individual edit satisfies the declared client trace-refinement relation** at all intermediate steps **if and only if**

\[
\boxed{
\forall i<m,\,\forall j\le n:\ b_j\in F_{e_i}(a_i)
\quad\land\quad
\forall j<n,\,\forall i\le m:\ a_i\in F_{f_j}(b_j).
}
\]

**Proof.** The first family checks every A-incrementing grid edge with exact source, destination, rights and old-client trace requirements; the second checks all B-incrementing edges. By previously proved G2 each complete shuffle consists entirely of these allowed edges, proving sufficiency. Conversely, each grid edge lies on some monotone complete shuffle; if every shuffle satisfies the stronger stepwise-refinement contract, that edge has the full rely/frame property. QED.

**F2 erratum and boundary (2026-10-13):** An earlier formulation claimed that the displayed F_e condition was necessary merely for *all-shuffle old-client safety*, but F_e additionally demands **stepwise trace refinement between neighboring source states**. Pure safety does not entail that stronger relation. For exactly old-client-safe shuffles, define F_e^safe by **removing the stepwise trace-refinement conjunct** and the same edge-by-edge G2 equivalence is valid. This repairs the necessity direction without altering the recorded Go/Ruby observations. The sufficiency direction of the stronger F2 was valid all along.

**Complexity result within the assumptions.** Instead of enumerating binomial(m+n,m) complete edit schedules, the rule requires m(n+1)+n(m+1)=2mn+m+n individual proof obligations. Verification complexity of any one trace obligation is *not* bounded by this count. If simultaneous edits, owner-right changes, or shared state make the linked state depend on edit order, the grid coordinates no longer represent states uniquely. Then the theorem does not apply: a history-enriched source transition system is required and the polynomial count may disappear.

The mathematically demanding *open* task is to derive source-observable, owner-checkable **sufficient conditions for frame-support stability** across edits without presupposing the very design property being explained. Source interpretation must compete directly against CCR 1.0 and **CCR 2.0** (original PDF not yet in Drive), Iris, and independently verifiable trace/interface refinement; none is defeated by this elementary set-theoretic theorem.

## XII. Research status after source and theory update

R11-P1 original third-party provider PASS plus R11-P1B two genuine 2024 independently maintained original consumer Go code paths PASS. G1/G2/L/K/F1/F2 are explicitly scoped mathematical theorems/proof schemas, NOT a certified semantic preservation theorem for arbitrary Go source, a new architecture law, or a real maintainer edit-labor study. The next remaining hard gate is history-aware source contract extraction, original-owner patch sequence composition, and prospectively predicted architecture preference reversal under independent genuine demands. P42 RUNNING / P43 HOLD / LAW-R2 NOT_AUTHORIZED.
