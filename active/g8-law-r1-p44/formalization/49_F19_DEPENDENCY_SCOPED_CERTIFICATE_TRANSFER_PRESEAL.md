# P44 F19 — prospective dependency-scoped source certificate transport preseal

SEALED RESEARCH PROTOCOL dated 2026-11-05. **No F19 source experiment has been executed and no performance/new-law result is claimed.** This document follows verified F18 negative result and must precede F19 candidate test implementation.

## Research question and precommitted skeptical rival

F18 transported source facts only across identical Go lexical token sequences. It did not reuse a proof across changed source semantics or identifier-renamed code, and the conventional exact-token cache was faster in one tiny original CI benchmark. Existing Hammer et al. ADAPTON/Nominal ADAPTON and Calcagno et al. bi-abduction already demonstrate incremental dependency reuse and modular footprint reasoning, so matching them is not novel.

F19 question: Can a small independently checked **source-footprint certificate** for client relation C survive code revisions that change only a PROVED non-dependent source region, without source-unsafe acceptance, with lower total issuance + verification + invalidation/reanalysis cost than a well-engineered conventional dependency cache/points-to + bi-abduction analyzer?

**Null comparator:** classical exact source dependency analysis and its cached dependency graph on identical revision history and information; use identical Go AST/typechecker/front-end and trusted repo/build context. The winner is judged on total computational work, bytes, correct accept/invalid/unknown outputs, proof trusted base and independent source holdout, not certificate verifier microtime alone.

## Proposed source/observer universe to declare before code

1. Pin source commit SHA, module versions, build tags, Go version, source ownership/authorized edit scope and old-client joint observer.
2. A certificate must name an exact source dependency slice and an explicit proof that every client-relevant allocation/read/write origin is inside that slice. Revisions of outside files are allowed ONLY when a separately checked noninterference condition holds. If no such proof exists return UNKNOWN.
3. Positive classes: identifier renaming with a valid renaming proof; edits to demonstrably non-dependent declarations, formatting-only changes. Negative controls: changed pointer alias; newly introduced global initialization, package-level side effect, method lookup/callback/reflective call, hidden build directive, type change, dependency edge crossing supposedly unrelated region, changed authorized editor rights. Unsupported changes cannot inherit a certificate.
4. Every source version independently compiles/runs Go native test cohorts including old-client input/output and selected schedule bounds. Green tests are evidence, NOT universal source-semantic coverage.
5. Compare candidate transport vs (A) exact classical full reanalysis, (B) classical dependency-cache, (C) bi-abduction/alias footprint decomposition when available with same constraints. A syntactic token hash that excludes changed source has no proof power alone.
6. Measure total issuance+transport/recomputation and bytes/CPU with repeated runs and uncertainty; keep failure cases and hold out independent source-edit histories. The researcher-selected initial fixture is NOT external blind generalization.

## Advancement and stop gates

- **Soundness:** any falsely reused certificate after a client-relevant edit invalidates this research route; reject unsafe prior proof reuse.
- **Classical comparison:** if the same dependency analysis/cache can do the job at equal or lower cost, record classical TIE/LOSE, not novel EAC.
- **Scope:** even sound results on a bounded Go grammar cannot be declared general Go G1–G7 closure.
- **BFS return:** the aim remains independently useful prediction of future safe modification capacity from real source, authenticated rights, clients and *measured* costs. Source naming/caching is instrumental, not the target.
- **Scientific authority:** Research OS Harvest is hypothesis/rival discovery; original Drive paper text and CI source runs are independently needed for load-bearing claims.

G1–G7 OPEN, LAW-R2 HOLD. Keep PR #12/#13 DRAFT and unmerged. New F19 results NONE at time of seal.
