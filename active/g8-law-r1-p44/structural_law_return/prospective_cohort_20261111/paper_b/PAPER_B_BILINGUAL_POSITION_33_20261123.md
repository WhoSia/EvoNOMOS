# 원칙을 공리처럼 말할 때
*When Principles Sound Like Axioms: SOLID, Coding Agents, and an Open Question about Design*

**Paper B · v33 · concise bilingual position paper · 2026-11-23 · AUTHOR-REVIEW DRAFT (NOT SUBMITTED)**

# 한국어 원고

## 초록

SOLID는 소프트웨어 설계에 관해 생각하고 토론하는 데 유용한 원칙이다. 하지만 “OCP를 위반한다”는 진단과 “그러므로 이 수정안을 반드시 거절해야 한다”는 결정 사이에는 설명해야 할 거리가 있다. 우리는 그 거리가 생략되는 순간, **조건을 갖춘 설계 조언이 공리처럼 취급되는 것 아닌가**라고 묻는다. 이 글은 SOLID의 역사적 조건성과 현대 코딩 에이전트의 규범적 어휘를 연결해, 원칙의 명칭·위반 판정·명령형 표현이 실제 수정 판단으로 옮겨가는 과정을 연구 대상으로 제안한다. 나아가 그러한 원칙들보다 더 일반적인 조건부 설계 구조가 존재할 가능성을 열어 두되, 그것을 이미 발견했다고 주장하지 않는다.

## 1. ‘위반’이라는 말 다음에 생략되는 것

Robert Martin의 1996년 도형 예제는 새 도형을 쉽게 추가할 수 있는 설계를 보여 준다. 그런데 원을 사각형보다 먼저 그리라는 요구가 등장하면, 어느 쪽이 그 순서를 책임져야 할지 다시 판단해야 한다. Martin이 말한 *전략적 닫힘*은 모든 변화에 미리 대비할 수 없다는 인정에서 출발했다. 그는 공개 멤버 변수의 나쁜 스타일을 반드시 나쁜 설계로 보지는 않았고, RTTI를 사용하더라도 OCP를 해치지 않는 경우까지 논의했다.

**Martin이 논한 개방–폐쇄 원칙에는 어떤 변화에 대비할지에 관한 조건이 있었다. 그 조건을 잊는 순간이 문제다.**

이를테면 다음 두 문장은 다르다. “이 코드는 OCP 위반으로 볼 수 있다.” “OCP 위반이므로 이 패치는 반드시 거절해야 한다.” 앞의 문장은 설계를 평가하지만, 뒤의 문장은 실제 행동을 지시한다. 그 사이에는 앞으로 예상되는 변화, 보호할 기존 동작, 팀이 승인한 설계 정책, 대안의 비용에 관한 판단이 있어야 한다. 연구자가 구성한 동일한 도서관 패치도 기존 책 출력의 보존 여부와 새로 요구한 기능에 따라 승인되거나 거절된다. 코드만 보고 붙인 이름으로는 그 결정을 끝낼 수 없다.

## 2. 원칙은 언제 규칙이 되는가

우리가 탐구하려는 것은 SOLID가 옳으냐 그르냐를 가리는 재판이 아니다. **원칙(principle), 권고(guideline), 위반(violation), 필수(must), 공리(axiom)**라는 말이 실제 문서와 AI의 판단에서 어떤 일을 하게 되는지 묻는 것이다. 이 단어들이 언제나 같은 순서로 변한다는 뜻도 아니고, 강한 표현을 쓰면 반드시 잘못이라는 뜻도 아니다. 어떤 프로젝트는 SOLID를 명시적으로 승인된 개발 정책으로 삼을 수 있으며, 그 경우 에이전트가 정책을 따르는 것은 정당할 수 있다.

그럼에도 의문은 남는다. 특정 원칙에 붙은 이름과 권위가 적용 조건을 설명하는 일보다 먼저 패치의 합격·불합격을 결정하는가? 그 판단이 요구사항이나 기존 호출자의 동작과 충돌할 때는 어떻게 되는가? 우리는 이러한 가능성을 *운영상의 준공리화*라고 잠정적으로 부른다. 수학적 공리를 발견했다는 말이 아니라, **경험적 조언이 문장 속에서 어떤 자격으로 행동을 요구하는지** 살펴보자는 제안이다.

이 문제는 문헌과 코드 양쪽에서 조사할 수 있다. 원전·교육 자료·코드 리뷰·에이전트 지침을 비교해 단서와 예외가 실제로 빠지는지 살피고, 별도의 실험에서는 동일한 코드와 요구 및 정당한 지시 권한을 둔 상태에서 SOLID 관련 어휘가 패치 선택과 근거 수정에 미치는 영향을 확인하면 된다. 단순한 표현 차이와 실제 코드 변경을 구별해야 한다. 물론 원전의 조건이 이후 문서에도 잘 보존되거나, 어휘를 바꾸어도 패치가 달라지지 않는다면 이 가설은 좁혀질 것이다.

## 3. 이미 알려진 것, 새롭게 물을 것

여기서 지시 효과 자체를 최초로 발견했다고 말할 수는 없다. Zhu 등의 2026년 연구는 기존 코드 관례와 새 요구 사이에서 코딩 에이전트가 어떤 구현을 선택하는지 실험했고, Laddha 등의 연구는 지시의 위치·역할·출처 표지가 응답에 미치는 영향을 분리했다. 특히 후자의 ‘label’은 **SOLID처럼 역사적으로 이름 붙은 설계 원칙이 아니라 지시 출처를 표시하는 말**이다. 두 연구 모두 우리의 출발점이지만, 설계 원칙이 *조건부 조언에서 실제 수정 결정을 구속하는 말로 쓰이는 현상* 자체를 검증한 결과는 아니다.

우리가 새롭게 제안하는 것은 거대한 실험을 하나 더 실행했다는 주장이 아니라, 그 특정한 언어적·설계적 문제를 함께 연구하자는 초대다. 이것은 SOLID에 대한 사소한 말장난과 다르다. 원칙을 어떻게 부르는지가 개발자가 어떤 대안을 검토하고 에이전트에게 무엇을 요구하는지에 영향을 준다면, 용어를 고치는 일은 설계를 판단하는 방식을 고치는 일과 연결될 수 있다. **그 연결이 실제로 존재하는지는 실험과 역사 자료가 답해야 한다.**

## 4. 그 원칙들보다 위에 무엇이 있을까

가장 야심찬 질문은 여기서 한 발 더 나아간다. SOLID의 다섯 이름은 서로 독립적인 최종 명령이 아니라, 변화의 종류·보존할 계약·의존성의 이동·설계의 시간적 비용을 함께 따지는 더 일반적인 문제의 부분적 해법일 수 있을까? 가능성은 있다. 그러나 LSP의 행동적 치환 가능성처럼 단순한 변경 비용으로 환원하기 어려운 조건도 있어, 다섯 원칙을 하나의 공식에 넣는 작업부터 답으로 정할 수는 없다.

이 상위 구조의 탐구는 별도 연구 과제다. Paper B가 먼저 남기려는 질문은 더 작고, 어쩌면 더 불편하다.

**우리는 원칙을 적용하고 있는가, 아니면 원칙의 이름에 판정권을 주고 있는가?**

---

# English manuscript

## Abstract

SOLID is useful language for reasoning about software design. Yet the statement “this violates OCP” does not, on its own, entail “therefore reject this patch.” Something must justify that move. We ask whether conditional design advice sometimes acquires the status of a near-axiom when its name, a violation label, or mandatory wording is carried into actual engineering decisions. The paper proposes a focused historical and empirical investigation of **the normative vocabulary surrounding SOLID**, especially in AI-assisted coding. It also leaves open a larger possibility: the familiar principles might be partial expressions of a more general, conditional account of design. We do not claim to have found that account.

## 1. The missing step after “violation”

Robert Martin's 1996 drawing example lets new kinds of shapes be added without rewriting a drawing loop. A new requirement—to draw circles before squares—nevertheless raises another question: who owns their order? Martin's *strategic closure* accepted that no program can anticipate every possible change. He also distinguished poor public-field style from necessarily poor design, and described an instance in which runtime type identification remains compatible with OCP.

**Martin's advice came with conditions about anticipated change. Losing them is the concern.**

Consider two sentences, authored here as examples: “This design may violate OCP.” “Because it violates OCP, this patch must be rejected.” The first classifies; the second directs action. Between them belong the expected changes, protected client behavior, authorized project policies, and the costs of alternative designs. In our investigator-constructed library example, the very same patch can be accepted or rejected under different stated requirements and legacy obligations. A label attached to the code cannot settle that maintenance verdict.

## 2. When a principle becomes a rule

This is not a trial in which SOLID must be found guilty or innocent. We are asking what words such as **principle, guideline, violation, must, and axiom** do in design discussions and agent instructions. They do not necessarily form a historical sequence, and mandatory language is not automatically inappropriate. A team may legitimately adopt a strict SOLID policy; complying with it may be the right action.

The open question is more precise. Does a recognized principle's name begin to settle a patch disposition before anyone has established the scope in which it applies? What happens when contract evidence points elsewhere? We provisionally call this possibility *operational quasi-axiomatization*: not a claim about formal mathematical axioms or hidden model beliefs, but a proposal to study the authority that design vocabulary exercises over engineering action.

There are two independently startable inquiries. One can trace qualifiers and exceptions from primary sources into teaching materials, reviews, and agent instructions. Another can hold source code, requirements, authorized policies, and legacy obligations fixed while testing whether SOLID-related wording changes actual patch choices or justified revision. Wording changes that affect only explanations would not establish a decision effect. Nor would a historical corpus in which qualifications remain intact support a story of their disappearance.

## 3. A distinct question, not an invented result

Related empirical ground is substantial. Zhu et al. (2026) examined how coding agents choose between repository precedent and new task intent. Laddha et al. (2026) separately studied position, actual message role, and the *source label* attached to competing instructions. Their “label” is an attribution of instruction origin, not the historically recognized name of a principle such as SOLID. These studies explain why generic claims about agents following rules or labels would not be new.

Our invitation is instead to connect **SOLID's conditional content, the normative force of its vocabulary, and the resulting engineering verdict**. If the way a principle is named changes what developers or agents count as an admissible design, then the language of software engineering may be part of its decision machinery. Whether such a change occurs, and under which legitimate constraints, remains to be established rather than announced.

## 4. Might there be a structure above the names?

The longer ambition is to ask whether the five familiar principles are partial solutions to a deeper conditional problem: expected changes, protected behavior, dependencies, and costs over time. Some may fit that account better than others. Behavioral substitutability under LSP, for example, cannot simply be equated with reducing future edit costs. A single elegant formula that erases such distinctions would be another dogma, not a discovery.

That is an independent research programme. This paper begins with a smaller, sharper question:

**Are we applying the principle—or giving its name the authority to decide?**

---

## Primary sources, two newly curated PDFs, and scope

- R. C. Martin (1996), [*The Open-Closed Principle*](https://www.cs.utexas.edu/~fares/papers/OCP.pdf); D. L. Parnas (1972), [information-hiding criterion](https://doi.org/10.1145/361598.361623); Parnas (1979), [program families and extension/contraction](https://ocw.mit.edu/courses/16-355j-software-engineering-concepts-fall-2005/1c68d0f98909a126ec5eb6a0ff358ec7_parnas_ease.pdf).
- Zhu et al. (2026), [*Precedent or Intent? What Coding Agents Follow When Evolving Existing Code*, arXiv 2610.38244v1](https://drive.google.com/file/d/1mk1MmGh5QfFUPmT_CTe9srLTDEZjU784/view); Laddha, Pradhan & Srivastava (2026), [*Position, Role or Label?*, arXiv 2610.33201v1](https://drive.google.com/file/d/1E-alGOnlpVPoE8IHSF1USVyRWhMVQHrv/view). Both PDF files were read and curated under the [Research OS 10_PAPERS folder](https://drive.google.com/drive/folders/1D2M4LHcejREhlyp6vTd71xxLLx-6ldUP).
- [Full source-reading and custody ledger](79_PAPER_B_R34_TWO_2026_PDFS_FULLTEXT_READING_AND_DRIVE_CUSTODY.md); [SOLID normative-language hypothesis](80_PAPER_B_R35_SOLID_NORMATIVE_LEXICON_AND_FALSIFIERS.md); [separate higher-order structure conjectures](81_EVONOMOS_R36_HIGHER_ORDER_STRUCTURE_INDEPENDENT_CONJECTURES.md); [original 2026-07-29 research intent](73_PAPER_B_R28_FOUNDING_INTENT_NOVELTY_CATEGORIES_RECONCILIATION.md).
- A practitioner [software design guide](https://software-engineering-guide.github.io/en-us/topics/02-02-software-design-principles/) already explicitly warns against design heuristics hardening into dogma. It is **contextual practitioner writing**, not a peer-reviewed confirmation of a SOLID historical trend. Any novelty claim is in the proposed source-scoped investigation, not being the first person to notice "dogma".
- **Not yet done:** systematic historical corpus coding, inter-rater reliability, live coding-agent trial, measurement of quasi-axiomatization prevalence, causal proof of lexical authority, or discovery of a universal design structure. The only new completed work in this iteration is source review, editorial synthesis, and two Drive file-management operations.
