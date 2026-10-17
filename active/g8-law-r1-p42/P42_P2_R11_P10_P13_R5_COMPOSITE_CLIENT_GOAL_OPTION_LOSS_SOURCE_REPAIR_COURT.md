# EvoNOMOS G8 LAW-R1-P42 — R11-P10-P13-R5
# Prospective Composite-Client Repair Viability, Exact Finite Cost Frontiers, and Irreversible Option Loss in Original Chi

**MATHEMATICAL AND SOURCE-TEST HYPOTHESES SEALED BEFORE IMPLEMENTATION · 2026-10-18 KST · P42 RUNNING / P43 HOLD / LAW-R2 NOT_AUTHORIZED**

## 0. The open research gap, without pretending to reinvent R4

P13-Q verified the original pinned Chi one-shot seven-edit source language, 13,700 full words including empty / 3,588 legal / unique EF structural conflict, with 13,440 length-4..7 heldout original native verdicts. P13-R3 proved EXACTLY 96 minimal joint source-admission and **eight fixed real HTTP client output** classes over all 3,588 legal source edit histories. P13-R4 proved the standard EXACT minimum edit-count recurrence for **any** terminal goal predicate based on those same eight probes, and verified two new numeric-vs-alpha goals on original Chi. This R5 does NOT claim the recurrence or 96-class quotient are new. Instead it **prospectively specifies genuinely new Boolean-conjunctive customer goals**, tests every admissible pair of owned source states as a source-realizable future edit path, and investigates the logical boundary between immediate repair and preserving options for alternative as-yet-undisclosed goals. No new HTTP alphabet or maintained source edits are added. The 'unseen' character of the goals is only relative to the previous R4 goal set—not unseen third-party PRs.

## 1. Frozen source scope and mathematical assumptions

Pinned maintained upstream: go-chi/chi @ `167e1e3bd039d060696b99c8da4e876ae04f42c1`, unchanged. Source modifications consist *only* of app-owned, once-only fresh-child-router `Mount` registrations, exactly the seven letters and paths fixed in P13:
A=/svc/a; B=/svc/b; C=/branch/one; D=/branch/two; E=/svc/{num:[0-9]+}; F=/svc/{alpha:[a-z]+}; G=/svc/a/deep.

Let Q={A,B,C,D,G}, T⊆Q, and z∈{none,E,F}. There are 32×3=96 legal installation supports X=T∪{z} with none interpreted as empty. H is the **entire** source-certified one-shot edit language, no repeated label and never E/F together. Every intermediate step must preserve GET /old 200/body old/no Flush. Every added `Mount` costs exactly one **synthetic application edit unit** (not human hours). Allowed source repairs are **additions only**; no unmount/refactoring, no upstream maintainer permissions.

Fixed client observations previously certified P13-R3: GET /branch/one/item (expected 200/body C iff C installed), /branch/two/item (expected 200/body D iff D installed), /svc/123/item (200/body E iff E installed), /svc/abc/item (200/body F iff F installed), plus /old and no Flush. All four main goals below are new Boolean combinations of **the old eight frozen probes**. The source response predictions are themselves prospective hypotheses subject to falsification, despite previous R3's 3,588 response factorization result.

## 2. Four new prospective goals (frozen BEFORE native tests)

- **g_CD:** C AND D simultaneously present as 200/body C and 200/body D, no Flush.
- **g_EC:** numeric source route E 200/body E AND /svc/abc/item 404 AND branch C 200/body C, no Flush.
- **g_FD:** alpha source route F 200/body F AND /svc/123/item 404 AND branch D 200/body D, no Flush.
- **g_EF:** numeric source route E 200/body E AND alpha source route F 200/body F simultaneously, no Flush. This last goal is deliberately **infeasible** inside the fixed additive source edit grammar; no code deletion or new handler actions are allowed.

Notation: 1_{C∉T} denotes one missing action. Predictions for EVERY 96 X:
\[
V_{CD}(T,z)=1_{C\notin T}+1_{D\notin T}.
\]
\[
V_{EC}(T,z)=
\begin{cases}
+\infty & z=F\\
1_{C\notin T}+1_{z=none} & z\in\{none,E\}.
\end{cases}
\]
\[
V_{FD}(T,z)=
\begin{cases}
+\infty & z=E\\
1_{D\notin T}+1_{z=none} & z\in\{none,F\}.
\end{cases}
\]
\[
V_{EF}(T,z)=+\infty.
\]
The minimum for a goal at an already satisfying world is 0. The formula for 96-world exact repair costs in P13-R4 is a **classical** finite directed acyclic weighted reachability theorem, not re-proved as a priority claim.

## 3. R5 mathematical count and prospective source oracle: 1,215 distinct forward-reachable pairs

For each of five free Q bits, a legal pair X⊆Y has choices (0→0), (0→1), (1→1), hence 3^5. For the E/F mutually exclusive component, the admissible ordered pairs are (none→none), (none→E), (none→F), (E→E), (F→F), hence 5. Thus the **FROZEN prediction**:
\[
\#\{(X,Y):X,Y\in S,\ X\subseteq Y\}=3^5\cdot 5=1215.
\]
Every such pair admits a research-owned original Chi source-edit path of exact length |Y\X| after starting with X; **all** its intermediate prefixes are admissible and old-safe. The single runtime final source state Y must satisfy the eight-probe constraints in the selected goal or fail them honestly. This is a heldout **source transition and cost oracle**, not 1,215 distinct prior unknown maintained framework patches.

Proposed P13-R5 test must:
1. Build each of the 96 start worlds in the original maintained Chi with app-owned source routes, check stagewise old client.
2. Enumerate all 96 Y and only for X⊆Y perform a **fresh original-source build of X then a concrete source edit suffix Y\X** (not a fake abstract graph edge). Check exact number of added source edits, stagewise old GET, endpoint old GET, all four client probes.
3. Compute attained minimum *from actual Go outcome receipts* for all four goals for each initial X, not just search the already predicted closed-form formula.
4. Compare **384 exact forecast cells = 96 worlds × 4 goals**, with all ∞ values explicitly requiring exhaustive eligible Y negative evidence. Compare 1215 actual legal source paths, with failure logging before verdict. If either original code rejects any predicted legal path or effects/cost differ, **FAIL and preserve witness**.
5. Probe blocked E→F and F→E on original source for all 32 T in separate fresh worlds, recording negative controls. Such blocked attempts are not counted as legal repairs.
6. Keep both equal-information classical weighted guarded LTS and the EvoNOMOS interpretation tied; do not claim a winning ranking from a mere representation choice.

## 4. Conditional mathematical consequence for architecture options (classical viability/kernel reasoning)

Let \(g_E,g_F\) be the existing P13-R4 numeric and alphabetic client goals. At z=none, V_E=V_F=1: after new goal is disclosed, choose E or F at unit cost. Prematurely committing E changes the vector to (0,+∞), and prematurely committing F changes it to (+∞,0), **even though the source only grew by one legal edit**. Thus installation order/choice can destroy some **future** customer satisfiability even while preserving all previously protected clients and remaining source syntactic validity. If the future goal comes from \{g_E,g_F\} only after an unforced choice E/F, no committed E/F option guarantees finite repair for both; retaining the undecided none-world does. This is not a rational preference theorem without specifying probabilistic goal likelihood, deadline, resource/latency model, or costs for deferring a decision.

More generally, new-client goals of the form Boolean combinations of **frozen real-source observation coordinates** are in the language for which P13-R3 q=96 is complete. For an **unknown new HTTP path, new source edit label, old client that checks history, removal action, or owner authority change**, the R5 certificates do NOT license point predictions and must ABSTAIN or demand source refinement. Stronger classic source-aware guarded weighted LTS yields the same formal conclusion; it is a positive methodological result if its explanatory power is sufficient.

## 5. Source certificates and scientific disposition

Prospective labels are fixed here before introducing an R5 checker or new Go client test. Required certificates are source pinned hash, original owner-app change scope, real 1215 path receipts, 384 forecast cells, negative mutual-exclusion controls, preseal ancestor proof, and preservation of original P13 ancestry. G1–G7 full arbitrary Go source/effect equivalence and external unknown PR rankings remain OPEN. Never equate this with actual human engineering effort or unrestricted Go owner rights.

**R11-P10-P13-R5: QUESTION PRESEALED · NO RESULT CLAIM UNTIL ORIGINAL-SOURCE CI RUN COMPLETES · P42 RUNNING · P43 HOLD · LAW-R2 NOT_AUTHORIZED.**
