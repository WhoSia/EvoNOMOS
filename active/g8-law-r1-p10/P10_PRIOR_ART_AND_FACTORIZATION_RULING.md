# LAW-R1-P10 — Prior-Art Kill and Factorization Ruling

## Target

P9 promoted the decision state:

`Pi(X,G,E)`

with:
- X = decision context,
- G = structural geometry,
- E = empirical/world-contact evidence.

P10 asks whether X and G merely coexist in the state representation or whether the action policy must model their interaction.

## Fresh matched-geometry holdout

Meson-python #912 was frozen before resolution reveal.

Precommit:
`active/g8-law-r1-p10/P10_MESON912_PRECOMMIT.json`

Resolution:
- mesonbuild/meson-python#914
- merge `49a633f0cac62bf2fe21ea6c15d00450a22bd5e2`

The same package/dependency geometry succeeds or fails depending on toolchain/environment provenance. The repair does not globally keep or remove all build RPATH entries. It preserves absolute paths needed for external installed dependencies while removing entries that only refer to the build tree.

Result:
**MATCHED_GEOMETRY_CONTEXT_EFFECT_SUPPORTED.**

## Development matched-geometry donors

### FFXI-Mission-Toolkit #269

Implementation moves to a package boundary while preserving the old root path as a compatibility CLI/import shim.

Merge:
`7d313401524a8dc003d6c1d061b3d3e664aff41e`

### OpenChia #10

A comparable namespace/package migration deliberately performs a hard break with no compatibility package, shim, fallback or dual-name detection.

Merge:
`4adb2a1b2de8d9b5c2bc133c32fa47e150ad7647`

These are development donors only, but show that migration geometry alone does not determine preservation policy.

## Matched-context discrimination donors

OpenPencil #624 exposed two independent failures in the same external installed-package context.

They required distinct structural interventions:

1. PR #612, merge `5689eccc0ca4556ea6f17fddc22933f3d9c06792`:
   remove published export conditions that target files absent from the tarball and add packed-release export validation.

2. commit `88c1077071328b8df68f282543f16e20e97930b4`:
   replace Bun-only filesystem globals in a Node-compatible CLI with node:fs/promises and enforce the runtime boundary.

Thus approximately matched X does not collapse distinct G into one generic compatibility action.

## Semantic-compatibility donor

RConsortium/S7 #734, merge `245aaf46355a48403ad580b366b817a9c4191851`, shows that a plain exported alias may be insufficient when downstream contracts depend on nominal class identity. The repair adds deprecation helpers that unwrap to the replacement across constructor, signature, inheritance and external-class resolution contexts.

## Prior-art kill

The existence of interaction effects is not novel.

Configurable-systems and software-product-line research already models:
- option interactions,
- environment/input sensitivity,
- configuration-specific performance changes,
- transfer across environments and releases.

Input-aware performance studies explicitly show that the effect of configuration can depend non-monotonically on input/environment, and performance-influence models include interaction terms.

Therefore P10 does not claim novelty for:
- X×G interaction,
- effect modification,
- context-conditioned configuration behavior,
- interaction-bearing performance or adaptation policies.

## Ruling candidate

The evidence rejects **policy separability**, not **state factorization**.

Allowed:

`state = (X,G,E)`

Rejected:

`Pi(X,G,E) = combine(Pi_X(X,E), Pi_G(G,E))`

as a general assumption.

Retained:

`Pi` may contain interaction-bearing rules over the joint state `(X,G,E)`.

The Meson holdout gives a bounded prospective witness that action selection depends jointly on structural path class and environmental/toolchain context.

No world in P10 shows the same materially specified `(X,G,E)` mapping to incompatible actions.

Therefore:
- interaction term: REQUIRED in bounded cases,
- state ontology: SUFFICIENT under current evidence,
- missing coordinate: NOT REOPENED,
- LAW-R2: NOT AUTHORIZED.

Candidate verdict:

`PASS_INTERACTION_REQUIRED__STATE_FACTORIZATION_SURVIVES__POLICY_SEPARABILITY_REJECTED__R2_NOT_AUTHORIZED`
