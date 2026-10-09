# P37-MATH-D — The Authority–Provenance Cut Obstruction for Historical Repair

**2026-10-10 KST · A COMPOSITIONAL CONDITIONAL THEOREM WITH CLASSICAL INFORMATION-FLOW ANCESTRY; NOT IDENTIFIED AS A NOVEL LAW.**

## Set-up

Take a finite directed **typed** module-event DAG G=(V,E), with source histories H at input ports, deterministic information-transfer maps on each edge, owner labels on edit loci, and authorized future repair relation Γ_B confined to module B. There is no event replay, side channel, external log, prearranged hidden key oracle or mutation of *already retained* historical state. All relevant routes by which historical source information can reach an authorized future B reader are included; concurrency/nondeterministic channels require a separate semantics, not this theorem.

For historical source h, write X_B(h) for **the entire state available to B** at the moment future repair starts (not merely the present HTTP response). A future demand d asks for a value t(h) distinguishable for two histories.

Call K an **authority-observation cut** if every path from source history h to the authorized future B reader crosses at least one channel in K and no unmodeled B-accessible historical provenance exists.

### Theorem D1 — noninjective historical cut forbids uniform B-only repair

If two histories h1!=h2 yield **the same available state** X_B(h1)=X_B(h2) after passage through K, but t(h1)!=t(h2), then there is **no single deterministic Γ_B-only future reader** r such that r(X_B(h))=t(h) for both histories.

**Proof.** Determinism and identical X_B force r(X_B(h1))=r(X_B(h2)); prescribed demands require distinct outputs, contradiction. This is the factorization obstruction. The cut condition is useful only to establish equality of the *complete authorized readable state*, not from current GET equality alone.

**Graph sufficient premise.** For a deterministic acyclic input flow, if every history-dependent B-accessible output factors through a common noninjective channel u:H→Z for which u(h1)=u(h2), then X_B factors through u and the theorem applies. It is invalid to argue that the presence of *one* lossy path proves the theorem while another accessible raw-log path survives; all bypass paths must be accounted for.

### Theorem D2 — preserved provenance is necessary for this uniform demand but not sufficient for repair

If a B-accessible retained representation distinguishes h1/h2, that removes D1's information-theoretic obstruction. It does **not** by itself guarantee a permitted Γ_B repair: ownership may forbid reading it, interfaces may prohibit adding methods, immutable legacy invariants may block safe composition, or the repair search might be undecidable. A **legal decoder and invariant-preserving source edit path** must additionally be demonstrated. This is the key difference between raw information potential and actual source repair reachability.

### Theorem D3 — timing is part of the structural state

Changing owner A's forwarding behavior after an event can preserve provenance of **subsequent** inputs, yet has no retroactive effect on the already collapsed X_B(h). Thus a repair path that changes upstream acquisition in the future is not an inverse map for a previously irreversible history. This is under the explicit no-replay assumption, not a universal claim about databases with audit logs or event sourcing.

## Real source instantiation and exact guard

[P37-C1 frozen contract](P37_C1_TWO_OWNER_CHI_GJSON_HISTORICAL_PROVENANCE_PRESEAL.md) and actual [project-authored two-owner original-library composition](../../tools/p37-c1/) instantiate:
- real pinned Chi inbound HTTP routing and project-written owner-A `ingress.StorePort` API;
- project-written owner-B archive holding semantic ID/revision and optional defensive copy of original JSON bytes, using real gjson `Result.Raw` for future keys;
- the two raw histories `{"id":7}` and `{"i\\u0064":7}`, both produce present `GET /state: id=7,rev=1`;
- forwarding policy retains distinct X_B, lossy forwarding collapses them into one X_B;
- Γ_B reader recovery possible in retained history, impossible uniformly in collapsed hidden histories; changing ingress forwarding only fixes later events.

The native unit test implements finite worlds and selected future-reader witnesses; this does **NOT** enumerate every possible Go source edit or mechanically prove the theorem for all Go programs. [Machine-readable owner graph](../../tools/p37-c1/model/owner_repair_graph.json) is a bounded formal model authored against the code, **not AST-extracted**.

## Relation to SOLID

A dependency-inverted, client-specific Go interface graph can still implement the **lossy** noninjective cut. A direct concrete high-to-low dependency can retain raw historical state, allowing one previously requested B-only repair. Therefore, no SOLID-style interface-only predicate is sufficient to guarantee this historical future demand; a narrow static DIP predicate is also not necessary for this *one* future demand. The broader [MATH-C restricted embedding](P37_MATH_C_SOLID_RESTRICTED_EMBEDDING_AND_PROVENANCE_COUNTERTHEOREMS.md) makes the meaning of 'SOLID is a special case' precise: formal SOLID class/interface designs constitute a restricted subdomain of typed repair systems, with observation and edit traces preserved under exact encoding. This is **not** a proof that EvoNOMOS has surpassed all classical design theory.

## Strong classical opponent

Theorem D1 is a deterministic information-channel factorization statement, and the provenance-cut formulation is a standard information-flow / dependency-graph shape; D2 is the familiar information-versus-authority sufficiency distinction. A genuinely new law would require nontrivial additional transportable predictions against strong classical program slicing, data provenance, noninterference and contextual semantics. No independent source-separated predictive signature exists yet.

**Verdict:** `P37_MATH_D_AUTHORITY_CUT_CONDITIONAL_THEOREM__SOURCE_LINKED_NATIVE_WITNESS__FULL_GRAPH_PROOF_ASSUMPTION_REQUIRED__SOLID_A_RESTRICTED_DOMAIN_ONLY__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.
