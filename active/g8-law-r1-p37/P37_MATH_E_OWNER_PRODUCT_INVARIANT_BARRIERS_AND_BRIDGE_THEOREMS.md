# P37-MATH-E — Invariant Barriers in Multi-Owner Repair Products: Safe Interleavings, Bridge States and Atomic Authority

**2026-10-10 KST · prospective mathematics, before real gorilla/sessions + securecookie source test. P37 OPEN.**

## Why this is structurally different from P37-MATH-D

MATH-D studied unavailable historical information: two source histories collapse to the same accessible state. Here **no information needs to be lost**. Both modules know the target version and can separately change. Nevertheless an **invariant preserving path may not exist** when only one owner can edit at a time. The joint repair relation is a constrained product graph with a compatibility predicate that **is not separable** into local module predicates.

Let owners A (producer/issuer) and B (consumer/reader) have typed local edit graphs G_A, G_B. Composite state (a,b) in S_A×S_B has invariant I(a,b)∈{false,true}; legal sequential Γ edits change **exactly one owner coordinate** per step and must keep I true at every checkpoint. Local repair May_A and May_B do NOT generally imply May_composite.

## Theorem E1 — Exact binary square obstruction

Each owner has state 0 and 1, with exactly one allowed monotone local edit 0→1. The composite initially (0,0), target (1,1). Assume both endpoints satisfy I.

Then:
```
May_sequential((0,0),(1,1),I)
  ⇔ I(1,0) OR I(0,1).
```
Proof: exactly two monotone 2-step interleavings exist, via (1,0) or (0,1), and an admissible path exists precisely when at least one intermediate satisfies I. This is a finite directed product graph fact (not new mathematics).

If both mixed states violate I, both owners have feasible **local** modifications but no safe sequential global modification. The global reachability predicate does not factor into `May_A ∧ May_B`.

**Three fundamentally different Γs**:
1. `Γ_seq` only one-owner edits, no mixed-valid state ⇒ no path;
2. `Γ_atomic` additionally authorizes direct jointly approved (0,0)→(1,1) (no intermediate checkpoint) ⇒ path, but actual coordinated deployment privilege is necessary;
3. `Γ_bridge` adds a compatibility state B* (reader understands versions 0 and 1) and edits B0→B*, A0→A1, B*→B1. Then `(0,B0)→(0,B*)→(1,B*)→(1,B1)` is a safe staged path *iff* I holds in every intermediate. If the original invariant additionally requires reading **old persisted content throughout** the window, the final B1 might still violate I even after bridge; then terminate at B*, wait for a certified expiry, or change the invariant/requirements explicitly. Never silently discard the historical demand.

## E2 — A sufficient bridge lemma

If the edges `b0→b*`, `a0→a1`, `b*→b1` exist in authorized owner graphs, and
```
I(a0,b0), I(a0,b*), I(a1,b*), I(a1,b1)
```
all hold, then the three-stage path is I-safe. If the final invariant is strengthened to require old historical payload acceptance and B1 rejects old payloads, the fourth premise is false. Therefore B* is a **conditional** path witness, never an unconditional cure.

The minimal number of bridge states is a graph search quantity relative to a fixed state grammar, I and Γ. An unrestricted compiler-generated bridge makes the number trivially small; a strict edit/ownership grammar can make it infinite. We cannot claim invariant barrier is a software-specific theorem beyond classical graph reachability, assume-guarantee or expand-and-contract migration.

## E3 — Comparison with SOLID

A and B can be perfectly separated by ports (DIP/ISP), each with one change owner (SRP), with behaviorally substitutable implementations (LSP) and extension-only changes (OCP) in some declared scopes, **yet I(1,0)=I(0,1)=false** and no sequential safe migration exists. Source-interface style alone does not imply temporal edit schedule feasibility.

Conversely a bridge state can exist in a concrete-coupled architecture that violates a chosen static DIP predicate. This is neither anti-SOLID advocacy nor evidence that the strong classical theory of rolling upgrades failed.

## First independent, naturally composed software target

Pinned original `gorilla/sessions@bb4cd60c952a9ce48ea0dc6cc7b282ff79c38263` **already imports** `gorilla/securecookie` via its actual original `CookieStore.New/Save`. The original `NewCookieStore` constructs codecs using `securecookie.CodecsFromPairs`. Original `securecookie.EncodeMulti` selects the first successful codec for writes; `DecodeMulti` tries codec alternatives for reads. This is real upstream inter-repo integration, **not newly authored two-owner glue**. The repos share the Gorilla ecosystem/organization, so independence is at the repository/module level, not independent social governance.

Next P37-E1 experiment freezes writer/reader deployment ownership, original source SHAs, keys supplied only as test fixtures, and a per-checkpoint ability to read emitted session cookie and old retained session cookie:
- writer owner A uses only old or new codec;
- reader owner B uses old-only, new-only, or dual-old/new codec;
- original states and mixed pair feasibility are tested directly using original session CookieStore and securecookie;
- terminal migration semantics require a declared old-cookie compatibility window, not merely new cookie acceptance.
No crypto strength/security recommendation is made based on this compatibility fixture.

## Strong classical competitor (not a straw rival)

Classical interface-compatibility/assume-guarantee, distributed deployment version skew and expand-contract directly predict the binary obstruction and dual-compatibility path. See USENIX SREcon 2026 *Escaping Version Skew: Formalizing Compatibility in a World of Partial Rollouts*, https://www.usenix.org/conference/srecon26americas/presentation/ostrow; this is a particularly close competitor, NOT a new EvoNOMOS discovery. A genuinely new-law claim would require a precommitted prediction not already explained by those models, proven over actual source dependency and authority constraints.

**Pre-experiment:** `P37_MATH_E1_EXACT_BINARY_GRAPH_CLASSICAL__E2_BRIDGE_CONDITIONAL__INDEPENDENT_NATURAL_INTEROP_GO_NATIVE_UNTESTED__DIP49_IDENTIFICATION_HOLD__LAW_R2_NOT_AUTHORIZED`.
