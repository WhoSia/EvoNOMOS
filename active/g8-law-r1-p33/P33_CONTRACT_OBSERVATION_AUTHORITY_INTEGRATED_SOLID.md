# P33 — Contract–Observation–Authority: An Integrated Conditional Mathematics of SOLID

**Generation:** EvoNOMOS G8 LAW-R1-P33.  
**Full theoretical strand:** demand-relative observation quotients, behavioral refinement, client-owned abstract ports, and change-conditioned ownership cost.  
**Claim class:** cited classical mathematics + a P33 interpretive synthesis. This is a valid conceptual/theoretical contribution without new mathematical results. No empirically novel universal OO law is claimed. **P33 OPEN / LAW-R2 NOT_AUTHORIZED.**

## 0. Origin genealogy recovered from the actual research archive

1. **Founding 2026-07-29:** distinguish design maxims from natural laws; identify why/when a software structure works under changing requirements. [Founding constitution](https://app.notion.com/p/3cbef561cf928127a917c84bc0056546).
2. **Generation VIII ORIGIN-R1-P11 (chat archive 10.md):** WIDE_BOUNDARY_REUSE versus CAPABILITY_SEGREGATED for Exa/Tavily search/fetch. OCP/DIP existing-wide-port reuse can **conflict** with ISP capability segregation. A unified theory must leave conflicting design advice possible.
3. **LAW-R1-P18 (chat archive 12.md; [Harvest W](https://app.notion.com/p/3edef561cf9281ffa0fdfed640e78aee)):** *Principle-as-Projection Hypothesis* (PPH): a named maxim may be a local projection/compression of richer conditional policy, not a primitive law. It is a theoretical hypothesis, not an established macro-law.
4. **LAW-R1-P23/P26/P27:** a correct abstract theorem is not a guaranteed source semantics; unobserved structure is non-unique, and orientation matters even at equal rank. This motivates distinct observational and ownership/edge layers.
5. **LAW-R1-P31 (chat archive 13.md):** LSP is a **substitution contract**, SRP/DIP/ISP are context-conditional *design choices*. They must not be flattened to five scalar cost heuristics.
6. **P32/P33:** Uptime Kuma source information loss, nonunique bounded repair choices, and the 65,536-case finite demand-quotient checker. These illustrate, but do not establish a new general software law.

Historical archive source: [Research OS EvoNOMOS Chat Archive](https://drive.google.com/drive/folders/1WvaxudLruNNycRG5WlUi9gPYk39XdJ-s), especially 9.md, 10.md, 12.md, 13.md. Historical statements do not acquire new empirical authority merely by appearing in this synthesis.

## 1. Direct prior-art debt — no invented theorem titles

- Barbara H. Liskov and Jeannette M. Wing, **A Behavioral Notion of Subtyping** (ACM TOPLAS 1994), DOI [10.1145/197320.197383](https://doi.org/10.1145/197320.197383), [author PDF](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf). Semantic subtyping preserves client-provable properties; preconditions, postconditions, invariants and history constraints. Original PDF was **not found by focused Drive title/author search**, not assumed unavailable universally.
- Robert C. Martin, **The Dependency Inversion Principle** (C++ Report column, 1996), [original author's PDF](https://objectmentor.com/resources/articles/dip.pdf). DIP is presented as a structural consequence of OCP and LSP in that essay. This P33 model separates **a sufficient safety proof** from **a source dependency/ownership choice**; not a claim the author gave the following formal graph semantics.
- Luca de Alfaro and Thomas A. Henzinger, **Interface Automata** (ESEC/FSE 2001), DOI [10.1145/503271.503226](https://doi.org/10.1145/503271.503226), [PDF](https://web.cs.wpi.edu/~heineman/html/teaching_/CS562/p109-de_alfaro.pdf). Assumptions about invocation order and guarantees about external interactions; input/output compatible refinement. DOI must be verified against the original publisher record before canonical PDF naming because third-party records contain conflicting strings.
- Parnas (1972/1979), Sullivan et al. (2001), Tishby et al. (1999/2000), Reiter, SemFix, DirectFix, Angelix, Guigue: already held in canonical Drive 10_PAPERS, as documented in the P33 six-paper court and previous quotient manuscript.
- Existing Design Rule Spaces/CSDG/co-change studies remain relevant to real maintenance prediction. The present document is **not** a claim to have defeated them.

## 2. The mathematical object

Fix an environment e, clients C, modules M, permitted configurations c, demand family D, and source edit grammar L. Define a contract-bearing architecture

    A = (M, P, I, o, K, Pre, E_compile, Bind, Owner, D, e).

- P: abstract ports; I: realizations/providers, assigned to ports by composition-root binding relation Bind ⊆ P × I.
- o_p:X→Z_p: observations/capabilities made available through port p, on an explicitly chosen domain X. This is an idealized total deterministic observation subcase, not every possible OO runtime.
- K_p(h)⊆Σ*: allowed **client-visible finite traces** under legal input/call history h; Pre_p contains the histories that clients are entitled to attempt.
- T_i(h)⊆Σ*: client-visible traces from concrete provider i under the same h (with an explicit abstraction of private implementation events). Nondeterminism is represented by multiple traces.
- E_compile⊆M×M: source/compile-time dependency direction, with arrow u→v meaning **u's source depends on v's declaration**. This is distinct from runtime invocation/dataflow.
- Owner(p): who controls the abstract port's change authority, not necessarily the same module into which the interface source is physically placed.
- D and e determine relevant requirements, allowable histories, error policy and the economic model; hidden or arbitrary environment shifts are not silently folded into proofs.

A **well-formed contract** has an explicit trace model, permitted inputs, error and termination behavior to the scope required; a type signature alone is insufficient.

## 3. ISP and OCP: demand-indexed observations (classical quotient theorem)

For total deterministic demand outputs g_d:X→Y_d, define

    x ≡_D y  iff  (∀d∈D) g_d(x)=g_d(y).
    q_D:X→X/≡_D.

A fixed interface observation o:X→Z admits downstream-only deterministic implementations h_d with g_d=h_d∘o for all d∈D precisely iff

    ker(o) ⊆ ⋂_{d∈D} ker(g_d) = ker(q_D).

Proof by defining h_d(z)=g_d(x) for any x with o(x)=z; independence of the representative is exactly the kernel condition. Already standard function factorization and observational quotient mathematics.

**ISP reading:** q_D is the coarsest *sufficient observable distinction* for that demand family, up to renaming labels. It does not decide the optimal count of methods, security exposure, or implementation cost.

**OCP reading:** if only new downstream decoders are permitted and o is frozen, a new d can be supported without changing the upstream information channel iff ker(o)⊆ker(g_d). Otherwise a colliding state pair is an impossibility witness *relative to the restriction*. General OCP permits other extension sites and therefore is not logically equivalent to this special theorem.

A change in D may make previously sufficient o insufficient. This is not a logical inconsistency in SOLID; it makes the domain of a design prescription explicit.

## 4. LSP: substitutability as behavior refinement, not type-name equality

**Safety-only contract refinement.** For every permitted input history h∈Pre_p, let T_i(h) be the set of visible outputs/traces emitted by implementation i and K_p(h) the allowed contract traces. A bounded safety substitution condition is

    Pre_p ⊆ Pre_i,    and    ∀h∈Pre_p: T_i(h) ⊆ K_p(h).

A replacement may allow *more* inputs (weaker precondition) and must offer *no behavior outside* the port's promises (stronger postcondition/guarantee), under the appropriate state abstraction.

**Classical client-safety lemma.** Suppose a client is verified safe for every trace in K_p(h) for all legal h, and implementation i refines K_p as above. Then binding i cannot produce a visible trace that violates that client's **trace-safety** property under the same histories: each emitted trace belongs to K_p(h), which the client already accepts. This is plain inclusion/transitivity and a restricted variant of established behavioral subtyping reasoning.

**Critical liveness caveat:** The empty trace set T_i(h)=∅ is a subset of any K_p(h), so safety inclusion by itself can be satisfied vacuously by a deadlocked/nonresponding implementation. Progress, termination, fairness, exception and eventual response guarantees need explicit additional clauses. We model a toy nonempty condition only in the bounded finite checker and do not treat it as a complete liveness semantics. Invariants and history constraints must remain in the client-visible specification.

**Trace counterexample:** With two readings in {0,1}, suppose a client requires nondecreasing observations K={"00","01","11"}. A provider implementing the same method names and individual value type but producing "10" violates LSP. Two otherwise equivalent implementations may type-check identically but differ under two-call history. A provider that accepts only "read" when the port clients may also invoke "configure" violates input-assumption substitutability, even if its outputs are good when it accepts the call.

LSP is a **semantic acceptability constraint** on a promised subtype or plugin substitute; unlike SRP, it is not a preference ranking of maintainability costs.

## 5. DIP: a separate structural/authority criterion

Let C be client/high-level policy module, P an abstract port, I a low-level implementation, and B the composition root/bootstrap. Under the **P33 strong source-inversion reading**, require:

1. (C,P)∈E_compile and (I,P)∈E_compile;
2. (C,I)∉E_compile and (P,I)∉E_compile;
3. Owner(P) is the client/policy side (or a stable independent contract authority), not dictated by I;
4. (P,I)∈Bind is configured by an authorized composition root separate from C's concrete source dependency;
5. I satisfies the port's behavioral contract in §4 for the specified legal client histories.

Conditions (1)–(4) identify a *strong client-controlled DIP architecture*. Item (5) additionally makes the implementation an **admissible substitution**. Physical module placement may vary: the real predicate needs explicit import edges and change-control authority, not just a class inheritance arrow. Other legitimate DIP implementations may use distinct ownership models, so this is a **chosen sufficient formal interpretation**, not the only industry definition.

- A client importing I directly may be perfectly LSP-safe but is **not** strongly inverted.
- Both C and I importing an interface P is not enough if P itself imports I or I unilaterally controls the port contract.
- A perfectly inverted compile graph does not make an I whose traces violate K_p safe.
- A stable port that satisfies LSP/DIP for D can still be inadequate for a **new demand D'** because the observation q_D loses needed distinctions. ISP/OCP must be rechecked.

Runtime call direction C→I *through a binding* may persist even when compile-time arrows point to P; DIP does not mean the runtime invocation direction is reversed.

## 6. Combined compositional certificate: safety, information and authority

For a proposed binding of I to port P and demand family D, define Boolean predicates

    Adequate(P,D) = [ker(o_p) ⊆ ker(q_D)]
    Refines(I,P) = [Pre_p⊆Pre_i and ∀h T_i(h)⊆K_p(h)]
    Progress(I,P) = [all stipulated liveness/nonblocking obligations hold]
    Inverted(C,P,I) = [source edges, injection and authority (1)–(4)].

The **P33 joint admissibility certificate** is their conjunction, with independently checked client specification and source contract provenance.

**Composition proposition (a cited synthesis of standard implications):** If all predicates hold, and the verified client uses only that port, and the emitted outputs from I are mediated by the same observation/trace abstraction, then:
- the demanded deterministic outputs have a factorization through o_p on the specified domain;
- the implementation's visible traces obey the client's safety contract, with progress according to the separately stated progress assumption;
- the architecture structurally satisfies P33's strong inversion reading.

**Proof:** factorization by §3, client safety by §4, graph/authority fact by the definition in §5. These are *different conjuncts*: removing the DIP conjunct does not automatically make behavior unsafe, and removing LSP does not change source graph direction. The integration is an **interpretive map of established mathematical facts** and not a purported deep new theorem.

**Independence counterexamples**, each with the other coordinate intact:
- **LSP but not DIP:** client directly imports a well-behaved concrete provider.
- **DIP but not LSP:** client/impl share a client-owned port but the provider emits "10" under an expected nondecreasing-history contract.
- **LSP+DIP but not OCP for d_new:** current port observation o_A tells only the first bit of a 2-bit source state; d_new asks for second bit. The port cannot recover it downstream without an independent information channel.
- **DIP graph but no genuine inversion authority:** concrete implementation owns/can mutate the supposed abstract contract or the port imports concrete implementation.
- **Trace-safety but no progress:** a silent provider has an empty bounded trace set.
- **ISP-minimal vs DIP extension convenience:** an information-minimal client-specific narrow port may require a new port/binding on a future demand; a wider boundary may be cheaper over some request distributions, but can impose irrelevant capabilities. ORIGIN-R1-P11 WIDE versus SEGREGATED is a concrete historical context, **not proof of a universal ordering**.

These demonstrate *why the five SOLID principles should be treated as coordinated constraints and conditional decisions, not as five equivalent formulas*.

## 7. SRP supplies change-conditioned cost, and PPH connects the maxims

For two change reasons A,B, with rates p_A,p_B,p_AB and costs c_g,c_a,c_b,k,λ (as stipulated in the preceding P33 document):

    C_group=c_g(p_A+p_B-p_AB)+λ(p_A+p_B-2p_AB)
    C_split=c_a p_A+c_b p_B+k.

This compares ownership choices **after** ensuring the required behavior and information conditions. A design with a lower expected SRP cost does not thereby satisfy LSP or adequately expose new OCP-required data.

A richer underlying decision problem, *without proposing an ungrounded scalar utility*, is:

    Feasible(e,D) = {a : all required contract/observation/substitution predicates hold}
    Pareto(e,D)   = nondominated S/L/C/A vectors of a∈Feasible(e,D)
    Policy(e,D)   = context-conditional admissible choices, with explicit abstention/ties.

This is where P18's Principle-as-Projection Hypothesis can be given a **formal interpretation**: a named principle is an explanation-level selector or projection over a region of Feasible(e,D) and Pareto(e,D), not a universal premise that forces the same architecture in every environment. No claim of general empirical optimality follows without a specified objective ordering and true demand distribution.

**The coherent five-principle picture:**

| SOLID | Mathematical role | Claim type |
|---|---|---|
| **S** — responsibility | choose a decomposition of authority along demand-change reasons, minimizing an explicit conditional cost (subject to behavioral feasibility) | conditional architecture policy |
| **O** — extension | closure of permitted downstream extensions under a demand-indexed observation, with factorization obstruction witnesses | admissibility boundary + policy choice |
| **L** — substitution | preserve promised client-visible behaviors/traces, input acceptance, invariant/history and stipulated progress | semantic contract gate |
| **I** — segregation | choose demand-sufficient capabilities and avoid irrelevant consumer obligations, allowing tradeoffs against future extension | information/capability design policy |
| **D** — inversion | orient **compile-time** source dependencies toward stable client-policy-owned abstractions, with injection, while binding only LSP-admissible implementations | structural/authority design policy + compatibility gate |

**Interpretive title candidate:** *Contract–Observation–Authority Geometry: A Conditional Mathematical Reconstruction of SOLID Design Principles.* This is a candidate paper title for the P33 theoretical strand, not a renaming of the P33 research stage.

## 8. Finite verifier and reproducibility

[Executable](../../tools/law-r1-p33-lsp-dip-contract-graph.mjs) tests all 4096 triples (I,K,Safe) of trace subsets over Σ²={00,01,10,11} for classical safety inclusion transitivity, and separately:
- accepting good vs bad-history vs overly strong-precondition providers;
- silent trace provider as the vacuity warning;
- source graph scenarios: proper client-owned inversion, direct concrete import, port importing concrete, concrete provider owning port;
- LSP-safe/direct-import, DIP-satisfied/LSP-unsafe, both satisfied/new demand information-insufficient;
- source-rooted P33 predecessor quotient model: existing [65,536 finite factorization checks](../../tools/law-r1-p33-demand-quotient.mjs) and already-known Uptime Kuma certificate-context collision.

The test is a finite **model** of dependency ownership; it does **not parse or certify the actual Uptime Kuma production dependency graph**. The combined hosted read-only workflow retains pinned source checks and human authoring, no repository writeback. **Verified read-only hosted run:** [37883377979](https://github.com/WhoSia/EvoNOMOS/actions/runs/37883377979) SUCCESS, job 113667872029, artifact `11595032811`, SHA256 `03d9ba0d338006071dc09c542ffbaf4a2e2f4a7bc815095e5c711f2b18651de9`. The workflow also completed the predecessor bounded source repair and demand-quotient checks. The new finite model checks 4096 trace-set triples and its independent LSP/DIP/ISP/OCP counterexamples. No full production JavaScript import graph was extracted.

## 9. What remains open

- Full programming-language behavioral subtyping with unbounded mutable states and concurrency: cite Liskov–Wing and interface automata; do not silently infer from finite traces.
- A faithful API ownership/source import and runtime binding extractor from actual OO code. The P33 finite graph is deliberately manually specified.
- The OCP/ISP-versus-DIP tradeoff under the historically executed P11 WIDE/SEGREGATED worlds; precise Q, cost scope, and independent context must be read from archived seal rather than guessed.
- Theorems stronger than the composition of well-known quotient/refinement/interface properties, only if worthwhile; **no novelty compulsions**.
- Manuscript-quality introduction, proofs, adversarial counterexamples and full citations. Interpretive scholarly contribution is already legitimate with the above scoped mathematics.

**P33 theory verdict:** \`P33_INTEGRATED_SOLID_INTERPRETATION_COMPLETE_AT_BOUNDED_MODEL_LEVEL__LSP_DIP_FINITE_CHECK_HOSTED_PASS__P33_OPEN__LAW_R2_NOT_AUTHORIZED\`.

## 10. Research-literature acquisition and disclosure policy — 2026-10-09

**Required on every future new paper recommendation or citation:** explicitly mark `Drive: HELD` with verified canonical Drive ID, or `Drive: NOT FOUND BY INDEXED SEARCH` with an authentic, checked **direct downloadable PDF URL**. When a DOI/publisher link is all that exists, label it as a landing page, not PDF. Never assert a PDF was downloaded or ingested unless actual Drive metadata proves it. Search alternate author/title/DOI terms to avoid duplicate intake; PDF arrival goes to 00_INTAKE, then original-first-page and duplicate audit prior to P&K canonical rename and 10_PAPERS move. This also applies to references in prose, Notion Harvests and future paper drafts.

### Newly cited, not currently located in indexed Drive search

1. **Liskov & Wing (1994), A Behavioral Notion of Subtyping.** Drive: NOT FOUND. Direct author PDF: https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf ; DOI 10.1145/197320.197383.
2. **Martin (1996), The Dependency Inversion Principle.** Drive: NOT FOUND. Direct original author PDF: https://objectmentor.com/resources/articles/dip.pdf ; historical C++ Report column, not a journal research paper.
3. **de Alfaro & Henzinger (2001), Interface Automata.** Drive: NOT FOUND. Direct university-hosted PDF: https://web.cs.wpi.edu/~heineman/html/teaching_/CS562/p109-de_alfaro.pdf ; **corrected** DOI 10.1145/503271.503226. Previous 10.1145/503209.503226 was bibliographically wrong for the cited ACM ESEC/FSE article. This correction overrides earlier unverified P33 DOI text.
4. **Ye, Martinez, Durieux & Monperrus (2021), A Comprehensive Study of Automatic Program Repair on the QuixBugs Benchmark.** Drive: NOT FOUND. Direct author-deposited journal-version manuscript PDF: https://arxiv.org/pdf/1805.03454 ; JSS DOI 10.1016/j.jss.2020.110825.
5. **Huang et al. (2023), A Survey on Automated Program Repair Techniques.** Drive: NOT FOUND. Direct arXiv PDF: https://arxiv.org/pdf/2303.18184 ; arXiv 2303.18184.

**Already in canonical Drive; do NOT request again:** Parnas 1972 and 1979, Sullivan et al. 2001, Tishby et al. 1999/2000, Angerer 2019, Hong 2024, Cai/DRSpaces, Reiter 1987, SemFix 2013, DirectFix 2015, Angelix 2016, Smith et al. 2015, Guigue 2014. This list is a scoped lookup summary, not a claim of full-library exhaustive enumeration.
