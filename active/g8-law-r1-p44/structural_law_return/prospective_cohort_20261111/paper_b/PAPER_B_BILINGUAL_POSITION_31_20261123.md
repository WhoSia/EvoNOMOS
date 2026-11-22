# 원칙이 명령이 되는 순간
*When Advice Becomes Authority: SOLID and Revisable Design Judgment in AI-Assisted Programming*

**Paper B · v31 · bilingual position manuscript · 2026-11-23 · author-review draft, not submitted.** 30판의 원래 연구 질문을 보존하면서 WRITING 3.0과 [LIRA 0.1](https://app.notion.com/p/420ef561cf928159986dc36b3c6464f8)을 이용해 문장과 문단의 기능에 따라 리듬을 새로 구성했다. 역사적 문제 제안이지 관측된 AI 효과나 새로운 설계 법칙의 발표는 아니다.

# 한국어 원고

## 초록

SOLID는 소프트웨어 설계의 유용한 언어다. 그러나 익숙한 원칙을 잘 설명할 수 있다는 사실과, 그 원칙으로 지금 눈앞의 수정안을 승인하거나 거절할 자격이 있다는 사실은 다르다. 객체지향 설계의 역사에는 이미 그런 판단의 조건이 들어 있었다. 우리는 그 조건이 교육과 코드 리뷰에서 어떻게 전달되고, AI 코딩 에이전트의 지침과 실행 과정에서 어떤 권위를 얻으며, 반대 증거가 나왔을 때 그 권위를 철회할 수 있는지 연구하자고 제안한다. 이를 *운영상의 준공리화*라는 문제로 부를 수는 있지만, 누군가 SOLID를 형식적 공리로 선포했다거나 AI가 이미 이를 맹목적으로 따른다는 뜻은 아니다. 이 글은 개념을 선언하는 대신, 역사적 원전과 작은 수정 사례에서 질문을 날카롭게 다듬고 연구자가 검증할 방법을 제시하는 짧은 포지션 논문이다.

## 1. 원을 먼저 그리라는 요구

Robert Martin이 1996년에 설명한 도형 프로그램은 새 도형을 추가하기에 편리했다. 각 도형이 자신을 그리는 방법을 알면, 그리기 함수를 뜯어고치지 않고도 도형의 종류를 늘릴 수 있기 때문이다. 그런데 모든 원을 사각형보다 먼저 그려야 한다면 이야기가 달라진다. 정렬의 책임은 그리기 함수에 있는가, 호출자에게 있는가, 아니면 별도의 정렬 정책으로 분리해야 하는가?

**원칙의 이름은 그 답을 대신하지 않는다.**

Martin 자신도 프로그램을 모든 가능한 변화로부터 닫아 둘 수 없으며, 대비할 변화를 선택해야 한다고 설명했다. 나아가 공개 멤버 변수가 보기 좋지 않은 스타일이어도 반드시 잘못된 설계인 것은 아니라고 구별했고, RTTI를 써도 OCP를 위반하지 않는 경우를 들었다. 더 거슬러 올라가면 Parnas가 1972년과 1979년에 논의한 정보 은닉과 프로그램 계열 역시 어떤 결정이 바뀔 수 있는지를 먼저 따졌다. 이 역사에서 얻는 교훈은 SOLID의 원저자가 틀렸다는 것이 아니라, **원칙의 근거에 언제나 변화의 종류와 보호할 의무가 들어 있었다**는 점이다.

## 2. 조언은 어떻게 권위를 갖는가

수업에서는 원칙을 배우고, 코드 리뷰에서는 그 원칙의 이름을 말하며, 자동화된 도구나 코딩 에이전트는 그 이름을 지침으로 읽을 수 있다. 서로 다른 일이다. 설명을 돕는 말이 실제 수정 권한을 행사하려면, 무엇을 바꿀 수 있고 어떤 이전 동작을 보존해야 하는지부터 알아야 한다. 그렇지 않다면 원칙의 인지도와 결정의 정당성을 뒤섞기 쉽다.

우리가 *운영상의 준공리화*라고 부르려는 것은 바로 그 위험이다. 형식 논리의 공리화를 비난하는 것도, 모델 안에 교조적인 믿음이 존재한다고 추정하는 것도 아니다. 조건부 조언이 출처와 적용 범위를 따지지 않은 채 패치를 움직이게 되는지를 묻는 작업이다. 중요한 것은 거절하는 능력만이 아니다. **새로운 사실 앞에서 원칙에 기대어 내린 판단을 고칠 수 있는가?** 그런 의미에서 원칙의 권위는 철회 가능해야 한다.

## 3. 같은 코드, 다른 결론

이전 판본에서 구성한 작은 도서관 예제를 생각해 보자. 고정된 수정안은 기술보고서를 지원하지만 정오표를 지원하지 않고, 기존 책 출력의 접두어도 `book`에서 `BOOK`으로 바꾼다. 요구가 기술보고서의 추가뿐이고 책 접두어를 보존할 의무가 없다면 이 사례의 조건에서는 승인할 수 있다. 반대로 접두어가 기존 계약의 일부라면 거절해야 하며, 정오표 지원까지 요구됐다면 접두어와 무관하게 미완성이다. 그 계약이 무엇인지 알 수 없다면 정답을 서둘러 고르기보다 판단을 보류하는 편이 옳다.

새 수학 정리를 제시한 것은 아니다. 이런 구별은 이미 요구공학과 계약 기반 설계에서 다뤄졌다. 우리가 다시 묻고 싶은 건 다른 대목이다. **AI가 코드에 붙인 ‘OCP 위반’이라는 표지를 실제 패치의 거절 사유로 옮길 때, 그 패치가 만족해야 할 요구와 보존해야 할 클라이언트를 끝까지 확인하는가?**

## 4. 낡은 원칙을 새롭게 조사하는 방법

SOLID 위반을 분류하는 언어모델 연구, 에이전트의 저장소 지침에 관한 실험, 오래된 지침이 코드와 충돌하는 사례, 코드 리뷰의 과잉 판정 연구는 이미 있다. 따라서 AI가 가끔 지시를 잘못 따른다는 관찰을 처음 제안하는 것은 아니다. Paper B가 열어 보려는 범위는 그보다 한 단계 더 역사적이면서도 구체적이다. **조건을 갖춘 설계 조언이 어떻게 권위를 얻어 코드 수정의 판단 기준으로 사용되는지, 그 권위는 어떤 증거로 정당화되거나 제한되는지**를 하나의 연구 대상으로 묶는다.

역사 연구자는 원전의 예외와 적용 조건이 교육 문헌 및 지침에 어떻게 남았는지 추적할 수 있고, 소프트웨어 공학 연구자는 실제 프로젝트의 요구와 기존 호출자 계약을 고정한 채 에이전트의 패치 선택을 비교할 수 있다. 한 가지 실험에서는 원칙의 이름이 붙은 조언과 같은 뜻의 이름 없는 조언을 대비해 볼 수 있겠지만, 그것만으로 전체 문제를 해결할 수는 없다. 이름이 주는 익숙함, 문장의 강조, 명시적 지시의 우선순위가 모두 판단에 영향을 줄 수 있기 때문이다. 무엇보다 **강한 SOLID 지시를 충실히 따른 행동이 정당한 사용자 지시 준수일 가능성**부터 열어 둬야 한다.

## 5. 원칙을 지킬 것인가, 언제 지킬 것인가

이 연구는 실패한 에이전트를 찾아 SOLID를 비난하려는 계획이 아니다. 원칙을 강조한 쪽이 기존 계약을 더 잘 보존하거나, 원칙의 이름이 설명의 어휘만 바꾸고 실제 패치는 바꾸지 않을 수도 있다. 그러면 그 사실을 그대로 받아들이고 연구 질문을 다시 좁혀야 한다. 향후에는 실제 변경의 연속과 유지보수자·에이전트의 비용까지 함께 살펴, 어느 조건에서 특정 원칙이 유익한지 설명하는 더 포괄적인 이론으로 나아갈 수 있다. 아직 그 법칙이나 토큰·에너지 절감 효과를 발견한 것은 아니다.

좋은 설계 원칙을 더 많이 외우는 일보다 어려운 문제가 남아 있다.

**그 원칙이 바로 이 코드를 바꾸라고 말할 권한은 어디에서 오는가?**

---

# English manuscript

## Abstract

SOLID gives software engineers a useful vocabulary for design. Knowing the vocabulary, however, is not the same as having sufficient grounds to accept or reject a particular patch. The history of object-oriented design already contains qualifications about anticipated change and obligations to existing clients. This position paper brings those qualifications into conversation with requirements engineering and the increasingly executable instructions of AI coding agents. We ask how design advice acquires authority over actual changes, and whether that authority can be revised when contrary evidence appears. *Operational quasi-axiomatization* names a possible failure of judgment, not an established fact about model beliefs or a claim that SOLID was ever formally declared an axiom system. We offer a historical argument, a small constructed case, and an invitation to test the question.

## 1. Draw the circles first

Robert Martin's 1996 drawing example makes one sort of change easy: a new type of shape can supply its drawing operation without rewriting the drawing loop. Now consider a different request—every circle must appear before every square. Who owns the ordering requirement? The drawing routine, its callers, or a separate ordering policy?

**The name of a principle cannot answer that question.**

Martin's own account recognizes that no nontrivial program can be closed against every possible change; closure must be strategic. He also distinguishes poor public-field style from necessarily poor design and gives a case in which run-time type identification is compatible with OCP. Long before the SOLID mnemonic, Parnas had tied modular boundaries to likely-changing design decisions and families of programs. These are not admissions that the original principles were wrong. They are evidence that the advice was already conditional.

## 2. From guidance to authority

A principle serves different purposes in a classroom, a code review, and an agent instruction file. Teaching the name of a principle does not settle who is authorized to change existing behavior or which clients must continue to work. Yet software agents can turn the words of such advice into actual edits, approvals, and refusals.

We propose examining the point at which conditional guidance acquires more authority than the task evidence warrants. That is the risk we call *operational quasi-axiomatization*. It is neither an objection to mathematical axioms nor an attempt to infer hidden beliefs inside a model. A sharper test concerns what happens after the agent receives credible contrary evidence: can it revise a principle-based decision, or does a familiar maxim retain force even when its application is no longer justified? For engineering decisions, authority should have conditions of withdrawal.

## 3. The patch stays still

In a library example constructed for this research, one fixed patch adds technical reports but not errata, and changes the old book-output prefix from `book` to `BOOK`. Under a report-only request with no protected prefix obligation, that patch can be accepted in the stipulated world. Protect the old prefix and it must be rejected; require errata as well and it is incomplete for another reason. If the old contract is unknown, the appropriate disposition may instead be to defer.

Nothing in this small example is a new theorem about requirements. That tradition already teaches us to reason from contracts. It makes the next question possible: **when a coding agent calls something an OCP violation, what licenses the move from that label to rejecting this specific patch?**

## 4. A research agenda with room to lose

Studies already assess SOLID-violation detection, repository instruction files, stale rules that conflict with source code, and false alarms in automated code review. We should not claim to have discovered the general phenomenon of agents following the wrong rule. Our proposed contribution is to connect the historical scope of design advice, its authority as an instruction, its effect on a concrete change, and the possibility of withdrawing a decision in light of better evidence.

A historian can trace whether a principle's original qualifications survive in later guidance. A requirements researcher can independently determine what a real patch must preserve; an AI researcher can then compare what agents actually change under matched tasks and permissions. One diagnostic could contrast familiar principle names with semantically matched unnamed advice, but that is only a lens. Familiarity, emphasis, and legitimate instruction precedence remain competing explanations. Following an explicitly authorized strict SOLID policy is not automatically an error.

## 5. Principles worth revising

This is not a search for guilty agents or a campaign against SOLID. Strict principle guidance may preserve legacy contracts better; principle labels may change explanations without changing patches. Both outcomes would narrow the account we have proposed. In the longer run, the same inquiry might help us describe when a design principle is beneficial, when an alternative works better, and whether a more general conditional theory of software design is possible. No such theory—and no token or energy saving—is established here.

There is a harder question than whether a programmer remembers the rule.

**Where does that rule get its authority to change this particular program?**

---

## Primary sources and scope notes (retained for author review)

- Parnas (1972), [modular decomposition](https://doi.org/10.1145/361598.361623); Parnas (1979), [extension and contraction / program families](https://ocw.mit.edu/courses/16-355j-software-engineering-concepts-fall-2005/1c68d0f98909a126ec5eb6a0ff358ec7_parnas_ease.pdf).
- Meyer (1988), *Object-Oriented Software Construction*, project recovered **partial** first-edition pages 22–25: [passage audit](13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md).
- Martin (1996), [*The Open-Closed Principle*](https://www.cs.utexas.edu/~fares/papers/OCP.pdf), especially strategic closure and heuristics/conventions.
- Pehlivan et al. (2025), [*Are We SOLID Yet?*](https://arxiv.org/abs/2509.03093); Gloaguen et al. (2026), [*Evaluating AGENTS.md*](https://arxiv.org/abs/2602.11988); Xu & Wu (2026), [*Stale Instruction Files Override the Code*](https://arxiv.org/abs/2610.30571).
- [Researcher-constructed fixed-patch case](31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md); [Paper B 2026-10-09 founding proposal](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_SOLID_OBJECT_ORIENTATION_AND_AI_QUASI_AXIOMATIZATION_PAPER_B.md); [Research OS LIRA 0.1](https://app.notion.com/p/420ef561cf928159986dc36b3c6464f8).
- No four-arm live agent trial, no name-effect trial, no historical causal transmission test and no general architecture law is established by this paper. Its claim is an interdisciplinary research invitation.
