# P37-C1D — Post-C1 Controlled Counterexample: Direct Concrete Dependency with Preserved Historical Provenance

**2026-10-10 KST.** This follow-up is sealed AFTER knowing C1 passed, BEFORE implementing the new concrete-dependent module. It is a **new declared negative control**, not an independent blinded law-identification holdout.

### Exact hypothesis

Create another owner-A HTTP ingress **directly typed against concrete `*archive.Store`**, instead of the prior `ingress.StorePort` abstraction. The high-level handler package must **import the concrete low-level archive package**; this violates a narrow, explicit static-code formalization of DIP (`high-level owner source imports concrete archive implementation`) but says nothing about every philosophical interpretation of SOLID.

Reuse the actual upstream chi router by delegating route construction to the existing `ingress` component. Forward original raw JSON bytes on first receipt. Test two histories with semantic ID 7 and distinct quoted lexical spellings `"id"` and `"i\\u0064"`. Identical original legacy GET id/revision, and newly repaired `archive.OriginalKeyAt(0)` returns the original spelling for both.

**Expected:** DIP-formal-static dependency predicate false; historical Q passes under `Γ_B` because original source was retained. This shows **that predicate is not a necessary condition for one particular future raw-history repair**. It does not establish that DIP can safely be ignored in general. Compare with the previous DIP-conforming interface-directed ingress which can still lose historical provenance. Strong classical information theory predicts both.

Freeze [separate test](../../tools/p37-c1/concrete_control_test.go) before [new concrete adapter](../../tools/p37-c1/concreteingress/concrete.go), original C1 experiment files unchanged. Native Go test/race/vet in a NEW workflow; source and test SHA archived.

**FROZEN:** `P37_C1D_STATIC_DIP_NEGATIVE_CONTROL_AFTER_C1__SOURCE_PENDING__CLASSICAL_PREDICTION__DIP49_HOLD`.
