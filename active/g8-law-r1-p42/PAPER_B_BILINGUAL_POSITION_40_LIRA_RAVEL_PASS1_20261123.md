# 공리로 선언한 적 없는 원칙들: 설계 원칙의 맥락별 지도를 향하여
*The Axioms We Never Declared: Toward a Contextual Atlas of Software Design Principles*

**EvoNOMOS · Paper B · v40 · LIRA/RAVEL local revision · 2026-11-23**

**장르:** 한·영 개념 논문 · **상태:** 저자 검토용 수정판 (v39 보존)

## 초록

설계 원칙은 판단을 돕기 위해 만들어졌지만, 때로는 판단의 이유를 대신한다. 코드 리뷰에서 ‘OCP 위반’이라는 진단만으로 수정이 요구될 때, 그 판단에 필요한 변경 전망과 동작 계약, 비용에 관한 근거는 어디에 있는가? 이 글은 설계 조언과 팀의 승인된 규칙, 동작 계약을 구별하면서, 각 원칙이 언제 정당화되는지를 기록하는 **설계 원칙의 맥락별 지도(contextual principle atlas)**를 제안한다. 이 지도는 원칙의 우열을 한 줄로 세우기보다 적용 영역의 겹침, 판단의 유보, 새로운 증거에 따른 수정을 드러낸다. 관련 수학 이론은 이미 풍부하다. 문제는 그 구조들을 실제 설계 논증의 조건과 연결할 수 있느냐는 데 있다.

**주제어:** 설계 원칙, 정당화 근거, 맥락, 공리화, 소프트웨어 진화, 비단조 추론, 설계 평가

## 1. 판단의 이름과 판단의 이유

코드 리뷰에서 “OCP를 어겼으니 고쳐야 한다”는 말을 들었다고 해 보자. 무엇을 어떻게 고쳐야 할까? 앞으로 늘어날 기능의 종류, 보존해야 할 기존 동작, 지금 변경하는 데 드는 비용을 모른다면 원칙의 이름만으로는 답할 수 없다. 반대로 팀이 OCP 준수를 명시적인 개발 규칙으로 정했다면 그 규칙을 따라야 할 이유가 따로 생긴다. **설계 조언과 팀의 규칙, 프로그램이 지켜야 하는 동작 계약은 서로 다른 근거를 요구한다.** 그런데 코드 리뷰에서는 그 차이가 생략되기 쉽다. SOLID나 DRY처럼 유용한 이름이 때로 **선언되지 않은 공리 같은 권위**를 얻는 순간은 바로 여기에서 출발한다.

Naur [1]는 프로그래밍을 프로그램이라는 결과물을 만드는 일만이 아니라, 개발자가 문제를 이해하고 그 이해를 축적하는 *이론 형성*으로 보았다. 코드가 수정될 때 필요한 것도 바로 그런 이해다. Toulmin [2]의 논증 이론을 빌리면, 설계 원칙의 이름은 주장이고 그 주장이 통할 조건은 별도로 제시해야 하는 정당화 근거에 가깝다. 이 연결을 통해 코드 리뷰에서 빠져 있던 질문이 또렷해진다. **그 이름이 언제 충분한 이유가 되는지는 별도로 설명해야 한다.**

## 2. 하나의 절대 법칙이 아니라 맥락별 지도

설계 원칙들이 서로 다른 문제를 보고 있다면, 원칙마다 유효한 영역을 그려 볼 수 있지 않을까? SOLID의 다섯 원칙, DRY, YAGNI, 정보 은닉, 디자인 패턴은 변경 방향과 기존 동작, 의존 관계, 협업 비용을 각기 다른 각도에서 다룬다. 반복해서 새로운 기능을 붙여야 한다면 확장 지점에 투자할 만하지만, 확장 가능성이 낮다면 같은 장치가 불필요한 복잡성이 될 수 있다. OCP와 YAGNI 중 하나가 언제나 옳다는 문제가 아니다. **어떤 변경 요구 아래에서 각 조언이 유용해지고, 그 영역이 겹치면 무엇을 비교해야 하는가?**

이 글에서 제안하는 **설계 원칙의 맥락별 지도(contextual principle atlas)**는 그런 질문을 기록하는 방법이다. 지도에 적힐 것은 원칙의 이름뿐 아니라 예상되는 변경, 지켜야 할 동작, 선택 가능한 설계, 팀 규칙의 권한, 비용을 판단하는 기준과 실제로 확보된 증거다. 원칙을 지지하는 맥락과 반박하는 맥락을 나란히 놓으면 적용 영역의 경계가 드러난다. 자료가 모자라면 판단을 남겨 두고, 지지와 반박이 함께 나오면 그 갈등도 지운 채 넘기지 않는다. 서로 다른 지역에서 쓰이는 지도들이 한 장으로 이어질 수도 있고, 끝내 맞물리지 않을 수도 있다. **우리가 찾는 상위 구조는 그 차이를 지워 버리는 법칙보다, 차이가 생기는 조건을 설명하는 관계에 가까울 것이다.**

## 3. 수학적 가능성과 먼저 인정해야 할 선행연구

이러한 지도에서 원칙의 적용 영역을 맥락의 부분집합으로 표현하거나 포함관계에 따라 비교할 수 있을 것이다. 그러나 집합의 포함관계와 개념격자는 이미 수학적으로 잘 연구되어 있으며, Ganter와 Wille [7]의 형식개념분석이 대표적이다. 지지와 반박이 동시에 존재하는 상태를 표현하는 다치논리 역시 기존 연구에 속한다 [8]. 새로운 정보가 들어왔을 때 판단을 어떻게 수정할지는 AGM의 신념 수정 [3]과 비교할 수 있고, 서로 다른 형식체계 사이에서 의미 보존을 논하는 institution 이론 [9]은 국소 지도를 연결하려는 시도에 엄격한 기준을 제공한다. 이들 이론이 **소프트웨어 설계 원칙을 이미 하나로 통일했다거나, 우리가 그보다 새로운 격자 정리를 발견했다는 뜻은 아니다**. 여러 구조가 부분적으로만 맞물리고 서로 환원되지 않는 결과도 충분히 가능하다.

소프트웨어 설계 자체에도 더 오래된 기준이 있다. Parnas [4]는 모듈을 어떤 원칙으로 나누는지가 변경과 이해 가능성에 미치는 영향을 논했고, Baldwin [5]은 모듈성 이론의 가정과 한계를 재검토했다. 따라서 “설계를 변경 요구와 연결한다”는 설명만으로는 새로운 이론이 되지 않는다. 본 제안의 구별되는 연구 과제는 **각 원칙의 적용 영역에 더해, 그 판단이 무엇으로 정당화되며 어떤 종류의 권위에 의존하는지 함께 기록할 수 있는가**를 검증하는 데 있다.

## 4. 원칙을 평가하는 기준도 지도에 남겨야 한다

소프트웨어 구조를 자동 탐색하는 알고리즘이 특정 설계를 최적으로 선택하더라도 그 결론은 선택된 목적함수와 제약에 상대적이다. Räihä [6]의 탐색 기반 소프트웨어 설계 연구는 표현 방식과 적합도 함수의 선택 자체가 중요한 설계 결정임을 보여 준다. 따라서 **목적함수 역시 누군가 선택한 판단 기준**이며, 최적화 알고리즘의 결과만으로 좋은 설계의 보편적 법칙이 입증되지는 않는다. 게다가 프로젝트가 채택한 정책은 지켜야 할 조직적 규칙일 수 있고, 동작 계약은 검증할 의미론적 의무이며, 유지보수 휴리스틱은 비교가 필요한 조건부 조언이다. 세 종류를 하나의 품질 점수로 뭉개면 평가 기준이 어디서 왔는지 알 수 없게 된다.

## 5. 제안의 검증 가능성과 한계

맥락별 지도가 유용한지 확인하려면 우선 실제 코드 변경 사례에서 독립적인 평가자들이 동일한 요구·계약·증거를 보고 원칙의 근거와 적용 범위를 얼마나 일관되게 기록하는지 살펴야 한다. 이후 단순한 설계 검토 체크리스트, 기존 형식적 명세 방식, source-aware 설계 분석과 비교하여 판단의 재현성, 유보의 적절성, 반례에 따른 개정 가능성을 평가할 수 있다. 이 접근이 더 많은 비용을 들이면서도 기존 방법보다 설명력이나 예측력을 개선하지 못한다면 새로운 지도의 실질적 가치에 의문을 제기해야 한다. 그 검증은 아직 수행되지 않았으며, 설계 원칙이 현실에서 얼마나 자주 ‘공리처럼’ 강제되는지도 측정하지 않았다. 따라서 우리는 **연구 질문과 형식적 가능성**을 제안하는 것이지, 완성된 경험 법칙을 보고하는 것이 아니다.

## 결론

EvoNOMOS가 제기하려는 질문은 두 가지다. **설계 원칙은 어떤 근거에서 공리처럼 강제될 수 있으며, 우리가 익숙한 이름으로 부르는 원칙들 위에는 아직 충분히 드러나지 않은 구조가 있는가?** 이제 두 질문은 맥락별 지도라는 한 가지 연구 프로그램에서 만난다. 하지만 그 지도의 목적은 모든 원칙에 절대적인 순위를 매기는 데 있지 않다. 오히려 하나의 판단이 성립하는 영역, 다른 영역으로 이동할 때 보존해야 할 조건, 새로운 반례 앞에서 수정해야 할 근거를 드러내는 데 있다. 원칙은 버릴 대상도, 시험을 면제받을 대상도 아니다. **이름이 남는 것보다 중요한 것은 그 이름을 정당화했던 사유가 남는 일이다.**

---

## Abstract

Design principles are meant to guide engineering judgment, yet their names sometimes substitute for its reasons. When a code review demands a change merely because it 'violates OCP,' what happened to the anticipated changes, behavioral obligations, and costs that would warrant that demand? We distinguish design advice from authorized team rules and behavioral contracts, then propose a **contextual principle atlas** to record where each principle is warranted, where its reasons conflict, and how a judgment changes with new evidence. Rather than ranking principles once and for all, the atlas traces overlapping domains and revisable arguments. Existing mathematical theories provide resources for this effort; the open task is to connect those structures to the conditions of actual software design judgments.

**Keywords:** software design principles, warrants, contextual reasoning, modularity, defeasible arguments, software evolution

## 1. Names and reasons

Imagine a code review that ends with: “This violates OCP, so it must be fixed.” What, exactly, should be changed? Without knowing which features are likely to grow, which behaviors must remain intact, and what the change will cost, the name of a principle cannot settle the question. If the team has explicitly adopted OCP as a rule, however, that rule has a separate source of authority. **Design advice, team policy, and behavioral contracts call for different kinds of reasons.** Code reviews can leave those distinctions unstated. That is one route by which useful names such as SOLID and DRY can acquire **the force of axioms that no one declared**.

For Naur [1], programming involves building a theory of the problem a program solves, not simply producing code. Changes demand that understanding. Toulmin's account of argument [2] gives us another way to ask what is missing: a principle can name the claim, but the grounds that warrant its use still have to be supplied. Applied to a code review, the question becomes sharper. **When is the name enough to justify the verdict?**

## 2. A contextual atlas, not an absolute law

What if familiar design principles are describing different regions of the same engineering landscape? SOLID, DRY, YAGNI, information hiding, and design patterns address directions of change, preserved behavior, dependencies, and coordination costs from different angles. An extension mechanism may justify its upfront complexity when variants are likely to recur; when demand is unlikely, the same mechanism may only add work. The useful question is not which of OCP or YAGNI wins everywhere. **Under which demands does each piece of advice hold, and what should we compare where their domains overlap?**

Our **contextual principle atlas** is a way to keep track of these questions. An entry records not only the named principle but anticipated changes, preserved behavior, available designs, the authority of team rules, evaluation criteria, and the evidence at hand. Placing supporting and defeating cases side by side makes their boundaries visible. Missing evidence leaves a judgment open; conflicting evidence remains in view rather than being forced into a single score. Local accounts may join into a larger picture—or fail to fit. **The higher structure worth seeking may be less a law that erases differences than a relation that explains where those differences arise.**

## 3. Mathematical resources and existing design theory

There are existing mathematical ways to describe portions of such an atlas. Order theory and formal concept analysis [7] can represent inclusion relations among domains. Many-valued logics [8] have already distinguished absent evidence from conflicting evidence. Belief revision [3] studies how commitments may be altered in response to new information. Institution theory [9] offers formal constraints for transporting satisfaction across differing signatures. Their existence does not unify software design principles; it also precludes presenting a powerset lattice or four-valued evidence state as an original mathematical discovery. Several partially connected, irreducible structures may be required.

Software engineering also has substantial prior art. Parnas [4] examined how criteria for modular decomposition influence comprehensibility and change. Baldwin [5] revisited assumptions and limitations in design-rules theory. Merely proposing to relate architecture to likely changes is therefore not a novel contribution. Our narrower research question is whether **scope, type of obligation, source of authority, and defeasible support can be represented together in design arguments**, and whether doing so adds value beyond existing methods.

## 4. Who chooses the objective?

An algorithm that searches for an optimal architecture does so relative to a chosen representation, objective function, and constraints. Räihä's survey of search-based software design [6] explicitly discusses the importance of representation and fitness-function choices. The **fitness function is itself a selected evaluative criterion**; the discovery of an optimum does not turn that criterion into a universal law of good design. A policy's authority, a behavioral specification's validity, and a heuristic's context-dependent utility cannot be safely collapsed into one undifferentiated quality score. An atlas should keep visible not only what a principle recommends, but who chose the standard by which that recommendation is evaluated.

## 5. How the proposal could fail

The atlas must earn its usefulness. One test would ask independent reviewers to annotate real code-change cases, separating required behavior, authorized policy, design heuristics, contrary evidence, and reasons for revising prior advice. Their judgments could be compared with simpler design checklists, established specification techniques, and source-aware design baselines for reproducibility, appropriate abstention, and explanatory value. If the atlas adds annotation costs without improving these outcomes, the claimed practical benefit weakens. No such empirical evaluation is reported here, and the prevalence of axiom-like appeals to design principles has not been measured. The proposal remains a **conceptual research programme**, not an established mathematical or empirical law.

## Conclusion

EvoNOMOS begins with two questions: **On what grounds can design advice acquire axiom-like authority, and might our familiar principles be fragments of structures we have not yet adequately described?** A contextual atlas gives these questions a shared research direction without presupposing a universal ordering of principles. It asks where a judgment is warranted, what must be preserved as circumstances change, and which reasons must be revised in the face of new evidence. A principle is neither something to discard casually nor something to exempt from examination. **What matters is not only whether its name survives, but whether the reasoning that once justified it survives with it.**

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
