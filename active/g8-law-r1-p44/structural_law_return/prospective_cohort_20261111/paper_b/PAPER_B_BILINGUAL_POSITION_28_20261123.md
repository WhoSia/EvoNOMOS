# 원칙은 언제 판정이 되는가? — AI 코딩 에이전트와 설계 조언의 권한

*When Does a Design Principle Become a Verdict? Operational Authority in AI Coding*

**Position paper · concise bilingual author-review manuscript · v28 / 2026-11-23 · NOT SUBMITTED**

이 논문은 기발한 수학적 법칙의 발견이나 에이전트 효과의 관측을 주장하지 않는다. 설계 조언이 코드 결정에서 갖는 권위를 검증하자고 제안한다. 기존 01–27판은 모두 보존한다.

# 한국어 원고

## 초록

설계 원칙을 아는 것과 그 원칙으로 특정 코드 수정을 결정할 자격을 갖추는 것은 같은 능력일까? 개방–폐쇄 원칙을 비롯한 SOLID 원칙은 소프트웨어의 변화를 다룰 유용한 언어지만, 어떤 변화를 예상하고 누구의 동작을 지켜야 하는지는 프로젝트마다 다르다. AI 코딩 에이전트가 설계 조언을 코드 수정과 검토 결정으로 옮기는 지금, 우리는 그 조언이 언제 근거를 넘어서는 권위를 갖는지 묻는다. 이 가능성을 ‘운영상의 준공리화’라고 부르되, 원칙을 따르는 행위와 잘못된 절대화를 미리 동일시하지 않는다. 우리는 역사적 원문과 동일 패치의 조건부 판정을 출발점으로 삼고, 실제 에이전트의 패치 선택과 반대 증거 이후의 수정을 시험할 연구 의제를 제안한다. 이 논문은 새로운 보편 설계 법칙이나 이미 관찰된 에이전트 효과를 발표하지 않는다.

## 1. 도형보다 먼저 정해야 할 것

1996년 Robert Martin은 새 도형을 쉽게 추가할 수 있는 설계에 다른 요구를 붙였다. 이번에는 원을 사각형보다 먼저 그려야 한다. 도형을 하나 더 만드는 일에 유리했던 구조가 순서를 바꾸는 일까지 저절로 해결하지는 않는다. 누가 정렬할 책임을 지는가—도형을 그리는 함수인가, 그 함수를 부르는 쪽인가? 개방–폐쇄 원칙이라는 이름만으로는 그 책임을 배분할 수 없다. AI가 ‘OCP 위반’이라는 라벨을 붙이는 일과, 그 라벨을 근거로 특정 패치를 거절하는 일도 그만큼 다르다.

## 2. 조건부 조언이 판정 규칙이 될 때

Meyer의 초기 개방–폐쇄 논의와 Martin의 ‘전략적 닫힘’에는 기존 사용자를 위한 안정성과 예상하는 변화의 종류가 함께 들어 있다. 원래부터 적용 조건이 있었던 원칙이 오늘날 모든 수정의 합격 기준으로 통용되는지는 별도로 확인해야 한다. 우리는 설계 원칙이 코드에 대한 설명을 넘어 실제 수정의 승인·거절에 행사하는 힘을 ‘운영상의 권위’라고 부른다. 그 권위가 요구사항과 보호할 계약의 근거를 부당하게 밀어내는 현상이 있다면, 이를 ‘운영상의 준공리화’라는 가설로 조사할 수 있다. 이는 수학의 공리화를 비판하는 주장도, 모델이 속으로 SOLID를 믿는다고 단정하는 주장도 아니다.

## 3. 코드가 그대로인데 판정은 바뀌는 경우

우리가 구성한 도서관 프로그램에서 하나의 패치는 기술보고서를 지원하지만 정오표를 지원하지 않고, 기존 책 출력의 접두어를 `book`에서 `BOOK`으로 바꾼다. 새 요구가 기술보고서 지원뿐이고 책 접두어가 보호할 계약 밖이라면, 그 패치는 이 사례의 조건에서 승인할 수 있다. 같은 접두어가 계약으로 보호된다면 소스를 한 줄도 더 바꾸지 않아도 판정은 거절로 뒤집힌다. 정오표까지 지원해야 한다면 기존 책 접두어의 보호 여부와 무관하게 거절해야 한다. 반대로 기술보고서만 요구된 상태에서 접두어 계약이 공개되지 않았다면, 정확한 판정은 보류다. 이 작은 구성 사례는 특정 에이전트가 교조적으로 행동했다는 실험 결과가 아니다.

## 4. 언어모델에게 정말 시험할 것

SOLID 위반을 찾는 분류 연구는 출발점이지 특정 수정안을 승인할 근거까지 검증하는 연구와 같지 않다. AI가 원칙을 자주 언급하는지보다, 그 원칙 때문에 어느 소스를 바꾸고 어떤 대안을 버리는지를 관찰해야 한다. 후속 실험에서는 같은 코드·요구·계약·도구 예산 아래 네 조건—지시 없음, 강한 SOLID, 범위가 명시된 SOLID, 요구와 증거 중심 지시—을 비교할 수 있다. 원칙에 맞는 구조가 도움이 되는 과제와 기계적 적용이 기존 계약을 해칠 수 있는 과제를 함께 넣어야 한다. 그러나 강한 SOLID 지시를 따른 것만으로 준공리화가 입증되는 것은 아니다. 원칙과 충돌하는 신뢰할 만한 근거가 실제로 전달됐는지, 그 근거가 어떤 지시보다 우선하는지, 이후 패치 판단이 바뀌었는지를 따져야 한다. 이 네 조건에 대한 실제 독립 에이전트 실행 결과는 아직 없다.

## 5. 이 아이디어를 어떻게 반박할까

원칙을 강조한 지시가 실제 패치가 아니라 설명의 어휘만 바꾼다면, 설계 결정에 특별한 권위를 행사했다는 증거는 약하다. 강한 원칙 지시가 기존 계약의 보존을 오히려 개선한다면, 그 이익 역시 결과로 받아들여야 한다. 일반적인 요구사항 추적만으로 모든 판단을 설명할 수 있다면, 새 이름보다 기존 이론이 더 나은 설명일 수 있다. 실험 결과가 전부 같거나 불확실해도, 그것을 억지로 준공리화의 다른 형태라고 부르지는 말아야 한다.

## 6. 함께 시험해 볼 질문

역사 연구자는 원칙이 설명될 때 적용 범위와 예외가 언제 생략되는지 문헌을 비교할 수 있다. 소프트웨어 공학 연구자는 같은 수정 요구와 계약을 둔 채 에이전트의 실제 패치 선택을 비교할 수 있다. 프로그램 언어·요구공학 연구자는 반대 증거와 지시 우선순위가 합당한 수정 판단으로 이어지는지 독립적으로 판정할 수 있다. 나중에 토큰·유지보수 비용·에너지까지 비교할 수는 있지만, 파일 수정 수가 줄었다는 사실만으로 그런 절감이 증명되지는 않는다. 코드가 원칙을 어겼는지를 묻기 전에, 그 원칙이 지금 이 코드를 바꿀 근거가 되는지부터 묻자.

---

# English manuscript

## Abstract

Knowing a design principle is not the same as knowing when it should decide a particular software change. SOLID, including the Open–Closed Principle, offers a useful language for change, but the expected changes and protected clients are project-specific. As AI coding agents translate design advice into actual patches and reviews, we ask when that advice gains authority beyond the evidence supporting its application. We call this possibility operational quasi-axiomatization without equating ordinary adherence with an unjustified override. Historical sources and a fixed-patch counterexample motivate a research agenda on patch choice and revision after credible contrary evidence. We claim neither a universal replacement for SOLID nor an already observed agent effect.

## 1. Before the shape comes the responsibility

In 1996, Robert Martin considered a drawing design that could accept new kinds of shapes. Then the requirement changed: circles had to be drawn before squares. A structure convenient for adding a shape does not automatically satisfy a request to change drawing order. Who must establish the order—the drawing routine or its callers? The label Open–Closed Principle cannot assign that responsibility on its own. Likewise, detecting an OCP violation is not the same act as rejecting a concrete patch because of it.

## 2. When advice acquires the force of a verdict

Meyer's original open–closed account and Martin's strategic closure both involve stable client obligations and anticipated kinds of change. Whether later practice treats such guidance as a universal acceptance rule is a separate empirical question. By operational authority we mean the force principle language actually exercises over approval, rejection, and construction of a patch. Where that authority unjustifiably displaces task requirements or protected clients, we propose investigating operational quasi-axiomatization. The proposal neither attacks mathematical axiomatization nor purports to read a model's internal beliefs.

## 3. A fixed patch, different verdicts

In a library example we constructed, one fixed patch handles technical reports but not errata and changes an old book prefix from `book` to `BOOK`. If reports are required and that prefix lies outside the protected contract, the patch is admissible under the stipulated case. If the prefix is protected, the very same patch must be rejected. If errata are also required, it must be rejected regardless of the book-prefix obligation. If only reports are required but prefix protection is unknown, the warranted disposition is to defer. These are verdicts under an author-constructed contract, not measurements of actual agent dogmatism.

## 4. What an agent experiment should actually test

Studies that classify SOLID violations do not, by that fact alone, evaluate whether a particular patch should be accepted. We should measure which source files an agent changes and which alternatives it rejects, not simply how often it utters a principle's name. One prospective study would compare four advice conditions—NONE, HARD_SOLID, SCOPED_SOLID, and EVIDENCE_CONDITIONAL—on identical sources, demands, protected clients, and tool budgets. The task set should include cases in which strict guidance helps and cases in which mechanical application threatens a protected contract. Following an explicit HARD_SOLID instruction is not, by itself, evidence of quasi-axiomatization. Investigators must establish the provenance and authority of contrary evidence and observe whether the agent appropriately revises, abstains, or reports an instruction conflict. No independent four-arm coding-agent trial has yet been completed.

## 5. How the idea might fail

If strict advice changes only explanatory vocabulary, there is little evidence that it acquired special authority over the patch. If it improves preservation of old clients, that benefit must be reported rather than explained away. If ordinary requirements traceability explains the decisions equally well, established theory may be the better account. Null or inconclusive results must not be renamed as further forms of quasi-axiomatization.

## 6. An invitation, not a manifesto

Historians can examine when explanations of design principles lose their stated scopes and exceptions. Software-engineering researchers can compare agents' actual patches while holding requirements and protected clients constant. Programming-language and requirements researchers can independently adjudicate counterevidence, instruction priority, and justified revision. Longitudinal token, maintenance, and energy costs are possible extensions, but fewer edited files do not establish any such savings. Before asking whether code violates a principle, ask whether that principle warrants changing this code.

---

## Source and scope notes
- Historical source: [Robert C. Martin, *The Open-Closed Principle* (1996)](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf); [Meyer 1988 first-edition passage recovery](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md). **The Meyer source in the project was recovered from surviving pages of a partial PDF, not a complete edition.**
- Related work: [Pehlivan et al., *Are We SOLID Yet?*, ASE 2025](https://consensus.app/papers/pehlivan-erg%C3%BCzen-are-we-solid-yet-an-empirical-study-on-prompting/w:b1674eb8-5f53-41da-afe8-01c8467a0da7/), specifically SOLID violation detection and prompting, not contract-grounded patch acceptance; [Parnas (1972)](https://doi.org/10.1145/361598.361623) and [Liskov & Wing (1994)](https://doi.org/10.1145/197320.197383) supply established prior reasoning about modularity and behavioral obligations.
- Constructed example: [same fixed patch under varied demands and contracts](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md), with [original v17 3×3 disclosure table](https://app.notion.com/p/41fef561cf9281da9ed2c282695b2c63) and [v19 additional-obligation sensitivity](https://app.notion.com/p/41fef561cf9281fabdf5d0548325beec).
- Pre-registered next comparison: [P35-B1 four-arm prompt study](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md), not yet executed with independent coding agents.
- Full editorial lineage: [R19A, v01–v07](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/61_PAPER_B_R19A_SENTENCE_LINEAGE_V01_V07.md); [R19B, v07–v14](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/62_PAPER_B_R19B_SENTENCE_LINEAGE_V07_V14.md); [R19C, v14–v21](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/63_PAPER_B_R19C_SENTENCE_LINEAGE_V14_V21.md); [R19D, v21–v27](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/64_PAPER_B_R19D_SENTENCE_LINEAGE_V21_V27.md).
- No new original-Go execution, no four-arm agent observations, no universal theorem, no measured token/energy saving, and no external human review for this redraft. Publication-ready reference checking remains open.