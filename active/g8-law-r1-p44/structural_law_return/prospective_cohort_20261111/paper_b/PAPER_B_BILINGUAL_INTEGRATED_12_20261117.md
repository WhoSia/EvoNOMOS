# Paper B — Bilingual Integrated Manuscript 12

Line edit of manuscript 11. 2026-11-17 KST. [Previous manuscript snapshot](https://github.com/WhoSia/EvoNOMOS/commit/5d99aa1b5212e581e8ef6600bb79b25dea97fa81).

통합 원고 12 · 한·영 문장 교정. 기준판은 [Paper B 통합 원고 11](https://app.notion.com/p/41bef561cf92811abb50f26b749e9ca5)이다.

**초록**

개방–폐쇄 원칙 위반이라는 판정은 언제 수정안을 거절할 근거가 되는가? SOLID 위반 분류 벤치마크에 저장된 프롬프트에서 제출 코드를 가리자 지시문 틀 24개가 남았다. 어느 틀에도 개별 변경 요구나 보호할 기존 동작이 따로 적혀 있지 않았다. 별도로 만든 도서관 프로그램에서는 같은 수정안을 실행하고, 그 결과에 적용할 요구와 계약을 바꿨다. 기존 책 출력을 보존해야 하거나 정오표를 지원해야 하면 수정안은 거절됐다. 이 사례에서 검토자는 공개된 사실과 양립하는 명세를 추려, 남은 명세가 모두 같은 결론을 가리킬 때 판정을 확정할 수 있었다.

**Abstract**

When does an open–closed principle violation justify rejecting a patch? Masking the submitted code in the saved prompts of a SOLID classification benchmark left 24 distinct templates. None separately stated what change an individual case required or what existing behavior it protected. In a separate catalog program, we ran one patch and varied the requirements and contract against which we judged its behavior. The patch failed when either the original book output had to be preserved or errata had to be supported. In this example, a reviewer could settle the verdict by retaining the specifications consistent with the disclosed facts and checking whether they all gave the same answer.

## 한국어 원고

### 1. 서론

로버트 마틴이 1996년에 예로 든 함수는 목록에 들어온 순서대로 도형을 그린다. 삼각형이 자신을 그리는 메서드를 갖고 있으면 이 함수에 손대지 않고 삼각형을 추가할 수 있다. 마틴은 여기에 새 요구를 붙였다. 모든 원을 사각형보다 먼저 그려야 한다. 기존 함수에 사각형으로 시작하는 목록을 넘기면 여전히 사각형부터 그린다.

원을 먼저 놓는 일은 누가 맡았을까? 호출자가 원을 앞에 모아 넘기기로 했다면 함수는 제 일을 한다. 함수가 어떤 목록을 받아도 그 순서를 보장하기로 했다면 고쳐야 한다. 소스에서 그리는 순서를 읽을 수는 있지만, 그 순서가 잘못됐는지는 누가 정렬을 맡았는지에 달려 있다.

마틴의 그리기 함수는 도형을 하나 더 추가할 때는 그대로 둘 수 있었다. 함수에 정렬까지 맡기면 얘기가 달라진다. 개방–폐쇄 원칙(OCP)을 들어 수정안을 거절하려면, 먼저 어떤 변경을 처리하고 어떤 동작을 계속 제공해야 하는지 밝혀야 한다.

분류 벤치마크의 저장 자료에서 모델에 어떤 지시가 주어졌는지 확인했다. 이어 도서관 예제에서 코드와 수정안을 고정한 채 새 요구와 기존 호출자에게 한 약속을 바꿨다. 도형 예제로 돌아가서는 별도 파일에 넣은 기능을 기존 함수로도 쓸 수 있는지 확인했다.

[Martin 1996, Listing 2와 Strategic Closure](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=6) · [벤치마크 기록 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [동일 패치 비교](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md)

### 2. 마이어와 마틴의 개방–폐쇄 원칙

마틴은 1996년 글에서 베르트랑 마이어의 1988년 초판 23쪽을 인용했다. 마이어에게 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 쓸 수 있는 모듈이다. 그의 도서관 예제에서 자료 유형을 하나씩 구별해 처리하는 프로그램에 기술보고서를 추가하면, 기존 모듈까지 고치거나 다시 컴파일해야 할 수 있다. 새 자료를 처리하는 코드의 위치에 따라 기존 모듈에 손이 가는 범위가 달라진다.

1995년 6월 공개 토론에서 카일 브라운은 잘못 설계된 클래스라면 소스를 고칠 수 있어야 한다고 했다. 마틴은 예상한 확장을 위해 기존 소스를 반드시 고쳐야 하는지를 물었다. 그러려면 어떤 변경이 생길지 미리 짚어야 한다. 2007년 공개 기록에는 다섯 원칙을 묶은 SOLID라는 이름이 나온다. 2009년 인터페이스 논쟁에서는 내부 클래스와 공개 플러그인 API에 서로 다른 조언이 제시됐다. 이 기록에서 확인할 수 있는 것은 당시 어떤 이유로 원칙을 적용했는지다. [1995년 토론](https://groups.google.com/g/comp.lang.c%2B%2B/c/nntTK8eH_Ag/m/uvoJEnDH9zAJ) · [2007년 자료](https://www.infoq.com/news/2007/01/principles-of-agile-design/) · [2009년 논쟁 기록](https://www.joelonsoftware.com/2009/01/31/from-podcast-38/)

마틴은 목록 정렬을 `DrawAllShapes`가 맡게 했다. 한 구현에서 `Circle::Precedes`는 상대 도형이 사각형이면 원을 먼저 놓는다. 원과 세 번째 도형의 순서를 정하려면 `Circle`도 고쳐야 할 수 있다. 반면 도형 종류별 순서를 표에 두면 사각형을 먼저 놓기 위해 표의 두 항목만 바꾸면 된다. 개별 도형을 넓이순으로 그리려면 그 표에 없는 정보가 필요하다.

마틴이 글 후반에 비교한 두 함수는 `dynamic_cast`를 쓴다. `DrawAllShapes`의 한 구현은 원과 사각형을 골라 그리고, `DrawSquaresOnly`는 사각형만 그린다. 둘 다 삼각형을 건너뛴다. 모든 도형을 그려야 할 때는 출력이 하나 빠진 셈이다. 사각형만 그려야 한다면 결과가 맞다. 코드와 프롬프트만 주어진 검토자는 각 함수에 어느 책임이 있는지 어디까지 알 수 있을까?

[Meyer 1988 초판 22–25쪽 대조 기록](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md) · [Martin 1996, 1쪽](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=1) · [Martin 1996, Listings 3–6, 9–10](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf)

### 3. 자료와 방법

벤치마크에서는 모델에 주어진 지시를 확인했다. 도서관 예제에서는 요구와 계약 가운데 일부만 알려졌을 때도 같은 수정안에 한 가지 결론을 내릴 수 있는지 확인했다.

OCP 참조 쌍 48개에는 각각 위반 예시와 그 수정본이 들어 있다. 저장 응답은 16개 파일에 48행씩, 총 768행이다. 각 행에는 제출 코드, 프롬프트, 기록된 모델 응답이 있다. 같은 프로그램이 여러 행에 걸쳐 나올 수 있다. 프롬프트마다 제출 코드가 한 번만 나오는지 확인하고 그 자리를 공통 표시로 바꿨다. 남은 문자열이 완전히 같으면 한 종류의 지시문 틀로 셌다.

틀의 문구를 직접 읽어 요구와 계약이 따로 적혀 있는지 확인했다. “삼각형도 그려야 한다”처럼 해당 사례의 새 동작을 요구하면 변경 요구로, “기존 너비 조회는 계속 지원해야 한다”처럼 유지할 동작을 밝히면 호출자 계약으로 보았다. 반복 분기에 다형성을 적용할 수 있는지 묻는 문구는 일반적인 판별 단서다. 이 검토는 코드를 가리고 남은 지시문을 대상으로 했다. 제출 코드나 아카이브의 다른 문서에는 추가 단서가 있을 수 있다.

저장 행의 제출 코드를 모든 OCP 참조 쌍의 수정 전후 소스와 대조했다. 원문 그대로 비교한 뒤 양끝 공백만 없애고 다시 비교했다. Python 참조 쌍에서는 구문 트리에서 최상위 클래스가 직접 선언한 메서드 이름을 비교했다. 밑줄로 시작하는 이름은 셈에서 뺐다. 이 검사로 선언이 빠졌는지는 알 수 있다. 상속을 통해 계속 호출할 수 있는지, 누군가 실제로 호출했는지, 그 호출을 계속 지원하기로 했는지는 각각 별도의 근거가 필요하다.

도서관 예제에서는 원래 소스, 수정안, 호출 입력과 편집 범위를 고정했다. 기존 클라이언트로 호출해 출력 문자열 또는 예외 유형과 메시지를 기록했다. 새 요구를 충족하고 기존 계약도 지킨 경우를 승인으로 셌다. 일부 정보만 주어진 경우에는 판정표에서 그 정보와 맞는 행만 남겼다. 그 행들이 모두 같은 결론을 가리키는지 확인했다. 벤치마크는 ZIP에 든 JSON과 JSONL을 읽어 감사했고, 도서관과 도형 예제는 직접 작성해 실행했다. 부록 A에 입력과 재현 명령을 두었다.

[감사 코드](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/audit_are_we_solid.py) · [고정 인벤토리](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/are_we_solid_inventory.json)

### 4. 벤치마크가 판정에 제공한 정보

Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다. 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다. 모델의 분류 결과는 그 참조 라벨과 대조했다. OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다. DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다. 전략 간에 동일한 틀은 없었다. 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.

Python `EXAMPLE`의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다. 제출된 `AreaCalculator`는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다. 새 도형을 지원한다면 이 분기가 수정 후보가 된다. 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.

별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 `Rectangle.get_width` 선언을 뺐다. 저장된 제출 코드 가운데 어느 참조 쌍의 수정 전후 소스와도 일치한 것은 없었다. 양끝 공백을 걷어 내도 결과는 같았다. 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다. 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.

**표 1. 저장된 입력과 수정안 판정에 필요한 근거.**

| 검토할 질문 | 자료에서 확인한 내용 | 수정안 판정에 필요한 근거 |
| --- | --- | --- |
| 어떤 정답을 맞히는가 | 원저는 저자들이 검증한 참조 위반 범주에 모델 응답이 얼마나 일치하는지 평가했다. [원저 §III-A, C–D](https://arxiv.org/html/2509.03093v1#S3) | 구체적인 수정안과 승인 기준 |
| 어떤 기능을 추가해야 하는가 | 저장 Python EXAMPLE은 다형성으로 처리할 만한 반복 분기를 찾도록 했다. 개별 변경 요구는 템플릿에 별도로 적혀 있지 않았다. [대조 코드와 저장 행 위치](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53) | 실제 요청, 수용 조건, 변경을 맡을 경계 |
| 어떤 호출을 계속 지원해야 하는가 | 저장 템플릿에는 보호할 호출자 계약이 따로 없었다. 별도의 37번 참조 쌍에서는 너비 getter 선언이 빠졌다. [참조 쌍 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) | 계약의 범위와 근거가 되는 API 문서, 호출 코드, 테스트 또는 합의 |
| 구현에서 어떤 경계를 바꿀 수 있는가 | 저장 지시는 위반 범주와 설명을 요구한다. 업무상의 파일·인터페이스 보호 범위는 그 지시문에서 확인되지 않는다. [원저 §III-B 및 저장 행](https://arxiv.org/html/2509.03093v1#S3) | 보호할 산출물, 허용된 수정 또는 새 모듈 추가와 같은 경로 |

프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다. 참조 쌍 37번은 별도 참조 JSON에 있다. [저장 아카이브](https://drive.google.com/file/d/12LDcKFBpJRkwH-zYJZ6Uhk9pE3RzgnUe/view) · [정확 일치 및 양끝 공백 제거 대조](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

[Pehlivan 등 §III](https://arxiv.org/html/2509.03093v1#S3) · [아카이브와 참조 쌍 37 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [저장 입력과 참조본 대조 코드](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

Bräuer 등(2018)은 측정 가능한 실천 규칙으로 설계 원칙의 어떤 부분을 포착할 수 있는지 전문가에게 물었다. Cabral 등(2024)은 기계학습 기능을 확장하는 상황에서 SOLID를 적용한 코드에 대해 참가자가 느낀 이해도와 확장 용이성을 조사했다. Zhu 등(2026)은 저장소에 구체적인 변경을 요구하고 기능 테스트와 구조 판정 기준을 적용했다. 다음 절에서는 수정안을 고정하고, 검토자가 알고 있는 요구와 계약에 따라 승인 결론이 달라지는지 살핀다. [Bräuer DOI](https://doi.org/10.1016/j.jss.2018.03.002) · [Cabral DOI](https://doi.org/10.1145/3644815.3644957) · [Zhu arXiv](https://arxiv.org/abs/2603.27745)

### 5. 같은 수정안의 판정이 달라질 때

마이어의 도서관 예제를 작은 프로그램으로 만들었다. `client.py`는 전달받은 목록 함수로 자료를 출력한다. 수정안은 그 함수에 새 처리를 덧붙이는 `reports.py`를 추가한다. `catalog.py`와 `client.py`의 소스는 그대로다. 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다. 기존 책 출력에서는 접두어가 `book`에서 `BOOK`으로 바뀐다.

기술보고서만 지원하면 되는 경우를 보자. 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다. 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다. 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다. 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.

**표 2. 같은 수정안에 적용한 요구와 계약.**

| 요구 | 기존 책 접두어 보호 | 새 요구 만족 | 기존 계약 보존 | 이 사례의 승인 기준 |
| --- | --- | --- | --- | --- |
| 기술보고서 | 아니오 | 예 | 예 | 승인 |
| 기술보고서 | 예 | 예 | 아니오 | 거절 |
| 기술보고서와 정오표 | 아니오 | 아니오 | 예 | 거절 |
| 기술보고서와 정오표 | 예 | 아니오 | 아니오 | 거절 |

“정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다. 둘 다 거절이다. 책 계약까지 확인할 필요는 없다. “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다. 하나는 승인, 하나는 거절이다. 이때 확인할 것은 기존 책 출력이 보호 대상인지다.

실제 명세가 검토하는 경우들 가운데 하나라는 전제에서 이 절차가 성립한다. 공개된 사실과 맞는 행이 없다면 명세 후보와 공개된 사실부터 다시 대조해야 한다. 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다. 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다. 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.

같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다. 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다. 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다. 다른 사례에서도 가능한 명세와 각각의 근거를 명시하면, 보류된 판정을 확정하기 위해 다음에 무엇을 확인할지 알 수 있다.

[네 조합의 재현](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md) · [정보 공개 조건별 결과](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/34_MAINTENANCE_JUDGMENT_UNDER_PARTIAL_DISCLOSURE.md)

### 6. 변경을 놓을 자리와 호출 경로

새 기능을 별도 파일에 넣을 수 있다면 기존 파일을 그대로 둘 수 있을까? 도형 예제로 돌아가 연산별로 파일을 나눈 구현과 도형별로 나눈 구현을 비교했다. 실행해 본 후보마다 수정한 기존 파일의 수를 셌다.

삼각형을 추가하려면 도형별 구현에서는 새 파일 하나면 됐고, 연산별 구현에서는 기존 그리기 파일을 고쳐야 했다. 이름표 연산을 추가할 때는 반대였다. 원과 사각형 파일을 각각 고쳐야 했던 도형별 구현과 달리, 연산별 구현은 새 파일에 연산을 둘 수 있었다. 네 수정안 모두 기능 검사를 통과했다(그림 1A).

이 차이가 같은 요구에서도 나타나는지 보려고 두 구현에 `render_many`를 추가했다. 도형 목록을 받아 각 출력에 대괄호를 붙이는 함수다. 변환을 각 도형에 맡기면 도형별 구현의 원과 사각형 파일을 고쳐야 한다고 예상했다. 공용 어댑터를 허용하면 두 구현에서 기존 파일을 그대로 둘 수 있을 것으로 봤다. 실제로 원과 사각형 파일을 고친 후보는 변환을 각 도형에 맡긴 경우뿐이었다. 네 후보 모두 새 파일 하나를 추가했다. 네 후보에서 입력 순서와 중복, 기존 원·사각형 렌더링은 유지됐고 빈 목록과 미지원 도형은 명세대로 처리됐다(그림 1B).

**그림 1. 수정한 기존 소스 파일 수.** A는 삼각형 추가와 이름표 연산 추가를 비교한다. B는 같은 배치 렌더링 요구에서 파일 배치 규칙을 바꾼 결과다. B의 네 후보는 모두 새 기능과 기존 동작 검사를 통과했고 새 파일을 하나씩 추가했다.

[PNG](https://drive.google.com/file/d/1uD_IpP77WJsKIWBngn72WEO9vp5JqzO1/view) · [SVG](https://drive.google.com/file/d/1swHCwTW3MNDv1mYE5-mCfsq73Iz1mnfZ/view) · [Batch prediction / 사전 예측](https://github.com/WhoSia/EvoNOMOS/commit/54d5af3f7ddcd4e74866b4b7f1b4ce188ed5aa7e) · [Batch fixture / 실행](https://github.com/WhoSia/EvoNOMOS/commit/d1ae74941da0539a8b8b8b330b9e6deb0e3aa83c) · [Figure source / 도판 코드](https://github.com/WhoSia/EvoNOMOS/commit/87f30604b8eca674030afa03a4798f277dfcc846)

다음 비교에서는 렌더링 결과 하나를 요청에 따라 대괄호로 감싸는 기능을 넣었다. 두 구현 모두 새 함수로 이 기능을 제공했다. 같은 어댑터를 추가한 상태에서 기존 함수에 `bracketed=True`를 넘기면 오류가 났다. 기존 함수에서 옵션을 받도록 하려면 연산별 후보는 기존 파일 하나, 도형별 후보는 두 개를 고쳤다. 기존 함수가 외부 변환 모듈을 불러오는 별도 기준선에서는 두 후보 모두 새 파일 하나로 옵션을 연결했다(표 3).

**표 3. 새 렌더링 옵션이 제공되는 호출 경로.**

| 새 기능을 받는 경로 | 연산별 배치 기존 파일 수정 | 도형별 배치 기존 파일 수정 | 각 배치의 새 파일 |
| --- | --- | --- | --- |
| 새 진입점 | 0 | 0 | 1 |
| 기존 진입점 | 1 | 2 | 0 |
| 확장 지점이 있는 기존 진입점 | 0 | 0 | 1 |

표 3의 마지막 행은 확장 지점을 마련한 다음부터 센 것이다. 이 비교에서 센 것은 기존 파일 수정 수다. 확장 지점을 처음 만드는 비용이나 실제 유지보수 작업량은 각각 따로 측정해야 한다.

[Prediction / 예측](https://github.com/WhoSia/EvoNOMOS/commit/76fa9222a7149b7c98a6315375834f2bd909fe0e) · [Execution / 실행](https://github.com/WhoSia/EvoNOMOS/commit/0ede7b241c8f9f50436be9703561bb9e7cc9fb8b)

### 7. 결론

사각형을 먼저 그린 함수에 수정을 요구하려면, 원을 먼저 놓는 일이 그 함수의 책임이라는 근거가 필요했다. 도서관 예제에서도 판정을 가른 것은 어떤 동작이 요구되고 보호되는가였다. 정오표가 필수라면 그 사실만으로 수정안을 거절할 수 있었다. 기술보고서만 필요하다면 기존 책 출력을 보호하기로 했는지에 따라 결론이 달라졌다.

같은 수정안을 검토하다 결론이 갈리면, 현재 알려진 사실과 맞는 명세를 남기고 어느 차이가 판정을 바꾸는지 확인할 수 있다. 이 글에서는 한 벤치마크의 저장 자료와 직접 작성한 예제로 그 방법을 보였다. 실제 저장소에서 어떤 문서나 테스트를 근거로 계약을 확정할 수 있는지, 검증하려는 기능이 어느 호출 경로에서 동작해야 하는지는 사례마다 추가 근거가 필요하다.

### 부록 A · 재현 자료

§3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다. §5–§6은 이 연구에서 만든 예제를 실행한다. 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다. 아래 표는 §5의 아홉 판정이다. 그림 1의 소스와 출력은 캡션 아래에 연결했다.

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

Martin’s drawing routine could stay as it was when the task was to add a shape. Making it responsible for sorting changes that judgment. A reviewer invoking the open–closed principle (OCP) to reject a patch needs to say what change the program must accommodate and what behavior it must preserve.

We inspect a classification benchmark’s archive to see what instructions its models received. In a separate catalog example we keep the code and patch fixed while varying the request and the promises to existing callers. We then return to drawing to test whether a feature added in a separate file can be reached through the original function.

[Martin 1996, Listing 2 and Strategic Closure](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=6) · [Benchmark archive audit](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [Fixed-patch comparison](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md)

### 2. The open–closed principle in Meyer and Martin

Martin attributed the principle to Bertrand Meyer, citing page 23 of the 1988 first edition. For Meyer, a closed module has a stable specification that other modules can rely on. His library example gives this a practical meaning. If a catalog handles publication types one by one, adding technical reports can require editing or recompiling existing modules. Where the new code goes affects how much of the existing system must change.

In a June 1995 public exchange, Kyle Brown argued that developers had to be able to fix a badly designed class. Martin asked whether an anticipated extension had to require an edit to existing source. That answer still depends on which changes can be anticipated. The public record uses SOLID for the five principles by 2007. A 2009 discussion gave different advice for internal classes and public plugin APIs. These records show why particular participants applied the principle as they did. [Contemporary exchange](https://groups.google.com/g/comp.lang.c%2B%2B/c/nntTK8eH_Ag/m/uvoJEnDH9zAJ) · [2007 report](https://www.infoq.com/news/2007/01/principles-of-agile-design/) · [2009 exchange](https://www.joelonsoftware.com/2009/01/31/from-podcast-38/)

Martin made `DrawAllShapes` responsible for sorting. In one implementation `Circle::Precedes` checks the other shape and puts a circle before a square. Deciding where a third shape belongs relative to a circle can require an edit to `Circle`. Placing the order of types in a table lets squares go first with a swap of two entries. Sorting individual shapes by area would require information that the table does not hold.

Later in the article Martin compares two uses of `dynamic_cast`. One version of `DrawAllShapes` draws circles and squares, and `DrawSquaresOnly` draws squares alone. Both skip a triangle. A triangle left undrawn is a missed output when the task is to draw all shapes. When the task is to draw squares, skipping it is correct. How much of that responsibility can a reviewer determine from code and a prompt?

[Meyer 1988, first edition, pp. 22–25](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md) · [Martin 1996, p. 1](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=1) · [Martin 1996, Listings 3–6, 9–10](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf)

### 3. Materials and methods

In the benchmark we examine the instructions given to the models. In the catalog example we test whether a single verdict follows when only part of the request or contract is disclosed.

The archive contains 48 OCP reference pairs, each with a violation example and its revision. The saved responses occupy 16 files of 48 records each, for a total of 768 records. Each record has submitted code, a prompt and a recorded model response. A program can appear in more than one record. We checked that the submitted code occurred once per prompt, then replaced it with a common placeholder. We counted templates by exact equality of the remaining strings.

We read the templates for separately stated requirements and contracts. An instruction such as asking for triangles to be drawn specifies a change in that case. Asking that an existing width query remain available states a caller contract. A direction to look for repeated branches where polymorphism might fit gives a general classification cue. We applied this reading to the instructions after masking the code. The submitted code and other archive material can supply further context.

We compared each saved submission with both sides of every OCP reference pair, first as stored and then after stripping leading and trailing whitespace. For the Python pairs we used syntax trees to compare the method names declared directly by top-level classes, omitting names that begin with an underscore. That comparison can show that a declaration disappeared. Establishing whether callers could still reach it through inheritance, used it in practice, or had been promised continued access requires separate evidence.

In the catalog we fixed the initial source, patch, caller inputs and edit boundary, which permitted adding a module. Through the existing client we recorded the output string or the exception type and message. We counted a patch as acceptable when it met the new requirement and preserved the applicable contract. For partial disclosure we retained the rows consistent with the disclosed facts and checked whether they agreed. For the archive audit we read the JSON and JSONL in the ZIP. For the catalog and drawing checks we ran examples written for this study. Appendix A gives the inputs and commands.

[Audit script](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/audit_are_we_solid.py) · [Pinned inventory](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/are_we_solid_inventory.json)

### 4. What the benchmark gives the reviewer

Pehlivan et al. chose violation scenarios and refined the generated examples. A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion. The benchmark compares model classifications with the resulting labels. After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL. No two strategies shared a template string. None of the templates separately stated the requested change or protected caller contract for an individual case.

One Python `EXAMPLE` prompt directs the reviewer to repeated branches where polymorphism might fit. The submitted `AreaCalculator` branches on shape type to calculate the area of a circle or rectangle. If a new shape is needed, that branch is a place to look. The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.

The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of `Rectangle.get_width`. None of the code saved as model submissions matched either side of any reference pair. Trimming outer whitespace yielded the same result. Pair 37 establishes that a declaration was removed. Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.

**Table 1. Evidence in the saved material and evidence needed to assess a patch.**

| Question | Evidence in the saved material | Evidence for a patch decision |
| --- | --- | --- |
| What counts as a correct answer? | The benchmark compares model responses with the violation labels verified by its authors. | The proposed edit and the criteria for acceptance. |
| Which behavior should be added? | The saved Python EXAMPLE prompt points to repeated branching where polymorphism would fit. The templates state no separate request for an individual case. | The actual request, its acceptance conditions, and the boundary responsible for it. |
| What do existing callers rely on? | The templates state no separate caller contract. The distinct reference pair 37 loses the width getter declaration. | The scope of the commitment and supporting API documentation, client code, tests, or agreement. |
| What may the implementation change? | The instructions ask for a violation category and an explanation. They do not specify protected implementation files or interfaces. | The protected artifacts and permitted changes, including whether a new module may be added. |

The prompt example is in JSONL line 13 (record ID 12). Pair 37 is in a separate reference JSON file. [Archived material](https://drive.google.com/file/d/12LDcKFBpJRkwH-zYJZ6Uhk9pE3RzgnUe/view) · [Source comparison](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

[Pehlivan et al., §III](https://arxiv.org/html/2509.03093v1#S3) · [Archive audit and reference pair 37](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [Submitted and reference source comparison](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

Bräuer et al. (2018) asked experts which parts of a design principle were captured by measurable practices. Cabral et al. (2024) asked participants how easy they found it to understand and extend code under a bundled SOLID treatment in a machine-learning scenario. Zhu et al. (2026) set repository change tasks and used functional and structural checks. In the next section we fix the patch and ask whether knowing a different requirement or caller contract changes the verdict. [Bräuer DOI](https://doi.org/10.1016/j.jss.2018.03.002) · [Cabral DOI](https://doi.org/10.1145/3644815.3644957) · [Zhu arXiv](https://arxiv.org/abs/2603.27745)

### 5. When the same patch warrants different decisions

We built a small catalog based on Meyer’s example. The client in `client.py` displays each publication through the catalog function passed to it. The patch adds `reports.py` to wrap that function. The source of `catalog.py` and `client.py` stays identical. The resulting catalog displays technical reports and still rejects errata. For books it now prints `BOOK` where it used to print `book`.

Suppose the only new requirement is to handle technical reports. If callers were promised the original book output, the changed prefix is grounds for rejection. If the book output is outside the contract, the same patch can be accepted. Table 2 applies both contracts again when errata are also required. Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.

**Table 2. Two requirements for accepting a fixed patch.**

| Request | Book prefix protected | Meets the request | Preserves the contract | Decision |
| --- | --- | --- | --- | --- |
| Technical reports | No | Yes | Yes | Accept |
| Technical reports | Yes | Yes | No | Reject |
| Technical reports and errata | No | No | Yes | Reject |
| Technical reports and errata | Yes | No | No | Reject |

Learning that errata are required leaves the last two rows of Table 2. Both reject the patch, so the book contract need not be settled first. Learning that technical reports are the whole request leaves the first two rows. One accepts and one rejects. The next question is whether the original book output is protected.

This procedure assumes that the actual specification is among the cases under consideration. If no row fits what was disclosed, the reviewer needs to recheck the candidate specifications against the facts. If the remaining rows disagree, the same information admits no single binary verdict that is right in every case. The reviewer can give a conditional answer or defer judgment. Appendix A gives the nine ways of disclosing or withholding the two fields in this example.

We ran a second patch to see whether the stricter specification was feasible under the same edit boundary. It adds one module, handles technical reports and errata, and keeps the original book output. A rejection in Table 2 need not end the search for a patch within that boundary. In another case, recording the possible specifications and the evidence for each can tell a reviewer what to check next.

[Reproduction of the four combinations](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md) · [Disclosure replay](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/34_MAINTENANCE_JUDGMENT_UNDER_PARTIAL_DISCLOSURE.md)

### 6. Where a change can live and how callers reach it

If a feature can go in a separate file, can the existing files stay as they are? We return to drawing and compare two layouts, one organized by operation and one by shape. We count the existing files actually edited by the candidates we ran.

Adding a triangle took one new file in the shape layout and an edit to the drawing file in the operation layout. For a labeling operation, the shape layout needed edits to both the circle and square files. The operation layout could add the labels in one new file. All four candidates passed the functional checks (Figure 1A).

We then gave both layouts the same task. The new `render_many` takes a list of shapes and brackets each result. We expected both shape files to change when each shape owned its transformation. Allowing a shared adapter, we expected both layouts to leave existing files alone. The only candidate to edit existing files was the one that assigned the transformation to each shape. It edited the circle and square files. All four added one file, preserved input order and duplicates, handled empty lists and unsupported shapes as specified, and kept the original circle and square renderings (Figure 1B).

**Figure 1. Number of existing source files edited.** Panel A compares adding a triangle with adding a labeling operation. Panel B changes the placement rule for the same batch-rendering request. All four candidates in B passed the new and legacy checks and added one file each.

[PNG](https://drive.google.com/file/d/1uD_IpP77WJsKIWBngn72WEO9vp5JqzO1/view) · [SVG](https://drive.google.com/file/d/1swHCwTW3MNDv1mYE5-mCfsq73Iz1mnfZ/view) · [Batch prediction](https://github.com/WhoSia/EvoNOMOS/commit/54d5af3f7ddcd4e74866b4b7f1b4ce188ed5aa7e) · [Batch fixture](https://github.com/WhoSia/EvoNOMOS/commit/d1ae74941da0539a8b8b8b330b9e6deb0e3aa83c) · [Figure source](https://github.com/WhoSia/EvoNOMOS/commit/87f30604b8eca674030afa03a4798f277dfcc846)

Next we added an option to bracket a single rendered result. Both layouts could offer it through a new function. With that same adapter installed, the original function still rejected `bracketed=True`. Of the candidates offering the option through the original function, the operation layout edited one existing file and the shape layout edited two. In a separate baseline the original function could already load an external decorator. There, each layout connected the option to the original function by adding one file (Table 3).

**Table 3. Call paths for the new rendering option.**

| Path that provides the feature | Existing files edited, operation layout | Existing files edited, shape layout | New files per layout |
| --- | --- | --- | --- |
| New entry point | 0 | 0 | 1 |
| Original entry point | 1 | 2 | 0 |
| Original entry point with a hook | 0 | 0 | 1 |

The final row of Table 3 starts after the hook is in place. The numbers count edited existing files. Introducing the hook and measuring actual maintenance effort would require separate measurements.

[Prediction](https://github.com/WhoSia/EvoNOMOS/commit/76fa9222a7149b7c98a6315375834f2bd909fe0e) · [Execution](https://github.com/WhoSia/EvoNOMOS/commit/0ede7b241c8f9f50436be9703561bb9e7cc9fb8b)

### 7. Conclusion

A square drawn first gives the reviewer grounds for an edit when putting circles first is the drawing function’s job. In the catalog, we could change what the patch was required to do and preserve while keeping its behavior fixed. A requirement to handle errata settled the verdict. With technical reports as the only new requirement, the verdict depended on the promise about book output.

When the known facts leave more than one verdict open, they can retain the specifications consistent with the known facts and identify which difference changes the verdict. We demonstrate this method with records from one benchmark and examples written for the study. In a repository, the evidence that establishes a promise and the call path on which to test it must be found case by case.

### Appendix A · Reproduction

The audit in Sections 3–4 reads JSON and JSONL from the archived ZIP. Sections 5–6 run examples written for this study. The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators. The table below gives the nine verdicts for Section 5.

[Reproduction notes](https://github.com/WhoSia/EvoNOMOS/commit/ed443890f0b5f9b171d68d010b605e7cefec7f14)

Both values of a withheld field remain possible. Defer means that the compatible rows include both acceptance and rejection.

| Disclosed request | Book prefix outside contract | Book prefix protected | Prefix contract withheld |
| --- | --- | --- | --- |
| Technical reports | Accept | Reject | Defer |
| Technical reports and errata | Reject | Reject | Reject |
| Request withheld | Defer | Reject | Defer |
