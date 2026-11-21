# EvoNOMOS — First Executed Source-to-Repair Cone, P35-P7 LIVE and SNAPSHOT

**2026-11-11 KST · TEN ORIGINAL GO SOURCE ACTIONS EXECUTED · 6/10 FINITE TEST-ACCEPTED · COMPLETE SOURCE REPAIR LAW NOT PROVEN · LAW-R2 HOLD**

## 1. Why this is different, and why it remains a narrow calibration

Previous P44 "decision-sufficient boundary" mathematical prototypes were fed hand-authored per-state loss tables, optimizer sets and authority relations. The present trial inputs real, independently maintained **go-chi/chi v5.1.0** source, its original Go test suites and *two already-pre-existing genuine architecture variant source files* from 2026-10-09 P35-P7. It executes pre-enumerated actual Go source edits, not merely naming graph arcs.

The customer demand comes from actual externally filed [go-chi/chi #1247](https://github.com/go-chi/chi/issues/1247). However, earlier EvoNOMOS P44 work already saw the issue and its known classical solution, so **this is not prospectively blind future-change forecasting, nor an independent maintainer experiment**. The two underlying architecture source alternatives originally predate the issue, but the five maintenance operators were selected afterward.

Original protected pre-issue source: LIVE blob \`ad9a2fbc0a30a39475f746068e74e2d3e6c93999\`, SNAPSHOT blob \`e9ca2c3863d5aa06ef0f0b9d168ddcf184713d75\`, both substituted into identical upstream original Go Git commit \`67be7d9cafdaeb4e04e887ff78d09e030ee43b00\`. No upstream source code was written to public Go Chi.

## 2. Frozen bounded repair grammar and exact execution

[Pre-execution contract](00_BOUNDED_SOURCE_REPAIR_PREEXECUTION.md) froze exactly five operations for **each** of the two source arms. [Source mutation script](mutate.py) applies only guarded existing-source expressions; [Go-native trial executor](run_original_source.py) copies each prior architecture back in before every candidate, runs old P35 D0/mode, old additional #1247 client regression, and new #1247 customer contract **separately**. Only when all named tests pass does it run native whole-upstream \`go test -count=1 ./...\` and \`go vet ./...\`. The finite grammar is intentionally not exhaustive.

| Action | Source change | Source edit sites | LIVE all named old/new + upstream+vet | SNAPSHOT all named old/new + upstream+vet |
|---|---|---:|---|---|
| \`none\` | no change | 0 | **FAIL** new issue | **FAIL** new issue |
| \`constructor\` | normalize pattern once in \`NewPattern\` | 1 | **PASS** | **PASS** |
| \`route_both\` | normalize the two registration call sites \`Route\`, \`RouteAny\` | 2 | **PASS** | **PASS** |
| \`remove_lookup_lower\` | remove request value lowercase normalization | 1 | **FAIL** old+new issue contracts | **FAIL** old+new issue contracts |
| \`match_lower\` | normalize stored \`Pattern.prefix/suffix\` before compare | 1 | **PASS** | **PASS** |

Actual source execution receipt: [final GitHub Actions #42929787723 **SUCCESS**](https://github.com/WhoSia/EvoNOMOS/actions/runs/42929787723), 10 explicit named \`SOURCE_REPAIR\` rows independently read from full job logs, with each accepted candidate requiring whole upstream Go suite and vet. Signed/uploaded experiment artifact named \`p44-original-source-finite-repair-grammar\` (artifact ID **13815104114**, SHA-256 digest **6f90cb78fd76adada0fcf55f9037b8e40077b9c4149c9beab97160f27d9d3555**) contains all per-candidate stage outcomes and failure output. It was produced by GitHub Actions without a bot-authored repository commit.

The program reports **both source arms**:
\[
\mathcal P_{\rm LIVE}=\mathcal P_{\rm SNAPSHOT}
=\{\texttt{constructor},\texttt{route\_both},\texttt{match\_lower}\}
\]
for the exact declared five-operator grammar and specified executable test oracle. All 3 valid remedies in each arm have one modified existing production Go file \`middleware/route_headers.go\`; candidate syntax sites have 1,2,1 touched locations. Thus \`constructor\` and \`match_lower\` tie on *minimal site count 1*; **this is NOT equivalent to equal maintainer time, lifetime cost, or guaranteed full semantic equivalence**. The source code for all three repairs might diverge on other direct callers or future requirements not in this fixed test oracle.

**Necessary counterexample:** removing request-side lowercase may seem a plausible way to satisfy an exact mixed-case match. In actual source tests it fails both old and new customer cases. This is why a context-free syntactic heuristic is not an actionability certificate.

## 3. Preserve both failed CI protocols and their exact reason

Two historical incomplete evaluations, [#42929285626 FAILED](https://github.com/WhoSia/EvoNOMOS/actions/runs/42929285626) and [#42929560562 FAILED](https://github.com/WhoSia/EvoNOMOS/actions/runs/42929560562), reached the eighth SOURCE_REPAIR row. Both aborted when the research-owned mutation script, originally matching unqualified \`r.Header.Get(header)\`, encountered the actual SNAPSHOT expression \`r.Header.Get(group.header)\` and raised \`ValueError: unexpected request sites 0\`. This was a **source grammar applicability / parser bug**, not a GO customer-contract mismatch or architecture performance deficit. The single change in commit [\`77fe874e\`](https://github.com/WhoSia/EvoNOMOS/commit/77fe874ebdfecde0c307d17677f8819fd0f27def) supports qualified original field expressions; no predeclared operation, customer fixture or old source was edited. A full clean rerun evaluated all 10. Earlier failures remain public and count as harness-debug history.

## 4. From actual source execution to conservative conflict theory

Let the **true semantically correct** authorized repairs in the limited grammar be \(\mathcal T(A,d;\mathcal E,\Gamma)\) and the **native suite passing** candidates be \(\mathcal P(A,d;\mathcal E)\). Under faithful deterministic tests as *necessary* contract checks and an independently authenticated edit-right set \(\mathcal E_\Gamma\), the elementary overapproximation is

\[
\mathcal T(A,d;\mathcal E,\Gamma)\subseteq
\mathcal P(A,d;\mathcal E)\cap\mathcal E_\Gamma .
\]

If for a set of observationally collapsed future demands the intersection of the **overapproximate** accepted sets is EMPTY, the intersection of true common repairs in that bounded grammar is also EMPTY. This is a sound **negative** conflict certificate *conditional on valid necessary tests*, not a correctness proof for passing repairs. The converse fails. The [separate formal note](01_FINITE_SOURCE_REPAIR_CONE_AND_SOUND_NEGATIVE_CONFLICT.md) gives the explicit qualifications.

At present, for the same fixed known demand in both prior architectures, the observed accepted grammar action intersection is **not empty** and indeed identical 3-operation sets. Therefore this original source witness does **NOT** produce a cross-architecture no-common-action conflict or an architecture-effect sign reversal. Do not manufacture one by inventing future demands or changing semantics after seeing the repair outcomes.

The earlier P44 finite optimizer hypergraph accepted completely specified \(\operatorname{Opt}\) and L matrices. This experiment yields something strictly different: **observable repair *eligibility* within a source grammar from actual tests, without a total cost order**. We cannot plug \(\mathcal P\) into \(\operatorname{Opt}\) as if every passing patch were fully correct and cost-optimal. A sound may/must abstraction, verified test oracle and externally measured effort are still missing. Standard enumerative program repair and test-based automated repair already do analogous search; priority novelty is NOT proven.

## 5. Consequences for SOLID-superordinate structural theory

LIVE/SNAPSHOT differ genuinely in registry observation timing, but both call identical shared \`NewPattern\` matching machinery, now verified by prior Go AST. The complete 10-run trial reinforces an ordinary change-impact explanation: a demand targeting shared pattern normalization yields the same locally viable repair site options across both structures.

This is a valuable **null control** against the mistaken premise that every deliberate architectural variation must change maintenance outcomes. It also illustrates that code factorization may multiply or concentrate repair locations (\`constructor\` single site versus \`route\_both\` two call sites), but no measured future requirements or developer effort establishes which should be preferred.

The potentially novel scientific target is now more tightly specified: calculate sound **source-extracted repair opportunity envelopes** from old-client contracts and authorized change grammars, obtain small conflict witnesses under partial observability, and show that these predict a conditional architecture selection frontier on truly independent future maintenance demands beyond equally informed program repair / Parnas / change impact / DSM. At least one nontrivial source/semantics theorem or strong verified new prediction is needed before LAW promotion.

## 6. Decision

**Keep:** exact pinned source, complete 10-action source experiment, both failed harness records, 3×2 accepted repairs, negative no-difference structural control, sound negative-cone logical inclusion.

**Do not claim:** new generalized SOLID law, true optimality of constructor patch, complete program verification, owner rights, actual independent agents, measurement of human labor, independently unknown future change or valid significance across two arms.

**Next high-value research step:** add a genuine source-derived behavioral abstraction of the \`Pattern\` + \`HeaderRouter\` change interface that can *certify* preservation of a declared bounded contract for all strings within explicit formal language/length constraints, and test may vs must cases **independently of this already-known issue**. If full symbolic execution is unjustified, constrain to the actual scanner's finite alphabet/grammar and prove bounds; do not generalize to arbitrary Go programs.

**P44 G1–G7 OPEN · LAW-R2 HOLD.**
