# EvoNOMOS P42 R11-P9-Q — Original Chi #1095: Optional-Capability Erasure and Conditional Source Repair

Date: 2026-10-17. P42 RUNNING; P43 HOLD; LAW-R2 NOT_AUTHORIZED. This is a P9-Q bounded supplement, not an R11-P10 opening.

## Why this is an EvoNOMOS structural-design question

The question is not whether a middleware patch fixes one header. It is whether a source edit can meet a new client demand while retaining existing clients' observable capabilities. Observational equivalence with respect to HTTP status and body need not preserve Go optional interface observations. The source edit must be indexed by old and new clients, not accepted on single-contract success.

### Actual third-party source; exact frozen identities

- Upstream: go-chi/chi PR #1095, https://github.com/go-chi/chi/pull/1095 ; contributor-proposed fix for 405 Allow to advertise implicit HEAD support under GetHead.
- Baseline commit f975af0cb10cbefaccf0422385420fe62722d648; middleware/get_head.go Git blob d4606d8be6db20534136b1dcdafaae3b361c23a7.
- Actual contributor proposal commit 9c6e3a8414e8968222cda63aa3297703d5c5f37a; the same file's Git blob 55edec16dfa0abb630772d60c3e3b3da804aa5f6.
- The proposal wraps next.ServeHTTP in getHeadAllowWriter for both HEAD and non-HEAD requests. That wrapper embeds http.ResponseWriter and directly implements WriteHeader/Write, but does not forward Flush. This is a source-level hypothesis subsequently verified by original Go.
- At the time inspected, the proposal was OPEN/UNMERGED. Neither successful source execution nor this analysis asserts upstream acceptance, reviewer intent, or ownership rights.

## Phase I: source-inspection-conditioned independent native experiment

Hypotheses frozen before *new native Go execution*: [668ed4ff](https://github.com/WhoSia/EvoNOMOS/commit/668ed4ff2f9c9c430f477093bd115abe1c8b8fb3). Exact inputs are not blind future PRs because the proposal source and its text had already been read. [Same independent native test](../../tools/p42/p2-r11-go/r11_p9q_chi1095_optional_capability_test.go), [read-only original-source workflow](../../.github/workflows/g8-p42-r11-p9q-chi1095-optional-capability.yml).

[GitHub Actions #39014842576 — SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39014842576), source-tested HEAD 3d64fc4276c9195f0cbd63c4c02a416ce6040418; artifact 12093919387 sha256:ac0a40b0f62779c68320d9dfd8a8d518118a549841fac0fb3f37c7b14b9c422f.

| Observable contract on actual Go | Baseline source | Contributor proposal |
|---|---|---|
| GET status 200, response body preserved | PASS | PASS |
| GET handler receives optional http.Flusher from recorder | TRUE | FALSE |
| POST against GET-only route gives 405 | PASS | PASS |
| POST 405 Allow advertises HEAD in addition to GET | FALSE (Allow GET) | TRUE (Allow GET,HEAD) |

In the actual native log: original GET200, old_flusher=true, POST405 Allow="GET"; contributor GET200, old_flusher=false, POST405 Allow="GET,HEAD". The research test's old client checks a real Go stdlib optional interface, but is itself research-authored. No claim is made that any specific production Chi application was affected.

## Phase II: research-authored constructive source-repair candidate

[Pre-candidate source-edit freeze 3118d233](https://github.com/WhoSia/EvoNOMOS/commit/3118d233782eb27afb81d5bc67782568acb2c342) precedes the authored [source-edit generator](../../tools/p42/p2-r11-go/r11_p9q_chi1095_construct_conditional_flusher.py), [positive/negative native test](../../tools/p42/p2-r11-go/r11_p9q_chi1095_constructive_repair_test.go) and [read-only workflow](../../.github/workflows/g8-p42-r11-p9q-chi1095-constructive-flusher.yml). The generator first asserts the contributor source text contains exactly two expected wrapper call sites, then constructs a candidate inside an isolated pinned checkout; this is NOT a contributed or merged upstream patch.

The candidate selects one of two concrete wrapper method sets:

1. When the underlying writer exposes http.Flusher, select a forwarding implementation exposing Flusher and retaining the proposal's 405 Allow override.
2. When the underlying writer does not expose Flusher, select the original non-Flusher core wrapper; do not invent the capability.

[Native GitHub Actions #39015053911 — SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39015053911); artifact 12094288454 sha256:65b47dbd0c111f4dbaca2dcbaa162399f0e35a33b9066ee517bb73944efa4f64.

| Research-only repair input | GET client observes Flusher | GET200 + old body | POST405 Allow |
|---|---|---|---|
| Native httptest.ResponseRecorder with Flusher | TRUE (preserved) | PASS | GET,HEAD |
| Interface-only wrapper without Flusher over same recorder | FALSE (preserved) | PASS | GET,HEAD |

Both independent subtests passed in original contributor Go source plus research candidate, at exact pinned source commit and tested GitHub HEAD b392d95051ebc56c10af3587165c0df745a2b838.

## Exact classical mathematical boundary

Let C(w) be the Boolean old-client observation of a direct Go type assertion w.(http.Flusher). Assume admissible underlying ResponseWriters include both C=0 and C=1. For a *fixed dynamic concrete wrapper type* T independent of input w, the truth of the assertion on T is constant, because it depends on T's method set, not the wrapped instance. Thus the mapping C(wrapped(w))=C(w) cannot hold for both admissible inputs if all wrapped values have type T.

Consequently, under direct optional-method-set observation, at least two distinguishable dynamic method-set forms are necessary, and our constructed conditional source edit suffices *for this one optional capability*. More generally, with k fully independent detectable optional interfaces and every 2^k capability pattern realized, exact preservation requires at least 2^k distinguishable observable method-set patterns. This is a classical elementary counting / Go interface-semantics observation, NOT a novel mathematics theorem, nor a lower bound on code lines, distinct source definitions or cost for other observation models.

Caveats: Clients that use http.NewResponseController with an Unwrap-capable wrapper observe a different contract. Similarly, Hijacker, ReaderFrom, Pusher, Controller.FlushError semantics, concurrent access, and all streaming timing/effects were NOT tested or preserved by this one-feature candidate. The two-phase tests do not prove full contextual refinement. In particular, do not label the research candidate globally safe or optimal.

## Scientific judgment and next discriminatory question

This is a real maintained-source witness that local source repair can improve a target protocol observation while reducing old-client *type-mediated capabilities*, and a narrow constructive repair that avoids this precise tradeoff. It is explained by classical Go interface method sets, contextual equivalence/refinement, and source-aware programming. No classic rival was defeated.

The scientific successor should stop rewarding mere code/test counts. Freeze a typed client/authority/behavior vocabulary *before future unknown demand*, compare source-level repair-option frontiers of actual competing architectures using identical rights and information, and measure coverage and legitimate abstention separately from accuracy. The original P9 source-rank **0/6** remains an immutable failure on the genuinely unseen 2026 demand cohort; treating Chi #1095 as a new blind-hit would be leakage. This case instead justifies extending the *future* grammar with optional capability effects, not retrospectively reclassifying the original sample.

**P42 RUNNING · P43 HOLD · LAW-R2 NOT_AUTHORIZED · R11-P10 NOT OPENED.**
