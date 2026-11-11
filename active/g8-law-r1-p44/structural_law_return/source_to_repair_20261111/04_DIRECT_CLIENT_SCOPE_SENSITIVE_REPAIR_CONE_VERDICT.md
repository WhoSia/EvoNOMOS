# EvoNOMOS — When an Existing Direct Client is Protected, an Actual Source Repair Cone Contracts

**2026-11-11 KST · original Go source run 10/10 complete · correct contract-scope verdict · no new math or architecture law · LAW-R2 HOLD**

## 1. Material scientific result

Previous [ten native source repairs](02_ALL_TEN_NATIVE_GO_REPAIR_ACTION_VERDICT.md) to two genuinely distinct Oct9 P35-P7 original Go header-router source architectures showed **three** viable patches per architecture when protecting D0 routing clients plus the independently reported external #1247 new route-matching requirement. That test suite was *not complete* with respect to other direct consumers of the separate exported \`NewPattern\` constructor and \`Pattern.Match\` API.

This study adds one **researcher-authored, explicitly optional** old-client preservation interpretation: a direct \`NewPattern\` caller expects historical case-sensitive matching behavior, as observed in the original Go source. It does NOT assert an official upstream documented semantic guarantee; an original library owner could intentionally authorize changing that behavior. The extra protected client is not an independently issued future demand; this is a **contract-scope sensitivity calibration** with the already known issue and already known repair operators.

[Pre-execution hypothesis, and an openly corrected mistyped string example before testing](03_DIRECT_CLIENT_CONTRACT_SCOPE_PREEXECUTION.md) froze the prediction that only caller-local \`route_both\` survives. Eight frozen [direct legacy regression cases](evo_direct_legacy_contract_test.go) check exact, prefix and suffix wildcard strings under changed and unchanged capitalization.

## 2. Real source execution

Input code: Oct 9 original source blobs LIVE \`ad9a2fbc0a30a39475f746068e74e2d3e6c93999\`, SNAPSHOT \`e9ca2c3863d5aa06ef0f0b9d168ddcf184713d75\`. Both substituted into separately reset ephemeral real upstream \`go-chi/chi\` v5.1.0 SHA \`67be7d9cafdaeb4e04e887ff78d09e030ee43b00\`. Same previously frozen five exact patch operators; **no source arch, patch grammar, or new route issue oracle altered**.

[Source-native Go CI **#42932257551 SUCCESS**](https://github.com/WhoSia/EvoNOMOS/actions/runs/42932257551): all **10/10** arm×repair cases executed with P35 D0/conditional mode, #1247 original old route tests, #1247 new route tests, eight old direct NewPattern tests. Whole original upstream Go suite and \`go vet ./...\` ran only on all-named-contract-passing candidates.

| Operation | Original route-only customer suite, each arm | New direct-old preservation test | Full combined customer acceptance, each arm |
|---|---|---|---|
| \`none\` | FAIL new route requirement | PASS | FAIL |
| \`constructor\` | PASS | **FAIL** | FAIL |
| \`route_both\` | PASS | PASS | **PASS** including full Go and vet |
| \`remove_lookup_lower\` | FAIL old and new routes | PASS | FAIL |
| \`match_lower\` | PASS | **FAIL** | FAIL |

Every result is the **same in both LIVE and SNAPSHOT**. CI job logs explicitly read back all ten \`DIRECT_SCOPE\` lines, absence of error, final SUCCESS and artifact uploaded. Final artifact is \`p44-direct-legacy-source-contract-court\`; the research-owned patcher, Go route tests and existing original full source code are preserved. No independent coding agent attempted to generate any candidate, and no actual person time was measured.

## 3. The actual mathematical structure: contract scope is a decision-repair constraint

Define the *test-accepted bounded source repair set* for a source architecture \(\mathfrak A\), limited patch grammar \(\mathcal E\) and frozen contract suite \(Q\):

\[
\mathcal P_{\mathfrak A}(Q)
=\{e\in\mathcal E:\operatorname{GoTests}(e(\mathfrak A),Q)=\mathrm{PASS}\}.
\]

If \(Q\subseteq Q'\), with valid stable deterministic test executions, then plainly
\[
\boxed{\mathcal P_{\mathfrak A}(Q')\subseteq \mathcal P_{\mathfrak A}(Q).}
\]
This is a **basic set inclusion**, not a new mathematical theorem or an empirical finding about all software.

The actual original source provides a **strict** witness under two explicitly different client-scope interpretations:

\[
\begin{aligned}
\mathcal P_{\rm LIVE}(Q_{\rm route})&=
\mathcal P_{\rm SNAPSHOT}(Q_{\rm route})
=\{\texttt{constructor},\texttt{route\_both},\texttt{match\_lower}\},\\
\mathcal P_{\rm LIVE}(Q_{\rm route}\cup Q_{\rm directOld})&=
\mathcal P_{\rm SNAPSHOT}(Q_{\rm route}\cup Q_{\rm directOld})
=\{\texttt{route\_both}\}.
\end{aligned}
\]

Concrete mechanism:
- \`constructor\` modifies the **exported direct API** \`NewPattern\` itself: \`NewPattern("Gold").Match("gold")\` switches from original FALSE to TRUE.
- \`match_lower\` changes \`Pattern.Match\` case-sensitivity for **all** clients, including unrelated direct callers.
- \`route_both\` transforms incoming configured patterns only in \`HeaderRouter.Route\` and \`RouteAny\`, leaving separate direct \`NewPattern\` constructor and matching methods untouched. Thus the new route behavior can be implemented while preserving the declared legacy direct client.
- All three production fixes reside in the same original Go production file: what differs is *the scope of affected public consumers*, not a simple touched-file count.

**Interpretation:** source repair eligibility must carry an explicit *customer-observation footprint*, not merely a syntactic dependency or number of edits. A small edit at a shared exported constructor can change more observed client contexts than a larger edit localized to two registration sites. This is a limited concrete instance of established contextual compatibility, regression preservation and information-hiding theories; no new software law follows by itself.

**Non-claim:** the local route fix is not necessarily preferred for global lifecycle economics, performance, or all future clients. It has two patch sites rather than one, and actual developer effort and upkeep are unknown. Under an API policy where direct \`NewPattern\` semantics are permitted to change, the constructor fix is again valid. *Which clients must be protected is a design/authority decision*, not determined by the code alone.

## 4. Specific relevance to SOLID-superordinate research

A candidate richer architecture object cannot merely encode source dependency edges \((V,E)\). It must encode which clients can observe behavior at each change boundary and **which observations are contractual obligations**. Without that, a proposed OCP/ISP/DIP intervention could look favorable when a hidden direct consumer makes the very same patch inadmissible. This empirical example still supports no automatic source-to-contract extraction algorithm, no causal law and no demonstrated advantage between two different registry-timing architectures.

A stronger future research object might include a client→observable behavior relation \(B\), a source-edit→potential observation footprint \(F\), and authorized repair relation \(\Gamma\), then attempt to derive conservative may/must client-preservation consequences. **A precise source-level soundness theorem** would need language semantics, unknown external callers and aliasing/reflection limitations. Full-information guarded LTS and established program slicing are strong prior competitors that cannot be treated as magically weaker.

## 5. Explicit novelty and prior art boundary

Test-based Automated Program Repair already distinguishes plausible passing patches from correct contract-preserving patches, and recognizes regression-suite undercoverage and patch overfitting:
- [Zemín et al. 2025, TOSEM, *An Empirical Study on the Suitability of Test-based Patch Acceptance Criteria*](https://researchportal.list.lu/publications/detail/an-empirical-study-on-the-suitability-of-test-based-patch-acceptance-criteria), compares test acceptance against formal specifications.
- [Song and Oh, OOPSLA 2025, *Enhancing APR with PRISM*](https://doi.org/10.1145/3763170), semantic overfitting patch assessment.
- [Martinez et al., Empirical Software Engineering 2024, *Test-based Patch Clustering*](https://doi.org/10.1007/s10664-024-10503-2), behavior-based candidate clustering.

These establish that extra oracles changing patch acceptance is **not a novel research finding in itself**. The possible EvoNOMOS contribution is the *source-extractable structural description of which public client-observation scopes are affected by an edit* and prospective conditional design selection with independently authored demands.

## 6. Disposition

**Keep:** clean original source test artifacts and precise contract-scope 3→1 collapse in both architectures; freeze which additional tests are authored versus external. This is one distinct bounded source discovery that materially sharpens the project direction.

**Stop:** repeated known Chi normalization defects or extra arbitrary client tests merely to inflate successful case counts. Current result is sufficient to motivate actual typed source-client impact analysis and verified behavioral abstraction.

**Next gate:** a semantic or source-verified *client observation footprint* checker, with demonstrably sound may-affect versus definitely-preserved conclusions under explicit edit grammar, and comparison to conventional dependency slicing. Then independent future public API requirements and actual architecture treatments (not variants sharing identical Pattern code), true maintainer work data.

**LAW-R2 HOLD / G1–G7 OPEN.**
