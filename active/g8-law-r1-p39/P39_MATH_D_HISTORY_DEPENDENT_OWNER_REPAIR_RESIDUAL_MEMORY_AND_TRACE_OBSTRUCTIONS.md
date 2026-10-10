# P39-MATH-D — History-Dependent Owner Repair and Exact Residual-State Memory

**2026-10-10 · Theory first · mathematical models only · strongest classical prior art undefeated · DIP49 HOLD / LAW-R2 NOT_AUTHORIZED.**

Source lineage: [Math-A](P39_MATH_A_LSP_REPAIR_LIFTING_AND_OWNER_HELLY_OBSTRUCTIONS.md) → [Math-B](P39_MATH_B_TYPED_SOLID_IMPLICATIONS_AND_CONDITIONAL_OCP_COROLLARY.md) → [Math-C](P39_MATH_C_MINIMUM_SOURCE_EDIT_CUTS_OWNER_PRECEDENCE_AND_ANTIMATROID_SURVIVAL.md). This stage removes the assumption that a set of applied source modifications is a sufficient future repair state.

## D0. Correct semantic contract

Let h be an authorized source-edit history, π(h) its currently installed physical source patches, and R_h the set of suffixes w for which the completed history hw constitutes a legal future repair. Current source equivalence π(h)=π(h') need NOT imply R_h=R_h'. The exact condition for lossless **future-language** prediction by π is that equality under π implies equality of the right residual languages. This is classical Myhill–Nerode right-congruence factorization, not a new theorem. If predictions only concern one existential demand instead of all suffix languages, a smaller quotient may suffice. Runtime histories under the original Liskov–Wing LSP are distinct from source-edit histories.

## D1. Minimal two-edit order witness

a,b are one-shot source edits that commute physically: π(ab)=π(ba)={a,b}. A declared synthetic owner policy permits a later source-extension edit q iff a preceded b. Thus abq is legal while baq is not. The source-only projection wrongly merges two distinguishable futures; at least one history/authority bit is needed for the declared q question. **No claim that real original Go repository permissions follow this synthetic rule.**

## D2. k independent owners: exact 2^k memory states in one source fiber

Take k independent source-edit pairs (a_i,b_i), i=1,...,k, all single-use. Every one of the (2k)! permutations installs the **same** final physical source. Owner i permits a future terminal extension edit q_i iff a_i precedes b_i. The rights signature is r_i(h)=1 iff a_i precedes b_i.

**Theorem D2.** At that single fully-applied source snapshot, precisely 2^k distinct residual future permissions exist, and any exact deterministic summary that must correctly answer each independently selectable q_i needs at least 2^k states, i.e. **k extra bits**. k bits suffice.

**Proof.** Any binary rights vector is realized by ordering each pair in the prescribed direction. Distinct vectors differ in some coordinate i; suffix q_i succeeds after one history and fails after the other. Therefore the 2^k residuals are pairwise distinct, and retaining those k bits exactly answers every q_i. Each profile has exactly (2k)! / 2^k source-edit permutations, by swapping members of each pair.

**Scope:** if only q_1 is queried, one bit suffices; if only “does any q succeed?” is queried, one aggregate bit suffices. The k-bit lower bound is task-family dependent and the synthetic rights policies are independent by hypothesis.

## D3. A sharp full-language minimum deterministic automaton

Let L_k contain precisely all words that apply each a_i,b_i exactly once in any order and then end in exactly one terminal q_j for which a_j came before b_j. No premature q or repeated source edit is accepted.

Each pair has five pre-approval states: 0 neither applied, 1 only a, 2 only b, 3 both with a before b, 4 both with b before a. There are 5^k pre-approval states, one accepting terminal and one rejecting sink.

**Theorem D3 (classical residual-state specialization):**
[
\operatorname{sc}(L_k)=5^k-2^k+2,qquad k\ge 1.
]

**Proof.** Exactly 2^k pre-approval states whose coordinates are all in {2,4} can never lead to a favorable q: merge them with the rejecting sink into one empty residual class. Every remaining pre-approval state has a successful completion. Two live states with different sets of applied edits have distinct residuals, because an accepting suffix for one must contain exactly its missing base edits, so it cannot finish the other. Two live states with the same installed edits but different completed-pair precedence differ on some q_i after finishing all remaining edits in the same order. One post-q accepting terminal has only the empty accepted suffix and gives an additional distinct class. Therefore (5^k−2^k) live pre-approval classes + one dead class + one accepting class is sharp.

[Independent Python automaton minimizer](../../tools/p39-math-d/history_residual_minimization.py) constructs all transitions, refines residual partitions to stability and additionally exhausts every (2k)! one-shot source-edit history. Results:

| k | Fully applied source histories | Future rights signatures at the same source | Exact minimal DFA states |
| --- | ---: | ---: | ---: |
| 1 | 2 | 2 | 5 |
| 2 | 24 | 4 | 23 |
| 3 | 720 | 8 | 119 |
| 4 | 40,320 | 16 | 611 |

**Do not conflate** k bits of extra memory *at the same finished source* with the number of states recognizing the **entire** language of partially applied patches.

## D4. Three classical rival attacks

**Myhill–Nerode and bisimulation:** the residual-language quotient is canonical, and a source-only relation merging ab with ba cannot be a full behavioral edit bisimulation because the future q edit is enabled after only one. The bound and full DFA result are classical residual-state arguments, not a new abstract minimization theory.

**Mazurkiewicz traces:** physical source transformations a_i and b_i commute, but the combined source+rights monitor does not have the I-diamond property (ab and ba lead to distinct q_i behavior). Trace independence must hold in the complete authorization/compatibility machine, not merely in the source projection. [*Theory of traces* (1988)](https://doi.org/10.1016/0304-3975(88)90051-5) is an earlier stronger theory.

**Unbounded obligations:** as a separate abstract policy, history-only events inc,dec adjust a nonnegative outstanding-obligation counter without changing physical source; approve is a final edit allowed iff the counter is zero. Histories inc^n have identical source snapshots yet suffix dec^n approve distinguishes inc^n from inc^m for every m≠n. By Myhill–Nerode, infinitely many right residuals exist: **no finite exact deterministic memory** for this stipulated unbounded monitor. A 100-pair n,m≤9 arithmetic sanity test passes. This is a classical one-counter nonregular-language example, NOT an empirical claim about maintainer practices.

## D5. Strong prior-art status and next gate

- [Myhill–Nerode residual-language/minimal states](https://doi.org/10.1016/j.jlamp.2018.03.002), directly checked published text; [register-automaton Myhill–Nerode extension (2022)](https://doi.org/10.1016/j.tcs.2022.01.015).
- [Classical trace theory (1988)](https://doi.org/10.1016/0304-3975(88)90051-5) and [I-diamond asynchronous automata](https://link.springer.com/chapter/10.1007/978-3-032-22730-0_19).
- [Bartoletti, Degano and Ferrari (2005), *History-Based Access Control with Local Policies*](https://doi.org/10.1007/978-3-540-31982-5_20). Relevant prior authorization theory, public abstract, not a claim of full original paper custody.
- User's Drive exact-title checks did **not** establish custody of full original Myhill–Nerode, Mazurkiewicz or history-based access-control papers. Source citations are public publications/abstracts, not assertions of full-paper reading.

**Scientific verdict:** exact 2^k final-source residual lower bound and sharp 5^k−2^k+2 full DFA construction are correct within this synthetic language but **classical Myhill–Nerode specialization**. Pure source edit commutation alone fails trace independence when owner-history rights are present. No original Go tests, no law discovery, no hosted P39 CI run claimed.

**Prospective P39-MATH-E problem (not opened):** seek a genuinely nontrivial source-realizable structural invariant or memory bound from verified owner/source interaction topology under equal classical comparison, instead of assuming an arbitrary rights automaton. Compare symbolic automata, product constructions, communication complexity and parameterized verification. P39 OPEN · DIP49 IDENTIFICATION HOLD · LAW-R2 NOT_AUTHORIZED.
