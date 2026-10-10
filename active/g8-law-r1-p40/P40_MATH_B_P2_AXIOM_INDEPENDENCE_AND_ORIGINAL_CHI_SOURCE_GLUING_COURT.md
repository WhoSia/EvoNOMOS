# P40-MATH-B-P2 — Source Guard Independence, Regex-Disjoint Mount Rejection and Lean Continuation Kernel

**EvoNOMOS Generation VIII LAW-R1-P40 · 2026-10-10 KST · original maintained Go source + scoped structural countermodels · P40 OPEN · NEW LAW HOLD · LAW-R2 NOT_AUTHORIZED.**

## Grounding and receipts

[P40-MATH-B base paper](P40_MATH_B_GUARDED_OBJECT_REPAIR_AXIOMS_AND_MINIMAL_FUTURE_BOUNDARY_THEOREMS.md) · [new source falsification tests](../../tools/p40-p4/original_chi_math_b_boundary_test.go) · [Lean theorem source](../../tools/p40-math-b/lean/P40MathBIndependence.lean) · [original pinned Go CI #38047053489 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38047053489).

Actual library: [unmodified go-chi/chi at commit 167e1e3bd039d060696b99c8da4e876ae04f42c1](https://github.com/go-chi/chi/tree/167e1e3bd039d060696b99c8da4e876ae04f42c1), built with the original Go 1.24 module. All repository tests live outside that external source. Go CI test head 2109c0e325712492a6bc9dd9bb9aed30b5afae58; actual job console logs contain source-boundary success markers. **The Lean receipt MUST be separately checked before being called PASS.** Initial Lean attempts failed on missing Lake manifest and missing Decidable typeclass instances, and were fixed rather than disguised.

## 1. Stronger native-source falsifier: disjoint HTTP request languages still cannot glue

Two source edits on independently fresh chi parent routers:
- N: Mount /service/{number:[0-9]+}, a child handling GET /item with response NUM:item. Old GET /old stays unchanged, and GET /service/123/item passes.
- A: Mount /service/{letter:[a-z]+}, a child handling GET /item with response ALPHA:item. Old GET /old stays unchanged, and GET /service/abc/item passes.

The two admitted path languages are disjoint: an ASCII-only decimal-digit segment cannot also be an ASCII-only lowercase-letter segment. Nevertheless, **both possible source registration orders on the same chi parent fail**: the second Mount panics with the original source guard saying it is mounting a handler on an existing path. The dedicated native Go test checked both singleton executions and both insertion orders; Actions run #38047053489 SUCCESS.

**A formally falsified scoped implication:**

Disjoint request-language support + each source edit individually admissible with preserved old client
\(\not\Rightarrow\) both source edits jointly admissible on the same parent chi router.

The cause is not runtime ambiguity of a request matched by both regexes. The native source requires an additional **implementation-level admission contract**: in mux.go Mount calls tree.findPattern on requested wildcard routes; tree.go's findPattern follows internal structural pattern nodes rather than deciding regex-language disjointness. Two HTTP languages may be disjoint while source registration is conservatively refused. No claim is made that all differently named regex pairs in chi are rejected or that the maintainers intended this exact policy.

This is stronger than P4's equal-literal-name collision, but **classical CSP with an accurate source reservation predicate** can already express it. A new universal source law is not established.

## 2. Independent alias-identity source counterexample

On the same parent router and the same fresh literal path /service/unique:
- A fresh chi.NewRouter child implements chi.Router, installs successfully, and its /item and old /old HTTP clients pass.
- An inline child returned by parent.With(identityMiddleware) implements the same chi.Router interface but shares parent.Mux.tree. Mounting it on /service/unique fails the ORIGINAL chi self-mount alias guard.

Both have the same exposed router interface and declared path; those two pieces of local information cannot decide whether native mounting succeeds. The alias handler is **not** asserted to be separately valid as a deployed HTTP child: this is specifically a source-level mount-admissibility test. This distinct guard survives even after namespace collision is excluded.

## 3. Separate deletion tests for three narrow assumptions

We distinguish:
- N — no conflict with the parent's source route reservation: with separate child trees and no late middleware, an occupied mount path is rejected while a fresh flat route name succeeds.
- R — no alias between parent and child routing trees: with the very same fresh mount name, mounting a distinct child succeeds but mounting parent.With-derived tree alias fails.
- T — compatible staging of global middleware: late Use after routes is rejected even in the absence of duplicate mount claims; pre-route Use succeeds.

These original-source controlled interventions refute dropping N, R or T while continuing to infer native admissibility **across the combined test domain**. Each source guard targets a different concrete failure mode. They are not a claim of an exact if-and-only-if characterization for every chi pattern, middleware behavior, ownership policy or version.

The six general semantic categories in Math-B (static typing, client semantics, owner rights, goals/invariants, boundary composition, dependency structure) are **not independently axiomatized yet**. They name kinds of data and semantic commitments rather than fully formulated, irredundant logical axioms. The current formal Lean study therefore restricts independence to N/R/T plus a named local guard profile, and reports full A-F independence as OPEN.

## 4. Lean kernel program and scope

The Lean 4 project is pinned to version 4.34.1. A declared source-state World includes typed acceptance, client-observed output, owner permissions, protected core, dependency target/port, route namespace, tree identity and middleware staging. LocalOK is a deliberately scoped conjunction; NamespaceFree, NoTreeAlias and OrderSafe are three separate propositions.

Finite witnesses badNamespace, badAlias, badOrder each violate exactly one boundary proposition while keeping the other two and LocalOK true; base satisfies all. This is **relative model independence**, not proof of the full original SOLID axioms. The stronger, general theorem proved in the same formalization is the classical no-factorization criterion:

For any observation signature σ:X→Q and decision g:X→Bool, if σ(x)=σ(y) but g(x)≠g(y), then NO map f:Q→Bool satisfies g=f∘σ.

A second general result proves source-continuation kernel inclusion. If a concrete transition step δ, an abstract transition hatδ, and observation maps obey q(δ(s,e))=hatδ(q(s),e) and o(s)=hatO(q(s)), then:

\[
q(s)=q(t)\Longrightarrow
\forall w\in E^*:\quad
o(\delta^*(s,w))=o(\delta^*(t,w)).
\]

This is a necessary condition on any exact deterministic future-edit abstraction. It does not prove a fully abstract quotient exists for arbitrary nondeterministic/historical source edits, and it is a classical simulation/Moore-machine fact. Real Go source fidelity is established separately by native Go tests, **not** by the Lean structure definitions.

No sorry, admit, or additional axioms are permitted in the Lean file. Successful Lean compilation and kernel checking must be confirmed through the dedicated hosted workflow and its checked source SHA.

## 5. Competition with existing theory and publication boundary

The strongest rivals remain:
- CSP with implementation source-reservation constraints; it predicts the regex-disjoint registration rejection once findPattern is included.
- Separation logic/ownership and alias analysis; it predicts the dynamic shared-tree self-mount problem.
- Rely/guarantee and guarded transition systems; they predict staging constraints.
- Go's own source contracts and compatibility rules; they explain behavior rather than merely offering analogies.
- Liskov–Wing behavioral subtyping, Parnas modularity/uses graph and observationally complete source abstractions remain foundational competitors.

These experiments strengthen the **source-backed necessity of more than local SOLID*/extensional HTTP observations** within a bounded χ grammar, but do NOT imply that every global interpretation of OCP or ISP misses this information.

**Verdict:** original Go tests PASS for three independent source guards and a genuinely stronger disjoint-regex source-gluing obstruction. Scoped Lean independence and kernel theory are conditional on hosted check status. Full independent A-F OO axioms NOT PROVED. New foundational law HOLD. P40 OPEN, LAW-R2 NOT_AUTHORIZED.
