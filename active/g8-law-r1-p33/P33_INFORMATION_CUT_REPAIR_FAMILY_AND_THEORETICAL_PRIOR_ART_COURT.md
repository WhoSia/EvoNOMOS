# P33 — Repair Admissibility, Information Cuts & Test-Domain Refinement

**Authority:** actual GitHub Actions source-pinned bounded test PASS; independent prospective evidence and production Q HOLD. No new mathematical theorem; LAW-R2 NOT_AUTHORIZED.

## 1. Source identity and executable result

P33 directly pinpoints real Uptime Kuma birth source commit 398482d590daaac0d44e288c9be3bc6f6667f8b8 and the relevant three exact Git blobs: server/model/monitor.js at 2ad572e53ed051825425f8783c91195cbd243d77; server/notification.js at b1a42d003a92e3760f6d33a4be59784a9cb4dbf2; server/notification-providers/notification-provider.js at 42079176c01cd2e6d46160bb6f6408d4ba263fd7.

GitHub executable: [tools/law-r1-p33-info-cut-repair-world.mjs](../../tools/law-r1-p33-info-cut-repair-world.mjs), [read-only workflow](../../.github/workflows/g8-law-r1-p33-information-cut.yml). Hosted run **37808780917 SUCCESS**, artifact **11564131346**, SHA256 **ef86e5a6b59f557be00dfd8cbd3655f1529a542cdad9ab7934b7cdf7664c6218**. Artifact inspected: source methods invoked with controlled DB/notification/template dependencies; both repair candidates pass two normal-name URL inputs. Only the caller-forwarding candidate passes both additional delimiter-collision inputs; dispatcher-parsing returns literal template fallback values in both collision tests.

A modifies **server/model/monitor.js**, adding an explicit structured monitor context argument at the original notification call; B modifies **server/notification.js**, using string-pattern extraction where monitor context is absent. The two supports are disjoint singletons within this frozen **two-candidate source-edit grammar**, and the unpatched original does not satisfy the normal-name context oracle. This is a *bounded repair-option existence demonstration*, not exhaustive source repair discovery. The user-facing bug issue #7639 was already known; the collision tests were constructed from the argument channel's grammar. Hence this is neither a new blind issue nor a victorious prospective H predictor.

The actual Uptime Kuma production system, Liquid engine, external provider transports and all original contracts were not fully executed: **BOUNDED_SOURCE_METHOD_ORACLE_ONLY**. The caller candidate forwards partial monitorJSON, not an independently verified complete object or compatibility with all provider types. Explicit assumptions: ordinary URL-form monitor, fixed notification config, and correctly behaving dependency mocks. No unconditional claim of fully valid production repairs.

## 2. Elementary information-cut proposition

Let X be the set of legitimate source states, f:X->M the observation exposed to the downstream component, and g:X->Y the required context-dependent result. For deterministic decoders h:M->Y, there exists h with g=h∘f on X **if and only if** ker(f) is a subset of ker(g). The forward direction follows from equality of observations; the reverse direction defines h on the image of f using any representative (well-defined by kernel inclusion) and extends it arbitrarily off the image. This is a **standard function factorization theorem**; P31 already warned against treating it as novel.

In the birth code the caller serializes message prefix of the form [name][url] with no escaping and passes two arguments. Under the same notification configuration, two distinct source states:

- x: name = alpha][https://x.invalid/ ; URL = https://y.invalid/
- y: name = alpha ; URL = https://x.invalid/][https://y.invalid/

produce exactly the same message [alpha][https://x.invalid/][https://y.invalid/] followed by the same certificate suffix. The target (name, URL) outputs are distinct, so *no downstream-only deterministic algorithm constrained to the same config and unchanged message* can faithfully recover both. A hypothetical downstream fix could introduce an independent DB lookup/extra channel; this theorem deliberately does not exclude that. A source call-site repair carries a new independent context argument across the information cut, removing the obstruction within the tested domain.

## 3. Repair-solution filtering is anti-monotone, minimal support families need not be

Fix a finite candidate grammar G, program test/acceptance contexts T0 subset T1, and pass predicate. Feasible candidate set F(T)= { p in G : forall t in T, p passes t }. Then F(T1) subset F(T0). This is trivial monotonicity of conjunction of constraints.

But the inclusion-minimal supports min_subseteq{ Supp(p):p in F(T)} need **not** be nested under that refinement: it can lose minimal supports; previously nonminimal supersets can become newly minimal if smaller repairs fail stronger tests. Toy example supports {a}, {b}, {a,b} all feasible under T0, only {a,b} under T1: min-support family changes from {{a},{b}} to {{a,b}}; this construction is standard finite set theory, not a novel structural law.

In the **real-source restricted two-option grammar** witnessed here, minimal families change from {{monitor.js},{notification.js}} on the small safe-domain oracle to {{monitor.js}} on the delimiter-collision strengthened oracle. This does NOT demonstrate global minimality among all possible Uptime Kuma source modifications.

An architecture-design law would need a source-grounded conditional account of when a property of a *feasible repair-family* predicts future Q and S/L/C/A effects better than extant methods.

## 4. The prior-art court remains undefeated

- **SemFix (Nguyen et al., ICSE 2013, DOI 10.1109/ICSE.2013.6606623)** — symbolic execution, repair constraints and synthesis.
- **DirectFix (Mechtaev et al., ICSE 2015, DOI 10.1109/ICSE.2015.63)** — repair size and structural preservation objectives.
- **Angelix (Mechtaev et al., ICSE 2016, DOI 10.1145/2884781.2884807)** — scalable multiline semantics-based patch synthesis.
- **Reiter (1987, DOI 10.1016/0004-3702(87)90062-2)** — diagnostic conflicts and minimal hitting sets. Does not automatically imply source repair semantics.
- **Smith et al. (2015, DOI 10.1145/2786805.2786825)** — repair overfitting and independent test validity.
- **Guigue (2014, DOI 10.1051/cocv/2013056)** — set-valued Pareto optimal control, viability kernels.
- **Angerer et al. (2019) CSDG**, **Hong et al. (2024) CoChangeFinder**, **Cai et al. (Design Rule Spaces)**, **Cámara et al. (2019) tradeoff spaces**: in original Drive 10_PAPERS. These exceed naive B0 static count baselines in distinct task settings.

DirectFix/Angelix and test overfitting already show that multiple repair candidates and test-dependent fitness are established research fields. Nothing here outruns strong B2 with abstract interpretation plus string/contract constraints. The new candidate is not 'multiple repairs exist' or a rediscovered factorization lemma. It is prospective conditional OO policy-and-contract geometry under identical functional oracle, with rival-matched information and independently held-out requirement.

## 5. Cross-shelf mathematical Harvest seeds, not promotions

**Fragment I — observability and correction authority:** a source-level contract can demand values outside a module's observed sigma-algebra/information partition. Crossing the cut requires new data or a restricted oracle; local code ingenuity cannot manufacture absent distinctions.

**Fragment II — antichain instability:** adding test contexts filters full repair implementations monotonically but support minimization can change its basis nonmonotonically. A source tool that treats a minimal-repair antichain as a permanent ontology risks invalid pruning after domain enlargement.

**Fragment III — restricted gluing problem:** define behaviors realizable by candidates in grammar G over input region U. Locally realizable behaviors need not compose to a globally realizable implementation over the union of regions. Category/sheaf terminology is only warranted with explicitly proven restriction maps and local-to-global hypotheses. A pretty sheaf label does not yield a novel OO mechanism.

**Fragment IV — set-valued conditional continuation:** future repair choice is a finite-horizon policy problem with set-valued Pareto return, not current support-minimization. A P33 real witness DISPERSED⊊DUAL initial file supports but 80 versus 75 later handwritten L; cumulative 102 vs 111 cautions against single-winner promotion.

**Fragment V — source-pair causal falsifier:** freeze I0 pre-patch input, admissible edit grammar and full oracle. Have B0+ topology/typed overlap, B1 temporally clean co-change, B2 CSDG/DRSpaces/APR repair synthesis and H forecast the same sign/admissibility/Pareto target on a fresh independent demand. If forecasts coincide or H loses, report negative result. Do not treat this retrospective negative control as discovery.

### Conclusion
**P33_TWO_BOUNDED_REPAIR_OPTIONS_HOSTED_PASS__INFORMATION_CUT_NEGATIVE_CONTROL__FULL_REAL_WORLD_ADMISSIBILITY_HOLD__STRONG_RIVAL_DISCRIMINATION_HOLD__LAW_R2_NOT_AUTHORIZED**.
