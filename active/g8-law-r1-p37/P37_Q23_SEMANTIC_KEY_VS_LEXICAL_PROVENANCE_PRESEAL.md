# P37-Q23 — Semantic-Equal Keys, Lexically Distinct Provenance, and Authority-Limited Recovery

**2026-10-10 KST · prospective source/test preseal · P37 OPEN.** This is about source information preservation and future repair graph structure, **not optimizing parser speed**.

## Two truly independent original Go baselines

Exact pins unchanged from P36-O12: `tidwall/gjson@690362d6edf4bcbde1e9f54d552d3814f1cd5bcb`, `buger/jsonparser@36a686d11807c62cd5a30d41b294d66969ea25d8`. Original gjson object iteration exposes semantic key `Result.Str` and original quoted key spelling `Result.Raw`; original jsonparser `ObjectEach` exposes decoded key bytes and raw value bytes, while the caller retains the *full JSON input* and can use original `Get(...,"meta")` to inspect raw object bytes. The difference is **API exposure**, not absence of information from the complete input.

## Identical new Q23 source contract

Opt-in one-file package extension:
```
func P37Q23SelectOriginalKey(doc []byte, policy string) (rawKey string, rawValue string, found bool, err error)
```
For **valid JSON root object**, unique top-level `meta` object, with scalar-number/string members (no nested values in this initial court), select the first or last member whose **decoded semantic key is `id`**, treating quoted `"id"` and `"i\\u0064"` as the same name. Return its exact original **quoted key lexeme** and exact original numeric value lexeme; all occurrences of semantic id must be numeric; nil document, missing meta or invalid policy are errors; missing id yields `found=false`, empty lexemes, nil error. Do not modify caller source. Positive tests include:
- `{"meta":{"id":1e+0,"i\\u0064":2.00}}`: first returns (`"id"`,`1e+0`), last (`"i\\u0064"`,`2.00`).
- `{"meta":{"i\\u0064":-0,"id":3E-2}}`: first (`"i\\u0064"`,`-0`), last (`"id"`,`3E-2`).
- no id, unescaped and escaped key elsewhere, and a semantic-id string-type negative case.
- concurrent immutable read-only calls PASS under Go race.

This is a **restricted grammar**, not a general JSON validator or parser replacement. Direct raw source reconstruction is permitted under `Γ_full` (one additive source file, full original bytes accessible). Under alternative `Γ_decoded_only` (only decoded key/value callback, no original input, no offset or event log) raw key spelling cannot be reconstructed for both histories `"id"` and `"i\\u0064"` from identical decoded key `id`, by classical indistinguishability. **The original jsonparser Q23 implementation is under Γ_full, not Γ_decoded_only; it must not be called impossible.**

## Relationship to P37 structural math and rival theories

This is a source-level counterfactual test of the information boundary that determines authorized future repair paths. Claiming `gjson` is universally more repairable than `jsonparser` would be false when full input and new source code are allowed. The positive predictions of strong classical source provenance/representation theory are that **both can repair Q23 under Γ_full**, but decoded-only interface cannot recover lexical spelling under Γ_decoded_only. Our hypothesis does not yet predict a different outcome from that strong classical competitor. Record a **DIP49 HOLD** unless a fresh, strongest-rival-separating query is identified.

Native source validation: exact original Go full/qualified baseline checks as in Q22, independent frozen Q23 contract tests, race, checks no original upstream source mutation. The known jsonparser original vet warnings and PR286 original failing tests must be separately qualified, not hidden.

**PRESEAL verdict:** `P37_Q23_FROZEN__FULL_INPUT_RECOVERY_EXPECTED_BOTH__DECODED_ONLY_NO_GO_CLASSICAL__NATIVE_UNTESTED__DIP49_HOLD`.
