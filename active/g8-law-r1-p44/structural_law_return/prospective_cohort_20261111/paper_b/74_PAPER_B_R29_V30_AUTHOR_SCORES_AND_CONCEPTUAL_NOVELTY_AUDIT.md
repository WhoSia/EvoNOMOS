# Paper B R29 — v30 Ambitious Framing, Sentence Evaluation and Prior-Art Confrontation

Score 0–1 is **subjective editor willingness to retain this wording**, not probability of correctness, scholarly firstness or observed efficacy. The conceptual agenda should be judged separately from empirical evidence and priority proof.

## Different novelty axes (editor's judgments only)
| Axis | Rating | Why |
| --- | ---: | --- |
| Ambition / reach of research problem | 0.93 | Links historical design advice, epistemic authority, code-patch adjudication, and revocability |
| Distinctiveness of cross-domain position framing | 0.87 | Explicit *authority life cycle* rather than generic 'AI follows rules' claim; global novelty not certified |
| Testable specificity | 0.76 | Contracts, prompted advice, evidence revision; named-label test is only one proposed probe |
| Current empirical evidence of AI overreach | 0.30 | No independent agent trial; motivating source examples do not supply effect rate |
| Provable worldwide priority/firstness | NOT VERIFIED | Adjacent studies already investigate rule obedience and code-review misclassification |
| Reader engagement / rhetorical structure | 0.89 | Opening question, Martin dilemma, high-concept ending; risk of 'axiom' rhetoric kept conditional |

## Sentence-level editorial record (all retained manuscript prose, two languages)
### 1. 초록 / Abstract
- **K01.01 · 0.98 · 창립 질문**: 소프트웨어 설계 원칙은 언제 조언을 넘어 판단을 구속하는 규칙이 되는가?
  - **판단:** 원칙의 권위라는 대상을 첫 문장에서 제시한다.
- **K01.02 · 0.95 · 조건성**: SOLID는 소프트웨어의 변화를 다루는 강력한 언어이지만, 어떤 변화가 예상되고 무엇을 보존해야 하는지는 그 이름만으로 정해지지 않는다.
  - **판단:** 원칙의 가치와 적용 한계를 공존시킨다.
- **K01.03 · 0.96 · 독자적 연구 프레임**: 우리는 객체지향 설계의 역사, 요구공학의 계약 논리, AI 코딩 에이전트의 실행 가능한 지침을 연결해, 설계 조언의 권위가 어떻게 형성되고 언제 수정되어야 하는지 묻는다.
  - **판단:** 세 분야의 단순 나열이 아니라 권위의 형성·집행·수정이라는 한 문제로 묶는다.
- **K01.04 · 0.88 · 개념과 경계**: 이를 ‘운영상의 준공리화’라는 연구 의제로 제안하되, 누군가 SOLID를 정식 공리로 선포했다거나 AI가 이미 이를 무조건적으로 따른다고 주장하지는 않는다.
  - **판단:** 매력적인 이름의 과잉 권위를 스스로 제한한다.
- **K01.05 · 0.95 · 증거 경계**: 고전적 원전과 동일 수정안의 조건부 판정은 출발점이며, 실제 에이전트가 원칙을 적용·유보·철회하는지는 아직 검증해야 할 질문이다.
  - **판단:** 연구 제안 장르와 실제 실험 미수행 상태를 한 문장에 결합한다.
- **E01.01 · 0.98 · Framing**: When does software design advice become a rule that governs a decision?
  - **판단:** Reader knows the object immediately.
- **E01.02 · 0.95 · Conditionality**: SOLID offers a powerful language for change, but its name alone does not establish which changes to anticipate or which clients to protect.
  - **판단:** Not an attack on SOLID.
- **E01.03 · 0.96 · Cross-domain synthesis**: We bring the history of object-oriented design, contractual reasoning in requirements engineering, and executable instructions for AI coding agents into one question: how does design advice acquire authority, and when should that authority be revised?
  - **판단:** States a concrete intellectual bridge, not the world's first empirical effect.
- **E01.04 · 0.88 · Terminology restraint**: We propose operational quasi-axiomatization as an agenda, not as a claim that anyone formally axiomatized SOLID or that agents have already been shown to obey it unconditionally.
  - **판단:** Avoids mind-reading and false historical assertions.
- **E01.05 · 0.95 · Genre honesty**: Historical sources and a fixed-patch counterexample motivate the inquiry; whether agents apply, suspend, or withdraw principle-based decisions remains an empirical question.
  - **판단:** Separates source and future results.

### 2. 1. 원칙은 판단을 대신하지 않는다 / 1. A principle does not make the decision
- **K02.01 · 0.96 · 역사적 시작**: Martin이 1996년에 제시한 도형 프로그램은 새 도형의 추가에는 열려 있었지만, 원을 사각형보다 먼저 그리라는 요구 앞에서는 다시 설계 판단을 필요로 했다.
  - **판단:** 원전의 변화 유형 대비를 간결하게 보여 준다.
- **K02.02 · 0.98 · 구체적 질문**: 누가 순서를 보장해야 하는가—그리는 함수인가, 호출자인가, 별도 정렬 정책인가?
  - **판단:** 논문의 가장 생생한 사례.
- **K02.03 · 0.99 · 중심 전환**: 원칙의 이름은 그 답을 대신할 수 없다.
  - **판단:** 짧지만 핵심 논증이므로 유지한다.
- **K02.04 · 0.94 · AI 도약**: 정확히 여기서 Paper B의 질문이 시작된다: 설계 원칙을 아는 기계가 그 원칙을 적용할 자격까지 아는가?
  - **판단:** 비유는 선명하지만 AI를 인격체처럼 다루지 않도록 표현의 여지가 있다.
- **E02.01 · 0.96 · Opening scene**: Martin's 1996 drawing example accommodated new kinds of shapes, yet a demand to draw every circle before every square called for a different design judgment.
  - **판단:** Uses a source-backed shift in anticipated change.
- **E02.02 · 0.98 · Concrete fork**: Who owns the ordering requirement—the drawing routine, its callers, or a separate policy?
  - **판단:** Precise, lively question.
- **E02.03 · 0.99 · Inferred limit**: The name of the principle cannot answer for them.
  - **판단:** Shortest important line.
- **E02.04 · 0.93 · AI transition**: This is where our inquiry begins: can a coding agent know a principle without knowing when it is entitled to apply it?
  - **판단:** A question about source-grounded decision ability, not a claim about belief.

### 3. 2. 역사에 이미 있던 조건을 다시 찾다 / 2. The qualifications were there all along
- **K03.01 · 0.94 · 고전적 선행**: 1972년 Parnas의 모듈 경계 논의와 1979년 프로그램 계열 연구는 변화할 가능성이 큰 결정을 어떻게 격리할지 고민했다.
  - **판단:** 역사를 장식이 아니라 원래 조건의 증거로 사용한다.
- **K03.02 · 0.96 · 조건부 역사**: Meyer는 확장성과 기존 이용자가 의존하는 안정된 설명을 함께 다뤘고, Martin은 모든 변화에 닫힌 프로그램은 불가능하므로 ‘전략적 닫힘’을 선택해야 한다고 설명했다.
  - **판단:** Meyer 원전은 일부 페이지 복구라는 출처 범위를 별도 명시한다.
- **K03.03 · 0.96 · 역사적 반전**: Martin은 공개 멤버 변수의 좋지 않은 스타일과 잘못된 설계를 구별했고, RTTI가 OCP를 해치지 않는 예외도 논의했다.
  - **판단:** 원저자 자신이 적용 범위를 따지는 실제 사례.
- **K03.04 · 0.97 · 역사 해석**: 이것은 SOLID의 창시자들을 교조주의자로 고발하는 이야기가 아니다.
  - **판단:** 원저 논지를 정확히 보호한다.
- **K03.05 · 0.93 · 새 프레임**: 그보다는 조건과 예외를 포함한 조언이 교육, 코드 리뷰, 에이전트 지침을 거치며 어떤 권위를 얻는지 묻는 역사·인식론적 탐구의 출발점이다.
  - **판단:** 실제 단순화의 역사적 전파는 미관측이므로 질문형으로 유지한다.
- **E03.01 · 0.94 · Classical antecedents**: Parnas's 1972 decomposition criterion and 1979 account of program families already asked which changing decisions a modular design ought to isolate.
  - **판단:** Credits earlier work.
- **E03.02 · 0.96 · Source argument**: Meyer joined extensibility to stable descriptions for clients, while Martin argued that closure against every change is impossible and must instead be strategic.
  - **판단:** Qualifies rhetoric with original texts.
- **E03.03 · 0.97 · Historical counterpoint**: Martin even separated a public field's poor style from necessarily poor design and described a case in which run-time type identification did not violate OCP.
  - **판단:** Not all rules are hard bans even in the original essay.
- **E03.04 · 0.97 · No strawman**: This is not an accusation that the authors of SOLID proclaimed an infallible doctrine.
  - **판단:** Explicit guard.
- **E03.05 · 0.94 · Research trajectory**: It is an invitation to ask what happens to the conditions and exceptions of design advice as that advice moves through teaching, code review, and agent instructions.
  - **판단:** The proposed transmission is not asserted to have been measured.

### 4. 3. 권위의 획득에서 철회까지 / 3. From acquiring authority to withdrawing it
- **K04.01 · 0.97 · 연구 객체**: 우리가 연구하려는 대상은 설계 원칙 자체의 참·거짓보다, 원칙이 특정 코드 수정에 미치는 운영상의 권위다.
  - **판단:** 표현을 스스로 실증 가능하게 좁힌다.
- **K04.02 · 0.95 · 관찰 구조**: 그 과정에는 적어도 네 순간이 있다: 원칙을 가르치는 순간, 지침으로 고정하는 순간, 실제 패치를 승인·거절하는 순간, 반대 증거를 받고 결정을 고치는 순간이다.
  - **판단:** 권위의 생애를 기술하지만 이미 확립된 자연 법칙이라 주장하지 않는다.
- **K04.03 · 0.96 · 인식론적 자율성**: 우리는 마지막 순간까지 포함해 원칙의 적용 권한을 잠정적이고 철회 가능한 것으로 다루자고 제안한다.
  - **판단:** 최초 창립 문제의식인 자율성과 철회 가능성을 복원한다.
- **K04.04 · 0.83 · 개념 위험**: 이 구조를 ‘운영상의 준공리화’라고 부르는 까닭은 원칙의 형식적 공리화를 비난하려는 것이 아니라, 조건부 조언이 실제 결정에서 충분한 근거 없이 명령의 힘을 갖는지를 시험하기 위해서다.
  - **판단:** 설명은 필요하지만 긴 문장과 새로운 명칭 자체의 학술적 가치는 미검증이다.
- **E04.01 · 0.97 · Object definition**: Our object is not the abstract truth of a design maxim but the operative authority it receives over a particular code change.
  - **판단:** Direct and bounded.
- **E04.02 · 0.95 · Process model**: That authority has at least four sites of inquiry: teaching the advice, encoding it as an instruction, using it to accept or reject a patch, and revising the decision after counterevidence.
  - **판단:** A proposed lens, not a discovered universal process.
- **E04.03 · 0.96 · Epistemic autonomy**: We propose treating principle-based authority as provisional and open to justified withdrawal.
  - **판단:** Preserves original ambition.
- **E04.04 · 0.84 · Conceptual caution**: Operational quasi-axiomatization is our name for the risk that conditional guidance is enforced beyond its grounds, not an attack on mathematical axioms.
  - **판단:** Requires more validation to remain beyond an evocative metaphor.

### 5. 4. 같은 코드에 다른 판정이 내려지는 이유 / 4. One patch does not contain its own verdict
- **K05.01 · 0.92 · 구성 사례**: 우리가 만든 도서관 예제에서는 기술보고서를 추가하되 정오표를 지원하지 않고, 기존 책 출력의 접두어까지 바꾸는 수정안을 고정했다.
  - **판단:** Meyer 원문 사례에 임의로 구성한 변경을 더했다는 출처를 분리한다.
- **K05.02 · 0.97 · 조건부 판정**: 기술보고서만 필요하고 접두어 보존 의무가 없다면 허용되지만, 접두어를 보존해야 하거나 정오표까지 필요하다면 같은 수정안도 거절된다.
  - **판단:** 무엇이 판정을 결정하는지 증명 가능한 범위에서 보인다.
- **K05.03 · 0.95 · 정보 부족**: 보호할 계약이 아직 알려지지 않았다면 즉시 승인이나 거절 대신 판단을 보류해야 할 수도 있다.
  - **판단:** 판정 보류의 정당성.
- **K05.04 · 0.99 · 역사적 정직성**: 이는 요구공학의 오래된 구별이지, 우리가 발견한 새 수학 법칙은 아니다.
  - **판단:** 실증 보강 사례와 독창성 주장을 절연한다.
- **K05.05 · 0.98 · 행동 연구 질문**: 그렇다면 AI가 ‘OCP 위반’이라고 분류한 결과를 실제 패치의 거절 근거로 옮길 때, 요구와 기존 계약의 증거를 어디까지 반영하는가?
  - **판단:** 이 예제가 후속 연구로 어떻게 이어지는지 구체적으로 연결한다.
- **E05.01 · 0.93 · Fixed case**: Our constructed library example holds fixed a patch that adds technical reports, omits errata, and alters an existing book-output prefix.
  - **판단:** Explicitly investigator-authored.
- **E05.02 · 0.97 · Conditional outcome**: That patch is acceptable when reports alone are required and the prefix is unprotected, but must be rejected if the prefix is protected or errata are also required.
  - **판단:** The same patch has no intrinsic verdict.
- **E05.03 · 0.96 · Uncertainty**: If the old contract is unknown, a justified response may be to defer judgment.
  - **판단:** No extrapolation from stipulated worlds.
- **E05.04 · 0.99 · Prior art**: This is familiar requirements reasoning, not a newly discovered mathematical law.
  - **판단:** Disarms a predictable novelty objection.
- **E05.05 · 0.98 · Transfer object**: The question for coding agents is whether a finding labeled 'OCP violation' is carried into patch rejection with due regard for those contracts.
  - **판단:** Connects case to AI behavior.

### 6. 5. 오래된 연구를 새 질문으로 연결하기 / 5. Making an old literature speak to a new decision
- **K06.01 · 0.96 · 정확한 위치**: 선행연구는 이미 SOLID 위반 분류, 에이전트 지침의 효과, 오래된 규칙과 코드의 충돌, 코드 리뷰의 과잉 수정을 다루었다.
  - **판단:** 기존 연구를 서로 분리되어 있었다고 잘못 선언하지 않는다.
- **K06.02 · 0.98 · 경쟁 연구 인정**: 따라서 우리가 ‘AI가 규칙을 따르기도 한다’는 사실을 처음 발견한 것은 아니다.
  - **판단:** 원고의 권위를 올리는 정직한 경쟁 설명.
- **K06.03 · 0.98 · 개척적 통합**: 여기서 제안하는 연결은 원칙의 역사적 조건, 현재의 지시 권한, 실제 패치의 계약 적합성, 이후 판단 철회를 하나의 연구 대상으로 묶는 것이다.
  - **판단:** 아이디어의 독창성을 효과의 최초 관측과 구별해 적극적으로 제시한다.
- **K06.04 · 0.90 · 측정 예시**: 예컨대 원칙 이름이 붙은 조언과 내용이 같은 익명 조언을 비교하면, 그 이름의 영향이 있는지 탐색할 수 있다.
  - **판단:** 좋은 돋보기이지만 논문 전체의 답은 아니라는 위치.
- **K06.05 · 0.95 · 방법론 반론**: 그러나 명칭 효과는 프레이밍이나 지시 우선순위의 일반적인 효과일 수 있으므로, 한 실험에서 차이가 나더라도 그것을 독립된 새 심리 기제로 선언할 수는 없다.
  - **판단:** 이름 실험이 프로젝트 전체를 축소하지 않게 제한한다.
- **E06.01 · 0.96 · Prior studies**: Existing studies already investigate SOLID-violation detection, agent instruction files, stale rules that conflict with code, and code-review overcorrection.
  - **판단:** Avoids sweeping firstness.
- **E06.02 · 0.98 · Priority limit**: We are not the first to notice that AI systems can follow inappropriate instructions.
  - **판단:** Prevents misleading framing.
- **E06.03 · 0.98 · Programmatic contribution**: Our proposed synthesis instead joins the original scope of design guidance, current instruction authority, contractual patch correctness, and the possibility of withdrawing a decision into one research problem.
  - **판단:** This is the work of the position paper.
- **E06.04 · 0.91 · One probe**: For instance, comparing recognizable principle names with equally authoritative unnamed advice can probe one part of that process.
  - **판단:** Restores label experiment as optional microscope.
- **E06.05 · 0.95 · Rival**: A name effect could still be ordinary framing or instruction-following, so it would not by itself reveal a new internal mechanism.
  - **판단:** Separates intervention from interpretation.

### 7. 6. 새로운 법칙을 선포하는 대신 연구를 열다 / 6. Open a field of questions, not a new commandment
- **K07.01 · 0.95 · 초대**: 이 문제에는 역사학자가 다룰 문헌의 변화, 요구공학자가 판정할 계약의 정당성, AI 연구자가 실험할 실제 수정 행동이 함께 있다.
  - **판단:** 서로 다른 분야의 방법을 단일 질문에 초대한다.
- **K07.02 · 0.98 · 반증**: 원칙의 이름이 판단을 바꾸지 않거나, 강한 SOLID 지시가 실제로 기존 계약을 더 잘 보존한다면 그 결과를 그대로 받아들여야 한다.
  - **판단:** 반대 결과가 학설의 일부를 약화시킬 수 있게 한다.
- **K07.03 · 0.89 · 장기 비전**: 더 긴 시간에서는 이런 결과를 토대로 SOLID가 언제 유용하고 어떤 경우 다른 구조가 나은지 설명하는 상위 이론을 찾을 수도 있다.
  - **판단:** 최초 아이디어의 야망을 되찾되 단언이 아니라 탐색으로 둔다.
- **K07.04 · 0.96 · 기여 명시**: 그러나 지금 이 글의 성과는 상위 법칙의 발견이 아니라, 관습처럼 사용되는 설계 원칙의 권위를 과학적 질문으로 바꾸자는 제안에 있다.
  - **판단:** 성과의 종류를 고유하게 규정한다.
- **K07.05 · 0.99 · 결론**: 좋은 원칙일수록 더 중요한 질문이 남는다: 그것이 바로 이 코드를 바꾸라고 말할 권한은 어디서 오는가?
  - **판단:** 문체적 개성을 살리면서 규범적 권위의 출처라는 본질로 닫는다.
- **E07.01 · 0.95 · Collaboration**: The question invites historians to track changes in guidance, requirements researchers to adjudicate protected obligations, and AI researchers to measure actual patch behavior.
  - **판단:** Concrete independent angles.
- **E07.02 · 0.98 · Falsifiability**: If familiar principle names make no difference, or strict SOLID advice preserves legacy clients better, those outcomes must count.
  - **판단:** A real chance to lose.
- **E07.03 · 0.89 · Vision**: In the longer run, this program may help explain when SOLID works, when another structure wins, and whether a more general account of good software design is possible.
  - **판단:** Ambitious but explicitly conditional.
- **E07.04 · 0.97 · Genre statement**: For now, our contribution is not such a law but an invitation to turn the authority of accepted design advice into an empirical and historical question.
  - **판단:** The 'newly opened inquiry' claim not pre-emptive global firstness.
- **E07.05 · 0.98 · Ending**: The better the principle, the more important the question: where does its authority to change this particular program come from?
  - **판단:** Distinctive, not a cliched AI manifesto.

## Adversarial critique
- **Unjustified historical storyline:** "principles passed through school into agents and acquired rule-like status" is a possible pathway to investigate, not a documented causal chain. v30 phrases it as questions.
- **Old field, new words:** Requirements traceability already studies client obligations; the paper's role is to ask about **epistemic and operational authority of design guidance in AI-mediated engineering**, not invent patch correctness.
- **Overbroad synthesis:** Joining three fields alone is not enough. The bridge is useful only if it enables identifiable history questions, behavioral comparisons and rebuttal/revision observations.
- **Rule obedience vs invalid rule:** Explicit authorized instructions may rationally dominate developer preference; revised authority doesn't mean arbitrary defiance of user policy.
- **Dogmatic replacement risk:** 'Operational quasi-axiomatization' may itself become another inflexible slogan. Always allow the possibility that observed outcomes are good ordinary instruction following, phrasing salience or classical requirements reasoning.
- **No artifice of certainty:** A position paper legitimately argues that an inquiry should be opened. It cannot claim the inquiry was never opened by anyone else or that the phenomenon is experimentally established.

## Mandatory retained scope
The name-effect contrast from v29 becomes a **single optional diagnostic**, not the entire thesis. Historical original and epistemic autonomy from 2026-07-29 and 2026-10-09 directly shape v30. Paper A / LAW-R2 formal conditional design law remains a longer-term objective **not claimed to be demonstrated here**.
