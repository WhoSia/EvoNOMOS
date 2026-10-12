# EvoNOMOS LAW-R1-P42-P2-R9 — Demand-Indexed Ownership Contracts and Repair Feasibility: Actual gRPC Client Contexts, Typable Alias Counterexamples, and the Limits of Structural Type Repair

**2026-10-12 KST · R9 original Go bounded PASS · no new universal TCS/OO theorem · P42 RUNNING · LAW-R2 NOT_AUTHORIZED.**

## Why would anyone do this?

A reviewer asks: *“Why test an artificial broken pool when the library already typechecks?”*

Because compiling a patch answers **whether it is accepted by the language**, not **whether it preserves what an existing client relies upon**. When a library migrates a public provider interface, many candidate adapters may compile, yet a network application's simultaneously outstanding payload buffers must not unexpectedly affect each other. A patch planner optimizing only method signatures can select a wrong candidate even with a fully green build. This is a mechanism of practical interest to library upgrades, dependency migration, protocol safety and source-level repair automation. **No claim that gRPC itself contained the fabricated bug.**

The intended *scientific explanandum* extends far beyond a Boolean "good buffer pool": for architecture state `s`, demand `d`, source edits `e`, and observations `Q_d`, study the **set of actual code-level repair options** that preserve the relevant clients, the transitions across future demands, and their cost vector.

[
\mathcal{F}_{s}(d)=\{e\in E_s : \mathrm{Compile}(s[e])\land
  \mathrm{ContextuallyRefines}_{Q_d}(s[e])\land\mathrm{Meets}_d(s[e])\}.
]

A robust theory has to explain how responsibility/interface/ownership boundaries alter the shape and reachability of these sets, **not** just repeatedly prove type compatibility does not imply behavioral compatibility.

## Evidence: source-real, frozen, replicated

[P42-P2-R8](P42_P2_RAVEL_R8_BEHAVIORAL_BUFFER_OWNERSHIP_AND_TYPED_REPAIR_REFINEMENT.md) tested two type-conforming authored implementations of the [unchanged historical grpc-go `mem.BufferPool` API](https://github.com/grpc/grpc-go/blob/9ab8b62505c85a5e03be1ae97949e960e24b6d4f/mem/buffer_pool.go), showing the deliberate aliasing provider violates a selected concurrent-outstanding-buffer isolation observation. R8 source native #38218758703 SUCCESS.

R9 added an original shipped **`mem.NopBufferPool`** comparator, keeping the same historical gRPC source commit and two *distinct* declared client contracts:
1. `C_iso`: while `a` is outstanding, mutating independently acquired `b` may not overwrite `a[0]`.
2. `C_return`: a researcher-declared **legacy adapter migration** contract: return of mutated bytes to the designated old backend must be observed. This is **NOT a demonstrated universal gRPC production client requirement**.

Frozen [R9 hypothesis registry](../../tools/p42/p2-r9/frozen_client_demand_and_provider_choices.json) created at commit `a69f7e59c82f68314e81665e6e88260ab57d699f`, before R9 native Go fixture existed; [prereg workflow #38220102503 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38220102503). The original-Go [source court #38220200873 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38220200873) tested HEAD `d1e50aedb5108a5958d3c0d5b2a629577bc2ed36`, artifact `11734375630`, SHA-256 `99e60a1dec129c6f88af781350bb6efbbb7a0dbe5b5cea40b08c635a7765417e`. The run enforces ancestor freeze, manifest byte equivalence, prior absence of native fixture, unchanged original source SHA, three structural Go assertions and all six acceptance markers. [Exact Go test fixture](../../tools/p42/p2-r9-native/demand_options_test.go).

| Provider | Compiles as actual `mem.BufferPool` | `C_iso` | `C_return` |
|---|---|---|---|
| Original upstream `mem.NopBufferPool` | yes | yes | no: no designated old backend in fixture |
| Researcher-authored legacy adapter | yes | yes | yes |
| Researcher-authored shared-backing pool | yes | **no** | no |

**Avoid invalid upgrading of a missing legacy backend to a general gRPC violation**. This experiment tests acceptance relative to an explicitly specified migration context. For the three declared candidates (P),

[
\mathcal A(C_{iso})=\{Nop,Adapter\},\quad
\mathcal A(C_{return})=\{Adapter\},\quad
\mathcal A(C_{iso}\land C_{return})=\{Adapter\}.
]

The sets are nested here. They show a **demand-conditioned strict restriction**, not a preference reversal, global source edit minimality, or two incomparable Pareto fronts. Any stronger "repair-option reversal" statement must exhibit an actual independent demand/metric pair and source-executed alternatives.

## Real research novelty gate: what R9 does NOT establish

Type-correct providers with different behavior and requirement-relative acceptance sets are wholly explainable by **behavioral subtyping, contextual refinement and separation/ownership logic**. Those strong classical approaches SURVIVE on the very same observation budget. Finite type-conforming alternatives plus a handcrafted deliberately wrong pool establish a useful *counterexample*, **not novelty**.

Further, `Get`/ `Put` method type definitions themselves do not enforce nonaliasing, unique ownership, thread safety, capacity discipline, exactly-once release or client performance. Each obligation requires its own well-scoped clients/evidence. An unsafe synthetic provider is not a shipped gRPC implementation nor proof of a production defect. A local Go test is not a full proof for all buffers/sizes/schedules. The R9 source fixture is deterministic and single-threaded, specifically avoiding a false claim of race freedom.

## What would convince a demanding outsider?

**An objectively useful result would be a repair-selection procedure on real library migrations with known clients that (i) excludes compilation-only false positives; (ii) returns source-realizable candidate edits and a checkable failure witness; (iii) predicts held-out requirement sequences better, cheaper or more informatively than equal-budget classical analyzers; and (iv) respects authority/evidence constraints instead of assuming every writable file may be changed.**

That is falsifiable:
- freeze independent, historically traceable **actual consumers** and their observables;
- discover real patches and alternative commits, not only author-defined faulty stubs;
- record both compiling edits and behaviors, including mutation, ownership escape and reclaim;
- compare a strong classical source-aware solution using separation logic, effect and alias analysis, behavioral refinement and constrained source-edit optimization;
- measure a cost **vector** (compile admissibility, preserved client obligations, modifications, runtime resource use), never invent a scalar universal OO goodness;
- isolate an identifiable source-structural explanation of **future repair reachability**: two equivalent current implementations with different reachable safe future adaptations, with a genuine source-validated edit transition graph.

The founding structural research goal remains: **under what demand and source constraints does modularity, port splitting, provider substitution or owner localization *cause* new safe repair paths—or eliminate them?** This could yield a useful conditional theorem; if standard refinement/real-options/change-impact models already derive it, that classical adequacy is a publishable negative-novelty conclusion.

## Proposed precise next court

**P42-P2-R10 — Consumer-Grounded Repair Reachability & Ownership-Effect Games: Historical gRPC Call-Site Witnesses, Alternative Source Patch Paths, Demand-Conditional Feasibility Boundaries & Equal-Information Classical Countermodels.**

R10 should require a fixed genuine historical gRPC consumer using two concurrently outstanding slices (or explicitly record if no historical consumer source can be found). Build multiple actual source edit transitions whose legitimacy/compilation/client outcomes are independently witnessed. Attempt a minimal *conditional* source patch or explain why multiple incomparable fixes survive; compare a strongest classical implementation under the same accessible evidence. Avoid claiming a new theorem just for showing the aliasing stub fails.

**R9 bounded Go source PASS; demand-indexed repair source geometry beyond this finite candidate table OPEN; historical consumer proof OPEN; LAW-R2 NOT_AUTHORIZED.**
