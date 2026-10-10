# P40-MATH-B-P5 — Real-Maintenance Source Evolution & Proof-Carrying Boundary Abstractions: Issue-Derived Prospective Edits, Semantic Simulation, Axiom Minimality & Independent Classical Falsification

**EvoNOMOS Generation VIII / LAW-R1-P40 · 2026-10-10 KST · bounded court · P40 OPEN · new mathematical law HOLD · LAW-R2 NOT_AUTHORIZED.**

## 0. Precise outcome and evidentiary scope

Three actual upstream open GitHub issues were read as *requirements* for new pinned-source probes: Echo #2895 (automatic HEAD), Echo #2619 (mid-segment wildcard ambiguity originally reported on v4.11.4), and Gin #4641 (AIP-136 literal-colon verbs and dynamic parameter suffixes). Eight distinct cases were registered before writing any P5 native Go test; six had a fixed forecast and two explicitly ABSTAINed. On original pinned source, **6/6 fixed forecasts matched and both abstentions yielded logged, non-scored observations**.

This is *issue-derived prospective execution*, NOT a blind holdout of upstream issue resolutions. Reporters had already described some historically observed behavior, the future test family was selected after reading those reports and fixed source structure, and feature availability in a newer pinned revision need not match an open issue's requested historical behavior. Never present 6/6 as independent real-world generalization accuracy.

Original external repositories were never mutated. The Go AST is parsed mechanically to attest eight named source-function anchors, but the contract and cases were researcher-selected; no whole-language source analysis or extracted Go→Lean simulation proof was certified.

## 1. Frozen first, observed later

- [Pre-registered issue-derived forecast contract](../../tools/p40-math-b-p5/issue_derived_prereg.json) at **Git commit ff1aad4f62809717e3f87a67b5085251b01c91ae**. Exactly eight cases: three Echo HEAD forecasts, two Gin colon forecasts plus static control, and two labelled ABSTAIN, one Echo wildcard one Gin parameter+verb suffix.
- [Go AST source anchor extractor](../../tools/p40-math-b-p5/issue_source_extract.go) parses original echo/router.go, echo/echo.go and gin/tree.go, records source-function line and AST-body SHA-256, confirms HEAD auto/default method resolution and literal-colon/wildcard parser references.
- [Pretest source-AST Actions #38051884912 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38051884912), checked HEAD e3ad61281adca8d6d767171e68419122289de906, artifact 11669169616 digest **sha256:761986ba8b365599ffbd4f9410e6d8ab59c8d44f7f0b9a719fed24912a5a3d82**.
- Native heldout Actions require (a) ancestry from the locked git commit, (b) byte-for-byte equality of registered predictions, (c) absence of P5 native tests at that earlier commit and (d) the exact original upstream Git SHA.
- First native run #38052018937 failed before Gin execution due Go module checksum setup; this was repaired with **go test -mod=mod**, a local *harness dependency-resolution change*. The frozen predictions and original upstream sources were not edited.

## 2. Issue sources, revisions and prospective source edits

| Target | Upstream evidence | Pinned original upstream SHA | Caution |
| --- | --- | --- | --- |
| labstack/echo #2895 | https://github.com/labstack/echo/issues/2895 — open feature request for automatic HEAD from GET | 3882266a3641a36fc2111b48cd597adab1c1ecea | Existing pinned v5 has an AutoHandleHEAD config; open issue alone does NOT imply absent functionality |
| labstack/echo #2619 | https://github.com/labstack/echo/issues/2619 — open complaint about wildcard path absorption, reported v4.11.4 | same pinned v5 | v4 report → v5 transfer was *ABSTAIN*, not a forced forecast |
| gin-gonic/gin #4641 | https://github.com/gin-gonic/gin/issues/4641 — open request for AIP-136 colon verbs | 0f09c3a9b4626d9fe9979cf4d0521d6ae32ab646 | static escaped colons and post-param suffixes must be treated separately |

## 3. Native Go prospective test outcomes

| Locked ID | Pretest commitment | Actual pinned-native verdict |
| --- | --- | --- |
| E-HEAD-DEFAULT | HEAD_405 | HEAD without automatic fallback returned HTTP 405; GET control worked. CONFIRMED |
| E-HEAD-OPTIN | HEAD_200_EMPTY_GET_EXECUTES | Opt-in HEAD returned HTTP 200 with empty body, GET-specific response header and GET handler incremented invocation count. CONFIRMED |
| E-HEAD-EXPLICIT | EXPLICIT_HEAD_PRIORITY | Explicit HEAD method handler selected rather than automatic GET fallback; GET handler not invoked. CONFIRMED |
| G-VERB-BARE | SECOND_REGISTRATION_PANICS | Unescaped colon routes collided when second wildcard name registered. CONFIRMED |
| G-VERB-ESCAPED | BOTH_REGISTER_AND_SERVE | Escaped literal-colon routes both registered and returned separate successful POST responses. CONFIRMED |
| G-STATIC-CONTROL | BOTH_REGISTER_AND_SERVE | Two unrelated static POST endpoints registered and served independently. CONFIRMED |
| E-WILD-TRANSFER | ABSTAIN | Both routes registered; GET /v2/foo/bar/tags/list returned **UPLOADS** from the /v2/*/blobs/uploads/:ref route (unexpected handler selection). NON-SCORED |
| G-VERB-PARAM-SUFFIX | ABSTAIN | Gin rejected /issue/customers/:customer_id\\:mutate because it contained invalid wildcard syntax in one segment; POST /issue/customers/123:mutate returned 404. NON-SCORED |

[Native Go original-source Actions #38052099200 SUCCESS, 2/2 jobs](https://github.com/WhoSia/EvoNOMOS/actions/runs/38052099200) on exact tested HEAD f515aa31033d1b226a12913ab0b575a282386fae. Independently machine-audited Go logs against frozen case IDs in [issue_certificate_court.py](../../tools/p40-math-b-p5/issue_certificate_court.py), [Actions #38052305081 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38052305081), checked HEAD 6190396c409d4aa3778de45ddf7b016b0fa143cf, Echo artifact 11669846343 digest sha256:25cc153386c3c51173bad5433edb9b9d8967d4556b537b6862f662299991506a; Gin artifact 11669921395 digest sha256:5389c3e3e2ee8a79f95e9d9ab69b186696ed74c5dc7cd1cede8c7a839ad53f8c.

**Important independent post-hoc checks, NOT preregistered forecasts:** after the Echo wildcard abstention showed misrouting, the same behavior was reproduced as a separate regression test; a second exploratory test confirmed two HEAD variants with *identical HTTP 200 status and empty body* but **different GET-handler side effect counts**. This independently passed [native Actions #38052437653](https://github.com/WhoSia/EvoNOMOS/actions/runs/38052437653), tested HEAD 9a721ec5a6c0d993869fab0f161e92d98558a437. Echo artifact 11670735005 sha256:2024b174e2c6ccf3912ebe50f71d0cd20406d951f8019a99c6720f29d8007268; Gin artifact 11670405415 sha256:4b579780271a50b080bbc4218c8cbedbc3cefc8fe4ffa1cea8429eab3e3ac2cf.

## 4. Noncircular source-boundary / observation obligations

These are *separate source semantics duties*, NOT yet a minimal basis of all OO axioms:

- **Registration grammar:** checked directly from native source; Gin bare versus escaped literal colon shows client URLs alone do not determine whether source registration is even possible.
- **Routing identity:** Echo #2619 reproduction shows permitted registration does not imply the request is dispatched to the intended named route. A source-admitted edit can fail a route-identity client contract.
- **HEAD resolution:** Echo method lookup prioritizes explicit HEAD, then conditionally GET as fallback if AutoHandleHEAD; default disabled behavior differs. Feature flag + explicit override are independently relevant guards for this bounded operation.
- **Side-effect frame:** HEAD status/body alone are insufficient to infer whether the GET handler executed. Native tests report equal observable status/body but distinct execution counts. Full side-effect-sensitive observation must be explicit, rather than inferred from HTTP response body alone.
- **Historical authority:** no source evidence was collected concerning external maintainers' actual permissions or approval. The Math-B history/owner-rights hypothesis remains synthetic until authoritative provenance is independently observed.

These establish source-realizable **pairwise nonentailment in chosen bounded settings**, not mutual independence of the six Math-B A–F axiom families. A claim of a full independent OO axiom basis would still require formally noncircular premises, one countermodel per omitted premise and a proved target implication that loses soundness when that premise is omitted.

## 5. Lean semantic simulation / proof-carrying boundary limits

[Lean formal source](../../tools/p40-math-b/lean/P40IssueSimulation.lean) defines a tiny deterministic HEAD operation state with explicit HEAD flag, GET handler existence, AutoHandleHEAD flag, GET invocation count and a hidden revision. The abstraction retains precisely the first four semantically relevant fields (compressing the two GET fallback guards into one) and erases the revision.

Within this explicitly restricted model, the declaration proves a dispatch correspondence, one-step commuting abstraction, a **finite-step simulation induction**, explicit-priority and fallback witness lemmas, and irrelevant-revision invariance. The augmented version also proves a classical non-factorization theorem: the projection onto status + empty HEAD body alone cannot decide whether the GET handler was executed. **A successful Lean source proof does not alone certify that Echo's full Go implementation refines this model.** AST anchors plus native tests corroborate the scoped matching examples, but a source-level transition interpretation theorem remains missing.

Earlier known-good proof compilation [Lean #38052171166 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38052171166) checked HEAD c227f94a5d859d492a60cbbd8786f8a37f5af1cd, artifact 11670126302 sha256:7c0e2214a47fb9f9da26758f749ede7e4b2ef2a1dec1e2cec1c320e76a1afd3d. The **latest augmented Lean 4.34.1 model** including the status/body-only nonfactorization theorem is now **INDEPENDENT KERNEL CHECK SUCCESS**: [Actions #38052415494](https://github.com/WhoSia/EvoNOMOS/actions/runs/38052415494), exact checked Lean source HEAD 44138216d34649240cb5762f95f550608e075c94, artifact 11670226133 digest sha256:54382ddcb91ef5bf114244ea5494c7512ce01651d078da59678e51e26c2dbc56. No sorry/axiom/admit is permitted. The Lean proof certifies only the declared restricted HEAD transition model; no verified interpretation of all Echo Go instructions has been constructed.

## 6. Independent classical theory competition and priority verdict

Source-oblivious model assumes HEAD and GET remain separated unless an explicit HEAD route is defined, and treats static-colon route segments as ordinary literals: it agrees with 4 of the 6 locked targets. An ordinary source-aware guarded dispatch/parser/CSP model using the precise pinned Echo method resolution and Gin trie-escape constraints explains all 6. [Classical reduction source](../../tools/p40-math-b-p5/p5_classical_reduction.py), [Actions #38052376071 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38052376071), artifact 11670006357 sha256:f49946733ae0ca220aece3e0d8971820b48d2a374731ef270fddaa6af13cbfb2.

| Classical competitor | Correspondence to frozen native verdicts |
| --- | --- |
| HTTP method + literal path-only heuristic | 4/6 |
| Source-aware classical CSP and guarded transitions | **6/6** |

**The stronger classical competitor survives.** The full source-aware prediction is a manually instantiated standard guarded transition/CSP account with implementation-specific source predicates, not a new mathematics of software repair. Separation logic's frame rule, data refinement, rely/guarantee and Liskov–Wing behavioral subtyping are not falsified by these cases.

## 7. Legitimate publication boundaries / next attack

1. Collect NEW issue/PR revisions before merging/fixing them, with held-out independent maintainer outcomes, multiple source versions, and representative error classes. Here pretest forecasts preceded *our* experiments but not public historical issue discussion.
2. Produce an executable Go AST + alias + routing constraint extractor whose **semantics-preserving relation to selected Go instructions** is checked by Lean or another trusted proof system, not only syntactic anchors.
3. Preregister competing CSP/frame and any proposed new source-math candidate using exactly the SAME source information, not advantaged retrospective data.
4. Build minimal source-realizable countermodels for typing, client behavior, authority, invariants, boundary, dependencies. Distinguish observed maintainer rights from invented laboratory flags; do not claim complete original SOLID derivation.

**Verdict: P40-MATH-B-P5 bounded issue-derived original-source court PASS (6/6 commitments + 2 honest abstentions). Bounded source-to-abstract simulation is classically proof-checkable; full Go simulation unproved. Historical SOLID axiomatic independence UNPROVED. Classical CSP/SL competitors SURVIVE. P40 OPEN; LAW-R2 NOT_AUTHORIZED; no universal new OO law.**
