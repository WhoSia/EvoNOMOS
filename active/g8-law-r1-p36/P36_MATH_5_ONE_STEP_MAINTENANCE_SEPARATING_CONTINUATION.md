# P36-MATH-5 — A One-Step Maintenance Separator Between Currently Indistinguishable Source Histories

**2026-10-10 KST · P36 OPEN · stated BEFORE O6's final 1093-word original-Go verdict, but AFTER O3–O5 source results.**

## Old mathematical link: DIP-42 / MATH-1 / DIP-48

Past finite continuation equivalence was studied long before P35 Go proofs. Two runtime states can agree under the **current observer** and yet be separated by a legal continuation. This is classical automata/Nerode theory and finite-observation non-identifiability. We now identify a **concrete original-source maintenance-action witness**, based on the same independent O6 reference contract. No new mathematical theorem is asserted.

## Exact two histories; equal HTTP and equal revision, distinct maintenance futures

Start the exact original Chi STABLE_ORDER source with three same-header route handlers A, B, C registered in that order, publishing immediately. Initial revision is 3. Consider alphabet `R=RegisterNew`, `D=DisableEarliest`, `E=EnableOldestDisabled`.

- `h1 = DDRR`: disable A, disable B, register new handler N2 then N3 after C. The current earliest enabled route is **C**, revision **7**, pending FIFO [A,B].
- `h2 = DDED`: disable A, disable B, restore A, disable A again. The current earliest enabled route is also **C**, revision **7**, pending FIFO [B,A].

Define current observer `O(s):=(HTTP tag on header test, published revision)`. Both states have **exactly the same O(s)=(C,7)**. They do *not* have equal private Go state, nor equal event logs or route counts. The choice of O is explicit, not hidden or retrofitted.

Under the same single legal future maintenance action `E`:
- `O(h1·E)=(A,8)`, since earliest pending is A.
- `O(h2·E)=(B,8)`, since earliest pending is B.

Thus a **one-letter distinguishing continuation** exists despite equal present functional response and revision; `h1` and `h2` are distinguished at depth 1 of the richer development-action alphabet. Both histories have length four and both have four successful actions, neutralizing a trivial revision/event-count separator. Note: the two histories have different numbers of active registered routes; an observer with a route-count introspection field could distinguish them earlier. The theorem is strictly relative to O, not a declaration of all-observer behavioral equivalence.

## Elementary exact impossibility lemma (classical)

Suppose `f : Output × Action → Output` were a deterministic Markov update law using **only O(s)**, and preserving the next output of the real source under every allowed action. Then from `O(s1)=O(s2)=(C,7)`:
```
f((C,7),E) = (A,8)
f((C,7),E) = (B,8)
```
contradiction `A≠B`. Hence no such observer-only deterministic state update f is faithful on this two-state witness. It does NOT mean that the full original source process is non-Markovian: augment the observer with the pending FIFO and registered order, and the future update can be Markov at that enriched state.

**DIP-50 readout**: O must be mapped by a fixed projection from real HTTP response and `Stats()` on the exact source prefix; our O6 original-Go reference checks every prefix of both `DDRR E` and `DDED E` (all words length at most 6). Do not upgrade this witness to verified native until O6 [CI #37966139703](https://github.com/WhoSia/EvoNOMOS/actions/runs/37966139703) confirms STABLE_ORDER all 1093 words. The separate successful O4/O5 tests already support the core transitions but do not expose this exact same-revision pair in one audit.

## Implication for discovering genuine software structural laws

Current outputs, apparent revision progress and static SOLID heuristics are **incomplete sufficient statistics** for which future change a design can correctly support. Hidden pending edit provenance and relation-preserving state can matter. This is a concrete experimental argument for upgrading structural evaluation from instantaneous scalar scores to *maintenance-contextual continuation classes*. The mathematical mechanism remains classical automata and contextual equivalence, not a beyond-classical new theorem or automatic winning architecture. An advanced classical history-aware competitor anticipates this outcome, so `DIP49_NOVEL_LAW_PAIR_HOLD` continues.

**At prereadback:** `TWO_EQUAL_CURRENT_OBSERVATIONS_SEPARATED_BY_ONE_FUTURE_MAINTENANCE_ACTION__O6_NATIVE_PENDING__CLASSICAL_NERODE_THEORY__LAW_R2_NOT_AUTHORIZED`.


## 2026-10-10 — Original Go confirmation of the projected history witness

This is the post-result audit, not a rewrite of the old prediction. [Original Chi four-arm O6 #37966139703](https://github.com/WhoSia/EvoNOMOS/actions/runs/37966139703) ended **4/4 SUCCESS**. In the STABLE_ORDER source arm, the logically independent reference test evaluated **every word length ≤6** (1,093 words, all action prefixes) and recorded full PASS (artifact 11633242485 SHA256 `4d840ab25fbe9a3c919eb10b5aa6250b9bf2e1d681997e7bd6b95d081492c3ea`). Hence the explicitly named `DDRRE` and `DDEDE` continuations were included in the original Go source conformance test and agree with the logical model. The two states are equal under the declared present projection `O=(HTTP C, published revision 7)` and differ after `Enable` (A vs B at revision 8). Their full actual Go states remain different; this is a **relative observer** failure of a Markov sufficient statistic, not a general impossibility of Markovian software models. No beyond-classical discovery.
