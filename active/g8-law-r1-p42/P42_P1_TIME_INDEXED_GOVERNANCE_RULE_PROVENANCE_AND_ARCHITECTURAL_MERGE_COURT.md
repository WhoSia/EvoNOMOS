# EvoNOMOS Generation VIII LAW-R1-P42-P1 — Time-Indexed Change Authorization & Governance-Rule Provenance: Merge-Event Replay, Effective Ruleset Reconstruction, Policy-Bypass Evidence & Non-Promotion of Unknown Rights

**Official user-authorized P42-P1 · 2026-10-11 KST · RAVEL: Discover → Plan → Execute → Verify → Iterate → Promotion/Hold/Reject · P42 RUNNING · LAW-R2 NOT_AUTHORIZED.**

## 0. Return to EvoNOMOS's founding explanandum

EvoNOMOS began as a search for conditions under which familiar OO/SOLID design doctrines **hold, fail or reverse in real software**; original ambition: precise source-realizable structure, necessary and sufficient conditions, counterexamples and—only if not reducible to existing theory—a genuine architectural law. A valid repair decision cannot be inferred from source compilability, nominal OO roles, a passing CI badge or a merge button. P42-P1 therefore asks a harder question in an actual router maintenance event:

> **Can the fact that an architectural edit was merged, paired with a visible protected-branch ruleset whose timestamps predate that merge, establish the rights and requirements that were actually operative at the editing time?**

**Answer at present: NO as a complete entitlement claim.** A genuine GitHub release-branch ruleset now supplies much stronger, source-grounded temporal evidence than P41's simple unknown; its history and classical branch-protection layers are still inaccessible. The distinction is proved as an information-loss countermodel in the *restricted formal language*, not as an accusation about a specific account or proof of GitHub's global semantics.

## 1. The real architecture change, not a fictional example

Public upstream **labstack/echo** pull request [#3132](https://github.com/labstack/echo/pull/3132):

- Title: `fix(router): handle escaped colons and inline verbs in v4`
- Intended architectural effect: backport changes to escaped-colon route parsing and inline-verb routing in the **v4** router; this is actual route-language/source mutation, not a fabricated governance event
- PR head commit: `499f5639f31c8e780bb58da1785beffcaf56b3e0`
- Merged by public platform account **`vishr`** on **2026-09-30T01:00:17Z** (2026-09-30 10:00:17 KST)
- Merge commit: `f085ffbe8f99de165bd920746920000ab56bd6bc`; [independently inspected historical Git commit](https://github.com/labstack/echo/commit/f085ffbe8f99de165bd920746920000ab56bd6bc) identifies its actual **first and only parent** as `5440f99719cc8de4be2ae6abfc8f275302791730`. These are exact **PRE/POST original source snapshots** available for next P42-P2; they are stronger than an unverified PR.base SHA.
- Actual changed files: `route_path.go`, `router.go`, `route_syntax_test.go`, `router_test.go`
- Two accessible review submissions by `vishr` at 2026-09-29T21:32:55Z and 22:15:33Z are **`COMMENTED`**, **not `APPROVED`**.
- GitHub PR's *current* `base.sha` is **not assumed** to be the historical base at the merge; the base ref `v4` and actual merge commit are independently checked.

The event and its changed-file identity were independently re-fetched and hash-receipted in [P42-P1 source court #38132348692 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38132348692), checked harness HEAD `a691550069717b16cd4632c137b1beeaf1ff94e4`, artifact `11699910587`, SHA-256 `54eae0a96cbf51c34365fe347d824eb564f9ec998b9b11599e487d8597da6e6f`; the later independently tested parent/child provenance receipt is #38132709607 (Section 3). This source court confirms the **code-change identity** and **platform merge event**, not whether the router code was behaviorally correct. Reproducing before/after real client outcomes at exact commits is a downstream P42-P2 obligation.

## 2. Newly discovered actual GitHub protection source

[Echo release branch Ruleset #24079530](https://github.com/labstack/echo/rules/24079530), title **Protect release branches**:

| Field in current public Ruleset | Verified value / boundary |
| --- | --- |
| Source and branch coverage | Repository `labstack/echo`; active now; `~DEFAULT_BRANCH`, `refs/heads/v4`, `refs/heads/v5` |
| `created_at` | **2026-09-28 02:50:19.651+09:00** |
| `updated_at` | **2026-09-28 07:25:26.228+09:00** |
| `pull_request.required_approving_review_count` | **0** in the current visible ruleset |
| `require_extra_approval_for_unattributed_changes` | **true** in the current visible ruleset; zero ordinary required reviews is NOT blanket proof that no conditional approvals can matter |
| `require_code_owner_review` | **false** in this current ruleset only |
| Additional published rules | branch deletion restriction; non-fast-forward restriction |
| `current_user_can_bypass` | **`never`** for the current API observer, NOT a historical rights determination for the merger `vishr` |
| `bypass_actors` field | **not returned**; must not infer that bypass is impossible, unused, or no exception actor exists |
| Historical Ruleset revisions | `GET /repos/labstack/echo/rulesets/24079530/history` → **HTTP 403** during independent CI |
| Classic protected-branch record | `GET /repos/labstack/echo/branches/v4/protection` → **HTTP 403** during independent CI |
| Organization-level historical controls | Not reconstructed, **UNKNOWN** |

Both listed rule metadata timestamps precede the actual **2026-09-30** PR merge. The comparison uses **offset-aware instants** rather than string representations; GitHub tools can serialize identical instants using different ISO UTC offsets. Our first CI caught this methodological issue and was repaired without changing the source event, hypothesis or permission claim.

**Key distinction:** a current ruleset's `updated_at` preceding the merge gives strong **temporal compatibility**, but without authoritative version history and full protection/bypass/source scope it does not independently certify that every effective policy layer—and the actor's actual entitlement—has been reconstructed for the merge. It would be scientifically incorrect to treat HTTP 403 as evidence that the rule did not exist.

GitHub documents the relevant [repository Ruleset API and historical version endpoint](https://docs.github.com/en/rest/repos/rules) and the [historical Ruleset scope/per-organization access requirements](https://docs.github.com/en/rest/orgs/rules). The latter are provenance requirements, not mere software API implementation details.

## 3. RAVEL falsification loop — no self-awarded pass

- **DISCOVER:** source-visible merged v4 router PR and public release-branch Ruleset ID, timestamps, conditional extra-approval flag, missing bypass-actor visibility.
- **PLAN:** lock exact PR actor/UTC/merge SHA, four changed file paths, two review states, Ruleset fields, expected API access limits and nine adversarial mutations in [discovery replay lock](../../tools/p42/p1/governance_discovery_and_replay_lock.json). This is *post-discovery replay registration*, NOT a blind out-of-sample forecast.
- **EXECUTE:** [source-only public REST read workflow](../../.github/workflows/g8-p42-p1-governance.yml) re-fetches original PR, issue merge events, submitted reviews, Ruleset list and detail, the real changed files, and access status to protected branch/history; no upstream source or settings are changed.
- **VERIFY:** [public event/rule metadata grader](../../tools/p42/p1/audit_live_governance.py) requires the original source fields, 5 rejected counterfeit records: wrong merge actor, wrong merge SHA, ruleset update after merge, loss of v4 applicability and forged `APPROVED` review. [Architecture code-fingerprint grader](../../tools/p42/p1/audit_architectural_change.py) requires the actual four file paths/patch head and 4 more rejection controls: fake head commit, file substitution, wrong base branch and **wrong actual historical merge-parent SHA**.
- **ITERATE:** original [Actions #38131993022 failed](https://github.com/WhoSia/EvoNOMOS/actions/runs/38131993022) on textual timestamp equality (timezone representation); revised comparison normalizes UTC instants and retained fail-closed timestamp drift checks. [#38132094734 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38132094734) recovered the governance source receipt. An additional strict check ensures `require_extra_approval_for_unattributed_changes=true`, with [#38132211212 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38132211212). The first source-to-code linkage [#38132348692 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38132348692) independently passed public replay and eight synthetic negative controls. The stronger final [#38132709607 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38132709607) also re-fetched the **real Git merge commit and its original parent** and passed **all nine** synthetic negative controls. Checked final source HEAD `7c4555b2158d7b5238ed4df98d0c42ef10b14f07`; final artifact `11699587778`, SHA-256 `670e32fb93c80e865ca207ec29743124beb92313a4f9578b2ba3593e81bcc262`. Intermediate [#38132668844 failed](https://github.com/WhoSia/EvoNOMOS/actions/runs/38132668844) because the post-upgrade source validator's success marker was out of sync with the stricter CI gate; the validator marker was corrected without changing any historical source expectation.
- **PROMOTION/HOLD/REJECT:** **PROMOTE** real historical merge operation and timestamp-ordered *presently visible* v4 Ruleset observations. **HOLD** complete policy at merge, actual actor authorization under all rule layers, organizational/normative legitimacy, source-code behavioral correctness and any new architecture law. **REJECT** invalid inference `merge succeeded ∧ current approval minimum 0 ⇒ fully authorized and always safe`.

The final hosted CI artifact contains raw public GitHub REST records, SHA-256 hashes and independent receipts. A copied Notion statement or single screenshot is not accepted as the source oracle.

## 4. Formal evidence boundary and causal ambiguity

[P42HistoricalAuthorityNonidentifiability.lean](../../tools/p42/lean/P42HistoricalAuthorityNonidentifiability.lean), importing the already verified [P42 P0 evidence judgement](../../tools/p42/lean/P42EvidenceJudgement.lean), formalizes:
- A `PublicSnapshot` of merge observed, current release ruleset, current ordinary minimum review count, and rule/merge timestamp order.
- Separately typed hidden evidence of **ruleset version at merge**, legacy branch protection, organization policy, actor eligibility at merge and institutional mandate.
- An `unknown` / `permitted` / `contradicted` *conditional abstract* policy verdict.
- Two explicitly **hypothetical** historical worlds sharing **the exact same public snapshot** but with different hidden legacy protection and opposite full conditional verdicts.
- A classical **nonfactorization** theorem: no total decision classifier of full historical permission can operate only on the public snapshot for all abstract worlds.
- A fail-safe result: the observed successful platform merge with current zero-approval minimum but absent other historical layers must yield **UNKNOWN**, not institutional permission.

The two historic-world counterexamples are deliberately **synthetic**; there is no finding of unauthorized or illegitimate action by `vishr` or any other identified person. The theorem is a classical information-sufficiency limit in an explicit model, not a claim of universal novelty, temporal-logic incompleteness or kernel-certified GitHub policy semantics.

**Lean 4.34.1 independent kernel VERIFIED:** [GitHub Actions #38132126187 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38132126187), checked complete P42 Lean source HEAD `0cc59672376a597a9048be69ed58a55097e0bdab`, artifact `11699507417`, SHA-256 `11ab2af1dab84ce71626e4ed88925a6b93b6e745ec3f4443b4633dc04823cc5d`. Earlier [#38132059621 failed](https://github.com/WhoSia/EvoNOMOS/actions/runs/38132059621) because Lean could not synthesize a decidability instance for the opaque `temporallyCompatible` predicate using `decide`; the correction explicitly unfolded the predicate with `simp` without changing the mathematical statement. No source-to-GitHub semantics compiler or complete historical authorization inference is claimed.

## 5. Against the strongest classical and legal/organizational rival

The strongest appropriate rival is not “review minimum 0 means the merge was justified”. It is an **open-world, time-indexed conjunctive policy evaluator** with separate sources for rule validity interval, actor capacity, legacy/org layers and discretionary institutional mandate. That rival reaches precisely the same **UNKNOWN** verdict on this observation set. No P42 novelty advantage survives that classical comparison; this is an explicit **negative reduction** consistent with EvoNOMOS's founding mandate.

The real software-science contribution here is **admissible evidence discipline** for future architecture judgments: an observed edit event is an event; applying a rule to that edit requires rule applicability, validity over the edit-time window, actor-specific evaluation and relevant provenance. The **actual source edit** is anchored in four router/route-syntax files, so later P42-P2 may test *what changed for clients*, rather than simply theorize about code governance.

## 6. Remaining debt and next gate

- **C1 Historical ruleset version:** read historical `history/{version_id}` only through an already-authorized audit mechanism. Never request someone else's credentials or attempt to evade API access limits. If unavailable, retain UNKNOWN.
- **C2 Classic and organization layers:** effective branch protection and any layered policy at 2026-09-30T01:00:17Z. Current Ruleset listing alone cannot certify global completeness.
- **C3 Actor privileges and legitimate mandate:** actual actor-specific role at that date, institutionally sanctioned change class, policy exceptions if disclosed; separate platform operation from normative permission.
- **B2 Source-to-behavior:** execute an independent, pinned before/after experiment on PR #3132's parser and inline verbs without modifying upstream or conflating test fixtures with historically observed production clients.
- **F and P42-P4:** source-grounded provider dependencies and genuinely previously unseen issues, with equal-information strong classical prospective rival; original P41-P4/P5 publication debt remains OPEN.

**P42-P1 scientific verdict: real PR and currently visible release Ruleset temporally linked; actual PRE/POST source commits identified and governance/source replay with NINE negative controls VERIFIED in CI #38132709607; restricted authority non-identifiability Lean kernel VERIFIED in CI #38132126187. P42-P1 CLOSED_AS_BOUNDED_OPEN_WORLD_GOVERNANCE_COURT; true complete historical permission still UNKNOWN, and no new OO law follows. P42 remains RUNNING, LAW-R2 NOT_AUTHORIZED.**
