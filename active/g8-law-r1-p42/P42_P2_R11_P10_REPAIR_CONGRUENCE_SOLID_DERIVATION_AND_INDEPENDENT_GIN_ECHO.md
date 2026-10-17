# EvoNOMOS R11-P10-P0 — Rights-Aware Repair Congruence and Conditional SOLID Derivation

Date: 2026-10-17. Status: Generation VIII LAW-R1-P42 RUNNING; R11-P10-P0 experiment OPEN, not a scientific PASS or LAW-R2. The existing HARC R11-P5 already supplies conditional fragments of SRP/OCP/LSP/ISP/DIP. We extend the question to exact source-rights repair prediction, rather than rebranding old conditional theorems.

## 1. The mathematical primitives do not assume SOLID

Let S consist of source-history states s=(P,L,R,G,C,H): source P, linking and dispatch L, runtime resource/alias effects R, evidenced authorized edit relation G, independently protected client contracts C and actual history H. Client k yields a declared trace Obs_k(s), including optional interface type assertions when a client is entitled to test them. A future independently specified demand d has a goal predicate Goal_d(s). Permitted source edits are labelled transitions s --(e,c)--> s' with source-right checks, buildability, stagewise preserved old clients, and nonnegative **vector** costs c. The path repair-cost frontier is

F(s,d) = ParetoMin { sum_{step in path} c(step) : path is finite, authorized, stagewise old-client-safe, and ends in Goal_d }.

If input rights or costs cannot be verified, abstain; an empty frontier proves impossibility only under the specified grammar, not for every conceivable repair. No SOLID principle or preferred architecture is an axiom.

## 2. RC1: exact cost-labelled repair congruence (classical)

A relation R on source-history states is an action-and-cost-labelled bisimulation if related states (a) agree on every protected client predicate and specified future goal, and (b) match each admissible labelled source edit, including its cost and authorization, with a transition to related successors, **in both directions**.

**RC1 theorem.** If s R t, then for every declared d, their sets of attainable costs of finite authorized, stagewise protected, goal-reaching repairs are equal; therefore F(s,d)=F(t).

**Proof.** By induction on path length. Length zero: related states agree on goal and protection, so zero cost is achievable in one iff in the other. For n+1, bisimulation matches the first authorized edit with equal label and cost and related successor; the induction hypothesis matches the suffix cost. Reverse simulation yields reverse set inclusion. Cost-set equality implies equality of Pareto-minimal costs. QED.

**Scientific boundary:** The hard part is producing a *source-certified* bisimulation that tracks owners, intermediate rights, real resource effects, versions and cost vectors. Bisimulation and weighted transition systems are classical; no novelty against CCR 2.0, Iris, DimSum, Simuliris or standard repair-state modelling is asserted.

### Why three intuitive quotients differ

1. HTTP body/status only: original sources can both return (200,old) while one exposes a Flush capability and another does not. A client demanding Flush distinguishes them.
2. HTTP plus method-set capability still omits rights: an owner may permit the capability-adding edit in one state and forbid it in an otherwise identical state, making future repair costs differ or one declared frontier empty.
3. HTTP plus relevant capability plus authorization can be an adequate *finite* repair quotient if its permitted edit transitions match; irrelevant hidden source tags may then be safely forgotten.

The [8-state finite checker](../../tools/p42/p2-r11/p10_structural_repair_quotient_court.py) enumerates Flush availability, edit authorization and irrelevant source tags. It deliberately rejects the first two abstractions, proves the last is a cost-labelled bisimulation in the constructed model, and computes F(Flush-present,d)={(0,0)}, F(Flush-absent/editable,d)={(1,1)}, F(Flush-absent/no-edit-right,d)=empty. These are **toy-source edit costs** (one synthetic source edit plus review), not measured real Gin/Echo engineer-hours.

## 3. RC2: capability observability creates a method-set complexity obstruction

For k genuinely independent optional Go interfaces that declared clients distinguish by direct type assertion, every fixed dynamic concrete wrapper type has a fixed k-bit method-set signature. If all 2^k input signatures are possible and old clients require exact signature preservation, at least 2^k **observationally distinct output wrapper signatures** must be representable. A conditional dispatcher selecting an appropriate concrete wrapper for each input signature suffices at the type-assertion level.

**Proof:** Exact preservation maps each distinct observed input signature to its same distinct output signature. Otherwise two distinguishable old clients collapse into one outcome, contradicting preservation. Pigeonhole yields the lower bound. Selecting one suitable wrapper per signature gives existence. QED.

If the *actual protected clients* observe only a subset of coordinates, the bound drops to the number of their distinct projected signatures. This bridges source-level obligations and a version of ISP: minimizing protected observable capabilities reduces required compatibility distinctions, but over-narrowing a port destroys correctness. No general LOC, implementation-type count or maintenance optimum follows. Go ResponseController/Unwrap or effectful methods require richer observational semantics. This is classical Go method-set logic, not a new theorem in mathematical priority.

## 4. Under these more primitive conditions, five SOLID principles follow conditionally

Each statement is an operational fragment, not a universal derivation of the original English slogans. The premises are program observations, verified source port cuts, rights and noninterference, not the SOLID rule itself.

**SRP:** Let source support split into X and Y with independently checked noninterfering edit semantics, rights and runtime frames. If a separately specified demand affects only X, an authorized X-path transports through Y without modifying Y. Proof: commute every X edit past stable Y; client traces for Y remain fixed at each step. This is a conditional separation of change reasons, not a recommendation for single-purpose classes in every system.

**OCP:** Assume an immutable protected core C interacts with extension E only through a fully observed port I. Independently verify a permitted sequence editing E (not C), preserving old port trace/refinement at each intermediate state, and satisfying new d. Old clients factor through I, hence remain protected; no core source edit occurs. This is precisely the restricted closed-core/open-extension consequence of the classical frame/port theorem.

**LSP:** Independently specify clients' admitted trace sets, including exceptional/resource returns. If a substitute produces only traces permitted by the old provider for every declared client context, then substitution maintains every such client. Proof: set inclusion of context-indexed traces. Subtype names do not prove this hypothesis, and a concrete forbidden trace falsifies it.

**ISP:** Independently source-verify that a client family observes only port projection I1 and edits to another port I2 do not modify I1 traces, source rights or resources. Then I2-only edits preserve that family's contracts by trace projection. Splitting method signatures alone does not certify noninterference.

**DIP:** Source and link analysis must establish that a stable core depends on providers only through a fully effect/capability-complete port I. If two independently maintained providers satisfy I, and provider substitution is legitimately authorized, the core need not be edited and old clients see the same/refined I trace. This does not assert abstraction has zero overhead or that every independent implementation actually implements identical effects.

These conditional proofs refine the ones already recorded in HARC R11-P5, and use RC1 to specify when a *compressed* port description is strong enough for **exact repair-cost forecasting**. No unique axiomatization of all SOLID slogans is claimed.

**Important Pareto subtlety.** When C is strengthened to C', permitted path sets shrink, but their Pareto-minimal cost frontiers need not form nested sets. Example: paths with costs 1 and 2 give frontier {1}; protecting an extra client can remove the cost-1 path, leaving frontier {2}. Never infer the frontiers themselves are subsets. Vector preferences require explicit decision rules.

## 5. Two independent maintained Go source architectures, prereg before native execution

[Freeze commit 35a3c898](https://github.com/WhoSia/EvoNOMOS/commit/35a3c8980206d38b4f65c508650336a453ecfbdd) records exact original Gin and Echo commits, later heldout PR IDs, source-conditioned predicted responses, classical rival and no-hindsight policy **before** the new original-Go tests.

- Gin source commit d3ffc9985281dcf4d3bef604cce4e662b1a327a6, response_writer.go blob 9035e6f1fd794d54063d6f50c3490e64d35a3647. Its Flush forwards only if underlying implements http.Flusher; unsupported writer silently bypasses delegation.
- Echo source commit 86d0223c7aa39b865a9452de3479897fcb5a3939, response.go blob 4da729c4786898ddb2dc361c19a303e55d149540. Its Flush invokes http.NewResponseController(...).Flush and signals ErrNotSupported via panic.
- Both independent historical real sources satisfy the research-authored old HTTP GET 200 / old test. Independent new future **client policies** conflict: graceful/no-panic unsupported Flush favors existing Gin behavior; fail-fast/visible unsupported Flush favors existing Echo behavior. This is policy-dependent compatibility, not a measured human repair-cost win.
- [Corrected original-source native Go CI #39017195968 PASS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39017195968) verifies both original source hashes, that the freeze predates test implementation, Gin native no-Flusher=NO_PANIC, Echo native no-Flusher=PANIC, both supported-Flusher=NO_PANIC. Our old clients and test writers are research-authored, frameworks unmodified.
- **Failed evidence must remain visible:** earlier #39017065840 had GitHub-level SUCCESS even though Echo's historical unrelated upstream tests failed to compile: shell pipeline lacked pipefail. This false PASS was disqualified; we fixed pipefail and used an isolated external client package importing the unchanged Echo production source. Only #39017195968 is the complete paired native result.

## 6. Blind PR-content holdout is an independent, separate gate

Before reading any later PR title/body/diff, the same freeze sealed first 8 GitHub PR IDs in each repository within 2026-08-20..2026-09-30, selected by created-ascending order without future outcome filters:
- gin-gonic/gin: 4811,4812,4813,4814,4815,4816,4817,4819.
- labstack/echo: 3067,3069,3070,3072,3073,3074,3075,3076.

No assumption that these are 16 distinct runtime demands, or that a Gin-specific patch transfers to Echo. After reveal, classify under frozen taxonomy and withhold architecture rank unless the *same executable future demand* can be independently applied to both original sources under the **same research-owned adapter edit grammar** and old contracts. Report coverage separately from conditional accuracy; original earlier P9 2026 unseen PR rank applicability **0/6 remains immutable**.

## 7. Research judgment

**What is proved mathematically:** RC1 conditional repair-cost preservation, RC2 capability-signature lower bound and five SOLID operational implications under explicit source/rights/trace conditions. These are classical structures. **What is tested in real source:** one independently chosen pair of maintained Go frameworks exhibits the frozen demand-policy reversal, while preserving the old tested GET contract. **What remains unproved:** extraction of a fully valid source-to-RC1 quotient across arbitrary projects, real maintainer rights/effort, general SOLID optimality, future PR architecture ranks, or superiority over classical theory.

Next high-value test is bounded source-owner adapter repair for both opposing policies under a frozen identical edit unit, followed by a correctly censored reveal of all 16 PR IDs. No P43 / LAW-R2 promotion.

**P42 RUNNING · R11-P10-P0 BOUNDED · P43 HOLD · LAW-R2 NOT_AUTHORIZED.**


## 8. P10-P2 update — exact matched one-handler repair frontiers (2026-10-17)

[Constructive prerequisite contract 8b570b19](https://github.com/WhoSia/EvoNOMOS/commit/8b570b1964286ef5d7c07e7799eaaa93ef2f6e87) was frozen **after** reading the original source and PR texts, but **before** writing and running the new candidate tests. The independent edit authority in this particular laboratory is narrow and observable: the researcher owns exactly the application-level handler attached to each framework via its *public* router API, **not** the upstream maintained source. A no-edit action has cost 0, replacing a handler has normalized cost 1. This is a bounded, deliberately constructed edit grammar, not real human effort/maintainer reviews.

[Actual Gin old source plus research one-handler repair](../../tools/p42/p2-r11-go/p10_gin_one_handler_repair_test.go): if underlying ResponseWriter exposed by original Gin's Unwrap lacks Flusher, the researcher-owned handler signals unsupported capability; when present it delegates to original Gin Flush; old GET200/old survives. [Actual Echo old source plus research one-handler repair](../../tools/p42/p2-r11-go/p10_echo_one_handler_repair_test.go): the researcher-owned handler unwraps the original Echo response and calls Flush only when the underlying source writer actually supports it; old GET200/old survives.

[Native original pinned GitHub Actions #39017870170 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39017870170), with both source SHA256-equivalent Git blobs verified, strict pipefail, independent Go tests and native logs:
- Gin FAIL-FAST demand: original no-edit Gin failed the demand (NO_PANIC), one research-owned handler edit passes (PANIC on unsupported Flush; supported writer passes).
- Echo GRACEFUL demand: original no-edit Echo failed the demand (PANIC), one research-owned handler edit passes (NO_PANIC on unsupported Flush; supported writer passes).
- Neither original framework source was edited. The required research handler was added as a test-only application adaptation.

Thus **within exactly the two-element normalized action grammar** and the two tested request modes the smallest number of changed application handler units is 1 in each reverse direction; for the other policy the baseline cost is 0. This establishes a **demand-dependent zero-versus-one bounded repair frontier reversal** under research-owned handler rights, **not** universal architecture optimality or empirically measured source ownership/team cost. It does not prove all old clients, HTTP optional methods, concurrency or lifetime behavior are preserved.

## 9. P10-P1 post-seal 16 real PR reveal — negative prospective architecture rank

[Original 16 PR records after IDs were sealed](../../tools/p42/p2-r11/p10_actual_gin_echo_16_PR_precontent_holdout_reveal_and_clustering.json) and [automated exact-ID, clustering, censoring checker](../../tools/p42/p2-r11/p10_precontent_pr_censoring_clustering_audit.py). The genuine 2026-08/09 original PR sample yields:
- 16 distinct PRs, but only **12 runtime/API/resource** PRs after excluding two documentation, one CI, one refactor-only record.
- **Nine clustered runtime/API/resource demands**, not 12 independent proposals: e.g. Gin read-header timeout (#4811/#4812), Gin nil-request PostForm (#4813/#4816), and Echo body-limit reader (#3072/#3073) are paired/related submissions. Selected PR status as at 2026-10-17: **5 MERGED, 5 OPEN, 6 CLOSED_UNMERGED**.
- Real independently exposed new themes include request-body ingestion limit (Gin #4817, Echo #3072/#3073), panic-free form access, router pooled skip-stack lifetime, CSRF config validation, Forwarded header, Go1.27 parameter API. Similar-sounding themes are **not** automatically the same formal client contract across both frameworks. No equal-old-contract, same-demand, identical adapter-rights native rank comparison was pre-frozen for them.
- The original pre-PR-text Gin/Echo predictive grammar froze source-conditioned **Flush policy**, not a transfer forecast for those 9 future demand clusters. Therefore **0 certified matched two-architecture rank predictions on the unseen PR demands**. Accuracy is **NOT ESTIMABLE**; do not convert this to a 0% hit rate. Original P9's **0/6** also remains unchanged.
- [Read-only #39017951228 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39017951228) independently rehashes frozen ID list from commit 35a3c898, ensures post-reveal file did not exist at freeze, checks all 16 IDs, 9 demand clusters, status censoring and 0 rank eligibility.

**Theory disposition:** RC1/RC2 and the five conditional SOLID fragments remain exact classical TCS deductions under their stated hypotheses; the two real maintained Go source families validate one pre-native **source-conditioned** preference reversal and one bounded, post-reveal authored repair-path reversal, but independent genuinely unforeseen source-repair ranking remains unsolved. This is meaningful experimental structure but **NOT a new general software design law**. Next attack must preregister a common portable demand grammar and its exact client/rights semantics *before* opening another cohort; equal-information source-aware classical rivals should score the same baseline.

**P42 RUNNING · R11-P10-P2 BOUNDED (NO LAW PROMOTION) · P43 HOLD · LAW-R2 NOT_AUTHORIZED.**
