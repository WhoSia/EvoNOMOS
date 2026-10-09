# P37-MATH-H — Ownership-Capability Bisimulation and Two Independent Obstructions to Global Repair Congruence

**2026-10-10 KST · AFTER E4 original-go native SUCCESS · P37 OPEN · CLASSICAL THEOREM / NEGATIVE CONTROLS**

## 1. The actual new structural coordinates (not a scalar SOLID score)

A typed software change state must include more than the current exposed behavior:
```
X = (source representation, source-derived operations, owner-edit relation Γ,
     accessible capability handles K, invariant I, demand family D,
     allowed composition contexts 𝒞).
```
An implementation can be locally excellent under conventional class/interface criteria and still lack a cross-owner authorized path. A readable historical cookie and **the authority and auxiliary state to interpret it** are different facts. In E4, Gorilla CookieStore holds application values in a signed client-side cookie, while SCS uses a server-side session store keyed by an opaque client token. These are independently evolved original algorithms (not just two adapters wrapping the same cookie codec).

## 2. H1 — capability- and owner-labeled repair bisimulation (classical)

Let states of two software systems carry (i) present observations, (ii) invariant `I`, (iii) owner+capability labels on authorized edits `s —(owner,κ)→ s'`, and (iv) acceptance of future demands `d`. If relation `R` preserves all four and is a labeled **strong bisimulation** (every permitted source edit has a matching same-labeled edit in the other system to R-related state, **in both directions**), then for every finite edit path preserving the invariant, its image/reverse-lift is a finite matching path preserving the invariant. Consequently `May(s,d)⇔May(t,d)`. With matched explicitly quantified reachable terminals and nonempty reachability, a nonvacuous Must-family also transfers.

Proof: induction on path length in each direction; invariant and target acceptance preserved at matching intermediate states. **This is standard bisimulation, not a new theorem.** Strong bisimulation may be overly restrictive for actual software repair workflows; weak/stuttering matches require separately declared closure and valid intermediate invariants.

Present semantic equality alone does not establish this bisimulation. In the E4 finite declared contexts, both original session algorithms return `stage=kept` when their own capabilities are available, yet a *SCS-store-only* reader distinguishes the two cookie representations. Thus the current semantic quotient fails under a future capability-restricted context.

## 3. H2 — rectangularity of I and independence of Γ are INDEPENDENT premises

Two local owner states 0/1, starting (0,0), target (1,1), and both local edges 0→1.

**Countermodel A: rectangular I but Γ nonproduct.**
Let all four combined states satisfy I=true (maximally rectangular). However global permissions allow A's change ONLY if B=0, and B's change ONLY if A=0. From (0,0) one can reach (1,0) or (0,1), but neither last edit is authorized; (1,1) is unreachable. Both owner-local May predicates are true, but global May false. A separate coordinated joint step would be a NEW Γ. This is a minimal *authority obstruction* even without incompatibility or information loss.

**Countermodel B: independent Γ but nonrectangular I.**
Let Γ be the complete asynchronous product. Let I contain only the start and goal (0,0),(1,1), excluding crossed/mixed states. Again no safe sequential path despite both local 0→1 edits. This is an *invariant obstruction* even without an authority restriction.

**Countermodel C: both independent.**
With rectangular I=true and complete async Γ, the two local edges have a safe combined path to (1,1), consistent with F theorem.

Hence **both** exact compatibility-factorization and cross-owner edit independence must be checked; no static SRP/ISP/DIP dependency rule automatically implies either property. All countermodels are classical product automata, access-control and assume–guarantee facts.

## 4. E4 original independent algorithm receipt and strongest rival

[E4 pinned native original-Go result](P37_E4_INDEPENDENT_SESSION_ALGORITHMS_NATIVE_VERDICT.md): original `gorilla/sessions@bb4cd60c952a9ce48ea0dc6cc7b282ff79c38263` with `securecookie@eae3c1840ec4adda88a4af683ad0f60bb690e7c2`, versus unrelated `alexedwards/scs/v2@209de6e426de9259665975ce16b91331d228f052`. An EvoNOMOS-authored dual-library reader uses only public original Go APIs. Original Go/race/vet and full SCS race suite PASS; source-linked capability graph explicitly probes `securecookie.DecodeMulti` vs SCS `doStoreFind`, `doStoreCommit`, and random token generation. The wrapper is a researcher-built integration; there is NO upstream natural direct dependency between these algorithms, and **no cryptographic security claim**.

The strongest classical comparator knows signed client-state vs server-store token representation, APIs, knowledge/access capabilities, edit permissions, and per-checkpoint legacy obligations. It predicts the E4 results; H is a **well-grounded structural synthesis but not identified as beyond-classical novelty**. To distinguish DIP49's future law candidate genuinely, one must preregister different conditional predictions from a *complete* strong baseline on independent fresh sources, not omit familiar authority or representation theory from the rival.

**Verdict:** `P37_MATH_H_CLASSICAL_CAPABILITY_BISIMULATION__RECTANGULARITY_AND_GAMMA_INDEPENDENCE_ORTHOGONAL__E4_TWO_TRUE_SOURCE_ALGORITHMS_PASS__DIP49_HOLD__LAW_R2_NOT_AUTHORIZED`.
