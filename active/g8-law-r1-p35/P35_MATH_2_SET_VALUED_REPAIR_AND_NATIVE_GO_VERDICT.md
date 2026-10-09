# P35-MATH-2 — Set-Valued Repairs, May/Must Logic and Four Real-Go Repair Witnesses

**2026-10-09. MATH-2 bounded scientific grade:** `MATH2_LEAN_KERNEL_PASS__REAL_GO_FOUR_REPAIR_WITNESSES_PASS__GO_PROLOG_COUNTERMODEL_PASS__CLASSICAL_THEORY_UNDEFEATED__P35_PARENT_OPEN__LAW_R2_NOT_AUTHORIZED`.

## Protected objective and recovered history

EvoNOMOS searches for genuinely novel *conditional mathematical laws of software structure and evolution*, tested on independently evolving Go software with equal semantic demands. **Do not** redefine the goal as responsibility boundaries, scalar economic repair cost, source-edit site predictions, or accumulating Lean lemmas.

Historical primary objects were already articulated on 2026-08-29–30, not first discovered in MATH-2: [DIP-49](https://app.notion.com/p/3ccef561cf92818484a4d55302715e84) froze prospective pair-separating symbolic law-queries and active learning stopping; [DIP-50](https://app.notion.com/p/3ccef561cf92811291b4c56437bc5b4b) demanded correct concrete query realization with pre-outcome context/prefix semantics, equal initial source, independent functional oracle, and output factoring; prior [14.md](https://drive.google.com/file/d/1TuweqOEc1KY14ddEJVoPbBJAiT-i3thP/view) already recognized the nondeterministic repair relation `R_d ⊆ A×A`. MATH-2 is an *actual-source contact* with parts of this machinery, **not** a new automata theorem.

## Actual pre-treatment chronology and independence

| Event | Human WhoSia commit | Binding |
| --- | --- | --- |
| Fix mathematical and original-source contract *before* Go patches | [`a8b5a67`](https://github.com/WhoSia/EvoNOMOS/commit/a8b5a67d1f976e3b447568fd58dd3b239892526e) | [Original MATH-2 protocol](P35_MATH_2_SET_VALUED_REPAIR_AND_REAL_GO_PRESEAL.md) |
| Freeze common D9/D10 acceptance cases, independent of treatment style | [`423be88`](https://github.com/WhoSia/EvoNOMOS/commit/423be88ebd70b16635c22248624cacbdc26ad67a) | [Go oracle](../../tools/p35-math2/tests/p35_math2_frozen_d9_d10_test.go) |
| Formal classical relational logic and separate countermodels | [`20475f8`](https://github.com/WhoSia/EvoNOMOS/commit/20475f85d2f25c4365ce19acf008f81653aa38e7) | [Lean source](../../tools/p35-math2/lean/EvoNOMOSMath2.lean), Prolog, Go |
| Actual twelve original-source snapshots, not just models | [`484f781`](https://github.com/WhoSia/EvoNOMOS/commit/484f781f5d94066a529937fa1976ab01d59bc7c1) | [Go D9-only, D10-only and combined patch variants](../../tools/p35-math2/arms) |
| Read-only original Go module / math CI | [`d4c228f`](https://github.com/WhoSia/EvoNOMOS/commit/d4c228f43e47219de0c074baec37752a6b869c74) | [Initial CI #37919807981](https://github.com/WhoSia/EvoNOMOS/actions/runs/37919807981) |
| Lean technical corrections, no weaker goals | [`3fa3998`](https://github.com/WhoSia/EvoNOMOS/commit/3fa39981ca7758ab23792d9bd118dc256543d3b4), [`e9f1806`](https://github.com/WhoSia/EvoNOMOS/commit/e9f18063fcc550b8130a49f42683479dbdc47be5) | [Full SUCCESS #37920470010](https://github.com/WhoSia/EvoNOMOS/actions/runs/37920470010) |

Initial CI **#37919807981 failed overall**, although `original-chi` and `prolog-go` actually succeeded; Lean compile errors in finite witness lemmas. First technical correction #37920276726 still failed in Lean; second correction explicitly simplified definitional reduction, leaving intended theorem statements and Go source families unchanged. Both failures retained, not counted as negative scientific evidence.

## Formal type-correct Lean verdict

Define `May(R,a,P) := ∃b, R(a,b) ∧ P(b)`; `Must(R,a,P) := (∃b,R(a,b)) ∧ ∀b,R(a,b)→P(b)`. The existence conjunct explicitly prohibits vacuous “must” judgments when no admissible repair exists. `TwoStep(R,S,a,c) := ∃b,R(a,b)∧S(b,c)`.

Exact source [`EvoNOMOSMath2.lean`](../../tools/p35-math2/lean/EvoNOMOSMath2.lean), pinned Lean4 v4.34.1, no `sorry/admit/axiom`, built by Lake and independent leanchecker:

- **T-MAY/MUST:** Must implies May. Restricting admissible relation to a nonempty subset preserves Must, assuming the predicate is unchanged. Applies to arbitrary underlying state types and repair relations.
- **T-COMMUTING SQUARE:** existence of the appropriate local square transfers a two-step path `R;S` to `S;R`; two opposite square hypotheses imply equal **reachable final-state sets**. Without these assumptions, no commutation theorem is asserted.
- **T-REALIZATION:** if frozen symbolic output factors through a concrete observation, `Q = psi ∘ O`, then symbolic distinction implies concrete observation distinction. This is a formal classical DIP-50 lemma, not a proof that a proposed Go measurement actually factors for all authorized outcomes.
- **C-CHOICE:** a Fin3 toy repair family has two distinct successors, one satisfying a chosen implementation-style predicate and one not. May holds while Must fails.
- **C-NONCOMMUTE:** a Fin5 toy has `R_a;R_b` reach one result and `R_b;R_a` another. These are **abstract finite relations**, not asserted as the outcome of concrete Go D9;D10 patch ordering.

SWI-Prolog `plunit` and native Go unit/race tests independently reconstruct these finite countermodels, including paths `AB=[three]` vs `BA=[four]`. This demonstrates a possible mathematical mechanism, not occurrence of that mechanism in real code.

## Actual source-level Go evidence

Original upstream [`go-chi/chi v5.1.0`](https://github.com/go-chi/chi/tree/67be7d9cafdaeb4e04e887ff78d09e030ee43b00) and original Go1.23 module/tests. Two old verified structural alternatives **LIVE** (current mutable routing registry looked up per request) and **SNAPSHOT** (fixed ordered route-group copy at Handler creation), each starting from its exact previous D8 source bytes.

Frozen semantics for the two *equal across ALL arms* subsequent demands:
- D9 supports any of multiple **physical HTTP header field values** when matching, with existing casefold, specificity and first-registered-per-key semantics.
- D10 treats research-scope *unquoted* comma-separated header fields as individually trimmed tokens, composing with D9. **Not** a general-purpose HTTP parser, no quoted commas or blanket RFC compliance claim.

For each architecture independently two distinct code organizations `inline` and `helper`, with self-contained previous source path and separate D9-only, D10-only, both D9+D10 snapshots. These are **twelve** executed source snapshots representing four final independently valid patches. Their distinct source SHA values at final combined stage:

| Original architectural world | Chosen patch organization | Final Go blob SHA | Native whole original module |
| --- | --- | --- | --- |
| LIVE | inline | `01923522c1b5479ca44f84ff580f2c8cad8125cd` | PASS |
| LIVE | helper | `37de396db3df5361f1c98a988699ce34b8fd7405` | PASS |
| SNAPSHOT | inline | `cfcb61ba81aa599f52d865ba790d0ce62d1d63f7` | PASS |
| SNAPSHOT | helper | `b9954c9e21f2cd4946812a7f8afcbcedc1cd9de7` | PASS |

The inline designs enumerate field values/tokens directly in `Handler`; helper designs add `p35Math2BestMatch` called from `Handler` and reuse `p35P7MatchStrength`. Both preserve the externally supplied original public Go API and all previous frozen D0/D8 and LIVE/SNAPSHOT sequential registration tests, while satisfying D9+D10.

[Final exact original Go CI **#37920470010**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37920470010) **SUCCESS in all 3 jobs**:
- `original-chi`: previous D8 source *EXPECTED FAIL* on D9 and D10, D9-only implementation passes D9 and expected-fails D10, D10-only passes a D10 witness and expected-fails a D9 witness, all **four independent final original-source alternatives PASS** their D0/D8/D9/D10 public acceptance and architecture mode, native `go vet ./middleware`, `go test -race -count=1 ./middleware`, and original complete `go test -count=1 ./...`.
- `prolog-go`: Go native `go vet`, `go test -race` and SWI-Prolog `plunit` PASS, with abstract May-not-Must and noncommuting relation countermodels.
- `lean`: Lean4 pinned build and independent leanchecker PASS with no proof holes/introduced axioms.
- Artifacts: original-Go ID **11611338733**, sha256 `39e788a70451765facd68a8cd5e7360c064ed2ea3c40634897980b7d06c7b4b6`; Go-Prolog ID **11611437644**, sha256 `9a1a1a4130ec2f8961e5341c8d8fc606fa2000261c0cde370d1123480634f964`; Lean ID **11611836995**, sha256 `96d1f1555a9e4497aaf7403c8680e8b0297b8f78cdeb39a47ff181edaf2f28ca`.

The original upshot is **real program repair is set-valued, with at least two distinct source implementations per old structural world**, not a unique function. This is a *lower-bound existence witness* only. Different code bytes/style do not prove unequal observable semantics beyond the frozen tests; neither all legal repairs nor minimum-source-change lower bounds nor architecture dominance were established.

## Critical validity boundaries and progress beyond historical DIP-49/50

**Partial real-world concrete source bridge achieved:** exact upstream Go source and two old structural implementations; same requirements; identical architecture-neutral functional tests; real finite first-prefix negative/positive controls; no post-outcome repair-oracle edits in the original MATH-2 wave. However the full DIP-49 authorized *pair-separating competing-law model family* is **not instantiated**, and DIP-50's global factorization/prefix certificates for every authorized state/domain/branch are **not established**. Original Go patches were not replayed as literal source transformations in both D9;D10 and D10;D9 orders; the abstract Lean noncommutation theorem is not empirical evidence of source-level order noncommutation.

The success therefore **does not establish a new SOLID or beyond-SOLID law**. Existing may/must logic, relational program semantics, software repair multiple plausible patches, and elementary commuting-diagram theory fully explain the formal portion. The main unresolved challenge is *new conditionally predictive differences between truly independent structural software alternatives under exactly the same multi-step demands*, falsified against strong classical rivals.

## Second robust oracle contact (separate time/bias tier)

An independent reference semantics over two research-specific header keys and **12×12×5=720** grid cases per original Go patch was **post-outcome sealed** in [MATH-2B oracle preseal](P35_MATH_2B_POSTOUTCOME_DIFFERENTIAL_ORACLE_PRESEAL.md) and [frozen Go test](../../tools/p35-math2b/tests/p35_math2b_differential_test.go). It must not retroactively strengthen the blind MATH-2 seal. A direct source-strength comparator independent of treatments specifies exact vs wildcard, first registration, physical vs comma tokens and fallback. Initial [MATH-2B CI #37924946610](https://github.com/WhoSia/EvoNOMOS/actions/runs/37924946610) stopped at a **test build error** (unused fmt import, before any comparisons); human [test-import fix](https://github.com/WhoSia/EvoNOMOS/commit/10f138d95cde3ed3730e825511193cc32e279fb0) makes no change to grid cases/reference/Go treatments. Corrected [read-only MATH-2B CI **#37925137057**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37925137057) **SUCCESS**: **four source alternatives × 720 fixed reference cases = 2,880 independent-reference comparisons** all PASS, as do preexisting acceptance tests on each arm. Receipt messages are `MATH2B_live_inline_REFERENCE_720_AND_PRIOR_CONTRACT_PASS`, `MATH2B_live_helper_REFERENCE_720_AND_PRIOR_CONTRACT_PASS`, `MATH2B_snapshot_inline_REFERENCE_720_AND_PRIOR_CONTRACT_PASS`, `MATH2B_snapshot_helper_REFERENCE_720_AND_PRIOR_CONTRACT_PASS`. Hosted artifact [**11614170007**](https://github.com/WhoSia/EvoNOMOS/actions/runs/37925137057/artifacts/11614170007), ZIP SHA256 `b1bf50b81b7f36a3148134d7b9d068f4d196dc9c0a6ec1d6daad8e965996ad33`. This is **post-outcome finite domain robustness**, not proof of complete HTTP semantics, full program equivalence or original blind replication. Fixed four treatment source files were unchanged throughout MATH-2B.

## Next research gate (NOT an excuse for more pure method prefaces)

1. Either produce a source-verified **commuting square** under two substantive, same-meaning Go change demands with both literal orderings and original native tests, or produce a source-backed noncommuting witness with valid **both** demand orders and matched observations; do not infer order dependence from one implementation path.
2. Freeze a small explicit candidate **structural law** rival family and DIP-49 query signatures before running, including a classical information-hiding/cache prediction and at least one alternative; require actual prediction disagreement.
3. DIP-50 faithful concrete realization: same initial source, action labels corresponding to identical functional demands, each prefix admissible, oracle fixed without architecture labels, and observation signatures distinguish rivals without aliasing.
4. Keep model/state equality, observed contract equivalence, repair-set membership, and prospective structural preference as separate objects; no scalar econometric reduction, no responsibility-boundary detour.
5. Replicate structural result in an *independent Go codebase* before claiming any beyond-SOLID law.

**Court:** `P35_MATH2_METHOD_AND_REAL_SOURCE_PASS__CORE_NOVELTY_HOLD__P35_OPEN__LAW_R2_NOT_AUTHORIZED`.
