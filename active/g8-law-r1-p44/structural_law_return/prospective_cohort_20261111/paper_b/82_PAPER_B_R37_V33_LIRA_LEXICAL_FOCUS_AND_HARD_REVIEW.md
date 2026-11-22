# Paper B R37 — v33 LIRA Cold Read: Protect the Core, Challenge the Words

2026-11-23 · **Selective internal editorial test of v33**. Score = subjective desire to keep this wording, not measured novelty, correctness, empirical reliability or "probability of author approval". This review does not simulate external peer approval or produce agent measurements.

## Global editorial verdict

The first chat's 2026-07-29 concern finally appears as the **paper's object**: when a defeasible SOLID principle is discussed as a violation, rule or quasi-axiom, does its textual force replace the conditions that justify applying it? Unlike v29's pure "OCP token effect" and v32's broader account of all kinds of authority, this is closer to the author's original irritation. The larger search for a higher-order structure is **one short concluding paragraph only**, while separate R36 memo handles it as an independent conjecture.

## Source- and phrase-specific LIRA

| Location | Quoted span (exact or bounded) | Score | Function | Reviewer diagnosis / decision |
| --- | --- | ---: | --- | --- |
| KO abstract | “SOLID는 소프트웨어 설계에 관해 생각하고 토론하는 데 유용한 원칙이다.” | 0.94 | respectful starting point | Keep; critique comes from evidence, not polemic |
| KO abstract | “'OCP를 위반한다'는 진단과 ... 반드시 거절해야 한다 ... 설명해야 할 거리가 있다.” | 0.99 | nucleus | **Protect.** Actual first-chat problem, condensed without new jargon |
| KO §1 | “원칙은 처음부터 조건을 필요로 했다.” | **0.61** | historical inference | Too broad about all principles/periods from one Martin example; narrow specifically to the cited original |
| KO §1 | “OCP 위반이므로 이 패치는 반드시 거절해야 한다.” | 0.98 | *author-constructed wording contrast* | Keep quotation attributed as an *invented* contrast, not a real transcript from a code review |
| KO §2 | “원칙(principle), 권고(guideline), 위반(violation), 필수(must), 공리(axiom)” | **0.84** | taxonomy | Good starting set, but "violation" is a *verdict* and "must" a *modality*, not members of one comparable grammatical class; mark separate speech acts |
| KO §2 | “어떤 프로젝트는 SOLID를 명시적으로 승인된 개발 정책으로 삼을 수 있으며” | 0.97 | strongest legitimate rival | Keep, prevents confusing valid policies with dogma |
| KO §2 | “이를 ... 운영상의 준공리화” | 0.86 | proposed label | Name evokes a mathematical claim. Preserve provisional status, never formal axiom proof |
| KO §3 | “두 연구 모두 우리의 출발점이지만...” | 0.91 | neighboring prior art | Careful, but other published/practitioner works already warn against design dogma; avoid claiming sole novelty |
| KO §3 | “설계 원칙이 조건부 조언에서 실제 수정 결정을 구속하는 말로 쓰이는 현상” | 0.93 | distinctive hypothesis | Keep, but cannot claim no one has tested analogous normativity |
| KO §4 | “SOLID의 다섯 이름은 서로 독립적인 최종 명령이 아니라...” | 0.91 | research vision | Correct as *question*; not a measured unification |
| KO §4 | “LSP의 행동적 치환 가능성처럼 단순한 변경 비용으로 환원하기 어려운 조건” | 0.97 | strong falsifier | Keep; blocks an oversimplified one-equation grand theory |
| KO ending | “우리는 원칙을 적용하고 있는가, 아니면 원칙의 이름에 판정권을 주고 있는가?” | 0.98 | distinctive ending | Keep. A concise memorable claim rather than an explanatory disclaimer |
| EN §1 | “The original advice needed conditions.” | **0.68** | historical inference | As with Korean, narrow to the Martin example; other OOP principles may not have identical scope vocabulary |
| EN §2 | “They do not necessarily form a historical sequence” | 0.96 | chronology restraint | Keep, crucial to avoid a fictitious evolution H→V→N→A |
| EN §3 | “Their 'label' is an attribution of instruction origin” | 0.99 | primary-source distinction | Critical source-backed discrimination from Laddha et al. |
| EN §4 | “a single elegant formula that erases such distinctions would be another dogma” | 0.96 | self-critique | Strong, human-readable line; keep |

## Three internal roles / same document, no bogus independent review
**Historian:** a source-specific claim is warranted for Martin's essay, but neither 30 years of unbroken transmission nor a trend of unconditional wording is established; direct new historical-corpus work needed. Revision should identify original authors by first name/context without falsely making "SOLID" a five-axiom 1996 authorial system.

**Linguist/pragmatics reviewer:** one list “principle/guideline/violation/must/axiom” places labels, judgment verbs, obligation modals and formal-status nouns side by side. That is deliberate because the study concerns changes in speech acts, but coding protocol must keep lexical vs pragmatic vs authority independent. Suggest **“어떤 말을 어떤 판단과 명령으로 바꾸는지”** rather than a bogus literal linear ladder.

**Skeptical SE referee:** Zhu et al. already isolate rule effects on code edits; Laddha et al. isolate instruction source labels. Practitioner [Software Engineering Guide](https://software-engineering-guide.github.io/en-us/topics/02-02-software-design-principles/) even explicitly warns about SOLID rules hardening into dogma. Thus *noticing that dogma can exist* is NOT an original discovery. The paper's still-unproven contribution proposal is a bounded, empirical inquiry into **SOLID-specific language, loss/retention of justification, and actual patch disposition**, with the candidate higher-order structure left in a separate research lane.

## Precise revisions authorized within v33 (not automatic v34)
1. `원칙은 처음부터 조건을 필요로 했다.` → `Martin이 논한 개방–폐쇄 원칙은 무엇을 바꿀지에 관한 조건부터 필요로 했다.`
2. `The original advice needed conditions.` → `In Martin's account, the advice came with conditions.`
3. If phrasing becomes cumbersome, keep the emphatic one-sentence hinge but replace only this overgeneralization; don't split and flatten the whole paragraph.
4. Maintain original historical paper/agent results as evidence labels; the two newly uploaded PDFs may change nearby novelty judgments, not prove ours.

## Experimental stop boundary
Do not pre-register a sprawling agent protocol inside the position paper. Publish this paper as an *idea invitation* after its author reviews the clean manuscript; keep historical archival sampling, inter-coder coding, controlled patch outcomes and higher-order theory in separately versioned memos.

**Disposition:** v33 core substantially closer to original founding intent; repair one English/Korean historical overstatement before treating it as a stable review candidate. External review and new causal effect still absent.
