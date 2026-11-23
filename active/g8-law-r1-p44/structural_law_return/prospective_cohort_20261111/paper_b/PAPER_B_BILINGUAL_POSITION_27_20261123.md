# Paper B v27 — When Do Design Principles Govern AI-Generated Patches? A Research Agenda on Operational Authority

**Bilingual historical-critical position paper · 2026-11-23 · WORKING DRAFT · NOT SUBMITTED.** Selective integration of *actually reopened* v01–v26, not a simple extension of v26. [Per-version inheritance ledger](58_PAPER_B_R16_V01_V26_CROSS_VERSION_SALVAGE_LEDGER.md) · [Five-pass adversarial/editorial decision record](59_PAPER_B_R17_FIVE_PASS_SIX_ROLE_ADVERSARIAL_INTEGRATION.md). Prior versions remain immutable. No new independent Go run, agent trial, energy metric or universal theorem is asserted.

# 한국어 원고

## 초록

설계 원칙을 이해하는 것과 그 원칙을 실제 소프트웨어 수정에 적용할 근거를 아는 것은 같은 능력일까? 개방–폐쇄 원칙이나 SOLID는 변경에 대처하는 방법을 설명하지만, 어떤 변화가 예상되는지와 기존 사용자에게 무엇을 보존해야 하는지는 프로그램마다 다르다. AI 코딩 에이전트가 이러한 조언을 읽고 코드 수정과 검토 판단까지 수행하는 상황에서, **조건부 설계 원칙이 적용 범위의 검토 없이 실질적인 승인·거절 규칙으로 사용되는가**라는 질문을 새롭게 연구할 필요가 있다. 우리는 이를 *운영상의 준공리화(operational quasi-axiomatization)*라는 반증 가능한 연구 대상으로 제안한다. Martin의 서로 다른 도형 변경 요구, SOLID 위반 분류에 관한 저장 자료, 요구와 기존 계약에 따라 같은 수정안의 판정이 달라지는 연구자 작성 사례로 이 질문의 경계를 설명한다. 이 자료는 에이전트의 준공리화 발생률이나 원인을 측정하지 않는다. 대신 역사적 지침의 조건성을 조사하고, 동일한 소스·요구·계약 아래 네 가지 설계 지시를 비교하며, 신뢰할 수 있는 반대 증거에 대한 패치 판단의 수정을 검증하는 후속 연구를 제안한다. 목적은 SOLID가 틀렸거나 더 우월한 설계 법칙을 발견했다고 선언하는 것이 아니라, **원칙의 이름이 실제 코드 결정에 행사하는 권위를 연구자들이 공동으로 측정할 수 있게 하는 것**이다.

## 1. 도형을 누가 정렬해야 하는가

Robert Martin이 1996년에 설명한 한 도형 프로그램은 객체가 자신의 그리기 동작을 제공하도록 하여 새 도형을 추가할 수 있게 했다. 그런데 새로운 요구가 등장한다. 모든 원을 사각형보다 먼저 그려야 한다. 목록의 순서대로 그리는 기존 함수는 새 도형의 추가에는 적합했지만 이 요구를 자동으로 만족하지 않았다. **원을 먼저 놓는 일이 함수의 책임인가, 호출자의 책임인가?** 기존 코드의 모습을 확인하는 것만으로 그 질문에 답할 수는 없다. 이때의 개방–폐쇄 원칙은 어떤 변경을 예상하고 어떤 동작을 보존할지 선택하도록 돕는 조언이지, 어떤 코드에도 문맥 없이 적용되는 합격 판정이 아니다. [Martin 1996](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf); [Paper B 01판 원문](https://app.notion.com/p/41bef561cf9281c2b45dee94b4744969).

오늘날 이 구별은 코드 리뷰뿐 아니라 AI 코딩 에이전트의 수정 과정에서도 중요하다. 원칙의 이름이 검토 설명에 등장하는 것과, 그 원칙을 이유로 특정 구현을 채택하거나 대안을 거절하는 것은 다르다. 실제 코드의 요구와 오래된 호출자 계약을 아는 개발자는 원칙이 유용한 경우를 찾아낼 수 있다. 반면 원칙을 기계적으로 적용하면 필요 없는 추상화를 만들거나 허용되는 수정안을 배제할 가능성도 있다. **우리는 그런 일이 널리 벌어지고 있다고 단정하지 않는다.** 어떤 조건에서 실제로 벌어지는지, 혹은 기존 지시 준수와 요구공학으로 충분히 설명되는지 묻는다.

이 글의 중심 제안은 설계 원칙의 *운영상의 권위(operational authority)*를 연구 대상으로 삼자는 것이다. 원칙이 사용됐는지, 패치를 바꾸었는지, 그 결과가 문서화된 계약에 적합했는지, 반대 증거에 따라 판단이 바뀌었는지를 구별한다. 이 질문이 AI 시대에 적절한 이유는 에이전트가 더 이상 설계 원칙을 서술하는 데 그치지 않고 실제 소스 코드에 적용할 수 있기 때문이다. 그러나 이 능력의 존재가 곧 부적절한 권위 행사에 관한 실증 결과인 것은 아니다.

## 2. 역사적으로도 닫힘에는 조건이 있었다

객체지향 프로그래밍의 발전이 하나의 SOLID 규칙집에서 출발한 것은 아니다. Simula의 모델링과 클래스, Smalltalk의 메시지, Parnas의 정보 은닉, Liskov와 Wing의 행동적 하위타입은 서로 다른 설계 문제를 다뤘다. 디자인 패턴에 관한 GoF의 고전적 작업과 SOLID 역시 서로 연관된 설계 지식을 제공하지만 동일한 개념이나 동일한 연대의 규범은 아니다. 역사를 하나의 원칙 체계로 환원하기보다, 당시의 저자들이 어떤 요구를 해결하려 했는지 살펴야 한다. [Black 2013](https://arxiv.org/abs/1303.0427); [Parnas 1972](https://doi.org/10.1145/361598.361623); [Liskov & Wing 1994](https://doi.org/10.1145/197320.197383).

Bertrand Meyer의 개방–폐쇄 설명에는 기존 클라이언트가 의존하는 안정된 설명과 새 종류를 수용할 확장 지점이라는 서로 다른 요구가 함께 등장한다. Martin은 1996년 논의에서 어떤 변화에 대비해 닫힘을 확보할지 선택하는 *strategic closure*를 강조한다. 도형의 종류가 늘어나는 요구와 그리기 순서가 바뀌는 요구가 다른 판단을 요구하는 이유다. 이 역사적 검토는 당시 저자들이 수학적으로 무조건적인 공리를 선포했다고 비판하는 근거가 아니라, 오히려 기존 원칙에도 적용할 조건이 포함돼 있음을 확인하게 해 준다. [Meyer 초판 본문 대조](./13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md).

그런데 실무와 도구에서 원칙이 인용될 때는 원칙을 정당화한 조건이 생략될 수도 있다. 이를 직접 검증할 수 있도록 우리는 **형식적 공리화**(명시적인 수학적 전제와 추론), **전문직적 정전화**(교육·실무에서 형성되는 역사적 권위), **운영상의 준공리화**(원칙의 이름이나 지침이 특정 수정 결정을 구속하는 행동)를 구별한다. 마지막 개념은 첫 두 현상의 자동적인 결과가 아니다. AI 모델의 내부 신념이나 특정 사전학습 자료를 추정하기 위한 이름도 아니다.

## 3. 한 수정안의 판정을 바꾸는 사실

소스의 구조적 특징을 보고 OCP 위반이라고 분류하는 것과, 실제 수정안의 승인 여부를 정하는 것은 요구하는 증거가 다르다. [Pehlivan 등(2025)](https://arxiv.org/abs/2509.03093)은 언어모델의 SOLID 위반 분류를 평가했다. 이 연구가 코드 수정의 승인에 필요한 프로젝트별 요구·보호 계약까지 실험했다고 해석해서는 안 된다. 우리가 보유한 OCP 저장 아카이브의 과거 독립 감사에는 **고유 제출 코드 48개, 저장 응답 768행, 서로 다른 마스킹된 프롬프트 틀 24개**가 기록되어 있다. 여기서 768은 독립적인 유지보수 요구의 개수가 아니며, 일부 코드 내부에는 설명 주석도 존재했다. [16판 원자료 감사](https://app.notion.com/p/41fef561cf9281be95b8cf89fad99c33).

이 둘의 차이를 명료하게 보여 주기 위해 이전 판본에서 작은 도서관 프로그램을 직접 구성했다. 후보 수정안은 기술보고서를 처리하지만 정오표는 지원하지 않고, 기존 책 출력의 접두어를 `book`에서 `BOOK`으로 바꾼다. 소스와 수정안을 고정하고, 실제로 요구하는 기능과 보호할 계약만 바꿔 다음과 같이 판정한다.

| 변경 요구 | 기존 책 접두어 보호 | 같은 수정안의 판정 |
| --- | --- | --- |
| 기술보고서만 지원 | 보호하지 않음 | **승인** |
| 기술보고서만 지원 | 보호함 | **거절** |
| 기술보고서와 정오표 지원 | 보호하지 않음 | **거절** |
| 기술보고서와 정오표 지원 | 보호함 | **거절** |

첫 행의 승인은 **연구자가 그 사례에 한정해 정한 요구·계약에 따른 승인**이다. 실제 사용자가 기존 접두어를 기대하지 않았다고 관찰한 결과가 아니다. 정오표 지원이 필수라면 접두어 보호 여부와 관계없이 거절할 수 있고, 기술보고서만 필요할 때 접두어 계약이 미공개라면 판정을 **보류**해야 한다. 보호받는 의무가 하나 더 밝혀지면 기존 승인도 바뀔 수 있다. [고정 패치 재현](./31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md); [17판 판정과 3×3 공개 표](https://app.notion.com/p/41fef561cf9281da9ed2c282695b2c63); [19판 추가 계약 민감도](https://app.notion.com/p/41fef561cf9281fabdf5d0548325beec).

이 사례는 요구공학과 Design by Contract가 오래전부터 다루어 온 문제를 보여 준다. 우리는 계약을 처음 발견하거나 이를 새로운 정리로 증명했다고 주장하지 않는다. 이 글에서 새로운 연구 대상으로 제안하는 것은 **기존 원칙을 인용하는 AI 에이전트가 이런 근거의 차이를 실제 수정 판단에 얼마나 반영하는지**다. 부적절한 전이가 보편적으로 발생한다고 가정하지 않고, 발생한다면 어떤 요구와 지시 환경에서 나타나는지 검증하려는 것이다.

## 4. '운영상의 준공리화'를 어떻게 구별할 것인가

원칙을 언급하는 문장은 위험 신호도 성공 지표도 아니다. 원칙이 실제로 어느 판단을 바꾸었는지 알아야 한다. 그 행동이 기존 계약을 어겼더라도 원인은 여러 가지일 수 있다. 에이전트가 코드를 잘못 읽었거나, 사용자 지시와 프로젝트의 원칙이 충돌했거나, 불완전한 테스트가 오류를 발견하지 못했을 수 있다.

특히 **강한 SOLID 지시를 따르는 것은 합당한 명시적 지시 준수일 수 있다.** 에이전트가 지시를 따른다는 사실만으로 독립적이고 무조건적인 SOLID 신념을 가졌다고 추론할 수 없다. 우리가 제안하는 후속 관찰에서는 원칙의 적용 근거가 불충분한데도 적법한 대안이 배제됐는지, 반대 근거의 출처와 우선순위는 확정돼 있는지, 추가 근거를 받은 뒤 에이전트가 결정을 수정하거나 정당하게 기권할 수 있는지를 각각 따져야 한다. [지시 준수와 권위의 식별 문제](./53_PAPER_B_R11_COMPLIANCE_VS_QUASI_AXIOM_IDENTIFICATION.md).

이것은 하나의 새로운 진리 판정 시스템을 곧바로 구현하자는 제안이 아니다. 구조적 위반 *분류*, 특정 패치의 *계약 적합성*, 검토자가 근거를 *제시할 수 있는지*, 반대 증거 뒤 *행동을 수정하는지*는 서로 다른 결과 변수다. 모두 동일한 기준으로 점수를 매겨 하나의 SOLID 준수율로 합칠 이유도 없다. 기존의 소스 인지 요구사항 추적이 판단을 충분히 설명한다면, 더 고유한 '준공리화 기제'가 있다는 주장은 철회하거나 좁혀야 한다.

## 5. 공동 연구를 위한 세 가지 실행 가능한 시작점

**역사·문헌 연구:** SOLID를 설명하는 원전, 시대별 교육 자료, 저장소 지침에서 원칙이 어떤 조건과 예외와 함께 제시되는지 확인한다. 표본 추출 시기와 문서 유형을 고정하고, 단순한 강제 표현의 증가가 과연 적용 범위의 삭제를 동반하는지 조사할 수 있다. 아무런 변화가 없거나 문서 유형만 다르다는 결과도 가능하다. 문헌의 변화만으로 AI가 그 변화를 일으켰다고 추론해서는 안 된다.

**실제 패치에 대한 지시 효과:** 소스 버전, 요구, 오래된 호출자 계약, 허용된 수정 범위, 기능 검사를 고정하고, 이전에 제안된 네 가지 지시 조건 **NONE / HARD_SOLID / SCOPED_SOLID / EVIDENCE_CONDITIONAL**을 새 에이전트 문맥에 배정할 수 있다. 원칙에 적합한 설계가 실제로 도움이 되는 과제와 기계적 적용이 불리한 과제를 모두 포함해야 한다. 결과는 코드의 정확성·보존 계약·수정 범위와 설명 어휘를 구분한다. 네 조건 모두 같은 적법한 패치를 만들거나 HARD_SOLID가 더 좋은 수정을 만든다면 그대로 보고한다. 이 비교의 인과 대상은 **주어진 지시 내용의 효과**이지 모델이 사전학습 중 어떤 철학을 받아들였는지가 아니다. [2026-10-09 P35-B1 사전 설계](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md).

**반대 증거에 대한 결정 수정:** 명세와 기존 클라이언트 테스트를 독립적으로 검증한 뒤, 같은 사실을 서로 다른 지시 조건의 에이전트에 제공해 수정·유지·기권·지시 충돌 보고를 구분한다. 원칙을 고수한 이유가 문서화된 상위 지시인지, 부정확한 요구 해석인지, 실제로 근거 없는 권위 부여인지 별도 판정한다. 전통적인 요구사항 추적 검토자와 같은 정보를 제공한 대조군이 동등하게 설명한다면 새로운 기제의 증거는 약해진다.

세 연구는 같은 질문을 다른 방법으로 공격하며, 어느 하나가 먼저 성공해야 다른 연구자가 착수할 수 있는 것은 아니다. 더 장기적으로는 SOLID형 구조와 함수·콜백 기반 설계의 실제 유지보수 요구, 수정 토큰·리뷰 노동·회귀 오류·에너지 등을 비교할 수도 있다. 다만 그러한 **비용 절감 효과나 보편적인 상위 설계 법칙은 현재 논문에서 측정하거나 발견한 결과가 아니다.**

## 6. 어떤 결과라면 가설을 좁혀야 하는가

다음 결과들은 제안의 강한 해석에 반대한다. 첫째, 명확한 요구와 계약 아래 모든 에이전트가 원칙의 문구와 무관하게 동일한 적법한 패치를 만든다. 둘째, 강한 SOLID 지시가 설명의 단어만 바꾸고 소스 코드는 바꾸지 않는다. 셋째, 강한 원칙이 특정 과제에서 정확성이나 계약 보존을 개선한다. 넷째, 관찰된 충돌과 실패가 원칙의 특별한 권위 때문이 아니라 정상적인 지시 우선순위, 불완전한 소스 정보 또는 기존 요구사항 추적으로 모두 설명된다. 이런 결과라면 '운영상의 준공리화'가 널리 발생하는 독립적인 현상이라는 주장을 강화해서는 안 된다.

우리의 문제 제기는 어떤 결론이 나와도 자동으로 맞는 것으로 정의된 이론이 아니다. 오히려 **어떤 증거가 나오면 이 가설을 버려야 하는지 명시한 연구 질문**이 되어야 한다. 현재 확인한 작은 반례와 분류 자료는 이 질문을 제기할 근거이지, 그 답은 아니다.

## 7. 결론

소프트웨어 설계 원칙은 변화를 설명하는 언어를 제공했다. AI 코딩 에이전트가 그 언어를 실제 수정 결정으로 옮길 수 있는 지금, 우리는 원칙이 *무엇을 설명하는가*뿐 아니라 *어떤 권위로 특정 패치를 결정하는가*를 따로 연구할 필요가 있다고 제안한다. 이를 **운영상의 준공리화**라는 반증 가능한 연구 문제로 부르되, 현상의 보편성이나 역사적 원인, 새로운 설계 법칙의 발견은 주장하지 않는다. 역사 연구자, 요구공학·프로그램 언어 연구자, AI 에이전트 실험 연구자가 각자의 방법으로 이 차이를 조사할 수 있다. 그 답이 기존 원칙을 강화하든 그 적용 범위를 좁히든, 더 신뢰할 수 있는 설계 조언을 만드는 데 도움이 될 것이다.

---

# English manuscript

## Abstract

Does knowing a design principle entail knowing when that principle should govern an actual software change? The Open–Closed Principle and related SOLID guidance describe how software might accommodate change, but the relevant changes and protected clients depend on the project. As AI coding agents move from describing designs to producing and judging patches, **we propose asking whether conditional guidance sometimes acquires decision authority without an adequate account of its scope**. We call this falsifiable research target *operational quasi-axiomatization*. Martin's contrasting shape-change requirements, an archive used to classify SOLID violations, and an author-constructed fixed-patch example clarify the distinction between naming a structural concern and justifying a concrete disposition. None establishes the prevalence or origin of such agent behavior. We propose three research entry points: tracing the scope of design advice in historical and developer-facing texts, testing instruction effects on actual patches under matched contracts, and measuring evidence-responsive revision after authenticated counterexamples. The objective is not to disprove SOLID or announce a superior mathematical design law but to invite a source-grounded investigation of **the authority principle language exercises over software modifications**.

## 1. Who must sort the shapes?

In Robert Martin's 1996 discussion, a drawing routine can accommodate another kind of shape when objects provide their own drawing operations. A new requirement changes the problem: every circle must be drawn before every square. A routine that draws shapes in the order received does not satisfy that requirement by itself. **Must the routine do the sorting, or must callers pass a sorted sequence?** Inspection of the loop alone cannot establish which party owns the responsibility. A principle that helps anticipate one kind of change does not automatically decide a different requirement. [Martin 1996](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf); [earliest bilingual manuscript](https://app.notion.com/p/41bef561cf9281c2b45dee94b4744969).

The same distinction matters when a coding agent is asked to extend a mature application. Citing OCP in an explanation is not identical to accepting one patch, generating a particular abstraction, or rejecting an otherwise feasible alternative because of that principle. Those acts may be justified by project requirements and policies. They might also omit relevant obligations. We do **not** presume widespread agent misuse. We propose finding out when any such divergence can be observed and when conventional instruction following or source-aware requirements reasoning already explains the decisions.

The object of study is a design principle's **operational authority**. Did it affect the patch, did the resulting patch satisfy protected clients, could the agent support its disposition with source evidence, and did a credible counterexample lead to revision or justified abstention? The ability to act on principle language makes these questions relevant to AI-assisted engineering; it does not answer them.

## 2. The original advice was conditional

The history of object orientation was not the development of one immutable SOLID rulebook. Simula's modeling and classes, Smalltalk's messaging, Parnas's information hiding, and Liskov and Wing's behavioral subtyping addressed distinct problems. The GoF design-pattern catalog and the later SOLID mnemonic also have different histories, although their design concerns may overlap. Their original problem settings deserve examination rather than being subsumed under a timeless slogan. [Black 2013](https://arxiv.org/abs/1303.0427); [Parnas 1972](https://doi.org/10.1145/361598.361623); [Liskov and Wing 1994](https://doi.org/10.1145/197320.197383).

Meyer's account combines extensibility with stable descriptions on which existing clients rely. Martin makes the strategic choice of changes against which a module should be closed explicit. Adding a shape and reordering existing kinds of shapes are different demands. That history provides evidence of **conditional guidance**, not grounds to accuse the original authors of having asserted five universal mathematical axioms. [Meyer first-edition passage audit](./13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md); [Martin 1996](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf).

But conditions can be lost when guidance travels through textbooks, review rubrics, repository instructions, and agent prompts. We distinguish **formal axiomatization**, the legitimate specification of premises and inference rules; **professional canonization**, historical authority gained through repeated use; and **operational quasi-axiomatization**, our hypothesized behavior in which a principle acquires decisive force over a particular software change without adequate scope or evidentiary support. The third is not automatically caused by the first two and provides no direct access to a model's hidden beliefs or pretraining contents.

## 3. A patch changes its verdict without changing its code

A structural classification and a patch disposition require different evidence. [Pehlivan et al.'s *Are We SOLID Yet?* (2025)](https://arxiv.org/abs/2509.03093) evaluates LLM-based SOLID-violation detection. It should not be described as an experiment establishing which specific maintenance patches deserve rejection. Our earlier independent inspection of its archived OCP subset distinguished **48 unique submitted code examples, 768 stored response rows and 24 masked prompt scaffolds**. The 768 rows were not independent real maintenance tasks, and code-internal comments were present in some samples. [Source and unit audit, v16](https://app.notion.com/p/41fef561cf9281be95b8cf89fad99c33).

To make the gap tangible, we previously constructed a small library-patch example. The *same candidate* adds technical-report support but does not add errata support and changes the prefix of an existing book output from `book` to `BOOK`. Holding the candidate fixed while varying the stipulated task and protected client obligation yields:

| Required extension | Old book prefix protected? | Fixed-patch disposition |
| --- | --- | --- |
| Technical reports only | No | **Accept** |
| Technical reports only | Yes | **Reject** |
| Technical reports and errata | No | **Reject** |
| Technical reports and errata | Yes | **Reject** |

Acceptance in the first row is **conditional on this investigator-defined contract**, not proof that an actual client did not depend on the prefix. If protection of the book prefix is not disclosed, the report-only case is **Defer**. An additional independent protected obligation may invalidate an earlier acceptance. [Executable fixed-patch case](./31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md); [v17 disclosure grid](https://app.notion.com/p/41fef561cf9281da9ed2c282695b2c63); [v19 additional-obligation sensitivity](https://app.notion.com/p/41fef561cf9281fabdf5d0548325beec).

Requirements engineering and Design by Contract already provide classical ways to express this distinction. Our contribution is not the invention of those premises or a new proof about all programs. We propose investigating **whether coding agents that invoke named design principles actually consult the relevant requirements and contracts when choosing, defending and revising a patch**.

## 4. Identifying operational authority without reading minds

Mentioning a principle is neither a failure nor a success indicator. We need to observe whether principle language affects a disposition. Even an unacceptable patch can have several explanations: incorrect code comprehension, conflicting instructions, missing test coverage, or an unjustified refusal to consider authorized alternatives.

**Following an explicit HARD_SOLID instruction may be legitimate policy compliance.** It is not evidence that an agent independently believes SOLID to be an infallible axiom. Proposed future observations must therefore establish the authority of the source-backed requirement and contrary evidence, distinguish permissible from mandatory choices, and examine whether an agent can revise or appropriately abstain when an admissible alternative is demonstrated. [Identification critique](./53_PAPER_B_R11_COMPLIANCE_VS_QUASI_AXIOM_IDENTIFICATION.md).

Structural *classification*, contractual *patch correctness*, the *provenance of reasons*, and *revision after rebuttal* are different outcomes. They should not be collapsed into a single SOLID-adherence score. If existing requirements-traceability methods with equal source information fully explain the observed behavior, there may be no new causal mechanism to identify. The term operational quasi-axiomatization is a proposal for an observable research target, not a diagnosis of the agent's mental state.

## 5. Three independent ways to join the inquiry

**Historical and documentary analysis.** Compare primary SOLID discussions, educational documents and repository instructions to assess how explicitly scope and exceptions accompany principles. Freeze sampling periods and document genres. A null result or a difference explained by document type is as valid as a finding of context-stripping. A temporal change in wording does not establish that AI caused the change.

**Instruction effects on actual patches.** Hold source commit, requirement, protected old clients, edit rights, test environment and tool budget constant, then compare fresh agent invocations assigned to the inherited four advice conditions: **NONE, HARD_SOLID, SCOPED_SOLID, EVIDENCE_CONDITIONAL**. Include tasks where a principle-conforming structure helps and tasks where mechanical application would be disadvantageous. Separate code and client-contract correctness from explanations. If all arms produce the same acceptable patch or strict guidance performs better, preserve that outcome. A randomized comparison may identify **effects of the injected advice**, not a causal mechanism in opaque pretraining. [Original October 2026 pre-agent protocol](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md).

**Revision under authenticated counterevidence.** Establish protected caller tests and task specifications independently before providing the same credible fact to different agent conditions. Distinguish justified revision, continued adherence, abstention and explicit instruction-conflict reports. Source and instruction hierarchy must be considered before inferring that a refusal was unjustified. If an ordinary source-aware requirements reviewer given the same information explains the outcome equally well, the claim of a distinctive principle-authority effect must be weakened.

These studies can start separately. Historians need not first build a Go benchmark, and experimentalists need not establish a new mathematical software law. Future work could also compare architectures under sequences of actual changes, measuring initial abstraction cost, agent tokens, reviewer effort, regressions and energy separately. **No reduction in such costs has been demonstrated by the present paper.**

## 6. Findings that should narrow the claim

Several outcomes would count against a strong quasi-axiomatization account. Given clear tasks and contracts, agents may produce equally valid patches regardless of principle wording. Strict guidance may change only explanatory vocabulary. It may improve contract preservation on a class of tasks. Apparent errors may be fully accounted for by valid instruction precedence, missing source evidence or ordinary requirements reasoning rather than a special design-principle effect. Such cases would not license a stronger claim by renaming all behavior quasi-axiomatization.

The position is therefore an invitation to a **falsifiable question**, not a theory defined to succeed regardless of observation. Existing constructed witnesses and classification records motivate that question but cannot answer it.

## 7. Conclusion

Software design principles provide a language for engineering change. Agents that can translate this language into executable patches make it worthwhile to study not only what a principle says but also **what authority it has over a particular modification**. We propose operational quasi-axiomatization as a falsifiable research object without presuming its prevalence, its historical causes, or the discovery of a superior design law. Historians, requirements and programming-language researchers, and coding-agent experimentalists can study its distinct aspects with their own evidence. A result that strengthens familiar principles or limits their scope would both help make engineering advice more accountable.

---

## Author-only provenance and editorial checks (not part of submission manuscript)

- This v27 manuscript deliberately restores: v01/v08 Martin responsibility opening; v09/v17 3×3 uncertainty in abbreviated form; v16 archive units and code-comment caveat; v19 additional protected-obligation sensitivity; v22/23 historical AI quasi-axiomatization core and original P35-B1 design; v25 legitimate instruction-compliance objection; v26 reader invitation and negatives.
- v02/v10/v12 code placement / pre-existing hooks, v20/#995/#1035 source-correction disputes, Go interface vs callback comparison, token/energy calculations, formal LAW-R2 and 70k-character v22 archive remain linked support or separate future studies, **not silently refuted or overwritten**.
- No real four-arm coding-agent executions in this turn or earlier verified materials. No new native-Go rerun. Prior source audit and executable witness are **inherited historical results**, not replicated today.
- Cross-version sources: [R16](58_PAPER_B_R16_V01_V26_CROSS_VERSION_SALVAGE_LEDGER.md). Multi-perspective review: [R17](59_PAPER_B_R17_FIVE_PASS_SIX_ROLE_ADVERSARIAL_INTEGRATION.md). New research novelty has **not** been established against every relevant current publication.
- Subsequent submission work needs accurate venue-dependent references, fact/source citation mapping, bilingual proofread, independent external review and a clean export. No fake peer-review claim and no automatic submission.
