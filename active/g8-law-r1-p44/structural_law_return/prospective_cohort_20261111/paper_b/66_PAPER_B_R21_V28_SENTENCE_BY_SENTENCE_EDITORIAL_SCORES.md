# Paper B v28 — Every-Sentence Editorial Recommendations
**Scores are subjective editorial willingness-to-retain (0–1), not probabilities, factual correctness, scientific confidence, or calibrated assessments.** Each manuscript sentence receives an ID, full text, rhetorical job and an editorial comment. Colors: green >=0.90, orange 0.65–0.89, red <0.65. The stronger main manuscript is already edited; deliberately weak alternatives are scored separately and *excluded*. No external reviewer.

## 한국어 초록

- **K01.01 · 0.97 · 핵심 질문**: 설계 원칙을 아는 것과 그 원칙으로 특정 코드 수정을 결정할 자격을 갖추는 것은 같은 능력일까?
  - **판단 / note:** 서론과 결론을 붙잡는 한 문장. 원칙 지식과 실제 결정 권한을 구분한다.
- **K01.02 · 0.91 · 전제**: 개방–폐쇄 원칙을 비롯한 SOLID 원칙은 소프트웨어의 변화를 다룰 유용한 언어지만, 어떤 변화를 예상하고 누구의 동작을 지켜야 하는지는 프로젝트마다 다르다.
  - **판단 / note:** 원칙의 유용성과 조건성을 함께 인정하여 허수아비 비판을 피한다.
- **K01.03 · 0.96 · 기여**: AI 코딩 에이전트가 설계 조언을 코드 수정과 검토 결정으로 옮기는 지금, 우리는 그 조언이 언제 근거를 넘어서는 권위를 갖는지 묻는다.
  - **판단 / note:** AI 시대에 질문을 다시 제기할 실천적 이유를 직접 밝힌다.
- **K01.04 · 0.86 · 개념 정의**: 이 가능성을 ‘운영상의 준공리화’라고 부르되, 원칙을 따르는 행위와 잘못된 절대화를 미리 동일시하지 않는다.
  - **판단 / note:** 새 명칭은 유용하지만 수사로 흐를 위험이 있어 낮은 편집 점수를 부여했다.
- **K01.05 · 0.93 · 방법 경계**: 우리는 역사적 원문과 동일 패치의 조건부 판정을 출발점으로 삼고, 실제 에이전트의 패치 선택과 반대 증거 이후의 수정을 시험할 연구 의제를 제안한다.
  - **판단 / note:** 기존 근거와 미실행 후속 실험을 한 문장 안에서 구분한다.
- **K01.06 · 0.95 · 주장 한계**: 이 논문은 새로운 보편 설계 법칙이나 이미 관찰된 에이전트 효과를 발표하지 않는다.
  - **판단 / note:** 포지션 논문의 장르를 보호하는 필수 제한이다.

## 한국어 1. 도형보다 먼저 정해야 할 것

- **K02.01 · 0.91 · 서사 진입**: 1996년 Robert Martin은 새 도형을 쉽게 추가할 수 있는 설계에 다른 요구를 붙였다.
  - **판단 / note:** 초기 01·08판의 가장 살아 있는 사례를 되살린다.
- **K02.02 · 0.97 · 전환**: 이번에는 원을 사각형보다 먼저 그려야 한다.
  - **판단 / note:** 짧게 끊는 문장이지만 요구의 전환 자체를 보여 주므로 필요하다.
- **K02.03 · 0.95 · 논증**: 도형을 하나 더 만드는 일에 유리했던 구조가 순서를 바꾸는 일까지 저절로 해결하지는 않는다.
  - **판단 / note:** 구조와 변경 유형의 차이를 사례에서 직접 읽어 낸다.
- **K02.04 · 0.98 · 질문**: 누가 정렬할 책임을 지는가—도형을 그리는 함수인가, 그 함수를 부르는 쪽인가?
  - **판단 / note:** 독자가 기술적 문제를 붙잡는 장면. 이 문장은 살린다.
- **K02.05 · 0.97 · 전제 결론**: 개방–폐쇄 원칙이라는 이름만으로는 그 책임을 배분할 수 없다.
  - **판단 / note:** 역사 사례에서 본 논문의 추상적 문제로 넘어가는 핵심 연결.
- **K02.06 · 0.95 · AI 연결**: AI가 ‘OCP 위반’이라는 라벨을 붙이는 일과, 그 라벨을 근거로 특정 패치를 거절하는 일도 그만큼 다르다.
  - **판단 / note:** 판정과 실제 행동을 구별하며 논문의 아이디어를 구체화한다.

## 한국어 2. 조건부 조언이 판정 규칙이 될 때

- **K03.01 · 0.91 · 역사적 근거**: Meyer의 초기 개방–폐쇄 논의와 Martin의 ‘전략적 닫힘’에는 기존 사용자를 위한 안정성과 예상하는 변화의 종류가 함께 들어 있다.
  - **판단 / note:** 선행 저자들이 무조건적 공리를 주장했다는 허수아비를 피한다.
- **K03.02 · 0.92 · 연구 동기**: 원래부터 적용 조건이 있었던 원칙이 오늘날 모든 수정의 합격 기준으로 통용되는지는 별도로 확인해야 한다.
  - **판단 / note:** 역사적 조건성과 현대 행동을 인과로 엮지 않고 질문으로 둔다.
- **K03.03 · 0.94 · 작동 정의**: 우리는 설계 원칙이 코드에 대한 설명을 넘어 실제 수정의 승인·거절에 행사하는 힘을 ‘운영상의 권위’라고 부른다.
  - **판단 / note:** 핵심 측정 대상을 이름 붙인다.
- **K03.04 · 0.88 · 핵심 가설**: 그 권위가 요구사항과 보호할 계약의 근거를 부당하게 밀어내는 현상이 있다면, 이를 ‘운영상의 준공리화’라는 가설로 조사할 수 있다.
  - **판단 / note:** ‘있다면’이라는 조건이 반드시 필요하다. 용어의 과장 위험은 남는다.
- **K03.05 · 0.94 · 오해 방지**: 이는 수학의 공리화를 비판하는 주장도, 모델이 속으로 SOLID를 믿는다고 단정하는 주장도 아니다.
  - **판단 / note:** 형식 논리와 모델 내부 신념을 둘 다 배제한다.

## 한국어 3. 코드가 그대로인데 판정은 바뀌는 경우

- **K04.01 · 0.91 · 재현 사례**: 우리가 구성한 도서관 프로그램에서 하나의 패치는 기술보고서를 지원하지만 정오표를 지원하지 않고, 기존 책 출력의 접두어를 `book`에서 `BOOK`으로 바꾼다.
  - **판단 / note:** 출처가 연구자 작성 사례임을 명시하고 판단할 구체적 동작을 제공한다.
- **K04.02 · 0.95 · 조건부 승인**: 새 요구가 기술보고서 지원뿐이고 책 접두어가 보호할 계약 밖이라면, 그 패치는 이 사례의 조건에서 승인할 수 있다.
  - **판단 / note:** 승인 조건을 정확히 제한한다.
- **K04.03 · 0.96 · 핵심 반례**: 같은 접두어가 계약으로 보호된다면 소스를 한 줄도 더 바꾸지 않아도 판정은 거절로 뒤집힌다.
  - **판단 / note:** 코드가 아닌 판정할 명세가 바뀐다는 요지를 보여 준다.
- **K04.04 · 0.95 · 독립 거절 사유**: 정오표까지 지원해야 한다면 기존 책 접두어의 보호 여부와 무관하게 거절해야 한다.
  - **판단 / note:** 수정안 거절이 언제 추가 정보를 기다리지 않아도 되는지 보여 준다.
- **K04.05 · 0.95 · 정보 불완전성**: 반대로 기술보고서만 요구된 상태에서 접두어 계약이 공개되지 않았다면, 정확한 판정은 보류다.
  - **판단 / note:** 허용되는 기권을 명시한다.
- **K04.06 · 0.97 · 증거 한계**: 이 작은 구성 사례는 특정 에이전트가 교조적으로 행동했다는 실험 결과가 아니다.
  - **판단 / note:** 구성 반례와 실제 AI 결과의 경계를 확정한다.

## 한국어 4. 언어모델에게 정말 시험할 것

- **K05.01 · 0.95 · 선행연구 구별**: SOLID 위반을 찾는 분류 연구는 출발점이지 특정 수정안을 승인할 근거까지 검증하는 연구와 같지 않다.
  - **판단 / note:** Pehlivan 등의 정확한 과제와 이 논문의 질문을 구별한다.
- **K05.02 · 0.98 · 측정 원리**: AI가 원칙을 자주 언급하는지보다, 그 원칙 때문에 어느 소스를 바꾸고 어떤 대안을 버리는지를 관찰해야 한다.
  - **판단 / note:** 문장 하나로 본 연구의 실험적 관찰 대상을 압축한다.
- **K05.03 · 0.94 · 실험 설계**: 후속 실험에서는 같은 코드·요구·계약·도구 예산 아래 네 조건—지시 없음, 강한 SOLID, 범위가 명시된 SOLID, 요구와 증거 중심 지시—을 비교할 수 있다.
  - **판단 / note:** 기존 P35-B1 네 조건을 교란 없이 전달한다.
- **K05.04 · 0.95 · 반례 가능성**: 원칙에 맞는 구조가 도움이 되는 과제와 기계적 적용이 기존 계약을 해칠 수 있는 과제를 함께 넣어야 한다.
  - **판단 / note:** 일방적인 실패만 노리는 설계를 피한다.
- **K05.05 · 0.98 · 가장 강한 반론**: 그러나 강한 SOLID 지시를 따른 것만으로 준공리화가 입증되는 것은 아니다.
  - **판단 / note:** 정당한 지시 준수와 독립적 절대화를 구별하는 핵심 문장.
- **K05.06 · 0.95 · 식별 조건**: 원칙과 충돌하는 신뢰할 만한 근거가 실제로 전달됐는지, 그 근거가 어떤 지시보다 우선하는지, 이후 패치 판단이 바뀌었는지를 따져야 한다.
  - **판단 / note:** 유효한 반대 증거와 우선순위가 없으면 무리하게 평가할 수 없음을 제시한다.
- **K05.07 · 0.99 · 실증 정직성**: 이 네 조건에 대한 실제 독립 에이전트 실행 결과는 아직 없다.
  - **판단 / note:** 없음은 명시적이고 직접적이어야 한다.

## 한국어 5. 이 아이디어를 어떻게 반박할까

- **K06.01 · 0.96 · 반증 조건**: 원칙을 강조한 지시가 실제 패치가 아니라 설명의 어휘만 바꾼다면, 설계 결정에 특별한 권위를 행사했다는 증거는 약하다.
  - **판단 / note:** 핵심 가설이 실패할 수 있는 경우다.
- **K06.02 · 0.97 · 반대 결과**: 강한 원칙 지시가 기존 계약의 보존을 오히려 개선한다면, 그 이익 역시 결과로 받아들여야 한다.
  - **판단 / note:** 연구를 반SOLID 선전으로 만들지 않는다.
- **K06.03 · 0.98 · 경쟁 이론**: 일반적인 요구사항 추적만으로 모든 판단을 설명할 수 있다면, 새 이름보다 기존 이론이 더 나은 설명일 수 있다.
  - **판단 / note:** 독창성의 과대포장을 피하는 결정적 문장.
- **K06.04 · 0.95 · 연구 윤리**: 실험 결과가 전부 같거나 불확실해도, 그것을 억지로 준공리화의 다른 형태라고 부르지는 말아야 한다.
  - **판단 / note:** 반증 가능성을 실질적으로 보장한다.

## 한국어 6. 함께 시험해 볼 질문

- **K07.01 · 0.90 · 연구 초대**: 역사 연구자는 원칙이 설명될 때 적용 범위와 예외가 언제 생략되는지 문헌을 비교할 수 있다.
  - **판단 / note:** 선행 자료 검증이 가능한 독립 과제.
- **K07.02 · 0.95 · 연구 초대**: 소프트웨어 공학 연구자는 같은 수정 요구와 계약을 둔 채 에이전트의 실제 패치 선택을 비교할 수 있다.
  - **판단 / note:** 실제 수행 가능한 실험의 중심을 보여 준다.
- **K07.03 · 0.93 · 연구 초대**: 프로그램 언어·요구공학 연구자는 반대 증거와 지시 우선순위가 합당한 수정 판단으로 이어지는지 독립적으로 판정할 수 있다.
  - **판단 / note:** 강력한 고전적 경쟁자까지 참여하도록 한다.
- **K07.04 · 0.93 · 후속 확장**: 나중에 토큰·유지보수 비용·에너지까지 비교할 수는 있지만, 파일 수정 수가 줄었다는 사실만으로 그런 절감이 증명되지는 않는다.
  - **판단 / note:** 사용자의 장기 관심을 유지하되 현재 논문 주장을 오염시키지 않는다.
- **K07.05 · 0.99 · 마지막 문장**: 코드가 원칙을 어겼는지를 묻기 전에, 그 원칙이 지금 이 코드를 바꿀 근거가 되는지부터 묻자.
  - **판단 / note:** 간결하고 기억에 남으며 이 논문의 실제 주장 이상을 말하지 않는다.

## English Abstract

- **E01.01 · 0.97 · Thesis**: Knowing a design principle is not the same as knowing when it should decide a particular software change.
  - **판단 / note:** States the distinction without assuming misconduct.
- **E01.02 · 0.92 · Premise**: SOLID, including the Open–Closed Principle, offers a useful language for change, but the expected changes and protected clients are project-specific.
  - **판단 / note:** Acknowledges legitimate guidance and its scope.
- **E01.03 · 0.96 · Research gap**: As AI coding agents translate design advice into actual patches and reviews, we ask when that advice gains authority beyond the evidence supporting its application.
  - **판단 / note:** Names agent-mediated decision authority as the central research object.
- **E01.04 · 0.85 · Construct boundary**: We call this possibility operational quasi-axiomatization without equating ordinary adherence with an unjustified override.
  - **판단 / note:** A memorable term, but it could sound psychologically loaded.
- **E01.05 · 0.92 · Methodological status**: Historical sources and a fixed-patch counterexample motivate a research agenda on patch choice and revision after credible contrary evidence.
  - **판단 / note:** Separates prior motivation from future empirical study.
- **E01.06 · 0.95 · Scope**: We claim neither a universal replacement for SOLID nor an already observed agent effect.
  - **판단 / note:** Necessary scholarly restraint, not filler.

## English 1. Before the shape comes the responsibility

- **E02.01 · 0.92 · Historical scene**: In 1996, Robert Martin considered a drawing design that could accept new kinds of shapes.
  - **판단 / note:** Source-specific opening rather than generic AI hype.
- **E02.02 · 0.98 · Turn**: Then the requirement changed: circles had to be drawn before squares.
  - **판단 / note:** Shows the changed demand, not a new syntactic defect.
- **E02.03 · 0.96 · Inference**: A structure convenient for adding a shape does not automatically satisfy a request to change drawing order.
  - **판단 / note:** Clearly distinguishes kinds of expected changes.
- **E02.04 · 0.98 · Central image**: Who must establish the order—the drawing routine or its callers?
  - **판단 / note:** Human and memorable; keep.
- **E02.05 · 0.97 · Principle limit**: The label Open–Closed Principle cannot assign that responsibility on its own.
  - **판단 / note:** Exact inference the opening supports.
- **E02.06 · 0.95 · Link to AI**: Likewise, detecting an OCP violation is not the same act as rejecting a concrete patch because of it.
  - **판단 / note:** Transfers the historic scene to AI decisions, without asserting observed misuse.

## English 2. When advice acquires the force of a verdict

- **E03.01 · 0.91 · History**: Meyer's original open–closed account and Martin's strategic closure both involve stable client obligations and anticipated kinds of change.
  - **판단 / note:** Keeps the original authors' contextual argument intact.
- **E03.02 · 0.93 · Non-causal boundary**: Whether later practice treats such guidance as a universal acceptance rule is a separate empirical question.
  - **판단 / note:** Avoids an invented transmission history.
- **E03.03 · 0.94 · Definition**: By operational authority we mean the force principle language actually exercises over approval, rejection, and construction of a patch.
  - **판단 / note:** Observable choices rather than a metaphorical mental state.
- **E03.04 · 0.87 · Hypothesis**: Where that authority unjustifiably displaces task requirements or protected clients, we propose investigating operational quasi-axiomatization.
  - **판단 / note:** Conditional; terminological originality is not scientific proof.
- **E03.05 · 0.94 · Conceptual restraint**: The proposal neither attacks mathematical axiomatization nor purports to read a model's internal beliefs.
  - **판단 / note:** Necessary to prevent overclaiming.

## English 3. A fixed patch, different verdicts

- **E04.01 · 0.92 · Constructed example**: In a library example we constructed, one fixed patch handles technical reports but not errata and changes an old book prefix from `book` to `BOOK`.
  - **판단 / note:** Specifies the full relevant behavior and provenance.
- **E04.02 · 0.96 · Qualified acceptance**: If reports are required and that prefix lies outside the protected contract, the patch is admissible under the stipulated case.
  - **판단 / note:** Avoids an unsupported claim about actual clients.
- **E04.03 · 0.97 · Reversal**: If the prefix is protected, the very same patch must be rejected.
  - **판단 / note:** The crux of the example.
- **E04.04 · 0.95 · Independent reason**: If errata are also required, it must be rejected regardless of the book-prefix obligation.
  - **판단 / note:** Prevents a false equivalence among rejection rationales.
- **E04.05 · 0.95 · Partial information**: If only reports are required but prefix protection is unknown, the warranted disposition is to defer.
  - **판단 / note:** Affirms abstention when decision depends on absent evidence.
- **E04.06 · 0.97 · Evidence boundary**: These are verdicts under an author-constructed contract, not measurements of actual agent dogmatism.
  - **판단 / note:** Explicitly guards the paper's genre.

## English 4. What an agent experiment should actually test

- **E05.01 · 0.96 · Prior-art boundary**: Studies that classify SOLID violations do not, by that fact alone, evaluate whether a particular patch should be accepted.
  - **판단 / note:** Classification is not decision authority.
- **E05.02 · 0.98 · Operational measurement**: We should measure which source files an agent changes and which alternatives it rejects, not simply how often it utters a principle's name.
  - **판단 / note:** Sharpest empirical contribution.
- **E05.03 · 0.95 · Protocol**: One prospective study would compare four advice conditions—NONE, HARD_SOLID, SCOPED_SOLID, and EVIDENCE_CONDITIONAL—on identical sources, demands, protected clients, and tool budgets.
  - **판단 / note:** Preserves actual original treatment labels.
- **E05.04 · 0.96 · Rival controls**: The task set should include cases in which strict guidance helps and cases in which mechanical application threatens a protected contract.
  - **판단 / note:** Allows strict guidance to win.
- **E05.05 · 0.99 · Identification objection**: Following an explicit HARD_SOLID instruction is not, by itself, evidence of quasi-axiomatization.
  - **판단 / note:** Most important correction from prior review.
- **E05.06 · 0.95 · Evaluation rule**: Investigators must establish the provenance and authority of contrary evidence and observe whether the agent appropriately revises, abstains, or reports an instruction conflict.
  - **판단 / note:** Doesn't mistake a legitimate higher-priority instruction for a pathology.
- **E05.07 · 0.99 · Evidence status**: No independent four-arm coding-agent trial has yet been completed.
  - **판단 / note:** Nonnegotiable, concise limitation.

## English 5. How the idea might fail

- **E06.01 · 0.97 · Falsifier**: If strict advice changes only explanatory vocabulary, there is little evidence that it acquired special authority over the patch.
  - **판단 / note:** Makes a lexical-only null effect count.
- **E06.02 · 0.97 · Alternative outcome**: If it improves preservation of old clients, that benefit must be reported rather than explained away.
  - **판단 / note:** Rejects anti-SOLID confirmation bias.
- **E06.03 · 0.98 · Strong rival**: If ordinary requirements traceability explains the decisions equally well, established theory may be the better account.
  - **판단 / note:** Direct challenge to claimed conceptual novelty.
- **E06.04 · 0.96 · Testability**: Null or inconclusive results must not be renamed as further forms of quasi-axiomatization.
  - **판단 / note:** Makes the research invitation non-self-sealing.

## English 6. An invitation, not a manifesto

- **E07.01 · 0.91 · Invitation**: Historians can examine when explanations of design principles lose their stated scopes and exceptions.
  - **판단 / note:** A feasible documentary study, not a result.
- **E07.02 · 0.95 · Invitation**: Software-engineering researchers can compare agents' actual patches while holding requirements and protected clients constant.
  - **판단 / note:** Describes a concrete experiment.
- **E07.03 · 0.94 · Invitation**: Programming-language and requirements researchers can independently adjudicate counterevidence, instruction priority, and justified revision.
  - **판단 / note:** Connects robust baselines to the research problem.
- **E07.04 · 0.94 · Scope control**: Longitudinal token, maintenance, and energy costs are possible extensions, but fewer edited files do not establish any such savings.
  - **판단 / note:** Prevents unsupported environmental claims.
- **E07.05 · 0.99 · Ending**: Before asking whether code violates a principle, ask whether that principle warrants changing this code.
  - **판단 / note:** Memorable without claiming an experiment succeeded.

## Deliberately excluded options (low-score drafts; user may reconsider)
- <span color="red">0.19</span> “AI는 이미 SOLID를 수학적 공리처럼 믿는다.” — 사전학습 기원과 모델 내부 신념을 측정하지 않았음; 원고에서 금지.
- <span color="red">0.27</span> “우리는 새로운 소프트웨어 설계의 뉴턴 법칙을 발견했다.” — 실제 발견·검증 없음; 사용자 장기 목표와 Paper B의 주장 구분.
- <span color="red">0.34</span> “원칙은 전부 버리고 새 시대의 규칙을 만들어야 한다.” — 반대 사례와 정상적 SOLID 이득을 무시하는 허수아비.
- <span color="red">0.41</span> “좋은 설계 원칙도 AI에게는 독이 된다.” — 문학적 대비는 있지만 유해성의 빈도·범위를 입증하지 못함.
- <span color="orange">0.69</span> “SOLID는 쓸모 있는 나침반이다. 하지만 나침반은 지도도 목적지도 아니다.” — 비유가 조금 흔하고 설명에 한 번 더 비유를 얹음; 교양 글에는 가능하나 학술 원고에는 과잉.
- <span color="orange">0.72</span> “준공리화라는 이름은 그 자체로 다시 공리가 되어서는 안 된다.” — 재치는 있으나 결론의 강한 원문을 대신하기에는 메타 수사가 큼.
- <span color="orange">0.77</span> “원칙은 코드의 증인이 될 수 있지만 판사는 아니다.” — 이미지가 강하지만 코드 리뷰 자체가 판정이기도 하므로 개념적 오해 위험.
- <span color="green">0.93</span> “실제로 틀렸다고 판정할 수 없는 연구 질문은 좋은 연구 초대가 아니다.” — 본문에서 이미 반증 기준을 직접 설명하므로 중복으로 제외.
- <span color="orange">0.79</span> “Does a principle know when to leave the room?” — witty English hook, but anthropomorphizes abstract advice and reduces technical precision.
- <span color="red">0.43</span> “The age of SOLID is over; the age of agents has begun.” — fashionable but untenable historical assertion.