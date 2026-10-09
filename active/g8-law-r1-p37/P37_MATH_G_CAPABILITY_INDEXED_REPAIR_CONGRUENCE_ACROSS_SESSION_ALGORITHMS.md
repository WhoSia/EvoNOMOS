# P37-MATH-G — Capability-Indexed Repair Congruence Across Distinct State Representations

**2026-10-10 KST · PRE-NATIVE MATH · P37 OPEN · DIP49 IDENTIFICATION_HOLD · LAW-R2 NOT_AUTHORIZED**

## Generalization from key rotation to genuinely different algorithms

E1–E3 shared the SAME underlying Gorilla codec even when HTTP integrations differed. E4 instead juxtaposes two independently implemented session representations: `gorilla/sessions` CookieStore saves session values in an authenticated client cookie; `alexedwards/scs/v2` stores values server-side and passes a random opaque session token in a cookie. The two algorithms/representations are distinct; a project-authored bridge/consumer is necessary. The sources are independently evolved, but **they are not naturally dependent on each other**. No source change or naturally integrated production application is asserted.

Let representations be typed protocols G and S with issuing programs W_G and W_S and reader capabilities `K⊆{k_G,store_S}` (a writer-issued G cookie can be interpreted using the G verification key; an S token requires a handle to the matching SCS server store). Let B be the restricted set of source-edit programs allowed to call **only** a finite exposed list of original library APIs and use supplied capability handles. Let `I_{live}(W,R)` mean the reader retrieves declared semantic value `stage=kept` from the current issuer's legitimate cookie; `I_{legacy}(R)` means it also retrieves that same value from the pre-upgrade G cookie. Existence of bridge is relative to B, these capabilities, and finite declared fixtures.

**Operational reachability signature:** `May_{Γ(K),I}((W_G,R_G),(W_S,R_{G∨S}))`, requiring each intermediate state preserve live and legacy values. Owner A edits the issuer from G to S, owner B edits the verifier from G-only to dual G∨S. Both edits are role-specific and successive; no joint atomic step is assumed.

### Proposition G1 (typed bridge witness, no novelty claim)
If B can install a dual verifier whose behavior is the union of the original G reader and the original S reader on the **disjoint admitted protocol sources**, and K includes both G verification and the original *same* SCS session store, then
```
(W_G,R_G)→_B(W_G,R_{G∨S})→_A(W_S,R_{G∨S})
```
is a safe path for the specified finite existing G cookie and newly issued S token. Proof by direct acceptance checks on the two representatives; this is **not** a universal proof of safe union for arbitrary untrusted cookies, ambiguous parsing, replay, name collision, expiry, authentication context, or storage loss. Those additional obligations must be modeled independently.

### Proposition G2 (capability withdrawal is not information destruction)
If the historical G cookie still exists but B loses authorized access to G verification key, the G source bytes remain present but the given Γ(K) has **no permitted G decoding operation**. Therefore the particular bridge program is unavailable under this restricted source-edit grammar. This is **not an information-theoretic impossibility of cryptographic key recovery**, nor impossibility under an arbitrary repair grammar, since a different permitted key service, logged decoded values, or a separate migration flow could change the premise. It is a capability-limited *reachability* fact.

### Proposition G3 (congruence depends on composition capability preservation)
Suppose two components match only on the current semantic observation `stage=kept`. They need not be future-contextually congruent: a context may require verification of old G cookies after A begins issuing S tokens, or may withdraw B's old G key or server store. Conversely under a restricted context class that preserves both capability handles and dual-reader behavior, a declared finite-session observation equality can be preserved. This is classical contextual equivalence / representation independence, not a novel theory.

### Strongest classical rival and prospective signatures

An actual strong classic `B_*` knows original module-level APIs, signed client state vs server-token semantics, explicit storage and key capabilities, edit-authorization grammar, and per-checkpoint compatibility. It predicts (i) pure cross-decoding fails, (ii) dual-authorized reader bridges finite representative sessions, (iii) capability withdrawal blocks the declared bridge but leaves the cookie bytes intact, and (iv) the staged graph differs with Γ. The H-candidate as currently specified makes **the same** predictions. These cases are **calibration and transfer of abstraction**, not qualifying DIP49 law discrimination. A future law challenge requires a new source-derived structural invariant and a *genuine* sealed prediction where `σ(H)≠σ(B_*)`.

**Novelty gate:** E4 original native source may refute the proposed practical bridge (e.g. interface subtleties); report failures as experimental data, do not rewrite this preregistered theorem to force success.

**PRESEAL:** `P37_MATH_G_CAPABILITY_TYPED_BRIDGE_CONDITIONAL_CLASSICAL__REAL_TWO_ALGORITHMS_NEXT__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.
