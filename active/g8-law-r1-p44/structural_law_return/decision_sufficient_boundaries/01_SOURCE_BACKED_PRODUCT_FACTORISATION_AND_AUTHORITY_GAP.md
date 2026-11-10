# EvoNOMOS — Source-backed Modular Decision Factorization and Three Distinct Failure Mechanisms

**2026-11-11 KST · P44 DECISION-SUFFICIENT BOUNDARIES · REAL GO AST SOURCE EVIDENCE / FINITE EXACT MODEL VERIFICATION · NO GENERAL SOURCE LAW · LAW-R2 HOLD**

## 0. Research-lead response: challenge our own novelty before adding a new theorem

The previous [minimal decision-conflict hypergraph program](00_RESEARCH_DIRECTION_HYPERGRAPH_OBSERVABILITY_AND_ARCHITECTURE_FRONTIER.md) accepts optimal-action sets and losses as **hand-specified inputs**. Its classical Bayesian regret and hypergraph-hitting-set math was correct in bounded tests, but alone is not a superior software architecture law.

More serious prior art retrieved now includes a **2026 paper explicitly formalizing observation fibers, state-dependent feasible actions and common-action deployability**: *A Framework for Reliable Deployment and Monitoring of AI Decision Systems Under Partial Observability*, [Applied Sciences 16(10):4917](https://www.mdpi.com/2076-3417/16/10/4917), section 3; its state-wise feasibility/fiber intersection is directly on point. Thus DO NOT claim our observation+authority consistency criterion, by itself, is new. Also [O'Hearn, Yang & Reynolds (2009), Separation and information hiding, TOPLAS](https://doi.org/10.1145/1498926.1498929), already proves sophisticated ownership transfer/separation rules; [Automatic modularity conformance checking (ICSE 2008)](https://doi.org/10.1145/1368088.1368144) already connects design rules and real code; [Design rules: past and future (2023)](https://academic.oup.com/icc/article/32/1/11/6868533) develops modularity/dependency structure. Publication-worthy novelty needs exact real-code extraction, scalable soundness, strong conventional rivals and generalizable maintenance outcomes; not a cosmetic theory title.

## 1. A precise upper-structure question

Let a source-based candidate architecture be two components A and B. Each has:
- a finite demand/environment state s_i, prior p_i, observable z_i(s_i) that maintainer can consult before deciding,
- a common finite action menu U_i but **state-wise authorized** choices \(\Gamma_i(s_i)\subseteq U_i\), nonempty for every reachable state,
- lifecycle loss \(\ell_i(s_i,u_i)\), with fixed units/weighting.

A robust observation-based policy must choose an action that remains **authorized in every state consistent with the observation it sees**, not merely in the most likely state.

**Product-factorization proposition (classical under explicit assumptions).** If:
1. the joint state support/prior is a FULL CARTESIAN PRODUCT with independent weights \(p_{AB}(s,t)=p_A(s)p_B(t)\),
2. the predecision observation is the pair \(z_{AB}(s,t)=(z_A(s),z_B(t))\),
3. the feasible joint action set is EXACTLY \(\Gamma_A(s)\times\Gamma_B(t)\), without shared owner/capability/global cap,
4. total loss is ADDITIVE \(\ell_{AB}((s,t),(u,v))=\ell_A(s,u)+\ell_B(t,v)\),

then **if each local observation fiber has at least one authorized common action**, the joint robust Bayes risk and the state-aware authorized oracle both factor:
\[
R^\mathrm{obs}_{AB}=R^\mathrm{obs}_A+R^\mathrm{obs}_B,\quad
R^\mathrm{auth}_{AB}=R^\mathrm{auth}_A+R^\mathrm{auth}_B,\quad
\Delta^\mathrm{obs}_{AB}=\Delta^\mathrm{obs}_A+\Delta^\mathrm{obs}_B.
\]

Proof: for every observed fiber pair, its uniformly feasible action set is
\((\bigcap_{s:z_A(s)=v}\Gamma_A(s))\times
(\bigcap_{t:z_B(t)=w}\Gamma_B(t))\).
Fubini's finite-sum identity and normalized independent conditional weights split the joint expected additive loss into one minimization over u and another over v. Summing over paired fibers gives the risk identity. State-by-state minimizations over the Cartesian action sets likewise split the oracle. The regret identity is their difference. This is a straightforward classical separation result; its value is precisely stating WHEN apparently modular software decisions genuinely decompose.

**Counterexamples actively checked:**
- **Shared authority**: each component can choose its own ideal action, but an owner prohibits mismatched pairs \((0,1),(1,0)\). Local risks sum to zero under full local observations; global cost becomes 1/2, because the admissible action set is not a product. Under the restricted authorized oracle, observation regret remains zero; the excess is a *rights-imposed* cost.
- **Correlated change processes**: component A's own observation hides its state, while B's reveals its (perfectly correlated) state. With the same additive losses and unconstrained independent action menu, a global policy seeing both signals has risk zero while the sum of locally chosen risks is 1/2. This violates prior independence, not source decomposition. It cautions against extrapolating syntactic file/module independence to independence of future requirements.
- **Cross-component verification/coordination cost**: a non-additive penalty for jointly selecting both locally correct actions breaks the additive risk identity even if the prior is independent and observations complete. With an extra cost 3 for both correct joint actions, the global optimal cost becomes 1 rather than local sum zero.
- **Hidden context-specific rights**: in state 0 only action 0 is allowed, state 1 only action 1, but both produce same visible signal. Both state-aware oracles exist; NO uniform authorized observation-based policy exists. Do not replace this logical infeasibility with a made-up finite average loss. Revealing the state restores feasibility if selecting the respective actions is within the actual permissions.

These examples are finite model artifacts, NOT demonstrated bugs in authentic chi/restic code.

## 2. Distinguish "cannot act", "cannot know", and "too costly"

With **a robust authorized policy existing**, define all with the SAME cost/environment basis:
- \(R_{\rm free}=\sum_s p_s\min_{a\in U} L(s,a)\): hypothetical action oracle ignoring ownership permissions.
- \(R_{\rm auth}=\sum_s p_s\min_{a\in\Gamma(s)} L(s,a)\): state-aware **authorized** oracle.
- \(R_{\rm obs}=\sum_v\min_{a\in\cap_{s:z(s)=v}\Gamma(s)}
   \sum_{s:z(s)=v}p_s L(s,a)\): predecision observable and robustly authorized policy.

Then, if every fiber admits a feasible common action,
\[
\boxed{R_{\rm obs}-R_{\rm free}=
\underbrace{(R_{\rm auth}-R_{\rm free})}_{\text{authority deficit}}
+\underbrace{(R_{\rm obs}-R_{\rm auth})}_{\text{observation deficit}}.}
\]
Both terms are \(\ge0\). If a fiber's authorized intersection is EMPTY, report "NO UNIFORMLY AUTHORIZED POLICY" **separately**, rather than inventing a regret number. This telescoping cost accounting is mathematically elementary, and it does not mean an owner access restriction is wrong or should be removed. Safety constraints can rightly impose a cost.

**Crucial negative control:** zero observation deficit does **NOT** imply good maintainability or low total cost. With perfectly observed states but a global owner restriction forbidding the desired action, observation deficit = 0 but authority deficit = 1/2. Earlier EvoNOMOS prototypes which only compared observation regret would silently miss this source/governance barrier.

This yields a concrete non-overclaiming *research instrumentation proposal*: report a vector
\[
\left(\mathbf 1\{\text{uniformly authorized policy exists}\},\
R_{\rm auth}-R_{\rm free},\
R_{\rm obs}-R_{\rm auth},\
C_{\rm source}+C_{\rm verification}+C_{\rm governance}\right)
\]
rather than a single "modularity score". Actual prices and all weights are still unmeasured. Similar distinctions already exist in formal verification/access control/decision theory; novelty would be source-backed predictive application, not the bookkeeping.

## 3. Actual real Go source extraction — bounded truthful evidence

The SOURCE bridge in this turn is small but **real**. Original P35-P7 LIVE and SNAPSHOT were independently compiled Go source alternatives authored Oct 9 and used in the later #1247 customer source test. The read-only [Go AST inspector](source_ast.go) parses:
- LIVE original blob \`ad9a2fbc0a30a39475f746068e74e2d3e6c93999\`,
- SNAPSHOT original blob \`e9ca2c3863d5aa06ef0f0b9d168ddcf184713d75\`.
It extracts the actual \`HeaderRouter.Handler\` returned request closure and distinguishes \`hr\` registry references in LIVE from precompiled \`groups\` references in SNAPSHOT; it also normalizes the authentic \`NewPattern\` function AST for both and verifies their SHA-256 identities match.

[Native GitHub Actions #42927259856](https://github.com/WhoSia/EvoNOMOS/actions/runs/42927259856) and later [#42927544419](https://github.com/WhoSia/EvoNOMOS/actions/runs/42927544419) verified original Git blob hashes, compiled the Go parser and ran the static witness. This supports a real **source-visible difference in when registration-state data is referenced**, plus a shared code point consistent with #1247's equal classical fix. It does NOT prove source ownership, program contextual equivalence, a typed program repair grammar, policy optimizer extraction or effort outcomes.

This explicitly resolves one previously stated project weakness only **partially**: source AST-derived observation features now exist, while loss/Opt/permission extraction STILL require external hand specification. Never pass hand-authored \(\Gamma,L,p\) off as automatically derived from the Go AST.

## 4. Computational audit and falsifiers

[Executable exact rational model](compositional_authority.py) and [adversarial model tests](test_compositional_authority.py) implement local risk, statewise authorized oracle, global joint risk, shared action-right constraints, correlated priors, non-additive coordination costs and the two-deficit accounting.

- **20,736 exhaustive tiny authorization/cost cases**: all 16 binary loss tables per component × 16 × 9 nonempty state-wise permission assignments per component × 9. Under product assumptions, test the local/global exact risk and oracle identities, including cases without a uniform permitted policy.
- Separate case tests inspect authority coupling, correlations, non-additive loss, logical observation/permission conflict, and zero authorized regret despite positive owner-imposed cost.
- Prior [hypergraph model](decision_conflict.py) and shortest witness DP tests are run in the SAME workflow as regression controls, not a new scientific law certification.
- Latest [CI #42927544419](https://github.com/WhoSia/EvoNOMOS/actions/runs/42927544419) source-AST and Python tests passed. This verifies FINITE model code and BOUNDED original source AST witnesses, not scientific originality or source-to-Opt correctness.

## 5. Next meaningful mathematical and source research, with falsification

**Research target:** take actual source-proven contract-preserving repair programs with owner edit rights, obtain an **auditable abstract interpretation** of which repair actions are definitely feasible, possibly feasible, and source-proven client-correct. Prove a sound abstraction-to-conflict guarantee that does not invent optimal actions from static dependencies alone. In parallel, measure repair/verification costs in real code and independently issued future demands, then compare *equal information* against ordinary compiler/static analyzer, Parnas change-decision split, DSM, separation logic and constrained Bayes selection.

The immediate hard counterexample to overcome is a **shared owner or cross-module invariant**. Purely syntactic SRP/OCP/DIP-like decomposition does NOT imply cost/repair-policy decomposability; one shared permission boundary or correlated demand family can invalidate the factoring conditions while leaving the modules syntactically separate.

A useful nontrivial theorem would relate **checkable source separation conditions** to conservative factoring or non-factorization bounds under explicit client contracts and edit rights. A verified real-program extraction pipeline and prospective accuracy would be the possible publication contribution. A source AST checksum and hand-built finite decision table do not satisfy this.

**Result:** mathematics and bounded source AST instrument pass; source-governance effects still hypothetical, external coding-agent runs = 0; **P44 G1–G7 OPEN / LAW-R2 HOLD**.
