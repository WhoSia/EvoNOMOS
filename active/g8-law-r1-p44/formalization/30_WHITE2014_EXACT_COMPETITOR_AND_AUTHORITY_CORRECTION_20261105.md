# P44 White 2014 original mathematical-source review: refine the claimed boundary

## Source provenance
Original White, Galindo, Saxena, Dougherty, Benavides & Schmidt (2014), `Evolving feature model configurations in software product lines`, Journal of Systems and Software 87, 119-136, DOI 10.1016/j.jss.2013.10.010. [Now-owned canonical original PDF](https://drive.google.com/file/d/1n4vr5-CR7P-_HHBzpkmHmoNzFqzmghDp/view). Acquired from Research OS 00_INTAKE and verified moved to 10_PAPERS, preserving file ID.

## Specific original sections actually inspected
- §3.1, general formal model: a multi-step configuration instance is given as a **6-tuple** containing edge constraints E, point constraints PC, a cost-change function of two configurations, maximum number of steps K, initial constraints and final constraints. The actual PDF formatting must be visually checked before transcribing exact tuple symbols because text extraction damages math glyphs.
- §3.3 edge constraints restrict inter-step changes, including cost budgets; point and edge constraints may change with stage.
- §2.5 discusses feature model drift, including new features, removals and new constraints. Drift is distinguished from individual configuration changes.
- Intro and contributions: MUSCLES maps multi-step product-line configuration into a CSP with optimized path selection and is an extension of White et al. 2009 prior research.
- §6.4 directly reports threats from random/generated feature models and mismatch to industrially realistic constraints.

## Why this is a strong classical rival
For a fixed finite feature domain, configuration validity, stagewise constraints and inter-step costs can be encoded as CSP/optimization. A P44 proposal presenting only a multi-step graph and optimal path will not exceed this earlier literature. Even model drift itself is already captured, so the phrase "adaptive future requirements" is insufficient for novelty.

A potentially different, still unproven source task is producing a *proof-carrying relation* between actual source edit operations, runtime behavior/old-client contract, editor rights and abstract features. It must be source-sound and materially more useful than equally informed CSP + program verification.

## Change in research design
- Compare the new F14 closed Go AST grammar with an exact classical source graph search; no advantage is expected in the trivial instance.
- A future richer fragment should map source-defined structural dependencies to feature constraints and compare exact CSP vs proposed source certificate under identical observers and authorized edits.
- Do not claim that a generated feature-model benchmark simulates maintained Go source.
- Prior-art priority: formally review White 2014's formulas/solver and White et al. 2009 predecessor before reporting any unprecedented multistep mechanism.

**Novelty verdict:** multi-step evolutionary minimum-cost problem is CLASSICAL; source verification contribution OPEN; P44 G1–G7 OPEN, LAW-R2 HOLD.
