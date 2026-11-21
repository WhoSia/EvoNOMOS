# Paper B v17 — Adversarial Editorial Review and Claim–Evidence Court (2026-11-21)

**Review mode:** rigorous *internal* critical referee, not independent external peer review. Manuscript v17 was read through its exact prior v16 source and target edits, and four original PDFs were inspected. Reviewed source [v17](PAPER_B_BILINGUAL_INTEGRATED_17_20261121.md). Do not attribute this review to an external scientist.

## 1. Core editorial decision

**Promising narrow research question, but HOLD on external validity and independent inference.** The paper can provide a serious conceptual/replication note on conditions under which OCP violation judgments warrant rejection of *one fixed patch*. It cannot establish industrial prevalence, a new general semantics of code review, causal harm from SOLID advice, or strong statistical outperformance.

The strongest claim is not “models violate OCP” or “principles cause wrong decisions”; it is the distinction among:
1. a classifier assigning a design-principle category;
2. an executable patch satisfying a *declared* new requirement and maintaining specified old obligations;
3. a reviewer having enough sourced information to promote that category into a rejection of this particular patch.

The third step is a question of inference-to-use, studied broadly before in Kane (2013) and requirements engineering; v17 supplies one carefully controlled, reproducible *case*.

## 2. Claim–evidence matrix: accept, narrow, or drop

| Manuscript claim | Evidence read | Defensible version | Required competitor |
|---|---|---|---|
| OCP has historically conditional meaning | Meyer 1988 1st ed., Martin 1996; archive 25 study | Cite specific stable specification, anticipated change and sorting responsibility passages, not industry-wide loss of nuance | Primary Meyer/Martin exact pages; historical commentary |
| 768 OCP records audited | Original archive + independent JSON audit documented in v16 | 768 **saved responses** from 48 unique submitted codes; 16 runs per code; 24 masked instruction templates; 64 fixed model-strategy-language cells | Archive provenance, repeat counts, normalization/AST caveats |
| Templates lack case-specific requirement | Frozen masked *instruction portion* inspected | No separately stated case-specific maintenance request or protected old caller in masked scaffolds; source code may have comments and clues | Pehlivan et al. task definition and actual JSONL entries |
| A fixed patch changes its accept/reject across contracts | Authored catalog code, predetermined requirement and old contract | One patch yields 1 YES/3 NO under author's four constructed worlds, not votes or adoption | Source outputs, proof that specified obligation is authoritative |
| Partial disclosure yields 1/5/3 | Four-world truth table and Chat26 independent 30-test CI | Exactly nine *information states*, one ACCEPT/five REJECT/three HOLD | Basic Boolean logic, no novelty credit |
| Reviewers in industry over-axiomatize | None | Hypothesis, not tested | Widyasari explanation corpus, Papotti actual review choices |
| LLM rationale generates overcorrection | Jin & Chen 2026 tests three benchmarks/five LLMs | External study's finding only; not experimentally replicated by Paper B | Jin & Chen current journal vs held arXiv-v1 edition |
| Acceptable PR means full requirements solved | Ling et al. 2026 public PR trajectories | NOT valid; accepted/merged/issue closed and requirement satisfied separable | Ling et al. primary examples |
| Existing call-path constraint matters | Authored drawing-function fixture | Alternative callable may satisfy new-entry-point request but not preserved old-entry-point requirement | Source-specific tests + Parnas uses relation; no architecture cost causal claim |

## 3. Four major referee objections

**R1: Normative circularity.** Table 2 was designed by the same authors who defined the contract. Hence obtaining a contract-dependent decision is logically inevitable. It is still valuable as a transparent witness, but the paper must neither present it as an observed reviewer failure nor infer field frequency. The substantive question is whether authentic project evidence can make the *contract choice* identifiable.

**R2: Dataset-to-patch transport.** Pehlivan's benchmark rewards violation classification. The catalog and reference-pair 37 are separate; no causal line connects a particular saved OCP output to an actual rejected patch. The precise inferential danger is *future downstream reuse* of a classification for rejection without project-specific demands. State this as a conditional risk, not the history of the benchmark itself.

**R3: Prior empirical explanations and judgments.** Widyasari et al. use 793 coded comments and already classify rule/principle justification; Papotti et al. directly measure human adoption of machine-proposed patches using 72 masters students; Jin & Chen quantify false negatives/false positives under requirement specification; Ling et al. demonstrate negotiated completion and deferred obligations. Paper B cannot claim that any of these questions went unstudied. Its narrow advantage is an **auditable evidence certificate for a fixed executable example**, not statistical novelty.

**R4: Independent validity and ecological inference.** The fixed library source was authored specifically to separate contract dimensions; different owners might use real contracts, backward-compatibility guarantees, constraints on changed modules or different behavior. Tests of hand-authored fixtures and static source signatures do not identify actual labor, user trust or cause of rejection.

## 4. Revision verdict by section

- Abstract: keep exact question and “over-axiomatization” defined as *misuse of conditional advice for a particular decision*. It must not imply historical evidence of field-wide misunderstanding. v17 stronger.
- §1: opening Martin scene is concrete and avoids listicle paragraphs; retain.
- §2: distinguish historical original source passages from retrospective public discussions; no teleological “SOLID became dogma”.
- §3: scope of 48 pairs/768 saved rows/24 templates/64 groups well delimited; formalize what code masking does NOT remove and define independent unit explicitly.
- §4: rivalry now present; make sure a reader can find *which* claim differs from each of four primary studies without narrative whiplash. Group Widyasari/Papotti (human observation) versus Jin (LLM conformance) versus Ling (process) in two successive paragraphs, as v17 does.
- §5: evidence certificate is new in manuscript v17 but classically elementary. Keep closest to Table 2 and explicit caveat about authored standards. Distinguish inconsistent evidence from legitimate HOLD.
- §6: original-call route problem stays short; a P44 Go adapter control is a secondary methodological analogy, not Paper B evidence. Prevent F37 code from overtaking paper B's scope.
- §7: close with a practical question: 'Which request, protected caller or authorized policy source makes this particular refusal warranted?' No claim of reviewer measured outcome.

## 5. Evidence debts and exact next empirical tests

1. Authenticated real-source request/contract provenance: an externally timestamped issue, API compatibility promise, test or PR comment *before* reviewing the source change.
2. Two independent annotators label evidence sufficiency without seeing the constructed answer; report agreement and disagreements, including cases where both abstain.
3. Source-specific judgment comparison: a principle-only assessment versus matched contract-evidence assessment on the same independently written patches, randomized order and bounded time, with outcomes not judged solely by the original author.
4. Before any claim that the “minimum-question” method reduces review cost, measure source lookups, questions, false rejections/acceptances and time; preserve all failure and abstention.
5. Compare with standard requirements-traceability, validation argument, conventional code review checklist and oracle-based program repair. If equal evidence suffices, report a classical TIE.

## 6. Current recommendation

**v17 is a credible research draft with unusually explicit claim ceilings.** A paper-ready submission still requires reference formatting, independent argument review, verifying original figure/caption and reproducibility appendix packaging, selecting a suitable article category, and at least one source-grounded real case if an empirical venue is sought. A conceptual position/methodological note can be narrower, provided it is unambiguous about its contributions and original sources.

**No new study of real reviewer decisions was conducted in this pass.**
