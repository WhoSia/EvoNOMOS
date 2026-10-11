# EvoNOMOS Generation VIII LAW-R1-P42-P2 — Source-Revision–Indexed Behavioral Counterfactuals & Observer Completeness: Native Router Grammar Interventions, Before/After Client Traces, Causal Repair Certificates & Classical Contextual Refinement

**Official P42-P2 paragraph name confirmed by user (2026-10-11 KST) · TCS-centered empirical/formal court · P42 RUNNING · Historical permission still UNKNOWN · LAW-R2 NOT_AUTHORIZED.**

## Executive mathematical question

The next EvoNOMOS question is **not** "which more quasi-axioms should we add to SOLID?" It is:

> For a real source revision transition (s_0\to s_1), which client contexts (c\in C) distinguish the resulting programs; what information is lost by a projection of observations; and what is the least distinguishing context family relative to an explicitly fixed hypothesis class?

These are classical **theoretical computer science (TCS)** questions of observational equivalence, finite-state distinguishability, refinement and hypothesis-relative test-suite characterization. A meaningful source-level structural result need not—and should not automatically—be dressed up as a novel fundamental mathematical axiom.

**Actual result:** For the unchanged historical Echo v4 commits from [PR #3132](https://github.com/labstack/echo/pull/3132), 5 preregistered contexts were executed on *each* original Go revision, for **10 original-source client traces**. Two old previously admitted client paths became 404; one request still returned 200 but changed its parameter interpretation; an old `/health` client remained invariant; and a client handler deliberately masking its HTTP output produced the exact same HTTP status/body despite different internal parameter bindings. **A richer observation splits an equivalence class collapsed by the coarse HTTP projection.** This is a bona fide source-grounded **bounded observational structure**; the general mathematics and the underlying tools remain classical.

## 1. Provenance and genuine preregistration

- Historical Echo v4 PRE source **`5440f99719cc8de4be2ae6abfc8f275302791730`**, exactly the sole actual Git parent of the POST commit.
- POST source **`f085ffbe8f99de165bd920746920000ab56bd6bc`**, real successful merged source PR #3132, not a synthetic router rewrite.
- Changed source files [route_path.go](https://github.com/labstack/echo/blob/f085ffbe8f99de165bd920746920000ab56bd6bc/route_path.go), [router.go](https://github.com/labstack/echo/blob/f085ffbe8f99de165bd920746920000ab56bd6bc/router.go), route_syntax_test.go and router_test.go. Actual parent/child source provenance independently recorded by [P42-P1 #38132709607 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38132709607).
- [Five-client behavior and TCS preregistration manifest](../../tools/p42/p2/preregistered_router_behavior_and_tcs_contexts.json) frozen at EvoNOMOS commit **`27311aa94e95c645d38f447be9a402b18f048163`** *before* P42-P2 native Go test files existed.
- [Pre-native standalone GitHub CI gate #38133170573 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38133170573) certifies manifest schema, expected statuses, exact original revision identities and **absence of native P42-P2 test file at freeze time**.
- Native workflow also checks the freeze SHA is a Git ancestor, requires byte-for-byte identical manifest to frozen commit, verifies both original Go source checkouts, checks POST Git HEAD^ equals PRE and verifies P42-P2 test file was absent in the prereg commit.
- **Not a blind external software forecast**: PR #3132 and its upstream author's tests were already inspected to design this follow-up. This is *pre-execution* data collection with a frozen selected-client oracle, not a novel unseen issue-prediction result.

## 2. Actual native original-Go source outcome

[Go source fixture](../../tools/p42/p2-native/counterfactual_source_test.go) executes in the **two exact original Echo v4 Go module checkouts** with no modifications to upstream source. Registration: `GET /r/:name\\:cancel`; independent stable `GET /health`. Handler records real `Context.Path`, `ParamNames`, `ParamValues`, `Param("name")`, handler identity, count, HTTP status, body and header. Two output views are compared: a diagnostic handler that exposes binding in the body, and a masked handler always returning HTTP 200 / body `MASKED`.

[Original Echo before/after Go Actions #38133360441 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38133360441), tested EvoNOMOS harness HEAD **`7001347761c10c612b7decab17548ac3dbf00ca7`**, artifact **`11699264733`**, SHA-256 **`c115a87c40cb3c7e4c955414438f3f209ba44c9c76b0580e60bdfc9db7b6277f`**. Native source-run transcripts were compared against the exact frozen manifest by [original-source Python audit](../../tools/p42/p2/audit_native_contexts.py), including five prescribed status pairs and hidden-binding changes.

| Declared request | PRE original v4 (5440f997) | POST original v4 (f085ffbe) | Observation judgment |
| --- | --- | --- | --- |
| `GET /health` | HTTP 200, body `health`, same named handler, one invocation | exact same full declared observation | bounded old-client invariance |
| `GET /r/foo` | HTTP 200, executed parameter route; `ParamNames=[name\\:cancel]` | HTTP 404, no handler executed | **source-realized admission/old-client regression** |
| `GET /r/foo:cancel` | HTTP 200; route param name `name\\:cancel`, value `foo:cancel`, `Param("name")=""` | HTTP 200; route param name `name`, value `foo`, `Param("name")="foo"` | **same HTTP status, different binding** |
| `GET /r/foo:other` | HTTP 200 | HTTP 404 | **source-realized admission/old-client regression** |
| masked `GET /r/foo:cancel` | HTTP 200, body `MASKED`, route selected | HTTP 200, body `MASKED`, same handler ID and route template, but changed internal name/binding | **same coarse HTTP observation, different handler-accessible semantic state** |

This is not a post-hoc redefinition of which old clients count. The original selected client suite was frozen before executing either P42 native fixture.

The source behavior is explained by the **real router grammar rewrite**, not by a broad SOLID label: the old source treated the escaped colon following a parameter as part of its parameter name, admitting arbitrary single segments. The changed source recognizes a literal inline verb and binds only the parameter prefix when the required verb is present. **Within the finite frozen corpus**, post-change route acceptance is a strict reduction for the parameter-only and alternate suffix requests, while the accepted `foo:cancel` request has different binding semantics. Do **not** extrapolate global language inclusion or all future client behavior without a general parser proof.

**Runner engineering transparency:** the original native CI [#38133345408 FAILED](https://github.com/WhoSia/EvoNOMOS/actions/runs/38133345408) only at a provenance gate because default shallow checkout excluded the POST commit's parent. The action was repaired by fetching depth two, with no change to frozen forecasts or original Echo source; final #38133360441 SUCCESS.

## 3. TCS semantics: observations, quotient refinement and separating contexts

Fix a source-indexed program semantics (\llbracket s\rrbracket : C\to T), with contexts (C) containing registered route grammars plus client request. Let `T` include explicitly permitted handler observations (not only HTTP output). Choose a **projection** (\pi:T\to O), e.g. status/body-only, or richer status/body/handler binding. Then for an observation family (Q\subseteq C), define

[
 s_1\;{\sim_{Q,\pi}}\; s_2
 \iff \forall c\in Q,\quad
 \pi(\llbracket s_1\rrbracket(c)) =
 \pi(\llbracket s_2\rrbracket(c)).
]

This is the kernel equivalence relation of the restricted observation map. If `π_fine` retains all observations that `π_coarse` retains, together with additional fields, then

[
\sim_{Q,\pi_{fine}}\;\subseteq\;\sim_{Q,\pi_{coarse}}.
]

**A strictness witness is now original-source grounded**: for the same masked request and handler, PRE and POST have identical status 200/body `MASKED` but disagree on `ParamNames`, `ParamValues` and `Param("name")`. Therefore they lie in the **same coarse HTTP class but different handler-accessible trace classes** on the chosen probe.

Importantly, an external HTTP-only client cannot see internal `ParamNames` if the handler deliberately masks them. The distinction becomes visible **only** when the observer family includes the application handler, its effects or an instrumented permitted trace. The diagnostic handler independently shows how it may become a real HTTP client-visible change if the application uses the parsed parameter in its output.

This is classical **contextual equivalence and refinement of observation kernels**, with conceptual kinship to **Myhill–Nerode distinguishability**, **Paige–Tarjan partition refinement** and automata **W-method characterization sets**. The present router fixture does **not** establish the conditions for applying a complete DFA/FSM conformance theorem, nor a minimal universal suite for unbounded Go HTTP routing semantics.

### Formal selected-world model and minimality

[Lean `P42ContextualSeparation.lean`](../../tools/p42/lean/P42ContextualSeparation.lean) defines:
- Three finite `World` hypotheses: PRE, POST and a **hypothetical** third implementation.
- Four abstract context names and a small status/parameter trace signature, reflecting selected original evidence only; `health` is invariant.
- Explicit coarse status projection with an inline-verb case where coarse observations agree but full observations differ.
- Separation predicates `distinguish suite x y` and `separates suite`; a two-context set `[bare,inlineVerb]` distinguishes all three *declared* worlds.
- A counterexample for **every singleton test query**: no one-query suite distinguishes all three hypotheses.
- Observer refinement of a full contextual equality into equality of status projections, but a concrete failure of the converse.

**Critical evidence boundary**: the third world is mathematical, **not** a third historical Echo version. “Two queries are minimal” applies to this three-hypothesis finite family, NOT the two actual source revisions (where one distinguishing request is enough) and NOT arbitrary Echo programs. These are classical finite separation facts rather than new axioms.

**Independent Lean 4.34.1 kernel VERIFIED:** [GitHub Actions #38133411294 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38133411294), checked exact proof HEAD `15c7ee28895ba91c8b6c53cc9bfac9e27e747ea7`, artifact `11700301485`, SHA-256 `e340d6d0a070731587214f26c07f16c015e6365811c356cc60f4cb3e93eaf38b`. The existing P42 proof workflow's 7-job Lake build explicitly compiled `P42ContextualSeparation` and independently ran `leanchecker` successfully. The theorem `bare_inline_is_separating_for_three_hypotheses` and the derived `no_single_query_separates_all_three_hypotheses` apply **only to the specified three-world family**, one world of which is hypothetical. Earlier [#38133230543 FAILED](https://github.com/WhoSia/EvoNOMOS/actions/runs/38133230543) because a Lean proof script attempted an `intro` on an already simplified goal; a revised, explicit equal-observation obstruction lemma gave an independently checked proof without changing the intended mathematical claim.

## 4. Classical reduction and genuine next theoretical frontier

- [CMU programming languages program-equivalence lectures](https://www.cs.cmu.edu/~fp/courses/15312-f02/lectures/22-equiv.html) already discuss observational equivalence and labeled transition/bisimulation ideas.
- [Myhill–Nerode theorem (math lecture notes)](https://www.maths.tcd.ie/~stalker/11602/notes/10.8-the-myhill-nerode-theorem.html) characterizes regular languages by residual-equivalence classes of distinguishing continuations.
- [Paige & Tarjan, 1987, *Three Partition Refinement Algorithms*](https://doi.org/10.1137/0216062) is a landmark for computing/coarsening partitions.
- [Complete Test Suites for Automata in Monoidal Closed Categories (2025)](https://link.springer.com/chapter/10.1007/978-3-031-90897-2_10) states that finite-suite completeness is **relative to a fault domain**: a finite suite cannot certify arbitrary implementations just because it distinguishes known examples.

**Strong classical competitor:** a source-aware contextual semantic model given identical PRE/POST source and the same observer budget predicts that inline-verb grammar and parameter binding change; ordinary partition refinement accounts for the altered observational quotient. It survives. There is no legitimate “P42 beats classical” result in this bounded data. The source-to-observer bridge and the *minimality relative to a nontrivial, independently justified fault domain* are the actual next mathematical hurdles.

## 5. Research stopping conditions and RAVEL decisions

**PROMOTE:** original Echo source-specific counterfactual result; genuine strictness of the selected HTTP-output vs handler-accessible observational quotients; frozen source/version/checkpoint provenance; conditional source-language grammar non-monotonicity in sampled requests.

**HOLD:** unbounded contextual equivalence for every Go client, source-to-Lean parser semantics correctness, complete handler-effects provenance, universal minimal context basis, security/authorization legitimacy of the original merge, and any fundamental new mathematical law.

**NEXT work within P42-P2:** require a source-realized *fault domain* of alternative repairs/implementations, an independently fixed observer family and prospective distinguishing tests; attempt finite-state abstraction with a simulation or failure certificate; measure whether additional source contexts genuinely refine partitions or merely duplicate existing witnesses. For actual PRE vs POST alone, a single request `/r/foo` already distinguishes them by HTTP status; do not present the two-probe theorem for the synthetic three-world domain as evidence that two are needed for this real pair.

**P42-P2 status: bounded original historical Echo v4 source before/after court VERIFIED (#38133360441) and finite observational TCS Lean kernel VERIFIED (#38133411294). Scope: P42-P2 first original-source/finite-theory court BOUNDED_PASS; P42-P2 further source-realized fault domains, all-context operational semantics and source-to-Lean bridge remain OPEN. P42 RUNNING; LAW-R2 NOT_AUTHORIZED.**
