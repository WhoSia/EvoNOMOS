# EvoNOMOS — Structural Law Paper A and Real Go Repair-Order Competition (MATH-3 planning seal)

**As of 2026-10-09:** REAL GO experimental gate planned; result **NOT YET OBSERVED**. No novel beyond-SOLID law claimed. Parent P35 OPEN, LAW-R2 NOT_AUTHORIZED.

## Research question

For the same original Go component with architectures LIVE and SNAPSHOT and two independent demand contracts D9 (repeat physical headers) and D10 (unquoted comma tokens), how do changes in **demand order**, choice among at least two valid repairs, and architectural representation affect the observed set of *admissible source outcomes*?

Formal intended object:

```
R_d(A) := { B | B is reachable from original Go source A by a permitted
                   actual source change AND satisfies fixed demand oracle d }
R_D9 ; R_D10   versus   R_D10 ; R_D9
```

Repair operators are **relations** of permitted software edits rather than functions. A successful source witness establishes `R_d(A)≠∅` but never enumerates the entire `R_d(A)`, fixes a unique optimal patch, or licenses `∀B∈R_d(A)` assertions. Identical oracle for both paths is required, but a binary Git merge conflict **is not a mathematical noncommutation theorem**.

## Already native-verified without misreporting order

P35-MATH-2 [Go four valid patch witnesses and Lean relation court](P35_MATH_2_SET_VALUED_REPAIR_AND_NATIVE_GO_VERDICT.md), original Go Actions #37920470010, separate 2,880-case independent reference model Actions #37925137057, both PASS. These show 2 source organizations (LIVE/SNAPSHOT) × 2 code repair styles (INLINE/HELPER) can satisfy D9 and D10, while original D9-only and D10-only source snapshots exist. **They do not establish the real paths (D9→D10) and (D10→D9).**

## Exact new order-of-edit gate

Original base Go: go-chi/chi `v5.1.0` immutable SHA `67be7d9cafdaeb4e04e887ff78d09e030ee43b00`. For each of four family combinations `LIVE/SNAPSHOT × INLINE/HELPER` freeze source bytes for D8 base, isolated D9-only repair, isolated D10-only repair, and an independently accepted D9∧D10 source. Select two orders.

**Phase O1 (source-operator interference only):** derive the single-demand textual hunks **only from D8→D9 and D8→D10** before evaluating merge success. On exact isolated D9 and D10 sources, try deterministic three-way integrations `merge(D9,D8,D10)` and `merge(D10,D8,D9)`; retain raw conflict diagnostics. If merge fails, mark `PATCH_REPLAY_CONFLICT/HOLD`, never replace with the already verified BOTH file or declare functional noncommutation. If merge cleanly succeeds, compile and run frozen D0/D8/D9/D10 oracle and original Go module/race tests separately. A clean merge is a concrete source witness, not a universal property of all semantic repair relations.

**Phase O2 (real admissible-path completion):** when a source merge fails or behavior differs, take each first-demand snapshot and independently implement the *second requirement*, preserving all earlier requirements. Commit the actual second edits, old/new Go AST changes and executable tests. Do **not** select the alternative by downstream ease or silently copy the canonical BOTH file. Record failures and at least one valid path for both orders if possible. Compare **sets of observed witnesses**, not asserted exhaustive `R` relations.

**Phase O3 (theory discrimination):** freeze a hypothesis about order/patch-alternative interaction that is not implied by syntactic patch overlap, ordinary caching or existing modularity prior art; new source and history-rich repository mandatory. If same-oracle endpoint behavior ties but structural consequences differ under **new later demand D11 presealed upfront**, that could suggest a genuinely informative moderator. D11 cannot be invented after observing order outcomes and called prospective.

## Why structure is more than a file count

Candidate mechanisms to investigate WITHOUT assuming they survive:
- **latent representation lock-in:** a first valid repair may narrow future patches by binding later decisions to a data representation even when early observable behavior agrees;
- **repair-option survival:** distinct patch families may collapse or branch under subsequent requirements, without assuming scalar effort;
- **order-sensitive semantic affordance:** same input/observable contract at each prefix can allow different policy/reconfiguration capabilities, affecting future admissible behaviors;
- **substitutability versus architecture preference:** contract preservation (LSP-like) may remain valid even if change adaptation (OCP/ISP/DIP-like) differs. Do not collapse them into one "SOLID compliance score."

These mechanisms are hypotheses; vanilla process algebra, refinement calculus, rewrite critical pairs, Church–Rosser/term rewriting, configuration spaces and program-repair search remain strong explanatory rivals. No claim of a new theorem until a condition produces prospective discriminating predictions on real code.

## Paper A synopsis (working English abstract — not submitted)

*"Software design principles such as SOLID are often discussed without a clear account of the future changes under which one implementation should be preferred to another. We model permissible maintenance as a set-valued relation rather than a unique edit function, and distinguish observable functional equivalence from preservation of future repair alternatives. In an original Go HTTP routing codebase, four independently organized patches already pass a frozen repeated-header and token contract, demonstrating nonuniqueness of admissible implementations within the explored grammar. We propose to study whether the order of matched future demands changes which valid implementations remain reachable, using explicit two-stage source edits, original module regressions, bounded independent reference models and formal Lean/Prolog countermodels. These experiments can reveal when existing principles have conditional relevance, but no universal design superiority is presupposed."*

**Publication evidence floor:** do not claim two actual real source order paths until both compiled/Go-tested; add independent genuine source cohort, coding-method rival baselines, and honest negative/neutral results. No falsely 'axiomatic' mathematics: use Lean as checker and Go for actual mechanism.
