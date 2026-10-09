# P37 — MATH-B and Q23 Post-Native Court: Contextual Congruence, Path Lifting, and Original JSON Lexical-Key Recovery

**2026-10-10 KST · P37 OPEN · POST-EXECUTION VERIFIED · DIP49 IDENTIFICATION HOLD / LAW-R2 NOT_AUTHORIZED**

## 1. Math-B executable counterexamples

[P37-MATH-B #37981820162](https://github.com/WhoSia/EvoNOMOS/actions/runs/37981820162) finished **SUCCESS**. Its [source](../../tools/p37-math-b/context_congruence_counterexamples.py) provides three bounded classical counterexamples: a context family `{id,C}` lacking composition closure where q(x)=q(y) and q(C(x))=q(C(y)) but q(C²(x))≠q(C²(y)); a source edit permitted alone but forbidden after context composition; and a source deadlock forward simulated by a target with an extra successful edit. Original console receipts explicitly contain `P37_MATH_B_CLASSICAL_COUNTEREXAMPLES_PASS`, `P37_MATH_B_REPAIR_CONTEXT_NOT_TRANSPARENT`, `P37_MATH_B_ONE_WAY_SIMULATION_NONCONVERSE`.

[MATH-B formal statement](P37_MATH_B_CONTEXTUAL_CONGRUENCE_AND_REPAIR_PATH_COMPOSITION.md) distinguishes:
- composition-closed contextual observational equivalence from arbitrary observational equality;
- preservation of existential future May by forward authorized graph simulation from its converse, which needs a path-lifting/reflection condition;
- equality of local and composed-context repair sets from a strong repair-transparent context assumption.
These are **classical algebraic/process-semantic conclusions**, not novel laws or generalized to every software context.

## 2. Original Q23 source semantics and before/after provenance boundary

[Pre-source/test Q23 seal](P37_Q23_SEMANTIC_KEY_VS_LEXICAL_PROVENANCE_PRESEAL.md) committed before separate tests and opt-in original-module source files. Original repositories/versions:
- `tidwall/gjson@690362d6edf4bcbde1e9f54d552d3814f1cd5bcb`: existing `Result.Str` supplies decoded key, `Result.Raw` original quoted spelling. [One additive research Go file](../../tools/p37-q23/arms/gjson/p37_q23_source.go) evaluates exactly Q23.
- `buger/jsonparser@36a686d11807c62cd5a30d41b294d66969ea25d8`: existing `ObjectEach` returns decoded semantic key and raw value; existing `Get(doc,"meta")` retains the raw original JSON object bytes. [One additive research Go file](../../tools/p37-q23/arms/jsonparser/p37_q23_source.go) recovers quoted field-key spellings from the raw scalar-only object and aligns them with original decoded ObjectEach traversal, validating semantic alignment and erroring if it fails. No original upstream code file was edited.

The **identical frozen Q23** tests verify `{"meta":{"id":1e+0,"i\\u0064":2.00}}` under first/last policy, reversed order, exact quoted key spelling and original number token, missing members, a nonnumeric semantic-id error, wrong policy, empty input and concurrent immutable read-only requests. The scope is a finite JSON scalar-field grammar with unique top-level meta; this is not a full JSON grammar validator, an all-method interface replacement or a formal proof for arbitrary nested objects.

[Independent original Go Q23 native GitHub Actions #37981761846](https://github.com/WhoSia/EvoNOMOS/actions/runs/37981761846) **completed SUCCESS 2/2 original-library jobs**, with `go test -vet=off -race -count=1 -run '^TestP37Q23' .` **PASS** and scoped `go vet -unreachable=false -unsafeptr=false ./...` PASS. The test files and production additive files are frozen and SHA archived. Original upstream gjson and jsonparser were pinned to exact committed SHAs. This **is not** a claim unqualified legacy jsonparser full Go/vet passes: P36-O12 already recorded pre-existing original PR286 and vet negatives and they are not silently erased by this Q23 source-specific court.

GitHub artifacts:
- gjson Q23 id **11641350297**, digest `sha256:467f4b9a8e6d4e06d75ce967eafb7339ccde83670367ea3282a95be510048bb2`.
- jsonparser Q23 id **11640759561**, digest `sha256:ae9d758c34ea64b72c924715ca56811ec0b139053523a7768b3914764a03805b`.

## 3. Sharp authority-dependent mathematical outcome

Let `L_1` be the raw key `"id"` and `L_2` the raw key `"i\\u0064"`, both decode to semantic name id. The projection `decode(L_1)=decode(L_2)` is many-to-one. Under `Γ_decoded_only`, the repair program sees only the same decoded key and numeric value for the two possible histories (choose equal numeric value in the no-go witness). Any deterministic decoder-only repair must produce the same answer but the new Q23 demands different exact raw spellings, a classical contradiction.

Under `Γ_full`, an authorized source addon can inspect original JSON bytes; both *real independent upstream modules* admit a Q23 source witness. Thus **there is no universal jsonparser information-theoretic impossibility**; the relevant factor is the accessible provenance and authorized path, not nominal module identity.

Strong classic rivals (data provenance, lexical parsing, data abstraction, representation independence, graph simulation) already predict both signs: `Γ_full` possible, `Γ_decoded_only` impossible. DIP-49 still lacks a prospectively differing signature between new-law candidate and strongest classical baseline. **No novel universal structural law claimed.**

## 4. Next structural attack

Now test whether **future repair observational equivalence is a congruence under API authority changes and compositions** by specifying a typed source-context product where state representations are shared, edit permissions differ, and a future demand distinguishes two observationally identical contexts. Freeze strong competing semantics predictions before original code intervention. Do not allow performance microbenchmarks to displace this principal research agenda.

**Verdict:** `P37_MATH_B_CLASSICAL_COUNTERMODELS_NATIVE_PASS__Q23_ORIGINAL_GJSON_AND_JSONPARSER_RACE_2_OF_2_PASS__SOURCE_PROVENANCE_AUTHORITY_BOUNDARY_VERIFIED__DIP49_IDENTIFICATION_HOLD__LAW_R2_NOT_AUTHORIZED`.
