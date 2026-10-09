# EvoNOMOS P35-MATH-2 — Set-Valued Go Repairs and Faithful DIP-49/50 Realization: Pre-Implementation Seal

**2026-10-09. Protocol first.** Parent P35 OPEN; LAW-R2 NOT_AUTHORIZED. This is NOT an original automata discovery. Do not recast as responsibility analysis, scalar edit-cost optimization or procedural bureaucracy.

## Prior lineage, not to rediscover

[DIP-49](https://app.notion.com/p/3ccef561cf92818484a4d55302715e84) froze candidate-pair distinguishing queries, identity-preserving adaptivity, MODEL_ESCAPE and identifiability holds; **no real outcome**. [DIP-50](https://app.notion.com/p/3ccef561cf92811291b4c56437bc5b4b) demanded outcome-blind concrete mapping beta, prefix correctness on exact base and frozen outcome-factorization, again **theorem-first, no execution**. [Earlier P31/P33 record in 14.md](https://drive.google.com/file/d/1TuweqOEc1KY14ddEJVoPbBJAiT-i3thP/view) explicitly proposed nondeterministic admissible repair relation `R_d⊆A×A`. MATH-1 is only a kernel-checked simpler instrumentation.

## Mathematical M2 claims to test (CLASSICAL, not novelty)

Represent admissible repair as `Repair(d,A,B)` relation. A patch witness `∃B,Repair(d,A,B)` **does NOT entail** every valid patch has its recorded syntactic property. `May(P) := ∃B,Repair∧P(B)`; `Must(P):=(∃B,Repair)∧∀B,Repair→P(B)`. The existential clause makes `Must` non-vacuous. Demand sequences are relational composition `R_a;R_b`, not deterministic functions. Prove:
- **T-MAY-MUST:** `Must P ⇒ May P` and legal-set restriction preserves must if at least one survivor remains.
- **T-SQUARE:** every `R_a;R_b` two-step path admits an exactly matching `R_b;R_a` final state iff corresponding path-inclusion; *bidirectional local commuting-square assumptions* imply equal final reachability sets, without claiming all repair relations commute.
- **T-REALIZATION (DIP-50):** a frozen symbolic observation `Q=ψ∘O_concrete` on the authorized domain guarantees `Q(x)≠Q(y) → O_concrete(x)≠O_concrete(y)`. This is a semantic transport lemma, not a new theorem.
- **C-CHOICE:** finite repair family with two distinct valid implementations makes a syntactic 'all repairs share the helper' claim FALSE, despite both satisfying contract.
- **C-NONCOMMUTE:** finite nondeterministic demand relation with `R_a;R_b` and `R_b;R_a` different reachable end states; neither ordered relation may be silently assumed equivalent. Go and SWI-Prolog independently check the finite countermodels; Lean must prove their exact claims without `sorry/admit/axiom`.

## Genuine original Go codebase and equal requirements

Base repository [go-chi/chi](https://github.com/go-chi/chi) frozen **v5.1.0** commit `67be7d9cafdaeb4e04e887ff78d09e030ee43b00`. Two *already implemented* structurally distinct original Go alternatives `tools/p35-p7/d8/{live,snapshot}/route_headers.go`; all experimental arms start from the exact byte-identical respective D8 base. Preserve actual Go API and:
- **LIVE:** new routes appended after Handler creation are visible on the next sequential request.
- **SNAPSHOT:** Handler's route groups are copied on construction; subsequent route registration is invisible to the older handler.
- Prior D0 and D8 acceptance tests and original chi full module and middleware race suite must PASS.

### Frozen additive functional demands (same across both structures AND both repair styles)

**D9 — repeated header FIELD VALUES:** an incoming request may carry multiple physical header field values with the same name (constructed via `http.Header.Add`). A registered route for that header matches if **any** physical field value matches its literal/wildcard pattern, case insensitive as in previous P7; never only inspect `Header.Get`'s first value. For a single header name, the first **registered route that matches any value** wins. For distinct header names, best match class EXACT>WILDCARD, and lexical header-name tie-break; preserve default, empty and `RouteAny`. No comma splitting is implied by D9 alone. Both old D8 arms predicted to FAIL new D9 cases, both independent repair styles predicted to PASS.

**D10 — unquoted comma token fields:** for the registered string-matching headers in this *research contract*, a header field value may be a comma-separated list of **unquoted** tokens, whitespace-trimmed around tokens; matching applies to each nonempty token. `["ping, pong"]` is logically equivalent to `["ping","pong"]` for route selection and must compose with D9 repeated physical fields. Tokens with quoted commas or other RFC structured fields are explicitly OUT OF SCOPE and must not be generalized to all HTTP headers. D10-on-D8 and D9-only are predicted to fail the respective missing demands; final D9+D10 arms must pass BOTH and all D0,D8 originals. All four finite patch families predicted PASS if correctly implemented; no predicted structural winner.

### Registered comparison dimensions and patched-source witnesses

For each LIVE/SNAPSHOT arm, independently build **two differently structured source patches**, `inline` (explicit value/token enumeration at call site) and `helper` (encapsulated value/token matching function), on the same original D8 Go code. At least two distinct, nonidentical Go source SHA and AST functions **that both pass** provide existential proof of patch nonuniqueness *in this explored witness set only*. They do not identify all valid repairs, minima, or necessary edit sites. D9-only and D10-only intermediate source cases must exist as counterfactual negative checks and must preserve D0/D8. Final D9+D10 source is a tested conjunction, but unless the source patches themselves are replayed in both literal orders, DO NOT claim measured order independence or noncommutation. No architecture ranking is authorized merely by counting files.

**Test oracle freezes before any D9/D10 implementation:** a separate committed Go test file defines the cases independently of implementation-style tags; original existing P7 D0/D8 tests copied unchanged. Original source checkout must verify exact Git hash. Read-only GitHub Actions can fetch Go toolchains and original public source, never modify upstream or auto-commit.

## Honesty / lineage boundaries

Actual DIP-49 candidate-law separation (distinct predictions among strong non-SOLID theory rivals) is NOT achieved merely by witnessing multiple implementations. DIP-50's realization gate can be **locally instantiated** for a declared concrete D9/D10 oracle if all required prefixes pass; broader law-automaton identification stays HOLD. Strong prior art: relational semantics, may/must nondeterministic refinement, commuting diagrams, automata learning, program repair overfitting and multiple plausible patches. The key advance sought here is faithfully executing the *previously missing bridge* between formally defined alternatives and real original Go, not conjuring new mathematics by renaming classical relations.

Freeze hierarchy: PRESEAL → TEST-ONLY COMMIT → LEAN/PROLOG FORMAL SOURCE → REAL GO PATCHES → INDEPENDENT NATIVE CI → EVIDENCE VERDICT. No outcome-dependent oracle changes permitted.
