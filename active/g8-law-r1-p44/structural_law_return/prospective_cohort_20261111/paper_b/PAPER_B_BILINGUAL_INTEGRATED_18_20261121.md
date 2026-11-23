# Paper B — Bilingual Integrated Manuscript 18 (2026-11-21)

Previous v16 Notion canonical working page: https://app.notion.com/p/41fef561cf9281be95b8cf89fad99c33

**v18 is a separate manuscript draft; v17 and all earlier versions remain unchanged.** This edition separates SOLID violation classification from justified patch disposition, corrects the bounded Boolean mathematical presentation, and removes a P44 Go tangent from the Paper B main argument. Independent real reviewer outcomes and F38 remain OPEN.

Previous versions preserved. v15: https://app.notion.com/p/41fef561cf928109bba4d8b8c58a76a7

Its predecessor v16 independently replayed the archived OCP benchmark source and bounded the inference from code-internal comments. This new version preserves that audit while adding the primary-source rivals and exact bounded evidence certificates. Source audit code: [independent Python script](./audit_ocp_archive_independent_20261121.py); output: [independent JSON](./OCP_INDEPENDENT_ARCHIVE_AUDIT_20261121.json). No reviewer observations or new external spec are claimed.

---


통합 원고 18 · 분류 결과에서 수정안 판단까지의 추론 근거 정리 (2026-11-21). <mention url="https://app.notion.com/p/41bef561cf9281e1864afb74a3bbb4ce">Paper B 통합 원고 12 · 한·영 문장 교정</mention>과 <mention url="https://app.notion.com/p/41fef561cf9281aaa8cfdf0ca6f9b56f">Paper B 통합 원고 13 · 과도한 공리화, 감사 층화, 판정의 전제</mention>, <mention url="https://app.notion.com/p/41fef561cf928121af24cb634cdad9e3">Paper B 통합 원고 14 · 고전적 전제 이론·재현 자료 정합성 교정</mention>과 <mention url="https://app.notion.com/p/41fef561cf928109bba4d8b8c58a76a7">Paper B 통합 원고 15 · 분류→판정의 근거와 미보유 원전 반영</mention>을 별도로 보존한다. 본 판에서 제외한 파일 배치 실험은 12판과 재현 자료에 그대로 있다.

<b>초록 · 집필 시안</b>

개방–폐쇄 원칙 위반이라는 판정은 언제 특정 수정안을 거절할 근거가 되는가? 마이어와 마틴에게 모듈의 닫힘은 안정된 명세와 예상하는 변경을 떠나 성립하는 성질이 아니었다. 그런데 어느 변경을 맡고 어떤 기존 동작을 보존해야 하는지 확인하기 전에 위반 판정만으로 거절을 확정한다면, 설계 조언에 그 전제가 허용하지 않는 권위를 부여하는 셈이다. 우리는 이러한 판정 방식의 위험을 <b>과도한 공리화(over-axiomatization)</b>라고 부른다.

한 SOLID 위반 분류 벤치마크의 저장된 OCP 입력 768건을 감사했다. 제출 코드를 가리자 지시문 틀 24개가 남았고, 같은 모델·전략·언어 조합에서 12개 코드에 같은 틀이 사용됐다. 별도로 만든 도서관 프로그램에서는 한 수정안의 동작을 고정하고 적용할 요구와 기존 계약을 바꿨다. 정오표 지원이 필수라면 책 출력의 보존 여부와 무관하게 수정안을 거절할 수 있었다. 기술보고서만 필요할 때는 책 출력을 보장했는지가 판정을 갈랐다.

이 사례들은 실제 리뷰에서 원칙이 오용되는 빈도를 보여 주지는 않는다. 코드 리뷰 설명·패치 수용·LLM 요구 적합성을 측정한 선행 실증과 구별하여, 분류 결과를 특정 수정안의 거절 근거로 옮기려면 어떤 요구·기존 계약·호출 경로가 확인돼야 하는지 논증한다. 그 근거가 일부만 공개된 네 명세의 작은 사례에서는 거절을 확정할 수 있는 조건과 추가 질문이 필요한 조건을 구분한다.

<b>Abstract · Working draft</b>

When does a finding that code violates the open–closed principle warrant rejecting a particular patch? For Meyer and Martin, closure depended on stable specifications and anticipated changes. Treating a violation label as sufficient grounds for rejection before establishing what the patch must accomplish or preserve gives conditional design advice more authority than its premises allow. We call this risk in the use of design advice <b>over-axiomatization</b>.

We audited 768 saved OCP records from one SOLID-violation classification benchmark. Masking the submitted code left 24 instruction scaffolds, constant across twelve programs within each model–strategy–language combination. In a separate executable catalog example, we held a patch fixed and varied the demand and the contract with existing callers. Requiring errata was enough to reject the patch regardless of the book-output contract; requiring only technical reports left the verdict dependent on that contract.

These examples do not estimate how often OCP is misused in actual reviews. Unlike studies measuring review explanations, patch adoption, or LLM conformance errors, we examine the inference required to use a classification as grounds for rejecting a fixed patch: a governing request, protected old-client obligations, and the relevant call path. In four authored specifications with partial disclosure, we distinguish a decisive reason for rejection from a decision that requires another question.

## 한국어 원고

### 1. 서론

로버트 마틴이 1996년에 예로 든 함수는 목록에 들어온 순서대로 도형을 그린다. 삼각형이 자신을 그리는 메서드를 갖고 있으면 이 함수에 손대지 않고 삼각형을 추가할 수 있다. 마틴은 여기에 새 요구를 붙였다. 모든 원을 사각형보다 먼저 그려야 한다. 기존 함수에 사각형으로 시작하는 목록을 넘기면 여전히 사각형부터 그린다.

원을 먼저 놓는 일은 누가 맡았을까? 호출자가 원을 앞에 모아 넘기기로 했다면 함수는 제 일을 한다. 함수가 어떤 목록을 받아도 그 순서를 보장하기로 했다면 고쳐야 한다. 소스에서 그리는 순서를 읽을 수는 있지만, 그 순서가 잘못됐는지는 누가 정렬을 맡았는지에 달려 있다.

마틴의 그리기 함수는 도형을 하나 더 추가할 때는 그대로 둘 수 있었다. 함수에 정렬까지 맡기면 얘기가 달라진다. 우리는 변경 요구와 기존 호출자에 대한 약속을 확인하지 않은 채 OCP 위반이라는 평가만으로 수정안 거절을 확정하는 위험을 <b>과도한 공리화</b>라고 부른다. 이 이름은 원칙 자체가 무조건적인 공리였다는 역사적 주장이 아니라, 원칙을 적용하는 판정 방식에 관한 것이다.

분류 벤치마크의 저장 자료에서 모델에 어떤 지시가 주어졌는지 확인했다. 이어 도서관 예제에서 코드와 수정안을 고정한 채 새 요구와 기존 호출자에게 한 약속을 바꿨다. 도형 예제로 돌아가서는 별도 파일에 넣은 기능을 기존 함수로도 쓸 수 있는지 확인했다.

[Martin 1996, Listing 2와 Strategic Closure](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=6) · [벤치마크 기록 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [동일 패치 비교](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md)

### 2. 마이어와 마틴의 개방–폐쇄 원칙

마틴은 1996년 글에서 베르트랑 마이어의 1988년 초판 23쪽을 인용했다. 마이어에게 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 쓸 수 있는 모듈이다. 그의 도서관 예제에서 자료 유형을 하나씩 구별해 처리하는 프로그램에 기술보고서를 추가하면, 기존 모듈까지 고치거나 다시 컴파일해야 할 수 있다. 새 자료를 처리하는 코드의 위치에 따라 기존 모듈에 손이 가는 범위가 달라진다.

1995년 6월 공개 토론에서 카일 브라운은 잘못 설계된 클래스라면 소스를 고칠 수 있어야 한다고 했다. 마틴은 예상한 확장을 위해 기존 소스를 반드시 고쳐야 하는지를 물었다. 그러려면 어떤 변경이 생길지 미리 짚어야 한다. 2007년 공개 기록에는 다섯 원칙을 묶은 SOLID라는 이름이 나온다. 2009년 인터페이스 논쟁에서는 내부 클래스와 공개 플러그인 API에 서로 다른 조언이 제시됐다. 이 기록은 당시 원칙을 적용하거나 반대할 때 어떤 이유를 제시했는지 보여 준다. SOLID라는 이름이 널리 퍼지면서 적용 조건에 대한 판단이 실제로 변했는지는 별도의 역사적 증거가 필요하다. [1995년 토론](https://groups.google.com/g/comp.lang.c%2B%2B/c/nntTK8eH_Ag/m/uvoJEnDH9zAJ) · [2007년 자료](https://www.infoq.com/news/2007/01/principles-of-agile-design/) · [2009년 논쟁 기록](https://www.joelonsoftware.com/2009/01/31/from-podcast-38/)

마틴은 목록 정렬을 <code>DrawAllShapes</code>가 맡게 했다. 한 구현에서 <code>Circle::Precedes</code>는 상대 도형이 사각형이면 원을 먼저 놓는다. 원과 세 번째 도형의 순서를 정하려면 <code>Circle</code>도 고쳐야 할 수 있다. 반면 도형 종류별 순서를 표에 두면 사각형을 먼저 놓기 위해 표의 두 항목만 바꾸면 된다. 개별 도형을 넓이순으로 그리려면 그 표에 없는 정보가 필요하다.

마틴이 글 후반에 비교한 두 함수는 <code>dynamic_cast</code>를 쓴다. <code>DrawAllShapes</code>의 한 구현은 원과 사각형을 골라 그리고, <code>DrawSquaresOnly</code>는 사각형만 그린다. 둘 다 삼각형을 건너뛴다. 모든 도형을 그려야 할 때는 출력이 하나 빠진 셈이다. 사각형만 그려야 한다면 결과가 맞다. 코드와 프롬프트만 주어진 검토자는 각 함수에 어느 책임이 있는지 어디까지 알 수 있을까?

[Meyer 1988 초판 22–25쪽 대조 기록](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md) · [Martin 1996, 1쪽](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=1) · [Martin 1996, Listings 3–6, 9–10](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf)

### 3. 자료와 방법

우리는 서로 다른 두 자료를 사용했다. 벤치마크에서는 분류를 요구받은 모델에게 실제로 어떤 입력이 주어졌는지 조사했다. 도서관 예제에서는 패치 한 개를 고정하고, 적용할 요구와 보호할 계약을 바꿔 가며 실행 결과와 승인 기준을 대조했다. 벤치마크의 저장 코드와 도서관 코드는 별개이고, 어느 쪽에도 실제 검토자의 승인·거절 판단은 포함되지 않는다.

OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다. 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다. 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다. 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다. 정확히 일치하는 지시문 틀은 24개였다. 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다. 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.

지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다. 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다. 이 판독은 제출 코드를 가린 지시문에 관한 것이다. 독립 감사에서 Python 저장 행 192개를 이루는 고유 코드 12개를 검사하자 4개에서 주석 토큰 46개를 발견했고, docstring을 포함한 코드는 없었다. 주석이 기능의 의도를 암시할 수 있으므로, 지시문에 개별 요구가 없다는 사실을 코드 전체에 명세 단서가 없다는 주장으로 확대하지 않았다. 다른 세 언어의 주석은 같은 방법으로 계수하지 않았다.

저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다. Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다. 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다. 압축 파일 안의 코드 자체는 실행하지 않았다.

도서관 예제에서는 원본 소스와 수정안, 호출 입력, 새 모듈을 추가할 수 있다는 편집 범위를 고정했다. 코드 실행으로 확인한 것은 구체적인 입력에서 나온 출력과 예외다. 반면 기술보고서·정오표 중 무엇을 요구하는지, 책 출력의 접두어가 보호 대상인지, <b>새 요구를 충족하면서 보호된 기존 동작을 보존해야 승인한다</b>는 기준은 모두 연구자가 정했다. 이는 서로 다른 종류의 근거다. 따라서 §5의 표는 독립 심사위원의 판정이 아니라 우리가 지정한 기준을 실행 관찰에 적용한 결과다. 일부 전제만 공개한 경우에는 두 요구와 두 계약으로 이루어진 후보 명세 중 공개된 사실과 맞는 것만 남겼다. 이 후보군 밖의 실제 요구나 계약까지 조사했다고 가정하지 않는다.

[원본 ZIP](https://drive.google.com/file/d/12LDcKFBpJRkwH-zYJZ6Uhk9pE3RzgnUe/view) · [확장 감사 코드](https://github.com/WhoSia/EvoNOMOS/commit/38618a38d024351cc41f7c778af5074cb0f39467) · [독립 감사 재현 코드](https://github.com/WhoSia/EvoNOMOS/commit/50ded2d679b3f2cd85ecbe7ce3301e221b7365f6) · [독립 감사 JSON 결과](https://github.com/WhoSia/EvoNOMOS/commit/3accc623830b3444281d4ef5bcf9a7d78301668c) · <mention url="https://app.notion.com/p/41fef561cf92812cba98df158627c995">Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21)</mention>

### 4. 벤치마크가 판정에 제공한 정보

Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다. 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다. 모델의 분류 결과는 그 참조 라벨과 대조했다. OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다. DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다. 전략 간에 동일한 틀은 없었다. 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.

추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. <code>gpt-4o-mini</code>와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다. 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다. 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.

Python <code>EXAMPLE</code>의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다. 제출된 <code>AreaCalculator</code>는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다. 새 도형을 지원한다면 이 분기가 수정 후보가 된다. 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.

별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 <code>Rectangle.get_width</code> 선언을 뺐다. 저장 코드와 참조 쌍은 앞에서 명시한 문자열 정규화 기준에서 일치하지 않았으며, Python 코드에 한한 AST 비교에서도 일치 사례가 없었다. 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다. 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.

<b>표 1. 저장된 입력과 수정안 판정에 필요한 근거.</b>

| 검토할 질문 | 자료에서 확인한 내용 | 수정안 판정에 필요한 근거 |
| --- | --- | --- |
| 어떤 정답을 맞히는가 | 원저는 저자들이 검증한 참조 위반 범주에 모델 응답이 얼마나 일치하는지 평가했다. [원저 §III-A, C–D](https://arxiv.org/html/2509.03093v1#S3) | 구체적인 수정안과 승인 기준 |
| 어떤 기능을 추가해야 하는가 | 저장 Python EXAMPLE은 다형성으로 처리할 만한 반복 분기를 찾도록 했다. 개별 변경 요구는 템플릿에 별도로 적혀 있지 않았다. [대조 코드와 저장 행 위치](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53) | 실제 요청, 수용 조건, 변경을 맡을 경계 |
| 어떤 호출을 계속 지원해야 하는가 | 저장 템플릿에는 보호할 호출자 계약이 따로 없었다. 별도의 37번 참조 쌍에서는 너비 getter 선언이 빠졌다. [참조 쌍 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) | 계약의 범위와 근거가 되는 API 문서, 호출 코드, 테스트 또는 합의 |
| 구현에서 어떤 경계를 바꿀 수 있는가 | 저장 지시는 위반 범주와 설명을 요구한다. 업무상의 파일·인터페이스 보호 범위는 그 지시문에서 확인되지 않는다. [원저 §III-B 및 저장 행](https://arxiv.org/html/2509.03093v1#S3) | 보호할 산출물, 허용된 수정 또는 새 모듈 추가와 같은 경로 |

프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다. 참조 쌍 37번은 별도 참조 JSON에 있다. [저장 아카이브](https://drive.google.com/file/d/12LDcKFBpJRkwH-zYJZ6Uhk9pE3RzgnUe/view) · [정확 일치 및 양끝 공백 제거 대조](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

[Pehlivan 등 §III](https://arxiv.org/html/2509.03093v1#S3) · [아카이브와 참조 쌍 37 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [저장 입력과 참조본 대조 코드](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

Bräuer 등(2018)은 설계 원칙을 어떻게 측정할지 전문가에게 물었고, Cabral 등(2024)은 SOLID를 적용한 코드를 이해하고 확장하는 경험을 조사했다. Zhu 등(2026)은 구체적인 저장소 변경 과제에 기능 및 구조 검사를 결합했다. 이들은 무엇을 평가하는지가 서로 다르다. 우리의 벤치마크 감사도 분류 성능을 부정하려는 것이 아니다. 분류에 성공했다는 증거를 수정안 거절의 증거로 옮길 때 무엇이 더 필요한지를 묻는다. [Bräuer](https://doi.org/10.1016/j.jss.2018.03.002) · [Cabral](https://doi.org/10.1145/3644815.3644957) · [Zhu](https://arxiv.org/abs/2603.27745)

실제 리뷰 연구는 이 논문의 주장 범위를 더 엄격하게 제한한다. Widyasari 등(2025)은 Gerrit 코드 리뷰 댓글 793건을 분석하고 규칙이나 원칙을 근거로 드는 설명 유형을 확인했다. 이는 원칙에 의거한 설명이 리뷰에 존재한다는 증거지만, 원칙이 잘못 적용돼 특정 수정안이 거절됐다는 증거는 아니다. Papotti 등(2024)은 컴퓨터과학 석사과정 학생 72명을 대상으로 보안 자동 수리 패치의 채택 여부를 실험했다. 제안 도구의 전문성을 알리는 정보에 따라 판단이 바뀌는 현상을 관찰했지만, 원칙 위반 라벨을 대상으로 한 연구는 아니다. 두 논문의 실제 사람에 대한 관측은 우리가 구성한 표 2의 승인 기준과 다르다. [Widyasari 등](https://doi.org/10.1145/3708518) · [Papotti 등](https://doi.org/10.1007/s10664-024-10506-z)

Jin과 Chen(2026)은 정답 코드와 결함 코드에 대한 다섯 언어 모델의 요구 적합성 판단을 세 프로그래밍 벤치마크에서 실험하고, 맞는 코드를 잘못 거절하는 현상과 설명·수정 제안을 요구하는 프롬프트의 위험을 보고했다. 따라서 LLM의 과잉 거절을 처음 지적했다고 주장할 수 없다. Ling·Zou·Liu(2026)는 공개 GitHub 변경 사례의 질적 연구에서 병합, 이슈 종료, 요구 충족이 서로 다른 결과일 수 있음을 논증했다. 수용 경계가 조건부라는 발견도 우리의 최초성이 아니다. 우리 사례는 <b>실행 결과가 고정된 패치에서 현재 공개된 요구·계약이 정당화하는 판정과 추가 질문을 정확하게 분리하는 재현 가능한 실례</b>다. [Jin·Chen, 읽은 arXiv v1](https://arxiv.org/abs/2603.00539) · [Ling 등](https://doi.org/10.3390/systems14101312)

그 질문 자체에도 중요한 선행연구가 있다. Kane(2013)은 검사 점수의 해석을 뒷받침하는 증거가 그 점수를 특정 결정에 사용하는 일까지 정당화하지는 않는다고 논했다. 이는 소프트웨어 리뷰를 실험한 결과가 아니라, 평가 결과의 <i>사용</i>을 따로 정당화해야 한다는 일반적인 논증이다. Zave와 Jackson(1997)은 요구사항, 기계 명세, 환경에 관한 지식이 어떻게 연결되는지 설명하면서 행위의 통제 주체를 구별했다. 원을 앞에 정렬할 책임이 호출자에게 있는지 함수에 있는지부터 따져야 한다는 우리의 질문도 이러한 오래된 문제의 한 사례다. 존스(1981) 역시 병렬 프로그램에서 환경 의존 조건과 프로그램 보장 조건의 양립을 다뤘다. 우리는 이 이론들을 새로 제안하지 않는다. [Kane](https://drive.google.com/file/d/1nbQUgK4kFkjKS4X9Op_q2e5H-Vgm8epM/view) · [Zave–Jackson](https://drive.google.com/file/d/1PwUeINSkW6vhhuUvYEh9YvGQFBWlWlav/view) · [Jones](https://drive.google.com/file/d/1c2vEnheOmaTgKti8eexRyks-vwkBdnv4/view)

Barr 등(2015)이 정리한 테스트 오라클 문제는 코드 실행과 올바름 판정 사이에도 근거가 필요함을 상기시킨다. §5의 시험은 지정된 호출의 동작을 확인하지만, 그 동작을 보존하겠다는 실제 프로젝트의 약속을 입증하지는 않는다. 따라서 다음 절의 요구·계약은 발견한 사실이 아니라 명시적으로 정한 전제다. [Barr 등](https://drive.google.com/file/d/1GvLHYntPcmuPdjuFmKZdenmBHeAy0SxY/view)

**분류 결과에서 수정안 거절까지.** 위반 범주를 맞혔다는 사실은 코드에 특정 구조가 있다는 평가를 뒷받침한다. 그러나 수정안을 거절하려면 (1) 누구에게서 나온 새 요구인지, (2) 기존 호출자에게 계속 보장하기로 한 동작이 무엇인지, (3) 그 동작과 새 기능을 어느 호출 경로로 제공해야 하는지까지 알아야 한다. 이 가운데 일부는 소스에 표시될 수 있지만, 관측한 구현이 곧 승인된 계약이라는 뜻은 아니다. 예컨대 같은 출력 변경을 보고도 책 출력이 보호 대상일 때와 아닐 때는 서로 다른 판정이 가능하다. 분류 라벨을 고정한 채 판정이 달라지는 반례는 §5에서 실행한 동일 패치의 네 명세에 한정된다. 이를 통해 분류 점수 자체를 부정하거나 실제 리뷰어가 라벨 때문에 패치를 거절했다고 주장하지 않는다.

### 5. 같은 수정안의 판정이 달라질 때

마이어의 도서관 예제를 작은 프로그램으로 만들었다. <code>client.py</code>는 전달받은 목록 함수로 자료를 출력한다. 수정안은 그 함수에 새 처리를 덧붙이는 <code>reports.py</code>를 추가한다. <code>catalog.py</code>와 <code>client.py</code>의 소스는 그대로다. 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다. 기존 책 출력에서는 접두어가 <code>book</code>에서 <code>BOOK</code>으로 바뀐다.

기술보고서만 지원하면 되는 경우를 보자. 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다. 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다. 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다. 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다. 책 접두어가 보호 대상이 아니라는 가정은 실제 이용자가 그 출력을 기대하지 않는다는 관찰이 아니다. 단지 이 비교에서 보존 의무로 정하지 않았다는 뜻이다.

<b>표 2. 같은 수정안에 적용한 요구와 계약.</b>

| 요구 | 기존 책 접두어 보호 | 새 요구 만족 | 기존 계약 보존 | 이 사례의 승인 기준 |
| --- | --- | --- | --- | --- |
| 기술보고서 | 아니오 | 예 | 예 | 승인 |
| 기술보고서 | 예 | 예 | 아니오 | 거절 |
| 기술보고서와 정오표 | 아니오 | 아니오 | 예 | 거절 |
| 기술보고서와 정오표 | 예 | 아니오 | 아니오 | 거절 |

“정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다. 둘 다 거절이다. 책 계약까지 확인할 필요는 없다. “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다. 하나는 승인, 하나는 거절이다. 이때 확인할 것은 기존 책 출력이 보호 대상인지다.

이 절차는 실제 명세가 표의 네 경우 중 하나라는 조건 아래서만 성립한다. 공개된 사실과 맞는 행이 하나도 없다면 승인이나 거절을 내릴 것이 아니라 자료 또는 후보군이 잘못됐는지 확인해야 한다. 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다. 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다. 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.

**최소 판정 근거.** 정오표 지원이 필수인지 여부를 $E$, 기존 책 출력 접두어를 보호하는지 여부를 $B$라고 두자. 연구자가 정한 네 명세에 한정하면, 이 고정 패치의 승인 조건은 $A(E,B)=\neg E\land\neg B$다. 따라서 승인에 필요한 최소 증거는 $\{\neg E,\neg B\}$이며, 거절을 확정하는 최소 증거는 $\{E\}$ 또는 $\{B\}$다. 두 조건을 모두 알 수 없다면, 승인 명세 $(E=0,B=0)$와 거절 명세 $(E=1,B=0)$가 양립하므로 판정을 보류한다. 기술보고서만 요구한다는 사실, 즉 $\neg E$가 확인되면 $B$를 물어 어느 쪽인지 결정할 수 있다. 반면 두 조건이 전부 미공개일 때는 하나의 예·아니오 질문만으로 모든 답변에 대해 판정을 확정하지 못한다.

이것은 새로운 논리 규칙이 아니라 고전적인 유한 정보 집합 판정이다. 별도 Python 코드는 네 명세의 공개 상태 아홉 가지, 최소 승인·거절 증거, 보류 상태의 대립 명세, 모순된 사실의 처리까지 검사했고 [독립 CI 30개 테스트](https://github.com/WhoSia/EvoNOMOS/actions/runs/44911870723)가 통과했다. 이 테스트가 실제 검토자의 판단이나 원본 도서관 프로그램의 전체 동작을 재검증한 것은 아니다. 또한 고정된 계약에 관한 사실을 <i>알게 되는 것</i>과 계약 자체를 <i>변경하는 것</i>을 구별해야 한다. 앞의 경우에는 가능한 명세의 집합이 줄지만, 뒤의 경우에는 승인 조건 자체가 달라질 수 있다.

같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다. 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다. 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다. 이 비교에서 얻은 것은 새로운 논리 규칙이 아니다. 한 사실만 알아도 거절이 확정되는 경우와, 책 출력 약속을 물어야 하는 경우를 구체적인 호출 결과로 구분한 것이다. 실제 리뷰에 적용하려면 요구서와 API 문서, 테스트 및 호출 기록에서 그 약속의 근거를 따로 찾아야 한다.

[네 조합의 재현](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md) · [정보 공개 조건별 결과](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/34_MAINTENANCE_JUDGMENT_UNDER_PARTIAL_DISCLOSURE.md)

### 6. 기존 호출 경로도 요구의 일부일 때

완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다. 여기서는 앞의 질문에 해당하는 관찰만 남긴다. 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 <code>bracketed=True</code>를 넘기면 인자를 거절했다. 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다. 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.

새 기능이 있다는 사실과 <b>요구된 호출 경로에서 쓸 수 있다는 사실</b>은 다르다. 보호해야 할 기존 진입점이 무엇인지 확인하지 않으면, 같은 옵션을 새 함수에서 제공했다는 사실만으로 수정안의 적합성을 판정할 수 없다. 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 <mention url="https://app.notion.com/p/41bef561cf9281e1864afb74a3bbb4ce">Paper B 통합 원고 12 · 한·영 문장 교정</mention> 및 [실행 기록](https://github.com/WhoSia/EvoNOMOS/commit/0ede7b241c8f9f50436be9703561bb9e7cc9fb8b)에 원형 그대로 보존했다.

### 7. 결론

마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다. 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다. 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다. 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다. <b>원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가</b>가 이 논문에서 다룬 질문이다.

실제 검토에서 먼저 확인할 것은 수정안의 새 기능만이 아니라, 요구한 사람이나 합의된 문서가 그 기능을 어느 진입점에서 제공하도록 정했는지다. 그다음 기존 호출자가 의존하는 동작 중 무엇이 보호 대상인지 요구서·API 문서·테스트·호출 코드에서 근거를 찾아야 한다. 이 근거가 둘 이상의 가능한 계약을 남긴다면, 원칙 위반이라는 이름으로 결론을 확정하기보다 계약의 출처와 범위를 묻는 편이 정확하다. 반대로 새로운 요구를 충족하지 못한다는 사실이 이미 확정됐다면, 어떤 기존 계약이 추가로 보호되는지 모두 조사하기 전에 해당 수정안을 거절할 수도 있다. 이러한 질문의 순서는 이 논문의 구성 사례에서 나온 실무적 제안이지, 실제 개발 조직의 효율이 개선됐다는 관측 결과는 아니다.

공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다. 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다. 이 연구는 한 벤치마크의 저장 입력과 연구자가 구성한 실행 예제만을 다뤘다. 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.

### 부록 A · 재현 자료

§3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다. 독립 감사 스크립트는 같은 ZIP을 실행 코드가 아닌 자료로 읽어 16개 JSONL 파일, 768행, 48개 고유 코드, 24개 틀, 64개 세부 집단을 재계산했고, Python 고유 코드 12개 중 주석이 있는 4개를 확인했다. 기록된 수치의 기준은 [JSON 결과](https://github.com/WhoSia/EvoNOMOS/commit/3accc623830b3444281d4ef5bcf9a7d78301668c)다. §5–§6은 이 연구에서 만든 예제를 실행한다. 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다. 아래 표는 §5의 아홉 판정이다. 12판에 있던 그림 1과 파일 배치 실험은 18판 본문에 싣지 않았으며, 원본 그림과 실행 기록을 12판에 보존했다.

[재현 자료 및 명령 / Reproduction notes](https://github.com/WhoSia/EvoNOMOS/commit/ed443890f0b5f9b171d68d010b605e7cefec7f14)

‘미공개’인 항목의 값은 두 가지 모두 가능하다. 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.

| 공개된 요구 | 책 접두어 보호 제외 | 책 접두어 보호 포함 | 책 접두어 계약 미공개 |
| --- | --- | --- | --- |
| 기술보고서 | 승인 | 거절 | 보류 |
| 기술보고서와 정오표 | 거절 | 거절 | 거절 |
| 요구 미공개 | 보류 | 거절 | 보류 |

## English manuscript

### 1. Introduction

In 1996 Robert Martin described a function that draws shapes in the order it receives them. A triangle can be added without touching the function if the triangle supplies its own drawing method. Then Martin changes the task. Every circle must be drawn before any square. Give the function a list that begins with a square and it still draws the square first.

Who was supposed to put the circles first? If the caller agreed to sort the list, the routine does its job. If the routine must guarantee that order for any list, it needs an edit. The source tells us what gets drawn first. The agreement tells us whether that is a problem.

Martin’s drawing routine could stay as it was when the task was to add a shape. Making it responsible for sorting changes that judgment. We use <b>over-axiomatization</b> for the risk of treating an OCP violation label as sufficient grounds to reject a patch without establishing the governing change and caller obligations. This is a claim about the use of advice, not a historical claim that OCP became a formal axiom.

We inspect a classification benchmark’s archive to see what instructions its models received. In a separate catalog example we keep the code and patch fixed while varying the request and the promises to existing callers. We then return to drawing to test whether a feature added in a separate file can be reached through the original function.

[Martin 1996, Listing 2 and Strategic Closure](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=6) · [Benchmark archive audit](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [Fixed-patch comparison](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md)

### 2. The open–closed principle in Meyer and Martin

Martin attributed the principle to Bertrand Meyer, citing page 23 of the 1988 first edition. For Meyer, a closed module has a stable specification that other modules can rely on. His library example gives this a practical meaning. If a catalog handles publication types one by one, adding technical reports can require editing or recompiling existing modules. Where the new code goes affects how much of the existing system must change.

In a June 1995 public exchange, Kyle Brown argued that developers had to be able to fix a badly designed class. Martin asked whether an anticipated extension had to require an edit to existing source. That answer still depends on which changes can be anticipated. The public record uses SOLID for the five principles by 2007. A 2009 discussion gave different advice for internal classes and public plugin APIs. These records show particular uses and objections. They do not establish that circulation of the SOLID label caused the governing conditions to change. [Contemporary exchange](https://groups.google.com/g/comp.lang.c%2B%2B/c/nntTK8eH_Ag/m/uvoJEnDH9zAJ) · [2007 report](https://www.infoq.com/news/2007/01/principles-of-agile-design/) · [2009 exchange](https://www.joelonsoftware.com/2009/01/31/from-podcast-38/)

Martin made <code>DrawAllShapes</code> responsible for sorting. In one implementation <code>Circle::Precedes</code> checks the other shape and puts a circle before a square. Deciding where a third shape belongs relative to a circle can require an edit to <code>Circle</code>. Placing the order of types in a table lets squares go first with a swap of two entries. Sorting individual shapes by area would require information that the table does not hold.

Later in the article Martin compares two uses of <code>dynamic_cast</code>. One version of <code>DrawAllShapes</code> draws circles and squares, and <code>DrawSquaresOnly</code> draws squares alone. Both skip a triangle. A triangle left undrawn is a missed output when the task is to draw all shapes. When the task is to draw squares, skipping it is correct. How much of that responsibility can a reviewer determine from code and a prompt?

[Meyer 1988, first edition, pp. 22–25](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md) · [Martin 1996, p. 1](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=1) · [Martin 1996, Listings 3–6, 9–10](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf)

### 3. Materials and methods

We used two distinct sources of evidence. We audited the saved benchmark inputs to determine what a classifier was actually asked to judge. Separately, we fixed one catalog patch and varied the demands and protected caller commitments against which its execution was assessed. The benchmark submissions are not instances of the catalog patch, and neither source records decisions by real reviewers.

The OCP reference material contains 48 before-and-after code pairs. Sixteen saved JSONL files each contain 48 records, yielding 768 rows. Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times. We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality. The result was 24 scaffolds. Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs. The 768 records are repeated submissions, not independent maintenance cases.

We separately read the masked instructions for case-specific change requests and protected caller commitments. An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape. We inspected the text outside the submitted code, not the whole semantic context. In a separate replication, the 192 saved Python rows reduced to twelve distinct code submissions; four contained a total of 46 comment tokens, and none had an AST-detected docstring. These comments may convey implementation intent, but counting them does not establish a contract. We did not perform the same comment-token audit for the other three languages.

We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace. For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions. These tests do not establish whether inherited methods remain available or whether callers were promised a behavior. We read code as archive data and did not execute it.

For the catalog, we fixed the baseline, candidate patch, calls and permission to add a module. Executing the code established outputs and exceptions for those calls. The possible demands (technical reports alone, or technical reports and errata), the two scopes of the book-output obligation, and <b>the rule that an acceptable patch must meet its demand and preserve protected behavior</b> were stipulated by us. Table 2 therefore applies authored criteria to observed behavior; it does not report independent human decisions. For partial disclosure, we retained only the candidate specifications compatible with known facts. We did not attempt to enumerate obligations outside these four constructed cases.

[Archived ZIP](https://drive.google.com/file/d/12LDcKFBpJRkwH-zYJZ6Uhk9pE3RzgnUe/view) · [Extended audit](https://github.com/WhoSia/EvoNOMOS/commit/38618a38d024351cc41f7c778af5074cb0f39467) · [Independent source audit](https://github.com/WhoSia/EvoNOMOS/commit/50ded2d679b3f2cd85ecbe7ce3301e221b7365f6) · [Recomputed JSON](https://github.com/WhoSia/EvoNOMOS/commit/3accc623830b3444281d4ef5bcf9a7d78301668c)

### 4. What the benchmark gives the reviewer

Pehlivan et al. chose violation scenarios and refined the generated examples. A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion. The benchmark compares model classifications with the resulting labels. After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL. No two strategies shared a template string. None of the templates separately stated the requested change or protected caller contract for an individual case.

An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: <code>gpt-4o-mini</code> differed from the other three models. Holding model, strategy and language fixed left one scaffold shared across twelve programs. No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST. These checks do not establish semantic independence or source lineage.

One Python <code>EXAMPLE</code> prompt directs the reviewer to repeated branches where polymorphism might fit. The submitted <code>AreaCalculator</code> branches on shape type to calculate the area of a circle or rectangle. If a new shape is needed, that branch is a place to look. The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.

The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of <code>Rectangle.get_width</code>. No submitted program matched a reference side under the reported textual normalizations, and the separate Python-only AST comparison also found no match. Pair 37 establishes that a declaration was removed. Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.

<b>Table 1. Evidence in the saved material and evidence needed to assess a patch.</b>

| Question | Evidence in the saved material | Evidence for a patch decision |
| --- | --- | --- |
| What counts as a correct answer? | The benchmark compares model responses with the violation labels verified by its authors. | The proposed edit and the criteria for acceptance. |
| Which behavior should be added? | The saved Python EXAMPLE prompt points to repeated branching where polymorphism would fit. The templates state no separate request for an individual case. | The actual request, its acceptance conditions, and the boundary responsible for it. |
| What do existing callers rely on? | The templates state no separate caller contract. The distinct reference pair 37 loses the width getter declaration. | The scope of the commitment and supporting API documentation, client code, tests, or agreement. |
| What may the implementation change? | The instructions ask for a violation category and an explanation. They do not specify protected implementation files or interfaces. | The protected artifacts and permitted changes, including whether a new module may be added. |

The prompt example is in JSONL line 13 (record ID 12). Pair 37 is in a separate reference JSON file. [Archived material](https://drive.google.com/file/d/12LDcKFBpJRkwH-zYJZ6Uhk9pE3RzgnUe/view) · [Source comparison](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

[Pehlivan et al., §III](https://arxiv.org/html/2509.03093v1#S3) · [Archive audit and reference pair 37](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [Submitted and reference source comparison](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

Bräuer et al. (2018) examined the measurement of design principles with experts; Cabral et al. (2024) studied understanding and extension under a bundled SOLID treatment; Zhu et al. (2026) supplied repository change tasks with functional and structural checks. These evaluate different objects. Our audit does not contest the benchmark's classification task. It asks what else would be needed to use such a classification as a reason to reject a patch. [Bräuer](https://doi.org/10.1016/j.jss.2018.03.002) · [Cabral](https://doi.org/10.1145/3644815.3644957) · [Zhu](https://arxiv.org/abs/2603.27745)

Empirical review studies narrow the claim further. Widyasari et al. (2025) coded 793 Gerrit review comments and identified explanation categories including appeals to rules or principles. This shows that principle-based explanations appear in review practice; it does not show that such principles caused an unjustified patch rejection. Papotti et al. (2024) experimentally studied 72 computer-science master's students deciding whether to adopt security patches proposed by automatic program repair tools, and found that information about the purported tool specialization influenced decisions. Unlike our stipulated Table 2 judgments, those were observed human choices. [Widyasari et al.](https://doi.org/10.1145/3708518) · [Papotti et al.](https://doi.org/10.1007/s10664-024-10506-z)

Jin and Chen (2026) tested five language models' judgments of canonical and buggy implementations against natural-language specifications across three programming benchmarks. They reported false rejection of correct code and risks from prompts that demand explanations or fixes. We cannot claim to have discovered LLM over-rejection or to improve its error rate: our archive does not record independent patch-acceptance judgments by those models. Ling, Zou, and Liu (2026) examined public agent-associated contributions and distinguished merges, issue closures, and requirement satisfaction. Conditional acceptance is not first discovered by this paper either. Our narrower addition is <b>to hold a patch's execution fixed and make explicit which partially disclosed requirement and contract facts warrant a verdict and which warrant further inquiry</b>. [Jin and Chen, held arXiv v1](https://arxiv.org/abs/2603.00539) · [Ling et al.](https://doi.org/10.3390/systems14101312)

This is not a new problem in general. Kane (2013) argues that evidence supporting an interpretation of test scores does not automatically justify using those scores for a particular decision. His work does not test software reviews; it establishes the importance of justifying an assessment's <i>use</i>. Zave and Jackson (1997) distinguish requirements, machine specifications and knowledge of the environment, including which actor controls an action. Whether sorting belongs to a caller or a drawing function is an instance of that longstanding question. Jones (1981) likewise developed conditions for compatible environmental reliance and program guarantees in parallel programs. We do not claim these distinctions as our invention. [Kane](https://drive.google.com/file/d/1nbQUgK4kFkjKS4X9Op_q2e5H-Vgm8epM/view) · [Zave and Jackson](https://drive.google.com/file/d/1PwUeINSkW6vhhuUvYEh9YvGQFBWlWlav/view) · [Jones](https://drive.google.com/file/d/1c2vEnheOmaTgKti8eexRyks-vwkBdnv4/view)

Barr et al.'s (2015) survey of the test-oracle problem makes a related point about our executable fixture. Tests establish outputs for chosen inputs; they do not, without an independently grounded oracle, establish which outputs a real project has promised to preserve. Thus the demands and contracts in Section 5 are explicit assumptions rather than requirements recovered from a repository. [Barr et al.](https://drive.google.com/file/d/1GvLHYntPcmuPdjuFmKZdenmBHeAy0SxY/view)

**From a classification to a patch disposition.** Correctly naming a design-principle violation supports a judgment about a structural feature of code. Rejecting a specific patch requires different grounds: (i) the source and scope of the new request, (ii) the behavior the project committed to existing callers, and (iii) the call path through which the request and those obligations must hold. Some clues may reside in source, but observed behavior is not automatically an authorized compatibility promise. The same change in book output can be unacceptable under one declared contract and acceptable under another. Section 5 supplies a fixed-patch, four-specification witness to that gap. It does not disprove the benchmark's classification scores or establish that a real reviewer rejected a patch because of an OCP label.

### 5. When the same patch warrants different decisions

We built a small catalog based on Meyer’s example. The client in <code>client.py</code> displays each publication through the catalog function passed to it. The patch adds <code>reports.py</code> to wrap that function. The source of <code>catalog.py</code> and <code>client.py</code> stays identical. The resulting catalog displays technical reports and still rejects errata. For books it now prints <code>BOOK</code> where it used to print <code>book</code>.

Suppose the only new requirement is to handle technical reports. If callers were promised the original book output, the changed prefix is grounds for rejection. If the book output is outside the contract, the same patch can be accepted. Table 2 applies both contracts again when errata are also required. Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata. Excluding the book prefix from our stipulated contract is not evidence that real users have no expectation about it; it only means this example does not impose that obligation.

<b>Table 2. Two requirements for accepting a fixed patch.</b>

| Request | Book prefix protected | Meets the request | Preserves the contract | Decision |
| --- | --- | --- | --- | --- |
| Technical reports | No | Yes | Yes | Accept |
| Technical reports | Yes | Yes | No | Reject |
| Technical reports and errata | No | No | Yes | Reject |
| Technical reports and errata | Yes | No | No | Reject |

Learning that errata are required leaves the last two rows of Table 2. Both reject the patch, so the book contract need not be settled first. Learning that technical reports are the whole request leaves the first two rows. One accepts and one rejects. The next question is whether the original book output is protected.

The procedure applies only if the actual specification is among these four authored cases. If disclosure rules out every row, an empty candidate set is a reason to question the evidence or the candidate set, not to infer acceptance or rejection. If the remaining rows disagree, the same information admits no single binary verdict that is right in every case. The reviewer can give a conditional answer or defer judgment. Appendix A gives the nine ways of disclosing or withholding the two fields in this example.

**Minimum evidence for a decision.** Let $E$ indicate that errata support is required and $B$ that the previous book prefix is protected. Within the four stipulated specifications, the acceptance predicate is $A(E,B)=\neg E\land\neg B$. Its unique inclusion-minimal acceptance certificate is $\{\neg E,\neg B\}$; the two separate minimal rejection certificates are $\{E\}$ and $\{B\}$. With both facts withheld, an accepting specification $(E=0,B=0)$ and a rejecting specification $(E=1,B=0)$ remain compatible, so deferral has explicit countermodels. After confirming reports-only ($\neg E$), asking whether the book prefix is protected determines the verdict. With both fields initially unknown, neither one binary question guarantees a verdict for every possible answer.

These are classical finite Boolean and version-space facts, not new inference rules. A separate Python replay checked the four worlds, nine disclosure states, inclusion-minimal certificates, contradictory evidence, and pairs of opposite-verdict worlds for deferred states; its [read-only 30-test CI](https://github.com/WhoSia/EvoNOMOS/actions/runs/44911870723) passed. That verifies the bounded decision logic, not actual human decisions or complete source behavior. Learning more about a fixed contract removes possible worlds; *renegotiating that contract* changes the legitimate obligation. The two transitions must not be conflated.

We ran a second patch to see whether the stricter specification was feasible under the same edit boundary. It adds one module, handles technical reports and errata, and keeps the original book output. A rejection in Table 2 need not end the search for a patch within that boundary. The contribution is not a new logical rule: it is a concrete account of why knowing that errata are required settles this decision, whereas a reports-only demand leaves the book-output commitment to be checked. Applying it to a real review would require finding that commitment in a request, API documentation, tests or caller records.

[Reproduction of the four combinations](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md) · [Disclosure replay](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/34_MAINTENANCE_JUDGMENT_UNDER_PARTIAL_DISCLOSURE.md)

### 6. When the original call path is part of the requirement

Deciding whether to accept a completed patch differs from choosing an architecture for future edits. We retain one observation relevant to acceptance. In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected <code>bracketed=True</code>. A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.

The presence of a feature is different from <b>its availability along a required route</b>. Unless the original entry point and its compatibility obligations are identified, implementation through a separate function cannot by itself establish that the requested behavior is available to existing callers. The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in <mention url="https://app.notion.com/p/41bef561cf9281e1864afb74a3bbb4ce">Paper B 통합 원고 12 · 한·영 문장 교정</mention> and its [execution record](https://github.com/WhoSia/EvoNOMOS/commit/0ede7b241c8f9f50436be9703561bb9e7cc9fb8b).

### 7. Conclusion

Drawing a square first establishes what a routine does, not whether it must be edited. That depends on whether sorting belongs to the routine's obligations. In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required. We did not observe a real OCP label being misused to reject a patch. We asked <b>what additional grounds a design-principle assessment needs before it can justify an engineering decision</b>.

A practical review should first ask not only whether the patch implements a feature but where the request or an authorized agreement requires that feature to be reachable. The reviewer should then locate the source of each protected old-client obligation in requests, API documentation, tests and actual call paths, without automatically treating every observed response as a promise. If those sources leave different legitimate contracts possible, asking who can settle the obligation is more defensible than turning an OCP label into a categorical rejection. Conversely, a demonstrated failure to meet an already binding new demand may reject the fixed patch before every other old-client promise is resolved. This sequence is a recommendation derived from our authored example, not evidence that it reduces actual review costs in an organization.

Keeping the specifications compatible with known facts and checking their verdicts is elementary logic. The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository. Our evidence is confined to one benchmark archive and authored executable examples. We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.

### Appendix A · Reproduction

The audits in Sections 3–4 read the archived JSON and JSONL as data. A separate script reproduced sixteen JSONL files, 768 rows, 48 distinct submissions, 24 scaffolds and 64 fixed model–strategy–language groups, and counted Python comments in four of twelve unique submissions. See the [machine-readable independent replay](https://github.com/WhoSia/EvoNOMOS/commit/3accc623830b3444281d4ef5bcf9a7d78301668c). Section 5 and the call-path check in Section 6 use examples written for this study. The shape-layout experiment and Figure 1 remain preserved in manuscript 12; manuscript 18 does not reframe them as a new measured maintenance-cost trial. The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators. The table below gives the nine verdicts for Section 5.

[Reproduction notes](https://github.com/WhoSia/EvoNOMOS/commit/ed443890f0b5f9b171d68d010b605e7cefec7f14)

Both values of a withheld field remain possible. Defer means that the compatible rows include both acceptance and rejection.

| Disclosed request | Book prefix outside contract | Book prefix protected | Prefix contract withheld |
| --- | --- | --- | --- |
| Technical reports | Accept | Reject | Defer |
| Technical reports and errata | Reject | Reject | Reject |
| Request withheld | Defer | Reject | Defer |

## 검증한 주요 참고문헌 · References (working)

- Meyer, B. (1988). <i>Object-Oriented Software Construction</i> (1st ed.), pp. 22–25. [초판 대조 기록](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md).
- Martin, R. C. (1996). <i>The Open–Closed Principle</i>. [원문](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf).
- Jones, C. B. (1981). <i>Development Methods for Computer Programs Including a Notion of Interference</i>. Oxford University Computing Laboratory, PRG-25. [입수된 스캔](https://drive.google.com/file/d/1c2vEnheOmaTgKti8eexRyks-vwkBdnv4/view) · [Oxford 기관 판본](https://www.cs.ox.ac.uk/files/9025/PRG-25.pdf).
- Pehlivan, F., Ergüzen, A. Ü., Yengejeh, S. M., Lami, M., & Koyuncu, A. (2025). <i>Are We SOLID Yet? An Empirical Study on Prompting LLMs to Detect Design Principle Violations</i>. ASE 2025 NIER. [arXiv:2509.03093](https://arxiv.org/abs/2509.03093).
- Bräuer et al. (2018). <i>Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research</i>. [DOI](https://doi.org/10.1016/j.jss.2018.03.002).
- Cabral et al. (2024). <i>Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding</i>. [DOI](https://doi.org/10.1145/3644815.3644957).
- Zhu, H., Zhang, Q., Wang, J., Yang, Z., & Qiu, Y. (2026). <i>Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits</i>. [arXiv:2603.27745](https://arxiv.org/abs/2603.27745).
- Kane, M. T. (2013). <i>Validating the Interpretations and Uses of Test Scores</i>. <i>Journal of Educational Measurement</i>, 50(1), 1–73. [DOI](https://doi.org/10.1111/jedm.12000) · [원문](https://drive.google.com/file/d/1nbQUgK4kFkjKS4X9Op_q2e5H-Vgm8epM/view).
- Zave, P., & Jackson, M. (1997). <i>Four Dark Corners of Requirements Engineering</i>. <i>ACM Transactions on Software Engineering and Methodology</i>, 6(1), 1–30. [DOI](https://doi.org/10.1145/237432.237434) · [원문](https://drive.google.com/file/d/1PwUeINSkW6vhhuUvYEh9YvGQFBWlWlav/view).
- Barr, E. T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S. (2015). <i>The Oracle Problem in Software Testing: A Survey</i>. <i>IEEE Transactions on Software Engineering</i>. [DOI](https://doi.org/10.1109/TSE.2014.2372785) · [원문](https://drive.google.com/file/d/1GvLHYntPcmuPdjuFmKZdenmBHeAy0SxY/view).

- Widyasari, R., Zhang, T., Bouraffa, A., Maalej, W., & Lo, D. (2025). <i>Explaining Explanations: An Empirical Study of Explanations in Code Reviews</i>. <i>ACM Transactions on Software Engineering and Methodology</i>, 34(6), Article 177. [DOI](https://doi.org/10.1145/3708518) · [보유 PDF](https://drive.google.com/file/d/1POjBSQkxLKYmTXPzb4Z6wYBpjJgItIQA/view).
- Papotti, A., Paramitha, R., & Massacci, F. (2024). <i>On the acceptance by code reviewers of candidate security patches suggested by Automated Program Repair tools</i>. <i>Empirical Software Engineering</i>, 29, Article 132. [DOI](https://doi.org/10.1007/s10664-024-10506-z) · [보유 PDF](https://drive.google.com/file/d/1Fmrm1uQIOTgevCYo6rQrkqaiaANpEvE4/view).
- Jin, H., & Chen, H. (2026). <i>Are LLMs Reliable Code Reviewers? Systematic Overcorrection in Requirement Conformance Judgement</i>. [읽은 판본: arXiv 2603.00539v1](https://arxiv.org/abs/2603.00539) · [보유 PDF](https://drive.google.com/file/d/1fWCLu97RGa1TvRt0RxuziolpRSh8rLW4/view).
- Ling, M., Zou, J., & Liu, X. (2026). <i>Negotiating Completion in Agentic Software Work: Acceptance Boundaries and Deferred Requirements</i>. <i>Systems</i>, 14, 1312. [DOI](https://doi.org/10.3390/systems14101312) · [보유 PDF](https://drive.google.com/file/d/10IrIflqxO0BtWAOJ3cEutu3glU2CogwN/view).

이 목록은 인용된 주요 자료를 확인할 수 있게 모은 집필용 서지이며, 서지형식·인용 위치·전수 대조를 마친 제출용 참고문헌은 아직 아니다. / These are verified reading anchors, not yet a fully formatted submission bibliography.
