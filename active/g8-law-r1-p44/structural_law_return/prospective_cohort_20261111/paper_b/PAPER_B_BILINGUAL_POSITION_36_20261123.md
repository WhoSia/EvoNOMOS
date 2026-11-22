# 공리로 선언한 적 없는 원칙들
*The Axioms We Never Declared: Software Design Principles and the Possibility of a Higher Structure*

**Paper B · v36 · CONCEPT-FIRST short bilingual position sketch · 2026-11-23 · AUTHOR REVIEW · NOT A PROVEN MATHEMATICAL THEORY**

## 한국어

소프트웨어 개발자들은 SOLID, DRY, KISS, YAGNI처럼 이름이 붙은 원칙을 배운다. 이것들은 문제를 빨리 이해하고 서로 설계를 논의하는 데 큰 도움이 된다. 하지만 한때 좋은 판단을 돕기 위해 만들어진 조언이 언제부터 코드의 합격과 불합격을 결정하는 법칙이 되었을까? 우리는 이 이름들이 수학적인 공리로 선포되었다고 주장하지 않는다. 오히려 그렇게 선포된 적 없는 원칙이 교육, 팀의 관례, 자동화된 리뷰, AI 코딩 지침을 거치며 **마치 공리처럼 다뤄질 수 있다는 가능성**에 주목한다. 이 현상이 실제로 얼마나 널리 일어났는지는 아직 별도로 조사해야 한다.

더 흥미로운 질문은 그다음이다. 어쩌면 SOLID의 다섯 원칙, 중복을 줄이라는 DRY, 불필요한 구현을 미루라는 YAGNI, 정보 은닉과 여러 디자인 패턴은 서로 독립된 최종 법칙이 아닐 수도 있다. 미래의 변경, 보존할 동작, 정보의 경계, 협업의 비용을 서로 다른 각도에서 바라본 **부분적인 지도**일 가능성은 없을까? 새로운 확장이 반복되는 상황에서 OCP가 설득력 있어도, 확장 자체가 거의 필요 없는 상황에서는 YAGNI가 더 절실할 수 있다. 이것은 두 원칙 중 하나가 거짓이라는 말이 아니라, 각 원칙의 **관할 범위**가 다를 수 있다는 생각이다.

수학에서는 하나의 대상을 여러 국소 좌표계로 다루기도 한다. 각 좌표계는 자기 영역에서는 유용하지만, 전체를 한 장의 지도로 표현해야만 하는 것은 아니다. 이 글은 이 비유에서 출발해 설계 원칙을 **전역적인 공리보다 맥락에 따라 유효한 국소적 관점**으로 다시 생각해 보자고 제안한다. 게임이론은 왜 한 설계 관습이 협업의 균형으로 오래 유지되는지, 비단조 논리와 신념 수정은 언제 익숙한 원칙을 철회할 수 있는지, 순서이론·개념격자·범주론은 서로 다른 원칙들의 적용 영역과 구성 관계를 어떻게 나타낼 수 있는지 묻도록 해 준다. 이미 존재하는 이 수학들이 곧바로 SOLID를 통일한다는 뜻은 아니다. **그 수학으로 설계 원칙들을 새롭게 읽는 것**이 이 글의 연구 제안이다.

그래서 우리의 질문은 "SOLID를 준수하면 성능이 오르는가"보다 크다. *누가 설계 원칙에 공리 같은 권위를 주었으며, 그것들이 더 깊은 어떤 구조의 조각이라면 우리는 그 구조를 발견할 수 있을까?* 하나의 상위 구조가 없다는 결론이 나와도 괜찮다. 중요한 것은 오래된 원칙들을 무작정 폐기하는 것도, 비판 없이 따르는 것도 아니라, **원칙 위에 어떤 질서가 있는지를 스스로 묻기 시작하는 것**이다.

## English

Software developers learn principles with memorable names: SOLID, DRY, KISS, YAGNI. They are useful for teaching, discussing, and making designs. Yet when did advice meant to guide judgment begin to sound like law—something that could settle the fate of a code change before its circumstances were discussed? We are not claiming that these principles were formally proclaimed mathematical axioms. We ask whether, through teaching, team conventions, automated review, and AI coding instructions, they can **come to function as though they were**. How often that happens remains a historical and empirical question.

The deeper possibility is more intriguing. Perhaps SOLID, information hiding, reuse heuristics, and familiar design patterns are not independent final truths. They may be **partial maps of a larger terrain**: different ways of looking at change, preserved behavior, information boundaries, and coordination. An extension-friendly design may make sense under repeated variation; resisting premature abstraction may make more sense elsewhere. OCP and YAGNI need not contradict each other if they speak to different regions of the design problem.

Mathematics sometimes describes a complex space with multiple local coordinate charts rather than one global map. We propose this as a starting analogy for design principles: not universal axioms but potentially **local views whose domains and overlaps matter**. Game theory asks why a convention can persist through coordination, even without universal technical optimality. Defeasible reasoning asks when an accepted principle should yield to new evidence. Order theory, concept lattices, and categorical compositionality invite us to ask what, if any, structure relates these partial views. None of those established mathematical theories is our invention, and their names alone do not demonstrate a single theory of SOLID. The proposal is to bring them into conversation with design practice.

The question, then, is larger than whether obeying SOLID improves one benchmark. **Who gave design principles their near-axiomatic authority, and could the principles be fragments of something more general?** We need not prejudge the answer. Even finding several irreducible structures would teach us more than elevating familiar slogans into laws.

## Source and claim integrity

- Origin of the two user-led questions: [EvoNOMOS first chat, 2026-07-29](https://drive.google.com/file/d/1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er/view) and [October 9 research discussion](https://drive.google.com/file/d/1TuweqOEc1KY14ddEJVoPbBJAiT-i3thP/view).
- Existing mathematics used as conceptual bridges, not claimed original: [Monderer–Shapley potential games](https://doi.org/10.1006/game.1996.0044); [Dung (1995) argumentation, owned original](https://drive.google.com/file/d/1QFpaDCwOINWeak1cXSXyvcN6Vrin3lkR/view); [Darwiche–Pearl (1997) belief revision, owned original](https://drive.google.com/file/d/1fMpdbYg_ewS5Cwyh_jWRDx1AfDo0R6Fi/view); [Ganter–Wille formal concept analysis](https://link.springer.com/book/10.1007/978-3-642-59830-2); [Fong–Spivak compositionality](https://arxiv.org/abs/1803.05316); [Cousot–Cousot abstract interpretation, owned original](https://drive.google.com/file/d/1hZfipMMYFSwpOVx4ZuhAIvkzt4jDptIl/view).
- [R52 cross-field idea atlas](97_EVONOMOS_R52_DESIGN_PRINCIPLES_HIGHER_MATH_IDEA_ATLAS.md) contains explicit distinctions, possible connections and limitations. The **local-chart metaphor is NOT a claim that software-design space has been shown to be a smooth manifold**, and no coordinate transition maps have been constructed. This is an idea paper; no new law, empirical trend or agent behavior is reported.
- Previous experimental/current writing research retained as independent tracks: [v35](PAPER_B_BILINGUAL_POSITION_35_20261123.md); [R36 higher-order conjectures](81_EVONOMOS_R36_HIGHER_ORDER_STRUCTURE_INDEPENDENT_CONJECTURES.md).

**Authorial status:** a short research thesis deserving conceptual development and scholarly comparison, not a mathematical theorem or an experimentally verified causal story.
