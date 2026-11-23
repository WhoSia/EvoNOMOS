# Paper B v23 — From Design Principles to Apparent Axioms in AI-Assisted Software Engineering

**Genre:** historical-critical position / research agenda, bilingual working manuscript. **Status:** not submitted; proposed agent effects unobserved; no universal theorem claimed. Previous full [v22](./PAPER_B_BILINGUAL_INTEGRATED_22_20261122.md) preserved with its audit appendices. This edition compresses rather than silently replacing prior research evidence.

## 한국어 원고

### 초록

SOLID는 설계 *원칙*인데, AI 코딩 에이전트나 코드 검토에서는 언제 그 원칙이 마치 따라야 할 *규칙* 또는 *공리*처럼 작동하게 되는가? 이 질문은 2026년 7월 29일 EvoNOMOS의 초기 연구 대화에서 제기됐다. 우리는 설계 조언에 반증 가능성과 적용 범위를 확인하지 않은 채 개별 수정안의 승인·거절을 결정할 권한을 부여하는 현상을 **운영상의 준공리화(operational quasi-axiomatization)**라는 연구 가설로 제안한다. 수리논리학에서 공리화 자체를 비판하는 것은 아니다. 역사적 원문과 SOLID 분류 벤치마크를 검토하고, 동일한 수정안의 승인 기준을 바꾸는 작은 실행 사례 및 실제 Go 라우터 이슈에서 요구와 우회책의 차이를 확인했다. 이 자료는 실제 코딩 에이전트가 준공리화된 행동을 보인 비율이나 그 인과 메커니즘을 측정하지 않는다. 우리는 네 가지 지시 조건—추가 지시 없음, 강제 SOLID, 조건부 SOLID, 요구·계약 근거 중심—을 동일한 Go 변경 과제에서 비교하는 후속 실험을 제안한다. 설계 원칙을 제거하기보다, 원칙의 이름과 실행 가능한 근거 사이의 간극을 별도 연구 대상으로 만들자는 것이 목적이다.

### 1. 서론: 원칙이 행위의 기준이 될 때

소프트웨어 개발자는 ‘개방–폐쇄 원칙을 위반했다’는 의견을 받을 수 있다. 그 의견은 특정 의존 방향이나 분기 구조를 잘 설명할 수 있지만, 그 자체만으로 어느 변경 요구를 충족해야 하며 어떤 기존 호출자를 보호해야 하는지 알려 주지는 않는다. 수정이 필요할 수도 있고, 원칙으로 기술된 패턴이 실제 요구에 잘 맞을 수도 있다. 우리는 원칙을 항상 채택하거나 항상 반박하는 태도보다 **원칙에 부여된 결론의 권한**을 구별하고자 한다.

[2026년 7월 29일 원본 대화](https://drive.google.com/file/d/1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er/view)는 원칙과 강제 규칙을 구별하면서 Codex·Claude Code와 같은 코딩 도구가 SOLID를 공리처럼 취급할 가능성을 문제 삼았다. [2026년 10월 9일 Paper B 초기 가설](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_SOLID_OBJECT_ORIENTATION_AND_AI_QUASI_AXIOMATIZATION_PAPER_B.md)은 이를 *operational quasi-axiomatization*으로 명명하고 최초 네 조건 실험을 제안했다. 초기 문서가 증명하는 것은 이 연구의 문제 제기와 연대기이지, 산업계 전반에 그러한 현상이 이미 일어났다는 사실은 아니다.

이 글의 기여는 (1) 준공리화를 판정 가능한 행동 가설로 좁혀 정의하고, (2) 원칙에 대한 구조적 분류에서 특정 패치에 대한 승인·거절로 넘어가는 문제를 하위 기제로 제시하며, (3) 이 가설을 반박할 수 있는 경쟁 설명과 실제 후속 실험을 제안하는 데 있다.

### 2. 역사: 공리, 정전, 원칙, 지시

객체지향의 역사는 한 개의 설계 규범이 축적된 역사가 아니다. 시뮬레이션과 클래스의 Simula 전통, 메시지와 상호작용을 중시한 Smalltalk의 설명, 모듈 분해 기준을 제시한 Parnas의 논의, 행동적 하위 타입을 다룬 Liskov–Wing의 논의는 서로 다른 문제를 다뤘다. Meyer와 Martin의 개방–폐쇄 원칙 역시 안정된 모듈 계약과 예상할 변경의 종류를 중요하게 다뤘다. Martin은 1996년 ‘Strategic Closure’에서 모든 변경에 닫힌 모듈을 만드는 일이 불가능하므로 어떤 변경을 예상하는지가 중요하다고 설명한다. 이러한 원문들은 동일하지도 무오류하지도 않다. 오늘날의 변화에 대응하는 예측력이 있는지 별도로 시험해야 한다.

여기서 **형식적 공리화**는 전제와 추론 규칙을 정확하게 정의하는 수학적 활동이며, **직업적 정전화**는 교육·실무에서 반복된 조언이 정통적인 지식으로 받아들여지는 역사적 과정이다. **운영상의 준공리화**는 더 좁은 행동적 주장이다. 에이전트나 검토자가 현재 요구·명시된 예외·기존 호출자 계약에 반하는 근거를 받았는데도, 원칙 이름만으로 허용 가능한 대안을 배제하는가? 강한 표현이 쓰였다는 이유만으로 이 가설이 참이 되는 것은 아니다. 또한 인간 리뷰어의 승인 관행, 저장소의 로컬 지시문, 코딩 에이전트의 실행 반응, 기초 모델 훈련 자료는 서로 다른 층위다.

### 3. 자료: 지금 확인한 것과 확인하지 않은 것

[AreWeSOLID 아카이브 감사](./18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md)에서 OCP 관련 저장 응답 행은 768개였다. 이는 독립적인 768개 소프트웨어 변경 사례가 아니라 **48개 고유 제출 코드가 각 16차례 나타난 기록**이다. 가린 뒤 구분되는 지시문 틀은 24개였다. 프롬프트는 분류 범주를 평가하기 위한 자료이지, 각 제출 코드에 관한 실제 유지보수 요구와 승인된 구계약을 모두 전달하는 판정 자료는 아니다. 코드 내부 단서가 일부 존재하므로 요구·계약 정보가 전혀 없었다고 단정하지도 않는다.

[고정 도서관 패치 사례](./31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md)에서는 한 패치가 기술보고서를 지원하지만 정오표 지원은 없고, 기존 책 출력의 접두어를 바꾼다. 정오표가 필수거나 구접두어가 계약상 보호된다면 거절하지만, 그 둘이 모두 요구되지 않는 작은 명세에서는 승인할 수 있다. 이는 연구자가 정의한 제한적인 기준의 *반례형 예시*이지 실제 프로젝트의 완전한 승인 규칙이 아니다. 제3의 별도 보호 의무를 추가하면 기존 승인이 미공개 상태에서 보류가 되는 것도 확인했다.

[Go Chi #995](https://github.com/go-chi/chi/issues/995)는 원작성자가 싱글턴 미들웨어가 정상 동작하거나 잘못된 재사용을 명시적으로 알리기를 요청한 이슈다. 인스턴스를 새로 만드는 우회책이 경로 테스트에 통과해도 원래 요청을 그대로 충족했다는 뜻은 아니다. [Chi #1035](https://github.com/go-chi/chi/issues/1035)에서는 최초의 정규식 경로 문제를 작성자가 후속 댓글에서 정정했다. 두 이슈를 Go v5.1.0에서 제한적으로 재현했지만 **OCP 지시가 실제 개발자에게 부당한 거절을 일으켰다는 자료는 아니다**.

### 4. 제안 개념: 원칙에서 수정안 판단으로의 전이

우리는 구조적 패턴의 *분류*와 특정 수정안의 *처리*를 구분하는 문제를 **원칙→수정안 판단의 전이 문제(principle-to-patch transport problem)**라고 부르자고 제안한다. 분류가 정확하더라도 그것이 패치를 거절할 충분한 이유인지는 새로운 요구, 보호받는 기존 동작, 편집 가능한 모듈 경계, 대체 구현의 가능성에 달려 있다. 그 요건이 실제로 확인되었다면 원칙에 기초한 경고는 타당할 수 있다.

이 개념이 요구공학이나 Design by Contract의 과거 연구에서 전혀 존재하지 않았다는 뜻은 아니다. 새로 제안하는 것은 이 구별을 **AI 설계 원칙 적용의 결과 변수**로 명시하고, (i) 코드 패턴 라벨의 정확도, (ii) 실제 수정안의 합격 가능성, (iii) 결정을 뒷받침하는 계약 근거, (iv) 반대 증거 이후 판단 변경을 독립적으로 측정하자는 연구 의제다. 문맥이 불충분할 때의 질문·기권 역시 하나의 결과다.

### 5. 실제로 구별할 경쟁 가설

네 프롬프트 조건을 [2026년 10월 9일 사전 설계](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md)에서 복원했다. `NONE`은 추가 설계 원칙을 지시하지 않는다. `HARD_SOLID`는 강한 원칙 준수를 요구한다. `SCOPED_SOLID`는 변경 종류와 예상 안정성에 따라 원칙을 적용한다. `EVIDENCE_CONDITIONAL`은 코드·변경 요구·기존 계약·대안을 통해 판단하고 근거가 부족하면 질문하거나 보류한다. 같은 소스 버전과 요구, 기존 계약, 도구, 모델·예산을 받되 설계 조언 단락만 다르게 해야 한다.

**원칙의 운영상 준공리화 가설**은 강제 지시가 다른 조건에 비해 계약에 어긋나는 구조적 고집이나 반례 이후 수정 불능을 더 많이 일으킬 수 있다고 예측한다. 그러나 **어휘 반복 가설**에 따르면 설명에서 SOLID만 더 자주 언급되고 코드는 달라지지 않는다. **과제·테스트 지배 가설**에 따르면 모든 조건의 코드가 동일하게 요구를 충족한다. 어떤 프로젝트에서는 강한 지시가 실제 개선을 가져올 수도 있다. 어느 쪽도 사전에 승자로 선언할 수 없다. 새 에이전트 문맥에서의 실제 생성·실행은 **아직 수행하지 않았다**.

### 6. 구현 가능한 연구 프로그램

미래 연구의 최소 단위는 동일한 실제 Go 변경 요구에 대한 각각의 독립된 에이전트 실행이다. 소스 버전·승인된 요구·구계약·수정 허용 범위·동일한 기능 오라클을 고정하고, 네 조건의 배정 순서와 모델별 균형을 기록한다. 주요 결과는 기존/신규 Go 테스트 성공 및 API 보존이다. 설명 속 원칙 인용, 새로운 추상화의 종류, 패치 크기, 반례를 제시한 후의 수정·기권은 별개의 결과 변수다. 자동 검사와 독립적인 사람의 코드·계약 검토가 다르면 그 불일치를 보존해야 한다.

기존 Go 두 구조에서 동일한 애플리케이션 필터를 추가하면 새 예약 경로 정책을 모두 충족한 [원본 Go 실험](https://github.com/WhoSia/EvoNOMOS/actions/runs/44926936243)은 이 방향의 중요한 **고전적 동률 대조 사례**다. 어떤 요구에서는 SOLID형 구조가 필수적이지 않다는 작은 근거일 뿐, 아직 네 프롬프트 조건의 에이전트 결과는 아니다. 프로젝트 수준에서 예상 변경이 달라지면 더 깊은 변경 비용 비교는 Paper C로, AI 지침 준공리화의 실제 빈도와 문헌·리뷰 인용 분석은 Paper D로 보내는 편이 적합하다.

### 7. 논의와 결론

Paper B는 SOLID가 틀렸다고 선언하지 않는다. 과거의 개발 지침이 현재 환경에서도 유용한 범위, 비효율적인 범위, 프로젝트 계약 때문에 강제되어야 하는 범위를 **서로 다른 이유로** 설명하자는 제안이다. 수리논리학의 광범위한 완전성 정리나 임의 Go 프로그램의 동형 증명은 이 문제를 제안하기 위한 필수 선행 조건이 아니다. 장래에 모든 코드에 대한 판정 가능성이나 효과의 보편성을 주장한다면 그때에는 정확한 수학적 정의와 별도 증명이 필요하다.

핵심 제안은 간단하다. AI가 설계 원칙의 언어를 더 많이 사용할수록, 그 언어가 실제 변경 결정에 어느 정도의 권한을 갖는지 추적하는 연구도 필요하다. 원칙을 믿는가 반박하는가보다 **어떤 요구·구계약·반대 사례를 받고 실제 결정을 바꾸는가**가 더 좋은 실험 질문이다. 이 원고는 완성된 효과 측정보다 이 연구 질문을 명명하고, 독립된 실험으로 반박할 수 있게 만드는 데 우선순위를 둔다.

---

## English manuscript

### Abstract

SOLID is a family of software-design *principles*. Under what circumstances might AI coding agents or review workflows make these principles function as hard *rules or apparent axioms*? This question appeared in the original EvoNOMOS discussion on July 29, 2026. We propose **operational quasi-axiomatization** as an empirical target: conditional design advice is granted authority to decide an individual patch without checking relevant changes, contracts, exceptions and competing implementations. This is not a critique of formal axiomatic reasoning. We situate the question historically, audit a stored OCP-classification benchmark, develop a fixed-patch contract counterexample, and examine third-party Go issue discussions distinguishing reported demands from passing workarounds. These sources do not establish the prevalence or causes of such agent behavior. We recover an earlier four-treatment proposal for agent experiments—no added guidance, hard SOLID, scoped SOLID and evidence-conditional design advice—and articulate behavioral outcomes and classical rivals. The paper aims to establish a falsifiable research question, not to assert a universal software law.

### 1. Introduction: advice with operational force

A code review may warn that an implementation violates the Open–Closed Principle. That warning can characterize a real structural feature, but it cannot alone determine which forthcoming change is required, which previously supported call must survive, or which repair the project is authorized to make. Both the warning and a rejection may be justified in a particular project. The distinction is the **authority assigned to the inference**.

The [original July 29, 2026 EvoNOMOS conversation](https://drive.google.com/file/d/1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er/view) distinguished a principle from a compulsory rule and asked whether tools including Codex and Claude Code might treat SOLID *as though* it were axiomatic. The [October 9 Paper B hypothesis](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_SOLID_OBJECT_ORIENTATION_AND_AI_QUASI_AXIOMATIZATION_PAPER_B.md) called this possibility *operational quasi-axiomatization* and outlined a controlled agent study. These documents establish the **internal chronology of an idea**, not evidence that the phenomenon has been observed across the industry, or historical priority over all existing requirements research.

We contribute an explicit conceptual distinction, one bounded classification-to-action witness, and an empirically falsifiable agent-study proposal. The ambition is to open a scientific question whose negative outcome would also be meaningful.

### 2. History: axioms, canons, and design instructions

Object-oriented software design was not born as a single five-rule system. Simula's modeling trajectory, Smalltalk's message-centered accounts, Parnas's modularity criterion, Liskov and Wing's behavioral subtyping, and Meyer and Martin's discussions of stable extension confront different problems. The Open–Closed Principle itself was not simply a claim that every old line must never change: Martin's 1996 discussion of *Strategic Closure* makes the choice of expected changes part of the engineering problem. These authors are historical interlocutors, not infallible authorities over modern tool-mediated practice.

We distinguish four phenomena. **Formal axiomatization** legitimately specifies premises and rules of inference. **Professional canonization** is a historical process whereby memorable advice becomes authoritative in teaching or practice. **Operational quasi-axiomatization**, our testable behavioral conjecture, arises when an agent or a reviewer continues to treat a principle name as binding even after relevant, credible contrary requirements or preserved contracts are supplied. **Normative legitimacy** asks whether that action was actually justified. Strong wording alone is not evidence of harmful behavior. Foundation-model weights, persistent repository files, immediate prompts, generated patches and human acceptance are distinct causal stages; our study cannot infer one from another without evidence.

### 3. What the existing evidence shows

Our [OCP archive audit](./18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) examined **768 stored response rows**, not 768 independent maintenance tasks. The stored archive contains **48 distinct submitted code examples repeated 16 times** and 24 distinct masked prompt scaffolds. The benchmark assesses a violation-classification task; it does not by itself supply a complete, authority-bearing maintenance requirement for each submitted patch. Some code includes hints, so we do not claim the inputs contain no relevant contextual information.

An [authored library-patch example](./31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md) demonstrates the distinction in a deliberately small setting. The candidate implements technical-report handling, omits errata and changes an older book-display prefix. Under the stipulated criteria it is admissible only when neither errata nor the previous prefix is a binding obligation. Extending the universe with a third independently protected obligation changes what evidence is sufficient for approval. These are author-defined worlds, not industrial acceptance statistics.

In [go-chi/chi issue #995](https://github.com/go-chi/chi/issues/995), the reporter wanted singleton middleware reuse to route correctly **or** to fail explicitly. A freshly allocated middleware instance was a practical workaround, yet passing its HTTP tests does not establish support for the originally requested singleton behavior. The reporter of [issue #1035](https://github.com/go-chi/chi/issues/1035) later withdrew one initial regex-subpath allegation, leaving a narrower method-precedence report. Our pinned original-Go reproduction checks limited HTTP effects; neither issue documents a reviewer wrongfully rejecting a patch because of OCP.

### 4. The principle-to-patch transport problem

We propose naming a narrower, testable mechanism: the **principle-to-patch transport problem**. A structural classifier can correctly identify a pattern, but applying the label to approve, reject or demand a specific refactoring additionally requires knowledge about the requested change, protected caller behavior, edit rights and feasible alternatives. The transport can be valid: a principle may genuinely summarize a binding project's need. It can also be overextended where these sources remain unknown or conflicting.

We do not claim requirements engineering, Design by Contract or code-review research overlooked obligations and authority. The proposed empirical contribution is to make **four distinct evaluands** explicit in AI-assisted design review: accuracy of structural labels, correctness of particular patch disposition, the provenance of binding requirements, and willingness to revise that disposition after conflicting evidence. Asking for missing requirements or abstaining can be an appropriate outcome.

### 5. Competing hypotheses and four instruction treatments

The [October 9, 2026 original preregistration design](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md) specified four conditions: `NONE`, no additional principle advice; `HARD_SOLID`, unconditional adherence; `SCOPED_SOLID`, advice linked to anticipated changes and interfaces; and `EVIDENCE_CONDITIONAL`, alternative comparison based on actual requests, contracts and uncertainty. Each agent should see the same pinned Go task, original source, regression requirements, tool access and budget; only design-advice text changes.

Our **operational quasi-axiomatization conjecture** predicts that hard instructions may increase inappropriate adherence or resistance to valid counterevidence. An equally serious **lexical-echo rival** predicts different SOLID explanations without different patches. A **task-and-tests dominance rival** predicts no material code difference across treatments. Hard guidance might even improve code under some demands. We preclude a predetermined sign of advantage. As of this manuscript **no randomized fresh-agent invocations or agent-generated repair outcomes have been collected**.

### 6. Research design and falsifiers

The proper experimental unit is a **fresh independent agent execution** on an originally frozen codebase with an authentic change request and preserved old-client contract. Block by task and model and predetermine balanced treatment assignments; keep time and tool budgets equal. Primary outcome categories should separate Go functional success, old-API behavior and an independent assessment of contractual admissibility. Secondary categories include modified source surface, type of additional abstraction, written principle citations, stated exceptions, abstention and response to a negative counterexample. Never score vocabulary frequency as software correctness.

Our existing [native Go equal-policy rival](https://github.com/WhoSia/EvoNOMOS/actions/runs/44926936243) demonstrates that two original router architectures can both satisfy the same researcher-authored reserved-path requirement using an ordinary outer wrapper, without editing frozen source arms. That is a useful **classical tie**, not a four-treatment agent result or a general source-architecture theorem. Paper C can compare architectural forecast reversals; Paper D can measure field prevalence of principle-citing reviews. Neither should be reported as already executed.

### 7. Discussion and conclusion

This is not a claim that SOLID is wrong. Established advice may be effective, ineffective, or indispensable depending on actual maintenance conditions, and such distinctions should be settled with source-grounded comparisons rather than inherited authority alone. A **position paper can propose and constrain an empirical research program without proving equivalence of all possible programs**; any future claim of general soundness, complexity-class separation or population treatment effect would require a different, much stronger evidentiary burden.

The proposal is that AI-assisted engineering needs research into **how much decision authority design-principle language receives**, not merely whether the language appears in generated prose. A strong result would identify the conditions under which the original principle correctly predicts a maintenance decision; an equally valuable negative result would show that code behavior follows the task requirements regardless of doctrinal prompt. The manuscript claims a named, falsifiable question and transparent bounded evidence, not observed industrial dogmatism.

---

## References and provenance (selected, working)

- [EvoNOMOS original dialogue (July 29, 2026)](https://drive.google.com/file/d/1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er/view). Project-internal origin record, not published scientific priority.
- [Original Paper B hypothesis (October 9, 2026)](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_SOLID_OBJECT_ORIENTATION_AND_AI_QUASI_AXIOMATIZATION_PAPER_B.md) and [P35-B1 agent trial proposal](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md).
- Parnas (1972), *On the criteria to be used in decomposing systems into modules*, DOI 10.1145/361598.361623.
- Meyer (1988), *Object-Oriented Software Construction*, first edition (partial primary-page custody; full edition not assumed).
- Liskov & Wing (1994), *A Behavioral Notion of Subtyping*, DOI 10.1145/197320.197383.
- Martin (1996), *The Open–Closed Principle*, original [primary PDF](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf).
- Martin (2000), *Design Principles and Design Patterns*, original account with scope qualification (PDF held in canonical Drive research shelf).
- Black (2013), *Object-oriented programming: Some history, and challenges for the next fifty years*, DOI 10.1016/j.ic.2013.08.002.
- Pehlivan et al. (2025), *Are We SOLID with LLMs?*, [arXiv:2509.03093](https://arxiv.org/abs/2509.03093). Distinct benchmark source archive and submitted-code layers must remain separate.
- Widyasari et al. (2025), *Explaining Explanations*, DOI 10.1145/3708518; Papotti et al. (2024), security-patch reviewer acceptance, DOI 10.1007/s10664-024-10506-z; Jin & Chen (2026), *Systematic Overcorrection*, [arXiv:2603.00539v1](https://arxiv.org/abs/2603.00539) held, journal edition not line-by-line compared; Ling et al. (2026), agentic-work acceptance boundaries, DOI 10.3390/systems14101312.
- [Actual Chi issue #995](https://github.com/go-chi/chi/issues/995), [#1035](https://github.com/go-chi/chi/issues/1035); [native Go 995](https://github.com/WhoSia/EvoNOMOS/actions/runs/44924853984), [native Go 1035](https://github.com/WhoSia/EvoNOMOS/actions/runs/44925028205), [classical equal-policy control](https://github.com/WhoSia/EvoNOMOS/actions/runs/44926936243).
- [Full v22 source audits and supplementary historical notes](./PAPER_B_BILINGUAL_INTEGRATED_22_20261122.md) retained without silently importing unverified findings.
