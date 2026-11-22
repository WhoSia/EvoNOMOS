# 원칙의 이름으로 코드를 바꿀 때
*When a Principle Becomes a Reason to Change Code: Design Authority and Its Limits in AI Programming*

**Paper B · v32 · bilingual position paper · 2026-11-23 · author-review draft, NOT submitted.** An interdisciplinary research proposal, not a report of a newly measured agent effect. Earlier v31 and its LIRA audit preserved.

# 한국어 원고

## 초록

좋은 설계 원칙은 코드를 개선할 이유를 준다. 하지만 그 원칙을 설명할 수 있다고 해서 눈앞의 수정안을 거절할 근거까지 확보되는 것은 아니다. 설계의 역사에는 어떤 변화에 대비하고 어떤 기존 동작을 지켜야 하는지에 대한 논의가 오래전부터 있었다. AI 코딩 에이전트가 원칙을 권고문으로만 읽는 게 아니라 실제 코드 수정과 검토에 활용하는 지금, 우리는 이 오래된 질문을 다른 층위에서 다시 묻는다. 설계 조언은 무엇을 근거로 실제 결정에 영향을 미치며, 그 근거가 달라졌을 때 판단은 어떻게 바뀌어야 하는가? 이 글은 이러한 **설계 원칙의 운영상 권위**를 역사·요구공학·AI 에이전트 연구가 함께 조사할 대상으로 제안한다.

## 1. 원을 먼저 그리라는 말

Robert Martin은 1996년 글에서 새 도형이 추가되더라도 그리기 루프를 수정하지 않아도 되는 설계를 설명했다. 한편 원을 사각형보다 먼저 그리라는 요구가 들어오면, 도형의 종류를 추가하는 일과는 다른 설계 판단이 필요하다. 순서를 보장할 책임은 그리기 함수에 있는가, 호출자에게 있는가, 별도의 정렬 정책에 있는가?

**OCP라는 이름은 그 답을 대신하지 않는다.**

실제로 Martin은 모든 변화에 대해 코드를 닫을 수는 없으므로 예상하는 변경에 맞춰 *전략적으로* 닫혀 있어야 한다고 설명했다. 공개 멤버 변수가 바람직하지 않은 스타일일지라도 반드시 잘못된 설계인 것은 아니며, RTTI 사용도 경우에 따라 OCP에 부합할 수 있다는 그의 예외 논의는 더 흥미롭다. Parnas가 앞서 제시한 정보 은닉과 프로그램 계열의 사고 역시 변화할 수 있는 결정이 무엇인지를 먼저 살피게 한다. 이 원전들은 설계 원칙이 적용될 조건을 생각할 자료다. 다만 이런 조건이 현대의 지침으로 전해지면서 실제로 얼마나 생략됐는지는 아직 별도로 조사해야 한다.

## 2. 이유, 권한, 영향

여기서 ‘권위’라는 말을 조심해서 써야 한다. **원칙을 적용할 기술적 이유**와 **그 지시를 집행할 정당한 권한**은 같지 않다. 예를 들어 어떤 변경이 OCP 관점에서 바람직해도 에이전트에게 기존 공개 API를 바꿀 권한이 없을 수 있고, 반대로 관리자가 강한 설계 규칙을 명시적으로 승인했다면 그 지시를 따르는 행위 자체를 교조주의라고 부르기도 어렵다.

한 가지가 더 있다. 원칙의 이름을 보여 줬더니 실제로 수정 방식이 바뀌었다면, 그것은 **행동에 영향을 주었다**는 관찰이지 그 결정이 옳았다는 판정은 아니다. 우리는 이 세 가지—기술적 근거, 정당한 지시 권한, 관찰되는 행동 변화—가 어디서 일치하고 어디서 갈라지는지 연구하고 싶다. *운영상의 준공리화*라는 표현은 그중에서도 적용 범위가 확인되지 않은 원칙이 충분한 이유처럼 취급되는 상황을 가리키는 잠정적 이름이다. 실제 에이전트에서 그런 현상이 어느 정도 나타나는지는 측정되지 않았다.

## 3. 고정된 패치가 답을 정해 주지는 않는다

우리가 구성한 도서관 사례에서는 기존 소스 파일은 그대로 두고 기술보고서용 제공자를 추가한다. 그런데 그 제공자는 정오표를 지원하지 않으며, 책 출력의 접두어를 `book`에서 `BOOK`으로 바꾼다. 기술보고서만 요구되고 접두어 보존 의무가 없다면 이 패치는 허용될 수 있다. 같은 패치라도 접두어가 기존 계약에 포함되면 거절해야 하고, 정오표까지 새로 지원해야 한다면 또 다른 이유로 불완전하다. 계약이 공개되지 않았다면 섣불리 합격이나 불합격을 정할 수도 없다.

코드는 그대로인데 판단이 달라지는 이유는 수수께끼가 아니다. **패치의 적합성은 코드와 요구사항, 보호해야 할 기존 동작을 함께 놓고 판단해야 하기 때문**이다. 반대로 OCP에 맞춰 변경 가능성이 높은 부분을 분리한 설계가 실제로 기존 호출자를 더 안전하게 보호한다면, 원칙을 근거로 그 대안을 선택하는 것도 정당할 수 있다. 우리가 알아내려는 것은 원칙을 자주 인용하는지보다, 에이전트가 이처럼 서로 다른 조건을 실제 패치 선택에 반영하는지다.

## 4. 무엇이 이미 연구되었는가

이 문제를 처음부터 새로 개척한다고 선언할 수는 없다. 2026년에는 코딩 에이전트가 기존 코드의 구현 관례와 새 지시를 어떻게 비교하는지 대규모로 분석한 연구가 발표됐고, 다른 연구는 지시가 도착한 위치·역할·표지가 판단에 미치는 영향을 따로 실험했다. SOLID 위반 분류, 저장소 지침, 오래된 규칙의 영향, 코드 리뷰의 과잉 판정에도 관련 선행연구가 있다.

이 연구들이 Paper B의 질문을 대신 끝내 주지는 않는다. 우리가 제안하는 연결은 **설계 원칙의 역사적 적용 조건 → 현재의 계약과 승인된 지시 → 실제 코드 수정 판단 → 새 증거에 따른 수정 또는 보류**라는 과정이다. 교육서와 개발 지침을 비교하면 적용 조건이 어떻게 전달되는지 살필 수 있고, 독립적으로 확인한 계약을 기준으로 실제 에이전트의 수정·거절·기권을 비교할 수 있다. 유명한 원칙의 이름을 붙였는지에 따른 차이를 측정하는 실험은 이 연구의 한 부분이지, 프로그램 전체를 대신하는 발견은 아니다.

## 5. 원칙을 무너뜨리지 않고, 적용을 묻다

실험에서 강한 OCP 지침이 실제로 기존 계약을 더 잘 지킨다면 어떨까. 그 결과는 이 연구의 실패가 아니라 원칙의 조건부 효용을 밝히는 자료다. 반대로 원칙 이름이 설명 문장에만 나타나고 코드 선택에는 영향을 주지 않는다면, 이름이 별도의 운영상 권위를 얻는다는 가설은 약해진다. 적법한 상위 지시를 따른 것과 부정확한 정보에 굴복한 것은 구별해야 하므로, 반대 증거를 제시하는 실험에서도 그 증거의 출처와 지시 우선순위를 명확히 해야 한다.

우리는 언젠가 더 넓은 설계 이론, 나아가 AI 코딩의 유지보수 비용까지 설명하고 싶다. 그러나 그 가능성을 지금 발견된 법칙이나 절감된 토큰의 수치로 포장할 생각은 없다.

**좋은 원칙이라면 더욱 물어야 한다. 이 코드를 바꾸라는 판단은 그 원칙의 어느 근거에서 나오는가?**

---

# English manuscript

## Abstract

A good design principle can be a reason to improve code. Knowing the principle, however, is not enough to justify rejecting a particular patch. Software-design history has long asked which changes an architecture should anticipate and which existing behaviors it must preserve. As coding agents turn design guidance into edits and review decisions, those questions gain a new setting. On what grounds does a principle influence a concrete change, and how should that decision respond when the grounds change? We propose **the operational authority of design principles** as a subject joining historical inquiry, requirements engineering, and research on coding agents.

## 1. Draw the circles first

In 1996, Robert Martin discussed a drawing design in which adding another shape need not require rewriting the drawing loop. But a demand to draw all circles before squares calls for a different design decision. Who owns the order: the loop, its callers, or a separate policy?

**The name OCP does not decide.**

Martin was explicit that no significant system can be closed against every possible change; closure has to be strategic. His discussion also distinguishes the poor style of public member variables from necessarily poor design, and allows runtime type identification in a case compatible with OCP. Earlier still, Parnas's work on information hiding and families of programs drew attention to decisions likely to change. These are historical resources for conditional design judgment, not evidence that we have traced a continuous transmission from those authors into today's agent instructions. Whether those qualifications survive, disappear, or change in later guidance remains to be studied.

## 2. Reasons, permission, influence

We need to distinguish three senses of authority. **Technical warrant** concerns whether a principle is a sound reason for a change under the relevant obligations. **Authorization** concerns whether the agent is legitimately empowered or required to make that change. A technically appealing refactor can still violate an approved public-API boundary; conversely, complying with an explicitly authorized strict policy is not, by itself, dogmatism.

A third matter is **behavioral influence**. If introducing a familiar principle changes which patch an agent selects, we have observed an effect on its behavior, not established the correctness of its choice. Our agenda is to examine how these three relations come apart or coincide. We use *operational quasi-axiomatization* as a provisional name for one possible failure: treating a principle as sufficient justification despite unresolved conditions of application. Its prevalence in actual agents is unknown.

## 3. The same patch, several legitimate verdicts

Our constructed library fixture holds the old source files fixed while adding a provider for technical reports. That provider does not support errata and changes the book-output prefix from `book` to `BOOK`. Under a report-only task with no obligation to preserve that prefix, the patch may be acceptable. Protect the prefix and it must be rejected; require errata too and it fails for a different reason. If the old contract is undisclosed, the evaluator may need to defer rather than invent it.

The apparent paradox disappears once we remember that **patch admissibility depends on the code, the requested change, and protected legacy behavior together**. The converse matters as well: if an OCP-oriented boundary demonstrably protects likely future changes and existing callers, choosing it may be the right engineering decision. What we want to investigate is whether agents respect both sides of that contextual judgment in actual edits—not merely how often they utter the acronym.

## 4. What the literature has already done

We are not the first to study coding agents' choices among competing sources of guidance. A 2026 study of repository precedent versus task intent already tested how agents respond to existing implementation patterns and explicit instructions. Another isolated position, message role, and textual label in instruction conflicts. Related work also covers SOLID-violation classification, repository instruction files, stale guidance, and automated-review overcorrection.

Our proposed connection is narrower in its mechanics but broader in its historical object: **the stated scope of a design principle, the current contracts and authorized directions, the resulting patch disposition, and justified revision or deferral after new evidence**. Historians could investigate how qualifications survive through teaching and development guidance; requirements researchers could supply independently adjudicated contract obligations; agent researchers could examine actual patches, refusals, and revisions. A named-versus-unnamed principle experiment is one diagnostic within this larger inquiry, not its entire contribution.

## 5. When should the rule apply?

Suppose strict OCP guidance improves preservation of old clients. That would be evidence for its conditional value, not a result we should explain away. If a principle's name changes explanations but leaves patches untouched, the case for a distinctive behavioral authority effect weakens. Tests involving contrary evidence must also respect its provenance and the actual instruction hierarchy: appropriately following an authorized higher-priority policy is not the same thing as overlooking a contract.

A broader conditional theory of design—and the cost of maintaining software with AI agents—remains an aspiration. Neither a new law nor a token-saving effect is reported here.

**The better the principle, the sharper the question: which of its grounds warrants changing this particular program?**

---

## References and provenance

- D. L. Parnas (1972), [modular decomposition](https://doi.org/10.1145/361598.361623); D. L. Parnas (1979), [extension and contraction](https://ocw.mit.edu/courses/16-355j-software-engineering-concepts-fall-2005/1c68d0f98909a126ec5eb6a0ff358ec7_parnas_ease.pdf).
- B. Meyer (1988), *Object-Oriented Software Construction*; first-edition source only partially recovered in [project passage note](13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md).
- R. C. Martin (1996), [*The Open-Closed Principle*](https://www.cs.utexas.edu/~fares/papers/OCP.pdf).
- Pehlivan et al. (2025), [*Are We SOLID Yet?*](https://arxiv.org/abs/2509.03093); Gloaguen et al. (2026), [*Evaluating AGENTS.md*](https://arxiv.org/abs/2602.11988); Xu & Wu (2026), [*Stale Instruction Files Override the Code*](https://arxiv.org/abs/2610.30571).
- Laddha, Pradhan & Srivastava (2026-10-23), [*Position, Role or Label?*](https://arxiv.org/abs/2610.33201); Zhu et al. (2026-10-28), [*Precedent or Intent?*](https://arxiv.org/abs/2610.38244). Both public full-text introductions/abstracts inspected for the current revision. Results cited belong to those authors.
- [Project-authored fixed source patch](31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md); [R32 trilemma and neighboring literature critique](77_PAPER_B_R32_AUTHORITY_TRILEMMA_AND_NEAREST_PRIOR_ART_COURT.md); [LIRA editorial method](https://app.notion.com/p/420ef561cf928159986dc36b3c6464f8).

**Evidential ceiling:** The constructed case and historical comparisons are motivation; no randomized experiment of the specified AI behavior or historical uptake process has been completed in this project. The paper proposes research instead of reporting its results.
