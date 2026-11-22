# Paper B R32 — The Authority Trilemma and Nearest-Prior-Art Defeat Court (2026-11-23)

**Source status:** directly reopened v31 and LIRA audit, project author-constructed fixed patch, 2026 founding-intent record and prior collision ledger. Also inspected current public full-text arXiv HTML for *Position, Role or Label?* and *Precedent or Intent?* on 2026-11-23. No original agent experiment was conducted. Internal review roles are not external reviewers.

## One-sentence severe diagnosis

**"Authority" is made to mean three different things without admitting the category changes; the historical premise and the laboratory example independently support conditional design judgments but do NOT themselves imply AI agents actually invest named principles with excessive power.** A reader can accept both premises yet see no distinctive research programme unless the bridge is stated as a comparative *question* with falsifiers.

## A three-way separation (not a discovered ontology)

| Object | Working operational definition | Example in Paper B | Distinct outcome |
| --- | --- | --- | --- |
| **Epistemic warrant** (grounds) | Technical reason offered to apply a heuristic to this change and protected obligations | OCP is useful if likely changes fit the selected extension boundary | Source/contract-compatible rationale, grounded explanation |
| **Deontic permission** (authorization) | Whether the agent/reviewer has the legitimate right/obligation to take a particular action under the actual authorized instruction hierarchy | A high-priority maintainer explicitly requires an OCP-compliant design; sources are tool observations | Authorized accept/reject/escalate/action; avoid describing legitimate compliance as error |
| **Causal uptake** (behavioral influence) | Whether exposure to a principle changes patch or judgment when source/task/roles are controlled | Named OCP guidance versus neutral guidance | Observed code diff, acceptance, revision or abstention |

An agent can have correct permission but a weak engineering rationale; correct rationale without permission to modify production; or a strong causal response without either. These cases are NOT logically interchangeable. The "operational quasi-axiomatization" hypothesis should be scoped to an **unwarranted transfer from heuristic status to patch-governing reason under actually applicable requirements**, and measured only where roles and evidence allow such a claim. A model need not internally 'believe' in axioms.

## Primary source witness: the limitation of code-only diagnosis

[Actual constructed fixed patch and case table](31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md) keep two legacy source files byte-identical and add a provider; the provider nevertheless changes rendered book prefix from `book` to `BOOK` and excludes errata. Acceptability flips between a report-only, unprotected-prefix contract and a protected-prefix or errata-required contract. These are declared research-author conditions, NOT historical Meyer text. The **strong inference** is that code-byte-only acceptance cannot decide contract acceptability across these worlds. The **weak inference NOT established** is whether an agent adopts a famous principle as if it outranked the contract; no live agent trials with those conditions were run.

The example can be criticized: its role is an *illustrative contractual non-identifiability witness*, not evidence that a well-specified standard evaluator cannot classify a violation. A code-only analysis might correctly say the candidate does or does not have a specific structural trait; it is only the *maintenance verdict* that depends on project-specific obligations. Preserve that subtle distinction.

## Newly inspected 2026 nearest direct rivals (more damaging than generic instruction papers)

1. **Anish Laddha, Nitesh Pradhan & Gaurav Srivastava (2026-10-23)**, [*Position, Role or Label? A Controlled Study of Instruction Conflicts in LLM Agents*](https://arxiv.org/abs/2610.33201). Abstract and full-text introductory methods inspected. 1,080 code-scored scenarios, 14 open-weight models, ~1.89M scored replies, interventions separating textual labels, message order and actual roles. **Defeats** broad novelty of experimentally separating role and label in instruction conflicts. It studies instruction arbitration, not the historical appropriateness of OCP for a particular legacy-client contract. Re-read full study before claiming a quantitative comparison to our proposed results.
2. **Haichao Zhu, Geyang Xu, Zhaorui Yang, Jiyuan Wang & Qian Zhang (2026-10-28)**, [*Precedent or Intent? What Coding Agents Follow When Evolving Existing Code*](https://arxiv.org/abs/2610.38244). Abstract and study framing read: 5,625 agent trials on precedent, agent defaults and explicit instructions, plus real repository validation. **Defeats** general claims that nobody has studied source precedent versus new instructions in coding agents. Their primary endpoint is implementation-choice preference where both can meet functional requirements, not necessarily named historical design principle + explicit *old-client acceptance oracle* + evidential withdrawal. But overlap is significant.
3. **2024 design-decision research agenda**, [*When rationality meets intuition: A research agenda for software design decision-making*](https://doi.org/10.1002/smr.2664), web source discoverable but publisher full-text access blocked in this pass. This is **explicitly NOT read in full**; title/metadata alone makes it a required comparison for any claim to have newly invented cross-disciplinary design-decision scholarship.
4. **2026 architectural rationale work**, [*Using LLMs in Generating Design Rationale for Software Architecture Decisions*](https://doi.org/10.1145/3785010), publisher summary checked, original full article not read in this pass. It challenges novelty of architecture decision rationale and LLMs as an unstudied pairing.
5. [*Toward an Evidence-Based Template for Agent Instruction Files*](https://arxiv.org/abs/2611.02383), 2026-11-02, studied 3,387 files from 1,000 repositories and maintenance of agent instructions; broad instruction genesis may already be mapped but is not a complete *SOLID historical lineage*.

### Status adjudication
Paper B's positive proposal is **not** "the first to connect software decisions and AI", nor "the first to manipulate instruction labels", nor "the first to show that existing code competes with instructions." What remains intellectually ambitious: studying **how a principle's scope conditions are preserved, omitted or renegotiated when an agent is asked to make a contract-sensitive change**, and deciding which observations would support or defeat an *operational authority transfer* explanation rather than familiar requirement-traceability and instruction-arbitration explanations. That is a research design and synthesis, not firstness certification.

## LIRA 0.1 — the important v31 revisions (scores are subjective keep-worthiness, not scientific truth probabilities)

| Exact v31 phrase | Keep score | Diagnosis | Required decision |
| --- | ---: | --- | --- |
| "그 원칙이 바로 이 코드를 바꾸라고 말할 권한은 어디에서 오는가?" | **0.99** | Distinctive authorial question, but rhetorical "권한" has at least three meanings | Keep ending and explicitly disambiguate earlier |
| "조건부 조언이 출처와 적용 범위를 따지지 않은 채 패치를 움직이게 되는지를 묻는 작업이다." | **0.95** | Good proposed target | Keep with non-observation language |
| "설명을 돕는 말이 실제 수정 권한을 행사하려면 ..." | **0.53** | Inappropriately merges a reason for a change with developer authorization | Rewrite as two distinct concerns |
| "원칙의 이름은 그 답을 대신하지 않는다." | **0.99** | Sharp hinge anchored in Martin example | Preserve untouched |
| "이 역사에서 얻는 교훈은 SOLID의 원저자가 틀렸다는 것이 아니라" | **0.58** | Recurrent defensive A-not-B sentence, wrongly singular "SOLID의 원저자" to Martin and Parnas; SOLID acronym later | Replace by direct source description |
| "새 수학 정리를 제시한 것은 아니다." | **0.34** | A generic disclaimer after a lively example drains rhythm; empirical status in footnote/intro suffices | Cut from main prose |
| "이 연구는 실패한 에이전트를 찾아 SOLID를 비난하려는 계획이 아니다." | **0.43** | Same generic pre-emptive denial; move the actual adversarial outcomes into a strong positive sentence | Cut |
| "원칙을 강조한 쪽이 기존 계약을 더 잘 보존하거나 ..." | **0.97** | Real counterhypothesis / reversal | Keep as substantive positive outcome |
| "역사 연구자는 ... 소프트웨어 공학 연구자는 ..." | **0.80** | Good interdisciplinarity but may read like an internal project plan | Condense into connected reader-facing prose |
| "정오표를 지원하지 않고 ... book/BOOK" | **0.94** | Precise author-built case but no file/contract history in body | Preserve provenance in nearby sentence, cite linked witness |
| "AI가 코드에 붙인 'OCP 위반'이라는 표지를 ... 끝까지 확인하는가?" | **0.96** | Crucial bridge from stable source to agent decision | Add the counter-case where principle **properly** motivates rejecting an implementation |
| "철회 가능해야 한다" / "For engineering decisions, authority should have conditions of withdrawal." | **0.78** | Normative thesis but danger of implying a tool-output countermand overrides system-level policy | Restrict revision to authorized applicable evidence; otherwise escalate under instruction hierarchy |

## Three legitimate scope failures

**F1 Category confusion:** An OCP label could be *structurally correct* even when patch is contractually acceptable. No reason to ban labels. Research **transfer from label to disposition**, not "all labels are wrong."

**F2 Policy overreach:** An explicit authorized strict policy can rightfully reject a patch despite otherwise passing functional contract tests. Do not equate that with scientifically wrong reasoning; record authorization separately.

**F3 Historical transmission gap:** Martin's own exceptions prove contextual source reasoning, NOT empirical loss of qualifiers through 30 years of education and AI training. A genealogy study needs textbooks, style guides, repo instruction records, dated changes. Until then phrase as inquiry rather than asserted chain.

## Editorial decision

**v32 should keep** the author's title/question, initial drawing scene, book/BOOK case, qualified experiment invitation, long-range theory ambition. **v32 should repair** the triple equivocation, show one valid principle-conforming counter-case, and replace defense-heavy paragraphs with direct positive analysis. Do not mechanically score all sentences or force uniform rhythm. One concise new metaphor is permitted only if it clarifies rather than decorates; let the prose do most of the work.

**Hard stop:** This critique is not peer-review confirmation and does not establish an observed AI effect; it is internally reasoned and grounded to a re-opened project artifact and cited public 2026 study text.
