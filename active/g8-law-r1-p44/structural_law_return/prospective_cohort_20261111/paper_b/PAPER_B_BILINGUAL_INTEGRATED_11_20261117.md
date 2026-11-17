# Paper B — Bilingual Integrated Manuscript 11

Materials, methods, and fixed-patch judgment. 2026-11-17 KST. [Previous manuscript snapshot](https://github.com/WhoSia/EvoNOMOS/commit/73669767d1c154f8e03563451a0b6c0ae991399b).

통합 원고 11 · 자료와 방법, 동일 수정안 판정. 기준판은 [Paper B 통합 원고 10 · 논증 흐름과 한·영 교정](https://app.notion.com/p/41bef561cf9281e9ac99ca92b78ce6aa)이다.

**초록 작업안 (한국어)**

개방–폐쇄 원칙 위반이라는 판정은 언제 구체적인 수정안을 거절할 근거가 되는가? 이 질문을 검토하기 위해 먼저 SOLID 위반 분류 벤치마크의 OCP 저장 자료에서 모델이 받은 지시를 살폈다. 제출 코드를 가린 결과 서로 다른 지시문 틀 24개가 남았다. 어느 틀에도 개별 변경 요구나 보호할 기존 동작이 따로 적혀 있지 않았다. 이어 도서관 예제의 소스와 수정안을 고정한 채, 그 수정안에 적용할 요구와 계약을 바꿨다. 기존 책의 접두어가 바뀐 수정안은 그 출력을 보호해야 할 때 거절됐다. 정오표 지원이 필수라는 사실 역시 거절에 충분했다. 이 비교를 바탕으로 공개된 정보와 양립하는 명세를 남기고, 그 명세에서 모두 같은 결론이 나올 때 판정을 확정하는 방법을 제시한다.

**Working abstract (English)**

When can an open–closed principle violation finding justify rejecting a particular patch? We first inspect the instructions in the saved OCP records of a SOLID classification benchmark. Masking the submitted code leaves 24 distinct instruction templates. None separately states the requested change for an individual case or a legacy behavior that the case protects. We then fix the source and patch of an executable catalog while varying the applicable requirement and caller contract. A patch that changes the book prefix is rejected when that output is protected. A requirement to render errata also suffices to reject the patch. The comparison gives us a procedure for reasoning from partial information: retain the specifications compatible with what is disclosed and settle the verdict when every remaining specification yields the same answer.

## 한국어 원고

### 1. 서론

로버트 마틴이 1996년에 예로 든 함수는 목록에 들어온 순서대로 도형을 그린다. 삼각형에 자기 자신을 그리는 동작이 있으면 이 함수에 손대지 않고도 삼각형을 추가할 수 있다. 마틴은 여기에 새 요구를 붙였다. 원은 사각형보다 먼저 그려야 한다. 목록의 맨 앞에 사각형이 있으면 함수는 여전히 그 사각형부터 그린다.

원을 먼저 그리는 일은 누가 맡았을까? 호출자가 원을 앞에 놓아 목록을 넘기기로 했다면 함수는 제 일을 한다. 어떤 목록을 받더라도 함수가 순서를 보장하기로 했다면 수정이 필요하다. 코드를 읽으면 무엇이 먼저 그려지는지 알 수 있다. 그 결과가 잘못됐는지를 판단하려면 호출자와 함수 사이에 어떤 약속이 있었는지도 알아야 한다.

도형 하나를 더 추가할 때 닫혀 있던 설계도 함수가 직접 정렬을 책임지는 순간 같은 방식으로 확장할 수 없었다. 개방–폐쇄 원칙(OCP)을 근거로 어떤 수정안에 ‘위반’이라고 표시할 때도, 그 판단을 받은 개발자는 프로그램이 어떤 변화에 대비해야 했고 어떤 동작을 계속 보장해야 했는지 물을 수 있다. 이 전제가 정해지기 전에 판정부터 확정하는 위험을 이 글에서는 설계 조언의 ‘과도한 공리화’라고 부른다.

분류 벤치마크에는 모델이 무엇을 보고 위반 여부를 답했는지 기록이 남아 있다. 그 기록을 읽어 분류에 주어진 근거를 확인한다. 수정안을 받아들일 근거는 별도로 시험한다. 코드가 같은데도 새 요구와 기존 호출자에 대한 약속에 따라 결론이 달라지는지 살핀다. 그 뒤 도형 예제로 돌아가 새 기능을 별도 파일에 넣었을 때 기존 호출자가 사용하던 함수로도 그 기능을 쓸 수 있는지 확인한다.

[Martin 1996, Listing 2와 Strategic Closure](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=6) · [벤치마크 기록 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [동일 패치 비교](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md)

### 2. 마이어와 마틴의 개방–폐쇄 원칙

마틴은 1996년 글에서 베르트랑 마이어의 1988년 초판 23쪽을 인용하며 원칙의 출처를 밝혔다. 마이어가 말한 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 사용할 수 있는 모듈이다. 마이어는 자료의 종류를 하나씩 구별해 처리하는 도서관 프로그램을 예로 든다. 기술보고서가 새로운 자료 유형으로 들어오면 이미 쓰이던 모듈까지 고치거나 다시 컴파일해야 할 수 있다. 새 자료를 처리하는 코드를 어디에 두느냐는 기존 모듈이 무엇에 의존할 수 있느냐와 맞물린다.

1995년 6월 공개 토론에서는 기존 모듈을 손댈 수 있다는 것과 손대야 한다는 것의 차이가 쟁점이었다. 카일 브라운은 잘못 설계된 클래스라면 개발자가 소스를 고칠 수 있어야 한다고 했다. 마틴의 답은 예상한 확장을 하려면 기존 소스를 반드시 고쳐야 하는지에 관한 것이었다. 어떤 변경이 생길지 미리 짚어야 한다는 어려움은 남았다. 2007년 공개 기록에는 다섯 원칙을 묶은 SOLID라는 이름이 나온다. 2009년의 인터페이스 논쟁에서도 내부 클래스의 인터페이스와 공개 플러그인 API에는 서로 다른 조언이 제시됐다. 이 자료들은 원칙이 어떻게 쓰이고 논쟁됐는지 보여 준다. SOLID라는 이름이 퍼지면서 적용 조건에 대한 판단이 실제로 바뀌었는지는 별도의 근거가 필요한 역사적 질문이다. [1995년 토론](https://groups.google.com/g/comp.lang.c%2B%2B/c/nntTK8eH_Ag/m/uvoJEnDH9zAJ) · [2007년 자료](https://www.infoq.com/news/2007/01/principles-of-agile-design/) · [2009년 논쟁 기록](https://www.joelonsoftware.com/2009/01/31/from-podcast-38/)

1996년 글에서 마틴은 목록 정렬을 `DrawAllShapes`가 맡게 했다. 한 구현에서는 `Circle::Precedes`가 상대 도형을 검사해 사각형이면 원을 먼저 놓는다. 세 번째 도형과 원의 순서를 정해야 하면 `Circle`을 다시 고칠 수 있다. 도형 종류별 순서를 표로 옮기면 사각형을 원보다 먼저 그리기 위해 두 항목의 위치만 바꾸면 된다. 그다음 요구가 개별 도형을 넓이순으로 그리는 것이라면 표에 없는 정보가 필요하다.

같은 글 후반에서 마틴은 `dynamic_cast`를 쓰는 함수 둘을 제시한다. `DrawAllShapes`의 한 구현은 원과 사각형을 골라 그리고, `DrawSquaresOnly`는 사각형을 골라 그린다. 둘 다 삼각형을 건너뛴다. 모든 도형을 그려야 하는 함수라면 그림 하나가 빠진 것이고, 사각형만 그려야 하는 함수라면 건너뛰는 것이 맞다. 여기서는 함수 이름과 설명을 읽으면 각각 무엇을 맡았는지 알 수 있다. 분류를 맡은 검토자에게 코드와 프롬프트가 주어졌을 때는 그 책임을 어디까지 확인할 수 있을까?

[Meyer 1988 초판 22–25쪽 대조 기록](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md) · [Martin 1996, 1쪽](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=1) · [Martin 1996, Listings 3–6, 9–10](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf)

### 3. 자료와 방법

같은 소스와 같은 수정안을 두고 유지보수 판정이 달라질 수 있는가? 이 질문을 검사하려면 검토자가 받은 정보와, 그 정보로 내려야 하는 판정을 따로 기록해야 한다. 먼저 위반 분류 벤치마크의 저장 자료에서 실제로 어떤 입력이 남아 있는지 확인했다. 이어 도서관 예제에서 판단에 필요한 사실 중 일부를 공개하지 않았을 때도 결론이 정해지는지 살폈다.

아카이브에서는 OCP 참조 쌍 48개와 저장 응답 768건을 별도로 셌다. 참조 쌍은 위반 예시와 수정 예시로 이루어진다. 저장 응답 한 건은 제출 코드, 프롬프트, 기록된 모델 응답을 한데 묶은 행이다. OCP 응답 파일은 16개이며 파일마다 48행이 있다. 저장 응답 수는 서로 다른 프로그램의 수를 뜻하지 않는다. 각 프롬프트에서 제출 코드가 정확히 한 번 나오는지 확인한 뒤 그 부분을 공통 자리표시자로 바꿨다. 지시문 틀은 남은 문자열이 완전히 같을 때 하나로 셌다.

이 기계적 집계에 이어 틀의 문구를 읽었다. ‘별도로 명시했다’는 것은 지시문이 해당 사례에 필요한 새 동작을 요구하거나, 기존 호출에서 계속 보장할 동작을 밝힌 경우를 가리킨다. 예컨대 “삼각형도 그려야 한다”는 변경 요구이고 “기존 너비 조회는 계속 지원해야 한다”는 호출자 계약이다. 반복 분기에 다형성을 적용할 만한지 물어보는 문구는 일반적인 판별 단서로 읽었다. 가려진 코드에 있는 단서나 아카이브의 다른 문서에 있는 맥락은 이 대조의 범위 밖이다.

출처를 연결할 때는 저장 행의 제출 코드를 모든 OCP 참조 쌍의 양쪽 소스와 비교했다. 문자열 그대로 대조한 뒤 양끝 공백만 걷어 내 비교를 반복했다. 이 절차로 확인할 수 있는 것은 두 기준에서의 문자열 일치 여부다. Python 참조 쌍에서는 최상위 클래스가 직접 선언한 메서드 이름을 구문 트리에서 읽었다. 밑줄로 시작하는 이름은 제외했다. 이 검사는 선언이 빠졌는지를 보여 준다. 기존 호출자가 그 메서드를 사용했는지, 상속을 통해 여전히 호출할 수 있는지, 계속 쓸 수 있다고 보장받았는지는 각각 별도의 근거가 필요하다.

도서관 예제에서는 기존 소스, 수정안, 호출 입력과 편집 범위를 고정했다. 기존 클라이언트가 부르는 경로에서 출력 문자열이나 예외의 유형·메시지를 기록하고, 먼저 새 요구를 충족하는지와 기존 계약을 지키는지를 따로 채점했다. 그 두 판정이 모두 참일 때 승인으로 정했다. 그다음 이미 계산한 판정표에서 공개된 정보와 맞는 행을 남겨, 일부 전제가 빠져도 승인이나 거절이 하나로 정해지는지 확인했다. 벤치마크 자료는 ZIP의 JSON·JSONL을 읽어 감사했다. 실행 검사는 이 연구에서 작성한 도서관·도형 예제로 수행했다. 부록 A에 입력과 재현 명령을 두었다.

[감사 코드](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/audit_are_we_solid.py) · [고정 인벤토리](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/are_we_solid_inventory.json)

### 4. 벤치마크가 판정에 제공한 정보

Pehlivan 등은 위반 시나리오를 정해 코드 예시를 생성하고 다듬었다. 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다. 모델의 분류 결과는 참조 라벨과 대조했다. OCP 저장 응답에서 제출 코드를 가리자 서로 다른 지시문 틀 24개가 남았다. 전략별로는 DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였고, 전략 간에 같은 문자열은 없었다. 어느 틀에도 개별 사례에 해당하는 새 요구나 보호할 호출자 계약을 따로 쓴 문구는 없었다.

그중 Python `EXAMPLE` 지시는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다. 제출된 `AreaCalculator`는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다. 새 도형을 지원할 때 이 분기가 수정 후보라는 판단은 코드에서 나온다. 그 확장이 실제 요구인지, 넓이 계산을 옮겨도 기존의 너비 조회를 지원해야 하는지는 검토 지시에 적혀 있지 않다.

너비 조회는 별도의 참조 쌍 37번에서 실제 편집 항목이 된다. 이 쌍에서는 넓이 계산을 도형 메서드로 옮기면서 `Rectangle.get_width` 선언을 뺐다. 저장된 제출 코드와 모든 참조 쌍의 양쪽 소스를 대조했을 때, 원본 문자열 비교와 양끝 공백을 제거한 비교 모두에서 일치가 없었다. 37번에서 직접 확인할 수 있는 것은 참조 소스에서 선언이 빠졌다는 사실까지다. 그 삭제가 수정안을 거절할 이유가 되려면 너비 조회를 기존 호출자에게 보장했다는 근거가 더 있어야 한다.

**표 1. 저장된 입력과 수정안 판정에 필요한 근거.**

| 검토할 질문 | 자료에서 확인한 내용 | 수정안 판정에 필요한 근거 |
| --- | --- | --- |
| 어떤 정답을 맞히는가 | 원저는 저자들이 검증한 참조 위반 범주에 모델 응답이 얼마나 일치하는지 평가했다. [원저 §III-A, C–D](https://arxiv.org/html/2509.03093v1#S3) | 구체적인 수정안과 승인 기준 |
| 어떤 기능을 추가해야 하는가 | 저장 Python EXAMPLE은 다형성으로 처리할 만한 반복 분기를 찾도록 했다. 개별 변경 요구는 템플릿에 별도로 적혀 있지 않았다. [대조 코드와 저장 행 위치](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53) | 실제 요청, 수용 조건, 변경을 맡을 경계 |
| 어떤 호출을 계속 지원해야 하는가 | 저장 템플릿에는 보호할 호출자 계약이 따로 없었다. 별도의 37번 참조 쌍에서는 너비 getter 선언이 빠졌다. [참조 쌍 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) | 계약의 범위와 근거가 되는 API 문서, 호출 코드, 테스트 또는 합의 |
| 구현에서 어떤 경계를 바꿀 수 있는가 | 저장 지시는 위반 범주와 설명을 요구한다. 업무상의 파일·인터페이스 보호 범위는 그 지시문에서 확인되지 않는다. [원저 §III-B 및 저장 행](https://arxiv.org/html/2509.03093v1#S3) | 보호할 산출물, 허용된 수정 또는 새 모듈 추가와 같은 경로 |

프롬프트 예시는 저장 JSONL 13행(ID 12)이다. 참조 쌍 37번은 별도의 ground truth JSON 위치다. [저장 아카이브](https://drive.google.com/file/d/12LDcKFBpJRkwH-zYJZ6Uhk9pE3RzgnUe/view) · [정확 일치 및 양끝 공백 제거 대조](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

[Pehlivan 등 §III](https://arxiv.org/html/2509.03093v1#S3) · [아카이브와 참조 쌍 37 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [저장 입력과 참조본 대조 코드](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

Bräuer 등(2018)은 전문가에게 측정 가능한 실천 규칙들이 설계 원칙을 얼마나 포착하는지 물었다. Cabral 등(2024)은 기계학습 기능을 확장하는 상황에서 SOLID를 묶어서 적용한 코드에 대해 참가자가 느낀 이해도와 확장 용이성을 조사했다. Zhu 등(2026)의 저장소 과제는 구체적인 변경을 주고 기능 테스트와 구조적 판정 기준을 적용한다. 참조 쌍 37번에서는 너비 조회를 계속 지원해야 했는지가 열려 있다. 다음 절에서는 이와 같은 종류의 정보가 판정에 어떤 차이를 만드는지 살핀다. 코드와 수정안을 그대로 두고 적용할 요구나 계약을 바꿀 수 있게 예제를 구성했다. [Bräuer DOI](https://doi.org/10.1016/j.jss.2018.03.002) · [Cabral DOI](https://doi.org/10.1145/3644815.3644957) · [Zhu arXiv](https://arxiv.org/abs/2603.27745)

### 5. 같은 수정안의 판정이 달라질 때

마이어가 예로 든 도서관 목록을 작은 프로그램으로 만들었다. 기존 `client.py`는 전달받은 목록 함수로 자료를 출력한다. 검토할 수정안은 그 함수에 새 처리를 덧붙이는 `reports.py` 하나를 추가하며, `catalog.py`와 `client.py`의 소스 내용은 바꾸지 않는다. 실행하면 기술보고서가 출력되고 정오표 요청은 여전히 거절된다. 기존 책 출력은 접두어 `book`이 `BOOK`으로 바뀐다.

이제 수정안의 코드와 같은 실행 기록을 검토자 둘에게 주고 둘 다 기술보고서만 지원하라는 요청을 받았다고 하자. 한쪽은 기존 호출자에게 책 출력을 그대로 돌려주기로 했다는 사실을 알고 있다. 다른 쪽에는 그 출력이 계약 밖이라고 명시한다. 책의 출력이 바뀐 사실은 두 사람에게 같다. 그 사실을 위반으로 볼지는 어느 계약이 적용되는가에 달려 있다. 표 2에서는 여기에 정오표 지원 요구까지 교차시켰다. 두 계약에 공통으로 들어 있는 것은 학술지·학회록 출력과, 정오표와 별개의 미지원 자료 유형을 거절하는 동작이다.

**표 2. 같은 수정안에 적용한 요구와 계약.**

| 요구 | 기존 책 접두어 보호 | 새 요구 만족 | 기존 계약 보존 | 이 사례의 승인 기준 |
| --- | --- | --- | --- | --- |
| 기술보고서 | 아니오 | 예 | 예 | 승인 |
| 기술보고서 | 예 | 예 | 아니오 | 거절 |
| 기술보고서와 정오표 | 아니오 | 아니오 | 예 | 거절 |
| 기술보고서와 정오표 | 예 | 아니오 | 아니오 | 거절 |

부분 정보로 판정할 때는 표에서 공개된 사실에 맞는 행만 남긴다. 검토 중에 “정오표도 이번에 지원해야 한다”고 들으면 아래 두 행이 남는다. 두 행 모두 거절이므로 책 계약을 확인하기 전에 결론을 낼 수 있다. “기술보고서만 필요하다”는 사실을 들으면 위 두 행이 남는다. 이때는 한 행은 승인, 한 행은 거절이다. 검토자가 다음으로 얻어야 할 답은 책 출력이 보호 대상인지다.

이 절차는 검토 중인 명세 가운데 실제 명세가 들어 있다는 전제에서 성립한다. 공개된 사실과 맞는 행이 하나도 없다면 먼저 비교에 넣은 명세와 공개된 내용을 다시 대조해야 한다. 승인과 거절이 모두 남는다면 동일한 정보만 받은 규칙은 어느 경우에도 맞는 하나의 판정을 골라낼 수 없다. 현재 답은 조건부로 제시하거나 보류할 수 있다. 부록 A의 3×3 표는 이 사례에서 요구와 계약을 각각 알리거나 가린 경우를 모두 적은 것이다.

같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다. 새 모듈 하나로 기술보고서와 정오표를 모두 처리하면서 기존 책 출력까지 보존했다. 표 2의 거절은 실행 가능한 대안이 있는 조건에서 특정 수정안에 내려진 판정이다. 이 방식을 다른 사례에 적용하려면, 무엇을 보장했는지에 대한 가능한 명세와 그 근거를 먼저 밝혀야 한다. 그래야 보류가 실제로 확인할 질문이 된다.

[네 조합의 재현](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md) · [정보 공개 조건별 결과](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/34_MAINTENANCE_JUDGMENT_UNDER_PARTIAL_DISCLOSURE.md)

### 6. 변경을 놓을 자리와 호출 경로

도서관 예제에서는 완성된 수정안 하나를 놓고 승인할 수 있는지를 따졌다. 구현을 고르는 단계에서는 다른 질문이 생긴다. 새 기능이 들어갈 자리와 그 기능을 호출할 자리가 주어졌을 때, 어떤 기존 파일에 손을 대야 할까? 도형 예제로 돌아가 연산별로 파일을 둔 구현과 도형별로 파일을 둔 구현을 비교했다. 이하의 수치는 실제로 실행한 후보가 수정한 기존 파일을 센 것이다.

삼각형을 추가할 때 도형별 구현은 삼각형 파일 하나를 더하면 됐다. 연산별 구현에서는 그리기를 맡은 기존 파일을 고쳤다. 이름표를 붙이는 연산을 추가하자 상황이 바뀌었다. 도형별 구현에서는 원과 사각형 파일을 각각 고쳤고, 연산별 구현에서는 이름표 연산을 새 파일에 둘 수 있었다. 네 수정안 모두 기능 검사를 통과했다. 어느 쪽의 기존 파일을 건드려야 하는지는 요청에 따라 달랐다(그림 1A).

그 차이가 같은 요구에서도 남는지 보기 위해 이번에는 양쪽에 `render_many`를 추가했다. 도형 목록을 받아 각 출력에 대괄호를 붙이는 함수다. 도형별 구현에서 출력 변환을 각 도형이 맡도록 정하면 원과 사각형 파일을 모두 고칠 것으로 예측했다. 공용 어댑터를 사용할 수 있으면 두 구현 모두 기존 파일을 그대로 두고 새 파일 하나에 기능을 담을 수 있다고 예측했다. 실행 결과, 도형별 구현이 변환을 각 도형에 배치한 후보에서만 기존 파일 두 개가 바뀌었다. 네 후보 모두 새 파일을 하나 추가했으며, 입력 순서와 중복을 보존하고 빈 목록과 미지원 도형을 명세대로 처리했다. 원과 사각형의 기존 렌더링도 유지됐다(그림 1B).

**그림 1. 기존 소스 파일 수정 수.** A는 삼각형 추가와 이름표 연산 추가를 비교한다. B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다. B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.

[PNG](https://drive.google.com/file/d/1uD_IpP77WJsKIWBngn72WEO9vp5JqzO1/view) · [SVG](https://drive.google.com/file/d/1swHCwTW3MNDv1mYE5-mCfsq73Iz1mnfZ/view) · [Batch prediction / 사전 예측](https://github.com/WhoSia/EvoNOMOS/commit/54d5af3f7ddcd4e74866b4b7f1b4ce188ed5aa7e) · [Batch fixture / 실행](https://github.com/WhoSia/EvoNOMOS/commit/d1ae74941da0539a8b8b8b330b9e6deb0e3aa83c) · [Figure source / 도판 코드](https://github.com/WhoSia/EvoNOMOS/commit/87f30604b8eca674030afa03a4798f277dfcc846)

공용 코드를 새 파일에 둘 수 있어도 호출자가 그 파일의 기능을 쓸 수 있는지는 따로 확인해야 한다. 이를 보기 위해 목록을 받는 배치 함수와 구별되는 요구를 주었다. 단일 렌더링 결과를 요청한 경우에만 대괄호로 감싸는 옵션이다. 두 구현 모두 새 함수로 이 옵션을 제공할 수 있었다. 그런데 같은 어댑터를 추가한 상태에서 예전 함수에 `bracketed=True`를 넘기자 인자가 거절됐다. 옵션을 예전 함수로 제공한 후보는 연산별 구현에서 기존 파일 하나, 도형별 구현에서 두 개를 고쳤다. 예전 함수가 외부 변환 모듈을 불러오도록 이미 구성된 별도 기준선에서는 두 구현 모두 새 파일 하나로 그 함수에 옵션을 연결했다(표 3).

**표 3. 새 렌더링 옵션이 제공되는 호출 경로.**

| 새 기능을 받는 경로 | 연산별 배치 기존 파일 수정 | 도형별 배치 기존 파일 수정 | 각 배치의 새 파일 |
| --- | --- | --- | --- |
| 새 진입점 | 0 | 0 | 1 |
| 기존 진입점 | 1 | 2 | 0 |
| 확장 지점이 있는 기존 진입점 | 0 | 0 | 1 |

표 3의 마지막 행은 확장 지점이 이미 놓인 상태에서 세기 시작한다. 확장 지점을 처음 마련하는 비용은 측정 범위 밖이다. 두 표본 구현에서 확인한 파일 수를 실제 작업량으로 해석하려면 별도의 측정이 필요하다.

[Prediction / 예측](https://github.com/WhoSia/EvoNOMOS/commit/76fa9222a7149b7c98a6315375834f2bd909fe0e) · [Execution / 실행](https://github.com/WhoSia/EvoNOMOS/commit/0ede7b241c8f9f50436be9703561bb9e7cc9fb8b)

### 7. 결론

사각형이 먼저 그려졌다는 실행 결과를 근거로 함수의 수정을 요구하려면, 원을 먼저 놓는 일이 그 함수의 책임임을 알아야 했다. 도서관 예제에서는 실행 기록을 고정한 채 그 책임에 해당하는 요구와 기존의 약속을 바꿀 수 있었다. 정오표가 필수라는 사실은 이 수정안을 곧바로 거절할 근거였다. 기술보고서만 필요할 때는 기존 책 출력을 보호해야 하는지 확인해야 했다.

이 글에서 제시한 방법은 같은 수정안에 대해 지금 가능한 명세를 드러내고, 어느 사실을 알면 결론이 정해지는지 시험하는 것이다. 실제 리뷰에서는 요구서나 테스트에서 적용할 계약을 읽어 낼 수 있다. §6처럼 호출 경로가 명세에 들어 있는 경우도 있다. 어떤 자료로 가능한 명세를 정하고 무엇을 시험하면 충분한지는 다른 사례와 방법들이 비교할 수 있는 질문으로 남는다. 이 연구의 관찰 근거는 한 벤치마크의 저장 자료와 직접 구성해 실행한 예제다.

### 부록 A · 재현 자료

§3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다. §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다. 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다. 그림 1의 소스와 출력 위치는 그림 캡션에 있다.

[재현 자료 및 명령 / Reproduction notes](https://github.com/WhoSia/EvoNOMOS/commit/ed443890f0b5f9b171d68d010b605e7cefec7f14)

아래에서 ‘미공개’는 해당 항목의 두 값이 모두 가능하다는 뜻이다. 보류는 공개된 정보와 양립하는 행 가운데 승인과 거절이 모두 남았을 때의 판정이다.

| 공개된 요구 | 책 접두어 보호 제외 | 책 접두어 보호 포함 | 책 접두어 계약 미공개 |
| --- | --- | --- | --- |
| 기술보고서 | 승인 | 거절 | 보류 |
| 기술보고서와 정오표 | 거절 | 거절 | 거절 |
| 요구 미공개 | 보류 | 거절 | 보류 |

## English manuscript

### 1. Introduction

In 1996, Robert Martin described a function that drew the shapes in a list in order. A triangle could be added without editing the function if the triangle supplied its own drawing operation. Martin then introduced a new requirement. Every circle had to be drawn before any square. Given a list that begins with a square, the same function still draws the square first.

Who was supposed to sort the list? If the caller was to put the circles first, the drawing function already does its job. If the function was to guarantee that order for any input, it falls short. Reading the code tells a reviewer what gets drawn first. The reviewer needs the agreement between caller and function to tell whether that is a defect.

Martin called the design closed with respect to the addition of a shape. The sorting requirement gives the same code a different test. That is where our question about the open–closed principle (OCP) begins. When a reviewer calls a proposed edit a violation, can the author recover from the verdict what the program was expected to accommodate or preserve? We use *over-axiomatization* for the risk of treating such a verdict as settled when those premises are still open.

A benchmark that scores agreement with reference labels makes that question tractable. Its archive lets us inspect the information actually supplied for classification. To test what an acceptance decision requires, we hold a patch fixed and vary the task and the promise to existing callers. We then return to drawing to see when a separate implementation can deliver an extension through the call the user already makes.

[Martin 1996, Listing 2 and Strategic Closure](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=6) · [Benchmark archive audit](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [Fixed-patch comparison](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md)

### 2. The open–closed principle in Meyer and Martin

In 1996 Martin attributed the principle to Bertrand Meyer, citing page 23 of the 1988 first edition. In Meyer’s account a module is closed once other modules can use it on the basis of a stable description. His library example gives that stability a concrete test. When technical reports become a new category, a program that handles each publication type explicitly may require edits to, or recompilation of, existing modules. The choice of where to handle the new type matters to the modules that already depend on the catalog.

Having to edit a module to extend it was the issue in a June 1995 public exchange. Kyle Brown argued that developers had to be able to fix a badly designed class. Martin’s reply distinguished the right to edit a class from the need to edit it for an anticipated extension. The design would still have to anticipate the right change. The label SOLID appears in the public record by 2007. In a 2009 discussion of interfaces, the distinction between a routine internal class and a public plugin API still mattered to the participants’ advice. These sources document particular uses and disagreements about the principle. A causal history of the acronym would require evidence of what changed as the label circulated. [Contemporary exchange](https://groups.google.com/g/comp.lang.c%2B%2B/c/nntTK8eH_Ag/m/uvoJEnDH9zAJ) · [2007 report](https://www.infoq.com/news/2007/01/principles-of-agile-design/) · [2009 exchange](https://www.joelonsoftware.com/2009/01/31/from-podcast-38/)

In the 1996 article Martin made sorting part of `DrawAllShapes`. In one implementation, `Circle::Precedes` puts a circle before a square by inspecting the other shape. A new rule about where a third type ranks against a circle can send the edit back into `Circle`. Martin moved the ranking of types into a table, so putting squares ahead of circles becomes a matter of swapping two entries. If the next request were to sort individual shapes by area, the table would need information it does not contain.

Later in the article Martin uses `dynamic_cast` in two routines. One version of `DrawAllShapes` recognizes circles and squares. `DrawSquaresOnly` selects squares. Both skip a triangle. The first routine leaves a shape undrawn when its job is to draw them all. The second skips exactly the shapes it is supposed to skip. Here the names and stated jobs make the distinction available to the reader. What can a classification reviewer establish when the input consists of code and a prompt?

[Meyer 1988, first edition, pp. 22–25](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md) · [Martin 1996, p. 1](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=1) · [Martin 1996, Listings 3–6, 9–10](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf)

### 3. Materials and methods

Can the same code and the same patch warrant different maintenance decisions? To examine this question, we record the information supplied to the reviewer separately from the decision it is meant to support. We first inspect what was saved as input to a violation-classification benchmark. In a separate catalog fixture, we then ask whether the decision is already settled when some facts relevant to it are withheld.

We counted 48 OCP reference pairs and 768 saved response records as different units. A reference pair consists of a violation example and its revision. A saved record contains the submitted source, its prompt, and the recorded model response. The archive has 16 OCP response files with 48 records each. These are counts of records, not of distinct programs. We checked that the submitted source occurred exactly once in each prompt, replaced that occurrence with a common placeholder, and counted the resulting instruction templates by exact string identity.

We then read the wording of the templates. We call a requirement separately stated if the instruction asks for a new behavior in the particular case, such as drawing triangles. A separately stated caller contract identifies behavior that must survive the change, such as keeping an existing width query available. A direction to look for branches where polymorphism might fit is a general classification cue. This reading concerns the instruction left after masking, so the result is scoped to that text. The submitted source and other material in the archive can carry further context.

To check provenance, we compared the code in every saved OCP record with both sides of every OCP reference pair. We compared the stored strings and repeated the comparison after stripping only leading and trailing whitespace. This tests textual identity under two specified rules. For the Python reference pairs we used syntax trees to compare the method names declared directly by top-level classes, excluding names beginning with an underscore. A disappearance in that comparison is evidence of a declaration change. Inherited availability, actual use by clients, and a promise of continued availability each require their own evidence.

In the catalog fixture we fixed the existing source, the candidate patch, the inputs to the client, and the permission to add a module. Through the existing client interface we recorded either the output string or the exception type and message. We scored the new requirement and the protected legacy behavior separately. Our fixture accepts a patch when it meets both conditions. We then took the resulting rows and retained those matching the disclosed facts to see whether partial information sufficed to settle the verdict. For the archive we inspected JSON and JSONL within the ZIP. The catalog and drawing checks execute fixtures built for this study. Appendix A identifies the inputs and reproduction commands.

[Audit script](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/audit_are_we_solid.py) · [Pinned inventory](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/are_we_solid_inventory.json)

### 4. What the benchmark gives the reviewer

Pehlivan et al. specified violation scenarios and refined the generated examples. A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion. The benchmark compares model classifications with the reference labels. Masking the submitted source in the saved OCP records left 24 distinct instruction templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE, and four SMELL. No string was shared across strategies. The templates gave no separate statement of either the change requested in a particular case or the caller contract protected in that case.

One saved Python `EXAMPLE` prompt directs the reviewer to repeated branches where polymorphism would fit. The submitted `AreaCalculator` checks the shape type before calculating the area of a circle or rectangle. The branch gives the reviewer somewhere to look if a new shape is requested. The prompt leaves open whether that is the task and whether calls reading a rectangle’s width must still work after its area calculation moves.

Width becomes a concrete issue in the separate reference pair 37. That revision moves area calculation onto the shapes and drops the declaration of `Rectangle.get_width`. No saved submission matched either side of any reference pair, whether we compared the stored strings or trimmed whitespace at their ends. In pair 37 we can establish that the declaration was removed. Turning its removal into a reason to reject the patch would require evidence that existing callers were promised continued access to the width.

**Table 1. Evidence in the saved material and evidence needed to assess a patch.**

| Question | Evidence in the saved material | Evidence for a patch decision |
| --- | --- | --- |
| What counts as a correct answer? | The benchmark compares model responses with the violation labels verified by its authors. | The proposed edit and the criteria for acceptance. |
| Which behavior should be added? | The saved Python EXAMPLE prompt points to repeated branching where polymorphism would fit. The templates state no separate request for an individual case. | The actual request, its acceptance conditions, and the boundary responsible for it. |
| What do existing callers rely on? | The templates state no separate caller contract. The distinct reference pair 37 loses the width getter declaration. | The scope of the commitment and supporting API documentation, client code, tests, or agreement. |
| What may the implementation change? | The instructions ask for a violation category and an explanation. They do not specify protected implementation files or interfaces. | The protected artifacts and permitted changes, including whether a new module may be added. |

The saved prompt is on JSONL line 13 (record ID 12). Reference pair 37 is in a separate ground-truth JSON file. [Archived material](https://drive.google.com/file/d/12LDcKFBpJRkwH-zYJZ6Uhk9pE3RzgnUe/view) · [Source comparison](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

[Pehlivan et al., §III](https://arxiv.org/html/2509.03093v1#S3) · [Archive audit and reference pair 37](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [Submitted and reference source comparison](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

Bräuer et al. (2018) asked experts how much of a design principle their measurable practices covered. Cabral et al. (2024) asked participants about understanding and ease of extension in a machine-learning scenario under a bundled SOLID treatment. Zhu et al. (2026) gave specific repository change tasks and checked them against functional tests and structural oracles. Reference pair 37 leaves open whether callers were promised continued access to the width. The next section tests what a fact of that kind can do for a decision. We use a fixture that lets us change the applicable requirement or contract while leaving the code and the patch in place. [Bräuer DOI](https://doi.org/10.1016/j.jss.2018.03.002) · [Cabral DOI](https://doi.org/10.1145/3644815.3644957) · [Zhu arXiv](https://arxiv.org/abs/2603.27745)

### 5. When the same patch warrants different decisions

We built a small version of Meyer’s library catalog. The existing `client.py` renders each item through the catalog function passed to it. The candidate patch adds `reports.py`, which wraps that function, leaving the contents of `catalog.py` and `client.py` identical. The client now renders technical reports and still rejects requests for errata. In book output the prefix changes from `book` to `BOOK`.

Give two reviewers the same patch, the same execution record, and a request to handle technical reports alone. Tell one that existing callers were promised the original book output. Tell the other that book output is outside the contract. Both see the same change in the book prefix. Whether it violates a commitment depends on the applicable contract. Table 2 crosses these two contracts with requests that either include or exclude errata. Both contracts preserve the rendering of journals and proceedings and the rejection of a separate unsupported publication type.

**Table 2. Two requirements for accepting a fixed patch.**

| Request | Book prefix protected | Meets the request | Preserves the contract | Decision |
| --- | --- | --- | --- | --- |
| Technical reports | No | Yes | Yes | Accept |
| Technical reports | Yes | Yes | No | Reject |
| Technical reports and errata | No | No | Yes | Reject |
| Technical reports and errata | Yes | No | No | Reject |

For a decision under partial information, keep the rows compatible with the disclosed facts. Learning that the release must support errata leaves the bottom two rows. Both reject the patch, so the book contract can remain open. Learning that technical reports are the entire request leaves the top two rows. One accepts and one rejects. The question to ask next is whether the original book output was protected.

This procedure assumes that the actual specification is among the cases considered. If no row fits what is disclosed, the first step is to check that specification set against the disclosed facts. If both verdicts remain, a rule that receives the same information cannot choose one binary answer that is right in every compatible case. The reviewer can give the conditional answers or defer the verdict. Appendix A gives all nine settings obtained by disclosing or withholding the two fields in this case.

We also ran a second patch to check whether the stricter specification was feasible under the same edit boundary. A single added module handles technical reports and errata and keeps the original book output. The rejections in Table 2 concern a specific patch under a specification that an alternative can meet. For another case, reporting the candidate specifications and the evidence for including them makes it possible to turn a deferred verdict into a concrete question.

[Reproduction of the four combinations](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md) · [Disclosure replay](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/34_MAINTENANCE_JUDGMENT_UNDER_PARTIAL_DISCLOSURE.md)

### 6. Where a change can live and how callers reach it

In the catalog case we asked whether to accept a completed patch. Choosing an implementation raises a further question. Given a place for the new behavior and a function through which callers must reach it, which existing files have to change? We return to drawing, comparing one implementation organized by operation with another organized by shape. The counts below are for candidates we built and ran.

To add a triangle in the shape layout, we added one file. In the operation layout we edited the existing file that handled drawing. A request for a labeling operation reversed the comparison. We edited the circle and square files in the shape layout and added a new file in the operation layout. All four candidates passed their functional checks. Which layout required edits to existing files depended on the request (Figure 1A).

To see whether that difference would persist under a common request, we added `render_many` to both layouts. It takes a list of shapes and brackets each result. We predicted that assigning the transformation to the shapes in the shape layout would require editing both their files. With a shared adapter available, we expected each layout to support the feature in one new file while leaving the existing files intact. The only candidate that edited existing files was the one assigning the transformation to the shape files. It edited two. All four added a file, preserved order and duplicates, handled empty lists and unsupported shapes as specified, and kept the existing circle and square renderings (Figure 1B).

**Figure 1. Existing source files edited.** Panel A compares adding a triangle with adding a labeling operation. Panel B holds the batch-rendering request fixed and varies the placement rule. All four candidates in panel B passed the new and legacy behavior checks and added one file each.

[PNG](https://drive.google.com/file/d/1uD_IpP77WJsKIWBngn72WEO9vp5JqzO1/view) · [SVG](https://drive.google.com/file/d/1swHCwTW3MNDv1mYE5-mCfsq73Iz1mnfZ/view) · [Batch prediction](https://github.com/WhoSia/EvoNOMOS/commit/54d5af3f7ddcd4e74866b4b7f1b4ce188ed5aa7e) · [Batch fixture](https://github.com/WhoSia/EvoNOMOS/commit/d1ae74941da0539a8b8b8b330b9e6deb0e3aa83c) · [Figure source](https://github.com/WhoSia/EvoNOMOS/commit/87f30604b8eca674030afa03a4798f277dfcc846)

An adapter can sit in a new file even when an existing caller has no way to use it. We tested this with a separate request for an option that brackets the result of a single render. Both layouts offered the option through a new function. When we tried `bracketed=True` on the old function after adding the same adapter, the function rejected the argument. The candidates that delivered the option through the original function edited one existing file in the operation layout and two in the shape layout. From a separate baseline in which the original function could already load an external decorator, a new file alone connected the option to that function in each layout (Table 3).

**Table 3. Call paths for the new rendering option.**

| Path that provides the feature | Existing files edited, operation layout | Existing files edited, shape layout | New files per layout |
| --- | --- | --- | --- |
| New entry point | 0 | 0 | 1 |
| Original entry point | 1 | 2 | 0 |
| Original entry point with a hook | 0 | 0 | 1 |

The last row of Table 3 starts counting after the hook is in place. We left the initial cost of introducing it outside the measurement. Relating these file counts to actual maintenance effort would require a separate measurement.

[Prediction](https://github.com/WhoSia/EvoNOMOS/commit/76fa9222a7149b7c98a6315375834f2bd909fe0e) · [Execution](https://github.com/WhoSia/EvoNOMOS/commit/0ede7b241c8f9f50436be9703561bb9e7cc9fb8b)

### 7. Conclusion

Seeing a square drawn first gives a reviewer a reason to change the drawing function when putting circles first is that function’s job. In the catalog we could hold the execution record fixed and vary the requirements and commitments that specify the job. An errata requirement settled rejection immediately. When technical reports were the whole request, the decision still turned on whether the original book output was protected.

The method in this paper makes the compatible specifications visible for a fixed patch and tests which fact would settle the decision. In a repository review, requirements and tests may help establish the scope of a promise. A specification can also name the required call path, as in Section 6. Which sources justify including a specification and which observations suffice to test it remain open to comparison across cases and methods. Our evidence comes from the saved material of one benchmark and the examples we built and ran.

### Appendix A · Reproduction

For Sections 3–4 the audit reads the archived JSON and JSONL. For Sections 5–6 the fixtures run the examples constructed for this study. The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.

[Reproduction notes](https://github.com/WhoSia/EvoNOMOS/commit/ed443890f0b5f9b171d68d010b605e7cefec7f14)

When a field is withheld, both of its recorded values remain possible. Defer means that at least one compatible row accepts the patch and at least one rejects it.

| Disclosed request | Book prefix outside contract | Book prefix protected | Prefix contract withheld |
| --- | --- | --- | --- |
| Technical reports | Accept | Reject | Defer |
| Technical reports and errata | Reject | Reject | Reject |
| Request withheld | Defer | Reject | Defer |
