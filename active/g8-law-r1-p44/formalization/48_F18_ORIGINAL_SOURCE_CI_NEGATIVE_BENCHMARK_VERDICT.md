# EvoNOMOS P44 F18 — original source CI, bounded transport, and negative classical benchmark verdict

Verified 2026-11-05. **CONSERVATIVE TOKEN-IDENTITY CERTIFICATE PASS / CLASSICAL TOKEN CACHE FASTER IN ONE CONTROLLED MICROBENCHMARK / REAL CHANGED-SOURCE TRANSPORT UNPROVEN / LAW-R2 HOLD.**

## Original verified receipts — keep failures

1. Initial F18 [original CI #41987593516](https://github.com/WhoSia/EvoNOMOS/actions/runs/41987593516), exact commit `493666dc0a4e068ca1a30d4a341b8c66933d2009`, **FAILED** during `TestTransportExactWhitespaceVariationAndClassicalBaseline`: a whitespace-only revision was judged INVALIDATED. Root cause: source-location-sensitive AST formatting in the initially selected digesting procedure. This is a concrete failed reuse test and was retained.
2. Corrective independent commit `aa8bc64d080af3c17527334452c4d5798041ab09` changed digest semantics to parser-validated, comment-free **Go lexical token sequence** (including semicolon-insertion tokens, excluding whitespace). A token match under frozen one-file build context supports reusing earlier typed source facts, conditionally on the separately authenticated original certificate issuance. It does not prove alpha-equivalence or arbitrary transformed-source equivalence.
3. [CI #41987907647](https://github.com/WhoSia/EvoNOMOS/actions/runs/41987907647), commit `c44e052838be07e61622a373b1d76077e4dfa62e`, **FAILED after all Go tests passed**: GitHub workflow benchmark test filter was written with a malformed quoted shell regular expression, so the benchmark invocation did not execute. Separate correction commit `fa7817e137837392848201f372ae5fcbfb1b1a54` uses a literal negative test name without shell-special dollar expansion. Keep this CI failure in chronology.
4. **FINAL ORIGINAL [CI #41988168928 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/41988168928)**, exact tested commit `fa7817e137837392848201f372ae5fcbfb1b1a54`, original job `127113775140`, Go 1.23.2 Linux amd64. Verified actual run conclusion, job and raw logs. All eleven existing F17+new F18 tests PASS, `go vet` PASS, Go race PASS, four F18 benchmark methods each at exactly 200 iterations PASS. Earlier concurrently cancelled workflow dispatches are not failed test verdicts.

## Original raw test controls

- `CERT_TRANSPORT shared=true/false formatting_only_reuse=true classical_full_reanalysis_agrees=true`.
- `CERT_INVALIDATION shared_to_disjoint=true full_classical_reanalysis_needed=true`.
- `CERT_TAMPER trusted_evidence_seal_rejects_mutated_source_facts=true`.
- `CERT_CONSERVATIVE_FALSE_INVALIDATION identifier_rename_not_reusable=true`.
- Malformed source or unsupported build directives return UNKNOWN; they are not declared SAFE.
- Earlier F17 native source patch execution and seven forbidden-source-shape controls still PASS.

## Direct original numerical benchmark receipt

**Single GitHub-hosted machine, one run, 200 repetitions per method, tiny closed Go source file, Go 1.23.2.** These numbers are descriptive, not a statistical estimate of production performance.

| Condition | ns/op | B/op | allocs/op |
|---|---:|---:|---:|
| Conventional exact Go token cache | 19,092 | 7,280 | 195 |
| F18 receipt-sealed certificate verification | 24,086 | 7,601 | 199 |
| Conventional full typechecked source alias reanalysis | 45,510 | 15,140 | 280 |
| Initial F18 certificate issuance | 55,865 | 22,744 | 479 |

F18 verification cost is about `24086/19092 = 1.262` times conventional exact token caching cost in this run and about `24086/45510 = 0.529` of full-source reanalysis cost. An observed reduction relative to full reanalysis is ALREADY PROVIDED by classical caching and cannot be claimed as uniquely EvoNOMOS. F18 issuance time must be included in any amortized comparison; no realistic invalidation frequency or production workload sampled. A simple classical exact-token cache performs the same invalidation logic with fewer bytes and allocations in this one trial.

## What the certificate *actually* certifies

Source `s` was previously parsed and typechecked by the F17 strict single-file no-side-effect grammar. The issued certificate stores a digest of its **Go lexical token stream** and source-derived alias/post-write facts. A trusted external source must pin the exact certificate `evidenceDigest`. `Verify(s',cert,pinnedSeal)` ensures externally pinned fields have not changed, parser rejects syntax/comments, then compares the Go token-stream digest. If identical, typed-source facts from s apply to s' in the same build context, assuming hash collision resistance and trust in lexer/parser/typechecker and original issuance.

**A hash stored beside a forged certificate is not authentication.** The code does not verify a cryptographic signature or retrieve independently anchored GitHub/Notion provenance. Actual trusted seal authority is an EXTERNAL premise. The test only demonstrates that a changed certificate is rejected if the supplied trusted seal remains pinned.

Only whitespace-only revisions reuse facts. Even a harmless identifier rename fails conservative cache identity and is correctly **INVALIDATED**, not auto-reproved equivalent. A source change to alias semantics invalidates, as it must. This is not compositional Adapton-like recomputation nor bi-abductive source footprint transport across materially edited code.

## External original literature and Harvest challenge

- Hammer et al. 2014 ADAPTON and Hammer et al. 2015 Incremental Computation with Names already establish demanding baseline ideas about dependency-driven reuse and from-scratch consistency.
- Diemert et al. 2023 incremental assurance distinguishes later evidence strengthening/weakening a safety argument.
- Calcagno et al. 2009 compositional bi-abduction infers frames and anti-frames; much stronger than a full-file token hash.
- Research OS P33 Harvest F01/F03/F05/F06 establishes information-cut and minimum-support cautions. Harvest is non-sovereign; independent primary paper/Go-source verification still mandatory.

Original source and Harvest reading ledger: [46_F18_DRIVE_ORIGINAL_AND_HARVEST_BACKFLOW_AUDIT.md](46_F18_DRIVE_ORIGINAL_AND_HARVEST_BACKFLOW_AUDIT.md). Proof scope and original skeptical null: [47_F18_CERTIFICATE_TRANSPORT_SOUNDNESS_AND_EXPECTED_NULL.md](47_F18_CERTIFICATE_TRANSPORT_SOUNDNESS_AND_EXPECTED_NULL.md). Previous pre-execution protocol was committed before implementation: [45_F18_PROSPECTIVE_CERTIFICATE_TRANSPORT_PREEXECUTION.md](45_F18_PROSPECTIVE_CERTIFICATE_TRANSPORT_PREEXECUTION.md).

## Scientific director decision

F18 achieves a correctly functioning conservative original-source token cache with a conditional integrity receipt, but not a new source certification capability beyond classical caching. For this bounded benchmark, the strong conventional cached baseline is faster than the F18 certificate verifier. **F18: BOUNDED PASS / CLASSICAL BASELINE ADVANTAGE / NOVELTY NEGATIVE / LAW-R2 HOLD.**

The necessary next discriminating question is whether one can attach a small **dependency-/footprint-scoped** independently checked proof that survives changes OUTSIDE the dependent code while correctly invalidating changes inside it, at lower total issuance + maintenance + verification cost than classical incremental computation/bi-abduction. This must use independently sealed changed-source revisions, strong rival exact source analysis, and actual source/rights/observer identity. If both methods tie, do not rename classical reuse as a structural law. General G1–G7 remains OPEN.
