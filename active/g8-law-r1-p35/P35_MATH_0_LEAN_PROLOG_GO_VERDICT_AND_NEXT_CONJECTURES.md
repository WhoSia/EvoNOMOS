# EvoNOMOS P35-MATH-0 — Lean, Prolog, Go Triple-Language Evidence Receipt and Proof-Relevance Gate

**2026-10-09 — `MATH0_LANGUAGE_BRIDGE_PASS__NO_NEW_THEORETICAL_LAW__P35_OPEN__LAW_R2_NOT_AUTHORIZED`**

## What genuinely passed

After the research protocol was published independently of the implementation, [Actions #37912493121](https://github.com/WhoSia/EvoNOMOS/actions/runs/37912493121) completed **SUCCESS** on two independent jobs in GitHub's read-only Ubuntu runners:

| Independent verification | Exact result | Artifact SHA256 |
| --- | --- | --- |
| Lean `v4.34.1` `lake build` with bundled independent `leanchecker`, explicit no `sorry`/`admit`/`axiom` lexical gate | `lean-kernel` **SUCCESS**, compiled 3 Lake jobs, independent checker success | `p35-math0-lean-core-foundation` ID **11606928415**, `a8f49fe3339eed73e9203e9ea26b19814ab7b350b3dd53db079244737bd97f55` |
| Native Go `1.23` `go vet`, `go test -race -count=1`, finite two-start JSON, separate SWI-Prolog `plunit` tests | `prolog-go-countermodels` **SUCCESS** | `p35-math0-go-prolog-bounded-countermodels` ID **11607133238**, `cb2fbee5369f0b8c8e40ccb35d418349a033eca1827fb6521193cd68120fcc24` |

**Original failed first CI** [#37912226509](https://github.com/WhoSia/EvoNOMOS/actions/runs/37912226509) is retained. That run's Go+Prolog job already PASSed, but Lean tooling stopped **before compilation** because lean-action requires `lake-manifest.json`. A new human WhoSia commit `d370a32` adds an empty-dependency Lake 1.2.0 manifest. Same `.lean` theorem statements/proof terms, same Go and Prolog source were successfully tested in the corrected #37912493121. No posthoc theory/proof modification concealed.

**Commits on `main`, independently human WhoSia authored/committed:** research [preseal `bae7da6`](https://github.com/WhoSia/EvoNOMOS/commit/bae7da600c23d3ec717a110070efa3917178a319), [sources `bd27e4a`](https://github.com/WhoSia/EvoNOMOS/commit/bd27e4a0d708fca620c8a7b824e0a0417418e39e), [workflow `6b58044`](https://github.com/WhoSia/EvoNOMOS/commit/6b58044bf0b01c71b07fd24b99239cdb693a23e5), [manifest correction `d370a32`](https://github.com/WhoSia/EvoNOMOS/commit/d370a32cab3268add50e1de40cdb12bad11d4e52), [research-home clarification `985d499`](https://github.com/WhoSia/EvoNOMOS/commit/985d499ce696e12c36334de643b2e3b64818afb7). No CI bot commits, no unreviewed ref writes.

## Minimal formal abstraction (NOT a new law)

Let `Design = {LIVE,SNAPSHOT}`, `World = Bool×Bool`. First coordinate is state at construction, second is currently available state; `Obs(LIVE,(b,c)) = c` and `Obs(SNAPSHOT,(b,c)) = b`. Define `ObsEq(C,A,B)` iff `∀w∈C, Obs(A,w)=Obs(B,w)`. Then:

1. If `C⊆D` and `ObsEq(D,A,B)`, then `ObsEq(C,A,B)` (the equivalence relation is antitone in the set of permitted observations).
2. For initial `(b,b)`, `Obs(LIVE)=Obs(SNAPSHOT)`.
3. For updated `(b,¬b)`, `Obs(LIVE)≠Obs(SNAPSHOT)`.
4. Every score formed *solely as a function of the initial output bit* gives the same value to the initially aligned strategies.

All are core Lean-checked lemmas in [`EvoNOMOSMath0.lean`](../../tools/p35-math0/lean/EvoNOMOSMath0.lean), without opaque axioms or proof holes. Independent [Prolog generator](../../tools/p35-math0/prolog/countermodels.pl) and [Go enumerator](../../tools/p35-math0/go/model.go) check both Boolean initial states as countermodels to the false implication **initial equivalence implies equivalence after a state change**.

**Epistemic boundary:** these are elementary consequences of definitions and classic temporal/state observation theory. A *mathematically valid formalization of a small two-bit abstraction is neither a theorem about the entire original Go router nor a newly discovered software-design law*. The actual [original Chi P7 Go A/B evidence](P35_P7_GO_STRUCTURAL_RIVAL_AND_CONDITIONAL_ENVIRONMENT_VERDICT.md) remains a separate test-backed source account.

## Mathematical discovery agenda (explicitly theory-competitive)

### A. Trace-depth equivalence and quotients

For actual software state machines with finite action alphabet `Σ`, define `A ~ₖ B` when no allowed trace of length at most `k` distinguishes them. Investigate strict filtrations, first separating trace, and how the relation behaves after machine composition, with recognized **automata equivalence / Myhill–Nerode / bisimulation** as strong *prior-art explanations*. This includes exact statements in Lean, bounded shortest-witness Prolog and independently generated Go state-machine examples. A textbook lemma is not a novelty claim.

### B. Structure composition under a fixed demanded behavior

Model two actual Go implementations with the same external behavior before composing with a third component; test when their contextual preorder is preserved, destroyed or incomparable. Seek a genuinely discriminating mathematical condition rather than naming 'responsibilities' or optimizing edit counts. Formal condition must include admissible composition and external observations; no theorem from syntactic shared-names alone.

### C. Admissible repair-set geometry beyond scalar cost

Define `Repair(A,d,Q,G)` as *the set* of modifications to A that satisfy requirement `d` and observable contract `Q` within fixed grammar `G`. Test whether demand conjunction, grammar expansion and architectural constraints preserve any inclusion/order relation, and explicitly attack false claims using Prolog small countermodels. Selected source patches only witness set nonemptiness; cannot establish family minima. If language meaning or constraint grammar shifts, state it before comparing.

**Research promotion:** only after exact definitions, adversarial countermodels, kernel-checked claim, existing-theory attack, original-Go independent A/B with matched demand sequences, and a second codebase. No tool count, commit count, proof count, scalar cost or MQR paperwork may automatically authorize a new LAW.

## Sources / technical standards (evidence, not authority)

- [Terence Tao, *Mathematics in the age of AI* (2026)](https://arxiv.org/abs/2608.16753): foregrounds goals and values of research even when AI becomes strong at solving problems. Does **not** prescribe our specific development workflow.
- [AlphaProof, *Nature* (2025)](https://www.nature.com/articles/s41586-025-09833-y): formalization, search and checking illustrate why machine-checked proofs matter. These methods do **not** imply our proposed software law is novel.
- [Lean official installation](https://lean-lang.org/install/manual/) and [Lean `lake` build documentation](https://github.com/leanprover/lean4/blob/master/src/lake/README.md); [SWI-Prolog test suite CLI](https://eu.swi-prolog.org/pldoc/man?section=pldoc-running).

**Research judgment: METHOD PASS.** The real question remains *what structural truth about evolving software, if any, can we prove that known theories do not already cover?* P35 continues.
