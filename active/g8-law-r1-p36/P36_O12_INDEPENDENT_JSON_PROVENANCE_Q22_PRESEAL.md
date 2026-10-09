# EvoNOMOS P36-O12 — Two Independently Evolved JSON Parsers: Lexical Provenance, Duplicate-Key Policies & Repair Authority

**2026-10-10 KST · FROZEN Q22 TEST CONTRACT BEFORE TREATMENT SOURCE · P36 OPEN.**

## Original independent non-router source evidence

This court deliberately leaves all router ecologies. Original independently authored and evolved Go packages:
- [tidwall/gjson](https://github.com/tidwall/gjson) at exact commit `690362d6edf4bcbde1e9f54d552d3814f1cd5bcb`, [gjson.go](https://github.com/tidwall/gjson/blob/690362d6edf4bcbde1e9f54d552d3814f1cd5bcb/gjson.go): `ParseBytes`, `Result.Get`, `Result.ForEach`, `Result.Raw` with structured result metadata.
- [buger/jsonparser](https://github.com/buger/jsonparser) at exact commit `36a686d11807c62cd5a30d41b294d66969ea25d8`, [parser.go](https://github.com/buger/jsonparser/blob/36a686d11807c62cd5a30d41b294d66969ea25d8/parser.go): `ObjectEach` returns raw value byte slices and ValueType / offset metadata.

These are independent original implementations with distinct public APIs. The next opt-in research methods will be **project-authored**, not maintainer-authored historical repairs. Original upstream file bytes must remain unchanged, all previous original tests should pass. No claim that duplicate object keys have a universally mandated first/last JSON semantics; that is the *new explicit client policy*.

## Q22: the SAME exact new client acceptance in both packages

New opt-in one-file API within each original package:
```
func P36O12SelectRaw(doc []byte, policy string) (token string, found bool, err error)
```
- `policy` exactly `first` or `last`, other/empty policies error;
- Document grammar for positive acceptance: syntactically valid JSON **root object** with a **unique top-level `meta` object**, containing zero or more fields including zero, one or multiple plain literal `"id"` members whose values are valid JSON **number tokens** (not string, bool or null). Object fields may have unrelated scalar values. Additional nested object or arrays are out of positive-scope initial Q22, except later independent Q23.
- `first` returns first original `id` numeric **lexeme**, `last` returns last, **without normalizing number spelling**; `1e+0` and `2.00` must survive exactly. If no `id`, output token empty, found false and nil error. Unsupported policy and a matching `id` with non-number value must produce an error (entire operation error, no silently discarded values). A nil/empty doc returns error. Input byte slice must not be mutated.
- Exact frozen cases:
  - `{"meta":{"id":1e+0,"other":9,"id":2.00}}`: first `1e+0`, last `2.00`.
  - `{"meta":{"id":-0,"id":3E-2,"id":10}}`: first `-0`, last `10`.
  - `{"meta":{"other":1}}`: no match.
  - `{"meta":{"id":"1","id":2}}`: both policies error, because Q22 declares ALL occurrences numeric.
  - `{"meta":{"id":4}}`: first/last both `4`.
  - document copied before and compared byte-for-byte after operation, and concurrent read-only calls safe.
- Strict full-document validation is OUTSIDE this Q22; malformed JSON except nil/empty is separately reserved for Q23. Do not equate a fast partial parser with a full JSON grammar validator.

Observe `O=(found, original-number-lexeme, error-class, unchanged-source)`. Quantitative measurements: same hosted Go version/runner with both pinned libraries, original module full `go test ./...`, `go test -race ./...`, `go vet ./...`, fixed Q22 positive/negative. Benchmark fixed `id` at beginning/end and duplicate count, independent `ns/op, B/op, allocs/op`, and whole build+N queries if useful. Native originals are not forcibly modified; Q22 extensions must be separate additive files. If a source requires repair, **only repair the source extension**, do not change frozen test contract.

## Typed competing hypotheses; what is and is NOT identified

`B_info+scan` (strong **classical** alternative) models exact preservation of JSON numeric tokens, API exposure of raw slices, full-vs-partial scans, duplicate-key semantics and lexical conversion. It predicts that **both packages can satisfy Q22** through their existing public provenance-bearing iteration without core edits. Raw byte availability is a source-level reason, not a surprising novel principle.

`H_γ` (EvoNOMOS *candidate*, NOT identified): with same current read semantics, source-edit authority `Γ`, typed provenance boundary and future change family determine a **repair-option survival topology** that could predict beyond `B_info+scan`'s raw information and operation counts alone. BUT a *maximally strong source-aware classical APR/data-refinement model* `B_*` also conditions on Γ and API, so **the present Q22 does not yield `σ(H_γ)≠σ(B_*)`**. No pretend contrast with a straw static scalar or no-history model. To earn DIP-49 identification, preregister a genuinely distinct future Q23 query and fixed quantitative or repair-survival signatures for Hγ and strong B* on novel holdout sources, after baseline calibration, before treatment. If no honest differing predictions can be articulated, maintain IDENTIFICATION HOLD.

## Disproof and chronology

Results may be non-PASS because of actual parser API behavior; do not relabel as structure laws. All original module sources and target commits fixed before testing, Q22 prior to additive source. Existing v1 Go APIs and third-party migration constraints persist, even if new opt-in method succeeds.

**Seal:** `P36_O12_NON_ROUTER_Q22_BEFORE_SOURCE__STRONG_CLASSICAL_INFORMATION_RIVAL_PREDICTS_BOTH_POSITIVE__H_STAR_NOT_IDENTIFIED__P37_NAME_ONLY_PREPARATION`.
