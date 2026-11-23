# P44 — Actual Original Chi Heldout Classical Selective-Gate Test, Including Failed Policy Prediction

**2026-11-10 KST · COMPLETE SOURCE-RUN SUCCESS / SCIENTIFIC POLICY NEGATIVE · AUTHORSHIP WhoSia · NO new causal architecture law**

## A. Full real-source rerun

[GitHub Actions #42755665543](https://github.com/WhoSia/EvoNOMOS/actions/runs/42755665543) SUCCESS. It clones the full public original Go source \`go-chi/chi\`, asserts exact Git commit \`67be7d9cafdaeb4e04e887ff78d09e030ee43b00\` (v5.1.0), rejects a shallow history, reads immutable [pre-2020 original B1 model seal](../../../../tools/p35-p5/seals/predictions-2020.json) and recomputes original nonmerge 2020–2024 triad-file Git cochanges via actual \`git log\` / \`git diff-tree\`. The original source reproduction guard matched precisely **40 commits, 47 seed queries, 13 positive cochange seeds, 34 singleton negative seeds**; always-alert B1 again has 9 correct locations, 34 singleton false alerts, matching P35-P5's published original counts. Both local standardized test job and full-history original source CI passed; full-history run contains **8 Python unit tests PASS** and a CI artifact JSON. No new Go production patch or maintainer agent was executed, and no semantic claim about necessary joint modification follows from cochanges.

**Pre-execution new rule** frozen in [commit d9ccccfb](01_P35_B1_CLASSICAL_SELECTIVE_GATE_PREEXECUTION.md), before this source rerun but after original holdout aggregates were already known: alert iff the previously sealed B1 top-partner frequency (context:22/33, mux:34/83, tree:34/64) is **strictly above 0.5**. It predicts alerts for context/tree seeds and abstention for mux. Threshold not tuned after observing this rerun. It is nonetheless **post-aggregate exploratory, not independent prospective**.

| Policy | Alerts | Correct source partner among positive | Wrong source partner among positive | False singleton alerts | Missed positive cochanges | Counted unit loss (false alert + wrong partner + missed positive) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| B1 always-alert | 47 | 9 | 4 | 34 | 0 | **38** |
| B1 0.5 selective | 26 | 6 | 2 | 18 | 5 | **25** |
| No-alert baseline | 0 | 0 | 0 | 0 | 13 | **13** |

Interpretation: filtering the original always-alert B1 reduced false alerts 34→18 and equal-unit loss 38→25. It ALSO missed 5 real cochange opportunities and dropped source-site hits 9→6, so it did not beat the trivial never-alert baseline at the chosen equal-unit loss. **There is no proof that an independent maintainer should actually omit repairs:** a Git coedit is not required repair proof, and miss-vs-alert costs are not measured.

## B. Immediate after-run logical correction: the 0.5 preseal was NOT a true Bayes-optimal gate for this task

**Keep the preseal unchanged; explicitly correct its justification here.** The frozen scalar from \`B1PairEvents/B1SeedEvents\` estimates training propensity for the *chosen top partner* to be coedited, \(p_{\mathrm{top}}\). But the scored binary question "is ANY other file edited?" has different probability \(p_{\mathrm{any}}\), generally \(p_{\mathrm{top}}\le p_{\mathrm{any}}\). Our scored loss also penalizes an alert that points at the wrong extra file as a failed location prediction. Therefore interpreting \`p_top>1/2\` as a **Bayes optimal binary ANY-extra-file gate** is not justified. That would only follow under restrictive conditions such as a unique feasible additional partner and calibrated probabilities, with the decision loss correctly matched to that target.

At equal one-unit false-alert, wrong-location, and missed-positive costs, the EXPECTED alert loss is \(1-p_{\mathrm{top}}\) (assuming alert succeeds exactly when that particular partner is coedited, with correct counted cost), while no-alert loss is \(p_{\mathrm{any}}\). So the ideal decision would alert iff:

\[
\boxed{p_{\mathrm{top}}+p_{\mathrm{any}}>1.}
\]

Those two probabilities must be estimated/calibrated separately using **precutoff training only**, with adequate uncertainty handling and an abstain option. Setting \(p_{\mathrm{any}}=p_{\mathrm{top}}\) without demonstrating equivalence is a misspecified target, potentially itself causing the negative test. Also, on multi-partner events with the top partner present, the binary "correct partner" metric may miss other required sites: even an alert marked correct does not certify complete repair.

A stronger classical selective policy should first predict the need for any extra-file change, then rank/inspect candidates and finally verify full old/new clients under actual source repair rights. Such a full model was **NOT FIT OR TESTED** this turn.

## C. Connection to 0.3 maintainer and founding law object

Early 0.3 original reported scripted synthetic maintainer architecture interaction, and MaintainCoder audit already warned that code-score location alone is not lifecycle utility. This actual original Chi source run shows why: an information tool can perform tolerably on known positive localization (9/13) yet cause substantial false work or omission under deployment loss. The correct conditional design estimand must include architecture × decision policy/maintainer × demand × observation budget and **actual completed repair quality**, not only syntax location hits or speed.

The original 0.4 dependency-atom analysis additionally warns that predeclared helper vs interface port vs composition root need legitimate background configurations. None of this study identifies a novel architecture-specific treatment effect or probes new maintainer execution. It does, however, expose a clearer **future experiment failure criterion**: a structural prediction is not actionably superior unless its decision gate reduces regret vs even a no-action comparator on the same dataset, without harming real customer obligations beyond a declared acceptable level.

## D. Research status

- Genuine original public Go Git history rerun: SUCCESS.
- Pre-outcome source-rerun cost-sensitive rule: RESULT NEGATIVE vs never alert.
- Distinct any-cochange gate calibration: OPEN.
- Actual paired source-architecture × equal-information coding agent factorial: NOT RUN.
- True unseen later customer demand, actual maintainer effort, rights, multiobjective causal lifecycle outcomes: OPEN.
- No false claim of independent 47 statistical observations: the 47 seed queries cluster in 40 commits; this deterministic descriptive table supplies **no population uncertainty inference**.
- G1–G7 OPEN; C5 NOT verified; LAW-R2 HOLD.

**Use this negative result to prioritize the real two-stage repair-decision/maintainer-interaction experiment. Retire more toy dataflow / Viper provenance demos as research mainline.**
