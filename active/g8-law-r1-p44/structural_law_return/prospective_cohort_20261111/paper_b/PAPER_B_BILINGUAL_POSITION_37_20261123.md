# 공리로 선언한 적 없는 원칙들
*The Axioms We Never Declared: Design Heuristics, Their Authority, and a Possible Higher Structure*

**Paper B · v37 · bilingual short conceptual position · 2026-11-23 · AUTHOR REVIEW. The proposal, not an empirical discovery or mathematical proof.**

## 한국어

소프트웨어 개발자는 SOLID, DRY, KISS, YAGNI처럼 이름이 붙은 설계 원칙을 배운다. 이 이름들은 경험을 나누고 어려운 설계 결정을 설명하는 데 유용하다. 그런데 코드 리뷰에서 “OCP를 어겼으니 고쳐야 한다”는 말이 나오면, 그 판단을 뒷받침하는 조건은 어디에 있는가? 지금 바뀔 가능성이 높은 것이 무엇인지, 어떤 기존 동작을 보존해야 하는지, 그 변경을 누가 요청했는지에 따라 답은 달라질 수 있다. 물론 팀이 OCP 준수를 명시적으로 요구했다면 따라야 할 프로젝트 규칙이 있을 수도 있다. 문제는 **설계에 관한 조언, 프로젝트가 승인한 규칙, 반드시 성립해야 할 동작의 계약을 같은 종류의 명제로 취급하는 순간** 생긴다. 우리는 SOLID가 정식 수학적 공리로 선언되었다고 주장하지 않는다. 다만 **선언되지 않은 공리 같은 권위**가 어떤 상황에서 생겨나는지 묻는다.

프로그래밍을 코드 생산보다 개발자의 *이론 형성*에 가깝게 본 Peter Naur의 1985년 논의는 이 질문에 오래된 토대를 제공한다. 프로그램을 고치는 사람에게 필요한 것은 기호와 문서만이 아니라, 그 프로그램이 해결하려는 문제를 이해하는 능력이라는 것이다. Stephen Toulmin도 논증의 공통적인 형식과 분야에 따라 달라지는 정당화 기준을 구별했다. 이 두 관점에서 보면, “OCP 위반”이라는 이름은 판단을 시작하는 단서일 수 있어도 그 판단의 이유 전체는 아니다. 그 이름이 언제 충분한 이유가 되는지는 별도로 설명해야 한다.

여기서 더 큰 가능성을 생각해 볼 수 있다. SOLID의 다섯 원칙, 중복을 줄이라는 DRY, 섣부른 구현을 경계하는 YAGNI, 정보 은닉과 디자인 패턴은 모두 하나의 공리계에서 연역된 정리가 아닐 수 있다. 오히려 변경의 방향, 보존할 기능, 의존 관계, 협업의 비용이라는 서로 다른 문제를 비추는 **부분적인 지도**에 가까울지도 모른다. OCP가 새로운 종류의 확장을 다룰 때 유익하고 YAGNI가 필요 없는 확장을 미룰 때 유익하다면, 두 원칙의 차이는 반드시 모순이 아니다. 각기 어떤 문제에서 효력을 갖는지, 그 영역이 겹칠 때 무엇을 우선할지 묻는 편이 더 생산적이다.

그런 관계를 수학적으로 나타낼 방법은 이미 여러 분야에서 발전해 왔다. 순서이론과 개념격자는 원칙의 적용 영역 및 포함 관계를, 비단조 논리와 신념 수정은 새로운 반례 앞에서 판단을 철회하는 방식을, 게임이론은 공유된 설계 관습이 협업 속에서 유지될 가능성을 생각하게 한다. 그러나 이것들이 곧바로 SOLID를 통일한다는 뜻은 아니다. 한 가지 상위 구조가 아니라 서로 환원되지 않는 여러 구조가 나올 수도 있다. 또한 소프트웨어 구조를 자동 탐색하는 알고리즘의 **목적함수 역시 누군가 선택한 판단 기준**이다. 알고리즘이 점수를 최적화했다는 사실은 그 점수가 좋은 설계의 법칙이라는 증명이 아니다.

EvoNOMOS가 제기하려는 질문은 두 가지다. **설계 원칙은 어떤 근거에서 공리처럼 강제될 수 있으며, 우리가 익숙한 이름으로 부르는 원칙들 위에는 아직 충분히 드러나지 않은 구조가 있는가?** 여기서 답을 먼저 선언하지는 않겠다. 원칙은 버릴 대상도, 시험을 면제받을 대상도 아니다. 이름이 남는 것보다 중요한 것은 그 이름을 정당화했던 사유가 남는 일이다.

## English

Software developers learn principles with memorable names: SOLID, DRY, KISS, YAGNI. Those names help us share experience and explain difficult design choices. But when a reviewer says, “This violates OCP, so it must be fixed,” where are the conditions that warrant the verdict? The answer may depend on what is likely to change, which existing behavior must survive, and who requested the change. A team may, of course, have deliberately adopted OCP as a binding local standard. The difficulty begins **when design advice, authorized project rules, and behavioral contracts are treated as the same kind of proposition**. We do not claim that SOLID was declared a mathematical axiom. We ask how advice can sometimes acquire **the force of an axiom that was never declared**.

Peter Naur's 1985 view of programming as *theory building* offers an older point of departure. What enables programmers to modify a system is not merely its code and documentation, but a situated understanding of the problem the program addresses. Stephen Toulmin likewise distinguished elements common to arguments from criteria of justification that depend on the field. On this view, “OCP violation” might begin an argument; it cannot, on its own, supply every reason that argument requires. The missing warrants matter.

A larger possibility follows. The five SOLID principles, DRY, YAGNI, information hiding, and design patterns need not be theorems derived from one undisputed axiom system. They might instead be **partial maps** of different concerns: directions of change, preserved behavior, dependencies, and coordination costs. OCP may be valuable when a system must accommodate recurring new variants; YAGNI may be valuable when extending it would be premature. Their recommendations do not necessarily contradict one another. The more interesting question concerns their domains, their overlaps, and how to judge cases where they seem to conflict.

There are existing mathematical resources for asking such questions. Order theory and concept lattices can prompt us to examine domains and inclusion relations; defeasible argumentation and belief revision offer accounts of retracting claims in light of new reasons; game theory helps explore how shared conventions might persist through coordination. None of these established theories automatically unifies SOLID. Several irreducible structures may be needed. Even the **fitness function** used in automatic software design represents a human choice about what deserves to count as improvement. A search algorithm's optimum is not, merely by being an optimum, a law of good design.

EvoNOMOS therefore begins with two questions. **On what grounds can a design principle acquire axiom-like force, and might our familiar principles be fragments of structures we have not yet adequately described?** We need not decide the answers in advance. A principle is neither something to discard casually nor something to exempt from examination. What matters is not only whether its name survives, but whether the reasoning that once justified it survives with it.

## Sources and scope

The core two research questions originated in the author's [first EvoNOMOS conversation, 2026-07-29](https://drive.google.com/file/d/1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er/view), revisited in the [2026-10-09 research discussion](https://drive.google.com/file/d/1TuweqOEc1KY14ddEJVoPbBJAiT-i3thP/view). This text is a **conceptual position**, not evidence that actual AI agents routinely obey SOLID as a universal axiom or that the Principle Atlas Hypothesis has been mathematically proved.

### Selected direct source readings
- Naur, P. (1985). [*Programming as Theory Building*](https://drive.google.com/file/d/1h6omxTHbuPYrKe_hjf0U_BtYCs1s8OgC/view). *Microprocessing and Microprogramming*, 15, 253–261. Original paper read; cited for programming as situated understanding, NOT an existing SOLID mathematical atlas.
- Toulmin, S. (1958; updated ed. 2003). [*The Uses of Argument*](https://drive.google.com/file/d/1gP-zJtB9YRYrbfwWwKwXl2GMWsobMizO/view). Original owned revised volume inspected in relevant parts; field-dependent warrants predate EvoNOMOS.
- Alchourrón, C. E., Gärdenfors, P., & Makinson, D. (1985). [*On the Logic of Theory Change*](https://drive.google.com/file/d/1nCMd4zfQcbr28HJkmFqRvHFsGWh8QabQ/view). *Journal of Symbolic Logic*, 50(2), 510–530. Already established mathematical belief-revision framework.
- Parnas, D. L. (1972). [*On the Criteria to Be Used in Decomposing Systems into Modules*](https://drive.google.com/file/d/1EcQRy3iehx4lUN7uGsZ1BFXU33HggcEQ/view); Parnas (1979), [*Designing Software for Ease of Extension and Contraction*](https://drive.google.com/file/d/1XGzB9hq_6wk6aXeVojMo1IeKoKCg704j/view). Existing software change and modularity criteria.
- Baldwin, C. Y. (2023). [*Design Rules: Past and Future*](https://drive.google.com/file/d/14QDJGv1bN_42BY-d15gnX2svKDXkE04Q/view). Original modularity theory author's self-critique. Räihä, O. (2010). [*A Survey on Search-Based Software Design*](https://drive.google.com/file/d/1BdFL0tU7Nna7jqQM0oPK6Ds1wdtyZS8S/view). Original survey, including representation and fitness-function choice.
- Suh's [Axiomatic Design](https://academic.oup.com/book/52792/chapter-abstract/421881976) is an intentional axiomatization precedent; Alexander's [*A Pattern Language*](https://christopher-alexander-ces-archive.org/book/a-pattern-language/) is a context-linked design-pattern precedent. Publisher/archive descriptions checked, not full books reread here.

### Research-track separation
The detailed cross-field [R52 mathematical atlas](97_EVONOMOS_R52_DESIGN_PRINCIPLES_HIGHER_MATH_IDEA_ATLAS.md), [R55 hidden fitness-function authority](100_EVONOMOS_R55_FITNESS_FUNCTIONS_HIDDEN_AXIOMS_AND_TYPED_PRINCIPLES.md), [R57 genre/Naur–Toulmin/LIRA audit](102_EVONOMOS_R57_GENRE_AUDIT_NAUR_TOULMIN_AGM_LIRA_V36.md), and earlier [v35 empirical programme](PAPER_B_BILINGUAL_POSITION_35_20261123.md) are **parallel work**, not requirements to prove before posing this idea. The local-chart analogy is a metaphor, not an assertion of a smooth manifold or known atlas of all design principles.

**Status: AUTHOR REVIEW. New interpretation and explicit questions; no universal theorem, empirical SOLID-dogmatism prevalence estimate or real-world architecture-effect finding claimed.**
