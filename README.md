# EvoNOMOS

**Evolutionary Nomology, Optimization, and Measurement of Software Organization**

EvoNOMOS studies the *conditions under which software organization changes the cost and safety of future changes*. It tests responsibility boundaries, dependency direction, behavioral contracts, interface capability, shared invariants, and migration paths in executable source. **SOLID is a family of conditional design hypotheses—not an axiomatic scoring system or a guaranteed architecture ranking.**

> **Current scientific head (2026-10-09):** Generation VIII · **LAW-R1-P35 OPEN** — *Independent Capability Engines, Cross-Operation Change Propagation, Source-Edit Locality & Demand-Conditioned SOLID Cost Geometry*. **LAW-R2 NOT AUTHORIZED.**

## Start here

| Surface | Canonical source | What it establishes |
| --- | --- | --- |
| Current experiment | [P35 technical opening](active/g8-law-r1-p35/P35_OPENING_INDEPENDENT_CAPABILITY_ENGINES.md) · [P35 Notion Run](https://app.notion.com/p/3f4ef561cf9281e6acd6c17204066784) | Two genuinely different in-memory Go storage organizations; matched behavioral and change demands |
| Verified predecessor | [P34 terminal](active/g8-law-r1-p34/P34_TERMINAL_SOURCE_EDITS_AND_P35_HANDOFF.md) | DIRECT/COMPOSED changed one method and +4/−1 lines each under KeyFile size rule; no locality winner |
| Theoretical foundation | [P33 integrated SOLID interpretation](active/g8-law-r1-p33/P33_CONTRACT_OBSERVATION_AUTHORITY_INTEGRATED_SOLID.md) · [Demand-relative quotient](active/g8-law-r1-p33/P33_DEMAND_RELATIVE_INTERFACE_QUOTIENTS_AND_CONDITIONAL_SOLID.md) | Classical factorization, contract refinement, authority and conditional change-cost theory; not a new universal mathematical theorem |
| Literature & rivals | [Harvest / source and repair families](https://app.notion.com/p/3f3ef561cf9281819a9fd930746e5ca5) | Parnas, Liskov–Wing, Martin, Design Rule Spaces, CSDG, repair synthesis, information cuts, set-valued continuation |
| Genealogy | [Active lineage](active/README.md) · [Research OS / Entry Card](https://app.notion.com/p/3caef561cf928153ae09eed2bf4b7d72) | Separate historical snapshots from current permission to make scientific claims |
| Native proof | [P35-P2 native Restic evidence](active/g8-law-r1-p35/P35_P2_NATIVE_RESTIC_EIGHT_WORLDS_AND_ARCHITECTURE_ADMISSIBILITY.md) · [P35 reproduction protocol](active/g8-law-r1-p35/P35_P1_REPRODUCTION_AND_SOURCE_BOUNDARY.md) | Eight separately compiled Go source worlds, original pinned Restic tests and negative controls; not full upstream test suite |

**Status hierarchy:** `CLOSED` means the named phase received its terminal verdict, not that every large scientific hypothesis passed. `METHOD PASS` certifies only the declared method. `HOLD` and `TERMINAL_NONRESULT` are not transformed into evidence by a later narrative. In particular, original ORIGIN-R1-P12 is still **TERMINAL_NONRESULT**.

## Research question

Given the **same public behavior**, the **same change demand**, and a disclosed repair grammar, when does one object/module boundary make change cheaper, safer or more expensive than another? What is observable before implementation, and when do different architectures become **nonidentifiable** under a chosen experiment?

Track the lifecycle vector **S / L / C / A / Q** where supported (physical edit sites; changed source lines; inter-component coordination; architectural burden/authority contacts where independently operationalized; behavior-oracle outcome). Do not collapse incomparable dimensions into a synthetic `SOLID quality` score or infer person-hours from call/dispatch counts.

A meaningful structural claim needs:
1. A pinned source state and stated behavior/history contract, including cancellation and error callbacks.
2. Explicit intervention and matched requirements; unchanged pre-demand negative control.
3. Actual source diffs, compile/test logs, and independent or strongest available analysis baseline.
4. Repair-strategy alternatives and identifiable conditions for a claimed advantage or reversal.
5. An honest limitation when static dependence, known factorization or representation choices already explain the result.

## Current empirical line: P33 → P34 → P35

### P33 — Conditional mathematical interpretation (CLOSED)

- **ISP / restricted OCP:** For demanded observations `g_d`, a boundary `o` can support downstream-only refinement only when `ker(o) ⊆ ker(g_d)`, under the stated deterministic setting. This is **classical function factorization** applied to design; it is not claimed as newly proved mathematics.
- **LSP:** Client-preserving substitutability requires contract/trace history and admissibility, not matching names or method signatures alone.
- **DIP:** Compile-time dependency inversion, runtime control flow, and ownership of the abstraction are distinct questions.
- **SRP:** Separation trades change-interference costs against its own coordination and evolution costs; sign depends on demand distribution and prices.
- Repair families are **grammar- and oracle-relative**. A recorded successful patch is not the complete family, and the smallest initial edit is not necessarily the smallest lifecycle cost.

[Integrated theory and its limits](active/g8-law-r1-p33/P33_CONTRACT_OBSERVATION_AUTHORITY_INTEGRATED_SOLID.md).

### P34 — Real Go behavior and source edits (CLOSED)

The same pinned [Restic `Backend` interface](https://github.com/restic/restic/blob/495982232cf1af184eac0a97871ef8161e8708ee/internal/restic/backend.go) (12 methods) was implemented by a DIRECT arm and a COMPOSED arm that **intentionally shared one data vault**. Hosted [P4 run #37888110765](https://github.com/WhoSia/EvoNOMOS/actions/runs/37888110765) reported **18/18 identical public-operation histories**, with 0 vs 18 *extra adapter→unit dispatches*. This measures dispatch topology, **not developer work**.

A separately precommitted KeyFile Save rule (reject >8 bytes, preserving prior data) made the unedited baseline fail. Hosted [P5 run #37889096693](https://github.com/WhoSia/EvoNOMOS/actions/runs/37889096693) passed in both patched arms. Both patches changed **one file, one method, +4/−1 lines**. This negative result shows a delegating object boundary need not improve locality under a single-operation demand. No universal conclusion about modularity follows.

### P35 — Independent state engines and coupled change (OPEN)

**Native upstream execution PASS (2026-10-09).** [GitHub Actions #37895607800](https://github.com/WhoSia/EvoNOMOS/actions/runs/37895607800) checked out the exact original `restic/restic@495982232cf1af184eac0a97871ef8161e8708ee`, compiled, vetted and race-tested **eight independent P35 source worlds**, re-ran the P34 18-operation public-history contract on each, and verified both pre-edit negative controls fail for the intended reason. All eight passed the native package regression; artifact [#11599942843](https://github.com/WhoSia/EvoNOMOS/actions/runs/37895607800) SHA-256 `49d38c9c60a7415c9b9395cb7c52db5e33cdf25e55297de6888d5f52fa89f85b`. Source, shared tests and a read-only reusable runner are [browser-readable Go files under `tools/p35-p1/`](tools/p35-p1/worlds/baseline/backend.go). **This is a bounded P35 package result, not a full upstream Restic test-suite or production storage certification.**


The P35 implementation comparison must eliminate P34's common vault:
- **UNIFIED:** one `map[Handle]record` authoritative for payload and logical size.
- **COMPOSED:** separately owned payload and metadata stores, a read decoder and removal coordination, connected by explicit consistency operations. Distinct maps are *not automatically a proof of operational independence*.

The first **local P35-P1** source experiment (2026-10-09) applied two requirements to the same P0 starting implementations:

| New demand | UNIFIED observed edit support | COMPOSED observed edit support | Scope |
| --- | --- | --- | --- |
| KeyFile-only length rule | 1 existing method | 1 existing method | Selected local Go source patches; both pass |
| Reversible versioned storage retaining arbitrary legacy data | 2 existing methods | 6 with separate version map; 5 with independent version storage or delegated tagged decoding; **4 with tagged payload decoded inside the payload store** | Selected candidate repair strategies, **not minimal architectures** |

In the versioning case a content prefix is not enough to classify old arbitrary byte streams: `S_old(x)=S_new(y)` with `x≠y` makes the two intended decodings incompatible unless distinguishing context exists. This is a **known information-cut obstruction**, not a new theorem. The experiment placed that additional information in different source structures and measured actual patches. The composed arm's change from 6 to 5 methods under an alternate implementation is itself evidence that one patch footprint does not characterize an entire design.

**Repair-grammar boundary:** [P35 repair-family and rival-baseline audit](active/g8-law-r1-p35/P35_P1_FOUR_METHOD_REPAIR_AND_STRONG_RIVAL_BOUNDARY.md) records a four-method COMPOSED variant that moves decoding into `payloadStore.get`. It **passes behavior but violates the frozen independence of the read decoder**. A five-method tagged-payload variant preserves that independence. Neither figure is a proven architectural minimum.

**Validation boundary:** Local shim checks were preliminary; **actual pinned Restic module package compile, `go vet`, `go test -race` and all eight P35 source-world regressions have now passed on a hosted read-only runner**. Baseline new-demand negatives failed as intended. Tests do not cover the entire upstream Restic module/production backend, real external durability, or independent future-demand prediction; B0+/B1/B2 strong rivals and grammar-complete minimum repair search remain open. The Go sources and [runner](tools/p35-p1/run_pinned_restic.sh) are committed to GitHub by the human account; [source-based verdict](active/g8-law-r1-p35/P35_P2_NATIVE_RESTIC_EIGHT_WORLDS_AND_ARCHITECTURE_ADMISSIBILITY.md).

## What would constitute a stronger result?

Potential impact `Impact(A,d)`, actual admissible repairs `R_A(d; T,G)`, and realized edit support `S_A(r)` answer **different** questions. A dependency graph may conservatively include every ultimately edited method yet fail to choose a unique repair. Conversely, conventional static/source-aware or architecture-design baselines may predict the edits just as well as any proposed new structural formalism.

**Competitors:** B0+ source-aware call/data/field/selector analysis; B1 genuine history-informed co-change predictors when history exists; B2 Parnas/Design Rule Spaces/CSDG and standard repair synthesis. Match access to source, demand knowledge, repair hints and outcome information. No victory by comparing a full-information new hypothesis to a deliberately crippled old model.

A meaningful mathematical next step is a **bounded set-valued, demand-conditioned repair-cost relation**, with admissibility stated explicitly. A new universal structure law does **not** follow just from naming that relation or from invoking category theory, sheaves, option value or Pareto geometry. Prefer executable counterexamples and failure of an actually viable rival over ornamental abstraction.

## Repository structure and reproducibility

```text
active/       Current experimental stages, exact verdicts and lineage
tools/        Executable Go/JS/Rust/Python methods and test harnesses
lawkit/       Finite law-candidate and structure probes
crates/       Rust support where appropriate
.github/      Hosted read-only test workflows
```

Go is used for Restic-native interface/behavior tests, Rust for appropriate high-throughput core analysis, and Python or JS for reproducible preparation and audits; language selection follows the actual substrate, not a mandatory polyglot checklist.

For the **verified P34** run, see [source](tools/p34-p4/pair.go), [18-step oracle](tools/p34-p4/pair_test.go), and [P5 materializer](tools/p34-p5/materialize.mjs). For **P35**, inspect [real Go source worlds](tools/p35-p1/worlds/baseline/backend.go), [original Restic runner](tools/p35-p1/run_pinned_restic.sh), and [hosted evidence](active/g8-law-r1-p35/P35_P2_NATIVE_RESTIC_EIGHT_WORLDS_AND_ARCHITECTURE_ADMISSIBILITY.md). Original Restic module package acceptance is demonstrated at the pinned commit, but broader upstream/production assertions are withheld.

## Literature and custody

Use **canonical original PDFs in Google Drive** before web summaries. Search `10_PAPERS` and existing Harvest by title, author, DOI and aliases; inspect the original methods and limits. Newly discussed papers must be labelled `Drive 보유` with the confirmed file or `Drive 미확보(색인 검색 기준)` with an independently checked legal *direct PDF* link if available. `00_INTAKE` → bibliographic/duplicate/byte checks → canonical `10_PAPERS` → readback → existing Harvest extension. Absence from search is not proof of global absence.

Relevant original sources already recorded as held include [Liskov & Wing 1994](https://drive.google.com/file/d/1g7ruRxKmmki7ts6fQ09MIOwuYPCeCVvl/view), [Martin 1996](https://drive.google.com/file/d/1fZQi6039W58RcQxTKFHiJZw22mU9kw7g/view), [de Alfaro & Henzinger 2001](https://drive.google.com/file/d/1NUV-6p3ANXDT6ftnURRb8LpwbSp1xTSV/view), and the original repair/diagnosis papers indexed in the [P33 Harvest](https://app.notion.com/p/3f3ef561cf9281819a9fd930746e5ca5). Do not treat citation prominence as evidence quality.

## Reproducibility, authorship and scope

- `main` is the canonical working branch. Pin source SHA and artifact hashes; avoid branch-per-stage archival structures.
- **BOT_CONTRIBUTION_ZERO:** GitHub Actions are computation-only (`contents: read`) and must **never** commit/push/tag/rewrite refs. Audit both commit author and committer before promoting changes. Bot-authored repo contributions are an immediate stop condition.
- Negative cases, superseded results and `HOLD` states are retained as *history*, not hidden or promoted.
- GitHub carries compact executable evidence; Notion maintains decisions and science narrative; Google Drive retains canonical original research files and historical conversation archive. The 1–14 chat exports are research context, **not** independently adjudicated outcome data.
- **No automatic LAW-R2**, no attribution of P34 outcomes to original ORIGIN-P12, and no independent new predictive architecture-law claim without the relevant strong-rival and held-out evidence.

**Next executable work:** with original Restic package compatibility now verified, compare architecture-admissible patch families (especially U2 vs C5) against equally informed source-aware B0+, historical B1 where available, and Parnas/DRSpaces/CSDG B2; then adjudicate P35 without premature global ranking. Pursue fresh real maintenance worlds where the current experiment is nonidentifying.
