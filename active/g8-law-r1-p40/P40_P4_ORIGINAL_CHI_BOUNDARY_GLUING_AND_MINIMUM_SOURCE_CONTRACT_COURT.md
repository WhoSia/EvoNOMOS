# P40-P4 — Original go-chi Boundary Repair Gluing and Minimal Source-Contract Obstructions

**2026-10-10 KST · P40 LAW-R1 OPEN · ORIGINAL UNMODIFIED PUBLICLY MAINTAINED Go SOURCE · CLASSICAL PRIOR-ART SURVIVES · LAW-R2 NOT_AUTHORIZED.**

[Source receipt and SHA pin](../../tools/p40-p4/ORIGINAL_SOURCE_PIN.md) · [actual Go integration tests](../../tools/p40-p4/original_chi_gluing_test.go) · [finite source contract theory checker](../../tools/p40-p4/boundary_minimum_certificate_court.py) · [hosted read-only Actions #38042896746 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38042896746). Immediate predecessors: [P40 P3 Go architecture/owner reversals](P40_P3_ARCHITECTURAL_RIVAL_REVERSALS_CONCRETE_GO_AND_OWNER_OPTION_CUT_THEOREM.md), [P39 Math-H source-order geometry](../g8-law-r1-p39/P39_MATH_H_EXACT_SEVEN_SHATTERING_TWO_ANCHOR_AMALGAMATION_AND_INFINITE_BOUNDS.md).

## P4-A. Real source and real contract

**Original maintained library:** [go-chi/chi](https://github.com/go-chi/chi), exact SHA `167e1e3bd039d060696b99c8da4e876ae04f42c1`, committed 2026-09-29, compiled using its own unmodified `go.mod` specifying `go 1.24`. GitHub Actions checks out original repository at EXACT SHA into a separate temporary workspace path and uses a local Go module replacement; no vendor copy or forked chi source has been committed or altered.

**Direct source findings (actual original at pinned SHA):**
- `chi.go`: `Router` interface embeds Go's `net/http.Handler` and `Routes`, exposing `Mount(pattern, handler)`, `Use(middleware...)` and subrouter construction.
- `mux.go`: `Mux.Mount` rejects a nil handler, a duplicate already-mounted route pattern and a router mounted onto itself; the same function mounts actual children using wildcards.
- `mux.go`: `Mux.Use` rejects addition of global middleware after routes have initialized the mux handler.
- `tree.go`: actual radix-tree `findPattern` used by the duplicate route check.

These source semantics—not a fictional SOLID rule—are the specification against which P4's exact Go program is tested.

## P4-B. Explicit two-module owner/source-edit grammar

Define a base parent router P, with pre-existing `GET /old` returning `unchanged`. Each independent module locally constructs one `chi.Router` handling relative `GET /` and `GET /item` with distinct A/B responses. Local source edits are:
- `e_A(a)`: add `P.Mount("/service/"+a, childA)`;
- `e_B(b)`: add `P.Mount("/service/"+b, childB)`.

In this **restricted experiment only**, a,b lie in K={a,b,c}, the canonical routes are flat and pairwise prefix-disjoint when unequal, children do not modify P's middleware, and all handlers are stateless. The old client `GET /old` must keep producing `unchanged` and each module's new request `GET /service/<key>/item` must produce its own output. An edit is accepted only if the original chi's runtime dispatch does not panic and these HTTP tests pass.

Each e_A and e_B in a fresh original parent is individually valid for ANY of three key choices. The question is whether locally valid source edits also admit a global composition on the SAME parent.

**Theorem P4.1 (pinned chi canonical-flat-mount gluing criterion):**
[
oxed{ operatorname{SafeGlue}(e_A(a),e_B(b))
iff a
eq b,qquad a,bin K.}
]

**Proof / original runtime support:** If a=b, `Mux.Mount` checks the second wildcard pattern against the parent's already mounted route and panics. If a≠b within the three canonical non-overlapping flat namespaces, the route registrations are disjoint, neither writes common state, and the old /old route and both independently selected new /item routes retain their responses. This is confirmed by **nine** actual global two-mount Go test cases. The three duplicate-key pairs fail by the expected original chi panic; the six distinct-key pairs pass. Each of six module+path singletons (A and B, three keys each) independently passed original Go client tests. **These counts characterize this test grammar only, not the full χ router language.**

**Minimal obstruction certificate:** `{e_A(a),e_B(a)}` is jointly UNSAT while each singleton is SAT. The minimal inconsistent source-repair family has **size 2** for this grammar. Separately, mounting a child followed by `Mux.Use` is forbidden; pre-route `Use` followed by mounting passes. This additional temporal restriction cannot be inferred from namespace disjointness alone.

## P4-C. Information completeness and exact minimum boundary memory

The parent needs sufficient *shared namespace boundary information* to determine whether two independently valid mount requests can compose. Consider any abstract local boundary code (eta:K	o Q), and a proposed exact classifier (J:Q^2	o{0,1}) such that
[
J(eta(a),eta(b))=[a
eq b]quad	ext{for all }a,bin K.
]

**Theorem P4.2 (minimum sufficient source-interface boundary code):**
[
oxed{exists J	ext{ exact for ALL pairs}iff
eta	ext{ injective},qquad
	ext{minimum fixed-width bits}=lceillog_2|K|ceil=2.}
]

**Proof:** If (eta(a)=eta(b)) with a≠b, classifier inputs for (a,a) and (a,b) are identical although real compatibility differs (0 vs 1), impossible. Conversely an injective (eta) lets J compare recovered keys. For three names at least three codewords, so minimum 2 bits. The independent finite checker enumerates all **27** three-label encodings and all **8** one-bit encodings, verifying exactly this theorem. This is the *classical observation factorization/kernel theorem* (P37, Myhill–Nerode family), not new information theory. It counts a code for a namespace label, not total memory needed by a deployed Go routing service.

**Why this matters:** It exhibits the *smallest source-realizable boundary datum* that a compositional proof must expose. A local “handler compiles and its own tests pass” certificate omits this shared namespace; even a source-modification that leaves each `http.Handler` method set unchanged may violate global safety when claims conflict.

## P4-D. General contract-local gluing theorem and scope limits

A source module (M_i) has local verified edit choices (R_i), a boundary projection (partial_i:R_i	o B_i) and a set of old-client observations (O_i). There is a proposed global (otimes) composition with explicit owner permission and invariant guard (Gamma,I).

**Standard sound composition sufficient rule (classical assume/guarantee/frame condition):**
1. Each local edit preserves its named old-client observations for its declared environment assumptions.
2. A common boundary contract identifies **all** cross-module resource reservations, method-name promotions, order dependencies and other effects relevant to the specified client observation grammar. This is an **adequacy assumption to prove**, not a free consequence of OOP.
3. Chosen local boundary demands are compatible in the exact shared constraint relation; the combined owner rights permit composition.
4. The composition operator satisfies a **frame/noninterference guarantee**: one module cannot change another module's client-relevant observations except through the declared boundary, and there are no hidden globally shared side effects.

Under these premises the combined system preserves old client behavior and satisfies the new demands if each component does. Proof: split client observations by module+boundary, use local preservation and frame for local observations and boundary compatibility for shared observations; reconstruct global behavior by explicit composition semantics. The theorem would be circular if frame/adequacy were defined as “global program stays safe”; they must instead be independently checked properties of source semantic/ownership footprints. On pinned chi's canonical-flat route grammar those premises have **concrete source meaning** (namespace key reservation, middleware sequencing, stateless handlers). On arbitrary χ regex/wildcard mounts, global middleware or shared state these premises are **not yet proved**, so no universal claim is made.

**Strong rival court:** classical rely/guarantee and separation logic frame reasoning, acyclic constraint join trees/Yannakakis (1981), abstract boundary contract factorization, Go chi's own documented mount collision and middleware order safeguards, Abramsky–Brandenburger (2011) sheaf-style local/global section obstructions. These theories already anticipate both noninterference sufficiency and gluing failure; P4 is an **original source-backed conditional specialization, not a new universal mathematics law**.

## P4-E. SOLID subset question (precise research boundary)

P4's actual-source result reveals the distinction between *local OO/SOLID properties* and *cross-module repair correctness*. Two locally identical one-handler, one-responsibility modules each communicate via the narrow standard `http.Handler` abstraction and preserve their old clients. The pair (A claims a, B claims a) and the pair (A claims a, B claims b) have identical **local-only structural profiles up to renaming**, but one fails and the other passes globally. Therefore the global gluing predicate **cannot factor through any purely local signature invariant under namespace renaming**. The omitted source-boundary equality relation is indispensable.

This yields a promising proof architecture: construct a richer typed category of OO modules, source edits, client contextual observations, ownership and boundary-resource reservations; the five classical SOLID principles become **specified, partial views** of that structure. Prove a strict reduct/cannot-reconstruct result with the same-name/different-name pair, instead of the philosophically indefensible assertion that the five slogans follow as universal axioms from all object-oriented code.

See [P40 Math-A foundational structural program](P40_MATH_A_OBJECT_REPAIR_STRUCTURES_AND_SOLID_STRICT_REDUCT_PROGRAM.md) for typed definitions, proof targets, independence countermodels, and prior-art limits.

## P4-F. Independent hosted original source evidence

[GitHub Actions #38042896746](https://github.com/WhoSia/EvoNOMOS/actions/runs/38042896746) **SUCCESS**, exact test source/workflow HEAD `fe8e927ba67a2418de15ee79dad1bd5d06eb1f06`, checked chi source SHA `167e1e3bd039d060696b99c8da4e876ae04f42c1` before executing actual Go tests. All three job steps independently passed: source commit assertion, actual original chi HTTP integration tests, and mathematical boundary classifier court. Artifact `11665784482` SHA256 `630be1ebb1a63ef3ac2635d5a26cb051f5b162eb02a1405b7994c0b48d484e76`. The original Go external repository remains unchanged.

**P40-P4 classification:** Actual original maintained source verification PASS · local/global namespace obstruction PASS · minimum 2-bit boundary signature PROVED · exact finite classical factorization · general SOLID strict reduct theorem research OPEN · independent NEW OO law novelty HOLD · LAW-R2 NOT_AUTHORIZED.
