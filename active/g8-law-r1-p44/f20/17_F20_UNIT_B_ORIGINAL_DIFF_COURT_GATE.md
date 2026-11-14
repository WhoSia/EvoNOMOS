# F20 Unit B — retrospective original-diff research gate

The source patch bodies for chi/httprouter/gin have now been read AFTER the A selection freeze. The tailored posthoc Go tests are ready in `oracles/`, and the pinned parent/post runner is committed. This is **historical evaluation**, not prospective prediction. Original upstream suite may be green at parent even when the oracle sees an affected behavior, and chi's older `TestMuxFind` even had comparator mistakes.

The three maintainers made qualitatively different changes: nested route pattern composition, a configuration-gated allowed-method set, and panic text at a boundary. They cannot be pooled without contract-specific encoding. Source/cost/risk classifications: chi routing functional; httprouter config-dependent header; gin invalid-input error. There is no source-certified actor right, complete context, or full Go proof.

Gate to C3: actual external GitHub Actions fetching exact parent/post, upstream test then new oracle with meaningful expected failure/success. If CI fails on environment/compile before comparison, mark UNKNOWN and retain. For each confirmed case report exact original job/sha, not just a workflow YAML.
