# Paper B v41 — R64 LIRA sentence-by-sentence + RAVEL S0–S6 cold read

**Exact input SHA:** f4a663599691f5e1ef539cd32237c49b59bd77fe (main); reference v39 72278d5b1d23f39cdaaade86979708c2abfb5c0b. LIRA scores are **one-editor provisional recommendations** for retaining current phrasing; they do not measure truth, authenticity, or model origin. Sentence tokenizer is punctuation-based; paragraphs retain final authority. Every sentence has an ID, score, diagnosis, and exact text. Korean/English parity is inspected by section rather than treating translations as 1:1 sentences.

## Quantitative checks (descriptive, not a goal)

- Scored sentences: 108 (K 57 / E 51).
- Scores under 0.75: 5; scores 0.90+: 23. These are *rubric classifications*, not an independent blinded study.
- v39 → v41 lost repetitive formal denials and repetitive metadata within the body; the source and evidence appendix is still maintained.

## Full sentence ledger
| ID | Keep 0–1 | Local concern | Source sentence | Note |
|---|---:|---|---|---|
| KA.01.01 | 0.85 | FLOW | 설계 원칙은 판단을 돕기 위해 만들어졌지만, 때로는 판단의 이유를 대신한다. | Preserve unless neighboring paragraph repeats its job |
| KA.01.02 | 0.91 | READER QUESTION | 코드 리뷰에서 ‘OCP 위반’이라는 진단만으로 수정이 요구될 때, 그 판단에 필요한 변경 전망과 동작 계약, 비용에 관한 근거는 어디에 있는가? | Question guides reader into concrete distinction |
| KA.01.03 | 0.94 | CORE | 이 글은 설계 조언과 팀의 승인된 규칙, 동작 계약을 구별하면서, 각 원칙이 언제 정당화되는지를 기록하는 **설계 원칙의 맥락별 지도(contextual principle atlas)**를 제안한다. | Direct contribution; keep unless claim status drifts |
| KA.01.04 | 0.85 | FLOW | 이 지도는 원칙의 우열을 한 줄로 세우기보다 적용 영역의 겹침, 판단의 유보, 새로운 증거에 따른 수정을 드러낸다. | Preserve unless neighboring paragraph repeats its job |
| KA.01.05 | 0.85 | FLOW | 관련 수학 이론은 이미 풍부하다. | Preserve unless neighboring paragraph repeats its job |
| KA.01.06 | 0.85 | FLOW | 문제는 그 구조들을 실제 설계 논증의 조건과 연결할 수 있느냐는 데 있다. | Preserve unless neighboring paragraph repeats its job |
| K1.01.01 | 0.85 | FLOW | 코드 리뷰에서 “OCP를 어겼으니 고쳐야 한다”는 말을 들었다고 해 보자. | Preserve unless neighboring paragraph repeats its job |
| K1.01.02 | 0.91 | READER QUESTION | 무엇을 어떻게 고쳐야 할까? | Question guides reader into concrete distinction |
| K1.01.03 | 0.85 | FLOW | 앞으로 늘어날 기능의 종류, 보존해야 할 기존 동작, 지금 변경하는 데 드는 비용을 모른다면 원칙의 이름만으로는 답할 수 없다. | Preserve unless neighboring paragraph repeats its job |
| K1.01.04 | 0.85 | FLOW | 반대로 팀이 OCP 준수를 명시적인 개발 규칙으로 정했다면 그 규칙을 따라야 할 이유가 따로 생긴다. | Preserve unless neighboring paragraph repeats its job |
| K1.01.05 | 0.74 | EVIDENCE LIMIT | **설계 조언과 팀의 규칙, 프로그램이 지켜야 하는 동작 계약은 서로 다른 근거를 요구한다.** 그런데 코드 리뷰에서는 그 차이가 생략되기 쉽다. | Plausible illustration, not measured prevalence; qualify by scene |
| K1.01.06 | 0.74 | GENERIC CLOSURE | SOLID나 DRY처럼 유용한 이름이 때로 **선언되지 않은 공리 같은 권위**를 얻는 순간은 바로 여기에서 출발한다. | Abstract meta-ending; consider more concrete observation |
| K1.02.01 | 0.86 | SOURCE BRIDGE | Naur [1]는 프로그래밍을 프로그램이라는 결과물을 만드는 일만이 아니라, 개발자가 문제를 이해하고 그 이해를 축적하는 *이론 형성*으로 보았다. | Keep reference, verify exactly what source supports |
| K1.02.02 | 0.85 | FLOW | 코드가 수정될 때 필요한 것도 바로 그런 이해다. | Preserve unless neighboring paragraph repeats its job |
| K1.02.03 | 0.86 | SOURCE BRIDGE | Toulmin [2]의 논증 이론을 빌리면, 설계 원칙의 이름은 주장이고 그 주장이 통할 조건은 별도로 제시해야 하는 정당화 근거에 가깝다. | Keep reference, verify exactly what source supports |
| K1.02.04 | 0.85 | FLOW | 이 연결을 통해 코드 리뷰에서 빠져 있던 질문이 또렷해진다. | Preserve unless neighboring paragraph repeats its job |
| K1.02.05 | 0.98 | VOICE PROTECT | **그 이름이 언제 충분한 이유가 되는지는 별도로 설명해야 한다.** | Preserve authorial question/ending; resist template polish |
| K2.01.01 | 0.89 | TYPED WARRANT | 설계 원칙들이 서로 다른 문제를 보고 있다면, 원칙마다 유효한 영역을 그려 볼 수 있지 않을까? | Critical distinction; watch repetitive contrast |
| K2.01.02 | 0.85 | FLOW | SOLID의 다섯 원칙, DRY, YAGNI, 정보 은닉, 디자인 패턴은 변경 방향과 기존 동작, 의존 관계, 협업 비용을 각기 다른 각도에서 다룬다. | Preserve unless neighboring paragraph repeats its job |
| K2.01.03 | 0.81 | MODALITY | 반복해서 새로운 기능을 붙여야 한다면 확장 지점에 투자할 만하지만, 확장 가능성이 낮다면 같은 장치가 불필요한 복잡성이 될 수 있다. | Assess whether qualification is epistemically needed |
| K2.01.04 | 0.91 | READER QUESTION | OCP와 YAGNI 중 하나가 언제나 옳다는 문제가 아니다. | Question guides reader into concrete distinction |
| K2.01.05 | 0.85 | FLOW | **어떤 변경 요구 아래에서 각 조언이 유용해지고, 그 영역이 겹치면 무엇을 비교해야 하는가?** | Preserve unless neighboring paragraph repeats its job |
| K2.02.01 | 0.94 | CORE | 이 글에서 제안하는 **설계 원칙의 맥락별 지도(contextual principle atlas)**는 그런 질문을 기록하는 방법이다. | Direct contribution; keep unless claim status drifts |
| K2.02.02 | 0.85 | FLOW | 지도에 적힐 것은 원칙의 이름뿐 아니라 예상되는 변경, 지켜야 할 동작, 선택 가능한 설계, 팀 규칙의 권한, 비용을 판단하는 기준과 실제로 확보된 증거다. | Preserve unless neighboring paragraph repeats its job |
| K2.02.03 | 0.94 | CORE | 원칙을 지지하는 맥락과 반박하는 맥락을 나란히 놓으면 적용 영역의 경계가 드러난다. | Direct contribution; keep unless claim status drifts |
| K2.02.04 | 0.94 | CORE | 자료가 모자라면 판단을 남겨 두고, 지지와 반박이 함께 나오면 그 갈등도 지운 채 넘기지 않는다. | Direct contribution; keep unless claim status drifts |
| K2.02.05 | 0.84 | SPECULATIVE METAPHOR | 서로 다른 지역에서 쓰이는 지도들이 한 장으로 이어질 수도 있고, 끝내 맞물리지 않을 수도 있다. | Promising metaphor; never assert sheaf gluing without proof |
| K2.02.06 | 0.84 | SPECULATIVE METAPHOR | **우리가 찾는 상위 구조는 그 차이를 지워 버리는 법칙보다, 차이가 생기는 조건을 설명하는 관계에 가까울 것이다.** | Promising metaphor; never assert sheaf gluing without proof |
| K3.01.01 | 0.85 | FLOW | 각 원칙을 지지하는 맥락을 모으면 집합이 되고, 그 집합들을 포함관계에 따라 배열할 수 있다. | Preserve unless neighboring paragraph repeats its job |
| K3.01.02 | 0.86 | SOURCE BRIDGE | 이 단계에서는 Ganter와 Wille [7]의 형식개념분석이 좋은 비교 대상이다. | Keep reference, verify exactly what source supports |
| K3.01.03 | 0.79 | CONNECTIVE | 그러나 적용 영역만으로는 판단의 역사를 설명하기 어렵다. | Check argumentative relation, not surface rhythm |
| K3.01.04 | 0.94 | CORE | 같은 변경 요구를 놓고 지지 근거와 반박 근거가 동시에 등장할 수 있고, 이후 다른 증거가 들어오면 권고도 달라진다. | Direct contribution; keep unless claim status drifts |
| K3.01.05 | 0.86 | SOURCE BRIDGE | Belnap의 다치논리 [8]는 앞의 충돌을, AGM의 신념 수정 [3]은 뒤의 개정을 검토할 출발점이 된다. | Keep reference, verify exactly what source supports |
| K3.01.06 | 0.89 | TYPED WARRANT | 서로 다른 영역의 판단을 연결하려면 그 사이에서 무엇이 보존되는지도 물어야 한다. | Critical distinction; watch repetitive contrast |
| K3.01.07 | 0.86 | SOURCE BRIDGE | Goguen과 Burstall의 institution 이론 [9]이 이 질문에 형식적 비교 기준을 제공한다. | Keep reference, verify exactly what source supports |
| K3.01.08 | 0.74 | GENERIC CLOSURE | **적용 영역의 순서, 증거의 충돌, 판단의 개정과 영역 사이의 연결은 같은 문제가 아니다.** 이 네 관계가 실제 설계에서 어떻게 맞물리는지가 연구할 대상이다. | Abstract meta-ending; consider more concrete observation |
| K3.02.01 | 0.85 | FLOW | 변경 요구를 고려해 소프트웨어를 나누어야 한다는 생각은 오래되었다. | Preserve unless neighboring paragraph repeats its job |
| K3.02.02 | 0.86 | SOURCE BRIDGE | Parnas [4]는 모듈 분할의 기준을 따졌고, Baldwin [5]은 모듈성 이론에서 가정했던 조건과 한계를 되짚었다. | Keep reference, verify exactly what source supports |
| K3.02.03 | 0.94 | CORE | 이 연구들과 나란히 놓았을 때 맥락별 지도가 던지는 질문은 조금 다르다. | Direct contribution; keep unless claim status drifts |
| K3.02.04 | 0.85 | FLOW | **특정 설계가 바뀌기 쉬운가를 넘어, 그 설계를 권하는 이유는 무엇이며 그 이유는 어떤 상황에서 효력을 잃는가?** | Preserve unless neighboring paragraph repeats its job |
| K4.01.01 | 0.85 | FLOW | 설계 탐색 알고리즘이 어떤 구조를 최적이라고 평가했다고 하자. | Preserve unless neighboring paragraph repeats its job |
| K4.01.02 | 0.85 | FLOW | 무엇을 최적화한 것일까? | Preserve unless neighboring paragraph repeats its job |
| K4.01.03 | 0.85 | FLOW | 수정 횟수를 줄이는 설계와 초기 구현 비용을 줄이는 설계는 같은 순서로 배열되지 않을 수 있다. | Preserve unless neighboring paragraph repeats its job |
| K4.01.04 | 0.86 | SOURCE BRIDGE | Räihä [6]가 검토한 탐색 기반 소프트웨어 설계에서도 후보 구조를 표현하는 방식과 적합도 함수의 선택은 중요한 결정이다. | Keep reference, verify exactly what source supports |
| K4.01.05 | 0.85 | FLOW | **목적함수 역시 누군가 선택한 판단 기준**이다. | Preserve unless neighboring paragraph repeats its job |
| K4.01.06 | 0.96 | CONTRIBUTION | 따라서 지도는 원칙에 대한 지지·반박 근거뿐 아니라 그 근거가 전제한 평가 기준도 기록해야 한다. | Protect typed evaluation-authority insight |
| K4.01.07 | 0.85 | FLOW | 팀이 정한 규칙을 따를 의무와 프로그램이 지켜야 할 동작 계약, 유지보수 비용에 관한 조언을 같은 점수로 치환하면 그 차이를 잃는다. | Preserve unless neighboring paragraph repeats its job |
| K5.01.01 | 0.85 | FLOW | 이 지도가 실무에 도움이 되는지는 별도로 시험해야 한다. | Preserve unless neighboring paragraph repeats its job |
| K5.01.02 | 0.85 | FLOW | 같은 코드 변경 사례와 자료를 받은 평가자들이 원칙의 적용 근거를 얼마나 일관되게 기록하는지, 새 반례가 등장했을 때 이전 판단의 어느 부분을 수정하는지 살펴볼 수 있다. | Preserve unless neighboring paragraph repeats its job |
| K5.01.03 | 0.85 | FLOW | 비교 대상은 간단한 설계 검토 체크리스트와 기존의 명세·설계 분석 방법이다. | Preserve unless neighboring paragraph repeats its job |
| K5.01.04 | 0.85 | FLOW | 평가에는 판단의 재현성, 타당한 판단 유보, 반례에 대한 수정 능력뿐 아니라 기록에 드는 시간도 포함되어야 한다. | Preserve unless neighboring paragraph repeats its job |
| K5.01.05 | 0.85 | FLOW | **기존 방법보다 이유를 분명하게 설명하지도 못하고 비용만 늘린다면 이 지도는 채택할 근거를 잃는다.** | Preserve unless neighboring paragraph repeats its job |
| KC.01.01 | 0.98 | VOICE PROTECT | **설계 원칙은 어떻게 선언되지 않은 공리 같은 권위를 얻게 되는가? | Preserve authorial question/ending; resist template polish |
| KC.01.02 | 0.94 | CORE | 그 원칙들의 적용 범위와 정당화 근거에는 아직 제대로 기술하지 못한 구조가 있을까?** 맥락별 지도는 두 질문을 함께 다룰 한 가지 시도다. | Direct contribution; keep unless claim status drifts |
| KC.01.03 | 0.85 | FLOW | 한 판단이 통하는 영역을 그린 다음, 조건이 달라질 때 어떤 근거가 남고 어떤 근거가 무너지는지 살펴보는 것이다. | Preserve unless neighboring paragraph repeats its job |
| KC.01.04 | 0.85 | FLOW | 원칙은 버릴 대상도, 시험을 면제받을 대상도 아니다. | Preserve unless neighboring paragraph repeats its job |
| KC.01.05 | 0.98 | VOICE PROTECT | **이름이 남는 것보다 중요한 것은 그 이름을 정당화했던 사유가 남는 일이다.** | Preserve authorial question/ending; resist template polish |
| EA.01.01 | 0.85 | FLOW | Design principles are meant to guide engineering judgment, yet their names sometimes substitute for its reasons. | Preserve unless neighboring paragraph repeats its job |
| EA.01.02 | 0.81 | MODALITY | When a code review demands a change merely because it 'violates OCP,' what happened to the anticipated changes, behavioral obligations, and costs that would warrant that demand? | Assess whether qualification is epistemically needed |
| EA.01.03 | 0.94 | CORE | We distinguish design advice from authorized team rules and behavioral contracts, then propose a **contextual principle atlas** to record where each principle is warranted, where its reasons conflict, and how a judgment changes with new evidence. | Direct contribution; keep unless claim status drifts |
| EA.01.04 | 0.85 | FLOW | Rather than ranking principles once and for all, the atlas traces overlapping domains and revisable arguments. | Preserve unless neighboring paragraph repeats its job |
| EA.01.05 | 0.85 | FLOW | Existing mathematical theories provide resources for this effort; the open task is to connect those structures to the conditions of actual software design judgments. | Preserve unless neighboring paragraph repeats its job |
| E1.01.01 | 0.91 | READER QUESTION | Imagine a code review that ends with: “This violates OCP, so it must be fixed.” What, exactly, should be changed? | Question guides reader into concrete distinction |
| E1.01.02 | 0.89 | TYPED WARRANT | Without knowing which features are likely to grow, which behaviors must remain intact, and what the change will cost, the name of a principle cannot settle the question. | Critical distinction; watch repetitive contrast |
| E1.01.03 | 0.79 | CONNECTIVE | If the team has explicitly adopted OCP as a rule, however, that rule has a separate source of authority. | Check argumentative relation, not surface rhythm |
| E1.01.04 | 0.74 | EVIDENCE LIMIT | **Design advice, team policy, and behavioral contracts call for different kinds of reasons.** Code reviews can leave those distinctions unstated. | Plausible illustration, not measured prevalence; qualify by scene |
| E1.01.05 | 0.98 | VOICE PROTECT | That is one route by which useful names such as SOLID and DRY can acquire **the force of axioms that no one declared**. | Preserve authorial question/ending; resist template polish |
| E1.02.01 | 0.86 | SOURCE BRIDGE | For Naur [1], programming involves building a theory of the problem a program solves, not simply producing code. | Keep reference, verify exactly what source supports |
| E1.02.02 | 0.85 | FLOW | Changes demand that understanding. | Preserve unless neighboring paragraph repeats its job |
| E1.02.03 | 0.86 | SOURCE BRIDGE | Toulmin's account of argument [2] gives us another way to ask what is missing: a principle can name the claim, but the grounds that warrant its use still have to be supplied. | Keep reference, verify exactly what source supports |
| E1.02.04 | 0.85 | FLOW | Applied to a code review, the question becomes sharper. | Preserve unless neighboring paragraph repeats its job |
| E1.02.05 | 0.85 | FLOW | **When is the name enough to justify the verdict?** | Preserve unless neighboring paragraph repeats its job |
| E2.01.01 | 0.91 | READER QUESTION | What if familiar design principles are describing different regions of the same engineering landscape? | Question guides reader into concrete distinction |
| E2.01.02 | 0.85 | FLOW | SOLID, DRY, YAGNI, information hiding, and design patterns address directions of change, preserved behavior, dependencies, and coordination costs from different angles. | Preserve unless neighboring paragraph repeats its job |
| E2.01.03 | 0.81 | MODALITY | An extension mechanism may justify its upfront complexity when variants are likely to recur; when demand is unlikely, the same mechanism may only add work. | Assess whether qualification is epistemically needed |
| E2.01.04 | 0.85 | FLOW | The useful question is not which of OCP or YAGNI wins everywhere. | Preserve unless neighboring paragraph repeats its job |
| E2.01.05 | 0.85 | FLOW | **Under which demands does each piece of advice hold, and what should we compare where their domains overlap?** | Preserve unless neighboring paragraph repeats its job |
| E2.02.01 | 0.94 | CORE | Our **contextual principle atlas** is a way to keep track of these questions. | Direct contribution; keep unless claim status drifts |
| E2.02.02 | 0.85 | FLOW | An entry records not only the named principle but anticipated changes, preserved behavior, available designs, the authority of team rules, evaluation criteria, and the evidence at hand. | Preserve unless neighboring paragraph repeats its job |
| E2.02.03 | 0.85 | FLOW | Placing supporting and defeating cases side by side makes their boundaries visible. | Preserve unless neighboring paragraph repeats its job |
| E2.02.04 | 0.79 | CONNECTIVE | Missing evidence leaves a judgment open; conflicting evidence remains in view rather than being forced into a single score. | Check argumentative relation, not surface rhythm |
| E2.02.05 | 0.81 | SPECULATIVE METAPHOR | Local accounts may join into a larger picture—or fail to fit. | Promising metaphor; never assert sheaf gluing without proof |
| E2.02.06 | 0.81 | SPECULATIVE METAPHOR | **The higher structure worth seeking may be less a law that erases differences than a relation that explains where those differences arise.** | Promising metaphor; never assert sheaf gluing without proof |
| E3.01.01 | 0.86 | SOURCE BRIDGE | Collect the contexts that support a principle, and we obtain a set; compare such sets by inclusion, and formal concept analysis [7] becomes a useful reference. | Keep reference, verify exactly what source supports |
| E3.01.02 | 0.85 | FLOW | But domains alone do not capture the history of a judgment. | Preserve unless neighboring paragraph repeats its job |
| E3.01.03 | 0.81 | MODALITY | Supporting and defeating arguments may coexist, and new evidence may revise the recommendation. | Assess whether qualification is epistemically needed |
| E3.01.04 | 0.86 | SOURCE BRIDGE | Belnap's many-valued logic [8] helps frame the first difficulty; AGM belief revision [3] offers a point of comparison for the second. | Keep reference, verify exactly what source supports |
| E3.01.05 | 0.85 | FLOW | Joining judgments from different contexts raises a further question: what must remain invariant as the context changes? | Preserve unless neighboring paragraph repeats its job |
| E3.01.06 | 0.85 | FLOW | Institution theory [9] provides one formal reference. | Preserve unless neighboring paragraph repeats its job |
| E3.01.07 | 0.74 | GENERIC CLOSURE | **Ordering domains, representing conflicting evidence, revising judgments, and connecting local accounts are distinct problems.** Their relationship in actual design practice is the object of inquiry. | Abstract meta-ending; consider more concrete observation |
| E3.02.01 | 0.85 | FLOW | Engineering design has long been tied to change. | Preserve unless neighboring paragraph repeats its job |
| E3.02.02 | 0.86 | SOURCE BRIDGE | Parnas [4] asked how systems should be divided into modules; Baldwin [5] revisited the assumptions and limits of design-rules theory. | Keep reference, verify exactly what source supports |
| E3.02.03 | 0.91 | READER QUESTION | The atlas asks a different question beside theirs: **Beyond whether an architecture accommodates change, what warrants the advice to choose it, and under which circumstances does that warrant fail?** | Question guides reader into concrete distinction |
| E4.01.01 | 0.85 | FLOW | Suppose a search algorithm selects an optimal architecture. | Preserve unless neighboring paragraph repeats its job |
| E4.01.02 | 0.91 | READER QUESTION | Optimal with respect to what? | Question guides reader into concrete distinction |
| E4.01.03 | 0.85 | FLOW | A design that minimizes near-term implementation effort need not minimize the cost of later changes. | Preserve unless neighboring paragraph repeats its job |
| E4.01.04 | 0.86 | SOURCE BRIDGE | In search-based software design, as Räihä [6] discusses, both representation and fitness-function choice matter. | Keep reference, verify exactly what source supports |
| E4.01.05 | 0.96 | CONTRIBUTION | **The fitness function is itself a selected evaluative criterion.** The atlas must therefore record the standards behind a recommendation as well as its evidence. | Protect typed evaluation-authority insight |
| E4.01.06 | 0.85 | FLOW | An authorized rule, a behavioral obligation, and an estimate of maintenance cost cannot be substituted for one another merely by placing them in a single score. | Preserve unless neighboring paragraph repeats its job |
| E5.01.01 | 0.85 | FLOW | Whether an atlas helps in practice is a separate question. | Preserve unless neighboring paragraph repeats its job |
| E5.01.02 | 0.85 | FLOW | Give independent reviewers the same code-change case and evidence, then ask whether they can consistently record a principle's grounds and revise the record when a counterexample appears. | Preserve unless neighboring paragraph repeats its job |
| E5.01.03 | 0.85 | FLOW | Compare their work with an ordinary design checklist and existing specification or design-analysis methods. | Preserve unless neighboring paragraph repeats its job |
| E5.01.04 | 0.85 | FLOW | Measure reproducibility, appropriate abstention, the quality of revision, and the time spent recording the reasons. | Preserve unless neighboring paragraph repeats its job |
| E5.01.05 | 0.85 | FLOW | **If the atlas makes judgments no clearer while imposing more work, it has lost its practical case.** | Preserve unless neighboring paragraph repeats its job |
| EC.01.01 | 0.85 | FLOW | **How does design advice acquire the authority of an undeclared axiom? | Preserve unless neighboring paragraph repeats its job |
| EC.01.02 | 0.85 | FLOW | Might the scope and grounds of our familiar principles reveal structures we have yet to describe?** A contextual atlas is one way to pursue both questions: locate the regions in which a judgment holds, then ask which of its reasons survive when the conditions change. | Preserve unless neighboring paragraph repeats its job |
| EC.01.03 | 0.85 | FLOW | A principle is neither something to discard casually nor something to exempt from examination. | Preserve unless neighboring paragraph repeats its job |
| EC.01.04 | 0.98 | VOICE PROTECT | **What matters is not only whether its name survives, but whether the reasoning that once justified it survives with it.** | Preserve authorial question/ending; resist template polish |

## RAVEL five-family adversarial review

1. **Invented authority or experience — PASS**: manuscript never claims observed reviewer prevalence or survey outcomes; example is explicitly introduced as hypothetical. Reference appendix preserved.
2. **Absent decisions or conditions — PASS with future test**: six atlas entry types explicit in §2. Prospectively operationalizing context and reviewer agreement remains open.
3. **Excessive defense — IMPROVED / WATCH**: repeated claims of not proving universality were removed from narrative and retained as provenance notes. Removing these never converts the proposed atlas into a mathematically proved object.
4. **Artificial symmetry — IMPROVED / WATCH**: less mechanical 'A not B' rhythm, more code-review question and source-specific explanation. Korean and English abstracts are aligned in intent, not literal sentence counts.
5. **Evidence/prose mismatch — HOLD for empirical claims**: Parnas/Naur/Räihä reused as literature basis, Belnap and formal concept analysis explicitly prior art, no data-driven 'tool improves decisions' verdict. Complete bibliography audit and outside reader study remain future work, not paper-body defects.

## Two chosen non-edits
- Preserve final line ‘이름이 남는 것보다 중요한 것은 그 이름을 정당화했던 사유가 남는 일이다.’ Its cadence and thesis are specific to the original author's question.
- Preserve the speculative 'local maps might join or fail to fit' as a *question-like proposition*, provided no mathematical gluing theorem is asserted.

## RAVEL dual-loop receipt
DOCUMENT LOOP: v39 census R63 → abstract/§1–2 v40 → §3–5/conclusion v41 → local scoring + stitch/cold read here. THEORY LOOP: user reported defense and AI-like tone, so separate scientific guardrails from body by default; **do not generalize this into a global ban on qualified claims**. Revert the rule if it makes the source/claim status materially less accurate in another paper.

**Freeze decision:** v41 is a substantive improvement but not 'final': author has not accepted voice, LIRA still has sentence-level weak spots, and authorial cold read is not a test performed by an external reader. Continue only when a concrete defect is found; avoid pointless score maximization.
