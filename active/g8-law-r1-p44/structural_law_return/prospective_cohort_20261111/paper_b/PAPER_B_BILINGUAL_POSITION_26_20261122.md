# Paper B v26 — When Design Advice Becomes an Unquestioned Rule: A Research Agenda for AI-Assisted Software Engineering

**Bilingual position-paper working manuscript · 2026-11-22 · NOT SUBMITTED.** Short invitation-first replacement draft. Previous [v25](PAPER_B_BILINGUAL_POSITION_25_20261122.md), v24, v23 and v22 retained. Scientific positioning recorded in [R14](56_PAPER_B_R14_IDEA_INVITATION_AND_PRIOR_ART_BOUNDARY.md). This paper poses a question; it does not report agent-treatment results, a new theorem, or observed energy savings.

# 한국어 원고

## 초록

소프트웨어 설계 원칙은 좋은 코드를 만드는 데 유용한 판단 기준이지만, 그 원칙이 언제까지 유효한지까지 자동으로 알려 주지는 않는다. 특히 AI 코딩 에이전트가 SOLID나 디자인 패턴을 설명할 뿐 아니라 실제 코드의 수정 방향을 선택하는 상황에서는, 역사적으로 조건부였던 조언이 마치 지켜야 할 규칙처럼 작동할 가능성을 다시 검토할 필요가 있다. 우리는 이를 **설계 원칙의 운영상 준공리화(operational quasi-axiomatization)**라는 연구 질문으로 제안한다. 핵심은 AI가 SOLID를 얼마나 자주 언급하는지가 아니라, 그 원칙이 요구사항과 기존 호출자 계약을 고려한 실제 패치 판단에 어떤 권위를 행사하며, 반대 증거가 나타났을 때 판단이 수정되는가이다. Meyer와 Martin의 개방–폐쇄 원칙 논의, SOLID 위반 분류 연구, 고정된 패치의 조건부 수용 사례를 통해 질문의 범위를 정한다. 이어 코딩 에이전트 지시 조건, 유지보수 요구, 계약 증거 및 결정 수정 행동을 구별하는 후속 연구를 제안한다. **우리는 준공리화가 이미 널리 발생한다고 주장하거나 새로운 보편 설계 법칙을 제시하지 않는다.** 목적은 기존 설계 원칙의 적용 범위와 AI 시대의 의사결정을 함께 연구할 수 있는, 반증 가능한 문제를 제안하는 것이다.

## 1. 설계 원칙을 따르는 것과 좋은 수정을 하는 것은 같은 일인가

어떤 프로그램을 확장해야 하는 개발자가 있다고 하자. 새 기능을 추가할 때마다 기존 코드를 고치는 구조는 개방–폐쇄 원칙에 어긋난다고 배웠을 수 있다. 개발자는 이를 바탕으로 인터페이스를 추가하거나 객체를 분리하는 선택을 한다. 그런데 실제 요구는 기존 코드 몇 줄의 단순한 수정으로 해결되고, 도입한 추상화는 지금도 이후에도 사용되지 않는다면 어떨까? 반대로 애초에 변동이 많은 기능을 인터페이스 뒤에 격리한 덕분에 반복 변경을 안전하게 처리한다면 어떨까? 두 사례 모두 가능하다. **설계 원칙에 이름이 붙어 있다는 사실만으로 특정 수정안의 품질은 결정되지 않는다.**

이 긴장은 AI 코딩 에이전트를 만나 새로운 형태로 드러난다. 사람이 원칙을 참조하는 것뿐 아니라, 도구에 원칙을 강한 지침으로 주입하고 그 도구가 코드와 검토 의견을 생성할 수 있기 때문이다. 이때 우리는 다음을 구별해야 한다. 에이전트가 원칙을 말하는가? 원칙에 맞는 코드를 생성하는가? 더 중요한 요구나 기존 계약과 충돌하면 다른 방법을 선택하는가? 충돌이 있을 때 기존 판단을 정당하게 수정하는가?

우리의 제안은 SOLID를 폐기하거나 다른 다섯 가지 원칙을 대신 만들자는 것이 아니다. **원칙의 실제 결정 권한을 독립적으로 연구하자**는 것이다. 이 질문은 올바른 원칙이 어떤 환경에서 유용한지, 다른 구조가 더 적합한 조건은 무엇인지에 관한 미래 연구로 이어질 수 있다.

## 2. 조건을 지닌 원칙이 보편 규칙으로 읽히는 경로

객체지향의 역사는 한 개의 만능 설계 표준이 탄생한 역사가 아니다. Simula의 클래스와 시뮬레이션, Smalltalk의 메시지, Parnas의 정보 은닉, Liskov와 Wing의 행동적 하위타입은 서로 다른 기술적 질문에 답했다. 이 차이를 무시하고 객체지향과 SOLID를 하나의 동일한 명령 체계로 취급하면, 설계를 평가할 때 필요한 전제를 놓치기 쉽다. [Black 2013](https://arxiv.org/abs/1303.0427); [Parnas 1972](https://doi.org/10.1145/361598.361623); [Liskov and Wing 1994](https://doi.org/10.1145/197320.197383).

Meyer의 개방–폐쇄 설명은 확장성과 기존 이용자의 안정된 설명을 결부했다. Martin의 [1996년 OCP 논문](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf)은 어떤 변경을 예상하는지에 따라 닫혀 있어야 할 부분이 달라짐을 구체적인 도형 사례로 설명한다. 새 도형의 도입과 출력 순서의 변경은 같은 종류의 수정이 아니다. 이 역사적 기록을 통해 확인되는 것은 원저자가 모든 미래 변경에 관해 유일한 구조를 보장했다는 사실이 아니라, **어떤 변화에 대비할 것인지 선택해야 한다는 조건성**이다. [Meyer 원전 대조](./13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md).

그렇다면 문제의 중심은 “원저자가 잘못된 공리를 주장했는가”가 아니다. 특정 상황에 맞는 조언이 교육, 코드 검토, 저장소 지침, 에이전트 프롬프트를 거치는 동안 적용 조건이 생략될 수 있는가이다. 이 가능성을 설명하는 용어로 우리는 *운영상의 준공리화*를 제안한다. **형식적 공리화**는 수학적 전제 설정이고, **전문직적 정전화**는 사회·역사적 권위 형성이다. 여기서 제안하는 **운영상의 준공리화**는 실제 수정 결정에서 원칙이 요구·계약·예외의 증거보다 우선하는지에 관한 행동적 가설이다. 세 현상을 혼동해서는 안 된다.

## 3. 무엇을 실제로 관찰해야 하는가

이 문제는 우선 SOLID **분류**와 패치 **판정**을 분리할 때 선명해진다. [Pehlivan 등(2025)](https://arxiv.org/abs/2509.03093)의 *Are We SOLID Yet?*은 언어모델이 코드의 SOLID 위반을 식별할 수 있는지 조사했다. 하지만 “구조에 위반이 있는가”와 “지금 이 패치를 병합할 것인가”는 별개 질문이다. 후자에는 해결할 요구, 보호할 기존 호출자 동작, 허용된 수정 권한, 실제 후보와 대안이 필요하다. 이는 요구공학과 계약 기반 설계의 기존 전통을 대체하는 발견이 아니라, **원칙 이름이 수정 결정에 전달되는 단계**를 별도의 AI 연구 대상으로 만들자는 제안이다.

이를 보여 주는 제한적인 사례가 있다. 우리가 작성한 도서관 패치는 기술보고서를 추가하지만 정오표를 지원하지 않고, 기존 책 출력의 접두어를 바꾼다. 정오표 지원이 필수인지, 기존 접두어의 보존이 계약에 포함되는지를 바꾸면 **같은 패치**에 대한 승인 결과가 달라진다. 이 결과는 연구자가 정의한 요구와 계약에 대한 실행 가능성 검산이다. 실제 에이전트가 SOLID 때문에 패치를 잘못 거절했다는 결과가 아니다. [고정 패치 재현](./31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md).

코드 언어와 패러다임도 문제의 범위를 드러낸다. Go의 함수 값·콜백과 인터페이스를 통한 확장은 서로 다른 구현 선택이지만, 하나의 OCP 라벨이 어느 쪽의 특정 수정을 반드시 거절해야 한다고 자동 판정해 주지 않는다. Go는 순수 함수형 언어가 아니며, 이 예시는 특정 패러다임의 성능 우위를 입증하려는 비교가 아니다. [Go 명세](https://go.dev/ref/spec); [별도 비교 메모](./55_PAPER_B_R13_PARADIGM_TRANSFER_AND_CALLBACK_NEGATIVE_CONTROL.md).

## 4. AI 시대의 네 가지 경쟁 설명

이 질문을 구체적인 연구 의제로 만들기 위해 우리는 기존에 작성한 네 가지 지시 조건을 활용할 수 있다. **NONE**은 추가적인 설계 조언을 주지 않는다. **HARD_SOLID**는 원칙을 강하게 지시한다. **SCOPED_SOLID**는 변경 범위에 맞춰 적용한다. **EVIDENCE_CONDITIONAL**은 요구·계약·대안의 증거를 기준으로 판단한다. 실제 실험에서는 모든 조건에 동일한 소스, 수정 과제, 기존 클라이언트 계약과 검사 환경을 제공해야 한다. [원래의 P35-B1 제안](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md).

이 비교에서 가능한 결과는 하나가 아니다. 강한 지시가 정당한 리팩터링을 개선할 수 있다. 네 조건의 패치가 완전히 같고 설명만 달라질 수 있다. 기존 테스트와 요구사항이 설계 지시의 효과를 압도할 수도 있다. 엄격한 지시가 부적절한 추상화를 유도할 수도 있다. **그 어느 것도 관찰하기 전에 승자로 정해서는 안 된다.**

여기에 가장 중요한 식별 문제가 있다. 에이전트가 HARD_SOLID를 따르는 이유는 SOLID를 무오류의 공리로 받아들여서가 아니라 **방금 받은 유효한 지시를 따르기 때문**일 수 있다. 따라서 강한 지시의 채택률을 곧바로 준공리화로 해석해서는 안 된다. 계약과 소스에서 확인한 반대 증거가 주어졌을 때 에이전트가 어떻게 대응하는지, 그 증거가 실제 지시 우선순위에서 얼마나 구속력이 있는지, 대안의 적법성을 독립적으로 검증할 수 있는지를 함께 조사해야 한다. 설명에서 SOLID를 더 많이 언급하는 현상과 소스 패치가 달라지는 현상도 구별해야 한다.

실제 네 조건 코딩 에이전트 비교는 **아직 실행되지 않았다**. 이 논문이 제시하는 것은 측정값이 아니라, 그 측정으로 무엇을 구별할 수 있고 구별할 수 없는지에 관한 연구 의제다.

## 5. 다른 연구자들에게 제안하는 연구 문제

**첫째, 원칙의 권위가 문헌과 지침에서 어떻게 표현되는가?** 역사적 원전과 현대 저장소 지침을 비교해 조건, 예외, 강제 표현의 유무를 분류할 수 있다. 서로 다른 시대의 문헌 표현을 비교하는 것만으로 AI가 권위를 강화했다는 인과 결론을 낼 수는 없다.

**둘째, 원칙의 언어가 실제 패치를 바꾸는가?** 동일한 변경 요구에 대한 서로 다른 지시 조건의 패치를 비교하고, 올바른 수정을 도왔는지, 불필요한 추상화를 만들었는지, 기존 클라이언트 계약을 보존했는지 측정할 수 있다. [Pehlivan 등의 SOLID 분류 연구](https://arxiv.org/abs/2509.03093)와 [Gloaguen 등의 AGENTS.md 지침 연구](https://arxiv.org/abs/2602.11988)는 각기 관련된 선행 출발점이지만, 이 질문의 특정 조건부 패치 판정을 그대로 해결하지는 않는다.

**셋째, 반대 증거 이후 판단을 바꾸는가?** 신뢰할 수 있는 계약과 기존 호출자 테스트를 제시한 뒤 판단 변경·보류·지시 충돌 보고를 서로 다르게 평가할 수 있다. [2026년 Google Research 연구](https://research.google/pubs/from-correctness-to-collaboration-a-human-centered-taxonomy-of-ai-agent-behavior-in-software-engineering/)처럼 개발자 지침과 바람직한 에이전트 행동을 분류한 연구가 이미 존재하므로, *우리가 최초로 에이전트 규칙을 연구한다*는 주장은 성립하지 않는다. 우리의 초점은 **설계 원칙의 권위가 개별 수정 판단에서 어떻게 작동하는가**에 있다.

**넷째, 이러한 원칙의 적용이 후속 유지보수 비용에 어떤 영향을 미치는가?** 수정 파일 수, 전체 에이전트 토큰 사용량, 오류, 시간, 에너지 등을 별도 변수로 측정할 수 있다. 원칙을 지켜 파일 수정이 줄었다는 사실만으로 토큰과 에너지가 줄었다고 추론해서는 안 된다. 특히 AI 개발의 총비용은 초기 추상화 비용과 반복된 변경 요구를 함께 고려해야 한다. 이 문제는 Paper B의 성과가 아니라 후속 연구를 위한 열린 질문이다.

## 6. 우리가 틀렸다고 판단해야 하는 경우

후속 실험에서 대다수 과제에 원칙에 따른 부당한 거절이 발견되지 않거나, 원칙 지시가 실제 코드가 아니라 설명의 어휘에만 영향을 주거나, 강한 원칙 지시가 검증된 계약 보존을 일관되게 개선할 수도 있다. 어느 결과든 연구자가 공개한 가설의 범위를 수정해야 한다. 기존 요구공학이나 강한 소스 인지 기준선이 동일한 현상을 충분히 설명할 수 있다면 새로운 기제를 발견했다고 주장할 수 없다. 따라서 이 논문은 SOLID의 폐기 선언도, 운영상 준공리화의 존재 증명도 아니다.

우리의 초대는 한정적이지만 분명하다. **코드를 검사하는 도구가 원칙의 이름을 아는 것과, 언제 그 원칙을 수정 결정에 적용해야 하는지를 아는 것은 같은 능력인가?** 이 차이를 역사·코드·계약·에이전트 행동의 독립된 증거로 조사하자는 것이다.

## 7. 결론

지난 수십 년간의 소프트웨어 설계 원칙은 변화에 대응하기 위한 언어를 제공했다. 이제 그 언어 자체가 AI 개발 도구의 판단을 어떻게 구속하는지 시험할 이유가 생겼다. 우리는 **운영상의 준공리화**를 특정 버그나 새 수학 법칙이 아니라, 설계 조언이 실제 수정안을 결정하는 데 행사하는 권위를 분석하기 위한 반증 가능한 연구 대상으로 제안한다. 이 질문을 함께 검증하는 연구자들이 늘어난다면, 그 결과가 원칙의 정당성을 뒷받침하든 그 적용 범위를 좁히든 소프트웨어 공학에 유익할 것이다.

---

# English manuscript

## Abstract

Software design principles help developers reason about change, but they do not by themselves specify the circumstances under which their advice should be binding. As AI coding agents move from describing designs to selecting and reviewing actual patches, historically conditional guidance may acquire the force of a seemingly unquestionable rule. We propose **operational quasi-axiomatization** as a falsifiable research question: when, if ever, does a named design principle displace task requirements, protected client contracts, or relevant counterevidence in AI-mediated software decisions? This is not a claim that contemporary agents already exhibit such behavior or that a superior universal design law has been found. We distinguish structural labels from patch dispositions, ground the question in earlier accounts of strategic closure and bounded contract examples, and propose a research agenda spanning historical documents, coding-agent interventions, evidence-responsive revision and downstream maintenance costs. The intended contribution is to invite empirical investigation of the authority software design principles exercise in actual engineering decisions, not to report an already measured effect.

## 1. Does following a principle mean making a good change?

Suppose a developer is asked to add a capability to a mature application. A familiar rule of thumb says that software should be open to extension while remaining closed to modification. The developer may add an interface or split a class to make the new capability fit that principle. In one project, the abstraction protects a frequently changing boundary and prevents regressions. In another, the requirement could have been met by a small authorized change and the abstraction is never used again. Both are plausible. The mere naming of a principle does not decide which edit is better for the actual maintenance demand.

This ambiguity takes on a new form when design advice is supplied directly to coding agents. An agent may not merely repeat the advice in prose; it may select files, construct interfaces, generate patches or reject alternatives. Those actions may be useful or fully justified by a local project policy. The research question is narrower: **when does the language of a historically conditional principle receive authority that exceeds its evidential or contractual scope?**

We propose to study this possibility under the name *operational quasi-axiomatization*. The point is not to replace SOLID with another mnemonic, to diagnose universal irrationality in current models or to declare an established design style obsolete. It is to separate the act of recognizing design advice from the authority that advice actually exercises over a patch.

## 2. Conditional guidance has a history

There is no reason to treat object orientation as a single continuous five-principle doctrine. Simula, Smalltalk, Parnas's information-hiding criterion and Liskov–Wing behavioral subtyping addressed materially different design questions. [Black 2013](https://arxiv.org/abs/1303.0427); [Parnas 1972](https://doi.org/10.1145/361598.361623); [Liskov and Wing 1994](https://doi.org/10.1145/197320.197383).

Meyer's open–closed account associates extensibility with descriptions on which existing clients may rely. [Martin's 1996 discussion](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf) explicitly emphasizes *strategic closure*: adding a new shape and changing the order in which shapes are drawn are different anticipated changes. A design optimized for one need not be equally suitable for the other. These historical sources do not support a caricature in which the original authors mathematically asserted five unconditional axioms. [Meyer source audit](./13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md).

The question is therefore not whether the first authors mistakenly derived immutable axioms. It is whether advice that originated with identifiable conditions can lose those conditions as it passes through instruction files, code-review rubrics and agent prompts. **Mathematical axiomatization**, **professional canonization** and **operational quasi-axiomatization** name different objects. We use the last term only for a hypothesized observable decision process, not for claims about what a model internally believes or has encountered in training.

## 3. From labeling code to judging a change

A structural label and a patch disposition require different evidence. [Pehlivan et al.'s 2025 *Are We SOLID Yet?*](https://arxiv.org/abs/2509.03093) addresses whether LLM prompts can detect SOLID violations across languages. Detecting a pattern does not independently establish that a particular edit should be approved or rejected. That decision also calls for the requested change, existing client commitments, authorized edits and feasible alternatives. Requirements engineering and Design by Contract already study these obligations. Our proposed target is the narrower **transition of design-principle language into operative patch authority** in AI development.

We illustrate the distinction with a bounded, author-constructed library modification: the same patch adds technical-report handling, does not handle errata, and changes an older book prefix. When the stipulated requirements and protected old-client behavior change, the patch's acceptability changes. The example is a witness about the logical insufficiency of a structural label, not evidence that an industrial reviewer or coding agent has rejected a real patch because of SOLID. [Constructed case](./31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md).

The phenomenon does not presuppose a class-based implementation. In Go, methods and interfaces can coexist with function-valued callbacks. Neither the use of classes nor the use of callbacks determines whether an actual extension meets its obligations; Go is not a purely functional language. We do not claim that one paradigm has a general cost advantage. [Go language specification](https://go.dev/ref/spec).

## 4. What would distinguish the competing explanations?

An earlier prospective study design compares four advice conditions: **NONE**, **HARD_SOLID**, **SCOPED_SOLID** and **EVIDENCE_CONDITIONAL**, under the same pinned source, client contracts, tasks, evaluator and tool budget. [Original protocol](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md). The design is prospective; no independent four-arm agent trial has been completed.

The possible outcomes are not limited to one favored theory. Strict advice may improve correct repairs. All conditions may yield identical code while explanations differ. Tests and explicit requirements may dominate prompt style. Strict design language may encourage an unnecessary abstraction or an unacceptable edit. A useful experiment has to preserve all of these possibilities, including null effects and reversals.

Most importantly, compliance with an explicit HARD_SOLID instruction is not direct evidence of quasi-axiomatization. An agent may be correctly following authorized policy. A failure to revise after receiving contrary evidence likewise needs interpretation under the actual instruction hierarchy, authenticated source contract and available legal alternatives. Even a randomized wording experiment can identify *effects of present instructions* without identifying either internal belief or pretraining origin. The target is observable, source-grounded patch disposition and evidence-responsive revision, not the number of times an agent writes “SOLID.” [Identification critique](./53_PAPER_B_R11_COMPLIANCE_VS_QUASI_AXIOM_IDENTIFICATION.md).

## 5. Four invitations to further research

**Historical and documentary inquiry:** Under what conditions are exceptions and scopes preserved or omitted when design advice enters teaching materials, project rules and agent prompts? Document shifts without inferring that AI caused them from a time trend alone.

**Agent behavior and patch adjudication:** Does advice wording change actual source repairs and contract preservation beyond explanatory vocabulary? Compare fixed tasks and independent source-aware alternatives, including cases in which strict guidance is legitimately helpful.

**Revision under counterevidence:** When given authenticated client requirements and failing compatibility cases, do agents change their decisions, abstain or flag instruction conflicts? What role does legitimate instruction priority play? The [Google Research 2026 taxonomy of coding-agent behavior](https://research.google/pubs/from-correctness-to-collaboration-a-human-centered-taxonomy-of-ai-agent-behavior-in-software-engineering/) already studies human-desired agent rules; our narrower interest is the use of **named design principles to dispose of particular code changes**.

**Downstream software and resource cost:** Across actual sequences of maintenance requests, do principles or alternative architectures alter patch sizes, repeated source-reading, token counts, regressions or energy cost? Initial abstraction cost and repeated repair cost must be measured together; fewer edited files does not prove lower token or energy use. This is a separate proposed study, not a present result.

These projects can be pursued independently. A historical researcher need not first build a Go agent benchmark, and an empirical coding-agent researcher need not discover a new general mathematical law. Their results can eventually inform one another.

## 6. What would defeat the hypothesis?

If source-comparable agents normally revise unjustified principle-based choices after credible evidence, the proposed failure mode may be rare or absent in those settings. If strict instruction only changes vocabulary or consistently improves contract correctness, the purported authority problem lacks the expected support there. If established requirements traceability and source-aware conventional baselines fully explain the observed behavior, no novel causal mechanism is identified. Each outcome would refine the research program, and none can be erased by renaming failure as a new kind of quasi-axiomatization.

Our invitation is deliberately modest: **does knowing a design principle entail knowing when it should govern a particular patch?** We propose studying the distance between those two abilities across historical evidence, real source tasks and controlled coding-agent behavior.

## 7. Conclusion

Software design principles have supplied a language for handling change. The emergence of agents that can turn that language into concrete edits makes its operative authority worth studying in its own right. We propose operational quasi-axiomatization as a falsifiable question about when revisable advice becomes binding in AI-assisted engineering. Researchers may find that the effect is substantial, negligible, legitimately beneficial or already explained by existing theories. The contribution of this paper is to define that shared question and invite the evidence required to answer it.

---

## Author's evidence ledger (not for publication)
- Historical early-origin conversations establish project provenance, not global scholarly precedence.
- The Pehlivan OCP archive counts 48 submitted examples / 768 responses / 24 masked templates in a prior direct repository audit (v25); the deliberately shorter invitation text does not need a statistics paragraph.
- External Google Research 2026 taxonomy was inspected through the public abstract/publisher description; no full-text claim or precise empirical effect is made.
- No actual four-arm agent intervention, no law theorem, no token or energy reduction measurement.
- No Lean proof is needed to publish the question; stronger future generality claims require separate evidence.
