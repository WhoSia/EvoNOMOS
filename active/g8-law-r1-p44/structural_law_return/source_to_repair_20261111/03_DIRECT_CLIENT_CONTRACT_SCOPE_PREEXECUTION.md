# P44 — Direct-Client Contract Scope as an Architectural Repair Moderator (Pre-execution)

**2026-11-11 KST · CURRENT ANALYST-DESIGNED OBSERVATION EXTENSION · NOT EXTERNAL FUTURE FORECAST**

The previously finished [10 original Go source repairs](02_ALL_TEN_NATIVE_GO_REPAIR_ACTION_VERDICT.md) yielded 3 tested viable actions per source architecture (constructor normalization, two route call-site normalization, matcher normalization), while only D0+route-level old+new customer oracles were run. However, \`NewPattern\` is a separately exported Go constructor and \`Pattern.Match\` is separately exported. Thus a legitimate *possible* older direct consumer can invoke these without the \`HeaderRouter\` route-registration sites.

This trial tests whether the original set of repair options is **contract-scope invariant**, not whether one architecture is better.

## Frozen pretest observations and commitments

From actual original 2026-10-09 Go source (both LIVE and SNAPSHOT), **unmodified** \`NewPattern\` stores the unnormalized input (split at the first '*') and \`Pattern.Match\` compares stored prefix/suffix verbatim. Before execution, source reading therefore predicts (not asserts tested outcome yet):

- \`NewPattern("Gold").Match("Gold")\` should be true.
- \`NewPattern("Gold").Match("gold")\` should be false.
- \`NewPattern("Go*").Match("Gold")\` should be false (prefix case differs).
- \`NewPattern("Go*").Match("GoLD")\` should be true.
- Similar direct case-sensitive suffix variants should be preserved.

These are **observations of the old implementation proposed as an explicit additional direct-client preservation contract**. They are NOT established contractual guarantees in Chi's official API documentation, and not an independent user's request. A maintainer may instead legitimately choose to CHANGE the semantics of the exported direct API. Therefore we test both scope interpretations rather than declaring one objectively correct.

Preserve original known external #1247 RouteHeaders new demand and original P35 D0/old route contracts, and add this *researcher-authored* direct \`NewPattern\` client preservation requirement. All five previously frozen source repair operators remain unchanged. For each of LIVE and SNAPSHOT, copy source arm from fixed Oct9 source SHA, apply same frozen operator, then execute:
1. Old D0/mode and original route old-contract tests;
2. Actual issue #1247 route new demand;
3. NEW direct legacy-client case-sensitive contract;
4. Full original \`go test ./...\` and \`go vet ./...\` only if (1)-(3) PASS.

Pre-execution **falsifiable prediction** from code inspection:
- \`route_both\` should keep direct \`NewPattern\` case-sensitive and satisfy #1247 via registration-site normalization.
- \`constructor\` should violate direct legacy-client semantics because it normalizes \`NewPattern\` itself.
- \`match_lower\` should violate direct legacy-client semantics because \`Match\` normalizes prefix/suffix.
- \`none\` should fail new route demand; \`remove_lookup_lower\` should fail old/new route demands.
- Thus **exactly one** original repair operator per architecture will be in the expanded **tested passing** action set: \`route_both\`.

A source-native execution can falsify this prediction. A failure should be retained, not silently rewritten or retested with changed customer oracles. No formal proof of full Go semantics and no long-term maintainer cost inferred. If predicted narrowing happens, the result demonstrates that source change *location* and **set of protected customer contexts** change finite repair eligibility, including an LSP-like old observable behavior constraint (without equating this to a full LSP theorem).

### Intentionally excluded

No general Unicode proof, no claims about client external use in production, no owner-authorized semantics, no independent agent, no prospective new demand or LAW-R2 promotion. No original source files or previous 10-run receipt changed.
