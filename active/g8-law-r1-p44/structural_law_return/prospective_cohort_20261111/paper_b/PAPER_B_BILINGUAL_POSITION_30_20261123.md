# 누가 설계 원칙에 명령할 권한을 주었는가? — AI 시대의 SOLID, 조건부 조언, 그리고 철회 가능한 판단

*Who Gave Design Principles the Authority to Command? SOLID, Conditional Advice, and Revisable Decisions in the Age of AI*

**Paper B v30 · Position paper / research programme · 2026-11-23 · author review draft, NOT SUBMITTED**

# 한국어 원고

## 초록

소프트웨어 설계 원칙은 언제 조언을 넘어 판단을 구속하는 규칙이 되는가? SOLID는 소프트웨어의 변화를 다루는 강력한 언어이지만, 어떤 변화가 예상되고 무엇을 보존해야 하는지는 그 이름만으로 정해지지 않는다. 우리는 객체지향 설계의 역사, 요구공학의 계약 논리, AI 코딩 에이전트의 실행 가능한 지침을 연결해, 설계 조언의 권위가 어떻게 형성되고 언제 수정되어야 하는지 묻는다. 이를 ‘운영상의 준공리화’라는 연구 의제로 제안하되, 누군가 SOLID를 정식 공리로 선포했다거나 AI가 이미 이를 무조건적으로 따른다고 주장하지는 않는다. 고전적 원전과 동일 수정안의 조건부 판정은 출발점이며, 실제 에이전트가 원칙을 적용·유보·철회하는지는 아직 검증해야 할 질문이다.

## 1. 원칙은 판단을 대신하지 않는다

Martin이 1996년에 제시한 도형 프로그램은 새 도형의 추가에는 열려 있었지만, 원을 사각형보다 먼저 그리라는 요구 앞에서는 다시 설계 판단을 필요로 했다. 누가 순서를 보장해야 하는가—그리는 함수인가, 호출자인가, 별도 정렬 정책인가? 원칙의 이름은 그 답을 대신할 수 없다. 정확히 여기서 Paper B의 질문이 시작된다: 설계 원칙을 아는 기계가 그 원칙을 적용할 자격까지 아는가?

## 2. 역사에 이미 있던 조건을 다시 찾다

1972년 Parnas의 모듈 경계 논의와 1979년 프로그램 계열 연구는 변화할 가능성이 큰 결정을 어떻게 격리할지 고민했다. Meyer는 확장성과 기존 이용자가 의존하는 안정된 설명을 함께 다뤘고, Martin은 모든 변화에 닫힌 프로그램은 불가능하므로 ‘전략적 닫힘’을 선택해야 한다고 설명했다. Martin은 공개 멤버 변수의 좋지 않은 스타일과 잘못된 설계를 구별했고, RTTI가 OCP를 해치지 않는 예외도 논의했다. 이것은 SOLID의 창시자들을 교조주의자로 고발하는 이야기가 아니다. 그보다는 조건과 예외를 포함한 조언이 교육, 코드 리뷰, 에이전트 지침을 거치며 어떤 권위를 얻는지 묻는 역사·인식론적 탐구의 출발점이다.

## 3. 권위의 획득에서 철회까지

우리가 연구하려는 대상은 설계 원칙 자체의 참·거짓보다, 원칙이 특정 코드 수정에 미치는 운영상의 권위다. 그 과정에는 적어도 네 순간이 있다: 원칙을 가르치는 순간, 지침으로 고정하는 순간, 실제 패치를 승인·거절하는 순간, 반대 증거를 받고 결정을 고치는 순간이다. 우리는 마지막 순간까지 포함해 원칙의 적용 권한을 잠정적이고 철회 가능한 것으로 다루자고 제안한다. 이 구조를 ‘운영상의 준공리화’라고 부르는 까닭은 원칙의 형식적 공리화를 비난하려는 것이 아니라, 조건부 조언이 실제 결정에서 충분한 근거 없이 명령의 힘을 갖는지를 시험하기 위해서다.

## 4. 같은 코드에 다른 판정이 내려지는 이유

우리가 만든 도서관 예제에서는 기술보고서를 추가하되 정오표를 지원하지 않고, 기존 책 출력의 접두어까지 바꾸는 수정안을 고정했다. 기술보고서만 필요하고 접두어 보존 의무가 없다면 허용되지만, 접두어를 보존해야 하거나 정오표까지 필요하다면 같은 수정안도 거절된다. 보호할 계약이 아직 알려지지 않았다면 즉시 승인이나 거절 대신 판단을 보류해야 할 수도 있다. 이는 요구공학의 오래된 구별이지, 우리가 발견한 새 수학 법칙은 아니다. 그렇다면 AI가 ‘OCP 위반’이라고 분류한 결과를 실제 패치의 거절 근거로 옮길 때, 요구와 기존 계약의 증거를 어디까지 반영하는가?

## 5. 오래된 연구를 새 질문으로 연결하기

선행연구는 이미 SOLID 위반 분류, 에이전트 지침의 효과, 오래된 규칙과 코드의 충돌, 코드 리뷰의 과잉 수정을 다루었다. 따라서 우리가 ‘AI가 규칙을 따르기도 한다’는 사실을 처음 발견한 것은 아니다. 여기서 제안하는 연결은 원칙의 역사적 조건, 현재의 지시 권한, 실제 패치의 계약 적합성, 이후 판단 철회를 하나의 연구 대상으로 묶는 것이다. 예컨대 원칙 이름이 붙은 조언과 내용이 같은 익명 조언을 비교하면, 그 이름의 영향이 있는지 탐색할 수 있다. 그러나 명칭 효과는 프레이밍이나 지시 우선순위의 일반적인 효과일 수 있으므로, 한 실험에서 차이가 나더라도 그것을 독립된 새 심리 기제로 선언할 수는 없다.

## 6. 새로운 법칙을 선포하는 대신 연구를 열다

이 문제에는 역사학자가 다룰 문헌의 변화, 요구공학자가 판정할 계약의 정당성, AI 연구자가 실험할 실제 수정 행동이 함께 있다. 원칙의 이름이 판단을 바꾸지 않거나, 강한 SOLID 지시가 실제로 기존 계약을 더 잘 보존한다면 그 결과를 그대로 받아들여야 한다. 더 긴 시간에서는 이런 결과를 토대로 SOLID가 언제 유용하고 어떤 경우 다른 구조가 나은지 설명하는 상위 이론을 찾을 수도 있다. 그러나 지금 이 글의 성과는 상위 법칙의 발견이 아니라, 관습처럼 사용되는 설계 원칙의 권위를 과학적 질문으로 바꾸자는 제안에 있다. 좋은 원칙일수록 더 중요한 질문이 남는다: 그것이 바로 이 코드를 바꾸라고 말할 권한은 어디서 오는가?

---

# English manuscript

## Abstract

When does software design advice become a rule that governs a decision? SOLID offers a powerful language for change, but its name alone does not establish which changes to anticipate or which clients to protect. We bring the history of object-oriented design, contractual reasoning in requirements engineering, and executable instructions for AI coding agents into one question: how does design advice acquire authority, and when should that authority be revised? We propose operational quasi-axiomatization as an agenda, not as a claim that anyone formally axiomatized SOLID or that agents have already been shown to obey it unconditionally. Historical sources and a fixed-patch counterexample motivate the inquiry; whether agents apply, suspend, or withdraw principle-based decisions remains an empirical question.

## 1. A principle does not make the decision

Martin's 1996 drawing example accommodated new kinds of shapes, yet a demand to draw every circle before every square called for a different design judgment. Who owns the ordering requirement—the drawing routine, its callers, or a separate policy? The name of the principle cannot answer for them. This is where our inquiry begins: can a coding agent know a principle without knowing when it is entitled to apply it?

## 2. The qualifications were there all along

Parnas's 1972 decomposition criterion and 1979 account of program families already asked which changing decisions a modular design ought to isolate. Meyer joined extensibility to stable descriptions for clients, while Martin argued that closure against every change is impossible and must instead be strategic. Martin even separated a public field's poor style from necessarily poor design and described a case in which run-time type identification did not violate OCP. This is not an accusation that the authors of SOLID proclaimed an infallible doctrine. It is an invitation to ask what happens to the conditions and exceptions of design advice as that advice moves through teaching, code review, and agent instructions.

## 3. From acquiring authority to withdrawing it

Our object is not the abstract truth of a design maxim but the operative authority it receives over a particular code change. That authority has at least four sites of inquiry: teaching the advice, encoding it as an instruction, using it to accept or reject a patch, and revising the decision after counterevidence. We propose treating principle-based authority as provisional and open to justified withdrawal. Operational quasi-axiomatization is our name for the risk that conditional guidance is enforced beyond its grounds, not an attack on mathematical axioms.

## 4. One patch does not contain its own verdict

Our constructed library example holds fixed a patch that adds technical reports, omits errata, and alters an existing book-output prefix. That patch is acceptable when reports alone are required and the prefix is unprotected, but must be rejected if the prefix is protected or errata are also required. If the old contract is unknown, a justified response may be to defer judgment. This is familiar requirements reasoning, not a newly discovered mathematical law. The question for coding agents is whether a finding labeled 'OCP violation' is carried into patch rejection with due regard for those contracts.

## 5. Making an old literature speak to a new decision

Existing studies already investigate SOLID-violation detection, agent instruction files, stale rules that conflict with code, and code-review overcorrection. We are not the first to notice that AI systems can follow inappropriate instructions. Our proposed synthesis instead joins the original scope of design guidance, current instruction authority, contractual patch correctness, and the possibility of withdrawing a decision into one research problem. For instance, comparing recognizable principle names with equally authoritative unnamed advice can probe one part of that process. A name effect could still be ordinary framing or instruction-following, so it would not by itself reveal a new internal mechanism.

## 6. Open a field of questions, not a new commandment

The question invites historians to track changes in guidance, requirements researchers to adjudicate protected obligations, and AI researchers to measure actual patch behavior. If familiar principle names make no difference, or strict SOLID advice preserves legacy clients better, those outcomes must count. In the longer run, this program may help explain when SOLID works, when another structure wins, and whether a more general account of good software design is possible. For now, our contribution is not such a law but an invitation to turn the authority of accepted design advice into an empirical and historical question. The better the principle, the more important the question: where does its authority to change this particular program come from?

---

## 역사적 근거·연구 계보·후속 검증 — Source notes
- [2026-07-29 최초 대화 기록, EvoNOMOS Archive 1.md](https://drive.google.com/file/d/1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er/view). 사용자가 구분한 원칙/규칙/사실상의 공리화, 인식론적 자율성, 조건부 설계 법칙의 발견이 연구 프로그램의 발단이다.
- [2026-10-08/09 대화 원본, Archive 14](https://drive.google.com/file/d/1TuweqOEc1KY14ddEJVoPbBJAiT-i3thP/view). 기존 수학을 활용해 SOLID를 새롭게 해석하는 것 역시 학술적 목표라는 원래 저자 방침.
- [P35 2026-10-09 Paper B 최초 연구 구상](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_SOLID_OBJECT_ORIENTATION_AND_AI_QUASI_AXIOMATIZATION_PAPER_B.md). 인식론적 자율성, 원칙의 권위와 철회, 역사 비판, 실증의 별도 지위.
- Parnas (1972), [“On the Criteria To Be Used in Decomposing Systems into Modules”](https://doi.org/10.1145/361598.361623); Parnas (1979), [“Designing Software for Ease of Extension and Contraction”](https://ocw.mit.edu/courses/16-355j-software-engineering-concepts-fall-2005/1c68d0f98909a126ec5eb6a0ff358ec7_parnas_ease.pdf).
- Meyer (1988), *Object-Oriented Software Construction*, **초판 일부 pp.22–25만 직접 복구된 자료**: [원전 복구 검증](13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md).
- Robert C. Martin (1996), [“The Open-Closed Principle”](https://www.cs.utexas.edu/~fares/papers/OCP.pdf), 특히 전략적 닫힘과 예외 논의.
- Pehlivan et al. (2025), [*Are We SOLID Yet?*](https://arxiv.org/abs/2509.03093); Gloaguen et al. (2026), [*Evaluating AGENTS.md*](https://arxiv.org/abs/2602.11988); [Xu & Wu, 2026 stale instructions](https://arxiv.org/abs/2610.30571); [2026 agent guardrails research](https://arxiv.org/abs/2604.11088). 관련 범위는 [R24 선행연구 충돌 원장](69_PAPER_B_R24_2026_NEAR_COLLISIONS_AND_NAME_EFFECT_ESTIMAND.md)에 구분했다.
- [고정 패치의 제한된 계약·판정 실례](31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md) — 프로젝트 저자 구성 사례이지 Meyer 원전의 정오표·접두어 표현이 아님.
- [기존 네 조건 에이전트 계획](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md) 및 [원칙 이름 효과 별도 제안](71_PAPER_B_R26_NAMED_PRINCIPLE_COUNTEREVIDENCE_PROTOCOL.md): 모두 실험 미실행.
- [창립 의도 복원 및 서로 다른 독창성 기준](73_PAPER_B_R28_FOUNDING_INTENT_NOVELTY_CATEGORIES_RECONCILIATION.md). 

**한계:** 인과적 역사 전파, AI 모델의 내부 신념, 실제 네 조건/원칙 이름 효과, 토큰·에너지 개선, 일반 설계 법칙의 존재는 이 포지션 논문에서 입증하지 않았다. 개척적인 문제 제안과 입증된 결과를 혼동하지 않는다.