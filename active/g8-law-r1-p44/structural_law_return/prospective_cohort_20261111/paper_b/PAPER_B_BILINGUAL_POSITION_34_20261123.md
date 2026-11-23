# 원칙을 지키기 전에, 원칙을 시험할 수 있는가?
*Before Obeying a Principle, Can We Test It? SOLID and the Search for Conditional Laws of Software Design*

**Paper B · v34 · bilingual position paper · 2026-11-23 · AUTHOR REVIEW / no new empirical law claimed**

# 한국어 원고

## 초록

SOLID는 널리 알려진 설계 원칙이지만, 어떤 코드에 적용해야 하는지까지 이름만으로 결정할 수는 없다. 개방–폐쇄 원칙(OCP)은 새로운 기능을 쉽게 확장하도록 권하지만, 그 확장 경계를 잘못 고르면 오히려 수정하기 어려운 구조를 만들 수 있다. 그렇다면 **좋은 설계 원칙이란 무엇이며, 어느 조건에서 좋은가?** 우리는 설계 원칙을 따를 명령이나 점수를 매길 체크리스트 대신, 적용 범위와 반례를 갖는 *검증 가능한 조건부 가설*로 연구하자고 제안한다. 실제 변경 요구, 보호할 동작, 유지보수자, 시간적 비용을 비교하여 기존 원칙이 유익한 조건을 식별하고, 더 나아가 기존 명칭으로 설명되지 않는 구조적 규칙을 발견할 수 있을까? AI 코딩 에이전트가 원칙을 쉽게 실행하고 반복할 수 있는 지금, 이 오래된 질문은 더 중요해졌다. 본 논문은 새로운 법칙을 발표하지 않는다. 그 법칙이 **어떻게 발견되거나 기각될 수 있어야 하는지**를 묻는다.

## 1. 이름을 아는 것과 적용할 이유를 아는 것

1996년 Robert Martin의 도형 프로그램에서 새 도형을 그리는 기능을 추가하려면 기존 그리기 루프를 매번 고칠 필요가 없도록 만들 수 있다. 하지만 “원은 사각형보다 먼저 그려라”라는 새 요구가 생기면 어디에 정렬의 책임을 둘지 다시 결정해야 한다. Martin이 말한 *전략적 닫힘*은 모든 변화를 미리 막을 수 없다는 사실을 전제로 한다. 앞으로 무엇이 바뀔 것인지에 따라 닫아야 할 경계가 달라진다는 것이다.

그런데 오늘날 “OCP 위반”이라는 표현은 설계상의 특징을 설명하는 말이면서, 때로 수정안을 거절하라는 요구처럼 읽힐 수 있다. 어느 팀에서는 정당한 정책일 수도 있다. 문제는 표현의 강도가 아니라 그 판단을 뒷받침할 조건이다. **좋은 원칙을 외워도, 지금 그 원칙을 적용해야 하는지는 여전히 모르기 때문이다.**

## 2. 같은 설계가 다른 미래를 만난다면

앞으로 서로 다른 보고서 형식을 계속 추가해야 하는 프로그램이라면 안정된 확장 경계에 투자하는 편이 유리할 수 있다. 반면 앞으로 바뀔 것은 보고서 종류가 아니라 모든 보고서에 공통된 처리 순서라면, 같은 추상화가 불필요한 우회를 늘릴 수도 있다. 어느 쪽이 낫다는 결론은 프로그램 한 장의 클래스 다이어그램보다 **예상되는 변경, 보호할 기존 계약, 변경을 수행할 사람이나 에이전트, 비용을 계산할 기간**에 더 많이 의존한다. 두 미래는 비교를 위한 가정이지, 이번 논문이 실제 프로젝트에서 관측한 결과가 아니다.

이 문제는 설계의 여러 기준을 한 점수로 뭉칠 수 있다는 뜻도 아니다. 가령 Liskov 치환 원칙(LSP)의 행동적 계약을 어기는 구현이 단기간 수정 비용을 낮춘다고 해도, 그 구현을 그냥 '효율적인 설계'로 승인할 수는 없다. 반드시 지켜야 하는 동작은 비용과 교환할 대상이 아니라 먼저 만족해야 할 조건이 될 수 있다. **원칙 사이에 우열을 매기기 전에, 무엇이 선택 가능한 설계인지부터 가려야 한다.**

## 3. 원칙을 발견하는 연구

우리가 제안하는 연구의 출발점은 SOLID의 다섯 이름이 아니라 변화하는 소프트웨어의 구체적인 문제다. 어떤 구조가 어떤 변화에 대응하면서 어떤 동작을 보존하고, 그 대가로 무엇을 지불하는지 확인한다. 같은 기능을 수행하는 여러 구조를 서로 다른 변경 과정에 노출시키고, 기존 원칙이 설명하는 유리함과 불리함을 비교한다. 잘 맞는 조건은 좁혀서 기술하고, 반례가 나오면 원칙을 수정하거나 적용 판단을 보류한다. 더 나아가 SOLID라는 이름을 미리 정답으로 지정하지 않은 채 구조적 개입을 재조합하여, 오래된 원칙과 닮았거나 전혀 다른 **조건부 설계 가설**을 찾아볼 수 있다.

여기에는 쉽지 않은 난제가 남는다. 미래 요구는 완전히 알려져 있지 않고, 유지보수 비용에는 사람·도구·시간에 관한 판단이 들어간다. 동일한 코드가 서로 다른 환경에서 다르게 평가될 수도 있으며, 서로 비교할 수 없는 설계들이 남을 수도 있다. 이 불확실성은 연구를 중단할 구실이 아니다. **보편적으로 옳은 원칙을 억지로 만들지 않고도, 언제 어떤 원칙을 믿을 만한지 밝히는 것**이 바로 연구의 목표다.

## 4. AI 시대의 설계 원칙

코딩 에이전트는 원칙의 이름을 읽고 실제 파일을 바꿀 수 있다. 그래서 조건부 조언이 “반드시 고쳐야 할 위반”이라는 어휘로 제시되는 현상은 조사할 가치가 있다. 그러나 그것은 이 연구의 한 증상이지 목적지 전체가 아니다. 이미 코딩 에이전트의 코드 관례와 명시 지시 간 선택, 지시의 역할·출처 표지 효과를 실험한 연구들이 있다. 우리에게 더 중요한 질문은 **어떤 원칙을 어떤 근거와 범위에서 적용해야 하는가, 그리고 더 나은 원칙을 배울 수 있는가**다.

새로운 설계 법칙의 존재를 전제할 필요는 없다. SOLID의 일부는 더 일반적인 구조적 판단으로 설명될 수 있고, 다른 일부는 환원되지 않는 독립된 조건일 수 있다. 그 구별을 찾는 과정 자체가 연구가 된다.

**원칙이 오랫동안 살아남았다는 사실은 존중할 이유다. 그 원칙을 시험하지 않아도 된다는 이유는 아니다.**

---

# English manuscript

## Abstract

SOLID is a familiar vocabulary of software design, but the vocabulary alone does not tell us when a principle should govern a particular change. The Open–Closed Principle (OCP) can make new extensions inexpensive; an abstraction placed at the wrong boundary can instead make future changes harder. **What makes a design principle good—and under which conditions?** We propose treating design principles not as commands to obey or checklist items to count, but as *defeasible, testable, conditional hypotheses*. By comparing protected behavior, plausible change processes, maintainers, and costs over time, could we identify where established principles help and discover structural regularities beyond their original names? AI coding agents can now enact and repeat design advice at scale, making the epistemic question consequential. This position paper does not announce a new law. It asks what it would take to **discover—or reject—one**.

## 1. Knowing the name is not knowing when to apply it

Robert Martin's 1996 drawing example shows how a new shape can be added without repeatedly changing the drawing loop. But the demand that circles appear before squares raises a different question: which component owns ordering? Martin's account of *strategic closure* accepts that no program can be closed against every possible change. A useful boundary depends on which changes are anticipated.

The phrase “OCP violation” can describe a structural feature. It can also sound like a veto on a patch; within a particular team's legitimately adopted rules, that veto might be warranted. The difficulty is not forceful wording by itself. **Learning the rule does not tell us whether this is the moment to use it.**

## 2. The same architecture, two possible futures

Suppose a program will acquire many new report formats. Investing in a stable extension boundary might pay off. Suppose instead that the next changes repeatedly alter a workflow shared by every report. The same abstraction could add indirection without purchasing useful flexibility. These are stipulated alternative futures, not empirical observations reported here. Which architecture is preferable depends on anticipated changes, legacy obligations, the maintainers or agents making the changes, and the time horizon of the comparison.

Not every design concern belongs in one scalar maintenance score. A subtype that violates a protected behavioral contract does not become acceptable merely because it is cheap to modify. For some properties—Liskov-style substitutability is a clear example—correctness can be an admissibility condition rather than an optional cost. **Before comparing designs, we must know which designs are even eligible.**

## 3. A research programme for discovering principles

Our starting point is not a five-letter mnemonic but the changing software system. What structural intervention preserves which behaviors under what kinds of change, and at which costs? We could compare functionally admissible alternatives under changing maintenance demands; specify the contexts in which a known principle helps, revise or abstain when counterexamples appear, and search combinations of structural interventions without prescribing SOLID labels as the answers. The result might be a recognizable old principle, a better-scoped version of it, or a new conditional design hypothesis.

The difficult part should not be hidden. Future requirements are uncertain; maintenance costs are shaped by people, tooling, and time; different purposes may leave several non-dominated designs. A research programme need not solve those difficulties in advance. Its purpose is to make them observable and to find **what evidence would warrant applying a principle rather than merely repeating it**.

## 4. What coding agents change

Coding agents can turn a design maxim into an actual edit or refusal. A historically conditional guideline rephrased as a “violation that must be fixed” is therefore worth investigating. But the linguistic shift is one possible symptom, not the full scientific destination. Existing studies have already examined coding agents' preferences for repository precedents versus explicit instructions and the effects of instruction position, role, and source labels. Our larger question is when a design principle is justified by the task and whether more useful principles can be learned.

A higher-order structure may explain some parts of SOLID while leaving other parts irreducible. That possibility is not a result we can assume. It is something to pursue with counterexamples and admissible comparisons.

**Survival is a reason to take a principle seriously. It is not a reason to stop testing it.**

---

## Source lineage and status

- [EvoNOMOS founding chat, 2026-07-29](https://drive.google.com/file/d/1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er/view), especially `Conditional Principle Formalism, Lifecycle Utility & No-Universal-Best Boundary`, synthetic intervention/revision cycles and author's “원칙과 규칙은 달라” objection.
- Martin (1996), [*The Open–Closed Principle*](https://www.cs.utexas.edu/~fares/papers/OCP.pdf); Parnas (1972), [modularization/information hiding](https://doi.org/10.1145/361598.361623); Liskov & Wing (1994), [*A Behavioral Notion of Subtyping*](https://www.cs.cmu.edu/~svc/papers/view-publications-lw94.html).
- Zhu et al. (2026), [*Precedent or Intent?*, user-curated PDF](https://drive.google.com/file/d/1mk1MmGh5QfFUPmT_CTe9srLTDEZjU784/view); Laddha et al. (2026), [*Position, Role or Label?*, user-curated PDF](https://drive.google.com/file/d/1E-alGOnlpVPoE8IHSF1USVyRWhMVQHrv/view). Their results are not EvoNOMOS experiments.
- [R39 founding-thesis recovery](84_PAPER_B_R39_FOUNDING_THESIS_RECOVERY_AND_SCOPE_DRIFT.md); [R36 separate higher-order structural conjectures](81_EVONOMOS_R36_HIGHER_ORDER_STRUCTURE_INDEPENDENT_CONJECTURES.md); [v33 lexical-focus predecessor](PAPER_B_BILINGUAL_POSITION_33_20261123.md).

**Boundaries:** No universal architectural principle has been found or proved; no randomized OCP-agent trial is reported here; no causal historical chain from primary authors to current model weights has been established. The contribution offered is a coherent, falsifiable research agenda and a historically motivated question, not a completed empirical discovery.
