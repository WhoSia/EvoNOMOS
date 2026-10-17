# EvoNOMOS G8 LAW-R1-P42 — R11-P10-P4: Source-Evidence Abstraction, Equal-Information Classical Rival, and Unseen PR Failure

**2026-10-17. Status: P42 RUNNING · R11-P10-P4 / P4Q bounded verification · P43 HOLD · LAW-R2 NOT_AUTHORIZED.**

## 1. Research question and fixed epistemic gates

Can an abstraction of authentic maintained source *certify enough information* to compare authorized future repair frontiers before knowing a demand, and, after receiving identical observations, outperform the strongest classical cost-labelled transition-system explanation? The underlying problem is demand-conditioned repair possibility, not proving SOLID axioms true or accumulating CI receipts.

**R11-P10-P4 source/heldout protocol was sealed [f2c66378](https://github.com/WhoSia/EvoNOMOS/commit/f2c663787d13c55dfcdbbdf3934de6a8d0426d2b) before writing the extractor/test and before opening selected Chi/Mux PR titles, descriptions or diffs.** Previous original Gin/Echo snapshots and client tests were already known; this is a **source-conditioned**, not blind-source discovery. The new PRs themselves existed before freeze. An earlier P9 study had seen related Chi/Gorilla *issue themes*; some revealed selected PRs are therefore not independent unforeseen problem types, and this is explicitly flagged below.

A mere method signature, a GitHub PR status, a passing CI, or a source file under GitHub is not evidence of complete runtime effects, actual maintainer edit authority, or human effort. Those are separate, potentially UNKNOWN fields.

## 2. Real source AST extractor: what is certified and what is not

[Go standard-library AST extractor](../../tools/p42/p2-r11-go/p10_p4_pinned_wrapper_ast_extractor.go) reads these exact pinned original source bytes:

- Gin d3ffc9985281dcf4d3bef604cce4e662b1a327a6, response_writer.go Git blob 9035e6f1fd794d54063d6f50c3490e64d35a3647. The concrete wrapper declares Flush and Unwrap; inside Flush AST is an optional type assertion to http.Flusher; no panic or ResponseController call there.
- Echo 86d0223c7aa39b865a9452de3479897fcb5a3939, response.go Git blob 4da729c4786898ddb2dc361c19a303e55d149540. Its wrapper declares Flush and Unwrap; the Flush AST calls http.NewResponseController and includes panic; it does not perform a direct http.Flusher type assertion in that method.

The extractor parses authentic Go AST and records receiver-specific declared methods, relevant syntax AST node presence, the source-file SHA-256, pinned Git identity, and explicit **UNKNOWN** for runtime semantics, upstream source-edit authority, complete type-system proof and human cost. AST syntax alone proves neither all-source behavior nor complete Go method-set compatibility. We test separately through the unmodified original framework sources under research-owned old clients and adapter edits.

[Original pinned Go and fair-rival workflow #39019143681 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39019143681), read-only, strict pipefail, pre-native freeze SHA check, two original source Git blob checks, source extraction, actual original and candidate adapter tests for Gin and Echo.

## 3. Equal-information classical rival — genuine comparison result is TIE

[HARC_RC and CLASSICAL_CTLS scorer](../../tools/p42/p2-r11/p10_p4_equal_information_harc_classical.py) receives exactly the same AST evidence, the same native original and research-owned one-handler Go observations, the same tiny permitted edit grammar, and the same synthetic cost vector (one changed app handler, one review-unit placeholder). HARC_RC uses a two-state finite repair quotient; CLASSICAL_CTLS separately enumerates the explicit cost-labelled edit graph. Both report **ABSTAIN** when rights or native observations are not established.

Four source × declared client-policy cases (Gin/Echo × graceful/fail-fast unsupported Flush), all originally source-conditioned, agree:

- Gin already supports graceful no-Flusher policy for 0 handler changes; a research-owned handler can enforce fail-fast with 1 normalized change.
- Echo already supports fail-fast no-Flusher policy with 0 changes; a research-owned handler can enforce graceful continuation with 1 normalized change.
- Both actual original sources preserved the research-authored old GET 200/old contract under those runs; this is NOT proof of every production old client.

**Result: 4/4 classical equal-information ties, HARC unique wins 0, classical unique wins 0.** This is the expected classical explanation, not validation of independent novel mathematical priority, full source bisimulation or real repair labor.

## 4. Sixteen truly unread PR IDs — honest negative prospective court

[Pre-text frozen cohort](../../tools/p42/p2-r11/frozen_p10_p4_source_ast_equal_information_rival_and_unread_prs.json) locked first eight created-ascending 2026-09-15 through 2026-10-10 PR IDs (unfiltered by future state):

- go-chi/chi: #1180, #1181, #1182, #1183, #1184, #1185, #1186, #1187.
- gorilla/mux: #813, #814, #815, #816, #817, #818, #819, #820.

[Complete descriptive postseal reveal](../../tools/p42/p2-r11/p10_p4_actual_chi_mux_16_unread_pr_reveal_and_eligibility.json), [strict ID, status, leakage and duplicate checker](../../tools/p42/p2-r11/p10_p4_actual_pr_sealed_eligibility_court.py), [GitHub Actions #39019427118 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39019427118): 16 PR IDs, **15 demand clusters** (Mux #818/#820 address a related semicolon delimiter issue), 11 OPEN, 4 CLOSED_UNMERGED, 1 MERGED at study observation time. **Five PRs** (#1181 Chi, #815/#816/#818/#820 Gorilla) concern previously studied issue themes, so the cohort cannot honestly be scored as sixteen independent genuinely new ideas. Labels for demand types were assigned AFTER reveal, not predictions.

The preregistered rank grammar demanded a *fully identical client contract on BOTH frozen Gin and Echo producer sources*, with the same authorized research-owned handler edit grammar and actual native comparison. **Zero of these PRs met that certification contract. Both HARC_RC and CLASSICAL_CTLS ABSTAIN on the new PR architecture rankings.** Selective accuracy is UNDEFINED, not 0%. Chi #1185 uses the word Flush, but requires specific Discard transport-effect semantics absent from the previously verified Gin/Echo handler grammar; keyword overlap is not semantics/ownership equivalence. Earlier P9 true unseen source-rank coverage 0/6 also remains unchanged.

## 5. P4Q — genuine upstream merged Chi #1185 exposes an effect that interface signatures hide

After the PR reveal, a **distinct post-content-read hypothesis** was sealed at [516f4efe](https://github.com/WhoSia/EvoNOMOS/commit/516f4efeb0393c98ce20399bc15fc90606b8bc3b) BEFORE writing new Go tests. Third-party actual source identities:

- Original pre-PR Chi b1c9ab47626cc46b34393ad4d35779c4363c4e1e, middleware/wrap_writer.go Git blob 6c2b5d59bf8ed78e6c595856d3ef114253fa7ad2.
- Actual merged contributor source from Chi [PR #1185](https://github.com/go-chi/chi/pull/1185), commit 9b3e51c349f3fa6cf120ae786a2835e89e81da2e, Git blob 2fdd9c44e3d3b98ebbead5b9e0287ea855efc163. Its original review/merge status is not a license for researcher to edit upstream.

[Research-owned single original-source Go fixture](../../tools/p42/p2-r11-go/p10_p4q_chi1185_discard_flush_effect_test.go) compiled unchanged source at both commits. [Native Go CI #39019598571 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/39019598571) confirmed, on both direct Flush and http.ResponseController.Flush:
- Both expose the same tested Go concrete outer type flushWriter and http.Flusher capability.
- Both report wrapper Status=200, BytesWritten=0, HTTP body bytes=0 for the selected client context.
- Without Discard, both pass Flush to the underlying ResponseRecorder.
- With Discard, **original** passes underlying Flush, but the actual **merged source** suppresses it.

Thus if projection q records only tested outer type, method set, Discard state, invocation method and those HTTP outputs **but not source-dependent effect policy**, the two source states have equal q yet different transport Flush events. There is no deterministic map from that q to the specified transport effect for this pair: a standard nonfactorization counterexample. Classical effect traces/contextual refinement explain the witness. This does not establish a source-agnostic new SOLID design law.

[Real-log proof extractor](../../tools/p42/p2-r11/p10_p4q_original_chi_effect_nonfactorization_proof.py) additionally enumerates all 2^6 subsets of candidate source-observable features across eight tested real-Go source/state/invocation worlds. Among those specific features, **(revision, Discard)** is the uniquely minimal set sufficient to predict transport Flush. This is a bounded empirical feature sufficiency fact and elementary finite partition argument, not a proof of global minimal software abstractions.

## 6. Formal consequence for SOLID and stronger-than-SOLID claims

Previous HARC R11-P5 derived five **conditional operational fragments** of SRP/OCP/LSP/ISP/DIP under independently discharged observation completeness, noninterference, authorization and versioned source-port assumptions. This stage illustrates what those premises really cost:

- For ISP, a small interface cannot be assumed complete merely because both providers implement Flusher: the client may legitimately observe transport effects conditional on Discard.
- For OCP/DIP, declaring a stable port does not prove that a wrapper edit preserves the old **effect trace**; a core-closed authorized extension path needs an effect-complete certificate.
- For LSP, same Go method set does not imply contextual substitution under a Discard-and-Flush client.
- For SRP, determining whether event ownership belongs to response writer or buffering layer is a source/resource separation obligation, not something derived from source code class names.

The genuine unsolved step is automatically producing a **sound source-to-HARC simulation** including edit rights, effectful dependency paths, resource lifetime, and independently chosen protected client contracts. AST facts plus finite named Go runs do not yet discharge it. A strong **equal-information classical event LTS** predicts all cases once supplied these exact effects; no claimed HARC superiority.

Scientific next gate: automatically source-certify a selected finite effect/authority interface cut; prefreeze *semantically matched* new demand and old-client test for actual independently maintained providers BEFORE disclosing future PRs; score HARC against a classical model using identical evidence. If sound extraction or matched cohort eligibility fails, report UNKNOWN/ABSTAIN and fix source extraction, not the metric.

**P42 RUNNING · P4/P4Q BOUNDED · P43 HOLD · LAW-R2 NOT_AUTHORIZED.**
