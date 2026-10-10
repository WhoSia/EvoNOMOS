# P40 P2 — Endpoint–Sequence Obstruction Decomposition and Atomic-Edit Counterfactuals

**2026-10-10 · P40 source-grounded theory development · exactly validated finite guarded edit model · strongest classical reachability rival undefeated · NEW-LAW HOLD.**

[P40 P0](P40_P0_AUTHORIZED_OPENING_COMPOSITIONAL_REPAIR_AND_ARCHITECTURE_LAW_CONTRACT.md) · [P1 actual Go method-set source matrix](P40_P1_GUARDED_SOURCE_REPAIR_COMPOSITION_AND_GO_INTERFACE_COURT.md) · [P2 independent formal enumerator](../../tools/p40-p2/guarded_repair_obstruction_court.py).

## P2-A. Distinguish three different kinds of repair failure

Fix the *typed original Go P40-P1 world*: unchanged old `Port.Run()` client, changeable `Fast`, optionally protected `Legacy`, two independently authorized source edits:
- T: publish a new API contract (widen existing `Port` versus declare `Advanced` extending unchanged Port).
- M: add `Fast.Next`.
- Goal: both T and M installed, Fast supports the new interface, and all protected original `Port` clients still compile and behave as promised.

Let source states be `00,10,01,11` with first bit T, second bit M. Safe(s) requires actual Go type-checking, old-client behavior under tests and the declared protected implementer. Source edit permission Γ includes some subset of the single-step edges `00→10→11`, `00→01→11` and an OPTIONAL atomic bundled edge `00→11`.

There are three mathematically distinct outcomes:
1. **Terminal/endpoint obstruction:** `Safe(11)=false`, so no legal sequence and no single atomic T+M edit can achieve the demanded endpoint, regardless of edit order or transition rights. Coupled widening with protected Legacy has exactly this type-set obstruction.
2. **Sequence/intermediate obstruction:** `Safe(11)=true`, but every owner-authorized *sequential* path crosses an unsafe intermediate source. This obstruction may disappear if an authorized atomic T+M edit is admitted. Coupled widening without protected Legacy, but with **T-first-only owner edit rights**, is such a world.
3. **Reachable safe repair:** at least one sequential or explicitly authorized atomic edge reaches the terminal goal while preserving old-client invariants.

**This distinction is real software architecture explanation** because the *same final desired capability* can fail for an entirely different reason under different interfaces and permission order. It is a **conditional result**, not a universal metric of maintainability or novelty over graph theory.

## P2-B. Exact repair-existence theorem for arbitrary guarded two-edit worlds

Let (c_{ij}) denote whether `ij` is safe. Let (a_T,a_M) allow first changes `00→10` and `00→01`, and (b_T,b_M) allow respective second changes `10→11` and `01→11`. Let (A) permit **one atomic two-region edit** `00→11`. This edge is an independently authorized operation and is not silently presumed.

**Theorem P2.1 (classical finite-state reachability, exact):**
[
oxed{operatorname{May}
=c_{00}land c_{11}land
left[Alor
  (c_{10}land a_Tland b_T)lor
  (c_{01}land a_Mland b_M)ight].}
]

**Proof:** Every allowable edit path from 00 to 11 either uses the direct atomic edge, visits 10, or visits 01; these are all possibilities under the declared edit grammar. Each branch exists iff all its intermediate vertices are safe and every used edge authorized. Conversely, each satisfied branch constructs exactly the corresponding safe path.

The condition is ordinary two-step guarded transition reachability (the 2D case of P1 grid DP). It is *not* a new law of software design. It is nevertheless falsifiable by actual Go source compile/behavior checks in P1.

## P2-C. Exact compiler-grounded architecture by edit-rights matrix

P1 independently used the Go compiler on ALL 16 source revision instances to establish the safe-state vectors (in order 00,10,01,11):
- coupled, without protected Legacy: ((1,0,1,1)).
- coupled, protected Legacy: ((1,0,1,0)).
- segregated `Advanced`, with/without protected Legacy: ((1,1,1,1)).

Combine those actually checked safe states with explicitly hypothetical OWNER edge rights. Consider sequential BOTH orders; T-FIRST only; M-FIRST only; T-FIRST plus atomic T+M; ATOMIC ONLY.

| Architecture and closed old contract | Both sequential | T-first | M-first | T-first + atomic | Atomic only |
| --- | --- | --- | --- | --- | --- |
| Coupled, no protected Legacy | YES | NO | YES | YES | YES |
| Coupled, protected Legacy | NO | NO | NO | NO | NO |
| Separate Advanced, no protected Legacy | YES | YES | YES | YES | YES |
| Separate Advanced, protected Legacy | YES | YES | YES | YES | YES |

**Counterfactual insight:** Atomic edit access can repair a **sequence-only** type-checking obstruction without fixing a **terminal old-client contract obstruction**. An owner policy requiring publication before provider modification reverses the coupled unprotected case from YES to NO. An immutable `Legacy` obligation prevents that repair even under permitted simultaneous changes. Separate capabilities retain a safe path in all explicitly listed owner regimes. No real maintainer owner policy has been observed here.

## P2-D. Exhaustive proof court, scope and competing theory

[Finite Python court](../../tools/p40-p2/guarded_repair_obstruction_court.py) tests ALL 16 four-state safety bitmasks and ALL 32 edge-authorization bitmasks (4 sequential plus 1 atomic), for **512 worlds**. It computes source repair reachability via independent breadth-first search and via the closed theorem formula; agreement is exact for all. Categorization: **384** worlds fail the initial or terminal invariant, **49** have valid endpoints but no legal edit path, **79** are reachable. These are combinatorial model counts, NOT observations from 512 maintained Go codebases.

**Classical competitors:** finite labeled transition reachability, strong Go interface method-set semantics, Menger cuts and interface segregation, adapters/API versioning and permission/atomic transaction models. This formal result directly reduces to standard reachability; **new mathematical/software law IDENTIFICATION HOLD**. Endpoint validity does not prove deployment safety or binary ecosystem compatibility, and our old-client behavioral test is bounded, not an exhaustive real-world behavioral subtype proof.

**Next scientific target (P40 P3 candidate, not automatically opened):** test structurally stronger rivals such as versioned adapter and wrapper transformations with equal old clients and future demand, including source-code edits that are authorized but NOT independent. Seek a stronger context-reversal theorem or find that classical plugin/adapter patterns subsume the effect. Do not confuse more scripts or CI steps with a new law.

**State:** P40 OPEN · P1 GO ACTUAL SOURCE COMPILATION PASS · P2 EXACT 512 MODEL / CLASSICAL · DIP49 HOLD · LAW-R2_NOT_AUTHORIZED.

## P2-E. Independent hosted mathematical receipt

[GitHub Actions #38040557732](https://github.com/WhoSia/EvoNOMOS/actions/runs/38040557732) **SUCCESS** on exact mathematical code/workflow commit `9ca3721ed211fcd8f89de4c16391e936f47dab94`, job `guarded-edit-proof` SUCCESS, source test step SUCCESS. Artifact `11665646792` SHA256 `546c72cd93a90e7f2f85734d3ffa8b65c2db19e631ab2bf2c699de152d899229`. Full 512-world BFS-versus-closed-form corpus: endpoint-invalid 384, endpoint-valid but path-blocked 49, endpoint-valid and repair-feasible 79. These are synthetic guard masks, not 512 real maintained Go repos. Actual 16 Go compilations remain [P40-P1 Actions #38040317493](https://github.com/WhoSia/EvoNOMOS/actions/runs/38040317493), distinct independent evidence. The mathematical model and Go compiler conclusions match under the named mapping; no general new architecture law identified.
