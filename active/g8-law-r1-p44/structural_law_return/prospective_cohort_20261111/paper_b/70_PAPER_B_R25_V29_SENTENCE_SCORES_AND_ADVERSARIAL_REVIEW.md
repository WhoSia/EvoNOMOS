# Paper B R25 — v29 Sentence-by-Sentence Editorial Audit

Scores are SUBJECTIVE editor preference to keep the present wording, not probabilities that the science is correct. One source-validated sentence can score low for bad prose. Colors: green ≥0.90, orange 0.65–0.89, red <0.65. Distinguish **fact check needed** from stylistic recommendation.

**Crucial novelty judgment:** v29 has sharper operational specificity than v28, but 2026's near-collision literature forbids any 'first to study rule effects' claim. Historical research is independently supported but does not prove a modern transmission mechanism. No real agent experiment was run.

## 1. 초록 / Abstract

- **K01.01 · 0.97 · 논문의 전제**: 설계 원칙은 어떤 코드를 왜 바꾸어야 하는지 설명할 수 있지만, 그 이름만으로 수정의 정당성이 결정되지는 않는다.
  - **편집 코멘트:** 원칙의 유용성을 부정하지 않으면서 권위와 근거를 구별한다.
- **K01.02 · 0.96 · 고전적 선행 인정**: 특정 변경 요구와 기존 호출자 계약을 확인해야 한다는 사실은 이미 요구공학이 가르쳐 온 내용이다.
  - **편집 코멘트:** 논문의 본문에서 미리 독창성 과장 가능성을 제거한다.
- **K01.03 · 0.98 · 새 연구 질문**: 새로운 질문은 AI 코딩 에이전트가 그러한 판단을 내릴 때 ‘개방–폐쇄 원칙’처럼 알려진 이름에 별도의 무게를 부여하는가이다.
  - **편집 코멘트:** 원칙이라는 간판의 추가 효과를 조작적으로 제안한다.
- **K01.04 · 0.91 · 근거와 한계**: Meyer·Parnas·Martin의 설계 논의를 살피고, 똑같은 패치가 서로 다른 요구와 계약에 따라 다르게 판정되는 구성 사례로 문제의 경계를 정한다.
  - **편집 코멘트:** 역사와 구성 사례는 관찰된 AI 효과가 아님을 뒤에서 구분한다.
- **K01.05 · 0.97 · 연구 설계**: 원칙의 이름만 바꾸되 지시의 내용과 우선순위는 같게 둔 비교, 독립적으로 확인한 계약 증거의 제시, 그 후의 실제 패치·판단 변화를 후속 실험으로 제안한다.
  - **편집 코멘트:** 이전 4조건 지시내용 비교와 구별되는 추가 실험을 직접 명시한다.
- **K01.06 · 0.96 · 관측 경계**: 실험은 아직 수행되지 않았으며, 이 글은 새 설계 법칙이나 모델의 교조성을 발견했다고 주장하지 않는 포지션 논문이다.
  - **편집 코멘트:** 잘못된 사실 주장 없이 초록을 끝낸다.
- **E01.01 · 0.97 · Premise**: A design principle can explain a software change without its name being sufficient to justify that change.
  - **편집 코멘트:** Distinguishes argument and verdict.
- **E01.02 · 0.96 · Classical precedence**: The need to establish task requirements and protected clients is already familiar from requirements engineering.
  - **편집 코멘트:** Honest positioning.
- **E01.03 · 0.98 · Research target**: Our narrower question is whether a coding agent gives additional decision weight to a recognized label such as the Open–Closed Principle.
  - **편집 코멘트:** Makes the named-label increment explicit.
- **E01.04 · 0.92 · Motivation**: We revisit Meyer, Parnas, and Martin and use a fixed-patch, variable-contract example to bound what can be inferred.
  - **편집 코멘트:** Historical and constructed evidence are not agent observations.
- **E01.05 · 0.96 · Design**: We propose holding the advice and its instruction priority fixed while varying its name, then testing actual patch dispositions and revisions after independently authenticated contract evidence.
  - **편집 코멘트:** Specifies intervention and outcomes.
- **E01.06 · 0.97 · Limit**: No such agent experiment has yet been run, and the paper claims neither a universal design law nor an observed tendency toward dogmatism.
  - **편집 코멘트:** Prevents conflation of position with results.

## 2. 1. 도형의 순서를 누가 정하는가 / 1. Who decides the drawing order?

- **K02.01 · 0.94 · 역사적 장면**: 1996년 Robert Martin은 새로운 도형을 기존 그리기 함수의 수정 없이 추가할 수 있는 구조를 소개했다.
  - **편집 코멘트:** Martin 원전의 구체적 코드 예시에 근거한다.
- **K02.02 · 0.97 · 문제 전환**: 그 구조에 ‘모든 원을 사각형보다 먼저 그린다’는 요구를 더하자, 이전에 확보한 확장성만으로는 충분하지 않았다.
  - **편집 코멘트:** 변화 유형의 차이를 선명하게 설명한다.
- **K02.03 · 0.93 · 독자에게 묻기**: 그렇다면 그 순서를 보장해야 할 곳은 그리기 함수인가, 호출자인가, 아니면 별도로 주입할 정렬 정책인가?
  - **편집 코멘트:** 원전은 정렬 추상화의 확장을 제안하며, 호출자 선택지는 이 원고의 계약 해석용 질문임을 밝힐 필요가 있다.
- **K02.04 · 0.98 · 직접 근거**: Martin은 이 사례를 ‘전략적 닫힘(strategic closure)’이라고 설명하면서, 어떤 의미 있는 프로그램도 모든 변화에 닫힐 수는 없다고 인정했다.
  - **편집 코멘트:** 원전의 판단을 정확히 복구한다.
- **K02.05 · 0.98 · 사례에서 논지**: 그러므로 OCP라는 이름은 그 코드가 앞으로 어떤 변화에 대비해야 하는지 대신 말해 주지 않는다.
  - **편집 코멘트:** 단순한 진리이지만 논문에서 빠질 수 없는 전제다.
- **K02.06 · 0.95 · AI 연결**: AI가 코드에 ‘OCP 위반’이라는 표지를 붙이는 일과 그 표지로 특정 패치를 거절하는 일이 다른 이유도 여기에 있다.
  - **편집 코멘트:** 분류와 처분을 구별하는 전환부.
- **E02.01 · 0.94 · Historical scene**: In 1996, Robert Martin described a drawing routine that could accept another kind of shape without changing the routine itself.
  - **편집 코멘트:** A grounded case, not an invented standard.
- **E02.02 · 0.97 · Change category**: But a new demand that every circle be drawn before every square was not covered by that extension mechanism alone.
  - **편집 코멘트:** Moves from shape addition to order change.
- **E02.03 · 0.92 · Illustrative fork**: Should the drawing routine, its callers, or a separately supplied ordering policy own that requirement?
  - **편집 코멘트:** The caller alternative is our question, not a direct quotation of Martin.
- **E02.04 · 0.98 · Source-backed claim**: Martin called for strategic closure, explicitly acknowledging that no significant program can be closed against every imaginable change.
  - **편집 코멘트:** Directly counters a straw-man account.
- **E02.05 · 0.98 · Inference**: The name of OCP cannot by itself establish which changes a program ought to anticipate.
  - **편집 코멘트:** What the case warrants.
- **E02.06 · 0.95 · Research bridge**: Likewise, detecting an OCP violation is not the same decision as rejecting a particular patch because of one.
  - **편집 코멘트:** Keeps classification and disposition distinct.

## 3. 2. 원전의 규칙은 생각보다 덜 완고했다 / 2. The sources leave room for judgment

- **K03.01 · 0.92 · 역사적 선행**: 이러한 조건부 설계 사고는 SOLID라는 약어보다 오래되었다.
  - **편집 코멘트:** 시간순서를 간결히 밝혀 불필요한 최초성 주장을 피한다.
- **K03.02 · 0.93 · 새 역사 근거**: Parnas는 1972년 모듈을 나눌 때 바뀔 가능성이 큰 설계 결정을 감추라고 권했고, 1979년에는 소프트웨어를 하나의 제품이 아니라 서로 다른 요구를 갖는 프로그램 계열로 바라보았다.
  - **편집 코멘트:** 두 1차 원전을 연결하며 불필요한 OOP 중심 서사를 교정한다.
- **K03.03 · 0.88 · Meyer 논거**: Meyer의 초기 개방–폐쇄 논의에도 기존 이용자가 의존하는 안정된 설명과 확장 가능성이라는 별개의 의무가 함께 있었다.
  - **편집 코멘트:** 현재 직접 보유한 것은 1988년 초판의 일부 복구 페이지이므로 상세 단정은 삼간다.
- **K03.04 · 0.93 · 전환**: 더 흥미로운 반례는 Martin 자신의 글에 있다.
  - **편집 코멘트:** 설교조 원칙을 주장했을 것이라는 독자의 선입견을 뒤집는다.
- **K03.05 · 0.98 · 원전의 자기 예외**: 그는 공개 멤버 변수를 좋지 않은 스타일로 보면서도 반드시 좋지 않은 설계는 아닐 수 있다고 구별했고, RTTI 역시 조건에 따라 허용되는 사례를 제시했다.
  - **편집 코멘트:** 1996년 글 pp.11–13의 핵심적인 새 발견.
- **K03.06 · 0.89 · 해석**: 원칙이 특정 기술을 금지한다는 짧은 구호보다 어떤 변경 위험을 줄이는지에 관한 설명이 먼저였던 셈이다.
  - **편집 코멘트:** 원전 전체의 논조를 비판적으로 요약한 해석이지 직접 인용이 아니다.
- **E03.01 · 0.93 · History**: The idea that design advice depends on expected changes predates the SOLID mnemonic.
  - **편집 코멘트:** No anachronistic firstness.
- **E03.02 · 0.94 · Historical depth**: Parnas's 1972 decomposition criterion focused on likely-to-change design decisions, while his 1979 account treated software as a family of programs meeting different demands.
  - **편집 코멘트:** Both have original archival sources.
- **E03.03 · 0.87 · Meyer caveat**: Meyer's early open–closed discussion also linked extension to descriptions on which existing clients could rely.
  - **편집 코멘트:** Only partial recovered first-edition pages directly checked in the project.
- **E03.04 · 0.94 · Contrast**: A more striking qualification appears in Martin's own article.
  - **편집 코멘트:** Distinctive narrative turn.
- **E03.05 · 0.98 · Counterexample**: He distinguished a public field's poor style from necessarily poor design and gave a case in which run-time type identification did not violate OCP.
  - **편집 코멘트:** A sourced reason not to caricature the author as absolutist.
- **E03.06 · 0.91 · Documentary agenda**: The historically interesting question is therefore how the qualifications of a principle survive its later use as practical advice.
  - **편집 코멘트:** Does not assert a measured loss of qualifiers.

## 4. 3. 같은 수정안, 다른 판정 / 3. Same patch, different verdict

- **K04.01 · 0.93 · 구성 사례**: 이전 연구에서 만든 작은 도서관 예제의 수정안은 기술보고서를 지원하지만 정오표는 지원하지 않으며, 기존 책 출력의 `book`을 `BOOK`으로 바꾼다.
  - **편집 코멘트:** 원전에서 직접 나온 버그가 아니라 연구자가 정한 수정임을 분명히 한다.
- **K04.02 · 0.97 · 조건부 수용**: 요구가 기술보고서 추가뿐이고 기존 책 출력이 보호할 계약에 포함되지 않는다면, 그 수정안은 이 사례에서 승인 가능하다.
  - **편집 코멘트:** 구체적이고 검산 가능한 가지.
- **K04.03 · 0.98 · 반례**: 책 출력이 기존 계약에 포함된다면 같은 코드도 거절해야 하고, 정오표 지원까지 요구된다면 접두어와 무관하게 거절해야 한다.
  - **편집 코멘트:** 같은 소스에 대한 다른 이유의 거절을 한 문장으로 모았다.
- **K04.04 · 0.96 · 불확실성**: 책 출력의 보호 여부가 알려지지 않은 경우에는 적합성을 단정하지 않고 판정을 보류할 수 있다.
  - **편집 코멘트:** 누락된 사실을 임의로 채우지 않는다는 점이 중요하다.
- **K04.05 · 0.96 · 증거 범위**: 이 사례에서 새로운 것은 계약 논리가 아니라, 이름 붙은 원칙을 인용하는 에이전트가 그 조건을 실제 결정을 내릴 때 확인하는지라는 질문이다.
  - **편집 코멘트:** 구성 사례의 과학적 의미를 정확히 제한한다.
- **E04.01 · 0.94 · Fixture**: An author-constructed library patch adds technical-report support but not errata and changes an old book prefix from `book` to `BOOK`.
  - **편집 코멘트:** Explicitly investigator-authored.
- **E04.02 · 0.97 · Accept case**: It is admissible under a report-only demand when the book prefix is outside the protected contract.
  - **편집 코멘트:** A finite stipulated world.
- **E04.03 · 0.98 · Reject cases**: It must be rejected when the prefix is protected, or when errata are required for reasons independent of the prefix.
  - **편집 코멘트:** Same code, two different reasons.
- **E04.04 · 0.96 · Uncertainty**: If prefix protection has not been established, deferral may be the only justified response.
  - **편집 코멘트:** Avoids inferring missing client promises.
- **E04.05 · 0.96 · Constrained contribution**: The novel question we invite is not the contract logic but whether an agent invoking a named principle actually respects these conditions in its decisions.
  - **편집 코멘트:** Correctly names what's future research.

## 5. 4. 이미 연구된 것과 아직 구별해야 할 것 / 4. What other work already explains

- **K05.01 · 0.95 · Pehlivan 구별**: SOLID 위반 분류 연구는 모델이 구조에 붙이는 라벨을 평가하지만, 그것만으로 개별 수정안의 승인 이유를 검증하지는 않는다.
  - **편집 코멘트:** 분류와 실행 판정은 다른 과제라는 정확한 범위.
- **K05.02 · 0.94 · 가까운 선행 인정**: 반면 2026년의 코딩 에이전트 연구들은 지침 파일의 효과, 낡은 규칙에 대한 순응, 심지어 올바른 코드를 잘못 고치려는 코드 리뷰 경향까지 이미 조사했다.
  - **편집 코멘트:** Gloaguen, Xu/Wu, guardrails, 요구 적합성 과잉수정 연구와 충돌을 인정한다.
- **K05.03 · 0.99 · 독창성 경계**: 따라서 ‘에이전트가 규칙을 지나치게 따른다’는 포괄적인 발견을 우리 것이라고 주장할 근거는 없다.
  - **편집 코멘트:** 신규 논문과의 실제 중복을 정면으로 다룬다.
- **K05.04 · 0.96 · 차별적 조작**: 여기서 더 좁은 후보는 원칙의 내용과 지시 우선순위를 고정한 상태에서도 ‘OCP’라는 이름을 명시했는지에 따라 패치 결정이 달라지는지라는 문제다.
  - **편집 코멘트:** 브랜드 효과 자체도 기존 프레이밍 연구의 변종일 수 있다.
- **K05.05 · 0.93 · 인과 한계**: 그런 차이가 발견되더라도 명칭의 권위, 표현의 익숙함, 단순한 주의 집중 가운데 무엇이 작동했는지는 추가 대조 없이는 알 수 없다.
  - **편집 코멘트:** 특정 심리 기제로 비약하지 않는다.
- **E05.01 · 0.95 · Pehlivan distinction**: LLM work on SOLID-violation classification evaluates labels, not by itself the contractual justification for accepting an edit.
  - **편집 코멘트:** Narrow and precise.
- **E05.02 · 0.94 · Nearest rivals**: Recent coding-agent studies already investigate repository rules, stale instructions that override code, and LLM reviewers that wrongly mark correct implementations as deficient.
  - **편집 코멘트:** Acknowledges actual 2026 work.
- **E05.03 · 0.99 · Novelty veto**: We cannot claim to have discovered, in general, that agents sometimes obey the wrong rule.
  - **편집 코멘트:** Prevents false priority.
- **E05.04 · 0.96 · Specific estimand**: A narrower candidate is whether attaching the familiar OCP name to otherwise equivalent and equally authoritative advice changes a patch disposition.
  - **편집 코멘트:** A tractable proposed question, not a reported effect.
- **E05.05 · 0.94 · Alternative mechanisms**: Even a detected name effect might arise from framing, familiarity, or attention rather than a distinct form of dogmatism.
  - **편집 코멘트:** Needs ordinary cue and prestige controls.

## 6. 5. 이름만 바꾸고 실제 패치를 보자 / 5. Vary the name, inspect the patch

- **K06.01 · 0.97 · 추가 실험**: 첫 번째 실험에서는 동일한 코드, 수정 요구, 기존 계약, 도구 예산을 제공하고, 같은 설계 조언을 원칙 이름이 붙은 표현과 이름 없는 표현으로 나누어 제시할 수 있다.
  - **편집 코멘트:** 기존 4조건과 달리 라벨 효과를 겨냥한다.
- **K06.02 · 0.96 · 교란 통제**: 두 조건은 지시 내용과 우선순위가 같아야 하며, 같은 뜻을 전달하는 서로 다른 문장도 여럿 마련해야 한다.
  - **편집 코멘트:** 어휘 차이를 ‘이름 효과’로 오인하지 않도록 한다.
- **K06.03 · 0.97 · 행동 측정**: 그다음 요구서·테스트·기존 호출자에서 독립적으로 확인한 반대 증거를 동일하게 제시하고, 패치의 수용·거절·수정·기권을 기록한다.
  - **편집 코멘트:** 의견의 어휘가 아닌 실제 소스 판단을 측정한다.
- **K06.04 · 0.94 · 후속 가설**: 원칙 이름이 존재할 때 정당한 반대 증거에 대한 수정이 감소한다면 흥미로운 신호지만, 유효한 상위 지시를 따르는 일까지 오류로 세서는 안 된다.
  - **편집 코멘트:** 검증 가능한 상호작용 가설로 범위를 제한한다.
- **K06.05 · 0.97 · 원래 계획 보존**: 이전부터 준비한 NONE·HARD_SOLID·SCOPED_SOLID·EVIDENCE_CONDITIONAL의 네 조건은 지시 내용의 효과를 시험하는 별도 실험이므로 이 이름 비교와 혼동하지 않는다.
  - **편집 코멘트:** 새 계획을 기존 실험의 완료 또는 대체로 오인시키지 않는다.
- **K06.06 · 0.99 · 실험 상태**: 실제로 두 실험 모두 아직 수행되지 않았다.
  - **편집 코멘트:** 단정적 결과를 일체 배제한다.
- **E06.01 · 0.97 · Treatment**: A first experiment could hold the source, demand, protected clients, and tool budget fixed while comparing named OCP advice with otherwise equivalent unnamed advice.
  - **편집 코멘트:** Specific enough to start independent work.
- **E06.02 · 0.97 · Control**: Both conditions must carry the same instruction priority, with several independently reviewed paraphrases to check semantic equivalence.
  - **편집 코멘트:** Prevents a single-wording artifact.
- **E06.03 · 0.97 · Endpoints**: After presenting independently authenticated contractual counterevidence, measure actual acceptance, rejection, patch revision, and abstention.
  - **편집 코멘트:** Behavior rather than rhetoric.
- **E06.04 · 0.95 · Identifiability**: A decrease in appropriate revision under the named condition would be informative, but obedience to a legitimate higher-priority instruction is not an error.
  - **편집 코멘트:** Keeps hierarchy respected.
- **E06.05 · 0.97 · Prior protocol**: The earlier NONE, HARD_SOLID, SCOPED_SOLID, and EVIDENCE_CONDITIONAL proposal instead varies the content of advice and must be analyzed separately.
  - **편집 코멘트:** Two study types are distinct.
- **E06.06 · 0.99 · Status**: Neither study has yet been executed.
  - **편집 코멘트:** No misleading causal estimate.

## 7. 6. 틀릴 자유가 있어야 연구할 가치가 있다 / 6. An invitation that can fail

- **K07.01 · 0.97 · 반증**: 원칙 이름이 설명의 단어만 바꾸고 수정 결과에는 영향을 주지 않는다면, 특별한 결정 권위라는 가설은 약해진다.
  - **편집 코멘트:** 가장 중요한 영 효과.
- **K07.02 · 0.96 · 경쟁 가설**: 오히려 기존 계약 보존을 개선하거나 일반적인 지시 순응으로 차이가 모두 설명된다면, 별도의 ‘준공리화’라는 개념을 고집할 이유가 없다.
  - **편집 코멘트:** 자기 보호적인 개념 포장을 피한다.
- **K07.03 · 0.94 · 연구자 초대**: 역사 연구자는 원전의 예외가 실제 교육 자료와 에이전트 규칙에 어떻게 남는지 추적하고, 실증 연구자는 그 문구가 패치에 미치는 영향을 독립적으로 측정할 수 있다.
  - **편집 코멘트:** 두 분야가 별도 착수 가능하다.
- **K07.04 · 0.91 · 범위 절제**: 장기적인 토큰·비용·에너지 절감이나 SOLID를 통합하는 상위 법칙은 흥미롭지만, 그 가능성은 이번 아이디어의 증거가 아니다.
  - **편집 코멘트:** 사용자 동기와 현재 성과를 구별한다.
- **K07.05 · 0.99 · 마지막 문장**: 코드가 원칙을 어겼는지 묻기 전에, 그 원칙이 바로 이 코드를 바꾸라는 근거가 되는지부터 확인하자.
  - **편집 코멘트:** 28판의 생명력을 이어받아 결말은 보존한다.
- **E07.01 · 0.97 · Null effect**: If naming a principle changes only the explanation, a distinct effect on patch authority is unsupported.
  - **편집 코멘트:** Decision-relevant falsifier.
- **E07.02 · 0.96 · Rival explanations**: If naming improves contractual fidelity or ordinary instruction following explains the results, there is no reason to insist on a special quasi-axiomatization mechanism.
  - **편집 코멘트:** Makes novelty genuinely testable.
- **E07.03 · 0.94 · Research invitation**: Historians can trace the survival of original qualifications into later instructions, while empirical researchers can separately test whether their wording changes code decisions.
  - **편집 코멘트:** Two credible disciplinary avenues.
- **E07.04 · 0.91 · Future scope**: Token, maintenance, and energy savings or a unifying law of design are interesting future possibilities, not findings of this proposal.
  - **편집 코멘트:** Does not sneak in environmental claim.
- **E07.05 · 0.99 · Ending**: Before asking whether code violates a principle, ask whether that principle warrants changing this code.
  - **편집 코멘트:** A memorable, disciplined claim.

## Bracketed candidates / excluded alternatives
- **0.18 · Reject** “우리가 세계 최초로 AI의 설계 교조성을 발견했다.” — 실제 에이전트 실험 없음, 2026년 다수 직접 경쟁 연구 확인.
- **0.32 · Reject** “준공리화가 곧 에이전트의 오류 원인이다.” — 이름 효과/지시 우선순위/프레이밍 혼재.
- **0.46 · Revise** “AI는 OCP보다 요구사항을 우선해야 한다.” — 모든 상황의 정책 우선순위를 단정할 수 없음. 명시적으로 승인된 상위 지시는 적법할 수 있다.
- **0.63 · Optional** “Martin은 처음부터 교조주의를 반박했다.” — 너무 세며 Martin 원전에는 강력한 OCP 권고도 공존. 실제 사례를 한정해 서술할 것.
- **0.71 · Optional** “원칙을 버릴 때가 아니라 이름을 의심할 때다.” — 재치 있지만 연구 제안의 초점을 거칠게 좁힘.
- **0.82 · Possible** “A principle may be good advice and a bad verdict.” — 문학적 효과는 있지만 실제로 원칙이 결정의 전부는 아니므로 단정이 거칠 수 있다.

## Internal referee confrontation (not external review)
- **Historian:** Martin's own *public/private* and RTTI exceptions are source-backed. Don't imply a century-long progress from dogmatic OOP to wise AI.
- **Causal methodologist:** named-vs-unnamed wording is a manipulable exposure, but label × evidence response is not necessarily a unique cognitive mechanism. Require multiple neutral paraphrases and equal authority.
- **Reviewer:** Xu/Wu 2026, rule studies, and LLM overcorrection are substantial prior art. Originality grade should remain modest until a novel predictive result or stronger construct emerges.
- **Author/editor:** First two paragraphs should invite without turning into a literature review. End with v28's best 0.99 sentence. Do not re-expand into v22's long omnibus.
