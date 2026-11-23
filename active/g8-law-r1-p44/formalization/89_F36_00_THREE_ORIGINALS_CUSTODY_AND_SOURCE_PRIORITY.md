# P44 F36 R1 — 2026-11-21 Research OS 00_INTAKE: Three Exact-Original Source Receipts and Priority Reading

**Scope:** evidence audit + first-pass text verification of three new in-Drive works. No new theorem, Go CI, automatic source-right attestation or Paper B reviewer observation. **P44 RUNNING · LAW-R2 HOLD · G1–G7 OPEN.**

## 1. Intake/current-custody observations

At first direct paginated scan, `00_INTAKE` folder ID `1MLtYh0pv8QUZDReYzRqjDrOjRkSJAD16` contained precisely three PDF records. During this session another process or user session **renamed and moved them**; the current second scan found **0** items in `00_INTAKE`. **This investigation did not issue Drive rename/move commands.** After movement, direct Drive metadata and raw-byte fetch were checked for all three. Do not backdate a move as our own result.

| Source (authenticated as listed) | Drive ID/current shelf | Container raw PDF bytes | SHA-256 of fetched raw bytes | PDF pages | Evidence limits |
| --- | --- | ---: | --- | ---: | --- |
| C. B. Jones (June 1981), *Development Methods for Computer Programs Including a Notion of Interference*, Technical Monograph PRG-25 | [11_SOURCES](https://drive.google.com/file/d/1c2vEnheOmaTgKti8eexRyks-vwkBdnv4/view) | 11,216,901 | `959f08ff08f9bf501bf7e190ecea17a0d67d02a9cf916a2c34eac107ddec2bc7` | 265 scanned PDF leaves | Original internal title page physically rendered and inspected. Oxford institutional [catalog](https://www.cs.ox.ac.uk/publications/publication3768-abstract.html) and [official PDF](https://www.cs.ox.ac.uk/files/9025/PRG-25.pdf) support title/author/date; **raw-byte identity with official web copy not established**. Scanned text layer blank in Drive. |
| Stephen Brookes (2004), *A Semantics for Concurrent Separation Logic* | [10_PAPERS](https://drive.google.com/file/d/1j-_Yc5YfUfx6viR1o4CtxNepKSaSIAFa/view) | 235,616 | `ecd8e540d990cf4aa48871ceaedce4bcf865d80b9ff4e5cf91dcf72bfa7c50fa` | 18 | Author-manuscript layout/title/abstract/body inspected, corresponding to [CONCUR 2004](https://dblp.org/rec/conf/concur/Brookes04.html), **not claimed to be page-identical Springer typeset version**. Distinct from held Brookes (2007) journal version. |
| Carliss Y. Baldwin & Kim B. Clark (2000), *Design Rules, Volume 1: The Power of Modularity*, MIT Press | [11_BOOKS](https://drive.google.com/file/d/1yQWVWQSVQRoRNaeH_SHDITdV1oDWr46K/view) | 6,386,345 | `c54830a80ef692fe08d70f0dbf003b23016073c2e69ed643d219d6e8d119a519` | 493 | Printed title/copyright contents identify 2000 volume; [MIT Press publisher](https://mitpress.mit.edu/9780262538206/design-rules-volume-1/) confirms bibliographic identity. The deposited in-Drive PDF filename suggests **third-party digitization**; publisher-original file identity is **not** established. |

**Custody:** downloaded raw PDFs were checked with PyMuPDF and SHA-256, not merely titles. Exact Drive parents were read back. Duplicate name checks did not locate another exact file in 10_PAPERS or 11_BOOKS, although title search is not a full byte-duplicate proof.

## 2. What the actual originals say, and the hard novelty boundaries

**Jones (1981), especially Ch. 2 (data refinement) and Ch. 4 §§4.1, 4.2, 4.4.** The original specification format explicitly records environment *rely* and process *guarantee* conditions; the realizability rule permits less reliance and stronger guarantee. The parallel-combination rule checks compatibility between each component's promised interference and the reliance tolerated by others. This is a pre-1983 source for **assumption/guarantee, refinement, compatible component effects**. Never claim these primitives originate with EvoNOMOS. But Jones' interference specification does **not** by itself authenticate contemporary GitHub maintainer rights, discover all allowed source edits, or predict a third party's future issue.

**Brookes (2004), introduction, resource and soundness sections.** An action-trace semantics with a *local* heap ownership interpretation and precise resource invariants supports compositional correctness of concurrent separation logic; the manuscript derives soundness and a race-freedom result under declared conditions. Classical effect/frame and race-safety reasoning can be a full-information rival for our source-derived alias/effect checks. Its semantic ownership of heap fragments is **not the same thing** as a current repository maintainer's authorization to alter source files.

**Baldwin & Clark (2000), introduction pp.12–15, Ch. 5 pp.123–141, Ch. 9 pp.221–244, Ch. 10 pp.245–282, Ch. 13 pp.323–346.** Six modular operators are already named: splitting, substitution, augmentation, exclusion, inversion, porting. Modular design makes future variation and parallel experimentation possible; economic *option value* measures benefits against costs. Chapter 13 explicitly notes a tradeoff: inversion/visibility may terminate experiments in hidden modules and thus eliminate useful options, even as it creates other value. Chapter 4/8 separate design/task structures from commercial contract structures. It would be incorrect to advertise “architecture creates future repair options,” “design rules shape which changes are possible,” or “an interface always improves flexibility” as newly discovered propositions. Their economic contracts are not automatically a proof of software-source edit permissions.

## 3. Source-derived synthesis for P44

**Before the new originals:** F35 proved a bounded app-owned callback dispatch parity under pinned go-chi/httprouter, correcting the self-forwarding comparator defect of F34; old-client safety scope narrow, LAW-R2 on HOLD.

**After reading the new originals:** We should describe the candidate contribution as **source-extracted, rights-evidenced, observer-indexed, demand-sequence-conditioned *decision certificates***, not a first theory of software design options, rely/guarantee or local heap frames. Source extraction/permission authentication is an empirical and technical capability still **not established**. A future user-owned code patch that preserves an API under checked requests gives stronger evidence than a synthetic graph, but not completeness of source edit possibilities or rights.

Keep evidence objects separate:
- (1) observed source state and frozen build closure;
- (2) admissible source edits under a stated grammar and actor authority;
- (3) jointly protected client behavior across intermediate steps;
- (4) later demands independently declared and timestamped before outcomes;
- (5) source/observer cost bounds and matched-information classical competing predictions.

None of the three originals alone supplies a modern repository's actual (2) or prospective (4). A conditional structural law could still be a valid contribution if a new source-grounded certificate makes held-out predictions under those data and outperforms conventional techniques under identical information; **no such advantage is claimed by this receipt**.

## 4. What goes to Paper B, what does not

Paper B deals with the **justification of rejecting one patch given known obligations**, not the comparative economic value of choosing architecture. Jones shows that explicit rely/guarantee assumptions are longstanding; Brookes and Baldwin–Clark are strong rivals in source-effects and future-option P44 work, respectively. Do not insert an entire account of option economics into the short Paper B. A brief separate bridge note could compare *review evidence sufficiency at a single patch* with *viability of future repair paths under ownership and future demands*.

## 5. Gates

- **F36 source requirement:** from independently maintained exact Go trees, construct *two independently implemented* initial-capability-matched design arms; do not compare a rigid baseline to a purpose-built flexible rival.
- **Rights gate:** source revision and user-owned fork grants must be recorded as separate from upstream maintainer permissions; an author name or repo write permission of an experimental fork does not establish upstream authority.
- **Prospective gate:** changes must be authored/selected independently of measured design outcomes, frozen before evaluating rival costs. Include failures, abstentions, concurrent client regressions and the cost of hooks/abstractions at initial setup.
- **Classical rival:** equal-information source SSA/alias & separation logic/rely-guarantee, plus modular real-options reasoning, tested against the exact proposed predictive claim.
- **Stop:** if no independent demand/permission evidence, return “controlled comparative example” or HOLD and do not advance LAW-R2.

This record supersedes **only the missing/located status for the three exact works** in [ledger 87](../87_PAPER_B_P44_MISSING_PRIMARY_LITERATURE_20261121.md) and F32's historical original-missing ledger; past snapshots remain unchanged.
