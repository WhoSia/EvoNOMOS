# P40 P1 — Go Method-Set Architecture Reversal and Guarded Repair Product

**2026-10-10 KST · ACTUAL GO SOURCE COMPILATION MICROCASE · THEORETICAL CORE · LAW-R1 P40 OPEN · NOVEL DESIGN LAW HOLD.**

[P40 authorized opening](P40_P0_AUTHORIZED_OPENING_COMPOSITIONAL_REPAIR_AND_ARCHITECTURE_LAW_CONTRACT.md) · [Go source revision checker](../../tools/p40-p1/go_interface_source_repair_court.py) · [P39 Math-H abstract cyclic repair geometry](../g8-law-r1-p39/P39_MATH_H_EXACT_SEVEN_SHATTERING_TWO_ANCHOR_AMALGAMATION_AND_INFINITE_BOUNDS.md).

## P1-A. The actual architectural question

Do owner and interface structure *cause* a difference in future allowed repairs even when existing user-visible behavior and the demanded new provider capability are held fixed?

Two programs use the same old run interface `Port`, mutable implementation `Fast`, and an old but possibly **protected** implementation `Legacy`:
- `Fast.Run() == 7`, `Legacy.Run() == 9`; both implement original `Port {Run() int}` and named old-client test `Old(Port)`. The old client and `Legacy` code cannot be edited in the protected-owner condition.
- New user demand: expose `Next() int` returning 42 **on Fast**, while every protected old client still accepts `Legacy`.
- Exactly two independent SOURCE edit operations are permitted: **T** publishes the additional API contract; **M** adds the concrete `Fast.Next()` method.
- **Coupled** design redefines the *existing* `Port` interface by adding `Next()`. **Segregated** design retains `Port` unchanged, and instead defines `Advanced interface {Port; Next() int}`.
- Explicit future capability acceptance is checked in the **final** revision, and in every old-client eligible revision `go test -count=1 ./...` must pass. A new `Advanced` declaration alone does not assert that `Fast` already implements it before edit M.

**These are programmatically generated, compilable synthetic Go source projects.** The tests are real Go compiler/test executions, but protected owner rights are controlled assumptions and the cases are not original external Go repositories. No real maintainer authorization, ecosystem prevalence, prospective hidden-label win or independent novel law is inferred.

## P1-B. Actual 16-revision compilation matrix

[Runnable Go compiler harness](../../tools/p40-p1/go_interface_source_repair_court.py) builds two different architectures × protected/not protected old `Legacy` obligation × all four subsets of T and M. Go test invokes actual Go compiler and checks old client outputs at every type-correct stage. Final states also assert new provider interface satisfaction and that `Next()==42`.

| Architecture | Protected Legacy | 00 | T-only 10 | M-only 01 | T+M 11 | Authorized safe repair paths to full demand |
| --- | --- | --- | --- | --- | --- | ---: |
| Coupled Port expansion | no | PASS | FAIL | PASS | PASS | 1 |
| Coupled Port expansion | yes | PASS | FAIL | PASS | FAIL | 0 |
| Split Advanced capability | no | PASS | PASS | PASS | PASS | 2 |
| Split Advanced capability | yes | PASS | PASS | PASS | PASS | 2 |

The three expected Go type-check failures occur precisely because `Fast` lacks `Next()` in T-only coupled programs (two protection conditions), or `Legacy` lacks `Next()` at the protected coupled T+M endpoint (one condition). These are purposeful **negative-controls**, not CI tool failures. All accepted revisions preserve the declared old-client runtime outputs. The protected `Legacy` condition includes a compile-time `var _ Port = Legacy{}` old-client type obligation.

**LOCAL reproducibility:** Independent local Python generation + Go 1.23.2 `go test` ran all 16 states, matching matrix, 3 deliberately invalid revisions. The checked-in harness encodes the same model. Until an Actions run is actually read back, no GitHub hosted CI success should be claimed for the checked-in version.

## P1-C. Exact bounded compositional theorem (classical)

Let `I` be the set of source revisions that compile and preserve all named old clients. Let edit T add the new API requirement and edit M add Fast's implementation; both one-shot source modifications are authorized by `Γ`. The **safe source path** must stay in I, with terminal state (T=1,M=1) additionally satisfying the future demand.

For an arbitrary guarded product of two **fixed local edit sequences** `A_0→...→A_p` and `B_0→...→B_q`, let `C(i,j)` denote joint source compatibility and old-client invariant at every intermediate product state. Let `u(i,j)`, `v(i,j)` be owner/legal guards permitting local A/B edges. Then the exact reachability recurrence is

[
R_{0,0}=C(0,0),quad
R_{i,j}=C(i,j)land
((i>0land R_{i-1,j}land u(i,j))lor
(j>0land R_{i,j-1}land v(i,j))),
]
with out-of-range predecessors false and initial state handled separately. All paths are monotone right/up grid paths.

**Proof**: Last edit of any legal path to (i,j) must be on the A or B axis; all earlier states safe by induction. Conversely, appending the corresponding authorized legal edit to an existing safe path yields a safe path to (i,j). Computational effort O(pq) once the local states and invariant/owner guards can be evaluated; evaluating arbitrary real Go builds may dominate. This is textbook guarded product reachability/dynamic programming, not novel mathematics. When the global invariant is rectangular and all owner edge guards independent, every shuffle of safe local paths is safe; when it couples source regions, local endpoint-validity does not imply a safe shuffle.

**P40 two-edit specialization:** If both endpoints safe, `countPaths = 1_{C(1,0)} + 1_{C(0,1)}` (provided respective owner edges permitted). The minimum number of internal safe-state removals needed to eliminate all existing endpoint paths is exactly this count in this 2×2 grid, by directed Menger/vertex-disjoint internal paths. Hence the actual source matrix gives `κ=0,1,2` in the cases above. If endpoint invalid, `May=0` and set `κ=0` by the declared convention; not a universal robustness metric.

## P1-D. Exact conditional architecture outcome, not an unconditional ranking

**Method-set consequence:** Go types implement basic interfaces iff all interface methods belong to their method set. A protected old `Legacy` implementing only `Run` is removed from the implementer type set when `Port` is widened with `Next`. Under the specified edit grammar (modify only `Port`, `Fast` and a fresh `Advanced` declaration), `Legacy` can never be repaired by any permitted edit. Thus the coupled architecture has no terminal safe path under the protected old-client contract. The segregated `Advanced` capability leaves original `Port` unchanged; after T and M the new interface is supported by `Fast`, while protected `Legacy` still supports `Port`. Both source-edit orders are accepted by the Go compiler.

**Context-dependent reversal claim is LIMITED:** without the protected implementer, coupled architecture can reach the new demand (though only with method-first order). It is ungrounded to infer that split has lower actual engineering cost or better runtime across ecosystems; type-check pass and number of legal two-step edit orders do not price code complexity, readability, API proliferation or deployment. This supports **conditional structural effect** rather than a universal "ISP/OCP always better" claim.

**Hard caveat:** A coupled system may use adapters, simultaneous atomic edits, a different edit grammar or compatible versioning, restoring paths. These are alternative mechanisms that the two-edit Γ currently excludes. This must be tested in P2 as strong classical architectural rivals, not quietly dismissed.

## P1-E. Competing prior art

- [Go Language Specification: interface type sets, method sets, embedding](https://go.dev/ref/spec): the type-checking difference is a directly expected consequence, not a new language theorem.
- Classic Interface Segregation / Open-Closed and extension interfaces; the model is a **formal conditional specialization** of existing design wisdom.
- Classical guarded product automata, finite-model reachability, compiler type checking and directed Menger connectivity: all account for bounded combinatorics.
- Original [Liskov–Wing 1994 behavioral subtyping](https://drive.google.com/file/d/1g7ruRxKmmki7ts6fQ09MIOwuYPCeCVvl/view): old runtime histories have their own pre/post/invariant semantics; source-edit histories are separate and may carry owner/compatibility guards.
- Source-realizable owner rights and future demand origin remain obligations before extending the result beyond this generated Go microcase.

## P1-F. Next actual theory gate

Construct two **equally capable** and prospectively comparable alternative architectures under the SAME closed-client and future-contract grammar: versioned adapters, wrappers, and interface extension. Model the precise authorized edit set and atomicity, compile all intermediate source variants, then seek a genuinely architectural condition under which relative repair **reachability, cost or option diversity** changes sign. Strong classical rivals must be implemented under identical evidence and resource budgets, not treated as strawmen.

**Status:** P40 OPEN · P1 GO-SOURCE MICROCASE LOCAL PASSED · GUARD-PRODUCT CLASSICAL · NEW-LAW IDENTIFICATION HOLD · LAW-R2 NOT_AUTHORIZED.

## P1-G. Verified hosted Go compiler receipt

[GitHub Actions run #38040317493](https://github.com/WhoSia/EvoNOMOS/actions/runs/38040317493) **SUCCESS** for checker/workflow HEAD `ace386fe5d30a6c32123957facb29e0469a54f4d`, job `go-source-court` and step compiling all sixteen source states **SUCCESS**. Artifact `11664774807` SHA256 `727bf0ef2012c436ba47b60a6dc06b23ed6502bdd5c32a930dbe15adb8549dec`. Python harness invokes actual `go test -count=1 ./...` with `GOPROXY=off`, no third-party deps. Expected 3 compiler negatives were asserted as part of successful court. **This is an ACTUAL Go source compilation**, unlike P39's synthetic edit-order tests, but does not assert any independent maintainer approval or natural external Go corpus result. Later Markdown/source changes are not part of this tested HEAD.

[P40 P2 endpoint-vs-intermediate safety and atomic patch model](P40_P2_ENDPOINT_SEQUENCE_OBSTRUCTION_AND_ATOMIC_SOURCE_EDIT_COURT.md) distinguishes a truly invalid terminal source from a valid terminal whose safe sequential path is blocked by owner/compile guards. Both remain classical finite-state reachability and Go type-set effects; new architecture-law identification HOLD.
