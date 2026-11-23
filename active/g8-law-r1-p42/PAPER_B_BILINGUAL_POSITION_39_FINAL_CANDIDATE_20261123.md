# 공리로 선언한 적 없는 원칙들: 설계 원칙의 맥락별 지도를 향하여
*The Axioms We Never Declared: Toward a Contextual Atlas of Software Design Principles*

**EvoNOMOS · Paper B · v39 · completed author-review candidate · 2026-11-23**

**Genre:** bilingual conceptual position paper. **Claim type:** philosophical and programmatic proposal, not a new mathematics theorem, empirical finding, or a validated tool. **Status:** COMPLETE MANUSCRIPT / AUTHOR SIGN-OFF PENDING.

## 초록

SOLID, DRY, YAGNI와 같은 소프트웨어 설계 원칙은 유용한 경험적 지침이지만, 실제 설계 판단에서는 적용 조건을 밝히지 않은 채 판정의 근거처럼 사용될 수 있다. 본 논문은 설계 휴리스틱, 팀이 승인한 규칙, 보존해야 할 동작 계약을 구별하고, 원칙의 정당화 근거를 변경 요구·비용·증거에 따라 추적하는 **맥락별 원칙 지도(contextual principle atlas)**를 연구 대상으로 제안한다. 여기서 지도는 모든 원칙을 환원하는 단일한 공리계가 아니라, 서로 부분적으로 겹치거나 충돌하는 판단 영역을 기록하는 구조다. 형식개념분석, 다치논리, 신념 수정, 형식명세 이론은 이 질문을 다룰 기존 도구이지만 지도 자체의 실증적 유효성이나 수학적 독창성을 증명하지 않는다. 핵심 질문은 원칙에 부여된 권위의 출처와, 맥락 변화 앞에서 어떤 판단을 보존·수정·유보해야 하는가에 있다.

**주제어:** 설계 원칙, 정당화 근거, 맥락, 공리화, 소프트웨어 진화, 비단조 추론, 설계 평가

## 1. 판단의 이름과 판단의 이유

소프트웨어 개발자는 SOLID, DRY, KISS, YAGNI처럼 이름이 붙은 설계 원칙을 배운다. 이 이름들은 경험을 나누고 어려운 설계 결정을 설명하는 데 유용하다. 그런데 코드 리뷰에서 “OCP를 어겼으니 고쳐야 한다”는 말이 나오면, 그 판단을 뒷받침하는 조건은 어디에 있는가? 지금 바뀔 가능성이 높은 것이 무엇인지, 어떤 기존 동작을 보존해야 하는지, 그 변경을 누가 요청했는지에 따라 답은 달라질 수 있다. 물론 팀이 OCP 준수를 명시적으로 요구했다면 따라야 할 프로젝트 규칙이 있을 수도 있다. 문제는 **설계에 관한 조언, 프로젝트가 승인한 규칙, 반드시 성립해야 할 동작의 계약을 같은 종류의 명제로 취급하는 순간** 생긴다. 우리는 SOLID가 정식 수학적 공리로 선언되었다고 주장하지 않는다. 다만 **선언되지 않은 공리 같은 권위**가 어떤 상황에서 생겨날 수 있는지 묻는다.

프로그래밍을 결과물의 생산보다 개발자의 *이론 형성*에 가깝게 본 Naur [1]의 논의는 이 질문에 오래된 토대를 제공한다. 프로그램을 변경하는 데 필요한 것은 코드와 문서만이 아니라 그 프로그램이 해결하려는 문제에 관한 이해라는 것이다. Toulmin [2]의 논증 이론도 주장과 이를 정당화하는 근거를 구별하게 한다. 두 저자가 현대의 SOLID 원칙이나 우리의 지도 개념을 제시한 것은 아니다. 그러나 이들의 논의를 오늘날의 설계 판단에 적용하면, **원칙의 이름은 논증의 출발점일 수 있어도 그 논증에 필요한 근거 전체를 대신하지는 못한다**는 질문이 생긴다. 그 이름이 언제 충분한 이유가 되는지는 별도로 설명해야 한다.

## 2. 하나의 절대 법칙이 아니라 맥락별 지도

여기서 더 큰 가능성을 생각해 볼 수 있다. SOLID의 다섯 원칙, DRY, YAGNI, 정보 은닉, 디자인 패턴은 하나의 공리계에서 연역된 정리가 아닐 수 있다. 오히려 변경의 방향, 보존할 기능, 의존 관계, 협업의 비용이라는 서로 다른 문제를 비추는 **부분적인 지도**에 가까울지도 모른다. 반복적인 확장을 예상할 때는 확장 지점을 미리 마련하는 편이 유리할 수 있지만, 그런 수요가 거의 없다면 같은 구조는 불필요한 복잡성이 될 수 있다. 이는 OCP와 YAGNI의 우열이 언제나 뒤집힌다는 실측 결과가 아니라, 판단에 필요한 전제가 달라질 수 있다는 개념적 예다. 두 원칙이 각기 어떤 문제에서 효력을 갖는지, 영역이 겹칠 때 무엇을 우선할지 묻는 편이 더 생산적이다.

우리는 이를 **설계 원칙의 맥락별 지도(contextual principle atlas)**라는 연구 대상으로 제안한다. 하나의 판단 기록에는 적어도 (i) 예상되는 변경 요구, (ii) 보존할 동작 계약, (iii) 허용되는 설계 대안, (iv) 명시적으로 승인된 팀의 규칙, (v) 비용 및 평가 기준, (vi) 현재의 지지·반박 증거가 구별되어야 한다. 이 기록을 통해 원칙의 적용 영역과 예외가 부분적으로 겹치는 관계를 탐구할 수 있다. 불확실한 영역에서 결론을 유보하는 것은 지도의 결함이 아니다. 동일한 맥락에서 지지 근거와 반박 근거가 함께 존재한다면 둘 중 하나를 지우기보다 그 갈등 자체를 기록해야 한다. **여기서 지도는 특정 좌표계나 미분가능한 다양체를 뜻하지 않으며, 전체 설계 판단이 하나의 절대적 수학 체계로 환원된다고 전제하지 않는다.**

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

Software design principles such as SOLID, DRY, and YAGNI compress valuable experience. Yet their names can also be invoked as if they alone justified a design verdict, without stating the conditions under which the advice applies. This position paper distinguishes defeasible heuristics from authorized project policies and behavioral contracts, and proposes a **contextual principle atlas**: a research programme for recording the domains, warrants, counterevidence, and revisions of design judgments. An atlas need not be a single universal axiom system. Formal concept analysis, many-valued logics, belief revision, and institution theory provide prior mathematical tools, not proof of a new theory of software design. The question is whether representing a principle together with its context and source of authority enables more explicit and revisable reasoning about evolving software systems.

**Keywords:** software design principles, warrants, contextual reasoning, modularity, defeasible arguments, software evolution

## 1. Names and reasons

Software developers learn design principles with memorable names: SOLID, DRY, KISS, YAGNI. These names help share experience and explain difficult choices. But when a reviewer says, “This violates OCP, so it must be fixed,” where are the conditions that warrant the verdict? The answer depends partly on the changes that are likely, the existing behavior that must survive, and who has requested or authorized the change. A team may deliberately adopt OCP as a binding local policy. The problem arises **when advice about design, duly authorized project rules, and behavioral contracts are treated as the same kind of proposition**. We do not claim that SOLID was formally declared a mathematical axiom. We ask instead when advice might acquire **the force of an axiom that was never declared**.

Peter Naur's account of programming as *theory building* [1] offers an older starting point. Changing a program requires a situated understanding of the problem, not simply access to code and documentation. Stephen Toulmin's account of argument [2] likewise directs attention to the grounds on which claims are warranted. Neither author presented our atlas or a theory of SOLID. Their work nevertheless motivates a distinction in current design discussions: naming a principle can start an argument, but cannot, by itself, provide all the premises that justify a recommendation. **The missing warrants matter.**

## 2. A contextual atlas, not an absolute law

A larger possibility follows. The five SOLID principles, DRY, YAGNI, information hiding, and design patterns need not be theorems of one universal calculus. They may be **partial maps** of different concerns: anticipated changes, preserved behavior, dependencies, and the costs of coordinating work. Preparing an extension mechanism may help when new variants will recur, yet impose unnecessary complexity when they will not. This is a conditional illustration, not a measurement of the relative success of OCP and YAGNI. The more interesting questions concern the domains in which each recommendation is defensible and how to reason when those domains overlap.

We call the proposed object a **contextual principle atlas**. A design judgment would record at least its anticipated changes, behavioral contract, available alternatives, explicitly authorized policies, evaluation criteria, and current supporting and defeating evidence. The atlas would therefore represent not just named principles but their scope and warrants. When evidence is missing, abstention is permissible; when support and defeat coexist, neither need be erased. The word *atlas* does not assert that software principles inhabit a differentiable manifold, that their local accounts satisfy a mathematical gluing theorem, or that all principles must reduce to one absolute structure.

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

[8] Dunn, J. M. (1976) and Belnap, N. D. (1977), established four-valued evidence and inference traditions. Bibliographic edition details need a separate citation audit; **do not represent the evidence-pair structure as original**.

[9] Goguen, J. A. & Burstall, R. M. (1992). Institutions: Abstract Model Theory for Specification and Programming. *Journal of the ACM*, 39(1), 95–146. [Edinburgh bibliographic repository](https://www.lfcs.inf.ed.ac.uk/reports/90/ECS-LFCS-90-106/). Existing abstract model theory, not a finished software heuristic atlas.

## Claim/evidence and release boundaries

- The OCP reviewer sentence and extension-versus-simplicity example are illustrative, not observed study data.
- The atlas is a proposed representation and research agenda, not a formally proved object with verified empirical predictive validity.
- The novel-*question* claim is deliberately narrower than a novelty or first-publication claim; further systematic literature review is needed for the latter.
- Behavioral contracts, authorized policies, and cost heuristics are different judgment types, which cannot be collapsed without additional semantics.
- v37 and v38 remain preserved separately. v35 empirical programme remains separate; LAW-R2 remains HOLD.
- This is a finished *draft manuscript* for author sign-off, not a claim of peer review, journal acceptance, or completed empirical validation.
