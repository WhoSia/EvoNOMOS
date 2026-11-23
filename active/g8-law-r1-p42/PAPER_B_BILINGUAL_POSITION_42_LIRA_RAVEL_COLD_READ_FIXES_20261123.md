# 공리로 선언한 적 없는 원칙들: 설계 원칙의 맥락별 지도를 향하여
*The Axioms We Never Declared: Toward a Contextual Atlas of Software Design Principles*

**EvoNOMOS · Paper B · v42 · LIRA/RAVEL second cold read · 2026-11-23**

**장르:** 한·영 개념 논문 · **상태:** 저자 검토용 2차 문장 교정판 (v37–v41 보존)

## 초록

설계 원칙은 판단을 돕기 위해 만들어졌지만, 때로는 판단의 이유를 대신한다. 코드 리뷰에서 ‘OCP 위반’이라는 진단만으로 수정이 요구될 때, 그 판단에 필요한 변경 전망과 동작 계약, 비용에 관한 근거는 어디에 있는가? 이 글은 설계 조언과 팀의 승인된 규칙, 동작 계약을 구별하면서, 각 원칙이 언제 정당화되는지를 기록하는 **설계 원칙의 맥락별 지도(contextual principle atlas)**를 제안한다. 이 지도는 원칙의 우열을 한 줄로 세우기보다 적용 영역의 겹침, 판단의 유보, 새로운 증거에 따른 수정을 드러낸다. 관련 수학 이론은 이미 풍부하다. 문제는 그 구조들을 실제 설계 논증의 조건과 연결할 수 있느냐는 데 있다.

**주제어:** 설계 원칙, 정당화 근거, 맥락, 공리화, 소프트웨어 진화, 비단조 추론, 설계 평가

## 1. 판단의 이름과 판단의 이유

코드 리뷰에서 “OCP를 어겼으니 고쳐야 한다”는 말을 들었다고 해 보자. 무엇을 어떻게 고쳐야 할까? 앞으로 늘어날 기능의 종류, 보존해야 할 기존 동작, 지금 변경하는 데 드는 비용을 모른다면 원칙의 이름만으로는 답할 수 없다. 반대로 팀이 OCP 준수를 명시적인 개발 규칙으로 정했다면 그 규칙을 따라야 할 이유가 따로 생긴다. **설계 조언과 팀의 규칙, 프로그램이 지켜야 하는 동작 계약은 서로 다른 근거를 요구한다.** 그런데 처음의 코드 리뷰 문장에는 그 근거가 적혀 있지 않다. 우리는 이렇게 이유가 빠진 판정이 **선언되지 않은 공리 같은 권위**로 굳어질 가능성에 주목한다.

Naur [1]는 프로그래밍을 프로그램이라는 결과물을 만드는 일만이 아니라, 개발자가 문제를 이해하고 그 이해를 축적하는 *이론 형성*으로 보았다. 코드가 수정될 때 필요한 것도 바로 그런 이해다. Toulmin [2]의 논증 이론을 빌리면, 설계 원칙의 이름은 주장이고 그 주장이 통할 조건은 별도로 제시해야 하는 정당화 근거에 가깝다. 이 연결을 통해 코드 리뷰에서 빠져 있던 질문이 또렷해진다. **그 이름이 언제 충분한 이유가 되는지는 별도로 설명해야 한다.**

## 2. 하나의 절대 법칙이 아니라 맥락별 지도

설계 원칙들이 서로 다른 문제를 보고 있다면, 원칙마다 유효한 영역을 그려 볼 수 있지 않을까? SOLID의 다섯 원칙, DRY, YAGNI, 정보 은닉, 디자인 패턴은 변경 방향과 기존 동작, 의존 관계, 협업 비용을 각기 다른 각도에서 다룬다. 반복해서 새로운 기능을 붙여야 한다면 확장 지점에 투자할 만하지만, 확장 가능성이 낮다면 같은 장치가 불필요한 복잡성이 될 수 있다. OCP와 YAGNI 중 하나가 언제나 옳다는 문제가 아니다. **어떤 변경 요구 아래에서 각 조언이 유용해지고, 그 영역이 겹치면 무엇을 비교해야 하는가?**

이 글에서 제안하는 **설계 원칙의 맥락별 지도(contextual principle atlas)**는 그런 질문을 기록하는 방법이다. 지도에 적힐 것은 원칙의 이름뿐 아니라 예상되는 변경, 지켜야 할 동작, 선택 가능한 설계, 팀 규칙의 권한, 비용을 판단하는 기준과 실제로 확보된 증거다. 원칙을 지지하는 맥락과 반박하는 맥락을 나란히 놓으면 적용 영역의 경계가 드러난다. 자료가 모자라면 판단을 남겨 두고, 지지와 반박이 함께 나오면 그 갈등도 지운 채 넘기지 않는다. 서로 다른 지역에서 쓰이는 지도들이 한 장으로 이어질 수도 있고, 끝내 맞물리지 않을 수도 있다. **우리가 찾는 상위 구조는 그 차이를 지워 버리는 법칙보다, 차이가 생기는 조건을 설명하는 관계에 가까울 것이다.**

## 3. 지도에는 어떤 수학이 필요한가

각 원칙을 지지하는 맥락을 모으면 집합이 되고, 그 집합들을 포함관계에 따라 배열할 수 있다. 이 단계에서는 Ganter와 Wille [7]의 형식개념분석이 좋은 비교 대상이다. 그러나 적용 영역만으로는 판단의 역사를 설명하기 어렵다. 같은 변경 요구를 놓고 지지 근거와 반박 근거가 동시에 등장할 수 있고, 이후 다른 증거가 들어오면 권고도 달라진다. Belnap의 다치논리 [8]는 앞의 충돌을, AGM의 신념 수정 [3]은 뒤의 개정을 검토할 출발점이 된다. 서로 다른 영역의 판단을 연결하려면 그 사이에서 무엇이 보존되는지도 물어야 한다. Goguen과 Burstall의 institution 이론 [9]이 이 질문에 형식적 비교 기준을 제공한다. **적용 영역을 정렬하는 일과 상충하는 증거를 기록하는 일은 다르며, 두 기록을 수정하거나 다른 영역으로 옮기는 데에도 각각의 규칙이 필요하다.** 그래서 설계 판단 하나를 다른 상황에 적용할 때 무엇이 보존되어야 하는지부터 묻게 된다.

변경 요구를 고려해 소프트웨어를 나누어야 한다는 생각은 오래되었다. Parnas [4]는 모듈 분할의 기준을 따졌고, Baldwin [5]은 모듈성 이론에서 가정했던 조건과 한계를 되짚었다. 이 연구들과 나란히 놓았을 때 맥락별 지도가 던지는 질문은 조금 다르다. **특정 설계가 바뀌기 쉬운가를 넘어, 그 설계를 권하는 이유는 무엇이며 그 이유는 어떤 상황에서 효력을 잃는가?**

## 4. 누가 ‘좋은 설계’의 기준을 정하는가

설계 탐색 알고리즘이 어떤 구조를 최적이라고 평가했다고 하자. 무엇을 최적화한 것일까? 수정 횟수를 줄이는 설계와 초기 구현 비용을 줄이는 설계는 같은 순서로 배열되지 않을 수 있다. Räihä [6]가 검토한 탐색 기반 소프트웨어 설계에서도 후보 구조를 표현하는 방식과 적합도 함수의 선택은 중요한 결정이다. **목적함수 역시 누군가 선택한 판단 기준**이다. 따라서 지도는 원칙에 대한 지지·반박 근거뿐 아니라 그 근거가 전제한 평가 기준도 기록해야 한다. 팀이 정한 규칙을 따를 의무와 프로그램이 지켜야 할 동작 계약, 유지보수 비용에 관한 조언을 같은 점수로 치환하면 그 차이를 잃는다.

## 5. 지도가 실제로 도움이 되는지

이 지도가 실무에 도움이 되는지는 별도로 시험해야 한다. 같은 코드 변경 사례와 자료를 받은 평가자들이 원칙의 적용 근거를 얼마나 일관되게 기록하는지, 새 반례가 등장했을 때 이전 판단의 어느 부분을 수정하는지 살펴볼 수 있다. 비교 대상은 간단한 설계 검토 체크리스트와 기존의 명세·설계 분석 방법이다. 평가에는 판단의 재현성, 타당한 판단 유보, 반례에 대한 수정 능력뿐 아니라 기록에 드는 시간도 포함되어야 한다. **기존 방법보다 이유를 분명하게 설명하지도 못하고 비용만 늘린다면 이 지도는 채택할 근거를 잃는다.**

## 결론

**설계 원칙은 어떻게 선언되지 않은 공리 같은 권위를 얻게 되는가? 그 원칙들의 적용 범위와 정당화 근거에는 아직 제대로 기술하지 못한 구조가 있을까?** 맥락별 지도는 두 질문을 함께 다룰 한 가지 시도다. 한 판단이 통하는 영역을 그린 다음, 조건이 달라질 때 어떤 근거가 남고 어떤 근거가 무너지는지 살펴보는 것이다. 원칙은 버릴 대상도, 시험을 면제받을 대상도 아니다. **이름이 남는 것보다 중요한 것은 그 이름을 정당화했던 사유가 남는 일이다.**

---

## Abstract

Design principles are meant to guide engineering judgment, yet their names sometimes substitute for its reasons. When a code review demands a change merely because it 'violates OCP,' what happened to the anticipated changes, behavioral obligations, and costs that would warrant that demand? We distinguish design advice from authorized team rules and behavioral contracts, then propose a **contextual principle atlas** to record where each principle is warranted, where its reasons conflict, and how a judgment changes with new evidence. Rather than ranking principles once and for all, the atlas traces overlapping domains and revisable arguments. Existing mathematical theories provide resources for this effort; the open task is to connect those structures to the conditions of actual software design judgments.

**Keywords:** software design principles, warrants, contextual reasoning, modularity, defeasible arguments, software evolution

## 1. Names and reasons

Imagine a code review that ends with: “This violates OCP, so it must be fixed.” What, exactly, should be changed? Without knowing which features are likely to grow, which behaviors must remain intact, and what the change will cost, the name of a principle cannot settle the question. If the team has explicitly adopted OCP as a rule, however, that rule has a separate source of authority. **Design advice, team policy, and behavioral contracts call for different kinds of reasons.** None of those reasons appears in the reviewer's sentence. Our concern is how such a reasonless verdict might acquire **the force of an axiom that no one declared**.

For Naur [1], programming involves building a theory of the problem a program solves, not simply producing code. Changes demand that understanding. Toulmin's account of argument [2] gives us another way to ask what is missing: a principle can name the claim, but the grounds that warrant its use still have to be supplied. Applied to a code review, the question becomes sharper. **When is the name enough to justify the verdict?**

## 2. A contextual atlas, not an absolute law

What if familiar design principles are describing different regions of the same engineering landscape? SOLID, DRY, YAGNI, information hiding, and design patterns address directions of change, preserved behavior, dependencies, and coordination costs from different angles. An extension mechanism may justify its upfront complexity when variants are likely to recur; when demand is unlikely, the same mechanism may only add work. The useful question is not which of OCP or YAGNI wins everywhere. **Under which demands does each piece of advice hold, and what should we compare where their domains overlap?**

Our **contextual principle atlas** is a way to keep track of these questions. An entry records not only the named principle but anticipated changes, preserved behavior, available designs, the authority of team rules, evaluation criteria, and the evidence at hand. Placing supporting and defeating cases side by side makes their boundaries visible. Missing evidence leaves a judgment open; conflicting evidence remains in view rather than being forced into a single score. Local accounts may join into a larger picture—or fail to fit. **The higher structure worth seeking may be less a law that erases differences than a relation that explains where those differences arise.**

## 3. What mathematics does the atlas need?

Collect the contexts that support a principle, and we obtain a set; compare such sets by inclusion, and formal concept analysis [7] becomes a useful reference. But domains alone do not capture the history of a judgment. Supporting and defeating arguments may coexist, and new evidence may revise the recommendation. Belnap's many-valued logic [8] helps frame the first difficulty; AGM belief revision [3] offers a point of comparison for the second. Joining judgments from different contexts raises a further question: what must remain invariant as the context changes? Institution theory [9] provides one formal reference. **Ordering domains and recording conflicting evidence are distinct tasks; revising either record or transferring it to another domain requires additional rules.** This leads to a more precise question: what must be preserved when a design judgment moves from one context to another?

Engineering design has long been tied to change. Parnas [4] asked how systems should be divided into modules; Baldwin [5] revisited the assumptions and limits of design-rules theory. The atlas asks a different question beside theirs: **Beyond whether an architecture accommodates change, what warrants the advice to choose it, and under which circumstances does that warrant fail?**

## 4. Who gets to define a good design?

Suppose a search algorithm selects an optimal architecture. Optimal with respect to what? A design that minimizes near-term implementation effort need not minimize the cost of later changes. In search-based software design, as Räihä [6] discusses, both representation and fitness-function choice matter. **The fitness function is itself a selected evaluative criterion.** The atlas must therefore record the standards behind a recommendation as well as its evidence. An authorized rule, a behavioral obligation, and an estimate of maintenance cost cannot be substituted for one another merely by placing them in a single score.

## 5. Does the atlas earn its keep?

Whether an atlas helps in practice is a separate question. Give independent reviewers the same code-change case and evidence, then ask whether they can consistently record a principle's grounds and revise the record when a counterexample appears. Compare their work with an ordinary design checklist and existing specification or design-analysis methods. Measure reproducibility, appropriate abstention, the quality of revision, and the time spent recording the reasons. **If the atlas makes judgments no clearer while imposing more work, it has lost its practical case.**

## Conclusion

**How does design advice acquire the authority of an undeclared axiom? Might the scope and grounds of our familiar principles reveal structures we have yet to describe?** A contextual atlas is one way to pursue both questions: locate the regions in which a judgment holds, then ask which of its reasons survive when the conditions change. A principle is neither something to discard casually nor something to exempt from examination. **What matters is not only whether its name survives, but whether the reasoning that once justified it survives with it.**

---

## References and evidence provenance

[1] Naur, P. (1985). Programming as Theory Building. *Microprocessing and Microprogramming*, 15, 253–261. [Owned primary PDF](https://drive.google.com/file/d/1h6omxTHbuPYrKe_hjf0U_BtYCs1s8OgC/view). Reopened directly, abstract and introductory position checked.

[2] Toulmin, S. (1958; 2003 updated edition). *The Uses of Argument*. [Owned book](https://drive.google.com/file/d/1gP-zJtB9YRYrbfwWwKwXl2GMWsobMizO/view). Relevant sections already reviewed in v37 archive; direct text not rechecked in this particular revision. Argumentation link is our interpretation.

[3] Alchourrón, C. E., Gärdenfors, P., & Makinson, D. (1985). On the Logic of Theory Change: Partial Meet Contraction and Revision Functions. *Journal of Symbolic Logic*, 50(2), 510–530. [Owned PDF](https://drive.google.com/file/d/1nCMd4zfQcbr28HJkmFqRvHFsGWh8QabQ/view).

[4] Parnas, D. L. (1972). On the Criteria To Be Used in Decomposing Systems into Modules. *Communications of the ACM*, 15(12), 1053–1058. [Owned primary PDF](https://drive.google.com/file/d/1EcQRy3iehx4lUN7uGsZ1BFXU33HggcEQ/view). Reopened directly, abstract and introduction checked. See also Parnas (1979), [Designing Software for Ease of Extension and Contraction](https://drive.google.com/file/d/1XGzB9hq_6wk6aXeVojMo1IeKoKCg704j/view).

[5] Baldwin, C. Y. (2023). *Design Rules: Past and Future*. [Owned PDF](https://drive.google.com/file/d/14QDJGv1bN_42BY-d15gnX2svKDXkE04Q/view). Previously reviewed in R54–R58.

[6] Räihä, O. (2010). A Survey on Search-Based Software Design. *Computer Science Review*, 4, 203–249. https://doi.org/10.1016/j.cosrev.2010.06.001. [Owned primary PDF](https://drive.google.com/file/d/1BdFL0tU7Nna7jqQM0oPK6Ds1wdtyZS8S/view). Reopened directly, abstract and introductory scope checked.

[7] Ganter, B. & Wille, R. (1999). *Formal Concept Analysis: Mathematical Foundations*. Springer. [Publisher](https://link.springer.com/book/10.1007/978-3-642-59830-2). Owned book filed in 11_BOOKS; the comparison is background mathematical prior art.

[8] Belnap, N. D., Jr. (1977). A Useful Four-Valued Logic. In *Modern Uses of Multiple-Valued Logic*, 8–37. Springer/Reidel. https://doi.org/10.1007/978-94-010-1161-7_2. The information ordering and support/defeat distinction are existing mathematical ideas; this paper does not claim their invention. Also compare earlier Dunn-related four-valued semantics, without treating it as evidence of a proven software-design atlas.

[9] Goguen, J. A. & Burstall, R. M. (1992). Institutions: Abstract Model Theory for Specification and Programming. *Journal of the ACM*, 39(1), 95–146. [Edinburgh bibliographic repository](https://www.lfcs.inf.ed.ac.uk/reports/90/ECS-LFCS-90-106/). Existing abstract model theory, not a finished software heuristic atlas.

## Claim/evidence and release boundaries

- The OCP reviewer sentence and extension-versus-simplicity example are illustrative, not observed study data.
- The atlas is a proposed representation and research agenda, not a formally proved object with verified empirical predictive validity.
- The novel-*question* claim is deliberately narrower than a novelty or first-publication claim; further systematic literature review is needed for the latter.
- Behavioral contracts, authorized policies, and cost heuristics are different judgment types, which cannot be collapsed without additional semantics.
- v37 and v38 remain preserved separately. v35 empirical programme remains separate; LAW-R2 remains HOLD.
- This is a finished *draft manuscript* for author sign-off, not a claim of peer review, journal acceptance, or completed empirical validation.
