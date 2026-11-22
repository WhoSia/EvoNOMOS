# 원칙의 이름은 언제 수정의 이유가 되는가? — AI 코딩 에이전트에서 설계 조언의 결정 권위

*When Does a Principle's Name Decide a Patch? Design Advice and Operational Authority in Coding Agents*

**Paper B · v29 · short bilingual position paper · 2026-11-23 · AUTHOR REVIEW / NOT SUBMITTED**

# 한국어 원고

## 초록

설계 원칙은 어떤 코드를 왜 바꾸어야 하는지 설명할 수 있지만, 그 이름만으로 수정의 정당성이 결정되지는 않는다. 특정 변경 요구와 기존 호출자 계약을 확인해야 한다는 사실은 이미 요구공학이 가르쳐 온 내용이다. 새로운 질문은 AI 코딩 에이전트가 그러한 판단을 내릴 때 ‘개방–폐쇄 원칙’처럼 알려진 이름에 별도의 무게를 부여하는가이다. Meyer·Parnas·Martin의 설계 논의를 살피고, 똑같은 패치가 서로 다른 요구와 계약에 따라 다르게 판정되는 구성 사례로 문제의 경계를 정한다. 원칙의 이름만 바꾸되 지시의 내용과 우선순위는 같게 둔 비교, 독립적으로 확인한 계약 증거의 제시, 그 후의 실제 패치·판단 변화를 후속 실험으로 제안한다. 실험은 아직 수행되지 않았으며, 이 글은 새 설계 법칙이나 모델의 교조성을 발견했다고 주장하지 않는 포지션 논문이다.

## 1. 도형의 순서를 누가 정하는가

1996년 Robert Martin은 새로운 도형을 기존 그리기 함수의 수정 없이 추가할 수 있는 구조를 소개했다. 그 구조에 ‘모든 원을 사각형보다 먼저 그린다’는 요구를 더하자, 이전에 확보한 확장성만으로는 충분하지 않았다. 그렇다면 그 순서를 보장해야 할 곳은 그리기 함수인가, 호출자인가, 아니면 별도로 주입할 정렬 정책인가? Martin은 이 사례를 ‘전략적 닫힘(strategic closure)’이라고 설명하면서, 어떤 의미 있는 프로그램도 모든 변화에 닫힐 수는 없다고 인정했다. 그러므로 OCP라는 이름은 그 코드가 앞으로 어떤 변화에 대비해야 하는지 대신 말해 주지 않는다. AI가 코드에 ‘OCP 위반’이라는 표지를 붙이는 일과 그 표지로 특정 패치를 거절하는 일이 다른 이유도 여기에 있다.

## 2. 원전의 규칙은 생각보다 덜 완고했다

이러한 조건부 설계 사고는 SOLID라는 약어보다 오래되었다. Parnas는 1972년 모듈을 나눌 때 바뀔 가능성이 큰 설계 결정을 감추라고 권했고, 1979년에는 소프트웨어를 하나의 제품이 아니라 서로 다른 요구를 갖는 프로그램 계열로 바라보았다. Meyer의 초기 개방–폐쇄 논의에도 기존 이용자가 의존하는 안정된 설명과 확장 가능성이라는 별개의 의무가 함께 있었다. 더 흥미로운 반례는 Martin 자신의 글에 있다. 그는 공개 멤버 변수를 좋지 않은 스타일로 보면서도 반드시 좋지 않은 설계는 아닐 수 있다고 구별했고, RTTI 역시 조건에 따라 허용되는 사례를 제시했다. 원칙이 특정 기술을 금지한다는 짧은 구호보다 어떤 변경 위험을 줄이는지에 관한 설명이 먼저였던 셈이다.

## 3. 같은 수정안, 다른 판정

이전 연구에서 만든 작은 도서관 예제의 수정안은 기술보고서를 지원하지만 정오표는 지원하지 않으며, 기존 책 출력의 `book`을 `BOOK`으로 바꾼다. 요구가 기술보고서 추가뿐이고 기존 책 출력이 보호할 계약에 포함되지 않는다면, 그 수정안은 이 사례에서 승인 가능하다. 책 출력이 기존 계약에 포함된다면 같은 코드도 거절해야 하고, 정오표 지원까지 요구된다면 접두어와 무관하게 거절해야 한다. 책 출력의 보호 여부가 알려지지 않은 경우에는 적합성을 단정하지 않고 판정을 보류할 수 있다. 이 사례에서 새로운 것은 계약 논리가 아니라, 이름 붙은 원칙을 인용하는 에이전트가 그 조건을 실제 결정을 내릴 때 확인하는지라는 질문이다.

## 4. 이미 연구된 것과 아직 구별해야 할 것

SOLID 위반 분류 연구는 모델이 구조에 붙이는 라벨을 평가하지만, 그것만으로 개별 수정안의 승인 이유를 검증하지는 않는다. 반면 2026년의 코딩 에이전트 연구들은 지침 파일의 효과, 낡은 규칙에 대한 순응, 심지어 올바른 코드를 잘못 고치려는 코드 리뷰 경향까지 이미 조사했다. 따라서 ‘에이전트가 규칙을 지나치게 따른다’는 포괄적인 발견을 우리 것이라고 주장할 근거는 없다. 여기서 더 좁은 후보는 원칙의 내용과 지시 우선순위를 고정한 상태에서도 ‘OCP’라는 이름을 명시했는지에 따라 패치 결정이 달라지는지라는 문제다. 그런 차이가 발견되더라도 명칭의 권위, 표현의 익숙함, 단순한 주의 집중 가운데 무엇이 작동했는지는 추가 대조 없이는 알 수 없다.

## 5. 이름만 바꾸고 실제 패치를 보자

첫 번째 실험에서는 동일한 코드, 수정 요구, 기존 계약, 도구 예산을 제공하고, 같은 설계 조언을 원칙 이름이 붙은 표현과 이름 없는 표현으로 나누어 제시할 수 있다. 두 조건은 지시 내용과 우선순위가 같아야 하며, 같은 뜻을 전달하는 서로 다른 문장도 여럿 마련해야 한다. 그다음 요구서·테스트·기존 호출자에서 독립적으로 확인한 반대 증거를 동일하게 제시하고, 패치의 수용·거절·수정·기권을 기록한다. 원칙 이름이 존재할 때 정당한 반대 증거에 대한 수정이 감소한다면 흥미로운 신호지만, 유효한 상위 지시를 따르는 일까지 오류로 세서는 안 된다. 이전부터 준비한 NONE·HARD_SOLID·SCOPED_SOLID·EVIDENCE_CONDITIONAL의 네 조건은 지시 내용의 효과를 시험하는 별도 실험이므로 이 이름 비교와 혼동하지 않는다. 실제로 두 실험 모두 아직 수행되지 않았다.

## 6. 틀릴 자유가 있어야 연구할 가치가 있다

원칙 이름이 설명의 단어만 바꾸고 수정 결과에는 영향을 주지 않는다면, 특별한 결정 권위라는 가설은 약해진다. 오히려 기존 계약 보존을 개선하거나 일반적인 지시 순응으로 차이가 모두 설명된다면, 별도의 ‘준공리화’라는 개념을 고집할 이유가 없다. 역사 연구자는 원전의 예외가 실제 교육 자료와 에이전트 규칙에 어떻게 남는지 추적하고, 실증 연구자는 그 문구가 패치에 미치는 영향을 독립적으로 측정할 수 있다. 장기적인 토큰·비용·에너지 절감이나 SOLID를 통합하는 상위 법칙은 흥미롭지만, 그 가능성은 이번 아이디어의 증거가 아니다. 코드가 원칙을 어겼는지 묻기 전에, 그 원칙이 바로 이 코드를 바꾸라는 근거가 되는지부터 확인하자.

---

# English manuscript

## Abstract

A design principle can explain a software change without its name being sufficient to justify that change. The need to establish task requirements and protected clients is already familiar from requirements engineering. Our narrower question is whether a coding agent gives additional decision weight to a recognized label such as the Open–Closed Principle. We revisit Meyer, Parnas, and Martin and use a fixed-patch, variable-contract example to bound what can be inferred. We propose holding the advice and its instruction priority fixed while varying its name, then testing actual patch dispositions and revisions after independently authenticated contract evidence. No such agent experiment has yet been run, and the paper claims neither a universal design law nor an observed tendency toward dogmatism.

## 1. Who decides the drawing order?

In 1996, Robert Martin described a drawing routine that could accept another kind of shape without changing the routine itself. But a new demand that every circle be drawn before every square was not covered by that extension mechanism alone. Should the drawing routine, its callers, or a separately supplied ordering policy own that requirement? Martin called for strategic closure, explicitly acknowledging that no significant program can be closed against every imaginable change. The name of OCP cannot by itself establish which changes a program ought to anticipate. Likewise, detecting an OCP violation is not the same decision as rejecting a particular patch because of one.

## 2. The sources leave room for judgment

The idea that design advice depends on expected changes predates the SOLID mnemonic. Parnas's 1972 decomposition criterion focused on likely-to-change design decisions, while his 1979 account treated software as a family of programs meeting different demands. Meyer's early open–closed discussion also linked extension to descriptions on which existing clients could rely. A more striking qualification appears in Martin's own article. He distinguished a public field's poor style from necessarily poor design and gave a case in which run-time type identification did not violate OCP. The historically interesting question is therefore how the qualifications of a principle survive its later use as practical advice.

## 3. Same patch, different verdict

An author-constructed library patch adds technical-report support but not errata and changes an old book prefix from `book` to `BOOK`. It is admissible under a report-only demand when the book prefix is outside the protected contract. It must be rejected when the prefix is protected, or when errata are required for reasons independent of the prefix. If prefix protection has not been established, deferral may be the only justified response. The novel question we invite is not the contract logic but whether an agent invoking a named principle actually respects these conditions in its decisions.

## 4. What other work already explains

LLM work on SOLID-violation classification evaluates labels, not by itself the contractual justification for accepting an edit. Recent coding-agent studies already investigate repository rules, stale instructions that override code, and LLM reviewers that wrongly mark correct implementations as deficient. We cannot claim to have discovered, in general, that agents sometimes obey the wrong rule. A narrower candidate is whether attaching the familiar OCP name to otherwise equivalent and equally authoritative advice changes a patch disposition. Even a detected name effect might arise from framing, familiarity, or attention rather than a distinct form of dogmatism.

## 5. Vary the name, inspect the patch

A first experiment could hold the source, demand, protected clients, and tool budget fixed while comparing named OCP advice with otherwise equivalent unnamed advice. Both conditions must carry the same instruction priority, with several independently reviewed paraphrases to check semantic equivalence. After presenting independently authenticated contractual counterevidence, measure actual acceptance, rejection, patch revision, and abstention. A decrease in appropriate revision under the named condition would be informative, but obedience to a legitimate higher-priority instruction is not an error. The earlier NONE, HARD_SOLID, SCOPED_SOLID, and EVIDENCE_CONDITIONAL proposal instead varies the content of advice and must be analyzed separately. Neither study has yet been executed.

## 6. An invitation that can fail

If naming a principle changes only the explanation, a distinct effect on patch authority is unsupported. If naming improves contractual fidelity or ordinary instruction following explains the results, there is no reason to insist on a special quasi-axiomatization mechanism. Historians can trace the survival of original qualifications into later instructions, while empirical researchers can separately test whether their wording changes code decisions. Token, maintenance, and energy savings or a unifying law of design are interesting future possibilities, not findings of this proposal. Before asking whether code violates a principle, ask whether that principle warrants changing this code.

---

## 검증한 역사·경쟁 연구와 재현 자료 — References and provenance

- Parnas, D. L. (1972), “On the Criteria To Be Used in Decomposing Systems into Modules,” *Communications of the ACM*, [DOI 10.1145/361598.361623](https://doi.org/10.1145/361598.361623). 
- Parnas, D. L. (1979), “Designing Software for Ease of Extension and Contraction,” *IEEE Transactions on Software Engineering*, 5(2). [MIT 보존 원문 PDF](https://ocw.mit.edu/courses/16-355j-software-engineering-concepts-fall-2005/1c68d0f98909a126ec5eb6a0ff358ec7_parnas_ease.pdf).
- Meyer, B. (1988), *Object-Oriented Software Construction*, 초판 pp.22–25: [프로젝트 원문 복구 기록](13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md). 원전 **전체가 아니라 일부 페이지를 복구해 확인**한 자료.
- Martin, R. C. (1996), “The Open-Closed Principle,” *The C++ Report*, [1차 논문 PDF](https://www.cs.utexas.edu/~fares/papers/OCP.pdf); 특히 “Strategic Closure” 및 “Heuristics and Conventions”. 본문은 직접 인용이 아닌 요약이며, 원문은 절대적 금지 규칙에 대한 반례를 포함한다.
- Gamma, E., Helm, R., Johnson, R., Vlissides, J. (1994), *Design Patterns: Elements of Reusable Object-Oriented Software*, [출판사](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-9780201633610). GoF의 23개 패턴과 SOLID의 후대 약어는 동일한 규범체계가 아님.
- Pehlivan et al. (2025), *Are We SOLID Yet?*, [ASE NIER](https://conf.researchr.org/details/ase-2025/ase-2025-nier-track/35/Are-We-SOLID-Yet-An-Empirical-Study-on-Prompting-LLMs-to-Detect-Design-Principle-Vio) — SOLID 위반 **분류** 문제.
- Gloaguen et al. (2026), [*Evaluating AGENTS.md*](https://arxiv.org/abs/2602.11988) — 저장소 지침의 성능 영향.
- [*Do Agent Rules Shape or Distort? Guardrails Beat Guidance*](https://arxiv.org/abs/2604.11088) (2026) — 지침 파일·규칙의 효과 실험.
- Xu and Wu (2026), [*Stale Instruction Files Override the Code in Coding Agents*](https://arxiv.org/abs/2610.30571) — 코드와 충돌하는 오래된 명시 지시의 영향.
- Mehtiyev et al. (2026), [*When Instruction Files Go Stale*](https://arxiv.org/abs/2611.09802) — 원본 코드·과제 고정, 지침의 최신성 및 비용.
- (2026), [*Are LLMs Reliable Code Reviewers? Systematic Overcorrection in Requirement Conformance Judgement*](https://doi.org/10.1007/s10515-026-00638-5) — 요구 적합성의 과잉 오류 판정과 수정 제안 검산.
- [동일 패치 실행·판정 원장](31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md); [2026-10-09 네 조건 사전 실험 설계](https://github.com/WhoSia/EvoNOMOS/blob/main/active/g8-law-r1-p35/P35_B1_GO_AGENT_SOLID_PROMPT_RANDOMIZATION_PRESEAL.md).
- [R23 역사 원전 추가 검증](68_PAPER_B_R23_HISTORICAL_MARTIN_PARNAS_HEURISTICS_AUDIT.md); [R24 2026년 선행연구 충돌 및 새 실험 질문](69_PAPER_B_R24_2026_NEAR_COLLISIONS_AND_NAME_EFFECT_ESTIMAND.md).
- 이 문서는 **제안 논문**이다. 이름 효과, 코드 수정 효과, 반대 증거 후 판단 변경, 토큰·에너지 효율은 이 프로젝트에서 이번에 측정하지 않았다. 역사 해석과 외부 실험 결과는 각각 해당 출처의 자료를 인용하며, 저자의 새 관측으로 주장하지 않는다.