# P40-MATH-B-P4 — Prospective Source-Boundary Contract Identification: Mechanically Extracted Admission Semantics, Axiom Irredundancy, Certified Gluing Predictions & Classical Reduction Tests

**EvoNOMOS Generation VIII LAW-R1-P40 · 2026-10-10 KST · ORIGINAL SOURCE, PRE-REGISTERED BOUNDED PREDICTIONS, CLASSICAL REDUCTION · P40 OPEN · NEW OO LAW HOLD · LAW-R2 NOT_AUTHORIZED.**

## 0. Executive verdict and the exact experimental target

The testable dependent variable is **source registration admission**, not automatic satisfaction of every module's behavioral demand. Each pre-registered case is a two-edit Go HTTP-router program within an explicitly restricted grammar. All individually registered edits must be Go-accepted and must satisfy the old client GET /old and their own new request probes on isolated instances. The joint edit is either accepted (no source-registration panic), or rejected (the pinned original implementation reports a registration panic). For an accepted joint edit, independent HTTP client probes are tested except where **intentional duplicate overwrite** makes the first independent new-client demand no longer simultaneously satisfiable; see Section 4. Failure to keep these outcome levels distinct would falsely certify SafeGlue.

**Prospective frozen admission forecasts: 16/16 supported by the original pinned Go source.** The corpus is constructed from known families with *new* route instances, not a random sample of real maintenance commits. The result is a narrow prospective operational verification, NOT general predictive accuracy or proof of a new foundation for SOLID.

## 1. Immutable pre-registration / temporal evidence barrier

Commit order is part of the experiment. At [forecast-frozen commit 119a83e096203442e54cb8271b3372b0e3ae9412](https://github.com/WhoSia/EvoNOMOS/commit/119a83e096203442e54cb8271b3372b0e3ae9412), the [16 frozen forecasts](../../tools/p40-math-b-p4/preregistered_predictions.json), Go AST source extractor and source-anchored forecast checker were present, but NO native holdout Go test files existed under the three subsequent experiment module paths.

[Pre-registration and mechanical AST gate Actions #38050885409 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38050885409), checked exact source HEAD 119a83e096203442e54cb8271b3372b0e3ae9412, artifact 11668554767 SHA-256 4b29904f40eb569f28a8e4050ab763b6839e32995b2c09e2192f82fad60e0837.

The later original-Go CI explicitly checks (i) the frozen commit is an ancestor of the native test run, (ii) the original forecast JSON has *byte-identical* content to the frozen ancestor (via git show + cmp), (iii) no native holdout Go test existed at that ancestor, and (iv) the checked third-party source matches the exact SHA. Early attempts #38050822042 (JSON key case mismatch) and #38050998893 (two Go test-harness compile errors) failed and were transparently repaired **without changing the 16 frozen predictions**. No success claim is based on those failed runs.

**Crucial methodological distinction:** The Go parser/AST mechanically confirms 12 selected code-level syntactic signals in the original implementation functions. The subsequent bounded forecast function was **human-authored from those source facts**, not mechanically inferred as a complete executable semantic specification. Call this *AST-anchored source-contract identification*, not fully automated extraction of arbitrary Go admission semantics. This constraint is part of the pre-registration document.

## 2. Three pinned, unchanged source ecosystems and observed controls

| Ecosystem | Exact external source SHA | Source contract extracted as bounded signal | Native future-edit forecasts |
| --- | --- | --- | --- |
| go-chi/chi v5 | 167e1e3bd039d060696b99c8da4e876ae04f42c1 | Mux.Mount uses tree.findPattern route reservation, shared-tree alias rejection, mALL; Mux.Use rejects late route-stage insertion | 5/5 |
| julienschmidt/httprouter | 484018016424d215c0b87c42f4c9b57d980fbd00 | Router.Handle indexes the radix root by HTTP method; node.addRoute detects wildcard/static and duplicate-handle conflicts | 6/6 |
| labstack/echo v5 | 3882266a3641a36fc2111b48cd597adab1c1ecea | DefaultRouter.insert models static and parameter children separately; Echo.New enables duplicate route overwrite by default | 5/5 |

The pinned httprouter upstream master commit is dated 2024-01-30; it is an **independent source ecosystem**, not evidence of active maintenance in 2026. The Echo pin has an observed upstream commit in October 2026. Original third-party source was checked out separately and NEVER modified.

The [native holdout CI #38051063271](https://github.com/WhoSia/EvoNOMOS/actions/runs/38051063271) passed **all three jobs** at tested HEAD d294b1b1f221bdb70ee462869535b4ad8e2b3b28:
- χ: 5/5, artifact 11669815022, digest sha256:3f9e6bce44aeece41fc027001bc5f4956891ccd3c64a823a977092f83d892f3e.
- H: 6/6, artifact 11669557624, digest sha256:3eee9931fe04d3f56798af931bc57ac618884e9b9f21969c3423c65c661cc7ea.
- Echo: 5/5, artifact 11668614874, digest sha256:57ecbf9480d1c149af591ae5ee338444f053eee6cf89faca21bd58dbee7c0c0f.

The original Go integration tests independently check each edit in isolation, native two-edit registration success/rejection, old GET /old, and admitted nonoverwriting new-client responses. Existing prior P3 proofs are **not** counted as these 16 observations. The test cases are new route strings in a bounded design-family; data dependence on prior P3 mechanism selection remains and must be disclosed.

## 3. A single source-oblivious signature cannot identify admission across these implementations

Let \(\sigma(x)\) report a paired route-template/method specification, individual admissibility and selected single-module HTTP client observations, omitting the implementation's actual route-registration algorithm. Let \(A(x)\) be joint source admission. Compare, for example, the same paired source requests:

- A: GET /pros/:tenant/reports;
- B: GET /pros/public/health.

The individually accepted edits and declared clients can be matched, but the shared GET-method wildcard/static routing tree in original H rejects the joint edit while Echo's static and parameter children admit both orders.

**Classical factorization obstruction (bounded):**
\[
 \sigma(x_H)=\sigma(x_E)\quad\text{and}\quad A(x_H)\neq A(x_E)
 \quad\Longrightarrow\quad
 \nexists f:\operatorname{codom}(\sigma)\to\{0,1\},\ A=f\circ\sigma .
\]
Proof: applying \(f\) to equal arguments must yield equal results, contradiction. Lean P3 already proved this general no-factorization implication. The current P4 prospective native source checks corroborate the concrete witnesses. There is NO assertion of whole-program contextual equivalence, and a classifier equipped with actual implementation semantics is not ruled out.

A particularly revealing P4 counterexample is Echo **ECHO-OVERWRITE**: both independent same-method edit registrations on the same route are locally permitted, and joint registration is also **source-admitted** because the default Echo configuration permits overwrite. Yet the LAST module's response replaces the FIRST module's independently required new-client response. Thus:
\[
\operatorname{SourceAdmit}(A;B)\not\Rightarrow
\operatorname{NewClientContract}_A(A;B)\land
\operatorname{NewClientContract}_B(A;B).
\]
This distinction is an actual behaviorally observable violation of the **stronger** global SafeGlue criterion despite source-admission success. It is not one of the six registration failures. Source-admitted cases = 10; source-rejected = 6. Of the accepted cases, **9 are nonoverwriting joint combinations satisfying both selected new-client expectations**, and 1 (Echo duplicate overwrite) intentionally lacks simultaneous preservation of the first new client's demand. This is explicitly captured by the native test oracle; do not quietly count it as SafeGlue.

## 4. Independent client-frame deletion witness beyond source admission

A supplemental, **post-prereg exploratory** original χ experiment compares:
- an otherwise identical source-accepted parent and child mount with no global middleware;
- a source-accepted parent that installs header-setting global middleware BEFORE the old route and mount, respecting chi's temporal registration rule.

Both variants admit registration; both return the unchanged old GET /old response **body** and the expected child /item response body. But the middleware changes the old client's observed HTTP header X-P40-Frame. If the old client contract includes full headers, the latter program violates it although namespace, alias and staging admission guards all hold. The source test is [client_frame_independence_test.go](../../tools/p40-math-b-p4/chi/client_frame_independence_test.go), independently verified by the updated [native Actions #38051201898 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38051201898) at tested HEAD 4aa8992b920f06bdc93f7e7f0544dc63c9e8ca1c.

This supports the **irredundancy of a separately specified old-client observational frame obligation** with respect to source registration predicates, not logical independence of every historical SOLID norm.

## 5. Classical competitor and ablation court — no novelty laundering

Compare deliberately weaker classifiers with a classical source-aware CSP explanation on the 16 cases. The outcomes are externally established by the native original Go Actions before baseline scoring. The scoring script uses the *already-validated frozen labels* as its reference (not an independently sampled empirical dataset).

| Model | Correct/16 | Interpretive scope |
| --- | ---: | --- |
| Both edits locally accepted ⇒ always predict joint admission | 10/16 | misses all 6 source-admission failures |
| Source text/method exact duplicate rejection only | 11/16 | misses 4 structural clashes and incorrectly rejects Echo's legal overwrite |
| Implementation-aware classical CSP with method-index, trie reservation and overwrite policy | 16/16 | accounts for every bounded admission result, SAME source-aware logic as the P4 rule |

[Classical baseline source](../../tools/p40-math-b-p4/classical_reduction_court.py) · [Actions #38051264475 SUCCESS](https://github.com/WhoSia/EvoNOMOS/actions/runs/38051264475), checked code HEAD d8e57740aad1fe6f7f754e2eeeeb8a04414b4b35; artifact 11669682649 SHA-256 79ee4638c7117a505be05f2af521ba32f70e89c4b4e96b8a305777f0ea396f43.

**Judgment:** classical CSP, source-dependent abstraction and separation/frame reasoning are sufficient competitors here; the same source-aware rule can be written as an ordinary finite constraint relation. A 16/16 outcome on a hand-designed holdout is NOT statistical proof of generalization, source correctness for arbitrary router languages, or evidence of mathematical priority.

## 6. Axiom irredundancy and Lean proof budget

Avoid the circular shortcut of defining a gluing axiom to mean "global gluing succeeds." Premises have to be verified by independent source facts, ownership metadata, compiler acceptance or actual old-client oracles. Status of the original Math-B premise kinds:

| Candidate source/semantic obligation | Independent evidence and proof status |
| --- | --- |
| A: syntax, static type and compiler acceptance | All tested heldout Go harnesses compile in successful runs; standalone *logical independence from all other kinds* UNPROVED |
| B: behavioral old-client frame | Original χ full-header witness shows source-admission success does NOT entail full old-client observation preservation; limited nonentailment grounded |
| C: owner/history-indexed edit rights | Earlier Math-B source-only non-Markov countermodel is conditional/synthetic; no authority claimed from public upstream maintainers |
| D: invariants, checkpoints and demand completion | Echo source-accepted overwrite refutes joint demand satisfaction from admission alone; complete irredundant axiom statement OPEN |
| E: source boundary and composition | Original χ namespace/alias/stage deletion witnesses, independent H/Echo source-algorithm reversal and 16 prospective admissions; bounded real source |
| F: dependency/capability incidence | Cannot be read off runtime traces alone (prior P39/P40); new independent native source premise countermodel OPEN |

Lean proof program: in addition to prior minimal-future-edit quotient necessity and N/R/T model independence, the new P4 file [P40MathBIndependence.lean](../../tools/p40-math-b/lean/P40MathBIndependence.lean) attempts a **genuinely non-circular classical resource-store** frame lemma. For distinct resource coordinates \(a\neq b\), updating \(a\) and \(b\) commutes and updating \(a\) preserves observations from unrelated coordinates. For identical coordinates, distinct writes do not generally commute. This is a source-*analogy* to separate method tree roots, not a formal Go implementation correctness theorem. **Record Lean kernel PASS only after checking the separate latest hosted run.**

The ultimate complete six-axiom independence theorem and strict derivation of historical SRP/OCP/LSP/ISP/DIP remains **UNPROVED**. Conjoining labels, selecting examples after outcomes or defining premise predicates as the target conclusion is explicitly disallowed.

## 7. Falsification program beyond P4

Meaningful next work:
1. Choose prospective *real-world PR/issue-derived* route edits from actively maintained projects and pre-register predictions without using test outcomes to choose the scenario. The present fixed route family is controlled but not an independent distribution.
2. Mechanically extract a **proof-carrying abstraction** from the AST and dataflow/alias/control flow, rather than manually verifying existence of chosen AST source anchors; formally validate a simulation between extracted source abstract transitions and actual language semantics.
3. Require source-realized independent countermodels for each new claimed axiom, with permission/ownership claims distinguished from freely invented laboratory policy.
4. Attempt to defeat **exact implementation-aware CSP + frame + behavioral refinement**, not weaker HTTP-language-overlap straw men. If classical theory explains outcomes, record classical collapse.

**P40 remains OPEN. LAW-R2 NOT_AUTHORIZED. NEW FOUNDATIONAL OO LAW HOLD.** This P4 provides time-ordered native-source predictions and sharply bounded necessity/incompleteness findings, not a universal mathematically new law.
