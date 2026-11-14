# P44-F25 — Milner CCS: 1980 original / 1986 LFCS author reissue, direct visual-reading court, finite executable classical baseline
Date 2026-11-06 (Asia/Seoul). SOURCE-FIRST. Research branch only; user-file custody intact. Neither a claim of a new software law nor complete 179-page manual reading.

## A. New original identified, bytes opened, custody corrected
Original Drive new user upload `1UMIKisS7TimmHL69CwgSK-Ga48iUptZV`, filename `A Calculus of Communicating Systems[1980].pdf`. Direct reading of actual rasterized page 1: **LFCS Report Series ECS-LFCS-86-7, August 1986, Laboratory for Foundations of Computer Science, University of Edinburgh**, original publication **Springer-Verlag Lecture Notes in Computer Science vol 92 (1980)**. On page 2, author Robin Milner and 1986 Edinburgh issue are explicitly printed. 179 scanned PDF pages; zero selectable/extractable text on inspected pages. PDF opens and selected independent pages (1, 2, 3, 4, 11, 21, 51, 101, 179) rendered and were directly inspected. PDF byte size 12,911,643 and SHA-256 `abe6657c1da4fea712452dde60a69453240848118781e99b4f6572a82630f8ad`. Filename metadata renamed to `Milner (1980 original; LFCS 1986 report issue) — A Calculus of Communicating Systems — ECS-LFCS-86-7 — IMAGE SCAN.pdf`, moved 00_INTAKE -> 11_BOOKS while retaining Drive ID, source unchanged. [Verified original](https://drive.google.com/file/d/1UMIKisS7TimmHL69CwgSK-Ga48iUptZV/view). This acquisition resolves the **1980 CCS text missing-title status**, but exact 1980 first printing physical edition remains distinguished from the 1986 reissue.

## B. Critical unexpected source discovery: the 1986 preface
Actual PDF page 3 (new preface) states the work was originally published by Springer in 1980; Edinburgh reissued because original was discontinued. Author says **NOT a revised edition**: original work unchanged except two pages (printed 129 and 130) were swapped in Springer edition, plus some typographical corrections. The new preface explicitly credits **David Park's idea of bisimulation** as the key development since the original, and explains replacing a descending chain of equivalences / induction-on-depth proof technique with a more direct greatest-bisimulation relation and relational witness proof method. Historical analysis MUST distinguish the 1980 body from the later 1986 prefatory reinterpretation. This is direct actual-page evidence, not a generic history inferred from memory.

## C. Targeted original reading: precise propositions with image page scope
- Printed p.3 (PDF p.11), §0 overview: systems are composed by mutual interaction/observation. CCS is explicitly an algebra of behaviours and derivatives, not just a graph representation.
- Printed p.13 (PDF p.21), Rigid Synchronization Trees: action-labelled rooted unordered finitely branching trees; plus as associative/commutative choice; nil as zero. This is a very early explicit algebraic route from local interaction to composition.
- Printed p.43 (PDF p.51), §3: decreasing observation-equivalence approximants and the subtlety that their limiting relation may not satisfy a naive recursive equation without stated finiteness assumptions. The technical theorem and image-finite limitations should not be generalized to arbitrary unbounded source programs.
- Printed p.93 (PDF p.101), Theorem 6.2 discusses correspondence of atomic programs/actions and their representations as communicating trees; Theorem 6.3 on same page announces congruence for CT strong equivalence. The point: **closure under composition is preexisting classical research**, not an EvoNOMOS novelty.
- Printed p.171 (PDF p.179) bibliography survives; this is structural evidence of readability, not proof every page passed.

These are selected deeply inspected pages, not cover-to-cover complete study. No OCR performed (not necessary to inspect printed pages). The image-only limitation remains a citation/navigation cost.

## D. Why the 1980 versus 1986 distinction matters
The original body builds a calculus with observation, derivative behaviours, and substitution-like operations; 1986 preface then offers a cleaner *bisimulation* re-presentation credited to Park. The story 'Milner proved the modern Park bisimulation formulation in 1980' would erase an important intellectual chronology. EvoNOMOS should similarly maintain exact date, information disclosure date, revision, authority, and provenance for each new proposed law.

## E. Executable classical baseline and countermodels
Two local files independently executed under Python with `python -m unittest -q`: **13 tests PASS**; bytecode compile also passed. Code committed separately under `formulation/f25_lts/finite_court.py` and `test_finite_court.py`. Main operations:
- explicit finite complete state tables with client observer symbols,
- authorised edit transition labels `(actor, demand, nonnegative integer cost)`,
- exact labelled greatest-fixed-point bisimulation as a classic baseline,
- bounded prefix trace-language enumeration,
- a Dijkstra-based *first qualifying edge* cost demo. **DO NOT confuse this last scalar with a sequential-persistent-demand repair cost**.
Falsification case A: `a.(b+c)` versus `a.b+a.c`: exactly the same finite action words, unequal bisimulation because after action a one graph retains both future choices and the other has committed to one branch.
Case B: same coarse runtime observer symbol but owner has an extension edge in graph A; graph B has none. Rights-labelled bisimulation detects a difference. Identical runtime observations cannot imply legal future edits.
Other tests: actor mismatch, unit-cost mismatch, observer mismatch, unknown target, incomplete transition table, negative cost, empty actor, lowest of multiple candidate edit costs, reflexivity, empty word, rights-sensitive trace mismatch.
Limitations: finite tables declared **complete by fiat**, observer symbol exact equality not a complete client semantics, no Go parser/alias completeness, no actor permit provenance beyond labels, no independent future demands, no classical source-analysis superiority, no conditional source soundness theorem beyond abstract fixed-point reasoning. These negative cases are **textbook bisimulation, not original new theory**. Source correctness of code should be audited if moved to external production.

## F. Strengthened path towards SOLID over-axiomatization critique
A raw SOLID checklist is an impoverished invariant: even identical trace language cannot reconstruct strategic future branching, and identical old-client runtime signals cannot reconstruct authorized source edits. To claim an adequate mathematical superstructure must index (1) full declared contextual observations, (2) actor-permission provenance, (3) versioned edit outcomes, (4) cost and reversibility, and (5) sequential demand histories. Hennessy–Milner 1985 and Milner 1980/1986 and 1999 provide strong PRIOR-ART barriers for observational equivalence, bisimulation and context congruence; the only promising target is **real-source verified extraction and practical predictive value** against these exact classical baselines.

## G. Stop and priority
- Literary milestone: three recent originals + CCS source are now present canonically. The CCS 1980 *work* no longer belongs in missing-title table; its acquired *edition* is the 1986 non-revised LFCS reissue.
- G1–G7 OPEN; LAW-R2 HOLD. PR #13 Draft/unmerged; main unchanged. No fictitious C5 prospective claim.
- Next experiment: typed Go source-aware actor/scope/alias extractor plus source mutation oracles; verify rollback, old-client observation, and expense. Benchmark against identical-information classical reachability / weighted bisim / CEGAR before naming any law.
