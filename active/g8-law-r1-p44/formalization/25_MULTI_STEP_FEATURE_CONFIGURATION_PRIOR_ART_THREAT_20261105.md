# P44 originality challenge: multi-step configurations with feature drift already studied

2026-11-05; EXTERNAL PUBLIC PAPER ABSTRACT/INTRODUCTION REVIEW, NOT A DRIVE-OWNED FULL FORMAL PROOF REVIEW.

White, Galindo, Saxena, Dougherty, Benavides & Schmidt (2014), *Evolving feature model configurations in software product lines*, Journal of Systems and Software 87, 119–136. DOI https://doi.org/10.1016/j.jss.2013.10.010. Original public article and abstract: https://www.sciencedirect.com/science/article/pii/S0164121213002434; academic source page https://www.isa.us.es/publications/type/article-journal/2014/evolving-feature-model-configurations-software-product-lines.

**Actual published contribution:** multi-step software product-line configuration under varying feature constraints, a constraint satisfaction problem mapping, optimization of cumulative and intermediate configuration cost, and feature-model drift as the valid-state model changes between steps. Their named approach MUSCLES handles sequences of valid configurations. This directly predates any P44 claim that the bare act of imposing stagewise constraints and minimizing configuration-path costs is novel.

## Implications for P44

A future paper may NOT claim novelty merely for:
- introducing a sequence of requirements and feature configurations;
- minimizing total cost of multi-step adjustments;
- respecting per-stage validity constraints;
- letting the available feature/edit model evolve in time.

Potential differences that still need ORIGINAL proof and empirical evidence:
1. Source-level concrete patch provenance and actor-specific rights rather than abstract product-line feature assignments.
2. Joint runtime customer trace observers including concurrency, not just Boolean feature compatibility.
3. Independently checked sound source-repair certificate that combines genuine edit-graph coverage and runtime trace coverage.
4. Proof-size/CPU/reuse or transfer improvement versus MUSCLES/CSP and other equally informed established classical methods.
5. Independent actual maintainer task evaluation; not investigator-created examples.

The PDF has **not been located in the accessible Drive filename search**; no canonical Drive file was moved or claimed. To evaluate originality, the source's complete definitions/formulas should be read after acquisition, not merely abstract and introduction. This is a PRIORITY P0/P1 missing paper rather than an optional decorative citation.

Comparison plan: build an exact feature CSP baseline from a genuinely finite, source-supported edit grammar, then compare certificate size, graph coverage, client-observer fidelity and proof checker cost. If the classical CSP computes all required optima equally accurately and efficiently, record TIE.

P44 LAW-R2 remains HOLD.
