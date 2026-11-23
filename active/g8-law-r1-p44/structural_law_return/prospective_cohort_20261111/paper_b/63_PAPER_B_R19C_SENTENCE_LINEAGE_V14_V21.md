# Paper B R19C — Sentence Diff Index, v14–v21
Same heuristic as R19A/B, full extracted prose sentences with matching source ordinal, truncated preview; source-page appendices may be included. NOT a complete semantic line proof. v14 repeated as cross-batch baseline.

## v14 · [Notion](https://app.notion.com/p/41fef561cf928121af24cb634cdad9e3)
### ko (122 sentences)
ko001 | BASE | — | 0.00 | 로버트 마틴이 1996년에 예로 든 함수는 목록에 들어온 순서대로 도형을 그린다.
ko002 | BASE | — | 0.00 | 삼각형이 자신을 그리는 메서드를 갖고 있으면 이 함수에 손대지 않고 삼각형을 추가할 수 있다.
ko003 | BASE | — | 0.00 | 기존 함수에 사각형으로 시작하는 목록을 넘기면 여전히 사각형부터 그린다.
ko004 | BASE | — | 0.00 | 호출자가 원을 앞에 모아 넘기기로 했다면 함수는 제 일을 한다.
ko005 | BASE | — | 0.00 | 함수가 어떤 목록을 받아도 그 순서를 보장하기로 했다면 고쳐야 한다.
ko006 | BASE | — | 0.00 | 소스에서 그리는 순서를 읽을 수는 있지만, 그 순서가 잘못됐는지는 누가 정렬을 맡았는지에 달려 있다.
ko007 | BASE | — | 0.00 | 마틴의 그리기 함수는 도형을 하나 더 추가할 때는 그대로 둘 수 있었다.
ko008 | BASE | — | 0.00 | 우리는 변경 요구와 기존 호출자에 대한 약속을 확인하지 않은 채 OCP 위반이라는 평가만으로 수정안 거절을 확정하는 위험을 과도한 공리화 라고 부른다.
ko009 | BASE | — | 0.00 | 이 이름은 원칙 자체가 무조건적인 공리였다는 역사적 주장이 아니라, 원칙을 적용하는 판정 방식에 관한 것이다.
ko010 | BASE | — | 0.00 | 분류 벤치마크의 저장 자료에서 모델에 어떤 지시가 주어졌는지 확인했다.
ko011 | BASE | — | 0.00 | 이어 도서관 예제에서 코드와 수정안을 고정한 채 새 요구와 기존 호출자에게 한 약속을 바꿨다.
ko012 | BASE | — | 0.00 | 도형 예제로 돌아가서는 별도 파일에 넣은 기능을 기존 함수로도 쓸 수 있는지 확인했다.
ko013 | BASE | — | 0.00 | · · 마틴은 1996년 글에서 베르트랑 마이어의 1988년 초판 23쪽을 인용했다.
ko014 | BASE | — | 0.00 | 마이어에게 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 쓸 수 있는 모듈이다.
ko015 | BASE | — | 0.00 | 그의 도서관 예제에서 자료 유형을 하나씩 구별해 처리하는 프로그램에 기술보고서를 추가하면, 기존 모듈까지 고치거나 다시 컴파일해야 할 수 있다.
ko016 | BASE | — | 0.00 | 새 자료를 처리하는 코드의 위치에 따라 기존 모듈에 손이 가는 범위가 달라진다.
ko017 | BASE | — | 0.00 | 1995년 6월 공개 토론에서 카일 브라운은 잘못 설계된 클래스라면 소스를 고칠 수 있어야 한다고 했다.
ko018 | BASE | — | 0.00 | 마틴은 예상한 확장을 위해 기존 소스를 반드시 고쳐야 하는지를 물었다.
ko019 | BASE | — | 0.00 | 그러려면 어떤 변경이 생길지 미리 짚어야 한다.
ko020 | BASE | — | 0.00 | 2007년 공개 기록에는 다섯 원칙을 묶은 SOLID라는 이름이 나온다.
ko021 | BASE | — | 0.00 | 2009년 인터페이스 논쟁에서는 내부 클래스와 공개 플러그인 API에 서로 다른 조언이 제시됐다.
ko022 | BASE | — | 0.00 | 이 기록은 당시 원칙을 적용하거나 반대할 때 어떤 이유를 제시했는지 보여 준다.
ko023 | BASE | — | 0.00 | SOLID라는 이름이 널리 퍼지면서 적용 조건에 대한 판단이 실제로 변했는지는 별도의 역사적 증거가 필요하다.
ko024 | BASE | — | 0.00 | · · 마틴은 목록 정렬을 DrawAllShapes 가 맡게 했다.
ko025 | BASE | — | 0.00 | 한 구현에서 Circle::Precedes 는 상대 도형이 사각형이면 원을 먼저 놓는다.
ko026 | BASE | — | 0.00 | 원과 세 번째 도형의 순서를 정하려면 Circle 도 고쳐야 할 수 있다.
ko027 | BASE | — | 0.00 | 반면 도형 종류별 순서를 표에 두면 사각형을 먼저 놓기 위해 표의 두 항목만 바꾸면 된다.
ko028 | BASE | — | 0.00 | 개별 도형을 넓이순으로 그리려면 그 표에 없는 정보가 필요하다.
ko029 | BASE | — | 0.00 | 마틴이 글 후반에 비교한 두 함수는 dynamic_cast 를 쓴다.
ko030 | BASE | — | 0.00 | DrawAllShapes 의 한 구현은 원과 사각형을 골라 그리고, DrawSquaresOnly 는 사각형만 그린다.
ko031 | BASE | — | 0.00 | 모든 도형을 그려야 할 때는 출력이 하나 빠진 셈이다.
ko032 | BASE | — | 0.00 | 코드와 프롬프트만 주어진 검토자는 각 함수에 어느 책임이 있는지 어디까지 알 수 있을까?
ko033 | BASE | — | 0.00 | · · 분류 결과에 필요한 정보와 수정안의 수용 여부를 정하는 정보는 구별해 조사했다.
ko034 | BASE | — | 0.00 | 첫 번째 작업은 보존된 벤치마크를 읽는 감사이고, 두 번째는 우리가 작성한 패치에 서로 다른 요구와 계약을 대입하는 구성 사례다.
ko035 | BASE | — | 0.00 | 두 자료의 개별 코드나 실제 개발자 판정을 서로 대응시키지는 않았다.
ko036 | BASE | — | 0.00 | OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다.
ko037 | BASE | — | 0.00 | 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다.
ko038 | BASE | — | 0.00 | 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다.
ko039 | BASE | — | 0.00 | 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다.
ko040 | BASE | — | 0.00 | 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다.
ko041 | BASE | — | 0.00 | 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.
ko042 | BASE | — | 0.00 | 지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다.
ko043 | BASE | — | 0.00 | 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다.
ko044 | BASE | — | 0.00 | 이 판독은 제출 코드를 가린 지시문에 관한 것이며, 코드의 이름과 구조에서 가능한 요구를 유추할 수 있다는 사실까지 부정하지 않는다.
ko045 | BASE | — | 0.00 | 저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다.
ko046 | BASE | — | 0.00 | Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다.
ko047 | BASE | — | 0.00 | 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다.
ko048 | BASE | — | 0.00 | 압축 파일 안의 코드 자체는 실행하지 않았다.
ko049 | BASE | — | 0.00 | 도서관 예제에서는 원래 소스와 수정안, 호출 입력, 새 모듈 추가를 허용한 편집 범위를 고정했다.
ko050 | BASE | — | 0.00 | 실제 호출에서 얻은 출력·예외는 실행 관찰로 기록했다.
ko051 | BASE | — | 0.00 | 새 요구를 충족하고 적용되는 기존 계약을 보존할 때 승인한다 는 기준은 연구자가 정했다.
ko052 | BASE | — | 0.00 | 따라서 §5의 승인·거절은 이 기준과 실행 결과에서 도출한 값이지 외부 심사위원이 내린 판단이 아니다.
ko053 | BASE | — | 0.00 | 일부 정보만 공개된 경우에는 공개된 사실과 양립하는 완전 명세를 남겨 판정이 일치하는지 확인했다.
ko054 | BASE | — | 0.00 | · · Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21) Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko055 | BASE | — | 0.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko056 | BASE | — | 0.00 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko057 | BASE | — | 0.00 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko058 | BASE | — | 0.00 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko059 | BASE | — | 0.00 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko060 | BASE | — | 0.00 | 추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. gpt-4o-mini 와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다.
ko061 | BASE | — | 0.00 | 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다.
ko062 | BASE | — | 0.00 | 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.
ko063 | BASE | — | 0.00 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko064 | BASE | — | 0.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko065 | BASE | — | 0.00 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko066 | BASE | — | 0.00 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko067 | BASE | — | 0.00 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko068 | BASE | — | 0.00 | 저장된 제출 코드와 참조 쌍의 수정 전후 소스는 앞에서 명시한 문자열·구문 트리 비교에서 일치하지 않았다.
ko069 | BASE | — | 0.00 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko070 | BASE | — | 0.00 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko071 | BASE | — | 0.00 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko072 | BASE | — | 0.00 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko073 | BASE | — | 0.00 | · · · Bräuer 등(2018)은 측정 가능한 실천 규칙으로 설계 원칙의 어떤 부분을 포착할 수 있는지 전문가에게 물었다.
ko074 | BASE | — | 0.00 | Cabral 등(2024)은 기계학습 기능을 확장하는 상황에서 SOLID를 적용한 코드에 대해 참가자가 느낀 이해도와 확장 용이성을 조사했다.
ko075 | BASE | — | 0.00 | Zhu 등(2026)은 저장소에 구체적인 변경을 요구하고 기능 테스트와 구조 판정 기준을 적용했다.
ko076 | BASE | — | 0.00 | 프로그램이 무엇을 가정하고 무엇을 보장하는지를 구별하는 생각 자체는 새롭지 않다.
ko077 | BASE | — | 0.00 | 존스(1981)는 병렬 프로그램의 명세에 환경에 대한 의존 조건과 프로그램의 보장 조건을 넣었고, 구성 요소 사이에서 두 조건이 양립해야 한다는 증명 규칙을 제시했다.
ko078 | BASE | — | 0.00 | 물론 존스가 연구한 것은 OCP 리뷰가 아니라 병렬 프로그램의 올바른 구현이다.
ko079 | BASE | — | 0.00 | 여기서는 그 형식 이론을 다시 만드는 대신, 원칙 위반이라는 의견을 특정 수정안의 거절 근거로 사용하려면 어떤 약속을 확인해야 하는지 묻는다.
ko080 | BASE | — | 0.00 | 다음 절에서는 수정안을 고정하고, 검토자가 알고 있는 요구와 계약에 따라 승인 결론이 달라지는지 살핀다.
ko081 | BASE | — | 0.00 | · · 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko082 | BASE | — | 0.00 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko083 | BASE | — | 0.00 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko084 | BASE | — | 0.00 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko085 | BASE | — | 0.00 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko086 | BASE | — | 0.00 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko087 | BASE | — | 0.00 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko088 | BASE | — | 0.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko089 | BASE | — | 0.00 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko090 | BASE | — | 0.00 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko091 | BASE | — | 0.00 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko092 | BASE | — | 0.00 | 실제 명세가 검토하는 경우들 가운데 하나라는 전제에서 이 절차가 성립한다.
ko093 | BASE | — | 0.00 | 공개된 사실과 맞는 행이 없다면 명세 후보와 공개된 사실부터 다시 대조해야 한다.
ko094 | BASE | — | 0.00 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko095 | BASE | — | 0.00 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko096 | BASE | — | 0.00 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko097 | BASE | — | 0.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko098 | BASE | — | 0.00 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko099 | BASE | — | 0.00 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko100 | BASE | — | 0.00 | 다른 사례에서도 가능한 명세와 각각의 근거를 명시하면, 보류된 판정을 확정하기 위해 다음에 무엇을 확인할지 알 수 있다.
ko101 | BASE | — | 0.00 | · 완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다.
ko102 | BASE | — | 0.00 | 여기서는 앞의 질문에 해당하는 관찰만 남긴다.
ko103 | BASE | — | 0.00 | 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 bracketed=True 를 넘기면 인자를 거절했다.
ko104 | BASE | — | 0.00 | 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다.
ko105 | BASE | — | 0.00 | 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.
ko106 | BASE | — | 0.00 | 새 기능이 있다는 사실과 요구된 호출 경로에서 쓸 수 있다는 사실 은 다르다.
ko107 | BASE | — | 0.00 | 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 Paper B 통합 원고 12 · 한·영 문장 교정 및 에 원형 그대로 보존했다.
ko108 | BASE | — | 0.00 | 마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다.
ko109 | BASE | — | 0.00 | 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다.
ko110 | BASE | — | 0.00 | 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다.
ko111 | BASE | — | 0.00 | 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다.
ko112 | BASE | — | 0.00 | 원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가 가 이 논문에서 다룬 질문이다.
ko113 | BASE | — | 0.00 | 공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다.
ko114 | BASE | — | 0.00 | 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다.
ko115 | BASE | — | 0.00 | 이 연구는 한 벤치마크의 저장 입력과 연구자가 구성한 실행 예제만을 다뤘다.
ko116 | BASE | — | 0.00 | 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.
ko117 | BASE | — | 0.00 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko118 | BASE | — | 0.00 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko119 | BASE | — | 0.00 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko120 | BASE | — | 0.00 | 12판에 있던 그림 1과 파일 배치 실험은 14판 본문에 싣지 않았으며, 원본 그림과 실행 기록을 12판에 보존했다.
ko121 | BASE | — | 0.00 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko122 | BASE | — | 0.00 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
Summary ko: SAME 0, EDIT 0, NEW 0

### en (151 sentences)
en001 | BASE | — | 0.00 | In 1996 Robert Martin described a function that draws shapes in the order it receives them.
en002 | BASE | — | 0.00 | A triangle can be added without touching the function if the triangle supplies its own drawing method.
en003 | BASE | — | 0.00 | Then Martin changes the task.
en004 | BASE | — | 0.00 | Every circle must be drawn before any square.
en005 | BASE | — | 0.00 | Give the function a list that begins with a square and it still draws the square first.
en006 | BASE | — | 0.00 | Who was supposed to put the circles first?
en007 | BASE | — | 0.00 | If the caller agreed to sort the list, the routine does its job.
en008 | BASE | — | 0.00 | If the routine must guarantee that order for any list, it needs an edit.
en009 | BASE | — | 0.00 | The source tells us what gets drawn first.
en010 | BASE | — | 0.00 | The agreement tells us whether that is a problem.
en011 | BASE | — | 0.00 | Martin’s drawing routine could stay as it was when the task was to add a shape.
en012 | BASE | — | 0.00 | Making it responsible for sorting changes that judgment.
en013 | BASE | — | 0.00 | We use over-axiomatization for the risk of treating an OCP violation label as sufficient grounds to reject a patch without establishing the governing change and caller obligations.
en014 | BASE | — | 0.00 | This is a claim about the use of advice, not a historical claim that OCP became a formal axiom.
en015 | BASE | — | 0.00 | We inspect a classification benchmark’s archive to see what instructions its models received.
en016 | BASE | — | 0.00 | In a separate catalog example we keep the code and patch fixed while varying the request and the promises to existing callers.
en017 | BASE | — | 0.00 | We then return to drawing to test whether a feature added in a separate file can be reached through the original function.
en018 | BASE | — | 0.00 | · · Martin attributed the principle to Bertrand Meyer, citing page 23 of the 1988 first edition.
en019 | BASE | — | 0.00 | For Meyer, a closed module has a stable specification that other modules can rely on.
en020 | BASE | — | 0.00 | His library example gives this a practical meaning.
en021 | BASE | — | 0.00 | If a catalog handles publication types one by one, adding technical reports can require editing or recompiling existing modules.
en022 | BASE | — | 0.00 | Where the new code goes affects how much of the existing system must change.
en023 | BASE | — | 0.00 | In a June 1995 public exchange, Kyle Brown argued that developers had to be able to fix a badly designed class.
en024 | BASE | — | 0.00 | Martin asked whether an anticipated extension had to require an edit to existing source.
en025 | BASE | — | 0.00 | That answer still depends on which changes can be anticipated.
en026 | BASE | — | 0.00 | The public record uses SOLID for the five principles by 2007.
en027 | BASE | — | 0.00 | A 2009 discussion gave different advice for internal classes and public plugin APIs.
en028 | BASE | — | 0.00 | These records show particular uses and objections.
en029 | BASE | — | 0.00 | They do not establish that circulation of the SOLID label caused the governing conditions to change.
en030 | BASE | — | 0.00 | · · Martin made DrawAllShapes responsible for sorting.
en031 | BASE | — | 0.00 | In one implementation Circle::Precedes checks the other shape and puts a circle before a square.
en032 | BASE | — | 0.00 | Deciding where a third shape belongs relative to a circle can require an edit to Circle .
en033 | BASE | — | 0.00 | Placing the order of types in a table lets squares go first with a swap of two entries.
en034 | BASE | — | 0.00 | Sorting individual shapes by area would require information that the table does not hold.
en035 | BASE | — | 0.00 | Later in the article Martin compares two uses of dynamic_cast .
en036 | BASE | — | 0.00 | One version of DrawAllShapes draws circles and squares, and DrawSquaresOnly draws squares alone.
en037 | BASE | — | 0.00 | A triangle left undrawn is a missed output when the task is to draw all shapes.
en038 | BASE | — | 0.00 | When the task is to draw squares, skipping it is correct.
en039 | BASE | — | 0.00 | How much of that responsibility can a reviewer determine from code and a prompt?
en040 | BASE | — | 0.00 | · · We separated the information used to classify code from the information needed to accept a patch.
en041 | BASE | — | 0.00 | The first part audits saved benchmark inputs; the second applies requirements and caller contracts that we specified to a patch we built.
en042 | BASE | — | 0.00 | We did not match the archive submissions to the catalog patch or to actual reviewers' decisions.
en043 | BASE | — | 0.00 | The OCP reference material contains 48 before-and-after code pairs.
en044 | BASE | — | 0.00 | Sixteen saved JSONL files each contain 48 records, yielding 768 rows.
en045 | BASE | — | 0.00 | Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times.
en046 | BASE | — | 0.00 | We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality.
en047 | BASE | — | 0.00 | The result was 24 scaffolds.
en048 | BASE | — | 0.00 | Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs.
en049 | BASE | — | 0.00 | The 768 records are repeated submissions, not independent maintenance cases.
en050 | BASE | — | 0.00 | We separately read the masked instructions for case-specific change requests and protected caller commitments.
en051 | BASE | — | 0.00 | An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape.
en052 | BASE | — | 0.00 | We inspected only the text outside the submitted code; names, comments and code structure may still give other clues.
en053 | BASE | — | 0.00 | We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace.
en054 | BASE | — | 0.00 | For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions.
en055 | BASE | — | 0.00 | These tests do not establish whether inherited methods remain available or whether callers were promised a behavior.
en056 | BASE | — | 0.00 | We read code as archive data and did not execute it.
en057 | BASE | — | 0.00 | For the catalog, we fixed the baseline, patch, input calls and permissible edit boundary, ran the calls, and recorded output or exceptions.
en058 | BASE | — | 0.00 | We defined acceptance as meeting the new demand and preserving the applicable contract.
en059 | BASE | — | 0.00 | The Section 5 verdicts follow from these authored criteria and the observed behavior; they are not independent human review decisions.
en060 | BASE | — | 0.00 | With partial disclosure, we retained the complete specifications compatible with known facts and checked whether the verdicts agreed.
en061 | BASE | — | 0.00 | · Pehlivan et al. chose violation scenarios and refined the generated examples.
en062 | BASE | — | 0.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en063 | BASE | — | 0.00 | The benchmark compares model classifications with the resulting labels.
en064 | BASE | — | 0.00 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en065 | BASE | — | 0.00 | No two strategies shared a template string.
en066 | BASE | — | 0.00 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en067 | BASE | — | 0.00 | An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: gpt-4o-mini differed from the other three models.
en068 | BASE | — | 0.00 | Holding model, strategy and language fixed left one scaffold shared across twelve programs.
en069 | BASE | — | 0.00 | No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST.
en070 | BASE | — | 0.00 | These checks do not establish semantic independence or source lineage.
en071 | BASE | — | 0.00 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en072 | BASE | — | 0.00 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en073 | BASE | — | 0.00 | If a new shape is needed, that branch is a place to look.
en074 | BASE | — | 0.00 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en075 | BASE | — | 0.00 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en076 | BASE | — | 0.00 | The source comparison reported above did not identify a submitted program identical to a reference side under the tested normalizations.
en077 | BASE | — | 0.00 | Pair 37 establishes that a declaration was removed.
en078 | BASE | — | 0.00 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en079 | BASE | — | 0.00 | Evidence in the saved material and evidence needed to assess a patch.
en080 | BASE | — | 0.00 | The prompt example is in JSONL line 13 (record ID 12).
en081 | BASE | — | 0.00 | Pair 37 is in a separate reference JSON file.
en082 | BASE | — | 0.00 | · · · Bräuer et al. (2018) asked experts which parts of a design principle were captured by measurable practices.
en083 | BASE | — | 0.00 | Cabral et al. (2024) asked participants how easy they found it to understand and extend code under a bundled SOLID treatment in a machine-learning scenario.
en084 | BASE | — | 0.00 | Zhu et al. (2026) set repository change tasks and used functional and structural checks.
en085 | BASE | — | 0.00 | Distinguishing assumptions from guarantees is not a new idea.
en086 | BASE | — | 0.00 | Jones (1981) included rely and guarantee conditions in his treatment of interference between parallel programs, with proof obligations for their compatibility.
en087 | BASE | — | 0.00 | His subject was the correctness of parallel programs, not OCP review.
en088 | BASE | — | 0.00 | We do not offer a new rely–guarantee calculus.
en089 | BASE | — | 0.00 | We ask instead what evidence licenses using a design-principle finding as grounds for rejecting this patch.
en090 | BASE | — | 0.00 | In the next section we fix the patch and ask whether knowing a different requirement or caller contract changes the verdict.
en091 | BASE | — | 0.00 | · · We built a small catalog based on Meyer’s example.
en092 | BASE | — | 0.00 | The client in client.py displays each publication through the catalog function passed to it.
en093 | BASE | — | 0.00 | The patch adds reports.py to wrap that function.
en094 | BASE | — | 0.00 | The source of catalog.py and client.py stays identical.
en095 | BASE | — | 0.00 | The resulting catalog displays technical reports and still rejects errata.
en096 | BASE | — | 0.00 | For books it now prints BOOK where it used to print book .
en097 | BASE | — | 0.00 | Suppose the only new requirement is to handle technical reports.
en098 | BASE | — | 0.00 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en099 | BASE | — | 0.00 | If the book output is outside the contract, the same patch can be accepted.
en100 | BASE | — | 0.00 | Table 2 applies both contracts again when errata are also required.
en101 | BASE | — | 0.00 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en102 | BASE | — | 0.00 | Two requirements for accepting a fixed patch.
en103 | BASE | — | 0.00 | Learning that errata are required leaves the last two rows of Table 2.
en104 | BASE | — | 0.00 | Both reject the patch, so the book contract need not be settled first.
en105 | BASE | — | 0.00 | Learning that technical reports are the whole request leaves the first two rows.
en106 | BASE | — | 0.00 | One accepts and one rejects.
en107 | BASE | — | 0.00 | The next question is whether the original book output is protected.
en108 | BASE | — | 0.00 | This procedure assumes that the actual specification is among the cases under consideration.
en109 | BASE | — | 0.00 | If no row fits what was disclosed, the reviewer needs to recheck the candidate specifications against the facts.
en110 | BASE | — | 0.00 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en111 | BASE | — | 0.00 | The reviewer can give a conditional answer or defer judgment.
en112 | BASE | — | 0.00 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en113 | BASE | — | 0.00 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en114 | BASE | — | 0.00 | It adds one module, handles technical reports and errata, and keeps the original book output.
en115 | BASE | — | 0.00 | A rejection in Table 2 need not end the search for a patch within that boundary.
en116 | BASE | — | 0.00 | In another case, recording the possible specifications and the evidence for each can tell a reviewer what to check next.
en117 | BASE | — | 0.00 | · Deciding whether to accept a completed patch differs from choosing an architecture for future edits.
en118 | BASE | — | 0.00 | We retain one observation relevant to acceptance.
en119 | BASE | — | 0.00 | In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected bracketed=True .
en120 | BASE | — | 0.00 | A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.
en121 | BASE | — | 0.00 | The presence of a feature is different from its availability along a required route .
en122 | BASE | — | 0.00 | The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in Paper B 통합 원고 12 · 한·영 문장 교정 and its .
en123 | BASE | — | 0.00 | Drawing a square first establishes what a routine does, not whether it must be edited.
en124 | BASE | — | 0.00 | That depends on whether sorting belongs to the routine's obligations.
en125 | BASE | — | 0.00 | In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required.
en126 | BASE | — | 0.00 | We did not observe a real OCP label being misused to reject a patch.
en127 | BASE | — | 0.00 | We asked what additional grounds a design-principle assessment needs before it can justify an engineering decision .
en128 | BASE | — | 0.00 | Keeping the specifications compatible with known facts and checking their verdicts is elementary logic.
en129 | BASE | — | 0.00 | The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository.
en130 | BASE | — | 0.00 | Our evidence is confined to one benchmark archive and authored executable examples.
en131 | BASE | — | 0.00 | We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.
en132 | BASE | — | 0.00 | The audit in Sections 3–4 reads JSON and JSONL from the archived ZIP.
en133 | BASE | — | 0.00 | Section 5 and the call-path check in Section 6 use examples written for this study.
en134 | BASE | — | 0.00 | The shape-layout experiment and Figure 1 remain preserved in manuscript 12.
en135 | BASE | — | 0.00 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en136 | BASE | — | 0.00 | The table below gives the nine verdicts for Section 5.
en137 | BASE | — | 0.00 | Both values of a withheld field remain possible.
en138 | BASE | — | 0.00 | Defer means that the compatible rows include both acceptance and rejection. - Meyer, B.
en139 | BASE | — | 0.00 | Object-Oriented Software Construction (1st ed.), pp.
en140 | BASE | — | 0.00 | The Open–Closed Principle . . - Jones, C.
en141 | BASE | — | 0.00 | Development Methods for Computer Programs Including a Notion of Interference .
en142 | BASE | — | 0.00 | Oxford University Computing Laboratory, PRG-25.
en143 | BASE | — | 0.00 | · . - Pehlivan, F., Ergüzen, A.
en144 | BASE | — | 0.00 | M., Lami, M., & Koyuncu, A.
en145 | BASE | — | 0.00 | An Empirical Study on Prompting LLMs to Detect Design Principle Violations .
en146 | BASE | — | 0.00 | ASE 2025 NIER. . - Bräuer et al.
en147 | BASE | — | 0.00 | Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research . . - Cabral et al.
en148 | BASE | — | 0.00 | Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding . . - Zhu, H., Zhang, Q., Wang, J., Yang, Z., & Qiu, Y.
en149 | BASE | — | 0.00 | Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits . .
en150 | BASE | — | 0.00 | 이 목록은 인용된 주요 자료를 확인할 수 있게 모은 집필용 서지이며, 서지형식·인용 위치·전수 대조를 마친 제출용 참고문헌은 아직 아니다.
en151 | BASE | — | 0.00 | / These are verified reading anchors, not yet a fully formatted submission bibliography.
Summary en: SAME 0, EDIT 0, NEW 0

## v15 · [Notion](https://app.notion.com/p/41fef561cf928109bba4d8b8c58a76a7)
### ko (133 sentences)
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
ko033 | NEW | ko021 | 0.04 | · · 우리는 서로 다른 두 자료를 사용했다.
ko034 | NEW | ko010 | 0.11 | 벤치마크에서는 분류를 요구받은 모델에게 실제로 어떤 입력이 주어졌는지 조사했다.
ko035 | NEW | ko049 | 0.09 | 도서관 예제에서는 패치 한 개를 고정하고, 적용할 요구와 보호할 계약을 바꿔 가며 실행 결과와 승인 기준을 대조했다.
ko036 | NEW | ko010 | 0.08 | 벤치마크의 저장 코드와 도서관 코드는 별개이고, 어느 쪽에도 실제 검토자의 승인·거절 판단은 포함되지 않는다.
ko037 | SAME | ko036 | 1.00 | OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다.
ko038 | SAME | ko037 | 1.00 | 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다.
ko039 | SAME | ko038 | 1.00 | 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다.
ko040 | SAME | ko039 | 1.00 | 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다.
ko041 | SAME | ko040 | 1.00 | 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다.
ko042 | SAME | ko041 | 1.00 | 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.
ko043 | SAME | ko042 | 1.00 | 지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다.
ko044 | SAME | ko043 | 1.00 | 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다.
ko045 | SAME | ko044 | 1.00 | 이 판독은 제출 코드를 가린 지시문에 관한 것이며, 코드의 이름과 구조에서 가능한 요구를 유추할 수 있다는 사실까지 부정하지 않는다.
ko046 | SAME | ko045 | 1.00 | 저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다.
ko047 | SAME | ko046 | 1.00 | Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다.
ko048 | SAME | ko047 | 1.00 | 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다.
ko049 | SAME | ko048 | 1.00 | 압축 파일 안의 코드 자체는 실행하지 않았다.
ko050 | EDIT | ko049 | 0.51 | 도서관 예제에서는 원본 소스와 수정안, 호출 입력, 새 모듈을 추가할 수 있다는 편집 범위를 고정했다.
ko051 | NEW | ko055 | 0.03 | 코드 실행으로 확인한 것은 구체적인 입력에서 나온 출력과 예외다.
ko052 | NEW | ko051 | 0.20 | 반면 기술보고서·정오표 중 무엇을 요구하는지, 책 출력의 접두어가 보호 대상인지, 새 요구를 충족하면서 보호된 기존 동작을 보존해야 승인한다 는 기준은 모두 연구자가 정했다.
ko053 | NEW | ko052 | 0.08 | 따라서 §5의 표는 독립 심사위원의 판정이 아니라 우리가 지정한 기준을 실행 관찰에 적용한 결과다.
ko054 | NEW | ko053 | 0.10 | 일부 전제만 공개한 경우에는 두 요구와 두 계약으로 이루어진 후보 명세 중 공개된 사실과 맞는 것만 남겼다.
ko055 | NEW | ko041 | 0.07 | 이 후보군 밖의 실제 요구나 계약까지 조사했다고 가정하지 않는다.
ko056 | SAME | ko054 | 1.00 | · · Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21) Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko057 | SAME | ko055 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko058 | SAME | ko056 | 1.00 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko059 | SAME | ko057 | 1.00 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko060 | SAME | ko058 | 1.00 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko061 | SAME | ko059 | 1.00 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko062 | SAME | ko060 | 1.00 | 추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. gpt-4o-mini 와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다.
ko063 | SAME | ko061 | 1.00 | 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다.
ko064 | SAME | ko062 | 1.00 | 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.
ko065 | SAME | ko063 | 1.00 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko066 | SAME | ko064 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko067 | SAME | ko065 | 1.00 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko068 | SAME | ko066 | 1.00 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko069 | SAME | ko067 | 1.00 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko070 | NEW | ko068 | 0.24 | 저장 코드와 참조 쌍은 앞에서 명시한 문자열 정규화 기준에서 일치하지 않았으며, Python 코드에 한한 AST 비교에서도 일치 사례가 없었다.
ko071 | SAME | ko069 | 1.00 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko072 | SAME | ko070 | 1.00 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko073 | SAME | ko071 | 1.00 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko074 | SAME | ko072 | 1.00 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko075 | NEW | ko074 | 0.23 | · · · Bräuer 등(2018)은 설계 원칙을 어떻게 측정할지 전문가에게 물었고, Cabral 등(2024)은 SOLID를 적용한 코드를 이해하고 확장하는 경험을 조사했다.
ko076 | NEW | ko075 | 0.17 | Zhu 등(2026)은 구체적인 저장소 변경 과제에 기능 및 구조 검사를 결합했다.
ko077 | NEW | ko010 | 0.04 | 우리의 벤치마크 감사도 분류 성능을 부정하려는 것이 아니다.
ko078 | NEW | ko111 | 0.07 | 분류에 성공했다는 증거를 수정안 거절의 증거로 옮길 때 무엇이 더 필요한지를 묻는다.
ko079 | NEW | ko036 | 0.02 | · · 그 질문 자체에도 중요한 선행연구가 있다.
ko080 | NEW | ko047 | 0.05 | Kane(2013)은 검사 점수의 해석을 뒷받침하는 증거가 그 점수를 특정 결정에 사용하는 일까지 정당화하지는 않는다고 논했다.
ko081 | NEW | ko089 | 0.04 | 이는 소프트웨어 리뷰를 실험한 결과가 아니라, 평가 결과의 사용 을 따로 정당화해야 한다는 일반적인 논증이다.
ko082 | NEW | ko061 | 0.02 | Zave와 Jackson(1997)은 요구사항, 기계 명세, 환경에 관한 지식이 어떻게 연결되는지 설명하면서 행위의 통제 주체를 구별했다.
ko083 | NEW | ko004 | 0.04 | 원을 앞에 정렬할 책임이 호출자에게 있는지 함수에 있는지부터 따져야 한다는 우리의 질문도 이러한 오래된 문제의 한 사례다.
ko084 | NEW | ko077 | 0.18 | 존스(1981) 역시 병렬 프로그램에서 환경 의존 조건과 프로그램 보장 조건의 양립을 다뤘다.
ko085 | NEW | ko070 | 0.03 | · · Barr 등(2015)이 정리한 테스트 오라클 문제는 코드 실행과 올바름 판정 사이에도 근거가 필요함을 상기시킨다.
ko086 | NEW | ko047 | 0.05 | §5의 시험은 지정된 호출의 동작을 확인하지만, 그 동작을 보존하겠다는 실제 프로젝트의 약속을 입증하지는 않는다.
ko087 | NEW | ko052 | 0.03 | 따라서 다음 절의 요구·계약은 발견한 사실이 아니라 명시적으로 정한 전제다.
ko088 | SAME | ko081 | 1.00 | 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko089 | SAME | ko082 | 1.00 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko090 | SAME | ko083 | 1.00 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko091 | SAME | ko084 | 1.00 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko092 | SAME | ko085 | 1.00 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko093 | SAME | ko086 | 1.00 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko094 | SAME | ko087 | 1.00 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko095 | SAME | ko088 | 1.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko096 | NEW | ko041 | 0.05 | 책 접두어가 보호 대상이 아니라는 가정은 실제 이용자가 그 출력을 기대하지 않는다는 관찰이 아니다.
ko097 | NEW | ko048 | 0.09 | 단지 이 비교에서 보존 의무로 정하지 않았다는 뜻이다.
ko098 | SAME | ko089 | 1.00 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko099 | SAME | ko090 | 1.00 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko100 | SAME | ko091 | 1.00 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko101 | NEW | ko092 | 0.17 | 이 절차는 실제 명세가 표의 네 경우 중 하나라는 조건 아래서만 성립한다.
ko102 | NEW | ko093 | 0.17 | 공개된 사실과 맞는 행이 하나도 없다면 승인이나 거절을 내릴 것이 아니라 자료 또는 후보군이 잘못됐는지 확인해야 한다.
ko103 | SAME | ko094 | 1.00 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko104 | SAME | ko095 | 1.00 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko105 | SAME | ko096 | 1.00 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko106 | SAME | ko097 | 1.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko107 | SAME | ko098 | 1.00 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko108 | SAME | ko099 | 1.00 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko109 | NEW | ko050 | 0.06 | 이 비교에서 얻은 것은 새로운 논리 규칙이 아니다.
ko110 | NEW | ko087 | 0.05 | 한 사실만 알아도 거절이 확정되는 경우와, 책 출력 약속을 물어야 하는 경우를 구체적인 호출 결과로 구분한 것이다.
ko111 | NEW | ko114 | 0.08 | 실제 리뷰에 적용하려면 요구서와 API 문서, 테스트 및 호출 기록에서 그 약속의 근거를 따로 찾아야 한다.
ko112 | SAME | ko101 | 1.00 | · 완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다.
ko113 | SAME | ko102 | 1.00 | 여기서는 앞의 질문에 해당하는 관찰만 남긴다.
ko114 | SAME | ko103 | 1.00 | 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 bracketed=True 를 넘기면 인자를 거절했다.
ko115 | SAME | ko104 | 1.00 | 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다.
ko116 | SAME | ko105 | 1.00 | 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.
ko117 | SAME | ko106 | 1.00 | 새 기능이 있다는 사실과 요구된 호출 경로에서 쓸 수 있다는 사실 은 다르다.
ko118 | SAME | ko107 | 1.00 | 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 Paper B 통합 원고 12 · 한·영 문장 교정 및 에 원형 그대로 보존했다.
ko119 | SAME | ko108 | 1.00 | 마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다.
ko120 | SAME | ko109 | 1.00 | 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다.
ko121 | SAME | ko110 | 1.00 | 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다.
ko122 | SAME | ko111 | 1.00 | 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다.
ko123 | SAME | ko112 | 1.00 | 원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가 가 이 논문에서 다룬 질문이다.
ko124 | SAME | ko113 | 1.00 | 공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다.
ko125 | SAME | ko114 | 1.00 | 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다.
ko126 | SAME | ko115 | 1.00 | 이 연구는 한 벤치마크의 저장 입력과 연구자가 구성한 실행 예제만을 다뤘다.
ko127 | SAME | ko116 | 1.00 | 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.
ko128 | SAME | ko117 | 1.00 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko129 | SAME | ko118 | 1.00 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko130 | SAME | ko119 | 1.00 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko131 | SAME | ko120 | 1.00 | 12판에 있던 그림 1과 파일 배치 실험은 14판 본문에 싣지 않았으며, 원본 그림과 실행 기록을 12판에 보존했다.
ko132 | SAME | ko121 | 1.00 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko133 | SAME | ko122 | 1.00 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
Summary ko: SAME 102, EDIT 1, NEW 30

### en (169 sentences)
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
en040 | NEW | en045 | 0.13 | · · We used two distinct sources of evidence.
en041 | NEW | en041 | 0.20 | We audited the saved benchmark inputs to determine what a classifier was actually asked to judge.
en042 | NEW | en050 | 0.30 | Separately, we fixed one catalog patch and varied the demands and protected caller commitments against which its execution was assessed.
en043 | NEW | en042 | 0.30 | The benchmark submissions are not instances of the catalog patch, and neither source records decisions by real reviewers.
en044 | SAME | en043 | 1.00 | The OCP reference material contains 48 before-and-after code pairs.
en045 | SAME | en044 | 1.00 | Sixteen saved JSONL files each contain 48 records, yielding 768 rows.
en046 | SAME | en045 | 1.00 | Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times.
en047 | SAME | en046 | 1.00 | We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality.
en048 | SAME | en047 | 1.00 | The result was 24 scaffolds.
en049 | SAME | en048 | 1.00 | Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs.
en050 | SAME | en049 | 1.00 | The 768 records are repeated submissions, not independent maintenance cases.
en051 | SAME | en050 | 1.00 | We separately read the masked instructions for case-specific change requests and protected caller commitments.
en052 | SAME | en051 | 1.00 | An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape.
en053 | SAME | en052 | 1.00 | We inspected only the text outside the submitted code; names, comments and code structure may still give other clues.
en054 | SAME | en053 | 1.00 | We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace.
en055 | SAME | en054 | 1.00 | For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions.
en056 | SAME | en055 | 1.00 | These tests do not establish whether inherited methods remain available or whether callers were promised a behavior.
en057 | SAME | en056 | 1.00 | We read code as archive data and did not execute it.
en058 | NEW | en057 | 0.39 | For the catalog, we fixed the baseline, candidate patch, calls and permission to add a module.
en059 | NEW | en057 | 0.20 | Executing the code established outputs and exceptions for those calls.
en060 | NEW | en114 | 0.19 | The possible demands (technical reports alone, or technical reports and errata), the two scopes of the book-output obligation, and the rule that an acceptable patch must meet its demand and preserve protected behavior we
en061 | NEW | en059 | 0.38 | Table 2 therefore applies authored criteria to observed behavior; it does not report independent human decisions.
en062 | EDIT | en060 | 0.55 | For partial disclosure, we retained only the candidate specifications compatible with known facts.
en063 | NEW | en050 | 0.15 | We did not attempt to enumerate obligations outside these four constructed cases.
en064 | SAME | en061 | 1.00 | · Pehlivan et al. chose violation scenarios and refined the generated examples.
en065 | SAME | en062 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en066 | SAME | en063 | 1.00 | The benchmark compares model classifications with the resulting labels.
en067 | SAME | en064 | 1.00 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en068 | SAME | en065 | 1.00 | No two strategies shared a template string.
en069 | SAME | en066 | 1.00 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en070 | SAME | en067 | 1.00 | An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: gpt-4o-mini differed from the other three models.
en071 | SAME | en068 | 1.00 | Holding model, strategy and language fixed left one scaffold shared across twelve programs.
en072 | SAME | en069 | 1.00 | No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST.
en073 | SAME | en070 | 1.00 | These checks do not establish semantic independence or source lineage.
en074 | SAME | en071 | 1.00 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en075 | SAME | en072 | 1.00 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en076 | SAME | en073 | 1.00 | If a new shape is needed, that branch is a place to look.
en077 | SAME | en074 | 1.00 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en078 | SAME | en075 | 1.00 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en079 | NEW | en076 | 0.39 | No submitted program matched a reference side under the reported textual normalizations, and the separate Python-only AST comparison also found no match.
en080 | SAME | en077 | 1.00 | Pair 37 establishes that a declaration was removed.
en081 | SAME | en078 | 1.00 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en082 | SAME | en079 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en083 | SAME | en080 | 1.00 | The prompt example is in JSONL line 13 (record ID 12).
en084 | SAME | en081 | 1.00 | Pair 37 is in a separate reference JSON file.
en085 | NEW | en084 | 0.29 | · · · Bräuer et al. (2018) examined the measurement of design principles with experts; Cabral et al. (2024) studied understanding and extension under a bundled SOLID treatment; Zhu et al. (2026) supplied repository chang
en086 | NEW | en028 | 0.13 | These evaluate different objects.
en087 | NEW | en063 | 0.26 | Our audit does not contest the benchmark's classification task.
en088 | NEW | en040 | 0.18 | It asks what else would be needed to use such a classification as a reason to reject a patch.
en089 | NEW | en085 | 0.13 | · · This is not a new problem in general.
en090 | NEW | en129 | 0.17 | Kane (2013) argues that evidence supporting an interpretation of test scores does not automatically justify using those scores for a particular decision.
en091 | NEW | en123 | 0.16 | His work does not test software reviews; it establishes the importance of justifying an assessment's use .
en092 | NEW | en090 | 0.14 | Zave and Jackson (1997) distinguish requirements, machine specifications and knowledge of the environment, including which actor controls an action.
en093 | NEW | en124 | 0.26 | Whether sorting belongs to a caller or a drawing function is an instance of that longstanding question.
en094 | NEW | en086 | 0.31 | Jones (1981) likewise developed conditions for compatible environmental reliance and program guarantees in parallel programs.
en095 | NEW | en101 | 0.12 | We do not claim these distinctions as our invention.
en096 | NEW | en066 | 0.08 | · · Barr et al.'s (2015) survey of the test-oracle problem makes a related point about our executable fixture.
en097 | NEW | en070 | 0.14 | Tests establish outputs for chosen inputs; they do not, without an independently grounded oracle, establish which outputs a real project has promised to preserve.
en098 | NEW | en090 | 0.17 | Thus the demands and contracts in Section 5 are explicit assumptions rather than requirements recovered from a repository.
en099 | SAME | en091 | 1.00 | We built a small catalog based on Meyer’s example.
en100 | SAME | en092 | 1.00 | The client in client.py displays each publication through the catalog function passed to it.
en101 | SAME | en093 | 1.00 | The patch adds reports.py to wrap that function.
en102 | SAME | en094 | 1.00 | The source of catalog.py and client.py stays identical.
en103 | SAME | en095 | 1.00 | The resulting catalog displays technical reports and still rejects errata.
en104 | SAME | en096 | 1.00 | For books it now prints BOOK where it used to print book .
en105 | SAME | en097 | 1.00 | Suppose the only new requirement is to handle technical reports.
en106 | SAME | en098 | 1.00 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en107 | SAME | en099 | 1.00 | If the book output is outside the contract, the same patch can be accepted.
en108 | SAME | en100 | 1.00 | Table 2 applies both contracts again when errata are also required.
en109 | SAME | en101 | 1.00 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en110 | NEW | en089 | 0.10 | Excluding the book prefix from our stipulated contract is not evidence that real users have no expectation about it; it only means this example does not impose that obligation.
en111 | SAME | en102 | 1.00 | Two requirements for accepting a fixed patch.
en112 | SAME | en103 | 1.00 | Learning that errata are required leaves the last two rows of Table 2.
en113 | SAME | en104 | 1.00 | Both reject the patch, so the book contract need not be settled first.
en114 | SAME | en105 | 1.00 | Learning that technical reports are the whole request leaves the first two rows.
en115 | SAME | en106 | 1.00 | One accepts and one rejects.
en116 | SAME | en107 | 1.00 | The next question is whether the original book output is protected.
en117 | NEW | en108 | 0.38 | The procedure applies only if the actual specification is among these four authored cases.
en118 | NEW | en138 | 0.13 | If disclosure rules out every row, an empty candidate set is a reason to question the evidence or the candidate set, not to infer acceptance or rejection.
en119 | SAME | en110 | 1.00 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en120 | SAME | en111 | 1.00 | The reviewer can give a conditional answer or defer judgment.
en121 | SAME | en112 | 1.00 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en122 | SAME | en113 | 1.00 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en123 | SAME | en114 | 1.00 | It adds one module, handles technical reports and errata, and keeps the original book output.
en124 | SAME | en115 | 1.00 | A rejection in Table 2 need not end the search for a patch within that boundary.
en125 | NEW | en125 | 0.17 | The contribution is not a new logical rule: it is a concrete account of why knowing that errata are required settles this decision, whereas a reports-only demand leaves the book-output commitment to be checked.
en126 | NEW | en129 | 0.22 | Applying it to a real review would require finding that commitment in a request, API documentation, tests or caller records.
en127 | SAME | en117 | 1.00 | · Deciding whether to accept a completed patch differs from choosing an architecture for future edits.
en128 | SAME | en118 | 1.00 | We retain one observation relevant to acceptance.
en129 | SAME | en119 | 1.00 | In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected bracketed=True .
en130 | SAME | en120 | 1.00 | A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.
en131 | SAME | en121 | 1.00 | The presence of a feature is different from its availability along a required route .
en132 | SAME | en122 | 1.00 | The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in Paper B 통합 원고 12 · 한·영 문장 교정 and its .
en133 | SAME | en123 | 1.00 | Drawing a square first establishes what a routine does, not whether it must be edited.
en134 | SAME | en124 | 1.00 | That depends on whether sorting belongs to the routine's obligations.
en135 | SAME | en125 | 1.00 | In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required.
en136 | SAME | en126 | 1.00 | We did not observe a real OCP label being misused to reject a patch.
en137 | SAME | en127 | 1.00 | We asked what additional grounds a design-principle assessment needs before it can justify an engineering decision .
en138 | SAME | en128 | 1.00 | Keeping the specifications compatible with known facts and checking their verdicts is elementary logic.
en139 | SAME | en129 | 1.00 | The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository.
en140 | SAME | en130 | 1.00 | Our evidence is confined to one benchmark archive and authored executable examples.
en141 | SAME | en131 | 1.00 | We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.
en142 | SAME | en132 | 1.00 | The audit in Sections 3–4 reads JSON and JSONL from the archived ZIP.
en143 | SAME | en133 | 1.00 | Section 5 and the call-path check in Section 6 use examples written for this study.
en144 | SAME | en134 | 1.00 | The shape-layout experiment and Figure 1 remain preserved in manuscript 12.
en145 | SAME | en135 | 1.00 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en146 | SAME | en136 | 1.00 | The table below gives the nine verdicts for Section 5.
en147 | SAME | en137 | 1.00 | Both values of a withheld field remain possible.
en148 | SAME | en138 | 1.00 | Defer means that the compatible rows include both acceptance and rejection. - Meyer, B.
en149 | SAME | en139 | 1.00 | Object-Oriented Software Construction (1st ed.), pp.
en150 | SAME | en140 | 1.00 | The Open–Closed Principle . . - Jones, C.
en151 | SAME | en141 | 1.00 | Development Methods for Computer Programs Including a Notion of Interference .
en152 | SAME | en142 | 1.00 | Oxford University Computing Laboratory, PRG-25.
en153 | SAME | en143 | 1.00 | · . - Pehlivan, F., Ergüzen, A.
en154 | SAME | en144 | 1.00 | M., Lami, M., & Koyuncu, A.
en155 | SAME | en145 | 1.00 | An Empirical Study on Prompting LLMs to Detect Design Principle Violations .
en156 | SAME | en146 | 1.00 | ASE 2025 NIER. . - Bräuer et al.
en157 | SAME | en147 | 1.00 | Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research . . - Cabral et al.
en158 | SAME | en148 | 1.00 | Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding . . - Zhu, H., Zhang, Q., Wang, J., Yang, Z., & Qiu, Y.
en159 | EDIT | en149 | 0.93 | Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits . . - Kane, M.
en160 | NEW | en035 | 0.12 | Validating the Interpretations and Uses of Test Scores .
en161 | NEW | en111 | 0.08 | Journal of Educational Measurement , 50(1), 1–73.
en162 | NEW | en044 | 0.03 | · . - Zave, P., & Jackson, M.
en163 | NEW | en102 | 0.17 | Four Dark Corners of Requirements Engineering .
en164 | NEW | en139 | 0.13 | ACM Transactions on Software Engineering and Methodology , 6(1), 1–30.
en165 | NEW | en065 | 0.04 | T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S.
en166 | NEW | en035 | 0.09 | The Oracle Problem in Software Testing: A Survey .
en167 | NEW | en139 | 0.16 | IEEE Transactions on Software Engineering .
en168 | SAME | en150 | 1.00 | 이 목록은 인용된 주요 자료를 확인할 수 있게 모은 집필용 서지이며, 서지형식·인용 위치·전수 대조를 마친 제출용 참고문헌은 아직 아니다.
en169 | SAME | en151 | 1.00 | / These are verified reading anchors, not yet a fully formatted submission bibliography.
Summary en: SAME 130, EDIT 2, NEW 37

## v16 · [Notion](https://app.notion.com/p/41fef561cf9281be95b8cf89fad99c33)
### ko (137 sentences)
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
ko033 | SAME | ko033 | 1.00 | · · 우리는 서로 다른 두 자료를 사용했다.
ko034 | SAME | ko034 | 1.00 | 벤치마크에서는 분류를 요구받은 모델에게 실제로 어떤 입력이 주어졌는지 조사했다.
ko035 | SAME | ko035 | 1.00 | 도서관 예제에서는 패치 한 개를 고정하고, 적용할 요구와 보호할 계약을 바꿔 가며 실행 결과와 승인 기준을 대조했다.
ko036 | SAME | ko036 | 1.00 | 벤치마크의 저장 코드와 도서관 코드는 별개이고, 어느 쪽에도 실제 검토자의 승인·거절 판단은 포함되지 않는다.
ko037 | SAME | ko037 | 1.00 | OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다.
ko038 | SAME | ko038 | 1.00 | 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다.
ko039 | SAME | ko039 | 1.00 | 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다.
ko040 | SAME | ko040 | 1.00 | 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다.
ko041 | SAME | ko041 | 1.00 | 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다.
ko042 | SAME | ko042 | 1.00 | 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.
ko043 | SAME | ko043 | 1.00 | 지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다.
ko044 | SAME | ko044 | 1.00 | 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다.
ko045 | NEW | ko045 | 0.32 | 이 판독은 제출 코드를 가린 지시문에 관한 것이다.
ko046 | NEW | ko063 | 0.06 | 독립 감사에서 Python 저장 행 192개를 이루는 고유 코드 12개를 검사하자 4개에서 주석 토큰 46개를 발견했고, docstring을 포함한 코드는 없었다.
ko047 | NEW | ko045 | 0.06 | 주석이 기능의 의도를 암시할 수 있으므로, 지시문에 개별 요구가 없다는 사실을 코드 전체에 명세 단서가 없다는 주장으로 확대하지 않았다.
ko048 | NEW | ko049 | 0.09 | 다른 세 언어의 주석은 같은 방법으로 계수하지 않았다.
ko049 | SAME | ko046 | 1.00 | 저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다.
ko050 | SAME | ko047 | 1.00 | Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다.
ko051 | SAME | ko048 | 1.00 | 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다.
ko052 | SAME | ko049 | 1.00 | 압축 파일 안의 코드 자체는 실행하지 않았다.
ko053 | SAME | ko050 | 1.00 | 도서관 예제에서는 원본 소스와 수정안, 호출 입력, 새 모듈을 추가할 수 있다는 편집 범위를 고정했다.
ko054 | SAME | ko051 | 1.00 | 코드 실행으로 확인한 것은 구체적인 입력에서 나온 출력과 예외다.
ko055 | SAME | ko052 | 1.00 | 반면 기술보고서·정오표 중 무엇을 요구하는지, 책 출력의 접두어가 보호 대상인지, 새 요구를 충족하면서 보호된 기존 동작을 보존해야 승인한다 는 기준은 모두 연구자가 정했다.
ko056 | SAME | ko053 | 1.00 | 따라서 §5의 표는 독립 심사위원의 판정이 아니라 우리가 지정한 기준을 실행 관찰에 적용한 결과다.
ko057 | SAME | ko054 | 1.00 | 일부 전제만 공개한 경우에는 두 요구와 두 계약으로 이루어진 후보 명세 중 공개된 사실과 맞는 것만 남겼다.
ko058 | SAME | ko055 | 1.00 | 이 후보군 밖의 실제 요구나 계약까지 조사했다고 가정하지 않는다.
ko059 | SAME | ko056 | 1.00 | · · · · Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21) Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko060 | SAME | ko057 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko061 | SAME | ko058 | 1.00 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko062 | SAME | ko059 | 1.00 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko063 | SAME | ko060 | 1.00 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko064 | SAME | ko061 | 1.00 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko065 | SAME | ko062 | 1.00 | 추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. gpt-4o-mini 와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다.
ko066 | SAME | ko063 | 1.00 | 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다.
ko067 | SAME | ko064 | 1.00 | 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.
ko068 | SAME | ko065 | 1.00 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko069 | SAME | ko066 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko070 | SAME | ko067 | 1.00 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko071 | SAME | ko068 | 1.00 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko072 | SAME | ko069 | 1.00 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko073 | SAME | ko070 | 1.00 | 저장 코드와 참조 쌍은 앞에서 명시한 문자열 정규화 기준에서 일치하지 않았으며, Python 코드에 한한 AST 비교에서도 일치 사례가 없었다.
ko074 | SAME | ko071 | 1.00 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko075 | SAME | ko072 | 1.00 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko076 | SAME | ko073 | 1.00 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko077 | SAME | ko074 | 1.00 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko078 | SAME | ko075 | 1.00 | · · · Bräuer 등(2018)은 설계 원칙을 어떻게 측정할지 전문가에게 물었고, Cabral 등(2024)은 SOLID를 적용한 코드를 이해하고 확장하는 경험을 조사했다.
ko079 | SAME | ko076 | 1.00 | Zhu 등(2026)은 구체적인 저장소 변경 과제에 기능 및 구조 검사를 결합했다.
ko080 | SAME | ko077 | 1.00 | 우리의 벤치마크 감사도 분류 성능을 부정하려는 것이 아니다.
ko081 | SAME | ko078 | 1.00 | 분류에 성공했다는 증거를 수정안 거절의 증거로 옮길 때 무엇이 더 필요한지를 묻는다.
ko082 | SAME | ko079 | 1.00 | · · 그 질문 자체에도 중요한 선행연구가 있다.
ko083 | SAME | ko080 | 1.00 | Kane(2013)은 검사 점수의 해석을 뒷받침하는 증거가 그 점수를 특정 결정에 사용하는 일까지 정당화하지는 않는다고 논했다.
ko084 | SAME | ko081 | 1.00 | 이는 소프트웨어 리뷰를 실험한 결과가 아니라, 평가 결과의 사용 을 따로 정당화해야 한다는 일반적인 논증이다.
ko085 | SAME | ko082 | 1.00 | Zave와 Jackson(1997)은 요구사항, 기계 명세, 환경에 관한 지식이 어떻게 연결되는지 설명하면서 행위의 통제 주체를 구별했다.
ko086 | SAME | ko083 | 1.00 | 원을 앞에 정렬할 책임이 호출자에게 있는지 함수에 있는지부터 따져야 한다는 우리의 질문도 이러한 오래된 문제의 한 사례다.
ko087 | SAME | ko084 | 1.00 | 존스(1981) 역시 병렬 프로그램에서 환경 의존 조건과 프로그램 보장 조건의 양립을 다뤘다.
ko088 | SAME | ko085 | 1.00 | · · Barr 등(2015)이 정리한 테스트 오라클 문제는 코드 실행과 올바름 판정 사이에도 근거가 필요함을 상기시킨다.
ko089 | SAME | ko086 | 1.00 | §5의 시험은 지정된 호출의 동작을 확인하지만, 그 동작을 보존하겠다는 실제 프로젝트의 약속을 입증하지는 않는다.
ko090 | SAME | ko087 | 1.00 | 따라서 다음 절의 요구·계약은 발견한 사실이 아니라 명시적으로 정한 전제다.
ko091 | SAME | ko088 | 1.00 | 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko092 | SAME | ko089 | 1.00 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko093 | SAME | ko090 | 1.00 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko094 | SAME | ko091 | 1.00 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko095 | SAME | ko092 | 1.00 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko096 | SAME | ko093 | 1.00 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko097 | SAME | ko094 | 1.00 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko098 | SAME | ko095 | 1.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko099 | SAME | ko096 | 1.00 | 책 접두어가 보호 대상이 아니라는 가정은 실제 이용자가 그 출력을 기대하지 않는다는 관찰이 아니다.
ko100 | SAME | ko097 | 1.00 | 단지 이 비교에서 보존 의무로 정하지 않았다는 뜻이다.
ko101 | SAME | ko098 | 1.00 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko102 | SAME | ko099 | 1.00 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko103 | SAME | ko100 | 1.00 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko104 | SAME | ko101 | 1.00 | 이 절차는 실제 명세가 표의 네 경우 중 하나라는 조건 아래서만 성립한다.
ko105 | SAME | ko102 | 1.00 | 공개된 사실과 맞는 행이 하나도 없다면 승인이나 거절을 내릴 것이 아니라 자료 또는 후보군이 잘못됐는지 확인해야 한다.
ko106 | SAME | ko103 | 1.00 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko107 | SAME | ko104 | 1.00 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko108 | SAME | ko105 | 1.00 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko109 | SAME | ko106 | 1.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko110 | SAME | ko107 | 1.00 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko111 | SAME | ko108 | 1.00 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko112 | SAME | ko109 | 1.00 | 이 비교에서 얻은 것은 새로운 논리 규칙이 아니다.
ko113 | SAME | ko110 | 1.00 | 한 사실만 알아도 거절이 확정되는 경우와, 책 출력 약속을 물어야 하는 경우를 구체적인 호출 결과로 구분한 것이다.
ko114 | SAME | ko111 | 1.00 | 실제 리뷰에 적용하려면 요구서와 API 문서, 테스트 및 호출 기록에서 그 약속의 근거를 따로 찾아야 한다.
ko115 | SAME | ko112 | 1.00 | · 완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다.
ko116 | SAME | ko113 | 1.00 | 여기서는 앞의 질문에 해당하는 관찰만 남긴다.
ko117 | SAME | ko114 | 1.00 | 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 bracketed=True 를 넘기면 인자를 거절했다.
ko118 | SAME | ko115 | 1.00 | 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다.
ko119 | SAME | ko116 | 1.00 | 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.
ko120 | SAME | ko117 | 1.00 | 새 기능이 있다는 사실과 요구된 호출 경로에서 쓸 수 있다는 사실 은 다르다.
ko121 | SAME | ko118 | 1.00 | 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 Paper B 통합 원고 12 · 한·영 문장 교정 및 에 원형 그대로 보존했다.
ko122 | SAME | ko119 | 1.00 | 마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다.
ko123 | SAME | ko120 | 1.00 | 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다.
ko124 | SAME | ko121 | 1.00 | 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다.
ko125 | SAME | ko122 | 1.00 | 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다.
ko126 | SAME | ko123 | 1.00 | 원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가 가 이 논문에서 다룬 질문이다.
ko127 | SAME | ko124 | 1.00 | 공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다.
ko128 | SAME | ko125 | 1.00 | 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다.
ko129 | SAME | ko126 | 1.00 | 이 연구는 한 벤치마크의 저장 입력과 연구자가 구성한 실행 예제만을 다뤘다.
ko130 | SAME | ko127 | 1.00 | 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.
ko131 | SAME | ko128 | 1.00 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko132 | NEW | ko038 | 0.10 | 독립 감사 스크립트는 같은 ZIP을 실행 코드가 아닌 자료로 읽어 16개 JSONL 파일, 768행, 48개 고유 코드, 24개 틀, 64개 세부 집단을 재계산했고, Python 고유 코드 12개 중 주석이 있는 4개를 확인했다.
ko133 | SAME | ko129 | 1.00 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko134 | SAME | ko130 | 1.00 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko135 | SAME | ko131 | 1.00 | 12판에 있던 그림 1과 파일 배치 실험은 14판 본문에 싣지 않았으며, 원본 그림과 실행 기록을 12판에 보존했다.
ko136 | SAME | ko132 | 1.00 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko137 | SAME | ko133 | 1.00 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
Summary ko: SAME 132, EDIT 0, NEW 5

### en (173 sentences)
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
en040 | SAME | en040 | 1.00 | · · We used two distinct sources of evidence.
en041 | SAME | en041 | 1.00 | We audited the saved benchmark inputs to determine what a classifier was actually asked to judge.
en042 | SAME | en042 | 1.00 | Separately, we fixed one catalog patch and varied the demands and protected caller commitments against which its execution was assessed.
en043 | SAME | en043 | 1.00 | The benchmark submissions are not instances of the catalog patch, and neither source records decisions by real reviewers.
en044 | SAME | en044 | 1.00 | The OCP reference material contains 48 before-and-after code pairs.
en045 | SAME | en045 | 1.00 | Sixteen saved JSONL files each contain 48 records, yielding 768 rows.
en046 | SAME | en046 | 1.00 | Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times.
en047 | SAME | en047 | 1.00 | We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality.
en048 | SAME | en048 | 1.00 | The result was 24 scaffolds.
en049 | SAME | en049 | 1.00 | Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs.
en050 | SAME | en050 | 1.00 | The 768 records are repeated submissions, not independent maintenance cases.
en051 | SAME | en051 | 1.00 | We separately read the masked instructions for case-specific change requests and protected caller commitments.
en052 | SAME | en052 | 1.00 | An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape.
en053 | NEW | en053 | 0.33 | We inspected the text outside the submitted code, not the whole semantic context.
en054 | NEW | en079 | 0.15 | In a separate replication, the 192 saved Python rows reduced to twelve distinct code submissions; four contained a total of 46 comment tokens, and none had an AST-detected docstring.
en055 | NEW | en087 | 0.15 | These comments may convey implementation intent, but counting them does not establish a contract.
en056 | NEW | en070 | 0.13 | We did not perform the same comment-token audit for the other three languages.
en057 | SAME | en054 | 1.00 | We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace.
en058 | SAME | en055 | 1.00 | For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions.
en059 | SAME | en056 | 1.00 | These tests do not establish whether inherited methods remain available or whether callers were promised a behavior.
en060 | SAME | en057 | 1.00 | We read code as archive data and did not execute it.
en061 | SAME | en058 | 1.00 | For the catalog, we fixed the baseline, candidate patch, calls and permission to add a module.
en062 | SAME | en059 | 1.00 | Executing the code established outputs and exceptions for those calls.
en063 | SAME | en060 | 1.00 | The possible demands (technical reports alone, or technical reports and errata), the two scopes of the book-output obligation, and the rule that an acceptable patch must meet its demand and preserve protected behavior we
en064 | SAME | en061 | 1.00 | Table 2 therefore applies authored criteria to observed behavior; it does not report independent human decisions.
en065 | SAME | en062 | 1.00 | For partial disclosure, we retained only the candidate specifications compatible with known facts.
en066 | SAME | en063 | 1.00 | We did not attempt to enumerate obligations outside these four constructed cases.
en067 | SAME | en064 | 1.00 | · · · Pehlivan et al. chose violation scenarios and refined the generated examples.
en068 | SAME | en065 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en069 | SAME | en066 | 1.00 | The benchmark compares model classifications with the resulting labels.
en070 | SAME | en067 | 1.00 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en071 | SAME | en068 | 1.00 | No two strategies shared a template string.
en072 | SAME | en069 | 1.00 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en073 | SAME | en070 | 1.00 | An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: gpt-4o-mini differed from the other three models.
en074 | SAME | en071 | 1.00 | Holding model, strategy and language fixed left one scaffold shared across twelve programs.
en075 | SAME | en072 | 1.00 | No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST.
en076 | SAME | en073 | 1.00 | These checks do not establish semantic independence or source lineage.
en077 | SAME | en074 | 1.00 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en078 | SAME | en075 | 1.00 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en079 | SAME | en076 | 1.00 | If a new shape is needed, that branch is a place to look.
en080 | SAME | en077 | 1.00 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en081 | SAME | en078 | 1.00 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en082 | SAME | en079 | 1.00 | No submitted program matched a reference side under the reported textual normalizations, and the separate Python-only AST comparison also found no match.
en083 | SAME | en080 | 1.00 | Pair 37 establishes that a declaration was removed.
en084 | SAME | en081 | 1.00 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en085 | SAME | en082 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en086 | SAME | en083 | 1.00 | The prompt example is in JSONL line 13 (record ID 12).
en087 | SAME | en084 | 1.00 | Pair 37 is in a separate reference JSON file.
en088 | SAME | en085 | 1.00 | · · · Bräuer et al. (2018) examined the measurement of design principles with experts; Cabral et al. (2024) studied understanding and extension under a bundled SOLID treatment; Zhu et al. (2026) supplied repository chang
en089 | SAME | en086 | 1.00 | These evaluate different objects.
en090 | SAME | en087 | 1.00 | Our audit does not contest the benchmark's classification task.
en091 | SAME | en088 | 1.00 | It asks what else would be needed to use such a classification as a reason to reject a patch.
en092 | SAME | en089 | 1.00 | · · This is not a new problem in general.
en093 | SAME | en090 | 1.00 | Kane (2013) argues that evidence supporting an interpretation of test scores does not automatically justify using those scores for a particular decision.
en094 | SAME | en091 | 1.00 | His work does not test software reviews; it establishes the importance of justifying an assessment's use .
en095 | SAME | en092 | 1.00 | Zave and Jackson (1997) distinguish requirements, machine specifications and knowledge of the environment, including which actor controls an action.
en096 | SAME | en093 | 1.00 | Whether sorting belongs to a caller or a drawing function is an instance of that longstanding question.
en097 | SAME | en094 | 1.00 | Jones (1981) likewise developed conditions for compatible environmental reliance and program guarantees in parallel programs.
en098 | SAME | en095 | 1.00 | We do not claim these distinctions as our invention.
en099 | SAME | en096 | 1.00 | · · Barr et al.'s (2015) survey of the test-oracle problem makes a related point about our executable fixture.
en100 | SAME | en097 | 1.00 | Tests establish outputs for chosen inputs; they do not, without an independently grounded oracle, establish which outputs a real project has promised to preserve.
en101 | SAME | en098 | 1.00 | Thus the demands and contracts in Section 5 are explicit assumptions rather than requirements recovered from a repository.
en102 | SAME | en099 | 1.00 | We built a small catalog based on Meyer’s example.
en103 | SAME | en100 | 1.00 | The client in client.py displays each publication through the catalog function passed to it.
en104 | SAME | en101 | 1.00 | The patch adds reports.py to wrap that function.
en105 | SAME | en102 | 1.00 | The source of catalog.py and client.py stays identical.
en106 | SAME | en103 | 1.00 | The resulting catalog displays technical reports and still rejects errata.
en107 | SAME | en104 | 1.00 | For books it now prints BOOK where it used to print book .
en108 | SAME | en105 | 1.00 | Suppose the only new requirement is to handle technical reports.
en109 | SAME | en106 | 1.00 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en110 | SAME | en107 | 1.00 | If the book output is outside the contract, the same patch can be accepted.
en111 | SAME | en108 | 1.00 | Table 2 applies both contracts again when errata are also required.
en112 | SAME | en109 | 1.00 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en113 | SAME | en110 | 1.00 | Excluding the book prefix from our stipulated contract is not evidence that real users have no expectation about it; it only means this example does not impose that obligation.
en114 | SAME | en111 | 1.00 | Two requirements for accepting a fixed patch.
en115 | SAME | en112 | 1.00 | Learning that errata are required leaves the last two rows of Table 2.
en116 | SAME | en113 | 1.00 | Both reject the patch, so the book contract need not be settled first.
en117 | SAME | en114 | 1.00 | Learning that technical reports are the whole request leaves the first two rows.
en118 | SAME | en115 | 1.00 | One accepts and one rejects.
en119 | SAME | en116 | 1.00 | The next question is whether the original book output is protected.
en120 | SAME | en117 | 1.00 | The procedure applies only if the actual specification is among these four authored cases.
en121 | SAME | en118 | 1.00 | If disclosure rules out every row, an empty candidate set is a reason to question the evidence or the candidate set, not to infer acceptance or rejection.
en122 | SAME | en119 | 1.00 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en123 | SAME | en120 | 1.00 | The reviewer can give a conditional answer or defer judgment.
en124 | SAME | en121 | 1.00 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en125 | SAME | en122 | 1.00 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en126 | SAME | en123 | 1.00 | It adds one module, handles technical reports and errata, and keeps the original book output.
en127 | SAME | en124 | 1.00 | A rejection in Table 2 need not end the search for a patch within that boundary.
en128 | SAME | en125 | 1.00 | The contribution is not a new logical rule: it is a concrete account of why knowing that errata are required settles this decision, whereas a reports-only demand leaves the book-output commitment to be checked.
en129 | SAME | en126 | 1.00 | Applying it to a real review would require finding that commitment in a request, API documentation, tests or caller records.
en130 | SAME | en127 | 1.00 | · Deciding whether to accept a completed patch differs from choosing an architecture for future edits.
en131 | SAME | en128 | 1.00 | We retain one observation relevant to acceptance.
en132 | SAME | en129 | 1.00 | In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected bracketed=True .
en133 | SAME | en130 | 1.00 | A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.
en134 | SAME | en131 | 1.00 | The presence of a feature is different from its availability along a required route .
en135 | SAME | en132 | 1.00 | The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in Paper B 통합 원고 12 · 한·영 문장 교정 and its .
en136 | SAME | en133 | 1.00 | Drawing a square first establishes what a routine does, not whether it must be edited.
en137 | SAME | en134 | 1.00 | That depends on whether sorting belongs to the routine's obligations.
en138 | SAME | en135 | 1.00 | In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required.
en139 | SAME | en136 | 1.00 | We did not observe a real OCP label being misused to reject a patch.
en140 | SAME | en137 | 1.00 | We asked what additional grounds a design-principle assessment needs before it can justify an engineering decision .
en141 | SAME | en138 | 1.00 | Keeping the specifications compatible with known facts and checking their verdicts is elementary logic.
en142 | SAME | en139 | 1.00 | The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository.
en143 | SAME | en140 | 1.00 | Our evidence is confined to one benchmark archive and authored executable examples.
en144 | SAME | en141 | 1.00 | We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.
en145 | EDIT | en142 | 0.57 | The audits in Sections 3–4 read the archived JSON and JSONL as data.
en146 | NEW | en071 | 0.18 | A separate script reproduced sixteen JSONL files, 768 rows, 48 distinct submissions, 24 scaffolds and 64 fixed model–strategy–language groups, and counted Python comments in four of twelve unique submissions.
en147 | SAME | en143 | 1.00 | Section 5 and the call-path check in Section 6 use examples written for this study.
en148 | SAME | en144 | 1.00 | The shape-layout experiment and Figure 1 remain preserved in manuscript 12.
en149 | SAME | en145 | 1.00 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en150 | SAME | en146 | 1.00 | The table below gives the nine verdicts for Section 5.
en151 | SAME | en147 | 1.00 | Both values of a withheld field remain possible.
en152 | SAME | en148 | 1.00 | Defer means that the compatible rows include both acceptance and rejection. - Meyer, B.
en153 | SAME | en149 | 1.00 | Object-Oriented Software Construction (1st ed.), pp.
en154 | SAME | en150 | 1.00 | The Open–Closed Principle . . - Jones, C.
en155 | SAME | en151 | 1.00 | Development Methods for Computer Programs Including a Notion of Interference .
en156 | SAME | en152 | 1.00 | Oxford University Computing Laboratory, PRG-25.
en157 | SAME | en153 | 1.00 | · . - Pehlivan, F., Ergüzen, A.
en158 | SAME | en154 | 1.00 | M., Lami, M., & Koyuncu, A.
en159 | SAME | en155 | 1.00 | An Empirical Study on Prompting LLMs to Detect Design Principle Violations .
en160 | SAME | en156 | 1.00 | ASE 2025 NIER. . - Bräuer et al.
en161 | SAME | en157 | 1.00 | Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research . . - Cabral et al.
en162 | SAME | en158 | 1.00 | Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding . . - Zhu, H., Zhang, Q., Wang, J., Yang, Z., & Qiu, Y.
en163 | SAME | en159 | 1.00 | Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits . . - Kane, M.
en164 | SAME | en160 | 1.00 | Validating the Interpretations and Uses of Test Scores .
en165 | SAME | en161 | 1.00 | Journal of Educational Measurement , 50(1), 1–73.
en166 | SAME | en162 | 1.00 | · . - Zave, P., & Jackson, M.
en167 | SAME | en163 | 1.00 | Four Dark Corners of Requirements Engineering .
en168 | SAME | en164 | 1.00 | ACM Transactions on Software Engineering and Methodology , 6(1), 1–30.
en169 | SAME | en165 | 1.00 | T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S.
en170 | SAME | en166 | 1.00 | The Oracle Problem in Software Testing: A Survey .
en171 | SAME | en167 | 1.00 | IEEE Transactions on Software Engineering .
en172 | SAME | en168 | 1.00 | 이 목록은 인용된 주요 자료를 확인할 수 있게 모은 집필용 서지이며, 서지형식·인용 위치·전수 대조를 마친 제출용 참고문헌은 아직 아니다.
en173 | SAME | en169 | 1.00 | / These are verified reading anchors, not yet a fully formatted submission bibliography.
Summary en: SAME 167, EDIT 1, NEW 5

## v17 · [Notion](https://app.notion.com/p/41fef561cf9281da9ed2c282695b2c63)
### ko (166 sentences)
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
ko033 | SAME | ko033 | 1.00 | · · 우리는 서로 다른 두 자료를 사용했다.
ko034 | SAME | ko034 | 1.00 | 벤치마크에서는 분류를 요구받은 모델에게 실제로 어떤 입력이 주어졌는지 조사했다.
ko035 | SAME | ko035 | 1.00 | 도서관 예제에서는 패치 한 개를 고정하고, 적용할 요구와 보호할 계약을 바꿔 가며 실행 결과와 승인 기준을 대조했다.
ko036 | SAME | ko036 | 1.00 | 벤치마크의 저장 코드와 도서관 코드는 별개이고, 어느 쪽에도 실제 검토자의 승인·거절 판단은 포함되지 않는다.
ko037 | SAME | ko037 | 1.00 | OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다.
ko038 | SAME | ko038 | 1.00 | 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다.
ko039 | SAME | ko039 | 1.00 | 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다.
ko040 | SAME | ko040 | 1.00 | 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다.
ko041 | SAME | ko041 | 1.00 | 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다.
ko042 | SAME | ko042 | 1.00 | 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.
ko043 | SAME | ko043 | 1.00 | 지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다.
ko044 | SAME | ko044 | 1.00 | 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다.
ko045 | SAME | ko045 | 1.00 | 이 판독은 제출 코드를 가린 지시문에 관한 것이다.
ko046 | SAME | ko046 | 1.00 | 독립 감사에서 Python 저장 행 192개를 이루는 고유 코드 12개를 검사하자 4개에서 주석 토큰 46개를 발견했고, docstring을 포함한 코드는 없었다.
ko047 | SAME | ko047 | 1.00 | 주석이 기능의 의도를 암시할 수 있으므로, 지시문에 개별 요구가 없다는 사실을 코드 전체에 명세 단서가 없다는 주장으로 확대하지 않았다.
ko048 | SAME | ko048 | 1.00 | 다른 세 언어의 주석은 같은 방법으로 계수하지 않았다.
ko049 | SAME | ko049 | 1.00 | 저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다.
ko050 | SAME | ko050 | 1.00 | Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다.
ko051 | SAME | ko051 | 1.00 | 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다.
ko052 | SAME | ko052 | 1.00 | 압축 파일 안의 코드 자체는 실행하지 않았다.
ko053 | SAME | ko053 | 1.00 | 도서관 예제에서는 원본 소스와 수정안, 호출 입력, 새 모듈을 추가할 수 있다는 편집 범위를 고정했다.
ko054 | SAME | ko054 | 1.00 | 코드 실행으로 확인한 것은 구체적인 입력에서 나온 출력과 예외다.
ko055 | SAME | ko055 | 1.00 | 반면 기술보고서·정오표 중 무엇을 요구하는지, 책 출력의 접두어가 보호 대상인지, 새 요구를 충족하면서 보호된 기존 동작을 보존해야 승인한다 는 기준은 모두 연구자가 정했다.
ko056 | SAME | ko056 | 1.00 | 따라서 §5의 표는 독립 심사위원의 판정이 아니라 우리가 지정한 기준을 실행 관찰에 적용한 결과다.
ko057 | SAME | ko057 | 1.00 | 일부 전제만 공개한 경우에는 두 요구와 두 계약으로 이루어진 후보 명세 중 공개된 사실과 맞는 것만 남겼다.
ko058 | SAME | ko058 | 1.00 | 이 후보군 밖의 실제 요구나 계약까지 조사했다고 가정하지 않는다.
ko059 | SAME | ko059 | 1.00 | · · · · Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21) Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko060 | SAME | ko060 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko061 | SAME | ko061 | 1.00 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko062 | SAME | ko062 | 1.00 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko063 | SAME | ko063 | 1.00 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko064 | SAME | ko064 | 1.00 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko065 | SAME | ko065 | 1.00 | 추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. gpt-4o-mini 와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다.
ko066 | SAME | ko066 | 1.00 | 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다.
ko067 | SAME | ko067 | 1.00 | 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.
ko068 | SAME | ko068 | 1.00 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko069 | SAME | ko069 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko070 | SAME | ko070 | 1.00 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko071 | SAME | ko071 | 1.00 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko072 | SAME | ko072 | 1.00 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko073 | SAME | ko073 | 1.00 | 저장 코드와 참조 쌍은 앞에서 명시한 문자열 정규화 기준에서 일치하지 않았으며, Python 코드에 한한 AST 비교에서도 일치 사례가 없었다.
ko074 | SAME | ko074 | 1.00 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko075 | SAME | ko075 | 1.00 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko076 | SAME | ko076 | 1.00 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko077 | SAME | ko077 | 1.00 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko078 | SAME | ko078 | 1.00 | · · · Bräuer 등(2018)은 설계 원칙을 어떻게 측정할지 전문가에게 물었고, Cabral 등(2024)은 SOLID를 적용한 코드를 이해하고 확장하는 경험을 조사했다.
ko079 | SAME | ko079 | 1.00 | Zhu 등(2026)은 구체적인 저장소 변경 과제에 기능 및 구조 검사를 결합했다.
ko080 | SAME | ko080 | 1.00 | 우리의 벤치마크 감사도 분류 성능을 부정하려는 것이 아니다.
ko081 | SAME | ko081 | 1.00 | 분류에 성공했다는 증거를 수정안 거절의 증거로 옮길 때 무엇이 더 필요한지를 묻는다.
ko082 | NEW | ko114 | 0.03 | · · 실제 리뷰 연구는 이 논문의 주장 범위를 더 엄격하게 제한한다.
ko083 | NEW | ko078 | 0.03 | Widyasari 등(2025)은 Gerrit 코드 리뷰 댓글 793건을 분석하고 규칙이나 원칙을 근거로 드는 설명 유형을 확인했다.
ko084 | NEW | ko111 | 0.06 | 이는 원칙에 의거한 설명이 리뷰에 존재한다는 증거지만, 원칙이 잘못 적용돼 특정 수정안이 거절됐다는 증거는 아니다.
ko085 | NEW | ko078 | 0.04 | Papotti 등(2024)은 컴퓨터과학 석사과정 학생 72명을 대상으로 보안 자동 수리 패치의 채택 여부를 실험했다.
ko086 | NEW | ko126 | 0.02 | 제안 도구의 전문성을 알리는 정보에 따라 판단이 바뀌는 현상을 관찰했지만, 원칙 위반 라벨을 대상으로 한 연구는 아니다.
ko087 | NEW | ko129 | 0.04 | 두 논문의 실제 사람에 대한 관측은 우리가 구성한 표 2의 승인 기준과 다르다.
ko088 | NEW | ko034 | 0.03 | · Jin과 Chen(2026)은 정답 코드와 결함 코드에 대한 다섯 언어 모델의 요구 적합성 판단을 세 프로그래밍 벤치마크에서 실험하고, 맞는 코드를 잘못 거절하는 현상과 설명·수정 제안을 요구하는 프롬프트의 위험을 보고했다.
ko089 | NEW | ko074 | 0.02 | 따라서 LLM의 과잉 거절을 처음 지적했다고 주장할 수 없다.
ko090 | NEW | ko033 | 0.03 | Ling·Zou·Liu(2026)는 공개 GitHub 변경 사례의 질적 연구에서 병합, 이슈 종료, 요구 충족이 서로 다른 결과일 수 있음을 논증했다.
ko091 | NEW | ko080 | 0.07 | 수용 경계가 조건부라는 발견도 우리의 최초성이 아니다.
ko092 | NEW | ko090 | 0.02 | 우리 사례는 실행 결과가 고정된 패치에서 현재 공개된 요구·계약이 정당화하는 판정과 추가 질문을 정확하게 분리하는 재현 가능한 실례 다.
ko093 | SAME | ko082 | 1.00 | · 그 질문 자체에도 중요한 선행연구가 있다.
ko094 | SAME | ko083 | 1.00 | Kane(2013)은 검사 점수의 해석을 뒷받침하는 증거가 그 점수를 특정 결정에 사용하는 일까지 정당화하지는 않는다고 논했다.
ko095 | SAME | ko084 | 1.00 | 이는 소프트웨어 리뷰를 실험한 결과가 아니라, 평가 결과의 사용 을 따로 정당화해야 한다는 일반적인 논증이다.
ko096 | SAME | ko085 | 1.00 | Zave와 Jackson(1997)은 요구사항, 기계 명세, 환경에 관한 지식이 어떻게 연결되는지 설명하면서 행위의 통제 주체를 구별했다.
ko097 | SAME | ko086 | 1.00 | 원을 앞에 정렬할 책임이 호출자에게 있는지 함수에 있는지부터 따져야 한다는 우리의 질문도 이러한 오래된 문제의 한 사례다.
ko098 | SAME | ko087 | 1.00 | 존스(1981) 역시 병렬 프로그램에서 환경 의존 조건과 프로그램 보장 조건의 양립을 다뤘다.
ko099 | SAME | ko088 | 1.00 | · · Barr 등(2015)이 정리한 테스트 오라클 문제는 코드 실행과 올바름 판정 사이에도 근거가 필요함을 상기시킨다.
ko100 | SAME | ko089 | 1.00 | §5의 시험은 지정된 호출의 동작을 확인하지만, 그 동작을 보존하겠다는 실제 프로젝트의 약속을 입증하지는 않는다.
ko101 | SAME | ko090 | 1.00 | 따라서 다음 절의 요구·계약은 발견한 사실이 아니라 명시적으로 정한 전제다.
ko102 | SAME | ko091 | 1.00 | 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko103 | SAME | ko092 | 1.00 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko104 | SAME | ko093 | 1.00 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko105 | SAME | ko094 | 1.00 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko106 | SAME | ko095 | 1.00 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko107 | SAME | ko096 | 1.00 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko108 | SAME | ko097 | 1.00 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko109 | SAME | ko098 | 1.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko110 | SAME | ko099 | 1.00 | 책 접두어가 보호 대상이 아니라는 가정은 실제 이용자가 그 출력을 기대하지 않는다는 관찰이 아니다.
ko111 | SAME | ko100 | 1.00 | 단지 이 비교에서 보존 의무로 정하지 않았다는 뜻이다.
ko112 | SAME | ko101 | 1.00 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko113 | SAME | ko102 | 1.00 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko114 | SAME | ko103 | 1.00 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko115 | SAME | ko104 | 1.00 | 이 절차는 실제 명세가 표의 네 경우 중 하나라는 조건 아래서만 성립한다.
ko116 | SAME | ko105 | 1.00 | 공개된 사실과 맞는 행이 하나도 없다면 승인이나 거절을 내릴 것이 아니라 자료 또는 후보군이 잘못됐는지 확인해야 한다.
ko117 | SAME | ko106 | 1.00 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko118 | SAME | ko107 | 1.00 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko119 | SAME | ko108 | 1.00 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko120 | NEW | ko055 | 0.04 | 이 네 가지 연구자 정의 명세 안에서 정오표가 필수인지 (E), 책 접두어를 보호하는지 (B)로 쓰면 현재 패치의 승인 조건은 (\\neg E\\land\\neg B)다.
ko121 | NEW | ko028 | 0.08 | 승인에는 두 조건 모두 부정이라는 정보가 필요하지만, 거절은 (E) 또는 (B) 가운데 어느 하나만 참이어도 확정된다.
ko122 | NEW | ko033 | 0.05 | 두 조건이 미공개라면 승인 명세 ((E=0,B=0))와 거절 명세 ((E=1,B=0))가 모두 남으므로 보류에는 서로 다른 결론을 내는 구체적 증거가 존재한다.
ko123 | NEW | ko102 | 0.16 | 기술보고서만 요구된다는 사실을 확인하면 다음 질문은 책 접두어 보호 여부다.
ko124 | NEW | ko106 | 0.05 | 반면 아무 사실도 모를 때에는 두 질문 중 하나만으로 모든 경우의 판정을 확정할 수 없다.
ko125 | NEW | ko112 | 0.29 | 이것은 새로운 논리 규칙이 아니라 고전적인 유한 정보 집합 판정이다.
ko126 | NEW | ko050 | 0.06 | 별도 Python 코드는 네 명세의 공개 상태 아홉 가지, 최소 승인·거절 증거, 보류 상태의 대립 명세, 모순된 사실의 처리까지 검사했고 가 통과했다.
ko127 | NEW | ko036 | 0.07 | 이 테스트가 실제 검토자의 판단이나 원본 도서관 프로그램의 전체 동작을 재검증한 것은 아니다.
ko128 | NEW | ko102 | 0.04 | 또한 고정된 계약에 관한 사실을 알게 되는 것 과 계약 자체를 변경하는 것 을 구별해야 한다.
ko129 | NEW | ko057 | 0.03 | 앞의 경우에는 가능한 명세의 집합이 줄지만, 뒤의 경우에는 승인 조건 자체가 달라질 수 있다.
ko130 | SAME | ko109 | 1.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko131 | SAME | ko110 | 1.00 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko132 | SAME | ko111 | 1.00 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko133 | SAME | ko112 | 1.00 | 이 비교에서 얻은 것은 새로운 논리 규칙이 아니다.
ko134 | SAME | ko113 | 1.00 | 한 사실만 알아도 거절이 확정되는 경우와, 책 출력 약속을 물어야 하는 경우를 구체적인 호출 결과로 구분한 것이다.
ko135 | SAME | ko114 | 1.00 | 실제 리뷰에 적용하려면 요구서와 API 문서, 테스트 및 호출 기록에서 그 약속의 근거를 따로 찾아야 한다.
ko136 | SAME | ko115 | 1.00 | · 완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다.
ko137 | SAME | ko116 | 1.00 | 여기서는 앞의 질문에 해당하는 관찰만 남긴다.
ko138 | SAME | ko117 | 1.00 | 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 bracketed=True 를 넘기면 인자를 거절했다.
ko139 | SAME | ko118 | 1.00 | 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다.
ko140 | SAME | ko119 | 1.00 | 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.
ko141 | SAME | ko120 | 1.00 | 새 기능이 있다는 사실과 요구된 호출 경로에서 쓸 수 있다는 사실 은 다르다.
ko142 | NEW | ko042 | 0.05 | 더 나아가 동일한 HTTP 응답도 모든 프로그램 문맥에서의 동등성을 의미하지 않는다.
ko143 | NEW | ko021 | 0.04 | 별도로 수행한 P44 원본 Go 대조군에서는 http.HandlerFunc 로 감싼 구현이 기존 추가 인터페이스 메서드를 노출하지 않는 반례를 확인했다.
ko144 | NEW | ko036 | 0.04 | 이 사례는 도서관 패치 실험과는 별개이며 고전적인 Go 타입 의미론으로 설명된다.
ko145 | SAME | ko121 | 1.00 | 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 Paper B 통합 원고 12 · 한·영 문장 교정 및 에 원형 그대로 보존했다.
ko146 | SAME | ko122 | 1.00 | 마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다.
ko147 | SAME | ko123 | 1.00 | 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다.
ko148 | SAME | ko124 | 1.00 | 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다.
ko149 | SAME | ko125 | 1.00 | 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다.
ko150 | SAME | ko126 | 1.00 | 원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가 가 이 논문에서 다룬 질문이다.
ko151 | NEW | ko118 | 0.05 | 실제 검토에서 먼저 확인할 것은 수정안의 새 기능만이 아니라, 요구한 사람이나 합의된 문서가 그 기능을 어느 진입점에서 제공하도록 정했는지다.
ko152 | NEW | ko114 | 0.14 | 그다음 기존 호출자가 의존하는 동작 중 무엇이 보호 대상인지 요구서·API 문서·테스트·호출 코드에서 근거를 찾아야 한다.
ko153 | NEW | ko126 | 0.05 | 이 근거가 둘 이상의 가능한 계약을 남긴다면, 원칙 위반이라는 이름으로 결론을 확정하기보다 계약의 출처와 범위를 묻는 편이 정확하다.
ko154 | NEW | ko119 | 0.10 | 반대로 새로운 요구를 충족하지 못한다는 사실이 이미 확정됐다면, 어떤 기존 계약이 추가로 보호되는지 모두 조사하기 전에 해당 수정안을 거절할 수도 있다.
ko155 | NEW | ko054 | 0.03 | 이러한 질문의 순서는 이 논문의 구성 사례에서 나온 실무적 제안이지, 실제 개발 조직의 효율이 개선됐다는 관측 결과는 아니다.
ko156 | SAME | ko127 | 1.00 | 공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다.
ko157 | SAME | ko128 | 1.00 | 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다.
ko158 | SAME | ko129 | 1.00 | 이 연구는 한 벤치마크의 저장 입력과 연구자가 구성한 실행 예제만을 다뤘다.
ko159 | SAME | ko130 | 1.00 | 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.
ko160 | SAME | ko131 | 1.00 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko161 | SAME | ko132 | 1.00 | 독립 감사 스크립트는 같은 ZIP을 실행 코드가 아닌 자료로 읽어 16개 JSONL 파일, 768행, 48개 고유 코드, 24개 틀, 64개 세부 집단을 재계산했고, Python 고유 코드 12개 중 주석이 있는 4개를 확인했다.
ko162 | SAME | ko133 | 1.00 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko163 | SAME | ko134 | 1.00 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko164 | EDIT | ko135 | 0.87 | 12판에 있던 그림 1과 파일 배치 실험은 17판 본문에 싣지 않았으며, 원본 그림과 실행 기록을 12판에 보존했다.
ko165 | SAME | ko136 | 1.00 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko166 | SAME | ko137 | 1.00 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
Summary ko: SAME 136, EDIT 1, NEW 29

### en (216 sentences)
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
en040 | SAME | en040 | 1.00 | · · We used two distinct sources of evidence.
en041 | SAME | en041 | 1.00 | We audited the saved benchmark inputs to determine what a classifier was actually asked to judge.
en042 | SAME | en042 | 1.00 | Separately, we fixed one catalog patch and varied the demands and protected caller commitments against which its execution was assessed.
en043 | SAME | en043 | 1.00 | The benchmark submissions are not instances of the catalog patch, and neither source records decisions by real reviewers.
en044 | SAME | en044 | 1.00 | The OCP reference material contains 48 before-and-after code pairs.
en045 | SAME | en045 | 1.00 | Sixteen saved JSONL files each contain 48 records, yielding 768 rows.
en046 | SAME | en046 | 1.00 | Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times.
en047 | SAME | en047 | 1.00 | We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality.
en048 | SAME | en048 | 1.00 | The result was 24 scaffolds.
en049 | SAME | en049 | 1.00 | Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs.
en050 | SAME | en050 | 1.00 | The 768 records are repeated submissions, not independent maintenance cases.
en051 | SAME | en051 | 1.00 | We separately read the masked instructions for case-specific change requests and protected caller commitments.
en052 | SAME | en052 | 1.00 | An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape.
en053 | SAME | en053 | 1.00 | We inspected the text outside the submitted code, not the whole semantic context.
en054 | SAME | en054 | 1.00 | In a separate replication, the 192 saved Python rows reduced to twelve distinct code submissions; four contained a total of 46 comment tokens, and none had an AST-detected docstring.
en055 | SAME | en055 | 1.00 | These comments may convey implementation intent, but counting them does not establish a contract.
en056 | SAME | en056 | 1.00 | We did not perform the same comment-token audit for the other three languages.
en057 | SAME | en057 | 1.00 | We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace.
en058 | SAME | en058 | 1.00 | For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions.
en059 | SAME | en059 | 1.00 | These tests do not establish whether inherited methods remain available or whether callers were promised a behavior.
en060 | SAME | en060 | 1.00 | We read code as archive data and did not execute it.
en061 | SAME | en061 | 1.00 | For the catalog, we fixed the baseline, candidate patch, calls and permission to add a module.
en062 | SAME | en062 | 1.00 | Executing the code established outputs and exceptions for those calls.
en063 | SAME | en063 | 1.00 | The possible demands (technical reports alone, or technical reports and errata), the two scopes of the book-output obligation, and the rule that an acceptable patch must meet its demand and preserve protected behavior we
en064 | SAME | en064 | 1.00 | Table 2 therefore applies authored criteria to observed behavior; it does not report independent human decisions.
en065 | SAME | en065 | 1.00 | For partial disclosure, we retained only the candidate specifications compatible with known facts.
en066 | SAME | en066 | 1.00 | We did not attempt to enumerate obligations outside these four constructed cases.
en067 | SAME | en067 | 1.00 | · · · Pehlivan et al. chose violation scenarios and refined the generated examples.
en068 | SAME | en068 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en069 | SAME | en069 | 1.00 | The benchmark compares model classifications with the resulting labels.
en070 | SAME | en070 | 1.00 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en071 | SAME | en071 | 1.00 | No two strategies shared a template string.
en072 | SAME | en072 | 1.00 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en073 | SAME | en073 | 1.00 | An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: gpt-4o-mini differed from the other three models.
en074 | SAME | en074 | 1.00 | Holding model, strategy and language fixed left one scaffold shared across twelve programs.
en075 | SAME | en075 | 1.00 | No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST.
en076 | SAME | en076 | 1.00 | These checks do not establish semantic independence or source lineage.
en077 | SAME | en077 | 1.00 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en078 | SAME | en078 | 1.00 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en079 | SAME | en079 | 1.00 | If a new shape is needed, that branch is a place to look.
en080 | SAME | en080 | 1.00 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en081 | SAME | en081 | 1.00 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en082 | SAME | en082 | 1.00 | No submitted program matched a reference side under the reported textual normalizations, and the separate Python-only AST comparison also found no match.
en083 | SAME | en083 | 1.00 | Pair 37 establishes that a declaration was removed.
en084 | SAME | en084 | 1.00 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en085 | SAME | en085 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en086 | SAME | en086 | 1.00 | The prompt example is in JSONL line 13 (record ID 12).
en087 | SAME | en087 | 1.00 | Pair 37 is in a separate reference JSON file.
en088 | SAME | en088 | 1.00 | · · · Bräuer et al. (2018) examined the measurement of design principles with experts; Cabral et al. (2024) studied understanding and extension under a bundled SOLID treatment; Zhu et al. (2026) supplied repository chang
en089 | SAME | en089 | 1.00 | These evaluate different objects.
en090 | SAME | en090 | 1.00 | Our audit does not contest the benchmark's classification task.
en091 | SAME | en091 | 1.00 | It asks what else would be needed to use such a classification as a reason to reject a patch.
en092 | NEW | en159 | 0.11 | · · Empirical review studies narrow the claim further.
en093 | NEW | en088 | 0.12 | Widyasari et al. (2025) coded 793 Gerrit review comments and identified explanation categories including appeals to rules or principles.
en094 | NEW | en094 | 0.11 | This shows that principle-based explanations appear in review practice; it does not show that such principles caused an unjustified patch rejection.
en095 | NEW | en082 | 0.16 | Papotti et al. (2024) experimentally studied 72 computer-science master's students deciding whether to adopt security patches proposed by automatic program repair tools, and found that information about the purported too
en096 | NEW | en064 | 0.12 | Unlike our stipulated Table 2 judgments, those were observed human choices.
en097 | NEW | en049 | 0.16 | · Jin and Chen (2026) tested five language models' judgments of canonical and buggy implementations against natural-language specifications across three programming benchmarks.
en098 | NEW | en101 | 0.14 | They reported false rejection of correct code and risks from prompts that demand explanations or fixes.
en099 | NEW | en121 | 0.13 | We cannot claim to have discovered LLM over-rejection or to improve its error rate: our archive does not record independent patch-acceptance judgments by those models.
en100 | NEW | en095 | 0.17 | Ling, Zou, and Liu (2026) examined public agent-associated contributions and distinguished merges, issue closures, and requirement satisfaction.
en101 | NEW | en123 | 0.14 | Conditional acceptance is not first discovered by this paper either.
en102 | NEW | en101 | 0.16 | Our narrower addition is to hold a patch's execution fixed and make explicit which partially disclosed requirement and contract facts warrant a verdict and which warrant further inquiry .
en103 | SAME | en092 | 1.00 | · This is not a new problem in general.
en104 | SAME | en093 | 1.00 | Kane (2013) argues that evidence supporting an interpretation of test scores does not automatically justify using those scores for a particular decision.
en105 | SAME | en094 | 1.00 | His work does not test software reviews; it establishes the importance of justifying an assessment's use .
en106 | SAME | en095 | 1.00 | Zave and Jackson (1997) distinguish requirements, machine specifications and knowledge of the environment, including which actor controls an action.
en107 | SAME | en096 | 1.00 | Whether sorting belongs to a caller or a drawing function is an instance of that longstanding question.
en108 | SAME | en097 | 1.00 | Jones (1981) likewise developed conditions for compatible environmental reliance and program guarantees in parallel programs.
en109 | SAME | en098 | 1.00 | We do not claim these distinctions as our invention.
en110 | SAME | en099 | 1.00 | · · Barr et al.'s (2015) survey of the test-oracle problem makes a related point about our executable fixture.
en111 | SAME | en100 | 1.00 | Tests establish outputs for chosen inputs; they do not, without an independently grounded oracle, establish which outputs a real project has promised to preserve.
en112 | SAME | en101 | 1.00 | Thus the demands and contracts in Section 5 are explicit assumptions rather than requirements recovered from a repository.
en113 | SAME | en102 | 1.00 | We built a small catalog based on Meyer’s example.
en114 | SAME | en103 | 1.00 | The client in client.py displays each publication through the catalog function passed to it.
en115 | SAME | en104 | 1.00 | The patch adds reports.py to wrap that function.
en116 | SAME | en105 | 1.00 | The source of catalog.py and client.py stays identical.
en117 | SAME | en106 | 1.00 | The resulting catalog displays technical reports and still rejects errata.
en118 | SAME | en107 | 1.00 | For books it now prints BOOK where it used to print book .
en119 | SAME | en108 | 1.00 | Suppose the only new requirement is to handle technical reports.
en120 | SAME | en109 | 1.00 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en121 | SAME | en110 | 1.00 | If the book output is outside the contract, the same patch can be accepted.
en122 | SAME | en111 | 1.00 | Table 2 applies both contracts again when errata are also required.
en123 | SAME | en112 | 1.00 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en124 | SAME | en113 | 1.00 | Excluding the book prefix from our stipulated contract is not evidence that real users have no expectation about it; it only means this example does not impose that obligation.
en125 | SAME | en114 | 1.00 | Two requirements for accepting a fixed patch.
en126 | SAME | en115 | 1.00 | Learning that errata are required leaves the last two rows of Table 2.
en127 | SAME | en116 | 1.00 | Both reject the patch, so the book contract need not be settled first.
en128 | SAME | en117 | 1.00 | Learning that technical reports are the whole request leaves the first two rows.
en129 | SAME | en118 | 1.00 | One accepts and one rejects.
en130 | SAME | en119 | 1.00 | The next question is whether the original book output is protected.
en131 | SAME | en120 | 1.00 | The procedure applies only if the actual specification is among these four authored cases.
en132 | SAME | en121 | 1.00 | If disclosure rules out every row, an empty candidate set is a reason to question the evidence or the candidate set, not to infer acceptance or rejection.
en133 | SAME | en122 | 1.00 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en134 | SAME | en123 | 1.00 | The reviewer can give a conditional answer or defer judgment.
en135 | SAME | en124 | 1.00 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en136 | NEW | en040 | 0.12 | Minimum evidence for a decision.
en137 | NEW | en063 | 0.14 | Let (E) mean that errata must be supported, and (B) that the previous book prefix is protected.
en138 | NEW | en114 | 0.15 | Only for the four stipulated worlds, the fixed patch is acceptable exactly when (\\neg E\\land\\neg B).
en139 | NEW | en114 | 0.16 | Establishing acceptance requires both negative facts.
en140 | NEW | en118 | 0.11 | Either positive fact suffices to reject.
en141 | NEW | en152 | 0.17 | With both facts withheld, an accepting world ((E=0,B=0)) and a rejecting world ((E=1,B=0)) remain compatible, supplying explicit witnesses for deferral.
en142 | NEW | en119 | 0.31 | Once reports-only is known, asking whether book output is protected settles the remaining question.
en143 | NEW | en135 | 0.09 | From the completely unknown state, neither binary question by itself resolves every answer branch.
en144 | NEW | en057 | 0.12 | These are classical finite Boolean and version-space facts, not new inference rules.
en145 | NEW | en082 | 0.13 | A separate Python replay checked the four worlds, nine disclosure states, inclusion-minimal certificates, contradictory evidence, and pairs of opposite-verdict worlds for deferred states; its passed.
en146 | NEW | en064 | 0.16 | That verifies the bounded decision logic, not actual human decisions or complete source behavior.
en147 | NEW | en113 | 0.17 | Learning more about a fixed contract removes possible worlds; renegotiating that contract changes the legitimate obligation.
en148 | NEW | en171 | 0.10 | The two transitions must not be conflated.
en149 | SAME | en125 | 1.00 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en150 | SAME | en126 | 1.00 | It adds one module, handles technical reports and errata, and keeps the original book output.
en151 | SAME | en127 | 1.00 | A rejection in Table 2 need not end the search for a patch within that boundary.
en152 | SAME | en128 | 1.00 | The contribution is not a new logical rule: it is a concrete account of why knowing that errata are required settles this decision, whereas a reports-only demand leaves the book-output commitment to be checked.
en153 | SAME | en129 | 1.00 | Applying it to a real review would require finding that commitment in a request, API documentation, tests or caller records.
en154 | SAME | en130 | 1.00 | · Deciding whether to accept a completed patch differs from choosing an architecture for future edits.
en155 | SAME | en131 | 1.00 | We retain one observation relevant to acceptance.
en156 | SAME | en132 | 1.00 | In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected bracketed=True .
en157 | SAME | en133 | 1.00 | A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.
en158 | SAME | en134 | 1.00 | The presence of a feature is different from its availability along a required route .
en159 | NEW | en155 | 0.12 | Moreover, equal HTTP responses do not entail equivalence in every programming context.
en160 | NEW | en055 | 0.12 | In a separate P44 original-Go negative control, wrapping an implementation in http.HandlerFunc removed exposure of its additional interface method.
en161 | NEW | en043 | 0.14 | That result concerns neither the catalog patch nor a newly discovered Go law; standard interface semantics explain it.
en162 | SAME | en135 | 1.00 | The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in Paper B 통합 원고 12 · 한·영 문장 교정 and its .
en163 | SAME | en136 | 1.00 | Drawing a square first establishes what a routine does, not whether it must be edited.
en164 | SAME | en137 | 1.00 | That depends on whether sorting belongs to the routine's obligations.
en165 | SAME | en138 | 1.00 | In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required.
en166 | SAME | en139 | 1.00 | We did not observe a real OCP label being misused to reject a patch.
en167 | SAME | en140 | 1.00 | We asked what additional grounds a design-principle assessment needs before it can justify an engineering decision .
en168 | NEW | en142 | 0.16 | A practical review should first ask not only whether the patch implements a feature but where the request or an authorized agreement requires that feature to be reachable.
en169 | NEW | en142 | 0.17 | The reviewer should then locate the source of each protected old-client obligation in requests, API documentation, tests and actual call paths, without automatically treating every observed response as a promise.
en170 | NEW | en013 | 0.13 | If those sources leave different legitimate contracts possible, asking who can settle the obligation is more defensible than turning an OCP label into a categorical rejection.
en171 | NEW | en138 | 0.12 | Conversely, a demonstrated failure to meet an already binding new demand may reject the fixed patch before every other old-client promise is resolved.
en172 | NEW | en143 | 0.17 | This sequence is a recommendation derived from our authored example, not evidence that it reduces actual review costs in an organization.
en173 | SAME | en141 | 1.00 | Keeping the specifications compatible with known facts and checking their verdicts is elementary logic.
en174 | SAME | en142 | 1.00 | The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository.
en175 | SAME | en143 | 1.00 | Our evidence is confined to one benchmark archive and authored executable examples.
en176 | SAME | en144 | 1.00 | We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.
en177 | SAME | en145 | 1.00 | The audits in Sections 3–4 read the archived JSON and JSONL as data.
en178 | SAME | en146 | 1.00 | A separate script reproduced sixteen JSONL files, 768 rows, 48 distinct submissions, 24 scaffolds and 64 fixed model–strategy–language groups, and counted Python comments in four of twelve unique submissions.
en179 | SAME | en147 | 1.00 | Section 5 and the call-path check in Section 6 use examples written for this study.
en180 | EDIT | en148 | 0.55 | The shape-layout experiment and Figure 1 remain preserved in manuscript 12; manuscript 17 does not reframe them as a new measured maintenance-cost trial.
en181 | SAME | en149 | 1.00 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en182 | SAME | en150 | 1.00 | The table below gives the nine verdicts for Section 5.
en183 | SAME | en151 | 1.00 | Both values of a withheld field remain possible.
en184 | SAME | en152 | 1.00 | Defer means that the compatible rows include both acceptance and rejection. - Meyer, B.
en185 | SAME | en153 | 1.00 | Object-Oriented Software Construction (1st ed.), pp.
en186 | SAME | en154 | 1.00 | The Open–Closed Principle . . - Jones, C.
en187 | SAME | en155 | 1.00 | Development Methods for Computer Programs Including a Notion of Interference .
en188 | SAME | en156 | 1.00 | Oxford University Computing Laboratory, PRG-25.
en189 | SAME | en157 | 1.00 | · . - Pehlivan, F., Ergüzen, A.
en190 | SAME | en158 | 1.00 | M., Lami, M., & Koyuncu, A.
en191 | SAME | en159 | 1.00 | An Empirical Study on Prompting LLMs to Detect Design Principle Violations .
en192 | SAME | en160 | 1.00 | ASE 2025 NIER. . - Bräuer et al.
en193 | SAME | en161 | 1.00 | Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research . . - Cabral et al.
en194 | SAME | en162 | 1.00 | Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding . . - Zhu, H., Zhang, Q., Wang, J., Yang, Z., & Qiu, Y.
en195 | SAME | en163 | 1.00 | Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits . . - Kane, M.
en196 | SAME | en164 | 1.00 | Validating the Interpretations and Uses of Test Scores .
en197 | SAME | en165 | 1.00 | Journal of Educational Measurement , 50(1), 1–73.
en198 | SAME | en166 | 1.00 | · . - Zave, P., & Jackson, M.
en199 | SAME | en167 | 1.00 | Four Dark Corners of Requirements Engineering .
en200 | SAME | en168 | 1.00 | ACM Transactions on Software Engineering and Methodology , 6(1), 1–30.
en201 | SAME | en169 | 1.00 | T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S.
en202 | SAME | en170 | 1.00 | The Oracle Problem in Software Testing: A Survey .
en203 | SAME | en171 | 1.00 | IEEE Transactions on Software Engineering .
en204 | NEW | en003 | 0.04 | · . - Widyasari, R., Zhang, T., Bouraffa, A., Maalej, W., & Lo, D.
en205 | NEW | en159 | 0.26 | Explaining Explanations: An Empirical Study of Explanations in Code Reviews .
en206 | EDIT | en168 | 0.72 | ACM Transactions on Software Engineering and Methodology , 34(6), Article 177.
en207 | NEW | en169 | 0.09 | · . - Papotti, A., Paramitha, R., & Massacci, F.
en208 | NEW | en082 | 0.13 | On the acceptance by code reviewers of candidate security patches suggested by Automated Program Repair tools .
en209 | NEW | en171 | 0.31 | Empirical Software Engineering , 29, Article 132.
en210 | NEW | en003 | 0.04 | · . - Jin, H., & Chen, H.
en211 | NEW | en039 | 0.11 | Are LLMs Reliable Code Reviewers?
en212 | NEW | en101 | 0.16 | Systematic Overcorrection in Requirement Conformance Judgement .
en213 | NEW | en139 | 0.03 | · . - Ling, M., Zou, J., & Liu, X.
en214 | NEW | en114 | 0.17 | Negotiating Completion in Agentic Software Work: Acceptance Boundaries and Deferred Requirements .
en215 | SAME | en172 | 1.00 | 이 목록은 인용된 주요 자료를 확인할 수 있게 모은 집필용 서지이며, 서지형식·인용 위치·전수 대조를 마친 제출용 참고문헌은 아직 아니다.
en216 | SAME | en173 | 1.00 | / These are verified reading anchors, not yet a fully formatted submission bibliography.
Summary en: SAME 172, EDIT 2, NEW 42

## v18 · [Notion](https://app.notion.com/p/41fef561cf928115a014dcd55136fc31)
### ko (171 sentences)
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
ko033 | SAME | ko033 | 1.00 | · · 우리는 서로 다른 두 자료를 사용했다.
ko034 | SAME | ko034 | 1.00 | 벤치마크에서는 분류를 요구받은 모델에게 실제로 어떤 입력이 주어졌는지 조사했다.
ko035 | SAME | ko035 | 1.00 | 도서관 예제에서는 패치 한 개를 고정하고, 적용할 요구와 보호할 계약을 바꿔 가며 실행 결과와 승인 기준을 대조했다.
ko036 | SAME | ko036 | 1.00 | 벤치마크의 저장 코드와 도서관 코드는 별개이고, 어느 쪽에도 실제 검토자의 승인·거절 판단은 포함되지 않는다.
ko037 | SAME | ko037 | 1.00 | OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다.
ko038 | SAME | ko038 | 1.00 | 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다.
ko039 | SAME | ko039 | 1.00 | 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다.
ko040 | SAME | ko040 | 1.00 | 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다.
ko041 | SAME | ko041 | 1.00 | 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다.
ko042 | SAME | ko042 | 1.00 | 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.
ko043 | SAME | ko043 | 1.00 | 지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다.
ko044 | SAME | ko044 | 1.00 | 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다.
ko045 | SAME | ko045 | 1.00 | 이 판독은 제출 코드를 가린 지시문에 관한 것이다.
ko046 | SAME | ko046 | 1.00 | 독립 감사에서 Python 저장 행 192개를 이루는 고유 코드 12개를 검사하자 4개에서 주석 토큰 46개를 발견했고, docstring을 포함한 코드는 없었다.
ko047 | SAME | ko047 | 1.00 | 주석이 기능의 의도를 암시할 수 있으므로, 지시문에 개별 요구가 없다는 사실을 코드 전체에 명세 단서가 없다는 주장으로 확대하지 않았다.
ko048 | SAME | ko048 | 1.00 | 다른 세 언어의 주석은 같은 방법으로 계수하지 않았다.
ko049 | SAME | ko049 | 1.00 | 저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다.
ko050 | SAME | ko050 | 1.00 | Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다.
ko051 | SAME | ko051 | 1.00 | 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다.
ko052 | SAME | ko052 | 1.00 | 압축 파일 안의 코드 자체는 실행하지 않았다.
ko053 | SAME | ko053 | 1.00 | 도서관 예제에서는 원본 소스와 수정안, 호출 입력, 새 모듈을 추가할 수 있다는 편집 범위를 고정했다.
ko054 | SAME | ko054 | 1.00 | 코드 실행으로 확인한 것은 구체적인 입력에서 나온 출력과 예외다.
ko055 | SAME | ko055 | 1.00 | 반면 기술보고서·정오표 중 무엇을 요구하는지, 책 출력의 접두어가 보호 대상인지, 새 요구를 충족하면서 보호된 기존 동작을 보존해야 승인한다 는 기준은 모두 연구자가 정했다.
ko056 | SAME | ko056 | 1.00 | 따라서 §5의 표는 독립 심사위원의 판정이 아니라 우리가 지정한 기준을 실행 관찰에 적용한 결과다.
ko057 | SAME | ko057 | 1.00 | 일부 전제만 공개한 경우에는 두 요구와 두 계약으로 이루어진 후보 명세 중 공개된 사실과 맞는 것만 남겼다.
ko058 | SAME | ko058 | 1.00 | 이 후보군 밖의 실제 요구나 계약까지 조사했다고 가정하지 않는다.
ko059 | SAME | ko059 | 1.00 | · · · · Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21) Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko060 | SAME | ko060 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko061 | SAME | ko061 | 1.00 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko062 | SAME | ko062 | 1.00 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko063 | SAME | ko063 | 1.00 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko064 | SAME | ko064 | 1.00 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko065 | SAME | ko065 | 1.00 | 추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. gpt-4o-mini 와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다.
ko066 | SAME | ko066 | 1.00 | 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다.
ko067 | SAME | ko067 | 1.00 | 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.
ko068 | SAME | ko068 | 1.00 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko069 | SAME | ko069 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko070 | SAME | ko070 | 1.00 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko071 | SAME | ko071 | 1.00 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko072 | SAME | ko072 | 1.00 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko073 | SAME | ko073 | 1.00 | 저장 코드와 참조 쌍은 앞에서 명시한 문자열 정규화 기준에서 일치하지 않았으며, Python 코드에 한한 AST 비교에서도 일치 사례가 없었다.
ko074 | SAME | ko074 | 1.00 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko075 | SAME | ko075 | 1.00 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko076 | SAME | ko076 | 1.00 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko077 | SAME | ko077 | 1.00 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko078 | SAME | ko078 | 1.00 | · · · Bräuer 등(2018)은 설계 원칙을 어떻게 측정할지 전문가에게 물었고, Cabral 등(2024)은 SOLID를 적용한 코드를 이해하고 확장하는 경험을 조사했다.
ko079 | SAME | ko079 | 1.00 | Zhu 등(2026)은 구체적인 저장소 변경 과제에 기능 및 구조 검사를 결합했다.
ko080 | SAME | ko080 | 1.00 | 우리의 벤치마크 감사도 분류 성능을 부정하려는 것이 아니다.
ko081 | SAME | ko081 | 1.00 | 분류에 성공했다는 증거를 수정안 거절의 증거로 옮길 때 무엇이 더 필요한지를 묻는다.
ko082 | SAME | ko082 | 1.00 | · · 실제 리뷰 연구는 이 논문의 주장 범위를 더 엄격하게 제한한다.
ko083 | SAME | ko083 | 1.00 | Widyasari 등(2025)은 Gerrit 코드 리뷰 댓글 793건을 분석하고 규칙이나 원칙을 근거로 드는 설명 유형을 확인했다.
ko084 | SAME | ko084 | 1.00 | 이는 원칙에 의거한 설명이 리뷰에 존재한다는 증거지만, 원칙이 잘못 적용돼 특정 수정안이 거절됐다는 증거는 아니다.
ko085 | SAME | ko085 | 1.00 | Papotti 등(2024)은 컴퓨터과학 석사과정 학생 72명을 대상으로 보안 자동 수리 패치의 채택 여부를 실험했다.
ko086 | SAME | ko086 | 1.00 | 제안 도구의 전문성을 알리는 정보에 따라 판단이 바뀌는 현상을 관찰했지만, 원칙 위반 라벨을 대상으로 한 연구는 아니다.
ko087 | SAME | ko087 | 1.00 | 두 논문의 실제 사람에 대한 관측은 우리가 구성한 표 2의 승인 기준과 다르다.
ko088 | SAME | ko088 | 1.00 | · Jin과 Chen(2026)은 정답 코드와 결함 코드에 대한 다섯 언어 모델의 요구 적합성 판단을 세 프로그래밍 벤치마크에서 실험하고, 맞는 코드를 잘못 거절하는 현상과 설명·수정 제안을 요구하는 프롬프트의 위험을 보고했다.
ko089 | SAME | ko089 | 1.00 | 따라서 LLM의 과잉 거절을 처음 지적했다고 주장할 수 없다.
ko090 | SAME | ko090 | 1.00 | Ling·Zou·Liu(2026)는 공개 GitHub 변경 사례의 질적 연구에서 병합, 이슈 종료, 요구 충족이 서로 다른 결과일 수 있음을 논증했다.
ko091 | SAME | ko091 | 1.00 | 수용 경계가 조건부라는 발견도 우리의 최초성이 아니다.
ko092 | SAME | ko092 | 1.00 | 우리 사례는 실행 결과가 고정된 패치에서 현재 공개된 요구·계약이 정당화하는 판정과 추가 질문을 정확하게 분리하는 재현 가능한 실례 다.
ko093 | SAME | ko093 | 1.00 | · 그 질문 자체에도 중요한 선행연구가 있다.
ko094 | SAME | ko094 | 1.00 | Kane(2013)은 검사 점수의 해석을 뒷받침하는 증거가 그 점수를 특정 결정에 사용하는 일까지 정당화하지는 않는다고 논했다.
ko095 | SAME | ko095 | 1.00 | 이는 소프트웨어 리뷰를 실험한 결과가 아니라, 평가 결과의 사용 을 따로 정당화해야 한다는 일반적인 논증이다.
ko096 | SAME | ko096 | 1.00 | Zave와 Jackson(1997)은 요구사항, 기계 명세, 환경에 관한 지식이 어떻게 연결되는지 설명하면서 행위의 통제 주체를 구별했다.
ko097 | SAME | ko097 | 1.00 | 원을 앞에 정렬할 책임이 호출자에게 있는지 함수에 있는지부터 따져야 한다는 우리의 질문도 이러한 오래된 문제의 한 사례다.
ko098 | SAME | ko098 | 1.00 | 존스(1981) 역시 병렬 프로그램에서 환경 의존 조건과 프로그램 보장 조건의 양립을 다뤘다.
ko099 | SAME | ko099 | 1.00 | · · Barr 등(2015)이 정리한 테스트 오라클 문제는 코드 실행과 올바름 판정 사이에도 근거가 필요함을 상기시킨다.
ko100 | SAME | ko100 | 1.00 | §5의 시험은 지정된 호출의 동작을 확인하지만, 그 동작을 보존하겠다는 실제 프로젝트의 약속을 입증하지는 않는다.
ko101 | SAME | ko101 | 1.00 | 따라서 다음 절의 요구·계약은 발견한 사실이 아니라 명시적으로 정한 전제다.
ko102 | NEW | ko141 | 0.08 | 위반 범주를 맞혔다는 사실은 코드에 특정 구조가 있다는 평가를 뒷받침한다.
ko103 | NEW | ko075 | 0.12 | 그러나 수정안을 거절하려면 (1) 누구에게서 나온 새 요구인지, (2) 기존 호출자에게 계속 보장하기로 한 동작이 무엇인지, (3) 그 동작과 새 기능을 어느 호출 경로로 제공해야 하는지까지 알아야 한다.
ko104 | NEW | ko149 | 0.06 | 이 가운데 일부는 소스에 표시될 수 있지만, 관측한 구현이 곧 승인된 계약이라는 뜻은 아니다.
ko105 | NEW | ko114 | 0.12 | 예컨대 같은 출력 변경을 보고도 책 출력이 보호 대상일 때와 아닐 때는 서로 다른 판정이 가능하다.
ko106 | NEW | ko011 | 0.04 | 분류 라벨을 고정한 채 판정이 달라지는 반례는 §5에서 실행한 동일 패치의 네 명세에 한정된다.
ko107 | NEW | ko058 | 0.07 | 이를 통해 분류 점수 자체를 부정하거나 실제 리뷰어가 라벨 때문에 패치를 거절했다고 주장하지 않는다.
ko108 | SAME | ko102 | 1.00 | 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko109 | SAME | ko103 | 1.00 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko110 | SAME | ko104 | 1.00 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko111 | SAME | ko105 | 1.00 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko112 | SAME | ko106 | 1.00 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko113 | SAME | ko107 | 1.00 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko114 | SAME | ko108 | 1.00 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko115 | SAME | ko109 | 1.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko116 | SAME | ko110 | 1.00 | 책 접두어가 보호 대상이 아니라는 가정은 실제 이용자가 그 출력을 기대하지 않는다는 관찰이 아니다.
ko117 | SAME | ko111 | 1.00 | 단지 이 비교에서 보존 의무로 정하지 않았다는 뜻이다.
ko118 | SAME | ko112 | 1.00 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko119 | SAME | ko113 | 1.00 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko120 | SAME | ko114 | 1.00 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko121 | SAME | ko115 | 1.00 | 이 절차는 실제 명세가 표의 네 경우 중 하나라는 조건 아래서만 성립한다.
ko122 | SAME | ko116 | 1.00 | 공개된 사실과 맞는 행이 하나도 없다면 승인이나 거절을 내릴 것이 아니라 자료 또는 후보군이 잘못됐는지 확인해야 한다.
ko123 | SAME | ko117 | 1.00 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko124 | SAME | ko118 | 1.00 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko125 | SAME | ko119 | 1.00 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko126 | NEW | ko120 | 0.13 | 정오표 지원이 필수인지 여부를 $E$, 기존 책 출력 접두어를 보호하는지 여부를 $B$라고 두자.
ko127 | NEW | ko120 | 0.22 | 연구자가 정한 네 명세에 한정하면, 이 고정 패치의 승인 조건은 $A(E,B)=\neg E\land\neg B$다.
ko128 | NEW | ko008 | 0.05 | 따라서 승인에 필요한 최소 증거는 $\{\neg E,\neg B\}$이며, 거절을 확정하는 최소 증거는 $\{E\}$ 또는 $\{B\}$다.
ko129 | NEW | ko122 | 0.23 | 두 조건을 모두 알 수 없다면, 승인 명세 $(E=0,B=0)$와 거절 명세 $(E=1,B=0)$가 양립하므로 판정을 보류한다.
ko130 | NEW | ko123 | 0.14 | 기술보고서만 요구한다는 사실, 즉 $\neg E$가 확인되면 $B$를 물어 어느 쪽인지 결정할 수 있다.
ko131 | NEW | ko124 | 0.09 | 반면 두 조건이 전부 미공개일 때는 하나의 예·아니오 질문만으로 모든 답변에 대해 판정을 확정하지 못한다.
ko132 | SAME | ko125 | 1.00 | 이것은 새로운 논리 규칙이 아니라 고전적인 유한 정보 집합 판정이다.
ko133 | SAME | ko126 | 1.00 | 별도 Python 코드는 네 명세의 공개 상태 아홉 가지, 최소 승인·거절 증거, 보류 상태의 대립 명세, 모순된 사실의 처리까지 검사했고 가 통과했다.
ko134 | SAME | ko127 | 1.00 | 이 테스트가 실제 검토자의 판단이나 원본 도서관 프로그램의 전체 동작을 재검증한 것은 아니다.
ko135 | SAME | ko128 | 1.00 | 또한 고정된 계약에 관한 사실을 알게 되는 것 과 계약 자체를 변경하는 것 을 구별해야 한다.
ko136 | SAME | ko129 | 1.00 | 앞의 경우에는 가능한 명세의 집합이 줄지만, 뒤의 경우에는 승인 조건 자체가 달라질 수 있다.
ko137 | SAME | ko130 | 1.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko138 | SAME | ko131 | 1.00 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko139 | SAME | ko132 | 1.00 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko140 | SAME | ko133 | 1.00 | 이 비교에서 얻은 것은 새로운 논리 규칙이 아니다.
ko141 | SAME | ko134 | 1.00 | 한 사실만 알아도 거절이 확정되는 경우와, 책 출력 약속을 물어야 하는 경우를 구체적인 호출 결과로 구분한 것이다.
ko142 | SAME | ko135 | 1.00 | 실제 리뷰에 적용하려면 요구서와 API 문서, 테스트 및 호출 기록에서 그 약속의 근거를 따로 찾아야 한다.
ko143 | SAME | ko136 | 1.00 | · 완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다.
ko144 | SAME | ko137 | 1.00 | 여기서는 앞의 질문에 해당하는 관찰만 남긴다.
ko145 | SAME | ko138 | 1.00 | 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 bracketed=True 를 넘기면 인자를 거절했다.
ko146 | SAME | ko139 | 1.00 | 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다.
ko147 | SAME | ko140 | 1.00 | 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.
ko148 | SAME | ko141 | 1.00 | 새 기능이 있다는 사실과 요구된 호출 경로에서 쓸 수 있다는 사실 은 다르다.
ko149 | NEW | ko146 | 0.07 | 보호해야 할 기존 진입점이 무엇인지 확인하지 않으면, 같은 옵션을 새 함수에서 제공했다는 사실만으로 수정안의 적합성을 판정할 수 없다.
ko150 | SAME | ko145 | 1.00 | 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 Paper B 통합 원고 12 · 한·영 문장 교정 및 에 원형 그대로 보존했다.
ko151 | SAME | ko146 | 1.00 | 마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다.
ko152 | SAME | ko147 | 1.00 | 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다.
ko153 | SAME | ko148 | 1.00 | 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다.
ko154 | SAME | ko149 | 1.00 | 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다.
ko155 | SAME | ko150 | 1.00 | 원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가 가 이 논문에서 다룬 질문이다.
ko156 | SAME | ko151 | 1.00 | 실제 검토에서 먼저 확인할 것은 수정안의 새 기능만이 아니라, 요구한 사람이나 합의된 문서가 그 기능을 어느 진입점에서 제공하도록 정했는지다.
ko157 | SAME | ko152 | 1.00 | 그다음 기존 호출자가 의존하는 동작 중 무엇이 보호 대상인지 요구서·API 문서·테스트·호출 코드에서 근거를 찾아야 한다.
ko158 | SAME | ko153 | 1.00 | 이 근거가 둘 이상의 가능한 계약을 남긴다면, 원칙 위반이라는 이름으로 결론을 확정하기보다 계약의 출처와 범위를 묻는 편이 정확하다.
ko159 | SAME | ko154 | 1.00 | 반대로 새로운 요구를 충족하지 못한다는 사실이 이미 확정됐다면, 어떤 기존 계약이 추가로 보호되는지 모두 조사하기 전에 해당 수정안을 거절할 수도 있다.
ko160 | SAME | ko155 | 1.00 | 이러한 질문의 순서는 이 논문의 구성 사례에서 나온 실무적 제안이지, 실제 개발 조직의 효율이 개선됐다는 관측 결과는 아니다.
ko161 | SAME | ko156 | 1.00 | 공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다.
ko162 | SAME | ko157 | 1.00 | 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다.
ko163 | SAME | ko158 | 1.00 | 이 연구는 한 벤치마크의 저장 입력과 연구자가 구성한 실행 예제만을 다뤘다.
ko164 | SAME | ko159 | 1.00 | 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.
ko165 | SAME | ko160 | 1.00 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko166 | SAME | ko161 | 1.00 | 독립 감사 스크립트는 같은 ZIP을 실행 코드가 아닌 자료로 읽어 16개 JSONL 파일, 768행, 48개 고유 코드, 24개 틀, 64개 세부 집단을 재계산했고, Python 고유 코드 12개 중 주석이 있는 4개를 확인했다.
ko167 | SAME | ko162 | 1.00 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko168 | SAME | ko163 | 1.00 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko169 | EDIT | ko164 | 0.87 | 12판에 있던 그림 1과 파일 배치 실험은 18판 본문에 싣지 않았으며, 원본 그림과 실행 기록을 12판에 보존했다.
ko170 | SAME | ko165 | 1.00 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko171 | SAME | ko166 | 1.00 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
Summary ko: SAME 157, EDIT 1, NEW 13

### en (220 sentences)
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
en040 | SAME | en040 | 1.00 | · · We used two distinct sources of evidence.
en041 | SAME | en041 | 1.00 | We audited the saved benchmark inputs to determine what a classifier was actually asked to judge.
en042 | SAME | en042 | 1.00 | Separately, we fixed one catalog patch and varied the demands and protected caller commitments against which its execution was assessed.
en043 | SAME | en043 | 1.00 | The benchmark submissions are not instances of the catalog patch, and neither source records decisions by real reviewers.
en044 | SAME | en044 | 1.00 | The OCP reference material contains 48 before-and-after code pairs.
en045 | SAME | en045 | 1.00 | Sixteen saved JSONL files each contain 48 records, yielding 768 rows.
en046 | SAME | en046 | 1.00 | Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times.
en047 | SAME | en047 | 1.00 | We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality.
en048 | SAME | en048 | 1.00 | The result was 24 scaffolds.
en049 | SAME | en049 | 1.00 | Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs.
en050 | SAME | en050 | 1.00 | The 768 records are repeated submissions, not independent maintenance cases.
en051 | SAME | en051 | 1.00 | We separately read the masked instructions for case-specific change requests and protected caller commitments.
en052 | SAME | en052 | 1.00 | An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape.
en053 | SAME | en053 | 1.00 | We inspected the text outside the submitted code, not the whole semantic context.
en054 | SAME | en054 | 1.00 | In a separate replication, the 192 saved Python rows reduced to twelve distinct code submissions; four contained a total of 46 comment tokens, and none had an AST-detected docstring.
en055 | SAME | en055 | 1.00 | These comments may convey implementation intent, but counting them does not establish a contract.
en056 | SAME | en056 | 1.00 | We did not perform the same comment-token audit for the other three languages.
en057 | SAME | en057 | 1.00 | We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace.
en058 | SAME | en058 | 1.00 | For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions.
en059 | SAME | en059 | 1.00 | These tests do not establish whether inherited methods remain available or whether callers were promised a behavior.
en060 | SAME | en060 | 1.00 | We read code as archive data and did not execute it.
en061 | SAME | en061 | 1.00 | For the catalog, we fixed the baseline, candidate patch, calls and permission to add a module.
en062 | SAME | en062 | 1.00 | Executing the code established outputs and exceptions for those calls.
en063 | SAME | en063 | 1.00 | The possible demands (technical reports alone, or technical reports and errata), the two scopes of the book-output obligation, and the rule that an acceptable patch must meet its demand and preserve protected behavior we
en064 | SAME | en064 | 1.00 | Table 2 therefore applies authored criteria to observed behavior; it does not report independent human decisions.
en065 | SAME | en065 | 1.00 | For partial disclosure, we retained only the candidate specifications compatible with known facts.
en066 | SAME | en066 | 1.00 | We did not attempt to enumerate obligations outside these four constructed cases.
en067 | SAME | en067 | 1.00 | · · · Pehlivan et al. chose violation scenarios and refined the generated examples.
en068 | SAME | en068 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en069 | SAME | en069 | 1.00 | The benchmark compares model classifications with the resulting labels.
en070 | SAME | en070 | 1.00 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en071 | SAME | en071 | 1.00 | No two strategies shared a template string.
en072 | SAME | en072 | 1.00 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en073 | SAME | en073 | 1.00 | An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: gpt-4o-mini differed from the other three models.
en074 | SAME | en074 | 1.00 | Holding model, strategy and language fixed left one scaffold shared across twelve programs.
en075 | SAME | en075 | 1.00 | No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST.
en076 | SAME | en076 | 1.00 | These checks do not establish semantic independence or source lineage.
en077 | SAME | en077 | 1.00 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en078 | SAME | en078 | 1.00 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en079 | SAME | en079 | 1.00 | If a new shape is needed, that branch is a place to look.
en080 | SAME | en080 | 1.00 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en081 | SAME | en081 | 1.00 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en082 | SAME | en082 | 1.00 | No submitted program matched a reference side under the reported textual normalizations, and the separate Python-only AST comparison also found no match.
en083 | SAME | en083 | 1.00 | Pair 37 establishes that a declaration was removed.
en084 | SAME | en084 | 1.00 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en085 | SAME | en085 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en086 | SAME | en086 | 1.00 | The prompt example is in JSONL line 13 (record ID 12).
en087 | SAME | en087 | 1.00 | Pair 37 is in a separate reference JSON file.
en088 | SAME | en088 | 1.00 | · · · Bräuer et al. (2018) examined the measurement of design principles with experts; Cabral et al. (2024) studied understanding and extension under a bundled SOLID treatment; Zhu et al. (2026) supplied repository chang
en089 | SAME | en089 | 1.00 | These evaluate different objects.
en090 | SAME | en090 | 1.00 | Our audit does not contest the benchmark's classification task.
en091 | SAME | en091 | 1.00 | It asks what else would be needed to use such a classification as a reason to reject a patch.
en092 | SAME | en092 | 1.00 | · · Empirical review studies narrow the claim further.
en093 | SAME | en093 | 1.00 | Widyasari et al. (2025) coded 793 Gerrit review comments and identified explanation categories including appeals to rules or principles.
en094 | SAME | en094 | 1.00 | This shows that principle-based explanations appear in review practice; it does not show that such principles caused an unjustified patch rejection.
en095 | SAME | en095 | 1.00 | Papotti et al. (2024) experimentally studied 72 computer-science master's students deciding whether to adopt security patches proposed by automatic program repair tools, and found that information about the purported too
en096 | SAME | en096 | 1.00 | Unlike our stipulated Table 2 judgments, those were observed human choices.
en097 | SAME | en097 | 1.00 | · Jin and Chen (2026) tested five language models' judgments of canonical and buggy implementations against natural-language specifications across three programming benchmarks.
en098 | SAME | en098 | 1.00 | They reported false rejection of correct code and risks from prompts that demand explanations or fixes.
en099 | SAME | en099 | 1.00 | We cannot claim to have discovered LLM over-rejection or to improve its error rate: our archive does not record independent patch-acceptance judgments by those models.
en100 | SAME | en100 | 1.00 | Ling, Zou, and Liu (2026) examined public agent-associated contributions and distinguished merges, issue closures, and requirement satisfaction.
en101 | SAME | en101 | 1.00 | Conditional acceptance is not first discovered by this paper either.
en102 | SAME | en102 | 1.00 | Our narrower addition is to hold a patch's execution fixed and make explicit which partially disclosed requirement and contract facts warrant a verdict and which warrant further inquiry .
en103 | SAME | en103 | 1.00 | · This is not a new problem in general.
en104 | SAME | en104 | 1.00 | Kane (2013) argues that evidence supporting an interpretation of test scores does not automatically justify using those scores for a particular decision.
en105 | SAME | en105 | 1.00 | His work does not test software reviews; it establishes the importance of justifying an assessment's use .
en106 | SAME | en106 | 1.00 | Zave and Jackson (1997) distinguish requirements, machine specifications and knowledge of the environment, including which actor controls an action.
en107 | SAME | en107 | 1.00 | Whether sorting belongs to a caller or a drawing function is an instance of that longstanding question.
en108 | SAME | en108 | 1.00 | Jones (1981) likewise developed conditions for compatible environmental reliance and program guarantees in parallel programs.
en109 | SAME | en109 | 1.00 | We do not claim these distinctions as our invention.
en110 | SAME | en110 | 1.00 | · · Barr et al.'s (2015) survey of the test-oracle problem makes a related point about our executable fixture.
en111 | SAME | en111 | 1.00 | Tests establish outputs for chosen inputs; they do not, without an independently grounded oracle, establish which outputs a real project has promised to preserve.
en112 | SAME | en112 | 1.00 | Thus the demands and contracts in Section 5 are explicit assumptions rather than requirements recovered from a repository.
en113 | NEW | en091 | 0.22 | From a classification to a patch disposition.
en114 | NEW | en191 | 0.22 | Correctly naming a design-principle violation supports a judgment about a structural feature of code.
en115 | NEW | en013 | 0.18 | Rejecting a specific patch requires different grounds: (i) the source and scope of the new request, (ii) the behavior the project committed to existing callers, and (iii) the call path through which the request and those
en116 | NEW | en169 | 0.15 | Some clues may reside in source, but observed behavior is not automatically an authorized compatibility promise.
en117 | NEW | en121 | 0.25 | The same change in book output can be unacceptable under one declared contract and acceptable under another.
en118 | NEW | en149 | 0.16 | Section 5 supplies a fixed-patch, four-specification witness to that gap.
en119 | NEW | en090 | 0.27 | It does not disprove the benchmark's classification scores or establish that a real reviewer rejected a patch because of an OCP label.
en120 | SAME | en113 | 1.00 | We built a small catalog based on Meyer’s example.
en121 | SAME | en114 | 1.00 | The client in client.py displays each publication through the catalog function passed to it.
en122 | SAME | en115 | 1.00 | The patch adds reports.py to wrap that function.
en123 | SAME | en116 | 1.00 | The source of catalog.py and client.py stays identical.
en124 | SAME | en117 | 1.00 | The resulting catalog displays technical reports and still rejects errata.
en125 | SAME | en118 | 1.00 | For books it now prints BOOK where it used to print book .
en126 | SAME | en119 | 1.00 | Suppose the only new requirement is to handle technical reports.
en127 | SAME | en120 | 1.00 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en128 | SAME | en121 | 1.00 | If the book output is outside the contract, the same patch can be accepted.
en129 | SAME | en122 | 1.00 | Table 2 applies both contracts again when errata are also required.
en130 | SAME | en123 | 1.00 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en131 | SAME | en124 | 1.00 | Excluding the book prefix from our stipulated contract is not evidence that real users have no expectation about it; it only means this example does not impose that obligation.
en132 | SAME | en125 | 1.00 | Two requirements for accepting a fixed patch.
en133 | SAME | en126 | 1.00 | Learning that errata are required leaves the last two rows of Table 2.
en134 | SAME | en127 | 1.00 | Both reject the patch, so the book contract need not be settled first.
en135 | SAME | en128 | 1.00 | Learning that technical reports are the whole request leaves the first two rows.
en136 | SAME | en129 | 1.00 | One accepts and one rejects.
en137 | SAME | en130 | 1.00 | The next question is whether the original book output is protected.
en138 | SAME | en131 | 1.00 | The procedure applies only if the actual specification is among these four authored cases.
en139 | SAME | en132 | 1.00 | If disclosure rules out every row, an empty candidate set is a reason to question the evidence or the candidate set, not to infer acceptance or rejection.
en140 | SAME | en133 | 1.00 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en141 | SAME | en134 | 1.00 | The reviewer can give a conditional answer or defer judgment.
en142 | SAME | en135 | 1.00 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en143 | SAME | en136 | 1.00 | Minimum evidence for a decision.
en144 | EDIT | en137 | 0.59 | Let $E$ indicate that errata support is required and $B$ that the previous book prefix is protected.
en145 | NEW | en138 | 0.28 | Within the four stipulated specifications, the acceptance predicate is $A(E,B)=\neg E\land\neg B$.
en146 | NEW | en145 | 0.17 | Its unique inclusion-minimal acceptance certificate is $\{\neg E,\neg B\}$; the two separate minimal rejection certificates are $\{E\}$ and $\{B\}$.
en147 | EDIT | en141 | 0.53 | With both facts withheld, an accepting specification $(E=0,B=0)$ and a rejecting specification $(E=1,B=0)$ remain compatible, so deferral has explicit countermodels.
en148 | NEW | en142 | 0.27 | After confirming reports-only ($\neg E$), asking whether the book prefix is protected determines the verdict.
en149 | NEW | en143 | 0.23 | With both fields initially unknown, neither one binary question guarantees a verdict for every possible answer.
en150 | SAME | en144 | 1.00 | These are classical finite Boolean and version-space facts, not new inference rules.
en151 | SAME | en145 | 1.00 | A separate Python replay checked the four worlds, nine disclosure states, inclusion-minimal certificates, contradictory evidence, and pairs of opposite-verdict worlds for deferred states; its passed.
en152 | SAME | en146 | 1.00 | That verifies the bounded decision logic, not actual human decisions or complete source behavior.
en153 | SAME | en147 | 1.00 | Learning more about a fixed contract removes possible worlds; renegotiating that contract changes the legitimate obligation.
en154 | SAME | en148 | 1.00 | The two transitions must not be conflated.
en155 | SAME | en149 | 1.00 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en156 | SAME | en150 | 1.00 | It adds one module, handles technical reports and errata, and keeps the original book output.
en157 | SAME | en151 | 1.00 | A rejection in Table 2 need not end the search for a patch within that boundary.
en158 | SAME | en152 | 1.00 | The contribution is not a new logical rule: it is a concrete account of why knowing that errata are required settles this decision, whereas a reports-only demand leaves the book-output commitment to be checked.
en159 | SAME | en153 | 1.00 | Applying it to a real review would require finding that commitment in a request, API documentation, tests or caller records.
en160 | SAME | en154 | 1.00 | · Deciding whether to accept a completed patch differs from choosing an architecture for future edits.
en161 | SAME | en155 | 1.00 | We retain one observation relevant to acceptance.
en162 | SAME | en156 | 1.00 | In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected bracketed=True .
en163 | SAME | en157 | 1.00 | A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.
en164 | SAME | en158 | 1.00 | The presence of a feature is different from its availability along a required route .
en165 | NEW | en157 | 0.18 | Unless the original entry point and its compatibility obligations are identified, implementation through a separate function cannot by itself establish that the requested behavior is available to existing callers.
en166 | SAME | en162 | 1.00 | The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in Paper B 통합 원고 12 · 한·영 문장 교정 and its .
en167 | SAME | en163 | 1.00 | Drawing a square first establishes what a routine does, not whether it must be edited.
en168 | SAME | en164 | 1.00 | That depends on whether sorting belongs to the routine's obligations.
en169 | SAME | en165 | 1.00 | In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required.
en170 | SAME | en166 | 1.00 | We did not observe a real OCP label being misused to reject a patch.
en171 | SAME | en167 | 1.00 | We asked what additional grounds a design-principle assessment needs before it can justify an engineering decision .
en172 | SAME | en168 | 1.00 | A practical review should first ask not only whether the patch implements a feature but where the request or an authorized agreement requires that feature to be reachable.
en173 | SAME | en169 | 1.00 | The reviewer should then locate the source of each protected old-client obligation in requests, API documentation, tests and actual call paths, without automatically treating every observed response as a promise.
en174 | SAME | en170 | 1.00 | If those sources leave different legitimate contracts possible, asking who can settle the obligation is more defensible than turning an OCP label into a categorical rejection.
en175 | SAME | en171 | 1.00 | Conversely, a demonstrated failure to meet an already binding new demand may reject the fixed patch before every other old-client promise is resolved.
en176 | SAME | en172 | 1.00 | This sequence is a recommendation derived from our authored example, not evidence that it reduces actual review costs in an organization.
en177 | SAME | en173 | 1.00 | Keeping the specifications compatible with known facts and checking their verdicts is elementary logic.
en178 | SAME | en174 | 1.00 | The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository.
en179 | SAME | en175 | 1.00 | Our evidence is confined to one benchmark archive and authored executable examples.
en180 | SAME | en176 | 1.00 | We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.
en181 | SAME | en177 | 1.00 | The audits in Sections 3–4 read the archived JSON and JSONL as data.
en182 | SAME | en178 | 1.00 | A separate script reproduced sixteen JSONL files, 768 rows, 48 distinct submissions, 24 scaffolds and 64 fixed model–strategy–language groups, and counted Python comments in four of twelve unique submissions.
en183 | SAME | en179 | 1.00 | Section 5 and the call-path check in Section 6 use examples written for this study.
en184 | SAME | en180 | 0.95 | The shape-layout experiment and Figure 1 remain preserved in manuscript 12; manuscript 18 does not reframe them as a new measured maintenance-cost trial.
en185 | SAME | en181 | 1.00 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en186 | SAME | en182 | 1.00 | The table below gives the nine verdicts for Section 5.
en187 | SAME | en183 | 1.00 | Both values of a withheld field remain possible.
en188 | SAME | en184 | 1.00 | Defer means that the compatible rows include both acceptance and rejection. - Meyer, B.
en189 | SAME | en185 | 1.00 | Object-Oriented Software Construction (1st ed.), pp.
en190 | SAME | en186 | 1.00 | The Open–Closed Principle . . - Jones, C.
en191 | SAME | en187 | 1.00 | Development Methods for Computer Programs Including a Notion of Interference .
en192 | SAME | en188 | 1.00 | Oxford University Computing Laboratory, PRG-25.
en193 | SAME | en189 | 1.00 | · . - Pehlivan, F., Ergüzen, A.
en194 | SAME | en190 | 1.00 | M., Lami, M., & Koyuncu, A.
en195 | SAME | en191 | 1.00 | An Empirical Study on Prompting LLMs to Detect Design Principle Violations .
en196 | SAME | en192 | 1.00 | ASE 2025 NIER. . - Bräuer et al.
en197 | SAME | en193 | 1.00 | Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research . . - Cabral et al.
en198 | SAME | en194 | 1.00 | Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding . . - Zhu, H., Zhang, Q., Wang, J., Yang, Z., & Qiu, Y.
en199 | SAME | en195 | 1.00 | Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits . . - Kane, M.
en200 | SAME | en196 | 1.00 | Validating the Interpretations and Uses of Test Scores .
en201 | SAME | en197 | 1.00 | Journal of Educational Measurement , 50(1), 1–73.
en202 | SAME | en198 | 1.00 | · . - Zave, P., & Jackson, M.
en203 | SAME | en199 | 1.00 | Four Dark Corners of Requirements Engineering .
en204 | SAME | en200 | 1.00 | ACM Transactions on Software Engineering and Methodology , 6(1), 1–30.
en205 | SAME | en201 | 1.00 | T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S.
en206 | SAME | en202 | 1.00 | The Oracle Problem in Software Testing: A Survey .
en207 | SAME | en203 | 1.00 | IEEE Transactions on Software Engineering .
en208 | SAME | en204 | 1.00 | · . - Widyasari, R., Zhang, T., Bouraffa, A., Maalej, W., & Lo, D.
en209 | SAME | en205 | 1.00 | Explaining Explanations: An Empirical Study of Explanations in Code Reviews .
en210 | SAME | en206 | 1.00 | ACM Transactions on Software Engineering and Methodology , 34(6), Article 177.
en211 | SAME | en207 | 1.00 | · . - Papotti, A., Paramitha, R., & Massacci, F.
en212 | SAME | en208 | 1.00 | On the acceptance by code reviewers of candidate security patches suggested by Automated Program Repair tools .
en213 | SAME | en209 | 1.00 | Empirical Software Engineering , 29, Article 132.
en214 | SAME | en210 | 1.00 | · . - Jin, H., & Chen, H.
en215 | SAME | en211 | 1.00 | Are LLMs Reliable Code Reviewers?
en216 | SAME | en212 | 1.00 | Systematic Overcorrection in Requirement Conformance Judgement .
en217 | SAME | en213 | 1.00 | · . - Ling, M., Zou, J., & Liu, X.
en218 | SAME | en214 | 1.00 | Negotiating Completion in Agentic Software Work: Acceptance Boundaries and Deferred Requirements .
en219 | SAME | en215 | 1.00 | 이 목록은 인용된 주요 자료를 확인할 수 있게 모은 집필용 서지이며, 서지형식·인용 위치·전수 대조를 마친 제출용 참고문헌은 아직 아니다.
en220 | SAME | en216 | 1.00 | / These are verified reading anchors, not yet a fully formatted submission bibliography.
Summary en: SAME 206, EDIT 2, NEW 12

## v19 · [Notion](https://app.notion.com/p/41fef561cf9281fabdf5d0548325beec)
### ko (190 sentences)
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
ko033 | SAME | ko033 | 1.00 | · · 우리는 서로 다른 두 자료를 사용했다.
ko034 | SAME | ko034 | 1.00 | 벤치마크에서는 분류를 요구받은 모델에게 실제로 어떤 입력이 주어졌는지 조사했다.
ko035 | SAME | ko035 | 1.00 | 도서관 예제에서는 패치 한 개를 고정하고, 적용할 요구와 보호할 계약을 바꿔 가며 실행 결과와 승인 기준을 대조했다.
ko036 | SAME | ko036 | 1.00 | 벤치마크의 저장 코드와 도서관 코드는 별개이고, 어느 쪽에도 실제 검토자의 승인·거절 판단은 포함되지 않는다.
ko037 | SAME | ko037 | 1.00 | OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다.
ko038 | SAME | ko038 | 1.00 | 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다.
ko039 | SAME | ko039 | 1.00 | 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다.
ko040 | SAME | ko040 | 1.00 | 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다.
ko041 | SAME | ko041 | 1.00 | 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다.
ko042 | SAME | ko042 | 1.00 | 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.
ko043 | SAME | ko043 | 1.00 | 지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다.
ko044 | SAME | ko044 | 1.00 | 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다.
ko045 | SAME | ko045 | 1.00 | 이 판독은 제출 코드를 가린 지시문에 관한 것이다.
ko046 | SAME | ko046 | 1.00 | 독립 감사에서 Python 저장 행 192개를 이루는 고유 코드 12개를 검사하자 4개에서 주석 토큰 46개를 발견했고, docstring을 포함한 코드는 없었다.
ko047 | SAME | ko047 | 1.00 | 주석이 기능의 의도를 암시할 수 있으므로, 지시문에 개별 요구가 없다는 사실을 코드 전체에 명세 단서가 없다는 주장으로 확대하지 않았다.
ko048 | SAME | ko048 | 1.00 | 다른 세 언어의 주석은 같은 방법으로 계수하지 않았다.
ko049 | SAME | ko049 | 1.00 | 저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다.
ko050 | SAME | ko050 | 1.00 | Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다.
ko051 | SAME | ko051 | 1.00 | 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다.
ko052 | SAME | ko052 | 1.00 | 압축 파일 안의 코드 자체는 실행하지 않았다.
ko053 | SAME | ko053 | 1.00 | 도서관 예제에서는 원본 소스와 수정안, 호출 입력, 새 모듈을 추가할 수 있다는 편집 범위를 고정했다.
ko054 | SAME | ko054 | 1.00 | 코드 실행으로 확인한 것은 구체적인 입력에서 나온 출력과 예외다.
ko055 | SAME | ko055 | 1.00 | 반면 기술보고서·정오표 중 무엇을 요구하는지, 책 출력의 접두어가 보호 대상인지, 새 요구를 충족하면서 보호된 기존 동작을 보존해야 승인한다 는 기준은 모두 연구자가 정했다.
ko056 | SAME | ko056 | 1.00 | 따라서 §5의 표는 독립 심사위원의 판정이 아니라 우리가 지정한 기준을 실행 관찰에 적용한 결과다.
ko057 | SAME | ko057 | 1.00 | 일부 전제만 공개한 경우에는 두 요구와 두 계약으로 이루어진 후보 명세 중 공개된 사실과 맞는 것만 남겼다.
ko058 | SAME | ko058 | 1.00 | 이 후보군 밖의 실제 요구나 계약까지 조사했다고 가정하지 않는다.
ko059 | SAME | ko059 | 1.00 | · · · · Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21) Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko060 | SAME | ko060 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko061 | SAME | ko061 | 1.00 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko062 | SAME | ko062 | 1.00 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko063 | SAME | ko063 | 1.00 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko064 | SAME | ko064 | 1.00 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko065 | SAME | ko065 | 1.00 | 추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. gpt-4o-mini 와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다.
ko066 | SAME | ko066 | 1.00 | 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다.
ko067 | SAME | ko067 | 1.00 | 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.
ko068 | SAME | ko068 | 1.00 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko069 | SAME | ko069 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko070 | SAME | ko070 | 1.00 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko071 | SAME | ko071 | 1.00 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko072 | SAME | ko072 | 1.00 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko073 | SAME | ko073 | 1.00 | 저장 코드와 참조 쌍은 앞에서 명시한 문자열 정규화 기준에서 일치하지 않았으며, Python 코드에 한한 AST 비교에서도 일치 사례가 없었다.
ko074 | SAME | ko074 | 1.00 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko075 | SAME | ko075 | 1.00 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko076 | SAME | ko076 | 1.00 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko077 | SAME | ko077 | 1.00 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko078 | SAME | ko078 | 1.00 | · · · Bräuer 등(2018)은 설계 원칙을 어떻게 측정할지 전문가에게 물었고, Cabral 등(2024)은 SOLID를 적용한 코드를 이해하고 확장하는 경험을 조사했다.
ko079 | SAME | ko079 | 1.00 | Zhu 등(2026)은 구체적인 저장소 변경 과제에 기능 및 구조 검사를 결합했다.
ko080 | SAME | ko080 | 1.00 | 우리의 벤치마크 감사도 분류 성능을 부정하려는 것이 아니다.
ko081 | SAME | ko081 | 1.00 | 분류에 성공했다는 증거를 수정안 거절의 증거로 옮길 때 무엇이 더 필요한지를 묻는다.
ko082 | SAME | ko082 | 1.00 | · · 실제 리뷰 연구는 이 논문의 주장 범위를 더 엄격하게 제한한다.
ko083 | SAME | ko083 | 1.00 | Widyasari 등(2025)은 Gerrit 코드 리뷰 댓글 793건을 분석하고 규칙이나 원칙을 근거로 드는 설명 유형을 확인했다.
ko084 | SAME | ko084 | 1.00 | 이는 원칙에 의거한 설명이 리뷰에 존재한다는 증거지만, 원칙이 잘못 적용돼 특정 수정안이 거절됐다는 증거는 아니다.
ko085 | SAME | ko085 | 1.00 | Papotti 등(2024)은 컴퓨터과학 석사과정 학생 72명을 대상으로 보안 자동 수리 패치의 채택 여부를 실험했다.
ko086 | SAME | ko086 | 1.00 | 제안 도구의 전문성을 알리는 정보에 따라 판단이 바뀌는 현상을 관찰했지만, 원칙 위반 라벨을 대상으로 한 연구는 아니다.
ko087 | SAME | ko087 | 1.00 | 두 논문의 실제 사람에 대한 관측은 우리가 구성한 표 2의 승인 기준과 다르다.
ko088 | SAME | ko088 | 1.00 | · Jin과 Chen(2026)은 정답 코드와 결함 코드에 대한 다섯 언어 모델의 요구 적합성 판단을 세 프로그래밍 벤치마크에서 실험하고, 맞는 코드를 잘못 거절하는 현상과 설명·수정 제안을 요구하는 프롬프트의 위험을 보고했다.
ko089 | SAME | ko089 | 1.00 | 따라서 LLM의 과잉 거절을 처음 지적했다고 주장할 수 없다.
ko090 | SAME | ko090 | 1.00 | Ling·Zou·Liu(2026)는 공개 GitHub 변경 사례의 질적 연구에서 병합, 이슈 종료, 요구 충족이 서로 다른 결과일 수 있음을 논증했다.
ko091 | SAME | ko091 | 1.00 | 수용 경계가 조건부라는 발견도 우리의 최초성이 아니다.
ko092 | SAME | ko092 | 1.00 | 우리 사례는 실행 결과가 고정된 패치에서 현재 공개된 요구·계약이 정당화하는 판정과 추가 질문을 정확하게 분리하는 재현 가능한 실례 다.
ko093 | SAME | ko093 | 1.00 | · 그 질문 자체에도 중요한 선행연구가 있다.
ko094 | SAME | ko094 | 1.00 | Kane(2013)은 검사 점수의 해석을 뒷받침하는 증거가 그 점수를 특정 결정에 사용하는 일까지 정당화하지는 않는다고 논했다.
ko095 | SAME | ko095 | 1.00 | 이는 소프트웨어 리뷰를 실험한 결과가 아니라, 평가 결과의 사용 을 따로 정당화해야 한다는 일반적인 논증이다.
ko096 | SAME | ko096 | 1.00 | Zave와 Jackson(1997)은 요구사항, 기계 명세, 환경에 관한 지식이 어떻게 연결되는지 설명하면서 행위의 통제 주체를 구별했다.
ko097 | SAME | ko097 | 1.00 | 원을 앞에 정렬할 책임이 호출자에게 있는지 함수에 있는지부터 따져야 한다는 우리의 질문도 이러한 오래된 문제의 한 사례다.
ko098 | SAME | ko098 | 1.00 | 존스(1981) 역시 병렬 프로그램에서 환경 의존 조건과 프로그램 보장 조건의 양립을 다뤘다.
ko099 | SAME | ko099 | 1.00 | · · Barr 등(2015)이 정리한 테스트 오라클 문제는 코드 실행과 올바름 판정 사이에도 근거가 필요함을 상기시킨다.
ko100 | SAME | ko100 | 1.00 | §5의 시험은 지정된 호출의 동작을 확인하지만, 그 동작을 보존하겠다는 실제 프로젝트의 약속을 입증하지는 않는다.
ko101 | SAME | ko101 | 1.00 | 따라서 다음 절의 요구·계약은 발견한 사실이 아니라 명시적으로 정한 전제다.
ko102 | SAME | ko102 | 1.00 | 위반 범주를 맞혔다는 사실은 코드에 특정 구조가 있다는 평가를 뒷받침한다.
ko103 | SAME | ko103 | 1.00 | 그러나 수정안을 거절하려면 (1) 누구에게서 나온 새 요구인지, (2) 기존 호출자에게 계속 보장하기로 한 동작이 무엇인지, (3) 그 동작과 새 기능을 어느 호출 경로로 제공해야 하는지까지 알아야 한다.
ko104 | SAME | ko104 | 1.00 | 이 가운데 일부는 소스에 표시될 수 있지만, 관측한 구현이 곧 승인된 계약이라는 뜻은 아니다.
ko105 | SAME | ko105 | 1.00 | 예컨대 같은 출력 변경을 보고도 책 출력이 보호 대상일 때와 아닐 때는 서로 다른 판정이 가능하다.
ko106 | SAME | ko106 | 1.00 | 분류 라벨을 고정한 채 판정이 달라지는 반례는 §5에서 실행한 동일 패치의 네 명세에 한정된다.
ko107 | SAME | ko107 | 1.00 | 이를 통해 분류 점수 자체를 부정하거나 실제 리뷰어가 라벨 때문에 패치를 거절했다고 주장하지 않는다.
ko108 | NEW | ko016 | 0.06 | 이 주장은 분류기에 어떤 정보를 주는지에 따라서도 달라진다.
ko109 | NEW | ko154 | 0.04 | 소스 코드만 보고 OCP 위반 여부를 판정하는 분류기라면 코드가 고정된 네 명세에서 입력과 출력 라벨을 동일하게 유지한다.
ko110 | NEW | ko064 | 0.06 | 반면 실제 요구서와 호출자 계약을 입력받는 문맥 의존적 평가자는 명세에 따라 판단을 변경할 수 있다.
ko111 | NEW | ko009 | 0.04 | 따라서 이 논문의 반례는 모든 OCP 평가가 언제나 같은 라벨을 낸다는 주장이 아니라, 고정된 소스의 위반 라벨만으로 서로 다른 실제 유지보수 판정을 식별할 수 없다는 제한된 주장 이다.
ko112 | NEW | ko067 | 0.05 | 기존 요구사항 추적표나 호환성 검토 역시 추가 근거를 물어 문제를 해결할 수 있으므로, 이를 우리의 새 방법만이 수행한다고 해석하지 않는다.
ko113 | SAME | ko108 | 1.00 | 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko114 | SAME | ko109 | 1.00 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko115 | SAME | ko110 | 1.00 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko116 | SAME | ko111 | 1.00 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko117 | SAME | ko112 | 1.00 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko118 | SAME | ko113 | 1.00 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko119 | SAME | ko114 | 1.00 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko120 | SAME | ko115 | 1.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko121 | SAME | ko116 | 1.00 | 책 접두어가 보호 대상이 아니라는 가정은 실제 이용자가 그 출력을 기대하지 않는다는 관찰이 아니다.
ko122 | SAME | ko117 | 1.00 | 단지 이 비교에서 보존 의무로 정하지 않았다는 뜻이다.
ko123 | SAME | ko118 | 1.00 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko124 | SAME | ko119 | 1.00 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko125 | SAME | ko120 | 1.00 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko126 | SAME | ko121 | 1.00 | 이 절차는 실제 명세가 표의 네 경우 중 하나라는 조건 아래서만 성립한다.
ko127 | SAME | ko122 | 1.00 | 공개된 사실과 맞는 행이 하나도 없다면 승인이나 거절을 내릴 것이 아니라 자료 또는 후보군이 잘못됐는지 확인해야 한다.
ko128 | SAME | ko123 | 1.00 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko129 | SAME | ko124 | 1.00 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko130 | SAME | ko125 | 1.00 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko131 | SAME | ko126 | 1.00 | 정오표 지원이 필수인지 여부를 $E$, 기존 책 출력 접두어를 보호하는지 여부를 $B$라고 두자.
ko132 | SAME | ko127 | 1.00 | 연구자가 정한 네 명세에 한정하면, 이 고정 패치의 승인 조건은 $A(E,B)=\neg E\land\neg B$다.
ko133 | SAME | ko128 | 1.00 | 따라서 승인에 필요한 최소 증거는 $\{\neg E,\neg B\}$이며, 거절을 확정하는 최소 증거는 $\{E\}$ 또는 $\{B\}$다.
ko134 | SAME | ko129 | 1.00 | 두 조건을 모두 알 수 없다면, 승인 명세 $(E=0,B=0)$와 거절 명세 $(E=1,B=0)$가 양립하므로 판정을 보류한다.
ko135 | SAME | ko130 | 1.00 | 기술보고서만 요구한다는 사실, 즉 $\neg E$가 확인되면 $B$를 물어 어느 쪽인지 결정할 수 있다.
ko136 | SAME | ko131 | 1.00 | 반면 두 조건이 전부 미공개일 때는 하나의 예·아니오 질문만으로 모든 답변에 대해 판정을 확정하지 못한다.
ko137 | SAME | ko132 | 1.00 | 이것은 새로운 논리 규칙이 아니라 고전적인 유한 정보 집합 판정이다.
ko138 | SAME | ko133 | 1.00 | 별도 Python 코드는 네 명세의 공개 상태 아홉 가지, 최소 승인·거절 증거, 보류 상태의 대립 명세, 모순된 사실의 처리까지 검사했고 가 통과했다.
ko139 | SAME | ko134 | 1.00 | 이 테스트가 실제 검토자의 판단이나 원본 도서관 프로그램의 전체 동작을 재검증한 것은 아니다.
ko140 | SAME | ko135 | 1.00 | 또한 고정된 계약에 관한 사실을 알게 되는 것 과 계약 자체를 변경하는 것 을 구별해야 한다.
ko141 | SAME | ko136 | 1.00 | 앞의 경우에는 가능한 명세의 집합이 줄지만, 뒤의 경우에는 승인 조건 자체가 달라질 수 있다.
ko142 | SAME | ko137 | 1.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko143 | SAME | ko138 | 1.00 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko144 | SAME | ko139 | 1.00 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko145 | SAME | ko140 | 1.00 | 이 비교에서 얻은 것은 새로운 논리 규칙이 아니다.
ko146 | SAME | ko141 | 1.00 | 한 사실만 알아도 거절이 확정되는 경우와, 책 출력 약속을 물어야 하는 경우를 구체적인 호출 결과로 구분한 것이다.
ko147 | SAME | ko142 | 1.00 | 실제 리뷰에 적용하려면 요구서와 API 문서, 테스트 및 호출 기록에서 그 약속의 근거를 따로 찾아야 한다.
ko148 | NEW | ko007 | 0.11 | · 계약 조건을 하나 더 추가했을 때의 민감도.
ko149 | NEW | ko087 | 0.02 | 위의 승인 규칙은 두 조건만 관련된다는 전제에 의존한다.
ko150 | NEW | ko127 | 0.06 | 이 고정 패치가 다른 독립적인 보호 의무도 위반한다고 연구자가 가정하고, 그 의무가 현재 실제로 적용되는지를 $C$라고 두자.
ko151 | NEW | ko127 | 0.13 | 세 의무 가운데 하나라도 적용되면 패치를 거절하도록 승인 기준을 새로 정하면 $A_3(E,B,C)=\neg E\land\neg B\land\neg C$가 된다.
ko152 | NEW | ko133 | 0.04 | 이때 네 명세는 여덟 가지 완전 명세로, 아홉 공개 상태는 스물일곱 공개 상태로 확장된다.
ko153 | NEW | ko061 | 0.03 | 전수 계산 결과는 승인 1개, 거절 19개, 보류 7개다.
ko154 | NEW | ko131 | 0.04 | 특히 예전 두 조건이 모두 거짓이라고 알더라도 $C$가 미공개라면 기존의 승인은 보류 로 바뀐다.
ko155 | NEW | ko101 | 0.04 | 반대로 $C$가 적용되지 않는다고 명시적으로 확인하면 원래의 아홉 상태와 승인 1·거절 5·보류 3 분포가 복원된다.
ko156 | NEW | ko154 | 0.12 | 이 계산은 실제로 새로운 보안·성능 결함을 발견했다는 뜻이 아니다.
ko157 | NEW | ko087 | 0.03 | $C$는 연구자가 만든 제삼의 독립 의무이고, 새 기준은 기존 승인 기준보다 엄격하다.
ko158 | NEW | ko075 | 0.04 | 그 목적은 필요한 요구를 전부 열거했다는 근거 없이 기존의 승인 판정을 일반화할 수 없음 을 드러내는 것이다.
ko159 | NEW | ko134 | 0.06 | 그렇다고 실제 검토자가 가능한 모든 요구를 무한히 조사해야 하는 것도 아니다.
ko160 | NEW | ko087 | 0.03 | 어떤 요구가 승인 기준에 포함되는지는 적격한 주체와 계약 출처에 의해 제한돼야 한다.
ko161 | NEW | ko150 | 0.04 | [전수 계산 코드](./paper_b_three_obligation_sensitivity.py) · [회귀 테스트](./test_paper_b_three_obligation_sensitivity.py).
ko162 | SAME | ko143 | 1.00 | 완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다.
ko163 | SAME | ko144 | 1.00 | 여기서는 앞의 질문에 해당하는 관찰만 남긴다.
ko164 | SAME | ko145 | 1.00 | 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 bracketed=True 를 넘기면 인자를 거절했다.
ko165 | SAME | ko146 | 1.00 | 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다.
ko166 | SAME | ko147 | 1.00 | 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.
ko167 | SAME | ko148 | 1.00 | 새 기능이 있다는 사실과 요구된 호출 경로에서 쓸 수 있다는 사실 은 다르다.
ko168 | SAME | ko149 | 1.00 | 보호해야 할 기존 진입점이 무엇인지 확인하지 않으면, 같은 옵션을 새 함수에서 제공했다는 사실만으로 수정안의 적합성을 판정할 수 없다.
ko169 | SAME | ko150 | 1.00 | 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 Paper B 통합 원고 12 · 한·영 문장 교정 및 에 원형 그대로 보존했다.
ko170 | SAME | ko151 | 1.00 | 마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다.
ko171 | SAME | ko152 | 1.00 | 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다.
ko172 | SAME | ko153 | 1.00 | 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다.
ko173 | SAME | ko154 | 1.00 | 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다.
ko174 | SAME | ko155 | 1.00 | 원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가 가 이 논문에서 다룬 질문이다.
ko175 | SAME | ko156 | 1.00 | 실제 검토에서 먼저 확인할 것은 수정안의 새 기능만이 아니라, 요구한 사람이나 합의된 문서가 그 기능을 어느 진입점에서 제공하도록 정했는지다.
ko176 | SAME | ko157 | 1.00 | 그다음 기존 호출자가 의존하는 동작 중 무엇이 보호 대상인지 요구서·API 문서·테스트·호출 코드에서 근거를 찾아야 한다.
ko177 | SAME | ko158 | 1.00 | 이 근거가 둘 이상의 가능한 계약을 남긴다면, 원칙 위반이라는 이름으로 결론을 확정하기보다 계약의 출처와 범위를 묻는 편이 정확하다.
ko178 | SAME | ko159 | 1.00 | 반대로 새로운 요구를 충족하지 못한다는 사실이 이미 확정됐다면, 어떤 기존 계약이 추가로 보호되는지 모두 조사하기 전에 해당 수정안을 거절할 수도 있다.
ko179 | SAME | ko160 | 1.00 | 이러한 질문의 순서는 이 논문의 구성 사례에서 나온 실무적 제안이지, 실제 개발 조직의 효율이 개선됐다는 관측 결과는 아니다.
ko180 | SAME | ko161 | 1.00 | 공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다.
ko181 | SAME | ko162 | 1.00 | 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다.
ko182 | EDIT | ko163 | 0.57 | 이 연구는 한 벤치마크의 저장 입력과 연구자가 구성한 실행 예제 및 추가 의무에 관한 논리적 민감도 분석만을 다뤘다.
ko183 | SAME | ko164 | 1.00 | 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.
ko184 | SAME | ko165 | 1.00 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko185 | SAME | ko166 | 1.00 | 독립 감사 스크립트는 같은 ZIP을 실행 코드가 아닌 자료로 읽어 16개 JSONL 파일, 768행, 48개 고유 코드, 24개 틀, 64개 세부 집단을 재계산했고, Python 고유 코드 12개 중 주석이 있는 4개를 확인했다.
ko186 | SAME | ko167 | 1.00 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko187 | SAME | ko168 | 1.00 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko188 | EDIT | ko169 | 0.87 | 12판에 있던 그림 1과 파일 배치 실험은 19판 본문에 싣지 않았으며, 원본 그림과 실행 기록을 12판에 보존했다.
ko189 | SAME | ko170 | 1.00 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko190 | SAME | ko171 | 1.00 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
Summary ko: SAME 169, EDIT 2, NEW 19

### en (238 sentences)
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
en040 | SAME | en040 | 1.00 | · · We used two distinct sources of evidence.
en041 | SAME | en041 | 1.00 | We audited the saved benchmark inputs to determine what a classifier was actually asked to judge.
en042 | SAME | en042 | 1.00 | Separately, we fixed one catalog patch and varied the demands and protected caller commitments against which its execution was assessed.
en043 | SAME | en043 | 1.00 | The benchmark submissions are not instances of the catalog patch, and neither source records decisions by real reviewers.
en044 | SAME | en044 | 1.00 | The OCP reference material contains 48 before-and-after code pairs.
en045 | SAME | en045 | 1.00 | Sixteen saved JSONL files each contain 48 records, yielding 768 rows.
en046 | SAME | en046 | 1.00 | Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times.
en047 | SAME | en047 | 1.00 | We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality.
en048 | SAME | en048 | 1.00 | The result was 24 scaffolds.
en049 | SAME | en049 | 1.00 | Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs.
en050 | SAME | en050 | 1.00 | The 768 records are repeated submissions, not independent maintenance cases.
en051 | SAME | en051 | 1.00 | We separately read the masked instructions for case-specific change requests and protected caller commitments.
en052 | SAME | en052 | 1.00 | An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape.
en053 | SAME | en053 | 1.00 | We inspected the text outside the submitted code, not the whole semantic context.
en054 | SAME | en054 | 1.00 | In a separate replication, the 192 saved Python rows reduced to twelve distinct code submissions; four contained a total of 46 comment tokens, and none had an AST-detected docstring.
en055 | SAME | en055 | 1.00 | These comments may convey implementation intent, but counting them does not establish a contract.
en056 | SAME | en056 | 1.00 | We did not perform the same comment-token audit for the other three languages.
en057 | SAME | en057 | 1.00 | We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace.
en058 | SAME | en058 | 1.00 | For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions.
en059 | SAME | en059 | 1.00 | These tests do not establish whether inherited methods remain available or whether callers were promised a behavior.
en060 | SAME | en060 | 1.00 | We read code as archive data and did not execute it.
en061 | SAME | en061 | 1.00 | For the catalog, we fixed the baseline, candidate patch, calls and permission to add a module.
en062 | SAME | en062 | 1.00 | Executing the code established outputs and exceptions for those calls.
en063 | SAME | en063 | 1.00 | The possible demands (technical reports alone, or technical reports and errata), the two scopes of the book-output obligation, and the rule that an acceptable patch must meet its demand and preserve protected behavior we
en064 | SAME | en064 | 1.00 | Table 2 therefore applies authored criteria to observed behavior; it does not report independent human decisions.
en065 | SAME | en065 | 1.00 | For partial disclosure, we retained only the candidate specifications compatible with known facts.
en066 | SAME | en066 | 1.00 | We did not attempt to enumerate obligations outside these four constructed cases.
en067 | SAME | en067 | 1.00 | · · · Pehlivan et al. chose violation scenarios and refined the generated examples.
en068 | SAME | en068 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en069 | SAME | en069 | 1.00 | The benchmark compares model classifications with the resulting labels.
en070 | SAME | en070 | 1.00 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en071 | SAME | en071 | 1.00 | No two strategies shared a template string.
en072 | SAME | en072 | 1.00 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en073 | SAME | en073 | 1.00 | An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: gpt-4o-mini differed from the other three models.
en074 | SAME | en074 | 1.00 | Holding model, strategy and language fixed left one scaffold shared across twelve programs.
en075 | SAME | en075 | 1.00 | No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST.
en076 | SAME | en076 | 1.00 | These checks do not establish semantic independence or source lineage.
en077 | SAME | en077 | 1.00 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en078 | SAME | en078 | 1.00 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en079 | SAME | en079 | 1.00 | If a new shape is needed, that branch is a place to look.
en080 | SAME | en080 | 1.00 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en081 | SAME | en081 | 1.00 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en082 | SAME | en082 | 1.00 | No submitted program matched a reference side under the reported textual normalizations, and the separate Python-only AST comparison also found no match.
en083 | SAME | en083 | 1.00 | Pair 37 establishes that a declaration was removed.
en084 | SAME | en084 | 1.00 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en085 | SAME | en085 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en086 | SAME | en086 | 1.00 | The prompt example is in JSONL line 13 (record ID 12).
en087 | SAME | en087 | 1.00 | Pair 37 is in a separate reference JSON file.
en088 | SAME | en088 | 1.00 | · · · Bräuer et al. (2018) examined the measurement of design principles with experts; Cabral et al. (2024) studied understanding and extension under a bundled SOLID treatment; Zhu et al. (2026) supplied repository chang
en089 | SAME | en089 | 1.00 | These evaluate different objects.
en090 | SAME | en090 | 1.00 | Our audit does not contest the benchmark's classification task.
en091 | SAME | en091 | 1.00 | It asks what else would be needed to use such a classification as a reason to reject a patch.
en092 | SAME | en092 | 1.00 | · · Empirical review studies narrow the claim further.
en093 | SAME | en093 | 1.00 | Widyasari et al. (2025) coded 793 Gerrit review comments and identified explanation categories including appeals to rules or principles.
en094 | SAME | en094 | 1.00 | This shows that principle-based explanations appear in review practice; it does not show that such principles caused an unjustified patch rejection.
en095 | SAME | en095 | 1.00 | Papotti et al. (2024) experimentally studied 72 computer-science master's students deciding whether to adopt security patches proposed by automatic program repair tools, and found that information about the purported too
en096 | SAME | en096 | 1.00 | Unlike our stipulated Table 2 judgments, those were observed human choices.
en097 | SAME | en097 | 1.00 | · Jin and Chen (2026) tested five language models' judgments of canonical and buggy implementations against natural-language specifications across three programming benchmarks.
en098 | SAME | en098 | 1.00 | They reported false rejection of correct code and risks from prompts that demand explanations or fixes.
en099 | SAME | en099 | 1.00 | We cannot claim to have discovered LLM over-rejection or to improve its error rate: our archive does not record independent patch-acceptance judgments by those models.
en100 | SAME | en100 | 1.00 | Ling, Zou, and Liu (2026) examined public agent-associated contributions and distinguished merges, issue closures, and requirement satisfaction.
en101 | SAME | en101 | 1.00 | Conditional acceptance is not first discovered by this paper either.
en102 | SAME | en102 | 1.00 | Our narrower addition is to hold a patch's execution fixed and make explicit which partially disclosed requirement and contract facts warrant a verdict and which warrant further inquiry .
en103 | SAME | en103 | 1.00 | · This is not a new problem in general.
en104 | SAME | en104 | 1.00 | Kane (2013) argues that evidence supporting an interpretation of test scores does not automatically justify using those scores for a particular decision.
en105 | SAME | en105 | 1.00 | His work does not test software reviews; it establishes the importance of justifying an assessment's use .
en106 | SAME | en106 | 1.00 | Zave and Jackson (1997) distinguish requirements, machine specifications and knowledge of the environment, including which actor controls an action.
en107 | SAME | en107 | 1.00 | Whether sorting belongs to a caller or a drawing function is an instance of that longstanding question.
en108 | SAME | en108 | 1.00 | Jones (1981) likewise developed conditions for compatible environmental reliance and program guarantees in parallel programs.
en109 | SAME | en109 | 1.00 | We do not claim these distinctions as our invention.
en110 | SAME | en110 | 1.00 | · · Barr et al.'s (2015) survey of the test-oracle problem makes a related point about our executable fixture.
en111 | SAME | en111 | 1.00 | Tests establish outputs for chosen inputs; they do not, without an independently grounded oracle, establish which outputs a real project has promised to preserve.
en112 | SAME | en112 | 1.00 | Thus the demands and contracts in Section 5 are explicit assumptions rather than requirements recovered from a repository.
en113 | SAME | en113 | 1.00 | From a classification to a patch disposition.
en114 | SAME | en114 | 1.00 | Correctly naming a design-principle violation supports a judgment about a structural feature of code.
en115 | SAME | en115 | 1.00 | Rejecting a specific patch requires different grounds: (i) the source and scope of the new request, (ii) the behavior the project committed to existing callers, and (iii) the call path through which the request and those
en116 | SAME | en116 | 1.00 | Some clues may reside in source, but observed behavior is not automatically an authorized compatibility promise.
en117 | SAME | en117 | 1.00 | The same change in book output can be unacceptable under one declared contract and acceptable under another.
en118 | SAME | en118 | 1.00 | Section 5 supplies a fixed-patch, four-specification witness to that gap.
en119 | SAME | en119 | 1.00 | It does not disprove the benchmark's classification scores or establish that a real reviewer rejected a patch because of an OCP label.
en120 | NEW | en015 | 0.19 | The inference also depends on what information the classifier receives.
en121 | NEW | en145 | 0.14 | A source-only OCP classifier has the same input, and hence the same classification output, across our four fixed-code specifications.
en122 | NEW | en051 | 0.15 | A context-sensitive evaluator given authentic requests and caller contracts may rightly return different assessments.
en123 | NEW | en049 | 0.16 | Our witness therefore does not say that all OCP evaluations are constant across contexts.
en124 | NEW | en050 | 0.16 | It shows only that a label based solely on fixed code cannot identify which distinct maintenance decision binds under unspecified obligations .
en125 | NEW | en177 | 0.13 | Ordinary requirements traceability and compatibility checklists can ask for these same missing facts; we claim no exclusive ability to do so.
en126 | SAME | en120 | 1.00 | We built a small catalog based on Meyer’s example.
en127 | SAME | en121 | 1.00 | The client in client.py displays each publication through the catalog function passed to it.
en128 | SAME | en122 | 1.00 | The patch adds reports.py to wrap that function.
en129 | SAME | en123 | 1.00 | The source of catalog.py and client.py stays identical.
en130 | SAME | en124 | 1.00 | The resulting catalog displays technical reports and still rejects errata.
en131 | SAME | en125 | 1.00 | For books it now prints BOOK where it used to print book .
en132 | SAME | en126 | 1.00 | Suppose the only new requirement is to handle technical reports.
en133 | SAME | en127 | 1.00 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en134 | SAME | en128 | 1.00 | If the book output is outside the contract, the same patch can be accepted.
en135 | SAME | en129 | 1.00 | Table 2 applies both contracts again when errata are also required.
en136 | SAME | en130 | 1.00 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en137 | SAME | en131 | 1.00 | Excluding the book prefix from our stipulated contract is not evidence that real users have no expectation about it; it only means this example does not impose that obligation.
en138 | SAME | en132 | 1.00 | Two requirements for accepting a fixed patch.
en139 | SAME | en133 | 1.00 | Learning that errata are required leaves the last two rows of Table 2.
en140 | SAME | en134 | 1.00 | Both reject the patch, so the book contract need not be settled first.
en141 | SAME | en135 | 1.00 | Learning that technical reports are the whole request leaves the first two rows.
en142 | SAME | en136 | 1.00 | One accepts and one rejects.
en143 | SAME | en137 | 1.00 | The next question is whether the original book output is protected.
en144 | SAME | en138 | 1.00 | The procedure applies only if the actual specification is among these four authored cases.
en145 | SAME | en139 | 1.00 | If disclosure rules out every row, an empty candidate set is a reason to question the evidence or the candidate set, not to infer acceptance or rejection.
en146 | SAME | en140 | 1.00 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en147 | SAME | en141 | 1.00 | The reviewer can give a conditional answer or defer judgment.
en148 | SAME | en142 | 1.00 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en149 | SAME | en143 | 1.00 | Minimum evidence for a decision.
en150 | SAME | en144 | 1.00 | Let $E$ indicate that errata support is required and $B$ that the previous book prefix is protected.
en151 | SAME | en145 | 1.00 | Within the four stipulated specifications, the acceptance predicate is $A(E,B)=\neg E\land\neg B$.
en152 | SAME | en146 | 1.00 | Its unique inclusion-minimal acceptance certificate is $\{\neg E,\neg B\}$; the two separate minimal rejection certificates are $\{E\}$ and $\{B\}$.
en153 | SAME | en147 | 1.00 | With both facts withheld, an accepting specification $(E=0,B=0)$ and a rejecting specification $(E=1,B=0)$ remain compatible, so deferral has explicit countermodels.
en154 | SAME | en148 | 1.00 | After confirming reports-only ($\neg E$), asking whether the book prefix is protected determines the verdict.
en155 | SAME | en149 | 1.00 | With both fields initially unknown, neither one binary question guarantees a verdict for every possible answer.
en156 | SAME | en150 | 1.00 | These are classical finite Boolean and version-space facts, not new inference rules.
en157 | SAME | en151 | 1.00 | A separate Python replay checked the four worlds, nine disclosure states, inclusion-minimal certificates, contradictory evidence, and pairs of opposite-verdict worlds for deferred states; its passed.
en158 | SAME | en152 | 1.00 | That verifies the bounded decision logic, not actual human decisions or complete source behavior.
en159 | SAME | en153 | 1.00 | Learning more about a fixed contract removes possible worlds; renegotiating that contract changes the legitimate obligation.
en160 | SAME | en154 | 1.00 | The two transitions must not be conflated.
en161 | SAME | en155 | 1.00 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en162 | SAME | en156 | 1.00 | It adds one module, handles technical reports and errata, and keeps the original book output.
en163 | SAME | en157 | 1.00 | A rejection in Table 2 need not end the search for a patch within that boundary.
en164 | SAME | en158 | 1.00 | The contribution is not a new logical rule: it is a concrete account of why knowing that errata are required settles this decision, whereas a reports-only demand leaves the book-output commitment to be checked.
en165 | SAME | en159 | 1.00 | Applying it to a real review would require finding that commitment in a request, API documentation, tests or caller records.
en166 | NEW | en168 | 0.11 | · Sensitivity to an additional binding obligation.
en167 | NEW | en168 | 0.10 | The preceding approval depends on assuming that the two listed facts exhaust the criteria that matter.
en168 | NEW | en155 | 0.16 | Suppose, as another author-stipulated condition, that this same patch would violate a separate obligation if it were binding; let $C$ indicate whether that third obligation applies.
en169 | NEW | en065 | 0.21 | Under the stricter criterion $A_3(E,B,C)=\neg E\land\neg B\land\neg C$, the universe has eight complete specifications and twenty-seven partial disclosure states.
en170 | NEW | en136 | 0.16 | Exhaustive evaluation yields one ACCEPT, nineteen REJECT and seven DEFER states.
en171 | NEW | en188 | 0.11 | Crucially, evidence that both $E$ and $B$ are false no longer suffices to approve while $C$ remains unknown: the previous ACCEPT becomes DEFER.
en172 | NEW | en112 | 0.12 | If $C$ is explicitly false, the prior nine-state table and its one/five/three distribution are recovered.
en173 | NEW | en103 | 0.14 | This is not an empirically observed safety or performance defect.
en174 | NEW | en168 | 0.13 | The third obligation and stronger criterion were authored for sensitivity analysis.
en175 | NEW | en165 | 0.16 | The point is narrower: one cannot generalize an approval from the original four-world set without evidence that the listed obligations exhaust the relevant acceptance conditions.
en176 | NEW | en115 | 0.17 | Reviewers are not thereby required to investigate arbitrary imaginable obligations; a binding requirement still needs a legitimate source and scope.
en177 | NEW | en066 | 0.14 | [Enumeration code](./paper_b_three_obligation_sensitivity.py) · [regression tests](./test_paper_b_three_obligation_sensitivity.py).
en178 | SAME | en160 | 1.00 | Deciding whether to accept a completed patch differs from choosing an architecture for future edits.
en179 | SAME | en161 | 1.00 | We retain one observation relevant to acceptance.
en180 | SAME | en162 | 1.00 | In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected bracketed=True .
en181 | SAME | en163 | 1.00 | A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.
en182 | SAME | en164 | 1.00 | The presence of a feature is different from its availability along a required route .
en183 | SAME | en165 | 1.00 | Unless the original entry point and its compatibility obligations are identified, implementation through a separate function cannot by itself establish that the requested behavior is available to existing callers.
en184 | SAME | en166 | 1.00 | The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in Paper B 통합 원고 12 · 한·영 문장 교정 and its .
en185 | SAME | en167 | 1.00 | Drawing a square first establishes what a routine does, not whether it must be edited.
en186 | SAME | en168 | 1.00 | That depends on whether sorting belongs to the routine's obligations.
en187 | SAME | en169 | 1.00 | In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required.
en188 | SAME | en170 | 1.00 | We did not observe a real OCP label being misused to reject a patch.
en189 | SAME | en171 | 1.00 | We asked what additional grounds a design-principle assessment needs before it can justify an engineering decision .
en190 | SAME | en172 | 1.00 | A practical review should first ask not only whether the patch implements a feature but where the request or an authorized agreement requires that feature to be reachable.
en191 | SAME | en173 | 1.00 | The reviewer should then locate the source of each protected old-client obligation in requests, API documentation, tests and actual call paths, without automatically treating every observed response as a promise.
en192 | SAME | en174 | 1.00 | If those sources leave different legitimate contracts possible, asking who can settle the obligation is more defensible than turning an OCP label into a categorical rejection.
en193 | SAME | en175 | 1.00 | Conversely, a demonstrated failure to meet an already binding new demand may reject the fixed patch before every other old-client promise is resolved.
en194 | SAME | en176 | 1.00 | This sequence is a recommendation derived from our authored example, not evidence that it reduces actual review costs in an organization.
en195 | SAME | en177 | 1.00 | Keeping the specifications compatible with known facts and checking their verdicts is elementary logic.
en196 | SAME | en178 | 1.00 | The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository.
en197 | EDIT | en179 | 0.68 | Our evidence is confined to one benchmark archive, authored executable examples, and an authored logical sensitivity check.
en198 | SAME | en180 | 1.00 | We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.
en199 | SAME | en181 | 1.00 | The audits in Sections 3–4 read the archived JSON and JSONL as data.
en200 | SAME | en182 | 1.00 | A separate script reproduced sixteen JSONL files, 768 rows, 48 distinct submissions, 24 scaffolds and 64 fixed model–strategy–language groups, and counted Python comments in four of twelve unique submissions.
en201 | SAME | en183 | 1.00 | Section 5 and the call-path check in Section 6 use examples written for this study.
en202 | SAME | en184 | 0.95 | The shape-layout experiment and Figure 1 remain preserved in manuscript 12; manuscript 19 does not reframe them as a new measured maintenance-cost trial.
en203 | SAME | en185 | 1.00 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en204 | SAME | en186 | 1.00 | The table below gives the nine verdicts for Section 5.
en205 | SAME | en187 | 1.00 | Both values of a withheld field remain possible.
en206 | SAME | en188 | 1.00 | Defer means that the compatible rows include both acceptance and rejection. - Meyer, B.
en207 | SAME | en189 | 1.00 | Object-Oriented Software Construction (1st ed.), pp.
en208 | SAME | en190 | 1.00 | The Open–Closed Principle . . - Jones, C.
en209 | SAME | en191 | 1.00 | Development Methods for Computer Programs Including a Notion of Interference .
en210 | SAME | en192 | 1.00 | Oxford University Computing Laboratory, PRG-25.
en211 | SAME | en193 | 1.00 | · . - Pehlivan, F., Ergüzen, A.
en212 | SAME | en194 | 1.00 | M., Lami, M., & Koyuncu, A.
en213 | SAME | en195 | 1.00 | An Empirical Study on Prompting LLMs to Detect Design Principle Violations .
en214 | SAME | en196 | 1.00 | ASE 2025 NIER. . - Bräuer et al.
en215 | SAME | en197 | 1.00 | Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research . . - Cabral et al.
en216 | SAME | en198 | 1.00 | Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding . . - Zhu, H., Zhang, Q., Wang, J., Yang, Z., & Qiu, Y.
en217 | SAME | en199 | 1.00 | Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits . . - Kane, M.
en218 | SAME | en200 | 1.00 | Validating the Interpretations and Uses of Test Scores .
en219 | SAME | en201 | 1.00 | Journal of Educational Measurement , 50(1), 1–73.
en220 | SAME | en202 | 1.00 | · . - Zave, P., & Jackson, M.
en221 | SAME | en203 | 1.00 | Four Dark Corners of Requirements Engineering .
en222 | SAME | en204 | 1.00 | ACM Transactions on Software Engineering and Methodology , 6(1), 1–30.
en223 | SAME | en205 | 1.00 | T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S.
en224 | SAME | en206 | 1.00 | The Oracle Problem in Software Testing: A Survey .
en225 | SAME | en207 | 1.00 | IEEE Transactions on Software Engineering .
en226 | SAME | en208 | 1.00 | · . - Widyasari, R., Zhang, T., Bouraffa, A., Maalej, W., & Lo, D.
en227 | SAME | en209 | 1.00 | Explaining Explanations: An Empirical Study of Explanations in Code Reviews .
en228 | SAME | en210 | 1.00 | ACM Transactions on Software Engineering and Methodology , 34(6), Article 177.
en229 | SAME | en211 | 1.00 | · . - Papotti, A., Paramitha, R., & Massacci, F.
en230 | SAME | en212 | 1.00 | On the acceptance by code reviewers of candidate security patches suggested by Automated Program Repair tools .
en231 | SAME | en213 | 1.00 | Empirical Software Engineering , 29, Article 132.
en232 | SAME | en214 | 1.00 | · . - Jin, H., & Chen, H.
en233 | SAME | en215 | 1.00 | Are LLMs Reliable Code Reviewers?
en234 | SAME | en216 | 1.00 | Systematic Overcorrection in Requirement Conformance Judgement .
en235 | SAME | en217 | 1.00 | · . - Ling, M., Zou, J., & Liu, X.
en236 | SAME | en218 | 1.00 | Negotiating Completion in Agentic Software Work: Acceptance Boundaries and Deferred Requirements .
en237 | SAME | en219 | 1.00 | 이 목록은 인용된 주요 자료를 확인할 수 있게 모은 집필용 서지이며, 서지형식·인용 위치·전수 대조를 마친 제출용 참고문헌은 아직 아니다.
en238 | SAME | en220 | 1.00 | / These are verified reading anchors, not yet a fully formatted submission bibliography.
Summary en: SAME 219, EDIT 1, NEW 18

## v20 · [Notion](https://app.notion.com/p/41fef561cf9281a7849bd8c8a6322130)
### ko (203 sentences)
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
ko033 | SAME | ko033 | 1.00 | · · 우리는 서로 다른 두 자료를 사용했다.
ko034 | SAME | ko034 | 1.00 | 벤치마크에서는 분류를 요구받은 모델에게 실제로 어떤 입력이 주어졌는지 조사했다.
ko035 | SAME | ko035 | 1.00 | 도서관 예제에서는 패치 한 개를 고정하고, 적용할 요구와 보호할 계약을 바꿔 가며 실행 결과와 승인 기준을 대조했다.
ko036 | SAME | ko036 | 1.00 | 벤치마크의 저장 코드와 도서관 코드는 별개이고, 어느 쪽에도 실제 검토자의 승인·거절 판단은 포함되지 않는다.
ko037 | SAME | ko037 | 1.00 | OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다.
ko038 | SAME | ko038 | 1.00 | 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다.
ko039 | SAME | ko039 | 1.00 | 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다.
ko040 | SAME | ko040 | 1.00 | 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다.
ko041 | SAME | ko041 | 1.00 | 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다.
ko042 | SAME | ko042 | 1.00 | 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.
ko043 | SAME | ko043 | 1.00 | 지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다.
ko044 | SAME | ko044 | 1.00 | 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다.
ko045 | SAME | ko045 | 1.00 | 이 판독은 제출 코드를 가린 지시문에 관한 것이다.
ko046 | SAME | ko046 | 1.00 | 독립 감사에서 Python 저장 행 192개를 이루는 고유 코드 12개를 검사하자 4개에서 주석 토큰 46개를 발견했고, docstring을 포함한 코드는 없었다.
ko047 | SAME | ko047 | 1.00 | 주석이 기능의 의도를 암시할 수 있으므로, 지시문에 개별 요구가 없다는 사실을 코드 전체에 명세 단서가 없다는 주장으로 확대하지 않았다.
ko048 | SAME | ko048 | 1.00 | 다른 세 언어의 주석은 같은 방법으로 계수하지 않았다.
ko049 | SAME | ko049 | 1.00 | 저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다.
ko050 | SAME | ko050 | 1.00 | Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다.
ko051 | SAME | ko051 | 1.00 | 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다.
ko052 | SAME | ko052 | 1.00 | 압축 파일 안의 코드 자체는 실행하지 않았다.
ko053 | SAME | ko053 | 1.00 | 도서관 예제에서는 원본 소스와 수정안, 호출 입력, 새 모듈을 추가할 수 있다는 편집 범위를 고정했다.
ko054 | SAME | ko054 | 1.00 | 코드 실행으로 확인한 것은 구체적인 입력에서 나온 출력과 예외다.
ko055 | SAME | ko055 | 1.00 | 반면 기술보고서·정오표 중 무엇을 요구하는지, 책 출력의 접두어가 보호 대상인지, 새 요구를 충족하면서 보호된 기존 동작을 보존해야 승인한다 는 기준은 모두 연구자가 정했다.
ko056 | SAME | ko056 | 1.00 | 따라서 §5의 표는 독립 심사위원의 판정이 아니라 우리가 지정한 기준을 실행 관찰에 적용한 결과다.
ko057 | SAME | ko057 | 1.00 | 일부 전제만 공개한 경우에는 두 요구와 두 계약으로 이루어진 후보 명세 중 공개된 사실과 맞는 것만 남겼다.
ko058 | SAME | ko058 | 1.00 | 이 후보군 밖의 실제 요구나 계약까지 조사했다고 가정하지 않는다.
ko059 | SAME | ko059 | 1.00 | · · · · Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21) Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko060 | SAME | ko060 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko061 | SAME | ko061 | 1.00 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko062 | SAME | ko062 | 1.00 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko063 | SAME | ko063 | 1.00 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko064 | SAME | ko064 | 1.00 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko065 | SAME | ko065 | 1.00 | 추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. gpt-4o-mini 와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다.
ko066 | SAME | ko066 | 1.00 | 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다.
ko067 | SAME | ko067 | 1.00 | 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.
ko068 | SAME | ko068 | 1.00 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko069 | SAME | ko069 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko070 | SAME | ko070 | 1.00 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko071 | SAME | ko071 | 1.00 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko072 | SAME | ko072 | 1.00 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko073 | SAME | ko073 | 1.00 | 저장 코드와 참조 쌍은 앞에서 명시한 문자열 정규화 기준에서 일치하지 않았으며, Python 코드에 한한 AST 비교에서도 일치 사례가 없었다.
ko074 | SAME | ko074 | 1.00 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko075 | SAME | ko075 | 1.00 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko076 | SAME | ko076 | 1.00 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko077 | SAME | ko077 | 1.00 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko078 | SAME | ko078 | 1.00 | · · · Bräuer 등(2018)은 설계 원칙을 어떻게 측정할지 전문가에게 물었고, Cabral 등(2024)은 SOLID를 적용한 코드를 이해하고 확장하는 경험을 조사했다.
ko079 | SAME | ko079 | 1.00 | Zhu 등(2026)은 구체적인 저장소 변경 과제에 기능 및 구조 검사를 결합했다.
ko080 | SAME | ko080 | 1.00 | 우리의 벤치마크 감사도 분류 성능을 부정하려는 것이 아니다.
ko081 | SAME | ko081 | 1.00 | 분류에 성공했다는 증거를 수정안 거절의 증거로 옮길 때 무엇이 더 필요한지를 묻는다.
ko082 | SAME | ko082 | 1.00 | · · 실제 리뷰 연구는 이 논문의 주장 범위를 더 엄격하게 제한한다.
ko083 | SAME | ko083 | 1.00 | Widyasari 등(2025)은 Gerrit 코드 리뷰 댓글 793건을 분석하고 규칙이나 원칙을 근거로 드는 설명 유형을 확인했다.
ko084 | SAME | ko084 | 1.00 | 이는 원칙에 의거한 설명이 리뷰에 존재한다는 증거지만, 원칙이 잘못 적용돼 특정 수정안이 거절됐다는 증거는 아니다.
ko085 | SAME | ko085 | 1.00 | Papotti 등(2024)은 컴퓨터과학 석사과정 학생 72명을 대상으로 보안 자동 수리 패치의 채택 여부를 실험했다.
ko086 | SAME | ko086 | 1.00 | 제안 도구의 전문성을 알리는 정보에 따라 판단이 바뀌는 현상을 관찰했지만, 원칙 위반 라벨을 대상으로 한 연구는 아니다.
ko087 | SAME | ko087 | 1.00 | 두 논문의 실제 사람에 대한 관측은 우리가 구성한 표 2의 승인 기준과 다르다.
ko088 | SAME | ko088 | 1.00 | · Jin과 Chen(2026)은 정답 코드와 결함 코드에 대한 다섯 언어 모델의 요구 적합성 판단을 세 프로그래밍 벤치마크에서 실험하고, 맞는 코드를 잘못 거절하는 현상과 설명·수정 제안을 요구하는 프롬프트의 위험을 보고했다.
ko089 | SAME | ko089 | 1.00 | 따라서 LLM의 과잉 거절을 처음 지적했다고 주장할 수 없다.
ko090 | SAME | ko090 | 1.00 | Ling·Zou·Liu(2026)는 공개 GitHub 변경 사례의 질적 연구에서 병합, 이슈 종료, 요구 충족이 서로 다른 결과일 수 있음을 논증했다.
ko091 | SAME | ko091 | 1.00 | 수용 경계가 조건부라는 발견도 우리의 최초성이 아니다.
ko092 | SAME | ko092 | 1.00 | 우리 사례는 실행 결과가 고정된 패치에서 현재 공개된 요구·계약이 정당화하는 판정과 추가 질문을 정확하게 분리하는 재현 가능한 실례 다.
ko093 | SAME | ko093 | 1.00 | · 그 질문 자체에도 중요한 선행연구가 있다.
ko094 | SAME | ko094 | 1.00 | Kane(2013)은 검사 점수의 해석을 뒷받침하는 증거가 그 점수를 특정 결정에 사용하는 일까지 정당화하지는 않는다고 논했다.
ko095 | SAME | ko095 | 1.00 | 이는 소프트웨어 리뷰를 실험한 결과가 아니라, 평가 결과의 사용 을 따로 정당화해야 한다는 일반적인 논증이다.
ko096 | SAME | ko096 | 1.00 | Zave와 Jackson(1997)은 요구사항, 기계 명세, 환경에 관한 지식이 어떻게 연결되는지 설명하면서 행위의 통제 주체를 구별했다.
ko097 | SAME | ko097 | 1.00 | 원을 앞에 정렬할 책임이 호출자에게 있는지 함수에 있는지부터 따져야 한다는 우리의 질문도 이러한 오래된 문제의 한 사례다.
ko098 | SAME | ko098 | 1.00 | 존스(1981) 역시 병렬 프로그램에서 환경 의존 조건과 프로그램 보장 조건의 양립을 다뤘다.
ko099 | SAME | ko099 | 1.00 | · · Barr 등(2015)이 정리한 테스트 오라클 문제는 코드 실행과 올바름 판정 사이에도 근거가 필요함을 상기시킨다.
ko100 | SAME | ko100 | 1.00 | §5의 시험은 지정된 호출의 동작을 확인하지만, 그 동작을 보존하겠다는 실제 프로젝트의 약속을 입증하지는 않는다.
ko101 | SAME | ko101 | 1.00 | 따라서 다음 절의 요구·계약은 발견한 사실이 아니라 명시적으로 정한 전제다.
ko102 | SAME | ko102 | 1.00 | 위반 범주를 맞혔다는 사실은 코드에 특정 구조가 있다는 평가를 뒷받침한다.
ko103 | SAME | ko103 | 1.00 | 그러나 수정안을 거절하려면 (1) 누구에게서 나온 새 요구인지, (2) 기존 호출자에게 계속 보장하기로 한 동작이 무엇인지, (3) 그 동작과 새 기능을 어느 호출 경로로 제공해야 하는지까지 알아야 한다.
ko104 | SAME | ko104 | 1.00 | 이 가운데 일부는 소스에 표시될 수 있지만, 관측한 구현이 곧 승인된 계약이라는 뜻은 아니다.
ko105 | SAME | ko105 | 1.00 | 예컨대 같은 출력 변경을 보고도 책 출력이 보호 대상일 때와 아닐 때는 서로 다른 판정이 가능하다.
ko106 | SAME | ko106 | 1.00 | 분류 라벨을 고정한 채 판정이 달라지는 반례는 §5에서 실행한 동일 패치의 네 명세에 한정된다.
ko107 | SAME | ko107 | 1.00 | 이를 통해 분류 점수 자체를 부정하거나 실제 리뷰어가 라벨 때문에 패치를 거절했다고 주장하지 않는다.
ko108 | SAME | ko108 | 1.00 | 이 주장은 분류기에 어떤 정보를 주는지에 따라서도 달라진다.
ko109 | SAME | ko109 | 1.00 | 소스 코드만 보고 OCP 위반 여부를 판정하는 분류기라면 코드가 고정된 네 명세에서 입력과 출력 라벨을 동일하게 유지한다.
ko110 | SAME | ko110 | 1.00 | 반면 실제 요구서와 호출자 계약을 입력받는 문맥 의존적 평가자는 명세에 따라 판단을 변경할 수 있다.
ko111 | SAME | ko111 | 1.00 | 따라서 이 논문의 반례는 모든 OCP 평가가 언제나 같은 라벨을 낸다는 주장이 아니라, 고정된 소스의 위반 라벨만으로 서로 다른 실제 유지보수 판정을 식별할 수 없다는 제한된 주장 이다.
ko112 | SAME | ko112 | 1.00 | 기존 요구사항 추적표나 호환성 검토 역시 추가 근거를 물어 문제를 해결할 수 있으므로, 이를 우리의 새 방법만이 수행한다고 해석하지 않는다.
ko113 | NEW | ko142 | 0.04 | 직접 작성하지 않은 사례에서도 요구와 동작을 분리할 수 있는지 살피기 위해 Go 웹 라우터 Chi의 공개 이슈 (2025년 5월 2일)를 그 후속 댓글과 함께 읽었다.
ko114 | NEW | ko005 | 0.01 | 작성자는 미들웨어 생성 함수가 같은 싱글턴 핸들러를 반환하면 중첩 라우터 그룹의 요청이 마지막 그룹에 전달되는 상황을 신고했다.
ko115 | NEW | ko022 | 0.02 | 다른 참여자는 생성 함수 호출마다 새 미들웨어 인스턴스를 반환하는 우회 코드를 제시했고, 원래 작성자는 그 방법을 이해한다고 답했다.
ko116 | NEW | ko101 | 0.04 | 그러나 작성자는 싱글턴을 그대로 써도 정상적인 라우팅이 되거나, 잘못된 재사용을 명시적으로 알려 주는 동작을 원한다는 점을 다시 밝혔다.
ko117 | NEW | ko123 | 0.08 | 따라서 새 인스턴스를 만들어 기존 세 경로에서 정답 응답이 나왔다는 사실이 확인되더라도, 그것을 싱글턴을 안전하게 지원해 달라는 원래 요청이 해결됐다는 증거로 바꿀 수는 없다.
ko118 | NEW | ko161 | 0.05 | 이 관찰은 Paper B에서 말하는 요구의 권위를 더 구체적으로 만든다.
ko119 | NEW | ko132 | 0.04 | 이슈의 기대 동작 , 참여자가 제안한 우회 수정 , 연구자가 선택한 테스트 통과 조건 은 서로 다른 자료다.
ko120 | NEW | ko170 | 0.07 | 원래 작성자가 제안된 우회를 알고 있다는 사실만으로 라이브러리 관리자가 API 계약 변경을 승인했다고 볼 수도 없다.
ko121 | NEW | ko173 | 0.11 | 반대로 이 이슈는 OCP 위반 분류가 실제 리뷰에서 잘못된 패치 거절을 일으켰다는 사례가 아니다.
ko122 | NEW | ko150 | 0.04 | 연구자가 이미 알려진 문제를 선택해 조사했으므로 독립적 전향 실험도 아니다.
ko123 | NEW | ko042 | 0.02 | · 또 다른 공개 이슈 에서는 작성자가 최초에 정규식 경로의 하위 경로 처리를 문제 삼았지만, 같은 날 후속 댓글에서 독립적인 재현 결과 그 부분은 문제가 아니었다고 정정했다.
ko124 | NEW | ko050 | 0.02 | 정적 경로와 매개변수 경로의 메서드 처리에 관한 나머지 문제와, 스스로 철회한 정규식 주장을 같은 수준의 확정 사실로 분류해서는 안 된다.
ko125 | NEW | ko170 | 0.05 | 이러한 출처 이력은 분류자가 읽는 코드만으로는 알 수 없는 정보이며, 이 논문이 제안하는 근거 확인 절차를 적용할 때 반드시 남겨야 하는 반대 사례다.
ko126 | SAME | ko113 | 1.00 | 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko127 | SAME | ko114 | 1.00 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko128 | SAME | ko115 | 1.00 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko129 | SAME | ko116 | 1.00 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko130 | SAME | ko117 | 1.00 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko131 | SAME | ko118 | 1.00 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko132 | SAME | ko119 | 1.00 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko133 | SAME | ko120 | 1.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko134 | SAME | ko121 | 1.00 | 책 접두어가 보호 대상이 아니라는 가정은 실제 이용자가 그 출력을 기대하지 않는다는 관찰이 아니다.
ko135 | SAME | ko122 | 1.00 | 단지 이 비교에서 보존 의무로 정하지 않았다는 뜻이다.
ko136 | SAME | ko123 | 1.00 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko137 | SAME | ko124 | 1.00 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko138 | SAME | ko125 | 1.00 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko139 | SAME | ko126 | 1.00 | 이 절차는 실제 명세가 표의 네 경우 중 하나라는 조건 아래서만 성립한다.
ko140 | SAME | ko127 | 1.00 | 공개된 사실과 맞는 행이 하나도 없다면 승인이나 거절을 내릴 것이 아니라 자료 또는 후보군이 잘못됐는지 확인해야 한다.
ko141 | SAME | ko128 | 1.00 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko142 | SAME | ko129 | 1.00 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko143 | SAME | ko130 | 1.00 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko144 | SAME | ko131 | 1.00 | 정오표 지원이 필수인지 여부를 $E$, 기존 책 출력 접두어를 보호하는지 여부를 $B$라고 두자.
ko145 | SAME | ko132 | 1.00 | 연구자가 정한 네 명세에 한정하면, 이 고정 패치의 승인 조건은 $A(E,B)=\neg E\land\neg B$다.
ko146 | SAME | ko133 | 1.00 | 따라서 승인에 필요한 최소 증거는 $\{\neg E,\neg B\}$이며, 거절을 확정하는 최소 증거는 $\{E\}$ 또는 $\{B\}$다.
ko147 | SAME | ko134 | 1.00 | 두 조건을 모두 알 수 없다면, 승인 명세 $(E=0,B=0)$와 거절 명세 $(E=1,B=0)$가 양립하므로 판정을 보류한다.
ko148 | SAME | ko135 | 1.00 | 기술보고서만 요구한다는 사실, 즉 $\neg E$가 확인되면 $B$를 물어 어느 쪽인지 결정할 수 있다.
ko149 | SAME | ko136 | 1.00 | 반면 두 조건이 전부 미공개일 때는 하나의 예·아니오 질문만으로 모든 답변에 대해 판정을 확정하지 못한다.
ko150 | SAME | ko137 | 1.00 | 이것은 새로운 논리 규칙이 아니라 고전적인 유한 정보 집합 판정이다.
ko151 | SAME | ko138 | 1.00 | 별도 Python 코드는 네 명세의 공개 상태 아홉 가지, 최소 승인·거절 증거, 보류 상태의 대립 명세, 모순된 사실의 처리까지 검사했고 가 통과했다.
ko152 | SAME | ko139 | 1.00 | 이 테스트가 실제 검토자의 판단이나 원본 도서관 프로그램의 전체 동작을 재검증한 것은 아니다.
ko153 | SAME | ko140 | 1.00 | 또한 고정된 계약에 관한 사실을 알게 되는 것 과 계약 자체를 변경하는 것 을 구별해야 한다.
ko154 | SAME | ko141 | 1.00 | 앞의 경우에는 가능한 명세의 집합이 줄지만, 뒤의 경우에는 승인 조건 자체가 달라질 수 있다.
ko155 | SAME | ko142 | 1.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko156 | SAME | ko143 | 1.00 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko157 | SAME | ko144 | 1.00 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko158 | SAME | ko145 | 1.00 | 이 비교에서 얻은 것은 새로운 논리 규칙이 아니다.
ko159 | SAME | ko146 | 1.00 | 한 사실만 알아도 거절이 확정되는 경우와, 책 출력 약속을 물어야 하는 경우를 구체적인 호출 결과로 구분한 것이다.
ko160 | SAME | ko147 | 1.00 | 실제 리뷰에 적용하려면 요구서와 API 문서, 테스트 및 호출 기록에서 그 약속의 근거를 따로 찾아야 한다.
ko161 | SAME | ko148 | 1.00 | · 계약 조건을 하나 더 추가했을 때의 민감도.
ko162 | SAME | ko149 | 1.00 | 위의 승인 규칙은 두 조건만 관련된다는 전제에 의존한다.
ko163 | SAME | ko150 | 1.00 | 이 고정 패치가 다른 독립적인 보호 의무도 위반한다고 연구자가 가정하고, 그 의무가 현재 실제로 적용되는지를 $C$라고 두자.
ko164 | SAME | ko151 | 1.00 | 세 의무 가운데 하나라도 적용되면 패치를 거절하도록 승인 기준을 새로 정하면 $A_3(E,B,C)=\neg E\land\neg B\land\neg C$가 된다.
ko165 | SAME | ko152 | 1.00 | 이때 네 명세는 여덟 가지 완전 명세로, 아홉 공개 상태는 스물일곱 공개 상태로 확장된다.
ko166 | SAME | ko153 | 1.00 | 전수 계산 결과는 승인 1개, 거절 19개, 보류 7개다.
ko167 | SAME | ko154 | 1.00 | 특히 예전 두 조건이 모두 거짓이라고 알더라도 $C$가 미공개라면 기존의 승인은 보류 로 바뀐다.
ko168 | SAME | ko155 | 1.00 | 반대로 $C$가 적용되지 않는다고 명시적으로 확인하면 원래의 아홉 상태와 승인 1·거절 5·보류 3 분포가 복원된다.
ko169 | SAME | ko156 | 1.00 | 이 계산은 실제로 새로운 보안·성능 결함을 발견했다는 뜻이 아니다.
ko170 | SAME | ko157 | 1.00 | $C$는 연구자가 만든 제삼의 독립 의무이고, 새 기준은 기존 승인 기준보다 엄격하다.
ko171 | SAME | ko158 | 1.00 | 그 목적은 필요한 요구를 전부 열거했다는 근거 없이 기존의 승인 판정을 일반화할 수 없음 을 드러내는 것이다.
ko172 | SAME | ko159 | 1.00 | 그렇다고 실제 검토자가 가능한 모든 요구를 무한히 조사해야 하는 것도 아니다.
ko173 | SAME | ko160 | 1.00 | 어떤 요구가 승인 기준에 포함되는지는 적격한 주체와 계약 출처에 의해 제한돼야 한다.
ko174 | SAME | ko161 | 1.00 | [전수 계산 코드](./paper_b_three_obligation_sensitivity.py) · [회귀 테스트](./test_paper_b_three_obligation_sensitivity.py).
ko175 | SAME | ko162 | 1.00 | 완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다.
ko176 | SAME | ko163 | 1.00 | 여기서는 앞의 질문에 해당하는 관찰만 남긴다.
ko177 | SAME | ko164 | 1.00 | 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 bracketed=True 를 넘기면 인자를 거절했다.
ko178 | SAME | ko165 | 1.00 | 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다.
ko179 | SAME | ko166 | 1.00 | 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.
ko180 | SAME | ko167 | 1.00 | 새 기능이 있다는 사실과 요구된 호출 경로에서 쓸 수 있다는 사실 은 다르다.
ko181 | SAME | ko168 | 1.00 | 보호해야 할 기존 진입점이 무엇인지 확인하지 않으면, 같은 옵션을 새 함수에서 제공했다는 사실만으로 수정안의 적합성을 판정할 수 없다.
ko182 | SAME | ko169 | 1.00 | 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 Paper B 통합 원고 12 · 한·영 문장 교정 및 에 원형 그대로 보존했다.
ko183 | SAME | ko170 | 1.00 | 마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다.
ko184 | SAME | ko171 | 1.00 | 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다.
ko185 | SAME | ko172 | 1.00 | 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다.
ko186 | SAME | ko173 | 1.00 | 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다.
ko187 | SAME | ko174 | 1.00 | 원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가 가 이 논문에서 다룬 질문이다.
ko188 | SAME | ko175 | 1.00 | 실제 검토에서 먼저 확인할 것은 수정안의 새 기능만이 아니라, 요구한 사람이나 합의된 문서가 그 기능을 어느 진입점에서 제공하도록 정했는지다.
ko189 | SAME | ko176 | 1.00 | 그다음 기존 호출자가 의존하는 동작 중 무엇이 보호 대상인지 요구서·API 문서·테스트·호출 코드에서 근거를 찾아야 한다.
ko190 | SAME | ko177 | 1.00 | 이 근거가 둘 이상의 가능한 계약을 남긴다면, 원칙 위반이라는 이름으로 결론을 확정하기보다 계약의 출처와 범위를 묻는 편이 정확하다.
ko191 | SAME | ko178 | 1.00 | 반대로 새로운 요구를 충족하지 못한다는 사실이 이미 확정됐다면, 어떤 기존 계약이 추가로 보호되는지 모두 조사하기 전에 해당 수정안을 거절할 수도 있다.
ko192 | SAME | ko179 | 1.00 | 이러한 질문의 순서는 이 논문의 구성 사례에서 나온 실무적 제안이지, 실제 개발 조직의 효율이 개선됐다는 관측 결과는 아니다.
ko193 | SAME | ko180 | 1.00 | 공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다.
ko194 | SAME | ko181 | 1.00 | 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다.
ko195 | EDIT | ko182 | 0.49 | 이 연구는 한 벤치마크의 저장 입력, 연구자가 구성한 실행 예제와 추가 의무에 관한 논리적 민감도 분석, 그리고 연구자가 후향적으로 선정한 두 외부 이슈의 텍스트 근거만을 다뤘다.
ko196 | SAME | ko183 | 1.00 | 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.
ko197 | SAME | ko184 | 1.00 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko198 | SAME | ko185 | 1.00 | 독립 감사 스크립트는 같은 ZIP을 실행 코드가 아닌 자료로 읽어 16개 JSONL 파일, 768행, 48개 고유 코드, 24개 틀, 64개 세부 집단을 재계산했고, Python 고유 코드 12개 중 주석이 있는 4개를 확인했다.
ko199 | SAME | ko186 | 1.00 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko200 | SAME | ko187 | 1.00 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko201 | EDIT | ko188 | 0.83 | 12판에 있던 그림 1과 파일 배치 실험은 20판 본문에 싣지 않았으며, 원본 그림과 실행 기록을 12판에 보존했다.
ko202 | SAME | ko189 | 1.00 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko203 | SAME | ko190 | 1.00 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
Summary ko: SAME 188, EDIT 2, NEW 13

### en (251 sentences)
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
en040 | SAME | en040 | 1.00 | · · We used two distinct sources of evidence.
en041 | SAME | en041 | 1.00 | We audited the saved benchmark inputs to determine what a classifier was actually asked to judge.
en042 | SAME | en042 | 1.00 | Separately, we fixed one catalog patch and varied the demands and protected caller commitments against which its execution was assessed.
en043 | SAME | en043 | 1.00 | The benchmark submissions are not instances of the catalog patch, and neither source records decisions by real reviewers.
en044 | SAME | en044 | 1.00 | The OCP reference material contains 48 before-and-after code pairs.
en045 | SAME | en045 | 1.00 | Sixteen saved JSONL files each contain 48 records, yielding 768 rows.
en046 | SAME | en046 | 1.00 | Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times.
en047 | SAME | en047 | 1.00 | We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality.
en048 | SAME | en048 | 1.00 | The result was 24 scaffolds.
en049 | SAME | en049 | 1.00 | Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs.
en050 | SAME | en050 | 1.00 | The 768 records are repeated submissions, not independent maintenance cases.
en051 | SAME | en051 | 1.00 | We separately read the masked instructions for case-specific change requests and protected caller commitments.
en052 | SAME | en052 | 1.00 | An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape.
en053 | SAME | en053 | 1.00 | We inspected the text outside the submitted code, not the whole semantic context.
en054 | SAME | en054 | 1.00 | In a separate replication, the 192 saved Python rows reduced to twelve distinct code submissions; four contained a total of 46 comment tokens, and none had an AST-detected docstring.
en055 | SAME | en055 | 1.00 | These comments may convey implementation intent, but counting them does not establish a contract.
en056 | SAME | en056 | 1.00 | We did not perform the same comment-token audit for the other three languages.
en057 | SAME | en057 | 1.00 | We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace.
en058 | SAME | en058 | 1.00 | For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions.
en059 | SAME | en059 | 1.00 | These tests do not establish whether inherited methods remain available or whether callers were promised a behavior.
en060 | SAME | en060 | 1.00 | We read code as archive data and did not execute it.
en061 | SAME | en061 | 1.00 | For the catalog, we fixed the baseline, candidate patch, calls and permission to add a module.
en062 | SAME | en062 | 1.00 | Executing the code established outputs and exceptions for those calls.
en063 | SAME | en063 | 1.00 | The possible demands (technical reports alone, or technical reports and errata), the two scopes of the book-output obligation, and the rule that an acceptable patch must meet its demand and preserve protected behavior we
en064 | SAME | en064 | 1.00 | Table 2 therefore applies authored criteria to observed behavior; it does not report independent human decisions.
en065 | SAME | en065 | 1.00 | For partial disclosure, we retained only the candidate specifications compatible with known facts.
en066 | SAME | en066 | 1.00 | We did not attempt to enumerate obligations outside these four constructed cases.
en067 | SAME | en067 | 1.00 | · · · Pehlivan et al. chose violation scenarios and refined the generated examples.
en068 | SAME | en068 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en069 | SAME | en069 | 1.00 | The benchmark compares model classifications with the resulting labels.
en070 | SAME | en070 | 1.00 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en071 | SAME | en071 | 1.00 | No two strategies shared a template string.
en072 | SAME | en072 | 1.00 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en073 | SAME | en073 | 1.00 | An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: gpt-4o-mini differed from the other three models.
en074 | SAME | en074 | 1.00 | Holding model, strategy and language fixed left one scaffold shared across twelve programs.
en075 | SAME | en075 | 1.00 | No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST.
en076 | SAME | en076 | 1.00 | These checks do not establish semantic independence or source lineage.
en077 | SAME | en077 | 1.00 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en078 | SAME | en078 | 1.00 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en079 | SAME | en079 | 1.00 | If a new shape is needed, that branch is a place to look.
en080 | SAME | en080 | 1.00 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en081 | SAME | en081 | 1.00 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en082 | SAME | en082 | 1.00 | No submitted program matched a reference side under the reported textual normalizations, and the separate Python-only AST comparison also found no match.
en083 | SAME | en083 | 1.00 | Pair 37 establishes that a declaration was removed.
en084 | SAME | en084 | 1.00 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en085 | SAME | en085 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en086 | SAME | en086 | 1.00 | The prompt example is in JSONL line 13 (record ID 12).
en087 | SAME | en087 | 1.00 | Pair 37 is in a separate reference JSON file.
en088 | SAME | en088 | 1.00 | · · · Bräuer et al. (2018) examined the measurement of design principles with experts; Cabral et al. (2024) studied understanding and extension under a bundled SOLID treatment; Zhu et al. (2026) supplied repository chang
en089 | SAME | en089 | 1.00 | These evaluate different objects.
en090 | SAME | en090 | 1.00 | Our audit does not contest the benchmark's classification task.
en091 | SAME | en091 | 1.00 | It asks what else would be needed to use such a classification as a reason to reject a patch.
en092 | SAME | en092 | 1.00 | · · Empirical review studies narrow the claim further.
en093 | SAME | en093 | 1.00 | Widyasari et al. (2025) coded 793 Gerrit review comments and identified explanation categories including appeals to rules or principles.
en094 | SAME | en094 | 1.00 | This shows that principle-based explanations appear in review practice; it does not show that such principles caused an unjustified patch rejection.
en095 | SAME | en095 | 1.00 | Papotti et al. (2024) experimentally studied 72 computer-science master's students deciding whether to adopt security patches proposed by automatic program repair tools, and found that information about the purported too
en096 | SAME | en096 | 1.00 | Unlike our stipulated Table 2 judgments, those were observed human choices.
en097 | SAME | en097 | 1.00 | · Jin and Chen (2026) tested five language models' judgments of canonical and buggy implementations against natural-language specifications across three programming benchmarks.
en098 | SAME | en098 | 1.00 | They reported false rejection of correct code and risks from prompts that demand explanations or fixes.
en099 | SAME | en099 | 1.00 | We cannot claim to have discovered LLM over-rejection or to improve its error rate: our archive does not record independent patch-acceptance judgments by those models.
en100 | SAME | en100 | 1.00 | Ling, Zou, and Liu (2026) examined public agent-associated contributions and distinguished merges, issue closures, and requirement satisfaction.
en101 | SAME | en101 | 1.00 | Conditional acceptance is not first discovered by this paper either.
en102 | SAME | en102 | 1.00 | Our narrower addition is to hold a patch's execution fixed and make explicit which partially disclosed requirement and contract facts warrant a verdict and which warrant further inquiry .
en103 | SAME | en103 | 1.00 | · This is not a new problem in general.
en104 | SAME | en104 | 1.00 | Kane (2013) argues that evidence supporting an interpretation of test scores does not automatically justify using those scores for a particular decision.
en105 | SAME | en105 | 1.00 | His work does not test software reviews; it establishes the importance of justifying an assessment's use .
en106 | SAME | en106 | 1.00 | Zave and Jackson (1997) distinguish requirements, machine specifications and knowledge of the environment, including which actor controls an action.
en107 | SAME | en107 | 1.00 | Whether sorting belongs to a caller or a drawing function is an instance of that longstanding question.
en108 | SAME | en108 | 1.00 | Jones (1981) likewise developed conditions for compatible environmental reliance and program guarantees in parallel programs.
en109 | SAME | en109 | 1.00 | We do not claim these distinctions as our invention.
en110 | SAME | en110 | 1.00 | · · Barr et al.'s (2015) survey of the test-oracle problem makes a related point about our executable fixture.
en111 | SAME | en111 | 1.00 | Tests establish outputs for chosen inputs; they do not, without an independently grounded oracle, establish which outputs a real project has promised to preserve.
en112 | SAME | en112 | 1.00 | Thus the demands and contracts in Section 5 are explicit assumptions rather than requirements recovered from a repository.
en113 | SAME | en113 | 1.00 | From a classification to a patch disposition.
en114 | SAME | en114 | 1.00 | Correctly naming a design-principle violation supports a judgment about a structural feature of code.
en115 | SAME | en115 | 1.00 | Rejecting a specific patch requires different grounds: (i) the source and scope of the new request, (ii) the behavior the project committed to existing callers, and (iii) the call path through which the request and those
en116 | SAME | en116 | 1.00 | Some clues may reside in source, but observed behavior is not automatically an authorized compatibility promise.
en117 | SAME | en117 | 1.00 | The same change in book output can be unacceptable under one declared contract and acceptable under another.
en118 | SAME | en118 | 1.00 | Section 5 supplies a fixed-patch, four-specification witness to that gap.
en119 | SAME | en119 | 1.00 | It does not disprove the benchmark's classification scores or establish that a real reviewer rejected a patch because of an OCP label.
en120 | SAME | en120 | 1.00 | The inference also depends on what information the classifier receives.
en121 | SAME | en121 | 1.00 | A source-only OCP classifier has the same input, and hence the same classification output, across our four fixed-code specifications.
en122 | SAME | en122 | 1.00 | A context-sensitive evaluator given authentic requests and caller contracts may rightly return different assessments.
en123 | SAME | en123 | 1.00 | Our witness therefore does not say that all OCP evaluations are constant across contexts.
en124 | SAME | en124 | 1.00 | It shows only that a label based solely on fixed code cannot identify which distinct maintenance decision binds under unspecified obligations .
en125 | SAME | en125 | 1.00 | Ordinary requirements traceability and compatibility checklists can ask for these same missing facts; we claim no exclusive ability to do so.
en126 | NEW | en136 | 0.10 | Reading contract authority from an external issue.
en127 | NEW | en080 | 0.13 | To check whether the distinction between a request and a test result survives outside our authored fixture, we inspected (May 2, 2025) and its subsequent discussion.
en128 | NEW | en141 | 0.13 | The reporter described nested router groups in which a middleware factory returning one mutable singleton handler sent requests to the final registered group.
en129 | NEW | en107 | 0.10 | Another participant proposed returning a fresh middleware instance on every factory invocation.
en130 | NEW | en164 | 0.11 | The reporter acknowledged knowing this workaround but reiterated the requested library-level behavior: correct routing with the singleton, or an explicit error on invalid reuse.
en131 | NEW | en183 | 0.21 | Successful responses from an implementation that abandons singleton reuse therefore do not, by themselves, establish satisfaction of the original API request.
en132 | NEW | en063 | 0.16 | Three evidence roles must stay separate: the reporter's requested behavior , the proposed application-level workaround , and a researcher's test oracle .
en133 | NEW | en194 | 0.13 | The reporter's acknowledgment of the workaround is not evidence of maintainer authorization of a new API contract.
en134 | NEW | en094 | 0.33 | Nor does the issue show that an OCP label caused an unjustified patch rejection.
en135 | NEW | en194 | 0.10 | We selected this historic issue after inspecting candidate sources, so it is an exploratory, nonblind example, not a prospective F38 cohort.
en136 | NEW | en203 | 0.14 | · The author of later corrected an initial complaint about regex handling on nested paths, stating that the regex problem did not reproduce in isolation.
en137 | NEW | en098 | 0.12 | This correction should not be mixed with the separate remaining report about method handling between static and parameterized routes.
en138 | NEW | en176 | 0.14 | Source chronology and author revisions are part of the evidence needed for a legitimate maintenance judgment, not extra facts inferable from a source-only design label.
en139 | SAME | en126 | 1.00 | We built a small catalog based on Meyer’s example.
en140 | SAME | en127 | 1.00 | The client in client.py displays each publication through the catalog function passed to it.
en141 | SAME | en128 | 1.00 | The patch adds reports.py to wrap that function.
en142 | SAME | en129 | 1.00 | The source of catalog.py and client.py stays identical.
en143 | SAME | en130 | 1.00 | The resulting catalog displays technical reports and still rejects errata.
en144 | SAME | en131 | 1.00 | For books it now prints BOOK where it used to print book .
en145 | SAME | en132 | 1.00 | Suppose the only new requirement is to handle technical reports.
en146 | SAME | en133 | 1.00 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en147 | SAME | en134 | 1.00 | If the book output is outside the contract, the same patch can be accepted.
en148 | SAME | en135 | 1.00 | Table 2 applies both contracts again when errata are also required.
en149 | SAME | en136 | 1.00 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en150 | SAME | en137 | 1.00 | Excluding the book prefix from our stipulated contract is not evidence that real users have no expectation about it; it only means this example does not impose that obligation.
en151 | SAME | en138 | 1.00 | Two requirements for accepting a fixed patch.
en152 | SAME | en139 | 1.00 | Learning that errata are required leaves the last two rows of Table 2.
en153 | SAME | en140 | 1.00 | Both reject the patch, so the book contract need not be settled first.
en154 | SAME | en141 | 1.00 | Learning that technical reports are the whole request leaves the first two rows.
en155 | SAME | en142 | 1.00 | One accepts and one rejects.
en156 | SAME | en143 | 1.00 | The next question is whether the original book output is protected.
en157 | SAME | en144 | 1.00 | The procedure applies only if the actual specification is among these four authored cases.
en158 | SAME | en145 | 1.00 | If disclosure rules out every row, an empty candidate set is a reason to question the evidence or the candidate set, not to infer acceptance or rejection.
en159 | SAME | en146 | 1.00 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en160 | SAME | en147 | 1.00 | The reviewer can give a conditional answer or defer judgment.
en161 | SAME | en148 | 1.00 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en162 | SAME | en149 | 1.00 | Minimum evidence for a decision.
en163 | SAME | en150 | 1.00 | Let $E$ indicate that errata support is required and $B$ that the previous book prefix is protected.
en164 | SAME | en151 | 1.00 | Within the four stipulated specifications, the acceptance predicate is $A(E,B)=\neg E\land\neg B$.
en165 | SAME | en152 | 1.00 | Its unique inclusion-minimal acceptance certificate is $\{\neg E,\neg B\}$; the two separate minimal rejection certificates are $\{E\}$ and $\{B\}$.
en166 | SAME | en153 | 1.00 | With both facts withheld, an accepting specification $(E=0,B=0)$ and a rejecting specification $(E=1,B=0)$ remain compatible, so deferral has explicit countermodels.
en167 | SAME | en154 | 1.00 | After confirming reports-only ($\neg E$), asking whether the book prefix is protected determines the verdict.
en168 | SAME | en155 | 1.00 | With both fields initially unknown, neither one binary question guarantees a verdict for every possible answer.
en169 | SAME | en156 | 1.00 | These are classical finite Boolean and version-space facts, not new inference rules.
en170 | SAME | en157 | 1.00 | A separate Python replay checked the four worlds, nine disclosure states, inclusion-minimal certificates, contradictory evidence, and pairs of opposite-verdict worlds for deferred states; its passed.
en171 | SAME | en158 | 1.00 | That verifies the bounded decision logic, not actual human decisions or complete source behavior.
en172 | SAME | en159 | 1.00 | Learning more about a fixed contract removes possible worlds; renegotiating that contract changes the legitimate obligation.
en173 | SAME | en160 | 1.00 | The two transitions must not be conflated.
en174 | SAME | en161 | 1.00 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en175 | SAME | en162 | 1.00 | It adds one module, handles technical reports and errata, and keeps the original book output.
en176 | SAME | en163 | 1.00 | A rejection in Table 2 need not end the search for a patch within that boundary.
en177 | SAME | en164 | 1.00 | The contribution is not a new logical rule: it is a concrete account of why knowing that errata are required settles this decision, whereas a reports-only demand leaves the book-output commitment to be checked.
en178 | SAME | en165 | 1.00 | Applying it to a real review would require finding that commitment in a request, API documentation, tests or caller records.
en179 | SAME | en166 | 1.00 | · Sensitivity to an additional binding obligation.
en180 | SAME | en167 | 1.00 | The preceding approval depends on assuming that the two listed facts exhaust the criteria that matter.
en181 | SAME | en168 | 1.00 | Suppose, as another author-stipulated condition, that this same patch would violate a separate obligation if it were binding; let $C$ indicate whether that third obligation applies.
en182 | SAME | en169 | 1.00 | Under the stricter criterion $A_3(E,B,C)=\neg E\land\neg B\land\neg C$, the universe has eight complete specifications and twenty-seven partial disclosure states.
en183 | SAME | en170 | 1.00 | Exhaustive evaluation yields one ACCEPT, nineteen REJECT and seven DEFER states.
en184 | SAME | en171 | 1.00 | Crucially, evidence that both $E$ and $B$ are false no longer suffices to approve while $C$ remains unknown: the previous ACCEPT becomes DEFER.
en185 | SAME | en172 | 1.00 | If $C$ is explicitly false, the prior nine-state table and its one/five/three distribution are recovered.
en186 | SAME | en173 | 1.00 | This is not an empirically observed safety or performance defect.
en187 | SAME | en174 | 1.00 | The third obligation and stronger criterion were authored for sensitivity analysis.
en188 | SAME | en175 | 1.00 | The point is narrower: one cannot generalize an approval from the original four-world set without evidence that the listed obligations exhaust the relevant acceptance conditions.
en189 | SAME | en176 | 1.00 | Reviewers are not thereby required to investigate arbitrary imaginable obligations; a binding requirement still needs a legitimate source and scope.
en190 | SAME | en177 | 1.00 | [Enumeration code](./paper_b_three_obligation_sensitivity.py) · [regression tests](./test_paper_b_three_obligation_sensitivity.py).
en191 | SAME | en178 | 1.00 | Deciding whether to accept a completed patch differs from choosing an architecture for future edits.
en192 | SAME | en179 | 1.00 | We retain one observation relevant to acceptance.
en193 | SAME | en180 | 1.00 | In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected bracketed=True .
en194 | SAME | en181 | 1.00 | A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.
en195 | SAME | en182 | 1.00 | The presence of a feature is different from its availability along a required route .
en196 | SAME | en183 | 1.00 | Unless the original entry point and its compatibility obligations are identified, implementation through a separate function cannot by itself establish that the requested behavior is available to existing callers.
en197 | SAME | en184 | 1.00 | The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in Paper B 통합 원고 12 · 한·영 문장 교정 and its .
en198 | SAME | en185 | 1.00 | Drawing a square first establishes what a routine does, not whether it must be edited.
en199 | SAME | en186 | 1.00 | That depends on whether sorting belongs to the routine's obligations.
en200 | SAME | en187 | 1.00 | In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required.
en201 | SAME | en188 | 1.00 | We did not observe a real OCP label being misused to reject a patch.
en202 | SAME | en189 | 1.00 | We asked what additional grounds a design-principle assessment needs before it can justify an engineering decision .
en203 | SAME | en190 | 1.00 | A practical review should first ask not only whether the patch implements a feature but where the request or an authorized agreement requires that feature to be reachable.
en204 | SAME | en191 | 1.00 | The reviewer should then locate the source of each protected old-client obligation in requests, API documentation, tests and actual call paths, without automatically treating every observed response as a promise.
en205 | SAME | en192 | 1.00 | If those sources leave different legitimate contracts possible, asking who can settle the obligation is more defensible than turning an OCP label into a categorical rejection.
en206 | SAME | en193 | 1.00 | Conversely, a demonstrated failure to meet an already binding new demand may reject the fixed patch before every other old-client promise is resolved.
en207 | SAME | en194 | 1.00 | This sequence is a recommendation derived from our authored example, not evidence that it reduces actual review costs in an organization.
en208 | SAME | en195 | 1.00 | Keeping the specifications compatible with known facts and checking their verdicts is elementary logic.
en209 | SAME | en196 | 1.00 | The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository.
en210 | EDIT | en197 | 0.70 | Our evidence is confined to one benchmark archive, authored executable examples, an authored logical sensitivity check, and two post hoc selected external issue threads.
en211 | SAME | en198 | 1.00 | We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.
en212 | SAME | en199 | 1.00 | The audits in Sections 3–4 read the archived JSON and JSONL as data.
en213 | SAME | en200 | 1.00 | A separate script reproduced sixteen JSONL files, 768 rows, 48 distinct submissions, 24 scaffolds and 64 fixed model–strategy–language groups, and counted Python comments in four of twelve unique submissions.
en214 | SAME | en201 | 1.00 | Section 5 and the call-path check in Section 6 use examples written for this study.
en215 | EDIT | en202 | 0.94 | The shape-layout experiment and Figure 1 remain preserved in manuscript 12; manuscript 20 does not reframe them as a new measured maintenance-cost trial.
en216 | SAME | en203 | 1.00 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en217 | SAME | en204 | 1.00 | The table below gives the nine verdicts for Section 5.
en218 | SAME | en205 | 1.00 | Both values of a withheld field remain possible.
en219 | SAME | en206 | 1.00 | Defer means that the compatible rows include both acceptance and rejection. - Meyer, B.
en220 | SAME | en207 | 1.00 | Object-Oriented Software Construction (1st ed.), pp.
en221 | SAME | en208 | 1.00 | The Open–Closed Principle . . - Jones, C.
en222 | SAME | en209 | 1.00 | Development Methods for Computer Programs Including a Notion of Interference .
en223 | SAME | en210 | 1.00 | Oxford University Computing Laboratory, PRG-25.
en224 | SAME | en211 | 1.00 | · . - Pehlivan, F., Ergüzen, A.
en225 | SAME | en212 | 1.00 | M., Lami, M., & Koyuncu, A.
en226 | SAME | en213 | 1.00 | An Empirical Study on Prompting LLMs to Detect Design Principle Violations .
en227 | SAME | en214 | 1.00 | ASE 2025 NIER. . - Bräuer et al.
en228 | SAME | en215 | 1.00 | Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research . . - Cabral et al.
en229 | SAME | en216 | 1.00 | Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding . . - Zhu, H., Zhang, Q., Wang, J., Yang, Z., & Qiu, Y.
en230 | SAME | en217 | 1.00 | Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits . . - Kane, M.
en231 | SAME | en218 | 1.00 | Validating the Interpretations and Uses of Test Scores .
en232 | SAME | en219 | 1.00 | Journal of Educational Measurement , 50(1), 1–73.
en233 | SAME | en220 | 1.00 | · . - Zave, P., & Jackson, M.
en234 | SAME | en221 | 1.00 | Four Dark Corners of Requirements Engineering .
en235 | SAME | en222 | 1.00 | ACM Transactions on Software Engineering and Methodology , 6(1), 1–30.
en236 | SAME | en223 | 1.00 | T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S.
en237 | SAME | en224 | 1.00 | The Oracle Problem in Software Testing: A Survey .
en238 | SAME | en225 | 1.00 | IEEE Transactions on Software Engineering .
en239 | SAME | en226 | 1.00 | · . - Widyasari, R., Zhang, T., Bouraffa, A., Maalej, W., & Lo, D.
en240 | SAME | en227 | 1.00 | Explaining Explanations: An Empirical Study of Explanations in Code Reviews .
en241 | SAME | en228 | 1.00 | ACM Transactions on Software Engineering and Methodology , 34(6), Article 177.
en242 | SAME | en229 | 1.00 | · . - Papotti, A., Paramitha, R., & Massacci, F.
en243 | SAME | en230 | 1.00 | On the acceptance by code reviewers of candidate security patches suggested by Automated Program Repair tools .
en244 | SAME | en231 | 1.00 | Empirical Software Engineering , 29, Article 132.
en245 | SAME | en232 | 1.00 | · . - Jin, H., & Chen, H.
en246 | SAME | en233 | 1.00 | Are LLMs Reliable Code Reviewers?
en247 | SAME | en234 | 1.00 | Systematic Overcorrection in Requirement Conformance Judgement .
en248 | SAME | en235 | 1.00 | · . - Ling, M., Zou, J., & Liu, X.
en249 | SAME | en236 | 1.00 | Negotiating Completion in Agentic Software Work: Acceptance Boundaries and Deferred Requirements .
en250 | SAME | en237 | 1.00 | 이 목록은 인용된 주요 자료를 확인할 수 있게 모은 집필용 서지이며, 서지형식·인용 위치·전수 대조를 마친 제출용 참고문헌은 아직 아니다.
en251 | SAME | en238 | 1.00 | / These are verified reading anchors, not yet a fully formatted submission bibliography.
Summary en: SAME 236, EDIT 2, NEW 13

## v21 · [Notion](https://app.notion.com/p/41fef561cf9281629eafc9e45223b58b)
### ko (217 sentences)
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
ko033 | SAME | ko033 | 1.00 | · · 우리는 서로 다른 두 자료를 사용했다.
ko034 | SAME | ko034 | 1.00 | 벤치마크에서는 분류를 요구받은 모델에게 실제로 어떤 입력이 주어졌는지 조사했다.
ko035 | SAME | ko035 | 1.00 | 도서관 예제에서는 패치 한 개를 고정하고, 적용할 요구와 보호할 계약을 바꿔 가며 실행 결과와 승인 기준을 대조했다.
ko036 | SAME | ko036 | 1.00 | 벤치마크의 저장 코드와 도서관 코드는 별개이고, 어느 쪽에도 실제 검토자의 승인·거절 판단은 포함되지 않는다.
ko037 | SAME | ko037 | 1.00 | OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다.
ko038 | SAME | ko038 | 1.00 | 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다.
ko039 | SAME | ko039 | 1.00 | 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다.
ko040 | SAME | ko040 | 1.00 | 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다.
ko041 | SAME | ko041 | 1.00 | 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다.
ko042 | SAME | ko042 | 1.00 | 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.
ko043 | SAME | ko043 | 1.00 | 지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다.
ko044 | SAME | ko044 | 1.00 | 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다.
ko045 | SAME | ko045 | 1.00 | 이 판독은 제출 코드를 가린 지시문에 관한 것이다.
ko046 | SAME | ko046 | 1.00 | 독립 감사에서 Python 저장 행 192개를 이루는 고유 코드 12개를 검사하자 4개에서 주석 토큰 46개를 발견했고, docstring을 포함한 코드는 없었다.
ko047 | SAME | ko047 | 1.00 | 주석이 기능의 의도를 암시할 수 있으므로, 지시문에 개별 요구가 없다는 사실을 코드 전체에 명세 단서가 없다는 주장으로 확대하지 않았다.
ko048 | SAME | ko048 | 1.00 | 다른 세 언어의 주석은 같은 방법으로 계수하지 않았다.
ko049 | SAME | ko049 | 1.00 | 저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다.
ko050 | SAME | ko050 | 1.00 | Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다.
ko051 | SAME | ko051 | 1.00 | 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다.
ko052 | SAME | ko052 | 1.00 | 압축 파일 안의 코드 자체는 실행하지 않았다.
ko053 | SAME | ko053 | 1.00 | 도서관 예제에서는 원본 소스와 수정안, 호출 입력, 새 모듈을 추가할 수 있다는 편집 범위를 고정했다.
ko054 | SAME | ko054 | 1.00 | 코드 실행으로 확인한 것은 구체적인 입력에서 나온 출력과 예외다.
ko055 | SAME | ko055 | 1.00 | 반면 기술보고서·정오표 중 무엇을 요구하는지, 책 출력의 접두어가 보호 대상인지, 새 요구를 충족하면서 보호된 기존 동작을 보존해야 승인한다 는 기준은 모두 연구자가 정했다.
ko056 | SAME | ko056 | 1.00 | 따라서 §5의 표는 독립 심사위원의 판정이 아니라 우리가 지정한 기준을 실행 관찰에 적용한 결과다.
ko057 | SAME | ko057 | 1.00 | 일부 전제만 공개한 경우에는 두 요구와 두 계약으로 이루어진 후보 명세 중 공개된 사실과 맞는 것만 남겼다.
ko058 | SAME | ko058 | 1.00 | 이 후보군 밖의 실제 요구나 계약까지 조사했다고 가정하지 않는다.
ko059 | SAME | ko059 | 1.00 | · · · · Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21) Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko060 | SAME | ko060 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko061 | SAME | ko061 | 1.00 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko062 | SAME | ko062 | 1.00 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko063 | SAME | ko063 | 1.00 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko064 | SAME | ko064 | 1.00 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko065 | SAME | ko065 | 1.00 | 추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. gpt-4o-mini 와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다.
ko066 | SAME | ko066 | 1.00 | 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다.
ko067 | SAME | ko067 | 1.00 | 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.
ko068 | SAME | ko068 | 1.00 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko069 | SAME | ko069 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko070 | SAME | ko070 | 1.00 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko071 | SAME | ko071 | 1.00 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko072 | SAME | ko072 | 1.00 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko073 | SAME | ko073 | 1.00 | 저장 코드와 참조 쌍은 앞에서 명시한 문자열 정규화 기준에서 일치하지 않았으며, Python 코드에 한한 AST 비교에서도 일치 사례가 없었다.
ko074 | SAME | ko074 | 1.00 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko075 | SAME | ko075 | 1.00 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko076 | SAME | ko076 | 1.00 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko077 | SAME | ko077 | 1.00 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko078 | SAME | ko078 | 1.00 | · · · Bräuer 등(2018)은 설계 원칙을 어떻게 측정할지 전문가에게 물었고, Cabral 등(2024)은 SOLID를 적용한 코드를 이해하고 확장하는 경험을 조사했다.
ko079 | SAME | ko079 | 1.00 | Zhu 등(2026)은 구체적인 저장소 변경 과제에 기능 및 구조 검사를 결합했다.
ko080 | SAME | ko080 | 1.00 | 우리의 벤치마크 감사도 분류 성능을 부정하려는 것이 아니다.
ko081 | SAME | ko081 | 1.00 | 분류에 성공했다는 증거를 수정안 거절의 증거로 옮길 때 무엇이 더 필요한지를 묻는다.
ko082 | SAME | ko082 | 1.00 | · · 실제 리뷰 연구는 이 논문의 주장 범위를 더 엄격하게 제한한다.
ko083 | SAME | ko083 | 1.00 | Widyasari 등(2025)은 Gerrit 코드 리뷰 댓글 793건을 분석하고 규칙이나 원칙을 근거로 드는 설명 유형을 확인했다.
ko084 | SAME | ko084 | 1.00 | 이는 원칙에 의거한 설명이 리뷰에 존재한다는 증거지만, 원칙이 잘못 적용돼 특정 수정안이 거절됐다는 증거는 아니다.
ko085 | SAME | ko085 | 1.00 | Papotti 등(2024)은 컴퓨터과학 석사과정 학생 72명을 대상으로 보안 자동 수리 패치의 채택 여부를 실험했다.
ko086 | SAME | ko086 | 1.00 | 제안 도구의 전문성을 알리는 정보에 따라 판단이 바뀌는 현상을 관찰했지만, 원칙 위반 라벨을 대상으로 한 연구는 아니다.
ko087 | SAME | ko087 | 1.00 | 두 논문의 실제 사람에 대한 관측은 우리가 구성한 표 2의 승인 기준과 다르다.
ko088 | SAME | ko088 | 1.00 | · Jin과 Chen(2026)은 정답 코드와 결함 코드에 대한 다섯 언어 모델의 요구 적합성 판단을 세 프로그래밍 벤치마크에서 실험하고, 맞는 코드를 잘못 거절하는 현상과 설명·수정 제안을 요구하는 프롬프트의 위험을 보고했다.
ko089 | SAME | ko089 | 1.00 | 따라서 LLM의 과잉 거절을 처음 지적했다고 주장할 수 없다.
ko090 | SAME | ko090 | 1.00 | Ling·Zou·Liu(2026)는 공개 GitHub 변경 사례의 질적 연구에서 병합, 이슈 종료, 요구 충족이 서로 다른 결과일 수 있음을 논증했다.
ko091 | SAME | ko091 | 1.00 | 수용 경계가 조건부라는 발견도 우리의 최초성이 아니다.
ko092 | SAME | ko092 | 1.00 | 우리 사례는 실행 결과가 고정된 패치에서 현재 공개된 요구·계약이 정당화하는 판정과 추가 질문을 정확하게 분리하는 재현 가능한 실례 다.
ko093 | SAME | ko093 | 1.00 | · 그 질문 자체에도 중요한 선행연구가 있다.
ko094 | SAME | ko094 | 1.00 | Kane(2013)은 검사 점수의 해석을 뒷받침하는 증거가 그 점수를 특정 결정에 사용하는 일까지 정당화하지는 않는다고 논했다.
ko095 | SAME | ko095 | 1.00 | 이는 소프트웨어 리뷰를 실험한 결과가 아니라, 평가 결과의 사용 을 따로 정당화해야 한다는 일반적인 논증이다.
ko096 | SAME | ko096 | 1.00 | Zave와 Jackson(1997)은 요구사항, 기계 명세, 환경에 관한 지식이 어떻게 연결되는지 설명하면서 행위의 통제 주체를 구별했다.
ko097 | SAME | ko097 | 1.00 | 원을 앞에 정렬할 책임이 호출자에게 있는지 함수에 있는지부터 따져야 한다는 우리의 질문도 이러한 오래된 문제의 한 사례다.
ko098 | SAME | ko098 | 1.00 | 존스(1981) 역시 병렬 프로그램에서 환경 의존 조건과 프로그램 보장 조건의 양립을 다뤘다.
ko099 | SAME | ko099 | 1.00 | · · Barr 등(2015)이 정리한 테스트 오라클 문제는 코드 실행과 올바름 판정 사이에도 근거가 필요함을 상기시킨다.
ko100 | SAME | ko100 | 1.00 | §5의 시험은 지정된 호출의 동작을 확인하지만, 그 동작을 보존하겠다는 실제 프로젝트의 약속을 입증하지는 않는다.
ko101 | SAME | ko101 | 1.00 | 따라서 다음 절의 요구·계약은 발견한 사실이 아니라 명시적으로 정한 전제다.
ko102 | SAME | ko102 | 1.00 | 위반 범주를 맞혔다는 사실은 코드에 특정 구조가 있다는 평가를 뒷받침한다.
ko103 | SAME | ko103 | 1.00 | 그러나 수정안을 거절하려면 (1) 누구에게서 나온 새 요구인지, (2) 기존 호출자에게 계속 보장하기로 한 동작이 무엇인지, (3) 그 동작과 새 기능을 어느 호출 경로로 제공해야 하는지까지 알아야 한다.
ko104 | SAME | ko104 | 1.00 | 이 가운데 일부는 소스에 표시될 수 있지만, 관측한 구현이 곧 승인된 계약이라는 뜻은 아니다.
ko105 | SAME | ko105 | 1.00 | 예컨대 같은 출력 변경을 보고도 책 출력이 보호 대상일 때와 아닐 때는 서로 다른 판정이 가능하다.
ko106 | SAME | ko106 | 1.00 | 분류 라벨을 고정한 채 판정이 달라지는 반례는 §5에서 실행한 동일 패치의 네 명세에 한정된다.
ko107 | SAME | ko107 | 1.00 | 이를 통해 분류 점수 자체를 부정하거나 실제 리뷰어가 라벨 때문에 패치를 거절했다고 주장하지 않는다.
ko108 | SAME | ko108 | 1.00 | 이 주장은 분류기에 어떤 정보를 주는지에 따라서도 달라진다.
ko109 | SAME | ko109 | 1.00 | 소스 코드만 보고 OCP 위반 여부를 판정하는 분류기라면 코드가 고정된 네 명세에서 입력과 출력 라벨을 동일하게 유지한다.
ko110 | SAME | ko110 | 1.00 | 반면 실제 요구서와 호출자 계약을 입력받는 문맥 의존적 평가자는 명세에 따라 판단을 변경할 수 있다.
ko111 | SAME | ko111 | 1.00 | 따라서 이 논문의 반례는 모든 OCP 평가가 언제나 같은 라벨을 낸다는 주장이 아니라, 고정된 소스의 위반 라벨만으로 서로 다른 실제 유지보수 판정을 식별할 수 없다는 제한된 주장 이다.
ko112 | SAME | ko112 | 1.00 | 기존 요구사항 추적표나 호환성 검토 역시 추가 근거를 물어 문제를 해결할 수 있으므로, 이를 우리의 새 방법만이 수행한다고 해석하지 않는다.
ko113 | SAME | ko113 | 1.00 | 직접 작성하지 않은 사례에서도 요구와 동작을 분리할 수 있는지 살피기 위해 Go 웹 라우터 Chi의 공개 이슈 (2025년 5월 2일)를 그 후속 댓글과 함께 읽었다.
ko114 | SAME | ko114 | 1.00 | 작성자는 미들웨어 생성 함수가 같은 싱글턴 핸들러를 반환하면 중첩 라우터 그룹의 요청이 마지막 그룹에 전달되는 상황을 신고했다.
ko115 | SAME | ko115 | 1.00 | 다른 참여자는 생성 함수 호출마다 새 미들웨어 인스턴스를 반환하는 우회 코드를 제시했고, 원래 작성자는 그 방법을 이해한다고 답했다.
ko116 | SAME | ko116 | 1.00 | 그러나 작성자는 싱글턴을 그대로 써도 정상적인 라우팅이 되거나, 잘못된 재사용을 명시적으로 알려 주는 동작을 원한다는 점을 다시 밝혔다.
ko117 | SAME | ko117 | 1.00 | 따라서 새 인스턴스를 만들어 기존 세 경로에서 정답 응답이 나왔다는 사실이 확인되더라도, 그것을 싱글턴을 안전하게 지원해 달라는 원래 요청이 해결됐다는 증거로 바꿀 수는 없다.
ko118 | SAME | ko118 | 1.00 | 이 관찰은 Paper B에서 말하는 요구의 권위를 더 구체적으로 만든다.
ko119 | SAME | ko119 | 1.00 | 이슈의 기대 동작 , 참여자가 제안한 우회 수정 , 연구자가 선택한 테스트 통과 조건 은 서로 다른 자료다.
ko120 | SAME | ko120 | 1.00 | 원래 작성자가 제안된 우회를 알고 있다는 사실만으로 라이브러리 관리자가 API 계약 변경을 승인했다고 볼 수도 없다.
ko121 | SAME | ko121 | 1.00 | 반대로 이 이슈는 OCP 위반 분류가 실제 리뷰에서 잘못된 패치 거절을 일으켰다는 사례가 아니다.
ko122 | SAME | ko122 | 1.00 | 연구자가 이미 알려진 문제를 선택해 조사했으므로 독립적 전향 실험도 아니다.
ko123 | SAME | ko123 | 1.00 | · 또 다른 공개 이슈 에서는 작성자가 최초에 정규식 경로의 하위 경로 처리를 문제 삼았지만, 같은 날 후속 댓글에서 독립적인 재현 결과 그 부분은 문제가 아니었다고 정정했다.
ko124 | SAME | ko124 | 1.00 | 정적 경로와 매개변수 경로의 메서드 처리에 관한 나머지 문제와, 스스로 철회한 정규식 주장을 같은 수준의 확정 사실로 분류해서는 안 된다.
ko125 | SAME | ko125 | 1.00 | 이러한 출처 이력은 분류자가 읽는 코드만으로는 알 수 없는 정보이며, 이 논문이 제안하는 근거 확인 절차를 적용할 때 반드시 남겨야 하는 반대 사례다.
ko126 | SAME | ko126 | 1.00 | 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko127 | SAME | ko127 | 1.00 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko128 | SAME | ko128 | 1.00 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko129 | SAME | ko129 | 1.00 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko130 | SAME | ko130 | 1.00 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko131 | SAME | ko131 | 1.00 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko132 | SAME | ko132 | 1.00 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko133 | SAME | ko133 | 1.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko134 | SAME | ko134 | 1.00 | 책 접두어가 보호 대상이 아니라는 가정은 실제 이용자가 그 출력을 기대하지 않는다는 관찰이 아니다.
ko135 | SAME | ko135 | 1.00 | 단지 이 비교에서 보존 의무로 정하지 않았다는 뜻이다.
ko136 | SAME | ko136 | 1.00 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko137 | SAME | ko137 | 1.00 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko138 | SAME | ko138 | 1.00 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko139 | SAME | ko139 | 1.00 | 이 절차는 실제 명세가 표의 네 경우 중 하나라는 조건 아래서만 성립한다.
ko140 | SAME | ko140 | 1.00 | 공개된 사실과 맞는 행이 하나도 없다면 승인이나 거절을 내릴 것이 아니라 자료 또는 후보군이 잘못됐는지 확인해야 한다.
ko141 | SAME | ko141 | 1.00 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko142 | SAME | ko142 | 1.00 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko143 | SAME | ko143 | 1.00 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko144 | SAME | ko144 | 1.00 | 정오표 지원이 필수인지 여부를 $E$, 기존 책 출력 접두어를 보호하는지 여부를 $B$라고 두자.
ko145 | SAME | ko145 | 1.00 | 연구자가 정한 네 명세에 한정하면, 이 고정 패치의 승인 조건은 $A(E,B)=\neg E\land\neg B$다.
ko146 | SAME | ko146 | 1.00 | 따라서 승인에 필요한 최소 증거는 $\{\neg E,\neg B\}$이며, 거절을 확정하는 최소 증거는 $\{E\}$ 또는 $\{B\}$다.
ko147 | SAME | ko147 | 1.00 | 두 조건을 모두 알 수 없다면, 승인 명세 $(E=0,B=0)$와 거절 명세 $(E=1,B=0)$가 양립하므로 판정을 보류한다.
ko148 | SAME | ko148 | 1.00 | 기술보고서만 요구한다는 사실, 즉 $\neg E$가 확인되면 $B$를 물어 어느 쪽인지 결정할 수 있다.
ko149 | SAME | ko149 | 1.00 | 반면 두 조건이 전부 미공개일 때는 하나의 예·아니오 질문만으로 모든 답변에 대해 판정을 확정하지 못한다.
ko150 | SAME | ko150 | 1.00 | 이것은 새로운 논리 규칙이 아니라 고전적인 유한 정보 집합 판정이다.
ko151 | SAME | ko151 | 1.00 | 별도 Python 코드는 네 명세의 공개 상태 아홉 가지, 최소 승인·거절 증거, 보류 상태의 대립 명세, 모순된 사실의 처리까지 검사했고 가 통과했다.
ko152 | SAME | ko152 | 1.00 | 이 테스트가 실제 검토자의 판단이나 원본 도서관 프로그램의 전체 동작을 재검증한 것은 아니다.
ko153 | SAME | ko153 | 1.00 | 또한 고정된 계약에 관한 사실을 알게 되는 것 과 계약 자체를 변경하는 것 을 구별해야 한다.
ko154 | SAME | ko154 | 1.00 | 앞의 경우에는 가능한 명세의 집합이 줄지만, 뒤의 경우에는 승인 조건 자체가 달라질 수 있다.
ko155 | SAME | ko155 | 1.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko156 | SAME | ko156 | 1.00 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko157 | SAME | ko157 | 1.00 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko158 | SAME | ko158 | 1.00 | 이 비교에서 얻은 것은 새로운 논리 규칙이 아니다.
ko159 | SAME | ko159 | 1.00 | 한 사실만 알아도 거절이 확정되는 경우와, 책 출력 약속을 물어야 하는 경우를 구체적인 호출 결과로 구분한 것이다.
ko160 | SAME | ko160 | 1.00 | 실제 리뷰에 적용하려면 요구서와 API 문서, 테스트 및 호출 기록에서 그 약속의 근거를 따로 찾아야 한다.
ko161 | SAME | ko161 | 1.00 | · 계약 조건을 하나 더 추가했을 때의 민감도.
ko162 | SAME | ko162 | 1.00 | 위의 승인 규칙은 두 조건만 관련된다는 전제에 의존한다.
ko163 | SAME | ko163 | 1.00 | 이 고정 패치가 다른 독립적인 보호 의무도 위반한다고 연구자가 가정하고, 그 의무가 현재 실제로 적용되는지를 $C$라고 두자.
ko164 | SAME | ko164 | 1.00 | 세 의무 가운데 하나라도 적용되면 패치를 거절하도록 승인 기준을 새로 정하면 $A_3(E,B,C)=\neg E\land\neg B\land\neg C$가 된다.
ko165 | SAME | ko165 | 1.00 | 이때 네 명세는 여덟 가지 완전 명세로, 아홉 공개 상태는 스물일곱 공개 상태로 확장된다.
ko166 | SAME | ko166 | 1.00 | 전수 계산 결과는 승인 1개, 거절 19개, 보류 7개다.
ko167 | SAME | ko167 | 1.00 | 특히 예전 두 조건이 모두 거짓이라고 알더라도 $C$가 미공개라면 기존의 승인은 보류 로 바뀐다.
ko168 | SAME | ko168 | 1.00 | 반대로 $C$가 적용되지 않는다고 명시적으로 확인하면 원래의 아홉 상태와 승인 1·거절 5·보류 3 분포가 복원된다.
ko169 | SAME | ko169 | 1.00 | 이 계산은 실제로 새로운 보안·성능 결함을 발견했다는 뜻이 아니다.
ko170 | SAME | ko170 | 1.00 | $C$는 연구자가 만든 제삼의 독립 의무이고, 새 기준은 기존 승인 기준보다 엄격하다.
ko171 | SAME | ko171 | 1.00 | 그 목적은 필요한 요구를 전부 열거했다는 근거 없이 기존의 승인 판정을 일반화할 수 없음 을 드러내는 것이다.
ko172 | SAME | ko172 | 1.00 | 그렇다고 실제 검토자가 가능한 모든 요구를 무한히 조사해야 하는 것도 아니다.
ko173 | SAME | ko173 | 1.00 | 어떤 요구가 승인 기준에 포함되는지는 적격한 주체와 계약 출처에 의해 제한돼야 한다.
ko174 | SAME | ko174 | 1.00 | [전수 계산 코드](./paper_b_three_obligation_sensitivity.py) · [회귀 테스트](./test_paper_b_three_obligation_sensitivity.py).
ko175 | SAME | ko175 | 1.00 | 완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다.
ko176 | SAME | ko176 | 1.00 | 여기서는 앞의 질문에 해당하는 관찰만 남긴다.
ko177 | SAME | ko177 | 1.00 | 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 bracketed=True 를 넘기면 인자를 거절했다.
ko178 | SAME | ko178 | 1.00 | 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다.
ko179 | SAME | ko179 | 1.00 | 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.
ko180 | SAME | ko180 | 1.00 | 새 기능이 있다는 사실과 요구된 호출 경로에서 쓸 수 있다는 사실 은 다르다.
ko181 | SAME | ko181 | 1.00 | 보호해야 할 기존 진입점이 무엇인지 확인하지 않으면, 같은 옵션을 새 함수에서 제공했다는 사실만으로 수정안의 적합성을 판정할 수 없다.
ko182 | SAME | ko182 | 1.00 | 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 Paper B 통합 원고 12 · 한·영 문장 교정 및 에 원형 그대로 보존했다.
ko183 | NEW | ko092 | 0.03 | AI가 코드의 구조를 분류하고 문제를 설명하는 일이 일반화될수록, 개발자가 받는 조언은 명료해질 수 있지만 분류 결과가 어떤 구체적 행동을 정당화하는지는 별도 문제로 남는다.
ko184 | NEW | ko127 | 0.03 | 우리는 이 간극을 \*\*원칙→수정안 판단의 전이 문제(principle-to-patch transport problem)\*\*라고 부르자고 제안한다.
ko185 | NEW | ko135 | 0.06 | 이 표현은 기존 요구공학·계약 이론·검증 이론에서 비슷한 문제를 다루지 않았다는 선언이 아니다.
ko186 | NEW | ko036 | 0.05 | 원칙 위반 분류의 정확도, 그 분류를 받은 개발자의 실제 승인·거절 판단, 해당 판단에 대한 요구·계약의 승인 근거를 서로 다른 평가 대상으로 놓자 는 연구 제안이다.
ko187 | NEW | ko121 | 0.06 | 원칙이 특정 프로젝트에서 보호해야 하는 변경 축을 정확히 가리킨다면, 구조적 경고가 실제 리뷰에서 중요한 단서가 될 수 있기 때문이다.
ko188 | NEW | ko009 | 0.03 | 문제는 원칙을 폐기할 것인지가 아니라, 그 단서에 어느 범위의 결론 권한을 부여할 것인지다.
ko189 | SAME | ko183 | 1.00 | 마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다.
ko190 | SAME | ko184 | 1.00 | 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다.
ko191 | SAME | ko185 | 1.00 | 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다.
ko192 | SAME | ko186 | 1.00 | 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다.
ko193 | SAME | ko187 | 1.00 | 원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가 가 이 논문에서 다룬 질문이다.
ko194 | NEW | — | 0.00 | 후속 연구를 위한 네 가지 반증 가능 질문.
ko195 | NEW | ko100 | 0.06 | 첫째, 코드와 원칙 라벨만 받은 검토자는 요구서·API 계약을 함께 받은 검토자보다 실제 프로젝트의 승인 기준을 더 자주 잘못 적용하는가?
ko196 | NEW | ko083 | 0.03 | 둘째, 원칙을 언급하는 코드 리뷰가 실제로 명세나 호출자 의무를 인용하는 비율은 어느 정도이며, 그 인용의 유무가 판단과 상관되는가?
ko197 | NEW | ko181 | 0.06 | 셋째, 새 기능을 구현했지만 기존 진입점이 제공되지 않는 수정안은 실무자가 어떻게 평가하는가?
ko198 | NEW | ko178 | 0.05 | 넷째, 조건부 설계 지침이 보편적인 금지 규칙보다 새로운 요구에서 더 정확한 변경 영향 예측을 제공하는가?
ko199 | NEW | ko135 | 0.06 | 이 네 질문은 아직 측정하지 않은 제안이다.
ko200 | NEW | ko112 | 0.05 | 동등한 정보와 시간을 받은 일반 요구사항 추적 검토가 같은 결과를 낸다면, 새 방법의 실용적 우위는 기각하거나 좁혀야 한다.
ko201 | NEW | ko019 | 0.02 | 실제 기존 원칙들이 일부 조건에서 오히려 강한 예측력을 보인다면 그 경우도 연구 결과에 남겨야 한다.
ko202 | SAME | ko188 | 1.00 | 실제 검토에서 먼저 확인할 것은 수정안의 새 기능만이 아니라, 요구한 사람이나 합의된 문서가 그 기능을 어느 진입점에서 제공하도록 정했는지다.
ko203 | SAME | ko189 | 1.00 | 그다음 기존 호출자가 의존하는 동작 중 무엇이 보호 대상인지 요구서·API 문서·테스트·호출 코드에서 근거를 찾아야 한다.
ko204 | SAME | ko190 | 1.00 | 이 근거가 둘 이상의 가능한 계약을 남긴다면, 원칙 위반이라는 이름으로 결론을 확정하기보다 계약의 출처와 범위를 묻는 편이 정확하다.
ko205 | SAME | ko191 | 1.00 | 반대로 새로운 요구를 충족하지 못한다는 사실이 이미 확정됐다면, 어떤 기존 계약이 추가로 보호되는지 모두 조사하기 전에 해당 수정안을 거절할 수도 있다.
ko206 | SAME | ko192 | 1.00 | 이러한 질문의 순서는 이 논문의 구성 사례에서 나온 실무적 제안이지, 실제 개발 조직의 효율이 개선됐다는 관측 결과는 아니다.
ko207 | SAME | ko193 | 1.00 | 공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다.
ko208 | SAME | ko194 | 1.00 | 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다.
ko209 | SAME | ko195 | 1.00 | 이 연구는 한 벤치마크의 저장 입력, 연구자가 구성한 실행 예제와 추가 의무에 관한 논리적 민감도 분석, 그리고 연구자가 후향적으로 선정한 두 외부 이슈의 텍스트 근거만을 다뤘다.
ko210 | SAME | ko196 | 1.00 | 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.
ko211 | SAME | ko197 | 1.00 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko212 | SAME | ko198 | 1.00 | 독립 감사 스크립트는 같은 ZIP을 실행 코드가 아닌 자료로 읽어 16개 JSONL 파일, 768행, 48개 고유 코드, 24개 틀, 64개 세부 집단을 재계산했고, Python 고유 코드 12개 중 주석이 있는 4개를 확인했다.
ko213 | SAME | ko199 | 1.00 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko214 | SAME | ko200 | 1.00 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko215 | EDIT | ko201 | 0.87 | 12판에 있던 그림 1과 파일 배치 실험은 21판 본문에 싣지 않았으며, 원본 그림과 실행 기록을 12판에 보존했다.
ko216 | SAME | ko202 | 1.00 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko217 | SAME | ko203 | 1.00 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
Summary ko: SAME 202, EDIT 1, NEW 14

### en (277 sentences)
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
en040 | SAME | en040 | 1.00 | · · We used two distinct sources of evidence.
en041 | SAME | en041 | 1.00 | We audited the saved benchmark inputs to determine what a classifier was actually asked to judge.
en042 | SAME | en042 | 1.00 | Separately, we fixed one catalog patch and varied the demands and protected caller commitments against which its execution was assessed.
en043 | SAME | en043 | 1.00 | The benchmark submissions are not instances of the catalog patch, and neither source records decisions by real reviewers.
en044 | SAME | en044 | 1.00 | The OCP reference material contains 48 before-and-after code pairs.
en045 | SAME | en045 | 1.00 | Sixteen saved JSONL files each contain 48 records, yielding 768 rows.
en046 | SAME | en046 | 1.00 | Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times.
en047 | SAME | en047 | 1.00 | We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality.
en048 | SAME | en048 | 1.00 | The result was 24 scaffolds.
en049 | SAME | en049 | 1.00 | Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs.
en050 | SAME | en050 | 1.00 | The 768 records are repeated submissions, not independent maintenance cases.
en051 | SAME | en051 | 1.00 | We separately read the masked instructions for case-specific change requests and protected caller commitments.
en052 | SAME | en052 | 1.00 | An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape.
en053 | SAME | en053 | 1.00 | We inspected the text outside the submitted code, not the whole semantic context.
en054 | SAME | en054 | 1.00 | In a separate replication, the 192 saved Python rows reduced to twelve distinct code submissions; four contained a total of 46 comment tokens, and none had an AST-detected docstring.
en055 | SAME | en055 | 1.00 | These comments may convey implementation intent, but counting them does not establish a contract.
en056 | SAME | en056 | 1.00 | We did not perform the same comment-token audit for the other three languages.
en057 | SAME | en057 | 1.00 | We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace.
en058 | SAME | en058 | 1.00 | For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions.
en059 | SAME | en059 | 1.00 | These tests do not establish whether inherited methods remain available or whether callers were promised a behavior.
en060 | SAME | en060 | 1.00 | We read code as archive data and did not execute it.
en061 | SAME | en061 | 1.00 | For the catalog, we fixed the baseline, candidate patch, calls and permission to add a module.
en062 | SAME | en062 | 1.00 | Executing the code established outputs and exceptions for those calls.
en063 | SAME | en063 | 1.00 | The possible demands (technical reports alone, or technical reports and errata), the two scopes of the book-output obligation, and the rule that an acceptable patch must meet its demand and preserve protected behavior we
en064 | SAME | en064 | 1.00 | Table 2 therefore applies authored criteria to observed behavior; it does not report independent human decisions.
en065 | SAME | en065 | 1.00 | For partial disclosure, we retained only the candidate specifications compatible with known facts.
en066 | SAME | en066 | 1.00 | We did not attempt to enumerate obligations outside these four constructed cases.
en067 | SAME | en067 | 1.00 | · · · Pehlivan et al. chose violation scenarios and refined the generated examples.
en068 | SAME | en068 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en069 | SAME | en069 | 1.00 | The benchmark compares model classifications with the resulting labels.
en070 | SAME | en070 | 1.00 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en071 | SAME | en071 | 1.00 | No two strategies shared a template string.
en072 | SAME | en072 | 1.00 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en073 | SAME | en073 | 1.00 | An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: gpt-4o-mini differed from the other three models.
en074 | SAME | en074 | 1.00 | Holding model, strategy and language fixed left one scaffold shared across twelve programs.
en075 | SAME | en075 | 1.00 | No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST.
en076 | SAME | en076 | 1.00 | These checks do not establish semantic independence or source lineage.
en077 | SAME | en077 | 1.00 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en078 | SAME | en078 | 1.00 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en079 | SAME | en079 | 1.00 | If a new shape is needed, that branch is a place to look.
en080 | SAME | en080 | 1.00 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en081 | SAME | en081 | 1.00 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en082 | SAME | en082 | 1.00 | No submitted program matched a reference side under the reported textual normalizations, and the separate Python-only AST comparison also found no match.
en083 | SAME | en083 | 1.00 | Pair 37 establishes that a declaration was removed.
en084 | SAME | en084 | 1.00 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en085 | SAME | en085 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en086 | SAME | en086 | 1.00 | The prompt example is in JSONL line 13 (record ID 12).
en087 | SAME | en087 | 1.00 | Pair 37 is in a separate reference JSON file.
en088 | SAME | en088 | 1.00 | · · · Bräuer et al. (2018) examined the measurement of design principles with experts; Cabral et al. (2024) studied understanding and extension under a bundled SOLID treatment; Zhu et al. (2026) supplied repository chang
en089 | SAME | en089 | 1.00 | These evaluate different objects.
en090 | SAME | en090 | 1.00 | Our audit does not contest the benchmark's classification task.
en091 | SAME | en091 | 1.00 | It asks what else would be needed to use such a classification as a reason to reject a patch.
en092 | SAME | en092 | 1.00 | · · Empirical review studies narrow the claim further.
en093 | SAME | en093 | 1.00 | Widyasari et al. (2025) coded 793 Gerrit review comments and identified explanation categories including appeals to rules or principles.
en094 | SAME | en094 | 1.00 | This shows that principle-based explanations appear in review practice; it does not show that such principles caused an unjustified patch rejection.
en095 | SAME | en095 | 1.00 | Papotti et al. (2024) experimentally studied 72 computer-science master's students deciding whether to adopt security patches proposed by automatic program repair tools, and found that information about the purported too
en096 | SAME | en096 | 1.00 | Unlike our stipulated Table 2 judgments, those were observed human choices.
en097 | SAME | en097 | 1.00 | · Jin and Chen (2026) tested five language models' judgments of canonical and buggy implementations against natural-language specifications across three programming benchmarks.
en098 | SAME | en098 | 1.00 | They reported false rejection of correct code and risks from prompts that demand explanations or fixes.
en099 | SAME | en099 | 1.00 | We cannot claim to have discovered LLM over-rejection or to improve its error rate: our archive does not record independent patch-acceptance judgments by those models.
en100 | SAME | en100 | 1.00 | Ling, Zou, and Liu (2026) examined public agent-associated contributions and distinguished merges, issue closures, and requirement satisfaction.
en101 | SAME | en101 | 1.00 | Conditional acceptance is not first discovered by this paper either.
en102 | SAME | en102 | 1.00 | Our narrower addition is to hold a patch's execution fixed and make explicit which partially disclosed requirement and contract facts warrant a verdict and which warrant further inquiry .
en103 | SAME | en103 | 1.00 | · This is not a new problem in general.
en104 | SAME | en104 | 1.00 | Kane (2013) argues that evidence supporting an interpretation of test scores does not automatically justify using those scores for a particular decision.
en105 | SAME | en105 | 1.00 | His work does not test software reviews; it establishes the importance of justifying an assessment's use .
en106 | SAME | en106 | 1.00 | Zave and Jackson (1997) distinguish requirements, machine specifications and knowledge of the environment, including which actor controls an action.
en107 | SAME | en107 | 1.00 | Whether sorting belongs to a caller or a drawing function is an instance of that longstanding question.
en108 | SAME | en108 | 1.00 | Jones (1981) likewise developed conditions for compatible environmental reliance and program guarantees in parallel programs.
en109 | SAME | en109 | 1.00 | We do not claim these distinctions as our invention.
en110 | SAME | en110 | 1.00 | · · Barr et al.'s (2015) survey of the test-oracle problem makes a related point about our executable fixture.
en111 | SAME | en111 | 1.00 | Tests establish outputs for chosen inputs; they do not, without an independently grounded oracle, establish which outputs a real project has promised to preserve.
en112 | SAME | en112 | 1.00 | Thus the demands and contracts in Section 5 are explicit assumptions rather than requirements recovered from a repository.
en113 | SAME | en113 | 1.00 | From a classification to a patch disposition.
en114 | SAME | en114 | 1.00 | Correctly naming a design-principle violation supports a judgment about a structural feature of code.
en115 | SAME | en115 | 1.00 | Rejecting a specific patch requires different grounds: (i) the source and scope of the new request, (ii) the behavior the project committed to existing callers, and (iii) the call path through which the request and those
en116 | SAME | en116 | 1.00 | Some clues may reside in source, but observed behavior is not automatically an authorized compatibility promise.
en117 | SAME | en117 | 1.00 | The same change in book output can be unacceptable under one declared contract and acceptable under another.
en118 | SAME | en118 | 1.00 | Section 5 supplies a fixed-patch, four-specification witness to that gap.
en119 | SAME | en119 | 1.00 | It does not disprove the benchmark's classification scores or establish that a real reviewer rejected a patch because of an OCP label.
en120 | SAME | en120 | 1.00 | The inference also depends on what information the classifier receives.
en121 | SAME | en121 | 1.00 | A source-only OCP classifier has the same input, and hence the same classification output, across our four fixed-code specifications.
en122 | SAME | en122 | 1.00 | A context-sensitive evaluator given authentic requests and caller contracts may rightly return different assessments.
en123 | SAME | en123 | 1.00 | Our witness therefore does not say that all OCP evaluations are constant across contexts.
en124 | SAME | en124 | 1.00 | It shows only that a label based solely on fixed code cannot identify which distinct maintenance decision binds under unspecified obligations .
en125 | SAME | en125 | 1.00 | Ordinary requirements traceability and compatibility checklists can ask for these same missing facts; we claim no exclusive ability to do so.
en126 | SAME | en126 | 1.00 | Reading contract authority from an external issue.
en127 | SAME | en127 | 1.00 | To check whether the distinction between a request and a test result survives outside our authored fixture, we inspected (May 2, 2025) and its subsequent discussion.
en128 | SAME | en128 | 1.00 | The reporter described nested router groups in which a middleware factory returning one mutable singleton handler sent requests to the final registered group.
en129 | SAME | en129 | 1.00 | Another participant proposed returning a fresh middleware instance on every factory invocation.
en130 | SAME | en130 | 1.00 | The reporter acknowledged knowing this workaround but reiterated the requested library-level behavior: correct routing with the singleton, or an explicit error on invalid reuse.
en131 | SAME | en131 | 1.00 | Successful responses from an implementation that abandons singleton reuse therefore do not, by themselves, establish satisfaction of the original API request.
en132 | SAME | en132 | 1.00 | Three evidence roles must stay separate: the reporter's requested behavior , the proposed application-level workaround , and a researcher's test oracle .
en133 | SAME | en133 | 1.00 | The reporter's acknowledgment of the workaround is not evidence of maintainer authorization of a new API contract.
en134 | SAME | en134 | 1.00 | Nor does the issue show that an OCP label caused an unjustified patch rejection.
en135 | SAME | en135 | 1.00 | We selected this historic issue after inspecting candidate sources, so it is an exploratory, nonblind example, not a prospective F38 cohort.
en136 | SAME | en136 | 1.00 | · The author of later corrected an initial complaint about regex handling on nested paths, stating that the regex problem did not reproduce in isolation.
en137 | SAME | en137 | 1.00 | This correction should not be mixed with the separate remaining report about method handling between static and parameterized routes.
en138 | SAME | en138 | 1.00 | Source chronology and author revisions are part of the evidence needed for a legitimate maintenance judgment, not extra facts inferable from a source-only design label.
en139 | SAME | en139 | 1.00 | We built a small catalog based on Meyer’s example.
en140 | SAME | en140 | 1.00 | The client in client.py displays each publication through the catalog function passed to it.
en141 | SAME | en141 | 1.00 | The patch adds reports.py to wrap that function.
en142 | SAME | en142 | 1.00 | The source of catalog.py and client.py stays identical.
en143 | SAME | en143 | 1.00 | The resulting catalog displays technical reports and still rejects errata.
en144 | SAME | en144 | 1.00 | For books it now prints BOOK where it used to print book .
en145 | SAME | en145 | 1.00 | Suppose the only new requirement is to handle technical reports.
en146 | SAME | en146 | 1.00 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en147 | SAME | en147 | 1.00 | If the book output is outside the contract, the same patch can be accepted.
en148 | SAME | en148 | 1.00 | Table 2 applies both contracts again when errata are also required.
en149 | SAME | en149 | 1.00 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en150 | SAME | en150 | 1.00 | Excluding the book prefix from our stipulated contract is not evidence that real users have no expectation about it; it only means this example does not impose that obligation.
en151 | SAME | en151 | 1.00 | Two requirements for accepting a fixed patch.
en152 | SAME | en152 | 1.00 | Learning that errata are required leaves the last two rows of Table 2.
en153 | SAME | en153 | 1.00 | Both reject the patch, so the book contract need not be settled first.
en154 | SAME | en154 | 1.00 | Learning that technical reports are the whole request leaves the first two rows.
en155 | SAME | en155 | 1.00 | One accepts and one rejects.
en156 | SAME | en156 | 1.00 | The next question is whether the original book output is protected.
en157 | SAME | en157 | 1.00 | The procedure applies only if the actual specification is among these four authored cases.
en158 | SAME | en158 | 1.00 | If disclosure rules out every row, an empty candidate set is a reason to question the evidence or the candidate set, not to infer acceptance or rejection.
en159 | SAME | en159 | 1.00 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en160 | SAME | en160 | 1.00 | The reviewer can give a conditional answer or defer judgment.
en161 | SAME | en161 | 1.00 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en162 | SAME | en162 | 1.00 | Minimum evidence for a decision.
en163 | SAME | en163 | 1.00 | Let $E$ indicate that errata support is required and $B$ that the previous book prefix is protected.
en164 | SAME | en164 | 1.00 | Within the four stipulated specifications, the acceptance predicate is $A(E,B)=\neg E\land\neg B$.
en165 | SAME | en165 | 1.00 | Its unique inclusion-minimal acceptance certificate is $\{\neg E,\neg B\}$; the two separate minimal rejection certificates are $\{E\}$ and $\{B\}$.
en166 | SAME | en166 | 1.00 | With both facts withheld, an accepting specification $(E=0,B=0)$ and a rejecting specification $(E=1,B=0)$ remain compatible, so deferral has explicit countermodels.
en167 | SAME | en167 | 1.00 | After confirming reports-only ($\neg E$), asking whether the book prefix is protected determines the verdict.
en168 | SAME | en168 | 1.00 | With both fields initially unknown, neither one binary question guarantees a verdict for every possible answer.
en169 | SAME | en169 | 1.00 | These are classical finite Boolean and version-space facts, not new inference rules.
en170 | SAME | en170 | 1.00 | A separate Python replay checked the four worlds, nine disclosure states, inclusion-minimal certificates, contradictory evidence, and pairs of opposite-verdict worlds for deferred states; its passed.
en171 | SAME | en171 | 1.00 | That verifies the bounded decision logic, not actual human decisions or complete source behavior.
en172 | SAME | en172 | 1.00 | Learning more about a fixed contract removes possible worlds; renegotiating that contract changes the legitimate obligation.
en173 | SAME | en173 | 1.00 | The two transitions must not be conflated.
en174 | SAME | en174 | 1.00 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en175 | SAME | en175 | 1.00 | It adds one module, handles technical reports and errata, and keeps the original book output.
en176 | SAME | en176 | 1.00 | A rejection in Table 2 need not end the search for a patch within that boundary.
en177 | SAME | en177 | 1.00 | The contribution is not a new logical rule: it is a concrete account of why knowing that errata are required settles this decision, whereas a reports-only demand leaves the book-output commitment to be checked.
en178 | SAME | en178 | 1.00 | Applying it to a real review would require finding that commitment in a request, API documentation, tests or caller records.
en179 | SAME | en179 | 1.00 | · Sensitivity to an additional binding obligation.
en180 | SAME | en180 | 1.00 | The preceding approval depends on assuming that the two listed facts exhaust the criteria that matter.
en181 | SAME | en181 | 1.00 | Suppose, as another author-stipulated condition, that this same patch would violate a separate obligation if it were binding; let $C$ indicate whether that third obligation applies.
en182 | SAME | en182 | 1.00 | Under the stricter criterion $A_3(E,B,C)=\neg E\land\neg B\land\neg C$, the universe has eight complete specifications and twenty-seven partial disclosure states.
en183 | SAME | en183 | 1.00 | Exhaustive evaluation yields one ACCEPT, nineteen REJECT and seven DEFER states.
en184 | SAME | en184 | 1.00 | Crucially, evidence that both $E$ and $B$ are false no longer suffices to approve while $C$ remains unknown: the previous ACCEPT becomes DEFER.
en185 | SAME | en185 | 1.00 | If $C$ is explicitly false, the prior nine-state table and its one/five/three distribution are recovered.
en186 | SAME | en186 | 1.00 | This is not an empirically observed safety or performance defect.
en187 | SAME | en187 | 1.00 | The third obligation and stronger criterion were authored for sensitivity analysis.
en188 | SAME | en188 | 1.00 | The point is narrower: one cannot generalize an approval from the original four-world set without evidence that the listed obligations exhaust the relevant acceptance conditions.
en189 | SAME | en189 | 1.00 | Reviewers are not thereby required to investigate arbitrary imaginable obligations; a binding requirement still needs a legitimate source and scope.
en190 | SAME | en190 | 1.00 | [Enumeration code](./paper_b_three_obligation_sensitivity.py) · [regression tests](./test_paper_b_three_obligation_sensitivity.py).
en191 | SAME | en191 | 1.00 | Deciding whether to accept a completed patch differs from choosing an architecture for future edits.
en192 | SAME | en192 | 1.00 | We retain one observation relevant to acceptance.
en193 | SAME | en193 | 1.00 | In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected bracketed=True .
en194 | SAME | en194 | 1.00 | A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.
en195 | SAME | en195 | 1.00 | The presence of a feature is different from its availability along a required route .
en196 | SAME | en196 | 1.00 | Unless the original entry point and its compatibility obligations are identified, implementation through a separate function cannot by itself establish that the requested behavior is available to existing callers.
en197 | SAME | en197 | 1.00 | The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in Paper B 통합 원고 12 · 한·영 문장 교정 and its .
en198 | NEW | en204 | 0.17 | AI-assisted review can make structural patterns easier to classify and explain without automatically establishing which maintenance actions a classification warrants.
en199 | NEW | en018 | 0.14 | We propose calling this gap the principle-to-patch transport problem .
en200 | NEW | en234 | 0.15 | The term is a proposed research focus, not a declaration that requirements engineering, behavioral contracts, or validation theory overlooked the problem.
en201 | NEW | en204 | 0.17 | It recommends separating three evaluands: the accuracy of a principle classification, the downstream approve/reject decision, and the authority of the specific requirements and preserved old-client promises that make the
en202 | NEW | en114 | 0.10 | Such transport need not always be defective: a correctly scoped structural warning may genuinely help a project preserve intended changes.
en203 | NEW | en104 | 0.18 | The question is when its evidence supports a particular action, and with what uncertainty.
en204 | SAME | en198 | 1.00 | Drawing a square first establishes what a routine does, not whether it must be edited.
en205 | SAME | en199 | 1.00 | That depends on whether sorting belongs to the routine's obligations.
en206 | SAME | en200 | 1.00 | In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required.
en207 | SAME | en201 | 1.00 | We did not observe a real OCP label being misused to reject a patch.
en208 | SAME | en202 | 1.00 | We asked what additional grounds a design-principle assessment needs before it can justify an engineering decision .
en209 | NEW | en220 | 0.11 | Four falsifiable directions.
en210 | NEW | en178 | 0.14 | First, do code-only reviewers given a principle label misapply real acceptance criteria more often than reviewers also supplied authentic requests and API commitments?
en211 | NEW | en093 | 0.17 | Second, how frequently do principle-citing review comments identify a binding requirement or preserved caller obligation, and is that associated with disposition?
en212 | NEW | en194 | 0.30 | Third, how do reviewers judge a patch that implements a feature through a new entry point but not the existing required call path?
en213 | NEW | en051 | 0.11 | Fourth, do conditional design policies predict maintenance impact on newly requested changes better than unconditional prohibitions?
en214 | NEW | en251 | 0.11 | These are proposals, not findings .
en215 | NEW | en125 | 0.16 | A conventional requirements-traceability review with equivalent sources and budget is an essential competitor; if it matches or outperforms the proposed framework, no distinct performance gain should be claimed.
en216 | NEW | en229 | 0.13 | Likewise, some traditional design principles may be strongly predictive under well-defined conditions, which this agenda should recover rather than dismiss.
en217 | SAME | en203 | 1.00 | A practical review should first ask not only whether the patch implements a feature but where the request or an authorized agreement requires that feature to be reachable.
en218 | SAME | en204 | 1.00 | The reviewer should then locate the source of each protected old-client obligation in requests, API documentation, tests and actual call paths, without automatically treating every observed response as a promise.
en219 | SAME | en205 | 1.00 | If those sources leave different legitimate contracts possible, asking who can settle the obligation is more defensible than turning an OCP label into a categorical rejection.
en220 | SAME | en206 | 1.00 | Conversely, a demonstrated failure to meet an already binding new demand may reject the fixed patch before every other old-client promise is resolved.
en221 | SAME | en207 | 1.00 | This sequence is a recommendation derived from our authored example, not evidence that it reduces actual review costs in an organization.
en222 | SAME | en208 | 1.00 | Keeping the specifications compatible with known facts and checking their verdicts is elementary logic.
en223 | SAME | en209 | 1.00 | The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository.
en224 | SAME | en210 | 1.00 | Our evidence is confined to one benchmark archive, authored executable examples, an authored logical sensitivity check, and two post hoc selected external issue threads.
en225 | SAME | en211 | 1.00 | We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.
en226 | SAME | en212 | 1.00 | The audits in Sections 3–4 read the archived JSON and JSONL as data.
en227 | SAME | en213 | 1.00 | A separate script reproduced sixteen JSONL files, 768 rows, 48 distinct submissions, 24 scaffolds and 64 fixed model–strategy–language groups, and counted Python comments in four of twelve unique submissions.
en228 | SAME | en214 | 1.00 | Section 5 and the call-path check in Section 6 use examples written for this study.
en229 | SAME | en215 | 0.95 | The shape-layout experiment and Figure 1 remain preserved in manuscript 12; manuscript 21 does not reframe them as a new measured maintenance-cost trial.
en230 | SAME | en216 | 1.00 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en231 | SAME | en217 | 1.00 | The table below gives the nine verdicts for Section 5.
en232 | SAME | en218 | 1.00 | Both values of a withheld field remain possible.
en233 | SAME | en219 | 1.00 | Defer means that the compatible rows include both acceptance and rejection. - Meyer, B.
en234 | SAME | en220 | 1.00 | Object-Oriented Software Construction (1st ed.), pp.
en235 | SAME | en221 | 1.00 | The Open–Closed Principle . . - Jones, C.
en236 | SAME | en222 | 1.00 | Development Methods for Computer Programs Including a Notion of Interference .
en237 | SAME | en223 | 1.00 | Oxford University Computing Laboratory, PRG-25.
en238 | SAME | en224 | 1.00 | · . - Pehlivan, F., Ergüzen, A.
en239 | SAME | en225 | 1.00 | M., Lami, M., & Koyuncu, A.
en240 | SAME | en226 | 1.00 | An Empirical Study on Prompting LLMs to Detect Design Principle Violations .
en241 | SAME | en227 | 1.00 | ASE 2025 NIER. . - Bräuer et al.
en242 | SAME | en228 | 1.00 | Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research . . - Cabral et al.
en243 | SAME | en229 | 1.00 | Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding . . - Zhu, H., Zhang, Q., Wang, J., Yang, Z., & Qiu, Y.
en244 | SAME | en230 | 1.00 | Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits . . - Kane, M.
en245 | SAME | en231 | 1.00 | Validating the Interpretations and Uses of Test Scores .
en246 | SAME | en232 | 1.00 | Journal of Educational Measurement , 50(1), 1–73.
en247 | SAME | en233 | 1.00 | · . - Zave, P., & Jackson, M.
en248 | SAME | en234 | 1.00 | Four Dark Corners of Requirements Engineering .
en249 | SAME | en235 | 1.00 | ACM Transactions on Software Engineering and Methodology , 6(1), 1–30.
en250 | SAME | en236 | 1.00 | T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S.
en251 | SAME | en237 | 1.00 | The Oracle Problem in Software Testing: A Survey .
en252 | SAME | en238 | 1.00 | IEEE Transactions on Software Engineering .
en253 | SAME | en239 | 1.00 | · . - Widyasari, R., Zhang, T., Bouraffa, A., Maalej, W., & Lo, D.
en254 | SAME | en240 | 1.00 | Explaining Explanations: An Empirical Study of Explanations in Code Reviews .
en255 | SAME | en241 | 1.00 | ACM Transactions on Software Engineering and Methodology , 34(6), Article 177.
en256 | SAME | en242 | 1.00 | · . - Papotti, A., Paramitha, R., & Massacci, F.
en257 | SAME | en243 | 1.00 | On the acceptance by code reviewers of candidate security patches suggested by Automated Program Repair tools .
en258 | SAME | en244 | 1.00 | Empirical Software Engineering , 29, Article 132.
en259 | SAME | en245 | 1.00 | · . - Jin, H., & Chen, H.
en260 | SAME | en246 | 1.00 | Are LLMs Reliable Code Reviewers?
en261 | SAME | en247 | 1.00 | Systematic Overcorrection in Requirement Conformance Judgement .
en262 | SAME | en248 | 1.00 | · . - Ling, M., Zou, J., & Liu, X.
en263 | SAME | en249 | 1.00 | Negotiating Completion in Agentic Software Work: Acceptance Boundaries and Deferred Requirements .
en264 | SAME | en250 | 1.00 | 이 목록은 인용된 주요 자료를 확인할 수 있게 모은 집필용 서지이며, 서지형식·인용 위치·전수 대조를 마친 제출용 참고문헌은 아직 아니다.
en265 | SAME | en251 | 1.00 | / These are verified reading anchors, not yet a fully formatted submission bibliography.
en266 | NEW | en014 | 0.11 | Historical priority boundary.
en267 | NEW | en132 | 0.10 | Paper B's explicit conceptual genealogy in this research archive goes through early manuscript 01–02, the later “SOLID history and AI quasi-axiomatization” handoff, and the 2026-11-21 Plan B′ editorial debate.
en268 | NEW | en055 | 0.10 | Recovered Notion pages document the trajectory, but the earliest complete ChatGPT transcript could not be retrieved in this session.
en269 | NEW | en247 | 0.16 | Do not claim an unverified first-in-world date or independent discovery of requirements traceability, OCP conditionals, or Boolean information lattices.
en270 | NEW | en051 | 0.17 | Paper C: compare design configurations under prospective new change requests and an equal-information rival; study whether structural success reverses with edit boundaries and old API obligations.
en271 | NEW | en178 | 0.15 | Paper D: estimate prevalence and outcomes of AI-assisted principle citation in real reviews using independent annotators and provenance-coded requests.
en272 | NEW | en188 | 0.14 | EvoNOMOS mainline: search for generalizable conditional mechanisms of source organization without claiming broad proofs from a selected set of Go routers.
en273 | NEW | en034 | 0.13 | Formalization ceiling: a position paper does not require proving a general program equivalence or an undecidable semantic relation.
en274 | NEW | en182 | 0.14 | Any future claim of universal soundness, completeness, impossibility, P/NP separation or measured performance advantage would require a precisely stated formal/empirical problem and separate verification.
en275 | NEW | en108 | 0.13 | General program semantic equivalence and P-versus-NP complexity are distinct questions; no reduction or complexity ranking is proposed here.
en276 | NEW | en092 | 0.14 | Methodological authority: Meyer/Martin and later review studies are historical interlocutors and empirical competitors, not unquestionable authorities.
en277 | NEW | en209 | 0.16 | If newer source-specific evidence supports a narrower or contrary conclusion, revise the candidate principle and document the contradiction.
Summary en: SAME 251, EDIT 0, NEW 26
