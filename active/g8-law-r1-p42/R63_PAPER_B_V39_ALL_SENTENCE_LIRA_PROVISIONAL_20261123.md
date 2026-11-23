# EvoNOMOS Paper B v39 — LIRA full sentence census (R63)

Exact source: main/PAPER_B_BILINGUAL_POSITION_39_FINAL_CANDIDATE_20261123.md, SHA 72278d5b1d23f39cdaaade86979708c2abfb5c0b. This is an **initial sentence-by-sentence editorial screening**, not an objective sentence-quality dataset. Scores are the reviewing assistant's subjective keep-as-written recommendations (0–1), distinct from source reliability and scientific merit. Segmentation on punctuation is mechanical and may split at abbreviation/inline citation boundaries; surrounding paragraphs govern decisions. No numerical target for distribution. RAVEL S0–S3: author anchors preserved; response to user's complaints of defensive and machine-like prose.

Scoring prefilter: strong core voice ~0.97, redundant defense ~0.21–0.35, generic transition ~0.51, prior-art shield ~0.59, ordinary connecting sentence ~0.83. **Scores are triage flags; decisions require contextual reading, not automatic adoption.** No external reviewer participated. This ledger is explicitly provisional until each sentence is independently scrutinized.

| ID | Retain | Diagnosis | Exact source sentence |
| --- | ---: | --- | --- |
| KA.01.01 | 0.83 | FLOW / inspect rhetoric | SOLID, DRY, YAGNI와 같은 소프트웨어 설계 원칙은 유용한 경험적 지침이지만, 실제 설계 판단에서는 적용 조건을 밝히지 않은 채 판정의 근거처럼 사용될 수 있다. |
| KA.01.02 | 0.69 | METADISCOURSE / directness | 본 논문은 설계 휴리스틱, 팀이 승인한 규칙, 보존해야 할 동작 계약을 구별하고, 원칙의 정당화 근거를 변경 요구·비용·증거에 따라 추적하는 **맥락별 원칙 지도(contextual principle atlas)**를 연구 대상으로 제안한다. |
| KA.01.03 | 0.83 | FLOW / inspect connective | 여기서 지도는 모든 원칙을 환원하는 단일한 공리계가 아니라, 서로 부분적으로 겹치거나 충돌하는 판단 영역을 기록하는 구조다. |
| KA.01.04 | 0.83 | FLOW / inspect connective | 형식개념분석, 다치논리, 신념 수정, 형식명세 이론은 이 질문을 다룰 기존 도구이지만 지도 자체의 실증적 유효성이나 수학적 독창성을 증명하지 않는다. |
| KA.01.05 | 0.83 | FLOW / inspect connective | 핵심 질문은 원칙에 부여된 권위의 출처와, 맥락 변화 앞에서 어떤 판단을 보존·수정·유보해야 하는가에 있다. |
| K1.01.01 | 0.83 | FLOW / inspect connective | 소프트웨어 개발자는 SOLID, DRY, KISS, YAGNI처럼 이름이 붙은 설계 원칙을 배운다. |
| K1.01.02 | 0.83 | FLOW / inspect connective | 이 이름들은 경험을 나누고 어려운 설계 결정을 설명하는 데 유용하다. |
| K1.01.03 | 0.96 | OPENING / protect | 그런데 코드 리뷰에서 “OCP를 어겼으니 고쳐야 한다”는 말이 나오면, 그 판단을 뒷받침하는 조건은 어디에 있는가? |
| K1.01.04 | 0.83 | FLOW / inspect connective | 지금 바뀔 가능성이 높은 것이 무엇인지, 어떤 기존 동작을 보존해야 하는지, 그 변경을 누가 요청했는지에 따라 답은 달라질 수 있다. |
| K1.01.05 | 0.83 | FLOW / inspect connective | 물론 팀이 OCP 준수를 명시적으로 요구했다면 따라야 할 프로젝트 규칙이 있을 수도 있다. |
| K1.01.06 | 0.83 | FLOW / inspect connective | 문제는 **설계에 관한 조언, 프로젝트가 승인한 규칙, 반드시 성립해야 할 동작의 계약을 같은 종류의 명제로 취급하는 순간** 생긴다. |
| K1.01.07 | 0.21 | DEFENSE / move to notes | 우리는 SOLID가 정식 수학적 공리로 선언되었다고 주장하지 않는다. |
| K1.01.08 | 0.97 | VOICE / protect | 다만 **선언되지 않은 공리 같은 권위**가 어떤 상황에서 생겨날 수 있는지 묻는다. |
| K1.02.01 | 0.83 | FLOW / inspect connective | 프로그래밍을 결과물의 생산보다 개발자의 *이론 형성*에 가깝게 본 Naur [1]의 논의는 이 질문에 오래된 토대를 제공한다. |
| K1.02.02 | 0.83 | FLOW / inspect connective | 프로그램을 변경하는 데 필요한 것은 코드와 문서만이 아니라 그 프로그램이 해결하려는 문제에 관한 이해라는 것이다. |
| K1.02.03 | 0.83 | FLOW / inspect rhetoric | Toulmin [2]의 논증 이론도 주장과 이를 정당화하는 근거를 구별하게 한다. |
| K1.02.04 | 0.31 | DEFENSE / move to provenance | 두 저자가 현대의 SOLID 원칙이나 우리의 지도 개념을 제시한 것은 아니다. |
| K1.02.05 | 0.97 | VOICE / protect | 그러나 이들의 논의를 오늘날의 설계 판단에 적용하면, **원칙의 이름은 논증의 출발점일 수 있어도 그 논증에 필요한 근거 전체를 대신하지는 못한다**는 질문이 생긴다. |
| K1.02.06 | 0.97 | VOICE / protect | 그 이름이 언제 충분한 이유가 되는지는 별도로 설명해야 한다. |
| K2.01.01 | 0.51 | GENERIC-TRANSITION / replace with concrete argument | 여기서 더 큰 가능성을 생각해 볼 수 있다. |
| K2.01.02 | 0.83 | FLOW / inspect rhetoric | SOLID의 다섯 원칙, DRY, YAGNI, 정보 은닉, 디자인 패턴은 하나의 공리계에서 연역된 정리가 아닐 수 있다. |
| K2.01.03 | 0.83 | FLOW / inspect connective | 오히려 변경의 방향, 보존할 기능, 의존 관계, 협업의 비용이라는 서로 다른 문제를 비추는 **부분적인 지도**에 가까울지도 모른다. |
| K2.01.04 | 0.83 | FLOW / inspect connective | 반복적인 확장을 예상할 때는 확장 지점을 미리 마련하는 편이 유리할 수 있지만, 그런 수요가 거의 없다면 같은 구조는 불필요한 복잡성이 될 수 있다. |
| K2.01.05 | 0.35 | DEFENSE / manuscript provenance | 이는 OCP와 YAGNI의 우열이 언제나 뒤집힌다는 실측 결과가 아니라, 판단에 필요한 전제가 달라질 수 있다는 개념적 예다. |
| K2.01.06 | 0.83 | FLOW / inspect connective | 두 원칙이 각기 어떤 문제에서 효력을 갖는지, 영역이 겹칠 때 무엇을 우선할지 묻는 편이 더 생산적이다. |
| K2.02.01 | 0.69 | METADISCOURSE / directness | 우리는 이를 **설계 원칙의 맥락별 지도(contextual principle atlas)**라는 연구 대상으로 제안한다. |
| K2.02.02 | 0.92 | CORE / protect | 하나의 판단 기록에는 적어도 (i) 예상되는 변경 요구, (ii) 보존할 동작 계약, (iii) 허용되는 설계 대안, (iv) 명시적으로 승인된 팀의 규칙, (v) 비용 및 평가 기준, (vi) 현재의 지지·반박 증거가 구별되어야 한다. |
| K2.02.03 | 0.83 | FLOW / inspect connective | 이 기록을 통해 원칙의 적용 영역과 예외가 부분적으로 겹치는 관계를 탐구할 수 있다. |
| K2.02.04 | 0.83 | FLOW / inspect connective | 불확실한 영역에서 결론을 유보하는 것은 지도의 결함이 아니다. |
| K2.02.05 | 0.83 | FLOW / inspect connective | 동일한 맥락에서 지지 근거와 반박 근거가 함께 존재한다면 둘 중 하나를 지우기보다 그 갈등 자체를 기록해야 한다. |
| K2.02.06 | 0.72 | CONTRAST / check if needed | **여기서 지도는 특정 좌표계나 미분가능한 다양체를 뜻하지 않으며, 전체 설계 판단이 하나의 절대적 수학 체계로 환원된다고 전제하지 않는다.** |
| K3.01.01 | 0.83 | FLOW / inspect connective | 이러한 지도에서 원칙의 적용 영역을 맥락의 부분집합으로 표현하거나 포함관계에 따라 비교할 수 있을 것이다. |
| K3.01.02 | 0.59 | PRIOR-ART useful but over-explained | 그러나 집합의 포함관계와 개념격자는 이미 수학적으로 잘 연구되어 있으며, Ganter와 Wille [7]의 형식개념분석이 대표적이다. |
| K3.01.03 | 0.83 | FLOW / inspect connective | 지지와 반박이 동시에 존재하는 상태를 표현하는 다치논리 역시 기존 연구에 속한다 [8]. |
| K3.01.04 | 0.83 | FLOW / inspect connective | 새로운 정보가 들어왔을 때 판단을 어떻게 수정할지는 AGM의 신념 수정 [3]과 비교할 수 있고, 서로 다른 형식체계 사이에서 의미 보존을 논하는 institution 이론 [9]은 국소 지도를 연결하려는 시도에 엄격한 기준을 제공한다. |
| K3.01.05 | 0.31 | DEFENSE / move to provenance | 이들 이론이 **소프트웨어 설계 원칙을 이미 하나로 통일했다거나, 우리가 그보다 새로운 격자 정리를 발견했다는 뜻은 아니다**. |
| K3.01.06 | 0.83 | FLOW / inspect connective | 여러 구조가 부분적으로만 맞물리고 서로 환원되지 않는 결과도 충분히 가능하다. |
| K3.02.01 | 0.83 | FLOW / inspect connective | 소프트웨어 설계 자체에도 더 오래된 기준이 있다. |
| K3.02.02 | 0.83 | FLOW / inspect rhetoric | Parnas [4]는 모듈을 어떤 원칙으로 나누는지가 변경과 이해 가능성에 미치는 영향을 논했고, Baldwin [5]은 모듈성 이론의 가정과 한계를 재검토했다. |
| K3.02.03 | 0.83 | FLOW / inspect connective | 따라서 “설계를 변경 요구와 연결한다”는 설명만으로는 새로운 이론이 되지 않는다. |
| K3.02.04 | 0.83 | FLOW / inspect connective | 본 제안의 구별되는 연구 과제는 **각 원칙의 적용 영역에 더해, 그 판단이 무엇으로 정당화되며 어떤 종류의 권위에 의존하는지 함께 기록할 수 있는가**를 검증하는 데 있다. |
| K4.01.01 | 0.83 | FLOW / inspect connective | 소프트웨어 구조를 자동 탐색하는 알고리즘이 특정 설계를 최적으로 선택하더라도 그 결론은 선택된 목적함수와 제약에 상대적이다. |
| K4.01.02 | 0.83 | FLOW / inspect rhetoric | Räihä [6]의 탐색 기반 소프트웨어 설계 연구는 표현 방식과 적합도 함수의 선택 자체가 중요한 설계 결정임을 보여 준다. |
| K4.01.03 | 0.83 | FLOW / inspect connective | 따라서 **목적함수 역시 누군가 선택한 판단 기준**이며, 최적화 알고리즘의 결과만으로 좋은 설계의 보편적 법칙이 입증되지는 않는다. |
| K4.01.04 | 0.83 | FLOW / inspect connective | 게다가 프로젝트가 채택한 정책은 지켜야 할 조직적 규칙일 수 있고, 동작 계약은 검증할 의미론적 의무이며, 유지보수 휴리스틱은 비교가 필요한 조건부 조언이다. |
| K4.01.05 | 0.83 | FLOW / inspect connective | 세 종류를 하나의 품질 점수로 뭉개면 평가 기준이 어디서 왔는지 알 수 없게 된다. |
| K5.01.01 | 0.92 | CORE / protect | 맥락별 지도가 유용한지 확인하려면 우선 실제 코드 변경 사례에서 독립적인 평가자들이 동일한 요구·계약·증거를 보고 원칙의 근거와 적용 범위를 얼마나 일관되게 기록하는지 살펴야 한다. |
| K5.01.02 | 0.83 | FLOW / inspect connective | 이후 단순한 설계 검토 체크리스트, 기존 형식적 명세 방식, source-aware 설계 분석과 비교하여 판단의 재현성, 유보의 적절성, 반례에 따른 개정 가능성을 평가할 수 있다. |
| K5.01.03 | 0.83 | FLOW / inspect connective | 이 접근이 더 많은 비용을 들이면서도 기존 방법보다 설명력이나 예측력을 개선하지 못한다면 새로운 지도의 실질적 가치에 의문을 제기해야 한다. |
| K5.01.04 | 0.31 | DEFENSE / move to provenance | 그 검증은 아직 수행되지 않았으며, 설계 원칙이 현실에서 얼마나 자주 ‘공리처럼’ 강제되는지도 측정하지 않았다. |
| K5.01.05 | 0.21 | DEFENSE / move to notes | 따라서 우리는 **연구 질문과 형식적 가능성**을 제안하는 것이지, 완성된 경험 법칙을 보고하는 것이 아니다. |
| KC.01.01 | 0.83 | FLOW / inspect rhetoric | EvoNOMOS가 제기하려는 질문은 두 가지다. |
| KC.01.02 | 0.92 | CORE / protect | **설계 원칙은 어떤 근거에서 공리처럼 강제될 수 있으며, 우리가 익숙한 이름으로 부르는 원칙들 위에는 아직 충분히 드러나지 않은 구조가 있는가?** 이제 두 질문은 맥락별 지도라는 한 가지 연구 프로그램에서 만난다. |
| KC.01.03 | 0.72 | CONTRAST / check if needed | 하지만 그 지도의 목적은 모든 원칙에 절대적인 순위를 매기는 데 있지 않다. |
| KC.01.04 | 0.83 | FLOW / inspect connective | 오히려 하나의 판단이 성립하는 영역, 다른 영역으로 이동할 때 보존해야 할 조건, 새로운 반례 앞에서 수정해야 할 근거를 드러내는 데 있다. |
| KC.01.05 | 0.83 | FLOW / inspect connective | 원칙은 버릴 대상도, 시험을 면제받을 대상도 아니다. |
| KC.01.06 | 0.99 | AUTHORIAL ENDING / protect | **이름이 남는 것보다 중요한 것은 그 이름을 정당화했던 사유가 남는 일이다.** |
| EA.01.01 | 0.83 | FLOW / inspect rhetoric | Software design principles such as SOLID, DRY, and YAGNI compress valuable experience. |
| EA.01.02 | 0.83 | FLOW / inspect rhetoric | Yet their names can also be invoked as if they alone justified a design verdict, without stating the conditions under which the advice applies. |
| EA.01.03 | 0.69 | METADISCOURSE / directness | This position paper distinguishes defeasible heuristics from authorized project policies and behavioral contracts, and proposes a **contextual principle atlas**: a research programme for recording the domains, warrants, counterevidence, and revisions of design judgments. |
| EA.01.04 | 0.72 | CONTRAST / check if needed | An atlas need not be a single universal axiom system. |
| EA.01.05 | 0.83 | FLOW / inspect rhetoric | Formal concept analysis, many-valued logics, belief revision, and institution theory provide prior mathematical tools, not proof of a new theory of software design. |
| EA.01.06 | 0.83 | FLOW / inspect rhetoric | The question is whether representing a principle together with its context and source of authority enables more explicit and revisable reasoning about evolving software systems. |
| E1.01.01 | 0.83 | FLOW / inspect rhetoric | Software developers learn design principles with memorable names: SOLID, DRY, KISS, YAGNI. |
| E1.01.02 | 0.83 | FLOW / inspect rhetoric | These names help share experience and explain difficult choices. |
| E1.01.03 | 0.96 | OPENING / protect | But when a reviewer says, “This violates OCP, so it must be fixed,” where are the conditions that warrant the verdict? |
| E1.01.04 | 0.83 | FLOW / inspect rhetoric | The answer depends partly on the changes that are likely, the existing behavior that must survive, and who has requested or authorized the change. |
| E1.01.05 | 0.83 | FLOW / inspect rhetoric | A team may deliberately adopt OCP as a binding local policy. |
| E1.01.06 | 0.83 | FLOW / inspect rhetoric | The problem arises **when advice about design, duly authorized project rules, and behavioral contracts are treated as the same kind of proposition**. |
| E1.01.07 | 0.21 | DEFENSE / move to notes | We do not claim that SOLID was formally declared a mathematical axiom. |
| E1.01.08 | 0.83 | FLOW / inspect rhetoric | We ask instead when advice might acquire **the force of an axiom that was never declared**. |
| E1.02.01 | 0.83 | FLOW / inspect rhetoric | Peter Naur's account of programming as *theory building* [1] offers an older starting point. |
| E1.02.02 | 0.72 | CONTRAST / check if needed | Changing a program requires a situated understanding of the problem, not simply access to code and documentation. |
| E1.02.03 | 0.83 | FLOW / inspect rhetoric | Stephen Toulmin's account of argument [2] likewise directs attention to the grounds on which claims are warranted. |
| E1.02.04 | 0.31 | DEFENSE / move to provenance | Neither author presented our atlas or a theory of SOLID. |
| E1.02.05 | 0.83 | FLOW / inspect rhetoric | Their work nevertheless motivates a distinction in current design discussions: naming a principle can start an argument, but cannot, by itself, provide all the premises that justify a recommendation. |
| E1.02.06 | 0.97 | VOICE / protect | **The missing warrants matter.** |
| E2.01.01 | 0.51 | GENERIC-TRANSITION / replace with concrete argument | A larger possibility follows. |
| E2.01.02 | 0.72 | CONTRAST / check if needed | The five SOLID principles, DRY, YAGNI, information hiding, and design patterns need not be theorems of one universal calculus. |
| E2.01.03 | 0.83 | FLOW / inspect rhetoric | They may be **partial maps** of different concerns: anticipated changes, preserved behavior, dependencies, and the costs of coordinating work. |
| E2.01.04 | 0.83 | FLOW / inspect rhetoric | Preparing an extension mechanism may help when new variants will recur, yet impose unnecessary complexity when they will not. |
| E2.01.05 | 0.35 | DEFENSE / manuscript provenance | This is a conditional illustration, not a measurement of the relative success of OCP and YAGNI. |
| E2.01.06 | 0.83 | FLOW / inspect rhetoric | The more interesting questions concern the domains in which each recommendation is defensible and how to reason when those domains overlap. |
| E2.02.01 | 0.69 | METADISCOURSE / directness | We call the proposed object a **contextual principle atlas**. |
| E2.02.02 | 0.92 | CORE / protect | A design judgment would record at least its anticipated changes, behavioral contract, available alternatives, explicitly authorized policies, evaluation criteria, and current supporting and defeating evidence. |
| E2.02.03 | 0.83 | FLOW / inspect rhetoric | The atlas would therefore represent not just named principles but their scope and warrants. |
| E2.02.04 | 0.83 | FLOW / inspect rhetoric | When evidence is missing, abstention is permissible; when support and defeat coexist, neither need be erased. |
| E2.02.05 | 0.35 | DEFENSE / manuscript provenance | The word *atlas* does not assert that software principles inhabit a differentiable manifold, that their local accounts satisfy a mathematical gluing theorem, or that all principles must reduce to one absolute structure. |
| E3.01.01 | 0.83 | FLOW / inspect rhetoric | There are existing mathematical ways to describe portions of such an atlas. |
| E3.01.02 | 0.83 | FLOW / inspect rhetoric | Order theory and formal concept analysis [7] can represent inclusion relations among domains. |
| E3.01.03 | 0.59 | PRIOR-ART useful but over-explained | Many-valued logics [8] have already distinguished absent evidence from conflicting evidence. |
| E3.01.04 | 0.83 | FLOW / inspect rhetoric | Belief revision [3] studies how commitments may be altered in response to new information. |
| E3.01.05 | 0.83 | FLOW / inspect rhetoric | Institution theory [9] offers formal constraints for transporting satisfaction across differing signatures. |
| E3.01.06 | 0.31 | DEFENSE / move to provenance | Their existence does not unify software design principles; it also precludes presenting a powerset lattice or four-valued evidence state as an original mathematical discovery. |
| E3.01.07 | 0.83 | FLOW / inspect rhetoric | Several partially connected, irreducible structures may be required. |
| E3.02.01 | 0.59 | PRIOR-ART useful but over-explained | Software engineering also has substantial prior art. |
| E3.02.02 | 0.83 | FLOW / inspect rhetoric | Parnas [4] examined how criteria for modular decomposition influence comprehensibility and change. |
| E3.02.03 | 0.83 | FLOW / inspect rhetoric | Baldwin [5] revisited assumptions and limitations in design-rules theory. |
| E3.02.04 | 0.83 | FLOW / inspect rhetoric | Merely proposing to relate architecture to likely changes is therefore not a novel contribution. |
| E3.02.05 | 0.83 | FLOW / inspect rhetoric | Our narrower research question is whether **scope, type of obligation, source of authority, and defeasible support can be represented together in design arguments**, and whether doing so adds value beyond existing methods. |
| E4.01.01 | 0.83 | FLOW / inspect rhetoric | An algorithm that searches for an optimal architecture does so relative to a chosen representation, objective function, and constraints. |
| E4.01.02 | 0.83 | FLOW / inspect rhetoric | Räihä's survey of search-based software design [6] explicitly discusses the importance of representation and fitness-function choices. |
| E4.01.03 | 0.72 | CONTRAST / check if needed | The **fitness function is itself a selected evaluative criterion**; the discovery of an optimum does not turn that criterion into a universal law of good design. |
| E4.01.04 | 0.83 | FLOW / inspect rhetoric | A policy's authority, a behavioral specification's validity, and a heuristic's context-dependent utility cannot be safely collapsed into one undifferentiated quality score. |
| E4.01.05 | 0.72 | CONTRAST / check if needed | An atlas should keep visible not only what a principle recommends, but who chose the standard by which that recommendation is evaluated. |
| E5.01.01 | 0.83 | FLOW / inspect rhetoric | The atlas must earn its usefulness. |
| E5.01.02 | 0.83 | FLOW / inspect rhetoric | One test would ask independent reviewers to annotate real code-change cases, separating required behavior, authorized policy, design heuristics, contrary evidence, and reasons for revising prior advice. |
| E5.01.03 | 0.83 | FLOW / inspect rhetoric | Their judgments could be compared with simpler design checklists, established specification techniques, and source-aware design baselines for reproducibility, appropriate abstention, and explanatory value. |
| E5.01.04 | 0.83 | FLOW / inspect rhetoric | If the atlas adds annotation costs without improving these outcomes, the claimed practical benefit weakens. |
| E5.01.05 | 0.31 | DEFENSE / move to provenance | No such empirical evaluation is reported here, and the prevalence of axiom-like appeals to design principles has not been measured. |
| E5.01.06 | 0.21 | DEFENSE / move to notes | The proposal remains a **conceptual research programme**, not an established mathematical or empirical law. |
| EC.01.01 | 0.72 | CONTRAST / check if needed | EvoNOMOS begins with two questions: **On what grounds can design advice acquire axiom-like authority, and might our familiar principles be fragments of structures we have not yet adequately described?** A contextual atlas gives these questions a shared research direction without presupposing a universal ordering of principles. |
| EC.01.02 | 0.83 | FLOW / inspect rhetoric | It asks where a judgment is warranted, what must be preserved as circumstances change, and which reasons must be revised in the face of new evidence. |
| EC.01.03 | 0.83 | FLOW / inspect rhetoric | A principle is neither something to discard casually nor something to exempt from examination. |
| EC.01.04 | 0.99 | AUTHORIAL ENDING / protect | **What matters is not only whether its name survives, but whether the reasoning that once justified it survives with it.** |

## RAVEL checkpoints
- S0 SOURCE: v39 exact SHA; v37 protected as reference; LIRA doctrine checked.
- S1 ARGUMENT: authority question → contextual atlas → earlier mathematics → evaluator authority → falsification.
- S2–S3: identify dominant defect types, then rewrite opening/abstract/atlas in v40. Protect strong original lines.
- S4 STITCH: inspect neighboring paragraphs, avoid repeated 'A not B' and citation dumping.
- S5 ADVERSARIAL: distinguish honest qualifiers from reflexive self-defense; move provenance controls to separate notes.
- S6 FREEZE: pending; revise v40 and compare Korean/English content before freezing.

## Editorial principle
A defense sentence cannot be deleted if its removal would upgrade a speculative claim into factual discovery. Prefer embedding modest scope in positive claims and keeping actual epistemic limits in a short endnote rather than rehearsing disclaimers at every transition.
