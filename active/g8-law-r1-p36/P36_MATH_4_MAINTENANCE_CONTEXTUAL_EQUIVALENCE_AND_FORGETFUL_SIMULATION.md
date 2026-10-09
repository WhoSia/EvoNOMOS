# P36-MATH-4 — Maintenance-Contextual Equivalence, Forgetful Simulation & the Boundary of Repair-Option Dominance

**2026-10-10 KST · P36 OPEN · P35 CLOSED (flowing stage).**

## Empirical impetus (native sources, not abstract toy test only)

Two independently evolved Go router substrates carry distinct publication costs in genuinely pinned upstream source:
- Original [Chi O6](https://github.com/WhoSia/EvoNOMOS/actions/runs/37951885323), follow-up isolated 32-baseline [Chi O1 #37954396262](https://github.com/WhoSia/EvoNOMOS/actions/runs/37954396262): frozen update/request semantics held, five repeated medians burst EAGER 79529 ns/op vs LAZY 62903; interleaved 80782 vs 83984, overlapping raw timing.
- Independent [Gorilla O2 original source #37958339620](https://github.com/WhoSia/EvoNOMOS/actions/runs/37958339620) **2/2 SUCCESS** (full original Go, vet, race and frozen 16U/16R semantics) and [same-runner two-order #37959460386](https://github.com/WhoSia/EvoNOMOS/actions/runs/37959460386) **2/2 SUCCESS**. Two CPU+order combinations have wildly different elapsed time but stable allocation fingerprints. On EPYC 9V45 EAGER-first same-runner median ns/op: burst EAGER 215501 / LAZY 79308; alternating EAGER 220930 / LAZY 242888. On EPYC 7763 LAZY-first: burst EAGER 380193 / LAZY 129513; alternating EAGER 377731 / LAZY 375193. **CPU generation and treatment order both changed**, hence cannot causally separate those effects. The alternate-case sign is not independently stable. Classical caching, route compilation cost and amortization are sufficient rivals.
- [Chi O3 actual future-option court #37961233537](https://github.com/WhoSia/EvoNOMOS/actions/runs/37961233537) **2/2 SUCCESS** under D14 real original Go full test/race/vet. Two D14 source repairs were frozen prospectively relative to independent later D15: RETAIN restores original registered handler in alpha and beta worlds and passes D15; ERASE fails D15 as expected with no retained original closure. **This is bounded source-visible future option survival** under `Γ_obs={RETAIN,ERASE}`; the failure was an expected scientific negative and was not hidden as a CI failure.

## Three fundamentally different equivalence relations

For development source-state S and a bounded observation/test oracle O_d:

(1) **Current runtime observational equivalence** `A ~_d B`: the frozen present functional histories yield equal O_d responses (and revisions) on the specified action alphabet.

(2) **Maintenance-option equivalence relative to permitted grammar Γ and future demand family E**: `A ≈_{Γ,E} B` iff for every e∈E the *sets of available repaired responses* (or separately existence/necessity of admissible repairs) coincide. This may be strictly finer than `~_d`. Only tested Γ and E; it is not a globally enumerable set of all real Go patches.

(3) **Cost/context equivalence** `A ≍_{Γ,E,c}B`: semantically admissible structures have the same conditional vector of startup/registration/dispatch/memory/GC/workload/race costs under fixed context c, not just scalar ‘better design’. Usually false even when (1) and (2) hold. Equality needs a declared quantitative tolerance, CI provenance and unit convention.

A transition structure for software development has **runtime labels** (HTTP requests/responses) and **development labels** (authorized Go source transformations respecting Γ, test changes, activation). Ordinary runtime bisimulation over the first alphabet does not guarantee bisimulation over the second alphabet. Treat this as a classical labelled-transition system, not a newly discovered category theory.

## Forgetful simulation (classical theorem, explicit nontrivial condition)

Let enriched state space R and erased state space E have a projection `π:R→E`. Let both support a shared alphabet of *permitted* actions `A`; let `δ_R:R×A→R` and `δ_E:E×A→E`. Suppose:
- **Step homomorphism:** for all r,a, `π(δ_R(r,a))=δ_E(π(r),a)`.
- **Observation commutation:** for all r, `O_R(r)=O_E(π(r))`.

Then for any finite trace w of actions from that shared alphabet:
```
π(run_R(r,w)) = run_E(π(r),w)
O_R(run_R(r,w)) = O_E(run_E(π(r),w)).
```
Proof by induction on w. **This does NOT follow merely from present tests `R~_dE`**. The homomorphism condition is the entire obligation. RETAIN restoring is a *strict extra ability only when D15 is added as a legal action to R but not simulatable by E*; which legal future edits are permitted changes the ordering.

**Research-wide prohibition:** it is invalid to invent a second future demand `D16` that requires ‘history has been erased all along’ and retroactively count RETAIN's D14 patch as incorrect simply to manufacture a symmetric reversal. If a retained system is permitted to discard information later, all functional behaviors available to ERASE may be simulated by RETAIN under Γ inclusive of forgetting. A real reversal requires an explicit **resource budget, latency/deletion deadline, observability authority, forbidden future edit, or lost external history** and must be measured or stated as a premise. This is classical simulation and information order (Blackwell-style), not an EvoNOMOS original theorem.

## A stronger scientific question suggested by the two actual Go worlds

Can we find an *independent genuine software change pair* where two representations are currently equivalent and preserve equal historical information, but **their real admissible repair graphs differ after one change** because of the topology of source edit permissions or coupled invariants—*while a preregistered strong classical modularity/program-slicing hypothesis predicts otherwise*?

We **cannot** claim we have identified such a split: existing O2 is classical caching, O3 is classical erased-information obstruction, MATH-1 is classical automata theory. This statement is a research-frontier question, not a measurement.

### Testable source law-candidate frontier, pre-results

Declare a fixed maintenance grammar Γ of real edit operations (budget, file ownership, runtime authority, middleware registration). Choose two representations carrying **equivalent restorable information** (to neutralize trivial erased-data confounding). Freeze two independent demands d and e, orders de and ed, their *prefix* correctness tests, repair sets and observation projection. Rivals:
- `B_information_only` predicts no future restore advantage from *amount of retained information*, since equal information is available in both. It makes no universal prediction about edit feasibility or cost under Γ.
- `B_classical_modularity` predicts effects of source boundaries only under separately declared coupling and repair-grammar assumptions, **not** from file-count or SOLID adherence alone.
- `H_repair-graph-topology` may predict a branch/option-survival distinction after prefix-correct d even when static information and observed function are equal, **provided a specific graph invariant and a non-overlapping classical-rival prediction are preregistered**.

At this point `σ_q(H)` vs `σ_q(B)` is **not separated**, as B allows both. Do not invent a sharp null straw man. Develop new independently testable constraints; do not upgrade from bounded simulation to a universal law.

## Empirical cost signatures requiring correct interpretation

On Gorilla original same-source O2 16U/16R burst, EAGER and LAZY have exactly 16 vs 1 post-baseline publications; allocation fingerprints in both paired runners are EAGER ~518194 B/op, LAZY 144120 B/op. Their *difference* ~374074 B/op is architecture/source-conditional, not per-build allocation rigorously attributed without instrumentation. Under alternation both ~517936 B/op, 4433 allocs/op. Chi analogous burst EAGER ~160014, LAZY ~107962; alternation ~159759 both. Allocation difference cannot be used as direct runtime performance predictor without GC and allocator context.

**Source authority**: all original-source runs above have archived SHA256 artifact ZIP receipts; see companion O2 and O3 receipt courts. Missing formal Lean `P36-O3` kernel verdict remains PENDING until original run [#37961481644](https://github.com/WhoSia/EvoNOMOS/actions/runs/37961481644) terminal readback. This new MATH-4 theorem must independently compile and check its proof; do not claim kernel-pass merely from written code.

**MATH-4 STATUS**: `CLASSICAL_SIMULATION_THEORY_SPECIFIED__REAL_GO_OPTION_NON-EQUIVALENCE_BOUNDED_PASS__SOURCE_GRAPH_GENUINE_DISCRIMINATION_OPEN__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.


## 2026-10-10 — Lean 4 checker receipt

The original [MATH-4 kernel workflow #37964349042](https://github.com/WhoSia/EvoNOMOS/actions/runs/37964349042) completed **SUCCESS**, single job, [P36Math4.lean](../../tools/p36-math4/lean/P36Math4.lean) proven without `sorry`/`admit`/`axiom`. The generic theorem requires a step-compatible projection and observation compatibility, then proves finite-trace compatibility by induction. It is classical, independent of whether our real Go source satisfies the premises. O6 supplies an explicit finite behavioral bridge on fixed traces, not a fully general refinement proof of Chi implementations.
