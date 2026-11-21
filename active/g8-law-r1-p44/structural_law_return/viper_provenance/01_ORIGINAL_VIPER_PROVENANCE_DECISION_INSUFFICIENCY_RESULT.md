# EvoNOMOS — Actual Viper v1.21.0 Decision-Information Insufficiency, Issue #2161

**2026-11-10 KST | independent externally authored REQUIREMENT; ORIGINAL-SOURCE NATIVE CI PASS; restricted deterministic policy non-identifiability; classical rival ties; NO ARCHITECTURE CAUSAL LAW or LAW-R2.**

## Why this is a different research unit

The founding goal is *conditional source architecture policy discovery*, not a sixth rerun of Chi namespace collisions, exact finite-state reachable goals or history-aware source replay. The 2026-11-10 six-role origin audit showed a mathematical gap: exact source-repair feasibility is not itself a design decision; the key target is **which source-observable information at choice time is sufficient to choose an action under future requirements**.

The independently authored, still-open at selection [spf13/viper issue #2161](https://github.com/spf13/viper/issues/2161), filed **2026-10-12** by an external contributor, asks for the effective setting source, including actual environment variable name, under override/flag/env/config/default precedence. Its realistic motivation is a value with different application lifecycle policy if externally supplied versus locally managed.

**Source frozen BEFORE research tests**: actual independently maintained Viper original tag \`v1.21.0\`, annotated tag object \`9d332ad291ae43150db75ef817217898eb14149c\`, underlying source commit \`394040caccbdf5821fa6839386a35f0fb1b1ee9e\` (tag 2025-09-08, prior to issue). [Pre-execution seal](00_VIPER_ISSUE_2161_BEFORE_SOURCE_EXECUTION_PREDICTION.md) committed as \`b07eac3f56612af84e2d80770c488c240cf6f88f\` **before** CI/run and original test implementation. Issue description was read before seal. No later solution PR/diff was read, but the task is **issue-informed selected**, not researcher-blind/random or an independently selected before-filed demand.

## Three distinct source-based claims, intentionally not conflated

**(i) Observational indistinguishability (native source fact).**
Two app-owned Viper worlds load identical YAML value \`service.token=same-token\`, same \`AutomaticEnv\`, prefix APP and dot-to-underscore replacer. W_file has absent \`APP_SERVICE_TOKEN\`, W_env sets it to \`same-token\`.

\`z=(GetString("service.token"),IsSet("service.token"),InConfig("service.token"),AllSettings())\` is **exactly equal** across worlds. Native Go test verifies this equality by \`reflect.DeepEqual\`, both values exactly \`same-token\`, both \`IsSet\` and \`InConfig\` true, and same full settings map. It also checks a different environment variable value causes the projection to split (negative control). Actual provenance is known from the research-controlled environmental intervention, not inferred from a non-existing Viper \`SourceOf\` API.

**(ii) Narrow policy impossibility (mathematical implication of a declared decision use case, NOT a fact about Viper's implicit policy).**
Actions F=refresh/manage locally, E=preserve as externally owned. For THIS synthetic-but-issue-motivated lifecycle contract, source file requires F and effective environment requires E. Both W have same z, so any deterministic policy \`a(z)\` must pick the same action; it fails at least one. Under unit regret J=1 for incorrect action and J=0 for correct, optimal minimax regret is **1**, proven by finite argmin fiber condition already recorded in the origin six-role audit. The CI test enumerates F,E and verifies this 1. This is standard finite decision theory, NOT a new software theorem. In the full real application, token refresh policy and losses need independent specification/measurement; these particular choices are **researcher-assigned**.

**(iii) Strong classical baseline already wins the narrow case.**
A conventional source-aware application comparator that knows the exact variable \`APP_SERVICE_TOKEN\` calls \`os.LookupEnv\`. It correctly predicts F in W_file and E in W_env (**2/2 verified**). It has information that value-only z does not. This is *not* unique advantage for EvoNOMOS. A generic original upstream \`SourceOf\` API remains unimplemented and **multiple BindEnv mappings, aliases, unset/empty semantics, flags, overrides and dynamic config mutations were not verified**. A known-name \`os.LookupEnv\` comparator may be invalid for those other contexts, but this has NOT been demonstrated in this run.

## Native source custody and execution

[Read-only GitHub Actions #42741554785 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/42741554785), at study CI commit \`3a658934de37de9f3e050fb709b820d73f228865\`. Workflow asserts exact upstream original Git commit before testing, copies only [research-owned external Go source test](evo_viper_provenance_test.go) into ephemeral original checkout, tests no original source edits, performs \`go mod download\`, \`go mod verify\`, read-only \`go vet -mod=readonly .\`, \`go test -mod=readonly -count=1 -v -run '^TestEvo' .\`, \`go test -mod=readonly -race -count=1 -run '^TestEvo' .\`. Job and logs read back, **five distinct native tests PASS**, vet/race PASS. No claim about the entire upstream suite, no original maintainer source modification, no independent upstream edit permission or actual patch-size comparison.

Native raw verdict tags:
- \`EVO_VIPER_EQUAL_PUBLIC_PROJECTION true value="same-token" isSet=true inConfig=true\`
- \`EVO_VIPER_VALUE_ONLY_MINIMAX_REGRET 1\`
- \`EVO_VIPER_CLASSICAL_KNOWN_ENV_2_OF_2 [F E]\`
- \`EVO_VIPER_NEGATIVE_CONTROL_DIFFERENT_VALUE file="same-token" env="different-token"\`

## Mathematical connection to P37/P40/P42 and scientific ceiling

For \`z:Ω→Z\` and action cost \`J(ω,t)\`, a context-sensitive choice policy with zero regret exists over a feature fiber only if its contexts' argmin sets intersect. Here z(W_file)=z(W_env) but {F} ∩ {E}=∅. Adding one correctly observed source bit \`b\` refines this pair and makes a policy possible; this is an **information-sufficiency counterexample**, not a proof that one bit suffices for the full Viper precedence graph, nor an original theorem.

P37-MATH-K already gives the exact classical information-factorization ceiling; P42-P14 already distinguishes unobserved future requirements from disclosed ones. The present issue provides **independent real source** where a natural public projection forgets a decision-relevant provenance distinction. The issue writer independently noticed this inadequacy before this study. Full-information classical source-aware comparison and provenance research can explain it already. Unlike P35, NO two equally capable *source architecture interventions* with actual multi-step maintenance and measured labor were compared. Thus **not enough to identify a novel OO structural design law**.

Prior research context verified separately: conventional software-configuration provenance literature exists (Xu & Sengupta 2005, "Provenance in Software Engineering - A Configuration Management View"; provenance fundamentals; configuration rule learning, e.g. Bhagwan et al. 2021). These are adjacent literature signposts, not claims that those papers prove this exact Viper API deficiency. Review complete source text before formal citation.

## Explicit next gate — NO automatic extension

The useful next science question is not "repeat value collisions with one more environment key" but:

> Under a FIXED information acquisition budget and protected client/reliability requirements, does choosing an architecture that records effective source provenance in an owned boundary improve future operator decisions or repair effort beyond realistic explicit-environment tracking and full original-source dependency models, across INDEPENDENT future demands with unchanged functional output?

Requires (1) two matched old-functional source architectures, (2) post-selection independently issued future task, (3) equal-source-information and baseline cost of acquiring provenance, (4) actual action/repair outcomes and multiobjective measurements, and (5) rights and source-effects evidence. If classical rival ties after accounting for cost, accept negative scientific result.

**NATIVE SOURCE DECISION-INFORMATION COUNTEREXAMPLE PASS / POLICY-LAW IDENTIFICATION HOLD / P44 G1–G7 OPEN / PR #13 DRAFT / LAW-R2 HOLD.**
