# Paper B R19B — Sentence Diff Index, v07–v14
R19A's v07 repeated as baseline to preserve cross-batch continuity. Fuzzy nearest Jaccard of character trigrams; sentence splitting heuristic, not semantics, table content excluded. Every extracted prose sentence indexed. SAME >= .94; EDIT >= .48; else NEW.

## v07 · [Source](https://app.notion.com/p/41bef561cf9281cbaf29c9a9b5daba1e)
### ko (150 segmented sentences)
ko001 | BASE | — | 0.00 | 로버트 마틴은 1996년 글에서 도형 목록을 받아 차례로 그리는 함수를 예로 들었다.
ko002 | BASE | — | 0.00 | 삼각형이 자신을 그리는 동작을 제공하면, 그 함수를 고치지 않고도 삼각형을 추가할 수 있었다.
ko003 | BASE | — | 0.00 | 같은 함수에 사각형으로 시작하는 목록을 주면 여전히 사각형부터 그린다.
ko004 | BASE | — | 0.00 | 원을 먼저 그리려면 누가 목록을 정렬해야 할까?
ko005 | BASE | — | 0.00 | 호출자가 정렬한 목록을 넘기기로 했다면 그리기 함수는 그대로 둘 수 있다.
ko006 | BASE | — | 0.00 | 어떤 목록을 받아도 함수가 순서를 보장하기로 했다면 지금 코드로는 부족하다.
ko007 | BASE | — | 0.00 | 소스 코드를 읽으면 함수가 정렬하지 않는다는 사실을 알 수 있다.
ko008 | BASE | — | 0.00 | 그 사실을 개방–폐쇄 원칙(OCP) 위반의 근거로 삼으려면 정렬을 누가 맡았는지도 알아야 한다.
ko009 | BASE | — | 0.00 | 여기에는 설계 원칙 자체보다 그 원칙을 사용하는 방식에 관한 문제가 있다.
ko010 | BASE | — | 0.00 | 마틴의 사례에서는 앞으로 어떤 변화에 대비할지를 정해야 비로소 어떤 코드를 닫아 둘지 논의할 수 있었다.
ko011 | BASE | — | 0.00 | 그 판단을 변경 요구가 빠진 ‘위반’ 판정으로 바꿔 사용한다면, 처음에는 결론을 정당화했던 전제가 사라진다.
ko012 | BASE | — | 0.00 | 우리는 이 위험을 원칙의 ‘과도한 공리화’라고 부른다.
ko013 | BASE | — | 0.00 | 이것은 SOLID 전체가 무효하다는 역사적 결론이 아니라, 조건부 설계 조언을 무조건적인 탈락 기준처럼 적용할 때 무엇을 잃는지 묻는 문제 제기다.
ko014 | BASE | — | 0.00 | 이 문제를 따지려면 ‘위반’이라고 분류하는 일과 특정 수정안을 거절하는 일을 먼저 나눠야 한다.
ko015 | BASE | — | 0.00 | SOLID 위반 분류 벤치마크의 저장 자료는 모델이 어떤 근거를 받았는지 보여 주지만, 특정 유지보수 요청이 승인되어야 하는지까지 판정하지는 않는다.
ko016 | BASE | — | 0.00 | 우리는 별도로 만든 도서관 프로그램에서 같은 수정안을 서로 다른 요구와 기존 호출자 계약 아래 두어 그 간격을 검사한다.
ko017 | BASE | — | 0.00 | 수정안 자체의 수용 여부를 따진 다음에는, 새로운 기능이 실제 호출 경로에 도달하도록 만드는 일이 어느 기존 파일을 바꾸게 하는지도 비교한다.
ko018 | BASE | — | 0.00 | · · 마틴은 1996년 글의 첫머리에서 이 원칙을 베르트랑 마이어에게서 가져왔다고 밝히며 1988년 초판 23쪽을 인용한다.
ko019 | BASE | — | 0.00 | 이어지는 두 사례를 다루는 이유는 SOLID 다섯 원칙의 기원을 한 줄로 연결하기 위해서가 아니라, OCP에 적용 조건이 명시되어 있었는지 살피기 위해서다.
ko020 | BASE | — | 0.00 | 마이어의 설명에서 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 사용할 수 있는 모듈이다.
ko021 | BASE | — | 0.00 | 도서관 프로그램이 자료의 종류를 하나씩 구별해 처리한다면 기술보고서 한 종류를 추가하는 데도 기존 모듈의 수정이나 재컴파일이 필요할 수 있다.
ko022 | BASE | — | 0.00 | 이때 설계자는 새 동작을 어디에 넣을지와 기존 사용자가 계속 어떤 동작에 의존할 수 있을지를 함께 고려하게 된다.
ko023 | BASE | — | 0.00 | 1995년 6월 공개 토론에서 Kyle Brown은 잘못 설계된 클래스라면 개발자가 소스를 고쳐야 한다고 반박했다.
ko024 | BASE | — | 0.00 | 마틴은 ‘닫혀 있다’는 말을 수정할 권한이 없다는 뜻이 아니라, 예상한 확장을 위해 기존 코드를 반드시 수정할 필요가 없다는 뜻으로 구분했다.
ko025 | BASE | — | 0.00 | 그는 어떤 변경이 생길지 미리 알아야 한다는 어려움도 인정했다.
ko026 | BASE | — | 0.00 | 이 논쟁은 OCP가 처음부터 단 하나의 무조건적 금지 명령으로 받아들여졌다고 가정하기 어렵게 한다.
ko027 | BASE | — | 0.00 | 2007년에는 다섯 원칙을 묶은 SOLID라는 명칭이 공개 기록에 나타나고, 2009년의 인터페이스 논쟁에서는 내부 클래스와 공개 플러그인 API가 서로 다른 판단을 요구했다.
ko028 | BASE | — | 0.00 | 이런 자료로 원칙의 전파와 수용 과정에 논쟁이 있었다는 점은 말할 수 있지만, 특정 약어나 자동화 도구가 조건을 탈락시켰다는 인과관계까지 증명할 수는 없다.
ko029 | BASE | — | 0.00 | · 마틴은 목록을 정렬하는 일을 DrawAllShapes 에 맡겼다.
ko030 | BASE | — | 0.00 | 첫 구현에서는 Circle::Precedes 가 상대 도형을 검사해 사각형이면 원을 앞에 놓았다.
ko031 | BASE | — | 0.00 | 새 도형이 들어왔을 때 원과 그 도형의 순서를 정하는 코드가 이미 Circle 안에 있었다.
ko032 | BASE | — | 0.00 | 마틴은 이어서 도형 종류별 순서를 표로 옮겼다.
ko033 | BASE | — | 0.00 | 이제 사각형을 원보다 먼저 그리라는 요청에는 표에서 두 항목의 위치를 바꾸면 된다.
ko034 | BASE | — | 0.00 | 개별 도형의 넓이순으로 그리라는 요구를 가정하면 표에 없는 정보가 필요하다.
ko035 | BASE | — | 0.00 | 어느 부분을 그대로 둘 수 있는지는 어떤 변경에 대비하느냐에 달려 있다.
ko036 | BASE | — | 0.00 | 타입 검사가 위반의 근거가 되는지도 함수가 맡은 일에 달려 있다.
ko037 | BASE | — | 0.00 | 글의 뒷부분에서 마틴은 dynamic_cast 를 쓰는 두 함수를 새로 제시한다.
ko038 | BASE | — | 0.00 | 원과 사각형을 가려 그리는 DrawAllShapes 와 목록에서 사각형만 골라 그리는 DrawSquaresOnly 다.
ko039 | BASE | — | 0.00 | 두 함수에 삼각형을 넣으면 어느 쪽도 그리지 않는다.
ko040 | BASE | — | 0.00 | 모든 도형을 그리기로 한 함수에서는 빠진 출력이고, 사각형만 그리기로 한 함수에서는 약속한 동작이다.
ko041 | BASE | — | 0.00 | 검토자가 어떤 근거로 두 경우를 구별할 수 있는지를 확인하려면, 실제로 받았던 코드와 지시를 구분해 살펴봐야 한다.
ko042 | BASE | — | 0.00 | 두 함수는 같은 구문을 사용하지만, 약속한 일이 달라 평가가 갈린다.
ko043 | BASE | — | 0.00 | 이 사례를 위반 여부의 판단으로 옮기려면 검토에 주어진 코드와 그 코드가 맡은 책임을 나눠야 한다.
ko044 | BASE | — | 0.00 | 우리는 먼저 자료를 어떤 단위로 읽었는지 밝힌 뒤, 저장된 분류 프롬프트에서 그 책임을 어디까지 확인할 수 있는지 살펴본다.
ko045 | BASE | — | 0.00 | · · 이 질문을 저장 자료에 적용하기 위해 분석 단위를 세 가지로 나눴다.
ko046 | BASE | — | 0.00 | 참조 코드 쌍에는 위반 예시와 그 수정 예시가 들어 있고, 저장 응답에는 모델에 제출된 코드와 프롬프트, 기록된 응답이 들어 있다.
ko047 | BASE | — | 0.00 | 프롬프트 틀은 저장 프롬프트에 정확히 한 번 나오는 제출 코드를 공통 자리표시자로 치환해 얻었다.
ko048 | BASE | — | 0.00 | 저장 응답의 제출 코드를 모든 참조 쌍의 수정 전·후 소스와 대조했다.
ko049 | BASE | — | 0.00 | 각 문자열을 그대로 비교한 뒤 양끝 공백을 제거해 다시 비교했다.
ko050 | BASE | — | 0.00 | Python 참조 쌍은 구문 트리로 파싱해 최상위 클래스의 메서드 선언 이름을 비교했다.
ko051 | BASE | — | 0.00 | 상속에 따른 호출 가능성, 실제 사용 여부, 보장의 범위는 별도 근거가 필요한 질문이다.
ko052 | BASE | — | 0.00 | 이 연구에서 작성한 도서관·도형 재현은 §5와 §6에서 정한 조건으로 실행했다.
ko053 | BASE | — | 0.00 | ZIP 안의 공개 재현 패키지 코드는 실행하지 않았다.
ko054 | BASE | — | 0.00 | 아카이브 식별 정보와 확인 명령은 부록 A에 있다.
ko055 | BASE | — | 0.00 | · Pehlivan 등은 위반 시나리오를 정하고, 생성한 코드 예시를 수정·검증한 뒤 의견이 갈린 사례의 참조 라벨을 논의로 정했다.
ko056 | BASE | — | 0.00 | SOLID 위반을 식별하는 모델 응답은 그 라벨과 대조했다.
ko057 | BASE | — | 0.00 | OCP에 해당하는 아카이브에는 참조 쌍 48개와 저장 응답 768건이 있다.
ko058 | BASE | — | 0.00 | 저장 프롬프트에서 제출 코드를 가렸을 때 서로 다른 문자열 24개가 남았고, 네 전략 사이에 동일한 틀은 없었다.
ko059 | BASE | — | 0.00 | 각 사례의 변경 요구나 기존 호출자 계약을 따로 밝힌 틀은 없었다.
ko060 | BASE | — | 0.00 | 이는 벤치마크가 본래 수행하려는 분류 과제를 잘못 설계했다는 뜻이 아니다.
ko061 | BASE | — | 0.00 | 특정 수정안을 승인하거나 거절하는 데 이 분류 결과를 사용하려면 추가 증거가 필요하다는 뜻이다.
ko062 | BASE | — | 0.00 | 저장된 Python EXAMPLE 지시는 다형성으로 처리할 만한 반복 분기를 찾도록 한다.
ko063 | BASE | — | 0.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko064 | BASE | — | 0.00 | 그 분기를 보면 새 도형을 추가할 때 어디에 손댈지 짐작할 수 있다.
ko065 | BASE | — | 0.00 | 새 도형 추가가 실제 요청인지, 사각형의 너비를 직접 읽는 호출을 계속 지원해야 하는지는 이 지시문에서 확인되지 않는다.
ko066 | BASE | — | 0.00 | 별도의 참조 쌍 37번은 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko067 | BASE | — | 0.00 | 원본 문자열과 양끝 공백을 제거한 문자열을 대조했을 때, 저장된 제출 코드와 참조 쌍의 어느 쪽도 일치하지 않았다.
ko068 | BASE | — | 0.00 | 따라서 여기서 근거로 삼는 것은 참조 쌍에서 확인한 선언의 변화다.
ko069 | BASE | — | 0.00 | 그 변화가 수정안을 거절할 이유가 되려면 호출자가 너비를 읽는 동작까지 보장받았는지 확인해야 한다.
ko070 | BASE | — | 0.00 | 이 참조 쌍에 실제 호출자가 있었다고 주장하지는 않는다.
ko071 | BASE | — | 0.00 | 대신 해당 문제가 판정에 영향을 줄 수 있는지 별도로 구성한 수정안에서 시험한다.
ko072 | BASE | — | 0.00 | 이 사례가 분류 평가를 대표하는 유일한 방식은 아니다.
ko073 | BASE | — | 0.00 | Bräuer 등(2018)은 설계 원칙을 측정 가능한 실천 규칙으로 옮길 때 전문가들이 보기에 무엇이 포착되고 무엇이 빠지는지 물었다.
ko074 | BASE | — | 0.00 | Cabral 등(2024)은 구체적인 기계학습 확장 상황에서 SOLID 적용 전후 코드에 대한 참가자의 이해도와 확장 용이성 인식을 조사했다.
ko075 | BASE | — | 0.00 | Zhu 등(2026)은 저장소 변경 요구에 기능 테스트와 구조적 판정 기준을 결합했다.
ko076 | BASE | — | 0.00 | 세 연구는 각각 원칙의 측정 범위, 사용자의 인식, 특정 변경에서의 기능·구조 적합성 을 관찰한다.
ko077 | BASE | — | 0.00 | 우리 비교의 결과 변수는 같은 패치가 명시된 요구와 계약 아래에서 승인 기준을 충족하는가다.
ko078 | BASE | — | 0.00 | 앞선 연구를 코드 판정의 실패 사례로 취급하지 않으면서도, 무엇을 측정해야 어떤 결정을 정당화할 수 있는지 서로 다른 관점에서 확인할 수 있다.
ko079 | BASE | — | 0.00 | 프롬프트 예시는 저장 JSONL 13행(ID 12)이다.
ko080 | BASE | — | 0.00 | 참조 쌍 37번은 별도의 ground truth JSON 위치다.
ko081 | BASE | — | 0.00 | · · · 마이어의 예를 바탕으로 작은 도서관 목록 프로그램을 만들었다.
ko082 | BASE | — | 0.00 | 검토할 수정안은 기술보고서를 처리하는 모듈을 추가한다.
ko083 | BASE | — | 0.00 | 기존 소스 파일 두 개는 바이트 단위로 그대로다.
ko084 | BASE | — | 0.00 | 실행하면 기술보고서는 출력되고 정오표는 여전히 거절된다.
ko085 | BASE | — | 0.00 | 기존 책 출력의 접두어는 book 에서 BOOK 으로 바뀐다.
ko086 | BASE | — | 0.00 | 기존 파일을 수정하지 않았다는 사실은 기존 호출 결과까지 보존했다는 뜻이 아니다.
ko087 | BASE | — | 0.00 | 변경된 동작은 우리가 만든 실행 예제에서 관찰했다.
ko088 | BASE | — | 0.00 | 수정안과 실행 결과, 새 모듈을 추가할 수 있는 편집 범위를 고정했다.
ko089 | BASE | — | 0.00 | 새 요구는 기술보고서만 지원하는 경우와 정오표까지 지원하는 경우로 나눴다.
ko090 | BASE | — | 0.00 | 두 계약은 모두 학술지와 학회록의 출력, 그리고 별개의 미지원 자료 유형을 거절하는 동작을 보호한다.
ko091 | BASE | — | 0.00 | 표 2의 승인은 새 요구와 보호할 계약을 모두 충족한 경우다.
ko092 | BASE | — | 0.00 | 기술보고서만 필요하고 책 접두어를 보호하지 않는 경우에 승인된다.
ko093 | BASE | — | 0.00 | 정오표가 필수라는 사실을 알면 책 접두어 계약을 모르더라도 거절할 수 있다.
ko094 | BASE | — | 0.00 | 기술보고서만 필요하다는 사실을 알 때는 책 접두어를 보장했는지가 결론을 가른다.
ko095 | BASE | — | 0.00 | 별도로 만든 수정안은 같은 편집 범위에서 새 모듈 하나를 추가해 두 자료 유형을 처리하고 모든 보호 동작을 지켰다.
ko096 | BASE | — | 0.00 | 판정에 필요한 정보가 일부만 주어지면, 그 정보와 양립하는 명세들을 비교할 수 있다.
ko097 | BASE | — | 0.00 | 모든 명세가 같은 판정을 내리면 그 판정을 내릴 수 있다.
ko098 | BASE | — | 0.00 | 서로 다른 판정이 나오면 조건마다 결론을 밝히거나, 어느 조건이 실제로 적용되는지 확인할 때까지 보류할 수 있다.
ko099 | BASE | — | 0.00 | 이 논증은 실제 명세가 검토 중인 집합에 들어 있어 그 집합이 비어 있지 않다는 전제에서 성립한다.
ko100 | BASE | — | 0.00 | 이때 한 가지 입력만 받아 언제나 승인 또는 거절 중 하나를 출력하는 규칙은, 서로 다른 정답이 남아 있는 두 조건을 동시에 맞힐 수 없다.
ko101 | BASE | — | 0.00 | 다만 이 논증만으로 SOLID의 다른 정리나 실제 현장의 판단 오류율을 추정할 수는 없다.
ko102 | BASE | — | 0.00 | 부록 A에는 이번 사례에서 검토한 정보 공개 조건 아홉 개가 있다.
ko103 | BASE | — | 0.00 | · 도서관 실험에서 확인한 것은 주어진 수정안의 적격성이었다.
ko104 | BASE | — | 0.00 | 다른 수정안이 더 적은 비용으로 같은 요구를 처리할 수 있는지는 아직 별도 문제다.
ko105 | BASE | — | 0.00 | 도형 예제로 돌아가, 어떤 변경에 대비할지와 새 기능을 어디에서 호출할지에 따라 기존 파일을 얼마나 수정하는지 비교한다.
ko106 | BASE | — | 0.00 | 여기서 세는 것은 실행한 후보들의 수정 파일 수이지 가능한 구현 전체의 최솟값이 아니다.
ko107 | BASE | — | 0.00 | 도형별 배치에서는 삼각형을 새 파일 하나로 추가했고, 이름표 연산을 추가할 때는 원과 사각형의 파일을 고쳤다.
ko108 | BASE | — | 0.00 | 연산별 배치에서는 반대로 삼각형을 추가할 때 그리기 파일을 고쳤고, 이름표 연산은 새 파일에 뒀다.
ko109 | BASE | — | 0.00 | 네 수정안이 모두 기능 검사를 통과했지만 기존 파일을 덜 건드리는 배치는 요구에 따라 달랐다(그림 1A).
ko110 | BASE | — | 0.00 | 두 번째 비교에서는 같은 배치 렌더링 함수를 추가했다.
ko111 | BASE | — | 0.00 | 이 함수는 도형 목록을 받아 각 렌더링 결과를 대괄호로 감싼다.
ko112 | BASE | — | 0.00 | 도형별 배치에서 변환을 각 도형 파일이 맡아야 하면 원과 사각형 파일을 고친다.
ko113 | BASE | — | 0.00 | 공용 어댑터를 허용하면 두 배치 모두 새 파일 하나로 기능을 제공할 수 있다고 예측했다.
ko114 | BASE | — | 0.00 | 실행한 네 후보는 모두 입력 순서와 중복을 보존하고 빈 목록과 미지원 도형을 명세대로 처리했다.
ko115 | BASE | — | 0.00 | 각 후보는 원과 사각형의 기존 렌더링을 유지했다.
ko116 | BASE | — | 0.00 | 기존 파일 두 개를 고친 것은 도형 파일이 변환을 맡은 후보뿐이었다.
ko117 | BASE | — | 0.00 | 네 후보 모두 새 파일 하나를 추가했다(그림 1B).
ko118 | BASE | — | 0.00 | A는 삼각형 추가와 이름표 연산 추가를 비교한다.
ko119 | BASE | — | 0.00 | B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다.
ko120 | BASE | — | 0.00 | B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.
ko121 | BASE | — | 0.00 | · · · · 세 번째 비교에서는 배치 함수 대신 기존 렌더링의 결과 하나를 선택적으로 감싸는 옵션을 사용했다.
ko122 | BASE | — | 0.00 | 새 모듈을 호출할 수 있는 경우에는 두 배치가 기존 파일을 그대로 뒀다.
ko123 | BASE | — | 0.00 | 같은 모듈을 추가한 상태에서 기존 함수에 bracketed=True 를 넘기면 함수는 그 인자를 받지 못했다.
ko124 | BASE | — | 0.00 | 기존 함수로 옵션을 제공한 후보는 연산별 배치에서 파일 하나, 도형별 배치에서 두 개를 고쳤다.
ko125 | BASE | — | 0.00 | 기존 함수가 외부 변환 모듈을 불러올 수 있도록 이미 구성된 별도 기준선에서는 두 배치 모두 새 파일 하나를 추가해 기존 호출 경로로 옵션을 제공했다(표 3).
ko126 | BASE | — | 0.00 | 확장 지점은 세 번째 행의 기준선에 이미 있었다.
ko127 | BASE | — | 0.00 | 따라서 이 행의 0개를 첫 설계에서 확장 지점을 처음 만드는 비용까지 포함한 결과로 읽어서는 안 된다.
ko128 | BASE | — | 0.00 | 여기서는 확장 지점이 도입된 비용을 별도로 측정하지 않았다.
ko129 | BASE | — | 0.00 | 같은 어댑터를 추가해도 기존 함수에서는 옵션을 쓸 수 없었던 대조 실행을 포함했다.
ko130 | BASE | — | 0.00 | · 기존 파일 수정 수가 적다는 사실만으로 변경에 더 잘 대응하는 설계라고 할 수는 없다.
ko131 | BASE | — | 0.00 | 새 파일을 추가할 수 있어도 그 파일이 실행되려면 호출자가 쓸 수 있는 경로가 필요하다.
ko132 | BASE | — | 0.00 | 표 3의 마지막 행은 확장 지점이 이미 있는 상태에서 이후에 고친 파일만 센다.
ko133 | BASE | — | 0.00 | 여기에 든 수정 수는 실행한 후보에 관한 관찰이다.
ko134 | BASE | — | 0.00 | 독립적으로 작성한 요구에서도 어떤 경로가 작동할지 예측할 수 있는지, 파일 수정 수가 실제 유지보수 부담과 어떻게 연결되는지는 남은 질문이다.
ko135 | BASE | — | 0.00 | 서론의 그리기 함수가 잘못됐는지는 정렬을 누가 맡았는지에 달려 있었다.
ko136 | BASE | — | 0.00 | 벤치마크는 모델의 응답을 참조 라벨과 대조해 분류 성능을 잰다.
ko137 | BASE | — | 0.00 | 그 판정을 구체적인 수정안에 적용하려면 어떤 기능이 필요한지, 어떤 동작을 기존 호출자에게 약속했는지를 확인해야 한다.
ko138 | BASE | — | 0.00 | 도서관 예제에서는 정오표 요구만으로 수정안을 거절할 수 있었다.
ko139 | BASE | — | 0.00 | 기술보고서만 필요한 경우에는 책 접두어 계약이 결론을 갈랐다.
ko140 | BASE | — | 0.00 | 어떤 수정안이 가능한지를 비교할 때는 호출자가 새 동작을 받을 수 있는 경로도 확인해야 한다.
ko141 | BASE | — | 0.00 | 검토 의견으로 변경을 요구하려면 어느 요구나 계약을 근거로 삼았는지, 어느 호출 경로에 적용되는지를 밝힐 수 있어야 한다.
ko142 | BASE | — | 0.00 | 그러면 개발자는 이미 내려진 결론의 근거를 확인하거나, 보류된 판정을 가를 사실을 더 찾을 수 있다.
ko143 | BASE | — | 0.00 | 이 결과는 한 벤치마크의 저장 자료와 여기서 구성해 실행한 후보의 범위에서 성립한다.
ko144 | BASE | — | 0.00 | 여기서 더 나아가려면 SOLID를 대체할 공리를 선언하기보다, 어떤 변경과 계약, 권한과 호출 경로가 주어졌을 때 설계의 유불리가 어떻게 달라지는지 예측할 수 있는 표현을 찾아야 한다.
ko145 | BASE | — | 0.00 | 그런 표현이 실제 독립 요구에서도 작동한다면, 익숙한 원칙이 유용한 이유뿐 아니라 그 조언을 따르지 않는 설계가 더 나은 조건도 설명할 수 있을 것이다.
ko146 | BASE | — | 0.00 | 이 가능성은 이번 논문의 결과가 아니라 다음에 검증할 가설로 남긴다.
ko147 | BASE | — | 0.00 | §3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다.
ko148 | BASE | — | 0.00 | §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다.
ko149 | BASE | — | 0.00 | 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다.
ko150 | BASE | — | 0.00 | 그림 1의 소스와 출력 위치는 그림 캡션에 있다.
Summary ko: SAME 0, EDIT 0, NEW 0

### en (157 segmented sentences)
en001 | BASE | — | 0.00 | In 1996, Robert Martin described a function that drew the shapes in a list in order.
en002 | BASE | — | 0.00 | A triangle could be added without editing the function if the triangle supplied its own drawing operation.
en003 | BASE | — | 0.00 | Martin then introduced a new requirement.
en004 | BASE | — | 0.00 | Every circle had to be drawn before any square.
en005 | BASE | — | 0.00 | Given a list that begins with a square, the same function still draws the square first.
en006 | BASE | — | 0.00 | Who is responsible for sorting the list?
en007 | BASE | — | 0.00 | If the caller must pass a sorted list, the drawing function can stay as it is.
en008 | BASE | — | 0.00 | If the function must produce the required order for any input list, the current code falls short.
en009 | BASE | — | 0.00 | A reviewer can see that the function does no sorting.
en010 | BASE | — | 0.00 | To take that fact as evidence of an open–closed principle (OCP) violation, the reviewer also needs to know who was meant to sort the shapes.
en011 | BASE | — | 0.00 | The difficulty is not simply whether the principle is sound.
en012 | BASE | — | 0.00 | In Martin's example, a designer must first identify the changes against which a routine ought to remain closed.
en013 | BASE | — | 0.00 | If that situated judgment is later used as a violation label without its premise, the label may carry the authority of a rule while omitting the reason for applying it.
en014 | BASE | — | 0.00 | We call this risk the over-axiomatization of design advice.
en015 | BASE | — | 0.00 | It is a question about how conditional advice is used, not a demonstrated history of the entire SOLID family.
en016 | BASE | — | 0.00 | The distinction becomes consequential when a violation label is treated as a reason to reject a particular edit.
en017 | BASE | — | 0.00 | A classification benchmark can show which instructions and examples were presented to a model; it cannot by itself settle the obligations of a separate maintenance request.
en018 | BASE | — | 0.00 | We inspect one such archive and then construct a fixed-patch comparison in which the new demand and the commitment to existing callers vary.
en019 | BASE | — | 0.00 | We also examine the routes by which a new behavior reaches the original callers, since an edit that can be written in a new file is not necessarily available through their existing entry points.
en020 | BASE | — | 0.00 | · · Martin opens his 1996 article by attributing the principle to Bertrand Meyer and citing page 23 of the 1988 first edition.
en021 | BASE | — | 0.00 | We examine this explicit citation link to recover the conditions under which OCP was argued for; it is not, by itself, a genealogy of all five SOLID principles.
en022 | BASE | — | 0.00 | A closed module in Meyer’s account is one that other modules can use on the basis of a stable specification.
en023 | BASE | — | 0.00 | If a library program distinguishes publication types one by one, adding technical reports can require edits to existing modules or recompiling them.
en024 | BASE | — | 0.00 | The designer must consider both where the new behavior can live and what existing users of the module can continue to rely on.
en025 | BASE | — | 0.00 | The principle was contested well before it became a mnemonic.
en026 | BASE | — | 0.00 | In a June 1995 public exchange, Kyle Brown objected that developers need to edit badly designed classes.
en027 | BASE | — | 0.00 | Martin distinguished a lack of permission to edit source from a design in which an anticipated extension does not require editing it; he also acknowledged the difficulty of anticipating change.
en028 | BASE | — | 0.00 | Public records refer to the five-principle SOLID grouping by 2007, and a 2009 dispute distinguished routine internal interfaces from stable public plugin interfaces.
en029 | BASE | — | 0.00 | The record documents debate across settings, not a proven causal history in which a mnemonic or a particular tool stripped the qualifications away.
en030 | BASE | — | 0.00 | · Martin assigned sorting to DrawAllShapes .
en031 | BASE | — | 0.00 | In the first implementation, Circle::Precedes inspected the other shape and put the circle first if it was a square.
en032 | BASE | — | 0.00 | The code that decided how a new shape would rank against a circle already lived in Circle .
en033 | BASE | — | 0.00 | Martin then moved the order of shape types into a table.
en034 | BASE | — | 0.00 | Putting squares first now requires swapping two entries.
en035 | BASE | — | 0.00 | Ordering individual shapes by area, for example, would require information outside the table.
en036 | BASE | — | 0.00 | Which part of the program can stay as it is depends on the change it must accommodate.
en037 | BASE | — | 0.00 | Whether a type check supports a violation finding also depends on the function’s obligation.
en038 | BASE | — | 0.00 | Later in the article, Martin presents two further functions that use dynamic_cast .
en039 | BASE | — | 0.00 | DrawAllShapes recognizes and draws circles and squares.
en040 | BASE | — | 0.00 | DrawSquaresOnly selects squares from the list and draws them.
en041 | BASE | — | 0.00 | Given a triangle, both skip it.
en042 | BASE | — | 0.00 | A function that promises to draw every shape has omitted an output, while a function that promises to draw squares has met its obligation.
en043 | BASE | — | 0.00 | We turn to saved classification prompts to see how much of that kind of obligation the reviewer could establish from the input.
en044 | BASE | — | 0.00 | Both functions contain type checks; their different obligations account for the different judgments.
en045 | BASE | — | 0.00 | Before assessing whether the saved prompts convey comparable obligations, we describe how we distinguished the reference examples from the submissions and instructions archived for the models.
en046 | BASE | — | 0.00 | · · To separate the obligations inferable from the inputs from the labels assigned by the benchmark, we distinguish three units in the archive.
en047 | BASE | — | 0.00 | A reference pair contains a violation example and its revision.
en048 | BASE | — | 0.00 | A saved response record contains the code submitted to the model, its prompt, and the recorded response.
en049 | BASE | — | 0.00 | We recover a prompt template by replacing the single exact occurrence of the submitted code with a common placeholder.
en050 | BASE | — | 0.00 | We compare templates as strings.
en051 | BASE | — | 0.00 | We compared each saved submission with the source on both sides of every reference pair, first as stored and again after trimming whitespace from both ends.
en052 | BASE | — | 0.00 | For Python reference pairs we parsed the syntax trees and compared names of methods declared in top-level classes, excluding names that begin with an underscore.
en053 | BASE | — | 0.00 | The comparison captures declaration changes.
en054 | BASE | — | 0.00 | Inherited availability, actual client use, and whether that use was protected each require separate evidence.
en055 | BASE | — | 0.00 | We ran the library and drawing fixtures built for this study under the conditions given in Sections 5 and 6.
en056 | BASE | — | 0.00 | We executed no code from the archived replication package.
en057 | BASE | — | 0.00 | Appendix A identifies the archive and the commands needed to reproduce the checks.
en058 | BASE | — | 0.00 | · Pehlivan et al. specified violation scenarios and refined and checked the generated examples.
en059 | BASE | — | 0.00 | They resolved disagreements about reference labels through discussion, then compared model classifications of SOLID violations with those labels.
en060 | BASE | — | 0.00 | The OCP archive contains 48 reference pairs and 768 saved response records.
en061 | BASE | — | 0.00 | Masking the submitted code yielded 24 distinct template strings, with no exact template shared across the four strategies.
en062 | BASE | — | 0.00 | None of the templates separately states a change request or a protected caller contract for an individual case.
en063 | BASE | — | 0.00 | That absence is not a defect in a benchmark whose stated task is classification.
en064 | BASE | — | 0.00 | It matters when the resulting label is asked to justify an engineering decision outside that task.
en065 | BASE | — | 0.00 | One saved Python EXAMPLE prompt points the reviewer to repeated branches where polymorphism would fit.
en066 | BASE | — | 0.00 | The submitted AreaCalculator checks the shape type before calculating the area of a circle or rectangle.
en067 | BASE | — | 0.00 | The branch suggests where an edit might go if a new shape is added.
en068 | BASE | — | 0.00 | The instruction leaves open whether anyone has requested that change and whether existing calls that read a rectangle’s width must still be supported.
en069 | BASE | — | 0.00 | In a separate reference pair, number 37, the revision moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en070 | BASE | — | 0.00 | No saved submission matched either side of the reference pairs in the exact or outer-whitespace-trimmed comparison.
en071 | BASE | — | 0.00 | Our evidence for the missing declaration comes from comparing the reference sources.
en072 | BASE | — | 0.00 | To argue that its removal warrants rejecting a patch, a reviewer would need to establish that callers were guaranteed access to the width.
en073 | BASE | — | 0.00 | We do not infer that a real caller used the deleted getter.
en074 | BASE | — | 0.00 | Instead, a separate executable fixture tests whether varying a protected commitment can change the verdict on a fixed edit.
en075 | BASE | — | 0.00 | Other research measures different aspects of this problem.
en076 | BASE | — | 0.00 | Bräuer et al. (2018) asked experts which parts of design principles were and were not captured by measurable practices.
en077 | BASE | — | 0.00 | Cabral et al. (2024) studied participants' understanding and perceived extension benefits in a concrete machine-learning scenario comparing bundled code treatments.
en078 | BASE | — | 0.00 | Zhu et al. (2026) evaluated repository changes against functional tests and structural oracles.
en079 | BASE | — | 0.00 | These instruments measure, respectively, coverage of principles, reported perceptions, and conformance under specified tasks .
en080 | BASE | — | 0.00 | Our fixed-patch fixture instead asks whether an acceptance verdict is stable under explicitly varied demands and protected contracts.
en081 | BASE | — | 0.00 | The distinction does not make the earlier instruments invalid; it identifies the decision for which each source supplies evidence.
en082 | BASE | — | 0.00 | Evidence in the saved material and evidence needed to assess a patch.
en083 | BASE | — | 0.00 | The saved prompt is on JSONL line 13 (record ID 12).
en084 | BASE | — | 0.00 | Reference pair 37 is in a separate ground-truth JSON file. 768 counts saved records.
en085 | BASE | — | 0.00 | · · · Following Meyer’s example, we built a small library catalog.
en086 | BASE | — | 0.00 | The proposed patch adds a module for technical reports.
en087 | BASE | — | 0.00 | The two existing source files remain byte-for-byte identical.
en088 | BASE | — | 0.00 | In execution, technical reports render and requests for errata are still rejected.
en089 | BASE | — | 0.00 | The prefix in an existing book’s output changes from book to BOOK .
en090 | BASE | — | 0.00 | The identity of the old source files therefore does not imply the preservation of every observable result; we verified the latter separately in our fixture.
en091 | BASE | — | 0.00 | We hold the patch, its observed behavior, and the boundary permitting new modules fixed.
en092 | BASE | — | 0.00 | The new requirement covers either technical reports alone or both technical reports and errata.
en093 | BASE | — | 0.00 | Both legacy contracts protect the rendering of journals and proceedings and require rejection of a separate unsupported type.
en094 | BASE | — | 0.00 | The broader contract also protects the original book prefix.
en095 | BASE | — | 0.00 | An acceptable candidate in Table 2 must meet both the new requirement and the applicable contract.
en096 | BASE | — | 0.00 | Two independent conditions for the same patch.
en097 | BASE | — | 0.00 | The patch is acceptable when only technical reports are required and the book prefix is outside the contract.
en098 | BASE | — | 0.00 | Knowing that errata are required suffices to reject it even before the prefix contract is known.
en099 | BASE | — | 0.00 | If only technical reports are required, the verdict turns on whether callers were promised the original prefix.
en100 | BASE | — | 0.00 | A separate patch adds one module within the same edit boundary, handles both new types, and preserves every protected observation.
en101 | BASE | — | 0.00 | With partial information, the reviewer can consider the specifications still compatible with the evidence.
en102 | BASE | — | 0.00 | If all give the same verdict, the reviewer can issue it.
en103 | BASE | — | 0.00 | If they disagree, the reviewer can give conditional verdicts or defer until the applicable specification can be established.
en104 | BASE | — | 0.00 | This argument assumes that the actual specification is in the compatible set, so the set is nonempty.
en105 | BASE | — | 0.00 | A rule that sees the same input and must always return a single binary verdict cannot be correct for two compatible specifications that require opposite answers.
en106 | BASE | — | 0.00 | This establishes an information limit, not an error rate for SOLID judgments in practice.
en107 | BASE | — | 0.00 | Appendix A gives the nine disclosure conditions for this case.
en108 | BASE | — | 0.00 | · Section 5 established whether one patch met a stated request and contract.
en109 | BASE | — | 0.00 | It did not determine the least costly way to meet them.
en110 | BASE | — | 0.00 | Returning to the drawing fixture, we ask which source boundaries the implemented candidates cross when the request, permitted placement, or caller route changes.
en111 | BASE | — | 0.00 | The counts describe those candidates, not a minimum over all possible implementations.
en112 | BASE | — | 0.00 | We first varied the request.
en113 | BASE | — | 0.00 | In the shape layout we added a triangle in one new file and edited the circle and square files to add a labeling operation.
en114 | BASE | — | 0.00 | In the operation layout we edited the drawing file to add the triangle and put the labeling operation in a new file.
en115 | BASE | — | 0.00 | All four candidates passed their functional checks.
en116 | BASE | — | 0.00 | Which layout left more existing files intact depended on the request (Figure 1A).
en117 | BASE | — | 0.00 | We then added the same batch-rendering function to both layouts.
en118 | BASE | — | 0.00 | It takes a list of shapes and brackets each rendered result.
en119 | BASE | — | 0.00 | We predicted that requiring the item transformation to live in the shape files would entail editing both files in the shape layout.
en120 | BASE | — | 0.00 | If a shared adapter was allowed, we predicted that either layout could add the feature in one new file.
en121 | BASE | — | 0.00 | All four candidates preserved order and duplicates, handled empty lists and unsupported shapes as specified, and preserved the existing circle and square renderings.
en122 | BASE | — | 0.00 | The candidate placing both transformations in the shape files edited two existing files.
en123 | BASE | — | 0.00 | All four added one file (Figure 1B).
en124 | BASE | — | 0.00 | Existing source files edited.
en125 | BASE | — | 0.00 | Panel A compares adding a triangle with adding a labeling operation.
en126 | BASE | — | 0.00 | Panel B holds the batch-rendering request fixed and varies the placement rule.
en127 | BASE | — | 0.00 | All four candidates in panel B passed the new and legacy behavior checks and added one file each.
en128 | BASE | — | 0.00 | · · · · The third comparison used an option to bracket a single rendering through the existing function.
en129 | BASE | — | 0.00 | Candidates that offered a new entry point left the existing files intact in both layouts.
en130 | BASE | — | 0.00 | With the same adapter added, the original functions still rejected bracketed=True .
en131 | BASE | — | 0.00 | The candidates offering the option through the original functions edited one file in the operation layout and two in the shape layout.
en132 | BASE | — | 0.00 | In a separate baseline whose original function could already load an external decorator, each layout delivered the option through the original entry point by adding a single file (Table 3).
en133 | BASE | — | 0.00 | Call paths for the new rendering option.
en134 | BASE | — | 0.00 | The hook was already present in the last row’s baseline.
en135 | BASE | — | 0.00 | Its zero-edits result does not include the cost of introducing that hook into the earlier baseline.
en136 | BASE | — | 0.00 | We did not measure that initial investment.
en137 | BASE | — | 0.00 | The negative control adds the same adapter and finds that the option remains unavailable through the original function.
en138 | BASE | — | 0.00 | · Fewer changed files do not by themselves establish a more maintainable design.
en139 | BASE | — | 0.00 | Permission to add a file needs to be paired with a path that the caller can actually use.
en140 | BASE | — | 0.00 | The last row of Table 3 starts counting after the hook is already in place.
en141 | BASE | — | 0.00 | These file counts describe the tested candidates.
en142 | BASE | — | 0.00 | Whether we can predict working paths for independently authored requests, and how these counts relate to maintenance effort, remain open.
en143 | BASE | — | 0.00 | Whether the drawing routine falls short depends on who must sort the list.
en144 | BASE | — | 0.00 | The benchmark measures classification performance by comparing model responses with its reference labels.
en145 | BASE | — | 0.00 | Applying a finding to a specific patch also requires knowing what change the patch must deliver and which behavior existing callers were promised.
en146 | BASE | — | 0.00 | In the catalog example, the errata requirement can settle a rejection on its own.
en147 | BASE | — | 0.00 | When only technical reports are needed, the verdict turns on the promise about the book prefix.
en148 | BASE | — | 0.00 | Comparing possible edits also requires knowing how the new behavior can reach its callers.
en149 | BASE | — | 0.00 | A review that calls for an edit should identify the request or commitment it relies on and the call path to which it applies.
en150 | BASE | — | 0.00 | The developer can then check the grounds for the verdict or identify the remaining fact that would settle it.
en151 | BASE | — | 0.00 | The evidence here covers the saved material of one benchmark and the candidates we constructed and ran.
en152 | BASE | — | 0.00 | Rather than announce a new set of axioms, the next step is to ask whether changes, protected commitments, authority, and caller routes can be represented in a form that predicts when one design has an advantage over anot
en153 | BASE | — | 0.00 | Such an account would be valuable if it explained both the usefulness of familiar principles and the conditions under which their preferred design loses.
en154 | BASE | — | 0.00 | The present paper poses that hypothesis; it does not establish it.
en155 | BASE | — | 0.00 | For Sections 3–4 the audit reads the archived JSON and JSONL.
en156 | BASE | — | 0.00 | For Sections 5–6 the fixtures run the examples constructed for this study.
en157 | BASE | — | 0.00 | The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.
Summary en: SAME 0, EDIT 0, NEW 0

## v08 · [Source](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/PAPER_B_BILINGUAL_INTEGRATED_08_20261117.md)
### ko (143 segmented sentences)
ko001 | NEW | ko001 | 0.10 | 로버트 마틴이 1996년에 예로 든 함수는 목록에 들어온 순서대로 도형을 그린다.
ko002 | NEW | ko002 | 0.32 | 삼각형에 자기 자신을 그리는 동작이 있으면 이 함수에 손대지 않고도 삼각형을 추가할 수 있다.
ko003 | NEW | ko003 | 0.18 | 목록의 맨 앞에 사각형이 있으면 함수는 여전히 그 사각형부터 그린다.
ko004 | NEW | ko005 | 0.26 | 호출자가 원을 앞에 놓아 목록을 넘기기로 했다면 함수는 제 일을 한다.
ko005 | NEW | ko006 | 0.41 | 어떤 목록을 받더라도 함수가 순서를 보장하기로 했다면 수정이 필요하다.
ko006 | NEW | ko007 | 0.17 | 코드를 읽으면 무엇이 먼저 그려지는지 알 수 있다.
ko007 | NEW | ko008 | 0.09 | 그 결과가 잘못됐는지를 판단하려면 호출자와 함수 사이에 어떤 약속이 있었는지도 알아야 한다.
ko008 | NEW | ko036 | 0.03 | 도형 하나를 더 추가할 때 닫혀 있던 설계도 함수가 직접 정렬을 책임지는 순간 같은 방식으로 확장할 수 없었다.
ko009 | NEW | ko008 | 0.08 | 개방–폐쇄 원칙(OCP)을 근거로 어떤 수정안에 ‘위반’이라고 표시할 때도, 그 판단을 받은 개발자는 프로그램이 어떤 변화에 대비해야 했고 어떤 동작을 계속 보장해야 했는지 물을 수 있다.
ko010 | NEW | ko012 | 0.23 | 이 전제가 정해지기 전에 판정부터 확정하는 위험을 이 글에서는 설계 조언의 ‘과도한 공리화’라고 부른다.
ko011 | NEW | ko015 | 0.07 | 분류 벤치마크에는 모델이 무엇을 보고 위반 여부를 답했는지 기록이 남아 있다.
ko012 | NEW | ko142 | 0.06 | 그 기록을 읽어 분류에 주어진 근거를 확인한다.
ko013 | NEW | ko016 | 0.08 | 코드가 같은데도 새 요구와 기존 호출자에 대한 약속에 따라 결론이 달라지는지 살핀다.
ko014 | NEW | ko105 | 0.09 | 그 뒤 도형 예제로 돌아가 새 기능을 별도 파일에 넣었을 때 기존 호출자가 사용하던 함수로도 그 기능을 쓸 수 있는지 확인한다.
ko015 | NEW | ko018 | 0.34 | · · 마틴은 1996년 글에서 베르트랑 마이어의 1988년 초판 23쪽을 인용하며 원칙의 출처를 밝혔다.
ko016 | EDIT | ko020 | 0.69 | 마이어가 말한 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 사용할 수 있는 모듈이다.
ko017 | NEW | ko021 | 0.24 | 마이어는 자료의 종류를 하나씩 구별해 처리하는 도서관 프로그램을 예로 든다.
ko018 | NEW | ko021 | 0.07 | 기술보고서가 새로운 자료 유형으로 들어오면 이미 쓰이던 모듈까지 고치거나 다시 컴파일해야 할 수 있다.
ko019 | NEW | ko022 | 0.07 | 새 자료를 처리하는 코드를 어디에 두느냐는 기존 모듈이 무엇에 의존할 수 있느냐와 맞물린다.
ko020 | NEW | ko023 | 0.16 | 1995년 6월 공개 토론에서는 기존 모듈을 손댈 수 있다는 것과 손대야 한다는 것의 차이가 쟁점이었다.
ko021 | NEW | ko023 | 0.31 | 카일 브라운은 잘못 설계된 클래스라면 개발자가 소스를 고칠 수 있어야 한다고 했다.
ko022 | NEW | ko024 | 0.08 | 마틴의 답은 예상한 확장을 하려면 기존 소스를 반드시 고쳐야 하는지에 관한 것이었다.
ko023 | NEW | ko025 | 0.41 | 어떤 변경이 생길지 미리 짚어야 한다는 어려움은 남았다.
ko024 | NEW | ko027 | 0.24 | 2007년 공개 기록에는 다섯 원칙을 묶은 SOLID라는 이름이 나온다.
ko025 | NEW | ko027 | 0.30 | 2009년의 인터페이스 논쟁에서도 내부 클래스의 인터페이스와 공개 플러그인 API에는 서로 다른 조언이 제시됐다.
ko026 | NEW | ko015 | 0.03 | 이 자료들은 원칙이 어떻게 쓰이고 논쟁됐는지 보여 준다.
ko027 | NEW | ko051 | 0.10 | SOLID라는 이름이 퍼지면서 적용 조건에 대한 판단이 실제로 바뀌었는지는 별도의 근거가 필요한 역사적 질문이다.
ko028 | NEW | ko001 | 0.16 | · · 1996년 글에서 마틴은 목록 정렬을 가 맡게 했다.
ko029 | NEW | ko030 | 0.36 | 한 구현에서는 가 상대 도형을 검사해 사각형이면 원을 먼저 놓는다.
ko030 | NEW | ko031 | 0.06 | 세 번째 도형과 원의 순서를 정해야 하면 을 다시 고칠 수 있다.
ko031 | NEW | ko033 | 0.30 | 도형 종류별 순서를 표로 옮기면 사각형을 원보다 먼저 그리기 위해 두 항목의 위치만 바꾸면 된다.
ko032 | NEW | ko034 | 0.38 | 그다음 요구가 개별 도형을 넓이순으로 그리는 것이라면 표에 없는 정보가 필요하다.
ko033 | NEW | ko037 | 0.13 | 같은 글 후반에서 마틴은 를 쓰는 함수 둘을 제시한다.
ko034 | NEW | ko038 | 0.10 | 의 한 구현은 원과 사각형을 골라 그리고, 는 사각형을 골라 그린다.
ko035 | NEW | ko040 | 0.15 | 모든 도형을 그려야 하는 함수라면 그림 하나가 빠진 것이고, 사각형만 그려야 하는 함수라면 건너뛰는 것이 맞다.
ko036 | NEW | ko007 | 0.06 | 여기서는 함수 이름과 설명을 읽으면 각각 무엇을 맡았는지 알 수 있다.
ko037 | NEW | ko044 | 0.18 | 분류를 맡은 검토자에게 코드와 프롬프트가 주어졌을 때는 그 책임을 어디까지 확인할 수 있을까?
ko038 | SAME | ko045 | 1.00 | · · 이 질문을 저장 자료에 적용하기 위해 분석 단위를 세 가지로 나눴다.
ko039 | SAME | ko046 | 1.00 | 참조 코드 쌍에는 위반 예시와 그 수정 예시가 들어 있고, 저장 응답에는 모델에 제출된 코드와 프롬프트, 기록된 응답이 들어 있다.
ko040 | SAME | ko047 | 1.00 | 프롬프트 틀은 저장 프롬프트에 정확히 한 번 나오는 제출 코드를 공통 자리표시자로 치환해 얻었다.
ko041 | SAME | ko048 | 1.00 | 저장 응답의 제출 코드를 모든 참조 쌍의 수정 전·후 소스와 대조했다.
ko042 | SAME | ko049 | 1.00 | 각 문자열을 그대로 비교한 뒤 양끝 공백을 제거해 다시 비교했다.
ko043 | SAME | ko050 | 1.00 | Python 참조 쌍은 구문 트리로 파싱해 최상위 클래스의 메서드 선언 이름을 비교했다.
ko044 | SAME | ko051 | 1.00 | 상속에 따른 호출 가능성, 실제 사용 여부, 보장의 범위는 별도 근거가 필요한 질문이다.
ko045 | SAME | ko052 | 1.00 | 이 연구에서 작성한 도서관·도형 재현은 §5와 §6에서 정한 조건으로 실행했다.
ko046 | SAME | ko053 | 1.00 | ZIP 안의 공개 재현 패키지 코드는 실행하지 않았다.
ko047 | SAME | ko054 | 1.00 | 아카이브 식별 정보와 확인 명령은 부록 A에 있다.
ko048 | SAME | ko055 | 1.00 | · Pehlivan 등은 위반 시나리오를 정하고, 생성한 코드 예시를 수정·검증한 뒤 의견이 갈린 사례의 참조 라벨을 논의로 정했다.
ko049 | SAME | ko056 | 1.00 | SOLID 위반을 식별하는 모델 응답은 그 라벨과 대조했다.
ko050 | SAME | ko057 | 1.00 | OCP에 해당하는 아카이브에는 참조 쌍 48개와 저장 응답 768건이 있다.
ko051 | SAME | ko058 | 1.00 | 저장 프롬프트에서 제출 코드를 가렸을 때 서로 다른 문자열 24개가 남았고, 네 전략 사이에 동일한 틀은 없었다.
ko052 | SAME | ko059 | 1.00 | 각 사례의 변경 요구나 기존 호출자 계약을 따로 밝힌 틀은 없었다.
ko053 | SAME | ko060 | 1.00 | 이는 벤치마크가 본래 수행하려는 분류 과제를 잘못 설계했다는 뜻이 아니다.
ko054 | SAME | ko061 | 1.00 | 특정 수정안을 승인하거나 거절하는 데 이 분류 결과를 사용하려면 추가 증거가 필요하다는 뜻이다.
ko055 | EDIT | ko062 | 0.72 | 저장된 Python 지시는 다형성으로 처리할 만한 반복 분기를 찾도록 한다.
ko056 | EDIT | ko063 | 0.55 | 제출된 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko057 | SAME | ko064 | 1.00 | 그 분기를 보면 새 도형을 추가할 때 어디에 손댈지 짐작할 수 있다.
ko058 | SAME | ko065 | 1.00 | 새 도형 추가가 실제 요청인지, 사각형의 너비를 직접 읽는 호출을 계속 지원해야 하는지는 이 지시문에서 확인되지 않는다.
ko059 | EDIT | ko066 | 0.55 | 별도의 참조 쌍 37번은 넓이 계산을 도형 메서드로 옮기면서 선언을 뺐다.
ko060 | SAME | ko067 | 1.00 | 원본 문자열과 양끝 공백을 제거한 문자열을 대조했을 때, 저장된 제출 코드와 참조 쌍의 어느 쪽도 일치하지 않았다.
ko061 | SAME | ko068 | 1.00 | 따라서 여기서 근거로 삼는 것은 참조 쌍에서 확인한 선언의 변화다.
ko062 | SAME | ko069 | 1.00 | 그 변화가 수정안을 거절할 이유가 되려면 호출자가 너비를 읽는 동작까지 보장받았는지 확인해야 한다.
ko063 | SAME | ko070 | 1.00 | 이 참조 쌍에 실제 호출자가 있었다고 주장하지는 않는다.
ko064 | SAME | ko071 | 1.00 | 대신 해당 문제가 판정에 영향을 줄 수 있는지 별도로 구성한 수정안에서 시험한다.
ko065 | SAME | ko072 | 1.00 | 이 사례가 분류 평가를 대표하는 유일한 방식은 아니다.
ko066 | SAME | ko073 | 1.00 | Bräuer 등(2018)은 설계 원칙을 측정 가능한 실천 규칙으로 옮길 때 전문가들이 보기에 무엇이 포착되고 무엇이 빠지는지 물었다.
ko067 | SAME | ko074 | 1.00 | Cabral 등(2024)은 구체적인 기계학습 확장 상황에서 SOLID 적용 전후 코드에 대한 참가자의 이해도와 확장 용이성 인식을 조사했다.
ko068 | SAME | ko075 | 1.00 | Zhu 등(2026)은 저장소 변경 요구에 기능 테스트와 구조적 판정 기준을 결합했다.
ko069 | SAME | ko076 | 1.00 | 세 연구는 각각 **원칙의 측정 범위, 사용자의 인식, 특정 변경에서의 기능·구조 적합성**을 관찰한다.
ko070 | SAME | ko077 | 1.00 | 우리 비교의 결과 변수는 같은 패치가 명시된 요구와 계약 아래에서 승인 기준을 충족하는가다.
ko071 | SAME | ko078 | 1.00 | 앞선 연구를 코드 판정의 실패 사례로 취급하지 않으면서도, 무엇을 측정해야 어떤 결정을 정당화할 수 있는지 서로 다른 관점에서 확인할 수 있다.
ko072 | SAME | ko079 | 1.00 | ** 프롬프트 예시는 저장 JSONL 13행(ID 12)이다.
ko073 | SAME | ko080 | 1.00 | 참조 쌍 37번은 별도의 ground truth JSON 위치다.
ko074 | SAME | ko081 | 1.00 | · · · 마이어의 예를 바탕으로 작은 도서관 목록 프로그램을 만들었다.
ko075 | SAME | ko082 | 1.00 | 검토할 수정안은 기술보고서를 처리하는 모듈을 추가한다.
ko076 | SAME | ko083 | 1.00 | 기존 소스 파일 두 개는 바이트 단위로 그대로다.
ko077 | SAME | ko084 | 1.00 | 실행하면 기술보고서는 출력되고 정오표는 여전히 거절된다.
ko078 | NEW | ko085 | 0.44 | 기존 책 출력의 접두어는 에서 으로 바뀐다.
ko079 | SAME | ko086 | 1.00 | 기존 파일을 수정하지 않았다는 사실은 기존 호출 결과까지 보존했다는 뜻이 아니다.
ko080 | SAME | ko087 | 1.00 | 변경된 동작은 우리가 만든 실행 예제에서 관찰했다.
ko081 | SAME | ko088 | 1.00 | 수정안과 실행 결과, 새 모듈을 추가할 수 있는 편집 범위를 고정했다.
ko082 | SAME | ko089 | 1.00 | 새 요구는 기술보고서만 지원하는 경우와 정오표까지 지원하는 경우로 나눴다.
ko083 | SAME | ko090 | 1.00 | 두 계약은 모두 학술지와 학회록의 출력, 그리고 별개의 미지원 자료 유형을 거절하는 동작을 보호한다.
ko084 | SAME | ko091 | 1.00 | 표 2의 승인은 새 요구와 보호할 계약을 모두 충족한 경우다.
ko085 | SAME | ko092 | 1.00 | ** 기술보고서만 필요하고 책 접두어를 보호하지 않는 경우에 승인된다.
ko086 | SAME | ko093 | 1.00 | 정오표가 필수라는 사실을 알면 책 접두어 계약을 모르더라도 거절할 수 있다.
ko087 | SAME | ko094 | 1.00 | 기술보고서만 필요하다는 사실을 알 때는 책 접두어를 보장했는지가 결론을 가른다.
ko088 | SAME | ko095 | 1.00 | 별도로 만든 수정안은 같은 편집 범위에서 새 모듈 하나를 추가해 두 자료 유형을 처리하고 모든 보호 동작을 지켰다.
ko089 | SAME | ko096 | 1.00 | 판정에 필요한 정보가 일부만 주어지면, 그 정보와 양립하는 명세들을 비교할 수 있다.
ko090 | SAME | ko097 | 1.00 | 모든 명세가 같은 판정을 내리면 그 판정을 내릴 수 있다.
ko091 | SAME | ko098 | 1.00 | 서로 다른 판정이 나오면 조건마다 결론을 밝히거나, 어느 조건이 실제로 적용되는지 확인할 때까지 보류할 수 있다.
ko092 | SAME | ko099 | 1.00 | 이 논증은 실제 명세가 검토 중인 집합에 들어 있어 그 집합이 비어 있지 않다는 전제에서 성립한다.
ko093 | SAME | ko100 | 1.00 | 이때 한 가지 입력만 받아 언제나 승인 또는 거절 중 하나를 출력하는 규칙은, 서로 다른 정답이 남아 있는 두 조건을 동시에 맞힐 수 없다.
ko094 | SAME | ko101 | 1.00 | 다만 이 논증만으로 SOLID의 다른 정리나 실제 현장의 판단 오류율을 추정할 수는 없다.
ko095 | SAME | ko102 | 1.00 | 부록 A에는 이번 사례에서 검토한 정보 공개 조건 아홉 개가 있다.
ko096 | SAME | ko103 | 1.00 | · 도서관 실험에서 확인한 것은 주어진 수정안의 적격성이었다.
ko097 | SAME | ko104 | 1.00 | 다른 수정안이 더 적은 비용으로 같은 요구를 처리할 수 있는지는 아직 별도 문제다.
ko098 | SAME | ko105 | 1.00 | 도형 예제로 돌아가, 어떤 변경에 대비할지와 새 기능을 어디에서 호출할지에 따라 기존 파일을 얼마나 수정하는지 비교한다.
ko099 | SAME | ko106 | 1.00 | 여기서 세는 것은 실행한 후보들의 수정 파일 수이지 가능한 구현 전체의 최솟값이 아니다.
ko100 | SAME | ko107 | 1.00 | 도형별 배치에서는 삼각형을 새 파일 하나로 추가했고, 이름표 연산을 추가할 때는 원과 사각형의 파일을 고쳤다.
ko101 | SAME | ko108 | 1.00 | 연산별 배치에서는 반대로 삼각형을 추가할 때 그리기 파일을 고쳤고, 이름표 연산은 새 파일에 뒀다.
ko102 | SAME | ko109 | 1.00 | 네 수정안이 모두 기능 검사를 통과했지만 기존 파일을 덜 건드리는 배치는 요구에 따라 달랐다(그림 1A).
ko103 | SAME | ko110 | 1.00 | 두 번째 비교에서는 같은 배치 렌더링 함수를 추가했다.
ko104 | SAME | ko111 | 1.00 | 이 함수는 도형 목록을 받아 각 렌더링 결과를 대괄호로 감싼다.
ko105 | SAME | ko112 | 1.00 | 도형별 배치에서 변환을 각 도형 파일이 맡아야 하면 원과 사각형 파일을 고친다.
ko106 | SAME | ko113 | 1.00 | 공용 어댑터를 허용하면 두 배치 모두 새 파일 하나로 기능을 제공할 수 있다고 예측했다.
ko107 | SAME | ko114 | 1.00 | 실행한 네 후보는 모두 입력 순서와 중복을 보존하고 빈 목록과 미지원 도형을 명세대로 처리했다.
ko108 | SAME | ko115 | 1.00 | 각 후보는 원과 사각형의 기존 렌더링을 유지했다.
ko109 | SAME | ko116 | 1.00 | 기존 파일 두 개를 고친 것은 도형 파일이 변환을 맡은 후보뿐이었다.
ko110 | SAME | ko117 | 1.00 | 네 후보 모두 새 파일 하나를 추가했다(그림 1B).
ko111 | SAME | ko118 | 1.00 | ** A는 삼각형 추가와 이름표 연산 추가를 비교한다.
ko112 | SAME | ko119 | 1.00 | B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다.
ko113 | SAME | ko120 | 1.00 | B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.
ko114 | SAME | ko121 | 1.00 | · · · · 세 번째 비교에서는 배치 함수 대신 기존 렌더링의 결과 하나를 선택적으로 감싸는 옵션을 사용했다.
ko115 | SAME | ko122 | 1.00 | 새 모듈을 호출할 수 있는 경우에는 두 배치가 기존 파일을 그대로 뒀다.
ko116 | EDIT | ko123 | 0.63 | 같은 모듈을 추가한 상태에서 기존 함수에 를 넘기면 함수는 그 인자를 받지 못했다.
ko117 | SAME | ko124 | 1.00 | 기존 함수로 옵션을 제공한 후보는 연산별 배치에서 파일 하나, 도형별 배치에서 두 개를 고쳤다.
ko118 | SAME | ko125 | 1.00 | 기존 함수가 외부 변환 모듈을 불러올 수 있도록 이미 구성된 별도 기준선에서는 두 배치 모두 새 파일 하나를 추가해 기존 호출 경로로 옵션을 제공했다(표 3).
ko119 | SAME | ko126 | 1.00 | ** 확장 지점은 세 번째 행의 기준선에 이미 있었다.
ko120 | SAME | ko127 | 1.00 | 따라서 이 행의 0개를 첫 설계에서 확장 지점을 처음 만드는 비용까지 포함한 결과로 읽어서는 안 된다.
ko121 | SAME | ko128 | 1.00 | 여기서는 확장 지점이 도입된 비용을 별도로 측정하지 않았다.
ko122 | SAME | ko129 | 1.00 | 같은 어댑터를 추가해도 기존 함수에서는 옵션을 쓸 수 없었던 대조 실행을 포함했다.
ko123 | SAME | ko130 | 1.00 | · 기존 파일 수정 수가 적다는 사실만으로 변경에 더 잘 대응하는 설계라고 할 수는 없다.
ko124 | SAME | ko131 | 1.00 | 새 파일을 추가할 수 있어도 그 파일이 실행되려면 호출자가 쓸 수 있는 경로가 필요하다.
ko125 | SAME | ko132 | 1.00 | 표 3의 마지막 행은 확장 지점이 이미 있는 상태에서 이후에 고친 파일만 센다.
ko126 | SAME | ko133 | 1.00 | 여기에 든 수정 수는 실행한 후보에 관한 관찰이다.
ko127 | SAME | ko134 | 1.00 | 독립적으로 작성한 요구에서도 어떤 경로가 작동할지 예측할 수 있는지, 파일 수정 수가 실제 유지보수 부담과 어떻게 연결되는지는 남은 질문이다.
ko128 | SAME | ko135 | 1.00 | 서론의 그리기 함수가 잘못됐는지는 정렬을 누가 맡았는지에 달려 있었다.
ko129 | SAME | ko136 | 1.00 | 벤치마크는 모델의 응답을 참조 라벨과 대조해 분류 성능을 잰다.
ko130 | SAME | ko137 | 1.00 | 그 판정을 구체적인 수정안에 적용하려면 어떤 기능이 필요한지, 어떤 동작을 기존 호출자에게 약속했는지를 확인해야 한다.
ko131 | SAME | ko138 | 1.00 | 도서관 예제에서는 정오표 요구만으로 수정안을 거절할 수 있었다.
ko132 | SAME | ko139 | 1.00 | 기술보고서만 필요한 경우에는 책 접두어 계약이 결론을 갈랐다.
ko133 | SAME | ko140 | 1.00 | 어떤 수정안이 가능한지를 비교할 때는 호출자가 새 동작을 받을 수 있는 경로도 확인해야 한다.
ko134 | SAME | ko141 | 1.00 | 검토 의견으로 변경을 요구하려면 어느 요구나 계약을 근거로 삼았는지, 어느 호출 경로에 적용되는지를 밝힐 수 있어야 한다.
ko135 | SAME | ko142 | 1.00 | 그러면 개발자는 이미 내려진 결론의 근거를 확인하거나, 보류된 판정을 가를 사실을 더 찾을 수 있다.
ko136 | SAME | ko143 | 1.00 | 이 결과는 한 벤치마크의 저장 자료와 여기서 구성해 실행한 후보의 범위에서 성립한다.
ko137 | SAME | ko144 | 1.00 | 여기서 더 나아가려면 SOLID를 대체할 공리를 선언하기보다, 어떤 변경과 계약, 권한과 호출 경로가 주어졌을 때 설계의 유불리가 어떻게 달라지는지 예측할 수 있는 표현을 찾아야 한다.
ko138 | SAME | ko145 | 1.00 | 그런 표현이 실제 독립 요구에서도 작동한다면, 익숙한 원칙이 유용한 이유뿐 아니라 그 조언을 따르지 않는 설계가 더 나은 조건도 설명할 수 있을 것이다.
ko139 | SAME | ko146 | 1.00 | 이 가능성은 이번 논문의 결과가 아니라 다음에 검증할 가설로 남긴다.
ko140 | SAME | ko147 | 1.00 | §3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다.
ko141 | SAME | ko148 | 1.00 | §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다.
ko142 | SAME | ko149 | 1.00 | 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다.
ko143 | SAME | ko150 | 1.00 | 그림 1의 소스와 출력 위치는 그림 캡션에 있다.
Summary ko: SAME 101, EDIT 5, NEW 37

### en (155 segmented sentences)
en001 | SAME | en001 | 1.00 | In 1996, Robert Martin described a function that drew the shapes in a list in order.
en002 | SAME | en002 | 1.00 | A triangle could be added without editing the function if the triangle supplied its own drawing operation.
en003 | SAME | en003 | 1.00 | Martin then introduced a new requirement.
en004 | SAME | en004 | 1.00 | Every circle had to be drawn before any square.
en005 | SAME | en005 | 1.00 | Given a list that begins with a square, the same function still draws the square first.
en006 | NEW | en006 | 0.17 | Who was supposed to sort the list?
en007 | NEW | en007 | 0.29 | If the caller was to put the circles first, the drawing function already does its job.
en008 | NEW | en008 | 0.35 | If the function was to guarantee that order for any input, it falls short.
en009 | NEW | en009 | 0.13 | Reading the code tells a reviewer what gets drawn first.
en010 | NEW | en009 | 0.16 | The reviewer needs the agreement between caller and function to tell whether that is a defect.
en011 | NEW | en012 | 0.14 | Martin called the design closed with respect to the addition of a shape.
en012 | NEW | en003 | 0.18 | The sorting requirement gives the same code a different test.
en013 | NEW | en010 | 0.22 | That is where our question about the open–closed principle (OCP) begins.
en014 | NEW | en147 | 0.13 | When a reviewer calls a proposed edit a violation, can the author recover from the verdict what the program was expected to accommodate or preserve?
en015 | NEW | en014 | 0.17 | We use *over-axiomatization* for the risk of treating such a verdict as settled when those premises are still open.
en016 | NEW | en059 | 0.20 | A benchmark that scores agreement with reference labels makes that question tractable.
en017 | NEW | en104 | 0.16 | Its archive lets us inspect the information actually supplied for classification.
en018 | NEW | en145 | 0.21 | To test what an acceptance decision requires, we hold a patch fixed and vary the task and the promise to existing callers.
en019 | NEW | en132 | 0.20 | We then return to drawing to see when a separate implementation can deliver an extension through the call the user already makes.
en020 | EDIT | en020 | 0.64 | · · In 1996 Martin attributed the principle to Bertrand Meyer, citing page 23 of the 1988 first edition.
en021 | EDIT | en022 | 0.51 | In Meyer’s account a module is closed once other modules can use it on the basis of a stable description.
en022 | NEW | en085 | 0.12 | His library example gives that stability a concrete test.
en023 | NEW | en023 | 0.37 | When technical reports become a new category, a program that handles each publication type explicitly may require edits to, or recompilation of, existing modules.
en024 | NEW | en024 | 0.15 | The choice of where to handle the new type matters to the modules that already depend on the catalog.
en025 | NEW | en026 | 0.23 | Having to edit a module to extend it was the issue in a June 1995 public exchange.
en026 | NEW | en026 | 0.36 | Kyle Brown argued that developers had to be able to fix a badly designed class.
en027 | NEW | en027 | 0.26 | Martin’s reply distinguished the right to edit a class from the need to edit it for an anticipated extension.
en028 | NEW | en027 | 0.12 | The design would still have to anticipate the right change.
en029 | NEW | en028 | 0.14 | The label SOLID appears in the public record by 2007.
en030 | NEW | en028 | 0.24 | In a 2009 discussion of interfaces, the distinction between a routine internal class and a public plugin API still mattered to the participants’ advice.
en031 | NEW | en011 | 0.14 | These sources document particular uses and disagreements about the principle.
en032 | NEW | en054 | 0.13 | A causal history of the acronym would require evidence of what changed as the label circulated.
en033 | NEW | en020 | 0.16 | · · In the 1996 article Martin made sorting part of .
en034 | NEW | en031 | 0.34 | In one implementation, puts a circle before a square by inspecting the other shape.
en035 | NEW | en032 | 0.18 | A new rule about where a third type ranks against a circle can send the edit back into .
en036 | NEW | en033 | 0.25 | Martin moved the ranking of types into a table, so putting squares ahead of circles becomes a matter of swapping two entries.
en037 | NEW | en035 | 0.34 | If the next request were to sort individual shapes by area, the table would need information it does not contain.
en038 | NEW | en038 | 0.28 | Later in the article Martin uses in two routines.
en039 | NEW | en039 | 0.38 | One version of recognizes circles and squares. selects squares.
en040 | NEW | en143 | 0.12 | The first routine leaves a shape undrawn when its job is to draw them all.
en041 | NEW | en154 | 0.10 | The second skips exactly the shapes it is supposed to skip.
en042 | NEW | en137 | 0.18 | Here the names and stated jobs make the distinction available to the reader.
en043 | NEW | en043 | 0.29 | What can a classification reviewer establish when the input consists of code and a prompt?
en044 | SAME | en046 | 1.00 | · · To separate the obligations inferable from the inputs from the labels assigned by the benchmark, we distinguish three units in the archive.
en045 | SAME | en047 | 1.00 | A reference pair contains a violation example and its revision.
en046 | SAME | en048 | 1.00 | A saved response record contains the code submitted to the model, its prompt, and the recorded response.
en047 | SAME | en049 | 1.00 | We recover a prompt template by replacing the single exact occurrence of the submitted code with a common placeholder.
en048 | SAME | en050 | 1.00 | We compare templates as strings.
en049 | SAME | en051 | 1.00 | We compared each saved submission with the source on both sides of every reference pair, first as stored and again after trimming whitespace from both ends.
en050 | SAME | en052 | 1.00 | For Python reference pairs we parsed the syntax trees and compared names of methods declared in top-level classes, excluding names that begin with an underscore.
en051 | SAME | en053 | 1.00 | The comparison captures declaration changes.
en052 | SAME | en054 | 1.00 | Inherited availability, actual client use, and whether that use was protected each require separate evidence.
en053 | SAME | en055 | 1.00 | We ran the library and drawing fixtures built for this study under the conditions given in Sections 5 and 6.
en054 | SAME | en056 | 1.00 | We executed no code from the archived replication package.
en055 | SAME | en057 | 1.00 | Appendix A identifies the archive and the commands needed to reproduce the checks.
en056 | SAME | en058 | 1.00 | · Pehlivan et al. specified violation scenarios and refined and checked the generated examples.
en057 | SAME | en059 | 1.00 | They resolved disagreements about reference labels through discussion, then compared model classifications of SOLID violations with those labels.
en058 | SAME | en060 | 1.00 | The OCP archive contains 48 reference pairs and 768 saved response records.
en059 | SAME | en061 | 1.00 | Masking the submitted code yielded 24 distinct template strings, with no exact template shared across the four strategies.
en060 | SAME | en062 | 1.00 | None of the templates separately states a change request or a protected caller contract for an individual case.
en061 | SAME | en063 | 1.00 | That absence is not a defect in a benchmark whose stated task is classification.
en062 | SAME | en064 | 1.00 | It matters when the resulting label is asked to justify an engineering decision outside that task.
en063 | EDIT | en065 | 0.88 | One saved Python prompt points the reviewer to repeated branches where polymorphism would fit.
en064 | EDIT | en066 | 0.87 | The submitted checks the shape type before calculating the area of a circle or rectangle.
en065 | SAME | en067 | 1.00 | The branch suggests where an edit might go if a new shape is added.
en066 | SAME | en068 | 1.00 | The instruction leaves open whether anyone has requested that change and whether existing calls that read a rectangle’s width must still be supported.
en067 | EDIT | en069 | 0.83 | In a separate reference pair, number 37, the revision moves area calculation onto the shapes and drops the declaration of .
en068 | SAME | en070 | 1.00 | No saved submission matched either side of the reference pairs in the exact or outer-whitespace-trimmed comparison.
en069 | SAME | en071 | 1.00 | Our evidence for the missing declaration comes from comparing the reference sources.
en070 | SAME | en072 | 1.00 | To argue that its removal warrants rejecting a patch, a reviewer would need to establish that callers were guaranteed access to the width.
en071 | SAME | en073 | 1.00 | We do not infer that a real caller used the deleted getter.
en072 | SAME | en074 | 1.00 | Instead, a separate executable fixture tests whether varying a protected commitment can change the verdict on a fixed edit.
en073 | SAME | en075 | 1.00 | Other research measures different aspects of this problem.
en074 | SAME | en076 | 1.00 | Bräuer et al. (2018) asked experts which parts of design principles were and were not captured by measurable practices.
en075 | SAME | en077 | 1.00 | Cabral et al. (2024) studied participants' understanding and perceived extension benefits in a concrete machine-learning scenario comparing bundled code treatments.
en076 | SAME | en078 | 1.00 | Zhu et al. (2026) evaluated repository changes against functional tests and structural oracles.
en077 | SAME | en079 | 1.00 | These instruments measure, respectively, **coverage of principles, reported perceptions, and conformance under specified tasks**.
en078 | SAME | en080 | 1.00 | Our fixed-patch fixture instead asks whether an acceptance verdict is stable under explicitly varied demands and protected contracts.
en079 | SAME | en081 | 1.00 | The distinction does not make the earlier instruments invalid; it identifies the decision for which each source supplies evidence.
en080 | SAME | en082 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en081 | SAME | en083 | 1.00 | ** The saved prompt is on JSONL line 13 (record ID 12).
en082 | SAME | en084 | 1.00 | Reference pair 37 is in a separate ground-truth JSON file. 768 counts saved records.
en083 | SAME | en085 | 1.00 | · · · Following Meyer’s example, we built a small library catalog.
en084 | SAME | en086 | 1.00 | The proposed patch adds a module for technical reports.
en085 | SAME | en087 | 1.00 | The two existing source files remain byte-for-byte identical.
en086 | SAME | en088 | 1.00 | In execution, technical reports render and requests for errata are still rejected.
en087 | EDIT | en089 | 0.84 | The prefix in an existing book’s output changes from to .
en088 | SAME | en090 | 1.00 | The identity of the old source files therefore does not imply the preservation of every observable result; we verified the latter separately in our fixture.
en089 | SAME | en091 | 1.00 | We hold the patch, its observed behavior, and the boundary permitting new modules fixed.
en090 | SAME | en092 | 1.00 | The new requirement covers either technical reports alone or both technical reports and errata.
en091 | SAME | en093 | 1.00 | Both legacy contracts protect the rendering of journals and proceedings and require rejection of a separate unsupported type.
en092 | SAME | en094 | 1.00 | The broader contract also protects the original book prefix.
en093 | SAME | en095 | 1.00 | An acceptable candidate in Table 2 must meet both the new requirement and the applicable contract.
en094 | SAME | en096 | 1.00 | Two independent conditions for the same patch.
en095 | SAME | en097 | 1.00 | ** The patch is acceptable when only technical reports are required and the book prefix is outside the contract.
en096 | SAME | en098 | 1.00 | Knowing that errata are required suffices to reject it even before the prefix contract is known.
en097 | SAME | en099 | 1.00 | If only technical reports are required, the verdict turns on whether callers were promised the original prefix.
en098 | SAME | en100 | 1.00 | A separate patch adds one module within the same edit boundary, handles both new types, and preserves every protected observation.
en099 | SAME | en101 | 1.00 | With partial information, the reviewer can consider the specifications still compatible with the evidence.
en100 | SAME | en102 | 1.00 | If all give the same verdict, the reviewer can issue it.
en101 | SAME | en103 | 1.00 | If they disagree, the reviewer can give conditional verdicts or defer until the applicable specification can be established.
en102 | SAME | en104 | 1.00 | This argument assumes that the actual specification is in the compatible set, so the set is nonempty.
en103 | SAME | en105 | 1.00 | A rule that sees the same input and must always return a single binary verdict cannot be correct for two compatible specifications that require opposite answers.
en104 | SAME | en106 | 1.00 | This establishes an information limit, not an error rate for SOLID judgments in practice.
en105 | SAME | en107 | 1.00 | Appendix A gives the nine disclosure conditions for this case.
en106 | SAME | en108 | 1.00 | · Section 5 established whether one patch met a stated request and contract.
en107 | SAME | en109 | 1.00 | It did not determine the least costly way to meet them.
en108 | SAME | en110 | 1.00 | Returning to the drawing fixture, we ask which source boundaries the implemented candidates cross when the request, permitted placement, or caller route changes.
en109 | SAME | en111 | 1.00 | The counts describe those candidates, not a minimum over all possible implementations.
en110 | SAME | en112 | 1.00 | We first varied the request.
en111 | SAME | en113 | 1.00 | In the shape layout we added a triangle in one new file and edited the circle and square files to add a labeling operation.
en112 | SAME | en114 | 1.00 | In the operation layout we edited the drawing file to add the triangle and put the labeling operation in a new file.
en113 | SAME | en115 | 1.00 | All four candidates passed their functional checks.
en114 | SAME | en116 | 1.00 | Which layout left more existing files intact depended on the request (Figure 1A).
en115 | SAME | en117 | 1.00 | We then added the same batch-rendering function to both layouts.
en116 | SAME | en118 | 1.00 | It takes a list of shapes and brackets each rendered result.
en117 | SAME | en119 | 1.00 | We predicted that requiring the item transformation to live in the shape files would entail editing both files in the shape layout.
en118 | SAME | en120 | 1.00 | If a shared adapter was allowed, we predicted that either layout could add the feature in one new file.
en119 | SAME | en121 | 1.00 | All four candidates preserved order and duplicates, handled empty lists and unsupported shapes as specified, and preserved the existing circle and square renderings.
en120 | SAME | en122 | 1.00 | The candidate placing both transformations in the shape files edited two existing files.
en121 | SAME | en123 | 1.00 | All four added one file (Figure 1B).
en122 | SAME | en124 | 1.00 | Existing source files edited.
en123 | SAME | en125 | 1.00 | ** Panel A compares adding a triangle with adding a labeling operation.
en124 | SAME | en126 | 1.00 | Panel B holds the batch-rendering request fixed and varies the placement rule.
en125 | SAME | en127 | 1.00 | All four candidates in panel B passed the new and legacy behavior checks and added one file each.
en126 | SAME | en128 | 1.00 | · · · · The third comparison used an option to bracket a single rendering through the existing function.
en127 | SAME | en129 | 1.00 | Candidates that offered a new entry point left the existing files intact in both layouts.
en128 | EDIT | en130 | 0.83 | With the same adapter added, the original functions still rejected .
en129 | SAME | en131 | 1.00 | The candidates offering the option through the original functions edited one file in the operation layout and two in the shape layout.
en130 | SAME | en132 | 1.00 | In a separate baseline whose original function could already load an external decorator, each layout delivered the option through the original entry point by adding a single file (Table 3).
en131 | SAME | en133 | 1.00 | Call paths for the new rendering option.
en132 | SAME | en134 | 1.00 | ** The hook was already present in the last row’s baseline.
en133 | SAME | en135 | 1.00 | Its zero-edits result does not include the cost of introducing that hook into the earlier baseline.
en134 | SAME | en136 | 1.00 | We did not measure that initial investment.
en135 | SAME | en137 | 1.00 | The negative control adds the same adapter and finds that the option remains unavailable through the original function.
en136 | SAME | en138 | 1.00 | · Fewer changed files do not by themselves establish a more maintainable design.
en137 | SAME | en139 | 1.00 | Permission to add a file needs to be paired with a path that the caller can actually use.
en138 | SAME | en140 | 1.00 | The last row of Table 3 starts counting after the hook is already in place.
en139 | SAME | en141 | 1.00 | These file counts describe the tested candidates.
en140 | SAME | en142 | 1.00 | Whether we can predict working paths for independently authored requests, and how these counts relate to maintenance effort, remain open.
en141 | SAME | en143 | 1.00 | Whether the drawing routine falls short depends on who must sort the list.
en142 | SAME | en144 | 1.00 | The benchmark measures classification performance by comparing model responses with its reference labels.
en143 | SAME | en145 | 1.00 | Applying a finding to a specific patch also requires knowing what change the patch must deliver and which behavior existing callers were promised.
en144 | SAME | en146 | 1.00 | In the catalog example, the errata requirement can settle a rejection on its own.
en145 | SAME | en147 | 1.00 | When only technical reports are needed, the verdict turns on the promise about the book prefix.
en146 | SAME | en148 | 1.00 | Comparing possible edits also requires knowing how the new behavior can reach its callers.
en147 | SAME | en149 | 1.00 | A review that calls for an edit should identify the request or commitment it relies on and the call path to which it applies.
en148 | SAME | en150 | 1.00 | The developer can then check the grounds for the verdict or identify the remaining fact that would settle it.
en149 | SAME | en151 | 1.00 | The evidence here covers the saved material of one benchmark and the candidates we constructed and ran.
en150 | SAME | en152 | 1.00 | Rather than announce a new set of axioms, the next step is to ask whether changes, protected commitments, authority, and caller routes can be represented in a form that predicts when one design has an advantage over anot
en151 | SAME | en153 | 1.00 | Such an account would be valuable if it explained both the usefulness of familiar principles and the conditions under which their preferred design loses.
en152 | SAME | en154 | 1.00 | The present paper poses that hypothesis; it does not establish it.
en153 | SAME | en155 | 1.00 | For Sections 3–4 the audit reads the archived JSON and JSONL.
en154 | SAME | en156 | 1.00 | For Sections 5–6 the fixtures run the examples constructed for this study.
en155 | SAME | en157 | 1.00 | The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.
Summary en: SAME 112, EDIT 7, NEW 36

## v09 · [Source](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/PAPER_B_BILINGUAL_INTEGRATED_09_20261117.md)
### ko (142 segmented sentences)
ko001 | SAME | ko001 | 1.00 | 로버트 마틴이 1996년에 예로 든 함수는 목록에 들어온 순서대로 도형을 그린다.
ko002 | SAME | ko002 | 1.00 | 삼각형에 자기 자신을 그리는 동작이 있으면 이 함수에 손대지 않고도 삼각형을 추가할 수 있다.
ko003 | SAME | ko003 | 1.00 | 목록의 맨 앞에 사각형이 있으면 함수는 여전히 그 사각형부터 그린다.
ko004 | SAME | ko004 | 1.00 | 호출자가 원을 앞에 놓아 목록을 넘기기로 했다면 함수는 제 일을 한다.
ko005 | SAME | ko005 | 1.00 | 어떤 목록을 받더라도 함수가 순서를 보장하기로 했다면 수정이 필요하다.
ko006 | SAME | ko006 | 1.00 | 코드를 읽으면 무엇이 먼저 그려지는지 알 수 있다.
ko007 | SAME | ko007 | 1.00 | 그 결과가 잘못됐는지를 판단하려면 호출자와 함수 사이에 어떤 약속이 있었는지도 알아야 한다.
ko008 | SAME | ko008 | 1.00 | 도형 하나를 더 추가할 때 닫혀 있던 설계도 함수가 직접 정렬을 책임지는 순간 같은 방식으로 확장할 수 없었다.
ko009 | SAME | ko009 | 1.00 | 개방–폐쇄 원칙(OCP)을 근거로 어떤 수정안에 ‘위반’이라고 표시할 때도, 그 판단을 받은 개발자는 프로그램이 어떤 변화에 대비해야 했고 어떤 동작을 계속 보장해야 했는지 물을 수 있다.
ko010 | SAME | ko010 | 1.00 | 이 전제가 정해지기 전에 판정부터 확정하는 위험을 이 글에서는 설계 조언의 ‘과도한 공리화’라고 부른다.
ko011 | SAME | ko011 | 1.00 | 분류 벤치마크에는 모델이 무엇을 보고 위반 여부를 답했는지 기록이 남아 있다.
ko012 | SAME | ko012 | 1.00 | 그 기록을 읽어 분류에 주어진 근거를 확인한다.
ko013 | SAME | ko013 | 1.00 | 코드가 같은데도 새 요구와 기존 호출자에 대한 약속에 따라 결론이 달라지는지 살핀다.
ko014 | SAME | ko014 | 1.00 | 그 뒤 도형 예제로 돌아가 새 기능을 별도 파일에 넣었을 때 기존 호출자가 사용하던 함수로도 그 기능을 쓸 수 있는지 확인한다.
ko015 | SAME | ko015 | 1.00 | · · 마틴은 1996년 글에서 베르트랑 마이어의 1988년 초판 23쪽을 인용하며 원칙의 출처를 밝혔다.
ko016 | SAME | ko016 | 1.00 | 마이어가 말한 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 사용할 수 있는 모듈이다.
ko017 | SAME | ko017 | 1.00 | 마이어는 자료의 종류를 하나씩 구별해 처리하는 도서관 프로그램을 예로 든다.
ko018 | SAME | ko018 | 1.00 | 기술보고서가 새로운 자료 유형으로 들어오면 이미 쓰이던 모듈까지 고치거나 다시 컴파일해야 할 수 있다.
ko019 | SAME | ko019 | 1.00 | 새 자료를 처리하는 코드를 어디에 두느냐는 기존 모듈이 무엇에 의존할 수 있느냐와 맞물린다.
ko020 | SAME | ko020 | 1.00 | 1995년 6월 공개 토론에서는 기존 모듈을 손댈 수 있다는 것과 손대야 한다는 것의 차이가 쟁점이었다.
ko021 | SAME | ko021 | 1.00 | 카일 브라운은 잘못 설계된 클래스라면 개발자가 소스를 고칠 수 있어야 한다고 했다.
ko022 | SAME | ko022 | 1.00 | 마틴의 답은 예상한 확장을 하려면 기존 소스를 반드시 고쳐야 하는지에 관한 것이었다.
ko023 | SAME | ko023 | 1.00 | 어떤 변경이 생길지 미리 짚어야 한다는 어려움은 남았다.
ko024 | SAME | ko024 | 1.00 | 2007년 공개 기록에는 다섯 원칙을 묶은 SOLID라는 이름이 나온다.
ko025 | SAME | ko025 | 1.00 | 2009년의 인터페이스 논쟁에서도 내부 클래스의 인터페이스와 공개 플러그인 API에는 서로 다른 조언이 제시됐다.
ko026 | SAME | ko026 | 1.00 | 이 자료들은 원칙이 어떻게 쓰이고 논쟁됐는지 보여 준다.
ko027 | SAME | ko027 | 1.00 | SOLID라는 이름이 퍼지면서 적용 조건에 대한 판단이 실제로 바뀌었는지는 별도의 근거가 필요한 역사적 질문이다.
ko028 | SAME | ko028 | 1.00 | · · 1996년 글에서 마틴은 목록 정렬을 가 맡게 했다.
ko029 | SAME | ko029 | 1.00 | 한 구현에서는 가 상대 도형을 검사해 사각형이면 원을 먼저 놓는다.
ko030 | SAME | ko030 | 1.00 | 세 번째 도형과 원의 순서를 정해야 하면 을 다시 고칠 수 있다.
ko031 | SAME | ko031 | 1.00 | 도형 종류별 순서를 표로 옮기면 사각형을 원보다 먼저 그리기 위해 두 항목의 위치만 바꾸면 된다.
ko032 | SAME | ko032 | 1.00 | 그다음 요구가 개별 도형을 넓이순으로 그리는 것이라면 표에 없는 정보가 필요하다.
ko033 | SAME | ko033 | 1.00 | 같은 글 후반에서 마틴은 를 쓰는 함수 둘을 제시한다.
ko034 | SAME | ko034 | 1.00 | 의 한 구현은 원과 사각형을 골라 그리고, 는 사각형을 골라 그린다.
ko035 | SAME | ko035 | 1.00 | 모든 도형을 그려야 하는 함수라면 그림 하나가 빠진 것이고, 사각형만 그려야 하는 함수라면 건너뛰는 것이 맞다.
ko036 | SAME | ko036 | 1.00 | 여기서는 함수 이름과 설명을 읽으면 각각 무엇을 맡았는지 알 수 있다.
ko037 | SAME | ko037 | 1.00 | 분류를 맡은 검토자에게 코드와 프롬프트가 주어졌을 때는 그 책임을 어디까지 확인할 수 있을까?
ko038 | NEW | ko039 | 0.05 | · · OCP 위반 예시가 담긴 참조 파일과 모델에 실제로 보낸 코드를 구분해 읽었다.
ko039 | NEW | ko039 | 0.42 | 참조 쌍에는 위반 예시와 수정 예시가, 저장 응답 한 건에는 제출 코드와 프롬프트, 기록된 응답이 들어 있다.
ko040 | NEW | ko040 | 0.47 | 검토 지시만 비교하기 위해 각 프롬프트에 정확히 한 번 나오는 제출 코드를 공통 자리표시자로 바꿨다.
ko041 | NEW | ko042 | 0.02 | 이렇게 얻은 틀은 문자열이 같을 때 같은 틀로 셌다.
ko042 | SAME | ko041 | 1.00 | 저장 응답의 제출 코드를 모든 참조 쌍의 수정 전·후 소스와 대조했다.
ko043 | NEW | ko042 | 0.34 | 문자열 그대로 비교하고 양끝 공백을 제거해 한 번 더 비교했다.
ko044 | SAME | ko043 | 1.00 | Python 참조 쌍은 구문 트리로 파싱해 최상위 클래스의 메서드 선언 이름을 비교했다.
ko045 | NEW | ko061 | 0.10 | 이름이 사라졌다면 선언의 변화를 확인한 것이다.
ko046 | NEW | ko124 | 0.09 | 그 메서드를 상속을 통해 계속 호출할 수 있는지, 기존 호출자가 사용했는지, 그 사용을 보장했는지는 각각 별도의 근거가 필요하다.
ko047 | NEW | ko140 | 0.28 | 아카이브 감사는 ZIP 안의 JSON·JSONL을 읽는 정적 분석이었다.
ko048 | NEW | ko141 | 0.20 | §5–§6의 동작과 계약은 이 연구에서 작성한 예제를 해당 절의 조건으로 실행해 확인했다.
ko049 | NEW | ko047 | 0.06 | 부록 A에 입력 자료와 재현 명령을 적었다.
ko050 | NEW | ko048 | 0.31 | · Pehlivan 등은 위반 시나리오를 정해 코드 예시를 생성하고 다듬었다.
ko051 | NEW | ko142 | 0.05 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko052 | NEW | ko050 | 0.40 | OCP 아카이브에서 참조 쌍 48개와 저장 응답 768건을 따로 확인했다.
ko053 | NEW | ko051 | 0.31 | 제출 코드를 가린 뒤에는 서로 다른 지시문 틀 24개가 남았고, 네 전략 사이에서 정확히 일치하는 틀은 없었다.
ko054 | NEW | ko009 | 0.08 | 개별 사례에서 어떤 변경을 요청했고 어떤 호출을 계속 보장해야 하는지를 별도로 밝힌 틀도 없었다.
ko055 | EDIT | ko055 | 0.62 | 그중 Python 지시는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko056 | SAME | ko056 | 1.00 | 제출된 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko057 | NEW | ko057 | 0.04 | 새 도형을 지원할 때 이 분기가 수정 후보라는 판단은 코드에서 나온다.
ko058 | NEW | ko058 | 0.10 | 그 확장이 실제 요구인지, 넓이 계산을 옮겨도 기존의 너비 조회를 지원해야 하는지는 검토 지시에 적혀 있지 않다.
ko059 | NEW | ko059 | 0.16 | 너비 조회는 별도의 참조 쌍 37번에서 실제 편집 항목이 된다.
ko060 | EDIT | ko059 | 0.55 | 이 쌍에서는 넓이 계산을 도형 메서드로 옮기면서 선언을 뺐다.
ko061 | NEW | ko060 | 0.27 | 저장된 제출 코드와 모든 참조 쌍의 양쪽 소스를 대조했을 때, 원본 문자열 비교와 양끝 공백을 제거한 비교 모두에서 일치가 없었다.
ko062 | NEW | ko061 | 0.06 | 37번에서 직접 확인할 수 있는 것은 참조 소스에서 선언이 빠졌다는 사실까지다.
ko063 | NEW | ko062 | 0.21 | 그 삭제가 수정안을 거절할 이유가 되려면 너비 조회를 기존 호출자에게 보장했다는 근거가 더 있어야 한다.
ko064 | SAME | ko072 | 1.00 | ** 프롬프트 예시는 저장 JSONL 13행(ID 12)이다.
ko065 | SAME | ko073 | 1.00 | 참조 쌍 37번은 별도의 ground truth JSON 위치다.
ko066 | NEW | ko071 | 0.06 | · · · 평가 방법에 따라 확인할 수 있는 내용의 범위도 달라진다.
ko067 | NEW | ko066 | 0.34 | Bräuer 등(2018)은 전문가에게 측정 가능한 실천 규칙들이 설계 원칙을 얼마나 포착하는지 물었다.
ko068 | NEW | ko067 | 0.36 | Cabral 등(2024)은 기계학습 기능을 확장하는 상황에서 SOLID를 묶어서 적용한 코드에 대해 참가자가 느낀 이해도와 확장 용이성을 조사했다.
ko069 | NEW | ko068 | 0.35 | Zhu 등(2026)의 저장소 과제는 구체적인 변경을 주고 기능 테스트와 구조적 판정 기준을 적용한다.
ko070 | NEW | ko064 | 0.08 | 다음 절에서는 이미 작성한 수정안에 적용할 요구와 계약을 바꾼다.
ko071 | NEW | ko081 | 0.05 | 너비 조회에서 남았던 질문을 재현할 수 있는 비교다.
ko072 | NEW | ko091 | 0.08 | 기존 호출자에게 보장한 동작만 달라져도 같은 수정안의 판정이 바뀌는지 확인할 수 있다.
ko073 | NEW | ko074 | 0.21 | · · 마이어가 예로 든 도서관 목록을 작은 프로그램으로 만들었다.
ko074 | NEW | ko075 | 0.17 | 기술보고서를 새로 처리하는 수정안 하나를 검토 대상으로 삼았다.
ko075 | EDIT | ko076 | 0.50 | 수정안은 모듈을 하나 추가하고 기존 소스 파일 두 개는 바이트 단위로 그대로 둔다.
ko076 | EDIT | ko077 | 0.55 | 실행하면 기술보고서가 출력되고 정오표 요청은 여전히 거절된다.
ko077 | NEW | ko081 | 0.11 | 이 실행 결과와 새 모듈 추가를 허용한 편집 범위는 네 경우에서 같다.
ko078 | NEW | ko082 | 0.16 | 새 요구가 기술보고서까지만 포함하는지 정오표까지 포함하는지를 바꿨다.
ko079 | EDIT | ko083 | 0.72 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개의 미지원 자료 유형을 거절하는 동작을 보호한다.
ko080 | NEW | ko070 | 0.05 | 새 요구를 충족하고 적용되는 계약을 지켰을 때 표 2에서 승인으로 판정했다.
ko081 | NEW | ko086 | 0.06 | ** 누군가 검토 중에 “정오표도 이번에 지원해야 한다”고 알려 주면, 책 접두어에 대한 답을 기다릴 필요가 없다.
ko082 | NEW | ko123 | 0.10 | 수정안이 정오표를 거절한다는 사실만으로 결론이 난다.
ko083 | NEW | ko087 | 0.08 | 책 접두어가 보호된다는 사실도 그것만으로 거절을 결정한다.
ko084 | NEW | ko085 | 0.24 | 이 표에서는 기술보고서만 필요하고 책 접두어는 보장 대상이 아니라는 두 사실이 모두 필요하다.
ko085 | EDIT | ko088 | 0.50 | 같은 편집 범위에서 새 모듈 하나로 두 자료 유형을 처리하고 모든 보호 동작을 지키는 수정안도 별도로 실행했다.
ko086 | NEW | — | 0.00 | 표 2에서 알려진 사실에 맞는 행만 남겨 보자.
ko087 | NEW | ko092 | 0.12 | 실제 명세가 이 비교에 포함돼 있다는 전제에서는 적어도 한 행이 남는다.
ko088 | NEW | ko090 | 0.13 | 남은 행이 모두 같은 결론을 가리키면 일부 조건이 여전히 미공개여도 판정을 내릴 수 있다.
ko089 | NEW | ko091 | 0.15 | 승인과 거절이 함께 남으면 판정을 조건부로 말하거나, 결론을 가를 사실을 확인할 때까지 보류할 수 있다.
ko090 | NEW | ko093 | 0.13 | 같은 입력에서 언제나 하나의 답을 내도록 한 규칙은 정답이 반대인 두 행을 동시에 맞힐 수 없다.
ko091 | NEW | ko095 | 0.20 | 부록 A는 이 비교에서 가능한 정보 공개 조건 아홉 가지를 보여 준다.
ko092 | NEW | ko095 | 0.08 | 각 칸은 한 사례에서 설계한 정보 조건이다.
ko093 | SAME | ko096 | 1.00 | · 도서관 실험에서 확인한 것은 주어진 수정안의 적격성이었다.
ko094 | SAME | ko097 | 1.00 | 다른 수정안이 더 적은 비용으로 같은 요구를 처리할 수 있는지는 아직 별도 문제다.
ko095 | SAME | ko098 | 1.00 | 도형 예제로 돌아가, 어떤 변경에 대비할지와 새 기능을 어디에서 호출할지에 따라 기존 파일을 얼마나 수정하는지 비교한다.
ko096 | SAME | ko099 | 1.00 | 여기서 세는 것은 실행한 후보들의 수정 파일 수이지 가능한 구현 전체의 최솟값이 아니다.
ko097 | SAME | ko100 | 1.00 | 도형별 배치에서는 삼각형을 새 파일 하나로 추가했고, 이름표 연산을 추가할 때는 원과 사각형의 파일을 고쳤다.
ko098 | SAME | ko101 | 1.00 | 연산별 배치에서는 반대로 삼각형을 추가할 때 그리기 파일을 고쳤고, 이름표 연산은 새 파일에 뒀다.
ko099 | SAME | ko102 | 1.00 | 네 수정안이 모두 기능 검사를 통과했지만 기존 파일을 덜 건드리는 배치는 요구에 따라 달랐다(그림 1A).
ko100 | SAME | ko103 | 1.00 | 두 번째 비교에서는 같은 배치 렌더링 함수를 추가했다.
ko101 | SAME | ko104 | 1.00 | 이 함수는 도형 목록을 받아 각 렌더링 결과를 대괄호로 감싼다.
ko102 | SAME | ko105 | 1.00 | 도형별 배치에서 변환을 각 도형 파일이 맡아야 하면 원과 사각형 파일을 고친다.
ko103 | SAME | ko106 | 1.00 | 공용 어댑터를 허용하면 두 배치 모두 새 파일 하나로 기능을 제공할 수 있다고 예측했다.
ko104 | SAME | ko107 | 1.00 | 실행한 네 후보는 모두 입력 순서와 중복을 보존하고 빈 목록과 미지원 도형을 명세대로 처리했다.
ko105 | SAME | ko108 | 1.00 | 각 후보는 원과 사각형의 기존 렌더링을 유지했다.
ko106 | SAME | ko109 | 1.00 | 기존 파일 두 개를 고친 것은 도형 파일이 변환을 맡은 후보뿐이었다.
ko107 | SAME | ko110 | 1.00 | 네 후보 모두 새 파일 하나를 추가했다(그림 1B).
ko108 | SAME | ko111 | 1.00 | ** A는 삼각형 추가와 이름표 연산 추가를 비교한다.
ko109 | SAME | ko112 | 1.00 | B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다.
ko110 | SAME | ko113 | 1.00 | B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.
ko111 | SAME | ko114 | 1.00 | · · · · 세 번째 비교에서는 배치 함수 대신 기존 렌더링의 결과 하나를 선택적으로 감싸는 옵션을 사용했다.
ko112 | SAME | ko115 | 1.00 | 새 모듈을 호출할 수 있는 경우에는 두 배치가 기존 파일을 그대로 뒀다.
ko113 | SAME | ko116 | 1.00 | 같은 모듈을 추가한 상태에서 기존 함수에 를 넘기면 함수는 그 인자를 받지 못했다.
ko114 | SAME | ko117 | 1.00 | 기존 함수로 옵션을 제공한 후보는 연산별 배치에서 파일 하나, 도형별 배치에서 두 개를 고쳤다.
ko115 | SAME | ko118 | 1.00 | 기존 함수가 외부 변환 모듈을 불러올 수 있도록 이미 구성된 별도 기준선에서는 두 배치 모두 새 파일 하나를 추가해 기존 호출 경로로 옵션을 제공했다(표 3).
ko116 | SAME | ko119 | 1.00 | ** 확장 지점은 세 번째 행의 기준선에 이미 있었다.
ko117 | SAME | ko120 | 1.00 | 따라서 이 행의 0개를 첫 설계에서 확장 지점을 처음 만드는 비용까지 포함한 결과로 읽어서는 안 된다.
ko118 | SAME | ko121 | 1.00 | 여기서는 확장 지점이 도입된 비용을 별도로 측정하지 않았다.
ko119 | SAME | ko122 | 1.00 | 같은 어댑터를 추가해도 기존 함수에서는 옵션을 쓸 수 없었던 대조 실행을 포함했다.
ko120 | SAME | ko123 | 1.00 | · 기존 파일 수정 수가 적다는 사실만으로 변경에 더 잘 대응하는 설계라고 할 수는 없다.
ko121 | SAME | ko124 | 1.00 | 새 파일을 추가할 수 있어도 그 파일이 실행되려면 호출자가 쓸 수 있는 경로가 필요하다.
ko122 | SAME | ko125 | 1.00 | 표 3의 마지막 행은 확장 지점이 이미 있는 상태에서 이후에 고친 파일만 센다.
ko123 | SAME | ko126 | 1.00 | 여기에 든 수정 수는 실행한 후보에 관한 관찰이다.
ko124 | SAME | ko127 | 1.00 | 독립적으로 작성한 요구에서도 어떤 경로가 작동할지 예측할 수 있는지, 파일 수정 수가 실제 유지보수 부담과 어떻게 연결되는지는 남은 질문이다.
ko125 | SAME | ko128 | 1.00 | 서론의 그리기 함수가 잘못됐는지는 정렬을 누가 맡았는지에 달려 있었다.
ko126 | SAME | ko129 | 1.00 | 벤치마크는 모델의 응답을 참조 라벨과 대조해 분류 성능을 잰다.
ko127 | SAME | ko130 | 1.00 | 그 판정을 구체적인 수정안에 적용하려면 어떤 기능이 필요한지, 어떤 동작을 기존 호출자에게 약속했는지를 확인해야 한다.
ko128 | SAME | ko131 | 1.00 | 도서관 예제에서는 정오표 요구만으로 수정안을 거절할 수 있었다.
ko129 | SAME | ko132 | 1.00 | 기술보고서만 필요한 경우에는 책 접두어 계약이 결론을 갈랐다.
ko130 | SAME | ko133 | 1.00 | 어떤 수정안이 가능한지를 비교할 때는 호출자가 새 동작을 받을 수 있는 경로도 확인해야 한다.
ko131 | SAME | ko134 | 1.00 | 검토 의견으로 변경을 요구하려면 어느 요구나 계약을 근거로 삼았는지, 어느 호출 경로에 적용되는지를 밝힐 수 있어야 한다.
ko132 | SAME | ko135 | 1.00 | 그러면 개발자는 이미 내려진 결론의 근거를 확인하거나, 보류된 판정을 가를 사실을 더 찾을 수 있다.
ko133 | SAME | ko136 | 1.00 | 이 결과는 한 벤치마크의 저장 자료와 여기서 구성해 실행한 후보의 범위에서 성립한다.
ko134 | SAME | ko137 | 1.00 | 여기서 더 나아가려면 SOLID를 대체할 공리를 선언하기보다, 어떤 변경과 계약, 권한과 호출 경로가 주어졌을 때 설계의 유불리가 어떻게 달라지는지 예측할 수 있는 표현을 찾아야 한다.
ko135 | SAME | ko138 | 1.00 | 그런 표현이 실제 독립 요구에서도 작동한다면, 익숙한 원칙이 유용한 이유뿐 아니라 그 조언을 따르지 않는 설계가 더 나은 조건도 설명할 수 있을 것이다.
ko136 | SAME | ko139 | 1.00 | 이 가능성은 이번 논문의 결과가 아니라 다음에 검증할 가설로 남긴다.
ko137 | SAME | ko140 | 1.00 | §3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다.
ko138 | SAME | ko141 | 1.00 | §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다.
ko139 | SAME | ko142 | 1.00 | 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다.
ko140 | SAME | ko143 | 1.00 | 그림 1의 소스와 출력 위치는 그림 캡션에 있다.
ko141 | NEW | ko054 | 0.07 | 아래에서 ‘미공개’는 해당 항목의 두 값이 모두 가능하다는 뜻이다.
ko142 | NEW | ko089 | 0.08 | 보류는 공개된 정보와 양립하는 행 가운데 승인과 거절이 모두 남았을 때의 판정이다.
Summary ko: SAME 90, EDIT 6, NEW 46

### en (154 segmented sentences)
en001 | SAME | en001 | 1.00 | In 1996, Robert Martin described a function that drew the shapes in a list in order.
en002 | SAME | en002 | 1.00 | A triangle could be added without editing the function if the triangle supplied its own drawing operation.
en003 | SAME | en003 | 1.00 | Martin then introduced a new requirement.
en004 | SAME | en004 | 1.00 | Every circle had to be drawn before any square.
en005 | SAME | en005 | 1.00 | Given a list that begins with a square, the same function still draws the square first.
en006 | SAME | en006 | 1.00 | Who was supposed to sort the list?
en007 | SAME | en007 | 1.00 | If the caller was to put the circles first, the drawing function already does its job.
en008 | SAME | en008 | 1.00 | If the function was to guarantee that order for any input, it falls short.
en009 | SAME | en009 | 1.00 | Reading the code tells a reviewer what gets drawn first.
en010 | SAME | en010 | 1.00 | The reviewer needs the agreement between caller and function to tell whether that is a defect.
en011 | SAME | en011 | 1.00 | Martin called the design closed with respect to the addition of a shape.
en012 | SAME | en012 | 1.00 | The sorting requirement gives the same code a different test.
en013 | SAME | en013 | 1.00 | That is where our question about the open–closed principle (OCP) begins.
en014 | SAME | en014 | 1.00 | When a reviewer calls a proposed edit a violation, can the author recover from the verdict what the program was expected to accommodate or preserve?
en015 | SAME | en015 | 1.00 | We use *over-axiomatization* for the risk of treating such a verdict as settled when those premises are still open.
en016 | SAME | en016 | 1.00 | A benchmark that scores agreement with reference labels makes that question tractable.
en017 | SAME | en017 | 1.00 | Its archive lets us inspect the information actually supplied for classification.
en018 | SAME | en018 | 1.00 | To test what an acceptance decision requires, we hold a patch fixed and vary the task and the promise to existing callers.
en019 | SAME | en019 | 1.00 | We then return to drawing to see when a separate implementation can deliver an extension through the call the user already makes.
en020 | SAME | en020 | 1.00 | · · In 1996 Martin attributed the principle to Bertrand Meyer, citing page 23 of the 1988 first edition.
en021 | SAME | en021 | 1.00 | In Meyer’s account a module is closed once other modules can use it on the basis of a stable description.
en022 | SAME | en022 | 1.00 | His library example gives that stability a concrete test.
en023 | SAME | en023 | 1.00 | When technical reports become a new category, a program that handles each publication type explicitly may require edits to, or recompilation of, existing modules.
en024 | SAME | en024 | 1.00 | The choice of where to handle the new type matters to the modules that already depend on the catalog.
en025 | SAME | en025 | 1.00 | Having to edit a module to extend it was the issue in a June 1995 public exchange.
en026 | SAME | en026 | 1.00 | Kyle Brown argued that developers had to be able to fix a badly designed class.
en027 | SAME | en027 | 1.00 | Martin’s reply distinguished the right to edit a class from the need to edit it for an anticipated extension.
en028 | SAME | en028 | 1.00 | The design would still have to anticipate the right change.
en029 | SAME | en029 | 1.00 | The label SOLID appears in the public record by 2007.
en030 | SAME | en030 | 1.00 | In a 2009 discussion of interfaces, the distinction between a routine internal class and a public plugin API still mattered to the participants’ advice.
en031 | SAME | en031 | 1.00 | These sources document particular uses and disagreements about the principle.
en032 | SAME | en032 | 1.00 | A causal history of the acronym would require evidence of what changed as the label circulated.
en033 | SAME | en033 | 1.00 | · · In the 1996 article Martin made sorting part of .
en034 | SAME | en034 | 1.00 | In one implementation, puts a circle before a square by inspecting the other shape.
en035 | SAME | en035 | 1.00 | A new rule about where a third type ranks against a circle can send the edit back into .
en036 | SAME | en036 | 1.00 | Martin moved the ranking of types into a table, so putting squares ahead of circles becomes a matter of swapping two entries.
en037 | SAME | en037 | 1.00 | If the next request were to sort individual shapes by area, the table would need information it does not contain.
en038 | SAME | en038 | 1.00 | Later in the article Martin uses in two routines.
en039 | SAME | en039 | 1.00 | One version of recognizes circles and squares. selects squares.
en040 | SAME | en040 | 1.00 | The first routine leaves a shape undrawn when its job is to draw them all.
en041 | SAME | en041 | 1.00 | The second skips exactly the shapes it is supposed to skip.
en042 | SAME | en042 | 1.00 | Here the names and stated jobs make the distinction available to the reader.
en043 | SAME | en043 | 1.00 | What can a classification reviewer establish when the input consists of code and a prompt?
en044 | NEW | en045 | 0.18 | · · We distinguished the reference examples of OCP violations from the code actually sent to models.
en045 | SAME | en045 | 1.00 | A reference pair contains a violation example and its revision.
en046 | EDIT | en046 | 0.77 | A saved response record contains the submitted code, its prompt, and the recorded response.
en047 | EDIT | en047 | 0.53 | To isolate the instructions, we replaced the single exact occurrence of the submitted code in each saved prompt with a common placeholder.
en048 | NEW | en048 | 0.22 | We counted the resulting templates by exact string identity.
en049 | EDIT | en049 | 0.83 | We compared each saved submission with both sides of every reference pair, first as stored and then after trimming whitespace from both ends.
en050 | EDIT | en050 | 0.87 | For the Python reference pairs we parsed the syntax trees and compared method names declared in top-level classes, excluding names that begin with an underscore.
en051 | NEW | en051 | 0.29 | A missing name in this comparison establishes a change in declarations.
en052 | NEW | en052 | 0.29 | Whether a caller could still use the method through inheritance, actually used it, or was promised continued access each requires separate evidence.
en053 | NEW | en153 | 0.26 | The archive audit was a static analysis of the JSON and JSONL within the ZIP.
en054 | NEW | en053 | 0.40 | The behavior and contract checks in Sections 5–6 come from running fixtures built for this study under the conditions specified in those sections.
en055 | NEW | en055 | 0.44 | Appendix A identifies the inputs and the reproduction commands.
en056 | EDIT | en056 | 0.88 | · Pehlivan et al. specified violation scenarios and refined the generated examples.
en057 | NEW | en057 | 0.25 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en058 | NEW | en142 | 0.47 | The benchmark compares model classifications with the reference labels.
en059 | EDIT | en058 | 0.51 | For OCP we counted 48 reference pairs and 768 saved response records separately.
en060 | EDIT | en059 | 0.59 | Masking the submitted code left 24 distinct instruction templates, with no exact match across the four strategies.
en061 | NEW | en060 | 0.37 | None of those templates separately stated which change an individual case called for or what its existing callers had been promised.
en062 | EDIT | en063 | 0.84 | One saved Python prompt directs the reviewer to repeated branches where polymorphism would fit.
en063 | SAME | en064 | 1.00 | The submitted checks the shape type before calculating the area of a circle or rectangle.
en064 | NEW | en065 | 0.26 | The branch gives the reviewer somewhere to look if a new shape is requested.
en065 | NEW | en066 | 0.34 | The prompt leaves open whether that is the task and whether calls reading a rectangle’s width must still work after its area calculation moves.
en066 | NEW | en082 | 0.20 | Width becomes a concrete issue in the separate reference pair 37.
en067 | EDIT | en067 | 0.63 | That revision moves area calculation onto the shapes and drops the declaration of .
en068 | EDIT | en068 | 0.50 | No saved submission matched either side of any reference pair, whether we compared the stored strings or trimmed whitespace at their ends.
en069 | NEW | en067 | 0.15 | In pair 37 we can establish that the declaration was removed.
en070 | NEW | en070 | 0.32 | Turning its removal into a reason to reject the patch would require evidence that existing callers were promised continued access to the width.
en071 | SAME | en080 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en072 | SAME | en081 | 1.00 | ** The saved prompt is on JSONL line 13 (record ID 12).
en073 | EDIT | en082 | 0.69 | Reference pair 37 is in a separate ground-truth JSON file.
en074 | NEW | en079 | 0.19 | · · · These distinctions matter when choosing an instrument.
en075 | NEW | en074 | 0.48 | Bräuer et al. (2018) asked experts how much of a design principle their measurable practices covered.
en076 | NEW | en075 | 0.46 | Cabral et al. (2024) asked participants about understanding and ease of extension in a machine-learning scenario under a bundled SOLID treatment.
en077 | EDIT | en076 | 0.58 | Zhu et al. (2026) gave specific repository change tasks and checked them against functional tests and structural oracles.
en078 | NEW | en018 | 0.19 | In the next comparison we hold a completed patch fixed and vary the request and contract against which it is judged.
en079 | NEW | en143 | 0.19 | This lets us reproduce the open question about the width getter in a setting where we can change what existing callers are promised and check whether the same patch still qualifies.
en080 | NEW | en083 | 0.26 | · · We built a small version of Meyer’s library catalog and took one patch that extends it to technical reports.
en081 | NEW | en085 | 0.43 | The patch adds one module and leaves both existing source files byte-for-byte identical.
en082 | EDIT | en086 | 0.59 | It renders technical reports and still rejects requests for errata.
en083 | NEW | en087 | 0.27 | It also changes one existing output.
en084 | NEW | en087 | 0.33 | The prefix in a book rendering goes from to .
en085 | NEW | en089 | 0.26 | The observed behavior and the permission to add a module are the same in all four cases.
en086 | NEW | en090 | 0.45 | The request may cover technical reports alone or require errata as well.
en087 | EDIT | en091 | 0.65 | Both variants of the caller contract protect the rendering of journals and proceedings and the rejection of a separate unsupported type.
en088 | SAME | en092 | 1.00 | The broader contract also protects the original book prefix.
en089 | NEW | en093 | 0.31 | In Table 2 a patch qualifies for acceptance when it meets the request and preserves the applicable contract.
en090 | NEW | en003 | 0.17 | Two requirements for accepting a fixed patch.
en091 | NEW | en100 | 0.14 | ** Suppose the reviewer learns that the release must support errata.
en092 | NEW | en096 | 0.17 | The patch rejects errata, so the reviewer can reject it while the book contract is still open.
en093 | NEW | en144 | 0.22 | Learning that the book prefix is protected also settles rejection on its own.
en094 | EDIT | en095 | 0.53 | Acceptance in this table takes two facts: technical reports are the whole request, and the book prefix is outside the contract.
en095 | EDIT | en098 | 0.85 | We also ran a separate patch that adds one module within the same edit boundary, handles both new types, and preserves every protected observation.
en096 | NEW | en099 | 0.19 | Keep only the rows of Table 2 compatible with what the reviewer knows.
en097 | NEW | en102 | 0.22 | At least one row remains if the actual specification is among the cases considered.
en098 | NEW | en101 | 0.15 | If the remaining rows agree, their common verdict is available now.
en099 | NEW | en101 | 0.36 | If they disagree, the reviewer can give a conditional verdict or wait for the fact that resolves the disagreement.
en100 | NEW | en103 | 0.17 | A rule forced to give a single answer on identical inputs cannot get both of two rows right when the correct answers differ.
en101 | NEW | en105 | 0.29 | Appendix A shows all nine disclosure settings.
en102 | NEW | en105 | 0.16 | Each cell is a designed information condition within this one case.
en103 | SAME | en106 | 1.00 | · Section 5 established whether one patch met a stated request and contract.
en104 | SAME | en107 | 1.00 | It did not determine the least costly way to meet them.
en105 | SAME | en108 | 1.00 | Returning to the drawing fixture, we ask which source boundaries the implemented candidates cross when the request, permitted placement, or caller route changes.
en106 | SAME | en109 | 1.00 | The counts describe those candidates, not a minimum over all possible implementations.
en107 | SAME | en110 | 1.00 | We first varied the request.
en108 | SAME | en111 | 1.00 | In the shape layout we added a triangle in one new file and edited the circle and square files to add a labeling operation.
en109 | SAME | en112 | 1.00 | In the operation layout we edited the drawing file to add the triangle and put the labeling operation in a new file.
en110 | SAME | en113 | 1.00 | All four candidates passed their functional checks.
en111 | SAME | en114 | 1.00 | Which layout left more existing files intact depended on the request (Figure 1A).
en112 | SAME | en115 | 1.00 | We then added the same batch-rendering function to both layouts.
en113 | SAME | en116 | 1.00 | It takes a list of shapes and brackets each rendered result.
en114 | SAME | en117 | 1.00 | We predicted that requiring the item transformation to live in the shape files would entail editing both files in the shape layout.
en115 | SAME | en118 | 1.00 | If a shared adapter was allowed, we predicted that either layout could add the feature in one new file.
en116 | SAME | en119 | 1.00 | All four candidates preserved order and duplicates, handled empty lists and unsupported shapes as specified, and preserved the existing circle and square renderings.
en117 | SAME | en120 | 1.00 | The candidate placing both transformations in the shape files edited two existing files.
en118 | SAME | en121 | 1.00 | All four added one file (Figure 1B).
en119 | SAME | en122 | 1.00 | Existing source files edited.
en120 | SAME | en123 | 1.00 | ** Panel A compares adding a triangle with adding a labeling operation.
en121 | SAME | en124 | 1.00 | Panel B holds the batch-rendering request fixed and varies the placement rule.
en122 | SAME | en125 | 1.00 | All four candidates in panel B passed the new and legacy behavior checks and added one file each.
en123 | SAME | en126 | 1.00 | · · · · The third comparison used an option to bracket a single rendering through the existing function.
en124 | SAME | en127 | 1.00 | Candidates that offered a new entry point left the existing files intact in both layouts.
en125 | SAME | en128 | 1.00 | With the same adapter added, the original functions still rejected .
en126 | SAME | en129 | 1.00 | The candidates offering the option through the original functions edited one file in the operation layout and two in the shape layout.
en127 | SAME | en130 | 1.00 | In a separate baseline whose original function could already load an external decorator, each layout delivered the option through the original entry point by adding a single file (Table 3).
en128 | SAME | en131 | 1.00 | Call paths for the new rendering option.
en129 | SAME | en132 | 1.00 | ** The hook was already present in the last row’s baseline.
en130 | SAME | en133 | 1.00 | Its zero-edits result does not include the cost of introducing that hook into the earlier baseline.
en131 | SAME | en134 | 1.00 | We did not measure that initial investment.
en132 | SAME | en135 | 1.00 | The negative control adds the same adapter and finds that the option remains unavailable through the original function.
en133 | SAME | en136 | 1.00 | · Fewer changed files do not by themselves establish a more maintainable design.
en134 | SAME | en137 | 1.00 | Permission to add a file needs to be paired with a path that the caller can actually use.
en135 | SAME | en138 | 1.00 | The last row of Table 3 starts counting after the hook is already in place.
en136 | SAME | en139 | 1.00 | These file counts describe the tested candidates.
en137 | SAME | en140 | 1.00 | Whether we can predict working paths for independently authored requests, and how these counts relate to maintenance effort, remain open.
en138 | SAME | en141 | 1.00 | Whether the drawing routine falls short depends on who must sort the list.
en139 | SAME | en142 | 1.00 | The benchmark measures classification performance by comparing model responses with its reference labels.
en140 | SAME | en143 | 1.00 | Applying a finding to a specific patch also requires knowing what change the patch must deliver and which behavior existing callers were promised.
en141 | SAME | en144 | 1.00 | In the catalog example, the errata requirement can settle a rejection on its own.
en142 | SAME | en145 | 1.00 | When only technical reports are needed, the verdict turns on the promise about the book prefix.
en143 | SAME | en146 | 1.00 | Comparing possible edits also requires knowing how the new behavior can reach its callers.
en144 | SAME | en147 | 1.00 | A review that calls for an edit should identify the request or commitment it relies on and the call path to which it applies.
en145 | SAME | en148 | 1.00 | The developer can then check the grounds for the verdict or identify the remaining fact that would settle it.
en146 | SAME | en149 | 1.00 | The evidence here covers the saved material of one benchmark and the candidates we constructed and ran.
en147 | SAME | en150 | 1.00 | Rather than announce a new set of axioms, the next step is to ask whether changes, protected commitments, authority, and caller routes can be represented in a form that predicts when one design has an advantage over anot
en148 | SAME | en151 | 1.00 | Such an account would be valuable if it explained both the usefulness of familiar principles and the conditions under which their preferred design loses.
en149 | SAME | en152 | 1.00 | The present paper poses that hypothesis; it does not establish it.
en150 | SAME | en153 | 1.00 | For Sections 3–4 the audit reads the archived JSON and JSONL.
en151 | SAME | en154 | 1.00 | For Sections 5–6 the fixtures run the examples constructed for this study.
en152 | SAME | en155 | 1.00 | The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.
en153 | NEW | en046 | 0.08 | When a field is withheld, both of its recorded values remain possible.
en154 | NEW | en070 | 0.11 | Defer means that at least one compatible row accepts the patch and at least one rejects it.
Summary en: SAME 98, EDIT 16, NEW 40

## v10 · [Source](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/PAPER_B_BILINGUAL_INTEGRATED_10_20261117.md)
### ko (138 segmented sentences)
ko001 | SAME | ko001 | 1.00 | 로버트 마틴이 1996년에 예로 든 함수는 목록에 들어온 순서대로 도형을 그린다.
ko002 | SAME | ko002 | 1.00 | 삼각형에 자기 자신을 그리는 동작이 있으면 이 함수에 손대지 않고도 삼각형을 추가할 수 있다.
ko003 | SAME | ko003 | 1.00 | 목록의 맨 앞에 사각형이 있으면 함수는 여전히 그 사각형부터 그린다.
ko004 | SAME | ko004 | 1.00 | 호출자가 원을 앞에 놓아 목록을 넘기기로 했다면 함수는 제 일을 한다.
ko005 | SAME | ko005 | 1.00 | 어떤 목록을 받더라도 함수가 순서를 보장하기로 했다면 수정이 필요하다.
ko006 | SAME | ko006 | 1.00 | 코드를 읽으면 무엇이 먼저 그려지는지 알 수 있다.
ko007 | SAME | ko007 | 1.00 | 그 결과가 잘못됐는지를 판단하려면 호출자와 함수 사이에 어떤 약속이 있었는지도 알아야 한다.
ko008 | SAME | ko008 | 1.00 | 도형 하나를 더 추가할 때 닫혀 있던 설계도 함수가 직접 정렬을 책임지는 순간 같은 방식으로 확장할 수 없었다.
ko009 | SAME | ko009 | 1.00 | 개방–폐쇄 원칙(OCP)을 근거로 어떤 수정안에 ‘위반’이라고 표시할 때도, 그 판단을 받은 개발자는 프로그램이 어떤 변화에 대비해야 했고 어떤 동작을 계속 보장해야 했는지 물을 수 있다.
ko010 | SAME | ko010 | 1.00 | 이 전제가 정해지기 전에 판정부터 확정하는 위험을 이 글에서는 설계 조언의 ‘과도한 공리화’라고 부른다.
ko011 | SAME | ko011 | 1.00 | 분류 벤치마크에는 모델이 무엇을 보고 위반 여부를 답했는지 기록이 남아 있다.
ko012 | SAME | ko012 | 1.00 | 그 기록을 읽어 분류에 주어진 근거를 확인한다.
ko013 | SAME | ko013 | 1.00 | 코드가 같은데도 새 요구와 기존 호출자에 대한 약속에 따라 결론이 달라지는지 살핀다.
ko014 | SAME | ko014 | 1.00 | 그 뒤 도형 예제로 돌아가 새 기능을 별도 파일에 넣었을 때 기존 호출자가 사용하던 함수로도 그 기능을 쓸 수 있는지 확인한다.
ko015 | SAME | ko015 | 1.00 | · · 마틴은 1996년 글에서 베르트랑 마이어의 1988년 초판 23쪽을 인용하며 원칙의 출처를 밝혔다.
ko016 | SAME | ko016 | 1.00 | 마이어가 말한 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 사용할 수 있는 모듈이다.
ko017 | SAME | ko017 | 1.00 | 마이어는 자료의 종류를 하나씩 구별해 처리하는 도서관 프로그램을 예로 든다.
ko018 | SAME | ko018 | 1.00 | 기술보고서가 새로운 자료 유형으로 들어오면 이미 쓰이던 모듈까지 고치거나 다시 컴파일해야 할 수 있다.
ko019 | SAME | ko019 | 1.00 | 새 자료를 처리하는 코드를 어디에 두느냐는 기존 모듈이 무엇에 의존할 수 있느냐와 맞물린다.
ko020 | SAME | ko020 | 1.00 | 1995년 6월 공개 토론에서는 기존 모듈을 손댈 수 있다는 것과 손대야 한다는 것의 차이가 쟁점이었다.
ko021 | SAME | ko021 | 1.00 | 카일 브라운은 잘못 설계된 클래스라면 개발자가 소스를 고칠 수 있어야 한다고 했다.
ko022 | SAME | ko022 | 1.00 | 마틴의 답은 예상한 확장을 하려면 기존 소스를 반드시 고쳐야 하는지에 관한 것이었다.
ko023 | SAME | ko023 | 1.00 | 어떤 변경이 생길지 미리 짚어야 한다는 어려움은 남았다.
ko024 | SAME | ko024 | 1.00 | 2007년 공개 기록에는 다섯 원칙을 묶은 SOLID라는 이름이 나온다.
ko025 | SAME | ko025 | 1.00 | 2009년의 인터페이스 논쟁에서도 내부 클래스의 인터페이스와 공개 플러그인 API에는 서로 다른 조언이 제시됐다.
ko026 | SAME | ko026 | 1.00 | 이 자료들은 원칙이 어떻게 쓰이고 논쟁됐는지 보여 준다.
ko027 | SAME | ko027 | 1.00 | SOLID라는 이름이 퍼지면서 적용 조건에 대한 판단이 실제로 바뀌었는지는 별도의 근거가 필요한 역사적 질문이다.
ko028 | SAME | ko028 | 1.00 | · · 1996년 글에서 마틴은 목록 정렬을 가 맡게 했다.
ko029 | SAME | ko029 | 1.00 | 한 구현에서는 가 상대 도형을 검사해 사각형이면 원을 먼저 놓는다.
ko030 | SAME | ko030 | 1.00 | 세 번째 도형과 원의 순서를 정해야 하면 을 다시 고칠 수 있다.
ko031 | SAME | ko031 | 1.00 | 도형 종류별 순서를 표로 옮기면 사각형을 원보다 먼저 그리기 위해 두 항목의 위치만 바꾸면 된다.
ko032 | SAME | ko032 | 1.00 | 그다음 요구가 개별 도형을 넓이순으로 그리는 것이라면 표에 없는 정보가 필요하다.
ko033 | SAME | ko033 | 1.00 | 같은 글 후반에서 마틴은 를 쓰는 함수 둘을 제시한다.
ko034 | SAME | ko034 | 1.00 | 의 한 구현은 원과 사각형을 골라 그리고, 는 사각형을 골라 그린다.
ko035 | SAME | ko035 | 1.00 | 모든 도형을 그려야 하는 함수라면 그림 하나가 빠진 것이고, 사각형만 그려야 하는 함수라면 건너뛰는 것이 맞다.
ko036 | SAME | ko036 | 1.00 | 여기서는 함수 이름과 설명을 읽으면 각각 무엇을 맡았는지 알 수 있다.
ko037 | SAME | ko037 | 1.00 | 분류를 맡은 검토자에게 코드와 프롬프트가 주어졌을 때는 그 책임을 어디까지 확인할 수 있을까?
ko038 | SAME | ko038 | 1.00 | · · OCP 위반 예시가 담긴 참조 파일과 모델에 실제로 보낸 코드를 구분해 읽었다.
ko039 | SAME | ko039 | 1.00 | 참조 쌍에는 위반 예시와 수정 예시가, 저장 응답 한 건에는 제출 코드와 프롬프트, 기록된 응답이 들어 있다.
ko040 | SAME | ko040 | 1.00 | 검토 지시만 비교하기 위해 각 프롬프트에 정확히 한 번 나오는 제출 코드를 공통 자리표시자로 바꿨다.
ko041 | SAME | ko041 | 1.00 | 이렇게 얻은 틀은 문자열이 같을 때 같은 틀로 셌다.
ko042 | SAME | ko042 | 1.00 | 저장 응답의 제출 코드를 모든 참조 쌍의 수정 전·후 소스와 대조했다.
ko043 | SAME | ko043 | 1.00 | 문자열 그대로 비교하고 양끝 공백을 제거해 한 번 더 비교했다.
ko044 | SAME | ko044 | 1.00 | Python 참조 쌍은 구문 트리로 파싱해 최상위 클래스의 메서드 선언 이름을 비교했다.
ko045 | SAME | ko045 | 1.00 | 이름이 사라졌다면 선언의 변화를 확인한 것이다.
ko046 | SAME | ko046 | 1.00 | 그 메서드를 상속을 통해 계속 호출할 수 있는지, 기존 호출자가 사용했는지, 그 사용을 보장했는지는 각각 별도의 근거가 필요하다.
ko047 | SAME | ko047 | 1.00 | 아카이브 감사는 ZIP 안의 JSON·JSONL을 읽는 정적 분석이었다.
ko048 | SAME | ko048 | 1.00 | §5–§6의 동작과 계약은 이 연구에서 작성한 예제를 해당 절의 조건으로 실행해 확인했다.
ko049 | SAME | ko049 | 1.00 | 부록 A에 입력 자료와 재현 명령을 적었다.
ko050 | SAME | ko050 | 1.00 | · Pehlivan 등은 위반 시나리오를 정해 코드 예시를 생성하고 다듬었다.
ko051 | SAME | ko051 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko052 | SAME | ko052 | 1.00 | OCP 아카이브에서 참조 쌍 48개와 저장 응답 768건을 따로 확인했다.
ko053 | SAME | ko053 | 1.00 | 제출 코드를 가린 뒤에는 서로 다른 지시문 틀 24개가 남았고, 네 전략 사이에서 정확히 일치하는 틀은 없었다.
ko054 | SAME | ko054 | 1.00 | 개별 사례에서 어떤 변경을 요청했고 어떤 호출을 계속 보장해야 하는지를 별도로 밝힌 틀도 없었다.
ko055 | SAME | ko055 | 1.00 | 그중 Python 지시는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko056 | SAME | ko056 | 1.00 | 제출된 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko057 | SAME | ko057 | 1.00 | 새 도형을 지원할 때 이 분기가 수정 후보라는 판단은 코드에서 나온다.
ko058 | SAME | ko058 | 1.00 | 그 확장이 실제 요구인지, 넓이 계산을 옮겨도 기존의 너비 조회를 지원해야 하는지는 검토 지시에 적혀 있지 않다.
ko059 | SAME | ko059 | 1.00 | 너비 조회는 별도의 참조 쌍 37번에서 실제 편집 항목이 된다.
ko060 | SAME | ko060 | 1.00 | 이 쌍에서는 넓이 계산을 도형 메서드로 옮기면서 선언을 뺐다.
ko061 | SAME | ko061 | 1.00 | 저장된 제출 코드와 모든 참조 쌍의 양쪽 소스를 대조했을 때, 원본 문자열 비교와 양끝 공백을 제거한 비교 모두에서 일치가 없었다.
ko062 | SAME | ko062 | 1.00 | 37번에서 직접 확인할 수 있는 것은 참조 소스에서 선언이 빠졌다는 사실까지다.
ko063 | SAME | ko063 | 1.00 | 그 삭제가 수정안을 거절할 이유가 되려면 너비 조회를 기존 호출자에게 보장했다는 근거가 더 있어야 한다.
ko064 | SAME | ko064 | 1.00 | ** 프롬프트 예시는 저장 JSONL 13행(ID 12)이다.
ko065 | SAME | ko065 | 1.00 | 참조 쌍 37번은 별도의 ground truth JSON 위치다.
ko066 | SAME | ko066 | 1.00 | · · · 평가 방법에 따라 확인할 수 있는 내용의 범위도 달라진다.
ko067 | SAME | ko067 | 1.00 | Bräuer 등(2018)은 전문가에게 측정 가능한 실천 규칙들이 설계 원칙을 얼마나 포착하는지 물었다.
ko068 | SAME | ko068 | 1.00 | Cabral 등(2024)은 기계학습 기능을 확장하는 상황에서 SOLID를 묶어서 적용한 코드에 대해 참가자가 느낀 이해도와 확장 용이성을 조사했다.
ko069 | SAME | ko069 | 1.00 | Zhu 등(2026)의 저장소 과제는 구체적인 변경을 주고 기능 테스트와 구조적 판정 기준을 적용한다.
ko070 | SAME | ko070 | 1.00 | 다음 절에서는 이미 작성한 수정안에 적용할 요구와 계약을 바꾼다.
ko071 | SAME | ko071 | 1.00 | 너비 조회에서 남았던 질문을 재현할 수 있는 비교다.
ko072 | SAME | ko072 | 1.00 | 기존 호출자에게 보장한 동작만 달라져도 같은 수정안의 판정이 바뀌는지 확인할 수 있다.
ko073 | SAME | ko073 | 1.00 | · · 마이어가 예로 든 도서관 목록을 작은 프로그램으로 만들었다.
ko074 | SAME | ko074 | 1.00 | 기술보고서를 새로 처리하는 수정안 하나를 검토 대상으로 삼았다.
ko075 | SAME | ko075 | 1.00 | 수정안은 모듈을 하나 추가하고 기존 소스 파일 두 개는 바이트 단위로 그대로 둔다.
ko076 | SAME | ko076 | 1.00 | 실행하면 기술보고서가 출력되고 정오표 요청은 여전히 거절된다.
ko077 | SAME | ko077 | 1.00 | 이 실행 결과와 새 모듈 추가를 허용한 편집 범위는 네 경우에서 같다.
ko078 | SAME | ko078 | 1.00 | 새 요구가 기술보고서까지만 포함하는지 정오표까지 포함하는지를 바꿨다.
ko079 | SAME | ko079 | 1.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개의 미지원 자료 유형을 거절하는 동작을 보호한다.
ko080 | SAME | ko080 | 1.00 | 새 요구를 충족하고 적용되는 계약을 지켰을 때 표 2에서 승인으로 판정했다.
ko081 | SAME | ko081 | 1.00 | ** 누군가 검토 중에 “정오표도 이번에 지원해야 한다”고 알려 주면, 책 접두어에 대한 답을 기다릴 필요가 없다.
ko082 | SAME | ko082 | 1.00 | 수정안이 정오표를 거절한다는 사실만으로 결론이 난다.
ko083 | SAME | ko083 | 1.00 | 책 접두어가 보호된다는 사실도 그것만으로 거절을 결정한다.
ko084 | SAME | ko084 | 1.00 | 이 표에서는 기술보고서만 필요하고 책 접두어는 보장 대상이 아니라는 두 사실이 모두 필요하다.
ko085 | SAME | ko085 | 1.00 | 같은 편집 범위에서 새 모듈 하나로 두 자료 유형을 처리하고 모든 보호 동작을 지키는 수정안도 별도로 실행했다.
ko086 | SAME | ko086 | 1.00 | 표 2에서 알려진 사실에 맞는 행만 남겨 보자.
ko087 | SAME | ko087 | 1.00 | 실제 명세가 이 비교에 포함돼 있다는 전제에서는 적어도 한 행이 남는다.
ko088 | SAME | ko088 | 1.00 | 남은 행이 모두 같은 결론을 가리키면 일부 조건이 여전히 미공개여도 판정을 내릴 수 있다.
ko089 | SAME | ko089 | 1.00 | 승인과 거절이 함께 남으면 판정을 조건부로 말하거나, 결론을 가를 사실을 확인할 때까지 보류할 수 있다.
ko090 | SAME | ko090 | 1.00 | 같은 입력에서 언제나 하나의 답을 내도록 한 규칙은 정답이 반대인 두 행을 동시에 맞힐 수 없다.
ko091 | SAME | ko091 | 1.00 | 부록 A는 이 비교에서 가능한 정보 공개 조건 아홉 가지를 보여 준다.
ko092 | SAME | ko092 | 1.00 | 각 칸은 한 사례에서 설계한 정보 조건이다.
ko093 | NEW | ko128 | 0.18 | · 도서관 예제에서는 완성된 수정안 하나를 놓고 승인할 수 있는지를 따졌다.
ko094 | NEW | ko100 | 0.03 | 구현을 고르는 단계에서는 다른 질문이 생긴다.
ko095 | NEW | ko112 | 0.07 | 새 기능이 들어갈 자리와 그 기능을 호출할 자리가 주어졌을 때, 어떤 기존 파일에 손을 대야 할까?
ko096 | NEW | ko095 | 0.10 | 도형 예제로 돌아가 연산별로 파일을 둔 구현과 도형별로 파일을 둔 구현을 비교했다.
ko097 | NEW | ko123 | 0.07 | 이하의 수치는 실제로 실행한 후보가 수정한 기존 파일을 센 것이다.
ko098 | NEW | ko097 | 0.14 | 삼각형을 추가할 때 도형별 구현은 삼각형 파일 하나를 더하면 됐다.
ko099 | NEW | ko098 | 0.12 | 연산별 구현에서는 그리기를 맡은 기존 파일을 고쳤다.
ko100 | NEW | ko097 | 0.07 | 이름표를 붙이는 연산을 추가하자 상황이 바뀌었다.
ko101 | NEW | ko097 | 0.19 | 도형별 구현에서는 원과 사각형 파일을 각각 고쳤고, 연산별 구현에서는 이름표 연산을 새 파일에 둘 수 있었다.
ko102 | NEW | ko099 | 0.20 | 어느 쪽의 기존 파일을 건드려야 하는지는 요청에 따라 달랐다(그림 1A).
ko103 | NEW | ko107 | 0.07 | 그 차이가 같은 요구에서도 남는지 보기 위해 이번에는 양쪽에 를 추가했다.
ko104 | NEW | ko101 | 0.20 | 도형 목록을 받아 각 출력에 대괄호를 붙이는 함수다.
ko105 | NEW | ko102 | 0.24 | 도형별 구현에서 출력 변환을 각 도형이 맡도록 정하면 원과 사각형 파일을 모두 고칠 것으로 예측했다.
ko106 | NEW | ko103 | 0.24 | 공용 어댑터를 사용할 수 있으면 두 구현 모두 기존 파일을 그대로 두고 새 파일 하나에 기능을 담을 수 있다고 예측했다.
ko107 | NEW | ko106 | 0.11 | 실행 결과, 도형별 구현이 변환을 각 도형에 배치한 후보에서만 기존 파일 두 개가 바뀌었다.
ko108 | EDIT | ko104 | 0.56 | 네 후보 모두 새 파일을 하나 추가했으며, 입력 순서와 중복을 보존하고 빈 목록과 미지원 도형을 명세대로 처리했다.
ko109 | NEW | ko105 | 0.33 | 원과 사각형의 기존 렌더링도 유지됐다(그림 1B).
ko110 | SAME | ko108 | 1.00 | ** A는 삼각형 추가와 이름표 연산 추가를 비교한다.
ko111 | SAME | ko109 | 1.00 | B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다.
ko112 | SAME | ko110 | 1.00 | B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.
ko113 | NEW | ko121 | 0.13 | · · · · 공용 코드를 새 파일에 둘 수 있어도 호출자가 그 파일의 기능을 쓸 수 있는지는 따로 확인해야 한다.
ko114 | NEW | ko111 | 0.05 | 이를 보기 위해 목록을 받는 배치 함수와 구별되는 요구를 주었다.
ko115 | NEW | ko101 | 0.17 | 단일 렌더링 결과를 요청한 경우에만 대괄호로 감싸는 옵션이다.
ko116 | NEW | ko103 | 0.11 | 두 구현 모두 새 함수로 이 옵션을 제공할 수 있었다.
ko117 | NEW | ko113 | 0.17 | 그런데 같은 어댑터를 추가한 상태에서 예전 함수에 를 넘기자 인자가 거절됐다.
ko118 | NEW | ko114 | 0.42 | 옵션을 예전 함수로 제공한 후보는 연산별 구현에서 기존 파일 하나, 도형별 구현에서 두 개를 고쳤다.
ko119 | NEW | ko115 | 0.40 | 예전 함수가 외부 변환 모듈을 불러오도록 이미 구성된 별도 기준선에서는 두 구현 모두 새 파일 하나로 그 함수에 옵션을 연결했다(표 3).
ko120 | NEW | ko122 | 0.38 | ** 표 3의 마지막 행은 확장 지점이 이미 놓인 상태에서 세기 시작한다.
ko121 | NEW | ko117 | 0.12 | 확장 지점을 처음 마련하는 비용은 측정 범위 밖이다.
ko122 | NEW | ko005 | 0.07 | 두 표본 구현에서 확인한 파일 수를 실제 작업량으로 해석하려면 별도의 측정이 필요하다.
ko123 | NEW | ko029 | 0.09 | · 서론에서 사각형을 먼저 그린 함수에 수정을 요구하려면, 원을 먼저 놓는 일이 그 함수의 책임임을 보여 줄 수 있어야 했다.
ko124 | NEW | ko128 | 0.14 | 도서관 예제에서는 그에 해당하는 사실이 구체적인 판정을 내렸다.
ko125 | NEW | ko076 | 0.06 | 정오표가 요구에 들어 있거나 기존 책 접두어를 보장했다면 이 수정안은 거절된다.
ko126 | NEW | ko066 | 0.12 | 어느 쪽이 알려졌는지에 따라 검토자가 더 확인할 내용도 달라진다.
ko127 | NEW | ko131 | 0.07 | 수정 방향을 제안할 때는 그 기능을 어느 호출에서 쓸 수 있어야 하는지도 말해야 한다.
ko128 | NEW | ko119 | 0.09 | 단일 렌더링 옵션은 새 함수에서 동작했지만, 그 사실만으로는 기존 함수에 옵션을 달라는 요구를 충족할 수 없었다.
ko129 | NEW | ko072 | 0.08 | 검토 의견에 요구와 보장할 동작을 적고 적용되는 호출을 지목하면, 개발자는 결론이 어느 사실에 기대는지 확인할 수 있다.
ko130 | NEW | ko133 | 0.31 | 이 연구에서 근거로 삼은 범위는 한 벤치마크의 저장 자료와 직접 구성해 실행한 후보들이다.
ko131 | NEW | ko124 | 0.06 | 새 요구를 독립적으로 작성해도 요구·계약·편집 권한·호출 경로를 기술하는 것만으로 어느 구현이 기존 코드를 더 많이 보존할지 미리 판별할 수 있는가?
ko132 | NEW | ko132 | 0.02 | 그 예측이 맞는 조건과 어긋나는 조건을 확인하는 일이 다음 연구다.
ko133 | SAME | ko137 | 1.00 | §3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다.
ko134 | SAME | ko138 | 1.00 | §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다.
ko135 | SAME | ko139 | 1.00 | 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다.
ko136 | SAME | ko140 | 1.00 | 그림 1의 소스와 출력 위치는 그림 캡션에 있다.
ko137 | SAME | ko141 | 1.00 | 아래에서 ‘미공개’는 해당 항목의 두 값이 모두 가능하다는 뜻이다.
ko138 | SAME | ko142 | 1.00 | 보류는 공개된 정보와 양립하는 행 가운데 승인과 거절이 모두 남았을 때의 판정이다.
Summary ko: SAME 101, EDIT 1, NEW 36

### en (148 segmented sentences)
en001 | SAME | en001 | 1.00 | In 1996, Robert Martin described a function that drew the shapes in a list in order.
en002 | SAME | en002 | 1.00 | A triangle could be added without editing the function if the triangle supplied its own drawing operation.
en003 | SAME | en003 | 1.00 | Martin then introduced a new requirement.
en004 | SAME | en004 | 1.00 | Every circle had to be drawn before any square.
en005 | SAME | en005 | 1.00 | Given a list that begins with a square, the same function still draws the square first.
en006 | SAME | en006 | 1.00 | Who was supposed to sort the list?
en007 | SAME | en007 | 1.00 | If the caller was to put the circles first, the drawing function already does its job.
en008 | SAME | en008 | 1.00 | If the function was to guarantee that order for any input, it falls short.
en009 | SAME | en009 | 1.00 | Reading the code tells a reviewer what gets drawn first.
en010 | SAME | en010 | 1.00 | The reviewer needs the agreement between caller and function to tell whether that is a defect.
en011 | SAME | en011 | 1.00 | Martin called the design closed with respect to the addition of a shape.
en012 | SAME | en012 | 1.00 | The sorting requirement gives the same code a different test.
en013 | SAME | en013 | 1.00 | That is where our question about the open–closed principle (OCP) begins.
en014 | SAME | en014 | 1.00 | When a reviewer calls a proposed edit a violation, can the author recover from the verdict what the program was expected to accommodate or preserve?
en015 | SAME | en015 | 1.00 | We use *over-axiomatization* for the risk of treating such a verdict as settled when those premises are still open.
en016 | SAME | en016 | 1.00 | A benchmark that scores agreement with reference labels makes that question tractable.
en017 | SAME | en017 | 1.00 | Its archive lets us inspect the information actually supplied for classification.
en018 | SAME | en018 | 1.00 | To test what an acceptance decision requires, we hold a patch fixed and vary the task and the promise to existing callers.
en019 | SAME | en019 | 1.00 | We then return to drawing to see when a separate implementation can deliver an extension through the call the user already makes.
en020 | SAME | en020 | 1.00 | · · In 1996 Martin attributed the principle to Bertrand Meyer, citing page 23 of the 1988 first edition.
en021 | SAME | en021 | 1.00 | In Meyer’s account a module is closed once other modules can use it on the basis of a stable description.
en022 | SAME | en022 | 1.00 | His library example gives that stability a concrete test.
en023 | SAME | en023 | 1.00 | When technical reports become a new category, a program that handles each publication type explicitly may require edits to, or recompilation of, existing modules.
en024 | SAME | en024 | 1.00 | The choice of where to handle the new type matters to the modules that already depend on the catalog.
en025 | SAME | en025 | 1.00 | Having to edit a module to extend it was the issue in a June 1995 public exchange.
en026 | SAME | en026 | 1.00 | Kyle Brown argued that developers had to be able to fix a badly designed class.
en027 | SAME | en027 | 1.00 | Martin’s reply distinguished the right to edit a class from the need to edit it for an anticipated extension.
en028 | SAME | en028 | 1.00 | The design would still have to anticipate the right change.
en029 | SAME | en029 | 1.00 | The label SOLID appears in the public record by 2007.
en030 | SAME | en030 | 1.00 | In a 2009 discussion of interfaces, the distinction between a routine internal class and a public plugin API still mattered to the participants’ advice.
en031 | SAME | en031 | 1.00 | These sources document particular uses and disagreements about the principle.
en032 | SAME | en032 | 1.00 | A causal history of the acronym would require evidence of what changed as the label circulated.
en033 | SAME | en033 | 1.00 | · · In the 1996 article Martin made sorting part of .
en034 | SAME | en034 | 1.00 | In one implementation, puts a circle before a square by inspecting the other shape.
en035 | SAME | en035 | 1.00 | A new rule about where a third type ranks against a circle can send the edit back into .
en036 | SAME | en036 | 1.00 | Martin moved the ranking of types into a table, so putting squares ahead of circles becomes a matter of swapping two entries.
en037 | SAME | en037 | 1.00 | If the next request were to sort individual shapes by area, the table would need information it does not contain.
en038 | SAME | en038 | 1.00 | Later in the article Martin uses in two routines.
en039 | SAME | en039 | 1.00 | One version of recognizes circles and squares. selects squares.
en040 | SAME | en040 | 1.00 | The first routine leaves a shape undrawn when its job is to draw them all.
en041 | SAME | en041 | 1.00 | The second skips exactly the shapes it is supposed to skip.
en042 | SAME | en042 | 1.00 | Here the names and stated jobs make the distinction available to the reader.
en043 | SAME | en043 | 1.00 | What can a classification reviewer establish when the input consists of code and a prompt?
en044 | SAME | en044 | 1.00 | · · We distinguished the reference examples of OCP violations from the code actually sent to models.
en045 | SAME | en045 | 1.00 | A reference pair contains a violation example and its revision.
en046 | SAME | en046 | 1.00 | A saved response record contains the submitted code, its prompt, and the recorded response.
en047 | SAME | en047 | 1.00 | To isolate the instructions, we replaced the single exact occurrence of the submitted code in each saved prompt with a common placeholder.
en048 | SAME | en048 | 1.00 | We counted the resulting templates by exact string identity.
en049 | SAME | en049 | 1.00 | We compared each saved submission with both sides of every reference pair, first as stored and then after trimming whitespace from both ends.
en050 | SAME | en050 | 1.00 | For the Python reference pairs we parsed the syntax trees and compared method names declared in top-level classes, excluding names that begin with an underscore.
en051 | SAME | en051 | 1.00 | A missing name in this comparison establishes a change in declarations.
en052 | SAME | en052 | 1.00 | Whether a caller could still use the method through inheritance, actually used it, or was promised continued access each requires separate evidence.
en053 | SAME | en053 | 1.00 | The archive audit was a static analysis of the JSON and JSONL within the ZIP.
en054 | SAME | en054 | 1.00 | The behavior and contract checks in Sections 5–6 come from running fixtures built for this study under the conditions specified in those sections.
en055 | SAME | en055 | 1.00 | Appendix A identifies the inputs and the reproduction commands.
en056 | SAME | en056 | 1.00 | · Pehlivan et al. specified violation scenarios and refined the generated examples.
en057 | SAME | en057 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en058 | SAME | en058 | 1.00 | The benchmark compares model classifications with the reference labels.
en059 | SAME | en059 | 1.00 | For OCP we counted 48 reference pairs and 768 saved response records separately.
en060 | SAME | en060 | 1.00 | Masking the submitted code left 24 distinct instruction templates, with no exact match across the four strategies.
en061 | SAME | en061 | 1.00 | None of those templates separately stated which change an individual case called for or what its existing callers had been promised.
en062 | SAME | en062 | 1.00 | One saved Python prompt directs the reviewer to repeated branches where polymorphism would fit.
en063 | SAME | en063 | 1.00 | The submitted checks the shape type before calculating the area of a circle or rectangle.
en064 | SAME | en064 | 1.00 | The branch gives the reviewer somewhere to look if a new shape is requested.
en065 | SAME | en065 | 1.00 | The prompt leaves open whether that is the task and whether calls reading a rectangle’s width must still work after its area calculation moves.
en066 | SAME | en066 | 1.00 | Width becomes a concrete issue in the separate reference pair 37.
en067 | SAME | en067 | 1.00 | That revision moves area calculation onto the shapes and drops the declaration of .
en068 | SAME | en068 | 1.00 | No saved submission matched either side of any reference pair, whether we compared the stored strings or trimmed whitespace at their ends.
en069 | SAME | en069 | 1.00 | In pair 37 we can establish that the declaration was removed.
en070 | SAME | en070 | 1.00 | Turning its removal into a reason to reject the patch would require evidence that existing callers were promised continued access to the width.
en071 | SAME | en071 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en072 | SAME | en072 | 1.00 | ** The saved prompt is on JSONL line 13 (record ID 12).
en073 | SAME | en073 | 1.00 | Reference pair 37 is in a separate ground-truth JSON file.
en074 | SAME | en074 | 1.00 | · · · These distinctions matter when choosing an instrument.
en075 | SAME | en075 | 1.00 | Bräuer et al. (2018) asked experts how much of a design principle their measurable practices covered.
en076 | SAME | en076 | 1.00 | Cabral et al. (2024) asked participants about understanding and ease of extension in a machine-learning scenario under a bundled SOLID treatment.
en077 | SAME | en077 | 1.00 | Zhu et al. (2026) gave specific repository change tasks and checked them against functional tests and structural oracles.
en078 | SAME | en078 | 1.00 | In the next comparison we hold a completed patch fixed and vary the request and contract against which it is judged.
en079 | SAME | en079 | 1.00 | This lets us reproduce the open question about the width getter in a setting where we can change what existing callers are promised and check whether the same patch still qualifies.
en080 | SAME | en080 | 1.00 | · · We built a small version of Meyer’s library catalog and took one patch that extends it to technical reports.
en081 | SAME | en081 | 1.00 | The patch adds one module and leaves both existing source files byte-for-byte identical.
en082 | SAME | en082 | 1.00 | It renders technical reports and still rejects requests for errata.
en083 | SAME | en083 | 1.00 | It also changes one existing output.
en084 | SAME | en084 | 1.00 | The prefix in a book rendering goes from to .
en085 | SAME | en085 | 1.00 | The observed behavior and the permission to add a module are the same in all four cases.
en086 | SAME | en086 | 1.00 | The request may cover technical reports alone or require errata as well.
en087 | SAME | en087 | 1.00 | Both variants of the caller contract protect the rendering of journals and proceedings and the rejection of a separate unsupported type.
en088 | SAME | en088 | 1.00 | The broader contract also protects the original book prefix.
en089 | SAME | en089 | 1.00 | In Table 2 a patch qualifies for acceptance when it meets the request and preserves the applicable contract.
en090 | SAME | en090 | 1.00 | Two requirements for accepting a fixed patch.
en091 | SAME | en091 | 1.00 | ** Suppose the reviewer learns that the release must support errata.
en092 | SAME | en092 | 1.00 | The patch rejects errata, so the reviewer can reject it while the book contract is still open.
en093 | SAME | en093 | 1.00 | Learning that the book prefix is protected also settles rejection on its own.
en094 | SAME | en094 | 1.00 | Acceptance in this table takes two facts: technical reports are the whole request, and the book prefix is outside the contract.
en095 | SAME | en095 | 1.00 | We also ran a separate patch that adds one module within the same edit boundary, handles both new types, and preserves every protected observation.
en096 | SAME | en096 | 1.00 | Keep only the rows of Table 2 compatible with what the reviewer knows.
en097 | SAME | en097 | 1.00 | At least one row remains if the actual specification is among the cases considered.
en098 | SAME | en098 | 1.00 | If the remaining rows agree, their common verdict is available now.
en099 | SAME | en099 | 1.00 | If they disagree, the reviewer can give a conditional verdict or wait for the fact that resolves the disagreement.
en100 | SAME | en100 | 1.00 | A rule forced to give a single answer on identical inputs cannot get both of two rows right when the correct answers differ.
en101 | SAME | en101 | 1.00 | Appendix A shows all nine disclosure settings.
en102 | SAME | en102 | 1.00 | Each cell is a designed information condition within this one case.
en103 | NEW | en141 | 0.14 | · In the catalog case we asked whether to accept a completed patch.
en104 | NEW | en074 | 0.21 | Choosing an implementation raises a further question.
en105 | NEW | en140 | 0.17 | Given a place for the new behavior and a function through which callers must reach it, which existing files have to change?
en106 | NEW | en019 | 0.21 | We return to drawing, comparing one implementation organized by operation with another organized by shape.
en107 | NEW | en136 | 0.22 | The counts below are for candidates we built and ran.
en108 | NEW | en108 | 0.41 | To add a triangle in the shape layout, we added one file.
en109 | NEW | en109 | 0.41 | In the operation layout we edited the existing file that handled drawing.
en110 | NEW | en120 | 0.28 | A request for a labeling operation reversed the comparison.
en111 | EDIT | en108 | 0.54 | We edited the circle and square files in the shape layout and added a new file in the operation layout.
en112 | SAME | en110 | 1.00 | All four candidates passed their functional checks.
en113 | EDIT | en111 | 0.57 | Which layout required edits to existing files depended on the request (Figure 1A).
en114 | NEW | en112 | 0.19 | To see whether that difference would persist under a common request, we added to both layouts.
en115 | EDIT | en113 | 0.83 | It takes a list of shapes and brackets each result.
en116 | EDIT | en114 | 0.55 | We predicted that assigning the transformation to the shapes in the shape layout would require editing both their files.
en117 | NEW | en115 | 0.29 | With a shared adapter available, we expected each layout to support the feature in one new file while leaving the existing files intact.
en118 | NEW | en117 | 0.43 | The only candidate that edited existing files was the one assigning the transformation to the shape files.
en119 | EDIT | en116 | 0.74 | All four added a file, preserved order and duplicates, handled empty lists and unsupported shapes as specified, and kept the existing circle and square renderings (Figure 1B).
en120 | SAME | en119 | 1.00 | Existing source files edited.
en121 | SAME | en120 | 1.00 | ** Panel A compares adding a triangle with adding a labeling operation.
en122 | SAME | en121 | 1.00 | Panel B holds the batch-rendering request fixed and varies the placement rule.
en123 | SAME | en122 | 1.00 | All four candidates in panel B passed the new and legacy behavior checks and added one file each.
en124 | NEW | en119 | 0.11 | · · · · An adapter can sit in a new file even when an existing caller has no way to use it.
en125 | NEW | en123 | 0.21 | We tested this with a separate request for an option that brackets the result of a single render.
en126 | NEW | en112 | 0.26 | Both layouts offered the option through a new function.
en127 | NEW | en125 | 0.32 | When we tried on the old function after adding the same adapter, the function rejected the argument.
en128 | EDIT | en126 | 0.66 | The candidates that delivered the option through the original function edited one existing file in the operation layout and two in the shape layout.
en129 | EDIT | en127 | 0.49 | From a separate baseline in which the original function could already load an external decorator, a new file alone connected the option to that function in each layout (Table 3).
en130 | SAME | en128 | 1.00 | Call paths for the new rendering option.
en131 | EDIT | en135 | 0.81 | ** The last row of Table 3 starts counting after the hook is in place.
en132 | NEW | en131 | 0.18 | We left the initial cost of introducing it outside the measurement.
en133 | NEW | en137 | 0.23 | Relating these file counts to actual maintenance effort would require a separate measurement.
en134 | NEW | en007 | 0.26 | · To require a change to the drawing function in the introduction, the reviewer had to establish that putting circles first was the function’s job.
en135 | NEW | en145 | 0.18 | In our catalog test the corresponding facts could settle an actual verdict.
en136 | NEW | en141 | 0.18 | A requirement to render errata or a promise to preserve the book prefix was enough to reject the patch.
en137 | NEW | en111 | 0.16 | The missing information worth asking for depended on which facts the reviewer already had.
en138 | NEW | en042 | 0.13 | A proposed fix also needs to say where the behavior must be available.
en139 | NEW | en126 | 0.24 | The single-render option worked through the new function, but the candidate providing it there still fell short of a request for the same option on the original function.
en140 | NEW | en145 | 0.15 | A review that names the required or protected behavior and points to the call it concerns gives the developer grounds they can check.
en141 | NEW | en146 | 0.47 | Our evidence comes from the stored material of one benchmark and the candidates we built and ran.
en142 | NEW | en137 | 0.20 | Can an account of requests, contracts, edit permissions, and call paths predict which implementation will preserve more existing code when the requests come from independent authors?
en143 | NEW | en042 | 0.16 | Testing where that prediction holds and where it breaks is the next research question.
en144 | SAME | en150 | 1.00 | For Sections 3–4 the audit reads the archived JSON and JSONL.
en145 | SAME | en151 | 1.00 | For Sections 5–6 the fixtures run the examples constructed for this study.
en146 | SAME | en152 | 1.00 | The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.
en147 | SAME | en153 | 1.00 | When a field is withheld, both of its recorded values remain possible.
en148 | SAME | en154 | 1.00 | Defer means that at least one compatible row accepts the patch and at least one rejects it.
Summary en: SAME 113, EDIT 8, NEW 27

## v11 · [Source](https://app.notion.com/p/41bef561cf92811abb50f26b749e9ca5)
### ko (157 segmented sentences)
ko001 | SAME | ko001 | 1.00 | 로버트 마틴이 1996년에 예로 든 함수는 목록에 들어온 순서대로 도형을 그린다.
ko002 | SAME | ko002 | 1.00 | 삼각형에 자기 자신을 그리는 동작이 있으면 이 함수에 손대지 않고도 삼각형을 추가할 수 있다.
ko003 | SAME | ko003 | 1.00 | 목록의 맨 앞에 사각형이 있으면 함수는 여전히 그 사각형부터 그린다.
ko004 | SAME | ko004 | 1.00 | 호출자가 원을 앞에 놓아 목록을 넘기기로 했다면 함수는 제 일을 한다.
ko005 | SAME | ko005 | 1.00 | 어떤 목록을 받더라도 함수가 순서를 보장하기로 했다면 수정이 필요하다.
ko006 | SAME | ko006 | 1.00 | 코드를 읽으면 무엇이 먼저 그려지는지 알 수 있다.
ko007 | SAME | ko007 | 1.00 | 그 결과가 잘못됐는지를 판단하려면 호출자와 함수 사이에 어떤 약속이 있었는지도 알아야 한다.
ko008 | SAME | ko008 | 1.00 | 도형 하나를 더 추가할 때 닫혀 있던 설계도 함수가 직접 정렬을 책임지는 순간 같은 방식으로 확장할 수 없었다.
ko009 | SAME | ko009 | 1.00 | 개방–폐쇄 원칙(OCP)을 근거로 어떤 수정안에 ‘위반’이라고 표시할 때도, 그 판단을 받은 개발자는 프로그램이 어떤 변화에 대비해야 했고 어떤 동작을 계속 보장해야 했는지 물을 수 있다.
ko010 | SAME | ko010 | 1.00 | 이 전제가 정해지기 전에 판정부터 확정하는 위험을 이 글에서는 설계 조언의 ‘과도한 공리화’라고 부른다.
ko011 | SAME | ko011 | 1.00 | 분류 벤치마크에는 모델이 무엇을 보고 위반 여부를 답했는지 기록이 남아 있다.
ko012 | SAME | ko012 | 1.00 | 그 기록을 읽어 분류에 주어진 근거를 확인한다.
ko013 | SAME | ko013 | 1.00 | 코드가 같은데도 새 요구와 기존 호출자에 대한 약속에 따라 결론이 달라지는지 살핀다.
ko014 | SAME | ko014 | 1.00 | 그 뒤 도형 예제로 돌아가 새 기능을 별도 파일에 넣었을 때 기존 호출자가 사용하던 함수로도 그 기능을 쓸 수 있는지 확인한다.
ko015 | SAME | ko015 | 1.00 | · · 마틴은 1996년 글에서 베르트랑 마이어의 1988년 초판 23쪽을 인용하며 원칙의 출처를 밝혔다.
ko016 | SAME | ko016 | 1.00 | 마이어가 말한 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 사용할 수 있는 모듈이다.
ko017 | SAME | ko017 | 1.00 | 마이어는 자료의 종류를 하나씩 구별해 처리하는 도서관 프로그램을 예로 든다.
ko018 | SAME | ko018 | 1.00 | 기술보고서가 새로운 자료 유형으로 들어오면 이미 쓰이던 모듈까지 고치거나 다시 컴파일해야 할 수 있다.
ko019 | SAME | ko019 | 1.00 | 새 자료를 처리하는 코드를 어디에 두느냐는 기존 모듈이 무엇에 의존할 수 있느냐와 맞물린다.
ko020 | SAME | ko020 | 1.00 | 1995년 6월 공개 토론에서는 기존 모듈을 손댈 수 있다는 것과 손대야 한다는 것의 차이가 쟁점이었다.
ko021 | SAME | ko021 | 1.00 | 카일 브라운은 잘못 설계된 클래스라면 개발자가 소스를 고칠 수 있어야 한다고 했다.
ko022 | SAME | ko022 | 1.00 | 마틴의 답은 예상한 확장을 하려면 기존 소스를 반드시 고쳐야 하는지에 관한 것이었다.
ko023 | SAME | ko023 | 1.00 | 어떤 변경이 생길지 미리 짚어야 한다는 어려움은 남았다.
ko024 | SAME | ko024 | 1.00 | 2007년 공개 기록에는 다섯 원칙을 묶은 SOLID라는 이름이 나온다.
ko025 | SAME | ko025 | 1.00 | 2009년의 인터페이스 논쟁에서도 내부 클래스의 인터페이스와 공개 플러그인 API에는 서로 다른 조언이 제시됐다.
ko026 | SAME | ko026 | 1.00 | 이 자료들은 원칙이 어떻게 쓰이고 논쟁됐는지 보여 준다.
ko027 | SAME | ko027 | 1.00 | SOLID라는 이름이 퍼지면서 적용 조건에 대한 판단이 실제로 바뀌었는지는 별도의 근거가 필요한 역사적 질문이다.
ko028 | EDIT | ko028 | 0.50 | · · 1996년 글에서 마틴은 목록 정렬을 DrawAllShapes 가 맡게 했다.
ko029 | EDIT | ko029 | 0.56 | 한 구현에서는 Circle::Precedes 가 상대 도형을 검사해 사각형이면 원을 먼저 놓는다.
ko030 | EDIT | ko030 | 0.67 | 세 번째 도형과 원의 순서를 정해야 하면 Circle 을 다시 고칠 수 있다.
ko031 | SAME | ko031 | 1.00 | 도형 종류별 순서를 표로 옮기면 사각형을 원보다 먼저 그리기 위해 두 항목의 위치만 바꾸면 된다.
ko032 | SAME | ko032 | 1.00 | 그다음 요구가 개별 도형을 넓이순으로 그리는 것이라면 표에 없는 정보가 필요하다.
ko033 | EDIT | ko033 | 0.53 | 같은 글 후반에서 마틴은 dynamic_cast 를 쓰는 함수 둘을 제시한다.
ko034 | NEW | ko034 | 0.36 | DrawAllShapes 의 한 구현은 원과 사각형을 골라 그리고, DrawSquaresOnly 는 사각형을 골라 그린다.
ko035 | SAME | ko035 | 1.00 | 모든 도형을 그려야 하는 함수라면 그림 하나가 빠진 것이고, 사각형만 그려야 하는 함수라면 건너뛰는 것이 맞다.
ko036 | SAME | ko036 | 1.00 | 여기서는 함수 이름과 설명을 읽으면 각각 무엇을 맡았는지 알 수 있다.
ko037 | SAME | ko037 | 1.00 | 분류를 맡은 검토자에게 코드와 프롬프트가 주어졌을 때는 그 책임을 어디까지 확인할 수 있을까?
ko038 | NEW | ko072 | 0.07 | · · 같은 소스와 같은 수정안을 두고 유지보수 판정이 달라질 수 있는가?
ko039 | NEW | ko127 | 0.05 | 이 질문을 검사하려면 검토자가 받은 정보와, 그 정보로 내려야 하는 판정을 따로 기록해야 한다.
ko040 | NEW | ko130 | 0.12 | 먼저 위반 분류 벤치마크의 저장 자료에서 실제로 어떤 입력이 남아 있는지 확인했다.
ko041 | NEW | ko124 | 0.08 | 이어 도서관 예제에서 판단에 필요한 사실 중 일부를 공개하지 않았을 때도 결론이 정해지는지 살폈다.
ko042 | EDIT | ko052 | 0.49 | 아카이브에서는 OCP 참조 쌍 48개와 저장 응답 768건을 별도로 셌다.
ko043 | NEW | ko039 | 0.16 | 참조 쌍은 위반 예시와 수정 예시로 이루어진다.
ko044 | NEW | ko039 | 0.19 | 저장 응답 한 건은 제출 코드, 프롬프트, 기록된 모델 응답을 한데 묶은 행이다.
ko045 | NEW | ko052 | 0.02 | OCP 응답 파일은 16개이며 파일마다 48행이 있다.
ko046 | NEW | ko053 | 0.05 | 저장 응답 수는 서로 다른 프로그램의 수를 뜻하지 않는다.
ko047 | NEW | ko040 | 0.38 | 각 프롬프트에서 제출 코드가 정확히 한 번 나오는지 확인한 뒤 그 부분을 공통 자리표시자로 바꿨다.
ko048 | NEW | ko041 | 0.15 | 지시문 틀은 남은 문자열이 완전히 같을 때 하나로 셌다.
ko049 | NEW | ko038 | 0.02 | 이 기계적 집계에 이어 틀의 문구를 읽었다.
ko050 | NEW | ko054 | 0.05 | ‘별도로 명시했다’는 것은 지시문이 해당 사례에 필요한 새 동작을 요구하거나, 기존 호출에서 계속 보장할 동작을 밝힌 경우를 가리킨다.
ko051 | NEW | ko081 | 0.05 | 예컨대 “삼각형도 그려야 한다”는 변경 요구이고 “기존 너비 조회는 계속 지원해야 한다”는 호출자 계약이다.
ko052 | NEW | ko055 | 0.07 | 반복 분기에 다형성을 적용할 만한지 물어보는 문구는 일반적인 판별 단서로 읽었다.
ko053 | NEW | ko121 | 0.06 | 가려진 코드에 있는 단서나 아카이브의 다른 문서에 있는 맥락은 이 대조의 범위 밖이다.
ko054 | NEW | ko042 | 0.18 | 출처를 연결할 때는 저장 행의 제출 코드를 모든 OCP 참조 쌍의 양쪽 소스와 비교했다.
ko055 | NEW | ko043 | 0.15 | 문자열 그대로 대조한 뒤 양끝 공백만 걷어 내 비교를 반복했다.
ko056 | NEW | ko062 | 0.12 | 이 절차로 확인할 수 있는 것은 두 기준에서의 문자열 일치 여부다.
ko057 | NEW | ko044 | 0.26 | Python 참조 쌍에서는 최상위 클래스가 직접 선언한 메서드 이름을 구문 트리에서 읽었다.
ko058 | NEW | ko046 | 0.42 | 기존 호출자가 그 메서드를 사용했는지, 상속을 통해 여전히 호출할 수 있는지, 계속 쓸 수 있다고 보장받았는지는 각각 별도의 근거가 필요하다.
ko059 | NEW | ko093 | 0.15 | 도서관 예제에서는 기존 소스, 수정안, 호출 입력과 편집 범위를 고정했다.
ko060 | NEW | ko080 | 0.08 | 기존 클라이언트가 부르는 경로에서 출력 문자열이나 예외의 유형·메시지를 기록하고, 먼저 새 요구를 충족하는지와 기존 계약을 지키는지를 따로 채점했다.
ko061 | NEW | ko080 | 0.07 | 그 두 판정이 모두 참일 때 승인으로 정했다.
ko062 | NEW | ko138 | 0.06 | 그다음 이미 계산한 판정표에서 공개된 정보와 맞는 행을 남겨, 일부 전제가 빠져도 승인이나 거절이 하나로 정해지는지 확인했다.
ko063 | NEW | ko133 | 0.27 | 벤치마크 자료는 ZIP의 JSON·JSONL을 읽어 감사했다.
ko064 | NEW | ko134 | 0.14 | 실행 검사는 이 연구에서 작성한 도서관·도형 예제로 수행했다.
ko065 | SAME | ko050 | 1.00 | · Pehlivan 등은 위반 시나리오를 정해 코드 예시를 생성하고 다듬었다.
ko066 | SAME | ko051 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko067 | NEW | ko053 | 0.29 | OCP 저장 응답에서 제출 코드를 가리자 서로 다른 지시문 틀 24개가 남았다.
ko068 | NEW | ko041 | 0.03 | 전략별로는 DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였고, 전략 간에 같은 문자열은 없었다.
ko069 | NEW | ko054 | 0.06 | 어느 틀에도 개별 사례에 해당하는 새 요구나 보호할 호출자 계약을 따로 쓴 문구는 없었다.
ko070 | EDIT | ko055 | 0.72 | 그중 Python EXAMPLE 지시는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko071 | EDIT | ko056 | 0.55 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko072 | SAME | ko057 | 1.00 | 새 도형을 지원할 때 이 분기가 수정 후보라는 판단은 코드에서 나온다.
ko073 | SAME | ko058 | 1.00 | 그 확장이 실제 요구인지, 넓이 계산을 옮겨도 기존의 너비 조회를 지원해야 하는지는 검토 지시에 적혀 있지 않다.
ko074 | SAME | ko059 | 1.00 | 너비 조회는 별도의 참조 쌍 37번에서 실제 편집 항목이 된다.
ko075 | EDIT | ko060 | 0.50 | 이 쌍에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko076 | SAME | ko061 | 1.00 | 저장된 제출 코드와 모든 참조 쌍의 양쪽 소스를 대조했을 때, 원본 문자열 비교와 양끝 공백을 제거한 비교 모두에서 일치가 없었다.
ko077 | SAME | ko062 | 1.00 | 37번에서 직접 확인할 수 있는 것은 참조 소스에서 선언이 빠졌다는 사실까지다.
ko078 | SAME | ko063 | 1.00 | 그 삭제가 수정안을 거절할 이유가 되려면 너비 조회를 기존 호출자에게 보장했다는 근거가 더 있어야 한다.
ko079 | SAME | ko064 | 1.00 | 프롬프트 예시는 저장 JSONL 13행(ID 12)이다.
ko080 | SAME | ko065 | 1.00 | 참조 쌍 37번은 별도의 ground truth JSON 위치다.
ko081 | SAME | ko067 | 1.00 | · · · Bräuer 등(2018)은 전문가에게 측정 가능한 실천 규칙들이 설계 원칙을 얼마나 포착하는지 물었다.
ko082 | SAME | ko068 | 1.00 | Cabral 등(2024)은 기계학습 기능을 확장하는 상황에서 SOLID를 묶어서 적용한 코드에 대해 참가자가 느낀 이해도와 확장 용이성을 조사했다.
ko083 | SAME | ko069 | 1.00 | Zhu 등(2026)의 저장소 과제는 구체적인 변경을 주고 기능 테스트와 구조적 판정 기준을 적용한다.
ko084 | NEW | ko059 | 0.20 | 참조 쌍 37번에서는 너비 조회를 계속 지원해야 했는지가 열려 있다.
ko085 | NEW | ko070 | 0.10 | 다음 절에서는 이와 같은 종류의 정보가 판정에 어떤 차이를 만드는지 살핀다.
ko086 | NEW | ko070 | 0.12 | 코드와 수정안을 그대로 두고 적용할 요구나 계약을 바꿀 수 있게 예제를 구성했다.
ko087 | SAME | ko073 | 1.00 | · · 마이어가 예로 든 도서관 목록을 작은 프로그램으로 만들었다.
ko088 | NEW | ko116 | 0.02 | 기존 client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko089 | NEW | ko075 | 0.03 | 검토할 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 하나를 추가하며, catalog.py 와 client.py 의 소스 내용은 바꾸지 않는다.
ko090 | SAME | ko076 | 1.00 | 실행하면 기술보고서가 출력되고 정오표 요청은 여전히 거절된다.
ko091 | NEW | ko125 | 0.04 | 기존 책 출력은 접두어 book 이 BOOK 으로 바뀐다.
ko092 | NEW | ko074 | 0.06 | 이제 수정안의 코드와 같은 실행 기록을 검토자 둘에게 주고 둘 다 기술보고서만 지원하라는 요청을 받았다고 하자.
ko093 | NEW | ko063 | 0.09 | 한쪽은 기존 호출자에게 책 출력을 그대로 돌려주기로 했다는 사실을 알고 있다.
ko094 | NEW | ko033 | 0.03 | 다른 쪽에는 그 출력이 계약 밖이라고 명시한다.
ko095 | NEW | ko079 | 0.02 | 책의 출력이 바뀐 사실은 두 사람에게 같다.
ko096 | NEW | ko080 | 0.04 | 그 사실을 위반으로 볼지는 어느 계약이 적용되는가에 달려 있다.
ko097 | NEW | ko086 | 0.06 | 표 2에서는 여기에 정오표 지원 요구까지 교차시켰다.
ko098 | NEW | ko079 | 0.34 | 두 계약에 공통으로 들어 있는 것은 학술지·학회록 출력과, 정오표와 별개의 미지원 자료 유형을 거절하는 동작이다.
ko099 | NEW | ko086 | 0.18 | 부분 정보로 판정할 때는 표에서 공개된 사실에 맞는 행만 남긴다.
ko100 | NEW | ko081 | 0.31 | 검토 중에 “정오표도 이번에 지원해야 한다”고 들으면 아래 두 행이 남는다.
ko101 | NEW | ko089 | 0.07 | 두 행 모두 거절이므로 책 계약을 확인하기 전에 결론을 낼 수 있다.
ko102 | NEW | ko084 | 0.16 | “기술보고서만 필요하다”는 사실을 들으면 위 두 행이 남는다.
ko103 | NEW | ko126 | 0.04 | 검토자가 다음으로 얻어야 할 답은 책 출력이 보호 대상인지다.
ko104 | NEW | ko087 | 0.17 | 이 절차는 검토 중인 명세 가운데 실제 명세가 들어 있다는 전제에서 성립한다.
ko105 | NEW | ko127 | 0.03 | 공개된 사실과 맞는 행이 하나도 없다면 먼저 비교에 넣은 명세와 공개된 내용을 다시 대조해야 한다.
ko106 | NEW | ko138 | 0.12 | 승인과 거절이 모두 남는다면 동일한 정보만 받은 규칙은 어느 경우에도 맞는 하나의 판정을 골라낼 수 없다.
ko107 | NEW | ko089 | 0.14 | 현재 답은 조건부로 제시하거나 보류할 수 있다.
ko108 | NEW | ko070 | 0.07 | 부록 A의 3×3 표는 이 사례에서 요구와 계약을 각각 알리거나 가린 경우를 모두 적은 것이다.
ko109 | NEW | ko085 | 0.13 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko110 | NEW | ko074 | 0.08 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리하면서 기존 책 출력까지 보존했다.
ko111 | NEW | ko070 | 0.04 | 표 2의 거절은 실행 가능한 대안이 있는 조건에서 특정 수정안에 내려진 판정이다.
ko112 | NEW | ko046 | 0.05 | 이 방식을 다른 사례에 적용하려면, 무엇을 보장했는지에 대한 가능한 명세와 그 근거를 먼저 밝혀야 한다.
ko113 | SAME | ko093 | 1.00 | · 도서관 예제에서는 완성된 수정안 하나를 놓고 승인할 수 있는지를 따졌다.
ko114 | SAME | ko094 | 1.00 | 구현을 고르는 단계에서는 다른 질문이 생긴다.
ko115 | SAME | ko095 | 1.00 | 새 기능이 들어갈 자리와 그 기능을 호출할 자리가 주어졌을 때, 어떤 기존 파일에 손을 대야 할까?
ko116 | SAME | ko096 | 1.00 | 도형 예제로 돌아가 연산별로 파일을 둔 구현과 도형별로 파일을 둔 구현을 비교했다.
ko117 | SAME | ko097 | 1.00 | 이하의 수치는 실제로 실행한 후보가 수정한 기존 파일을 센 것이다.
ko118 | SAME | ko098 | 1.00 | 삼각형을 추가할 때 도형별 구현은 삼각형 파일 하나를 더하면 됐다.
ko119 | SAME | ko099 | 1.00 | 연산별 구현에서는 그리기를 맡은 기존 파일을 고쳤다.
ko120 | SAME | ko100 | 1.00 | 이름표를 붙이는 연산을 추가하자 상황이 바뀌었다.
ko121 | SAME | ko101 | 1.00 | 도형별 구현에서는 원과 사각형 파일을 각각 고쳤고, 연산별 구현에서는 이름표 연산을 새 파일에 둘 수 있었다.
ko122 | SAME | ko102 | 1.00 | 어느 쪽의 기존 파일을 건드려야 하는지는 요청에 따라 달랐다(그림 1A).
ko123 | EDIT | ko103 | 0.65 | 그 차이가 같은 요구에서도 남는지 보기 위해 이번에는 양쪽에 render_many 를 추가했다.
ko124 | SAME | ko104 | 1.00 | 도형 목록을 받아 각 출력에 대괄호를 붙이는 함수다.
ko125 | SAME | ko105 | 1.00 | 도형별 구현에서 출력 변환을 각 도형이 맡도록 정하면 원과 사각형 파일을 모두 고칠 것으로 예측했다.
ko126 | SAME | ko106 | 1.00 | 공용 어댑터를 사용할 수 있으면 두 구현 모두 기존 파일을 그대로 두고 새 파일 하나에 기능을 담을 수 있다고 예측했다.
ko127 | SAME | ko107 | 1.00 | 실행 결과, 도형별 구현이 변환을 각 도형에 배치한 후보에서만 기존 파일 두 개가 바뀌었다.
ko128 | SAME | ko108 | 1.00 | 네 후보 모두 새 파일을 하나 추가했으며, 입력 순서와 중복을 보존하고 빈 목록과 미지원 도형을 명세대로 처리했다.
ko129 | SAME | ko109 | 1.00 | 원과 사각형의 기존 렌더링도 유지됐다(그림 1B).
ko130 | SAME | ko110 | 1.00 | A는 삼각형 추가와 이름표 연산 추가를 비교한다.
ko131 | SAME | ko111 | 1.00 | B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다.
ko132 | SAME | ko112 | 1.00 | B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.
ko133 | SAME | ko113 | 1.00 | · · · · 공용 코드를 새 파일에 둘 수 있어도 호출자가 그 파일의 기능을 쓸 수 있는지는 따로 확인해야 한다.
ko134 | SAME | ko114 | 1.00 | 이를 보기 위해 목록을 받는 배치 함수와 구별되는 요구를 주었다.
ko135 | SAME | ko115 | 1.00 | 단일 렌더링 결과를 요청한 경우에만 대괄호로 감싸는 옵션이다.
ko136 | SAME | ko116 | 1.00 | 두 구현 모두 새 함수로 이 옵션을 제공할 수 있었다.
ko137 | EDIT | ko117 | 0.62 | 그런데 같은 어댑터를 추가한 상태에서 예전 함수에 bracketed=True 를 넘기자 인자가 거절됐다.
ko138 | SAME | ko118 | 1.00 | 옵션을 예전 함수로 제공한 후보는 연산별 구현에서 기존 파일 하나, 도형별 구현에서 두 개를 고쳤다.
ko139 | SAME | ko119 | 1.00 | 예전 함수가 외부 변환 모듈을 불러오도록 이미 구성된 별도 기준선에서는 두 구현 모두 새 파일 하나로 그 함수에 옵션을 연결했다(표 3).
ko140 | SAME | ko120 | 1.00 | 표 3의 마지막 행은 확장 지점이 이미 놓인 상태에서 세기 시작한다.
ko141 | SAME | ko121 | 1.00 | 확장 지점을 처음 마련하는 비용은 측정 범위 밖이다.
ko142 | SAME | ko122 | 1.00 | 두 표본 구현에서 확인한 파일 수를 실제 작업량으로 해석하려면 별도의 측정이 필요하다.
ko143 | NEW | ko123 | 0.37 | · 사각형이 먼저 그려졌다는 실행 결과를 근거로 함수의 수정을 요구하려면, 원을 먼저 놓는 일이 그 함수의 책임임을 알아야 했다.
ko144 | NEW | ko124 | 0.17 | 도서관 예제에서는 실행 기록을 고정한 채 그 책임에 해당하는 요구와 기존의 약속을 바꿀 수 있었다.
ko145 | NEW | ko125 | 0.08 | 정오표가 필수라는 사실은 이 수정안을 곧바로 거절할 근거였다.
ko146 | NEW | ko084 | 0.10 | 기술보고서만 필요할 때는 기존 책 출력을 보호해야 하는지 확인해야 했다.
ko147 | NEW | ko072 | 0.04 | 이 글에서 제시한 방법은 같은 수정안에 대해 지금 가능한 명세를 드러내고, 어느 사실을 알면 결론이 정해지는지 시험하는 것이다.
ko148 | NEW | ko070 | 0.06 | 실제 리뷰에서는 요구서나 테스트에서 적용할 계약을 읽어 낼 수 있다.
ko149 | NEW | ko125 | 0.04 | §6처럼 호출 경로가 명세에 들어 있는 경우도 있다.
ko150 | NEW | ko071 | 0.03 | 어떤 자료로 가능한 명세를 정하고 무엇을 시험하면 충분한지는 다른 사례와 방법들이 비교할 수 있는 질문으로 남는다.
ko151 | NEW | ko130 | 0.42 | 이 연구의 관찰 근거는 한 벤치마크의 저장 자료와 직접 구성해 실행한 예제다.
ko152 | SAME | ko133 | 1.00 | §3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다.
ko153 | SAME | ko134 | 1.00 | §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다.
ko154 | SAME | ko135 | 1.00 | 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다.
ko155 | SAME | ko136 | 1.00 | 그림 1의 소스와 출력 위치는 그림 캡션에 있다.
ko156 | SAME | ko137 | 1.00 | 아래에서 ‘미공개’는 해당 항목의 두 값이 모두 가능하다는 뜻이다.
ko157 | SAME | ko138 | 1.00 | 보류는 공개된 정보와 양립하는 행 가운데 승인과 거절이 모두 남았을 때의 판정이다.
Summary ko: SAME 81, EDIT 10, NEW 66

### en (171 segmented sentences)
en001 | SAME | en001 | 1.00 | In 1996, Robert Martin described a function that drew the shapes in a list in order.
en002 | SAME | en002 | 1.00 | A triangle could be added without editing the function if the triangle supplied its own drawing operation.
en003 | SAME | en003 | 1.00 | Martin then introduced a new requirement.
en004 | SAME | en004 | 1.00 | Every circle had to be drawn before any square.
en005 | SAME | en005 | 1.00 | Given a list that begins with a square, the same function still draws the square first.
en006 | SAME | en006 | 1.00 | Who was supposed to sort the list?
en007 | SAME | en007 | 1.00 | If the caller was to put the circles first, the drawing function already does its job.
en008 | SAME | en008 | 1.00 | If the function was to guarantee that order for any input, it falls short.
en009 | SAME | en009 | 1.00 | Reading the code tells a reviewer what gets drawn first.
en010 | SAME | en010 | 1.00 | The reviewer needs the agreement between caller and function to tell whether that is a defect.
en011 | SAME | en011 | 1.00 | Martin called the design closed with respect to the addition of a shape.
en012 | SAME | en012 | 1.00 | The sorting requirement gives the same code a different test.
en013 | SAME | en013 | 1.00 | That is where our question about the open–closed principle (OCP) begins.
en014 | SAME | en014 | 1.00 | When a reviewer calls a proposed edit a violation, can the author recover from the verdict what the program was expected to accommodate or preserve?
en015 | SAME | en015 | 1.00 | We use over-axiomatization for the risk of treating such a verdict as settled when those premises are still open.
en016 | SAME | en016 | 1.00 | A benchmark that scores agreement with reference labels makes that question tractable.
en017 | SAME | en017 | 1.00 | Its archive lets us inspect the information actually supplied for classification.
en018 | SAME | en018 | 1.00 | To test what an acceptance decision requires, we hold a patch fixed and vary the task and the promise to existing callers.
en019 | SAME | en019 | 1.00 | We then return to drawing to see when a separate implementation can deliver an extension through the call the user already makes.
en020 | SAME | en020 | 1.00 | · · In 1996 Martin attributed the principle to Bertrand Meyer, citing page 23 of the 1988 first edition.
en021 | SAME | en021 | 1.00 | In Meyer’s account a module is closed once other modules can use it on the basis of a stable description.
en022 | SAME | en022 | 1.00 | His library example gives that stability a concrete test.
en023 | SAME | en023 | 1.00 | When technical reports become a new category, a program that handles each publication type explicitly may require edits to, or recompilation of, existing modules.
en024 | SAME | en024 | 1.00 | The choice of where to handle the new type matters to the modules that already depend on the catalog.
en025 | SAME | en025 | 1.00 | Having to edit a module to extend it was the issue in a June 1995 public exchange.
en026 | SAME | en026 | 1.00 | Kyle Brown argued that developers had to be able to fix a badly designed class.
en027 | SAME | en027 | 1.00 | Martin’s reply distinguished the right to edit a class from the need to edit it for an anticipated extension.
en028 | SAME | en028 | 1.00 | The design would still have to anticipate the right change.
en029 | SAME | en029 | 1.00 | The label SOLID appears in the public record by 2007.
en030 | SAME | en030 | 1.00 | In a 2009 discussion of interfaces, the distinction between a routine internal class and a public plugin API still mattered to the participants’ advice.
en031 | SAME | en031 | 1.00 | These sources document particular uses and disagreements about the principle.
en032 | SAME | en032 | 1.00 | A causal history of the acronym would require evidence of what changed as the label circulated.
en033 | EDIT | en033 | 0.71 | · · In the 1996 article Martin made sorting part of DrawAllShapes .
en034 | EDIT | en034 | 0.82 | In one implementation, Circle::Precedes puts a circle before a square by inspecting the other shape.
en035 | SAME | en035 | 0.97 | A new rule about where a third type ranks against a circle can send the edit back into Circle .
en036 | SAME | en036 | 1.00 | Martin moved the ranking of types into a table, so putting squares ahead of circles becomes a matter of swapping two entries.
en037 | SAME | en037 | 1.00 | If the next request were to sort individual shapes by area, the table would need information it does not contain.
en038 | EDIT | en038 | 0.70 | Later in the article Martin uses dynamic_cast in two routines.
en039 | EDIT | en039 | 0.57 | One version of DrawAllShapes recognizes circles and squares.
en040 | NEW | en039 | 0.21 | DrawSquaresOnly selects squares.
en041 | SAME | en040 | 1.00 | The first routine leaves a shape undrawn when its job is to draw them all.
en042 | SAME | en041 | 1.00 | The second skips exactly the shapes it is supposed to skip.
en043 | SAME | en042 | 1.00 | Here the names and stated jobs make the distinction available to the reader.
en044 | SAME | en043 | 1.00 | What can a classification reviewer establish when the input consists of code and a prompt?
en045 | NEW | en012 | 0.20 | · · Can the same code and the same patch warrant different maintenance decisions?
en046 | NEW | en137 | 0.14 | To examine this question, we record the information supplied to the reviewer separately from the decision it is meant to support.
en047 | NEW | en058 | 0.19 | We first inspect what was saved as input to a violation-classification benchmark.
en048 | NEW | en019 | 0.14 | In a separate catalog fixture, we then ask whether the decision is already settled when some facts relevant to it are withheld.
en049 | EDIT | en059 | 0.58 | We counted 48 OCP reference pairs and 768 saved response records as different units.
en050 | EDIT | en045 | 0.73 | A reference pair consists of a violation example and its revision.
en051 | EDIT | en046 | 0.76 | A saved record contains the submitted source, its prompt, and the recorded model response.
en052 | NEW | en059 | 0.15 | The archive has 16 OCP response files with 48 records each.
en053 | NEW | en074 | 0.12 | These are counts of records, not of distinct programs.
en054 | NEW | en047 | 0.41 | We checked that the submitted source occurred exactly once in each prompt, replaced that occurrence with a common placeholder, and counted the resulting instruction templates by exact string identity.
en055 | NEW | en048 | 0.15 | We then read the wording of the templates.
en056 | NEW | en019 | 0.15 | We call a requirement separately stated if the instruction asks for a new behavior in the particular case, such as drawing triangles.
en057 | NEW | en105 | 0.17 | A separately stated caller contract identifies behavior that must survive the change, such as keeping an existing width query available.
en058 | NEW | en062 | 0.23 | A direction to look for branches where polymorphism might fit is a general classification cue.
en059 | NEW | en060 | 0.14 | This reading concerns the instruction left after masking, so the result is scoped to that text.
en060 | NEW | en046 | 0.13 | The submitted source and other material in the archive can carry further context.
en061 | NEW | en049 | 0.29 | To check provenance, we compared the code in every saved OCP record with both sides of every OCP reference pair.
en062 | NEW | en068 | 0.22 | We compared the stored strings and repeated the comparison after stripping only leading and trailing whitespace.
en063 | NEW | en054 | 0.11 | This tests textual identity under two specified rules.
en064 | EDIT | en050 | 0.65 | For the Python reference pairs we used syntax trees to compare the method names declared directly by top-level classes, excluding names beginning with an underscore.
en065 | NEW | en051 | 0.27 | A disappearance in that comparison is evidence of a declaration change.
en066 | NEW | en052 | 0.26 | Inherited availability, actual use by clients, and a promise of continued availability each require their own evidence.
en067 | NEW | en085 | 0.23 | In the catalog fixture we fixed the existing source, the candidate patch, the inputs to the client, and the permission to add a module.
en068 | NEW | en128 | 0.15 | Through the existing client interface we recorded either the output string or the exception type and message.
en069 | NEW | en123 | 0.18 | We scored the new requirement and the protected legacy behavior separately.
en070 | NEW | en089 | 0.17 | Our fixture accepts a patch when it meets both conditions.
en071 | NEW | en015 | 0.15 | We then took the resulting rows and retained those matching the disclosed facts to see whether partial information sufficed to settle the verdict.
en072 | NEW | en053 | 0.38 | For the archive we inspected JSON and JSONL within the ZIP.
en073 | NEW | en054 | 0.23 | The catalog and drawing checks execute fixtures built for this study.
en074 | EDIT | en055 | 0.88 | Appendix A identifies the inputs and reproduction commands.
en075 | SAME | en056 | 1.00 | · Pehlivan et al. specified violation scenarios and refined the generated examples.
en076 | SAME | en057 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en077 | SAME | en058 | 1.00 | The benchmark compares model classifications with the reference labels.
en078 | NEW | en060 | 0.34 | Masking the submitted source in the saved OCP records left 24 distinct instruction templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE, and four SMELL.
en079 | NEW | en060 | 0.13 | No string was shared across strategies.
en080 | NEW | en087 | 0.21 | The templates gave no separate statement of either the change requested in a particular case or the caller contract protected in that case.
en081 | EDIT | en062 | 0.88 | One saved Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism would fit.
en082 | EDIT | en063 | 0.87 | The submitted AreaCalculator checks the shape type before calculating the area of a circle or rectangle.
en083 | SAME | en064 | 1.00 | The branch gives the reviewer somewhere to look if a new shape is requested.
en084 | SAME | en065 | 1.00 | The prompt leaves open whether that is the task and whether calls reading a rectangle’s width must still work after its area calculation moves.
en085 | SAME | en066 | 1.00 | Width becomes a concrete issue in the separate reference pair 37.
en086 | EDIT | en067 | 0.78 | That revision moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en087 | SAME | en068 | 1.00 | No saved submission matched either side of any reference pair, whether we compared the stored strings or trimmed whitespace at their ends.
en088 | SAME | en069 | 1.00 | In pair 37 we can establish that the declaration was removed.
en089 | SAME | en070 | 1.00 | Turning its removal into a reason to reject the patch would require evidence that existing callers were promised continued access to the width.
en090 | SAME | en071 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en091 | SAME | en072 | 1.00 | The saved prompt is on JSONL line 13 (record ID 12).
en092 | SAME | en073 | 1.00 | Reference pair 37 is in a separate ground-truth JSON file.
en093 | SAME | en075 | 1.00 | · · · Bräuer et al. (2018) asked experts how much of a design principle their measurable practices covered.
en094 | SAME | en076 | 1.00 | Cabral et al. (2024) asked participants about understanding and ease of extension in a machine-learning scenario under a bundled SOLID treatment.
en095 | SAME | en077 | 1.00 | Zhu et al. (2026) gave specific repository change tasks and checked them against functional tests and structural oracles.
en096 | NEW | en070 | 0.33 | Reference pair 37 leaves open whether callers were promised continued access to the width.
en097 | NEW | en143 | 0.13 | The next section tests what a fact of that kind can do for a decision.
en098 | NEW | en089 | 0.17 | We use a fixture that lets us change the applicable requirement or contract while leaving the code and the patch in place.
en099 | NEW | en080 | 0.46 | · · We built a small version of Meyer’s library catalog.
en100 | NEW | en128 | 0.17 | The existing client.py renders each item through the catalog function passed to it.
en101 | NEW | en081 | 0.14 | The candidate patch adds reports.py , which wraps that function, leaving the contents of catalog.py and client.py identical.
en102 | EDIT | en082 | 0.79 | The client now renders technical reports and still rejects requests for errata.
en103 | NEW | en084 | 0.23 | In book output the prefix changes from book to BOOK .
en104 | NEW | en086 | 0.22 | Give two reviewers the same patch, the same execution record, and a request to handle technical reports alone.
en105 | NEW | en070 | 0.23 | Tell one that existing callers were promised the original book output.
en106 | NEW | en094 | 0.17 | Tell the other that book output is outside the contract.
en107 | NEW | en094 | 0.14 | Both see the same change in the book prefix.
en108 | NEW | en089 | 0.21 | Whether it violates a commitment depends on the applicable contract.
en109 | NEW | en016 | 0.17 | Table 2 crosses these two contracts with requests that either include or exclude errata.
en110 | EDIT | en087 | 0.59 | Both contracts preserve the rendering of journals and proceedings and the rejection of a separate unsupported publication type.
en111 | SAME | en090 | 1.00 | Two requirements for accepting a fixed patch.
en112 | NEW | en096 | 0.18 | For a decision under partial information, keep the rows compatible with the disclosed facts.
en113 | NEW | en091 | 0.46 | Learning that the release must support errata leaves the bottom two rows.
en114 | NEW | en092 | 0.37 | Both reject the patch, so the book contract can remain open.
en115 | NEW | en086 | 0.24 | Learning that technical reports are the entire request leaves the top two rows.
en116 | NEW | en148 | 0.21 | One accepts and one rejects.
en117 | NEW | en088 | 0.22 | The question to ask next is whether the original book output was protected.
en118 | EDIT | en097 | 0.51 | This procedure assumes that the actual specification is among the cases considered.
en119 | NEW | en097 | 0.15 | If no row fits what is disclosed, the first step is to check that specification set against the disclosed facts.
en120 | NEW | en099 | 0.13 | If both verdicts remain, a rule that receives the same information cannot choose one binary answer that is right in every compatible case.
en121 | NEW | en099 | 0.32 | The reviewer can give the conditional answers or defer the verdict.
en122 | NEW | en101 | 0.30 | Appendix A gives all nine settings obtained by disclosing or withholding the two fields in this case.
en123 | NEW | en095 | 0.22 | We also ran a second patch to check whether the stricter specification was feasible under the same edit boundary.
en124 | NEW | en082 | 0.24 | A single added module handles technical reports and errata and keeps the original book output.
en125 | NEW | en097 | 0.15 | The rejections in Table 2 concern a specific patch under a specification that an alternative can meet.
en126 | NEW | en097 | 0.14 | For another case, reporting the candidate specifications and the evidence for including them makes it possible to turn a deferred verdict into a concrete question.
en127 | SAME | en103 | 1.00 | · In the catalog case we asked whether to accept a completed patch.
en128 | SAME | en104 | 1.00 | Choosing an implementation raises a further question.
en129 | SAME | en105 | 1.00 | Given a place for the new behavior and a function through which callers must reach it, which existing files have to change?
en130 | SAME | en106 | 1.00 | We return to drawing, comparing one implementation organized by operation with another organized by shape.
en131 | SAME | en107 | 1.00 | The counts below are for candidates we built and ran.
en132 | SAME | en108 | 1.00 | To add a triangle in the shape layout, we added one file.
en133 | SAME | en109 | 1.00 | In the operation layout we edited the existing file that handled drawing.
en134 | SAME | en110 | 1.00 | A request for a labeling operation reversed the comparison.
en135 | SAME | en111 | 1.00 | We edited the circle and square files in the shape layout and added a new file in the operation layout.
en136 | SAME | en112 | 1.00 | All four candidates passed their functional checks.
en137 | SAME | en113 | 1.00 | Which layout required edits to existing files depended on the request (Figure 1A).
en138 | EDIT | en114 | 0.87 | To see whether that difference would persist under a common request, we added render_many to both layouts.
en139 | SAME | en115 | 1.00 | It takes a list of shapes and brackets each result.
en140 | SAME | en116 | 1.00 | We predicted that assigning the transformation to the shapes in the shape layout would require editing both their files.
en141 | SAME | en117 | 1.00 | With a shared adapter available, we expected each layout to support the feature in one new file while leaving the existing files intact.
en142 | SAME | en118 | 1.00 | The only candidate that edited existing files was the one assigning the transformation to the shape files.
en143 | SAME | en119 | 1.00 | All four added a file, preserved order and duplicates, handled empty lists and unsupported shapes as specified, and kept the existing circle and square renderings (Figure 1B).
en144 | SAME | en120 | 1.00 | Existing source files edited.
en145 | SAME | en121 | 1.00 | Panel A compares adding a triangle with adding a labeling operation.
en146 | SAME | en122 | 1.00 | Panel B holds the batch-rendering request fixed and varies the placement rule.
en147 | SAME | en123 | 1.00 | All four candidates in panel B passed the new and legacy behavior checks and added one file each.
en148 | SAME | en124 | 1.00 | · · · · An adapter can sit in a new file even when an existing caller has no way to use it.
en149 | SAME | en125 | 1.00 | We tested this with a separate request for an option that brackets the result of a single render.
en150 | SAME | en126 | 1.00 | Both layouts offered the option through a new function.
en151 | EDIT | en127 | 0.82 | When we tried bracketed=True on the old function after adding the same adapter, the function rejected the argument.
en152 | SAME | en128 | 1.00 | The candidates that delivered the option through the original function edited one existing file in the operation layout and two in the shape layout.
en153 | SAME | en129 | 1.00 | From a separate baseline in which the original function could already load an external decorator, a new file alone connected the option to that function in each layout (Table 3).
en154 | SAME | en130 | 1.00 | Call paths for the new rendering option.
en155 | SAME | en131 | 1.00 | The last row of Table 3 starts counting after the hook is in place.
en156 | SAME | en132 | 1.00 | We left the initial cost of introducing it outside the measurement.
en157 | SAME | en133 | 1.00 | Relating these file counts to actual maintenance effort would require a separate measurement.
en158 | NEW | en134 | 0.37 | · Seeing a square drawn first gives a reviewer a reason to change the drawing function when putting circles first is that function’s job.
en159 | NEW | en018 | 0.17 | In the catalog we could hold the execution record fixed and vary the requirements and commitments that specify the job.
en160 | NEW | en136 | 0.18 | An errata requirement settled rejection immediately.
en161 | NEW | en094 | 0.20 | When technical reports were the whole request, the decision still turned on whether the original book output was protected.
en162 | NEW | en078 | 0.13 | The method in this paper makes the compatible specifications visible for a fixed patch and tests which fact would settle the decision.
en163 | NEW | en043 | 0.14 | In a repository review, requirements and tests may help establish the scope of a promise.
en164 | NEW | en097 | 0.16 | A specification can also name the required call path, as in Section 6.
en165 | NEW | en097 | 0.12 | Which sources justify including a specification and which observations suffice to test it remain open to comparison across cases and methods.
en166 | EDIT | en141 | 0.71 | Our evidence comes from the saved material of one benchmark and the examples we built and ran.
en167 | SAME | en144 | 1.00 | For Sections 3–4 the audit reads the archived JSON and JSONL.
en168 | SAME | en145 | 1.00 | For Sections 5–6 the fixtures run the examples constructed for this study.
en169 | SAME | en146 | 1.00 | The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.
en170 | SAME | en147 | 1.00 | When a field is withheld, both of its recorded values remain possible.
en171 | SAME | en148 | 1.00 | Defer means that at least one compatible row accepts the patch and at least one rejects it.
Summary en: SAME 89, EDIT 18, NEW 64

## v12 · [Source](https://app.notion.com/p/41bef561cf9281e1864afb74a3bbb4ce)
### ko (129 segmented sentences)
ko001 | SAME | ko001 | 1.00 | 로버트 마틴이 1996년에 예로 든 함수는 목록에 들어온 순서대로 도형을 그린다.
ko002 | NEW | ko002 | 0.46 | 삼각형이 자신을 그리는 메서드를 갖고 있으면 이 함수에 손대지 않고 삼각형을 추가할 수 있다.
ko003 | NEW | ko003 | 0.18 | 기존 함수에 사각형으로 시작하는 목록을 넘기면 여전히 사각형부터 그린다.
ko004 | EDIT | ko004 | 0.63 | 호출자가 원을 앞에 모아 넘기기로 했다면 함수는 제 일을 한다.
ko005 | NEW | ko005 | 0.35 | 함수가 어떤 목록을 받아도 그 순서를 보장하기로 했다면 고쳐야 한다.
ko006 | NEW | ko007 | 0.06 | 소스에서 그리는 순서를 읽을 수는 있지만, 그 순서가 잘못됐는지는 누가 정렬을 맡았는지에 달려 있다.
ko007 | NEW | ko121 | 0.05 | 마틴의 그리기 함수는 도형을 하나 더 추가할 때는 그대로 둘 수 있었다.
ko008 | NEW | ko009 | 0.15 | 개방–폐쇄 원칙(OCP)을 들어 수정안을 거절하려면, 먼저 어떤 변경을 처리하고 어떤 동작을 계속 제공해야 하는지 밝혀야 한다.
ko009 | NEW | ko040 | 0.33 | 분류 벤치마크의 저장 자료에서 모델에 어떤 지시가 주어졌는지 확인했다.
ko010 | NEW | ko144 | 0.21 | 이어 도서관 예제에서 코드와 수정안을 고정한 채 새 요구와 기존 호출자에게 한 약속을 바꿨다.
ko011 | NEW | ko014 | 0.29 | 도형 예제로 돌아가서는 별도 파일에 넣은 기능을 기존 함수로도 쓸 수 있는지 확인했다.
ko012 | EDIT | ko015 | 0.70 | · · 마틴은 1996년 글에서 베르트랑 마이어의 1988년 초판 23쪽을 인용했다.
ko013 | EDIT | ko016 | 0.56 | 마이어에게 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 쓸 수 있는 모듈이다.
ko014 | NEW | ko018 | 0.29 | 그의 도서관 예제에서 자료 유형을 하나씩 구별해 처리하는 프로그램에 기술보고서를 추가하면, 기존 모듈까지 고치거나 다시 컴파일해야 할 수 있다.
ko015 | NEW | ko019 | 0.18 | 새 자료를 처리하는 코드의 위치에 따라 기존 모듈에 손이 가는 범위가 달라진다.
ko016 | EDIT | ko021 | 0.55 | 1995년 6월 공개 토론에서 카일 브라운은 잘못 설계된 클래스라면 소스를 고칠 수 있어야 한다고 했다.
ko017 | NEW | ko022 | 0.40 | 마틴은 예상한 확장을 위해 기존 소스를 반드시 고쳐야 하는지를 물었다.
ko018 | EDIT | ko023 | 0.52 | 그러려면 어떤 변경이 생길지 미리 짚어야 한다.
ko019 | SAME | ko024 | 1.00 | 2007년 공개 기록에는 다섯 원칙을 묶은 SOLID라는 이름이 나온다.
ko020 | EDIT | ko025 | 0.62 | 2009년 인터페이스 논쟁에서는 내부 클래스와 공개 플러그인 API에 서로 다른 조언이 제시됐다.
ko021 | NEW | ko056 | 0.13 | 이 기록에서 확인할 수 있는 것은 당시 어떤 이유로 원칙을 적용했는지다.
ko022 | EDIT | ko028 | 0.75 | · · 마틴은 목록 정렬을 DrawAllShapes 가 맡게 했다.
ko023 | EDIT | ko029 | 0.57 | 한 구현에서 Circle::Precedes 는 상대 도형이 사각형이면 원을 먼저 놓는다.
ko024 | NEW | ko030 | 0.28 | 원과 세 번째 도형의 순서를 정하려면 Circle 도 고쳐야 할 수 있다.
ko025 | NEW | ko031 | 0.30 | 반면 도형 종류별 순서를 표에 두면 사각형을 먼저 놓기 위해 표의 두 항목만 바꾸면 된다.
ko026 | EDIT | ko032 | 0.51 | 개별 도형을 넓이순으로 그리려면 그 표에 없는 정보가 필요하다.
ko027 | NEW | ko033 | 0.27 | 마틴이 글 후반에 비교한 두 함수는 dynamic_cast 를 쓴다.
ko028 | EDIT | ko034 | 0.92 | DrawAllShapes 의 한 구현은 원과 사각형을 골라 그리고, DrawSquaresOnly 는 사각형만 그린다.
ko029 | NEW | ko035 | 0.12 | 모든 도형을 그려야 할 때는 출력이 하나 빠진 셈이다.
ko030 | NEW | ko037 | 0.16 | 코드와 프롬프트만 주어진 검토자는 각 함수에 어느 책임이 있는지 어디까지 알 수 있을까?
ko031 | NEW | ko012 | 0.09 | · · 벤치마크에서는 모델에 주어진 지시를 확인했다.
ko032 | NEW | ko113 | 0.14 | 도서관 예제에서는 요구와 계약 가운데 일부만 알려졌을 때도 같은 수정안에 한 가지 결론을 내릴 수 있는지 확인했다.
ko033 | NEW | ko042 | 0.15 | OCP 참조 쌍 48개에는 각각 위반 예시와 그 수정본이 들어 있다.
ko034 | NEW | ko045 | 0.11 | 저장 응답은 16개 파일에 48행씩, 총 768행이다.
ko035 | NEW | ko044 | 0.37 | 각 행에는 제출 코드, 프롬프트, 기록된 모델 응답이 있다.
ko036 | NEW | ko087 | 0.08 | 같은 프로그램이 여러 행에 걸쳐 나올 수 있다.
ko037 | NEW | ko047 | 0.19 | 프롬프트마다 제출 코드가 한 번만 나오는지 확인하고 그 자리를 공통 표시로 바꿨다.
ko038 | NEW | ko048 | 0.37 | 남은 문자열이 완전히 같으면 한 종류의 지시문 틀로 셌다.
ko039 | NEW | ko040 | 0.10 | 틀의 문구를 직접 읽어 요구와 계약이 따로 적혀 있는지 확인했다.
ko040 | NEW | ko051 | 0.33 | “삼각형도 그려야 한다”처럼 해당 사례의 새 동작을 요구하면 변경 요구로, “기존 너비 조회는 계속 지원해야 한다”처럼 유지할 동작을 밝히면 호출자 계약으로 보았다.
ko041 | EDIT | ko052 | 0.50 | 반복 분기에 다형성을 적용할 수 있는지 묻는 문구는 일반적인 판별 단서다.
ko042 | NEW | ko067 | 0.09 | 이 검토는 코드를 가리고 남은 지시문을 대상으로 했다.
ko043 | NEW | ko053 | 0.19 | 제출 코드나 아카이브의 다른 문서에는 추가 단서가 있을 수 있다.
ko044 | NEW | ko054 | 0.40 | 저장 행의 제출 코드를 모든 OCP 참조 쌍의 수정 전후 소스와 대조했다.
ko045 | NEW | ko055 | 0.16 | 원문 그대로 비교한 뒤 양끝 공백만 없애고 다시 비교했다.
ko046 | EDIT | ko057 | 0.67 | Python 참조 쌍에서는 구문 트리에서 최상위 클래스가 직접 선언한 메서드 이름을 비교했다.
ko047 | NEW | ko058 | 0.27 | 상속을 통해 계속 호출할 수 있는지, 누군가 실제로 호출했는지, 그 호출을 계속 지원하기로 했는지는 각각 별도의 근거가 필요하다.
ko048 | EDIT | ko059 | 0.74 | 도서관 예제에서는 원래 소스, 수정안, 호출 입력과 편집 범위를 고정했다.
ko049 | NEW | ko060 | 0.15 | 기존 클라이언트로 호출해 출력 문자열 또는 예외 유형과 메시지를 기록했다.
ko050 | NEW | ko060 | 0.09 | 새 요구를 충족하고 기존 계약도 지킨 경우를 승인으로 셌다.
ko051 | NEW | ko062 | 0.10 | 일부 정보만 주어진 경우에는 판정표에서 그 정보와 맞는 행만 남겼다.
ko052 | NEW | ko040 | 0.09 | 그 행들이 모두 같은 결론을 가리키는지 확인했다.
ko053 | NEW | ko063 | 0.25 | 벤치마크는 ZIP에 든 JSON과 JSONL을 읽어 감사했고, 도서관과 도형 예제는 직접 작성해 실행했다.
ko054 | EDIT | ko065 | 0.54 | · Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko055 | SAME | ko066 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko056 | NEW | ko076 | 0.02 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko057 | EDIT | ko067 | 0.57 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko058 | EDIT | ko068 | 0.62 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko059 | EDIT | ko069 | 0.50 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko060 | EDIT | ko070 | 0.69 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko061 | SAME | ko071 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko062 | NEW | ko072 | 0.29 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko063 | NEW | ko073 | 0.34 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko064 | EDIT | ko075 | 0.79 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko065 | NEW | ko076 | 0.11 | 저장된 제출 코드 가운데 어느 참조 쌍의 수정 전후 소스와도 일치한 것은 없었다.
ko066 | NEW | ko077 | 0.06 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko067 | NEW | ko078 | 0.25 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko068 | EDIT | ko079 | 0.63 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko069 | NEW | ko080 | 0.27 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko070 | NEW | ko081 | 0.35 | · · · Bräuer 등(2018)은 측정 가능한 실천 규칙으로 설계 원칙의 어떤 부분을 포착할 수 있는지 전문가에게 물었다.
ko071 | EDIT | ko082 | 0.89 | Cabral 등(2024)은 기계학습 기능을 확장하는 상황에서 SOLID를 적용한 코드에 대해 참가자가 느낀 이해도와 확장 용이성을 조사했다.
ko072 | NEW | ko083 | 0.44 | Zhu 등(2026)은 저장소에 구체적인 변경을 요구하고 기능 테스트와 구조 판정 기준을 적용했다.
ko073 | NEW | ko013 | 0.17 | 다음 절에서는 수정안을 고정하고, 검토자가 알고 있는 요구와 계약에 따라 승인 결론이 달라지는지 살핀다.
ko074 | EDIT | ko088 | 0.49 | · · 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko075 | EDIT | ko089 | 0.58 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko076 | NEW | ko090 | 0.37 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko077 | NEW | ko091 | 0.35 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko078 | NEW | ko093 | 0.27 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko079 | NEW | ko094 | 0.19 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko080 | NEW | ko073 | 0.06 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko081 | NEW | ko098 | 0.17 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko082 | NEW | ko100 | 0.29 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko083 | EDIT | ko102 | 0.72 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko084 | NEW | ko103 | 0.28 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko085 | NEW | ko104 | 0.21 | 실제 명세가 검토하는 경우들 가운데 하나라는 전제에서 이 절차가 성립한다.
ko086 | NEW | ko105 | 0.33 | 공개된 사실과 맞는 행이 없다면 명세 후보와 공개된 사실부터 다시 대조해야 한다.
ko087 | NEW | ko106 | 0.17 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko088 | NEW | ko107 | 0.26 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko089 | NEW | ko108 | 0.09 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko090 | SAME | ko109 | 1.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko091 | EDIT | ko110 | 0.59 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko092 | NEW | ko109 | 0.06 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko093 | NEW | ko112 | 0.12 | 다른 사례에서도 가능한 명세와 각각의 근거를 명시하면, 보류된 판정을 확정하기 위해 다음에 무엇을 확인할지 알 수 있다.
ko094 | NEW | ko126 | 0.15 | · 새 기능을 별도 파일에 넣을 수 있다면 기존 파일을 그대로 둘 수 있을까?
ko095 | EDIT | ko116 | 0.72 | 도형 예제로 돌아가 연산별로 파일을 나눈 구현과 도형별로 나눈 구현을 비교했다.
ko096 | NEW | ko117 | 0.13 | 실행해 본 후보마다 수정한 기존 파일의 수를 셌다.
ko097 | NEW | ko119 | 0.18 | 삼각형을 추가하려면 도형별 구현에서는 새 파일 하나면 됐고, 연산별 구현에서는 기존 그리기 파일을 고쳐야 했다.
ko098 | NEW | ko121 | 0.36 | 원과 사각형 파일을 각각 고쳐야 했던 도형별 구현과 달리, 연산별 구현은 새 파일에 연산을 둘 수 있었다.
ko099 | NEW | ko132 | 0.15 | 네 수정안 모두 기능 검사를 통과했다(그림 1A).
ko100 | NEW | ko123 | 0.45 | 이 차이가 같은 요구에서도 나타나는지 보려고 두 구현에 render_many 를 추가했다.
ko101 | SAME | ko124 | 1.00 | 도형 목록을 받아 각 출력에 대괄호를 붙이는 함수다.
ko102 | NEW | ko125 | 0.22 | 변환을 각 도형에 맡기면 도형별 구현의 원과 사각형 파일을 고쳐야 한다고 예상했다.
ko103 | NEW | ko126 | 0.19 | 공용 어댑터를 허용하면 두 구현에서 기존 파일을 그대로 둘 수 있을 것으로 봤다.
ko104 | NEW | ko125 | 0.17 | 실제로 원과 사각형 파일을 고친 후보는 변환을 각 도형에 맡긴 경우뿐이었다.
ko105 | NEW | ko128 | 0.25 | 네 후보에서 입력 순서와 중복, 기존 원·사각형 렌더링은 유지됐고 빈 목록과 미지원 도형은 명세대로 처리됐다(그림 1B).
ko106 | SAME | ko130 | 1.00 | A는 삼각형 추가와 이름표 연산 추가를 비교한다.
ko107 | NEW | ko131 | 0.36 | B는 같은 배치 렌더링 요구에서 파일 배치 규칙을 바꾼 결과다.
ko108 | NEW | ko132 | 0.40 | B의 네 후보는 모두 새 기능과 기존 동작 검사를 통과했고 새 파일을 하나씩 추가했다.
ko109 | NEW | ko135 | 0.20 | · · · · 다음 비교에서는 렌더링 결과 하나를 요청에 따라 대괄호로 감싸는 기능을 넣었다.
ko110 | NEW | ko136 | 0.38 | 두 구현 모두 새 함수로 이 기능을 제공했다.
ko111 | EDIT | ko137 | 0.53 | 같은 어댑터를 추가한 상태에서 기존 함수에 bracketed=True 를 넘기면 오류가 났다.
ko112 | NEW | ko138 | 0.25 | 기존 함수에서 옵션을 받도록 하려면 연산별 후보는 기존 파일 하나, 도형별 후보는 두 개를 고쳤다.
ko113 | EDIT | ko139 | 0.49 | 기존 함수가 외부 변환 모듈을 불러오는 별도 기준선에서는 두 후보 모두 새 파일 하나로 옵션을 연결했다(표 3).
ko114 | NEW | ko140 | 0.27 | 표 3의 마지막 행은 확장 지점을 마련한 다음부터 센 것이다.
ko115 | NEW | ko119 | 0.10 | 이 비교에서 센 것은 기존 파일 수정 수다.
ko116 | NEW | ko141 | 0.13 | 확장 지점을 처음 만드는 비용이나 실제 유지보수 작업량은 각각 따로 측정해야 한다.
ko117 | NEW | ko143 | 0.33 | · 사각형을 먼저 그린 함수에 수정을 요구하려면, 원을 먼저 놓는 일이 그 함수의 책임이라는 근거가 필요했다.
ko118 | NEW | ko059 | 0.10 | 도서관 예제에서도 판정을 가른 것은 어떤 동작이 요구되고 보호되는가였다.
ko119 | NEW | ko145 | 0.21 | 정오표가 필수라면 그 사실만으로 수정안을 거절할 수 있었다.
ko120 | NEW | ko146 | 0.24 | 기술보고서만 필요하다면 기존 책 출력을 보호하기로 했는지에 따라 결론이 달라졌다.
ko121 | NEW | ko147 | 0.07 | 같은 수정안을 검토하다 결론이 갈리면, 현재 알려진 사실과 맞는 명세를 남기고 어느 차이가 판정을 바꾸는지 확인할 수 있다.
ko122 | NEW | ko151 | 0.29 | 이 글에서는 한 벤치마크의 저장 자료와 직접 작성한 예제로 그 방법을 보였다.
ko123 | NEW | ko058 | 0.08 | 실제 저장소에서 어떤 문서나 테스트를 근거로 계약을 확정할 수 있는지, 검증하려는 기능이 어느 호출 경로에서 동작해야 하는지는 사례마다 추가 근거가 필요하다.
ko124 | NEW | ko063 | 0.24 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko125 | NEW | ko153 | 0.17 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko126 | NEW | ko154 | 0.40 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko127 | NEW | ko155 | 0.26 | 그림 1의 소스와 출력은 캡션 아래에 연결했다.
ko128 | NEW | ko156 | 0.18 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko129 | NEW | ko157 | 0.26 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
Summary ko: SAME 7, EDIT 28, NEW 94

### en (151 segmented sentences)
en001 | EDIT | en001 | 0.59 | In 1996 Robert Martin described a function that draws shapes in the order it receives them.
en002 | EDIT | en002 | 0.59 | A triangle can be added without touching the function if the triangle supplies its own drawing method.
en003 | NEW | en003 | 0.13 | Then Martin changes the task.
en004 | EDIT | en004 | 0.69 | Every circle must be drawn before any square.
en005 | EDIT | en005 | 0.73 | Give the function a list that begins with a square and it still draws the square first.
en006 | NEW | en006 | 0.39 | Who was supposed to put the circles first?
en007 | NEW | en006 | 0.23 | If the caller agreed to sort the list, the routine does its job.
en008 | NEW | en008 | 0.31 | If the routine must guarantee that order for any list, it needs an edit.
en009 | NEW | en009 | 0.38 | The source tells us what gets drawn first.
en010 | NEW | en010 | 0.26 | The agreement tells us whether that is a problem.
en011 | NEW | en041 | 0.15 | Martin’s drawing routine could stay as it was when the task was to add a shape.
en012 | NEW | en012 | 0.11 | Making it responsible for sorting changes that judgment.
en013 | NEW | en014 | 0.19 | A reviewer invoking the open–closed principle (OCP) to reject a patch needs to say what change the program must accommodate and what behavior it must preserve.
en014 | NEW | en047 | 0.29 | We inspect a classification benchmark’s archive to see what instructions its models received.
en015 | NEW | en018 | 0.28 | In a separate catalog example we keep the code and patch fixed while varying the request and the promises to existing callers.
en016 | NEW | en019 | 0.30 | We then return to drawing to test whether a feature added in a separate file can be reached through the original function.
en017 | EDIT | en020 | 0.92 | · · Martin attributed the principle to Bertrand Meyer, citing page 23 of the 1988 first edition.
en018 | NEW | en021 | 0.27 | For Meyer, a closed module has a stable specification that other modules can rely on.
en019 | NEW | en022 | 0.35 | His library example gives this a practical meaning.
en020 | NEW | en023 | 0.38 | If a catalog handles publication types one by one, adding technical reports can require editing or recompiling existing modules.
en021 | NEW | en129 | 0.12 | Where the new code goes affects how much of the existing system must change.
en022 | EDIT | en026 | 0.71 | In a June 1995 public exchange, Kyle Brown argued that developers had to be able to fix a badly designed class.
en023 | NEW | en027 | 0.30 | Martin asked whether an anticipated extension had to require an edit to existing source.
en024 | NEW | en028 | 0.19 | That answer still depends on which changes can be anticipated.
en025 | NEW | en029 | 0.30 | The public record uses SOLID for the five principles by 2007.
en026 | NEW | en030 | 0.34 | A 2009 discussion gave different advice for internal classes and public plugin APIs.
en027 | NEW | en031 | 0.22 | These records show why particular participants applied the principle as they did.
en028 | NEW | en033 | 0.35 | · · Martin made DrawAllShapes responsible for sorting.
en029 | EDIT | en034 | 0.67 | In one implementation Circle::Precedes checks the other shape and puts a circle before a square.
en030 | NEW | en035 | 0.20 | Deciding where a third shape belongs relative to a circle can require an edit to Circle .
en031 | NEW | en036 | 0.25 | Placing the order of types in a table lets squares go first with a swap of two entries.
en032 | NEW | en037 | 0.45 | Sorting individual shapes by area would require information that the table does not hold.
en033 | EDIT | en038 | 0.52 | Later in the article Martin compares two uses of dynamic_cast .
en034 | EDIT | en039 | 0.57 | One version of DrawAllShapes draws circles and squares, and DrawSquaresOnly draws squares alone.
en035 | NEW | en041 | 0.19 | A triangle left undrawn is a missed output when the task is to draw all shapes.
en036 | NEW | en040 | 0.19 | When the task is to draw squares, skipping it is correct.
en037 | NEW | en044 | 0.21 | How much of that responsibility can a reviewer determine from code and a prompt?
en038 | NEW | en077 | 0.19 | · · In the benchmark we examine the instructions given to the models.
en039 | NEW | en080 | 0.17 | In the catalog example we test whether a single verdict follows when only part of the request or contract is disclosed.
en040 | NEW | en050 | 0.47 | The archive contains 48 OCP reference pairs, each with a violation example and its revision.
en041 | NEW | en052 | 0.26 | The saved responses occupy 16 files of 48 records each, for a total of 768 records.
en042 | NEW | en051 | 0.40 | Each record has submitted code, a prompt and a recorded model response.
en043 | NEW | en053 | 0.16 | A program can appear in more than one record.
en044 | NEW | en054 | 0.37 | We checked that the submitted code occurred once per prompt, then replaced it with a common placeholder.
en045 | NEW | en054 | 0.18 | We counted templates by exact equality of the remaining strings.
en046 | NEW | en069 | 0.24 | We read the templates for separately stated requirements and contracts.
en047 | NEW | en056 | 0.21 | An instruction such as asking for triangles to be drawn specifies a change in that case.
en048 | NEW | en057 | 0.33 | Asking that an existing width query remain available states a caller contract.
en049 | EDIT | en058 | 0.78 | A direction to look for repeated branches where polymorphism might fit gives a general classification cue.
en050 | NEW | en059 | 0.37 | We applied this reading to the instructions after masking the code.
en051 | EDIT | en060 | 0.49 | The submitted code and other archive material can supply further context.
en052 | NEW | en062 | 0.35 | We compared each saved submission with both sides of every OCP reference pair, first as stored and then after stripping leading and trailing whitespace.
en053 | EDIT | en064 | 0.71 | For the Python pairs we used syntax trees to compare the method names declared directly by top-level classes, omitting names that begin with an underscore.
en054 | NEW | en065 | 0.43 | That comparison can show that a declaration disappeared.
en055 | NEW | en089 | 0.26 | Establishing whether callers could still reach it through inheritance, used it in practice, or had been promised continued access requires separate evidence.
en056 | NEW | en067 | 0.29 | In the catalog we fixed the initial source, patch, caller inputs and edit boundary, which permitted adding a module.
en057 | EDIT | en068 | 0.77 | Through the existing client we recorded the output string or the exception type and message.
en058 | NEW | en098 | 0.23 | We counted a patch as acceptable when it met the new requirement and preserved the applicable contract.
en059 | NEW | en071 | 0.27 | For partial disclosure we retained the rows consistent with the disclosed facts and checked whether they agreed.
en060 | NEW | en072 | 0.41 | For the archive audit we read the JSON and JSONL in the ZIP.
en061 | NEW | en073 | 0.43 | For the catalog and drawing checks we ran examples written for this study.
en062 | NEW | en074 | 0.44 | Appendix A gives the inputs and commands.
en063 | EDIT | en075 | 0.76 | · Pehlivan et al. chose violation scenarios and refined the generated examples.
en064 | SAME | en076 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en065 | EDIT | en077 | 0.77 | The benchmark compares model classifications with the resulting labels.
en066 | EDIT | en078 | 0.59 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en067 | NEW | en079 | 0.42 | No two strategies shared a template string.
en068 | NEW | en080 | 0.38 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en069 | EDIT | en081 | 0.75 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en070 | EDIT | en082 | 0.60 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en071 | NEW | en083 | 0.26 | If a new shape is needed, that branch is a place to look.
en072 | NEW | en084 | 0.41 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en073 | EDIT | en086 | 0.68 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en074 | NEW | en087 | 0.36 | None of the code saved as model submissions matched either side of any reference pair.
en075 | NEW | en062 | 0.15 | Trimming outer whitespace yielded the same result.
en076 | EDIT | en088 | 0.57 | Pair 37 establishes that a declaration was removed.
en077 | NEW | en089 | 0.38 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en078 | SAME | en090 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en079 | EDIT | en091 | 0.50 | The prompt example is in JSONL line 13 (record ID 12).
en080 | EDIT | en092 | 0.64 | Pair 37 is in a separate reference JSON file.
en081 | EDIT | en093 | 0.56 | · · · Bräuer et al. (2018) asked experts which parts of a design principle were captured by measurable practices.
en082 | EDIT | en094 | 0.63 | Cabral et al. (2024) asked participants how easy they found it to understand and extend code under a bundled SOLID treatment in a machine-learning scenario.
en083 | NEW | en095 | 0.46 | Zhu et al. (2026) set repository change tasks and used functional and structural checks.
en084 | NEW | en098 | 0.24 | In the next section we fix the patch and ask whether knowing a different requirement or caller contract changes the verdict.
en085 | NEW | en099 | 0.35 | · · We built a small catalog based on Meyer’s example.
en086 | EDIT | en100 | 0.48 | The client in client.py displays each publication through the catalog function passed to it.
en087 | NEW | en101 | 0.30 | The patch adds reports.py to wrap that function.
en088 | NEW | en101 | 0.25 | The source of catalog.py and client.py stays identical.
en089 | NEW | en102 | 0.38 | The resulting catalog displays technical reports and still rejects errata.
en090 | NEW | en013 | 0.07 | For books it now prints BOOK where it used to print book .
en091 | NEW | en104 | 0.23 | Suppose the only new requirement is to handle technical reports.
en092 | NEW | en105 | 0.41 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en093 | NEW | en106 | 0.39 | If the book output is outside the contract, the same patch can be accepted.
en094 | NEW | en109 | 0.18 | Table 2 applies both contracts again when errata are also required.
en095 | NEW | en110 | 0.43 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en096 | SAME | en111 | 1.00 | Two requirements for accepting a fixed patch.
en097 | NEW | en113 | 0.33 | Learning that errata are required leaves the last two rows of Table 2.
en098 | NEW | en114 | 0.48 | Both reject the patch, so the book contract need not be settled first.
en099 | EDIT | en115 | 0.66 | Learning that technical reports are the whole request leaves the first two rows.
en100 | SAME | en116 | 1.00 | One accepts and one rejects.
en101 | EDIT | en117 | 0.67 | The next question is whether the original book output is protected.
en102 | EDIT | en118 | 0.84 | This procedure assumes that the actual specification is among the cases under consideration.
en103 | NEW | en119 | 0.46 | If no row fits what was disclosed, the reviewer needs to recheck the candidate specifications against the facts.
en104 | NEW | en120 | 0.33 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en105 | EDIT | en121 | 0.55 | The reviewer can give a conditional answer or defer judgment.
en106 | EDIT | en122 | 0.53 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en107 | EDIT | en123 | 0.78 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en108 | EDIT | en124 | 0.77 | It adds one module, handles technical reports and errata, and keeps the original book output.
en109 | NEW | en125 | 0.19 | A rejection in Table 2 need not end the search for a patch within that boundary.
en110 | NEW | en126 | 0.33 | In another case, recording the possible specifications and the evidence for each can tell a reviewer what to check next.
en111 | NEW | en133 | 0.16 | · If a feature can go in a separate file, can the existing files stay as they are?
en112 | NEW | en130 | 0.43 | We return to drawing and compare two layouts, one organized by operation and one by shape.
en113 | NEW | en142 | 0.24 | We count the existing files actually edited by the candidates we ran.
en114 | NEW | en135 | 0.39 | Adding a triangle took one new file in the shape layout and an edit to the drawing file in the operation layout.
en115 | NEW | en135 | 0.46 | For a labeling operation, the shape layout needed edits to both the circle and square files.
en116 | NEW | en135 | 0.30 | The operation layout could add the labels in one new file.
en117 | EDIT | en136 | 0.73 | All four candidates passed the functional checks (Figure 1A).
en118 | NEW | en107 | 0.17 | We then gave both layouts the same task.
en119 | EDIT | en139 | 0.67 | The new render_many takes a list of shapes and brackets each result.
en120 | NEW | en142 | 0.22 | We expected both shape files to change when each shape owned its transformation.
en121 | NEW | en141 | 0.30 | Allowing a shared adapter, we expected both layouts to leave existing files alone.
en122 | EDIT | en142 | 0.66 | The only candidate to edit existing files was the one that assigned the transformation to each shape.
en123 | NEW | en135 | 0.39 | It edited the circle and square files.
en124 | EDIT | en143 | 0.79 | All four added one file, preserved input order and duplicates, handled empty lists and unsupported shapes as specified, and kept the original circle and square renderings (Figure 1B).
en125 | EDIT | en144 | 0.74 | Number of existing source files edited.
en126 | SAME | en145 | 1.00 | Panel A compares adding a triangle with adding a labeling operation.
en127 | EDIT | en146 | 0.51 | Panel B changes the placement rule for the same batch-rendering request.
en128 | EDIT | en147 | 0.73 | All four candidates in B passed the new and legacy checks and added one file each.
en129 | NEW | en149 | 0.29 | · · · · Next we added an option to bracket a single rendered result.
en130 | EDIT | en150 | 0.55 | Both layouts could offer it through a new function.
en131 | NEW | en151 | 0.32 | With that same adapter installed, the original function still rejected bracketed=True .
en132 | EDIT | en152 | 0.70 | Of the candidates offering the option through the original function, the operation layout edited one existing file and the shape layout edited two.
en133 | EDIT | en153 | 0.50 | In a separate baseline the original function could already load an external decorator.
en134 | NEW | en153 | 0.33 | There, each layout connected the option to the original function by adding one file (Table 3).
en135 | SAME | en154 | 1.00 | Call paths for the new rendering option.
en136 | EDIT | en155 | 0.58 | The final row of Table 3 starts after the hook is in place.
en137 | NEW | en144 | 0.32 | The numbers count edited existing files.
en138 | EDIT | en157 | 0.57 | Introducing the hook and measuring actual maintenance effort would require separate measurements.
en139 | EDIT | en158 | 0.56 | · A square drawn first gives the reviewer grounds for an edit when putting circles first is the drawing function’s job.
en140 | NEW | en159 | 0.18 | In the catalog, we could change what the patch was required to do and preserve while keeping its behavior fixed.
en141 | NEW | en160 | 0.29 | A requirement to handle errata settled the verdict.
en142 | NEW | en124 | 0.22 | With technical reports as the only new requirement, the verdict depended on the promise about book output.
en143 | NEW | en126 | 0.17 | When the known facts leave more than one verdict open, they can retain the specifications consistent with the known facts and identify which difference changes the verdict.
en144 | NEW | en166 | 0.23 | We demonstrate this method with records from one benchmark and examples written for the study.
en145 | NEW | en163 | 0.23 | In a repository, the evidence that establishes a promise and the call path on which to test it must be found case by case.
en146 | EDIT | en167 | 0.54 | The audit in Sections 3–4 reads JSON and JSONL from the archived ZIP.
en147 | NEW | en168 | 0.36 | Sections 5–6 run examples written for this study.
en148 | EDIT | en169 | 0.57 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en149 | NEW | en167 | 0.15 | The table below gives the nine verdicts for Section 5.
en150 | NEW | en170 | 0.41 | Both values of a withheld field remain possible.
en151 | NEW | en171 | 0.39 | Defer means that the compatible rows include both acceptance and rejection.
Summary en: SAME 6, EDIT 47, NEW 98

## v13 · [Source](https://app.notion.com/p/41fef561cf9281aaa8cfdf0ca6f9b56f)
### ko (118 segmented sentences)
ko001 | SAME | ko001 | 1.00 | 로버트 마틴이 1996년에 예로 든 함수는 목록에 들어온 순서대로 도형을 그린다.
ko002 | SAME | ko002 | 1.00 | 삼각형이 자신을 그리는 메서드를 갖고 있으면 이 함수에 손대지 않고 삼각형을 추가할 수 있다.
ko003 | SAME | ko003 | 1.00 | 기존 함수에 사각형으로 시작하는 목록을 넘기면 여전히 사각형부터 그린다.
ko004 | SAME | ko004 | 1.00 | 호출자가 원을 앞에 모아 넘기기로 했다면 함수는 제 일을 한다.
ko005 | SAME | ko005 | 1.00 | 함수가 어떤 목록을 받아도 그 순서를 보장하기로 했다면 고쳐야 한다.
ko006 | SAME | ko006 | 1.00 | 소스에서 그리는 순서를 읽을 수는 있지만, 그 순서가 잘못됐는지는 누가 정렬을 맡았는지에 달려 있다.
ko007 | SAME | ko007 | 1.00 | 마틴의 그리기 함수는 도형을 하나 더 추가할 때는 그대로 둘 수 있었다.
ko008 | NEW | ko010 | 0.11 | 우리는 변경 요구와 기존 호출자에 대한 약속을 확인하지 않은 채 OCP 위반이라는 평가만으로 수정안 거절을 확정하는 위험을 과도한 공리화 라고 부른다.
ko009 | NEW | ko021 | 0.04 | 이 이름은 원칙 자체가 무조건적인 공리였다는 역사적 주장이 아니라, 원칙을 적용하는 판정 방식에 관한 것이다.
ko010 | SAME | ko009 | 1.00 | 분류 벤치마크의 저장 자료에서 모델에 어떤 지시가 주어졌는지 확인했다.
ko011 | SAME | ko010 | 1.00 | 이어 도서관 예제에서 코드와 수정안을 고정한 채 새 요구와 기존 호출자에게 한 약속을 바꿨다.
ko012 | SAME | ko011 | 1.00 | 도형 예제로 돌아가서는 별도 파일에 넣은 기능을 기존 함수로도 쓸 수 있는지 확인했다.
ko013 | SAME | ko012 | 1.00 | · · 마틴은 1996년 글에서 베르트랑 마이어의 1988년 초판 23쪽을 인용했다.
ko014 | SAME | ko013 | 1.00 | 마이어에게 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 쓸 수 있는 모듈이다.
ko015 | SAME | ko014 | 1.00 | 그의 도서관 예제에서 자료 유형을 하나씩 구별해 처리하는 프로그램에 기술보고서를 추가하면, 기존 모듈까지 고치거나 다시 컴파일해야 할 수 있다.
ko016 | SAME | ko015 | 1.00 | 새 자료를 처리하는 코드의 위치에 따라 기존 모듈에 손이 가는 범위가 달라진다.
ko017 | SAME | ko016 | 1.00 | 1995년 6월 공개 토론에서 카일 브라운은 잘못 설계된 클래스라면 소스를 고칠 수 있어야 한다고 했다.
ko018 | SAME | ko017 | 1.00 | 마틴은 예상한 확장을 위해 기존 소스를 반드시 고쳐야 하는지를 물었다.
ko019 | SAME | ko018 | 1.00 | 그러려면 어떤 변경이 생길지 미리 짚어야 한다.
ko020 | SAME | ko019 | 1.00 | 2007년 공개 기록에는 다섯 원칙을 묶은 SOLID라는 이름이 나온다.
ko021 | SAME | ko020 | 1.00 | 2009년 인터페이스 논쟁에서는 내부 클래스와 공개 플러그인 API에 서로 다른 조언이 제시됐다.
ko022 | NEW | ko021 | 0.16 | 이 기록은 당시 원칙을 적용하거나 반대할 때 어떤 이유를 제시했는지 보여 준다.
ko023 | NEW | ko019 | 0.12 | SOLID라는 이름이 널리 퍼지면서 적용 조건에 대한 판단이 실제로 변했는지는 별도의 역사적 증거가 필요하다.
ko024 | SAME | ko022 | 1.00 | · · 마틴은 목록 정렬을 DrawAllShapes 가 맡게 했다.
ko025 | SAME | ko023 | 1.00 | 한 구현에서 Circle::Precedes 는 상대 도형이 사각형이면 원을 먼저 놓는다.
ko026 | SAME | ko024 | 1.00 | 원과 세 번째 도형의 순서를 정하려면 Circle 도 고쳐야 할 수 있다.
ko027 | SAME | ko025 | 1.00 | 반면 도형 종류별 순서를 표에 두면 사각형을 먼저 놓기 위해 표의 두 항목만 바꾸면 된다.
ko028 | SAME | ko026 | 1.00 | 개별 도형을 넓이순으로 그리려면 그 표에 없는 정보가 필요하다.
ko029 | SAME | ko027 | 1.00 | 마틴이 글 후반에 비교한 두 함수는 dynamic_cast 를 쓴다.
ko030 | SAME | ko028 | 1.00 | DrawAllShapes 의 한 구현은 원과 사각형을 골라 그리고, DrawSquaresOnly 는 사각형만 그린다.
ko031 | SAME | ko029 | 1.00 | 모든 도형을 그려야 할 때는 출력이 하나 빠진 셈이다.
ko032 | SAME | ko030 | 1.00 | 코드와 프롬프트만 주어진 검토자는 각 함수에 어느 책임이 있는지 어디까지 알 수 있을까?
ko033 | NEW | ko056 | 0.04 | · · 분류 결과에 필요한 정보와 수정안의 수용 여부를 정하는 정보는 구별해 조사했다.
ko034 | NEW | ko039 | 0.04 | 첫 번째 작업은 보존된 벤치마크를 읽는 감사이고, 두 번째는 우리가 작성한 패치에 서로 다른 요구와 계약을 대입하는 구성 사례다.
ko035 | NEW | ko088 | 0.02 | 두 자료의 개별 코드나 실제 개발자 판정을 서로 대응시키지는 않았다.
ko036 | NEW | ko033 | 0.10 | OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다.
ko037 | EDIT | ko034 | 0.67 | 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다.
ko038 | NEW | ko035 | 0.04 | 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다.
ko039 | NEW | ko037 | 0.17 | 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다.
ko040 | NEW | ko042 | 0.04 | 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다.
ko041 | NEW | ko034 | 0.05 | 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.
ko042 | NEW | ko059 | 0.11 | 지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다.
ko043 | NEW | ko060 | 0.14 | 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다.
ko044 | NEW | ko057 | 0.07 | 이 판독은 제출 코드를 가린 지시문에 관한 것이며, 코드의 이름과 구조에서 가능한 요구를 유추할 수 있다는 사실까지 부정하지 않는다.
ko045 | NEW | ko065 | 0.11 | 저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다.
ko046 | NEW | ko046 | 0.18 | Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다.
ko047 | NEW | ko120 | 0.05 | 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다.
ko048 | NEW | — | 0.00 | 압축 파일 안의 코드 자체는 실행하지 않았다.
ko049 | EDIT | ko048 | 0.54 | 도서관 예제에서는 원래 소스와 수정안, 호출 입력, 새 모듈 추가를 허용한 편집 범위를 고정했다.
ko050 | NEW | ko049 | 0.04 | 실제 호출에서 얻은 출력·예외는 실행 관찰로 기록했다.
ko051 | NEW | ko050 | 0.17 | 새 요구를 충족하고 적용되는 기존 계약을 보존할 때 승인한다 는 기준은 연구자가 정했다.
ko052 | NEW | ko066 | 0.02 | 따라서 §5의 승인·거절은 이 기준과 실행 결과에서 도출한 값이지 외부 심사위원이 내린 판단이 아니다.
ko053 | NEW | ko051 | 0.08 | 일부 정보만 공개된 경우에는 공개된 사실과 양립하는 완전 명세를 남겨 판정이 일치하는지 확인했다.
ko054 | NEW | ko054 | 0.46 | · · Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21) Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko055 | SAME | ko055 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko056 | SAME | ko056 | 1.00 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko057 | SAME | ko057 | 1.00 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko058 | SAME | ko058 | 1.00 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko059 | SAME | ko059 | 1.00 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko060 | NEW | ko058 | 0.09 | 추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. gpt-4o-mini 와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다.
ko061 | NEW | ko046 | 0.06 | 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다.
ko062 | NEW | ko056 | 0.02 | 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.
ko063 | SAME | ko060 | 1.00 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko064 | SAME | ko061 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko065 | SAME | ko062 | 1.00 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko066 | SAME | ko063 | 1.00 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko067 | SAME | ko064 | 1.00 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko068 | SAME | ko065 | 1.00 | 저장된 제출 코드 가운데 어느 참조 쌍의 수정 전후 소스와도 일치한 것은 없었다.
ko069 | SAME | ko066 | 1.00 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko070 | SAME | ko067 | 1.00 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko071 | SAME | ko068 | 1.00 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko072 | SAME | ko069 | 1.00 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko073 | SAME | ko070 | 1.00 | · · · Bräuer 등(2018)은 측정 가능한 실천 규칙으로 설계 원칙의 어떤 부분을 포착할 수 있는지 전문가에게 물었다.
ko074 | SAME | ko071 | 1.00 | Cabral 등(2024)은 기계학습 기능을 확장하는 상황에서 SOLID를 적용한 코드에 대해 참가자가 느낀 이해도와 확장 용이성을 조사했다.
ko075 | SAME | ko072 | 1.00 | Zhu 등(2026)은 저장소에 구체적인 변경을 요구하고 기능 테스트와 구조 판정 기준을 적용했다.
ko076 | SAME | ko073 | 1.00 | 다음 절에서는 수정안을 고정하고, 검토자가 알고 있는 요구와 계약에 따라 승인 결론이 달라지는지 살핀다.
ko077 | SAME | ko074 | 1.00 | · · 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko078 | SAME | ko075 | 1.00 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko079 | SAME | ko076 | 1.00 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko080 | SAME | ko077 | 1.00 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko081 | SAME | ko078 | 1.00 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko082 | SAME | ko079 | 1.00 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko083 | SAME | ko080 | 1.00 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko084 | SAME | ko081 | 1.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko085 | SAME | ko082 | 1.00 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko086 | SAME | ko083 | 1.00 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko087 | SAME | ko084 | 1.00 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko088 | SAME | ko085 | 1.00 | 실제 명세가 검토하는 경우들 가운데 하나라는 전제에서 이 절차가 성립한다.
ko089 | SAME | ko086 | 1.00 | 공개된 사실과 맞는 행이 없다면 명세 후보와 공개된 사실부터 다시 대조해야 한다.
ko090 | SAME | ko087 | 1.00 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko091 | SAME | ko088 | 1.00 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko092 | SAME | ko089 | 1.00 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko093 | SAME | ko090 | 1.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko094 | SAME | ko091 | 1.00 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko095 | SAME | ko092 | 1.00 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko096 | SAME | ko093 | 1.00 | 다른 사례에서도 가능한 명세와 각각의 근거를 명시하면, 보류된 판정을 확정하기 위해 다음에 무엇을 확인할지 알 수 있다.
ko097 | NEW | ko079 | 0.09 | · 완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다.
ko098 | NEW | — | 0.00 | 여기서는 앞의 질문에 해당하는 관찰만 남긴다.
ko099 | NEW | ko111 | 0.27 | 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 bracketed=True 를 넘기면 인자를 거절했다.
ko100 | NEW | ko112 | 0.05 | 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다.
ko101 | NEW | ko050 | 0.09 | 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.
ko102 | NEW | ko123 | 0.06 | 새 기능이 있다는 사실과 요구된 호출 경로에서 쓸 수 있다는 사실 은 다르다.
ko103 | NEW | ko115 | 0.07 | 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 Paper B 통합 원고 12 · 한·영 문장 교정 및 에 원형 그대로 보존했다.
ko104 | NEW | ko003 | 0.11 | 마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다.
ko105 | NEW | ko005 | 0.15 | 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다.
ko106 | NEW | ko010 | 0.09 | 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다.
ko107 | NEW | ko067 | 0.04 | 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다.
ko108 | NEW | ko008 | 0.03 | 원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가 가 이 논문에서 다룬 질문이다.
ko109 | NEW | ko121 | 0.08 | 공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다.
ko110 | NEW | ko123 | 0.09 | 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다.
ko111 | NEW | ko122 | 0.14 | 이 연구는 한 벤치마크의 저장 입력과 연구자가 구성한 실행 예제만을 다뤘다.
ko112 | NEW | ko123 | 0.04 | 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.
ko113 | SAME | ko124 | 1.00 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko114 | SAME | ko125 | 1.00 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko115 | SAME | ko126 | 1.00 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko116 | SAME | ko127 | 1.00 | 그림 1의 소스와 출력은 캡션 아래에 연결했다.
ko117 | SAME | ko128 | 1.00 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko118 | SAME | ko129 | 1.00 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
Summary ko: SAME 73, EDIT 2, NEW 43

### en (133 segmented sentences)
en001 | SAME | en001 | 1.00 | In 1996 Robert Martin described a function that draws shapes in the order it receives them.
en002 | SAME | en002 | 1.00 | A triangle can be added without touching the function if the triangle supplies its own drawing method.
en003 | SAME | en003 | 1.00 | Then Martin changes the task.
en004 | SAME | en004 | 1.00 | Every circle must be drawn before any square.
en005 | SAME | en005 | 1.00 | Give the function a list that begins with a square and it still draws the square first.
en006 | SAME | en006 | 1.00 | Who was supposed to put the circles first?
en007 | SAME | en007 | 1.00 | If the caller agreed to sort the list, the routine does its job.
en008 | SAME | en008 | 1.00 | If the routine must guarantee that order for any list, it needs an edit.
en009 | SAME | en009 | 1.00 | The source tells us what gets drawn first.
en010 | SAME | en010 | 1.00 | The agreement tells us whether that is a problem.
en011 | SAME | en011 | 1.00 | Martin’s drawing routine could stay as it was when the task was to add a shape.
en012 | SAME | en012 | 1.00 | Making it responsible for sorting changes that judgment.
en013 | NEW | en077 | 0.14 | We use over-axiomatization for the risk of treating an OCP violation label as sufficient grounds to reject a patch without establishing the governing change and caller obligations.
en014 | NEW | en026 | 0.07 | This is a claim about the use of advice, not a historical claim that OCP became a formal axiom.
en015 | SAME | en014 | 1.00 | We inspect a classification benchmark’s archive to see what instructions its models received.
en016 | SAME | en015 | 1.00 | In a separate catalog example we keep the code and patch fixed while varying the request and the promises to existing callers.
en017 | SAME | en016 | 1.00 | We then return to drawing to test whether a feature added in a separate file can be reached through the original function.
en018 | SAME | en017 | 1.00 | · · Martin attributed the principle to Bertrand Meyer, citing page 23 of the 1988 first edition.
en019 | SAME | en018 | 1.00 | For Meyer, a closed module has a stable specification that other modules can rely on.
en020 | SAME | en019 | 1.00 | His library example gives this a practical meaning.
en021 | SAME | en020 | 1.00 | If a catalog handles publication types one by one, adding technical reports can require editing or recompiling existing modules.
en022 | SAME | en021 | 1.00 | Where the new code goes affects how much of the existing system must change.
en023 | SAME | en022 | 1.00 | In a June 1995 public exchange, Kyle Brown argued that developers had to be able to fix a badly designed class.
en024 | SAME | en023 | 1.00 | Martin asked whether an anticipated extension had to require an edit to existing source.
en025 | SAME | en024 | 1.00 | That answer still depends on which changes can be anticipated.
en026 | SAME | en025 | 1.00 | The public record uses SOLID for the five principles by 2007.
en027 | SAME | en026 | 1.00 | A 2009 discussion gave different advice for internal classes and public plugin APIs.
en028 | NEW | en027 | 0.28 | These records show particular uses and objections.
en029 | NEW | en076 | 0.14 | They do not establish that circulation of the SOLID label caused the governing conditions to change.
en030 | SAME | en028 | 1.00 | · · Martin made DrawAllShapes responsible for sorting.
en031 | SAME | en029 | 1.00 | In one implementation Circle::Precedes checks the other shape and puts a circle before a square.
en032 | SAME | en030 | 1.00 | Deciding where a third shape belongs relative to a circle can require an edit to Circle .
en033 | SAME | en031 | 1.00 | Placing the order of types in a table lets squares go first with a swap of two entries.
en034 | SAME | en032 | 1.00 | Sorting individual shapes by area would require information that the table does not hold.
en035 | SAME | en033 | 1.00 | Later in the article Martin compares two uses of dynamic_cast .
en036 | SAME | en034 | 1.00 | One version of DrawAllShapes draws circles and squares, and DrawSquaresOnly draws squares alone.
en037 | SAME | en035 | 1.00 | A triangle left undrawn is a missed output when the task is to draw all shapes.
en038 | SAME | en036 | 1.00 | When the task is to draw squares, skipping it is correct.
en039 | SAME | en037 | 1.00 | How much of that responsibility can a reviewer determine from code and a prompt?
en040 | NEW | en078 | 0.16 | · · We separated the information used to classify code from the information needed to accept a patch.
en041 | NEW | en058 | 0.18 | The first part audits saved benchmark inputs; the second applies requirements and caller contracts that we specified to a patch we built.
en042 | NEW | en074 | 0.12 | We did not match the archive submissions to the catalog patch or to actual reviewers' decisions.
en043 | NEW | en040 | 0.25 | The OCP reference material contains 48 before-and-after code pairs.
en044 | NEW | en041 | 0.19 | Sixteen saved JSONL files each contain 48 records, yielding 768 rows.
en045 | NEW | en066 | 0.12 | Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times.
en046 | NEW | en044 | 0.30 | We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality.
en047 | NEW | en075 | 0.11 | The result was 24 scaffolds.
en048 | NEW | en065 | 0.09 | Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs.
en049 | NEW | en064 | 0.13 | The 768 records are repeated submissions, not independent maintenance cases.
en050 | NEW | en068 | 0.27 | We separately read the masked instructions for case-specific change requests and protected caller commitments.
en051 | NEW | en049 | 0.41 | An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape.
en052 | NEW | en051 | 0.18 | We inspected only the text outside the submitted code; names, comments and code structure may still give other clues.
en053 | NEW | en052 | 0.30 | We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace.
en054 | NEW | en073 | 0.17 | For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions.
en055 | NEW | en055 | 0.18 | These tests do not establish whether inherited methods remain available or whether callers were promised a behavior.
en056 | NEW | en060 | 0.14 | We read code as archive data and did not execute it.
en057 | NEW | en056 | 0.30 | For the catalog, we fixed the baseline, patch, input calls and permissible edit boundary, ran the calls, and recorded output or exceptions.
en058 | NEW | en058 | 0.34 | We defined acceptance as meeting the new demand and preserving the applicable contract.
en059 | NEW | en064 | 0.13 | The Section 5 verdicts follow from these authored criteria and the observed behavior; they are not independent human review decisions.
en060 | NEW | en059 | 0.44 | With partial disclosure, we retained the complete specifications compatible with known facts and checked whether the verdicts agreed.
en061 | SAME | en063 | 1.00 | · Pehlivan et al. chose violation scenarios and refined the generated examples.
en062 | SAME | en064 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en063 | SAME | en065 | 1.00 | The benchmark compares model classifications with the resulting labels.
en064 | SAME | en066 | 1.00 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en065 | SAME | en067 | 1.00 | No two strategies shared a template string.
en066 | SAME | en068 | 1.00 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en067 | NEW | en144 | 0.12 | An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: gpt-4o-mini differed from the other three models.
en068 | NEW | en067 | 0.12 | Holding model, strategy and language fixed left one scaffold shared across twelve programs.
en069 | NEW | en052 | 0.21 | No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST.
en070 | NEW | en088 | 0.13 | These checks do not establish semantic independence or source lineage.
en071 | SAME | en069 | 1.00 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en072 | SAME | en070 | 1.00 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en073 | SAME | en071 | 1.00 | If a new shape is needed, that branch is a place to look.
en074 | SAME | en072 | 1.00 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en075 | SAME | en073 | 1.00 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en076 | SAME | en074 | 1.00 | None of the code saved as model submissions matched either side of any reference pair.
en077 | SAME | en075 | 1.00 | Trimming outer whitespace yielded the same result.
en078 | SAME | en076 | 1.00 | Pair 37 establishes that a declaration was removed.
en079 | SAME | en077 | 1.00 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en080 | SAME | en078 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en081 | SAME | en079 | 1.00 | The prompt example is in JSONL line 13 (record ID 12).
en082 | SAME | en080 | 1.00 | Pair 37 is in a separate reference JSON file.
en083 | SAME | en081 | 1.00 | · · · Bräuer et al. (2018) asked experts which parts of a design principle were captured by measurable practices.
en084 | SAME | en082 | 1.00 | Cabral et al. (2024) asked participants how easy they found it to understand and extend code under a bundled SOLID treatment in a machine-learning scenario.
en085 | SAME | en083 | 1.00 | Zhu et al. (2026) set repository change tasks and used functional and structural checks.
en086 | SAME | en084 | 1.00 | In the next section we fix the patch and ask whether knowing a different requirement or caller contract changes the verdict.
en087 | SAME | en085 | 1.00 | · · We built a small catalog based on Meyer’s example.
en088 | SAME | en086 | 1.00 | The client in client.py displays each publication through the catalog function passed to it.
en089 | SAME | en087 | 1.00 | The patch adds reports.py to wrap that function.
en090 | SAME | en088 | 1.00 | The source of catalog.py and client.py stays identical.
en091 | SAME | en089 | 1.00 | The resulting catalog displays technical reports and still rejects errata.
en092 | SAME | en090 | 1.00 | For books it now prints BOOK where it used to print book .
en093 | SAME | en091 | 1.00 | Suppose the only new requirement is to handle technical reports.
en094 | SAME | en092 | 1.00 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en095 | SAME | en093 | 1.00 | If the book output is outside the contract, the same patch can be accepted.
en096 | SAME | en094 | 1.00 | Table 2 applies both contracts again when errata are also required.
en097 | SAME | en095 | 1.00 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en098 | SAME | en096 | 1.00 | Two requirements for accepting a fixed patch.
en099 | SAME | en097 | 1.00 | Learning that errata are required leaves the last two rows of Table 2.
en100 | SAME | en098 | 1.00 | Both reject the patch, so the book contract need not be settled first.
en101 | SAME | en099 | 1.00 | Learning that technical reports are the whole request leaves the first two rows.
en102 | SAME | en100 | 1.00 | One accepts and one rejects.
en103 | SAME | en101 | 1.00 | The next question is whether the original book output is protected.
en104 | SAME | en102 | 1.00 | This procedure assumes that the actual specification is among the cases under consideration.
en105 | SAME | en103 | 1.00 | If no row fits what was disclosed, the reviewer needs to recheck the candidate specifications against the facts.
en106 | SAME | en104 | 1.00 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en107 | SAME | en105 | 1.00 | The reviewer can give a conditional answer or defer judgment.
en108 | SAME | en106 | 1.00 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en109 | SAME | en107 | 1.00 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en110 | SAME | en108 | 1.00 | It adds one module, handles technical reports and errata, and keeps the original book output.
en111 | SAME | en109 | 1.00 | A rejection in Table 2 need not end the search for a patch within that boundary.
en112 | SAME | en110 | 1.00 | In another case, recording the possible specifications and the evidence for each can tell a reviewer what to check next.
en113 | NEW | en096 | 0.12 | · Deciding whether to accept a completed patch differs from choosing an architecture for future edits.
en114 | NEW | en151 | 0.12 | We retain one observation relevant to acceptance.
en115 | NEW | en131 | 0.36 | In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected bracketed=True .
en116 | NEW | en057 | 0.19 | A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.
en117 | NEW | en084 | 0.10 | The presence of a feature is different from its availability along a required route .
en118 | NEW | en132 | 0.16 | The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in Paper B 통합 원고 12 · 한·영 문장 교정 and its .
en119 | NEW | en139 | 0.18 | Drawing a square first establishes what a routine does, not whether it must be edited.
en120 | NEW | en024 | 0.13 | That depends on whether sorting belongs to the routine's obligations.
en121 | NEW | en142 | 0.30 | In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required.
en122 | NEW | en013 | 0.12 | We did not observe a real OCP label being misused to reject a patch.
en123 | NEW | en081 | 0.11 | We asked what additional grounds a design-principle assessment needs before it can justify an engineering decision .
en124 | NEW | en143 | 0.23 | Keeping the specifications compatible with known facts and checking their verdicts is elementary logic.
en125 | NEW | en091 | 0.15 | The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository.
en126 | NEW | en144 | 0.17 | Our evidence is confined to one benchmark archive and authored executable examples.
en127 | NEW | en110 | 0.09 | We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.
en128 | SAME | en146 | 1.00 | The audit in Sections 3–4 reads JSON and JSONL from the archived ZIP.
en129 | SAME | en147 | 1.00 | Sections 5–6 run examples written for this study.
en130 | SAME | en148 | 1.00 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en131 | SAME | en149 | 1.00 | The table below gives the nine verdicts for Section 5.
en132 | SAME | en150 | 1.00 | Both values of a withheld field remain possible.
en133 | SAME | en151 | 1.00 | Defer means that the compatible rows include both acceptance and rejection.
Summary en: SAME 89, EDIT 0, NEW 44

## v14 · [Source](https://app.notion.com/p/41fef561cf928121af24cb634cdad9e3)
### ko (122 segmented sentences)
ko001 | SAME | ko001 | 1.00 | 로버트 마틴이 1996년에 예로 든 함수는 목록에 들어온 순서대로 도형을 그린다.
ko002 | SAME | ko002 | 1.00 | 삼각형이 자신을 그리는 메서드를 갖고 있으면 이 함수에 손대지 않고 삼각형을 추가할 수 있다.
ko003 | SAME | ko003 | 1.00 | 기존 함수에 사각형으로 시작하는 목록을 넘기면 여전히 사각형부터 그린다.
ko004 | SAME | ko004 | 1.00 | 호출자가 원을 앞에 모아 넘기기로 했다면 함수는 제 일을 한다.
ko005 | SAME | ko005 | 1.00 | 함수가 어떤 목록을 받아도 그 순서를 보장하기로 했다면 고쳐야 한다.
ko006 | SAME | ko006 | 1.00 | 소스에서 그리는 순서를 읽을 수는 있지만, 그 순서가 잘못됐는지는 누가 정렬을 맡았는지에 달려 있다.
ko007 | SAME | ko007 | 1.00 | 마틴의 그리기 함수는 도형을 하나 더 추가할 때는 그대로 둘 수 있었다.
ko008 | SAME | ko008 | 1.00 | 우리는 변경 요구와 기존 호출자에 대한 약속을 확인하지 않은 채 OCP 위반이라는 평가만으로 수정안 거절을 확정하는 위험을 과도한 공리화 라고 부른다.
ko009 | SAME | ko009 | 1.00 | 이 이름은 원칙 자체가 무조건적인 공리였다는 역사적 주장이 아니라, 원칙을 적용하는 판정 방식에 관한 것이다.
ko010 | SAME | ko010 | 1.00 | 분류 벤치마크의 저장 자료에서 모델에 어떤 지시가 주어졌는지 확인했다.
ko011 | SAME | ko011 | 1.00 | 이어 도서관 예제에서 코드와 수정안을 고정한 채 새 요구와 기존 호출자에게 한 약속을 바꿨다.
ko012 | SAME | ko012 | 1.00 | 도형 예제로 돌아가서는 별도 파일에 넣은 기능을 기존 함수로도 쓸 수 있는지 확인했다.
ko013 | SAME | ko013 | 1.00 | · · 마틴은 1996년 글에서 베르트랑 마이어의 1988년 초판 23쪽을 인용했다.
ko014 | SAME | ko014 | 1.00 | 마이어에게 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 쓸 수 있는 모듈이다.
ko015 | SAME | ko015 | 1.00 | 그의 도서관 예제에서 자료 유형을 하나씩 구별해 처리하는 프로그램에 기술보고서를 추가하면, 기존 모듈까지 고치거나 다시 컴파일해야 할 수 있다.
ko016 | SAME | ko016 | 1.00 | 새 자료를 처리하는 코드의 위치에 따라 기존 모듈에 손이 가는 범위가 달라진다.
ko017 | SAME | ko017 | 1.00 | 1995년 6월 공개 토론에서 카일 브라운은 잘못 설계된 클래스라면 소스를 고칠 수 있어야 한다고 했다.
ko018 | SAME | ko018 | 1.00 | 마틴은 예상한 확장을 위해 기존 소스를 반드시 고쳐야 하는지를 물었다.
ko019 | SAME | ko019 | 1.00 | 그러려면 어떤 변경이 생길지 미리 짚어야 한다.
ko020 | SAME | ko020 | 1.00 | 2007년 공개 기록에는 다섯 원칙을 묶은 SOLID라는 이름이 나온다.
ko021 | SAME | ko021 | 1.00 | 2009년 인터페이스 논쟁에서는 내부 클래스와 공개 플러그인 API에 서로 다른 조언이 제시됐다.
ko022 | SAME | ko022 | 1.00 | 이 기록은 당시 원칙을 적용하거나 반대할 때 어떤 이유를 제시했는지 보여 준다.
ko023 | SAME | ko023 | 1.00 | SOLID라는 이름이 널리 퍼지면서 적용 조건에 대한 판단이 실제로 변했는지는 별도의 역사적 증거가 필요하다.
ko024 | SAME | ko024 | 1.00 | · · 마틴은 목록 정렬을 DrawAllShapes 가 맡게 했다.
ko025 | SAME | ko025 | 1.00 | 한 구현에서 Circle::Precedes 는 상대 도형이 사각형이면 원을 먼저 놓는다.
ko026 | SAME | ko026 | 1.00 | 원과 세 번째 도형의 순서를 정하려면 Circle 도 고쳐야 할 수 있다.
ko027 | SAME | ko027 | 1.00 | 반면 도형 종류별 순서를 표에 두면 사각형을 먼저 놓기 위해 표의 두 항목만 바꾸면 된다.
ko028 | SAME | ko028 | 1.00 | 개별 도형을 넓이순으로 그리려면 그 표에 없는 정보가 필요하다.
ko029 | SAME | ko029 | 1.00 | 마틴이 글 후반에 비교한 두 함수는 dynamic_cast 를 쓴다.
ko030 | SAME | ko030 | 1.00 | DrawAllShapes 의 한 구현은 원과 사각형을 골라 그리고, DrawSquaresOnly 는 사각형만 그린다.
ko031 | SAME | ko031 | 1.00 | 모든 도형을 그려야 할 때는 출력이 하나 빠진 셈이다.
ko032 | SAME | ko032 | 1.00 | 코드와 프롬프트만 주어진 검토자는 각 함수에 어느 책임이 있는지 어디까지 알 수 있을까?
ko033 | SAME | ko033 | 1.00 | · · 분류 결과에 필요한 정보와 수정안의 수용 여부를 정하는 정보는 구별해 조사했다.
ko034 | SAME | ko034 | 1.00 | 첫 번째 작업은 보존된 벤치마크를 읽는 감사이고, 두 번째는 우리가 작성한 패치에 서로 다른 요구와 계약을 대입하는 구성 사례다.
ko035 | SAME | ko035 | 1.00 | 두 자료의 개별 코드나 실제 개발자 판정을 서로 대응시키지는 않았다.
ko036 | SAME | ko036 | 1.00 | OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다.
ko037 | SAME | ko037 | 1.00 | 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다.
ko038 | SAME | ko038 | 1.00 | 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다.
ko039 | SAME | ko039 | 1.00 | 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다.
ko040 | SAME | ko040 | 1.00 | 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다.
ko041 | SAME | ko041 | 1.00 | 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.
ko042 | SAME | ko042 | 1.00 | 지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다.
ko043 | SAME | ko043 | 1.00 | 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다.
ko044 | SAME | ko044 | 1.00 | 이 판독은 제출 코드를 가린 지시문에 관한 것이며, 코드의 이름과 구조에서 가능한 요구를 유추할 수 있다는 사실까지 부정하지 않는다.
ko045 | SAME | ko045 | 1.00 | 저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다.
ko046 | SAME | ko046 | 1.00 | Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다.
ko047 | SAME | ko047 | 1.00 | 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다.
ko048 | SAME | ko048 | 1.00 | 압축 파일 안의 코드 자체는 실행하지 않았다.
ko049 | SAME | ko049 | 1.00 | 도서관 예제에서는 원래 소스와 수정안, 호출 입력, 새 모듈 추가를 허용한 편집 범위를 고정했다.
ko050 | SAME | ko050 | 1.00 | 실제 호출에서 얻은 출력·예외는 실행 관찰로 기록했다.
ko051 | SAME | ko051 | 1.00 | 새 요구를 충족하고 적용되는 기존 계약을 보존할 때 승인한다 는 기준은 연구자가 정했다.
ko052 | SAME | ko052 | 1.00 | 따라서 §5의 승인·거절은 이 기준과 실행 결과에서 도출한 값이지 외부 심사위원이 내린 판단이 아니다.
ko053 | SAME | ko053 | 1.00 | 일부 정보만 공개된 경우에는 공개된 사실과 양립하는 완전 명세를 남겨 판정이 일치하는지 확인했다.
ko054 | SAME | ko054 | 1.00 | · · Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21) Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko055 | SAME | ko055 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko056 | SAME | ko056 | 1.00 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko057 | SAME | ko057 | 1.00 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko058 | SAME | ko058 | 1.00 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko059 | SAME | ko059 | 1.00 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko060 | SAME | ko060 | 1.00 | 추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. gpt-4o-mini 와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다.
ko061 | SAME | ko061 | 1.00 | 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다.
ko062 | SAME | ko062 | 1.00 | 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.
ko063 | SAME | ko063 | 1.00 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko064 | SAME | ko064 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko065 | SAME | ko065 | 1.00 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko066 | SAME | ko066 | 1.00 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko067 | SAME | ko067 | 1.00 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko068 | NEW | ko068 | 0.22 | 저장된 제출 코드와 참조 쌍의 수정 전후 소스는 앞에서 명시한 문자열·구문 트리 비교에서 일치하지 않았다.
ko069 | SAME | ko069 | 1.00 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko070 | SAME | ko070 | 1.00 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko071 | SAME | ko071 | 1.00 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko072 | SAME | ko072 | 1.00 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko073 | SAME | ko073 | 1.00 | · · · Bräuer 등(2018)은 측정 가능한 실천 규칙으로 설계 원칙의 어떤 부분을 포착할 수 있는지 전문가에게 물었다.
ko074 | SAME | ko074 | 1.00 | Cabral 등(2024)은 기계학습 기능을 확장하는 상황에서 SOLID를 적용한 코드에 대해 참가자가 느낀 이해도와 확장 용이성을 조사했다.
ko075 | SAME | ko075 | 1.00 | Zhu 등(2026)은 저장소에 구체적인 변경을 요구하고 기능 테스트와 구조 판정 기준을 적용했다.
ko076 | NEW | ko105 | 0.04 | 프로그램이 무엇을 가정하고 무엇을 보장하는지를 구별하는 생각 자체는 새롭지 않다.
ko077 | NEW | ko085 | 0.03 | 존스(1981)는 병렬 프로그램의 명세에 환경에 대한 의존 조건과 프로그램의 보장 조건을 넣었고, 구성 요소 사이에서 두 조건이 양립해야 한다는 증명 규칙을 제시했다.
ko078 | NEW | ko077 | 0.03 | 물론 존스가 연구한 것은 OCP 리뷰가 아니라 병렬 프로그램의 올바른 구현이다.
ko079 | NEW | ko108 | 0.11 | 여기서는 그 형식 이론을 다시 만드는 대신, 원칙 위반이라는 의견을 특정 수정안의 거절 근거로 사용하려면 어떤 약속을 확인해야 하는지 묻는다.
ko080 | SAME | ko076 | 1.00 | 다음 절에서는 수정안을 고정하고, 검토자가 알고 있는 요구와 계약에 따라 승인 결론이 달라지는지 살핀다.
ko081 | SAME | ko077 | 1.00 | · · 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko082 | SAME | ko078 | 1.00 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko083 | SAME | ko079 | 1.00 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko084 | SAME | ko080 | 1.00 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko085 | SAME | ko081 | 1.00 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko086 | SAME | ko082 | 1.00 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko087 | SAME | ko083 | 1.00 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko088 | SAME | ko084 | 1.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko089 | SAME | ko085 | 1.00 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko090 | SAME | ko086 | 1.00 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko091 | SAME | ko087 | 1.00 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko092 | SAME | ko088 | 1.00 | 실제 명세가 검토하는 경우들 가운데 하나라는 전제에서 이 절차가 성립한다.
ko093 | SAME | ko089 | 1.00 | 공개된 사실과 맞는 행이 없다면 명세 후보와 공개된 사실부터 다시 대조해야 한다.
ko094 | SAME | ko090 | 1.00 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko095 | SAME | ko091 | 1.00 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko096 | SAME | ko092 | 1.00 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko097 | SAME | ko093 | 1.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko098 | SAME | ko094 | 1.00 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko099 | SAME | ko095 | 1.00 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko100 | SAME | ko096 | 1.00 | 다른 사례에서도 가능한 명세와 각각의 근거를 명시하면, 보류된 판정을 확정하기 위해 다음에 무엇을 확인할지 알 수 있다.
ko101 | SAME | ko097 | 1.00 | · 완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다.
ko102 | SAME | ko098 | 1.00 | 여기서는 앞의 질문에 해당하는 관찰만 남긴다.
ko103 | SAME | ko099 | 1.00 | 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 bracketed=True 를 넘기면 인자를 거절했다.
ko104 | SAME | ko100 | 1.00 | 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다.
ko105 | SAME | ko101 | 1.00 | 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.
ko106 | SAME | ko102 | 1.00 | 새 기능이 있다는 사실과 요구된 호출 경로에서 쓸 수 있다는 사실 은 다르다.
ko107 | SAME | ko103 | 1.00 | 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 Paper B 통합 원고 12 · 한·영 문장 교정 및 에 원형 그대로 보존했다.
ko108 | SAME | ko104 | 1.00 | 마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다.
ko109 | SAME | ko105 | 1.00 | 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다.
ko110 | SAME | ko106 | 1.00 | 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다.
ko111 | SAME | ko107 | 1.00 | 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다.
ko112 | SAME | ko108 | 1.00 | 원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가 가 이 논문에서 다룬 질문이다.
ko113 | SAME | ko109 | 1.00 | 공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다.
ko114 | SAME | ko110 | 1.00 | 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다.
ko115 | SAME | ko111 | 1.00 | 이 연구는 한 벤치마크의 저장 입력과 연구자가 구성한 실행 예제만을 다뤘다.
ko116 | SAME | ko112 | 1.00 | 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.
ko117 | SAME | ko113 | 1.00 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko118 | SAME | ko114 | 1.00 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko119 | SAME | ko115 | 1.00 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko120 | NEW | ko094 | 0.03 | 12판에 있던 그림 1과 파일 배치 실험은 14판 본문에 싣지 않았으며, 원본 그림과 실행 기록을 12판에 보존했다.
ko121 | SAME | ko117 | 1.00 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko122 | SAME | ko118 | 1.00 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
Summary ko: SAME 116, EDIT 0, NEW 6

### en (151 segmented sentences)
en001 | SAME | en001 | 1.00 | In 1996 Robert Martin described a function that draws shapes in the order it receives them.
en002 | SAME | en002 | 1.00 | A triangle can be added without touching the function if the triangle supplies its own drawing method.
en003 | SAME | en003 | 1.00 | Then Martin changes the task.
en004 | SAME | en004 | 1.00 | Every circle must be drawn before any square.
en005 | SAME | en005 | 1.00 | Give the function a list that begins with a square and it still draws the square first.
en006 | SAME | en006 | 1.00 | Who was supposed to put the circles first?
en007 | SAME | en007 | 1.00 | If the caller agreed to sort the list, the routine does its job.
en008 | SAME | en008 | 1.00 | If the routine must guarantee that order for any list, it needs an edit.
en009 | SAME | en009 | 1.00 | The source tells us what gets drawn first.
en010 | SAME | en010 | 1.00 | The agreement tells us whether that is a problem.
en011 | SAME | en011 | 1.00 | Martin’s drawing routine could stay as it was when the task was to add a shape.
en012 | SAME | en012 | 1.00 | Making it responsible for sorting changes that judgment.
en013 | SAME | en013 | 1.00 | We use over-axiomatization for the risk of treating an OCP violation label as sufficient grounds to reject a patch without establishing the governing change and caller obligations.
en014 | SAME | en014 | 1.00 | This is a claim about the use of advice, not a historical claim that OCP became a formal axiom.
en015 | SAME | en015 | 1.00 | We inspect a classification benchmark’s archive to see what instructions its models received.
en016 | SAME | en016 | 1.00 | In a separate catalog example we keep the code and patch fixed while varying the request and the promises to existing callers.
en017 | SAME | en017 | 1.00 | We then return to drawing to test whether a feature added in a separate file can be reached through the original function.
en018 | SAME | en018 | 1.00 | · · Martin attributed the principle to Bertrand Meyer, citing page 23 of the 1988 first edition.
en019 | SAME | en019 | 1.00 | For Meyer, a closed module has a stable specification that other modules can rely on.
en020 | SAME | en020 | 1.00 | His library example gives this a practical meaning.
en021 | SAME | en021 | 1.00 | If a catalog handles publication types one by one, adding technical reports can require editing or recompiling existing modules.
en022 | SAME | en022 | 1.00 | Where the new code goes affects how much of the existing system must change.
en023 | SAME | en023 | 1.00 | In a June 1995 public exchange, Kyle Brown argued that developers had to be able to fix a badly designed class.
en024 | SAME | en024 | 1.00 | Martin asked whether an anticipated extension had to require an edit to existing source.
en025 | SAME | en025 | 1.00 | That answer still depends on which changes can be anticipated.
en026 | SAME | en026 | 1.00 | The public record uses SOLID for the five principles by 2007.
en027 | SAME | en027 | 1.00 | A 2009 discussion gave different advice for internal classes and public plugin APIs.
en028 | SAME | en028 | 1.00 | These records show particular uses and objections.
en029 | SAME | en029 | 1.00 | They do not establish that circulation of the SOLID label caused the governing conditions to change.
en030 | SAME | en030 | 1.00 | · · Martin made DrawAllShapes responsible for sorting.
en031 | SAME | en031 | 1.00 | In one implementation Circle::Precedes checks the other shape and puts a circle before a square.
en032 | SAME | en032 | 1.00 | Deciding where a third shape belongs relative to a circle can require an edit to Circle .
en033 | SAME | en033 | 1.00 | Placing the order of types in a table lets squares go first with a swap of two entries.
en034 | SAME | en034 | 1.00 | Sorting individual shapes by area would require information that the table does not hold.
en035 | SAME | en035 | 1.00 | Later in the article Martin compares two uses of dynamic_cast .
en036 | SAME | en036 | 1.00 | One version of DrawAllShapes draws circles and squares, and DrawSquaresOnly draws squares alone.
en037 | SAME | en037 | 1.00 | A triangle left undrawn is a missed output when the task is to draw all shapes.
en038 | SAME | en038 | 1.00 | When the task is to draw squares, skipping it is correct.
en039 | SAME | en039 | 1.00 | How much of that responsibility can a reviewer determine from code and a prompt?
en040 | SAME | en040 | 1.00 | · · We separated the information used to classify code from the information needed to accept a patch.
en041 | SAME | en041 | 1.00 | The first part audits saved benchmark inputs; the second applies requirements and caller contracts that we specified to a patch we built.
en042 | SAME | en042 | 1.00 | We did not match the archive submissions to the catalog patch or to actual reviewers' decisions.
en043 | SAME | en043 | 1.00 | The OCP reference material contains 48 before-and-after code pairs.
en044 | SAME | en044 | 1.00 | Sixteen saved JSONL files each contain 48 records, yielding 768 rows.
en045 | SAME | en045 | 1.00 | Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times.
en046 | SAME | en046 | 1.00 | We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality.
en047 | SAME | en047 | 1.00 | The result was 24 scaffolds.
en048 | SAME | en048 | 1.00 | Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs.
en049 | SAME | en049 | 1.00 | The 768 records are repeated submissions, not independent maintenance cases.
en050 | SAME | en050 | 1.00 | We separately read the masked instructions for case-specific change requests and protected caller commitments.
en051 | SAME | en051 | 1.00 | An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape.
en052 | SAME | en052 | 1.00 | We inspected only the text outside the submitted code; names, comments and code structure may still give other clues.
en053 | SAME | en053 | 1.00 | We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace.
en054 | SAME | en054 | 1.00 | For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions.
en055 | SAME | en055 | 1.00 | These tests do not establish whether inherited methods remain available or whether callers were promised a behavior.
en056 | SAME | en056 | 1.00 | We read code as archive data and did not execute it.
en057 | SAME | en057 | 1.00 | For the catalog, we fixed the baseline, patch, input calls and permissible edit boundary, ran the calls, and recorded output or exceptions.
en058 | SAME | en058 | 1.00 | We defined acceptance as meeting the new demand and preserving the applicable contract.
en059 | SAME | en059 | 1.00 | The Section 5 verdicts follow from these authored criteria and the observed behavior; they are not independent human review decisions.
en060 | SAME | en060 | 1.00 | With partial disclosure, we retained the complete specifications compatible with known facts and checked whether the verdicts agreed.
en061 | SAME | en061 | 1.00 | · Pehlivan et al. chose violation scenarios and refined the generated examples.
en062 | SAME | en062 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en063 | SAME | en063 | 1.00 | The benchmark compares model classifications with the resulting labels.
en064 | SAME | en064 | 1.00 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en065 | SAME | en065 | 1.00 | No two strategies shared a template string.
en066 | SAME | en066 | 1.00 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en067 | SAME | en067 | 1.00 | An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: gpt-4o-mini differed from the other three models.
en068 | SAME | en068 | 1.00 | Holding model, strategy and language fixed left one scaffold shared across twelve programs.
en069 | SAME | en069 | 1.00 | No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST.
en070 | SAME | en070 | 1.00 | These checks do not establish semantic independence or source lineage.
en071 | SAME | en071 | 1.00 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en072 | SAME | en072 | 1.00 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en073 | SAME | en073 | 1.00 | If a new shape is needed, that branch is a place to look.
en074 | SAME | en074 | 1.00 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en075 | SAME | en075 | 1.00 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en076 | NEW | en045 | 0.20 | The source comparison reported above did not identify a submitted program identical to a reference side under the tested normalizations.
en077 | SAME | en078 | 1.00 | Pair 37 establishes that a declaration was removed.
en078 | SAME | en079 | 1.00 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en079 | SAME | en080 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en080 | SAME | en081 | 1.00 | The prompt example is in JSONL line 13 (record ID 12).
en081 | SAME | en082 | 1.00 | Pair 37 is in a separate reference JSON file.
en082 | SAME | en083 | 1.00 | · · · Bräuer et al. (2018) asked experts which parts of a design principle were captured by measurable practices.
en083 | SAME | en084 | 1.00 | Cabral et al. (2024) asked participants how easy they found it to understand and extend code under a bundled SOLID treatment in a machine-learning scenario.
en084 | SAME | en085 | 1.00 | Zhu et al. (2026) set repository change tasks and used functional and structural checks.
en085 | NEW | en008 | 0.12 | Distinguishing assumptions from guarantees is not a new idea.
en086 | NEW | en133 | 0.12 | Jones (1981) included rely and guarantee conditions in his treatment of interference between parallel programs, with proof obligations for their compatibility.
en087 | NEW | en028 | 0.09 | His subject was the correctness of parallel programs, not OCP review.
en088 | NEW | en008 | 0.10 | We do not offer a new rely–guarantee calculus.
en089 | NEW | en079 | 0.20 | We ask instead what evidence licenses using a design-principle finding as grounds for rejecting this patch.
en090 | SAME | en086 | 1.00 | In the next section we fix the patch and ask whether knowing a different requirement or caller contract changes the verdict.
en091 | SAME | en087 | 1.00 | · · We built a small catalog based on Meyer’s example.
en092 | SAME | en088 | 1.00 | The client in client.py displays each publication through the catalog function passed to it.
en093 | SAME | en089 | 1.00 | The patch adds reports.py to wrap that function.
en094 | SAME | en090 | 1.00 | The source of catalog.py and client.py stays identical.
en095 | SAME | en091 | 1.00 | The resulting catalog displays technical reports and still rejects errata.
en096 | SAME | en092 | 1.00 | For books it now prints BOOK where it used to print book .
en097 | SAME | en093 | 1.00 | Suppose the only new requirement is to handle technical reports.
en098 | SAME | en094 | 1.00 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en099 | SAME | en095 | 1.00 | If the book output is outside the contract, the same patch can be accepted.
en100 | SAME | en096 | 1.00 | Table 2 applies both contracts again when errata are also required.
en101 | SAME | en097 | 1.00 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en102 | SAME | en098 | 1.00 | Two requirements for accepting a fixed patch.
en103 | SAME | en099 | 1.00 | Learning that errata are required leaves the last two rows of Table 2.
en104 | SAME | en100 | 1.00 | Both reject the patch, so the book contract need not be settled first.
en105 | SAME | en101 | 1.00 | Learning that technical reports are the whole request leaves the first two rows.
en106 | SAME | en102 | 1.00 | One accepts and one rejects.
en107 | SAME | en103 | 1.00 | The next question is whether the original book output is protected.
en108 | SAME | en104 | 1.00 | This procedure assumes that the actual specification is among the cases under consideration.
en109 | SAME | en105 | 1.00 | If no row fits what was disclosed, the reviewer needs to recheck the candidate specifications against the facts.
en110 | SAME | en106 | 1.00 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en111 | SAME | en107 | 1.00 | The reviewer can give a conditional answer or defer judgment.
en112 | SAME | en108 | 1.00 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en113 | SAME | en109 | 1.00 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en114 | SAME | en110 | 1.00 | It adds one module, handles technical reports and errata, and keeps the original book output.
en115 | SAME | en111 | 1.00 | A rejection in Table 2 need not end the search for a patch within that boundary.
en116 | SAME | en112 | 1.00 | In another case, recording the possible specifications and the evidence for each can tell a reviewer what to check next.
en117 | SAME | en113 | 1.00 | · Deciding whether to accept a completed patch differs from choosing an architecture for future edits.
en118 | SAME | en114 | 1.00 | We retain one observation relevant to acceptance.
en119 | SAME | en115 | 1.00 | In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected bracketed=True .
en120 | SAME | en116 | 1.00 | A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.
en121 | SAME | en117 | 1.00 | The presence of a feature is different from its availability along a required route .
en122 | SAME | en118 | 1.00 | The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in Paper B 통합 원고 12 · 한·영 문장 교정 and its .
en123 | SAME | en119 | 1.00 | Drawing a square first establishes what a routine does, not whether it must be edited.
en124 | SAME | en120 | 1.00 | That depends on whether sorting belongs to the routine's obligations.
en125 | SAME | en121 | 1.00 | In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required.
en126 | SAME | en122 | 1.00 | We did not observe a real OCP label being misused to reject a patch.
en127 | SAME | en123 | 1.00 | We asked what additional grounds a design-principle assessment needs before it can justify an engineering decision .
en128 | SAME | en124 | 1.00 | Keeping the specifications compatible with known facts and checking their verdicts is elementary logic.
en129 | SAME | en125 | 1.00 | The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository.
en130 | SAME | en126 | 1.00 | Our evidence is confined to one benchmark archive and authored executable examples.
en131 | SAME | en127 | 1.00 | We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.
en132 | SAME | en128 | 1.00 | The audit in Sections 3–4 reads JSON and JSONL from the archived ZIP.
en133 | NEW | en129 | 0.45 | Section 5 and the call-path check in Section 6 use examples written for this study.
en134 | NEW | en118 | 0.11 | The shape-layout experiment and Figure 1 remain preserved in manuscript 12.
en135 | SAME | en130 | 1.00 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en136 | SAME | en131 | 1.00 | The table below gives the nine verdicts for Section 5.
en137 | SAME | en132 | 1.00 | Both values of a withheld field remain possible.
en138 | EDIT | en133 | 0.91 | Defer means that the compatible rows include both acceptance and rejection. - Meyer, B.
en139 | NEW | en028 | 0.14 | Object-Oriented Software Construction (1st ed.), pp.
en140 | NEW | en026 | 0.12 | The Open–Closed Principle . . - Jones, C.
en141 | NEW | en054 | 0.10 | Development Methods for Computer Programs Including a Notion of Interference .
en142 | NEW | en008 | 0.08 | Oxford University Computing Laboratory, PRG-25.
en143 | NEW | en061 | 0.10 | · . - Pehlivan, F., Ergüzen, A.
en144 | NEW | en089 | 0.02 | M., Lami, M., & Koyuncu, A.
en145 | NEW | en123 | 0.13 | An Empirical Study on Prompting LLMs to Detect Design Principle Violations .
en146 | NEW | en083 | 0.09 | ASE 2025 NIER. . - Bräuer et al.
en147 | NEW | en083 | 0.16 | Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research . . - Cabral et al.
en148 | NEW | en084 | 0.18 | Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding . . - Zhu, H., Zhang, Q., Wang, J., Yang, Z., & Qiu, Y.
en149 | NEW | en046 | 0.11 | Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits . .
en150 | NEW | — | 0.00 | 이 목록은 인용된 주요 자료를 확인할 수 있게 모은 집필용 서지이며, 서지형식·인용 위치·전수 대조를 마친 제출용 참고문헌은 아직 아니다.
en151 | NEW | en049 | 0.14 | / These are verified reading anchors, not yet a fully formatted submission bibliography.
Summary en: SAME 129, EDIT 1, NEW 21
