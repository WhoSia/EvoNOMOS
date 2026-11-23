# Paper B R19A — Sentence-Level Diff Index, v01–v07
Exact Notion source bodies fetched 2026-11-23. Intl.Segmenter ko/en; normalizer removes markup, links, table lines; fuzzy 3-gram Jaccard nearest match. SAME ≥0.94, EDIT ≥0.48, NEW otherwise. Match is editorial navigation, NOT semantic equivalence. Every extracted prose sentence gets one entry. v01 is baseline.

## v01 · [Notion](https://app.notion.com/p/41bef561cf9281c2b45dee94b4744969)
### KO (153 sentences; prior 0)
ko001 | BASE | — | 0.00 | 1996년 로버트 마틴은 도형 목록을 받아 하나씩 그리는 함수를 예로 들었다.
ko002 | BASE | — | 0.00 | 삼각형을 추가해도 삼각형이 자기를 그리는 방법을 제공하면 함수는 그대로 쓸 수 있었다.
ko003 | BASE | — | 0.00 | 마틴은 이 예를 보여 준 뒤 요구를 바꿨다.
ko004 | BASE | — | 0.00 | 이제 모든 원을 사각형보다 먼저 그려야 한다.
ko005 | BASE | — | 0.00 | 같은 함수에 사각형이 맨 앞에 든 목록을 넘기면 여전히 사각형부터 그린다.
ko006 | BASE | — | 0.00 | 호출자가 목록을 정렬해서 넘기기로 했다면 그리기 함수는 그대로 둘 수 있다.
ko007 | BASE | — | 0.00 | 함수가 어떤 목록을 받아도 원부터 그리기로 했다면 지금 코드로는 부족하다.
ko008 | BASE | — | 0.00 | 코드를 읽으면 함수가 목록을 정렬하지 않는다는 사실은 알 수 있다.
ko009 | BASE | — | 0.00 | 그 사실을 수정안을 거절할 근거로 쓰려면, 정렬을 누가 맡기로 했는지도 알아야 한다.
ko010 | BASE | — | 0.00 | ‘개방–폐쇄 원칙 위반’이라고만 적힌 검토 의견을 받았다면, 개발자는 먼저 자기 함수가 어떤 책임을 어겼다는 것인지 물어야 한다.
ko011 | BASE | — | 0.00 | 그 책임은 실제 분류 과제에서 모델에게 어떻게 전달되는가?
ko012 | BASE | — | 0.00 | SOLID 위반을 식별하는 한 벤치마크는 모델의 응답을 저자들이 정한 라벨과 대조한다.
ko013 | BASE | — | 0.00 | 우리는 개방–폐쇄 원칙에 관한 저장 프롬프트를 살펴봤다.
ko014 | BASE | — | 0.00 | 검토한 템플릿에는 사례별 변경 요구나 기존 호출자에게 보장한 동작이 따로 적혀 있지 않았다.
ko015 | BASE | — | 0.00 | 코드나 별도 시나리오에 단서가 있을 수 있다.
ko016 | BASE | — | 0.00 | 판정을 실제 수정 결정에 쓰려면, 그 단서가 어떤 책임을 뒷받침하는지 확인해야 한다.
ko017 | BASE | — | 0.00 | 그 책임이 결론을 가르는지 보려고 같은 수정안을 서로 다른 요구와 계약 아래 놓았다.
ko018 | BASE | — | 0.00 | 새 요구를 충족하지 못한다는 사실만으로도 거절이 가능한 경우가 있었다.
ko019 | BASE | — | 0.00 | 반면 새 요구를 충족한 뒤에도 기존 동작을 어디까지 보장했는지에 따라 승인 여부가 갈리는 경우가 있었다.
ko020 | BASE | — | 0.00 | 위반 판정을 받은 개발자에게 필요한 것은 바로 그 차이다.
ko021 | BASE | — | 0.00 | 지금 가진 근거로 거절이 결정되는지, 무엇을 더 확인해야 결정할 수 있는지다.
ko022 | BASE | — | 0.00 | 어떤 수정안이 가능한지를 판단하는 데도 같은 전제가 필요하다.
ko023 | BASE | — | 0.00 | 도형 예제의 후속 비교에서는 기능을 고정하고 호출 경로를 바꿔, 기존 파일을 그대로 둘 수 있는 후보가 언제 생기는지 확인한다.
ko024 | BASE | — | 0.00 | · · 마틴은 1996년 글의 첫머리에서 개방–폐쇄 원칙을 베르트랑 마이어에게서 가져왔다고 밝히고, 1988년 초판 23쪽을 인용했다.
ko025 | BASE | — | 0.00 | 마이어의 설명에서 모듈이 닫혀 있다는 것은 다른 모듈이 안정된 설명을 바탕으로 그것을 사용할 수 있다는 뜻이다.
ko026 | BASE | — | 0.00 | 구현을 들여다보면 여러 동작을 알 수 있지만, 그중 어디까지 계속 의존해도 되는지는 모듈이 약속한 설명에 달려 있다.
ko027 | BASE | — | 0.00 | 마이어는 도서관 프로그램에 기술보고서를 추가하는 예에서 이 구분을 구체화한다.
ko028 | BASE | — | 0.00 | 기존 모듈이 자료의 종류를 하나씩 구별해 처리한다면, 기술보고서 한 종류를 추가하는 데도 기존 모듈의 수정이나 재컴파일이 뒤따를 수 있다.
ko029 | BASE | — | 0.00 | 새 기능을 어디에 둘지가 중요한 이유는, 그 결정에 따라 기존 모듈을 사용하던 쪽에 돌아가는 일이 달라지기 때문이다.
ko030 | BASE | — | 0.00 | 마틴은 목록을 정렬하는 일을 DrawAllShapes 에 맡겼다.
ko031 | BASE | — | 0.00 | 함수는 도형 두 개를 어떤 순서로 그릴지 비교할 수 있어야 했다.
ko032 | BASE | — | 0.00 | Circle::Precedes 는 상대가 사각형이면 원을 먼저 그리도록 했다.
ko033 | BASE | — | 0.00 | 새 도형이 들어와 원과의 순서를 정해야 할 때, 그 결정을 내리는 코드는 이미 Circle 안에 있었다.
ko034 | BASE | — | 0.00 | 비교 함수는 두 도형의 실행 시 타입 이름을 얻어 표에서 각자의 위치를 찾는다.
ko035 | BASE | — | 0.00 | 사각형을 원보다 먼저 그리라는 요청이 들어오면 표에서 두 항목의 순서를 바꾸면 된다.
ko036 | BASE | — | 0.00 | ‘넓이가 작은 도형부터 그려 달라’는 요청이라면 표를 아무리 고쳐도 소용이 없다.
ko037 | BASE | — | 0.00 | 어느 부분을 그대로 둘 수 있는가는 어떤 순서 변경을 요구하느냐에 달려 있다.
ko038 | BASE | — | 0.00 | 마틴은 같은 글의 뒤에서 dynamic_cast 를 쓰는 두 함수를 나란히 놓았다.
ko039 | BASE | — | 0.00 | 하나는 원과 사각형을 가려내 각각 그리는 DrawAllShapes 다.
ko040 | BASE | — | 0.00 | 삼각형을 넘기면 어느 분기에도 들어가지 않는다.
ko041 | BASE | — | 0.00 | 다른 하나는 목록에서 사각형만 골라 그리는 DrawSquaresOnly 다.
ko042 | BASE | — | 0.00 | 앞의 함수에서는 그려야 할 도형을 빠뜨린 셈이고, 뒤의 함수에서는 사각형만 그린다는 약속을 지킨 셈이다.
ko043 | BASE | — | 0.00 | 두 함수 모두 실행 중에 도형의 타입을 검사한다.
ko044 | BASE | — | 0.00 | 그 검사를 보고 개방–폐쇄 원칙 위반을 판정하려면, 먼저 새 도형이 들어왔을 때 함수가 무엇을 해야 하는지 알아야 한다.
ko045 | BASE | — | 0.00 | 이름이나 주변 코드에 단서가 있을 수 있다.
ko046 | BASE | — | 0.00 | 그런 단서만으로 판단이 서지 않을 때는, 판정에 필요한 요구가 검토자에게 어디까지 주어졌는지가 중요해진다.
ko047 | BASE | — | 0.00 | · · 아카이브 감사에서는 분석 단위를 세 가지로 나눴다.
ko048 | BASE | — | 0.00 | 참조 코드 쌍은 위반 예시와 그에 대응하는 수정 예시로 이루어진다.
ko049 | BASE | — | 0.00 | 저장 응답 행에는 제출 코드, 프롬프트, 응답이 들어 있다.
ko050 | BASE | — | 0.00 | 각 프롬프트에서 정확히 한 번 나타나는 제출 코드를 같은 자리표시자로 바꿔 프롬프트 템플릿을 만들었다.
ko051 | BASE | — | 0.00 | OCP 자료에서 참조 코드 쌍 48개, 저장 응답 행 768개, 문자열이 서로 다른 템플릿 24개를 확인했다.
ko052 | BASE | — | 0.00 | 네 전략의 템플릿 사이에 문자열이 같은 경우는 없었다.
ko053 | BASE | — | 0.00 | 저장 기록의 제출 코드는 모든 참조 쌍의 수정 전·후 소스와 대조했다.
ko054 | BASE | — | 0.00 | 원문 그대로 비교하고, 문자열 양끝의 공백을 제거한 뒤 다시 비교했다.
ko055 | BASE | — | 0.00 | 이후 분석에서 프롬프트의 지시를 설명할 때는 저장 기록을, 수정 전후의 선언을 비교할 때는 참조 쌍을 인용한다.
ko056 | BASE | — | 0.00 | Python 예시에서는 코드의 추상 구문 트리를 읽어 최상위 클래스에 선언된 메서드 이름을 대조했다.
ko057 | BASE | — | 0.00 | 밑줄로 시작하는 이름은 집계 대상에서 제외했다.
ko058 | BASE | — | 0.00 | 이 방법으로 확인할 수 있는 것은 어떤 선언이 수정 전후에 나타나거나 사라졌는지다.
ko059 | BASE | — | 0.00 | 상속을 통해 호출할 수 있는지, 외부에서 사용해 왔는지, 그 사용을 계속 보장하기로 했는지는 각각 다른 증거가 필요하다.
ko060 | BASE | — | 0.00 | 공개 재현 패키지의 코드는 실행하지 않았다.
ko061 | BASE | — | 0.00 | · Pehlivan 등은 언어 모델이 코드 예시에서 SOLID 위반을 식별할 수 있는지 평가했다.
ko062 | BASE | — | 0.00 | 저자들은 먼저 위반 시나리오를 정하고, 생성한 예시 코드를 수정하고 검증했다.
ko063 | BASE | — | 0.00 | 의견이 갈리면 논의해서 참조 라벨을 정했다.
ko064 | BASE | — | 0.00 | 모델의 응답은 저자들이 이렇게 정한 분류를 얼마나 잘 재현하는지에 따라 평가됐다.
ko065 | BASE | — | 0.00 | 저장된 Python EXAMPLE 기록 한 건을 보면, 프롬프트는 다형성으로 처리할 만한 로직에 if-else 나 switch 분기가 반복되는 곳을 찾으라고 한다.
ko066 | BASE | — | 0.00 | 제출된 AreaCalculator 는 실제로 도형의 종류를 확인한 뒤 원과 사각형의 넓이를 각각 계산한다.
ko067 | BASE | — | 0.00 | 검토자는 새 도형을 추가한다면 이 분기에 손댈 수 있다고 추론할 수 있다.
ko068 | BASE | — | 0.00 | 그 도형을 추가하는 일이 실제 요구인지, 사각형의 너비를 직접 읽는 호출을 계속 지원해야 하는지는 프롬프트의 지시문에서 정해 주지 않는다.
ko069 | BASE | — | 0.00 | 저장된 OCP 기록 768건에서 제출 코드를 가리면 문자열이 서로 다른 프롬프트 틀 24개가 남는다.
ko070 | BASE | — | 0.00 | 개별 사례의 변경 요구나 보호할 호출자 계약을 따로 명시한 틀은 없었다.
ko071 | BASE | — | 0.00 | 참조 자료에도 같은 넓이 계산 문제를 사용한 코드 쌍이 있다.
ko072 | BASE | — | 0.00 | 37번 쌍의 수정본은 도형마다 넓이를 구하는 메서드를 두고 Rectangle.get_width 선언을 뺐다.
ko073 | BASE | — | 0.00 | 저장 프롬프트의 코드와 이 참조본은 서로 다른 소스다.
ko074 | BASE | — | 0.00 | 참조본에서 선언이 사라졌다는 사실은 두 버전을 대조하면 알 수 있다.
ko075 | BASE | — | 0.00 | 여기서 넓이만 구하는 호출자에게는 도형을 추가할 때 바뀌는 코드가 중요할 수 있다.
ko076 | BASE | — | 0.00 | 사각형의 너비를 직접 읽어 온 호출자에게는 그 호출의 지원 여부가 중요하다.
ko077 | BASE | — | 0.00 | 어느 쪽이 판정을 좌우하는지 확인하려면, 같은 수정안을 두고 새 요구와 기존 약속을 바꿔 볼 필요가 있다.
ko078 | BASE | — | 0.00 | 프롬프트 예시는 저장 JSONL 13행(ID 12)이다.
ko079 | BASE | — | 0.00 | 참조 쌍 37번은 별도의 ground truth JSON 위치다.
ko080 | BASE | — | 0.00 | · · · 마이어가 새 자료 유형을 추가하는 사례를 바탕으로 작은 도서관 목록 프로그램을 만들었다.
ko081 | BASE | — | 0.00 | 이 수정안은 기술보고서를 처리하는 모듈을 추가한다.
ko082 | BASE | — | 0.00 | 기존 소스 파일 두 개는 바이트 단위로 동일하다.
ko083 | BASE | — | 0.00 | 책 출력의 접두어는 book 에서 BOOK 으로 바뀐다.
ko084 | BASE | — | 0.00 | 기술보고서 출력은 성공하고 정오표 요청은 여전히 거절된다.
ko085 | BASE | — | 0.00 | 네 조건에서 수정안, 허용된 편집 범위와 실행 관찰값을 고정했다.
ko086 | BASE | — | 0.00 | 새 요구는 기술보고서만 지원하거나, 기술보고서와 정오표를 둘 다 지원하는 것이다.
ko087 | BASE | — | 0.00 | 기존 계약은 학술지와 학회록의 출력, 그리고 별개의 미지원 자료 유형을 거절하는 동작을 공통으로 보호한다.
ko088 | BASE | — | 0.00 | 이 비교에서는 새 요구와 기존 계약을 모두 만족하는 수정안을 승인한다.
ko089 | BASE | — | 0.00 | 기술보고서만 필요하고 책 표기까지 보호하지 않을 때 이 수정안은 승인된다.
ko090 | BASE | — | 0.00 | 정오표를 요구하면 새 요구를 충족하지 못한다.
ko091 | BASE | — | 0.00 | 새 모듈만 추가하는 별도 구현이 두 자료 유형을 모두 지원하면서 책 표기를 비롯한 모든 보호 동작을 유지했으므로, 같은 편집 범위 안에서 네 조건의 요구와 계약은 모두 충족 가능하다.
ko092 | BASE | — | 0.00 | 정오표가 필수라는 사실을 알면 책 표기 계약을 확인하기 전에도 이 수정안을 거절할 수 있다.
ko093 | BASE | — | 0.00 | 기술보고서만 필요하다는 사실을 알 때는 책 표기까지 보장했는지에 따라 결론이 갈린다.
ko094 | BASE | — | 0.00 | 이렇게 보면 검토자는 어떤 정보가 빠졌는지에 더해, 어떤 질문에 답하면 결정을 내릴 수 있는지도 알 수 있다.
ko095 | BASE | — | 0.00 | 현재 증거와 양립하는 명세들이 모두 같은 판정을 내놓으면 그 증거만으로도 결정을 내릴 수 있다.
ko096 | BASE | — | 0.00 | 두 명세가 서로 다른 판정을 내놓는데 검토자가 받는 입력은 같다면, 하나의 승인 또는 거절로 둘을 모두 맞힐 수 없다.
ko097 | BASE | — | 0.00 | 이 경우 검토자는 각 조건에서의 결론을 따로 밝히거나, 두 명세를 구별할 사실을 확인할 때까지 보류할 수 있다.
ko098 | BASE | — | 0.00 | 이 논증은 양립하는 명세가 적어도 하나 있고 실제 명세가 그 집합에 속한다는 전제에서 성립한다.
ko099 | BASE | — | 0.00 | 모든 행에서 기존 파일과 패치, 시험 입력과 관찰값, 허용된 파일 추가 경계를 동일하게 둔다.
ko100 | BASE | — | 0.00 | 좁은 계약은 저널·학회 자료와 미지원 종류의 거절을 보호한다.
ko101 | BASE | — | 0.00 | · 이 비교에서 거절의 근거가 되는 것은 구체적인 실패다.
ko102 | BASE | — | 0.00 | 정오표를 요구하는데 처리하지 못하거나, 이미 보호하기로 한 책 표기가 달라진다.
ko103 | BASE | — | 0.00 | 검토자는 확인된 요구나 계약 위반을 근거로 수정안을 거절할 수 있다.
ko104 | BASE | — | 0.00 | 이제 남는 설계 문제는 어떤 구조가 그런 계약을 지키면서 이후 변경에 덜 드는지를 예측하는 것이다.
ko105 | BASE | — | 0.00 | 그 설명이 설계 원칙을 넘어서는지 보려면, 아직 답을 모르는 다음 요구를 정하고 어느 설계가 더 유리할지 먼저 말할 수 있어야 한다.
ko106 | BASE | — | 0.00 | 그 예측을 시험하기 위해 도형 사례로 돌아가 보자.
ko107 | BASE | — | 0.00 | 도형마다 그리는 코드를 두면 삼각형은 새 파일 하나로 추가할 수 있었다.
ko108 | BASE | — | 0.00 | 같은 구조에서 원과 사각형에 이름표를 붙이는 새 연산을 넣으려면 기존 도형 파일 두 개를 고쳐야 했다.
ko109 | BASE | — | 0.00 | 연산마다 파일을 두는 구현에서는 이름표 연산을 새 파일로 넣을 수 있었고, 삼각형을 그리려면 기존 그리기 파일을 고쳐야 했다.
ko110 | BASE | — | 0.00 | 이 비교에서 기존 파일에 손대는 횟수를 줄여 준 것은 어느 한 구조의 일반적인 성질이 아니라, 파일을 나눈 기준과 요구가 바뀐 방향의 관계였다.
ko111 | BASE | — | 0.00 | 이번에는 요구와 기존 호출이 기대하는 동작을 그대로 두고, 어느 파일에 기능을 넣을 수 있는지를 바꿨다.
ko112 | BASE | — | 0.00 | 새 함수는 도형 목록을 받아 입력 순서대로 각 도형을 그린 결과를 대괄호로 감싼다.
ko113 | BASE | — | 0.00 | 항목을 변환하는 코드를 기존 도형 파일이 직접 맡도록 하면, 도형별 구현에서는 원과 사각형 파일을 모두 수정해야 한다고 예측했다.
ko114 | BASE | — | 0.00 | 공용 어댑터가 기존 렌더러의 결과를 감싸도 된다면, 두 구현 모두 새 파일 하나만으로 기능을 제공할 수 있다고 예측했다.
ko115 | BASE | — | 0.00 | 구현 전에 두 예측을 기록한 뒤 네 후보를 실행했다.
ko116 | BASE | — | 0.00 | 네 후보 모두 입력 순서와 중복을 유지했고, 빈 목록과 지원하지 않는 도형을 명세대로 처리했다.
ko117 | BASE | — | 0.00 | 기존 파일을 고친 후보는 도형 파일에 항목 변환을 맡긴 경우뿐이었다.
ko118 | BASE | — | 0.00 | 바뀐 파일은 원과 사각형의 파일 두 개였다.
ko119 | BASE | — | 0.00 | 다른 세 후보에서는 기존 파일의 바이트가 그대로였다.
ko120 | BASE | — | 0.00 | 네 경우 모두 배치 진입점을 새 파일 하나에 두었다.
ko121 | BASE | — | 0.00 | 그림 1의 왼쪽은 바라는 기능을 따로 바꿨을 때, 오른쪽은 같은 기능에 허용된 구현 경로만 바꿨을 때의 결과다.
ko122 | BASE | — | 0.00 | 공용 어댑터를 허용한다는 조건은 호출자가 그 모듈을 실제로 사용할 수 있다는 뜻인가?
ko123 | BASE | — | 0.00 | 다음 비교에서는 기존 원과 사각형의 기본 출력은 그대로 두고, 선택적으로 결과를 대괄호로 감싸도록 했다.
ko124 | BASE | — | 0.00 | 새 모듈로 호출할 수 있을 때는 두 배치 모두 기존 파일을 고치지 않았다.
ko125 | BASE | — | 0.00 | 같은 모듈을 추가한 채 원래 함수에 새 옵션을 넘기면, 원래 함수는 그 인자를 받지 못했다.
ko126 | BASE | — | 0.00 | 원래 함수로 기능을 제공한 후보는 연산별 배치에서 기존 파일 하나, 도형별 배치에서 둘을 수정했다.
ko127 | BASE | — | 0.00 | 처음부터 외부 변환 함수를 불러올 수 있게 해 둔 별도 기준선에서는 원래 함수로 호출해도 새 파일 하나만 추가하면 됐다.
ko128 | BASE | — | 0.00 | 어디에 파일을 놓아도 되는지 알면 후보를 만들 수 있다.
ko129 | BASE | — | 0.00 | 그 후보가 기존 호출에도 새 기능을 전달할 수 있는지 알려면, 실행 중에 그 코드까지 도달하는 경로가 있어야 한다.
ko130 | BASE | — | 0.00 | 미리 설치된 확장 지점은 그 경로를 만들고, 표 3의 마지막 행은 그 지점이 이미 있던 상태에서의 추가 변경을 센다.
ko131 | BASE | — | 0.00 | 독립적으로 작성한 요구에 대해서도 어느 경로가 작동할지 미리 예측하려면 별도의 평가가 필요하다.
ko132 | BASE | — | 0.00 | A는 서로 다른 두 요구를, B는 동일한 배치 렌더링 요구에 적용한 두 배치 규칙을 비교한다.
ko133 | BASE | — | 0.00 | B의 네 후보는 모두 같은 기능·기존 동작 검사를 통과했고 새 파일 하나를 추가했다.
ko134 | BASE | — | 0.00 | / Existing source files edited.
ko135 | BASE | — | 0.00 | Panel A varies the request.
ko136 | BASE | — | 0.00 | Panel B varies the placement rule for the same batch-rendering request.
ko137 | BASE | — | 0.00 | Each candidate in panel B passed the common behavior checks and added one file.
ko138 | BASE | — | 0.00 | · · · · 표 3 · 새 렌더링 옵션의 호출 경로 / Entry points for the new rendering option 셋째 행의 변경 수는 확장 지점을 이미 둔 별도 기준선에서 센 것이다.
ko139 | BASE | — | 0.00 | 두 배치 모두 원래 진입점만 사용한 대조 실행에서 모듈만 추가했을 때 새 옵션이 거부됨을 확인했다.
ko140 | BASE | — | 0.00 | · 도형을 그리는 함수에 개방–폐쇄 원칙을 적용하려면 먼저 어떤 순서로 그려야 하고 누가 그 순서를 맡는지 알아야 한다.
ko141 | BASE | — | 0.00 | 코드 리뷰에서도 같은 정보가 판정을 가른다.
ko142 | BASE | — | 0.00 | 저장 프롬프트에서 확인한 분류 지시는 벤치마크의 참조 라벨을 맞히는 데 쓰인다.
ko143 | BASE | — | 0.00 | 실제 수정안의 수용 여부를 판단할 때는 새 요구와 기존 호출자에게 보장한 동작을 함께 살펴야 한다.
ko144 | BASE | — | 0.00 | 같은 도서관 수정안도 이 조건에 따라 승인되거나 거절됐다.
ko145 | BASE | — | 0.00 | 정오표가 필수라는 사실만으로 거절을 결정할 수 있었고, 기술보고서만 요구할 때는 책 표기 계약을 알아야 했다.
ko146 | BASE | — | 0.00 | 설계를 비교할 때는 수정안이 해당 호출자에게 도달하는지도 따져야 한다.
ko147 | BASE | — | 0.00 | 도형 예제에서는 추가 모듈을 호출할 수 있는지, 기존 진입점에 확장 지점이 있는지에 따라 기존 파일을 그대로 둘 수 있는 후보가 달라졌다.
ko148 | BASE | — | 0.00 | 검토 의견에 새 요구와 보호할 계약, 적용되는 호출 경로를 명시하면 개발자는 거절 이유를 확인하거나 판정에 필요한 다음 사실을 물을 수 있다.
ko149 | BASE | — | 0.00 | 이 글이 확인한 범위는 한 벤치마크의 저장 자료와 직접 구성한 수정안이다.
ko150 | BASE | — | 0.00 | §3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다.
ko151 | BASE | — | 0.00 | §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다.
ko152 | BASE | — | 0.00 | 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다.
ko153 | BASE | — | 0.00 | 그림 1의 소스와 출력 위치는 그림 캡션에 있다.
Summary ko: same 0; edited 0; new 0.

### EN (167 sentences; prior 0)
en001 | BASE | — | 0.00 | In 1996, Robert Martin described a function that took a list of shapes and drew them one by one.
en002 | BASE | — | 0.00 | A triangle could be added without touching the function, provided the triangle supplied its own drawing operation.
en003 | BASE | — | 0.00 | Martin then changed the requirement.
en004 | BASE | — | 0.00 | Every circle now had to be drawn before any square.
en005 | BASE | — | 0.00 | Give the same function a list with a square at the front and it still draws the square first.
en006 | BASE | — | 0.00 | Where should the edit go?
en007 | BASE | — | 0.00 | If callers agree to sort the list before passing it in, the drawing function can stay as it is.
en008 | BASE | — | 0.00 | If the function is responsible for putting circles first regardless of input order, its current implementation falls short.
en009 | BASE | — | 0.00 | The source tells us that the function does no sorting.
en010 | BASE | — | 0.00 | Rejecting a patch on those grounds also requires knowing who was meant to sort the list.
en011 | BASE | — | 0.00 | A review comment that says only “open–closed principle violation” leaves the developer to ask which obligation the function was supposed to meet.
en012 | BASE | — | 0.00 | How does that obligation reach the model in a classification task?
en013 | BASE | — | 0.00 | One benchmark for identifying SOLID violations evaluates model responses against labels established by its authors.
en014 | BASE | — | 0.00 | We examine its saved prompts for the open–closed principle.
en015 | BASE | — | 0.00 | In the templates we inspected, the case-specific change request and the commitment to existing callers were not stated separately.
en016 | BASE | — | 0.00 | The code or an accompanying scenario may offer clues.
en017 | BASE | — | 0.00 | Using the verdict to decide whether to take an edit requires checking what obligations those clues establish.
en018 | BASE | — | 0.00 | We test whether those obligations can decide the outcome by placing the same patch under different demands and contracts.
en019 | BASE | — | 0.00 | In one condition, a failure to meet the new requirement suffices to reject the edit.
en020 | BASE | — | 0.00 | In another, the new requirement is met and the decision turns on what existing callers were promised.
en021 | BASE | — | 0.00 | For the developer receiving the review, that difference determines what to do next.
en022 | BASE | — | 0.00 | The evidence may already warrant rejection, or the decision may depend on a fact the reviewer still needs to establish.
en023 | BASE | — | 0.00 | The same premises matter when asking which edits are available in the first place.
en024 | BASE | — | 0.00 | A follow-up comparison in the drawing fixture keeps the feature fixed and varies the caller’s route to see when a candidate can leave the existing files intact.
en025 | BASE | — | 0.00 | · · At the start of his 1996 article, Martin attributes the open–closed principle to Bertrand Meyer and cites page 23 of the 1988 first edition.
en026 | BASE | — | 0.00 | In Meyer's account, a module is closed when other modules can use it on the basis of a stable description.
en027 | BASE | — | 0.00 | Reading the implementation may tell a client how the module happens to behave.
en028 | BASE | — | 0.00 | The description tells the client which behavior it can continue to rely on.
en029 | BASE | — | 0.00 | Meyer makes the problem concrete by adding technical reports to a library program.
en030 | BASE | — | 0.00 | If existing modules handle publication types by distinguishing them one by one, adding even one type can require changes or recompilation in those modules.
en031 | BASE | — | 0.00 | Where the new functionality goes matters because that choice determines which existing users of the module have more work to do.
en032 | BASE | — | 0.00 | Martin assigned sorting to DrawAllShapes .
en033 | BASE | — | 0.00 | The function needed a way to compare two shapes and decide which to draw first.
en034 | BASE | — | 0.00 | In the first implementation, the circle inspected the other shape.
en035 | BASE | — | 0.00 | Circle::Precedes put the circle first if the other shape was a square.
en036 | BASE | — | 0.00 | When a new kind of shape arrived and its place relative to a circle had to be decided, the code making that decision already lived inside Circle .
en037 | BASE | — | 0.00 | Martin moved the ordering of shape types into a table.
en038 | BASE | — | 0.00 | The comparison function obtains the two shapes’ runtime type names and looks up their positions in the table.
en039 | BASE | — | 0.00 | If squares now have to be drawn before circles, the two entries can trade places.
en040 | BASE | — | 0.00 | A request to draw smaller shapes first by area calls for a different change.
en041 | BASE | — | 0.00 | The table records the order of shape types and carries no information about the area of an individual shape.
en042 | BASE | — | 0.00 | Which part of the program can stay as it is depends on the change being requested.
en043 | BASE | — | 0.00 | The same question arises with type checks.
en044 | BASE | — | 0.00 | Later in the article, Martin puts two functions that use dynamic_cast side by side.
en045 | BASE | — | 0.00 | One, DrawAllShapes , recognizes circles and squares and draws them.
en046 | BASE | — | 0.00 | A triangle falls through both branches.
en047 | BASE | — | 0.00 | The other, DrawSquaresOnly , selects squares from a list and draws them.
en048 | BASE | — | 0.00 | A triangle goes undrawn there as well.
en049 | BASE | — | 0.00 | In the first function, a shape that should have been drawn is skipped.
en050 | BASE | — | 0.00 | In the second, skipping it is part of what the function promises to do.
en051 | BASE | — | 0.00 | Both functions inspect a shape’s type at runtime.
en052 | BASE | — | 0.00 | To treat that check as evidence of an Open–Closed Principle violation, a reviewer first needs to know what the function owes a caller who supplies a new kind of shape.
en053 | BASE | — | 0.00 | A name or the surrounding code may offer a clue.
en054 | BASE | — | 0.00 | Where those clues leave the obligation open, the verdict depends on what the reviewer was told about the required behavior.
en055 | BASE | — | 0.00 | · · The archive audit uses three units.
en056 | BASE | — | 0.00 | A reference pair contains a violation example and its corresponding revision.
en057 | BASE | — | 0.00 | A saved response record contains the submitted code, the prompt, and the recorded response.
en058 | BASE | — | 0.00 | We recovered each prompt template by replacing the single exact occurrence of the submitted code with a common placeholder.
en059 | BASE | — | 0.00 | The OCP material yielded 48 reference pairs, 768 saved response records, and 24 templates with distinct text.
en060 | BASE | — | 0.00 | No template string was shared across the four strategies.
en061 | BASE | — | 0.00 | We compared every saved submission with the source on both sides of every reference pair.
en062 | BASE | — | 0.00 | We compared the original strings and repeated the comparison after trimming whitespace from both ends.
en063 | BASE | — | 0.00 | Neither comparison yielded an exact match.
en064 | BASE | — | 0.00 | We use saved records to describe the prompt instructions and reference pairs to compare declarations across revisions.
en065 | BASE | — | 0.00 | For the Python pairs, we parsed the code and compared method names declared in top-level classes.
en066 | BASE | — | 0.00 | We excluded names beginning with an underscore.
en067 | BASE | — | 0.00 | The comparison identifies declarations that appear or disappear between versions.
en068 | BASE | — | 0.00 | Inherited availability, actual use by callers, and commitments to preserve that use require additional evidence.
en069 | BASE | — | 0.00 | We executed no code from the replication archive.
en070 | BASE | — | 0.00 | · Pehlivan et al. evaluated whether language models could identify SOLID violations in code examples.
en071 | BASE | — | 0.00 | The authors specified violation scenarios, then refined and verified the generated code examples.
en072 | BASE | — | 0.00 | They resolved disagreement about the reference labels through discussion.
en073 | BASE | — | 0.00 | They assessed model responses against the resulting classifications.
en074 | BASE | — | 0.00 | One saved Python record from the EXAMPLE condition directs the reviewer to look for repeated if-else or switch branches where polymorphism would fit.
en075 | BASE | — | 0.00 | Its submitted AreaCalculator checks a shape’s type before calculating the area of a circle or rectangle.
en076 | BASE | — | 0.00 | A reviewer can infer that adding a shape might require editing that branch.
en077 | BASE | — | 0.00 | The instructions leave open whether anyone has requested such an extension and whether callers that read a rectangle’s width must still be supported.
en078 | BASE | — | 0.00 | Masking the submitted code in the 768 saved OCP records leaves 24 distinct prompt templates.
en079 | BASE | — | 0.00 | None separately states a change request or protected caller contract for an individual case.
en080 | BASE | — | 0.00 | A separate reference pair uses the same area-calculation setup.
en081 | BASE | — | 0.00 | In pair 37, the revised code moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en082 | BASE | — | 0.00 | This pair and the code in the saved prompt are distinct source texts.
en083 | BASE | — | 0.00 | Comparing the two versions of the reference pair establishes that a declaration disappeared.
en084 | BASE | — | 0.00 | For a caller that only calculates area, the relevant question may be what has to change when a new shape is added.
en085 | BASE | — | 0.00 | For a caller that reads a rectangle’s width directly, continued support for the call matters.
en086 | BASE | — | 0.00 | To see which premise can settle the verdict, we hold a patch fixed and vary the requested extension and the obligations to existing callers.
en087 | BASE | — | 0.00 | Evidence in the saved material and evidence needed to assess a patch.
en088 | BASE | — | 0.00 | The saved prompt is on JSONL line 13 (record ID 12).
en089 | BASE | — | 0.00 | Reference pair 37 is in a separate ground-truth JSON file. 768 counts saved records.
en090 | BASE | — | 0.00 | · · · We built a small library catalog based on Meyer's example of adding a publication type.
en091 | BASE | — | 0.00 | The patch adds a module that handles technical reports.
en092 | BASE | — | 0.00 | The two existing source files remain byte-for-byte identical.
en093 | BASE | — | 0.00 | The prefix in the rendering of an existing book changes from book to BOOK .
en094 | BASE | — | 0.00 | Technical reports render successfully and requests for errata are still rejected.
en095 | BASE | — | 0.00 | We hold the patch, the permitted edit boundary, and the observed execution results fixed across four conditions.
en096 | BASE | — | 0.00 | The new request calls for technical reports alone or for both technical reports and errata.
en097 | BASE | — | 0.00 | Both client contracts protect the rendering of journals and proceedings and the rejection of a separate unsupported publication type.
en098 | BASE | — | 0.00 | The broader contract also protects the original book prefix.
en099 | BASE | — | 0.00 | We accept the patch in this comparison when it meets the new request and preserves the existing contract.
en100 | BASE | — | 0.00 | The patch is acceptable when only reports are needed and the book prefix is outside the contract.
en101 | BASE | — | 0.00 | Requiring errata causes it to fail the new request.
en102 | BASE | — | 0.00 | Protecting the book prefix causes it to fail the existing contract.
en103 | BASE | — | 0.00 | A separate implementation adds only a new module, handles both new types, and preserves every protected outcome, including the original book prefix.
en104 | BASE | — | 0.00 | The demand and contract are therefore jointly satisfiable in all four conditions under the same edit boundary.
en105 | BASE | — | 0.00 | Learning that errata are required suffices to reject this patch even before the book contract is known.
en106 | BASE | — | 0.00 | Learning that only technical reports are required leaves the decision open until we know whether the prefix was promised.
en107 | BASE | — | 0.00 | The reviewer can thus identify which outstanding question would settle the decision.
en108 | BASE | — | 0.00 | If all specifications compatible with the available evidence yield the same verdict, that evidence suffices for the decision.
en109 | BASE | — | 0.00 | If two specifications yield different verdicts and the reviewer receives identical input in both, any single binary verdict fails to agree with at least one specification.
en110 | BASE | — | 0.00 | The reviewer can report conditional decisions or defer until a distinguishing fact is known.
en111 | BASE | — | 0.00 | This argument assumes that the compatible set is nonempty and contains the actual specification.
en112 | BASE | — | 0.00 | Two independent conditions for the same patch.
en113 | BASE | — | 0.00 | · In this comparison, a rejection has a specific basis.
en114 | BASE | — | 0.00 | The patch either fails to support required errata or changes a book prefix that callers were promised.
en115 | BASE | — | 0.00 | A reviewer can use such a failure to enforce a stated commitment.
en116 | BASE | — | 0.00 | The remaining design question is which architecture will preserve those commitments at lower cost as requirements change.
en117 | BASE | — | 0.00 | To test the explanatory reach of such an account, we would need to specify a new requirement independently and predict which design will handle it more easily before observing the outcome.
en118 | BASE | — | 0.00 | The drawing example gives us a way to test that prediction.
en119 | BASE | — | 0.00 | With drawing code organized by shape, adding a triangle took one new file.
en120 | BASE | — | 0.00 | Adding a labeling operation for circles and squares required editing both existing shape files.
en121 | BASE | — | 0.00 | In the implementation organized by operation, labeling went into a new file, while drawing a triangle required editing the existing drawing file.
en122 | BASE | — | 0.00 | All four patches passed their functional checks.
en123 | BASE | — | 0.00 | In this comparison, how many existing files an edit touched depended on how the file boundaries lined up with the requested extension.
en124 | BASE | — | 0.00 | We next held the requirement and the legacy caller’s observations fixed and varied where the new behavior could live.
en125 | BASE | — | 0.00 | The new function takes a list of shapes and returns their rendered strings, each enclosed in brackets, in input order.
en126 | BASE | — | 0.00 | If each shape file had to own its item transformation, we predicted that the shape-organized candidate would have to edit both existing shape files.
en127 | BASE | — | 0.00 | If a shared adapter could decorate the result of the existing renderer, we predicted that either layout could provide the feature in one new file.
en128 | BASE | — | 0.00 | We recorded the predictions before implementing the candidates and then ran all four.
en129 | BASE | — | 0.00 | They preserved input order and repeated items, handled the empty list and unsupported shapes as specified, and preserved the existing circle and square renderings.
en130 | BASE | — | 0.00 | The only candidate that changed existing files was the shape-organized implementation under the ownership rule.
en131 | BASE | — | 0.00 | It edited the circle and square files.
en132 | BASE | — | 0.00 | The other three kept the existing files byte-for-byte.
en133 | BASE | — | 0.00 | All four added one file containing the batch entry point.
en134 | BASE | — | 0.00 | Figure 1 pairs the earlier change-of-request comparison with this change-of-placement comparison.
en135 | BASE | — | 0.00 | What happens if a caller cannot use the shared adapter?
en136 | BASE | — | 0.00 | We kept the default rendering of circles and squares and added an option to enclose the result in brackets.
en137 | BASE | — | 0.00 | When callers could use a new module, both layouts left their existing files intact.
en138 | BASE | — | 0.00 | With the same module added, calls through the original rendering functions still rejected the new keyword.
en139 | BASE | — | 0.00 | The candidates that delivered the option through those functions edited one existing file in the operation layout and two in the shape layout.
en140 | BASE | — | 0.00 | In a separate baseline equipped with a hook that could load an external decorator, adding one file sufficed even through the original functions.
en141 | BASE | — | 0.00 | Permission to add a file lets a developer write a candidate.
en142 | BASE | — | 0.00 | To deliver the change through an existing call, the execution must also be able to reach the new code.
en143 | BASE | — | 0.00 | A pre-existing hook supplies such a path.
en144 | BASE | — | 0.00 | The last row of Table 3 counts the edits made once that hook was in place.
en145 | BASE | — | 0.00 | Predicting which paths will work for independently authored requests requires a separate evaluation.
en146 | BASE | — | 0.00 | A는 서로 다른 두 요구를, B는 동일한 배치 렌더링 요구에 적용한 두 배치 규칙을 비교한다.
en147 | BASE | — | 0.00 | B의 네 후보는 모두 같은 기능·기존 동작 검사를 통과했고 새 파일 하나를 추가했다.
en148 | BASE | — | 0.00 | / Existing source files edited.
en149 | BASE | — | 0.00 | Panel A varies the request.
en150 | BASE | — | 0.00 | Panel B varies the placement rule for the same batch-rendering request.
en151 | BASE | — | 0.00 | Each candidate in panel B passed the common behavior checks and added one file.
en152 | BASE | — | 0.00 | · · · · 표 3 · 새 렌더링 옵션의 호출 경로 / Entry points for the new rendering option 셋째 행의 변경 수는 확장 지점을 이미 둔 별도 기준선에서 센 것이다.
en153 | BASE | — | 0.00 | 두 배치 모두 원래 진입점만 사용한 대조 실행에서 모듈만 추가했을 때 새 옵션이 거부됨을 확인했다.
en154 | BASE | — | 0.00 | · Applying the open–closed principle to a drawing routine starts with knowing which order the shapes must appear in and who is responsible for that order.
en155 | BASE | — | 0.00 | Code review faces the same question about a change and its obligations.
en156 | BASE | — | 0.00 | The archived instructions support classification against the benchmark’s reference labels.
en157 | BASE | — | 0.00 | Evaluating an actual patch also takes a concrete request and an account of what existing callers were promised.
en158 | BASE | — | 0.00 | The same catalog patch was accepted or rejected under different specifications.
en159 | BASE | — | 0.00 | A requirement to handle errata sufficed to reject it.
en160 | BASE | — | 0.00 | When only technical reports were required, the decision turned on the contract for the book prefix.
en161 | BASE | — | 0.00 | Comparing designs adds a question about how the change reaches its callers.
en162 | BASE | — | 0.00 | In the drawing fixture, the existence of an additive candidate depended on whether callers could take a new route or reach an extension hook through their original entry point.
en163 | BASE | — | 0.00 | A review that specifies the request, the protected contract, and the relevant call path lets a developer check the grounds for rejection or identify the fact still needed to decide.
en164 | BASE | — | 0.00 | The evidence here covers the saved records of one benchmark and the patches constructed for these comparisons.
en165 | BASE | — | 0.00 | For Sections 3–4 the audit reads the archived JSON and JSONL.
en166 | BASE | — | 0.00 | For Sections 5–6 the fixtures run the examples constructed for this study.
en167 | BASE | — | 0.00 | The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.
Summary en: same 0; edited 0; new 0.

## v02 · [Notion](https://app.notion.com/p/41bef561cf92819fa364da217c66be0f)
### KO (147 sentences; prior 153)
ko001 | SAME | ko001 | 1.00 | 1996년 로버트 마틴은 도형 목록을 받아 하나씩 그리는 함수를 예로 들었다.
ko002 | SAME | ko002 | 1.00 | 삼각형을 추가해도 삼각형이 자기를 그리는 방법을 제공하면 함수는 그대로 쓸 수 있었다.
ko003 | SAME | ko003 | 1.00 | 마틴은 이 예를 보여 준 뒤 요구를 바꿨다.
ko004 | SAME | ko004 | 1.00 | 이제 모든 원을 사각형보다 먼저 그려야 한다.
ko005 | SAME | ko005 | 1.00 | 같은 함수에 사각형이 맨 앞에 든 목록을 넘기면 여전히 사각형부터 그린다.
ko006 | SAME | ko006 | 1.00 | 호출자가 목록을 정렬해서 넘기기로 했다면 그리기 함수는 그대로 둘 수 있다.
ko007 | SAME | ko007 | 1.00 | 함수가 어떤 목록을 받아도 원부터 그리기로 했다면 지금 코드로는 부족하다.
ko008 | SAME | ko008 | 1.00 | 코드를 읽으면 함수가 목록을 정렬하지 않는다는 사실은 알 수 있다.
ko009 | SAME | ko009 | 1.00 | 그 사실을 수정안을 거절할 근거로 쓰려면, 정렬을 누가 맡기로 했는지도 알아야 한다.
ko010 | SAME | ko010 | 1.00 | ‘개방–폐쇄 원칙 위반’이라고만 적힌 검토 의견을 받았다면, 개발자는 먼저 자기 함수가 어떤 책임을 어겼다는 것인지 물어야 한다.
ko011 | SAME | ko011 | 1.00 | 그 책임은 실제 분류 과제에서 모델에게 어떻게 전달되는가?
ko012 | SAME | ko012 | 1.00 | SOLID 위반을 식별하는 한 벤치마크는 모델의 응답을 저자들이 정한 라벨과 대조한다.
ko013 | SAME | ko013 | 1.00 | 우리는 개방–폐쇄 원칙에 관한 저장 프롬프트를 살펴봤다.
ko014 | SAME | ko014 | 1.00 | 검토한 템플릿에는 사례별 변경 요구나 기존 호출자에게 보장한 동작이 따로 적혀 있지 않았다.
ko015 | SAME | ko015 | 1.00 | 코드나 별도 시나리오에 단서가 있을 수 있다.
ko016 | SAME | ko016 | 1.00 | 판정을 실제 수정 결정에 쓰려면, 그 단서가 어떤 책임을 뒷받침하는지 확인해야 한다.
ko017 | SAME | ko017 | 1.00 | 그 책임이 결론을 가르는지 보려고 같은 수정안을 서로 다른 요구와 계약 아래 놓았다.
ko018 | SAME | ko018 | 1.00 | 새 요구를 충족하지 못한다는 사실만으로도 거절이 가능한 경우가 있었다.
ko019 | SAME | ko019 | 1.00 | 반면 새 요구를 충족한 뒤에도 기존 동작을 어디까지 보장했는지에 따라 승인 여부가 갈리는 경우가 있었다.
ko020 | SAME | ko020 | 1.00 | 위반 판정을 받은 개발자에게 필요한 것은 바로 그 차이다.
ko021 | SAME | ko021 | 1.00 | 지금 가진 근거로 거절이 결정되는지, 무엇을 더 확인해야 결정할 수 있는지다.
ko022 | SAME | ko022 | 1.00 | 어떤 수정안이 가능한지를 판단하는 데도 같은 전제가 필요하다.
ko023 | SAME | ko023 | 1.00 | 도형 예제의 후속 비교에서는 기능을 고정하고 호출 경로를 바꿔, 기존 파일을 그대로 둘 수 있는 후보가 언제 생기는지 확인한다.
ko024 | SAME | ko024 | 1.00 | · · 마틴은 1996년 글의 첫머리에서 개방–폐쇄 원칙을 베르트랑 마이어에게서 가져왔다고 밝히고, 1988년 초판 23쪽을 인용했다.
ko025 | SAME | ko025 | 1.00 | 마이어의 설명에서 모듈이 닫혀 있다는 것은 다른 모듈이 안정된 설명을 바탕으로 그것을 사용할 수 있다는 뜻이다.
ko026 | SAME | ko026 | 1.00 | 구현을 들여다보면 여러 동작을 알 수 있지만, 그중 어디까지 계속 의존해도 되는지는 모듈이 약속한 설명에 달려 있다.
ko027 | SAME | ko027 | 1.00 | 마이어는 도서관 프로그램에 기술보고서를 추가하는 예에서 이 구분을 구체화한다.
ko028 | SAME | ko028 | 1.00 | 기존 모듈이 자료의 종류를 하나씩 구별해 처리한다면, 기술보고서 한 종류를 추가하는 데도 기존 모듈의 수정이나 재컴파일이 뒤따를 수 있다.
ko029 | SAME | ko029 | 1.00 | 새 기능을 어디에 둘지가 중요한 이유는, 그 결정에 따라 기존 모듈을 사용하던 쪽에 돌아가는 일이 달라지기 때문이다.
ko030 | SAME | ko030 | 1.00 | 마틴은 목록을 정렬하는 일을 DrawAllShapes 에 맡겼다.
ko031 | SAME | ko031 | 1.00 | 함수는 도형 두 개를 어떤 순서로 그릴지 비교할 수 있어야 했다.
ko032 | SAME | ko032 | 1.00 | Circle::Precedes 는 상대가 사각형이면 원을 먼저 그리도록 했다.
ko033 | SAME | ko033 | 1.00 | 새 도형이 들어와 원과의 순서를 정해야 할 때, 그 결정을 내리는 코드는 이미 Circle 안에 있었다.
ko034 | SAME | ko034 | 1.00 | 비교 함수는 두 도형의 실행 시 타입 이름을 얻어 표에서 각자의 위치를 찾는다.
ko035 | SAME | ko035 | 1.00 | 사각형을 원보다 먼저 그리라는 요청이 들어오면 표에서 두 항목의 순서를 바꾸면 된다.
ko036 | SAME | ko036 | 1.00 | ‘넓이가 작은 도형부터 그려 달라’는 요청이라면 표를 아무리 고쳐도 소용이 없다.
ko037 | SAME | ko037 | 1.00 | 어느 부분을 그대로 둘 수 있는가는 어떤 순서 변경을 요구하느냐에 달려 있다.
ko038 | SAME | ko038 | 1.00 | 마틴은 같은 글의 뒤에서 dynamic_cast 를 쓰는 두 함수를 나란히 놓았다.
ko039 | SAME | ko039 | 1.00 | 하나는 원과 사각형을 가려내 각각 그리는 DrawAllShapes 다.
ko040 | SAME | ko040 | 1.00 | 삼각형을 넘기면 어느 분기에도 들어가지 않는다.
ko041 | SAME | ko041 | 1.00 | 다른 하나는 목록에서 사각형만 골라 그리는 DrawSquaresOnly 다.
ko042 | SAME | ko042 | 1.00 | 앞의 함수에서는 그려야 할 도형을 빠뜨린 셈이고, 뒤의 함수에서는 사각형만 그린다는 약속을 지킨 셈이다.
ko043 | SAME | ko043 | 1.00 | 두 함수 모두 실행 중에 도형의 타입을 검사한다.
ko044 | SAME | ko044 | 1.00 | 그 검사를 보고 개방–폐쇄 원칙 위반을 판정하려면, 먼저 새 도형이 들어왔을 때 함수가 무엇을 해야 하는지 알아야 한다.
ko045 | SAME | ko045 | 1.00 | 이름이나 주변 코드에 단서가 있을 수 있다.
ko046 | SAME | ko046 | 1.00 | 그런 단서만으로 판단이 서지 않을 때는, 판정에 필요한 요구가 검토자에게 어디까지 주어졌는지가 중요해진다.
ko047 | SAME | ko047 | 1.00 | · · 아카이브 감사에서는 분석 단위를 세 가지로 나눴다.
ko048 | SAME | ko048 | 1.00 | 참조 코드 쌍은 위반 예시와 그에 대응하는 수정 예시로 이루어진다.
ko049 | SAME | ko049 | 1.00 | 저장 응답 행에는 제출 코드, 프롬프트, 응답이 들어 있다.
ko050 | SAME | ko050 | 1.00 | 각 프롬프트에서 정확히 한 번 나타나는 제출 코드를 같은 자리표시자로 바꿔 프롬프트 템플릿을 만들었다.
ko051 | SAME | ko053 | 1.00 | 저장 기록의 제출 코드는 모든 참조 쌍의 수정 전·후 소스와 대조했다.
ko052 | SAME | ko054 | 1.00 | 원문 그대로 비교하고, 문자열 양끝의 공백을 제거한 뒤 다시 비교했다.
ko053 | SAME | ko055 | 1.00 | 이후 분석에서 프롬프트의 지시를 설명할 때는 저장 기록을, 수정 전후의 선언을 비교할 때는 참조 쌍을 인용한다.
ko054 | SAME | ko056 | 1.00 | Python 예시에서는 코드의 추상 구문 트리를 읽어 최상위 클래스에 선언된 메서드 이름을 대조했다.
ko055 | SAME | ko057 | 1.00 | 밑줄로 시작하는 이름은 집계 대상에서 제외했다.
ko056 | SAME | ko058 | 1.00 | 이 방법으로 확인할 수 있는 것은 어떤 선언이 수정 전후에 나타나거나 사라졌는지다.
ko057 | SAME | ko059 | 1.00 | 상속을 통해 호출할 수 있는지, 외부에서 사용해 왔는지, 그 사용을 계속 보장하기로 했는지는 각각 다른 증거가 필요하다.
ko058 | SAME | ko060 | 1.00 | 공개 재현 패키지의 코드는 실행하지 않았다.
ko059 | SAME | ko061 | 1.00 | · Pehlivan 등은 언어 모델이 코드 예시에서 SOLID 위반을 식별할 수 있는지 평가했다.
ko060 | SAME | ko062 | 1.00 | 저자들은 먼저 위반 시나리오를 정하고, 생성한 예시 코드를 수정하고 검증했다.
ko061 | SAME | ko063 | 1.00 | 의견이 갈리면 논의해서 참조 라벨을 정했다.
ko062 | SAME | ko064 | 1.00 | 모델의 응답은 저자들이 이렇게 정한 분류를 얼마나 잘 재현하는지에 따라 평가됐다.
ko063 | SAME | ko065 | 1.00 | 저장된 Python EXAMPLE 기록 한 건을 보면, 프롬프트는 다형성으로 처리할 만한 로직에 if-else 나 switch 분기가 반복되는 곳을 찾으라고 한다.
ko064 | SAME | ko066 | 1.00 | 제출된 AreaCalculator 는 실제로 도형의 종류를 확인한 뒤 원과 사각형의 넓이를 각각 계산한다.
ko065 | SAME | ko067 | 1.00 | 검토자는 새 도형을 추가한다면 이 분기에 손댈 수 있다고 추론할 수 있다.
ko066 | SAME | ko068 | 1.00 | 그 도형을 추가하는 일이 실제 요구인지, 사각형의 너비를 직접 읽는 호출을 계속 지원해야 하는지는 프롬프트의 지시문에서 정해 주지 않는다.
ko067 | NEW | ko013 | 0.10 | 개방–폐쇄 원칙 자료는 참조 쌍 48개와 저장 응답 768건이다.
ko068 | NEW | ko069 | 0.12 | 제출 코드를 가려 얻은 프롬프트 틀은 문자열 기준으로 24개였고, 네 전략 사이에 같은 문자열을 공유한 틀은 없었다.
ko069 | SAME | ko070 | 1.00 | 개별 사례의 변경 요구나 보호할 호출자 계약을 따로 명시한 틀은 없었다.
ko070 | SAME | ko071 | 1.00 | 참조 자료에도 같은 넓이 계산 문제를 사용한 코드 쌍이 있다.
ko071 | SAME | ko072 | 1.00 | 37번 쌍의 수정본은 도형마다 넓이를 구하는 메서드를 두고 Rectangle.get_width 선언을 뺐다.
ko072 | SAME | ko073 | 1.00 | 저장 프롬프트의 코드와 이 참조본은 서로 다른 소스다.
ko073 | SAME | ko074 | 1.00 | 참조본에서 선언이 사라졌다는 사실은 두 버전을 대조하면 알 수 있다.
ko074 | SAME | ko075 | 1.00 | 여기서 넓이만 구하는 호출자에게는 도형을 추가할 때 바뀌는 코드가 중요할 수 있다.
ko075 | SAME | ko076 | 1.00 | 사각형의 너비를 직접 읽어 온 호출자에게는 그 호출의 지원 여부가 중요하다.
ko076 | SAME | ko077 | 1.00 | 어느 쪽이 판정을 좌우하는지 확인하려면, 같은 수정안을 두고 새 요구와 기존 약속을 바꿔 볼 필요가 있다.
ko077 | SAME | ko078 | 1.00 | 프롬프트 예시는 저장 JSONL 13행(ID 12)이다.
ko078 | SAME | ko079 | 1.00 | 참조 쌍 37번은 별도의 ground truth JSON 위치다.
ko079 | SAME | ko080 | 1.00 | · · · 마이어가 새 자료 유형을 추가하는 사례를 바탕으로 작은 도서관 목록 프로그램을 만들었다.
ko080 | SAME | ko081 | 1.00 | 이 수정안은 기술보고서를 처리하는 모듈을 추가한다.
ko081 | SAME | ko082 | 1.00 | 기존 소스 파일 두 개는 바이트 단위로 동일하다.
ko082 | SAME | ko083 | 1.00 | 책 출력의 접두어는 book 에서 BOOK 으로 바뀐다.
ko083 | SAME | ko084 | 1.00 | 기술보고서 출력은 성공하고 정오표 요청은 여전히 거절된다.
ko084 | SAME | ko085 | 1.00 | 네 조건에서 수정안, 허용된 편집 범위와 실행 관찰값을 고정했다.
ko085 | SAME | ko086 | 1.00 | 새 요구는 기술보고서만 지원하거나, 기술보고서와 정오표를 둘 다 지원하는 것이다.
ko086 | SAME | ko087 | 1.00 | 기존 계약은 학술지와 학회록의 출력, 그리고 별개의 미지원 자료 유형을 거절하는 동작을 공통으로 보호한다.
ko087 | SAME | ko088 | 1.00 | 이 비교에서는 새 요구와 기존 계약을 모두 만족하는 수정안을 승인한다.
ko088 | SAME | ko099 | 1.00 | 모든 행에서 기존 파일과 패치, 시험 입력과 관찰값, 허용된 파일 추가 경계를 동일하게 둔다.
ko089 | SAME | ko100 | 1.00 | 좁은 계약은 저널·학회 자료와 미지원 종류의 거절을 보호한다.
ko090 | SAME | ko089 | 1.00 | 기술보고서만 필요하고 책 표기까지 보호하지 않을 때 이 수정안은 승인된다.
ko091 | SAME | ko090 | 1.00 | 정오표를 요구하면 새 요구를 충족하지 못한다.
ko092 | SAME | ko091 | 1.00 | 새 모듈만 추가하는 별도 구현이 두 자료 유형을 모두 지원하면서 책 표기를 비롯한 모든 보호 동작을 유지했으므로, 같은 편집 범위 안에서 네 조건의 요구와 계약은 모두 충족 가능하다.
ko093 | SAME | ko092 | 1.00 | 정오표가 필수라는 사실을 알면 책 표기 계약을 확인하기 전에도 이 수정안을 거절할 수 있다.
ko094 | SAME | ko093 | 1.00 | 기술보고서만 필요하다는 사실을 알 때는 책 표기까지 보장했는지에 따라 결론이 갈린다.
ko095 | SAME | ko094 | 1.00 | 이렇게 보면 검토자는 어떤 정보가 빠졌는지에 더해, 어떤 질문에 답하면 결정을 내릴 수 있는지도 알 수 있다.
ko096 | SAME | ko095 | 1.00 | 현재 증거와 양립하는 명세들이 모두 같은 판정을 내놓으면 그 증거만으로도 결정을 내릴 수 있다.
ko097 | SAME | ko096 | 1.00 | 두 명세가 서로 다른 판정을 내놓는데 검토자가 받는 입력은 같다면, 하나의 승인 또는 거절로 둘을 모두 맞힐 수 없다.
ko098 | SAME | ko097 | 1.00 | 이 경우 검토자는 각 조건에서의 결론을 따로 밝히거나, 두 명세를 구별할 사실을 확인할 때까지 보류할 수 있다.
ko099 | SAME | ko098 | 1.00 | 이 논증은 양립하는 명세가 적어도 하나 있고 실제 명세가 그 집합에 속한다는 전제에서 성립한다.
ko100 | NEW | ko088 | 0.13 | · §5에서는 주어진 수정안이 요구와 계약을 만족하는지 확인했다.
ko101 | NEW | ko111 | 0.07 | 이번에는 그런 수정안을 어디에 둘 수 있는지 비교한다.
ko102 | NEW | ko082 | 0.09 | 세 비교에서 기존 소스 파일의 수정 수를 세고, 각 후보의 기능과 기존 동작을 확인했다.
ko103 | SAME | ko106 | 1.00 | 그 예측을 시험하기 위해 도형 사례로 돌아가 보자.
ko104 | SAME | ko107 | 1.00 | 도형마다 그리는 코드를 두면 삼각형은 새 파일 하나로 추가할 수 있었다.
ko105 | SAME | ko108 | 1.00 | 같은 구조에서 원과 사각형에 이름표를 붙이는 새 연산을 넣으려면 기존 도형 파일 두 개를 고쳐야 했다.
ko106 | SAME | ko109 | 1.00 | 연산마다 파일을 두는 구현에서는 이름표 연산을 새 파일로 넣을 수 있었고, 삼각형을 그리려면 기존 그리기 파일을 고쳐야 했다.
ko107 | SAME | ko110 | 1.00 | 이 비교에서 기존 파일에 손대는 횟수를 줄여 준 것은 어느 한 구조의 일반적인 성질이 아니라, 파일을 나눈 기준과 요구가 바뀐 방향의 관계였다.
ko108 | SAME | ko111 | 1.00 | 이번에는 요구와 기존 호출이 기대하는 동작을 그대로 두고, 어느 파일에 기능을 넣을 수 있는지를 바꿨다.
ko109 | SAME | ko112 | 1.00 | 새 함수는 도형 목록을 받아 입력 순서대로 각 도형을 그린 결과를 대괄호로 감싼다.
ko110 | SAME | ko113 | 1.00 | 항목을 변환하는 코드를 기존 도형 파일이 직접 맡도록 하면, 도형별 구현에서는 원과 사각형 파일을 모두 수정해야 한다고 예측했다.
ko111 | SAME | ko114 | 1.00 | 공용 어댑터가 기존 렌더러의 결과를 감싸도 된다면, 두 구현 모두 새 파일 하나만으로 기능을 제공할 수 있다고 예측했다.
ko112 | SAME | ko115 | 1.00 | 구현 전에 두 예측을 기록한 뒤 네 후보를 실행했다.
ko113 | SAME | ko116 | 1.00 | 네 후보 모두 입력 순서와 중복을 유지했고, 빈 목록과 지원하지 않는 도형을 명세대로 처리했다.
ko114 | SAME | ko117 | 1.00 | 기존 파일을 고친 후보는 도형 파일에 항목 변환을 맡긴 경우뿐이었다.
ko115 | SAME | ko118 | 1.00 | 바뀐 파일은 원과 사각형의 파일 두 개였다.
ko116 | SAME | ko119 | 1.00 | 다른 세 후보에서는 기존 파일의 바이트가 그대로였다.
ko117 | SAME | ko120 | 1.00 | 네 경우 모두 배치 진입점을 새 파일 하나에 두었다.
ko118 | SAME | ko121 | 1.00 | 그림 1의 왼쪽은 바라는 기능을 따로 바꿨을 때, 오른쪽은 같은 기능에 허용된 구현 경로만 바꿨을 때의 결과다.
ko119 | NEW | ko109 | 0.06 | A는 삼각형 추가와 이름표 연산 추가를 비교한다.
ko120 | NEW | ko132 | 0.19 | B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다.
ko121 | NEW | ko133 | 0.44 | B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.
ko122 | SAME | ko122 | 1.00 | · · · · 공용 어댑터를 허용한다는 조건은 호출자가 그 모듈을 실제로 사용할 수 있다는 뜻인가?
ko123 | SAME | ko123 | 1.00 | 다음 비교에서는 기존 원과 사각형의 기본 출력은 그대로 두고, 선택적으로 결과를 대괄호로 감싸도록 했다.
ko124 | SAME | ko124 | 1.00 | 새 모듈로 호출할 수 있을 때는 두 배치 모두 기존 파일을 고치지 않았다.
ko125 | SAME | ko125 | 1.00 | 같은 모듈을 추가한 채 원래 함수에 새 옵션을 넘기면, 원래 함수는 그 인자를 받지 못했다.
ko126 | SAME | ko126 | 1.00 | 원래 함수로 기능을 제공한 후보는 연산별 배치에서 기존 파일 하나, 도형별 배치에서 둘을 수정했다.
ko127 | SAME | ko127 | 1.00 | 처음부터 외부 변환 함수를 불러올 수 있게 해 둔 별도 기준선에서는 원래 함수로 호출해도 새 파일 하나만 추가하면 됐다.
ko128 | NEW | ko130 | 0.07 | 확장 지점은 세 번째 행의 기준선에 이미 있었다.
ko129 | NEW | ko042 | 0.05 | 같은 어댑터를 추가해도 기존 함수에서는 옵션을 쓸 수 없었던 대조 실행을 포함했다.
ko130 | SAME | ko128 | 1.00 | · 어디에 파일을 놓아도 되는지 알면 후보를 만들 수 있다.
ko131 | SAME | ko129 | 1.00 | 그 후보가 기존 호출에도 새 기능을 전달할 수 있는지 알려면, 실행 중에 그 코드까지 도달하는 경로가 있어야 한다.
ko132 | SAME | ko130 | 1.00 | 미리 설치된 확장 지점은 그 경로를 만들고, 표 3의 마지막 행은 그 지점이 이미 있던 상태에서의 추가 변경을 센다.
ko133 | SAME | ko131 | 1.00 | 독립적으로 작성한 요구에 대해서도 어느 경로가 작동할지 미리 예측하려면 별도의 평가가 필요하다.
ko134 | SAME | ko140 | 1.00 | 도형을 그리는 함수에 개방–폐쇄 원칙을 적용하려면 먼저 어떤 순서로 그려야 하고 누가 그 순서를 맡는지 알아야 한다.
ko135 | SAME | ko141 | 1.00 | 코드 리뷰에서도 같은 정보가 판정을 가른다.
ko136 | SAME | ko142 | 1.00 | 저장 프롬프트에서 확인한 분류 지시는 벤치마크의 참조 라벨을 맞히는 데 쓰인다.
ko137 | SAME | ko143 | 1.00 | 실제 수정안의 수용 여부를 판단할 때는 새 요구와 기존 호출자에게 보장한 동작을 함께 살펴야 한다.
ko138 | SAME | ko144 | 1.00 | 같은 도서관 수정안도 이 조건에 따라 승인되거나 거절됐다.
ko139 | SAME | ko145 | 1.00 | 정오표가 필수라는 사실만으로 거절을 결정할 수 있었고, 기술보고서만 요구할 때는 책 표기 계약을 알아야 했다.
ko140 | SAME | ko146 | 1.00 | 설계를 비교할 때는 수정안이 해당 호출자에게 도달하는지도 따져야 한다.
ko141 | SAME | ko147 | 1.00 | 도형 예제에서는 추가 모듈을 호출할 수 있는지, 기존 진입점에 확장 지점이 있는지에 따라 기존 파일을 그대로 둘 수 있는 후보가 달라졌다.
ko142 | SAME | ko148 | 1.00 | 검토 의견에 새 요구와 보호할 계약, 적용되는 호출 경로를 명시하면 개발자는 거절 이유를 확인하거나 판정에 필요한 다음 사실을 물을 수 있다.
ko143 | SAME | ko149 | 1.00 | 이 글이 확인한 범위는 한 벤치마크의 저장 자료와 직접 구성한 수정안이다.
ko144 | SAME | ko150 | 1.00 | §3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다.
ko145 | SAME | ko151 | 1.00 | §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다.
ko146 | SAME | ko152 | 1.00 | 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다.
ko147 | SAME | ko153 | 1.00 | 그림 1의 소스와 출력 위치는 그림 캡션에 있다.
Summary ko: same 137; edited 0; new 10.

### EN (163 sentences; prior 167)
en001 | SAME | en001 | 1.00 | In 1996, Robert Martin described a function that took a list of shapes and drew them one by one.
en002 | SAME | en002 | 1.00 | A triangle could be added without touching the function, provided the triangle supplied its own drawing operation.
en003 | SAME | en003 | 1.00 | Martin then changed the requirement.
en004 | SAME | en004 | 1.00 | Every circle now had to be drawn before any square.
en005 | SAME | en005 | 1.00 | Give the same function a list with a square at the front and it still draws the square first.
en006 | SAME | en006 | 1.00 | Where should the edit go?
en007 | SAME | en007 | 1.00 | If callers agree to sort the list before passing it in, the drawing function can stay as it is.
en008 | SAME | en008 | 1.00 | If the function is responsible for putting circles first regardless of input order, its current implementation falls short.
en009 | SAME | en009 | 1.00 | The source tells us that the function does no sorting.
en010 | SAME | en010 | 1.00 | Rejecting a patch on those grounds also requires knowing who was meant to sort the list.
en011 | SAME | en011 | 1.00 | A review comment that says only “open–closed principle violation” leaves the developer to ask which obligation the function was supposed to meet.
en012 | SAME | en012 | 1.00 | How does that obligation reach the model in a classification task?
en013 | SAME | en013 | 1.00 | One benchmark for identifying SOLID violations evaluates model responses against labels established by its authors.
en014 | SAME | en014 | 1.00 | We examine its saved prompts for the open–closed principle.
en015 | SAME | en015 | 1.00 | In the templates we inspected, the case-specific change request and the commitment to existing callers were not stated separately.
en016 | SAME | en016 | 1.00 | The code or an accompanying scenario may offer clues.
en017 | SAME | en017 | 1.00 | Using the verdict to decide whether to take an edit requires checking what obligations those clues establish.
en018 | SAME | en018 | 1.00 | We test whether those obligations can decide the outcome by placing the same patch under different demands and contracts.
en019 | SAME | en019 | 1.00 | In one condition, a failure to meet the new requirement suffices to reject the edit.
en020 | SAME | en020 | 1.00 | In another, the new requirement is met and the decision turns on what existing callers were promised.
en021 | SAME | en021 | 1.00 | For the developer receiving the review, that difference determines what to do next.
en022 | SAME | en022 | 1.00 | The evidence may already warrant rejection, or the decision may depend on a fact the reviewer still needs to establish.
en023 | SAME | en023 | 1.00 | The same premises matter when asking which edits are available in the first place.
en024 | SAME | en024 | 1.00 | A follow-up comparison in the drawing fixture keeps the feature fixed and varies the caller’s route to see when a candidate can leave the existing files intact.
en025 | SAME | en025 | 1.00 | · · At the start of his 1996 article, Martin attributes the open–closed principle to Bertrand Meyer and cites page 23 of the 1988 first edition.
en026 | SAME | en026 | 1.00 | In Meyer's account, a module is closed when other modules can use it on the basis of a stable description.
en027 | SAME | en027 | 1.00 | Reading the implementation may tell a client how the module happens to behave.
en028 | SAME | en028 | 1.00 | The description tells the client which behavior it can continue to rely on.
en029 | SAME | en029 | 1.00 | Meyer makes the problem concrete by adding technical reports to a library program.
en030 | SAME | en030 | 1.00 | If existing modules handle publication types by distinguishing them one by one, adding even one type can require changes or recompilation in those modules.
en031 | SAME | en031 | 1.00 | Where the new functionality goes matters because that choice determines which existing users of the module have more work to do.
en032 | SAME | en032 | 1.00 | Martin assigned sorting to DrawAllShapes .
en033 | SAME | en033 | 1.00 | The function needed a way to compare two shapes and decide which to draw first.
en034 | SAME | en034 | 1.00 | In the first implementation, the circle inspected the other shape.
en035 | SAME | en035 | 1.00 | Circle::Precedes put the circle first if the other shape was a square.
en036 | SAME | en036 | 1.00 | When a new kind of shape arrived and its place relative to a circle had to be decided, the code making that decision already lived inside Circle .
en037 | SAME | en037 | 1.00 | Martin moved the ordering of shape types into a table.
en038 | SAME | en038 | 1.00 | The comparison function obtains the two shapes’ runtime type names and looks up their positions in the table.
en039 | SAME | en039 | 1.00 | If squares now have to be drawn before circles, the two entries can trade places.
en040 | SAME | en040 | 1.00 | A request to draw smaller shapes first by area calls for a different change.
en041 | SAME | en041 | 1.00 | The table records the order of shape types and carries no information about the area of an individual shape.
en042 | SAME | en042 | 1.00 | Which part of the program can stay as it is depends on the change being requested.
en043 | SAME | en043 | 1.00 | The same question arises with type checks.
en044 | SAME | en044 | 1.00 | Later in the article, Martin puts two functions that use dynamic_cast side by side.
en045 | SAME | en045 | 1.00 | One, DrawAllShapes , recognizes circles and squares and draws them.
en046 | SAME | en046 | 1.00 | A triangle falls through both branches.
en047 | SAME | en047 | 1.00 | The other, DrawSquaresOnly , selects squares from a list and draws them.
en048 | SAME | en048 | 1.00 | A triangle goes undrawn there as well.
en049 | SAME | en049 | 1.00 | In the first function, a shape that should have been drawn is skipped.
en050 | SAME | en050 | 1.00 | In the second, skipping it is part of what the function promises to do.
en051 | SAME | en051 | 1.00 | Both functions inspect a shape’s type at runtime.
en052 | SAME | en052 | 1.00 | To treat that check as evidence of an Open–Closed Principle violation, a reviewer first needs to know what the function owes a caller who supplies a new kind of shape.
en053 | SAME | en053 | 1.00 | A name or the surrounding code may offer a clue.
en054 | SAME | en054 | 1.00 | Where those clues leave the obligation open, the verdict depends on what the reviewer was told about the required behavior.
en055 | SAME | en055 | 1.00 | · · The archive audit uses three units.
en056 | SAME | en056 | 1.00 | A reference pair contains a violation example and its corresponding revision.
en057 | SAME | en057 | 1.00 | A saved response record contains the submitted code, the prompt, and the recorded response.
en058 | SAME | en058 | 1.00 | We recovered each prompt template by replacing the single exact occurrence of the submitted code with a common placeholder.
en059 | SAME | en061 | 1.00 | We compared every saved submission with the source on both sides of every reference pair.
en060 | SAME | en062 | 1.00 | We compared the original strings and repeated the comparison after trimming whitespace from both ends.
en061 | SAME | en063 | 1.00 | Neither comparison yielded an exact match.
en062 | SAME | en064 | 1.00 | We use saved records to describe the prompt instructions and reference pairs to compare declarations across revisions.
en063 | SAME | en065 | 1.00 | For the Python pairs, we parsed the code and compared method names declared in top-level classes.
en064 | SAME | en066 | 1.00 | We excluded names beginning with an underscore.
en065 | SAME | en067 | 1.00 | The comparison identifies declarations that appear or disappear between versions.
en066 | SAME | en068 | 1.00 | Inherited availability, actual use by callers, and commitments to preserve that use require additional evidence.
en067 | SAME | en069 | 1.00 | We executed no code from the replication archive.
en068 | SAME | en070 | 1.00 | · Pehlivan et al. evaluated whether language models could identify SOLID violations in code examples.
en069 | SAME | en071 | 1.00 | The authors specified violation scenarios, then refined and verified the generated code examples.
en070 | SAME | en072 | 1.00 | They resolved disagreement about the reference labels through discussion.
en071 | SAME | en073 | 1.00 | They assessed model responses against the resulting classifications.
en072 | SAME | en074 | 1.00 | One saved Python record from the EXAMPLE condition directs the reviewer to look for repeated if-else or switch branches where polymorphism would fit.
en073 | SAME | en075 | 1.00 | Its submitted AreaCalculator checks a shape’s type before calculating the area of a circle or rectangle.
en074 | SAME | en076 | 1.00 | A reviewer can infer that adding a shape might require editing that branch.
en075 | SAME | en077 | 1.00 | The instructions leave open whether anyone has requested such an extension and whether callers that read a rectangle’s width must still be supported.
en076 | NEW | en059 | 0.42 | The OCP material contains 48 reference pairs and 768 saved responses.
en077 | NEW | en060 | 0.39 | Masking the submitted code yielded 24 exact distinct prompt templates, with no template string shared across the four strategies.
en078 | SAME | en079 | 1.00 | None separately states a change request or protected caller contract for an individual case.
en079 | SAME | en080 | 1.00 | A separate reference pair uses the same area-calculation setup.
en080 | SAME | en081 | 1.00 | In pair 37, the revised code moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en081 | SAME | en082 | 1.00 | This pair and the code in the saved prompt are distinct source texts.
en082 | SAME | en083 | 1.00 | Comparing the two versions of the reference pair establishes that a declaration disappeared.
en083 | SAME | en084 | 1.00 | For a caller that only calculates area, the relevant question may be what has to change when a new shape is added.
en084 | SAME | en085 | 1.00 | For a caller that reads a rectangle’s width directly, continued support for the call matters.
en085 | SAME | en086 | 1.00 | To see which premise can settle the verdict, we hold a patch fixed and vary the requested extension and the obligations to existing callers.
en086 | SAME | en087 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en087 | SAME | en088 | 1.00 | The saved prompt is on JSONL line 13 (record ID 12).
en088 | SAME | en089 | 1.00 | Reference pair 37 is in a separate ground-truth JSON file. 768 counts saved records.
en089 | SAME | en090 | 1.00 | · · · We built a small library catalog based on Meyer's example of adding a publication type.
en090 | SAME | en091 | 1.00 | The patch adds a module that handles technical reports.
en091 | SAME | en092 | 1.00 | The two existing source files remain byte-for-byte identical.
en092 | SAME | en093 | 1.00 | The prefix in the rendering of an existing book changes from book to BOOK .
en093 | SAME | en094 | 1.00 | Technical reports render successfully and requests for errata are still rejected.
en094 | SAME | en095 | 1.00 | We hold the patch, the permitted edit boundary, and the observed execution results fixed across four conditions.
en095 | SAME | en096 | 1.00 | The new request calls for technical reports alone or for both technical reports and errata.
en096 | SAME | en097 | 1.00 | Both client contracts protect the rendering of journals and proceedings and the rejection of a separate unsupported publication type.
en097 | SAME | en098 | 1.00 | The broader contract also protects the original book prefix.
en098 | SAME | en099 | 1.00 | We accept the patch in this comparison when it meets the new request and preserves the existing contract.
en099 | SAME | en112 | 1.00 | Two independent conditions for the same patch.
en100 | SAME | en100 | 1.00 | The patch is acceptable when only reports are needed and the book prefix is outside the contract.
en101 | SAME | en101 | 1.00 | Requiring errata causes it to fail the new request.
en102 | SAME | en102 | 1.00 | Protecting the book prefix causes it to fail the existing contract.
en103 | SAME | en103 | 1.00 | A separate implementation adds only a new module, handles both new types, and preserves every protected outcome, including the original book prefix.
en104 | SAME | en104 | 1.00 | The demand and contract are therefore jointly satisfiable in all four conditions under the same edit boundary.
en105 | SAME | en105 | 1.00 | Learning that errata are required suffices to reject this patch even before the book contract is known.
en106 | SAME | en106 | 1.00 | Learning that only technical reports are required leaves the decision open until we know whether the prefix was promised.
en107 | SAME | en107 | 1.00 | The reviewer can thus identify which outstanding question would settle the decision.
en108 | SAME | en108 | 1.00 | If all specifications compatible with the available evidence yield the same verdict, that evidence suffices for the decision.
en109 | SAME | en109 | 1.00 | If two specifications yield different verdicts and the reviewer receives identical input in both, any single binary verdict fails to agree with at least one specification.
en110 | SAME | en110 | 1.00 | The reviewer can report conditional decisions or defer until a distinguishing fact is known.
en111 | SAME | en111 | 1.00 | This argument assumes that the compatible set is nonempty and contains the actual specification.
en112 | NEW | en099 | 0.17 | · Section 5 asked whether a given patch satisfies the request and contract.
en113 | NEW | en143 | 0.11 | We now ask where such a patch can be placed.
en114 | NEW | en148 | 0.23 | Across three comparisons, we count edited existing source files and check each candidate’s new and legacy behavior.
en115 | SAME | en118 | 1.00 | The drawing example gives us a way to test that prediction.
en116 | SAME | en119 | 1.00 | With drawing code organized by shape, adding a triangle took one new file.
en117 | SAME | en120 | 1.00 | Adding a labeling operation for circles and squares required editing both existing shape files.
en118 | SAME | en121 | 1.00 | In the implementation organized by operation, labeling went into a new file, while drawing a triangle required editing the existing drawing file.
en119 | SAME | en122 | 1.00 | All four patches passed their functional checks.
en120 | SAME | en123 | 1.00 | In this comparison, how many existing files an edit touched depended on how the file boundaries lined up with the requested extension.
en121 | SAME | en124 | 1.00 | We next held the requirement and the legacy caller’s observations fixed and varied where the new behavior could live.
en122 | SAME | en125 | 1.00 | The new function takes a list of shapes and returns their rendered strings, each enclosed in brackets, in input order.
en123 | SAME | en126 | 1.00 | If each shape file had to own its item transformation, we predicted that the shape-organized candidate would have to edit both existing shape files.
en124 | SAME | en127 | 1.00 | If a shared adapter could decorate the result of the existing renderer, we predicted that either layout could provide the feature in one new file.
en125 | SAME | en128 | 1.00 | We recorded the predictions before implementing the candidates and then ran all four.
en126 | SAME | en129 | 1.00 | They preserved input order and repeated items, handled the empty list and unsupported shapes as specified, and preserved the existing circle and square renderings.
en127 | SAME | en130 | 1.00 | The only candidate that changed existing files was the shape-organized implementation under the ownership rule.
en128 | SAME | en131 | 1.00 | It edited the circle and square files.
en129 | SAME | en132 | 1.00 | The other three kept the existing files byte-for-byte.
en130 | SAME | en133 | 1.00 | All four added one file containing the batch entry point.
en131 | SAME | en134 | 1.00 | Figure 1 pairs the earlier change-of-request comparison with this change-of-placement comparison.
en132 | SAME | en148 | 1.00 | Existing source files edited.
en133 | NEW | en120 | 0.24 | Panel A compares adding a triangle with adding a labeling operation.
en134 | EDIT | en150 | 0.60 | Panel B holds the batch-rendering request fixed and varies the placement rule.
en135 | EDIT | en151 | 0.58 | All four candidates in panel B passed the new and legacy behavior checks and added one file each.
en136 | SAME | en135 | 1.00 | · · · · What happens if a caller cannot use the shared adapter?
en137 | SAME | en136 | 1.00 | We kept the default rendering of circles and squares and added an option to enclose the result in brackets.
en138 | SAME | en137 | 1.00 | When callers could use a new module, both layouts left their existing files intact.
en139 | SAME | en138 | 1.00 | With the same module added, calls through the original rendering functions still rejected the new keyword.
en140 | SAME | en139 | 1.00 | The candidates that delivered the option through those functions edited one existing file in the operation layout and two in the shape layout.
en141 | SAME | en140 | 1.00 | In a separate baseline equipped with a hook that could load an external decorator, adding one file sufficed even through the original functions.
en142 | NEW | en152 | 0.28 | Call paths for the new rendering option.
en143 | NEW | en144 | 0.15 | The hook was already present in the last row’s baseline.
en144 | NEW | en138 | 0.22 | The negative control adds the same adapter and finds that the option remains unavailable through the original function.
en145 | SAME | en141 | 1.00 | · Permission to add a file lets a developer write a candidate.
en146 | SAME | en142 | 1.00 | To deliver the change through an existing call, the execution must also be able to reach the new code.
en147 | SAME | en143 | 1.00 | A pre-existing hook supplies such a path.
en148 | SAME | en144 | 1.00 | The last row of Table 3 counts the edits made once that hook was in place.
en149 | SAME | en145 | 1.00 | Predicting which paths will work for independently authored requests requires a separate evaluation.
en150 | SAME | en154 | 1.00 | Applying the open–closed principle to a drawing routine starts with knowing which order the shapes must appear in and who is responsible for that order.
en151 | SAME | en155 | 1.00 | Code review faces the same question about a change and its obligations.
en152 | SAME | en156 | 1.00 | The archived instructions support classification against the benchmark’s reference labels.
en153 | SAME | en157 | 1.00 | Evaluating an actual patch also takes a concrete request and an account of what existing callers were promised.
en154 | SAME | en158 | 1.00 | The same catalog patch was accepted or rejected under different specifications.
en155 | SAME | en159 | 1.00 | A requirement to handle errata sufficed to reject it.
en156 | SAME | en160 | 1.00 | When only technical reports were required, the decision turned on the contract for the book prefix.
en157 | SAME | en161 | 1.00 | Comparing designs adds a question about how the change reaches its callers.
en158 | SAME | en162 | 1.00 | In the drawing fixture, the existence of an additive candidate depended on whether callers could take a new route or reach an extension hook through their original entry point.
en159 | SAME | en163 | 1.00 | A review that specifies the request, the protected contract, and the relevant call path lets a developer check the grounds for rejection or identify the fact still needed to decide.
en160 | SAME | en164 | 1.00 | The evidence here covers the saved records of one benchmark and the patches constructed for these comparisons.
en161 | SAME | en165 | 1.00 | For Sections 3–4 the audit reads the archived JSON and JSONL.
en162 | SAME | en166 | 1.00 | For Sections 5–6 the fixtures run the examples constructed for this study.
en163 | SAME | en167 | 1.00 | The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.
Summary en: same 152; edited 2; new 9.

## v03 · [Notion](https://app.notion.com/p/41bef561cf9281968d9adaf0d0a5ffef)
### KO (113 sentences; prior 147)
ko001 | EDIT | ko001 | 0.50 | 로버트 마틴은 1996년 글에서 도형 목록을 받아 차례로 그리는 함수를 예로 들었다.
ko002 | NEW | ko002 | 0.24 | 삼각형이 자신을 그리는 동작을 제공하면, 그 함수를 고치지 않고도 삼각형을 추가할 수 있었다.
ko003 | NEW | ko005 | 0.42 | 같은 함수에 사각형으로 시작하는 목록을 주면 여전히 사각형부터 그린다.
ko004 | NEW | ko006 | 0.12 | 원을 먼저 그리려면 누가 목록을 정렬해야 할까?
ko005 | EDIT | ko006 | 0.58 | 호출자가 정렬한 목록을 넘기기로 했다면 그리기 함수는 그대로 둘 수 있다.
ko006 | EDIT | ko007 | 0.51 | 어떤 목록을 받아도 함수가 순서를 보장하기로 했다면 지금 코드로는 부족하다.
ko007 | EDIT | ko008 | 0.53 | 소스 코드를 읽으면 함수가 정렬하지 않는다는 사실을 알 수 있다.
ko008 | NEW | ko009 | 0.28 | 그 사실을 개방–폐쇄 원칙(OCP) 위반의 근거로 삼으려면 정렬을 누가 맡았는지도 알아야 한다.
ko009 | NEW | ko022 | 0.07 | 이 글은 그와 같은 전제가 세 가지 판단에 어떻게 쓰이는지 살핀다.
ko010 | NEW | ko143 | 0.14 | 먼저 SOLID 위반 분류 벤치마크의 저장 자료를 조사해 모델에게 주어진 정보의 범위를 확인한다.
ko011 | NEW | ko076 | 0.11 | 이어서 도서관 프로그램의 같은 수정안을 놓고 새 요구와 기존 호출자 계약을 달리하면 승인 여부가 어떻게 달라지는지 비교한다.
ko012 | NEW | ko141 | 0.23 | 마지막으로 도형 예제로 돌아가, 호출자가 이용할 수 있는 경로에 따라 기존 파일을 그대로 둘 수 있는지 살핀다.
ko013 | EDIT | ko024 | 0.69 | · · 마틴은 1996년 글의 첫머리에서 이 원칙을 베르트랑 마이어에게서 가져왔다고 밝히며 1988년 초판 23쪽을 인용한다.
ko014 | NEW | ko025 | 0.27 | 마이어의 설명에서 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 사용할 수 있는 모듈이다.
ko015 | EDIT | ko028 | 0.70 | 도서관 프로그램이 자료의 종류를 하나씩 구별해 처리한다면 기술보고서 한 종류를 추가하는 데도 기존 모듈의 수정이나 재컴파일이 필요할 수 있다.
ko016 | NEW | ko019 | 0.04 | 이때 설계자는 새 동작을 어디에 넣을지와 기존 사용자가 계속 어떤 동작에 의존할 수 있을지를 함께 고려하게 된다.
ko017 | SAME | ko030 | 1.00 | 마틴은 목록을 정렬하는 일을 DrawAllShapes 에 맡겼다.
ko018 | NEW | ko032 | 0.32 | 첫 구현에서는 Circle::Precedes 가 상대 도형을 검사해 사각형이면 원을 앞에 놓았다.
ko019 | NEW | ko033 | 0.35 | 새 도형이 들어왔을 때 원과 그 도형의 순서를 정하는 코드가 이미 Circle 안에 있었다.
ko020 | NEW | ko003 | 0.07 | 마틴은 이어서 도형 종류별 순서를 표로 옮겼다.
ko021 | EDIT | ko035 | 0.51 | 이제 사각형을 원보다 먼저 그리라는 요청에는 표에서 두 항목의 위치를 바꾸면 된다.
ko022 | NEW | ko035 | 0.07 | 개별 도형의 넓이순으로 그리라는 요구를 가정하면 표에 없는 정보가 필요하다.
ko023 | NEW | ko037 | 0.44 | 어느 부분을 그대로 둘 수 있는지는 어떤 변경에 대비하느냐에 달려 있다.
ko024 | NEW | ko026 | 0.06 | 타입 검사가 위반의 근거가 되는지도 함수가 맡은 일에 달려 있다.
ko025 | NEW | ko038 | 0.36 | 글의 뒷부분에서 마틴은 dynamic_cast 를 쓰는 두 함수를 새로 제시한다.
ko026 | EDIT | ko041 | 0.53 | 원과 사각형을 가려 그리는 DrawAllShapes 와 목록에서 사각형만 골라 그리는 DrawSquaresOnly 다.
ko027 | NEW | ko040 | 0.16 | 두 함수에 삼각형을 넣으면 어느 쪽도 그리지 않는다.
ko028 | NEW | ko042 | 0.13 | 모든 도형을 그리기로 한 함수에서는 빠진 출력이고, 사각형만 그리기로 한 함수에서는 약속한 동작이다.
ko029 | NEW | ko013 | 0.13 | 이 차이를 검토자가 입력에서 알아볼 수 있는지 확인하기 위해 실제로 저장된 분류 프롬프트를 살펴봤다.
ko030 | NEW | ko049 | 0.15 | 참조 코드 쌍에는 위반 예시와 그 수정 예시가 들어 있고, 저장 응답에는 모델에 제출된 코드와 프롬프트, 기록된 응답이 들어 있다.
ko031 | NEW | ko050 | 0.25 | 프롬프트 틀은 저장 프롬프트에 정확히 한 번 나오는 제출 코드를 공통 자리표시자로 치환해 얻었다.
ko032 | EDIT | ko051 | 0.56 | 저장 응답의 제출 코드를 모든 참조 쌍의 수정 전·후 소스와 대조했다.
ko033 | NEW | ko052 | 0.28 | 각 문자열을 그대로 비교한 뒤 양끝 공백을 제거해 다시 비교했다.
ko034 | NEW | ko054 | 0.19 | Python 참조 쌍은 구문 트리로 파싱해 최상위 클래스의 메서드 선언 이름을 비교했다.
ko035 | NEW | ko057 | 0.03 | 상속에 따른 호출 가능성, 실제 사용 여부, 보장의 범위는 별도 근거가 필요한 질문이다.
ko036 | NEW | ko145 | 0.12 | 이 연구에서 작성한 도서관·도형 재현은 §5와 §6에서 정한 조건으로 실행했다.
ko037 | EDIT | ko058 | 0.57 | ZIP 안의 공개 재현 패키지 코드는 실행하지 않았다.
ko038 | NEW | ko047 | 0.06 | 아카이브 식별 정보와 확인 명령은 부록 A에 있다.
ko039 | NEW | ko060 | 0.18 | · Pehlivan 등은 위반 시나리오를 정하고, 생성한 코드 예시를 수정·검증한 뒤 의견이 갈린 사례의 참조 라벨을 논의로 정했다.
ko040 | NEW | ko012 | 0.32 | SOLID 위반을 식별하는 모델 응답은 그 라벨과 대조했다.
ko041 | NEW | ko067 | 0.38 | OCP에 해당하는 아카이브에는 참조 쌍 48개와 저장 응답 768건이 있다.
ko042 | NEW | ko068 | 0.25 | 저장 프롬프트에서 제출 코드를 가렸을 때 서로 다른 문자열 24개가 남았고, 네 전략 사이에 동일한 틀은 없었다.
ko043 | NEW | ko069 | 0.42 | 각 사례의 변경 요구나 기존 호출자 계약을 따로 밝힌 틀은 없었다.
ko044 | NEW | ko063 | 0.28 | 저장된 Python EXAMPLE 지시는 다형성으로 처리할 만한 반복 분기를 찾도록 한다.
ko045 | EDIT | ko064 | 0.61 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko046 | NEW | ko065 | 0.16 | 그 분기를 보면 새 도형을 추가할 때 어디에 손댈지 짐작할 수 있다.
ko047 | NEW | ko066 | 0.42 | 새 도형 추가가 실제 요청인지, 사각형의 너비를 직접 읽는 호출을 계속 지원해야 하는지는 이 지시문에서 확인되지 않는다.
ko048 | NEW | ko071 | 0.32 | 별도의 참조 쌍 37번은 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko049 | NEW | ko051 | 0.08 | 원본 문자열과 양끝 공백을 제거한 문자열을 대조했을 때, 저장된 제출 코드와 참조 쌍의 어느 쪽도 일치하지 않았다.
ko050 | NEW | ko136 | 0.06 | 따라서 여기서 근거로 삼는 것은 참조 쌍에서 확인한 선언의 변화다.
ko051 | NEW | ko009 | 0.09 | 그 변화가 수정안을 거절할 이유가 되려면 호출자가 너비를 읽는 동작까지 보장받았는지 확인해야 한다.
ko052 | NEW | ko076 | 0.06 | 다음 절에서는 바로 그 보장을 바꾸면 같은 수정안의 판정이 달라지는지 본다.
ko053 | SAME | ko077 | 1.00 | 프롬프트 예시는 저장 JSONL 13행(ID 12)이다.
ko054 | SAME | ko078 | 1.00 | 참조 쌍 37번은 별도의 ground truth JSON 위치다.
ko055 | EDIT | ko079 | 0.51 | · · · 마이어의 예를 바탕으로 작은 도서관 목록 프로그램을 만들었다.
ko056 | EDIT | ko080 | 0.83 | 검토할 수정안은 기술보고서를 처리하는 모듈을 추가한다.
ko057 | EDIT | ko081 | 0.62 | 기존 소스 파일 두 개는 바이트 단위로 그대로다.
ko058 | NEW | ko083 | 0.28 | 실행하면 기술보고서는 출력되고 정오표는 여전히 거절된다.
ko059 | EDIT | ko082 | 0.90 | 기존 책 출력의 접두어는 book 에서 BOOK 으로 바뀐다.
ko060 | NEW | ko084 | 0.11 | 수정안과 실행 결과, 새 모듈을 추가할 수 있는 편집 범위를 고정했다.
ko061 | NEW | ko085 | 0.35 | 새 요구는 기술보고서만 지원하는 경우와 정오표까지 지원하는 경우로 나눴다.
ko062 | EDIT | ko086 | 0.65 | 두 계약은 모두 학술지와 학회록의 출력, 그리고 별개의 미지원 자료 유형을 거절하는 동작을 보호한다.
ko063 | NEW | ko087 | 0.11 | 표 2의 승인은 새 요구와 보호할 계약을 모두 충족한 경우다.
ko064 | NEW | ko090 | 0.34 | 기술보고서만 필요하고 책 접두어를 보호하지 않는 경우에 승인된다.
ko065 | NEW | ko093 | 0.36 | 정오표가 필수라는 사실을 알면 책 접두어 계약을 모르더라도 거절할 수 있다.
ko066 | NEW | ko094 | 0.40 | 기술보고서만 필요하다는 사실을 알 때는 책 접두어를 보장했는지가 결론을 가른다.
ko067 | NEW | ko092 | 0.14 | 별도로 만든 수정안은 같은 편집 범위에서 새 모듈 하나를 추가해 두 자료 유형을 처리하고 모든 보호 동작을 지켰다.
ko068 | NEW | ko096 | 0.11 | 판정에 필요한 정보가 일부만 주어지면, 그 정보와 양립하는 명세들을 비교할 수 있다.
ko069 | NEW | ko096 | 0.17 | 모든 명세가 같은 판정을 내리면 그 판정을 내릴 수 있다.
ko070 | NEW | ko098 | 0.18 | 서로 다른 판정이 나오면 조건마다 결론을 밝히거나, 어느 조건이 실제로 적용되는지 확인할 때까지 보류할 수 있다.
ko071 | NEW | ko099 | 0.26 | 이 논증은 실제 명세가 검토 중인 집합에 들어 있어 그 집합이 비어 있지 않다는 전제에서 성립한다.
ko072 | NEW | ko014 | 0.02 | 부록 A에는 이번 사례에서 검토한 정보 공개 조건 아홉 개가 있다.
ko073 | NEW | ko100 | 0.19 | · §5에서 거절된 것은 주어진 수정안이다.
ko074 | NEW | ko101 | 0.27 | 이제 도형 예제로 돌아가, 같은 요청을 처리하는 구현을 어디에 둘 수 있는지 비교한다.
ko075 | NEW | ko102 | 0.11 | 세 비교에서 실행한 후보들의 기존 파일 수정 수를 센다.
ko076 | NEW | ko106 | 0.14 | 도형별 배치에서는 삼각형을 새 파일 하나로 추가했고, 이름표 연산을 추가할 때는 원과 사각형의 파일을 고쳤다.
ko077 | NEW | ko106 | 0.16 | 연산별 배치에서는 반대로 삼각형을 추가할 때 그리기 파일을 고쳤고, 이름표 연산은 새 파일에 뒀다.
ko078 | NEW | ko121 | 0.10 | 네 수정안이 모두 기능 검사를 통과했지만 기존 파일을 덜 건드리는 배치는 요구에 따라 달랐다(그림 1A).
ko079 | NEW | ko120 | 0.08 | 두 번째 비교에서는 같은 배치 렌더링 함수를 추가했다.
ko080 | NEW | ko109 | 0.42 | 이 함수는 도형 목록을 받아 각 렌더링 결과를 대괄호로 감싼다.
ko081 | NEW | ko110 | 0.13 | 도형별 배치에서 변환을 각 도형 파일이 맡아야 하면 원과 사각형 파일을 고친다.
ko082 | NEW | ko111 | 0.36 | 공용 어댑터를 허용하면 두 배치 모두 새 파일 하나로 기능을 제공할 수 있다고 예측했다.
ko083 | NEW | ko113 | 0.40 | 실행한 네 후보는 모두 입력 순서와 중복을 보존하고 빈 목록과 미지원 도형을 명세대로 처리했다.
ko084 | NEW | ko115 | 0.14 | 각 후보는 원과 사각형의 기존 렌더링을 유지했다.
ko085 | NEW | ko114 | 0.19 | 기존 파일 두 개를 고친 것은 도형 파일이 변환을 맡은 후보뿐이었다.
ko086 | NEW | ko117 | 0.09 | 네 후보 모두 새 파일 하나를 추가했다(그림 1B).
ko087 | SAME | ko119 | 1.00 | A는 삼각형 추가와 이름표 연산 추가를 비교한다.
ko088 | SAME | ko120 | 1.00 | B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다.
ko089 | SAME | ko121 | 1.00 | B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.
ko090 | NEW | ko123 | 0.10 | · · · · 세 번째 비교에서는 배치 함수 대신 기존 렌더링의 결과 하나를 선택적으로 감싸는 옵션을 사용했다.
ko091 | NEW | ko124 | 0.21 | 새 모듈을 호출할 수 있는 경우에는 두 배치가 기존 파일을 그대로 뒀다.
ko092 | NEW | ko125 | 0.32 | 같은 모듈을 추가한 상태에서 기존 함수에 bracketed=True 를 넘기면 함수는 그 인자를 받지 못했다.
ko093 | NEW | ko126 | 0.39 | 기존 함수로 옵션을 제공한 후보는 연산별 배치에서 파일 하나, 도형별 배치에서 두 개를 고쳤다.
ko094 | NEW | ko127 | 0.15 | 기존 함수가 외부 변환 모듈을 불러올 수 있도록 이미 구성된 별도 기준선에서는 두 배치 모두 새 파일 하나를 추가해 기존 호출 경로로 옵션을 제공했다(표 3).
ko095 | SAME | ko128 | 1.00 | 확장 지점은 세 번째 행의 기준선에 이미 있었다.
ko096 | SAME | ko129 | 1.00 | 같은 어댑터를 추가해도 기존 함수에서는 옵션을 쓸 수 없었던 대조 실행을 포함했다.
ko097 | NEW | ko104 | 0.07 | · 새 파일을 추가할 수 있어도 그 파일이 실행되려면 호출자가 쓸 수 있는 경로가 필요하다.
ko098 | NEW | ko132 | 0.24 | 표 3의 마지막 행은 확장 지점이 이미 있는 상태에서 이후에 고친 파일만 센다.
ko099 | NEW | ko058 | 0.03 | 여기에 든 수정 수는 실행한 후보에 관한 관찰이다.
ko100 | NEW | ko133 | 0.19 | 독립적으로 작성한 요구에서도 어떤 경로가 작동할지 예측할 수 있는지, 파일 수정 수가 실제 유지보수 부담과 어떻게 연결되는지는 남은 질문이다.
ko101 | NEW | ko009 | 0.07 | 서론의 그리기 함수가 잘못됐는지는 정렬을 누가 맡았는지에 달려 있었다.
ko102 | NEW | ko012 | 0.26 | 벤치마크는 모델의 응답을 참조 라벨과 대조해 분류 성능을 잰다.
ko103 | NEW | ko137 | 0.10 | 그 판정을 구체적인 수정안에 적용하려면 어떤 기능이 필요한지, 어떤 동작을 기존 호출자에게 약속했는지를 확인해야 한다.
ko104 | NEW | ko093 | 0.15 | 도서관 예제에서는 정오표 요구만으로 수정안을 거절할 수 있었다.
ko105 | NEW | ko090 | 0.13 | 기술보고서만 필요한 경우에는 책 접두어 계약이 결론을 갈랐다.
ko106 | NEW | ko022 | 0.18 | 어떤 수정안이 가능한지를 비교할 때는 호출자가 새 동작을 받을 수 있는 경로도 확인해야 한다.
ko107 | NEW | ko142 | 0.06 | 검토 의견으로 변경을 요구하려면 어느 요구나 계약을 근거로 삼았는지, 어느 호출 경로에 적용되는지를 밝힐 수 있어야 한다.
ko108 | NEW | ko142 | 0.12 | 그러면 개발자는 이미 내려진 결론의 근거를 확인하거나, 보류된 판정을 가를 사실을 더 찾을 수 있다.
ko109 | NEW | ko143 | 0.20 | 이 결과는 한 벤치마크의 저장 자료와 여기서 구성해 실행한 후보의 범위에서 성립한다.
ko110 | SAME | ko144 | 1.00 | §3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다.
ko111 | SAME | ko145 | 1.00 | §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다.
ko112 | SAME | ko146 | 1.00 | 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다.
ko113 | SAME | ko147 | 1.00 | 그림 1의 소스와 출력 위치는 그림 캡션에 있다.
Summary ko: same 12; edited 16; new 85.

### EN (124 sentences; prior 163)
en001 | EDIT | en001 | 0.57 | In 1996, Robert Martin described a function that drew the shapes in a list in order.
en002 | EDIT | en002 | 0.74 | A triangle could be added without editing the function if the triangle supplied its own drawing operation.
en003 | NEW | en003 | 0.40 | Martin then introduced a new requirement.
en004 | EDIT | en004 | 0.83 | Every circle had to be drawn before any square.
en005 | EDIT | en005 | 0.57 | Given a list that begins with a square, the same function still draws the square first.
en006 | NEW | en150 | 0.19 | Who is responsible for sorting the list?
en007 | NEW | en007 | 0.45 | If the caller must pass a sorted list, the drawing function can stay as it is.
en008 | NEW | en008 | 0.22 | If the function must produce the required order for any input list, the current code falls short.
en009 | NEW | en009 | 0.46 | A reviewer can see that the function does no sorting.
en010 | NEW | en052 | 0.37 | To take that fact as evidence of an open–closed principle (OCP) violation, the reviewer also needs to know who was meant to sort the shapes.
en011 | NEW | en020 | 0.12 | We examine how such premises enter three decisions.
en012 | NEW | en013 | 0.25 | First, we audit the saved material from a benchmark for classifying SOLID violations to see what information the model received.
en013 | NEW | en085 | 0.29 | Next, we hold a patch to a library program fixed and vary the new requirement and the contract with existing callers.
en014 | NEW | en024 | 0.37 | Finally, we return to the drawing example and vary the paths available to callers to see when a candidate can leave existing files intact.
en015 | EDIT | en025 | 0.61 | · · Martin opens his 1996 article by attributing the principle to Bertrand Meyer and citing page 23 of the 1988 first edition.
en016 | EDIT | en026 | 0.51 | A closed module in Meyer’s account is one that other modules can use on the basis of a stable specification.
en017 | NEW | en030 | 0.42 | If a library program distinguishes publication types one by one, adding technical reports can require edits to existing modules or recompiling them.
en018 | NEW | en031 | 0.23 | The designer must consider both where the new behavior can live and what existing users of the module can continue to rely on.
en019 | SAME | en032 | 1.00 | Martin assigned sorting to DrawAllShapes .
en020 | EDIT | en034 | 0.55 | In the first implementation, Circle::Precedes inspected the other shape and put the circle first if it was a square.
en021 | NEW | en036 | 0.28 | The code that decided how a new shape would rank against a circle already lived in Circle .
en022 | EDIT | en037 | 0.77 | Martin then moved the order of shape types into a table.
en023 | NEW | en039 | 0.15 | Putting squares first now requires swapping two entries.
en024 | NEW | en041 | 0.29 | Ordering individual shapes by area, for example, would require information outside the table.
en025 | EDIT | en042 | 0.62 | Which part of the program can stay as it is depends on the change it must accommodate.
en026 | NEW | en011 | 0.18 | Whether a type check supports a violation finding also depends on the function’s obligation.
en027 | EDIT | en044 | 0.68 | Later in the article, Martin presents two further functions that use dynamic_cast .
en028 | EDIT | en045 | 0.82 | DrawAllShapes recognizes and draws circles and squares.
en029 | EDIT | en047 | 0.74 | DrawSquaresOnly selects squares from the list and draws them.
en030 | NEW | en046 | 0.20 | Given a triangle, both skip it.
en031 | NEW | en050 | 0.15 | A function that promises to draw every shape has omitted an output, while a function that promises to draw squares has met its obligation.
en032 | NEW | en012 | 0.19 | We turn to saved classification prompts to see how much of that kind of obligation the reviewer could establish from the input.
en033 | NEW | en055 | 0.36 | · · We distinguish three units in the archive.
en034 | EDIT | en056 | 0.75 | A reference pair contains a violation example and its revision.
en035 | EDIT | en057 | 0.71 | A saved response record contains the code submitted to the model, its prompt, and the recorded response.
en036 | EDIT | en058 | 0.90 | We recover a prompt template by replacing the single exact occurrence of the submitted code with a common placeholder.
en037 | NEW | en060 | 0.16 | We compare templates as strings.
en038 | EDIT | en059 | 0.52 | We compared each saved submission with the source on both sides of every reference pair, first as stored and again after trimming whitespace from both ends.
en039 | NEW | en063 | 0.40 | For Python reference pairs we parsed the syntax trees and compared names of methods declared in top-level classes, excluding names that begin with an underscore.
en040 | NEW | en065 | 0.29 | The comparison captures declaration changes.
en041 | NEW | en066 | 0.35 | Inherited availability, actual client use, and whether that use was protected each require separate evidence.
en042 | NEW | en162 | 0.24 | We ran the library and drawing fixtures built for this study under the conditions given in Sections 5 and 6.
en043 | EDIT | en067 | 0.69 | We executed no code from the archived replication package.
en044 | NEW | en163 | 0.18 | Appendix A identifies the archive and the commands needed to reproduce the checks.
en045 | EDIT | en069 | 0.50 | · Pehlivan et al. specified violation scenarios and refined and checked the generated examples.
en046 | NEW | en070 | 0.47 | They resolved disagreements about reference labels through discussion, then compared model classifications of SOLID violations with those labels.
en047 | EDIT | en076 | 0.64 | The OCP archive contains 48 reference pairs and 768 saved response records.
en048 | EDIT | en077 | 0.78 | Masking the submitted code yielded 24 distinct template strings, with no exact template shared across the four strategies.
en049 | EDIT | en078 | 0.78 | None of the templates separately states a change request or a protected caller contract for an individual case.
en050 | EDIT | en072 | 0.50 | One saved Python EXAMPLE prompt points the reviewer to repeated branches where polymorphism would fit.
en051 | EDIT | en073 | 0.81 | The submitted AreaCalculator checks the shape type before calculating the area of a circle or rectangle.
en052 | NEW | en083 | 0.18 | The branch suggests where an edit might go if a new shape is added.
en053 | EDIT | en075 | 0.66 | The instruction leaves open whether anyone has requested that change and whether existing calls that read a rectangle’s width must still be supported.
en054 | EDIT | en080 | 0.67 | In a separate reference pair, number 37, the revision moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en055 | NEW | en059 | 0.26 | No saved submission matched either side of the reference pairs in the exact or outer-whitespace-trimmed comparison.
en056 | NEW | en082 | 0.25 | Our evidence for the missing declaration comes from comparing the reference sources.
en057 | NEW | en022 | 0.19 | To argue that its removal warrants rejecting a patch, a reviewer would need to establish that callers were guaranteed access to the width.
en058 | NEW | en018 | 0.20 | We test whether such a guarantee can change the decision for the same patch.
en059 | SAME | en086 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en060 | SAME | en087 | 1.00 | The saved prompt is on JSONL line 13 (record ID 12).
en061 | SAME | en088 | 1.00 | Reference pair 37 is in a separate ground-truth JSON file. 768 counts saved records.
en062 | NEW | en089 | 0.47 | · · · Following Meyer’s example, we built a small library catalog.
en063 | EDIT | en090 | 0.54 | The proposed patch adds a module for technical reports.
en064 | SAME | en091 | 1.00 | The two existing source files remain byte-for-byte identical.
en065 | EDIT | en093 | 0.66 | In execution, technical reports render and requests for errata are still rejected.
en066 | EDIT | en092 | 0.57 | The prefix in an existing book’s output changes from book to BOOK .
en067 | NEW | en094 | 0.30 | We hold the patch, its observed behavior, and the boundary permitting new modules fixed.
en068 | EDIT | en095 | 0.59 | The new requirement covers either technical reports alone or both technical reports and errata.
en069 | EDIT | en096 | 0.68 | Both legacy contracts protect the rendering of journals and proceedings and require rejection of a separate unsupported type.
en070 | SAME | en097 | 1.00 | The broader contract also protects the original book prefix.
en071 | NEW | en098 | 0.19 | An acceptable candidate in Table 2 must meet both the new requirement and the applicable contract.
en072 | SAME | en099 | 1.00 | Two independent conditions for the same patch.
en073 | EDIT | en100 | 0.72 | The patch is acceptable when only technical reports are required and the book prefix is outside the contract.
en074 | EDIT | en105 | 0.64 | Knowing that errata are required suffices to reject it even before the prefix contract is known.
en075 | NEW | en106 | 0.33 | If only technical reports are required, the verdict turns on whether callers were promised the original prefix.
en076 | NEW | en103 | 0.39 | A separate patch adds one module within the same edit boundary, handles both new types, and preserves every protected observation.
en077 | NEW | en108 | 0.27 | With partial information, the reviewer can consider the specifications still compatible with the evidence.
en078 | NEW | en054 | 0.16 | If all give the same verdict, the reviewer can issue it.
en079 | NEW | en110 | 0.26 | If they disagree, the reviewer can give conditional verdicts or defer until the applicable specification can be established.
en080 | EDIT | en111 | 0.74 | This argument assumes that the actual specification is in the compatible set, so the set is nonempty.
en081 | NEW | en099 | 0.24 | Appendix A gives the nine disclosure conditions for this case.
en082 | NEW | en119 | 0.16 | · Section 5 assessed a proposed patch.
en083 | NEW | en115 | 0.20 | We return to the drawing example to ask where an implementation that satisfies a request can be placed.
en084 | EDIT | en114 | 0.53 | Across three comparisons, we count the existing source files edited by the candidates we ran.
en085 | NEW | en003 | 0.17 | We first varied the request.
en086 | NEW | en117 | 0.31 | In the shape layout we added a triangle in one new file and edited the circle and square files to add a labeling operation.
en087 | NEW | en118 | 0.29 | In the operation layout we edited the drawing file to add the triangle and put the labeling operation in a new file.
en088 | EDIT | en119 | 0.67 | All four candidates passed their functional checks.
en089 | NEW | en138 | 0.24 | Which layout left more existing files intact depended on the request (Figure 1A).
en090 | NEW | en139 | 0.24 | We then added the same batch-rendering function to both layouts.
en091 | NEW | en122 | 0.33 | It takes a list of shapes and brackets each rendered result.
en092 | NEW | en123 | 0.32 | We predicted that requiring the item transformation to live in the shape files would entail editing both files in the shape layout.
en093 | EDIT | en124 | 0.52 | If a shared adapter was allowed, we predicted that either layout could add the feature in one new file.
en094 | EDIT | en126 | 0.62 | All four candidates preserved order and duplicates, handled empty lists and unsupported shapes as specified, and preserved the existing circle and square renderings.
en095 | NEW | en123 | 0.32 | The candidate placing both transformations in the shape files edited two existing files.
en096 | NEW | en130 | 0.33 | All four added one file (Figure 1B).
en097 | SAME | en132 | 1.00 | Existing source files edited.
en098 | SAME | en133 | 1.00 | Panel A compares adding a triangle with adding a labeling operation.
en099 | SAME | en134 | 1.00 | Panel B holds the batch-rendering request fixed and varies the placement rule.
en100 | SAME | en135 | 1.00 | All four candidates in panel B passed the new and legacy behavior checks and added one file each.
en101 | NEW | en137 | 0.20 | · · · · The third comparison used an option to bracket a single rendering through the existing function.
en102 | NEW | en138 | 0.32 | Candidates that offered a new entry point left the existing files intact in both layouts.
en103 | NEW | en139 | 0.41 | With the same adapter added, the original functions still rejected bracketed=True .
en104 | EDIT | en140 | 0.59 | The candidates offering the option through the original functions edited one file in the operation layout and two in the shape layout.
en105 | NEW | en141 | 0.39 | In a separate baseline whose original function could already load an external decorator, each layout delivered the option through the original entry point by adding a single file (Table 3).
en106 | SAME | en142 | 1.00 | Call paths for the new rendering option.
en107 | SAME | en143 | 1.00 | The hook was already present in the last row’s baseline.
en108 | SAME | en144 | 1.00 | The negative control adds the same adapter and finds that the option remains unavailable through the original function.
en109 | NEW | en145 | 0.20 | · Permission to add a file therefore needs to be paired with a path that the caller can actually use.
en110 | NEW | en148 | 0.30 | The last row of Table 3 starts counting after the hook is already in place.
en111 | NEW | en114 | 0.14 | These file counts describe the tested candidates.
en112 | NEW | en149 | 0.29 | Whether we can predict working paths for independently authored requests, and how these counts relate to maintenance effort, remain open.
en113 | NEW | en007 | 0.17 | Whether the drawing routine falls short depends on who must sort the list.
en114 | NEW | en152 | 0.30 | The benchmark measures classification performance by comparing model responses with its reference labels.
en115 | NEW | en153 | 0.24 | Applying a finding to a specific patch also requires knowing what change the patch must deliver and which behavior existing callers were promised.
en116 | NEW | en155 | 0.24 | In the catalog example, the errata requirement can settle a rejection on its own.
en117 | NEW | en156 | 0.37 | When only technical reports are needed, the verdict turns on the promise about the book prefix.
en118 | NEW | en157 | 0.20 | Comparing possible edits also requires knowing how the new behavior can reach its callers.
en119 | NEW | en159 | 0.21 | A review that calls for an edit should identify the request or commitment it relies on and the call path to which it applies.
en120 | NEW | en159 | 0.24 | The developer can then check the grounds for the verdict or identify the remaining fact that would settle it.
en121 | NEW | en160 | 0.48 | The evidence here covers the saved material of one benchmark and the candidates we constructed and ran.
en122 | SAME | en161 | 1.00 | For Sections 3–4 the audit reads the archived JSON and JSONL.
en123 | SAME | en162 | 1.00 | For Sections 5–6 the fixtures run the examples constructed for this study.
en124 | SAME | en163 | 1.00 | The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.
Summary en: same 17; edited 38; new 69.

## v04 · [Notion](https://app.notion.com/p/41bef561cf9281338542d18745ef9f9e)
### KO (133 sentences; prior 113)
ko001 | SAME | ko001 | 1.00 | 로버트 마틴은 1996년 글에서 도형 목록을 받아 차례로 그리는 함수를 예로 들었다.
ko002 | SAME | ko002 | 1.00 | 삼각형이 자신을 그리는 동작을 제공하면, 그 함수를 고치지 않고도 삼각형을 추가할 수 있었다.
ko003 | SAME | ko003 | 1.00 | 같은 함수에 사각형으로 시작하는 목록을 주면 여전히 사각형부터 그린다.
ko004 | SAME | ko004 | 1.00 | 원을 먼저 그리려면 누가 목록을 정렬해야 할까?
ko005 | SAME | ko005 | 1.00 | 호출자가 정렬한 목록을 넘기기로 했다면 그리기 함수는 그대로 둘 수 있다.
ko006 | SAME | ko006 | 1.00 | 어떤 목록을 받아도 함수가 순서를 보장하기로 했다면 지금 코드로는 부족하다.
ko007 | SAME | ko007 | 1.00 | 소스 코드를 읽으면 함수가 정렬하지 않는다는 사실을 알 수 있다.
ko008 | SAME | ko008 | 1.00 | 그 사실을 개방–폐쇄 원칙(OCP) 위반의 근거로 삼으려면 정렬을 누가 맡았는지도 알아야 한다.
ko009 | NEW | ko099 | 0.05 | 여기에는 설계 원칙 자체보다 그 원칙을 사용하는 방식에 관한 문제가 있다.
ko010 | NEW | ko104 | 0.06 | 마틴의 사례에서는 앞으로 어떤 변화에 대비할지를 정해야 비로소 어떤 코드를 닫아 둘지 논의할 수 있었다.
ko011 | NEW | ko043 | 0.03 | 그 판단을 변경 요구가 빠진 ‘위반’ 판정으로 바꿔 사용한다면, 처음에는 결론을 정당화했던 전제가 사라진다.
ko012 | NEW | — | 0.00 | 우리는 이 위험을 원칙의 ‘과도한 공리화’라고 부른다.
ko013 | NEW | ko040 | 0.04 | 이것은 SOLID 전체가 무효하다는 역사적 결론이 아니라, 조건부 설계 조언을 무조건적인 탈락 기준처럼 적용할 때 무엇을 잃는지 묻는 문제 제기다.
ko014 | SAME | ko009 | 1.00 | 이 글은 그와 같은 전제가 세 가지 판단에 어떻게 쓰이는지 살핀다.
ko015 | SAME | ko010 | 1.00 | 먼저 SOLID 위반 분류 벤치마크의 저장 자료를 조사해 모델에게 주어진 정보의 범위를 확인한다.
ko016 | SAME | ko011 | 1.00 | 이어서 도서관 프로그램의 같은 수정안을 놓고 새 요구와 기존 호출자 계약을 달리하면 승인 여부가 어떻게 달라지는지 비교한다.
ko017 | SAME | ko012 | 1.00 | 마지막으로 도형 예제로 돌아가, 호출자가 이용할 수 있는 경로에 따라 기존 파일을 그대로 둘 수 있는지 살핀다.
ko018 | SAME | ko013 | 1.00 | · · 마틴은 1996년 글의 첫머리에서 이 원칙을 베르트랑 마이어에게서 가져왔다고 밝히며 1988년 초판 23쪽을 인용한다.
ko019 | NEW | ko040 | 0.04 | 이어지는 두 사례를 다루는 이유는 SOLID 다섯 원칙의 기원을 한 줄로 연결하기 위해서가 아니라, OCP에 적용 조건이 명시되어 있었는지 살피기 위해서다.
ko020 | SAME | ko014 | 1.00 | 마이어의 설명에서 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 사용할 수 있는 모듈이다.
ko021 | SAME | ko015 | 1.00 | 도서관 프로그램이 자료의 종류를 하나씩 구별해 처리한다면 기술보고서 한 종류를 추가하는 데도 기존 모듈의 수정이나 재컴파일이 필요할 수 있다.
ko022 | SAME | ko016 | 1.00 | 이때 설계자는 새 동작을 어디에 넣을지와 기존 사용자가 계속 어떤 동작에 의존할 수 있을지를 함께 고려하게 된다.
ko023 | SAME | ko017 | 1.00 | 마틴은 목록을 정렬하는 일을 DrawAllShapes 에 맡겼다.
ko024 | SAME | ko018 | 1.00 | 첫 구현에서는 Circle::Precedes 가 상대 도형을 검사해 사각형이면 원을 앞에 놓았다.
ko025 | SAME | ko019 | 1.00 | 새 도형이 들어왔을 때 원과 그 도형의 순서를 정하는 코드가 이미 Circle 안에 있었다.
ko026 | SAME | ko020 | 1.00 | 마틴은 이어서 도형 종류별 순서를 표로 옮겼다.
ko027 | SAME | ko021 | 1.00 | 이제 사각형을 원보다 먼저 그리라는 요청에는 표에서 두 항목의 위치를 바꾸면 된다.
ko028 | SAME | ko022 | 1.00 | 개별 도형의 넓이순으로 그리라는 요구를 가정하면 표에 없는 정보가 필요하다.
ko029 | SAME | ko023 | 1.00 | 어느 부분을 그대로 둘 수 있는지는 어떤 변경에 대비하느냐에 달려 있다.
ko030 | SAME | ko024 | 1.00 | 타입 검사가 위반의 근거가 되는지도 함수가 맡은 일에 달려 있다.
ko031 | SAME | ko025 | 1.00 | 글의 뒷부분에서 마틴은 dynamic_cast 를 쓰는 두 함수를 새로 제시한다.
ko032 | SAME | ko026 | 1.00 | 원과 사각형을 가려 그리는 DrawAllShapes 와 목록에서 사각형만 골라 그리는 DrawSquaresOnly 다.
ko033 | SAME | ko027 | 1.00 | 두 함수에 삼각형을 넣으면 어느 쪽도 그리지 않는다.
ko034 | SAME | ko028 | 1.00 | 모든 도형을 그리기로 한 함수에서는 빠진 출력이고, 사각형만 그리기로 한 함수에서는 약속한 동작이다.
ko035 | SAME | ko029 | 1.00 | 이 차이를 검토자가 입력에서 알아볼 수 있는지 확인하기 위해 실제로 저장된 분류 프롬프트를 살펴봤다.
ko036 | NEW | ko007 | 0.05 | 두 함수가 같은 구문을 썼다는 사실보다, 무엇을 하기로 한 함수인가에 따라 평가가 갈린다는 점이 중요하다.
ko037 | NEW | ko072 | 0.03 | 이 사례에서 원칙은 코드의 모양만 보고 도출한 정리가 아니라, 어떤 변경을 수용할지에 관한 설계 판단이다.
ko038 | NEW | ko103 | 0.06 | 따라서 다음 절의 분류 라벨을 읽을 때도, 라벨의 근거와 그 라벨을 적용하려는 결정을 구별해야 한다.
ko039 | SAME | ko030 | 1.00 | 참조 코드 쌍에는 위반 예시와 그 수정 예시가 들어 있고, 저장 응답에는 모델에 제출된 코드와 프롬프트, 기록된 응답이 들어 있다.
ko040 | SAME | ko031 | 1.00 | 프롬프트 틀은 저장 프롬프트에 정확히 한 번 나오는 제출 코드를 공통 자리표시자로 치환해 얻었다.
ko041 | SAME | ko032 | 1.00 | 저장 응답의 제출 코드를 모든 참조 쌍의 수정 전·후 소스와 대조했다.
ko042 | SAME | ko033 | 1.00 | 각 문자열을 그대로 비교한 뒤 양끝 공백을 제거해 다시 비교했다.
ko043 | SAME | ko034 | 1.00 | Python 참조 쌍은 구문 트리로 파싱해 최상위 클래스의 메서드 선언 이름을 비교했다.
ko044 | SAME | ko035 | 1.00 | 상속에 따른 호출 가능성, 실제 사용 여부, 보장의 범위는 별도 근거가 필요한 질문이다.
ko045 | SAME | ko036 | 1.00 | 이 연구에서 작성한 도서관·도형 재현은 §5와 §6에서 정한 조건으로 실행했다.
ko046 | SAME | ko037 | 1.00 | ZIP 안의 공개 재현 패키지 코드는 실행하지 않았다.
ko047 | SAME | ko038 | 1.00 | 아카이브 식별 정보와 확인 명령은 부록 A에 있다.
ko048 | SAME | ko039 | 1.00 | · Pehlivan 등은 위반 시나리오를 정하고, 생성한 코드 예시를 수정·검증한 뒤 의견이 갈린 사례의 참조 라벨을 논의로 정했다.
ko049 | SAME | ko040 | 1.00 | SOLID 위반을 식별하는 모델 응답은 그 라벨과 대조했다.
ko050 | SAME | ko041 | 1.00 | OCP에 해당하는 아카이브에는 참조 쌍 48개와 저장 응답 768건이 있다.
ko051 | SAME | ko042 | 1.00 | 저장 프롬프트에서 제출 코드를 가렸을 때 서로 다른 문자열 24개가 남았고, 네 전략 사이에 동일한 틀은 없었다.
ko052 | SAME | ko043 | 1.00 | 각 사례의 변경 요구나 기존 호출자 계약을 따로 밝힌 틀은 없었다.
ko053 | NEW | ko102 | 0.04 | 이는 벤치마크가 본래 수행하려는 분류 과제를 잘못 설계했다는 뜻이 아니다.
ko054 | NEW | ko022 | 0.05 | 특정 수정안을 승인하거나 거절하는 데 이 분류 결과를 사용하려면 추가 증거가 필요하다는 뜻이다.
ko055 | SAME | ko044 | 1.00 | 저장된 Python EXAMPLE 지시는 다형성으로 처리할 만한 반복 분기를 찾도록 한다.
ko056 | SAME | ko045 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko057 | SAME | ko046 | 1.00 | 그 분기를 보면 새 도형을 추가할 때 어디에 손댈지 짐작할 수 있다.
ko058 | SAME | ko047 | 1.00 | 새 도형 추가가 실제 요청인지, 사각형의 너비를 직접 읽는 호출을 계속 지원해야 하는지는 이 지시문에서 확인되지 않는다.
ko059 | SAME | ko048 | 1.00 | 별도의 참조 쌍 37번은 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko060 | SAME | ko049 | 1.00 | 원본 문자열과 양끝 공백을 제거한 문자열을 대조했을 때, 저장된 제출 코드와 참조 쌍의 어느 쪽도 일치하지 않았다.
ko061 | SAME | ko050 | 1.00 | 따라서 여기서 근거로 삼는 것은 참조 쌍에서 확인한 선언의 변화다.
ko062 | SAME | ko051 | 1.00 | 그 변화가 수정안을 거절할 이유가 되려면 호출자가 너비를 읽는 동작까지 보장받았는지 확인해야 한다.
ko063 | SAME | ko052 | 1.00 | 다음 절에서는 바로 그 보장을 바꾸면 같은 수정안의 판정이 달라지는지 본다.
ko064 | SAME | ko053 | 1.00 | 프롬프트 예시는 저장 JSONL 13행(ID 12)이다.
ko065 | SAME | ko054 | 1.00 | 참조 쌍 37번은 별도의 ground truth JSON 위치다.
ko066 | SAME | ko055 | 1.00 | · · · 마이어의 예를 바탕으로 작은 도서관 목록 프로그램을 만들었다.
ko067 | SAME | ko056 | 1.00 | 검토할 수정안은 기술보고서를 처리하는 모듈을 추가한다.
ko068 | SAME | ko057 | 1.00 | 기존 소스 파일 두 개는 바이트 단위로 그대로다.
ko069 | SAME | ko058 | 1.00 | 실행하면 기술보고서는 출력되고 정오표는 여전히 거절된다.
ko070 | SAME | ko059 | 1.00 | 기존 책 출력의 접두어는 book 에서 BOOK 으로 바뀐다.
ko071 | NEW | ko037 | 0.06 | 기존 파일을 수정하지 않았다는 사실은 기존 호출 결과까지 보존했다는 뜻이 아니다.
ko072 | NEW | ko104 | 0.05 | 변경된 동작은 우리가 만든 실행 예제에서 관찰했다.
ko073 | SAME | ko060 | 1.00 | 수정안과 실행 결과, 새 모듈을 추가할 수 있는 편집 범위를 고정했다.
ko074 | SAME | ko061 | 1.00 | 새 요구는 기술보고서만 지원하는 경우와 정오표까지 지원하는 경우로 나눴다.
ko075 | SAME | ko062 | 1.00 | 두 계약은 모두 학술지와 학회록의 출력, 그리고 별개의 미지원 자료 유형을 거절하는 동작을 보호한다.
ko076 | SAME | ko063 | 1.00 | 표 2의 승인은 새 요구와 보호할 계약을 모두 충족한 경우다.
ko077 | SAME | ko064 | 1.00 | 기술보고서만 필요하고 책 접두어를 보호하지 않는 경우에 승인된다.
ko078 | SAME | ko065 | 1.00 | 정오표가 필수라는 사실을 알면 책 접두어 계약을 모르더라도 거절할 수 있다.
ko079 | SAME | ko066 | 1.00 | 기술보고서만 필요하다는 사실을 알 때는 책 접두어를 보장했는지가 결론을 가른다.
ko080 | SAME | ko067 | 1.00 | 별도로 만든 수정안은 같은 편집 범위에서 새 모듈 하나를 추가해 두 자료 유형을 처리하고 모든 보호 동작을 지켰다.
ko081 | SAME | ko068 | 1.00 | 판정에 필요한 정보가 일부만 주어지면, 그 정보와 양립하는 명세들을 비교할 수 있다.
ko082 | SAME | ko069 | 1.00 | 모든 명세가 같은 판정을 내리면 그 판정을 내릴 수 있다.
ko083 | SAME | ko070 | 1.00 | 서로 다른 판정이 나오면 조건마다 결론을 밝히거나, 어느 조건이 실제로 적용되는지 확인할 때까지 보류할 수 있다.
ko084 | SAME | ko071 | 1.00 | 이 논증은 실제 명세가 검토 중인 집합에 들어 있어 그 집합이 비어 있지 않다는 전제에서 성립한다.
ko085 | NEW | ko042 | 0.02 | 이때 한 가지 입력만 받아 언제나 승인 또는 거절 중 하나를 출력하는 규칙은, 서로 다른 정답이 남아 있는 두 조건을 동시에 맞힐 수 없다.
ko086 | NEW | ko040 | 0.05 | 다만 이 논증만으로 SOLID의 다른 정리나 실제 현장의 판단 오류율을 추정할 수는 없다.
ko087 | SAME | ko072 | 1.00 | 부록 A에는 이번 사례에서 검토한 정보 공개 조건 아홉 개가 있다.
ko088 | SAME | ko073 | 1.00 | · §5에서 거절된 것은 주어진 수정안이다.
ko089 | SAME | ko074 | 1.00 | 이제 도형 예제로 돌아가, 같은 요청을 처리하는 구현을 어디에 둘 수 있는지 비교한다.
ko090 | SAME | ko075 | 1.00 | 세 비교에서 실행한 후보들의 기존 파일 수정 수를 센다.
ko091 | SAME | ko076 | 1.00 | 도형별 배치에서는 삼각형을 새 파일 하나로 추가했고, 이름표 연산을 추가할 때는 원과 사각형의 파일을 고쳤다.
ko092 | SAME | ko077 | 1.00 | 연산별 배치에서는 반대로 삼각형을 추가할 때 그리기 파일을 고쳤고, 이름표 연산은 새 파일에 뒀다.
ko093 | SAME | ko078 | 1.00 | 네 수정안이 모두 기능 검사를 통과했지만 기존 파일을 덜 건드리는 배치는 요구에 따라 달랐다(그림 1A).
ko094 | SAME | ko079 | 1.00 | 두 번째 비교에서는 같은 배치 렌더링 함수를 추가했다.
ko095 | SAME | ko080 | 1.00 | 이 함수는 도형 목록을 받아 각 렌더링 결과를 대괄호로 감싼다.
ko096 | SAME | ko081 | 1.00 | 도형별 배치에서 변환을 각 도형 파일이 맡아야 하면 원과 사각형 파일을 고친다.
ko097 | SAME | ko082 | 1.00 | 공용 어댑터를 허용하면 두 배치 모두 새 파일 하나로 기능을 제공할 수 있다고 예측했다.
ko098 | SAME | ko083 | 1.00 | 실행한 네 후보는 모두 입력 순서와 중복을 보존하고 빈 목록과 미지원 도형을 명세대로 처리했다.
ko099 | SAME | ko084 | 1.00 | 각 후보는 원과 사각형의 기존 렌더링을 유지했다.
ko100 | SAME | ko085 | 1.00 | 기존 파일 두 개를 고친 것은 도형 파일이 변환을 맡은 후보뿐이었다.
ko101 | SAME | ko086 | 1.00 | 네 후보 모두 새 파일 하나를 추가했다(그림 1B).
ko102 | SAME | ko087 | 1.00 | A는 삼각형 추가와 이름표 연산 추가를 비교한다.
ko103 | SAME | ko088 | 1.00 | B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다.
ko104 | SAME | ko089 | 1.00 | B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.
ko105 | SAME | ko090 | 1.00 | · · · · 세 번째 비교에서는 배치 함수 대신 기존 렌더링의 결과 하나를 선택적으로 감싸는 옵션을 사용했다.
ko106 | SAME | ko091 | 1.00 | 새 모듈을 호출할 수 있는 경우에는 두 배치가 기존 파일을 그대로 뒀다.
ko107 | SAME | ko092 | 1.00 | 같은 모듈을 추가한 상태에서 기존 함수에 bracketed=True 를 넘기면 함수는 그 인자를 받지 못했다.
ko108 | SAME | ko093 | 1.00 | 기존 함수로 옵션을 제공한 후보는 연산별 배치에서 파일 하나, 도형별 배치에서 두 개를 고쳤다.
ko109 | SAME | ko094 | 1.00 | 기존 함수가 외부 변환 모듈을 불러올 수 있도록 이미 구성된 별도 기준선에서는 두 배치 모두 새 파일 하나를 추가해 기존 호출 경로로 옵션을 제공했다(표 3).
ko110 | SAME | ko095 | 1.00 | 확장 지점은 세 번째 행의 기준선에 이미 있었다.
ko111 | NEW | ko095 | 0.04 | 따라서 이 행의 0개를 첫 설계에서 확장 지점을 처음 만드는 비용까지 포함한 결과로 읽어서는 안 된다.
ko112 | NEW | ko037 | 0.07 | 여기서는 확장 지점이 도입된 비용을 별도로 측정하지 않았다.
ko113 | SAME | ko096 | 1.00 | 같은 어댑터를 추가해도 기존 함수에서는 옵션을 쓸 수 없었던 대조 실행을 포함했다.
ko114 | SAME | ko097 | 1.00 | · 새 파일을 추가할 수 있어도 그 파일이 실행되려면 호출자가 쓸 수 있는 경로가 필요하다.
ko115 | SAME | ko098 | 1.00 | 표 3의 마지막 행은 확장 지점이 이미 있는 상태에서 이후에 고친 파일만 센다.
ko116 | SAME | ko099 | 1.00 | 여기에 든 수정 수는 실행한 후보에 관한 관찰이다.
ko117 | SAME | ko100 | 1.00 | 독립적으로 작성한 요구에서도 어떤 경로가 작동할지 예측할 수 있는지, 파일 수정 수가 실제 유지보수 부담과 어떻게 연결되는지는 남은 질문이다.
ko118 | SAME | ko101 | 1.00 | 서론의 그리기 함수가 잘못됐는지는 정렬을 누가 맡았는지에 달려 있었다.
ko119 | SAME | ko102 | 1.00 | 벤치마크는 모델의 응답을 참조 라벨과 대조해 분류 성능을 잰다.
ko120 | SAME | ko103 | 1.00 | 그 판정을 구체적인 수정안에 적용하려면 어떤 기능이 필요한지, 어떤 동작을 기존 호출자에게 약속했는지를 확인해야 한다.
ko121 | SAME | ko104 | 1.00 | 도서관 예제에서는 정오표 요구만으로 수정안을 거절할 수 있었다.
ko122 | SAME | ko105 | 1.00 | 기술보고서만 필요한 경우에는 책 접두어 계약이 결론을 갈랐다.
ko123 | SAME | ko106 | 1.00 | 어떤 수정안이 가능한지를 비교할 때는 호출자가 새 동작을 받을 수 있는 경로도 확인해야 한다.
ko124 | SAME | ko107 | 1.00 | 검토 의견으로 변경을 요구하려면 어느 요구나 계약을 근거로 삼았는지, 어느 호출 경로에 적용되는지를 밝힐 수 있어야 한다.
ko125 | SAME | ko108 | 1.00 | 그러면 개발자는 이미 내려진 결론의 근거를 확인하거나, 보류된 판정을 가를 사실을 더 찾을 수 있다.
ko126 | SAME | ko109 | 1.00 | 이 결과는 한 벤치마크의 저장 자료와 여기서 구성해 실행한 후보의 범위에서 성립한다.
ko127 | NEW | ko011 | 0.06 | 여기서 더 나아가려면 SOLID를 대체할 공리를 선언하기보다, 어떤 변경과 계약, 권한과 호출 경로가 주어졌을 때 설계의 유불리가 어떻게 달라지는지 예측할 수 있는 표현을 찾아야 한다.
ko128 | NEW | ko100 | 0.04 | 그런 표현이 실제 독립 요구에서도 작동한다면, 익숙한 원칙이 유용한 이유뿐 아니라 그 조언을 따르지 않는 설계가 더 나은 조건도 설명할 수 있을 것이다.
ko129 | NEW | ko035 | 0.02 | 이 가능성은 이번 논문의 결과가 아니라 다음에 검증할 가설로 남긴다.
ko130 | SAME | ko110 | 1.00 | §3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다.
ko131 | SAME | ko111 | 1.00 | §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다.
ko132 | SAME | ko112 | 1.00 | 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다.
ko133 | SAME | ko113 | 1.00 | 그림 1의 소스와 출력 위치는 그림 캡션에 있다.
Summary ko: same 113; edited 0; new 20.

### EN (144 sentences; prior 124)
en001 | SAME | en001 | 1.00 | In 1996, Robert Martin described a function that drew the shapes in a list in order.
en002 | SAME | en002 | 1.00 | A triangle could be added without editing the function if the triangle supplied its own drawing operation.
en003 | SAME | en003 | 1.00 | Martin then introduced a new requirement.
en004 | SAME | en004 | 1.00 | Every circle had to be drawn before any square.
en005 | SAME | en005 | 1.00 | Given a list that begins with a square, the same function still draws the square first.
en006 | SAME | en006 | 1.00 | Who is responsible for sorting the list?
en007 | SAME | en007 | 1.00 | If the caller must pass a sorted list, the drawing function can stay as it is.
en008 | SAME | en008 | 1.00 | If the function must produce the required order for any input list, the current code falls short.
en009 | SAME | en009 | 1.00 | A reviewer can see that the function does no sorting.
en010 | SAME | en010 | 1.00 | To take that fact as evidence of an open–closed principle (OCP) violation, the reviewer also needs to know who was meant to sort the shapes.
en011 | NEW | en015 | 0.10 | The difficulty is not simply whether the principle is sound.
en012 | NEW | en120 | 0.11 | In Martin's example, a designer must first identify the changes against which a routine ought to remain closed.
en013 | NEW | en012 | 0.10 | If that situated judgment is later used as a violation label without its premise, the label may carry the authority of a rule while omitting the reason for applying it.
en014 | NEW | en106 | 0.07 | We call this risk the over-axiomatization of design advice.
en015 | NEW | en072 | 0.09 | It is a question about how conditional advice is used, not a demonstrated history of the entire SOLID family.
en016 | SAME | en011 | 1.00 | We examine how such premises enter three decisions.
en017 | SAME | en012 | 1.00 | First, we audit the saved material from a benchmark for classifying SOLID violations to see what information the model received.
en018 | SAME | en013 | 1.00 | Next, we hold a patch to a library program fixed and vary the new requirement and the contract with existing callers.
en019 | SAME | en014 | 1.00 | Finally, we return to the drawing example and vary the paths available to callers to see when a candidate can leave existing files intact.
en020 | SAME | en015 | 1.00 | · · Martin opens his 1996 article by attributing the principle to Bertrand Meyer and citing page 23 of the 1988 first edition.
en021 | NEW | en081 | 0.12 | We examine this explicit citation link to recover the conditions under which OCP was argued for; it is not, by itself, a genealogy of all five SOLID principles.
en022 | SAME | en016 | 1.00 | A closed module in Meyer’s account is one that other modules can use on the basis of a stable specification.
en023 | SAME | en017 | 1.00 | If a library program distinguishes publication types one by one, adding technical reports can require edits to existing modules or recompiling them.
en024 | SAME | en018 | 1.00 | The designer must consider both where the new behavior can live and what existing users of the module can continue to rely on.
en025 | SAME | en019 | 1.00 | Martin assigned sorting to DrawAllShapes .
en026 | SAME | en020 | 1.00 | In the first implementation, Circle::Precedes inspected the other shape and put the circle first if it was a square.
en027 | SAME | en021 | 1.00 | The code that decided how a new shape would rank against a circle already lived in Circle .
en028 | SAME | en022 | 1.00 | Martin then moved the order of shape types into a table.
en029 | SAME | en023 | 1.00 | Putting squares first now requires swapping two entries.
en030 | SAME | en024 | 1.00 | Ordering individual shapes by area, for example, would require information outside the table.
en031 | SAME | en025 | 1.00 | Which part of the program can stay as it is depends on the change it must accommodate.
en032 | SAME | en026 | 1.00 | Whether a type check supports a violation finding also depends on the function’s obligation.
en033 | SAME | en027 | 1.00 | Later in the article, Martin presents two further functions that use dynamic_cast .
en034 | SAME | en028 | 1.00 | DrawAllShapes recognizes and draws circles and squares.
en035 | SAME | en029 | 1.00 | DrawSquaresOnly selects squares from the list and draws them.
en036 | SAME | en030 | 1.00 | Given a triangle, both skip it.
en037 | SAME | en031 | 1.00 | A function that promises to draw every shape has omitted an output, while a function that promises to draw squares has met its obligation.
en038 | SAME | en032 | 1.00 | We turn to saved classification prompts to see how much of that kind of obligation the reviewer could establish from the input.
en039 | NEW | en080 | 0.14 | The decisive distinction is not between two syntactic patterns: both functions contain type checks.
en040 | NEW | en032 | 0.12 | It is between the obligations they were written to satisfy.
en041 | NEW | en108 | 0.13 | This makes the original example a conditional design argument rather than a proof that one source pattern is universally defective.
en042 | NEW | en033 | 0.16 | We carry that distinction into the classification archive.
en043 | SAME | en033 | 1.00 | · · We distinguish three units in the archive.
en044 | SAME | en034 | 1.00 | A reference pair contains a violation example and its revision.
en045 | SAME | en035 | 1.00 | A saved response record contains the code submitted to the model, its prompt, and the recorded response.
en046 | SAME | en036 | 1.00 | We recover a prompt template by replacing the single exact occurrence of the submitted code with a common placeholder.
en047 | SAME | en037 | 1.00 | We compare templates as strings.
en048 | SAME | en038 | 1.00 | We compared each saved submission with the source on both sides of every reference pair, first as stored and again after trimming whitespace from both ends.
en049 | SAME | en039 | 1.00 | For Python reference pairs we parsed the syntax trees and compared names of methods declared in top-level classes, excluding names that begin with an underscore.
en050 | SAME | en040 | 1.00 | The comparison captures declaration changes.
en051 | SAME | en041 | 1.00 | Inherited availability, actual client use, and whether that use was protected each require separate evidence.
en052 | SAME | en042 | 1.00 | We ran the library and drawing fixtures built for this study under the conditions given in Sections 5 and 6.
en053 | SAME | en043 | 1.00 | We executed no code from the archived replication package.
en054 | SAME | en044 | 1.00 | Appendix A identifies the archive and the commands needed to reproduce the checks.
en055 | SAME | en045 | 1.00 | · Pehlivan et al. specified violation scenarios and refined and checked the generated examples.
en056 | SAME | en046 | 1.00 | They resolved disagreements about reference labels through discussion, then compared model classifications of SOLID violations with those labels.
en057 | SAME | en047 | 1.00 | The OCP archive contains 48 reference pairs and 768 saved response records.
en058 | SAME | en048 | 1.00 | Masking the submitted code yielded 24 distinct template strings, with no exact template shared across the four strategies.
en059 | SAME | en049 | 1.00 | None of the templates separately states a change request or a protected caller contract for an individual case.
en060 | NEW | en114 | 0.19 | That absence is not a defect in a benchmark whose stated task is classification.
en061 | NEW | en024 | 0.13 | It matters when the resulting label is asked to justify an engineering decision outside that task.
en062 | SAME | en050 | 1.00 | One saved Python EXAMPLE prompt points the reviewer to repeated branches where polymorphism would fit.
en063 | SAME | en051 | 1.00 | The submitted AreaCalculator checks the shape type before calculating the area of a circle or rectangle.
en064 | SAME | en052 | 1.00 | The branch suggests where an edit might go if a new shape is added.
en065 | SAME | en053 | 1.00 | The instruction leaves open whether anyone has requested that change and whether existing calls that read a rectangle’s width must still be supported.
en066 | SAME | en054 | 1.00 | In a separate reference pair, number 37, the revision moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en067 | SAME | en055 | 1.00 | No saved submission matched either side of the reference pairs in the exact or outer-whitespace-trimmed comparison.
en068 | SAME | en056 | 1.00 | Our evidence for the missing declaration comes from comparing the reference sources.
en069 | SAME | en057 | 1.00 | To argue that its removal warrants rejecting a patch, a reviewer would need to establish that callers were guaranteed access to the width.
en070 | SAME | en058 | 1.00 | We test whether such a guarantee can change the decision for the same patch.
en071 | SAME | en059 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en072 | SAME | en060 | 1.00 | The saved prompt is on JSONL line 13 (record ID 12).
en073 | SAME | en061 | 1.00 | Reference pair 37 is in a separate ground-truth JSON file. 768 counts saved records.
en074 | SAME | en062 | 1.00 | · · · Following Meyer’s example, we built a small library catalog.
en075 | SAME | en063 | 1.00 | The proposed patch adds a module for technical reports.
en076 | SAME | en064 | 1.00 | The two existing source files remain byte-for-byte identical.
en077 | SAME | en065 | 1.00 | In execution, technical reports render and requests for errata are still rejected.
en078 | SAME | en066 | 1.00 | The prefix in an existing book’s output changes from book to BOOK .
en079 | NEW | en076 | 0.13 | The identity of the old source files therefore does not imply the preservation of every observable result; we verified the latter separately in our fixture.
en080 | SAME | en067 | 1.00 | We hold the patch, its observed behavior, and the boundary permitting new modules fixed.
en081 | SAME | en068 | 1.00 | The new requirement covers either technical reports alone or both technical reports and errata.
en082 | SAME | en069 | 1.00 | Both legacy contracts protect the rendering of journals and proceedings and require rejection of a separate unsupported type.
en083 | SAME | en070 | 1.00 | The broader contract also protects the original book prefix.
en084 | SAME | en071 | 1.00 | An acceptable candidate in Table 2 must meet both the new requirement and the applicable contract.
en085 | SAME | en072 | 1.00 | Two independent conditions for the same patch.
en086 | SAME | en073 | 1.00 | The patch is acceptable when only technical reports are required and the book prefix is outside the contract.
en087 | SAME | en074 | 1.00 | Knowing that errata are required suffices to reject it even before the prefix contract is known.
en088 | SAME | en075 | 1.00 | If only technical reports are required, the verdict turns on whether callers were promised the original prefix.
en089 | SAME | en076 | 1.00 | A separate patch adds one module within the same edit boundary, handles both new types, and preserves every protected observation.
en090 | SAME | en077 | 1.00 | With partial information, the reviewer can consider the specifications still compatible with the evidence.
en091 | SAME | en078 | 1.00 | If all give the same verdict, the reviewer can issue it.
en092 | SAME | en079 | 1.00 | If they disagree, the reviewer can give conditional verdicts or defer until the applicable specification can be established.
en093 | SAME | en080 | 1.00 | This argument assumes that the actual specification is in the compatible set, so the set is nonempty.
en094 | NEW | en080 | 0.15 | A rule that sees the same input and must always return a single binary verdict cannot be correct for two compatible specifications that require opposite answers.
en095 | NEW | en012 | 0.10 | This establishes an information limit, not an error rate for SOLID judgments in practice.
en096 | SAME | en081 | 1.00 | Appendix A gives the nine disclosure conditions for this case.
en097 | SAME | en082 | 1.00 | · Section 5 assessed a proposed patch.
en098 | SAME | en083 | 1.00 | We return to the drawing example to ask where an implementation that satisfies a request can be placed.
en099 | SAME | en084 | 1.00 | Across three comparisons, we count the existing source files edited by the candidates we ran.
en100 | SAME | en085 | 1.00 | We first varied the request.
en101 | SAME | en086 | 1.00 | In the shape layout we added a triangle in one new file and edited the circle and square files to add a labeling operation.
en102 | SAME | en087 | 1.00 | In the operation layout we edited the drawing file to add the triangle and put the labeling operation in a new file.
en103 | SAME | en088 | 1.00 | All four candidates passed their functional checks.
en104 | SAME | en089 | 1.00 | Which layout left more existing files intact depended on the request (Figure 1A).
en105 | SAME | en090 | 1.00 | We then added the same batch-rendering function to both layouts.
en106 | SAME | en091 | 1.00 | It takes a list of shapes and brackets each rendered result.
en107 | SAME | en092 | 1.00 | We predicted that requiring the item transformation to live in the shape files would entail editing both files in the shape layout.
en108 | SAME | en093 | 1.00 | If a shared adapter was allowed, we predicted that either layout could add the feature in one new file.
en109 | SAME | en094 | 1.00 | All four candidates preserved order and duplicates, handled empty lists and unsupported shapes as specified, and preserved the existing circle and square renderings.
en110 | SAME | en095 | 1.00 | The candidate placing both transformations in the shape files edited two existing files.
en111 | SAME | en096 | 1.00 | All four added one file (Figure 1B).
en112 | SAME | en097 | 1.00 | Existing source files edited.
en113 | SAME | en098 | 1.00 | Panel A compares adding a triangle with adding a labeling operation.
en114 | SAME | en099 | 1.00 | Panel B holds the batch-rendering request fixed and varies the placement rule.
en115 | SAME | en100 | 1.00 | All four candidates in panel B passed the new and legacy behavior checks and added one file each.
en116 | SAME | en101 | 1.00 | · · · · The third comparison used an option to bracket a single rendering through the existing function.
en117 | SAME | en102 | 1.00 | Candidates that offered a new entry point left the existing files intact in both layouts.
en118 | SAME | en103 | 1.00 | With the same adapter added, the original functions still rejected bracketed=True .
en119 | SAME | en104 | 1.00 | The candidates offering the option through the original functions edited one file in the operation layout and two in the shape layout.
en120 | SAME | en105 | 1.00 | In a separate baseline whose original function could already load an external decorator, each layout delivered the option through the original entry point by adding a single file (Table 3).
en121 | SAME | en106 | 1.00 | Call paths for the new rendering option.
en122 | SAME | en107 | 1.00 | The hook was already present in the last row’s baseline.
en123 | NEW | en107 | 0.12 | Its zero-edits result does not include the cost of introducing that hook into the earlier baseline.
en124 | NEW | en081 | 0.08 | We did not measure that initial investment.
en125 | SAME | en108 | 1.00 | The negative control adds the same adapter and finds that the option remains unavailable through the original function.
en126 | SAME | en109 | 1.00 | · Permission to add a file therefore needs to be paired with a path that the caller can actually use.
en127 | SAME | en110 | 1.00 | The last row of Table 3 starts counting after the hook is already in place.
en128 | SAME | en111 | 1.00 | These file counts describe the tested candidates.
en129 | SAME | en112 | 1.00 | Whether we can predict working paths for independently authored requests, and how these counts relate to maintenance effort, remain open.
en130 | SAME | en113 | 1.00 | Whether the drawing routine falls short depends on who must sort the list.
en131 | SAME | en114 | 1.00 | The benchmark measures classification performance by comparing model responses with its reference labels.
en132 | SAME | en115 | 1.00 | Applying a finding to a specific patch also requires knowing what change the patch must deliver and which behavior existing callers were promised.
en133 | SAME | en116 | 1.00 | In the catalog example, the errata requirement can settle a rejection on its own.
en134 | SAME | en117 | 1.00 | When only technical reports are needed, the verdict turns on the promise about the book prefix.
en135 | SAME | en118 | 1.00 | Comparing possible edits also requires knowing how the new behavior can reach its callers.
en136 | SAME | en119 | 1.00 | A review that calls for an edit should identify the request or commitment it relies on and the call path to which it applies.
en137 | SAME | en120 | 1.00 | The developer can then check the grounds for the verdict or identify the remaining fact that would settle it.
en138 | SAME | en121 | 1.00 | The evidence here covers the saved material of one benchmark and the candidates we constructed and ran.
en139 | NEW | en041 | 0.13 | Rather than announce a new set of axioms, the next step is to ask whether changes, protected commitments, authority, and caller routes can be represented in a form that predicts when one design has an advantage over anot
en140 | NEW | en016 | 0.10 | Such an account would be valuable if it explained both the usefulness of familiar principles and the conditions under which their preferred design loses.
en141 | NEW | en080 | 0.10 | The present paper poses that hypothesis; it does not establish it.
en142 | SAME | en122 | 1.00 | For Sections 3–4 the audit reads the archived JSON and JSONL.
en143 | SAME | en123 | 1.00 | For Sections 5–6 the fixtures run the examples constructed for this study.
en144 | SAME | en124 | 1.00 | The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.
Summary en: same 124; edited 0; new 20.

## v05 · [Notion](https://app.notion.com/p/41bef561cf928187b1b7fc100f9a0995)
### KO (137 sentences; prior 133)
ko001 | SAME | ko001 | 1.00 | 로버트 마틴은 1996년 글에서 도형 목록을 받아 차례로 그리는 함수를 예로 들었다.
ko002 | SAME | ko002 | 1.00 | 삼각형이 자신을 그리는 동작을 제공하면, 그 함수를 고치지 않고도 삼각형을 추가할 수 있었다.
ko003 | SAME | ko003 | 1.00 | 같은 함수에 사각형으로 시작하는 목록을 주면 여전히 사각형부터 그린다.
ko004 | SAME | ko004 | 1.00 | 원을 먼저 그리려면 누가 목록을 정렬해야 할까?
ko005 | SAME | ko005 | 1.00 | 호출자가 정렬한 목록을 넘기기로 했다면 그리기 함수는 그대로 둘 수 있다.
ko006 | SAME | ko006 | 1.00 | 어떤 목록을 받아도 함수가 순서를 보장하기로 했다면 지금 코드로는 부족하다.
ko007 | SAME | ko007 | 1.00 | 소스 코드를 읽으면 함수가 정렬하지 않는다는 사실을 알 수 있다.
ko008 | SAME | ko008 | 1.00 | 그 사실을 개방–폐쇄 원칙(OCP) 위반의 근거로 삼으려면 정렬을 누가 맡았는지도 알아야 한다.
ko009 | SAME | ko009 | 1.00 | 여기에는 설계 원칙 자체보다 그 원칙을 사용하는 방식에 관한 문제가 있다.
ko010 | SAME | ko010 | 1.00 | 마틴의 사례에서는 앞으로 어떤 변화에 대비할지를 정해야 비로소 어떤 코드를 닫아 둘지 논의할 수 있었다.
ko011 | SAME | ko011 | 1.00 | 그 판단을 변경 요구가 빠진 ‘위반’ 판정으로 바꿔 사용한다면, 처음에는 결론을 정당화했던 전제가 사라진다.
ko012 | SAME | ko012 | 1.00 | 우리는 이 위험을 원칙의 ‘과도한 공리화’라고 부른다.
ko013 | SAME | ko013 | 1.00 | 이것은 SOLID 전체가 무효하다는 역사적 결론이 아니라, 조건부 설계 조언을 무조건적인 탈락 기준처럼 적용할 때 무엇을 잃는지 묻는 문제 제기다.
ko014 | NEW | ko054 | 0.09 | 이 문제를 따지려면 ‘위반’이라고 분류하는 일과 특정 수정안을 거절하는 일을 먼저 나눠야 한다.
ko015 | NEW | ko015 | 0.19 | SOLID 위반 분류 벤치마크의 저장 자료는 모델이 어떤 근거를 받았는지 보여 주지만, 특정 유지보수 요청이 승인되어야 하는지까지 판정하지는 않는다.
ko016 | NEW | ko016 | 0.21 | 우리는 별도로 만든 도서관 프로그램에서 같은 수정안을 서로 다른 요구와 기존 호출자 계약 아래 두어 그 간격을 검사한다.
ko017 | NEW | ko093 | 0.04 | 수정안 자체의 수용 여부를 따진 다음에는, 새로운 기능이 실제 호출 경로에 도달하도록 만드는 일이 어느 기존 파일을 바꾸게 하는지도 비교한다.
ko018 | SAME | ko018 | 1.00 | · · 마틴은 1996년 글의 첫머리에서 이 원칙을 베르트랑 마이어에게서 가져왔다고 밝히며 1988년 초판 23쪽을 인용한다.
ko019 | SAME | ko019 | 1.00 | 이어지는 두 사례를 다루는 이유는 SOLID 다섯 원칙의 기원을 한 줄로 연결하기 위해서가 아니라, OCP에 적용 조건이 명시되어 있었는지 살피기 위해서다.
ko020 | SAME | ko020 | 1.00 | 마이어의 설명에서 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 사용할 수 있는 모듈이다.
ko021 | SAME | ko021 | 1.00 | 도서관 프로그램이 자료의 종류를 하나씩 구별해 처리한다면 기술보고서 한 종류를 추가하는 데도 기존 모듈의 수정이나 재컴파일이 필요할 수 있다.
ko022 | SAME | ko022 | 1.00 | 이때 설계자는 새 동작을 어디에 넣을지와 기존 사용자가 계속 어떤 동작에 의존할 수 있을지를 함께 고려하게 된다.
ko023 | SAME | ko023 | 1.00 | 마틴은 목록을 정렬하는 일을 DrawAllShapes 에 맡겼다.
ko024 | SAME | ko024 | 1.00 | 첫 구현에서는 Circle::Precedes 가 상대 도형을 검사해 사각형이면 원을 앞에 놓았다.
ko025 | SAME | ko025 | 1.00 | 새 도형이 들어왔을 때 원과 그 도형의 순서를 정하는 코드가 이미 Circle 안에 있었다.
ko026 | SAME | ko026 | 1.00 | 마틴은 이어서 도형 종류별 순서를 표로 옮겼다.
ko027 | SAME | ko027 | 1.00 | 이제 사각형을 원보다 먼저 그리라는 요청에는 표에서 두 항목의 위치를 바꾸면 된다.
ko028 | SAME | ko028 | 1.00 | 개별 도형의 넓이순으로 그리라는 요구를 가정하면 표에 없는 정보가 필요하다.
ko029 | SAME | ko029 | 1.00 | 어느 부분을 그대로 둘 수 있는지는 어떤 변경에 대비하느냐에 달려 있다.
ko030 | SAME | ko030 | 1.00 | 타입 검사가 위반의 근거가 되는지도 함수가 맡은 일에 달려 있다.
ko031 | SAME | ko031 | 1.00 | 글의 뒷부분에서 마틴은 dynamic_cast 를 쓰는 두 함수를 새로 제시한다.
ko032 | SAME | ko032 | 1.00 | 원과 사각형을 가려 그리는 DrawAllShapes 와 목록에서 사각형만 골라 그리는 DrawSquaresOnly 다.
ko033 | SAME | ko033 | 1.00 | 두 함수에 삼각형을 넣으면 어느 쪽도 그리지 않는다.
ko034 | SAME | ko034 | 1.00 | 모든 도형을 그리기로 한 함수에서는 빠진 출력이고, 사각형만 그리기로 한 함수에서는 약속한 동작이다.
ko035 | NEW | ko035 | 0.08 | 검토자가 어떤 근거로 두 경우를 구별할 수 있는지를 확인하려면, 실제로 받았던 코드와 지시를 구분해 살펴봐야 한다.
ko036 | NEW | ko036 | 0.16 | 두 함수는 같은 구문을 사용하지만, 약속한 일이 달라 평가가 갈린다.
ko037 | NEW | ko088 | 0.02 | 이 사례를 위반 여부의 판단으로 옮기려면 검토에 주어진 코드와 그 코드가 맡은 책임을 나눠야 한다.
ko038 | NEW | ko035 | 0.13 | 우리는 먼저 자료를 어떤 단위로 읽었는지 밝힌 뒤, 저장된 분류 프롬프트에서 그 책임을 어디까지 확인할 수 있는지 살펴본다.
ko039 | NEW | ko074 | 0.04 | · · 이 질문을 저장 자료에 적용하기 위해 분석 단위를 세 가지로 나눴다.
ko040 | SAME | ko039 | 1.00 | 참조 코드 쌍에는 위반 예시와 그 수정 예시가 들어 있고, 저장 응답에는 모델에 제출된 코드와 프롬프트, 기록된 응답이 들어 있다.
ko041 | SAME | ko040 | 1.00 | 프롬프트 틀은 저장 프롬프트에 정확히 한 번 나오는 제출 코드를 공통 자리표시자로 치환해 얻었다.
ko042 | SAME | ko041 | 1.00 | 저장 응답의 제출 코드를 모든 참조 쌍의 수정 전·후 소스와 대조했다.
ko043 | SAME | ko042 | 1.00 | 각 문자열을 그대로 비교한 뒤 양끝 공백을 제거해 다시 비교했다.
ko044 | SAME | ko043 | 1.00 | Python 참조 쌍은 구문 트리로 파싱해 최상위 클래스의 메서드 선언 이름을 비교했다.
ko045 | SAME | ko044 | 1.00 | 상속에 따른 호출 가능성, 실제 사용 여부, 보장의 범위는 별도 근거가 필요한 질문이다.
ko046 | SAME | ko045 | 1.00 | 이 연구에서 작성한 도서관·도형 재현은 §5와 §6에서 정한 조건으로 실행했다.
ko047 | SAME | ko046 | 1.00 | ZIP 안의 공개 재현 패키지 코드는 실행하지 않았다.
ko048 | SAME | ko047 | 1.00 | 아카이브 식별 정보와 확인 명령은 부록 A에 있다.
ko049 | SAME | ko048 | 1.00 | · Pehlivan 등은 위반 시나리오를 정하고, 생성한 코드 예시를 수정·검증한 뒤 의견이 갈린 사례의 참조 라벨을 논의로 정했다.
ko050 | SAME | ko049 | 1.00 | SOLID 위반을 식별하는 모델 응답은 그 라벨과 대조했다.
ko051 | SAME | ko050 | 1.00 | OCP에 해당하는 아카이브에는 참조 쌍 48개와 저장 응답 768건이 있다.
ko052 | SAME | ko051 | 1.00 | 저장 프롬프트에서 제출 코드를 가렸을 때 서로 다른 문자열 24개가 남았고, 네 전략 사이에 동일한 틀은 없었다.
ko053 | SAME | ko052 | 1.00 | 각 사례의 변경 요구나 기존 호출자 계약을 따로 밝힌 틀은 없었다.
ko054 | SAME | ko053 | 1.00 | 이는 벤치마크가 본래 수행하려는 분류 과제를 잘못 설계했다는 뜻이 아니다.
ko055 | SAME | ko054 | 1.00 | 특정 수정안을 승인하거나 거절하는 데 이 분류 결과를 사용하려면 추가 증거가 필요하다는 뜻이다.
ko056 | SAME | ko055 | 1.00 | 저장된 Python EXAMPLE 지시는 다형성으로 처리할 만한 반복 분기를 찾도록 한다.
ko057 | SAME | ko056 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko058 | SAME | ko057 | 1.00 | 그 분기를 보면 새 도형을 추가할 때 어디에 손댈지 짐작할 수 있다.
ko059 | SAME | ko058 | 1.00 | 새 도형 추가가 실제 요청인지, 사각형의 너비를 직접 읽는 호출을 계속 지원해야 하는지는 이 지시문에서 확인되지 않는다.
ko060 | SAME | ko059 | 1.00 | 별도의 참조 쌍 37번은 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko061 | SAME | ko060 | 1.00 | 원본 문자열과 양끝 공백을 제거한 문자열을 대조했을 때, 저장된 제출 코드와 참조 쌍의 어느 쪽도 일치하지 않았다.
ko062 | SAME | ko061 | 1.00 | 따라서 여기서 근거로 삼는 것은 참조 쌍에서 확인한 선언의 변화다.
ko063 | SAME | ko062 | 1.00 | 그 변화가 수정안을 거절할 이유가 되려면 호출자가 너비를 읽는 동작까지 보장받았는지 확인해야 한다.
ko064 | NEW | ko061 | 0.05 | 이 참조 쌍에 실제 호출자가 있었다고 주장하지는 않는다.
ko065 | NEW | ko073 | 0.04 | 대신 해당 문제가 판정에 영향을 줄 수 있는지 별도로 구성한 수정안에서 시험한다.
ko066 | SAME | ko064 | 1.00 | 프롬프트 예시는 저장 JSONL 13행(ID 12)이다.
ko067 | SAME | ko065 | 1.00 | 참조 쌍 37번은 별도의 ground truth JSON 위치다.
ko068 | SAME | ko066 | 1.00 | · · · 마이어의 예를 바탕으로 작은 도서관 목록 프로그램을 만들었다.
ko069 | SAME | ko067 | 1.00 | 검토할 수정안은 기술보고서를 처리하는 모듈을 추가한다.
ko070 | SAME | ko068 | 1.00 | 기존 소스 파일 두 개는 바이트 단위로 그대로다.
ko071 | SAME | ko069 | 1.00 | 실행하면 기술보고서는 출력되고 정오표는 여전히 거절된다.
ko072 | SAME | ko070 | 1.00 | 기존 책 출력의 접두어는 book 에서 BOOK 으로 바뀐다.
ko073 | SAME | ko071 | 1.00 | 기존 파일을 수정하지 않았다는 사실은 기존 호출 결과까지 보존했다는 뜻이 아니다.
ko074 | SAME | ko072 | 1.00 | 변경된 동작은 우리가 만든 실행 예제에서 관찰했다.
ko075 | SAME | ko073 | 1.00 | 수정안과 실행 결과, 새 모듈을 추가할 수 있는 편집 범위를 고정했다.
ko076 | SAME | ko074 | 1.00 | 새 요구는 기술보고서만 지원하는 경우와 정오표까지 지원하는 경우로 나눴다.
ko077 | SAME | ko075 | 1.00 | 두 계약은 모두 학술지와 학회록의 출력, 그리고 별개의 미지원 자료 유형을 거절하는 동작을 보호한다.
ko078 | SAME | ko076 | 1.00 | 표 2의 승인은 새 요구와 보호할 계약을 모두 충족한 경우다.
ko079 | SAME | ko077 | 1.00 | 기술보고서만 필요하고 책 접두어를 보호하지 않는 경우에 승인된다.
ko080 | SAME | ko078 | 1.00 | 정오표가 필수라는 사실을 알면 책 접두어 계약을 모르더라도 거절할 수 있다.
ko081 | SAME | ko079 | 1.00 | 기술보고서만 필요하다는 사실을 알 때는 책 접두어를 보장했는지가 결론을 가른다.
ko082 | SAME | ko080 | 1.00 | 별도로 만든 수정안은 같은 편집 범위에서 새 모듈 하나를 추가해 두 자료 유형을 처리하고 모든 보호 동작을 지켰다.
ko083 | SAME | ko081 | 1.00 | 판정에 필요한 정보가 일부만 주어지면, 그 정보와 양립하는 명세들을 비교할 수 있다.
ko084 | SAME | ko082 | 1.00 | 모든 명세가 같은 판정을 내리면 그 판정을 내릴 수 있다.
ko085 | SAME | ko083 | 1.00 | 서로 다른 판정이 나오면 조건마다 결론을 밝히거나, 어느 조건이 실제로 적용되는지 확인할 때까지 보류할 수 있다.
ko086 | SAME | ko084 | 1.00 | 이 논증은 실제 명세가 검토 중인 집합에 들어 있어 그 집합이 비어 있지 않다는 전제에서 성립한다.
ko087 | SAME | ko085 | 1.00 | 이때 한 가지 입력만 받아 언제나 승인 또는 거절 중 하나를 출력하는 규칙은, 서로 다른 정답이 남아 있는 두 조건을 동시에 맞힐 수 없다.
ko088 | SAME | ko086 | 1.00 | 다만 이 논증만으로 SOLID의 다른 정리나 실제 현장의 판단 오류율을 추정할 수는 없다.
ko089 | SAME | ko087 | 1.00 | 부록 A에는 이번 사례에서 검토한 정보 공개 조건 아홉 개가 있다.
ko090 | NEW | ko088 | 0.19 | · 도서관 실험에서 확인한 것은 주어진 수정안의 적격성이었다.
ko091 | NEW | ko073 | 0.06 | 다른 수정안이 더 적은 비용으로 같은 요구를 처리할 수 있는지는 아직 별도 문제다.
ko092 | NEW | ko089 | 0.18 | 도형 예제로 돌아가, 어떤 변경에 대비할지와 새 기능을 어디에서 호출할지에 따라 기존 파일을 얼마나 수정하는지 비교한다.
ko093 | NEW | ko090 | 0.13 | 여기서 세는 것은 실행한 후보들의 수정 파일 수이지 가능한 구현 전체의 최솟값이 아니다.
ko094 | SAME | ko091 | 1.00 | 도형별 배치에서는 삼각형을 새 파일 하나로 추가했고, 이름표 연산을 추가할 때는 원과 사각형의 파일을 고쳤다.
ko095 | SAME | ko092 | 1.00 | 연산별 배치에서는 반대로 삼각형을 추가할 때 그리기 파일을 고쳤고, 이름표 연산은 새 파일에 뒀다.
ko096 | SAME | ko093 | 1.00 | 네 수정안이 모두 기능 검사를 통과했지만 기존 파일을 덜 건드리는 배치는 요구에 따라 달랐다(그림 1A).
ko097 | SAME | ko094 | 1.00 | 두 번째 비교에서는 같은 배치 렌더링 함수를 추가했다.
ko098 | SAME | ko095 | 1.00 | 이 함수는 도형 목록을 받아 각 렌더링 결과를 대괄호로 감싼다.
ko099 | SAME | ko096 | 1.00 | 도형별 배치에서 변환을 각 도형 파일이 맡아야 하면 원과 사각형 파일을 고친다.
ko100 | SAME | ko097 | 1.00 | 공용 어댑터를 허용하면 두 배치 모두 새 파일 하나로 기능을 제공할 수 있다고 예측했다.
ko101 | SAME | ko098 | 1.00 | 실행한 네 후보는 모두 입력 순서와 중복을 보존하고 빈 목록과 미지원 도형을 명세대로 처리했다.
ko102 | SAME | ko099 | 1.00 | 각 후보는 원과 사각형의 기존 렌더링을 유지했다.
ko103 | SAME | ko100 | 1.00 | 기존 파일 두 개를 고친 것은 도형 파일이 변환을 맡은 후보뿐이었다.
ko104 | SAME | ko101 | 1.00 | 네 후보 모두 새 파일 하나를 추가했다(그림 1B).
ko105 | SAME | ko102 | 1.00 | A는 삼각형 추가와 이름표 연산 추가를 비교한다.
ko106 | SAME | ko103 | 1.00 | B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다.
ko107 | SAME | ko104 | 1.00 | B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.
ko108 | SAME | ko105 | 1.00 | · · · · 세 번째 비교에서는 배치 함수 대신 기존 렌더링의 결과 하나를 선택적으로 감싸는 옵션을 사용했다.
ko109 | SAME | ko106 | 1.00 | 새 모듈을 호출할 수 있는 경우에는 두 배치가 기존 파일을 그대로 뒀다.
ko110 | SAME | ko107 | 1.00 | 같은 모듈을 추가한 상태에서 기존 함수에 bracketed=True 를 넘기면 함수는 그 인자를 받지 못했다.
ko111 | SAME | ko108 | 1.00 | 기존 함수로 옵션을 제공한 후보는 연산별 배치에서 파일 하나, 도형별 배치에서 두 개를 고쳤다.
ko112 | SAME | ko109 | 1.00 | 기존 함수가 외부 변환 모듈을 불러올 수 있도록 이미 구성된 별도 기준선에서는 두 배치 모두 새 파일 하나를 추가해 기존 호출 경로로 옵션을 제공했다(표 3).
ko113 | SAME | ko110 | 1.00 | 확장 지점은 세 번째 행의 기준선에 이미 있었다.
ko114 | SAME | ko111 | 1.00 | 따라서 이 행의 0개를 첫 설계에서 확장 지점을 처음 만드는 비용까지 포함한 결과로 읽어서는 안 된다.
ko115 | SAME | ko112 | 1.00 | 여기서는 확장 지점이 도입된 비용을 별도로 측정하지 않았다.
ko116 | SAME | ko113 | 1.00 | 같은 어댑터를 추가해도 기존 함수에서는 옵션을 쓸 수 없었던 대조 실행을 포함했다.
ko117 | NEW | ko090 | 0.11 | · 기존 파일 수정 수가 적다는 사실만으로 변경에 더 잘 대응하는 설계라고 할 수는 없다.
ko118 | SAME | ko114 | 1.00 | 새 파일을 추가할 수 있어도 그 파일이 실행되려면 호출자가 쓸 수 있는 경로가 필요하다.
ko119 | SAME | ko115 | 1.00 | 표 3의 마지막 행은 확장 지점이 이미 있는 상태에서 이후에 고친 파일만 센다.
ko120 | SAME | ko116 | 1.00 | 여기에 든 수정 수는 실행한 후보에 관한 관찰이다.
ko121 | SAME | ko117 | 1.00 | 독립적으로 작성한 요구에서도 어떤 경로가 작동할지 예측할 수 있는지, 파일 수정 수가 실제 유지보수 부담과 어떻게 연결되는지는 남은 질문이다.
ko122 | SAME | ko118 | 1.00 | 서론의 그리기 함수가 잘못됐는지는 정렬을 누가 맡았는지에 달려 있었다.
ko123 | SAME | ko119 | 1.00 | 벤치마크는 모델의 응답을 참조 라벨과 대조해 분류 성능을 잰다.
ko124 | SAME | ko120 | 1.00 | 그 판정을 구체적인 수정안에 적용하려면 어떤 기능이 필요한지, 어떤 동작을 기존 호출자에게 약속했는지를 확인해야 한다.
ko125 | SAME | ko121 | 1.00 | 도서관 예제에서는 정오표 요구만으로 수정안을 거절할 수 있었다.
ko126 | SAME | ko122 | 1.00 | 기술보고서만 필요한 경우에는 책 접두어 계약이 결론을 갈랐다.
ko127 | SAME | ko123 | 1.00 | 어떤 수정안이 가능한지를 비교할 때는 호출자가 새 동작을 받을 수 있는 경로도 확인해야 한다.
ko128 | SAME | ko124 | 1.00 | 검토 의견으로 변경을 요구하려면 어느 요구나 계약을 근거로 삼았는지, 어느 호출 경로에 적용되는지를 밝힐 수 있어야 한다.
ko129 | SAME | ko125 | 1.00 | 그러면 개발자는 이미 내려진 결론의 근거를 확인하거나, 보류된 판정을 가를 사실을 더 찾을 수 있다.
ko130 | SAME | ko126 | 1.00 | 이 결과는 한 벤치마크의 저장 자료와 여기서 구성해 실행한 후보의 범위에서 성립한다.
ko131 | SAME | ko127 | 1.00 | 여기서 더 나아가려면 SOLID를 대체할 공리를 선언하기보다, 어떤 변경과 계약, 권한과 호출 경로가 주어졌을 때 설계의 유불리가 어떻게 달라지는지 예측할 수 있는 표현을 찾아야 한다.
ko132 | SAME | ko128 | 1.00 | 그런 표현이 실제 독립 요구에서도 작동한다면, 익숙한 원칙이 유용한 이유뿐 아니라 그 조언을 따르지 않는 설계가 더 나은 조건도 설명할 수 있을 것이다.
ko133 | SAME | ko129 | 1.00 | 이 가능성은 이번 논문의 결과가 아니라 다음에 검증할 가설로 남긴다.
ko134 | SAME | ko130 | 1.00 | §3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다.
ko135 | SAME | ko131 | 1.00 | §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다.
ko136 | SAME | ko132 | 1.00 | 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다.
ko137 | SAME | ko133 | 1.00 | 그림 1의 소스와 출력 위치는 그림 캡션에 있다.
Summary ko: same 121; edited 0; new 16.

### EN (145 sentences; prior 144)
en001 | SAME | en001 | 1.00 | In 1996, Robert Martin described a function that drew the shapes in a list in order.
en002 | SAME | en002 | 1.00 | A triangle could be added without editing the function if the triangle supplied its own drawing operation.
en003 | SAME | en003 | 1.00 | Martin then introduced a new requirement.
en004 | SAME | en004 | 1.00 | Every circle had to be drawn before any square.
en005 | SAME | en005 | 1.00 | Given a list that begins with a square, the same function still draws the square first.
en006 | SAME | en006 | 1.00 | Who is responsible for sorting the list?
en007 | SAME | en007 | 1.00 | If the caller must pass a sorted list, the drawing function can stay as it is.
en008 | SAME | en008 | 1.00 | If the function must produce the required order for any input list, the current code falls short.
en009 | SAME | en009 | 1.00 | A reviewer can see that the function does no sorting.
en010 | SAME | en010 | 1.00 | To take that fact as evidence of an open–closed principle (OCP) violation, the reviewer also needs to know who was meant to sort the shapes.
en011 | SAME | en011 | 1.00 | The difficulty is not simply whether the principle is sound.
en012 | SAME | en012 | 1.00 | In Martin's example, a designer must first identify the changes against which a routine ought to remain closed.
en013 | SAME | en013 | 1.00 | If that situated judgment is later used as a violation label without its premise, the label may carry the authority of a rule while omitting the reason for applying it.
en014 | SAME | en014 | 1.00 | We call this risk the over-axiomatization of design advice.
en015 | SAME | en015 | 1.00 | It is a question about how conditional advice is used, not a demonstrated history of the entire SOLID family.
en016 | NEW | en013 | 0.14 | The distinction becomes consequential when a violation label is treated as a reason to reject a particular edit.
en017 | NEW | en131 | 0.16 | A classification benchmark can show which instructions and examples were presented to a model; it cannot by itself settle the obligations of a separate maintenance request.
en018 | NEW | en018 | 0.22 | We inspect one such archive and then construct a fixed-patch comparison in which the new demand and the commitment to existing callers vary.
en019 | NEW | en120 | 0.15 | We also examine the routes by which a new behavior reaches the original callers, since an edit that can be written in a new file is not necessarily available through their existing entry points.
en020 | SAME | en020 | 1.00 | · · Martin opens his 1996 article by attributing the principle to Bertrand Meyer and citing page 23 of the 1988 first edition.
en021 | SAME | en021 | 1.00 | We examine this explicit citation link to recover the conditions under which OCP was argued for; it is not, by itself, a genealogy of all five SOLID principles.
en022 | SAME | en022 | 1.00 | A closed module in Meyer’s account is one that other modules can use on the basis of a stable specification.
en023 | SAME | en023 | 1.00 | If a library program distinguishes publication types one by one, adding technical reports can require edits to existing modules or recompiling them.
en024 | SAME | en024 | 1.00 | The designer must consider both where the new behavior can live and what existing users of the module can continue to rely on.
en025 | SAME | en025 | 1.00 | Martin assigned sorting to DrawAllShapes .
en026 | SAME | en026 | 1.00 | In the first implementation, Circle::Precedes inspected the other shape and put the circle first if it was a square.
en027 | SAME | en027 | 1.00 | The code that decided how a new shape would rank against a circle already lived in Circle .
en028 | SAME | en028 | 1.00 | Martin then moved the order of shape types into a table.
en029 | SAME | en029 | 1.00 | Putting squares first now requires swapping two entries.
en030 | SAME | en030 | 1.00 | Ordering individual shapes by area, for example, would require information outside the table.
en031 | SAME | en031 | 1.00 | Which part of the program can stay as it is depends on the change it must accommodate.
en032 | SAME | en032 | 1.00 | Whether a type check supports a violation finding also depends on the function’s obligation.
en033 | SAME | en033 | 1.00 | Later in the article, Martin presents two further functions that use dynamic_cast .
en034 | SAME | en034 | 1.00 | DrawAllShapes recognizes and draws circles and squares.
en035 | SAME | en035 | 1.00 | DrawSquaresOnly selects squares from the list and draws them.
en036 | SAME | en036 | 1.00 | Given a triangle, both skip it.
en037 | SAME | en037 | 1.00 | A function that promises to draw every shape has omitted an output, while a function that promises to draw squares has met its obligation.
en038 | SAME | en038 | 1.00 | We turn to saved classification prompts to see how much of that kind of obligation the reviewer could establish from the input.
en039 | NEW | en039 | 0.28 | Both functions contain type checks; their different obligations account for the different judgments.
en040 | NEW | en068 | 0.18 | Before assessing whether the saved prompts convey comparable obligations, we describe how we distinguished the reference examples from the submissions and instructions archived for the models.
en041 | NEW | en043 | 0.31 | · · To separate the obligations inferable from the inputs from the labels assigned by the benchmark, we distinguish three units in the archive.
en042 | SAME | en044 | 1.00 | A reference pair contains a violation example and its revision.
en043 | SAME | en045 | 1.00 | A saved response record contains the code submitted to the model, its prompt, and the recorded response.
en044 | SAME | en046 | 1.00 | We recover a prompt template by replacing the single exact occurrence of the submitted code with a common placeholder.
en045 | SAME | en047 | 1.00 | We compare templates as strings.
en046 | SAME | en048 | 1.00 | We compared each saved submission with the source on both sides of every reference pair, first as stored and again after trimming whitespace from both ends.
en047 | SAME | en049 | 1.00 | For Python reference pairs we parsed the syntax trees and compared names of methods declared in top-level classes, excluding names that begin with an underscore.
en048 | SAME | en050 | 1.00 | The comparison captures declaration changes.
en049 | SAME | en051 | 1.00 | Inherited availability, actual client use, and whether that use was protected each require separate evidence.
en050 | SAME | en052 | 1.00 | We ran the library and drawing fixtures built for this study under the conditions given in Sections 5 and 6.
en051 | SAME | en053 | 1.00 | We executed no code from the archived replication package.
en052 | SAME | en054 | 1.00 | Appendix A identifies the archive and the commands needed to reproduce the checks.
en053 | SAME | en055 | 1.00 | · Pehlivan et al. specified violation scenarios and refined and checked the generated examples.
en054 | SAME | en056 | 1.00 | They resolved disagreements about reference labels through discussion, then compared model classifications of SOLID violations with those labels.
en055 | SAME | en057 | 1.00 | The OCP archive contains 48 reference pairs and 768 saved response records.
en056 | SAME | en058 | 1.00 | Masking the submitted code yielded 24 distinct template strings, with no exact template shared across the four strategies.
en057 | SAME | en059 | 1.00 | None of the templates separately states a change request or a protected caller contract for an individual case.
en058 | SAME | en060 | 1.00 | That absence is not a defect in a benchmark whose stated task is classification.
en059 | SAME | en061 | 1.00 | It matters when the resulting label is asked to justify an engineering decision outside that task.
en060 | SAME | en062 | 1.00 | One saved Python EXAMPLE prompt points the reviewer to repeated branches where polymorphism would fit.
en061 | SAME | en063 | 1.00 | The submitted AreaCalculator checks the shape type before calculating the area of a circle or rectangle.
en062 | SAME | en064 | 1.00 | The branch suggests where an edit might go if a new shape is added.
en063 | SAME | en065 | 1.00 | The instruction leaves open whether anyone has requested that change and whether existing calls that read a rectangle’s width must still be supported.
en064 | SAME | en066 | 1.00 | In a separate reference pair, number 37, the revision moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en065 | SAME | en067 | 1.00 | No saved submission matched either side of the reference pairs in the exact or outer-whitespace-trimmed comparison.
en066 | SAME | en068 | 1.00 | Our evidence for the missing declaration comes from comparing the reference sources.
en067 | SAME | en069 | 1.00 | To argue that its removal warrants rejecting a patch, a reviewer would need to establish that callers were guaranteed access to the width.
en068 | NEW | en108 | 0.09 | We do not infer that a real caller used the deleted getter.
en069 | NEW | en139 | 0.17 | Instead, a separate executable fixture tests whether varying a protected commitment can change the verdict on a fixed edit.
en070 | SAME | en071 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en071 | SAME | en072 | 1.00 | The saved prompt is on JSONL line 13 (record ID 12).
en072 | SAME | en073 | 1.00 | Reference pair 37 is in a separate ground-truth JSON file. 768 counts saved records.
en073 | SAME | en074 | 1.00 | · · · Following Meyer’s example, we built a small library catalog.
en074 | SAME | en075 | 1.00 | The proposed patch adds a module for technical reports.
en075 | SAME | en076 | 1.00 | The two existing source files remain byte-for-byte identical.
en076 | SAME | en077 | 1.00 | In execution, technical reports render and requests for errata are still rejected.
en077 | SAME | en078 | 1.00 | The prefix in an existing book’s output changes from book to BOOK .
en078 | SAME | en079 | 1.00 | The identity of the old source files therefore does not imply the preservation of every observable result; we verified the latter separately in our fixture.
en079 | SAME | en080 | 1.00 | We hold the patch, its observed behavior, and the boundary permitting new modules fixed.
en080 | SAME | en081 | 1.00 | The new requirement covers either technical reports alone or both technical reports and errata.
en081 | SAME | en082 | 1.00 | Both legacy contracts protect the rendering of journals and proceedings and require rejection of a separate unsupported type.
en082 | SAME | en083 | 1.00 | The broader contract also protects the original book prefix.
en083 | SAME | en084 | 1.00 | An acceptable candidate in Table 2 must meet both the new requirement and the applicable contract.
en084 | SAME | en085 | 1.00 | Two independent conditions for the same patch.
en085 | SAME | en086 | 1.00 | The patch is acceptable when only technical reports are required and the book prefix is outside the contract.
en086 | SAME | en087 | 1.00 | Knowing that errata are required suffices to reject it even before the prefix contract is known.
en087 | SAME | en088 | 1.00 | If only technical reports are required, the verdict turns on whether callers were promised the original prefix.
en088 | SAME | en089 | 1.00 | A separate patch adds one module within the same edit boundary, handles both new types, and preserves every protected observation.
en089 | SAME | en090 | 1.00 | With partial information, the reviewer can consider the specifications still compatible with the evidence.
en090 | SAME | en091 | 1.00 | If all give the same verdict, the reviewer can issue it.
en091 | SAME | en092 | 1.00 | If they disagree, the reviewer can give conditional verdicts or defer until the applicable specification can be established.
en092 | SAME | en093 | 1.00 | This argument assumes that the actual specification is in the compatible set, so the set is nonempty.
en093 | SAME | en094 | 1.00 | A rule that sees the same input and must always return a single binary verdict cannot be correct for two compatible specifications that require opposite answers.
en094 | SAME | en095 | 1.00 | This establishes an information limit, not an error rate for SOLID judgments in practice.
en095 | SAME | en096 | 1.00 | Appendix A gives the nine disclosure conditions for this case.
en096 | NEW | en059 | 0.16 | · Section 5 established whether one patch met a stated request and contract.
en097 | NEW | en124 | 0.09 | It did not determine the least costly way to meet them.
en098 | NEW | en098 | 0.25 | Returning to the drawing fixture, we ask which source boundaries the implemented candidates cross when the request, permitted placement, or caller route changes.
en099 | NEW | en128 | 0.28 | The counts describe those candidates, not a minimum over all possible implementations.
en100 | SAME | en100 | 1.00 | We first varied the request.
en101 | SAME | en101 | 1.00 | In the shape layout we added a triangle in one new file and edited the circle and square files to add a labeling operation.
en102 | SAME | en102 | 1.00 | In the operation layout we edited the drawing file to add the triangle and put the labeling operation in a new file.
en103 | SAME | en103 | 1.00 | All four candidates passed their functional checks.
en104 | SAME | en104 | 1.00 | Which layout left more existing files intact depended on the request (Figure 1A).
en105 | SAME | en105 | 1.00 | We then added the same batch-rendering function to both layouts.
en106 | SAME | en106 | 1.00 | It takes a list of shapes and brackets each rendered result.
en107 | SAME | en107 | 1.00 | We predicted that requiring the item transformation to live in the shape files would entail editing both files in the shape layout.
en108 | SAME | en108 | 1.00 | If a shared adapter was allowed, we predicted that either layout could add the feature in one new file.
en109 | SAME | en109 | 1.00 | All four candidates preserved order and duplicates, handled empty lists and unsupported shapes as specified, and preserved the existing circle and square renderings.
en110 | SAME | en110 | 1.00 | The candidate placing both transformations in the shape files edited two existing files.
en111 | SAME | en111 | 1.00 | All four added one file (Figure 1B).
en112 | SAME | en112 | 1.00 | Existing source files edited.
en113 | SAME | en113 | 1.00 | Panel A compares adding a triangle with adding a labeling operation.
en114 | SAME | en114 | 1.00 | Panel B holds the batch-rendering request fixed and varies the placement rule.
en115 | SAME | en115 | 1.00 | All four candidates in panel B passed the new and legacy behavior checks and added one file each.
en116 | SAME | en116 | 1.00 | · · · · The third comparison used an option to bracket a single rendering through the existing function.
en117 | SAME | en117 | 1.00 | Candidates that offered a new entry point left the existing files intact in both layouts.
en118 | SAME | en118 | 1.00 | With the same adapter added, the original functions still rejected bracketed=True .
en119 | SAME | en119 | 1.00 | The candidates offering the option through the original functions edited one file in the operation layout and two in the shape layout.
en120 | SAME | en120 | 1.00 | In a separate baseline whose original function could already load an external decorator, each layout delivered the option through the original entry point by adding a single file (Table 3).
en121 | SAME | en121 | 1.00 | Call paths for the new rendering option.
en122 | SAME | en122 | 1.00 | The hook was already present in the last row’s baseline.
en123 | SAME | en123 | 1.00 | Its zero-edits result does not include the cost of introducing that hook into the earlier baseline.
en124 | SAME | en124 | 1.00 | We did not measure that initial investment.
en125 | SAME | en125 | 1.00 | The negative control adds the same adapter and finds that the option remains unavailable through the original function.
en126 | NEW | en141 | 0.12 | · Fewer changed files do not by themselves establish a more maintainable design.
en127 | EDIT | en126 | 0.87 | Permission to add a file needs to be paired with a path that the caller can actually use.
en128 | SAME | en127 | 1.00 | The last row of Table 3 starts counting after the hook is already in place.
en129 | SAME | en128 | 1.00 | These file counts describe the tested candidates.
en130 | SAME | en129 | 1.00 | Whether we can predict working paths for independently authored requests, and how these counts relate to maintenance effort, remain open.
en131 | SAME | en130 | 1.00 | Whether the drawing routine falls short depends on who must sort the list.
en132 | SAME | en131 | 1.00 | The benchmark measures classification performance by comparing model responses with its reference labels.
en133 | SAME | en132 | 1.00 | Applying a finding to a specific patch also requires knowing what change the patch must deliver and which behavior existing callers were promised.
en134 | SAME | en133 | 1.00 | In the catalog example, the errata requirement can settle a rejection on its own.
en135 | SAME | en134 | 1.00 | When only technical reports are needed, the verdict turns on the promise about the book prefix.
en136 | SAME | en135 | 1.00 | Comparing possible edits also requires knowing how the new behavior can reach its callers.
en137 | SAME | en136 | 1.00 | A review that calls for an edit should identify the request or commitment it relies on and the call path to which it applies.
en138 | SAME | en137 | 1.00 | The developer can then check the grounds for the verdict or identify the remaining fact that would settle it.
en139 | SAME | en138 | 1.00 | The evidence here covers the saved material of one benchmark and the candidates we constructed and ran.
en140 | SAME | en139 | 1.00 | Rather than announce a new set of axioms, the next step is to ask whether changes, protected commitments, authority, and caller routes can be represented in a form that predicts when one design has an advantage over anot
en141 | SAME | en140 | 1.00 | Such an account would be valuable if it explained both the usefulness of familiar principles and the conditions under which their preferred design loses.
en142 | SAME | en141 | 1.00 | The present paper poses that hypothesis; it does not establish it.
en143 | SAME | en142 | 1.00 | For Sections 3–4 the audit reads the archived JSON and JSONL.
en144 | SAME | en143 | 1.00 | For Sections 5–6 the fixtures run the examples constructed for this study.
en145 | SAME | en144 | 1.00 | The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.
Summary en: same 130; edited 1; new 14.

## v06 · [Notion](https://app.notion.com/p/41bef561cf92816d8046c0412661621c)
### KO (150 sentences; prior 137)
ko001 | SAME | ko001 | 1.00 | 로버트 마틴은 1996년 글에서 도형 목록을 받아 차례로 그리는 함수를 예로 들었다.
ko002 | SAME | ko002 | 1.00 | 삼각형이 자신을 그리는 동작을 제공하면, 그 함수를 고치지 않고도 삼각형을 추가할 수 있었다.
ko003 | SAME | ko003 | 1.00 | 같은 함수에 사각형으로 시작하는 목록을 주면 여전히 사각형부터 그린다.
ko004 | SAME | ko004 | 1.00 | 원을 먼저 그리려면 누가 목록을 정렬해야 할까?
ko005 | SAME | ko005 | 1.00 | 호출자가 정렬한 목록을 넘기기로 했다면 그리기 함수는 그대로 둘 수 있다.
ko006 | SAME | ko006 | 1.00 | 어떤 목록을 받아도 함수가 순서를 보장하기로 했다면 지금 코드로는 부족하다.
ko007 | SAME | ko007 | 1.00 | 소스 코드를 읽으면 함수가 정렬하지 않는다는 사실을 알 수 있다.
ko008 | SAME | ko008 | 1.00 | 그 사실을 개방–폐쇄 원칙(OCP) 위반의 근거로 삼으려면 정렬을 누가 맡았는지도 알아야 한다.
ko009 | SAME | ko009 | 1.00 | 여기에는 설계 원칙 자체보다 그 원칙을 사용하는 방식에 관한 문제가 있다.
ko010 | SAME | ko010 | 1.00 | 마틴의 사례에서는 앞으로 어떤 변화에 대비할지를 정해야 비로소 어떤 코드를 닫아 둘지 논의할 수 있었다.
ko011 | SAME | ko011 | 1.00 | 그 판단을 변경 요구가 빠진 ‘위반’ 판정으로 바꿔 사용한다면, 처음에는 결론을 정당화했던 전제가 사라진다.
ko012 | SAME | ko012 | 1.00 | 우리는 이 위험을 원칙의 ‘과도한 공리화’라고 부른다.
ko013 | SAME | ko013 | 1.00 | 이것은 SOLID 전체가 무효하다는 역사적 결론이 아니라, 조건부 설계 조언을 무조건적인 탈락 기준처럼 적용할 때 무엇을 잃는지 묻는 문제 제기다.
ko014 | SAME | ko014 | 1.00 | 이 문제를 따지려면 ‘위반’이라고 분류하는 일과 특정 수정안을 거절하는 일을 먼저 나눠야 한다.
ko015 | SAME | ko015 | 1.00 | SOLID 위반 분류 벤치마크의 저장 자료는 모델이 어떤 근거를 받았는지 보여 주지만, 특정 유지보수 요청이 승인되어야 하는지까지 판정하지는 않는다.
ko016 | SAME | ko016 | 1.00 | 우리는 별도로 만든 도서관 프로그램에서 같은 수정안을 서로 다른 요구와 기존 호출자 계약 아래 두어 그 간격을 검사한다.
ko017 | SAME | ko017 | 1.00 | 수정안 자체의 수용 여부를 따진 다음에는, 새로운 기능이 실제 호출 경로에 도달하도록 만드는 일이 어느 기존 파일을 바꾸게 하는지도 비교한다.
ko018 | SAME | ko018 | 1.00 | · · 마틴은 1996년 글의 첫머리에서 이 원칙을 베르트랑 마이어에게서 가져왔다고 밝히며 1988년 초판 23쪽을 인용한다.
ko019 | SAME | ko019 | 1.00 | 이어지는 두 사례를 다루는 이유는 SOLID 다섯 원칙의 기원을 한 줄로 연결하기 위해서가 아니라, OCP에 적용 조건이 명시되어 있었는지 살피기 위해서다.
ko020 | SAME | ko020 | 1.00 | 마이어의 설명에서 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 사용할 수 있는 모듈이다.
ko021 | NEW | ko054 | 0.03 | 1995년 6월 공개 토론에서 Kyle Brown은 잘못 설계된 클래스라면 개발자가 소스를 고쳐야 한다고 반박했다.
ko022 | NEW | ko073 | 0.06 | 마틴은 ‘닫혀 있다’는 말을 수정할 권한이 없다는 뜻이 아니라, 예상한 확장을 위해 기존 코드를 반드시 수정할 필요가 없다는 뜻으로 구분했다.
ko023 | NEW | ko029 | 0.06 | 그는 어떤 변경이 생길지 미리 알아야 한다는 어려움도 인정했다.
ko024 | NEW | ko013 | 0.02 | 이 논쟁은 OCP가 처음부터 단 하나의 무조건적 금지 명령으로 받아들여졌다고 가정하기 어렵게 한다.
ko025 | NEW | ko019 | 0.04 | 2007년에는 다섯 원칙을 묶은 SOLID라는 명칭이 공개 기록에 나타나고, 2009년의 인터페이스 논쟁에서는 내부 클래스와 공개 플러그인 API가 서로 다른 판단을 요구했다.
ko026 | NEW | ko117 | 0.03 | 이런 자료로 원칙의 전파와 수용 과정에 논쟁이 있었다는 점은 말할 수 있지만, 특정 약어나 자동화 도구가 조건을 탈락시켰다는 인과관계까지 증명할 수는 없다.
ko027 | SAME | ko021 | 1.00 | · 도서관 프로그램이 자료의 종류를 하나씩 구별해 처리한다면 기술보고서 한 종류를 추가하는 데도 기존 모듈의 수정이나 재컴파일이 필요할 수 있다.
ko028 | SAME | ko022 | 1.00 | 이때 설계자는 새 동작을 어디에 넣을지와 기존 사용자가 계속 어떤 동작에 의존할 수 있을지를 함께 고려하게 된다.
ko029 | SAME | ko023 | 1.00 | 마틴은 목록을 정렬하는 일을 DrawAllShapes 에 맡겼다.
ko030 | SAME | ko024 | 1.00 | 첫 구현에서는 Circle::Precedes 가 상대 도형을 검사해 사각형이면 원을 앞에 놓았다.
ko031 | SAME | ko025 | 1.00 | 새 도형이 들어왔을 때 원과 그 도형의 순서를 정하는 코드가 이미 Circle 안에 있었다.
ko032 | SAME | ko026 | 1.00 | 마틴은 이어서 도형 종류별 순서를 표로 옮겼다.
ko033 | SAME | ko027 | 1.00 | 이제 사각형을 원보다 먼저 그리라는 요청에는 표에서 두 항목의 위치를 바꾸면 된다.
ko034 | SAME | ko028 | 1.00 | 개별 도형의 넓이순으로 그리라는 요구를 가정하면 표에 없는 정보가 필요하다.
ko035 | SAME | ko029 | 1.00 | 어느 부분을 그대로 둘 수 있는지는 어떤 변경에 대비하느냐에 달려 있다.
ko036 | SAME | ko030 | 1.00 | 타입 검사가 위반의 근거가 되는지도 함수가 맡은 일에 달려 있다.
ko037 | SAME | ko031 | 1.00 | 글의 뒷부분에서 마틴은 dynamic_cast 를 쓰는 두 함수를 새로 제시한다.
ko038 | SAME | ko032 | 1.00 | 원과 사각형을 가려 그리는 DrawAllShapes 와 목록에서 사각형만 골라 그리는 DrawSquaresOnly 다.
ko039 | SAME | ko033 | 1.00 | 두 함수에 삼각형을 넣으면 어느 쪽도 그리지 않는다.
ko040 | SAME | ko034 | 1.00 | 모든 도형을 그리기로 한 함수에서는 빠진 출력이고, 사각형만 그리기로 한 함수에서는 약속한 동작이다.
ko041 | SAME | ko035 | 1.00 | 검토자가 어떤 근거로 두 경우를 구별할 수 있는지를 확인하려면, 실제로 받았던 코드와 지시를 구분해 살펴봐야 한다.
ko042 | SAME | ko036 | 1.00 | 두 함수는 같은 구문을 사용하지만, 약속한 일이 달라 평가가 갈린다.
ko043 | SAME | ko037 | 1.00 | 이 사례를 위반 여부의 판단으로 옮기려면 검토에 주어진 코드와 그 코드가 맡은 책임을 나눠야 한다.
ko044 | SAME | ko038 | 1.00 | 우리는 먼저 자료를 어떤 단위로 읽었는지 밝힌 뒤, 저장된 분류 프롬프트에서 그 책임을 어디까지 확인할 수 있는지 살펴본다.
ko045 | SAME | ko039 | 1.00 | · · 이 질문을 저장 자료에 적용하기 위해 분석 단위를 세 가지로 나눴다.
ko046 | SAME | ko040 | 1.00 | 참조 코드 쌍에는 위반 예시와 그 수정 예시가 들어 있고, 저장 응답에는 모델에 제출된 코드와 프롬프트, 기록된 응답이 들어 있다.
ko047 | SAME | ko041 | 1.00 | 프롬프트 틀은 저장 프롬프트에 정확히 한 번 나오는 제출 코드를 공통 자리표시자로 치환해 얻었다.
ko048 | SAME | ko042 | 1.00 | 저장 응답의 제출 코드를 모든 참조 쌍의 수정 전·후 소스와 대조했다.
ko049 | SAME | ko043 | 1.00 | 각 문자열을 그대로 비교한 뒤 양끝 공백을 제거해 다시 비교했다.
ko050 | SAME | ko044 | 1.00 | Python 참조 쌍은 구문 트리로 파싱해 최상위 클래스의 메서드 선언 이름을 비교했다.
ko051 | SAME | ko045 | 1.00 | 상속에 따른 호출 가능성, 실제 사용 여부, 보장의 범위는 별도 근거가 필요한 질문이다.
ko052 | SAME | ko046 | 1.00 | 이 연구에서 작성한 도서관·도형 재현은 §5와 §6에서 정한 조건으로 실행했다.
ko053 | SAME | ko047 | 1.00 | ZIP 안의 공개 재현 패키지 코드는 실행하지 않았다.
ko054 | SAME | ko048 | 1.00 | 아카이브 식별 정보와 확인 명령은 부록 A에 있다.
ko055 | SAME | ko049 | 1.00 | · Pehlivan 등은 위반 시나리오를 정하고, 생성한 코드 예시를 수정·검증한 뒤 의견이 갈린 사례의 참조 라벨을 논의로 정했다.
ko056 | SAME | ko050 | 1.00 | SOLID 위반을 식별하는 모델 응답은 그 라벨과 대조했다.
ko057 | SAME | ko051 | 1.00 | OCP에 해당하는 아카이브에는 참조 쌍 48개와 저장 응답 768건이 있다.
ko058 | SAME | ko052 | 1.00 | 저장 프롬프트에서 제출 코드를 가렸을 때 서로 다른 문자열 24개가 남았고, 네 전략 사이에 동일한 틀은 없었다.
ko059 | SAME | ko053 | 1.00 | 각 사례의 변경 요구나 기존 호출자 계약을 따로 밝힌 틀은 없었다.
ko060 | SAME | ko054 | 1.00 | 이는 벤치마크가 본래 수행하려는 분류 과제를 잘못 설계했다는 뜻이 아니다.
ko061 | SAME | ko055 | 1.00 | 특정 수정안을 승인하거나 거절하는 데 이 분류 결과를 사용하려면 추가 증거가 필요하다는 뜻이다.
ko062 | SAME | ko056 | 1.00 | 저장된 Python EXAMPLE 지시는 다형성으로 처리할 만한 반복 분기를 찾도록 한다.
ko063 | SAME | ko057 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko064 | SAME | ko058 | 1.00 | 그 분기를 보면 새 도형을 추가할 때 어디에 손댈지 짐작할 수 있다.
ko065 | SAME | ko059 | 1.00 | 새 도형 추가가 실제 요청인지, 사각형의 너비를 직접 읽는 호출을 계속 지원해야 하는지는 이 지시문에서 확인되지 않는다.
ko066 | SAME | ko060 | 1.00 | 별도의 참조 쌍 37번은 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko067 | NEW | ko054 | 0.02 | 이 사례가 분류 평가를 대표하는 유일한 방식은 아니다.
ko068 | NEW | ko009 | 0.04 | Bräuer 등(2018)은 설계 원칙을 측정 가능한 실천 규칙으로 옮길 때 전문가들이 보기에 무엇이 포착되고 무엇이 빠지는지 물었다.
ko069 | NEW | ko050 | 0.04 | Cabral 등(2024)은 구체적인 기계학습 확장 상황에서 SOLID 적용 전후 코드에 대한 참가자의 이해도와 확장 용이성 인식을 조사했다.
ko070 | NEW | ko053 | 0.04 | Zhu 등(2026)은 저장소 변경 요구에 기능 테스트와 구조적 판정 기준을 결합했다.
ko071 | NEW | ko012 | 0.02 | 세 연구는 각각 원칙의 측정 범위, 사용자의 인식, 특정 변경에서의 기능·구조 적합성 을 관찰한다.
ko072 | NEW | ko016 | 0.04 | 우리 비교의 결과 변수는 같은 패치가 명시된 요구와 계약 아래에서 승인 기준을 충족하는가다.
ko073 | NEW | ko085 | 0.05 | 앞선 연구를 코드 판정의 실패 사례로 취급하지 않으면서도, 무엇을 측정해야 어떤 결정을 정당화할 수 있는지 서로 다른 관점에서 확인할 수 있다.
ko074 | SAME | ko061 | 1.00 | · · 원본 문자열과 양끝 공백을 제거한 문자열을 대조했을 때, 저장된 제출 코드와 참조 쌍의 어느 쪽도 일치하지 않았다.
ko075 | SAME | ko062 | 1.00 | 따라서 여기서 근거로 삼는 것은 참조 쌍에서 확인한 선언의 변화다.
ko076 | SAME | ko063 | 1.00 | 그 변화가 수정안을 거절할 이유가 되려면 호출자가 너비를 읽는 동작까지 보장받았는지 확인해야 한다.
ko077 | SAME | ko064 | 1.00 | 이 참조 쌍에 실제 호출자가 있었다고 주장하지는 않는다.
ko078 | SAME | ko065 | 1.00 | 대신 해당 문제가 판정에 영향을 줄 수 있는지 별도로 구성한 수정안에서 시험한다.
ko079 | SAME | ko066 | 1.00 | 프롬프트 예시는 저장 JSONL 13행(ID 12)이다.
ko080 | SAME | ko067 | 1.00 | 참조 쌍 37번은 별도의 ground truth JSON 위치다.
ko081 | SAME | ko068 | 1.00 | · · · 마이어의 예를 바탕으로 작은 도서관 목록 프로그램을 만들었다.
ko082 | SAME | ko069 | 1.00 | 검토할 수정안은 기술보고서를 처리하는 모듈을 추가한다.
ko083 | SAME | ko070 | 1.00 | 기존 소스 파일 두 개는 바이트 단위로 그대로다.
ko084 | SAME | ko071 | 1.00 | 실행하면 기술보고서는 출력되고 정오표는 여전히 거절된다.
ko085 | SAME | ko072 | 1.00 | 기존 책 출력의 접두어는 book 에서 BOOK 으로 바뀐다.
ko086 | SAME | ko073 | 1.00 | 기존 파일을 수정하지 않았다는 사실은 기존 호출 결과까지 보존했다는 뜻이 아니다.
ko087 | SAME | ko074 | 1.00 | 변경된 동작은 우리가 만든 실행 예제에서 관찰했다.
ko088 | SAME | ko075 | 1.00 | 수정안과 실행 결과, 새 모듈을 추가할 수 있는 편집 범위를 고정했다.
ko089 | SAME | ko076 | 1.00 | 새 요구는 기술보고서만 지원하는 경우와 정오표까지 지원하는 경우로 나눴다.
ko090 | SAME | ko077 | 1.00 | 두 계약은 모두 학술지와 학회록의 출력, 그리고 별개의 미지원 자료 유형을 거절하는 동작을 보호한다.
ko091 | SAME | ko078 | 1.00 | 표 2의 승인은 새 요구와 보호할 계약을 모두 충족한 경우다.
ko092 | SAME | ko079 | 1.00 | 기술보고서만 필요하고 책 접두어를 보호하지 않는 경우에 승인된다.
ko093 | SAME | ko080 | 1.00 | 정오표가 필수라는 사실을 알면 책 접두어 계약을 모르더라도 거절할 수 있다.
ko094 | SAME | ko081 | 1.00 | 기술보고서만 필요하다는 사실을 알 때는 책 접두어를 보장했는지가 결론을 가른다.
ko095 | SAME | ko082 | 1.00 | 별도로 만든 수정안은 같은 편집 범위에서 새 모듈 하나를 추가해 두 자료 유형을 처리하고 모든 보호 동작을 지켰다.
ko096 | SAME | ko083 | 1.00 | 판정에 필요한 정보가 일부만 주어지면, 그 정보와 양립하는 명세들을 비교할 수 있다.
ko097 | SAME | ko084 | 1.00 | 모든 명세가 같은 판정을 내리면 그 판정을 내릴 수 있다.
ko098 | SAME | ko085 | 1.00 | 서로 다른 판정이 나오면 조건마다 결론을 밝히거나, 어느 조건이 실제로 적용되는지 확인할 때까지 보류할 수 있다.
ko099 | SAME | ko086 | 1.00 | 이 논증은 실제 명세가 검토 중인 집합에 들어 있어 그 집합이 비어 있지 않다는 전제에서 성립한다.
ko100 | SAME | ko087 | 1.00 | 이때 한 가지 입력만 받아 언제나 승인 또는 거절 중 하나를 출력하는 규칙은, 서로 다른 정답이 남아 있는 두 조건을 동시에 맞힐 수 없다.
ko101 | SAME | ko088 | 1.00 | 다만 이 논증만으로 SOLID의 다른 정리나 실제 현장의 판단 오류율을 추정할 수는 없다.
ko102 | SAME | ko089 | 1.00 | 부록 A에는 이번 사례에서 검토한 정보 공개 조건 아홉 개가 있다.
ko103 | SAME | ko090 | 1.00 | · 도서관 실험에서 확인한 것은 주어진 수정안의 적격성이었다.
ko104 | SAME | ko091 | 1.00 | 다른 수정안이 더 적은 비용으로 같은 요구를 처리할 수 있는지는 아직 별도 문제다.
ko105 | SAME | ko092 | 1.00 | 도형 예제로 돌아가, 어떤 변경에 대비할지와 새 기능을 어디에서 호출할지에 따라 기존 파일을 얼마나 수정하는지 비교한다.
ko106 | SAME | ko093 | 1.00 | 여기서 세는 것은 실행한 후보들의 수정 파일 수이지 가능한 구현 전체의 최솟값이 아니다.
ko107 | SAME | ko094 | 1.00 | 도형별 배치에서는 삼각형을 새 파일 하나로 추가했고, 이름표 연산을 추가할 때는 원과 사각형의 파일을 고쳤다.
ko108 | SAME | ko095 | 1.00 | 연산별 배치에서는 반대로 삼각형을 추가할 때 그리기 파일을 고쳤고, 이름표 연산은 새 파일에 뒀다.
ko109 | SAME | ko096 | 1.00 | 네 수정안이 모두 기능 검사를 통과했지만 기존 파일을 덜 건드리는 배치는 요구에 따라 달랐다(그림 1A).
ko110 | SAME | ko097 | 1.00 | 두 번째 비교에서는 같은 배치 렌더링 함수를 추가했다.
ko111 | SAME | ko098 | 1.00 | 이 함수는 도형 목록을 받아 각 렌더링 결과를 대괄호로 감싼다.
ko112 | SAME | ko099 | 1.00 | 도형별 배치에서 변환을 각 도형 파일이 맡아야 하면 원과 사각형 파일을 고친다.
ko113 | SAME | ko100 | 1.00 | 공용 어댑터를 허용하면 두 배치 모두 새 파일 하나로 기능을 제공할 수 있다고 예측했다.
ko114 | SAME | ko101 | 1.00 | 실행한 네 후보는 모두 입력 순서와 중복을 보존하고 빈 목록과 미지원 도형을 명세대로 처리했다.
ko115 | SAME | ko102 | 1.00 | 각 후보는 원과 사각형의 기존 렌더링을 유지했다.
ko116 | SAME | ko103 | 1.00 | 기존 파일 두 개를 고친 것은 도형 파일이 변환을 맡은 후보뿐이었다.
ko117 | SAME | ko104 | 1.00 | 네 후보 모두 새 파일 하나를 추가했다(그림 1B).
ko118 | SAME | ko105 | 1.00 | A는 삼각형 추가와 이름표 연산 추가를 비교한다.
ko119 | SAME | ko106 | 1.00 | B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다.
ko120 | SAME | ko107 | 1.00 | B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.
ko121 | SAME | ko108 | 1.00 | · · · · 세 번째 비교에서는 배치 함수 대신 기존 렌더링의 결과 하나를 선택적으로 감싸는 옵션을 사용했다.
ko122 | SAME | ko109 | 1.00 | 새 모듈을 호출할 수 있는 경우에는 두 배치가 기존 파일을 그대로 뒀다.
ko123 | SAME | ko110 | 1.00 | 같은 모듈을 추가한 상태에서 기존 함수에 bracketed=True 를 넘기면 함수는 그 인자를 받지 못했다.
ko124 | SAME | ko111 | 1.00 | 기존 함수로 옵션을 제공한 후보는 연산별 배치에서 파일 하나, 도형별 배치에서 두 개를 고쳤다.
ko125 | SAME | ko112 | 1.00 | 기존 함수가 외부 변환 모듈을 불러올 수 있도록 이미 구성된 별도 기준선에서는 두 배치 모두 새 파일 하나를 추가해 기존 호출 경로로 옵션을 제공했다(표 3).
ko126 | SAME | ko113 | 1.00 | 확장 지점은 세 번째 행의 기준선에 이미 있었다.
ko127 | SAME | ko114 | 1.00 | 따라서 이 행의 0개를 첫 설계에서 확장 지점을 처음 만드는 비용까지 포함한 결과로 읽어서는 안 된다.
ko128 | SAME | ko115 | 1.00 | 여기서는 확장 지점이 도입된 비용을 별도로 측정하지 않았다.
ko129 | SAME | ko116 | 1.00 | 같은 어댑터를 추가해도 기존 함수에서는 옵션을 쓸 수 없었던 대조 실행을 포함했다.
ko130 | SAME | ko117 | 1.00 | · 기존 파일 수정 수가 적다는 사실만으로 변경에 더 잘 대응하는 설계라고 할 수는 없다.
ko131 | SAME | ko118 | 1.00 | 새 파일을 추가할 수 있어도 그 파일이 실행되려면 호출자가 쓸 수 있는 경로가 필요하다.
ko132 | SAME | ko119 | 1.00 | 표 3의 마지막 행은 확장 지점이 이미 있는 상태에서 이후에 고친 파일만 센다.
ko133 | SAME | ko120 | 1.00 | 여기에 든 수정 수는 실행한 후보에 관한 관찰이다.
ko134 | SAME | ko121 | 1.00 | 독립적으로 작성한 요구에서도 어떤 경로가 작동할지 예측할 수 있는지, 파일 수정 수가 실제 유지보수 부담과 어떻게 연결되는지는 남은 질문이다.
ko135 | SAME | ko122 | 1.00 | 서론의 그리기 함수가 잘못됐는지는 정렬을 누가 맡았는지에 달려 있었다.
ko136 | SAME | ko123 | 1.00 | 벤치마크는 모델의 응답을 참조 라벨과 대조해 분류 성능을 잰다.
ko137 | SAME | ko124 | 1.00 | 그 판정을 구체적인 수정안에 적용하려면 어떤 기능이 필요한지, 어떤 동작을 기존 호출자에게 약속했는지를 확인해야 한다.
ko138 | SAME | ko125 | 1.00 | 도서관 예제에서는 정오표 요구만으로 수정안을 거절할 수 있었다.
ko139 | SAME | ko126 | 1.00 | 기술보고서만 필요한 경우에는 책 접두어 계약이 결론을 갈랐다.
ko140 | SAME | ko127 | 1.00 | 어떤 수정안이 가능한지를 비교할 때는 호출자가 새 동작을 받을 수 있는 경로도 확인해야 한다.
ko141 | SAME | ko128 | 1.00 | 검토 의견으로 변경을 요구하려면 어느 요구나 계약을 근거로 삼았는지, 어느 호출 경로에 적용되는지를 밝힐 수 있어야 한다.
ko142 | SAME | ko129 | 1.00 | 그러면 개발자는 이미 내려진 결론의 근거를 확인하거나, 보류된 판정을 가를 사실을 더 찾을 수 있다.
ko143 | SAME | ko130 | 1.00 | 이 결과는 한 벤치마크의 저장 자료와 여기서 구성해 실행한 후보의 범위에서 성립한다.
ko144 | SAME | ko131 | 1.00 | 여기서 더 나아가려면 SOLID를 대체할 공리를 선언하기보다, 어떤 변경과 계약, 권한과 호출 경로가 주어졌을 때 설계의 유불리가 어떻게 달라지는지 예측할 수 있는 표현을 찾아야 한다.
ko145 | SAME | ko132 | 1.00 | 그런 표현이 실제 독립 요구에서도 작동한다면, 익숙한 원칙이 유용한 이유뿐 아니라 그 조언을 따르지 않는 설계가 더 나은 조건도 설명할 수 있을 것이다.
ko146 | SAME | ko133 | 1.00 | 이 가능성은 이번 논문의 결과가 아니라 다음에 검증할 가설로 남긴다.
ko147 | SAME | ko134 | 1.00 | §3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다.
ko148 | SAME | ko135 | 1.00 | §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다.
ko149 | SAME | ko136 | 1.00 | 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다.
ko150 | SAME | ko137 | 1.00 | 그림 1의 소스와 출력 위치는 그림 캡션에 있다.
Summary ko: same 137; edited 0; new 13.

### EN (157 sentences; prior 145)
en001 | SAME | en001 | 1.00 | In 1996, Robert Martin described a function that drew the shapes in a list in order.
en002 | SAME | en002 | 1.00 | A triangle could be added without editing the function if the triangle supplied its own drawing operation.
en003 | SAME | en003 | 1.00 | Martin then introduced a new requirement.
en004 | SAME | en004 | 1.00 | Every circle had to be drawn before any square.
en005 | SAME | en005 | 1.00 | Given a list that begins with a square, the same function still draws the square first.
en006 | SAME | en006 | 1.00 | Who is responsible for sorting the list?
en007 | SAME | en007 | 1.00 | If the caller must pass a sorted list, the drawing function can stay as it is.
en008 | SAME | en008 | 1.00 | If the function must produce the required order for any input list, the current code falls short.
en009 | SAME | en009 | 1.00 | A reviewer can see that the function does no sorting.
en010 | SAME | en010 | 1.00 | To take that fact as evidence of an open–closed principle (OCP) violation, the reviewer also needs to know who was meant to sort the shapes.
en011 | SAME | en011 | 1.00 | The difficulty is not simply whether the principle is sound.
en012 | SAME | en012 | 1.00 | In Martin's example, a designer must first identify the changes against which a routine ought to remain closed.
en013 | SAME | en013 | 1.00 | If that situated judgment is later used as a violation label without its premise, the label may carry the authority of a rule while omitting the reason for applying it.
en014 | SAME | en014 | 1.00 | We call this risk the over-axiomatization of design advice.
en015 | SAME | en015 | 1.00 | It is a question about how conditional advice is used, not a demonstrated history of the entire SOLID family.
en016 | SAME | en016 | 1.00 | The distinction becomes consequential when a violation label is treated as a reason to reject a particular edit.
en017 | SAME | en017 | 1.00 | A classification benchmark can show which instructions and examples were presented to a model; it cannot by itself settle the obligations of a separate maintenance request.
en018 | SAME | en018 | 1.00 | We inspect one such archive and then construct a fixed-patch comparison in which the new demand and the commitment to existing callers vary.
en019 | SAME | en019 | 1.00 | We also examine the routes by which a new behavior reaches the original callers, since an edit that can be written in a new file is not necessarily available through their existing entry points.
en020 | SAME | en020 | 1.00 | · · Martin opens his 1996 article by attributing the principle to Bertrand Meyer and citing page 23 of the 1988 first edition.
en021 | SAME | en021 | 1.00 | We examine this explicit citation link to recover the conditions under which OCP was argued for; it is not, by itself, a genealogy of all five SOLID principles.
en022 | SAME | en022 | 1.00 | A closed module in Meyer’s account is one that other modules can use on the basis of a stable specification.
en023 | NEW | en011 | 0.12 | The principle was contested well before it became a mnemonic.
en024 | NEW | en126 | 0.08 | In a June 1995 public exchange, Kyle Brown objected that developers need to edit badly designed classes.
en025 | NEW | en133 | 0.13 | Martin distinguished a lack of permission to edit source from a design in which an anticipated extension does not require editing it; he also acknowledged the difficulty of anticipating change.
en026 | NEW | en040 | 0.12 | Public records refer to the five-principle SOLID grouping by 2007, and a 2009 dispute distinguished routine internal interfaces from stable public plugin interfaces.
en027 | NEW | en016 | 0.13 | The record documents debate across settings, not a proven causal history in which a mnemonic or a particular tool stripped the qualifications away.
en028 | SAME | en023 | 1.00 | · If a library program distinguishes publication types one by one, adding technical reports can require edits to existing modules or recompiling them.
en029 | SAME | en024 | 1.00 | The designer must consider both where the new behavior can live and what existing users of the module can continue to rely on.
en030 | SAME | en025 | 1.00 | Martin assigned sorting to DrawAllShapes .
en031 | SAME | en026 | 1.00 | In the first implementation, Circle::Precedes inspected the other shape and put the circle first if it was a square.
en032 | SAME | en027 | 1.00 | The code that decided how a new shape would rank against a circle already lived in Circle .
en033 | SAME | en028 | 1.00 | Martin then moved the order of shape types into a table.
en034 | SAME | en029 | 1.00 | Putting squares first now requires swapping two entries.
en035 | SAME | en030 | 1.00 | Ordering individual shapes by area, for example, would require information outside the table.
en036 | SAME | en031 | 1.00 | Which part of the program can stay as it is depends on the change it must accommodate.
en037 | SAME | en032 | 1.00 | Whether a type check supports a violation finding also depends on the function’s obligation.
en038 | SAME | en033 | 1.00 | Later in the article, Martin presents two further functions that use dynamic_cast .
en039 | SAME | en034 | 1.00 | DrawAllShapes recognizes and draws circles and squares.
en040 | SAME | en035 | 1.00 | DrawSquaresOnly selects squares from the list and draws them.
en041 | SAME | en036 | 1.00 | Given a triangle, both skip it.
en042 | SAME | en037 | 1.00 | A function that promises to draw every shape has omitted an output, while a function that promises to draw squares has met its obligation.
en043 | SAME | en038 | 1.00 | We turn to saved classification prompts to see how much of that kind of obligation the reviewer could establish from the input.
en044 | SAME | en039 | 1.00 | Both functions contain type checks; their different obligations account for the different judgments.
en045 | SAME | en040 | 1.00 | Before assessing whether the saved prompts convey comparable obligations, we describe how we distinguished the reference examples from the submissions and instructions archived for the models.
en046 | SAME | en041 | 1.00 | · · To separate the obligations inferable from the inputs from the labels assigned by the benchmark, we distinguish three units in the archive.
en047 | SAME | en042 | 1.00 | A reference pair contains a violation example and its revision.
en048 | SAME | en043 | 1.00 | A saved response record contains the code submitted to the model, its prompt, and the recorded response.
en049 | SAME | en044 | 1.00 | We recover a prompt template by replacing the single exact occurrence of the submitted code with a common placeholder.
en050 | SAME | en045 | 1.00 | We compare templates as strings.
en051 | SAME | en046 | 1.00 | We compared each saved submission with the source on both sides of every reference pair, first as stored and again after trimming whitespace from both ends.
en052 | SAME | en047 | 1.00 | For Python reference pairs we parsed the syntax trees and compared names of methods declared in top-level classes, excluding names that begin with an underscore.
en053 | SAME | en048 | 1.00 | The comparison captures declaration changes.
en054 | SAME | en049 | 1.00 | Inherited availability, actual client use, and whether that use was protected each require separate evidence.
en055 | SAME | en050 | 1.00 | We ran the library and drawing fixtures built for this study under the conditions given in Sections 5 and 6.
en056 | SAME | en051 | 1.00 | We executed no code from the archived replication package.
en057 | SAME | en052 | 1.00 | Appendix A identifies the archive and the commands needed to reproduce the checks.
en058 | SAME | en053 | 1.00 | · Pehlivan et al. specified violation scenarios and refined and checked the generated examples.
en059 | SAME | en054 | 1.00 | They resolved disagreements about reference labels through discussion, then compared model classifications of SOLID violations with those labels.
en060 | SAME | en055 | 1.00 | The OCP archive contains 48 reference pairs and 768 saved response records.
en061 | SAME | en056 | 1.00 | Masking the submitted code yielded 24 distinct template strings, with no exact template shared across the four strategies.
en062 | SAME | en057 | 1.00 | None of the templates separately states a change request or a protected caller contract for an individual case.
en063 | SAME | en058 | 1.00 | That absence is not a defect in a benchmark whose stated task is classification.
en064 | SAME | en059 | 1.00 | It matters when the resulting label is asked to justify an engineering decision outside that task.
en065 | SAME | en060 | 1.00 | One saved Python EXAMPLE prompt points the reviewer to repeated branches where polymorphism would fit.
en066 | SAME | en061 | 1.00 | The submitted AreaCalculator checks the shape type before calculating the area of a circle or rectangle.
en067 | SAME | en062 | 1.00 | The branch suggests where an edit might go if a new shape is added.
en068 | SAME | en063 | 1.00 | The instruction leaves open whether anyone has requested that change and whether existing calls that read a rectangle’s width must still be supported.
en069 | SAME | en064 | 1.00 | In a separate reference pair, number 37, the revision moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en070 | NEW | en039 | 0.11 | Other research measures different aspects of this problem.
en071 | NEW | en141 | 0.11 | Bräuer et al. (2018) asked experts which parts of design principles were and were not captured by measurable practices.
en072 | NEW | en018 | 0.09 | Cabral et al. (2024) studied participants' understanding and perceived extension benefits in a concrete machine-learning scenario comparing bundled code treatments.
en073 | NEW | en063 | 0.11 | Zhu et al. (2026) evaluated repository changes against functional tests and structural oracles.
en074 | NEW | en132 | 0.14 | These instruments measure, respectively, coverage of principles, reported perceptions, and conformance under specified tasks .
en075 | NEW | en069 | 0.24 | Our fixed-patch fixture instead asks whether an acceptance verdict is stable under explicitly varied demands and protected contracts.
en076 | NEW | en066 | 0.13 | The distinction does not make the earlier instruments invalid; it identifies the decision for which each source supplies evidence.
en077 | SAME | en065 | 1.00 | · · No saved submission matched either side of the reference pairs in the exact or outer-whitespace-trimmed comparison.
en078 | SAME | en066 | 1.00 | Our evidence for the missing declaration comes from comparing the reference sources.
en079 | SAME | en067 | 1.00 | To argue that its removal warrants rejecting a patch, a reviewer would need to establish that callers were guaranteed access to the width.
en080 | SAME | en068 | 1.00 | We do not infer that a real caller used the deleted getter.
en081 | SAME | en069 | 1.00 | Instead, a separate executable fixture tests whether varying a protected commitment can change the verdict on a fixed edit.
en082 | SAME | en070 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en083 | SAME | en071 | 1.00 | The saved prompt is on JSONL line 13 (record ID 12).
en084 | SAME | en072 | 1.00 | Reference pair 37 is in a separate ground-truth JSON file. 768 counts saved records.
en085 | SAME | en073 | 1.00 | · · · Following Meyer’s example, we built a small library catalog.
en086 | SAME | en074 | 1.00 | The proposed patch adds a module for technical reports.
en087 | SAME | en075 | 1.00 | The two existing source files remain byte-for-byte identical.
en088 | SAME | en076 | 1.00 | In execution, technical reports render and requests for errata are still rejected.
en089 | SAME | en077 | 1.00 | The prefix in an existing book’s output changes from book to BOOK .
en090 | SAME | en078 | 1.00 | The identity of the old source files therefore does not imply the preservation of every observable result; we verified the latter separately in our fixture.
en091 | SAME | en079 | 1.00 | We hold the patch, its observed behavior, and the boundary permitting new modules fixed.
en092 | SAME | en080 | 1.00 | The new requirement covers either technical reports alone or both technical reports and errata.
en093 | SAME | en081 | 1.00 | Both legacy contracts protect the rendering of journals and proceedings and require rejection of a separate unsupported type.
en094 | SAME | en082 | 1.00 | The broader contract also protects the original book prefix.
en095 | SAME | en083 | 1.00 | An acceptable candidate in Table 2 must meet both the new requirement and the applicable contract.
en096 | SAME | en084 | 1.00 | Two independent conditions for the same patch.
en097 | SAME | en085 | 1.00 | The patch is acceptable when only technical reports are required and the book prefix is outside the contract.
en098 | SAME | en086 | 1.00 | Knowing that errata are required suffices to reject it even before the prefix contract is known.
en099 | SAME | en087 | 1.00 | If only technical reports are required, the verdict turns on whether callers were promised the original prefix.
en100 | SAME | en088 | 1.00 | A separate patch adds one module within the same edit boundary, handles both new types, and preserves every protected observation.
en101 | SAME | en089 | 1.00 | With partial information, the reviewer can consider the specifications still compatible with the evidence.
en102 | SAME | en090 | 1.00 | If all give the same verdict, the reviewer can issue it.
en103 | SAME | en091 | 1.00 | If they disagree, the reviewer can give conditional verdicts or defer until the applicable specification can be established.
en104 | SAME | en092 | 1.00 | This argument assumes that the actual specification is in the compatible set, so the set is nonempty.
en105 | SAME | en093 | 1.00 | A rule that sees the same input and must always return a single binary verdict cannot be correct for two compatible specifications that require opposite answers.
en106 | SAME | en094 | 1.00 | This establishes an information limit, not an error rate for SOLID judgments in practice.
en107 | SAME | en095 | 1.00 | Appendix A gives the nine disclosure conditions for this case.
en108 | SAME | en096 | 1.00 | · Section 5 established whether one patch met a stated request and contract.
en109 | SAME | en097 | 1.00 | It did not determine the least costly way to meet them.
en110 | SAME | en098 | 1.00 | Returning to the drawing fixture, we ask which source boundaries the implemented candidates cross when the request, permitted placement, or caller route changes.
en111 | SAME | en099 | 1.00 | The counts describe those candidates, not a minimum over all possible implementations.
en112 | SAME | en100 | 1.00 | We first varied the request.
en113 | SAME | en101 | 1.00 | In the shape layout we added a triangle in one new file and edited the circle and square files to add a labeling operation.
en114 | SAME | en102 | 1.00 | In the operation layout we edited the drawing file to add the triangle and put the labeling operation in a new file.
en115 | SAME | en103 | 1.00 | All four candidates passed their functional checks.
en116 | SAME | en104 | 1.00 | Which layout left more existing files intact depended on the request (Figure 1A).
en117 | SAME | en105 | 1.00 | We then added the same batch-rendering function to both layouts.
en118 | SAME | en106 | 1.00 | It takes a list of shapes and brackets each rendered result.
en119 | SAME | en107 | 1.00 | We predicted that requiring the item transformation to live in the shape files would entail editing both files in the shape layout.
en120 | SAME | en108 | 1.00 | If a shared adapter was allowed, we predicted that either layout could add the feature in one new file.
en121 | SAME | en109 | 1.00 | All four candidates preserved order and duplicates, handled empty lists and unsupported shapes as specified, and preserved the existing circle and square renderings.
en122 | SAME | en110 | 1.00 | The candidate placing both transformations in the shape files edited two existing files.
en123 | SAME | en111 | 1.00 | All four added one file (Figure 1B).
en124 | SAME | en112 | 1.00 | Existing source files edited.
en125 | SAME | en113 | 1.00 | Panel A compares adding a triangle with adding a labeling operation.
en126 | SAME | en114 | 1.00 | Panel B holds the batch-rendering request fixed and varies the placement rule.
en127 | SAME | en115 | 1.00 | All four candidates in panel B passed the new and legacy behavior checks and added one file each.
en128 | SAME | en116 | 1.00 | · · · · The third comparison used an option to bracket a single rendering through the existing function.
en129 | SAME | en117 | 1.00 | Candidates that offered a new entry point left the existing files intact in both layouts.
en130 | SAME | en118 | 1.00 | With the same adapter added, the original functions still rejected bracketed=True .
en131 | SAME | en119 | 1.00 | The candidates offering the option through the original functions edited one file in the operation layout and two in the shape layout.
en132 | SAME | en120 | 1.00 | In a separate baseline whose original function could already load an external decorator, each layout delivered the option through the original entry point by adding a single file (Table 3).
en133 | SAME | en121 | 1.00 | Call paths for the new rendering option.
en134 | SAME | en122 | 1.00 | The hook was already present in the last row’s baseline.
en135 | SAME | en123 | 1.00 | Its zero-edits result does not include the cost of introducing that hook into the earlier baseline.
en136 | SAME | en124 | 1.00 | We did not measure that initial investment.
en137 | SAME | en125 | 1.00 | The negative control adds the same adapter and finds that the option remains unavailable through the original function.
en138 | SAME | en126 | 1.00 | · Fewer changed files do not by themselves establish a more maintainable design.
en139 | SAME | en127 | 1.00 | Permission to add a file needs to be paired with a path that the caller can actually use.
en140 | SAME | en128 | 1.00 | The last row of Table 3 starts counting after the hook is already in place.
en141 | SAME | en129 | 1.00 | These file counts describe the tested candidates.
en142 | SAME | en130 | 1.00 | Whether we can predict working paths for independently authored requests, and how these counts relate to maintenance effort, remain open.
en143 | SAME | en131 | 1.00 | Whether the drawing routine falls short depends on who must sort the list.
en144 | SAME | en132 | 1.00 | The benchmark measures classification performance by comparing model responses with its reference labels.
en145 | SAME | en133 | 1.00 | Applying a finding to a specific patch also requires knowing what change the patch must deliver and which behavior existing callers were promised.
en146 | SAME | en134 | 1.00 | In the catalog example, the errata requirement can settle a rejection on its own.
en147 | SAME | en135 | 1.00 | When only technical reports are needed, the verdict turns on the promise about the book prefix.
en148 | SAME | en136 | 1.00 | Comparing possible edits also requires knowing how the new behavior can reach its callers.
en149 | SAME | en137 | 1.00 | A review that calls for an edit should identify the request or commitment it relies on and the call path to which it applies.
en150 | SAME | en138 | 1.00 | The developer can then check the grounds for the verdict or identify the remaining fact that would settle it.
en151 | SAME | en139 | 1.00 | The evidence here covers the saved material of one benchmark and the candidates we constructed and ran.
en152 | SAME | en140 | 1.00 | Rather than announce a new set of axioms, the next step is to ask whether changes, protected commitments, authority, and caller routes can be represented in a form that predicts when one design has an advantage over anot
en153 | SAME | en141 | 1.00 | Such an account would be valuable if it explained both the usefulness of familiar principles and the conditions under which their preferred design loses.
en154 | SAME | en142 | 1.00 | The present paper poses that hypothesis; it does not establish it.
en155 | SAME | en143 | 1.00 | For Sections 3–4 the audit reads the archived JSON and JSONL.
en156 | SAME | en144 | 1.00 | For Sections 5–6 the fixtures run the examples constructed for this study.
en157 | SAME | en145 | 1.00 | The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.
Summary en: same 145; edited 0; new 12.

## v07 · [Notion](https://app.notion.com/p/41bef561cf9281cbaf29c9a9b5daba1e)
### KO (150 sentences; prior 150)
ko001 | SAME | ko001 | 1.00 | 로버트 마틴은 1996년 글에서 도형 목록을 받아 차례로 그리는 함수를 예로 들었다.
ko002 | SAME | ko002 | 1.00 | 삼각형이 자신을 그리는 동작을 제공하면, 그 함수를 고치지 않고도 삼각형을 추가할 수 있었다.
ko003 | SAME | ko003 | 1.00 | 같은 함수에 사각형으로 시작하는 목록을 주면 여전히 사각형부터 그린다.
ko004 | SAME | ko004 | 1.00 | 원을 먼저 그리려면 누가 목록을 정렬해야 할까?
ko005 | SAME | ko005 | 1.00 | 호출자가 정렬한 목록을 넘기기로 했다면 그리기 함수는 그대로 둘 수 있다.
ko006 | SAME | ko006 | 1.00 | 어떤 목록을 받아도 함수가 순서를 보장하기로 했다면 지금 코드로는 부족하다.
ko007 | SAME | ko007 | 1.00 | 소스 코드를 읽으면 함수가 정렬하지 않는다는 사실을 알 수 있다.
ko008 | SAME | ko008 | 1.00 | 그 사실을 개방–폐쇄 원칙(OCP) 위반의 근거로 삼으려면 정렬을 누가 맡았는지도 알아야 한다.
ko009 | SAME | ko009 | 1.00 | 여기에는 설계 원칙 자체보다 그 원칙을 사용하는 방식에 관한 문제가 있다.
ko010 | SAME | ko010 | 1.00 | 마틴의 사례에서는 앞으로 어떤 변화에 대비할지를 정해야 비로소 어떤 코드를 닫아 둘지 논의할 수 있었다.
ko011 | SAME | ko011 | 1.00 | 그 판단을 변경 요구가 빠진 ‘위반’ 판정으로 바꿔 사용한다면, 처음에는 결론을 정당화했던 전제가 사라진다.
ko012 | SAME | ko012 | 1.00 | 우리는 이 위험을 원칙의 ‘과도한 공리화’라고 부른다.
ko013 | SAME | ko013 | 1.00 | 이것은 SOLID 전체가 무효하다는 역사적 결론이 아니라, 조건부 설계 조언을 무조건적인 탈락 기준처럼 적용할 때 무엇을 잃는지 묻는 문제 제기다.
ko014 | SAME | ko014 | 1.00 | 이 문제를 따지려면 ‘위반’이라고 분류하는 일과 특정 수정안을 거절하는 일을 먼저 나눠야 한다.
ko015 | SAME | ko015 | 1.00 | SOLID 위반 분류 벤치마크의 저장 자료는 모델이 어떤 근거를 받았는지 보여 주지만, 특정 유지보수 요청이 승인되어야 하는지까지 판정하지는 않는다.
ko016 | SAME | ko016 | 1.00 | 우리는 별도로 만든 도서관 프로그램에서 같은 수정안을 서로 다른 요구와 기존 호출자 계약 아래 두어 그 간격을 검사한다.
ko017 | SAME | ko017 | 1.00 | 수정안 자체의 수용 여부를 따진 다음에는, 새로운 기능이 실제 호출 경로에 도달하도록 만드는 일이 어느 기존 파일을 바꾸게 하는지도 비교한다.
ko018 | SAME | ko018 | 1.00 | · · 마틴은 1996년 글의 첫머리에서 이 원칙을 베르트랑 마이어에게서 가져왔다고 밝히며 1988년 초판 23쪽을 인용한다.
ko019 | SAME | ko019 | 1.00 | 이어지는 두 사례를 다루는 이유는 SOLID 다섯 원칙의 기원을 한 줄로 연결하기 위해서가 아니라, OCP에 적용 조건이 명시되어 있었는지 살피기 위해서다.
ko020 | SAME | ko020 | 1.00 | 마이어의 설명에서 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 사용할 수 있는 모듈이다.
ko021 | SAME | ko027 | 1.00 | 도서관 프로그램이 자료의 종류를 하나씩 구별해 처리한다면 기술보고서 한 종류를 추가하는 데도 기존 모듈의 수정이나 재컴파일이 필요할 수 있다.
ko022 | SAME | ko028 | 1.00 | 이때 설계자는 새 동작을 어디에 넣을지와 기존 사용자가 계속 어떤 동작에 의존할 수 있을지를 함께 고려하게 된다.
ko023 | SAME | ko021 | 1.00 | 1995년 6월 공개 토론에서 Kyle Brown은 잘못 설계된 클래스라면 개발자가 소스를 고쳐야 한다고 반박했다.
ko024 | SAME | ko022 | 1.00 | 마틴은 ‘닫혀 있다’는 말을 수정할 권한이 없다는 뜻이 아니라, 예상한 확장을 위해 기존 코드를 반드시 수정할 필요가 없다는 뜻으로 구분했다.
ko025 | SAME | ko023 | 1.00 | 그는 어떤 변경이 생길지 미리 알아야 한다는 어려움도 인정했다.
ko026 | SAME | ko024 | 1.00 | 이 논쟁은 OCP가 처음부터 단 하나의 무조건적 금지 명령으로 받아들여졌다고 가정하기 어렵게 한다.
ko027 | SAME | ko025 | 1.00 | 2007년에는 다섯 원칙을 묶은 SOLID라는 명칭이 공개 기록에 나타나고, 2009년의 인터페이스 논쟁에서는 내부 클래스와 공개 플러그인 API가 서로 다른 판단을 요구했다.
ko028 | SAME | ko026 | 1.00 | 이런 자료로 원칙의 전파와 수용 과정에 논쟁이 있었다는 점은 말할 수 있지만, 특정 약어나 자동화 도구가 조건을 탈락시켰다는 인과관계까지 증명할 수는 없다.
ko029 | SAME | ko029 | 1.00 | · 마틴은 목록을 정렬하는 일을 DrawAllShapes 에 맡겼다.
ko030 | SAME | ko030 | 1.00 | 첫 구현에서는 Circle::Precedes 가 상대 도형을 검사해 사각형이면 원을 앞에 놓았다.
ko031 | SAME | ko031 | 1.00 | 새 도형이 들어왔을 때 원과 그 도형의 순서를 정하는 코드가 이미 Circle 안에 있었다.
ko032 | SAME | ko032 | 1.00 | 마틴은 이어서 도형 종류별 순서를 표로 옮겼다.
ko033 | SAME | ko033 | 1.00 | 이제 사각형을 원보다 먼저 그리라는 요청에는 표에서 두 항목의 위치를 바꾸면 된다.
ko034 | SAME | ko034 | 1.00 | 개별 도형의 넓이순으로 그리라는 요구를 가정하면 표에 없는 정보가 필요하다.
ko035 | SAME | ko035 | 1.00 | 어느 부분을 그대로 둘 수 있는지는 어떤 변경에 대비하느냐에 달려 있다.
ko036 | SAME | ko036 | 1.00 | 타입 검사가 위반의 근거가 되는지도 함수가 맡은 일에 달려 있다.
ko037 | SAME | ko037 | 1.00 | 글의 뒷부분에서 마틴은 dynamic_cast 를 쓰는 두 함수를 새로 제시한다.
ko038 | SAME | ko038 | 1.00 | 원과 사각형을 가려 그리는 DrawAllShapes 와 목록에서 사각형만 골라 그리는 DrawSquaresOnly 다.
ko039 | SAME | ko039 | 1.00 | 두 함수에 삼각형을 넣으면 어느 쪽도 그리지 않는다.
ko040 | SAME | ko040 | 1.00 | 모든 도형을 그리기로 한 함수에서는 빠진 출력이고, 사각형만 그리기로 한 함수에서는 약속한 동작이다.
ko041 | SAME | ko041 | 1.00 | 검토자가 어떤 근거로 두 경우를 구별할 수 있는지를 확인하려면, 실제로 받았던 코드와 지시를 구분해 살펴봐야 한다.
ko042 | SAME | ko042 | 1.00 | 두 함수는 같은 구문을 사용하지만, 약속한 일이 달라 평가가 갈린다.
ko043 | SAME | ko043 | 1.00 | 이 사례를 위반 여부의 판단으로 옮기려면 검토에 주어진 코드와 그 코드가 맡은 책임을 나눠야 한다.
ko044 | SAME | ko044 | 1.00 | 우리는 먼저 자료를 어떤 단위로 읽었는지 밝힌 뒤, 저장된 분류 프롬프트에서 그 책임을 어디까지 확인할 수 있는지 살펴본다.
ko045 | SAME | ko045 | 1.00 | · · 이 질문을 저장 자료에 적용하기 위해 분석 단위를 세 가지로 나눴다.
ko046 | SAME | ko046 | 1.00 | 참조 코드 쌍에는 위반 예시와 그 수정 예시가 들어 있고, 저장 응답에는 모델에 제출된 코드와 프롬프트, 기록된 응답이 들어 있다.
ko047 | SAME | ko047 | 1.00 | 프롬프트 틀은 저장 프롬프트에 정확히 한 번 나오는 제출 코드를 공통 자리표시자로 치환해 얻었다.
ko048 | SAME | ko048 | 1.00 | 저장 응답의 제출 코드를 모든 참조 쌍의 수정 전·후 소스와 대조했다.
ko049 | SAME | ko049 | 1.00 | 각 문자열을 그대로 비교한 뒤 양끝 공백을 제거해 다시 비교했다.
ko050 | SAME | ko050 | 1.00 | Python 참조 쌍은 구문 트리로 파싱해 최상위 클래스의 메서드 선언 이름을 비교했다.
ko051 | SAME | ko051 | 1.00 | 상속에 따른 호출 가능성, 실제 사용 여부, 보장의 범위는 별도 근거가 필요한 질문이다.
ko052 | SAME | ko052 | 1.00 | 이 연구에서 작성한 도서관·도형 재현은 §5와 §6에서 정한 조건으로 실행했다.
ko053 | SAME | ko053 | 1.00 | ZIP 안의 공개 재현 패키지 코드는 실행하지 않았다.
ko054 | SAME | ko054 | 1.00 | 아카이브 식별 정보와 확인 명령은 부록 A에 있다.
ko055 | SAME | ko055 | 1.00 | · Pehlivan 등은 위반 시나리오를 정하고, 생성한 코드 예시를 수정·검증한 뒤 의견이 갈린 사례의 참조 라벨을 논의로 정했다.
ko056 | SAME | ko056 | 1.00 | SOLID 위반을 식별하는 모델 응답은 그 라벨과 대조했다.
ko057 | SAME | ko057 | 1.00 | OCP에 해당하는 아카이브에는 참조 쌍 48개와 저장 응답 768건이 있다.
ko058 | SAME | ko058 | 1.00 | 저장 프롬프트에서 제출 코드를 가렸을 때 서로 다른 문자열 24개가 남았고, 네 전략 사이에 동일한 틀은 없었다.
ko059 | SAME | ko059 | 1.00 | 각 사례의 변경 요구나 기존 호출자 계약을 따로 밝힌 틀은 없었다.
ko060 | SAME | ko060 | 1.00 | 이는 벤치마크가 본래 수행하려는 분류 과제를 잘못 설계했다는 뜻이 아니다.
ko061 | SAME | ko061 | 1.00 | 특정 수정안을 승인하거나 거절하는 데 이 분류 결과를 사용하려면 추가 증거가 필요하다는 뜻이다.
ko062 | SAME | ko062 | 1.00 | 저장된 Python EXAMPLE 지시는 다형성으로 처리할 만한 반복 분기를 찾도록 한다.
ko063 | SAME | ko063 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko064 | SAME | ko064 | 1.00 | 그 분기를 보면 새 도형을 추가할 때 어디에 손댈지 짐작할 수 있다.
ko065 | SAME | ko065 | 1.00 | 새 도형 추가가 실제 요청인지, 사각형의 너비를 직접 읽는 호출을 계속 지원해야 하는지는 이 지시문에서 확인되지 않는다.
ko066 | SAME | ko066 | 1.00 | 별도의 참조 쌍 37번은 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko067 | SAME | ko074 | 1.00 | 원본 문자열과 양끝 공백을 제거한 문자열을 대조했을 때, 저장된 제출 코드와 참조 쌍의 어느 쪽도 일치하지 않았다.
ko068 | SAME | ko075 | 1.00 | 따라서 여기서 근거로 삼는 것은 참조 쌍에서 확인한 선언의 변화다.
ko069 | SAME | ko076 | 1.00 | 그 변화가 수정안을 거절할 이유가 되려면 호출자가 너비를 읽는 동작까지 보장받았는지 확인해야 한다.
ko070 | SAME | ko077 | 1.00 | 이 참조 쌍에 실제 호출자가 있었다고 주장하지는 않는다.
ko071 | SAME | ko078 | 1.00 | 대신 해당 문제가 판정에 영향을 줄 수 있는지 별도로 구성한 수정안에서 시험한다.
ko072 | SAME | ko067 | 1.00 | 이 사례가 분류 평가를 대표하는 유일한 방식은 아니다.
ko073 | SAME | ko068 | 1.00 | Bräuer 등(2018)은 설계 원칙을 측정 가능한 실천 규칙으로 옮길 때 전문가들이 보기에 무엇이 포착되고 무엇이 빠지는지 물었다.
ko074 | SAME | ko069 | 1.00 | Cabral 등(2024)은 구체적인 기계학습 확장 상황에서 SOLID 적용 전후 코드에 대한 참가자의 이해도와 확장 용이성 인식을 조사했다.
ko075 | SAME | ko070 | 1.00 | Zhu 등(2026)은 저장소 변경 요구에 기능 테스트와 구조적 판정 기준을 결합했다.
ko076 | SAME | ko071 | 1.00 | 세 연구는 각각 원칙의 측정 범위, 사용자의 인식, 특정 변경에서의 기능·구조 적합성 을 관찰한다.
ko077 | SAME | ko072 | 1.00 | 우리 비교의 결과 변수는 같은 패치가 명시된 요구와 계약 아래에서 승인 기준을 충족하는가다.
ko078 | SAME | ko073 | 1.00 | 앞선 연구를 코드 판정의 실패 사례로 취급하지 않으면서도, 무엇을 측정해야 어떤 결정을 정당화할 수 있는지 서로 다른 관점에서 확인할 수 있다.
ko079 | SAME | ko079 | 1.00 | 프롬프트 예시는 저장 JSONL 13행(ID 12)이다.
ko080 | SAME | ko080 | 1.00 | 참조 쌍 37번은 별도의 ground truth JSON 위치다.
ko081 | SAME | ko081 | 1.00 | · · · 마이어의 예를 바탕으로 작은 도서관 목록 프로그램을 만들었다.
ko082 | SAME | ko082 | 1.00 | 검토할 수정안은 기술보고서를 처리하는 모듈을 추가한다.
ko083 | SAME | ko083 | 1.00 | 기존 소스 파일 두 개는 바이트 단위로 그대로다.
ko084 | SAME | ko084 | 1.00 | 실행하면 기술보고서는 출력되고 정오표는 여전히 거절된다.
ko085 | SAME | ko085 | 1.00 | 기존 책 출력의 접두어는 book 에서 BOOK 으로 바뀐다.
ko086 | SAME | ko086 | 1.00 | 기존 파일을 수정하지 않았다는 사실은 기존 호출 결과까지 보존했다는 뜻이 아니다.
ko087 | SAME | ko087 | 1.00 | 변경된 동작은 우리가 만든 실행 예제에서 관찰했다.
ko088 | SAME | ko088 | 1.00 | 수정안과 실행 결과, 새 모듈을 추가할 수 있는 편집 범위를 고정했다.
ko089 | SAME | ko089 | 1.00 | 새 요구는 기술보고서만 지원하는 경우와 정오표까지 지원하는 경우로 나눴다.
ko090 | SAME | ko090 | 1.00 | 두 계약은 모두 학술지와 학회록의 출력, 그리고 별개의 미지원 자료 유형을 거절하는 동작을 보호한다.
ko091 | SAME | ko091 | 1.00 | 표 2의 승인은 새 요구와 보호할 계약을 모두 충족한 경우다.
ko092 | SAME | ko092 | 1.00 | 기술보고서만 필요하고 책 접두어를 보호하지 않는 경우에 승인된다.
ko093 | SAME | ko093 | 1.00 | 정오표가 필수라는 사실을 알면 책 접두어 계약을 모르더라도 거절할 수 있다.
ko094 | SAME | ko094 | 1.00 | 기술보고서만 필요하다는 사실을 알 때는 책 접두어를 보장했는지가 결론을 가른다.
ko095 | SAME | ko095 | 1.00 | 별도로 만든 수정안은 같은 편집 범위에서 새 모듈 하나를 추가해 두 자료 유형을 처리하고 모든 보호 동작을 지켰다.
ko096 | SAME | ko096 | 1.00 | 판정에 필요한 정보가 일부만 주어지면, 그 정보와 양립하는 명세들을 비교할 수 있다.
ko097 | SAME | ko097 | 1.00 | 모든 명세가 같은 판정을 내리면 그 판정을 내릴 수 있다.
ko098 | SAME | ko098 | 1.00 | 서로 다른 판정이 나오면 조건마다 결론을 밝히거나, 어느 조건이 실제로 적용되는지 확인할 때까지 보류할 수 있다.
ko099 | SAME | ko099 | 1.00 | 이 논증은 실제 명세가 검토 중인 집합에 들어 있어 그 집합이 비어 있지 않다는 전제에서 성립한다.
ko100 | SAME | ko100 | 1.00 | 이때 한 가지 입력만 받아 언제나 승인 또는 거절 중 하나를 출력하는 규칙은, 서로 다른 정답이 남아 있는 두 조건을 동시에 맞힐 수 없다.
ko101 | SAME | ko101 | 1.00 | 다만 이 논증만으로 SOLID의 다른 정리나 실제 현장의 판단 오류율을 추정할 수는 없다.
ko102 | SAME | ko102 | 1.00 | 부록 A에는 이번 사례에서 검토한 정보 공개 조건 아홉 개가 있다.
ko103 | SAME | ko103 | 1.00 | · 도서관 실험에서 확인한 것은 주어진 수정안의 적격성이었다.
ko104 | SAME | ko104 | 1.00 | 다른 수정안이 더 적은 비용으로 같은 요구를 처리할 수 있는지는 아직 별도 문제다.
ko105 | SAME | ko105 | 1.00 | 도형 예제로 돌아가, 어떤 변경에 대비할지와 새 기능을 어디에서 호출할지에 따라 기존 파일을 얼마나 수정하는지 비교한다.
ko106 | SAME | ko106 | 1.00 | 여기서 세는 것은 실행한 후보들의 수정 파일 수이지 가능한 구현 전체의 최솟값이 아니다.
ko107 | SAME | ko107 | 1.00 | 도형별 배치에서는 삼각형을 새 파일 하나로 추가했고, 이름표 연산을 추가할 때는 원과 사각형의 파일을 고쳤다.
ko108 | SAME | ko108 | 1.00 | 연산별 배치에서는 반대로 삼각형을 추가할 때 그리기 파일을 고쳤고, 이름표 연산은 새 파일에 뒀다.
ko109 | SAME | ko109 | 1.00 | 네 수정안이 모두 기능 검사를 통과했지만 기존 파일을 덜 건드리는 배치는 요구에 따라 달랐다(그림 1A).
ko110 | SAME | ko110 | 1.00 | 두 번째 비교에서는 같은 배치 렌더링 함수를 추가했다.
ko111 | SAME | ko111 | 1.00 | 이 함수는 도형 목록을 받아 각 렌더링 결과를 대괄호로 감싼다.
ko112 | SAME | ko112 | 1.00 | 도형별 배치에서 변환을 각 도형 파일이 맡아야 하면 원과 사각형 파일을 고친다.
ko113 | SAME | ko113 | 1.00 | 공용 어댑터를 허용하면 두 배치 모두 새 파일 하나로 기능을 제공할 수 있다고 예측했다.
ko114 | SAME | ko114 | 1.00 | 실행한 네 후보는 모두 입력 순서와 중복을 보존하고 빈 목록과 미지원 도형을 명세대로 처리했다.
ko115 | SAME | ko115 | 1.00 | 각 후보는 원과 사각형의 기존 렌더링을 유지했다.
ko116 | SAME | ko116 | 1.00 | 기존 파일 두 개를 고친 것은 도형 파일이 변환을 맡은 후보뿐이었다.
ko117 | SAME | ko117 | 1.00 | 네 후보 모두 새 파일 하나를 추가했다(그림 1B).
ko118 | SAME | ko118 | 1.00 | A는 삼각형 추가와 이름표 연산 추가를 비교한다.
ko119 | SAME | ko119 | 1.00 | B는 배치 렌더링 요구를 고정하고 파일 배치 규칙을 바꾼다.
ko120 | SAME | ko120 | 1.00 | B의 네 후보는 모두 기능·기존 동작 검사를 통과했으며 한 파일씩 추가했다.
ko121 | SAME | ko121 | 1.00 | · · · · 세 번째 비교에서는 배치 함수 대신 기존 렌더링의 결과 하나를 선택적으로 감싸는 옵션을 사용했다.
ko122 | SAME | ko122 | 1.00 | 새 모듈을 호출할 수 있는 경우에는 두 배치가 기존 파일을 그대로 뒀다.
ko123 | SAME | ko123 | 1.00 | 같은 모듈을 추가한 상태에서 기존 함수에 bracketed=True 를 넘기면 함수는 그 인자를 받지 못했다.
ko124 | SAME | ko124 | 1.00 | 기존 함수로 옵션을 제공한 후보는 연산별 배치에서 파일 하나, 도형별 배치에서 두 개를 고쳤다.
ko125 | SAME | ko125 | 1.00 | 기존 함수가 외부 변환 모듈을 불러올 수 있도록 이미 구성된 별도 기준선에서는 두 배치 모두 새 파일 하나를 추가해 기존 호출 경로로 옵션을 제공했다(표 3).
ko126 | SAME | ko126 | 1.00 | 확장 지점은 세 번째 행의 기준선에 이미 있었다.
ko127 | SAME | ko127 | 1.00 | 따라서 이 행의 0개를 첫 설계에서 확장 지점을 처음 만드는 비용까지 포함한 결과로 읽어서는 안 된다.
ko128 | SAME | ko128 | 1.00 | 여기서는 확장 지점이 도입된 비용을 별도로 측정하지 않았다.
ko129 | SAME | ko129 | 1.00 | 같은 어댑터를 추가해도 기존 함수에서는 옵션을 쓸 수 없었던 대조 실행을 포함했다.
ko130 | SAME | ko130 | 1.00 | · 기존 파일 수정 수가 적다는 사실만으로 변경에 더 잘 대응하는 설계라고 할 수는 없다.
ko131 | SAME | ko131 | 1.00 | 새 파일을 추가할 수 있어도 그 파일이 실행되려면 호출자가 쓸 수 있는 경로가 필요하다.
ko132 | SAME | ko132 | 1.00 | 표 3의 마지막 행은 확장 지점이 이미 있는 상태에서 이후에 고친 파일만 센다.
ko133 | SAME | ko133 | 1.00 | 여기에 든 수정 수는 실행한 후보에 관한 관찰이다.
ko134 | SAME | ko134 | 1.00 | 독립적으로 작성한 요구에서도 어떤 경로가 작동할지 예측할 수 있는지, 파일 수정 수가 실제 유지보수 부담과 어떻게 연결되는지는 남은 질문이다.
ko135 | SAME | ko135 | 1.00 | 서론의 그리기 함수가 잘못됐는지는 정렬을 누가 맡았는지에 달려 있었다.
ko136 | SAME | ko136 | 1.00 | 벤치마크는 모델의 응답을 참조 라벨과 대조해 분류 성능을 잰다.
ko137 | SAME | ko137 | 1.00 | 그 판정을 구체적인 수정안에 적용하려면 어떤 기능이 필요한지, 어떤 동작을 기존 호출자에게 약속했는지를 확인해야 한다.
ko138 | SAME | ko138 | 1.00 | 도서관 예제에서는 정오표 요구만으로 수정안을 거절할 수 있었다.
ko139 | SAME | ko139 | 1.00 | 기술보고서만 필요한 경우에는 책 접두어 계약이 결론을 갈랐다.
ko140 | SAME | ko140 | 1.00 | 어떤 수정안이 가능한지를 비교할 때는 호출자가 새 동작을 받을 수 있는 경로도 확인해야 한다.
ko141 | SAME | ko141 | 1.00 | 검토 의견으로 변경을 요구하려면 어느 요구나 계약을 근거로 삼았는지, 어느 호출 경로에 적용되는지를 밝힐 수 있어야 한다.
ko142 | SAME | ko142 | 1.00 | 그러면 개발자는 이미 내려진 결론의 근거를 확인하거나, 보류된 판정을 가를 사실을 더 찾을 수 있다.
ko143 | SAME | ko143 | 1.00 | 이 결과는 한 벤치마크의 저장 자료와 여기서 구성해 실행한 후보의 범위에서 성립한다.
ko144 | SAME | ko144 | 1.00 | 여기서 더 나아가려면 SOLID를 대체할 공리를 선언하기보다, 어떤 변경과 계약, 권한과 호출 경로가 주어졌을 때 설계의 유불리가 어떻게 달라지는지 예측할 수 있는 표현을 찾아야 한다.
ko145 | SAME | ko145 | 1.00 | 그런 표현이 실제 독립 요구에서도 작동한다면, 익숙한 원칙이 유용한 이유뿐 아니라 그 조언을 따르지 않는 설계가 더 나은 조건도 설명할 수 있을 것이다.
ko146 | SAME | ko146 | 1.00 | 이 가능성은 이번 논문의 결과가 아니라 다음에 검증할 가설로 남긴다.
ko147 | SAME | ko147 | 1.00 | §3–§4는 ZIP에 보존된 JSON·JSONL을 읽는다.
ko148 | SAME | ko148 | 1.00 | §5–§6은 이 연구에서 작성한 예제의 기능과 계약을 실행으로 확인한다.
ko149 | SAME | ko149 | 1.00 | 아카이브 SHA-256, Python 3.11 이상 실행 명령, 저장 행·참조 쌍의 정확한 위치, §5의 3×3 전수 판정은 재현 자료에 넣었다.
ko150 | SAME | ko150 | 1.00 | 그림 1의 소스와 출력 위치는 그림 캡션에 있다.
Summary ko: same 150; edited 0; new 0.

### EN (157 sentences; prior 157)
en001 | SAME | en001 | 1.00 | In 1996, Robert Martin described a function that drew the shapes in a list in order.
en002 | SAME | en002 | 1.00 | A triangle could be added without editing the function if the triangle supplied its own drawing operation.
en003 | SAME | en003 | 1.00 | Martin then introduced a new requirement.
en004 | SAME | en004 | 1.00 | Every circle had to be drawn before any square.
en005 | SAME | en005 | 1.00 | Given a list that begins with a square, the same function still draws the square first.
en006 | SAME | en006 | 1.00 | Who is responsible for sorting the list?
en007 | SAME | en007 | 1.00 | If the caller must pass a sorted list, the drawing function can stay as it is.
en008 | SAME | en008 | 1.00 | If the function must produce the required order for any input list, the current code falls short.
en009 | SAME | en009 | 1.00 | A reviewer can see that the function does no sorting.
en010 | SAME | en010 | 1.00 | To take that fact as evidence of an open–closed principle (OCP) violation, the reviewer also needs to know who was meant to sort the shapes.
en011 | SAME | en011 | 1.00 | The difficulty is not simply whether the principle is sound.
en012 | SAME | en012 | 1.00 | In Martin's example, a designer must first identify the changes against which a routine ought to remain closed.
en013 | SAME | en013 | 1.00 | If that situated judgment is later used as a violation label without its premise, the label may carry the authority of a rule while omitting the reason for applying it.
en014 | SAME | en014 | 1.00 | We call this risk the over-axiomatization of design advice.
en015 | SAME | en015 | 1.00 | It is a question about how conditional advice is used, not a demonstrated history of the entire SOLID family.
en016 | SAME | en016 | 1.00 | The distinction becomes consequential when a violation label is treated as a reason to reject a particular edit.
en017 | SAME | en017 | 1.00 | A classification benchmark can show which instructions and examples were presented to a model; it cannot by itself settle the obligations of a separate maintenance request.
en018 | SAME | en018 | 1.00 | We inspect one such archive and then construct a fixed-patch comparison in which the new demand and the commitment to existing callers vary.
en019 | SAME | en019 | 1.00 | We also examine the routes by which a new behavior reaches the original callers, since an edit that can be written in a new file is not necessarily available through their existing entry points.
en020 | SAME | en020 | 1.00 | · · Martin opens his 1996 article by attributing the principle to Bertrand Meyer and citing page 23 of the 1988 first edition.
en021 | SAME | en021 | 1.00 | We examine this explicit citation link to recover the conditions under which OCP was argued for; it is not, by itself, a genealogy of all five SOLID principles.
en022 | SAME | en022 | 1.00 | A closed module in Meyer’s account is one that other modules can use on the basis of a stable specification.
en023 | SAME | en028 | 1.00 | If a library program distinguishes publication types one by one, adding technical reports can require edits to existing modules or recompiling them.
en024 | SAME | en029 | 1.00 | The designer must consider both where the new behavior can live and what existing users of the module can continue to rely on.
en025 | SAME | en023 | 1.00 | The principle was contested well before it became a mnemonic.
en026 | SAME | en024 | 1.00 | In a June 1995 public exchange, Kyle Brown objected that developers need to edit badly designed classes.
en027 | SAME | en025 | 1.00 | Martin distinguished a lack of permission to edit source from a design in which an anticipated extension does not require editing it; he also acknowledged the difficulty of anticipating change.
en028 | SAME | en026 | 1.00 | Public records refer to the five-principle SOLID grouping by 2007, and a 2009 dispute distinguished routine internal interfaces from stable public plugin interfaces.
en029 | SAME | en027 | 1.00 | The record documents debate across settings, not a proven causal history in which a mnemonic or a particular tool stripped the qualifications away.
en030 | SAME | en030 | 1.00 | · Martin assigned sorting to DrawAllShapes .
en031 | SAME | en031 | 1.00 | In the first implementation, Circle::Precedes inspected the other shape and put the circle first if it was a square.
en032 | SAME | en032 | 1.00 | The code that decided how a new shape would rank against a circle already lived in Circle .
en033 | SAME | en033 | 1.00 | Martin then moved the order of shape types into a table.
en034 | SAME | en034 | 1.00 | Putting squares first now requires swapping two entries.
en035 | SAME | en035 | 1.00 | Ordering individual shapes by area, for example, would require information outside the table.
en036 | SAME | en036 | 1.00 | Which part of the program can stay as it is depends on the change it must accommodate.
en037 | SAME | en037 | 1.00 | Whether a type check supports a violation finding also depends on the function’s obligation.
en038 | SAME | en038 | 1.00 | Later in the article, Martin presents two further functions that use dynamic_cast .
en039 | SAME | en039 | 1.00 | DrawAllShapes recognizes and draws circles and squares.
en040 | SAME | en040 | 1.00 | DrawSquaresOnly selects squares from the list and draws them.
en041 | SAME | en041 | 1.00 | Given a triangle, both skip it.
en042 | SAME | en042 | 1.00 | A function that promises to draw every shape has omitted an output, while a function that promises to draw squares has met its obligation.
en043 | SAME | en043 | 1.00 | We turn to saved classification prompts to see how much of that kind of obligation the reviewer could establish from the input.
en044 | SAME | en044 | 1.00 | Both functions contain type checks; their different obligations account for the different judgments.
en045 | SAME | en045 | 1.00 | Before assessing whether the saved prompts convey comparable obligations, we describe how we distinguished the reference examples from the submissions and instructions archived for the models.
en046 | SAME | en046 | 1.00 | · · To separate the obligations inferable from the inputs from the labels assigned by the benchmark, we distinguish three units in the archive.
en047 | SAME | en047 | 1.00 | A reference pair contains a violation example and its revision.
en048 | SAME | en048 | 1.00 | A saved response record contains the code submitted to the model, its prompt, and the recorded response.
en049 | SAME | en049 | 1.00 | We recover a prompt template by replacing the single exact occurrence of the submitted code with a common placeholder.
en050 | SAME | en050 | 1.00 | We compare templates as strings.
en051 | SAME | en051 | 1.00 | We compared each saved submission with the source on both sides of every reference pair, first as stored and again after trimming whitespace from both ends.
en052 | SAME | en052 | 1.00 | For Python reference pairs we parsed the syntax trees and compared names of methods declared in top-level classes, excluding names that begin with an underscore.
en053 | SAME | en053 | 1.00 | The comparison captures declaration changes.
en054 | SAME | en054 | 1.00 | Inherited availability, actual client use, and whether that use was protected each require separate evidence.
en055 | SAME | en055 | 1.00 | We ran the library and drawing fixtures built for this study under the conditions given in Sections 5 and 6.
en056 | SAME | en056 | 1.00 | We executed no code from the archived replication package.
en057 | SAME | en057 | 1.00 | Appendix A identifies the archive and the commands needed to reproduce the checks.
en058 | SAME | en058 | 1.00 | · Pehlivan et al. specified violation scenarios and refined and checked the generated examples.
en059 | SAME | en059 | 1.00 | They resolved disagreements about reference labels through discussion, then compared model classifications of SOLID violations with those labels.
en060 | SAME | en060 | 1.00 | The OCP archive contains 48 reference pairs and 768 saved response records.
en061 | SAME | en061 | 1.00 | Masking the submitted code yielded 24 distinct template strings, with no exact template shared across the four strategies.
en062 | SAME | en062 | 1.00 | None of the templates separately states a change request or a protected caller contract for an individual case.
en063 | SAME | en063 | 1.00 | That absence is not a defect in a benchmark whose stated task is classification.
en064 | SAME | en064 | 1.00 | It matters when the resulting label is asked to justify an engineering decision outside that task.
en065 | SAME | en065 | 1.00 | One saved Python EXAMPLE prompt points the reviewer to repeated branches where polymorphism would fit.
en066 | SAME | en066 | 1.00 | The submitted AreaCalculator checks the shape type before calculating the area of a circle or rectangle.
en067 | SAME | en067 | 1.00 | The branch suggests where an edit might go if a new shape is added.
en068 | SAME | en068 | 1.00 | The instruction leaves open whether anyone has requested that change and whether existing calls that read a rectangle’s width must still be supported.
en069 | SAME | en069 | 1.00 | In a separate reference pair, number 37, the revision moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en070 | SAME | en077 | 1.00 | No saved submission matched either side of the reference pairs in the exact or outer-whitespace-trimmed comparison.
en071 | SAME | en078 | 1.00 | Our evidence for the missing declaration comes from comparing the reference sources.
en072 | SAME | en079 | 1.00 | To argue that its removal warrants rejecting a patch, a reviewer would need to establish that callers were guaranteed access to the width.
en073 | SAME | en080 | 1.00 | We do not infer that a real caller used the deleted getter.
en074 | SAME | en081 | 1.00 | Instead, a separate executable fixture tests whether varying a protected commitment can change the verdict on a fixed edit.
en075 | SAME | en070 | 1.00 | Other research measures different aspects of this problem.
en076 | SAME | en071 | 1.00 | Bräuer et al. (2018) asked experts which parts of design principles were and were not captured by measurable practices.
en077 | SAME | en072 | 1.00 | Cabral et al. (2024) studied participants' understanding and perceived extension benefits in a concrete machine-learning scenario comparing bundled code treatments.
en078 | SAME | en073 | 1.00 | Zhu et al. (2026) evaluated repository changes against functional tests and structural oracles.
en079 | SAME | en074 | 1.00 | These instruments measure, respectively, coverage of principles, reported perceptions, and conformance under specified tasks .
en080 | SAME | en075 | 1.00 | Our fixed-patch fixture instead asks whether an acceptance verdict is stable under explicitly varied demands and protected contracts.
en081 | SAME | en076 | 1.00 | The distinction does not make the earlier instruments invalid; it identifies the decision for which each source supplies evidence.
en082 | SAME | en082 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en083 | SAME | en083 | 1.00 | The saved prompt is on JSONL line 13 (record ID 12).
en084 | SAME | en084 | 1.00 | Reference pair 37 is in a separate ground-truth JSON file. 768 counts saved records.
en085 | SAME | en085 | 1.00 | · · · Following Meyer’s example, we built a small library catalog.
en086 | SAME | en086 | 1.00 | The proposed patch adds a module for technical reports.
en087 | SAME | en087 | 1.00 | The two existing source files remain byte-for-byte identical.
en088 | SAME | en088 | 1.00 | In execution, technical reports render and requests for errata are still rejected.
en089 | SAME | en089 | 1.00 | The prefix in an existing book’s output changes from book to BOOK .
en090 | SAME | en090 | 1.00 | The identity of the old source files therefore does not imply the preservation of every observable result; we verified the latter separately in our fixture.
en091 | SAME | en091 | 1.00 | We hold the patch, its observed behavior, and the boundary permitting new modules fixed.
en092 | SAME | en092 | 1.00 | The new requirement covers either technical reports alone or both technical reports and errata.
en093 | SAME | en093 | 1.00 | Both legacy contracts protect the rendering of journals and proceedings and require rejection of a separate unsupported type.
en094 | SAME | en094 | 1.00 | The broader contract also protects the original book prefix.
en095 | SAME | en095 | 1.00 | An acceptable candidate in Table 2 must meet both the new requirement and the applicable contract.
en096 | SAME | en096 | 1.00 | Two independent conditions for the same patch.
en097 | SAME | en097 | 1.00 | The patch is acceptable when only technical reports are required and the book prefix is outside the contract.
en098 | SAME | en098 | 1.00 | Knowing that errata are required suffices to reject it even before the prefix contract is known.
en099 | SAME | en099 | 1.00 | If only technical reports are required, the verdict turns on whether callers were promised the original prefix.
en100 | SAME | en100 | 1.00 | A separate patch adds one module within the same edit boundary, handles both new types, and preserves every protected observation.
en101 | SAME | en101 | 1.00 | With partial information, the reviewer can consider the specifications still compatible with the evidence.
en102 | SAME | en102 | 1.00 | If all give the same verdict, the reviewer can issue it.
en103 | SAME | en103 | 1.00 | If they disagree, the reviewer can give conditional verdicts or defer until the applicable specification can be established.
en104 | SAME | en104 | 1.00 | This argument assumes that the actual specification is in the compatible set, so the set is nonempty.
en105 | SAME | en105 | 1.00 | A rule that sees the same input and must always return a single binary verdict cannot be correct for two compatible specifications that require opposite answers.
en106 | SAME | en106 | 1.00 | This establishes an information limit, not an error rate for SOLID judgments in practice.
en107 | SAME | en107 | 1.00 | Appendix A gives the nine disclosure conditions for this case.
en108 | SAME | en108 | 1.00 | · Section 5 established whether one patch met a stated request and contract.
en109 | SAME | en109 | 1.00 | It did not determine the least costly way to meet them.
en110 | SAME | en110 | 1.00 | Returning to the drawing fixture, we ask which source boundaries the implemented candidates cross when the request, permitted placement, or caller route changes.
en111 | SAME | en111 | 1.00 | The counts describe those candidates, not a minimum over all possible implementations.
en112 | SAME | en112 | 1.00 | We first varied the request.
en113 | SAME | en113 | 1.00 | In the shape layout we added a triangle in one new file and edited the circle and square files to add a labeling operation.
en114 | SAME | en114 | 1.00 | In the operation layout we edited the drawing file to add the triangle and put the labeling operation in a new file.
en115 | SAME | en115 | 1.00 | All four candidates passed their functional checks.
en116 | SAME | en116 | 1.00 | Which layout left more existing files intact depended on the request (Figure 1A).
en117 | SAME | en117 | 1.00 | We then added the same batch-rendering function to both layouts.
en118 | SAME | en118 | 1.00 | It takes a list of shapes and brackets each rendered result.
en119 | SAME | en119 | 1.00 | We predicted that requiring the item transformation to live in the shape files would entail editing both files in the shape layout.
en120 | SAME | en120 | 1.00 | If a shared adapter was allowed, we predicted that either layout could add the feature in one new file.
en121 | SAME | en121 | 1.00 | All four candidates preserved order and duplicates, handled empty lists and unsupported shapes as specified, and preserved the existing circle and square renderings.
en122 | SAME | en122 | 1.00 | The candidate placing both transformations in the shape files edited two existing files.
en123 | SAME | en123 | 1.00 | All four added one file (Figure 1B).
en124 | SAME | en124 | 1.00 | Existing source files edited.
en125 | SAME | en125 | 1.00 | Panel A compares adding a triangle with adding a labeling operation.
en126 | SAME | en126 | 1.00 | Panel B holds the batch-rendering request fixed and varies the placement rule.
en127 | SAME | en127 | 1.00 | All four candidates in panel B passed the new and legacy behavior checks and added one file each.
en128 | SAME | en128 | 1.00 | · · · · The third comparison used an option to bracket a single rendering through the existing function.
en129 | SAME | en129 | 1.00 | Candidates that offered a new entry point left the existing files intact in both layouts.
en130 | SAME | en130 | 1.00 | With the same adapter added, the original functions still rejected bracketed=True .
en131 | SAME | en131 | 1.00 | The candidates offering the option through the original functions edited one file in the operation layout and two in the shape layout.
en132 | SAME | en132 | 1.00 | In a separate baseline whose original function could already load an external decorator, each layout delivered the option through the original entry point by adding a single file (Table 3).
en133 | SAME | en133 | 1.00 | Call paths for the new rendering option.
en134 | SAME | en134 | 1.00 | The hook was already present in the last row’s baseline.
en135 | SAME | en135 | 1.00 | Its zero-edits result does not include the cost of introducing that hook into the earlier baseline.
en136 | SAME | en136 | 1.00 | We did not measure that initial investment.
en137 | SAME | en137 | 1.00 | The negative control adds the same adapter and finds that the option remains unavailable through the original function.
en138 | SAME | en138 | 1.00 | · Fewer changed files do not by themselves establish a more maintainable design.
en139 | SAME | en139 | 1.00 | Permission to add a file needs to be paired with a path that the caller can actually use.
en140 | SAME | en140 | 1.00 | The last row of Table 3 starts counting after the hook is already in place.
en141 | SAME | en141 | 1.00 | These file counts describe the tested candidates.
en142 | SAME | en142 | 1.00 | Whether we can predict working paths for independently authored requests, and how these counts relate to maintenance effort, remain open.
en143 | SAME | en143 | 1.00 | Whether the drawing routine falls short depends on who must sort the list.
en144 | SAME | en144 | 1.00 | The benchmark measures classification performance by comparing model responses with its reference labels.
en145 | SAME | en145 | 1.00 | Applying a finding to a specific patch also requires knowing what change the patch must deliver and which behavior existing callers were promised.
en146 | SAME | en146 | 1.00 | In the catalog example, the errata requirement can settle a rejection on its own.
en147 | SAME | en147 | 1.00 | When only technical reports are needed, the verdict turns on the promise about the book prefix.
en148 | SAME | en148 | 1.00 | Comparing possible edits also requires knowing how the new behavior can reach its callers.
en149 | SAME | en149 | 1.00 | A review that calls for an edit should identify the request or commitment it relies on and the call path to which it applies.
en150 | SAME | en150 | 1.00 | The developer can then check the grounds for the verdict or identify the remaining fact that would settle it.
en151 | SAME | en151 | 1.00 | The evidence here covers the saved material of one benchmark and the candidates we constructed and ran.
en152 | SAME | en152 | 1.00 | Rather than announce a new set of axioms, the next step is to ask whether changes, protected commitments, authority, and caller routes can be represented in a form that predicts when one design has an advantage over anot
en153 | SAME | en153 | 1.00 | Such an account would be valuable if it explained both the usefulness of familiar principles and the conditions under which their preferred design loses.
en154 | SAME | en154 | 1.00 | The present paper poses that hypothesis; it does not establish it.
en155 | SAME | en155 | 1.00 | For Sections 3–4 the audit reads the archived JSON and JSONL.
en156 | SAME | en156 | 1.00 | For Sections 5–6 the fixtures run the examples constructed for this study.
en157 | SAME | en157 | 1.00 | The reproduction notes give the archive digest, the commands for Python 3.11 or later, the record and pair locators, and the complete Section 5 disclosure grid.
Summary en: same 157; edited 0; new 0.
