# Three readings on what an OCP judgment measures

2026-11-17 KST. Read from the three filed PDFs. Section and table numbers refer to those editions. This comparison supplies prior work and constraints for Paper B's historical argument.

## Bräuer, Plösch, Saft and Körner (2018)

In §3.1 the paper defines OCP by minimizing edits to existing source when functionality is added. §§3.2–3.3 describe six online focus groups with 31 experts overall. Three of those groups considered OCP alongside four other principles. §4.2 and Table 4 rank individual measurement practices. Avoiding runtime type identification and using interfaces as return types received moderate relevance, while the broad practice UseAbstractions ranked low. These are relevance judgments about specific practices under the study's method. The measures are neither interchangeable nor empirical tests of the time taken for a particular extension.

§4.3 makes the procedure visible. A participant divides 100 points among coverage by proposed practices, additional coverage by suggested practices, and aspects still uncovered, before privately reconsidering an interim group result. In Table 6 the three OCP groups allocate 9.0, 19.4 and 32.0 points to uncovered aspects. Table 11 reports 20.8 and ranks OCP highest in the paper's cross-principle summary. The simple unweighted mean of the displayed group values is about 20.13. Cite the group spread or describe 20.8 explicitly as the authors' reported summary. No assumption about the aggregation or an independently reproduced absolute rate is needed in the manuscript.

Paper B can state that attempts to make OCP inspectable were already accompanied by a check of what the chosen practices left out. What the elicitation estimates is coverage of a principle according to participants. We ask for evidence supporting an action taken on a particular patch, with different tests for different obligations. [Filed preprint](https://drive.google.com/file/d/1ez5xnadnq_x3ttLln3cvU-G_CNqhxrXS/view) · [DOI](https://doi.org/10.1016/j.jss.2018.03.002).

## Cabral, Kalinowski, Baldassarre, Villamizar, Escovedo and Lopes (2024)

§§3.2–3.8 use code taken from an industrial ML application, with randomized assignment to the original and SOLID-restructured treatments in three repeated trials. The 100 participants compare code through a questionnaire. §3.4 names two ordinal outcome families, perceived difficulty of understanding and agreement with expected benefits. The OCP scenario in §4 introduces additional regression models. The questionnaire asks about perceived understanding (Q9), ease of extension (Q11) and whether pre-existing code needed changing (Q13).

Table 6 and §5.2 report a pooled difference for Q9 without rejection in the Bari and PUC-Rio trials, and pooled differences favoring the SOLID treatment on Q11 and Q13. The study uses alpha = .10. The recruitment and source limits are discussed in §6. The questions are useful for understanding which benefits participants recognized under a specified task. Assignment was to a whole refactoring, and participants reviewed supplied code and answered questions. The study does not identify the isolated effect of OCP on executed maintenance time, defects or change locality.

This is a source for a concrete demand: new regressors may fit an existing extension seam. A different demand, such as changing a common evaluation protocol for all registered regressors, can motivate a follow-up case. That demand and its predicted effect would be EvoNOMOS hypotheses. [Filed authors' version](https://drive.google.com/file/d/1Jej4TkYvBj-5IXZ_FUiO62aihMK5MsRf/view) · [DOI](https://doi.org/10.1145/3644815.3644957).

## Zhu, Zhang, Wang, Yang and Qiu (2026)

§2 case 001 extends a C++ helper across three steps while holding app/main.cc call sites fixed. Both representative edits pass functional tests. The structural oracle demands a centralized reusable implementation and checks for generic-function patterns and a limit on explicit per-type overload definitions. Seventeen of the 23 configurations chose an overloaded implementation in that case. This is direct prior art for evaluating a change task under named constraints. It is also a place to distinguish a measurable oracle from a broader claim about field maintenance costs.

§3.2 and Fig. 3 place TASK.md on the model-visible side and SPEC.md and the evaluator on the author side. In case 021 the visible task requests an inline filter and preservation of existing behavior. It does not require reuse of the validation module in its wording. The evaluator inspects characteristics of duplicate parsing. §3.3 lists how functional and structural checks are combined. §5.3 reports 64 of 483 configuration–case outcomes passing the functional tests and failing the structural oracle. §6.2 limits inference to the authored small C++ repositories, one sample per configuration–case and case-specific structural constraints.

For Paper B, record separately which premises the evaluated agent sees and which criteria the evaluator enforces. A declared hidden oracle can provide a stable research measurement even when the agent cannot read it. A maintenance decision based on the output needs the scope of that criterion available for inspection. Paper B holds a candidate patch fixed and varies supported specifications. Both lines can use an observed witness, and their interventions differ. [Filed preprint](https://drive.google.com/file/d/1eJpWy7dYi9COw8dOb3NnVBF_F942Y8OH/view) · [arXiv DOI](https://doi.org/10.48550/arXiv.2603.27745).

## Keep distinct in the manuscript

| Instrument | Fixed or declared in that instrument | Outcome it warrants citing |
|---|---|---|
| Bräuer et al. | Principle definitions, proposed practices, assessment procedure | Expert assessments of relevance and coverage |
| Cabral et al. | An ML scenario and two code treatments | Participant perceptions under bundled assignment |
| Zhu et al. | Repository change scenarios and case-specific oracles | Functional and structural conformance rates on their authored suite |
| EvoNOMOS library witness | One patch, a fixed module boundary, declared alternative demands and client contracts | Whether a maintenance verdict remains invariant across these alternatives |

The comparison makes no claim of a single causal historical trajectory. It motivates two audit questions: what is visible to the party being evaluated, and what becomes available to the party deciding whether to rely on the score?
