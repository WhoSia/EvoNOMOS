# EvoNOMOS G8 P42-P2-R11-P7 — Prospective Architecture-Repair Dominance under Independent Demand and Maintainer Authority

**Scientific status (2026-10-13):** Real independently maintained Chi/Gorilla source: original native Go PASS. The genuine BEFORE-PR-reveal demand classifier ABSTAIN; separate AFTER-PR-reveal / BEFORE-native exact source forecast PASS. Strong source-aware classical prediction matches all source outcomes. Original upstream source edits and actual contributor legal rights not assumed. New-law authority HOLD; P42 RUNNING, P43 HOLD, LAW-R2 NOT_AUTHORIZED.

## 0. Actual question and sample boundaries

The founding question is not whether inheritance, modularity or SOLID sounds desirable. It is **which source-level design under independently originating demand, protected old clients, editable regions, resource and release constraints retains safe feasible repair paths at lower conditional cost; why does its relative advantage reverse or disappear?** Source-run repair effects, mathematical sufficiency and strong classical explanations must be kept separate.

Authentic independently evolved competing original Go modules:
- [go-chi/chi core at 67be7d9c](https://github.com/go-chi/chi/tree/67be7d9cafdaeb4e04e887ff78d09e030ee43b00), radix routing, original source mux.go SHA-blob 6dc1904d9b6b99ab5e5f36c376cf777f512063f6. Real source calls setPathValue(rctx, r) after matching; the matching route remains accessible via chi.RouteContext(...).RoutePattern().
- [gorilla/mux core at b4617d0b](https://github.com/gorilla/mux/tree/b4617d0b9670ad14039b2739167fd35a60f557c5), ordered route list, original source mux.go blob 1e089906fad5715477ba0c785562a43f0d987a8a, route.go blob e8f11df221f089306926ac23775906a4a50cde62. Matched values available through mux.Vars, template via mux.CurrentRoute(...).GetPathTemplate().

The original cores are naturally evolved; the one-handler adaptation below is explicitly human research-authored in the project tests. It is not an accepted upstream patch, not evidence of an upstream permission grant, and not a production equivalence proof.

## 1. Chronological pre-registration without forecast laundering

1. [Phase A seal WhoSia 79872f3b](https://github.com/WhoSia/EvoNOMOS/commit/79872f3b44cbe4740d9304795870fb626c8c9c4b) fixed both original repo refs and **prior-to-reading-PR-content** demand selection: first two chronologically created merged Chi PRs matching the frozen query (repo:go-chi/chi, route, 2025-01-01 through 2026-09-15), no cherry-picking; five predeclared demand categories and ABSTAIN for others. The source and cost-budget comparators were named before the heldout content reveal.
2. After freezing Phase A, the returned first two were [Chi PR #985](https://github.com/go-chi/chi/pull/985), created 2025-02-23 / merged 2025-08-15 by contributor catatsuy, and [Chi PR #986](https://github.com/go-chi/chi/pull/986), created 2025-03-03 / merged 2025-08-26 by contributor Gusted. #985 is a **PathValue usage documentation/example** (the original Chi source ALREADY supported this function). #986 is actual Go 1.23 Request.Pattern propagation implementation in mux.go, two build-tag files and a native test. This is independently originating real software change demand, though only merged PRs are sampled.
3. **Phase A stricter sign/repair prediction grade = ABSTAIN**, as standard Go-request field propagation is not among the frozen demand sign categories. Retrospectively declaring the two PRs to be correctly predicted architectural wins would be false.
4. After the PR body/diff reading but BEFORE writing the native P7 test code, [Phase B WhoSia pre-native behavioral matrix 2a4062d3](https://github.com/WhoSia/EvoNOMOS/commit/2a4062d3c76b561a66ecfbe9fb44c21dc1f0df01) separately recorded concrete original-2024 router source outcome predictions and strict fail criteria. Thus Phase B is a real preregistered native SOURCE verification, **not** blind future-demand forecasting.

## 2. Native original source evidence, bounded observer

The same old GET /health handler returns exactly HTTP 200, literal OLD and is called once under each source. The same new GET /users/Ada handler is bound to GET /users/{userID}; both original cores already extract route param Ada to their private route context. Future request #985 requires standard http.Request.PathValue("userID")=Ada; #986 requires standard http.Request.Pattern="/users/{userID}".

| Original source configuration | Old 200/OLD once | Private param | Standard PathValue | Standard Pattern |
| --- | --- | --- | --- | --- |
| Chi original 2024, NO edits | PASS | Ada | Ada | empty |
| Gorilla original 2024, NO edits | PASS | Ada | empty | empty |
| Chi original + project test-only handler adapter | PASS | Ada | Ada | /users/{userID} |
| Gorilla original + project test-only handler adapter | PASS | Ada | Ada | /users/{userID} |

The project-authored handler adapter obtains already present route context, applies req.SetPathValue and req.Pattern assignments. Original upstream core implementation is SHA-pinned and not touched. Original Go runtime tests and race tests PASS in [first complete hosted source court #38342521453](https://github.com/WhoSia/EvoNOMOS/actions/runs/38342521453); original fixtures: [Chi](../../tools/p42/p2-r11-go/r11_p7_chi_original_router_test.go) and [Gorilla](../../tools/p42/p2-r11-go/r11_p7_gorilla_original_router_test.go). First complete artifact ID 11786918967, SHA256 32110545c72d5185d5f7d0b0c4d43e937f9009c8ec96286125fc390d33eca57a. Root module's selected source and race tests were executed, NOT every upstream package's entire test suite.

This is **not** evidence the original Gorilla maintainer implemented or even accepted either feature. It shows selected application client-side adapter reachability in unchanged source.

## 3. Same-demand authorized repair frontier, limited to one explicit grammar

Define research-rights regime Gamma+ as allowing one client handler adapter addition, and Gamma0 as forbidding this additional research-side source edit. These are **counterfactual research-user permissions**, not historical legal/institutional upstream access. Under the precisely enumerated grammar {unchanged source, one new handler adapter}, the minimal additional adapter-operation count is:

| Exactly requested later feature | Chi Gamma+ | Gorilla Gamma+ | Gamma0 restriction |
| --- | ---: | ---: | --- |
| Old client only | 0 | 0 | Both 0 |
| #985 standard PathValue | **0** | 1 | Chi 0; Gorilla not repairable |
| #986 standard Pattern | 1 | 1 | Both not repairable |
| #985 and #986 jointly | 1 | 1 | Both not repairable |

This is a finite two-state exhaustive proof **under one operation grammar**: compare actual native unmodified versus adapter traces against fixed demands; reject forbidden edits and select minimum path length. It does NOT establish repository-wide minimal patch size or lower real developer effort; some other unseen patch might solve either demand more cheaply.

Crucial discovery boundary: **a missing public standard request field is not equivalent to information lost by the source program**. Chi's internal RoutePattern and Gorilla's CurrentRoute/GetPathTemplate preserve sufficient source information to fill this future request port. The P33/Parnas deterministic criterion kernel(observation) subset kernel(required-output) distinguishes truly irretrievable information from adapter/wiring/ownership obstacles.

## 4. Equivalent semantics, measured source-running costs

On the first same physical Go 1.23.12 CI runner, paired order Chi→Gorilla→Gorilla→Chi, 3 Go benchmark repetitions per order and one bounded matched GET /users/Ada, the two test-only repaired adapters both meet the exact declared public observation. Bench latency/alloc values (6 raw repetitions each) are:

| selected matched future client | median ns/op | B/op | allocs/op |
| --- | ---: | ---: | ---: |
| Chi + handler adapter | 1036.5 | 1492 | 13 |
| Gorilla + handler adapter | 1643.0 | 2276 | 19 |

These are one host's descriptive matched-client measurements. They include distinct adapter implementation costs; they exclude original full lifecycle build/deployment/migration/review costs. The 2026-10-10 P36 O10/O11 source experiments on Chi and Gorilla already showed that changing route workload and integrated lifecycle length changes rank, including nonmonotonic timing ranks. Do not assert intrinsic global Chi superiority or erase those earlier opposite cells. Later CI reruns retain their own raw medians; never silently reuse first-run numbers as current run results.

## 5. Equal-information strongest rivals and correction log

[Independent classical actual-native-data scorer](../../tools/p42/p2-r11/p7_equal_information_classical_native_frontier.py) receives **the same exact original source facts, protected observable fields, edit grammar and rights regimes** as HARC. Classical source-aware call resolution and guarded trace refinement predicts all raw/adapted Go outcomes; finite reachability gives the same 0/1/unreachable frontier. On this case, HARC has **NO distinctive predictive advantage over classical theory**. CCR 2.0 (Song & Cho, 2025, Enhanced Vertical Compositionality and relational sep-logic), Iris (Jung et al. 2018 RA/ghost state), DimSum (Sammler et al. 2023 event-based multi-language linking), Simuliris (Gäher et al. 2022 concurrent fair contextual refinement), de Alfaro/Henzinger interface automata 2001 and Sullivan et al. real-options 2001 remain live. These academic proof assistants have NOT been run with a translated actual full Chi/Gorilla program; do not call the comparator execution a mechanized CCR/Iris benchmark.

The first extra scorer CI attempted to parse nested template braces in native Go log with a non-greedy regex and FAILED at the independent Python parsing step. The original Go tests, race tests and benchmark had already PASSED. Correction touched **only the parser**, retained both original frozen manifests and source fixtures; it was not a source hypothesis failure.

## 6. Mathematics: what is general, why it is not automatically novel

A history-enriched source state H has actual code, dynamic dispatch/route-context, client promises indexed by release, resource ownership and a time-indexed eligible edit relation Gamma. For finite demand d and budget B define R(H,d,Gamma,B) as the set of all **intermediately safe** legal source-edit paths leading to d, with vector costs. Compare Pareto minimal frontiers, not an invented generic scalar "modularity score".

**Conditional reachability/abstraction theorem (classical):** if a projection pi from history states respects initial protected observations, legal edit labels, cost labels, future demand goals and successor projected states, then projected-equal states have equal reachable repair-cost frontiers at every bounded finite path horizon. Proof: induction on legal path length with cost and objective preservation. This is a classical costed labeled transition-system bisimulation/congruence principle, **not** a new theorem of general programming languages. Its practical hard part is a *sound, useful, compressed and independently forecast-capable source extractor* for real Go/Ruby/function/data/event architectures under actual governance and old consumers.

**Three distinguishable obstructions to safe downward-only extensions:**
1. Information: raw observation o collapses source states required by the future demand; strict kernel-factorization obstruction (P33 Uptime Kuma example).
2. Institutional source scope: enough data is present but the allowed source actions do not include a needed adapter; actual upstream rights currently UNKNOWN, counterfactual Gamma0 is explicit.
3. Intermediate resource/history frame: accessible data is not safely composable across lifetime or temporal updates (actual R10/R11 gRPC-Go buffer-pool case).

These distinctions allow the five SOLID operational fragments developed in [R11-P5 HARC](P42_P2_R11_P5_HARC_HISTORY_CONDITIONED_REPAIR_CALCULUS_SOLID_AS_CONDITIONAL_FRAGMENTS.md) to be **conditional projections of a broader source-edit ontology** without pretending informal SOLID is one theorem or that abstract class boundaries are always optimal.

## 7. Harvest genealogy and new ambition

Read Notion EvoNOMOS Literature Harvest F15, F19, F20–F27, F31, F66–F71, F77–F79 and founding constitution:
- P33 demand-relative quotient and conditional five-principle interpretation were already established. No originality claimed for the factorization theorem.
- F20 API Braess needs endogenous interface-owner coordination, not merely the fact that adding a wrapper costs something.
- F21: sampling merged PRs selects on survival; no inference to abandoned/rejected future change difficulty.
- F22/F25: endpoint feasibility differs from source-safe staged migration, with temporary adapters possibly worthwhile.
- F23: same dependency graph can have different feasible repair sets under different histories of protected contract and rights.
- F24: real PR #985 is a strong negative control — a merged example documenting already available capability, **not** an implementation-repair event.
- F27: exaptation is possible; an earlier source capability proved useful later, but this does not show the earlier maintainer predicted that later demand.
- F66–F71: independently evolved Chi/Gorilla pair, matched contract Q21, resource sign reversals and failed simple lifecycle timing threshold predate P7 and limit overclaim.
- F78/F79: global rights/non-factorization and future repair quotient remain serious formal problems.

**New primary scientific goal:** prospective claims that discriminate equal-info source-aware classical rivals for *unseen demand ecologies and actual costed owner-constrained path frontiers*, including negative controls, rejected/abandoned requests, and at least one truly independent functional/event-driven program. If strong rivals continue predicting equally, the honest output may be a rigorously integrated but **attributed, non-novel** mathematical framework for architectural decision-making, not a fabricated alternative universal law.

**Current:** Real original core and client native PASS, source-aware classical adequate, first phase strictly ABSTAIN, second phase PASS, rights beyond past public integration UNKNOWN. P42 RUNNING · P43 HOLD · LAW-R2 NOT_AUTHORIZED.
