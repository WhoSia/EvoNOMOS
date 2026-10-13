# EvoNOMOS LAW-R1-P42-P2-R11 — Independent Consumer Ownership Contracts, Conditional Source-Repair Composition and a Non-Circular SOLID Reduct

**Phase:** R11-P0 SOURCE DISCOVERY + MATHEMATICAL PROGRAM / EXTERNAL NATIVE COURT NOT YET RUN. **Parent:** [R10-P3 checked source edit paths](P42_P2_RAVEL_R10_P3_MULTISTEP_REPAIR_SEMANTIC_COMPOSITION_AND_ORIGIN_CONTEXT.md). **Prior freeze:** [R11-P0](../../tools/p42/p2-r11/frozen_independent_consumers_and_composition_hypotheses.json), sealed at `ce8a91808631556707b33f203b4a17ba5a5bf365`, before this paper.

## 1. What actually changed from R10

R10's sole authentic maintained consumer was the **inside-grpc-go** 2024 `mem.Copy / Buffer.Free` execution path; the additional `sharedPool`, alternative adapters and return-count requirement were authored by the researchers. R11 has now **read actual external source files from separate project repositories**, not merely searched names.

| Independently maintained source | Direct inspected code | Distinct client-relevant obligation | Source readiness |
| --- | --- | --- | --- |
| [Cortex codec, `pkg/cortexpb/codec.go`](https://github.com/cortexproject/cortex/blob/master/pkg/cortexpb/codec.go) | `encoding.RegisterCodecV2`, original `mem.Buffer`, `Get / Put`, `mem.NewBuffer`, `ReleasableMessage.RegisterBuffer`, Nop/default pool selection | Message ownership may escape into a releasable message rather than be returned immediately; alternative `Unmarshal` path chooses Nop pool for non-releasable messages | SOURCE CONFIRMED, independent repo; version-matched 2024 native compile/test NOT DONE |
| [Google Cloud Storage Go, source ref `37f936ac`, `storage/client_test.go`](https://github.com/googleapis/google-cloud-go/blob/37f936ac9d69e173da0ba4123e382c52b2dd741f/storage/client_test.go) | `testBufferPool.Get/Put` wraps `mem.DefaultBufferPool`; `TestReadCodecLeaksEmulated` injects `expgrpc.WithBufferPool` and checks allocated vs freed bytes | Original client-level tests independently observe resource-return accounting in a real storage protocol | SOURCE CONFIRMED, pinned Git ref from October 2026; not a confirmed *contemporaneous 2024* consumer |
| [Milvus codec buffer pool, source ref `4610a590`](https://github.com/milvus-io/milvus/blob/4610a590c49ee5d15b81d8d10d3ef15853458745/pkg/util/resource/codec_buffer_pool.go) | Private tiered `mem.BufferPool` using `sync.Pool` for dirty buffers, separate fallback, documented overwriting-before-publication responsibility | Allocation/reuse can preserve stale contents; correct consumers must initialize all visible bytes, distinct from simple release/alias contracts | SOURCE CONFIRMED; provides distinct implementation, not yet native tested or validated as 2024 historical consumer |

These are **three different program roles** (codec with prolonged ownership, protocol integration with independent accounting, dirty-memory provider). They must NOT be portrayed as all implementing or consuming the same exact call site; the external consumer/provider wiring still needs qualification. The sources were found in public code indexed around 2026; the assumption of contemporaneous 2024 provenance has not yet passed.

## 2. Source-state and context semantics without assuming SOLID

Define a typed source evolution system independently of any design maxim:

```text
P : actual source trees, build graph and interface signatures
E : typed edits (including create/delete source file and dependency wiring)
A(s,e,o) : owner o may perform edit e from source state s
C : client execution contexts with visible traces and resource obligations
D : future requirements (not necessarily known at design time)
T(s,c) : execution traces of source s in client context c
Safe(s,c) : observed client contract holds over traces T(s,c)
-> : compilation-valid, owner-authorized source-edit transition
```

An architecture `A` in this system is a **subgraph of typed source states and allowed edits**, not an arbitrary numerical SOLID score. A source-level interventional comparison chooses two otherwise matched architectures `A,B`, the same existing clients, genuine independent future requirements, and registered outcomes (e.g. correctness, regressions, capability feasibility, changed code, optional effort measures).

For a sequence `H=(s_0,e_1,s_1,...,e_n,s_n)`, old client preservation is `∀i∀c∈C_old Safe(s_i,c)`. Future repair feasibility relative to a policy `Γ` and demand `d` is the existence of a **finite authorized transition path preserving the old clients at each step** whose endpoint satisfies `d`. This notion is classical labelled transition-system reachability with invariants unless a strictly stronger theorem or prediction is obtained.

### Composition of two owner-separated source edits

Suppose two independently maintained modules have source states `s_1,s_2`, ownership authorities `Γ_1,Γ_2`, edits `e_1,e_2`, and a shared boundary interface `B` observed by clients. Let `s_1⊗_B s_2` mean a *defined* linked system (undefined composition is not silently treated as safe).

**Sufficient conditional composition proposition (restricted):**

Assume:

1. Both edits are authorized, type- and build-preserving in **every** intermediate linked source state.
2. Each edit contextually refines its own module's client-observable traces under an explicit **rely condition** on the other module and the shared ownership interface.
3. Each edit preserves the other module's rely condition (**frame stability**), including `Get`/release ownership obligations, aliasing, and publication visibility at `B`.
4. The relevant client observations of the linked system are captured by the specified interface-local trace assumptions; no hidden cross-boundary side effects or extra clients exist within the declared scope.
5. The two chosen source edit paths are actually linked and checked at each stage, with no unmodelled owner/authority changes.

Then the composition of their validated edit stages preserves the specified combined old-client traces (up to the declared contextual refinement relation); the final composite meets new demands only **if those demands were separately proved for the endpoint**. The argument is classical assume/guarantee + frame-style reasoning, and assumes precisely the conditions needed to transport the local refinements. **This is a sufficient proof schema, not a novel unconditional theorem.**

**Countermodel when framing is omitted:** two locally safe modifications each return the same physical region as an available buffer to an independent consumer while an outstanding reference to it still exists. Without shared lifetime/alias guarantees, each isolated test can pass, yet a linked client witnesses a corrupted first payload. This is consistent with R10's actual Go negative-control phenomenon, though R11 has **not** reproduced it inside the external Cortex/Storage/Milvus programs. Consequently, disjoint changed files, separate repository owners, or a matching method signature **alone do not imply safe source-edit composition**.

## 3. SOLID as a non-circular **restricted interpretation** only

Do not add SOLID to the source model's axioms. Instead define independent primitive properties from real source edits, client traces and dependency/authority structure:

- **Responsibility partition (`R`):** chosen change obligations are associated with separately editable regions, relative to a registered demand family.
- **Extension preservation (`X`):** a new demand can be implemented without violating specified old clients and frozen-region restrictions.
- **Substitutive refinement (`S`):** one implementation refines another under an explicitly identified client set, precondition and trace contract.
- **Interface observation restriction (`I`):** each client has a required capability/observation footprint, and unnecessary demands may be absent from that client's interface.
- **Dependency boundary factoring (`D`):** explicit module/client obligations can be routed through a designated stable contract rather than concrete implementation identity.

Given *chosen* precise definitions of SRP, OCP, LSP, ISP, and DIP, an interpretation may associate them with restricted predicates of `R,X,S,I,D`. That is **definability/interpretability** inside the typed source evolution universe, NOT a theorem that all software obeys SOLID, that all original verbal versions of SOLID have unique formal meaning, or that SOLID's conjunction is a necessary/sufficient criterion of architecture superiority.

To avoid a tautology: the primitive relation `Safe` is specified from independent client oracles and actual source execution, **not by requiring SOLID**. The proposed `R,X,S,I,D` conditions can be false or incomparable in a given program. An eventual "proper restricted fragment" statement needs a genuine **strict inclusion witness**: two systems sharing the prescribed restricted SOLID signature but distinguished by resource lifetime / old-client repair path ability, with independent compilation and source evidence. Earlier P40 local-SOLID* versus globally conflicting `chi.Mount` was a scoped candidate of precisely this pattern, **not** a proof about every canonical SOLID formulation.

## 4. Falsifiable context-dependent architecture advantage, before native outcome

The next measurement must compare **two source-level design alternatives under matched independent demands**, not code fabricated solely to satisfy a favored structural predicate.

**Registered qualitative predictions (not experimental outcomes):**

- If a source modification is local to an implementation and the direct architecture already has a stable single modification point, a new adapter boundary is not predicted to improve that modification's minimum changed-source support. P34's prior genuine Restic source comparison already found one edit site in each alternative in one single-write demand, so a universal "more indirection improves change locality" prediction is already falsified for that context.
- If the external consumer must retain a buffer past the initiating call and another consumer needs release-accounting observability, an architecture that enforces ownership transfer at the boundary **might** make some future changes admissible; but it may also add restrictions, extra coordination, or an illegal intermediate edit path. Do **not** preregister that it must win. Check the two sides of the predicted context reversal with independent actual source consumers.
- A successful discriminating experiment must compare strong rivals with the **same real source**, old client contracts, hidden outcome labels, actual maintainers' edit rights (or clearly synthetic rights), and repair grammar. A classical ownership/alias model plus standard incremental refinement and conventional adapter changes must be considered before any EvoNOMOS-specific explanation is promoted.

These claims are potential independent *prospective* tests. No outcome measurements, sign reversal, novel math theorem, or independent three-repo original-Go CI PASS is asserted in R11-P0.

## 5. Prior-art defeat gates

The most direct modern theoretical rival is [Conditional Contextual Refinement (CCR, POPL 2023, DOI 10.1145/3571232)](https://doi.org/10.1145/3571232), specifically unifying contextual refinement composition with conditional specifications and modular ownership. Other immediate rivals are the separation-logic frame rule, rely-guarantee, contextual equivalence, trace semantics, source-level alias/points-to analysis, and finite graph/CSP reachability. Each is **prior art**, not a discovery attributed to EvoNOMOS.

Mathematical novelty would require a formally proved nontrivial property of **source-authorized edit families and prospective client contexts** not immediately reducible to these established mechanisms, with a genuinely different prediction under equal evidence. The role of SOLID is at best a rigorously defined **partial interpretation** in that larger model, and the reduction has to be independently checked.

**Next court:** historical source version custody → specific external compiled consumer on compatible grpc-go baseline → consumer's own old-client test run → paired source architectures with genuinely later demands → allowed edit sequence composition and head-to-head classical attack. Keep P42 RUNNING · P43 HOLD · LAW-R2 NOT_AUTHORIZED.
