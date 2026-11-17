# Paper B — Bilingual Integrated Manuscript 07

Archived working manuscript copied from [Notion integrated 07](https://app.notion.com/p/41bef561cf9281cbaf29c9a9b5daba1e), 2026-11-17 KST. Earlier Notion copies 01–06 remain preserved. Not a peer-reviewed result; historical causal claims and independent maintenance experiments are not established.


Working integration copy 07, 2026-11-17. Changes from copy 06: place historical reception after the Meyer example; place competing research after the archive audit's concrete evidence; preserve all former copies. Preserves the full seven-section bilingual manuscript and appendix from [Paper B 통합 원고 03 · 한·영 문장 편집본](https://app.notion.com/p/41bef561cf9281968d9adaf0d0a5ffef). Editorial changes: restore the conditional advice / violation-label question; delimit historical inference, benchmark classification and patch acceptance; make the information limit and pre-existing hook assumptions explicit; state the proposed deeper mathematical account as a future test rather than a finding. The earlier copy is unchanged.

서론부터 결론까지 각 언어로 연달아 읽는 판본이다. 아래 본문에는 문단 단위 편집을 반영했다. 별도의 확대 집필 목표는 작업실의 작업표를 따른다.

**통합 교정본 05 · 초록 작업안 (한국어)**

이 글은 개방–폐쇄 원칙을 잘못된 규칙으로 선언하기보다, 어떤 변경을 예상하고 어떤 기존 동작을 보존해야 한다는 조건부 설계 조언이 언제 수정안을 배제하는 판정으로 취급되는지 묻는다. 마이어와 마틴의 원전을 통해 판단의 전제를 추적하고, SOLID 위반 분류 벤치마크의 저장 자료에서 모델에게 제공된 정보의 범위를 감사했다. 별도로 구성한 도서관 프로그램에서는 코드를 고정한 채 새 요구와 보호할 계약을 바꾸자 동일 수정안의 승인 여부가 달라졌다. 도형 구조 비교에서는 요구를 처리하는 파일의 위치뿐 아니라 기존 호출자가 새 기능에 도달하는 경로에 따라 수정 범위가 달라졌다. 결과는 해당 아카이브와 실행 후보에 한정된다. 이 글은 설계 원칙의 유용성을 부정하지 않으며, 위반 라벨이 구체적인 공학적 결정을 정당화하려면 어떤 전제가 필요한지 밝히려 한다.

**Working abstract (English)**

This paper asks when a conditional design argument becomes a seemingly self-sufficient violation verdict. We read Meyer and Martin to recover the changes and commitments against which the open–closed principle was argued, then audit the stored inputs of one benchmark that classifies SOLID violations. The benchmark evaluates agreement with reference labels; it does not determine whether an unrelated maintenance patch should be accepted. In a separate executable library fixture, the very same patch receives different verdicts as the requested extension and the protected caller contract vary. Further drawing fixtures show that the existing files a candidate must edit also depend on permitted placement and whether callers can reach the added behavior through their entry points. The evidence is limited to the archived material and the constructed candidates. Rather than reject design principles as such, we argue that using a violation label to justify an engineering decision requires recovering the concrete obligations on which that decision rests.

## 한국어 원고

### 1. 서론

로버트 마틴은 1996년 글에서 도형 목록을 받아 차례로 그리는 함수를 예로 들었다. 삼각형이 자신을 그리는 동작을 제공하면, 그 함수를 고치지 않고도 삼각형을 추가할 수 있었다. 이 설계에 마틴은 새 요구를 붙였다. 모든 원을 사각형보다 먼저 그려야 한다. 같은 함수에 사각형으로 시작하는 목록을 주면 여전히 사각형부터 그린다.

원을 먼저 그리려면 누가 목록을 정렬해야 할까? 호출자가 정렬한 목록을 넘기기로 했다면 그리기 함수는 그대로 둘 수 있다. 어떤 목록을 받아도 함수가 순서를 보장하기로 했다면 지금 코드로는 부족하다. 소스 코드를 읽으면 함수가 정렬하지 않는다는 사실을 알 수 있다. 그 사실을 개방–폐쇄 원칙(OCP) 위반의 근거로 삼으려면 정렬을 누가 맡았는지도 알아야 한다.

여기에는 설계 원칙 자체보다 그 원칙을 사용하는 방식에 관한 문제가 있다. 마틴의 사례에서는 앞으로 어떤 변화에 대비할지를 정해야 비로소 어떤 코드를 닫아 둘지 논의할 수 있었다. 그 판단을 변경 요구가 빠진 ‘위반’ 판정으로 바꿔 사용한다면, 처음에는 결론을 정당화했던 전제가 사라진다. 우리는 이 위험을 원칙의 ‘과도한 공리화’라고 부른다. 이것은 SOLID 전체가 무효하다는 역사적 결론이 아니라, 조건부 설계 조언을 무조건적인 탈락 기준처럼 적용할 때 무엇을 잃는지 묻는 문제 제기다.

이 문제를 따지려면 ‘위반’이라고 분류하는 일과 특정 수정안을 거절하는 일을 먼저 나눠야 한다. SOLID 위반 분류 벤치마크의 저장 자료는 모델이 어떤 근거를 받았는지 보여 주지만, 특정 유지보수 요청이 승인되어야 하는지까지 판정하지는 않는다. 우리는 별도로 만든 도서관 프로그램에서 같은 수정안을 서로 다른 요구와 기존 호출자 계약 아래 두어 그 간격을 검사한다. 수정안 자체의 수용 여부를 따진 다음에는, 새로운 기능이 실제 호출 경로에 도달하도록 만드는 일이 어느 기존 파일을 바꾸게 하는지도 비교한다.

[Martin 1996, Listing 2와 Strategic Closure](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=6) · [벤치마크 기록 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [동일 패치 비교](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md)

### 2. 마이어와 마틴의 개방–폐쇄 원칙

마틴은 1996년 글의 첫머리에서 이 원칙을 베르트랑 마이어에게서 가져왔다고 밝히며 1988년 초판 23쪽을 인용한다. 이어지는 두 사례를 다루는 이유는 SOLID 다섯 원칙의 기원을 한 줄로 연결하기 위해서가 아니라, OCP에 적용 조건이 명시되어 있었는지 살피기 위해서다. 마이어의 설명에서 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 사용할 수 있는 모듈이다.

도서관 프로그램이 자료의 종류를 하나씩 구별해 처리한다면 기술보고서 한 종류를 추가하는 데도 기존 모듈의 수정이나 재컴파일이 필요할 수 있다. 이때 설계자는 새 동작을 어디에 넣을지와 기존 사용자가 계속 어떤 동작에 의존할 수 있을지를 함께 고려하게 된다.

이 원칙은 정착하기 전부터 이견을 낳았다. 1995년 6월 공개 토론에서 Kyle Brown은 잘못 설계된 클래스라면 개발자가 소스를 고쳐야 한다고 반박했다. 마틴은 ‘닫혀 있다’는 말을 수정할 권한이 없다는 뜻이 아니라, 예상한 확장을 위해 기존 코드를 반드시 수정할 필요가 없다는 뜻으로 구분했다. 그는 어떤 변경이 생길지 미리 알아야 한다는 어려움도 인정했다. [당시 토론](https://groups.google.com/g/comp.lang.c%2B%2B/c/nntTK8eH_Ag/m/uvoJEnDH9zAJ)

이 논쟁은 OCP가 처음부터 단 하나의 무조건적 금지 명령으로 받아들여졌다고 가정하기 어렵게 한다. 2007년에는 다섯 원칙을 묶은 SOLID라는 명칭이 공개 기록에 나타나고, 2009년의 인터페이스 논쟁에서는 내부 클래스와 공개 플러그인 API가 서로 다른 판단을 요구했다. 이런 자료로 원칙의 전파와 수용 과정에 논쟁이 있었다는 점은 말할 수 있지만, 특정 약어나 자동화 도구가 조건을 탈락시켰다는 인과관계까지 증명할 수는 없다. [2007년 자료](https://www.infoq.com/news/2007/01/principles-of-agile-design/) · [2009년 논쟁 기록](https://www.joelonsoftware.com/2009/01/31/from-podcast-38/)

마틴은 목록을 정렬하는 일을 `DrawAllShapes`에 맡겼다. 첫 구현에서는 `Circle::Precedes`가 상대 도형을 검사해 사각형이면 원을 앞에 놓았다. 새 도형이 들어왔을 때 원과 그 도형의 순서를 정하는 코드가 이미 `Circle` 안에 있었다. 마틴은 이어서 도형 종류별 순서를 표로 옮겼다. 이제 사각형을 원보다 먼저 그리라는 요청에는 표에서 두 항목의 위치를 바꾸면 된다. 개별 도형의 넓이순으로 그리라는 요구를 가정하면 표에 없는 정보가 필요하다. 어느 부분을 그대로 둘 수 있는지는 어떤 변경에 대비하느냐에 달려 있다.

타입 검사가 위반의 근거가 되는지도 함수가 맡은 일에 달려 있다. 글의 뒷부분에서 마틴은 `dynamic_cast`를 쓰는 두 함수를 새로 제시한다. 원과 사각형을 가려 그리는 `DrawAllShapes`와 목록에서 사각형만 골라 그리는 `DrawSquaresOnly`다. 두 함수에 삼각형을 넣으면 어느 쪽도 그리지 않는다. 모든 도형을 그리기로 한 함수에서는 빠진 출력이고, 사각형만 그리기로 한 함수에서는 약속한 동작이다. 검토자가 어떤 근거로 두 경우를 구별할 수 있는지를 확인하려면, 실제로 받았던 코드와 지시를 구분해 살펴봐야 한다.

두 함수는 같은 구문을 사용하지만, 약속한 일이 달라 평가가 갈린다. 이 사례를 위반 여부의 판단으로 옮기려면 검토에 주어진 코드와 그 코드가 맡은 책임을 나눠야 한다. 우리는 먼저 자료를 어떤 단위로 읽었는지 밝힌 뒤, 저장된 분류 프롬프트에서 그 책임을 어디까지 확인할 수 있는지 살펴본다.

[Meyer 1988 초판 22–25쪽 대조 기록](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md) · [Martin 1996, 1쪽](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=1) · [Martin 1996, Listings 3–6, 9–10](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf)

### 3. 자료와 방법

이 질문을 저장 자료에 적용하기 위해 분석 단위를 세 가지로 나눴다. 참조 코드 쌍에는 위반 예시와 그 수정 예시가 들어 있고, 저장 응답에는 모델에 제출된 코드와 프롬프트, 기록된 응답이 들어 있다. 프롬프트 틀은 저장 프롬프트에 정확히 한 번 나오는 제출 코드를 공통 자리표시자로 치환해 얻었다. 틀의 동일성은 문자열로 판단했다.

저장 응답의 제출 코드를 모든 참조 쌍의 수정 전·후 소스와 대조했다. 각 문자열을 그대로 비교한 뒤 양끝 공백을 제거해 다시 비교했다. Python 참조 쌍은 구문 트리로 파싱해 최상위 클래스의 메서드 선언 이름을 비교했다. 밑줄로 시작하는 이름은 제외했다. 이 비교는 선언의 변화만 포착한다. 상속에 따른 호출 가능성, 실제 사용 여부, 보장의 범위는 별도 근거가 필요한 질문이다.

이 연구에서 작성한 도서관·도형 재현은 §5와 §6에서 정한 조건으로 실행했다. ZIP 안의 공개 재현 패키지 코드는 실행하지 않았다. 아카이브 식별 정보와 확인 명령은 부록 A에 있다.

[감사 코드](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/audit_are_we_solid.py) · [고정 인벤토리](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/are_we_solid_inventory.json)

### 4. 벤치마크가 판정에 제공한 정보

Pehlivan 등은 위반 시나리오를 정하고, 생성한 코드 예시를 수정·검증한 뒤 의견이 갈린 사례의 참조 라벨을 논의로 정했다. SOLID 위반을 식별하는 모델 응답은 그 라벨과 대조했다. OCP에 해당하는 아카이브에는 참조 쌍 48개와 저장 응답 768건이 있다. 저장 프롬프트에서 제출 코드를 가렸을 때 서로 다른 문자열 24개가 남았고, 네 전략 사이에 동일한 틀은 없었다. 각 사례의 변경 요구나 기존 호출자 계약을 따로 밝힌 틀은 없었다. 이는 벤치마크가 본래 수행하려는 분류 과제를 잘못 설계했다는 뜻이 아니다. 특정 수정안을 승인하거나 거절하는 데 이 분류 결과를 사용하려면 추가 증거가 필요하다는 뜻이다.

저장된 Python `EXAMPLE` 지시는 다형성으로 처리할 만한 반복 분기를 찾도록 한다. 제출된 `AreaCalculator`는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다. 그 분기를 보면 새 도형을 추가할 때 어디에 손댈지 짐작할 수 있다. 새 도형 추가가 실제 요청인지, 사각형의 너비를 직접 읽는 호출을 계속 지원해야 하는지는 이 지시문에서 확인되지 않는다.

별도의 참조 쌍 37번은 넓이 계산을 도형 메서드로 옮기면서 `Rectangle.get_width` 선언을 뺐다.

원본 문자열과 양끝 공백을 제거한 문자열을 대조했을 때, 저장된 제출 코드와 참조 쌍의 어느 쪽도 일치하지 않았다. 따라서 여기서 근거로 삼는 것은 참조 쌍에서 확인한 선언의 변화다. 그 변화가 수정안을 거절할 이유가 되려면 호출자가 너비를 읽는 동작까지 보장받았는지 확인해야 한다. 이 참조 쌍에 실제 호출자가 있었다고 주장하지는 않는다. 대신 해당 문제가 판정에 영향을 줄 수 있는지 별도로 구성한 수정안에서 시험한다.

이 사례가 분류 평가를 대표하는 유일한 방식은 아니다. Bräuer 등(2018)은 설계 원칙을 측정 가능한 실천 규칙으로 옮길 때 전문가들이 보기에 무엇이 포착되고 무엇이 빠지는지 물었다. Cabral 등(2024)은 구체적인 기계학습 확장 상황에서 SOLID 적용 전후 코드에 대한 참가자의 이해도와 확장 용이성 인식을 조사했다. Zhu 등(2026)은 저장소 변경 요구에 기능 테스트와 구조적 판정 기준을 결합했다. 세 연구는 각각 **원칙의 측정 범위, 사용자의 인식, 특정 변경에서의 기능·구조 적합성**을 관찰한다. 우리 비교의 결과 변수는 같은 패치가 명시된 요구와 계약 아래에서 승인 기준을 충족하는가다. 앞선 연구를 코드 판정의 실패 사례로 취급하지 않으면서도, 무엇을 측정해야 어떤 결정을 정당화할 수 있는지 서로 다른 관점에서 확인할 수 있다. [Bräuer DOI](https://doi.org/10.1016/j.jss.2018.03.002) · [Cabral DOI](https://doi.org/10.1145/3644815.3644957) · [Zhu arXiv](https://arxiv.org/abs/2603.27745)

**표 1. 저장된 입력과 수정안 판정에 필요한 근거.**

| 검토할 질문 | 자료에서 확인한 내용 | 수정안 판정에 필요한 근거 |
| --- | --- | --- |
| 어떤 정답을 맞히는가 | 원저는 저자들이 검증한 참조 위반 범주에 모델 응답이 얼마나 일치하는지 평가했다. [원저 §III-A, C–D](https://arxiv.org/html/2509.03093v1#S3) | 구체적인 수정안과 승인 기준 |
| 어떤 기능을 추가해야 하는가 | 저장 Python EXAMPLE은 다형성으로 처리할 만한 반복 분기를 찾도록 했다. 개별 변경 요구는 템플릿에 별도로 적혀 있지 않았다. [대조 코드와 저장 행 위치](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53) | 실제 요청, 수용 조건, 변경을 맡을 경계 |
| 어떤 호출을 계속 지원해야 하는가 | 저장 템플릿에는 보호할 호출자 계약이 따로 없었다. 별도의 37번 참조 쌍에서는 너비 getter 선언이 빠졌다. [참조 쌍 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) | 계약의 범위와 근거가 되는 API 문서, 호출 코드, 테스트 또는 합의 |
| 구현에서 어떤 경계를 바꿀 수 있는가 | 저장 지시는 위반 범주와 설명을 요구한다. 업무상의 파일·인터페이스 보호 범위는 그 지시문에서 확인되지 않는다. [원저 §III-B 및 저장 행](https://arxiv.org/html/2509.03093v1#S3) | 보호할 산출물, 허용된 수정 또는 새 모듈 추가와 같은 경로 |

프롬프트 예시는 저장 JSONL 13행(ID 12)이다. 참조 쌍 37번은 별도의 ground truth JSON 위치다. 768은 저장 행의 수다. [저장 아카이브](https://drive.google.com/file/d/12LDcKFBpJRkwH-zYJZ6Uhk9pE3RzgnUe/view) · [정확 일치 및 양끝 공백 제거 대조](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

[Pehlivan 등 §III](https://arxiv.org/html/2509.03093v1#S3) · [아카이브와 행 37의 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [저장 입력과 참조본 대조 코드](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

### 5. 같은 수정안의 판정이 달라질 때

마이어의 예를 바탕으로 작은 도서관 목록 프로그램을 만들었다. 검토할 수정안은 기술보고서를 처리하는 모듈을 추가한다. 기존 소스 파일 두 개는 바이트 단위로 그대로다. 실행하면 기술보고서는 출력되고 정오표는 여전히 거절된다. 기존 책 출력의 접두어는 `book`에서 `BOOK`으로 바뀐다. 기존 파일을 수정하지 않았다는 사실은 기존 호출 결과까지 보존했다는 뜻이 아니다. 변경된 동작은 우리가 만든 실행 예제에서 관찰했다.

수정안과 실행 결과, 새 모듈을 추가할 수 있는 편집 범위를 고정했다. 새 요구는 기술보고서만 지원하는 경우와 정오표까지 지원하는 경우로 나눴다. 두 계약은 모두 학술지와 학회록의 출력, 그리고 별개의 미지원 자료 유형을 거절하는 동작을 보호한다. 넓은 계약은 원래 책 접두어까지 보호한다. 표 2의 승인은 새 요구와 보호할 계약을 모두 충족한 경우다.

**표 2. 같은 패치의 독립된 두 기준.**

| 요구 | 계약에 책 표기 포함 | 새 요구 만족 | 기존 계약 보존 | 이 사례의 승인 기준 |
| --- | --- | --- | --- | --- |
| 기술보고서 | 아니오 | 예 | 예 | 승인 |
| 기술보고서 | 예 | 예 | 아니오 | 거절 |
| 기술보고서와 정오표 | 아니오 | 아니오 | 예 | 거절 |
| 기술보고서와 정오표 | 예 | 아니오 | 아니오 | 거절 |

기술보고서만 필요하고 책 접두어를 보호하지 않는 경우에 승인된다. 정오표가 필수라는 사실을 알면 책 접두어 계약을 모르더라도 거절할 수 있다. 기술보고서만 필요하다는 사실을 알 때는 책 접두어를 보장했는지가 결론을 가른다. 별도로 만든 수정안은 같은 편집 범위에서 새 모듈 하나를 추가해 두 자료 유형을 처리하고 모든 보호 동작을 지켰다.

판정에 필요한 정보가 일부만 주어지면, 그 정보와 양립하는 명세들을 비교할 수 있다. 모든 명세가 같은 판정을 내리면 그 판정을 내릴 수 있다. 서로 다른 판정이 나오면 조건마다 결론을 밝히거나, 어느 조건이 실제로 적용되는지 확인할 때까지 보류할 수 있다. 이 논증은 실제 명세가 검토 중인 집합에 들어 있어 그 집합이 비어 있지 않다는 전제에서 성립한다. 이때 한 가지 입력만 받아 언제나 승인 또는 거절 중 하나를 출력하는 규칙은, 서로 다른 정답이 남아 있는 두 조건을 동시에 맞힐 수 없다. 다만 이 논증만으로 SOLID의 다른 정리나 실제 현장의 판단 오류율을 추정할 수는 없다. 부록 A에는 이번 사례에서 검토한 정보 공개 조건 아홉 개가 있다.

[네 조합의 재현](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md) · [정보 공개 조건별 결과](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/34_MAINTENANCE_JUDGMENT_UNDER_PARTIAL_DISCLOSURE.md)

### 6. 변경을 놓을 자리와 호출 경로

도서관 실험에서 확인한 것은 주어진 수정안의 적격성이었다. 다른 수정안이 더 적은 비용으로 같은 요구를 처리할 수 있는지는 아직 별도 문제다. 도형 예제로 돌아가, 어떤 변경에 대비할지와 새 기능을 어디에서 호출할지에 따라 기존 파일을 얼마나 수정하는지 비교한다. 여기서 세는 것은 실행한 후보들의 수정 파일 수이지 가능한 구현 전체의 최솟값이 아니다.

첫 비교에서는 요구를 바꿨다. 도형별 배치에서는 삼각형을 새 파일 하나로 추가했고, 이름표 연산을 추가할 때는 원과 사각형의 파일을 고쳤다. 연산별 배치에서는 반대로 삼각형을 추가할 때 그리기 파일을 고쳤고, 이름표 연산은 새 파일에 뒀다. 네 수정안이 모두 기능 검사를 통과했지만 기존 파일을 덜 건드리는 배치는 요구에 따라 달랐다(그림 1A).

두 번째 비교에서는 같은 배치 렌더링 함수를 추가했다. 이 함수는 도형 목록을 받아 각 렌더링 결과를 대괄호로 감싼다. 도형별 배치에서 변환을 각 도형 파일이 맡아야 하면 원과 사각형 파일을 고친다. 공용 어댑터를 허용하면 두 배치 모두 새 파일 하나로 기능을 제공할 수 있다고 예측했다. 실행한 네 후보는 모두 입력 순서와 중복을 보존하고 빈 목록과 미지원 도형을 명세대로 처리했다. 각 후보는 원과 사각형의 기존 렌더링을 유지했다. 기존 파일 두 개를 고친 것은 도형 파일이 변환을 맡은 후보뿐이었다. 네 후보 모두 새 파일 하나를 추가했다(그림 1B).

**그림 1. 기존 소스 파일 수정 수.** A는 삼각형 추가와 이름표 연산 추가를 비교한다. B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다. B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.

[PNG](https://drive.google.com/file/d/1uD_IpP77WJsKIWBngn72WEO9vp5JqzO1/view) · [SVG](https://drive.google.com/file/d/1swHCwTW3MNDv1mYE5-mCfsq73Iz1mnfZ/view) · [Batch prediction / 사전 예측](https://github.com/WhoSia/EvoNOMOS/commit/54d5af3f7ddcd4e74866b4b7f1b4ce188ed5aa7e) · [Batch fixture / 실행](https://github.com/WhoSia/EvoNOMOS/commit/d1ae74941da0539a8b8b8b330b9e6deb0e3aa83c) · [Figure source / 도판 코드](https://github.com/WhoSia/EvoNOMOS/commit/87f30604b8eca674030afa03a4798f277dfcc846)

세 번째 비교에서는 배치 함수 대신 기존 렌더링의 결과 하나를 선택적으로 감싸는 옵션을 사용했다. 새 모듈을 호출할 수 있는 경우에는 두 배치가 기존 파일을 그대로 뒀다. 같은 모듈을 추가한 상태에서 기존 함수에 `bracketed=True`를 넘기면 함수는 그 인자를 받지 못했다. 기존 함수로 옵션을 제공한 후보는 연산별 배치에서 파일 하나, 도형별 배치에서 두 개를 고쳤다. 기존 함수가 외부 변환 모듈을 불러올 수 있도록 이미 구성된 별도 기준선에서는 두 배치 모두 새 파일 하나를 추가해 기존 호출 경로로 옵션을 제공했다(표 3).

**표 3. 새 렌더링 옵션이 제공되는 호출 경로.**

| 새 기능을 받는 경로 | 연산별 배치 기존 파일 수정 | 도형별 배치 기존 파일 수정 | 각 배치의 새 파일 |
| --- | --- | --- | --- |
| 새 진입점 | 0 | 0 | 1 |
| 기존 진입점 | 1 | 2 | 0 |
| 확장 지점이 있는 기존 진입점 | 0 | 0 | 1 |

확장 지점은 세 번째 행의 기준선에 이미 있었다. 따라서 이 행의 0개를 첫 설계에서 확장 지점을 처음 만드는 비용까지 포함한 결과로 읽어서는 안 된다. 여기서는 확장 지점이 도입된 비용을 별도로 측정하지 않았다. 같은 어댑터를 추가해도 기존 함수에서는 옵션을 쓸 수 없었던 대조 실행을 포함했다.

[Prediction / 예측](https://github.com/WhoSia/EvoNOMOS/commit/76fa9222a7149b7c98a6315375834f2bd909fe0e) · [Execution / 실행](https://github.com/WhoSia/EvoNOMOS/commit/0ede7b241c8f9f50436be9703561bb9e7cc9fb8b)

기존 파일 수정 수가 적다는 사실만으로 변경에 더 잘 대응하는 설계라고 할 수는 없다. 새 파일을 추가할 수 있어도 그 파일이 실행되려면 호출자가 쓸 수 있는 경로가 필요하다. 표 3의 마지막 행은 확장 지점이 이미 있는 상태에서 이후에 고친 파일만 센다. 여기에 든 수정 수는 실행한 후보에 관한 관찰이다. 독립적으로 작성한 요구에서도 어떤 경로가 작동할지 예측할 수 있는지, 파일 수정 수가 실제 유지보수 부담과 어떻게 연결되는지는 남은 질문이다.

### 7. 결론

서론의 그리기 함수가 잘못됐는지는 정렬을 누가 맡았는지에 달려 있었다. 벤치마크는 모델의 응답을 참조 라벨과 대조해 분류 성능을 잰다. 그 판정을 구체적인 수정안에 적용하려면 어떤 기능이 필요한지, 어떤 동작을 기존 호출자에게 약속했는지를 확인해야 한다. 도서관 예제에서는 정오표 요구만으로 수정안을 거절할 수 있었다. 기술보고서만 필요한 경우에는 책 접두어 계약이 결론을 갈랐다.

어떤 수정안이 가능한지를 비교할 때는 호출자가 새 동작을 받을 수 있는 경로도 확인해야 한다. 검토 의견으로 변경을 요구하려면 어느 요구나 계약을 근거로 삼았는지, 어느 호출 경로에 적용되는지를 밝힐 수 있어야 한다. 그러면 개발자는 이미 내려진 결론의 근거를 확인하거나, 보류된 판정을 가를 사실을 더 찾을 수 있다. 이 결과는 한 벤치마크의 저장 자료와 여기서 구성해 실행한 후보의 범위에서 성립한다.

여기서 더 나아가려면 SOLID를 대체할 공리를 선언하기보다, 어떤 변경과 계약, 권한과 호출 경로가 주어졌을 때 설계의 유불리가 어떻게 달라지는지 예측할 수 있는 표현을 찾아야 한다. 그런 표현이 실제 독립 요구에서도 작동한다면, 익숙한 원칙이 유용한 이유뿐 아니라 그 조언을 따르지 않는 설계가 더 나은 조건도 설명할 수 있을 것이다. 이 가능성은 이번 논문의 결과가 아니라 다음에 검증할 가설로 남긴다.

### 부록 A · 재현 자료

§3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다. §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다. 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다. 그림 1의 소스와 출력 위치는 그림 캡션에 있다.

[재현 자료 및 명령 / Reproduction notes](https://github.com/WhoSia/EvoNOMOS/commit/ed443890f0b5f9b171d68d010b605e7cefec7f14)

## English manuscript

### 1. Introduction

In 1996, Robert Martin described a function that drew the shapes in a list in order. A triangle could be added without editing the function if the triangle supplied its own drawing operation. Martin then introduced a new requirement. Every circle had to be drawn before any square. Given a list that begins with a square, the same function still draws the square first.

Who is responsible for sorting the list? If the caller must pass a sorted list, the drawing function can stay as it is. If the function must produce the required order for any input list, the current code falls short. A reviewer can see that the function does no sorting. To take that fact as evidence of an open–closed principle (OCP) violation, the reviewer also needs to know who was meant to sort the shapes.

The difficulty is not simply whether the principle is sound. In Martin's example, a designer must first identify the changes against which a routine ought to remain closed. If that situated judgment is later used as a violation label without its premise, the label may carry the authority of a rule while omitting the reason for applying it. We call this risk the over-axiomatization of design advice. It is a question about how conditional advice is used, not a demonstrated history of the entire SOLID family.

The distinction becomes consequential when a violation label is treated as a reason to reject a particular edit. A classification benchmark can show which instructions and examples were presented to a model; it cannot by itself settle the obligations of a separate maintenance request. We inspect one such archive and then construct a fixed-patch comparison in which the new demand and the commitment to existing callers vary. We also examine the routes by which a new behavior reaches the original callers, since an edit that can be written in a new file is not necessarily available through their existing entry points.

[Martin 1996, Listing 2와 Strategic Closure](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=6) · [벤치마크 기록 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [동일 패치 비교](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md)

### 2. The open–closed principle in Meyer and Martin

Martin opens his 1996 article by attributing the principle to Bertrand Meyer and citing page 23 of the 1988 first edition. We examine this explicit citation link to recover the conditions under which OCP was argued for; it is not, by itself, a genealogy of all five SOLID principles. A closed module in Meyer’s account is one that other modules can use on the basis of a stable specification.

If a library program distinguishes publication types one by one, adding technical reports can require edits to existing modules or recompiling them. The designer must consider both where the new behavior can live and what existing users of the module can continue to rely on.

The principle was contested well before it became a mnemonic. In a June 1995 public exchange, Kyle Brown objected that developers need to edit badly designed classes. Martin distinguished a lack of permission to edit source from a design in which an anticipated extension does not <i>require</i> editing it; he also acknowledged the difficulty of anticipating change. [Contemporary exchange](https://groups.google.com/g/comp.lang.c%2B%2B/c/nntTK8eH_Ag/m/uvoJEnDH9zAJ)

Public records refer to the five-principle SOLID grouping by 2007, and a 2009 dispute distinguished routine internal interfaces from stable public plugin interfaces. The record documents debate across settings, not a proven causal history in which a mnemonic or a particular tool stripped the qualifications away. [2007 report](https://www.infoq.com/news/2007/01/principles-of-agile-design/) · [2009 exchange](https://www.joelonsoftware.com/2009/01/31/from-podcast-38/)

Martin assigned sorting to `DrawAllShapes`. In the first implementation, `Circle::Precedes` inspected the other shape and put the circle first if it was a square. The code that decided how a new shape would rank against a circle already lived in `Circle`. Martin then moved the order of shape types into a table. Putting squares first now requires swapping two entries. Ordering individual shapes by area, for example, would require information outside the table. Which part of the program can stay as it is depends on the change it must accommodate.

Whether a type check supports a violation finding also depends on the function’s obligation. Later in the article, Martin presents two further functions that use `dynamic_cast`. `DrawAllShapes` recognizes and draws circles and squares. `DrawSquaresOnly` selects squares from the list and draws them. Given a triangle, both skip it. A function that promises to draw every shape has omitted an output, while a function that promises to draw squares has met its obligation. We turn to saved classification prompts to see how much of that kind of obligation the reviewer could establish from the input.

Both functions contain type checks; their different obligations account for the different judgments. Before assessing whether the saved prompts convey comparable obligations, we describe how we distinguished the reference examples from the submissions and instructions archived for the models.

[Meyer 1988 초판 22–25쪽 대조 기록](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md) · [Martin 1996, 1쪽](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf#page=1) · [Martin 1996, Listings 3–6, 9–10](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf)

### 3. Materials and methods

To separate the obligations inferable from the inputs from the labels assigned by the benchmark, we distinguish three units in the archive. A reference pair contains a violation example and its revision. A saved response record contains the code submitted to the model, its prompt, and the recorded response. We recover a prompt template by replacing the single exact occurrence of the submitted code with a common placeholder. We compare templates as strings.

We compared each saved submission with the source on both sides of every reference pair, first as stored and again after trimming whitespace from both ends. For Python reference pairs we parsed the syntax trees and compared names of methods declared in top-level classes, excluding names that begin with an underscore. The comparison captures declaration changes. Inherited availability, actual client use, and whether that use was protected each require separate evidence.

We ran the library and drawing fixtures built for this study under the conditions given in Sections 5 and 6. We executed no code from the archived replication package. Appendix A identifies the archive and the commands needed to reproduce the checks.

[감사 코드](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/audit_are_we_solid.py) · [고정 인벤토리](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/are_we_solid_inventory.json)

### 4. What the benchmark gives the reviewer

Pehlivan et al. specified violation scenarios and refined and checked the generated examples. They resolved disagreements about reference labels through discussion, then compared model classifications of SOLID violations with those labels. The OCP archive contains 48 reference pairs and 768 saved response records. Masking the submitted code yielded 24 distinct template strings, with no exact template shared across the four strategies. None of the templates separately states a change request or a protected caller contract for an individual case. That absence is not a defect in a benchmark whose stated task is classification. It matters when the resulting label is asked to justify an engineering decision outside that task.

One saved Python `EXAMPLE` prompt points the reviewer to repeated branches where polymorphism would fit. The submitted `AreaCalculator` checks the shape type before calculating the area of a circle or rectangle. The branch suggests where an edit might go if a new shape is added. The instruction leaves open whether anyone has requested that change and whether existing calls that read a rectangle’s width must still be supported.

In a separate reference pair, number 37, the revision moves area calculation onto the shapes and drops the declaration of `Rectangle.get_width`.

No saved submission matched either side of the reference pairs in the exact or outer-whitespace-trimmed comparison. Our evidence for the missing declaration comes from comparing the reference sources. To argue that its removal warrants rejecting a patch, a reviewer would need to establish that callers were guaranteed access to the width. We do not infer that a real caller used the deleted getter. Instead, a separate executable fixture tests whether varying a protected commitment can change the verdict on a fixed edit.

Other research measures different aspects of this problem. Bräuer et al. (2018) asked experts which parts of design principles were and were not captured by measurable practices. Cabral et al. (2024) studied participants' understanding and perceived extension benefits in a concrete machine-learning scenario comparing bundled code treatments. Zhu et al. (2026) evaluated repository changes against functional tests and structural oracles. These instruments measure, respectively, **coverage of principles, reported perceptions, and conformance under specified tasks**. Our fixed-patch fixture instead asks whether an acceptance verdict is stable under explicitly varied demands and protected contracts. The distinction does not make the earlier instruments invalid; it identifies the decision for which each source supplies evidence. [Bräuer DOI](https://doi.org/10.1016/j.jss.2018.03.002) · [Cabral DOI](https://doi.org/10.1145/3644815.3644957) · [Zhu arXiv](https://arxiv.org/abs/2603.27745)

**Table 1. Evidence in the saved material and evidence needed to assess a patch.**

| Question | Evidence in the saved material | Evidence for a patch decision |
| --- | --- | --- |
| What counts as a correct answer? | The benchmark compares model responses with the violation labels verified by its authors. | The proposed edit and the criteria for acceptance. |
| Which behavior should be added? | The saved Python EXAMPLE prompt points to repeated branching where polymorphism would fit. The templates state no separate request for an individual case. | The actual request, its acceptance conditions, and the boundary responsible for it. |
| What do existing callers rely on? | The templates state no separate caller contract. The distinct reference pair 37 loses the width getter declaration. | The scope of the commitment and supporting API documentation, client code, tests, or agreement. |
| What may the implementation change? | The instructions ask for a violation category and an explanation. They do not specify protected implementation files or interfaces. | The protected artifacts and permitted changes, including whether a new module may be added. |

The saved prompt is on JSONL line 13 (record ID 12). Reference pair 37 is in a separate ground-truth JSON file. 768 counts saved records. [Archived material](https://drive.google.com/file/d/12LDcKFBpJRkwH-zYJZ6Uhk9pE3RzgnUe/view) · [Source comparison](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

[Pehlivan 등 §III](https://arxiv.org/html/2509.03093v1#S3) · [아카이브와 행 37의 감사](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) · [저장 입력과 참조본 대조 코드](https://github.com/WhoSia/EvoNOMOS/commit/f1b8e739de5a868a2526ed6256ba784c6e58ec53)

### 5. When the same patch warrants different decisions

Following Meyer’s example, we built a small library catalog. The proposed patch adds a module for technical reports. The two existing source files remain byte-for-byte identical. In execution, technical reports render and requests for errata are still rejected. The prefix in an existing book’s output changes from `book` to `BOOK`. The identity of the old source files therefore does not imply the preservation of every observable result; we verified the latter separately in our fixture.

We hold the patch, its observed behavior, and the boundary permitting new modules fixed. The new requirement covers either technical reports alone or both technical reports and errata. Both legacy contracts protect the rendering of journals and proceedings and require rejection of a separate unsupported type. The broader contract also protects the original book prefix. An acceptable candidate in Table 2 must meet both the new requirement and the applicable contract.

**Table 2. Two independent conditions for the same patch.**

| Request | Book prefix protected | Meets the request | Preserves the contract | Decision |
| --- | --- | --- | --- | --- |
| Technical reports | No | Yes | Yes | Accept |
| Technical reports | Yes | Yes | No | Reject |
| Technical reports and errata | No | No | Yes | Reject |
| Technical reports and errata | Yes | No | No | Reject |

The patch is acceptable when only technical reports are required and the book prefix is outside the contract. Knowing that errata are required suffices to reject it even before the prefix contract is known. If only technical reports are required, the verdict turns on whether callers were promised the original prefix. A separate patch adds one module within the same edit boundary, handles both new types, and preserves every protected observation.

With partial information, the reviewer can consider the specifications still compatible with the evidence. If all give the same verdict, the reviewer can issue it. If they disagree, the reviewer can give conditional verdicts or defer until the applicable specification can be established. This argument assumes that the actual specification is in the compatible set, so the set is nonempty. A rule that sees the same input and must always return a single binary verdict cannot be correct for two compatible specifications that require opposite answers. This establishes an information limit, not an error rate for SOLID judgments in practice. Appendix A gives the nine disclosure conditions for this case.

[네 조합의 재현](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md) · [정보 공개 조건별 결과](https://github.com/WhoSia/EvoNOMOS/blob/6e4232e4dd7d8c330c4d5631caf7f1215344f7d6/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/34_MAINTENANCE_JUDGMENT_UNDER_PARTIAL_DISCLOSURE.md)

### 6. Where a change can live and how callers reach it

Section 5 established whether one patch met a stated request and contract. It did not determine the least costly way to meet them. Returning to the drawing fixture, we ask which source boundaries the implemented candidates cross when the request, permitted placement, or caller route changes. The counts describe those candidates, not a minimum over all possible implementations.

We first varied the request. In the shape layout we added a triangle in one new file and edited the circle and square files to add a labeling operation. In the operation layout we edited the drawing file to add the triangle and put the labeling operation in a new file. All four candidates passed their functional checks. Which layout left more existing files intact depended on the request (Figure 1A).

We then added the same batch-rendering function to both layouts. It takes a list of shapes and brackets each rendered result. We predicted that requiring the item transformation to live in the shape files would entail editing both files in the shape layout. If a shared adapter was allowed, we predicted that either layout could add the feature in one new file. All four candidates preserved order and duplicates, handled empty lists and unsupported shapes as specified, and preserved the existing circle and square renderings. The candidate placing both transformations in the shape files edited two existing files. All four added one file (Figure 1B).

**Figure 1. Existing source files edited.** Panel A compares adding a triangle with adding a labeling operation. Panel B holds the batch-rendering request fixed and varies the placement rule. All four candidates in panel B passed the new and legacy behavior checks and added one file each.

[PNG](https://drive.google.com/file/d/1uD_IpP77WJsKIWBngn72WEO9vp5JqzO1/view) · [SVG](https://drive.google.com/file/d/1swHCwTW3MNDv1mYE5-mCfsq73Iz1mnfZ/view) · [Batch prediction / 사전 예측](https://github.com/WhoSia/EvoNOMOS/commit/54d5af3f7ddcd4e74866b4b7f1b4ce188ed5aa7e) · [Batch fixture / 실행](https://github.com/WhoSia/EvoNOMOS/commit/d1ae74941da0539a8b8b8b330b9e6deb0e3aa83c) · [Figure source / 도판 코드](https://github.com/WhoSia/EvoNOMOS/commit/87f30604b8eca674030afa03a4798f277dfcc846)

The third comparison used an option to bracket a single rendering through the existing function. Candidates that offered a new entry point left the existing files intact in both layouts. With the same adapter added, the original functions still rejected `bracketed=True`. The candidates offering the option through the original functions edited one file in the operation layout and two in the shape layout. In a separate baseline whose original function could already load an external decorator, each layout delivered the option through the original entry point by adding a single file (Table 3).

**Table 3. Call paths for the new rendering option.**

| Path that provides the feature | Existing files edited, operation layout | Existing files edited, shape layout | New files per layout |
| --- | --- | --- | --- |
| New entry point | 0 | 0 | 1 |
| Original entry point | 1 | 2 | 0 |
| Original entry point with a hook | 0 | 0 | 1 |

The hook was already present in the last row’s baseline. Its zero-edits result does not include the cost of introducing that hook into the earlier baseline. We did not measure that initial investment. The negative control adds the same adapter and finds that the option remains unavailable through the original function.

[Prediction / 예측](https://github.com/WhoSia/EvoNOMOS/commit/76fa9222a7149b7c98a6315375834f2bd909fe0e) · [Execution / 실행](https://github.com/WhoSia/EvoNOMOS/commit/0ede7b241c8f9f50436be9703561bb9e7cc9fb8b)

Fewer changed files do not by themselves establish a more maintainable design. Permission to add a file needs to be paired with a path that the caller can actually use. The last row of Table 3 starts counting after the hook is already in place. These file counts describe the tested candidates. Whether we can predict working paths for independently authored requests, and how these counts relate to maintenance effort, remain open.

### 7. Conclusion

Whether the drawing routine falls short depends on who must sort the list. The benchmark measures classification performance by comparing model responses with its reference labels. Applying a finding to a specific patch also requires knowing what change the patch must deliver and which behavior existing callers were promised. In the catalog example, the errata requirement can settle a rejection on its own. When only technical reports are needed, the verdict turns on the promise about the book prefix.

Comparing possible edits also requires knowing how the new behavior can reach its callers. A review that calls for an edit should identify the request or commitment it relies on and the call path to which it applies. The developer can then check the grounds for the verdict or identify the remaining fact that would settle it. The evidence here covers the saved material of one benchmark and the candidates we constructed and ran.

Rather than announce a new set of axioms, the next step is to ask whether changes, protected commitments, authority, and caller routes can be represented in a form that predicts when one design has an advantage over another. Such an account would be valuable if it explained both the usefulness of familiar principles and the conditions under which their preferred design loses. The present paper poses that hypothesis; it does not establish it.

### Appendix A · Reproduction

For Sections 3–4 the audit reads the archived JSON and JSONL. For Sections 5–6 the fixtures run the examples constructed for this study. The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.

[재현 자료 및 명령 / Reproduction notes](https://github.com/WhoSia/EvoNOMOS/commit/ed443890f0b5f9b171d68d010b605e7cefec7f14)
