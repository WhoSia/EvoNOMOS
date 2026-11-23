# Paper B v24 — When Design Principles Become Rules: Operational Quasi-Axiomatization in AI-Assisted Software Engineering

**Bilingual short position manuscript · 2026-11-22 · DRAFT FOR AUTHOR REVIEW · NOT SUBMITTED.** This version is an argumentative compression of [v23](PAPER_B_BILINGUAL_POSITION_23_20261122.md), not a report of new agent experiments. The full earlier audit and research evidence remain archived in [v22](PAPER_B_BILINGUAL_INTEGRATED_22_20261122.md). Argument frozen in [R12](54_PAPER_B_R12_POSITION_FIRST_EDITORIAL_PRESEAL.md).

# 한국어 원고

## 초록

소프트웨어 설계 원칙은 특정 변경에 대처하기 위한 조언이지만, 코드 검토와 AI 코딩 에이전트의 작업에서는 그 원칙의 이름이 때때로 수정안의 승인 또는 거절을 결정하는 규칙처럼 사용될 수 있다. **우리는 조건부 설계 조언이 실제 요구와 반대 증거를 검토할 기회를 대체하며 구속력을 얻는 현상을 '운영상의 준공리화(operational quasi-axiomatization)'라는 반증 가능한 연구 대상으로 제안한다.** 이 표현은 수학적 공리화 자체를 비판하거나, 현재의 언어모델이 실제로 SOLID를 무조건 따르고 있다고 단정하지 않는다. Meyer와 Martin의 개방–폐쇄 원칙 해석을 검토하면 설계가 무엇에 대해 닫혀 있어야 하는지는 예상하는 변경과 기존 호출자의 의무에 달려 있다. 선행 SOLID 분류 벤치마크를 특정 코드 수정의 수용 판단과 구분하고, 같은 수정안을 서로 다른 요구와 보호 계약 아래 평가하는 제한적 재현 사례를 제시한다. 이어 코딩 에이전트에 주어진 원칙 지시가 설명의 어휘만 바꾸는지, 실제 패치 선택을 바꾸는지, 반대 증거 이후의 판단까지 바꾸는지 시험하는 네 조건 연구를 제안한다. 이 논문의 기여는 준공리화의 발생률을 보고하는 것이 아니라, 설계 원칙이 실제 소프트웨어 변경에 대해 어떤 권위를 행사하는지 경험적으로 묻는 독립적인 문제를 정의하는 데 있다.

## 1. 서론 — 원칙의 이름이 수정안을 거절하는 이유가 되는 순간

어떤 코드에 대해 '개방–폐쇄 원칙(OCP)을 위반했다'는 검토 의견이 나왔다고 하자. 그 의견이 적절한 구조적 특징을 발견했을 수는 있다. 그러나 해당 구조를 수정해야 하는지는 별개의 문제다. 새 요구가 무엇인지, 기존 호출자가 어느 동작에 의존하는지, 수정할 수 있는 소스의 범위가 어디까지인지, 다른 구현이 가능한지에 따라 선택이 달라질 수 있다. 설계 원칙이 설명하는 구조와, 그 원칙을 근거로 특정 패치를 승인하거나 거절하는 일은 동일하지 않다.

이 차이가 중요한 것은 소프트웨어 설계의 조언이 점점 더 코드 생성·검토를 수행하는 도구에도 전달되기 때문이다. 개발자는 원칙을 자신의 판단에 참고할 수도 있지만, 에이전트에게 명시적인 지시로 전달할 수도 있다. 그 결과 원칙은 설명 문장에 머무르지 않고 어떤 파일을 고칠지, 어떤 리팩터링을 요구할지, 어느 대안을 배제할지에 영향을 줄 수 있다. 그러한 영향 자체가 잘못은 아니다. 다만 **원칙의 이름이 그 적용 범위를 입증하는 증거보다 더 큰 결정 권한을 갖게 되는지**는 따로 조사할 필요가 있다.

우리는 이 문제를 '운영상의 준공리화'라고 부른다. 이것은 AI가 실제로 그렇게 행동한다는 확정된 실증 결과가 아니라, 그러한 행동이 있는지 알아보기 위한 연구 가설이다. 이 글은 (1) 역사적 설계 원칙에 원래 존재했던 조건과 예외를 복원하고, (2) 구조적 위반 분류와 특정 수정안의 수용 판단 사이에 필요한 근거를 구별하며, (3) 그 간극에서 AI 에이전트가 어떤 선택을 하는지 반증 가능하게 연구할 방법을 제안한다.

## 2. 역사적 원칙은 무엇에 대해 닫혀 있었는가

객체지향 프로그래밍의 역사와 SOLID의 역사는 동일하지 않다. Simula의 시뮬레이션·클래스, Smalltalk의 객체 메시지, Parnas의 정보 은닉, Liskov와 Wing의 행동적 하위타입은 서로 다른 문제와 평가 기준에서 발전했다. 이들을 다섯 글자 약어가 처음부터 지배했던 단일한 설계 교리로 서술하면, 각각의 구별을 잃는다. [Black 2013](https://arxiv.org/abs/1303.0427), [Parnas 1972](https://doi.org/10.1145/361598.361623), [Liskov & Wing 1994](https://doi.org/10.1145/197320.197383).

Meyer의 초기 개방–폐쇄 설명은 모듈의 확장 가능성과 기존 사용자를 위한 안정된 설명을 함께 다룬다. Martin은 [1996년 OCP 논문](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf)의 도형 그리기 사례에서 새 도형의 지원과 도형 종류별 그리기 순서 변경을 구별했다. 새로운 종류의 도형을 추가하는 데 적합했던 구조가, 이미 정해진 도형의 출력 순서를 바꾸는 요구에는 다른 수정 지점을 필요로 할 수 있다. Martin의 핵심 문제는 모든 변화에 영원히 닫힌 설계를 찾는 일이 아니라 **어떤 변화에 대해 닫힘을 확보할지 선택하는 일**이었다. 따라서 그 원저자를 무조건적인 형식 공리를 주장한 사람으로 취급하는 것은 역사적 근거에 맞지 않는다. [Meyer 1988 독해 기록](./13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md), [Martin 1996 사례 검토](./29_MARTIN_1996_STRATEGIC_CLOSURE.md).

이 역사적 조건성은 과거 원칙이 현재에도 유용할 수 있다는 가능성을 배제하지 않는다. 다만 원칙의 이름만으로 모든 코드 변경을 판정할 수 있다는 근거도 제공하지 않는다. 어떤 변경 분포와 클라이언트 계약 아래에서 그 원칙이 좋은 예측을 하는지는 별도의 문제다.

## 3. 제안 개념 — 운영상 준공리화

'공리'라는 비유에는 세 가지 혼동이 있다. **형식적 공리화**는 명확한 전제와 추론 규칙을 설정하는 정당한 수학적 활동이다. **전문직적 정전화**는 교육·문헌·실무를 거치며 특정 조언이 권위를 얻는 역사적 과정이다. 그와 구별되는 **운영상의 준공리화**는 설계 원칙을 언급한 사실만으로, 실제 수정안을 판단하는 데 필요한 요구·계약·예외·대안의 검토가 생략되거나 밀려나는 행동에 관한 가설이다. 어느 단계에서든 명시적 지시, 조직의 규칙 또는 계약이 원칙의 적용을 정당화한다면 이를 곧바로 부당한 준공리화로 분류해서는 안 된다.

우리는 다음의 더 좁은 문제를 '원칙에서 수정안 판단으로의 전이(principle-to-patch transport)'라고 부른다. 코드 (s)에 어떤 구조적 특징 (L(s))가 있다는 판정만으로 후보 수정안 (p)의 적법성이 결정되지 않는다. 수정안을 받아들일 수 있는지는 적어도 새 요구 (D), 보존할 기존 동작 (C), 허가된 수정 권한 (A)와 실제 후보 (p)에 의해 달라진다.

[
mathrm{Accept}(pmid D,C,A)
eq f(L(s))quad	ext{in general}.
]

이 식은 새 계산법이나 독창적인 불가능성 정리가 아니다. **구조적 라벨만으로 수정안의 승인 결정을 일반적으로 충분히 도출할 수 없다는 문제 제기를 압축한 표기**다. 요구공학, Design by Contract, 문맥적 동등성과 기존 수정 탐색 연구는 이 구별의 중요한 선행 이론이다. 우리가 새롭게 연구하자고 제안하는 것은 AI가 원칙의 언어를 사용할 때 이러한 다른 근거를 어디까지 고려하는지, 그리고 반대 증거가 주어지면 실제 결정을 어떻게 바꾸는지이다.

## 4. 분류 결과와 수정안 판단 사이에 남는 정보

Pehlivan 등(2025)의 [*Are We SOLID Yet?*](https://arxiv.org/abs/2509.03093)은 여러 프로그래밍 언어의 SOLID 위반을 LLM 프롬프트로 분류하는 문제를 다룬다. 이 작업의 목적은 분류 성능을 조사하는 것이며, 개별 코드 수정안의 승인 권한을 실험했다는 뜻이 아니다. 우리가 확보된 자료로 재감사한 OCP 부분에는 48개 제출 코드가 16번씩 나타난 768개 저장 응답 행과 24개의 서로 다른 마스킹된 지시문 틀이 있었다. 이 수는 768개의 독립적인 유지보수 과제를 의미하지 않는다. 저장 프롬프트에는 별도로 기술된 사례별 변경 요구나 보호할 호출자 계약이 없었지만, 코드 자체의 단서까지 전혀 없었다고 단정할 수는 없다. [자료 감사](./18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md).

이 차이를 검토하기 위해 우리는 오래된 도서관 프로그램을 변형한 작은 **연구자 작성 재현 사례**를 사용했다. 한 고정 패치는 기술보고서를 추가하지만 정오표 지원은 제공하지 않고, 기존 책 출력의 접두어를 변경한다. 정오표를 새 요구로 추가하거나 이전 접두어를 기존 호출자 계약으로 보호하면, 같은 패치에 대한 승인 판단이 달라진다. 코드와 패치 자체가 변했기 때문이 아니라 **판정할 명세가 달라졌기 때문**이다. 이는 우리가 지정한 네 조건에서 관찰된 제한적 결과이며 실제 프로젝트에서 이러한 상황이 얼마나 발생하는지 보여 주지 않는다. [재현 조건과 코드](./31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md).

관건은 SOLID 위반을 분류하는 일이 무의미하다는 주장이 아니다. 분류는 검토자가 의심해야 할 위치를 알려 줄 수 있다. 다만 분류 정확도가 곧 특정 패치의 적법한 거절을 의미하지는 않는다. 이 간극을 보고하려면 분류에 사용한 코드와, 실제 수정을 판단할 근거를 별도로 기록해야 한다.

## 5. AI 시대에 무엇을 검증해야 하는가

프로젝트 수준의 지침을 전달하는 통로가 존재한다고 해서 특정 모델이 SOLID를 공리로 학습했다는 결론은 나오지 않는다. 예컨대 Gloaguen 등(2026)은 [저장소 지침 파일이 코딩 에이전트에 미치는 영향](https://arxiv.org/abs/2602.11988)을 조사했지만, 이는 SOLID의 준공리화나 그 훈련 기원을 직접 검증하는 연구가 아니다. 프롬프트, 저장소 규칙, 모델이 생성한 설명, 실제 패치, 사람의 최종 승인은 서로 다른 관찰 단위다.

따라서 우리가 [기존에 제안한 네 조건](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md)—추가 조언 없음(NONE), 강한 SOLID 지시(HARD_SOLID), 범위가 명시된 SOLID 지시(SCOPED_SOLID), 요구·계약 증거 중심 지시(EVIDENCE_CONDITIONAL)—은 동일한 소스 버전·요구·검사·도구 예산 아래에서 비교해야 한다. 결과도 원칙을 언급한 단어 수, 실제 코드 변경, 기존 호출자 계약의 보존, 판단의 수정·기권으로 나누어 평가해야 한다.

여기에는 중요한 반론이 있다. 에이전트가 HARD_SOLID 지시를 따랐다는 사실 자체는 준공리화를 입증하지 않는다. 에이전트는 원칙을 독립적인 진실로 믿는 대신, 방금 받은 명시적 지시에 복종했을 수 있다. 설령 잘못된 패치가 나왔더라도 원인이 지시 충돌인지, 코드 이해 실패인지, 원칙의 부당한 권위 부여인지 구별해야 한다. **일관된 원칙 언급과 반대 증거 이후에도 지속되는 불합리한 수정안 거절은 같은 관측이 아니다.** [식별 문제 상세](./53_PAPER_B_R11_COMPLIANCE_VS_QUASI_AXIOM_IDENTIFICATION.md).

후속 실험에서는 원칙과 요구가 일치하는 과제, 기계적인 적용이 기존 계약과 충돌하는 과제, 필요한 정보가 불충분한 과제를 모두 포함해야 한다. 강한 SOLID 지시가 어떤 과제에서는 성능을 개선할 수 있다는 가능성을 먼저 열어 둬야 한다. 반대로 네 조건이 모두 동일한 올바른 코드를 생성하거나, 설명의 어휘만 달라진다면 준공리화에 대한 행동적 증거는 얻지 못한 것이다. 정당한 반대 증거를 받은 뒤 에이전트가 수정을 재고하는지도 별도로 평가할 수 있지만, 그 근거는 동일한 지시 우선순위와 소스 계약 아래 해석해야 한다.

**이 실험은 아직 실행되지 않았다.** 프롬프트와 결과 기록기, 제한적 원본 Go 실험은 준비돼 있지만 이를 실제 네 조건 에이전트 비교의 결과로 바꾸어 서술해서는 안 된다.

## 6. 논의 — 더 좋은 원칙보다, 원칙의 권위를 검증하는 방법

설계 원칙을 조건부로 다루자는 제안은 이미 오래된 소프트웨어 공학의 직관 및 형식 이론과 연결된다. 이 논문의 주장은 모든 기존 원칙을 폐기하거나, 요구·계약을 처음 발견했다는 것이 아니다. AI가 코드를 생성하거나 검토하는 과정에서 **원칙이 어떤 관찰 가능한 결정 권한을 행사하는지**를 연구의 중심 변수로 삼자는 것이다.

이 질문에는 반대 결과가 존재한다. 충분히 명시된 요구 아래서 엄격한 설계 지침이 더 안정적인 코드를 만들 수 있다. 명시적 지시가 없는 모델은 SOLID를 전혀 적용하지 않을 수 있다. 강한 지시는 코드에는 영향을 주지 않고 설명에만 남을 수 있다. 이러한 결과를 허용하지 않는 연구라면 '준공리화'라는 표현 자체가 또 다른 검증되지 않은 교리가 되고 만다.

소프트웨어 공학이 앞으로 필요로 하는 것은 원칙을 따르는 모델이나 원칙을 반대하는 모델이라는 이분법보다, **원칙의 적용을 정당화하는 요구·계약·반대 증거를 확인하고 그에 따라 결정을 바꿀 수 있는 모델**인지 묻는 연구다. 이러한 문제를 정의하는 것이 Paper B의 기여다. 특정 아키텍처의 비용 우위, 장기적 조직 성과와 새 설계 법칙의 형식 증명은 EvoNOMOS의 후속 연구에서 별도로 검증할 수 있다.

## 7. 결론

SOLID 같은 설계 원칙의 가치는 모든 수정에 적용되는 규칙이라는 데 있지 않을 수 있다. 오히려 어떤 변화에서 유용하고 어떤 계약 앞에서 수정되어야 하는지를 설명할 수 있을 때 그 조언은 더 신뢰할 만해진다. 우리는 AI 코딩 에이전트 시대에 설계 원칙이 설명에서 실제 선택으로 넘어가는 순간을 독립적인 실증 연구 대상으로 제안했다. **원칙의 이름이 아니라, 그 이름에 부여된 결정 권한과 반대 증거 이후의 행동을 연구하자.**

---

# English manuscript

## Abstract

Software design principles offer guidance about how a system might accommodate change. In code review and AI-assisted development, however, a principle's name may acquire the force of a rule for accepting, rejecting, or reshaping an individual patch. We propose **operational quasi-axiomatization** as a falsifiable research target: the possibility that conditional design advice comes to displace examination of actual requirements, protected client behavior, exceptions, and available repairs. This is neither a critique of mathematical axiomatization nor an empirical claim that current coding agents already treat SOLID as an unconditional truth. Early accounts of the Open–Closed Principle made extensibility relative to anticipated change and stable client obligations. We distinguish a structural-violation classification from the decision whether a particular repair is acceptable, illustrate that distinction with one explicitly constructed, fixed-patch contract example, and outline controlled coding-agent experiments comparing strict, scoped, evidence-conditional, and absent SOLID guidance. The empirical target is not the frequency of SOLID vocabulary but the authority that principle language exercises over source changes and the way decisions respond to counterevidence. We offer a position and research agenda, not an estimate of agent behavior.

## 1. Introduction: when advice decides an edit

Suppose a reviewer states that a module violates the Open–Closed Principle (OCP). The statement may correctly identify a design pattern. It does not, by itself, establish which future change is required, which existing clients must continue working, which source files can be edited, or whether a different repair is available. The same pattern may be a useful warning in one maintenance task and irrelevant to the acceptance of a particular patch in another. Recognizing a principle-related structure and using that recognition to dispose of a concrete patch are distinct acts.

This distinction matters as software design advice enters coding-agent workflows. A human may consider a principle among several reasons; an agent may receive it as an explicit project instruction or task-specific constraint. The instruction can then influence the code it writes and the alternatives it rejects. Such influence may be useful and fully authorized. The empirical question is whether a principle's *name* is sometimes given decision authority beyond the scope and evidence that justify its use.

We call the possibility **operational quasi-axiomatization**. We do not presume that it is prevalent, that a foundation model internally believes in SOLID, or that an original designer intended to state universal mathematical axioms. We argue for a falsifiable research problem linking historical design advice, patch-specific authority, and the observable behavior of coding agents.

## 2. Closure was already relative to change

The histories of object orientation and SOLID should not be collapsed into one continuous five-rule doctrine. Simula's class-based simulation, Smalltalk's message-oriented accounts, Parnas's information-hiding criterion, and Liskov and Wing's behavioral subtyping addressed different design questions. Their differences matter because they associate software quality with distinct observations and changes rather than a single syntactic label. [Black 2013](https://arxiv.org/abs/1303.0427); [Parnas 1972](https://doi.org/10.1145/361598.361623); [Liskov and Wing 1994](https://doi.org/10.1145/197320.197383).

Meyer's account of open and closed modules joins extension with the stability of descriptions used by clients. Martin's [1996 discussion of OCP](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf) then makes strategic closure explicit. A drawing routine may accommodate another kind of shape without revision while a request to change the ordering of shapes may require a different locus of modification. Which change should be cheap is an engineering choice, not a universal property conferred by the OCP label. It would mischaracterize Martin to claim that he formally established five unconditional design axioms. [Meyer passage audit](./13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md); [Martin's strategic-closure example](./29_MARTIN_1996_STRATEGIC_CLOSURE.md).

Historical advice can remain useful in modern development without being beyond revision. The question is which requirements and future changes justify its authority.

## 3. The proposed phenomenon

Three ideas must be separated. **Formal axiomatization** specifies premises and inference rules, which can be legitimate and precise. **Professional canonization** describes a historical process in which repeated advice becomes widely authoritative. **Operational quasi-axiomatization** concerns a narrower, potentially observable event: the use of a design principle as a decisive constraint in an actual modification despite relevant evidence that its purported authority is inapplicable or unsettled. The latter is not established merely because an agent uses imperative language or follows an explicitly authorized instruction.

We call the narrower inference step the **principle-to-patch transport problem**. A structural label (L(s)) for source (s) does not generally determine whether a patch (p) should be accepted. Acceptance depends on a specified demand (D), existing client obligations (C), edit authority (A), and the particular candidate. Symbolically, (mathrm{Accept}(pmid D,C,A)) cannot in general be recovered from (L(s)) alone. This is an explanatory notation, not a newly proven undecidability theorem. Requirements engineering, Design by Contract, contextual equivalence, and source-aware repair all provide relevant prior theory. Our proposed contribution is to turn the *operational authority* exercised by principle language into a direct research question for AI-assisted development.

## 4. What current evidence does—and does not—show

[Pehlivan et al. (2025), *Are We SOLID Yet?*](https://arxiv.org/abs/2509.03093), studies prompting LLMs to identify SOLID violations across languages. Such classification is not itself a test of whether a particular patch should be accepted or rejected. In our prior inspection of its OCP archive, 48 submitted code examples occurred across 768 stored response rows, with 24 distinguishable masked prompt scaffolds. These are not 768 independent maintenance tasks. Item-specific protected client contracts or change demands were not separately stated in the saved prompt templates; code-internal clues may nonetheless remain. [Archive receipt](./18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md).

To expose the difference we constructed a small library-patch example. A fixed proposed addition supports technical reports but omits errata and changes an older book prefix. Varying whether errata are required and whether the older prefix is contractually protected changes whether that *same patch* is admissible under the authored specification. The difference is in the requirements against which the patch is evaluated, not an observed industrial reviewer or coding agent. [Constructed witness](./31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md).

This example does not make structural classifiers useless. A classifier may correctly direct attention to code that deserves scrutiny. Our point is that an individual maintenance decision also requires traceable grounds for the scope of the request, client protections, edit authority, and alternatives.

## 5. Making apparent authority testable

Repository instructions are a real delivery channel for coding agents, but their availability says nothing by itself about the contents of model pretraining. For example, [Gloaguen et al. (2026)](https://arxiv.org/abs/2602.11988) examine repository-level context files and coding-agent task performance; they do not directly measure SOLID-induced patch rejection or prove a training-origin mechanism. Prompts, source context, model explanations, generated patches, tests, and final review decisions must be measured separately.

Our inherited [four-treatment design](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md) compares NONE, HARD_SOLID, SCOPED_SOLID, and EVIDENCE_CONDITIONAL advice on the same pinned source, task, tests, rights and tool budget. Outcomes would distinguish code correctness and preserved clients from the language used to justify the patch; they would also record revision or abstention after independently sourced contrary evidence.

A serious identification objection arises here. An agent that follows HARD_SOLID may simply be obeying the experiment's instruction, rather than treating SOLID as an independent truth. Even a bad patch may result from conflicts between instructions, weak source comprehension, or incomplete tests. We therefore propose examining tasks where principle-aligned design is valid, tasks where a mechanical refactoring would break a protected obligation, and cases where the available evidence does not warrant a disposition. A conforming hard-rule implementation may win in the first stratum; models may tie throughout; words may change without changes to source. All of these are legitimate rival outcomes. Subsequent factual rebuttals can test responsiveness, but must be interpreted under the actual instruction hierarchy rather than treated as direct access to internal beliefs. [Identification analysis](./53_PAPER_B_R11_COMPLIANCE_VS_QUASI_AXIOM_IDENTIFICATION.md).

No independent four-arm coding-agent execution has yet been performed. The proposed study can estimate certain **effects of present instructions** if implemented with valid randomization and evaluation. It cannot, without further evidence, identify the causal influence of hidden pretraining examples or the long-run historical process of professional canonization.

## 6. Discussion: an empirical question, not a new commandment

Arguing that design advice should remain revisable is compatible with established software engineering theory; we do not claim to have invented contracts, exceptions, or contextual judgment. Nor do we recommend discarding SOLID. We instead ask that the authority principle language exercises in a coding workflow be an explicit empirical variable. Its outcomes include justified adherence, unjustified insistence, evidence-responsive revision, ordinary instruction compliance, lexical repetition, and abstention when obligations are unknown.

This framing allows the hypothesis to fail. Strict guidance might improve maintenance outcomes in some contexts. Agents may generate equally good patches under all conditions. A supposed principle effect may disappear once a source-aware classical planning baseline is given the same information. Such results constrain the phenomenon rather than threaten the legitimacy of its investigation.

What matters is not whether a coding agent can recite a principle but whether its actual choices reflect the requirements, client contracts, and counterexamples that bear on the decision. Source-level architectural reversal and maintenance cost can be investigated in separate EvoNOMOS studies; they need not be claimed by this position paper.

## 7. Conclusion

A design principle earns practical authority when its use can be justified for the changes and obligations at hand, not merely through repetition of its name. We propose operational quasi-axiomatization as a falsifiable question about when AI-assisted software decisions elevate conditional advice into binding action. The immediate research opportunity is to observe **what the principle changes in a patch, and what credible counterevidence changes in the agent's decision**. This is the proposed object of study, not an already demonstrated fact.

---

## Evidence and citation notes (for author, not manuscript text)

- The archival OCP counts, library reconstruction and original Go witnesses are prior EvoNOMOS work; none is an observed four-arm agent-effect estimate.
- Exact bibliographic formatting, original pagination and quotations should be checked against canonical held PDFs before submission. The above text primarily paraphrases ideas and cites the recorded source chain.
- F37's app-owned router negative control established equal capability for a bounded reserved-route wrapper; including its full details here would distract from the single central thesis. Keep in v22/v23 or supporting archive.
- The earlier formal discussion of principle-to-patch inference has requirements-engineering precedents; do not claim first invention of that distinction.
- A null result in the future experiment is compatible with the paper's status as a proposal for a falsifiable research target.
