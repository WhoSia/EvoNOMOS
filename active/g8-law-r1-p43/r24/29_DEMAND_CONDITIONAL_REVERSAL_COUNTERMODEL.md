# Conditional architecture preference is not a scalar universal order

Synthetic equal-initial-observation models:
- A0 -> AX costs 1, A0 -> AY costs 5.
- B0 -> BX costs 5, B0 -> BY costs 1.

All transitions are authorized under the same declared app right, and all intermediate/target states satisfy the old-client contract. Demand X prefers A by 1<5, demand Y prefers B by 1<5.

Thus no total order of architectures independent of future-demand distribution follows merely from baseline observational equivalence. If a distribution over future demands and scalar cost semantics is explicitly fixed, an expected-cost ranking may still exist.

This countermodel is intentionally classical and synthetic; it cannot serve as an independently maintained original-software superiority result. The Go test demonstrates the finite numerical reversal only.
