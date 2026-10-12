# EvoNOMOS Generation VIII LAW-R1-P42 — P42-P2-R5 Capability-Obligation Coupling & Demand-Correlation Geometry: Source-Realized Interface Boundaries, Consumer-Specific Conformance, Change-Propagation Cuts & Conditional Pareto Reversals

**2026-10-12 KST · user-approved P42-P2-R5 · RAVEL frozen 4×4 original Go-language source/typecheck experiment · source-bounded mechanism PASS · independent Lean kernel evidence tracked separately · P42 RUNNING · P43 NOT_AUTHORIZED_YET · LAW-R2 NOT_AUTHORIZED.**

## 0. Return to the founding explanandum, not an exercise in pseudo-axioms

EvoNOMOS began by asking **when actual object-oriented and modular source structures give a consequential advantage under changing external demands**, with opposite structural regimes and testable reversals. [R4 canonical](P42_P2_RAVEL_R4_DEMAND_INDEXED_REPAIR_TRANSITION_SYSTEMS_AND_OPTION_FIBERS.md) demonstrated source-realized future-demand-dependent and time-order-dependent minimum edit routes, while avoiding the false whole-lifecycle claim that a larger upfront source surface always wins.

R5 moves from **one fallback route registration** to a *genuinely typed* Go interface/provider/consumer/composition-root source mechanism. Instead of inventing five independent SOLID axioms, ask:

> Which provider capability obligations does a consumer boundary induce, where do source changes propagate under a specified future demand, and when does bundling versus splitting the boundary reverse its lifecycle cost advantage?

The mathematical object is a demand-indexed *incidence/cut geometry* of provider capabilities, consumer requirements and source-edit locations. Neither this definition nor the minimal change site counting is mathematically novel relative to classical structural subtyping, information hiding, feature dependencies, module impact analysis and finite edit systems.

## 1. Epistemic source scope and frozen oracle

**Real source:** all 4 baselines, 16 future altered programs and 3 intentionally non-conforming programs are **actual compiled and executed native Go 1.25 source files** (`contracts.go`, `core.go`, `read_client.go`, `export_client.go`, `assembly.go`, `providers.go`, `main.go`) in *isolated module assemblies generated from a checked-in Go-source generator*. Go itself, not an in-chat Python surrogate, admitted or rejected interface conformance and produced actual output. The independent grader inspected actual generated source file bytes and counted specified edited signature/wiring/forced-method locations.

**Source provenance limit:** these are **researcher-authored Go alternatives**, not historical independent Go repository architectures, not changed original Echo upstream and not an existing production codebase. They instantiate **original, unmodified Go language method-set/typechecking semantics**, but are not a proven generalized original-source external benchmark. This distinction is central to the scope of conclusions.

[Frozen 4×4 hypotheses](../../tools/p42/p2-r5/frozen_capability_demand_matrix.json) were authored **before the native case generator existed**, at original freeze ancestor `16bf17a36bdc38852228b36dae8ca37764173de9`. Independent [pretest GitHub Actions #38207620728 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38207620728) validates sixteen exact forecast site-vectors and explicitly tests that the generator file was absent at freeze. The native workflow independently replays the original ancestor, byte compares the frozen manifest and rejects the generator if it existed before freeze.

### Four architecture/source conditions

| Candidate | Selected clients depend on | Interface shape | Initial interface declarations |
| --- | --- | --- | ---: |
| BUNDLE_DIRECT (BD) | concrete `*Core` | no interface actually consumed | 0 |
| BUNDLE_PORT (BP) | port/interface | one **two-method** bundle contract `Read()+Export()` consumed by both clients | 1 |
| SEGREGATE_DIRECT (SD) | concrete `*Core` | no interface actually consumed | 0 |
| SEGREGATE_PORT (SP) | ports/interfaces | one **Read-only** and one **Export-only** contract | 2 |

**Negative factorial identification note:** BD and SD have identical effective Go interface semantics because their clients are concrete. The BUNDLE/SEGREGATE factor is not actively realized in DIRECT, which is deliberately a **negative control**: interface declaration intentions cannot generate an effect unless the source graph actually routes clients through the interface boundary. Do not claim four fully distinct structures.

### Four future demand types

- **R:** replace READ provider only with `ReadAlt` implementing `Read()`; export continues via `Core`.
- **X:** replace EXPORT provider only with `ExportAlt` implementing `Export()`; read continues via `Core`.
- **RX:** two independently supplied partial providers, `ReadAlt` and `ExportAlt`, serving respective clients.
- **C:** one correlated combined provider `BothAlt` implementing both methods, serving both clients.

All starting programs return `READ0/EXPORT0`. After each intervention the 16 native compiled programs return the preregistered partial/coordinated replacements. **RX and C have the SAME delivered client outputs but DIFFERENT distribution of methods across actual provider types**: a meaningful source structural intervention independent of current output.

## 2. Native source/typechecking and measured edit-site vectors

[Go source generator](../../tools/p42/p2-r5/make_native_cases.py), [source-byte/Go-output independent audit](../../tools/p42/p2-r5/audit_native_go.py), and [Go native CI](../../.github/workflows/g8-p42-p2-r5-native.yml) checked these registered vectors:

Each cell is the count of source locations changed relative to the respective architecture's baseline, **not** total changed lines, LOC, engineer-hours, deployment cost or performance. One changed concrete consumer signature counts 1, one changed composition-root provider construction expression counts 1, and one extra **irrelevant provider method** required to typecheck a bundled interface counts 1. New useful provider implementations are also present, but **tracked separately** because they are required by the demand and are not a propagation cost difference across architecture regimes.

| Architecture | R (partial read) | X (partial export) | RX (two partial providers) | C (full coordinated provider) |
| --- | ---: | ---: | ---: | ---: |
| BUNDLE_DIRECT | **2** | **2** | **4** | **4** |
| BUNDLE_PORT | **2** | **2** | **4** | **2** |
| SEGREGATE_DIRECT | **2** | **2** | **4** | **4** |
| SEGREGATE_PORT | **1** | **1** | **2** | **2** |

**Mechanism, not scoreboard:**
- `DIRECT`: partial new provider cannot be passed to a consumer demanding concrete `*Core`; changing one consumer concrete argument type propagates a source signature edit per replaced client, beyond one composition-root wiring edit.
- `PORT`: the consumer signature is unchanged when new provider satisfies the corresponding interface; composition-root wiring still changes.
- `BUNDLE_PORT`: a read-only replacement with only `Read()` is rejected by the real Go compiler because the client port also demands `Export()` that it NEVER calls. An extra adapter method is required just for the broader interface's type obligation. Symmetrically, exporting alone forces `Read()`. Two independent partial providers force TWO extra methods; one combined two-method provider (C) forces NONE.
- `SEGREGATE_PORT`: each consumer requires only the selected capability; a partial provider typechecks without extra irrelevant methods. But its *birth-time* interface declaration surface is larger (two narrowly scoped interface definitions vs one bundle).
- BD vs SD exactly tie in this experiment. An unused structural intention is not an active causal treatment.

**Negative compiler attack:** intentionally omit irrelevant adapter methods in BP for R, X and RX: **3 real Go build failures**, each requiring the relevant missing method, while corresponding fully adapted source variants compile and run. This shows structural conformance is a language-checkable obligation, not a diagrammatic hypothesis.

[Native Actions #38207862662 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38207862662), checked exact native harness HEAD `77bbb3e0ab66b173606bfee1af84b0a5c0186bbd`; artifact **`11728200630`**, SHA-256 **`ebabd04b5215a1fc2f7137e77b4e60802817caa65bdb60404407fac05caf7d9d`**. Results: **4 baseline runs, 16 altered Go compilation+run successes, 3 authentic negative compiler rejections, 16 independently checked exact source edit-site vectors**. The artifact includes actual materialized Go files, compile failures, outputs, source hashes, and grader receipt.

## 3. TCS interpretation: capability-obligation incidence and change-propagation cuts

For a consumer (c), let (R(c)) be the set of methods its **actually typed** boundary requires, and (K(p)) the methods a candidate provider (p) supplies. The omitted *method obligation set* is:

[
\Delta(c,p)=R(c)\setminus K(p).
]

The Go compiler accepts the port substitution only when (Delta(c,p)=\varnothing). This is ordinary **structural type satisfaction**, not a novel theorem.

For a read-only provider `ReadAlt`, (K(p)=\{Read\}):

[
R_{BP}(read)=\{Read,Export\},\quad
R_{SP}(read)=\{Read\}.
]
Hence

[
|\Delta_{BP}(read,ReadAlt)|=1,qquad
|\Delta_{SP}(read,ReadAlt)|=0.
]

For independent replacements RX, deficits sum across separate providers: BP=2, SP=0. For a correlated new provider implementing both methods, (K(BothAlt)=\{Read,Export\}), and **both interface designs have zero deficits**. Thus the source-observed **interaction** is between boundary granularity and the correlation structure of replacement provider capabilities, not a universal single-axis "interfaces small good" ordering.

A source-propagation cut can be represented by the vector

[
v_{E}(a,d)=(\#\text{consumer signatures},\#\text{wiring expressions},\#\text{forced methods})
]

for architecture (a), demand (d), grammar (E). For R: BD/SD ((1,1,0)), BP ((0,1,1)), SP ((0,1,0)). **Two programs may have the same scalar count 2 while their edit vectors and failure mechanisms differ**: BD's change propagates into consumer source; BP's obligation propagates into provider method implementation. A scalar loses information about direction, authorship and downstream source compatibility.

The **initial declaration surface** adds a separate coordinate. BP requires one shared interface declaration and SP two narrow definitions. Without conditioning on demand correlation and the policy used to value future forced implementation, "always segregate" is false. **But those counts are not actual total lifecycle financial cost.**

## 4. Conditional Pareto reversal, with sensitivity transparent

For an *illustrative one-shot*, choose a hypothetical partial-provider arrival probability (p), and weight (w>0) assigned to a forced irrelevant method implementation. Count only initial interface definitions (BP=1 vs SP=2) plus **differential** future forced method obligations; the common one-call composition wiring and demand-required useful method implementations cancel under this restricted comparison:

[
C_{BP}-C_{SP}=-1+p w.
]

- If (p w<1): BP scores lower on this declared synthetic scalar; a coordinated full provider C gives (p=0).
- If (p w>1): SP scores lower; independent partial arrivals become sufficiently frequent or expensive.
- If (p w=1): tie.

**Neither (p) nor (w) was estimated from real engineering work**; this is a conditional mathematical preference boundary, not a productivity claim. In a multi-event stream, changes to provider types can reoccur and initial interfaces may be revised, so the one-shot formula is **not** a result for arbitrary R→X→C sequences. For comparisons including DIRECT, consumer signature edits and caller-compatibility effects must remain separate terms; there is no defensible single winner for all four options.

## 5. Mathematically checked structural claims and novelty barrier

[P42CapabilityObligationGeometry.lean](../../tools/p42/lean/P42CapabilityObligationGeometry.lean) is the bounded formal model of:
1. **Structural conformance** of read-only/export-only providers for bundled vs narrow ports, and of a combined provider under both.
2. The 4×4 declared finite source-site edit vectors and a correlated-vs-independent provider obligation difference.
3. **No effect of unused BUNDLE vs SEGREGATE intention** when clients are concretely typed DIRECT.
4. **Nonfactorization through current behavior**: all four baselines have the same selected READ0/EXPORT0 outputs but future forced method obligations differ, so future obligation cannot be derived solely from current output.
5. A conditional up-front-versus-late surface reversal as an integer count/weight theorem.

**Independent Lean 4.34.1 kernel VERIFIED:** [GitHub Actions #38208092970 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38208092970), exact source HEAD `c25487826c0f154a59d4899a439f1d1df8cb8649`, artifact `11727944285`, SHA-256 `53154bd77f93e78937882b9071b1c043f1e3c385348770865c5438aaeb0ba0e6`. The proof covers restricted Go-method incidence/conformance, 16 registered source-site forecasts as finite equalities, source-grounded mode collapse in DIRECT, correlation-sensitive forced method obligations, present-output-to-future-obligation nonfactorization and an integer-count conditional boundary. First CI [#38208011335 FAILED](https://github.com/WhoSia/EvoNOMOS/actions/runs/38208011335) solely because of an unnormalized Nat addition in the final surface-order lemma; the repair normalized the expression without changing its mathematical proposition. This independent Lean model is related to actual Go by checked example correspondence, **NOT** a formally proved source-to-Lean full abstraction or interpreter correctness theorem.

The underlying mathematics is **classical**: structural subtyping, incidence relations, finite path counting, method-set obligations, information hiding and change propagation. The true next scientific obstacle is a source-derived, predictive theorem about **demand-dependent propagation cuts** that remains valid across nontrivial independently observed codebases and beats equally informed existing dependency-graph analyses. Neither GO nor Lean in R5 establishes such novelty.

## 6. Classical rival court and hard negative outcome

Real relevant antecedents include:
- **B. Cafeo, E. Cirilo, A. Garcia, F. Dantas & J. Lee, 2016**, *Feature dependencies as change propagators: An exploratory study of software product lines*, [DOI 10.1016/j.infsof.2015.08.009](https://doi.org/10.1016/j.infsof.2015.08.009). This study of five evolving product lines directly examined dependencies and change propagation and concluded that merely minimizing feature dependencies is not necessarily the right improvement objective; coupling effects depend on the properties of dependencies.
- **J. D. McGregor, 2003**, *The Evolution of Product Line Assets*, [CMU SEI publication](https://www.sei.cmu.edu/library/the-evolution-of-product-line-assets/). Product-line artifacts propagate change along their dependency relations and require disciplined evolution management.
- **D. L. Parnas, 1972**, *On the Criteria to Be Used in Decomposing Systems into Modules*, DOI 10.1145/361598.361623. Information hiding seeks to limit the visibility of unstable design decisions across consumers.
- Source-aware Go interface method-set checking and ordinary dependency-cut counting predict the exact table **with the same information as EvoNOMOS**. The classic comparator is explanatory and **not an independently blinded implemented external prediction contest**.
- Earlier P42 [R4](P42_P2_RAVEL_R4_DEMAND_INDEXED_REPAIR_TRANSITION_SYSTEMS_AND_OPTION_FIBERS.md) already acknowledged DeltaCCS, featured transition systems and finite source edit graphs.

There is a research-relevant **negative factor result**: only **PORT** makes the interface boundary causal in this narrow controlled study; within DIRECT, bundle-vs-segregate labels alone have no effect. There is also a genuine **source-level conditional interaction** between provider capability distribution (separate vs correlated) and forced unwanted methods. But there is **no new nonclassical TCS law yet**.

## 7. P43 decision: DO NOT advance yet

**Scientific decision: P43 NOT YET AUTHORIZED. Keep R6 inside P42.** R5 gives a portable mechanism hypothesis, but the evidence consists of researcher-authored Go microprograms, only 16 variants and an illustrative unmeasured lifecycle weighting. Creating P43 now would risk substituting an attractive theorem name for real evidence of a domain transition. P42 still owes:
- **Independent source ecosystems**, including real historical interface/provider and caller changes, rather than one generated Go vocabulary;
- **Prospective frozen future demands** that were not used in constructing the source case generator, and a real external client population;
- An independently implemented **classical propagation-cut/impact analysis model** with the same source and contract information, rather than a manually labelled equal-information table;
- **Type-and-effect/compatibility semantics** and source edit grammar with actual diff-based edit consequences, including cross-package API consumption and backwards compatibility, not only source sites in a compiled microprogram;
- A conclusive P42-P4/P5 comparative court and stopping/publication verdict before strong novel-law promotion.

### Proposed next paragraph

> **P42-P2-R6 — Cross-Ecology Capability-Propagation Cutsets & Demand-Indexed Program Refinement: Historical Interface Changes, External Consumer Compatibility, Independent Classical Predictors & Minimal Source-Repair Certificates**

This is a proposal for the **next P42** work unit, not a claim it has run.

**P43 should be considered only after R6 and an external P42-P4/P5 scientific synthesis distinguish what is adequately explained by existing software product-line theories from any genuinely irreducible research target.** Then propose a P43 research question arising from evidence, not from numbering momentum. **R5 CLOSED_AS_BOUNDED_NATIVE_GO_AND_FINITE_TCS_COURT (both original Go language CI and Lean independent kernel SUCCESS). P42 RUNNING; P43 NOT_STARTED; LAW-R2 NOT_AUTHORIZED.**
