# P34-P2 — Original TrueForge P11, Temporal LSP/ISP, Review Authority

**P34 OPEN / P2 METHOD PASS / LAW-R2 NOT_AUTHORIZED.** This restores **ORIGIN-R1-P11** (Exa #852 → Tavily #853), not **LAW-R1-P11** (state sufficiency Pi(X,G,E)).

## Authentic original receipt
[Historical terminal JSON](https://github.com/WhoSia/EvoNOMOS/blob/e2e5a2e43c899e9e3574b615ba2375b32d0895fb/active/g8-origin-r1-p11-p3/receipts/P3_TERMINAL.json), [frozen rival constitution](https://github.com/WhoSia/EvoNOMOS/blob/e2e5a2e43c899e9e3574b615ba2375b32d0895fb/active/g8-origin-r1-p11-p3/inherited/RIVAL_CONSTITUTION.json), [real-demand contract](https://github.com/WhoSia/EvoNOMOS/blob/e2e5a2e43c899e9e3574b615ba2375b32d0895fb/active/g8-origin-r1-p11-p3/inherited/DUAL_REAL_DEMAND_CONTRACT.json). TrueForge pre-demand commit `dd421b79216c9b42eefd7b0191e546919f8be3f1`. Original hosted run `36382197510` SUCCESS.

| Arm | Exa phase 0 (S,L,C,A,Q) | Tavily phase 1 |
| --- | --- | --- |
| WIDE | (5,156,1,2,1) | (6,166,1,3,1) |
| SEG | (5,183,0,2,1) | (6,135,0,3,1) |
| SEG−WIDE | (0,+27,−1,0,0) | (0,−31,−1,0,0) |

Phase0 TRADEOFF; phase1 SEG **phasewise** Pareto dominance. CBL-C1 mechanism supported in two real search-only demands, CIL-C1 later membership discrimination absent, **no total design winner**. Both arms had Q=1 under the original shared mock oracle. These are source-recovered historical outcomes, not new measurements.

## Temporal interpretation
Pre-demand TypeScript `IWebSearchProvider` requires both `search` and `fetch`. WIDE truthfully keeps search+fetch for every configured provider. SEG creates search-only Exa/Tavily while preserving Parallel's search+fetch.

A **search-only client** requires configure→advertise search→call search→valid return: both arms are behaviorally acceptable. A **broad search+fetch client** may legally fetch after selecting any provider: WIDE admits this, SEG does not for Exa/Tavily. Hence SEG is **not a substitute for WIDE's broader client promise** but this does *not* make SEG inherently LSP-invalid: its exposed interface contract is different. Under actual frozen demand, search-only, both meet the contractual Q. ISP prefers no irrelevant fetch exposure/burden (C=0) while initial SEG extra handwritten churn was +27. Later phase churn difference reverses to −31. No universal optimality follows.

[Executable finite model](../../tools/law-r1-p34-origin-p11-temporal.mjs) verifies 20 phase/provider/arm/client combinations and matches exact historic vectors using immutable historical+donor source checkouts. [Read-only hosted run 37886244507](https://github.com/WhoSia/EvoNOMOS/actions/runs/37886244507) SUCCESS, artifact `11596172591`, SHA256 `0a784d92df32f68058556d5e52070036ac8881d6919a326b6939e9b575ecc6da`. This does **not** re-execute original TypeScript treatments or implement full temporal interface-automata games.

## Source governance evidence, independent of import syntax
Pre-demand [CODEOWNERS](https://github.com/truefoundry/trueforge/blob/dd421b79216c9b42eefd7b0191e546919f8be3f1/.github/CODEOWNERS) has a root wildcard covering core web search, listing @heerambavi1998 among responsible reviewers. [CONTRIBUTING](https://github.com/truefoundry/trueforge/blob/dd421b79216c9b42eefd7b0191e546919f8be3f1/CONTRIBUTING.md) requires maintainer approval before community issue PR submissions. Historical [PR #761](https://github.com/truefoundry/trueforge/pull/761) actually changes WebSearchProvider.ts and was **approved by @heerambavi1998** September 17 and merged. [PR #833](https://github.com/truefoundry/trueforge/pull/833) further changes provider machinery; approved by @heerambavi1998 and another reviewer September 22 and merged. Both were prior to the demands.

This establishes **documented review responsibility + realized approvals**, not exclusive contract-change sovereignty. The branch-protection API returned HTTP 403 to this integration, so whether code-owner review was enforceable as a branch rule is UNKNOWN. Later Exa PR #888 is explicitly excluded from pre-demand evidence.

## Original literature / chronology
[Drive HELD Liskov–Wing 1994](https://drive.google.com/file/d/1g7ruRxKmmki7ts6fQ09MIOwuYPCeCVvl/view), [Drive HELD Martin 1996](https://drive.google.com/file/d/1fZQi6039W58RcQxTKFHiJZw22mU9kw7g/view), [Drive HELD de Alfaro–Henzinger 2001](https://drive.google.com/file/d/1NUV-6p3ANXDT6ftnURRb8LpwbSp1xTSV/view). Archived [EvoNOMOS 10.md](https://drive.google.com/file/d/1CSIprWnMZKS3UCcP1SfZ6ZquhoxwH_lX/view) records ORIGIN-P11; [12.md](https://drive.google.com/file/d/13zoHWfi38aBshA4dG61JpmwmXH4MUT5j/view) discusses different LAW-P11.

**Next:** actual mock-wire temporal trace validation, CODEOWNERS authority changes over time, and independent demand with co-required fetch. No prospective law win yet.

**Verdict:** `P34_P2_ORIGIN_HISTORICAL_RECONSTITUTION_PASS__CLIENT_RELATIVE_LSP_ISP_PASS__INDEPENDENT_REVIEW_AUTHORITY_PARTIAL__LAW_R2_HOLD`.
