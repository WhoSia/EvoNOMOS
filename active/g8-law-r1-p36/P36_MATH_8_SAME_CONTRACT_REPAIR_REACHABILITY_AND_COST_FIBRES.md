# P36-MATH-8 — Same-Contract Repair Fibres, Source-Authority Transitions & Cost-Conditional Dominance

**2026-10-10 KST · P36 OPEN / P35 CLOSED. Original Chi/Gorilla O10 Q21 contract and source treatments committed BEFORE this mathematics. Native outcome and cost numbers are intentionally not presumed here.**

## Why this is a necessary methodological pivot after O9

O9's reciprocal preference between original Chi CORE trie and Gorilla CORE ordered route list was on **two incompatible client contracts** Q19 specificity and Q20 chronology, so could not identify an architecture ranking under fixed behavior. In O10, define **one identical client contract** `Q21`: explicit policy argument chooses specificity or chronology, both histories PS/SP and paths GET /members/me, /members/42, /outside. Both original upstream packages are unchanged; a project-authored one-file opt-in adapter is added to each original module, never represented as a naturally evolved upstream maintainer repair.

## Source-state, contracts and edit-authority fibres

For source `A`, source authority / admissible edit grammar `Γ`, explicit client contract `Q`, observation `O`, environment `c`, define
```
F(A;Γ,Q,c) := { B : A --Γ--> B ∧ Q(O(B,c)) passes }.
```
`F != ∅` means **at least one source repair witness**. It says nothing about unique patch, globally minimal diff, robustness beyond Q, all legal clients, or a universal notion of 'architectural advantage'.

Three authority regimes:
- `Γ_0 = {identity}`: no source edits. Old CORE original implementations do not offer the exact new selectable `P36O10... ` API, so Q21 as stated is not met.
- `Γ_add`: exactly one additive original-module Go source file, zero modifications to old upstream source, configuration before publication, new opt-in name allowed. A positive original source witness makes `F(A;Γ_add,Q21,c)≠∅`.
- `Γ_legacy`: retrofit **existing** public APIs and all third-party callers without migration or altered observable behavior. An additive API alone **does not** establish reachability in this regime. Caller opt-in is an explicit migration burden, not a claim of automatic compatibility of new behavior.

If one class of permitted edits is truly a subset of another (`Γ_0⊆Γ_add` with identical safety/acceptance) then source-repair reachability is monotone in authority: `F(A;Γ_0,Q) ⊆ F(A;Γ_add,Q)`. Trivial set inclusion, not a new general theorem. Resource budgets, API change restrictions and test evidence must be included when comparing Γ.

## Relational invariant surface

Both Q21 adapters must preserve:
1. **client-selected dispatch policy**: under policy STATIC precedence is independent of registration history, under CHRONOLOGY it is history dependent;
2. **Q0 guard**: generic-only path always PARAM and outside always 404;
3. **registration immutability**: after Handler publication, future Register refuses, dispatch is race-free under concurrent requests;
4. **legacy noninterference**: original `chi.NewRouter` or `mux.NewRouter` source and public behavior remain unchanged.

These are tested Q-boundary properties. A broad claim that source repairs are equivalent as machines requires a much richer input alphabet and context. In particular, middleware, param extraction, method mismatch/HEAD/OPTIONS, subrouters, and registrations after publication remain **outside** the frozen grammar.

## Cost: a partial order on compatible Q-successful source witnesses

For `B∈F` and fixed context c and workload w, record vector
```
C(B;c,w) = (latency_per_dispatch, B_per_dispatch, allocs_per_dispatch,
             build_latency, B_per_build, allocs_per_build,
             migration_cost, source-change_scope, long-run-ownership cost).
```
Only measured entries are numerical. This may be compared by vector Pareto dominance; no unexplained weighted scalar quality. If A fails Q21 and B passes, A's fast service on the failing semantics is not a **valid** Q21 performance competitor.

Distinguish:
- within-code policy comparisons (same original library, same CI runner);
- cross-original-module same-Q comparisons (same CI runner and Go version, source-adapter overhead included);
- broader hardware / version / migration transport (not established by one host).
Building mini Chi core routers per route vs sorting before Gorilla's single core Router is **a confound by explicit research-authored adaptation strategy**. A speed difference would be evidence for these two *witness repairs*, not necessarily for all possible Chi vs Gorilla repairs, nor a causal penalty imposed by the original architecture alone.

## Strong classical rival — still unbeaten

Data abstraction, conditional refactoring, routing trie/list precedence, code cloning/adapter patterns, finite-state continuation and algorithmic amortized analysis already predict the possibility of explicit semantic policy support through extensions. A stronger law H* would have to yield **a prospectively different, calibrated prediction** against this source-aware classical baseline for an independent future source change under the same Q and Γ. Unspecified 'SOLID should win' is **not a real rival**.

A valuable negative result is: `F(Chi;Γ_add,Q21,c)` and `F(Gorilla;Γ_add,Q21,c)` both populated; conditional cost vectors differ, but no uniquely identified new law follows. Preserve both successful and failing tests with raw CI artifacts and receipts.

**Verdict before native readback:** `SAME_CONTRACT_AND_ALLOWED_SOURCE_GRAMMAR_DEFINED__REPAIR_EXISTENCE_AND_COST_NATIVE_PENDING__DIP49_NEW_LAW_IDENTIFICATION_HOLD__LAW_R2_NOT_AUTHORIZED`.
