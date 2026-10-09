# P37-E4 PRESEAL — Independent Session Algorithms: Gorilla Client-State Cookies vs SCS Server-Store Tokens

**2026-10-10 KST · independent original source preregistration BEFORE test and bridge source · P37 OPEN**

Original immutable inputs:
- `gorilla/sessions@bb4cd60c952a9ce48ea0dc6cc7b282ff79c38263`, `gorilla/securecookie@eae3c1840ec4adda88a4af683ad0f60bb690e7c2`: original `CookieStore.New/Save` signs serialized session values into the cookie, verified by `securecookie.DecodeMulti`. Original source `store.go`, `securecookie.go`.
- `alexedwards/scs/v2@209de6e426de9259665975ce16b91331d228f052`: original `SessionManager.Load/Put/Commit/GetString` puts data in server-side `Store` (default in-memory `memstore`), and issues a random token rather than serialized session values. Original source `data.go`, `session.go`, `memstore/memstore.go`.

The **libraries and algorithms are independently evolved and do not naturally depend on each other**. Our new `tools/p37-e4` integration is research-authored, for transfer testing, not an existing upstream deployment. No production source in either original upstream repository may be edited. Source pins/go.mod and source SHA must be recorded in CI.

**Q_E4**: Existing live application observer asks for value `stage=kept`. Two different *legitimate, synthetic* original cookie types are issued:
- G-cookie: original gorilla CookieStore writes values client-side with test-only key.
- S-token: original SCS manager commits `stage=kept` to server memory store, yielding opaque token.
No security efficacy tests, attack surface probing, brute forcing, or advice for real sessions. Read via original library public methods, not text substring heuristics.

**Frozen expected observation matrix**:
| Reader | G cookie | S token |
| --- | --- | --- |
| G-only original reader | true | false |
| S-only original reader with corresponding existing SCS Store | false | true |
| G∨S project-authored bridge with **both** capabilities | true | true |
| same bridge restricted to **only SCS store**, no G key | false | true |
| same bridge restricted to **only G key**, no SCS store | true | false |

The bridge must **not** grant an invalid cookie access or silently treat an unknown token as a valid session. It should call the declared original reader APIs and select a result only for observed `stage=kept`. It is scoped to finite test fixtures and does not establish any authentication security property.

**Sequential migration graph**: A is writer/issuer with source G→S. B is independent reader/deployer with G→(G∨S), or G→S; only single-owner steps allowed, and `I_live ∧ I_legacy` holds at every checkpoint until an explicit obligation-end event. Prediction:
- both direct single-owner flips without bridge violate a checkpoint;
- B adds original-source API dual bridge first, then A changes writer, preserving both observed values;
- removing G capability before old-cookie obligation ends makes the state unsafe;
- withdrawing *capabilities* changes **allowed edit graph**, not actual historical bytes.

**Strongest baseline**: classical representation independence, authenticated client state vs opaque server-token architecture, API change impact, assume–guarantee, and phased migrations predict **the exact same sign matrix**. Consequently outcome is a stringent new independent-mechanism **transport** but not a DIP49-discriminating new law. The source-graph is bounded to declared original APIs and chosen bridge grammar. Do not extrapolate to all possible source edits.

Tests must be committed *before* bridge source, and native workflow must run Go vet/race over new composite, pinned module verification, source file digests and compatibility test subcases. If original test expectation fails, record negative, repair **implementation or tooling only** under frozen test contract.

**PRESEAL:** `P37_E4_TRUE_INDEPENDENT_SESSION_ALGORITHM_Q_FROZEN__FULL_CAPABILITY_BRIDGE_PREDICTED__CAPABILITY_REMOVAL_NEGATIVE__NATIVE_PENDING__DIP49_IDENTIFICATION_HOLD__LAW_R2_NOT_AUTHORIZED`.
