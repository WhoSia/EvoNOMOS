# Paper B R19D — Sentence Diff Index v21–v27
Same sentence segmentation + char-3-gram nearest candidate. VERY IMPORTANT: exact text equality/near matches do not certify the underlying scientific or semantic correctness. v21 repeated boundary baseline. Document sections are extracted by Korean/English manuscript markers.

## v21 · [Source](https://app.notion.com/p/41fef561cf9281629eafc9e45223b58b)
### ko (217 sentences)
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
ko033 | BASE | — | 0.00 | · · 우리는 서로 다른 두 자료를 사용했다.
ko034 | BASE | — | 0.00 | 벤치마크에서는 분류를 요구받은 모델에게 실제로 어떤 입력이 주어졌는지 조사했다.
ko035 | BASE | — | 0.00 | 도서관 예제에서는 패치 한 개를 고정하고, 적용할 요구와 보호할 계약을 바꿔 가며 실행 결과와 승인 기준을 대조했다.
ko036 | BASE | — | 0.00 | 벤치마크의 저장 코드와 도서관 코드는 별개이고, 어느 쪽에도 실제 검토자의 승인·거절 판단은 포함되지 않는다.
ko037 | BASE | — | 0.00 | OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다.
ko038 | BASE | — | 0.00 | 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다.
ko039 | BASE | — | 0.00 | 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다.
ko040 | BASE | — | 0.00 | 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다.
ko041 | BASE | — | 0.00 | 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다.
ko042 | BASE | — | 0.00 | 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.
ko043 | BASE | — | 0.00 | 지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다.
ko044 | BASE | — | 0.00 | 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다.
ko045 | BASE | — | 0.00 | 이 판독은 제출 코드를 가린 지시문에 관한 것이다.
ko046 | BASE | — | 0.00 | 독립 감사에서 Python 저장 행 192개를 이루는 고유 코드 12개를 검사하자 4개에서 주석 토큰 46개를 발견했고, docstring을 포함한 코드는 없었다.
ko047 | BASE | — | 0.00 | 주석이 기능의 의도를 암시할 수 있으므로, 지시문에 개별 요구가 없다는 사실을 코드 전체에 명세 단서가 없다는 주장으로 확대하지 않았다.
ko048 | BASE | — | 0.00 | 다른 세 언어의 주석은 같은 방법으로 계수하지 않았다.
ko049 | BASE | — | 0.00 | 저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다.
ko050 | BASE | — | 0.00 | Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다.
ko051 | BASE | — | 0.00 | 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다.
ko052 | BASE | — | 0.00 | 압축 파일 안의 코드 자체는 실행하지 않았다.
ko053 | BASE | — | 0.00 | 도서관 예제에서는 원본 소스와 수정안, 호출 입력, 새 모듈을 추가할 수 있다는 편집 범위를 고정했다.
ko054 | BASE | — | 0.00 | 코드 실행으로 확인한 것은 구체적인 입력에서 나온 출력과 예외다.
ko055 | BASE | — | 0.00 | 반면 기술보고서·정오표 중 무엇을 요구하는지, 책 출력의 접두어가 보호 대상인지, 새 요구를 충족하면서 보호된 기존 동작을 보존해야 승인한다 는 기준은 모두 연구자가 정했다.
ko056 | BASE | — | 0.00 | 따라서 §5의 표는 독립 심사위원의 판정이 아니라 우리가 지정한 기준을 실행 관찰에 적용한 결과다.
ko057 | BASE | — | 0.00 | 일부 전제만 공개한 경우에는 두 요구와 두 계약으로 이루어진 후보 명세 중 공개된 사실과 맞는 것만 남겼다.
ko058 | BASE | — | 0.00 | 이 후보군 밖의 실제 요구나 계약까지 조사했다고 가정하지 않는다.
ko059 | BASE | — | 0.00 | · · · · Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21) Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko060 | BASE | — | 0.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko061 | BASE | — | 0.00 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko062 | BASE | — | 0.00 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko063 | BASE | — | 0.00 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko064 | BASE | — | 0.00 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko065 | BASE | — | 0.00 | 추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. gpt-4o-mini 와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다.
ko066 | BASE | — | 0.00 | 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다.
ko067 | BASE | — | 0.00 | 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.
ko068 | BASE | — | 0.00 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko069 | BASE | — | 0.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko070 | BASE | — | 0.00 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko071 | BASE | — | 0.00 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko072 | BASE | — | 0.00 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko073 | BASE | — | 0.00 | 저장 코드와 참조 쌍은 앞에서 명시한 문자열 정규화 기준에서 일치하지 않았으며, Python 코드에 한한 AST 비교에서도 일치 사례가 없었다.
ko074 | BASE | — | 0.00 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko075 | BASE | — | 0.00 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko076 | BASE | — | 0.00 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko077 | BASE | — | 0.00 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko078 | BASE | — | 0.00 | · · · Bräuer 등(2018)은 설계 원칙을 어떻게 측정할지 전문가에게 물었고, Cabral 등(2024)은 SOLID를 적용한 코드를 이해하고 확장하는 경험을 조사했다.
ko079 | BASE | — | 0.00 | Zhu 등(2026)은 구체적인 저장소 변경 과제에 기능 및 구조 검사를 결합했다.
ko080 | BASE | — | 0.00 | 우리의 벤치마크 감사도 분류 성능을 부정하려는 것이 아니다.
ko081 | BASE | — | 0.00 | 분류에 성공했다는 증거를 수정안 거절의 증거로 옮길 때 무엇이 더 필요한지를 묻는다.
ko082 | BASE | — | 0.00 | · · 실제 리뷰 연구는 이 논문의 주장 범위를 더 엄격하게 제한한다.
ko083 | BASE | — | 0.00 | Widyasari 등(2025)은 Gerrit 코드 리뷰 댓글 793건을 분석하고 규칙이나 원칙을 근거로 드는 설명 유형을 확인했다.
ko084 | BASE | — | 0.00 | 이는 원칙에 의거한 설명이 리뷰에 존재한다는 증거지만, 원칙이 잘못 적용돼 특정 수정안이 거절됐다는 증거는 아니다.
ko085 | BASE | — | 0.00 | Papotti 등(2024)은 컴퓨터과학 석사과정 학생 72명을 대상으로 보안 자동 수리 패치의 채택 여부를 실험했다.
ko086 | BASE | — | 0.00 | 제안 도구의 전문성을 알리는 정보에 따라 판단이 바뀌는 현상을 관찰했지만, 원칙 위반 라벨을 대상으로 한 연구는 아니다.
ko087 | BASE | — | 0.00 | 두 논문의 실제 사람에 대한 관측은 우리가 구성한 표 2의 승인 기준과 다르다.
ko088 | BASE | — | 0.00 | · Jin과 Chen(2026)은 정답 코드와 결함 코드에 대한 다섯 언어 모델의 요구 적합성 판단을 세 프로그래밍 벤치마크에서 실험하고, 맞는 코드를 잘못 거절하는 현상과 설명·수정 제안을 요구하는 프롬프트의 위험을 보고했다.
ko089 | BASE | — | 0.00 | 따라서 LLM의 과잉 거절을 처음 지적했다고 주장할 수 없다.
ko090 | BASE | — | 0.00 | Ling·Zou·Liu(2026)는 공개 GitHub 변경 사례의 질적 연구에서 병합, 이슈 종료, 요구 충족이 서로 다른 결과일 수 있음을 논증했다.
ko091 | BASE | — | 0.00 | 수용 경계가 조건부라는 발견도 우리의 최초성이 아니다.
ko092 | BASE | — | 0.00 | 우리 사례는 실행 결과가 고정된 패치에서 현재 공개된 요구·계약이 정당화하는 판정과 추가 질문을 정확하게 분리하는 재현 가능한 실례 다.
ko093 | BASE | — | 0.00 | · 그 질문 자체에도 중요한 선행연구가 있다.
ko094 | BASE | — | 0.00 | Kane(2013)은 검사 점수의 해석을 뒷받침하는 증거가 그 점수를 특정 결정에 사용하는 일까지 정당화하지는 않는다고 논했다.
ko095 | BASE | — | 0.00 | 이는 소프트웨어 리뷰를 실험한 결과가 아니라, 평가 결과의 사용 을 따로 정당화해야 한다는 일반적인 논증이다.
ko096 | BASE | — | 0.00 | Zave와 Jackson(1997)은 요구사항, 기계 명세, 환경에 관한 지식이 어떻게 연결되는지 설명하면서 행위의 통제 주체를 구별했다.
ko097 | BASE | — | 0.00 | 원을 앞에 정렬할 책임이 호출자에게 있는지 함수에 있는지부터 따져야 한다는 우리의 질문도 이러한 오래된 문제의 한 사례다.
ko098 | BASE | — | 0.00 | 존스(1981) 역시 병렬 프로그램에서 환경 의존 조건과 프로그램 보장 조건의 양립을 다뤘다.
ko099 | BASE | — | 0.00 | · · Barr 등(2015)이 정리한 테스트 오라클 문제는 코드 실행과 올바름 판정 사이에도 근거가 필요함을 상기시킨다.
ko100 | BASE | — | 0.00 | §5의 시험은 지정된 호출의 동작을 확인하지만, 그 동작을 보존하겠다는 실제 프로젝트의 약속을 입증하지는 않는다.
ko101 | BASE | — | 0.00 | 따라서 다음 절의 요구·계약은 발견한 사실이 아니라 명시적으로 정한 전제다.
ko102 | BASE | — | 0.00 | 위반 범주를 맞혔다는 사실은 코드에 특정 구조가 있다는 평가를 뒷받침한다.
ko103 | BASE | — | 0.00 | 그러나 수정안을 거절하려면 (1) 누구에게서 나온 새 요구인지, (2) 기존 호출자에게 계속 보장하기로 한 동작이 무엇인지, (3) 그 동작과 새 기능을 어느 호출 경로로 제공해야 하는지까지 알아야 한다.
ko104 | BASE | — | 0.00 | 이 가운데 일부는 소스에 표시될 수 있지만, 관측한 구현이 곧 승인된 계약이라는 뜻은 아니다.
ko105 | BASE | — | 0.00 | 예컨대 같은 출력 변경을 보고도 책 출력이 보호 대상일 때와 아닐 때는 서로 다른 판정이 가능하다.
ko106 | BASE | — | 0.00 | 분류 라벨을 고정한 채 판정이 달라지는 반례는 §5에서 실행한 동일 패치의 네 명세에 한정된다.
ko107 | BASE | — | 0.00 | 이를 통해 분류 점수 자체를 부정하거나 실제 리뷰어가 라벨 때문에 패치를 거절했다고 주장하지 않는다.
ko108 | BASE | — | 0.00 | 이 주장은 분류기에 어떤 정보를 주는지에 따라서도 달라진다.
ko109 | BASE | — | 0.00 | 소스 코드만 보고 OCP 위반 여부를 판정하는 분류기라면 코드가 고정된 네 명세에서 입력과 출력 라벨을 동일하게 유지한다.
ko110 | BASE | — | 0.00 | 반면 실제 요구서와 호출자 계약을 입력받는 문맥 의존적 평가자는 명세에 따라 판단을 변경할 수 있다.
ko111 | BASE | — | 0.00 | 따라서 이 논문의 반례는 모든 OCP 평가가 언제나 같은 라벨을 낸다는 주장이 아니라, 고정된 소스의 위반 라벨만으로 서로 다른 실제 유지보수 판정을 식별할 수 없다는 제한된 주장 이다.
ko112 | BASE | — | 0.00 | 기존 요구사항 추적표나 호환성 검토 역시 추가 근거를 물어 문제를 해결할 수 있으므로, 이를 우리의 새 방법만이 수행한다고 해석하지 않는다.
ko113 | BASE | — | 0.00 | 직접 작성하지 않은 사례에서도 요구와 동작을 분리할 수 있는지 살피기 위해 Go 웹 라우터 Chi의 공개 이슈 (2025년 5월 2일)를 그 후속 댓글과 함께 읽었다.
ko114 | BASE | — | 0.00 | 작성자는 미들웨어 생성 함수가 같은 싱글턴 핸들러를 반환하면 중첩 라우터 그룹의 요청이 마지막 그룹에 전달되는 상황을 신고했다.
ko115 | BASE | — | 0.00 | 다른 참여자는 생성 함수 호출마다 새 미들웨어 인스턴스를 반환하는 우회 코드를 제시했고, 원래 작성자는 그 방법을 이해한다고 답했다.
ko116 | BASE | — | 0.00 | 그러나 작성자는 싱글턴을 그대로 써도 정상적인 라우팅이 되거나, 잘못된 재사용을 명시적으로 알려 주는 동작을 원한다는 점을 다시 밝혔다.
ko117 | BASE | — | 0.00 | 따라서 새 인스턴스를 만들어 기존 세 경로에서 정답 응답이 나왔다는 사실이 확인되더라도, 그것을 싱글턴을 안전하게 지원해 달라는 원래 요청이 해결됐다는 증거로 바꿀 수는 없다.
ko118 | BASE | — | 0.00 | 이 관찰은 Paper B에서 말하는 요구의 권위를 더 구체적으로 만든다.
ko119 | BASE | — | 0.00 | 이슈의 기대 동작 , 참여자가 제안한 우회 수정 , 연구자가 선택한 테스트 통과 조건 은 서로 다른 자료다.
ko120 | BASE | — | 0.00 | 원래 작성자가 제안된 우회를 알고 있다는 사실만으로 라이브러리 관리자가 API 계약 변경을 승인했다고 볼 수도 없다.
ko121 | BASE | — | 0.00 | 반대로 이 이슈는 OCP 위반 분류가 실제 리뷰에서 잘못된 패치 거절을 일으켰다는 사례가 아니다.
ko122 | BASE | — | 0.00 | 연구자가 이미 알려진 문제를 선택해 조사했으므로 독립적 전향 실험도 아니다.
ko123 | BASE | — | 0.00 | · 또 다른 공개 이슈 에서는 작성자가 최초에 정규식 경로의 하위 경로 처리를 문제 삼았지만, 같은 날 후속 댓글에서 독립적인 재현 결과 그 부분은 문제가 아니었다고 정정했다.
ko124 | BASE | — | 0.00 | 정적 경로와 매개변수 경로의 메서드 처리에 관한 나머지 문제와, 스스로 철회한 정규식 주장을 같은 수준의 확정 사실로 분류해서는 안 된다.
ko125 | BASE | — | 0.00 | 이러한 출처 이력은 분류자가 읽는 코드만으로는 알 수 없는 정보이며, 이 논문이 제안하는 근거 확인 절차를 적용할 때 반드시 남겨야 하는 반대 사례다.
ko126 | BASE | — | 0.00 | 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko127 | BASE | — | 0.00 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko128 | BASE | — | 0.00 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko129 | BASE | — | 0.00 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko130 | BASE | — | 0.00 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko131 | BASE | — | 0.00 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko132 | BASE | — | 0.00 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko133 | BASE | — | 0.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko134 | BASE | — | 0.00 | 책 접두어가 보호 대상이 아니라는 가정은 실제 이용자가 그 출력을 기대하지 않는다는 관찰이 아니다.
ko135 | BASE | — | 0.00 | 단지 이 비교에서 보존 의무로 정하지 않았다는 뜻이다.
ko136 | BASE | — | 0.00 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko137 | BASE | — | 0.00 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko138 | BASE | — | 0.00 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko139 | BASE | — | 0.00 | 이 절차는 실제 명세가 표의 네 경우 중 하나라는 조건 아래서만 성립한다.
ko140 | BASE | — | 0.00 | 공개된 사실과 맞는 행이 하나도 없다면 승인이나 거절을 내릴 것이 아니라 자료 또는 후보군이 잘못됐는지 확인해야 한다.
ko141 | BASE | — | 0.00 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko142 | BASE | — | 0.00 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko143 | BASE | — | 0.00 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko144 | BASE | — | 0.00 | 정오표 지원이 필수인지 여부를 $E$, 기존 책 출력 접두어를 보호하는지 여부를 $B$라고 두자.
ko145 | BASE | — | 0.00 | 연구자가 정한 네 명세에 한정하면, 이 고정 패치의 승인 조건은 $A(E,B)=\neg E\land\neg B$다.
ko146 | BASE | — | 0.00 | 따라서 승인에 필요한 최소 증거는 $\{\neg E,\neg B\}$이며, 거절을 확정하는 최소 증거는 $\{E\}$ 또는 $\{B\}$다.
ko147 | BASE | — | 0.00 | 두 조건을 모두 알 수 없다면, 승인 명세 $(E=0,B=0)$와 거절 명세 $(E=1,B=0)$가 양립하므로 판정을 보류한다.
ko148 | BASE | — | 0.00 | 기술보고서만 요구한다는 사실, 즉 $\neg E$가 확인되면 $B$를 물어 어느 쪽인지 결정할 수 있다.
ko149 | BASE | — | 0.00 | 반면 두 조건이 전부 미공개일 때는 하나의 예·아니오 질문만으로 모든 답변에 대해 판정을 확정하지 못한다.
ko150 | BASE | — | 0.00 | 이것은 새로운 논리 규칙이 아니라 고전적인 유한 정보 집합 판정이다.
ko151 | BASE | — | 0.00 | 별도 Python 코드는 네 명세의 공개 상태 아홉 가지, 최소 승인·거절 증거, 보류 상태의 대립 명세, 모순된 사실의 처리까지 검사했고 가 통과했다.
ko152 | BASE | — | 0.00 | 이 테스트가 실제 검토자의 판단이나 원본 도서관 프로그램의 전체 동작을 재검증한 것은 아니다.
ko153 | BASE | — | 0.00 | 또한 고정된 계약에 관한 사실을 알게 되는 것 과 계약 자체를 변경하는 것 을 구별해야 한다.
ko154 | BASE | — | 0.00 | 앞의 경우에는 가능한 명세의 집합이 줄지만, 뒤의 경우에는 승인 조건 자체가 달라질 수 있다.
ko155 | BASE | — | 0.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko156 | BASE | — | 0.00 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko157 | BASE | — | 0.00 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko158 | BASE | — | 0.00 | 이 비교에서 얻은 것은 새로운 논리 규칙이 아니다.
ko159 | BASE | — | 0.00 | 한 사실만 알아도 거절이 확정되는 경우와, 책 출력 약속을 물어야 하는 경우를 구체적인 호출 결과로 구분한 것이다.
ko160 | BASE | — | 0.00 | 실제 리뷰에 적용하려면 요구서와 API 문서, 테스트 및 호출 기록에서 그 약속의 근거를 따로 찾아야 한다.
ko161 | BASE | — | 0.00 | · 계약 조건을 하나 더 추가했을 때의 민감도.
ko162 | BASE | — | 0.00 | 위의 승인 규칙은 두 조건만 관련된다는 전제에 의존한다.
ko163 | BASE | — | 0.00 | 이 고정 패치가 다른 독립적인 보호 의무도 위반한다고 연구자가 가정하고, 그 의무가 현재 실제로 적용되는지를 $C$라고 두자.
ko164 | BASE | — | 0.00 | 세 의무 가운데 하나라도 적용되면 패치를 거절하도록 승인 기준을 새로 정하면 $A_3(E,B,C)=\neg E\land\neg B\land\neg C$가 된다.
ko165 | BASE | — | 0.00 | 이때 네 명세는 여덟 가지 완전 명세로, 아홉 공개 상태는 스물일곱 공개 상태로 확장된다.
ko166 | BASE | — | 0.00 | 전수 계산 결과는 승인 1개, 거절 19개, 보류 7개다.
ko167 | BASE | — | 0.00 | 특히 예전 두 조건이 모두 거짓이라고 알더라도 $C$가 미공개라면 기존의 승인은 보류 로 바뀐다.
ko168 | BASE | — | 0.00 | 반대로 $C$가 적용되지 않는다고 명시적으로 확인하면 원래의 아홉 상태와 승인 1·거절 5·보류 3 분포가 복원된다.
ko169 | BASE | — | 0.00 | 이 계산은 실제로 새로운 보안·성능 결함을 발견했다는 뜻이 아니다.
ko170 | BASE | — | 0.00 | $C$는 연구자가 만든 제삼의 독립 의무이고, 새 기준은 기존 승인 기준보다 엄격하다.
ko171 | BASE | — | 0.00 | 그 목적은 필요한 요구를 전부 열거했다는 근거 없이 기존의 승인 판정을 일반화할 수 없음 을 드러내는 것이다.
ko172 | BASE | — | 0.00 | 그렇다고 실제 검토자가 가능한 모든 요구를 무한히 조사해야 하는 것도 아니다.
ko173 | BASE | — | 0.00 | 어떤 요구가 승인 기준에 포함되는지는 적격한 주체와 계약 출처에 의해 제한돼야 한다.
ko174 | BASE | — | 0.00 | [전수 계산 코드](./paper_b_three_obligation_sensitivity.py) · [회귀 테스트](./test_paper_b_three_obligation_sensitivity.py).
ko175 | BASE | — | 0.00 | 완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다.
ko176 | BASE | — | 0.00 | 여기서는 앞의 질문에 해당하는 관찰만 남긴다.
ko177 | BASE | — | 0.00 | 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 bracketed=True 를 넘기면 인자를 거절했다.
ko178 | BASE | — | 0.00 | 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다.
ko179 | BASE | — | 0.00 | 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.
ko180 | BASE | — | 0.00 | 새 기능이 있다는 사실과 요구된 호출 경로에서 쓸 수 있다는 사실 은 다르다.
ko181 | BASE | — | 0.00 | 보호해야 할 기존 진입점이 무엇인지 확인하지 않으면, 같은 옵션을 새 함수에서 제공했다는 사실만으로 수정안의 적합성을 판정할 수 없다.
ko182 | BASE | — | 0.00 | 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 Paper B 통합 원고 12 · 한·영 문장 교정 및 에 원형 그대로 보존했다.
ko183 | BASE | — | 0.00 | AI가 코드의 구조를 분류하고 문제를 설명하는 일이 일반화될수록, 개발자가 받는 조언은 명료해질 수 있지만 분류 결과가 어떤 구체적 행동을 정당화하는지는 별도 문제로 남는다.
ko184 | BASE | — | 0.00 | 우리는 이 간극을 \*\*원칙→수정안 판단의 전이 문제(principle-to-patch transport problem)\*\*라고 부르자고 제안한다.
ko185 | BASE | — | 0.00 | 이 표현은 기존 요구공학·계약 이론·검증 이론에서 비슷한 문제를 다루지 않았다는 선언이 아니다.
ko186 | BASE | — | 0.00 | 원칙 위반 분류의 정확도, 그 분류를 받은 개발자의 실제 승인·거절 판단, 해당 판단에 대한 요구·계약의 승인 근거를 서로 다른 평가 대상으로 놓자 는 연구 제안이다.
ko187 | BASE | — | 0.00 | 원칙이 특정 프로젝트에서 보호해야 하는 변경 축을 정확히 가리킨다면, 구조적 경고가 실제 리뷰에서 중요한 단서가 될 수 있기 때문이다.
ko188 | BASE | — | 0.00 | 문제는 원칙을 폐기할 것인지가 아니라, 그 단서에 어느 범위의 결론 권한을 부여할 것인지다.
ko189 | BASE | — | 0.00 | 마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다.
ko190 | BASE | — | 0.00 | 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다.
ko191 | BASE | — | 0.00 | 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다.
ko192 | BASE | — | 0.00 | 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다.
ko193 | BASE | — | 0.00 | 원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가 가 이 논문에서 다룬 질문이다.
ko194 | BASE | — | 0.00 | 후속 연구를 위한 네 가지 반증 가능 질문.
ko195 | BASE | — | 0.00 | 첫째, 코드와 원칙 라벨만 받은 검토자는 요구서·API 계약을 함께 받은 검토자보다 실제 프로젝트의 승인 기준을 더 자주 잘못 적용하는가?
ko196 | BASE | — | 0.00 | 둘째, 원칙을 언급하는 코드 리뷰가 실제로 명세나 호출자 의무를 인용하는 비율은 어느 정도이며, 그 인용의 유무가 판단과 상관되는가?
ko197 | BASE | — | 0.00 | 셋째, 새 기능을 구현했지만 기존 진입점이 제공되지 않는 수정안은 실무자가 어떻게 평가하는가?
ko198 | BASE | — | 0.00 | 넷째, 조건부 설계 지침이 보편적인 금지 규칙보다 새로운 요구에서 더 정확한 변경 영향 예측을 제공하는가?
ko199 | BASE | — | 0.00 | 이 네 질문은 아직 측정하지 않은 제안이다.
ko200 | BASE | — | 0.00 | 동등한 정보와 시간을 받은 일반 요구사항 추적 검토가 같은 결과를 낸다면, 새 방법의 실용적 우위는 기각하거나 좁혀야 한다.
ko201 | BASE | — | 0.00 | 실제 기존 원칙들이 일부 조건에서 오히려 강한 예측력을 보인다면 그 경우도 연구 결과에 남겨야 한다.
ko202 | BASE | — | 0.00 | 실제 검토에서 먼저 확인할 것은 수정안의 새 기능만이 아니라, 요구한 사람이나 합의된 문서가 그 기능을 어느 진입점에서 제공하도록 정했는지다.
ko203 | BASE | — | 0.00 | 그다음 기존 호출자가 의존하는 동작 중 무엇이 보호 대상인지 요구서·API 문서·테스트·호출 코드에서 근거를 찾아야 한다.
ko204 | BASE | — | 0.00 | 이 근거가 둘 이상의 가능한 계약을 남긴다면, 원칙 위반이라는 이름으로 결론을 확정하기보다 계약의 출처와 범위를 묻는 편이 정확하다.
ko205 | BASE | — | 0.00 | 반대로 새로운 요구를 충족하지 못한다는 사실이 이미 확정됐다면, 어떤 기존 계약이 추가로 보호되는지 모두 조사하기 전에 해당 수정안을 거절할 수도 있다.
ko206 | BASE | — | 0.00 | 이러한 질문의 순서는 이 논문의 구성 사례에서 나온 실무적 제안이지, 실제 개발 조직의 효율이 개선됐다는 관측 결과는 아니다.
ko207 | BASE | — | 0.00 | 공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다.
ko208 | BASE | — | 0.00 | 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다.
ko209 | BASE | — | 0.00 | 이 연구는 한 벤치마크의 저장 입력, 연구자가 구성한 실행 예제와 추가 의무에 관한 논리적 민감도 분석, 그리고 연구자가 후향적으로 선정한 두 외부 이슈의 텍스트 근거만을 다뤘다.
ko210 | BASE | — | 0.00 | 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.
ko211 | BASE | — | 0.00 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko212 | BASE | — | 0.00 | 독립 감사 스크립트는 같은 ZIP을 실행 코드가 아닌 자료로 읽어 16개 JSONL 파일, 768행, 48개 고유 코드, 24개 틀, 64개 세부 집단을 재계산했고, Python 고유 코드 12개 중 주석이 있는 4개를 확인했다.
ko213 | BASE | — | 0.00 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko214 | BASE | — | 0.00 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko215 | BASE | — | 0.00 | 12판에 있던 그림 1과 파일 배치 실험은 21판 본문에 싣지 않았으며, 원본 그림과 실행 기록을 12판에 보존했다.
ko216 | BASE | — | 0.00 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko217 | BASE | — | 0.00 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
Summary ko: SAME 0, EDIT 0, NEW 0

### en (277 sentences)
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
en040 | BASE | — | 0.00 | · · We used two distinct sources of evidence.
en041 | BASE | — | 0.00 | We audited the saved benchmark inputs to determine what a classifier was actually asked to judge.
en042 | BASE | — | 0.00 | Separately, we fixed one catalog patch and varied the demands and protected caller commitments against which its execution was assessed.
en043 | BASE | — | 0.00 | The benchmark submissions are not instances of the catalog patch, and neither source records decisions by real reviewers.
en044 | BASE | — | 0.00 | The OCP reference material contains 48 before-and-after code pairs.
en045 | BASE | — | 0.00 | Sixteen saved JSONL files each contain 48 records, yielding 768 rows.
en046 | BASE | — | 0.00 | Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times.
en047 | BASE | — | 0.00 | We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality.
en048 | BASE | — | 0.00 | The result was 24 scaffolds.
en049 | BASE | — | 0.00 | Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs.
en050 | BASE | — | 0.00 | The 768 records are repeated submissions, not independent maintenance cases.
en051 | BASE | — | 0.00 | We separately read the masked instructions for case-specific change requests and protected caller commitments.
en052 | BASE | — | 0.00 | An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape.
en053 | BASE | — | 0.00 | We inspected the text outside the submitted code, not the whole semantic context.
en054 | BASE | — | 0.00 | In a separate replication, the 192 saved Python rows reduced to twelve distinct code submissions; four contained a total of 46 comment tokens, and none had an AST-detected docstring.
en055 | BASE | — | 0.00 | These comments may convey implementation intent, but counting them does not establish a contract.
en056 | BASE | — | 0.00 | We did not perform the same comment-token audit for the other three languages.
en057 | BASE | — | 0.00 | We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace.
en058 | BASE | — | 0.00 | For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions.
en059 | BASE | — | 0.00 | These tests do not establish whether inherited methods remain available or whether callers were promised a behavior.
en060 | BASE | — | 0.00 | We read code as archive data and did not execute it.
en061 | BASE | — | 0.00 | For the catalog, we fixed the baseline, candidate patch, calls and permission to add a module.
en062 | BASE | — | 0.00 | Executing the code established outputs and exceptions for those calls.
en063 | BASE | — | 0.00 | The possible demands (technical reports alone, or technical reports and errata), the two scopes of the book-output obligation, and the rule that an acceptable patch must meet its demand and preserve protected behavior we
en064 | BASE | — | 0.00 | Table 2 therefore applies authored criteria to observed behavior; it does not report independent human decisions.
en065 | BASE | — | 0.00 | For partial disclosure, we retained only the candidate specifications compatible with known facts.
en066 | BASE | — | 0.00 | We did not attempt to enumerate obligations outside these four constructed cases.
en067 | BASE | — | 0.00 | · · · Pehlivan et al. chose violation scenarios and refined the generated examples.
en068 | BASE | — | 0.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en069 | BASE | — | 0.00 | The benchmark compares model classifications with the resulting labels.
en070 | BASE | — | 0.00 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en071 | BASE | — | 0.00 | No two strategies shared a template string.
en072 | BASE | — | 0.00 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en073 | BASE | — | 0.00 | An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: gpt-4o-mini differed from the other three models.
en074 | BASE | — | 0.00 | Holding model, strategy and language fixed left one scaffold shared across twelve programs.
en075 | BASE | — | 0.00 | No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST.
en076 | BASE | — | 0.00 | These checks do not establish semantic independence or source lineage.
en077 | BASE | — | 0.00 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en078 | BASE | — | 0.00 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en079 | BASE | — | 0.00 | If a new shape is needed, that branch is a place to look.
en080 | BASE | — | 0.00 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en081 | BASE | — | 0.00 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en082 | BASE | — | 0.00 | No submitted program matched a reference side under the reported textual normalizations, and the separate Python-only AST comparison also found no match.
en083 | BASE | — | 0.00 | Pair 37 establishes that a declaration was removed.
en084 | BASE | — | 0.00 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en085 | BASE | — | 0.00 | Evidence in the saved material and evidence needed to assess a patch.
en086 | BASE | — | 0.00 | The prompt example is in JSONL line 13 (record ID 12).
en087 | BASE | — | 0.00 | Pair 37 is in a separate reference JSON file.
en088 | BASE | — | 0.00 | · · · Bräuer et al. (2018) examined the measurement of design principles with experts; Cabral et al. (2024) studied understanding and extension under a bundled SOLID treatment; Zhu et al. (2026) supplied repository chang
en089 | BASE | — | 0.00 | These evaluate different objects.
en090 | BASE | — | 0.00 | Our audit does not contest the benchmark's classification task.
en091 | BASE | — | 0.00 | It asks what else would be needed to use such a classification as a reason to reject a patch.
en092 | BASE | — | 0.00 | · · Empirical review studies narrow the claim further.
en093 | BASE | — | 0.00 | Widyasari et al. (2025) coded 793 Gerrit review comments and identified explanation categories including appeals to rules or principles.
en094 | BASE | — | 0.00 | This shows that principle-based explanations appear in review practice; it does not show that such principles caused an unjustified patch rejection.
en095 | BASE | — | 0.00 | Papotti et al. (2024) experimentally studied 72 computer-science master's students deciding whether to adopt security patches proposed by automatic program repair tools, and found that information about the purported too
en096 | BASE | — | 0.00 | Unlike our stipulated Table 2 judgments, those were observed human choices.
en097 | BASE | — | 0.00 | · Jin and Chen (2026) tested five language models' judgments of canonical and buggy implementations against natural-language specifications across three programming benchmarks.
en098 | BASE | — | 0.00 | They reported false rejection of correct code and risks from prompts that demand explanations or fixes.
en099 | BASE | — | 0.00 | We cannot claim to have discovered LLM over-rejection or to improve its error rate: our archive does not record independent patch-acceptance judgments by those models.
en100 | BASE | — | 0.00 | Ling, Zou, and Liu (2026) examined public agent-associated contributions and distinguished merges, issue closures, and requirement satisfaction.
en101 | BASE | — | 0.00 | Conditional acceptance is not first discovered by this paper either.
en102 | BASE | — | 0.00 | Our narrower addition is to hold a patch's execution fixed and make explicit which partially disclosed requirement and contract facts warrant a verdict and which warrant further inquiry .
en103 | BASE | — | 0.00 | · This is not a new problem in general.
en104 | BASE | — | 0.00 | Kane (2013) argues that evidence supporting an interpretation of test scores does not automatically justify using those scores for a particular decision.
en105 | BASE | — | 0.00 | His work does not test software reviews; it establishes the importance of justifying an assessment's use .
en106 | BASE | — | 0.00 | Zave and Jackson (1997) distinguish requirements, machine specifications and knowledge of the environment, including which actor controls an action.
en107 | BASE | — | 0.00 | Whether sorting belongs to a caller or a drawing function is an instance of that longstanding question.
en108 | BASE | — | 0.00 | Jones (1981) likewise developed conditions for compatible environmental reliance and program guarantees in parallel programs.
en109 | BASE | — | 0.00 | We do not claim these distinctions as our invention.
en110 | BASE | — | 0.00 | · · Barr et al.'s (2015) survey of the test-oracle problem makes a related point about our executable fixture.
en111 | BASE | — | 0.00 | Tests establish outputs for chosen inputs; they do not, without an independently grounded oracle, establish which outputs a real project has promised to preserve.
en112 | BASE | — | 0.00 | Thus the demands and contracts in Section 5 are explicit assumptions rather than requirements recovered from a repository.
en113 | BASE | — | 0.00 | From a classification to a patch disposition.
en114 | BASE | — | 0.00 | Correctly naming a design-principle violation supports a judgment about a structural feature of code.
en115 | BASE | — | 0.00 | Rejecting a specific patch requires different grounds: (i) the source and scope of the new request, (ii) the behavior the project committed to existing callers, and (iii) the call path through which the request and those
en116 | BASE | — | 0.00 | Some clues may reside in source, but observed behavior is not automatically an authorized compatibility promise.
en117 | BASE | — | 0.00 | The same change in book output can be unacceptable under one declared contract and acceptable under another.
en118 | BASE | — | 0.00 | Section 5 supplies a fixed-patch, four-specification witness to that gap.
en119 | BASE | — | 0.00 | It does not disprove the benchmark's classification scores or establish that a real reviewer rejected a patch because of an OCP label.
en120 | BASE | — | 0.00 | The inference also depends on what information the classifier receives.
en121 | BASE | — | 0.00 | A source-only OCP classifier has the same input, and hence the same classification output, across our four fixed-code specifications.
en122 | BASE | — | 0.00 | A context-sensitive evaluator given authentic requests and caller contracts may rightly return different assessments.
en123 | BASE | — | 0.00 | Our witness therefore does not say that all OCP evaluations are constant across contexts.
en124 | BASE | — | 0.00 | It shows only that a label based solely on fixed code cannot identify which distinct maintenance decision binds under unspecified obligations .
en125 | BASE | — | 0.00 | Ordinary requirements traceability and compatibility checklists can ask for these same missing facts; we claim no exclusive ability to do so.
en126 | BASE | — | 0.00 | Reading contract authority from an external issue.
en127 | BASE | — | 0.00 | To check whether the distinction between a request and a test result survives outside our authored fixture, we inspected (May 2, 2025) and its subsequent discussion.
en128 | BASE | — | 0.00 | The reporter described nested router groups in which a middleware factory returning one mutable singleton handler sent requests to the final registered group.
en129 | BASE | — | 0.00 | Another participant proposed returning a fresh middleware instance on every factory invocation.
en130 | BASE | — | 0.00 | The reporter acknowledged knowing this workaround but reiterated the requested library-level behavior: correct routing with the singleton, or an explicit error on invalid reuse.
en131 | BASE | — | 0.00 | Successful responses from an implementation that abandons singleton reuse therefore do not, by themselves, establish satisfaction of the original API request.
en132 | BASE | — | 0.00 | Three evidence roles must stay separate: the reporter's requested behavior , the proposed application-level workaround , and a researcher's test oracle .
en133 | BASE | — | 0.00 | The reporter's acknowledgment of the workaround is not evidence of maintainer authorization of a new API contract.
en134 | BASE | — | 0.00 | Nor does the issue show that an OCP label caused an unjustified patch rejection.
en135 | BASE | — | 0.00 | We selected this historic issue after inspecting candidate sources, so it is an exploratory, nonblind example, not a prospective F38 cohort.
en136 | BASE | — | 0.00 | · The author of later corrected an initial complaint about regex handling on nested paths, stating that the regex problem did not reproduce in isolation.
en137 | BASE | — | 0.00 | This correction should not be mixed with the separate remaining report about method handling between static and parameterized routes.
en138 | BASE | — | 0.00 | Source chronology and author revisions are part of the evidence needed for a legitimate maintenance judgment, not extra facts inferable from a source-only design label.
en139 | BASE | — | 0.00 | We built a small catalog based on Meyer’s example.
en140 | BASE | — | 0.00 | The client in client.py displays each publication through the catalog function passed to it.
en141 | BASE | — | 0.00 | The patch adds reports.py to wrap that function.
en142 | BASE | — | 0.00 | The source of catalog.py and client.py stays identical.
en143 | BASE | — | 0.00 | The resulting catalog displays technical reports and still rejects errata.
en144 | BASE | — | 0.00 | For books it now prints BOOK where it used to print book .
en145 | BASE | — | 0.00 | Suppose the only new requirement is to handle technical reports.
en146 | BASE | — | 0.00 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en147 | BASE | — | 0.00 | If the book output is outside the contract, the same patch can be accepted.
en148 | BASE | — | 0.00 | Table 2 applies both contracts again when errata are also required.
en149 | BASE | — | 0.00 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en150 | BASE | — | 0.00 | Excluding the book prefix from our stipulated contract is not evidence that real users have no expectation about it; it only means this example does not impose that obligation.
en151 | BASE | — | 0.00 | Two requirements for accepting a fixed patch.
en152 | BASE | — | 0.00 | Learning that errata are required leaves the last two rows of Table 2.
en153 | BASE | — | 0.00 | Both reject the patch, so the book contract need not be settled first.
en154 | BASE | — | 0.00 | Learning that technical reports are the whole request leaves the first two rows.
en155 | BASE | — | 0.00 | One accepts and one rejects.
en156 | BASE | — | 0.00 | The next question is whether the original book output is protected.
en157 | BASE | — | 0.00 | The procedure applies only if the actual specification is among these four authored cases.
en158 | BASE | — | 0.00 | If disclosure rules out every row, an empty candidate set is a reason to question the evidence or the candidate set, not to infer acceptance or rejection.
en159 | BASE | — | 0.00 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en160 | BASE | — | 0.00 | The reviewer can give a conditional answer or defer judgment.
en161 | BASE | — | 0.00 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en162 | BASE | — | 0.00 | Minimum evidence for a decision.
en163 | BASE | — | 0.00 | Let $E$ indicate that errata support is required and $B$ that the previous book prefix is protected.
en164 | BASE | — | 0.00 | Within the four stipulated specifications, the acceptance predicate is $A(E,B)=\neg E\land\neg B$.
en165 | BASE | — | 0.00 | Its unique inclusion-minimal acceptance certificate is $\{\neg E,\neg B\}$; the two separate minimal rejection certificates are $\{E\}$ and $\{B\}$.
en166 | BASE | — | 0.00 | With both facts withheld, an accepting specification $(E=0,B=0)$ and a rejecting specification $(E=1,B=0)$ remain compatible, so deferral has explicit countermodels.
en167 | BASE | — | 0.00 | After confirming reports-only ($\neg E$), asking whether the book prefix is protected determines the verdict.
en168 | BASE | — | 0.00 | With both fields initially unknown, neither one binary question guarantees a verdict for every possible answer.
en169 | BASE | — | 0.00 | These are classical finite Boolean and version-space facts, not new inference rules.
en170 | BASE | — | 0.00 | A separate Python replay checked the four worlds, nine disclosure states, inclusion-minimal certificates, contradictory evidence, and pairs of opposite-verdict worlds for deferred states; its passed.
en171 | BASE | — | 0.00 | That verifies the bounded decision logic, not actual human decisions or complete source behavior.
en172 | BASE | — | 0.00 | Learning more about a fixed contract removes possible worlds; renegotiating that contract changes the legitimate obligation.
en173 | BASE | — | 0.00 | The two transitions must not be conflated.
en174 | BASE | — | 0.00 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en175 | BASE | — | 0.00 | It adds one module, handles technical reports and errata, and keeps the original book output.
en176 | BASE | — | 0.00 | A rejection in Table 2 need not end the search for a patch within that boundary.
en177 | BASE | — | 0.00 | The contribution is not a new logical rule: it is a concrete account of why knowing that errata are required settles this decision, whereas a reports-only demand leaves the book-output commitment to be checked.
en178 | BASE | — | 0.00 | Applying it to a real review would require finding that commitment in a request, API documentation, tests or caller records.
en179 | BASE | — | 0.00 | · Sensitivity to an additional binding obligation.
en180 | BASE | — | 0.00 | The preceding approval depends on assuming that the two listed facts exhaust the criteria that matter.
en181 | BASE | — | 0.00 | Suppose, as another author-stipulated condition, that this same patch would violate a separate obligation if it were binding; let $C$ indicate whether that third obligation applies.
en182 | BASE | — | 0.00 | Under the stricter criterion $A_3(E,B,C)=\neg E\land\neg B\land\neg C$, the universe has eight complete specifications and twenty-seven partial disclosure states.
en183 | BASE | — | 0.00 | Exhaustive evaluation yields one ACCEPT, nineteen REJECT and seven DEFER states.
en184 | BASE | — | 0.00 | Crucially, evidence that both $E$ and $B$ are false no longer suffices to approve while $C$ remains unknown: the previous ACCEPT becomes DEFER.
en185 | BASE | — | 0.00 | If $C$ is explicitly false, the prior nine-state table and its one/five/three distribution are recovered.
en186 | BASE | — | 0.00 | This is not an empirically observed safety or performance defect.
en187 | BASE | — | 0.00 | The third obligation and stronger criterion were authored for sensitivity analysis.
en188 | BASE | — | 0.00 | The point is narrower: one cannot generalize an approval from the original four-world set without evidence that the listed obligations exhaust the relevant acceptance conditions.
en189 | BASE | — | 0.00 | Reviewers are not thereby required to investigate arbitrary imaginable obligations; a binding requirement still needs a legitimate source and scope.
en190 | BASE | — | 0.00 | [Enumeration code](./paper_b_three_obligation_sensitivity.py) · [regression tests](./test_paper_b_three_obligation_sensitivity.py).
en191 | BASE | — | 0.00 | Deciding whether to accept a completed patch differs from choosing an architecture for future edits.
en192 | BASE | — | 0.00 | We retain one observation relevant to acceptance.
en193 | BASE | — | 0.00 | In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected bracketed=True .
en194 | BASE | — | 0.00 | A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.
en195 | BASE | — | 0.00 | The presence of a feature is different from its availability along a required route .
en196 | BASE | — | 0.00 | Unless the original entry point and its compatibility obligations are identified, implementation through a separate function cannot by itself establish that the requested behavior is available to existing callers.
en197 | BASE | — | 0.00 | The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in Paper B 통합 원고 12 · 한·영 문장 교정 and its .
en198 | BASE | — | 0.00 | AI-assisted review can make structural patterns easier to classify and explain without automatically establishing which maintenance actions a classification warrants.
en199 | BASE | — | 0.00 | We propose calling this gap the principle-to-patch transport problem .
en200 | BASE | — | 0.00 | The term is a proposed research focus, not a declaration that requirements engineering, behavioral contracts, or validation theory overlooked the problem.
en201 | BASE | — | 0.00 | It recommends separating three evaluands: the accuracy of a principle classification, the downstream approve/reject decision, and the authority of the specific requirements and preserved old-client promises that make the
en202 | BASE | — | 0.00 | Such transport need not always be defective: a correctly scoped structural warning may genuinely help a project preserve intended changes.
en203 | BASE | — | 0.00 | The question is when its evidence supports a particular action, and with what uncertainty.
en204 | BASE | — | 0.00 | Drawing a square first establishes what a routine does, not whether it must be edited.
en205 | BASE | — | 0.00 | That depends on whether sorting belongs to the routine's obligations.
en206 | BASE | — | 0.00 | In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required.
en207 | BASE | — | 0.00 | We did not observe a real OCP label being misused to reject a patch.
en208 | BASE | — | 0.00 | We asked what additional grounds a design-principle assessment needs before it can justify an engineering decision .
en209 | BASE | — | 0.00 | Four falsifiable directions.
en210 | BASE | — | 0.00 | First, do code-only reviewers given a principle label misapply real acceptance criteria more often than reviewers also supplied authentic requests and API commitments?
en211 | BASE | — | 0.00 | Second, how frequently do principle-citing review comments identify a binding requirement or preserved caller obligation, and is that associated with disposition?
en212 | BASE | — | 0.00 | Third, how do reviewers judge a patch that implements a feature through a new entry point but not the existing required call path?
en213 | BASE | — | 0.00 | Fourth, do conditional design policies predict maintenance impact on newly requested changes better than unconditional prohibitions?
en214 | BASE | — | 0.00 | These are proposals, not findings .
en215 | BASE | — | 0.00 | A conventional requirements-traceability review with equivalent sources and budget is an essential competitor; if it matches or outperforms the proposed framework, no distinct performance gain should be claimed.
en216 | BASE | — | 0.00 | Likewise, some traditional design principles may be strongly predictive under well-defined conditions, which this agenda should recover rather than dismiss.
en217 | BASE | — | 0.00 | A practical review should first ask not only whether the patch implements a feature but where the request or an authorized agreement requires that feature to be reachable.
en218 | BASE | — | 0.00 | The reviewer should then locate the source of each protected old-client obligation in requests, API documentation, tests and actual call paths, without automatically treating every observed response as a promise.
en219 | BASE | — | 0.00 | If those sources leave different legitimate contracts possible, asking who can settle the obligation is more defensible than turning an OCP label into a categorical rejection.
en220 | BASE | — | 0.00 | Conversely, a demonstrated failure to meet an already binding new demand may reject the fixed patch before every other old-client promise is resolved.
en221 | BASE | — | 0.00 | This sequence is a recommendation derived from our authored example, not evidence that it reduces actual review costs in an organization.
en222 | BASE | — | 0.00 | Keeping the specifications compatible with known facts and checking their verdicts is elementary logic.
en223 | BASE | — | 0.00 | The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository.
en224 | BASE | — | 0.00 | Our evidence is confined to one benchmark archive, authored executable examples, an authored logical sensitivity check, and two post hoc selected external issue threads.
en225 | BASE | — | 0.00 | We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.
en226 | BASE | — | 0.00 | The audits in Sections 3–4 read the archived JSON and JSONL as data.
en227 | BASE | — | 0.00 | A separate script reproduced sixteen JSONL files, 768 rows, 48 distinct submissions, 24 scaffolds and 64 fixed model–strategy–language groups, and counted Python comments in four of twelve unique submissions.
en228 | BASE | — | 0.00 | Section 5 and the call-path check in Section 6 use examples written for this study.
en229 | BASE | — | 0.00 | The shape-layout experiment and Figure 1 remain preserved in manuscript 12; manuscript 21 does not reframe them as a new measured maintenance-cost trial.
en230 | BASE | — | 0.00 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en231 | BASE | — | 0.00 | The table below gives the nine verdicts for Section 5.
en232 | BASE | — | 0.00 | Both values of a withheld field remain possible.
en233 | BASE | — | 0.00 | Defer means that the compatible rows include both acceptance and rejection. - Meyer, B.
en234 | BASE | — | 0.00 | Object-Oriented Software Construction (1st ed.), pp.
en235 | BASE | — | 0.00 | The Open–Closed Principle . . - Jones, C.
en236 | BASE | — | 0.00 | Development Methods for Computer Programs Including a Notion of Interference .
en237 | BASE | — | 0.00 | Oxford University Computing Laboratory, PRG-25.
en238 | BASE | — | 0.00 | · . - Pehlivan, F., Ergüzen, A.
en239 | BASE | — | 0.00 | M., Lami, M., & Koyuncu, A.
en240 | BASE | — | 0.00 | An Empirical Study on Prompting LLMs to Detect Design Principle Violations .
en241 | BASE | — | 0.00 | ASE 2025 NIER. . - Bräuer et al.
en242 | BASE | — | 0.00 | Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research . . - Cabral et al.
en243 | BASE | — | 0.00 | Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding . . - Zhu, H., Zhang, Q., Wang, J., Yang, Z., & Qiu, Y.
en244 | BASE | — | 0.00 | Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits . . - Kane, M.
en245 | BASE | — | 0.00 | Validating the Interpretations and Uses of Test Scores .
en246 | BASE | — | 0.00 | Journal of Educational Measurement , 50(1), 1–73.
en247 | BASE | — | 0.00 | · . - Zave, P., & Jackson, M.
en248 | BASE | — | 0.00 | Four Dark Corners of Requirements Engineering .
en249 | BASE | — | 0.00 | ACM Transactions on Software Engineering and Methodology , 6(1), 1–30.
en250 | BASE | — | 0.00 | T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S.
en251 | BASE | — | 0.00 | The Oracle Problem in Software Testing: A Survey .
en252 | BASE | — | 0.00 | IEEE Transactions on Software Engineering .
en253 | BASE | — | 0.00 | · . - Widyasari, R., Zhang, T., Bouraffa, A., Maalej, W., & Lo, D.
en254 | BASE | — | 0.00 | Explaining Explanations: An Empirical Study of Explanations in Code Reviews .
en255 | BASE | — | 0.00 | ACM Transactions on Software Engineering and Methodology , 34(6), Article 177.
en256 | BASE | — | 0.00 | · . - Papotti, A., Paramitha, R., & Massacci, F.
en257 | BASE | — | 0.00 | On the acceptance by code reviewers of candidate security patches suggested by Automated Program Repair tools .
en258 | BASE | — | 0.00 | Empirical Software Engineering , 29, Article 132.
en259 | BASE | — | 0.00 | · . - Jin, H., & Chen, H.
en260 | BASE | — | 0.00 | Are LLMs Reliable Code Reviewers?
en261 | BASE | — | 0.00 | Systematic Overcorrection in Requirement Conformance Judgement .
en262 | BASE | — | 0.00 | · . - Ling, M., Zou, J., & Liu, X.
en263 | BASE | — | 0.00 | Negotiating Completion in Agentic Software Work: Acceptance Boundaries and Deferred Requirements .
en264 | BASE | — | 0.00 | 이 목록은 인용된 주요 자료를 확인할 수 있게 모은 집필용 서지이며, 서지형식·인용 위치·전수 대조를 마친 제출용 참고문헌은 아직 아니다.
en265 | BASE | — | 0.00 | / These are verified reading anchors, not yet a fully formatted submission bibliography.
en266 | BASE | — | 0.00 | Historical priority boundary.
en267 | BASE | — | 0.00 | Paper B's explicit conceptual genealogy in this research archive goes through early manuscript 01–02, the later “SOLID history and AI quasi-axiomatization” handoff, and the 2026-11-21 Plan B′ editorial debate.
en268 | BASE | — | 0.00 | Recovered Notion pages document the trajectory, but the earliest complete ChatGPT transcript could not be retrieved in this session.
en269 | BASE | — | 0.00 | Do not claim an unverified first-in-world date or independent discovery of requirements traceability, OCP conditionals, or Boolean information lattices.
en270 | BASE | — | 0.00 | Paper C: compare design configurations under prospective new change requests and an equal-information rival; study whether structural success reverses with edit boundaries and old API obligations.
en271 | BASE | — | 0.00 | Paper D: estimate prevalence and outcomes of AI-assisted principle citation in real reviews using independent annotators and provenance-coded requests.
en272 | BASE | — | 0.00 | EvoNOMOS mainline: search for generalizable conditional mechanisms of source organization without claiming broad proofs from a selected set of Go routers.
en273 | BASE | — | 0.00 | Formalization ceiling: a position paper does not require proving a general program equivalence or an undecidable semantic relation.
en274 | BASE | — | 0.00 | Any future claim of universal soundness, completeness, impossibility, P/NP separation or measured performance advantage would require a precisely stated formal/empirical problem and separate verification.
en275 | BASE | — | 0.00 | General program semantic equivalence and P-versus-NP complexity are distinct questions; no reduction or complexity ranking is proposed here.
en276 | BASE | — | 0.00 | Methodological authority: Meyer/Martin and later review studies are historical interlocutors and empirical competitors, not unquestionable authorities.
en277 | BASE | — | 0.00 | If newer source-specific evidence supports a narrower or contrary conclusion, revise the candidate principle and document the contradiction.
Summary en: SAME 0, EDIT 0, NEW 0

## v22 · [Source](https://app.notion.com/p/41fef561cf9281019920ff51bb84ae91)
### ko (243 sentences)
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
ko013 | NEW | ko078 | 0.05 | 2026년 7월 29일 EvoNOMOS 0.5 채팅 원문에서는 설계 원칙과 강제 규칙을 구별하면서 Codex·Claude Code 같은 코딩 도구가 SOLID를 마치 공리처럼 다룰 가능성에 의문을 제기했다.
ko014 | NEW | ko080 | 0.03 | 당시부터 제안된 연구 방향은 그 원칙을 수학으로 전부 환원하는 것이 아니라, 설계 조언이 어느 경로로 명령의 권위를 얻는지 역사와 실제 코드로 살펴보고, 그 권위가 부당하다면 반례로 수정하자는 것이었다.
ko015 | NEW | ko100 | 0.08 | 이 두 자료는 아이디어의 연구 내부 연대기 를 확인해 주지만, AI가 이미 그런 행동을 보인다는 사실이나 세계 최초 발견권을 입증하지는 않는다.
ko016 | NEW | ko082 | 0.02 | 논리적 공리화는 공리, 추론 규칙, 적용 범위를 밝히고 그 결과를 증명하는 정당한 수학적 작업이다.
ko017 | NEW | ko009 | 0.03 | 전문 직역에서의 정전(canon) 형성은 교육과 실무 관행에 관한 역사적 현상이다.
ko018 | NEW | ko101 | 0.03 | 우리가 새로 검증하자고 제안하는 운영상의 준공리화 는 특정 코딩 에이전트나 평가 루프가 개별 프로젝트의 요구·계약에 반대되는 근거가 제시되었는데도 원칙의 이름을 절대적 선택 기준으로 취급하는 행동이다.
ko019 | NEW | ko130 | 0.08 | 어떤 수정안을 거절하는 것이 정당한지는 다시 별개의 규범적 질문이다.
ko020 | NEW | ko076 | 0.03 | 이 네 현상을 한데 섞으면 설계 원칙의 역사, 모델 훈련, 프롬프트 반응과 개발자의 승인 행동을 잘못된 인과관계로 묶게 된다.
ko021 | SAME | ko013 | 1.00 | 마틴은 1996년 글에서 베르트랑 마이어의 1988년 초판 23쪽을 인용했다.
ko022 | SAME | ko014 | 1.00 | 마이어에게 닫힌 모듈은 다른 모듈이 안정된 명세에 기대어 쓸 수 있는 모듈이다.
ko023 | SAME | ko015 | 1.00 | 그의 도서관 예제에서 자료 유형을 하나씩 구별해 처리하는 프로그램에 기술보고서를 추가하면, 기존 모듈까지 고치거나 다시 컴파일해야 할 수 있다.
ko024 | SAME | ko016 | 1.00 | 새 자료를 처리하는 코드의 위치에 따라 기존 모듈에 손이 가는 범위가 달라진다.
ko025 | SAME | ko017 | 1.00 | 1995년 6월 공개 토론에서 카일 브라운은 잘못 설계된 클래스라면 소스를 고칠 수 있어야 한다고 했다.
ko026 | SAME | ko018 | 1.00 | 마틴은 예상한 확장을 위해 기존 소스를 반드시 고쳐야 하는지를 물었다.
ko027 | SAME | ko019 | 1.00 | 그러려면 어떤 변경이 생길지 미리 짚어야 한다.
ko028 | SAME | ko020 | 1.00 | 2007년 공개 기록에는 다섯 원칙을 묶은 SOLID라는 이름이 나온다.
ko029 | SAME | ko021 | 1.00 | 2009년 인터페이스 논쟁에서는 내부 클래스와 공개 플러그인 API에 서로 다른 조언이 제시됐다.
ko030 | SAME | ko022 | 1.00 | 이 기록은 당시 원칙을 적용하거나 반대할 때 어떤 이유를 제시했는지 보여 준다.
ko031 | SAME | ko023 | 1.00 | SOLID라는 이름이 널리 퍼지면서 적용 조건에 대한 판단이 실제로 변했는지는 별도의 역사적 증거가 필요하다.
ko032 | SAME | ko024 | 1.00 | · · 마틴은 목록 정렬을 DrawAllShapes 가 맡게 했다.
ko033 | SAME | ko025 | 1.00 | 한 구현에서 Circle::Precedes 는 상대 도형이 사각형이면 원을 먼저 놓는다.
ko034 | SAME | ko026 | 1.00 | 원과 세 번째 도형의 순서를 정하려면 Circle 도 고쳐야 할 수 있다.
ko035 | SAME | ko027 | 1.00 | 반면 도형 종류별 순서를 표에 두면 사각형을 먼저 놓기 위해 표의 두 항목만 바꾸면 된다.
ko036 | SAME | ko028 | 1.00 | 개별 도형을 넓이순으로 그리려면 그 표에 없는 정보가 필요하다.
ko037 | SAME | ko029 | 1.00 | 마틴이 글 후반에 비교한 두 함수는 dynamic_cast 를 쓴다.
ko038 | SAME | ko030 | 1.00 | DrawAllShapes 의 한 구현은 원과 사각형을 골라 그리고, DrawSquaresOnly 는 사각형만 그린다.
ko039 | SAME | ko031 | 1.00 | 모든 도형을 그려야 할 때는 출력이 하나 빠진 셈이다.
ko040 | SAME | ko032 | 1.00 | 코드와 프롬프트만 주어진 검토자는 각 함수에 어느 책임이 있는지 어디까지 알 수 있을까?
ko041 | SAME | ko033 | 1.00 | · · 우리는 서로 다른 두 자료를 사용했다.
ko042 | SAME | ko034 | 1.00 | 벤치마크에서는 분류를 요구받은 모델에게 실제로 어떤 입력이 주어졌는지 조사했다.
ko043 | SAME | ko035 | 1.00 | 도서관 예제에서는 패치 한 개를 고정하고, 적용할 요구와 보호할 계약을 바꿔 가며 실행 결과와 승인 기준을 대조했다.
ko044 | SAME | ko036 | 1.00 | 벤치마크의 저장 코드와 도서관 코드는 별개이고, 어느 쪽에도 실제 검토자의 승인·거절 판단은 포함되지 않는다.
ko045 | SAME | ko037 | 1.00 | OCP 참조 자료에는 위반 사례와 수정 사례를 묶은 코드 쌍 48개가 있다.
ko046 | SAME | ko038 | 1.00 | 저장 응답은 16개 JSONL 파일에 48행씩, 총 768행이다.
ko047 | SAME | ko039 | 1.00 | 정확한 소스 문자열 기준으로 구별한 제출 코드는 48개이고 각각 16회 나타났다.
ko048 | SAME | ko040 | 1.00 | 각 저장 행에 제출 코드가 프롬프트에 정확히 한 번 들어 있는지 확인한 뒤 공통 표시로 바꿔 나머지 지시문을 비교했다.
ko049 | SAME | ko041 | 1.00 | 모델·전략·언어를 고정한 64개 조합 각각에서는 12개 코드에 같은 지시문 틀이 사용됐다.
ko050 | SAME | ko042 | 1.00 | 768행을 독립적인 유지보수 사례 768개로 취급하지 않는다.
ko051 | SAME | ko043 | 1.00 | 지시문에 구체적인 변경 요구나 보호할 기존 호출이 따로 적혀 있는지는 문자열 집계와 구별해 판독했다.
ko052 | SAME | ko044 | 1.00 | 다형성으로 처리할 분기를 찾으라는 지시는 분류의 단서이지만, 삼각형을 추가하라는 개별 요청과는 다르다.
ko053 | SAME | ko045 | 1.00 | 이 판독은 제출 코드를 가린 지시문에 관한 것이다.
ko054 | SAME | ko046 | 1.00 | 독립 감사에서 Python 저장 행 192개를 이루는 고유 코드 12개를 검사하자 4개에서 주석 토큰 46개를 발견했고, docstring을 포함한 코드는 없었다.
ko055 | SAME | ko047 | 1.00 | 주석이 기능의 의도를 암시할 수 있으므로, 지시문에 개별 요구가 없다는 사실을 코드 전체에 명세 단서가 없다는 주장으로 확대하지 않았다.
ko056 | SAME | ko048 | 1.00 | 다른 세 언어의 주석은 같은 방법으로 계수하지 않았다.
ko057 | SAME | ko049 | 1.00 | 저장된 제출 코드와 48개 참조 쌍의 양쪽 소스를 원문, 양끝 공백 제거, 모든 공백 제거 기준으로 대조했다.
ko058 | SAME | ko050 | 1.00 | Python 코드에 대해서는 구문 트리(AST)도 비교했고, 참조 쌍에서 사라진 공개 메서드 선언을 별도로 확인했다.
ko059 | SAME | ko051 | 1.00 | 이 검사로 메서드의 상속 가능성, 실제 사용 여부, 보호하기로 한 계약을 확정하지는 않는다.
ko060 | SAME | ko052 | 1.00 | 압축 파일 안의 코드 자체는 실행하지 않았다.
ko061 | SAME | ko053 | 1.00 | 도서관 예제에서는 원본 소스와 수정안, 호출 입력, 새 모듈을 추가할 수 있다는 편집 범위를 고정했다.
ko062 | SAME | ko054 | 1.00 | 코드 실행으로 확인한 것은 구체적인 입력에서 나온 출력과 예외다.
ko063 | SAME | ko055 | 1.00 | 반면 기술보고서·정오표 중 무엇을 요구하는지, 책 출력의 접두어가 보호 대상인지, 새 요구를 충족하면서 보호된 기존 동작을 보존해야 승인한다 는 기준은 모두 연구자가 정했다.
ko064 | SAME | ko056 | 1.00 | 따라서 §5의 표는 독립 심사위원의 판정이 아니라 우리가 지정한 기준을 실행 관찰에 적용한 결과다.
ko065 | SAME | ko057 | 1.00 | 일부 전제만 공개한 경우에는 두 요구와 두 계약으로 이루어진 후보 명세 중 공개된 사실과 맞는 것만 남겼다.
ko066 | SAME | ko058 | 1.00 | 이 후보군 밖의 실제 요구나 계약까지 조사했다고 가정하지 않는다.
ko067 | SAME | ko059 | 1.00 | · · · · Paper B · Claude 심사 판정 및 원본 ZIP 독립 재감사 (2026-11-21) Pehlivan 등은 위반 시나리오를 정하고 생성된 코드 예시를 다듬었다.
ko068 | SAME | ko060 | 1.00 | 두 번째 저자가 참조 쌍의 정확성과 일관성을 독립적으로 확인했고, 이견은 논의로 해결했다.
ko069 | SAME | ko061 | 1.00 | 모델의 분류 결과는 그 참조 라벨과 대조했다.
ko070 | SAME | ko062 | 1.00 | OCP 저장 응답의 제출 코드를 가리자 지시문 틀 24개가 남았다.
ko071 | SAME | ko063 | 1.00 | DEFAULT 4개, ENSEMBLE 8개, EXAMPLE 8개, SMELL 4개였다.
ko072 | SAME | ko064 | 1.00 | 어느 틀에도 개별 변경 요구나 보호할 호출자 계약을 따로 적은 문구는 없었다.
ko073 | SAME | ko065 | 1.00 | 추가 감사에서는 ENSEMBLE과 EXAMPLE에 같은 언어라도 모델별로 두 가지 틀이 쓰였음을 확인했다. gpt-4o-mini 와 나머지 세 모델의 지시문이 달랐으며, 정확한 (모델·전략·언어) 조합을 고정하면 12개 코드에 같은 지시가 적용됐다.
ko074 | SAME | ko066 | 1.00 | 저장 코드는 참조 쌍과 모든 공백을 제거해 비교해도 일치하지 않았고, 저장된 Python 192행도 참조 측 Python AST와 같은 경우가 없었다.
ko075 | SAME | ko067 | 1.00 | 이 결과는 코드들이 서로 관련 없는 문제를 다룬다는 의미까지 증명하지 않는다.
ko076 | SAME | ko068 | 1.00 | Python EXAMPLE 의 한 프롬프트는 다형성으로 처리할 만한 반복 분기를 찾으라고 한다.
ko077 | SAME | ko069 | 1.00 | 제출된 AreaCalculator 는 도형의 종류를 확인해 원과 사각형의 넓이를 계산한다.
ko078 | SAME | ko070 | 1.00 | 새 도형을 지원한다면 이 분기가 수정 후보가 된다.
ko079 | SAME | ko071 | 1.00 | 다만 그 변경이 실제로 요청됐는지, 넓이 계산을 옮긴 뒤에도 기존 너비 조회를 지원해야 하는지는 지시문에 적혀 있지 않다.
ko080 | SAME | ko072 | 1.00 | 별도 참조 쌍 37번에서는 넓이 계산을 도형 메서드로 옮기면서 Rectangle.get_width 선언을 뺐다.
ko081 | SAME | ko073 | 1.00 | 저장 코드와 참조 쌍은 앞에서 명시한 문자열 정규화 기준에서 일치하지 않았으며, Python 코드에 한한 AST 비교에서도 일치 사례가 없었다.
ko082 | SAME | ko074 | 1.00 | 따라서 37번 쌍은 선언이 빠진 사실을 확인하는 데만 쓴다.
ko083 | SAME | ko075 | 1.00 | 그 삭제를 이유로 수정안을 거절하려면, 기존 호출자에게 너비 조회를 계속 제공하기로 했다는 근거가 필요하다.
ko084 | SAME | ko076 | 1.00 | 프롬프트 예시는 저장 JSONL의 13행(ID 12)에 있다.
ko085 | SAME | ko077 | 1.00 | 참조 쌍 37번은 별도 참조 JSON에 있다.
ko086 | SAME | ko078 | 1.00 | · · · Bräuer 등(2018)은 설계 원칙을 어떻게 측정할지 전문가에게 물었고, Cabral 등(2024)은 SOLID를 적용한 코드를 이해하고 확장하는 경험을 조사했다.
ko087 | SAME | ko079 | 1.00 | Zhu 등(2026)은 구체적인 저장소 변경 과제에 기능 및 구조 검사를 결합했다.
ko088 | SAME | ko080 | 1.00 | 우리의 벤치마크 감사도 분류 성능을 부정하려는 것이 아니다.
ko089 | SAME | ko081 | 1.00 | 분류에 성공했다는 증거를 수정안 거절의 증거로 옮길 때 무엇이 더 필요한지를 묻는다.
ko090 | SAME | ko082 | 1.00 | · · 실제 리뷰 연구는 이 논문의 주장 범위를 더 엄격하게 제한한다.
ko091 | SAME | ko083 | 1.00 | Widyasari 등(2025)은 Gerrit 코드 리뷰 댓글 793건을 분석하고 규칙이나 원칙을 근거로 드는 설명 유형을 확인했다.
ko092 | SAME | ko084 | 1.00 | 이는 원칙에 의거한 설명이 리뷰에 존재한다는 증거지만, 원칙이 잘못 적용돼 특정 수정안이 거절됐다는 증거는 아니다.
ko093 | SAME | ko085 | 1.00 | Papotti 등(2024)은 컴퓨터과학 석사과정 학생 72명을 대상으로 보안 자동 수리 패치의 채택 여부를 실험했다.
ko094 | SAME | ko086 | 1.00 | 제안 도구의 전문성을 알리는 정보에 따라 판단이 바뀌는 현상을 관찰했지만, 원칙 위반 라벨을 대상으로 한 연구는 아니다.
ko095 | SAME | ko087 | 1.00 | 두 논문의 실제 사람에 대한 관측은 우리가 구성한 표 2의 승인 기준과 다르다.
ko096 | SAME | ko088 | 1.00 | · Jin과 Chen(2026)은 정답 코드와 결함 코드에 대한 다섯 언어 모델의 요구 적합성 판단을 세 프로그래밍 벤치마크에서 실험하고, 맞는 코드를 잘못 거절하는 현상과 설명·수정 제안을 요구하는 프롬프트의 위험을 보고했다.
ko097 | SAME | ko089 | 1.00 | 따라서 LLM의 과잉 거절을 처음 지적했다고 주장할 수 없다.
ko098 | SAME | ko090 | 1.00 | Ling·Zou·Liu(2026)는 공개 GitHub 변경 사례의 질적 연구에서 병합, 이슈 종료, 요구 충족이 서로 다른 결과일 수 있음을 논증했다.
ko099 | SAME | ko091 | 1.00 | 수용 경계가 조건부라는 발견도 우리의 최초성이 아니다.
ko100 | SAME | ko092 | 1.00 | 우리 사례는 실행 결과가 고정된 패치에서 현재 공개된 요구·계약이 정당화하는 판정과 추가 질문을 정확하게 분리하는 재현 가능한 실례 다.
ko101 | SAME | ko093 | 1.00 | · 그 질문 자체에도 중요한 선행연구가 있다.
ko102 | SAME | ko094 | 1.00 | Kane(2013)은 검사 점수의 해석을 뒷받침하는 증거가 그 점수를 특정 결정에 사용하는 일까지 정당화하지는 않는다고 논했다.
ko103 | SAME | ko095 | 1.00 | 이는 소프트웨어 리뷰를 실험한 결과가 아니라, 평가 결과의 사용 을 따로 정당화해야 한다는 일반적인 논증이다.
ko104 | SAME | ko096 | 1.00 | Zave와 Jackson(1997)은 요구사항, 기계 명세, 환경에 관한 지식이 어떻게 연결되는지 설명하면서 행위의 통제 주체를 구별했다.
ko105 | SAME | ko097 | 1.00 | 원을 앞에 정렬할 책임이 호출자에게 있는지 함수에 있는지부터 따져야 한다는 우리의 질문도 이러한 오래된 문제의 한 사례다.
ko106 | SAME | ko098 | 1.00 | 존스(1981) 역시 병렬 프로그램에서 환경 의존 조건과 프로그램 보장 조건의 양립을 다뤘다.
ko107 | SAME | ko099 | 1.00 | · · Barr 등(2015)이 정리한 테스트 오라클 문제는 코드 실행과 올바름 판정 사이에도 근거가 필요함을 상기시킨다.
ko108 | SAME | ko100 | 1.00 | §5의 시험은 지정된 호출의 동작을 확인하지만, 그 동작을 보존하겠다는 실제 프로젝트의 약속을 입증하지는 않는다.
ko109 | SAME | ko101 | 1.00 | 따라서 다음 절의 요구·계약은 발견한 사실이 아니라 명시적으로 정한 전제다.
ko110 | SAME | ko102 | 1.00 | 위반 범주를 맞혔다는 사실은 코드에 특정 구조가 있다는 평가를 뒷받침한다.
ko111 | SAME | ko103 | 1.00 | 그러나 수정안을 거절하려면 (1) 누구에게서 나온 새 요구인지, (2) 기존 호출자에게 계속 보장하기로 한 동작이 무엇인지, (3) 그 동작과 새 기능을 어느 호출 경로로 제공해야 하는지까지 알아야 한다.
ko112 | SAME | ko104 | 1.00 | 이 가운데 일부는 소스에 표시될 수 있지만, 관측한 구현이 곧 승인된 계약이라는 뜻은 아니다.
ko113 | SAME | ko105 | 1.00 | 예컨대 같은 출력 변경을 보고도 책 출력이 보호 대상일 때와 아닐 때는 서로 다른 판정이 가능하다.
ko114 | SAME | ko106 | 1.00 | 분류 라벨을 고정한 채 판정이 달라지는 반례는 §5에서 실행한 동일 패치의 네 명세에 한정된다.
ko115 | SAME | ko107 | 1.00 | 이를 통해 분류 점수 자체를 부정하거나 실제 리뷰어가 라벨 때문에 패치를 거절했다고 주장하지 않는다.
ko116 | SAME | ko108 | 1.00 | 이 주장은 분류기에 어떤 정보를 주는지에 따라서도 달라진다.
ko117 | SAME | ko109 | 1.00 | 소스 코드만 보고 OCP 위반 여부를 판정하는 분류기라면 코드가 고정된 네 명세에서 입력과 출력 라벨을 동일하게 유지한다.
ko118 | SAME | ko110 | 1.00 | 반면 실제 요구서와 호출자 계약을 입력받는 문맥 의존적 평가자는 명세에 따라 판단을 변경할 수 있다.
ko119 | SAME | ko111 | 1.00 | 따라서 이 논문의 반례는 모든 OCP 평가가 언제나 같은 라벨을 낸다는 주장이 아니라, 고정된 소스의 위반 라벨만으로 서로 다른 실제 유지보수 판정을 식별할 수 없다는 제한된 주장 이다.
ko120 | SAME | ko112 | 1.00 | 기존 요구사항 추적표나 호환성 검토 역시 추가 근거를 물어 문제를 해결할 수 있으므로, 이를 우리의 새 방법만이 수행한다고 해석하지 않는다.
ko121 | SAME | ko113 | 1.00 | 직접 작성하지 않은 사례에서도 요구와 동작을 분리할 수 있는지 살피기 위해 Go 웹 라우터 Chi의 공개 이슈 (2025년 5월 2일)를 그 후속 댓글과 함께 읽었다.
ko122 | SAME | ko114 | 1.00 | 작성자는 미들웨어 생성 함수가 같은 싱글턴 핸들러를 반환하면 중첩 라우터 그룹의 요청이 마지막 그룹에 전달되는 상황을 신고했다.
ko123 | SAME | ko115 | 1.00 | 다른 참여자는 생성 함수 호출마다 새 미들웨어 인스턴스를 반환하는 우회 코드를 제시했고, 원래 작성자는 그 방법을 이해한다고 답했다.
ko124 | SAME | ko116 | 1.00 | 그러나 작성자는 싱글턴을 그대로 써도 정상적인 라우팅이 되거나, 잘못된 재사용을 명시적으로 알려 주는 동작을 원한다는 점을 다시 밝혔다.
ko125 | SAME | ko117 | 1.00 | 따라서 새 인스턴스를 만들어 기존 세 경로에서 정답 응답이 나왔다는 사실이 확인되더라도, 그것을 싱글턴을 안전하게 지원해 달라는 원래 요청이 해결됐다는 증거로 바꿀 수는 없다.
ko126 | SAME | ko118 | 1.00 | 이 관찰은 Paper B에서 말하는 요구의 권위를 더 구체적으로 만든다.
ko127 | SAME | ko119 | 1.00 | 이슈의 기대 동작 , 참여자가 제안한 우회 수정 , 연구자가 선택한 테스트 통과 조건 은 서로 다른 자료다.
ko128 | SAME | ko120 | 1.00 | 원래 작성자가 제안된 우회를 알고 있다는 사실만으로 라이브러리 관리자가 API 계약 변경을 승인했다고 볼 수도 없다.
ko129 | SAME | ko121 | 1.00 | 반대로 이 이슈는 OCP 위반 분류가 실제 리뷰에서 잘못된 패치 거절을 일으켰다는 사례가 아니다.
ko130 | SAME | ko122 | 1.00 | 연구자가 이미 알려진 문제를 선택해 조사했으므로 독립적 전향 실험도 아니다.
ko131 | SAME | ko123 | 1.00 | · 또 다른 공개 이슈 에서는 작성자가 최초에 정규식 경로의 하위 경로 처리를 문제 삼았지만, 같은 날 후속 댓글에서 독립적인 재현 결과 그 부분은 문제가 아니었다고 정정했다.
ko132 | SAME | ko124 | 1.00 | 정적 경로와 매개변수 경로의 메서드 처리에 관한 나머지 문제와, 스스로 철회한 정규식 주장을 같은 수준의 확정 사실로 분류해서는 안 된다.
ko133 | SAME | ko125 | 1.00 | 이러한 출처 이력은 분류자가 읽는 코드만으로는 알 수 없는 정보이며, 이 논문이 제안하는 근거 확인 절차를 적용할 때 반드시 남겨야 하는 반대 사례다.
ko134 | NEW | ko042 | 0.02 | 2026년 10월 9일 작성한 는 다음 네 조건을 동일한 Go 유지보수 과제, 같은 소스 버전, 같은 기존 계약과 테스트, 동일한 도구 접근·시간 예산으로 비교하도록 했다.
ko135 | NEW | ko142 | 0.03 | NONE 은 추가 설계 원칙 지시가 없는 조건이다.
ko136 | NEW | ko020 | 0.06 | HARD_SOLID 는 무조건적인 SOLID 준수를 요구한다.
ko137 | NEW | ko009 | 0.07 | SCOPED_SOLID 는 요구 유형과 구조 변경의 범위에 따라 원칙을 적용하도록 한다.
ko138 | NEW | ko174 | 0.03 | EVIDENCE_CONDITIONAL 은 코드·실제 요구·보존 계약·대안을 비교하고 근거가 부족하면 기권하도록 한다.
ko139 | NEW | ko190 | 0.04 | 모든 조건은 각기 새로운 에이전트 문맥에서 실행하고 순서의 영향을 통제해야 한다.
ko140 | NEW | ko192 | 0.04 | 본 논문에는 해당 네 조건을 실제로 수행한 에이전트 결과가 없다.
ko141 | NEW | ko020 | 0.03 | 코드와 실행 테스트가 같은데 설명만 SOLID를 더 많이 인용한다면 어휘 반복(lexical echo) 가설이 지지되고, 이는 실제 설계 선택의 준공리화와 다르다.
ko142 | NEW | ko205 | 0.05 | 네 조건이 모두 기존 계약을 지키는 수정안을 만든다면 과제 명세·테스트가 지배한다 는 고전적인 대안 설명이 지지된다.
ko143 | NEW | ko020 | 0.05 | 무조건적 SOLID 지시가 어떤 과제에서는 유익할 가능성도 열어 둬야 한다.
ko144 | NEW | ko121 | 0.04 | 서로 다른 Go 과제에서 잘못된 거절·정답률·추가 추상화·반례 제시 후 수정 가능성 등을 별도로 측정해야 한다.
ko145 | NEW | ko010 | 0.02 | 이를 설계하기 전부터 예측한 방향만 보도하면 결과를 자료에 맞춘 문제가 발생한다.
ko146 | NEW | ko023 | 0.05 | 이 실험이 성공해도 입증되는 것은 그 프롬프트 조건이 해당 실행에서 미친 효과 이지, 특정 모델의 학습 자료에 SOLID가 포함됐다는 주장이나 산업 전체의 역사적 변화가 아니다.
ko147 | SAME | ko126 | 1.00 | 마이어의 도서관 예제를 작은 프로그램으로 만들었다. client.py 는 전달받은 목록 함수로 자료를 출력한다.
ko148 | SAME | ko127 | 1.00 | 수정안은 그 함수에 새 처리를 덧붙이는 reports.py 를 추가한다. catalog.py 와 client.py 의 소스는 그대로다.
ko149 | SAME | ko128 | 1.00 | 수정 후에는 기술보고서가 출력되고 정오표는 계속 거절된다.
ko150 | SAME | ko129 | 1.00 | 기존 책 출력에서는 접두어가 book 에서 BOOK 으로 바뀐다.
ko151 | SAME | ko130 | 1.00 | 책 출력을 그대로 돌려주기로 했다면 접두어가 바뀐 수정안을 거절한다.
ko152 | SAME | ko131 | 1.00 | 책 출력이 계약 밖이라면 같은 수정안을 승인할 수 있다.
ko153 | SAME | ko132 | 1.00 | 표 2는 이 두 계약을 정오표까지 지원해야 하는 경우에도 적용한다.
ko154 | SAME | ko133 | 1.00 | 두 계약 모두 학술지와 학회록의 출력, 그리고 정오표와 별개인 미지원 자료 유형의 거절 동작을 보호한다.
ko155 | SAME | ko134 | 1.00 | 책 접두어가 보호 대상이 아니라는 가정은 실제 이용자가 그 출력을 기대하지 않는다는 관찰이 아니다.
ko156 | SAME | ko135 | 1.00 | 단지 이 비교에서 보존 의무로 정하지 않았다는 뜻이다.
ko157 | SAME | ko136 | 1.00 | “정오표도 지원해야 한다”는 사실이 확인되면 표 2의 아래 두 행이 남는다.
ko158 | SAME | ko137 | 1.00 | “기술보고서만 필요하다”는 사실을 알면 위 두 행이 남는다.
ko159 | SAME | ko138 | 1.00 | 이때 확인할 것은 기존 책 출력이 보호 대상인지다.
ko160 | SAME | ko139 | 1.00 | 이 절차는 실제 명세가 표의 네 경우 중 하나라는 조건 아래서만 성립한다.
ko161 | SAME | ko140 | 1.00 | 공개된 사실과 맞는 행이 하나도 없다면 승인이나 거절을 내릴 것이 아니라 자료 또는 후보군이 잘못됐는지 확인해야 한다.
ko162 | SAME | ko141 | 1.00 | 두 판정이 모두 남으면 현재 정보만으로는 어느 경우에도 맞는 한 가지 판정을 내릴 수 없다.
ko163 | SAME | ko142 | 1.00 | 검토자는 조건부 판정을 제시하거나 결론을 보류할 수 있다.
ko164 | SAME | ko143 | 1.00 | 부록 A에는 요구와 계약의 공개 여부를 조합한 아홉 경우를 실었다.
ko165 | SAME | ko144 | 1.00 | 정오표 지원이 필수인지 여부를 $E$, 기존 책 출력 접두어를 보호하는지 여부를 $B$라고 두자.
ko166 | SAME | ko145 | 1.00 | 연구자가 정한 네 명세에 한정하면, 이 고정 패치의 승인 조건은 $A(E,B)=\neg E\land\neg B$다.
ko167 | SAME | ko146 | 1.00 | 따라서 승인에 필요한 최소 증거는 $\{\neg E,\neg B\}$이며, 거절을 확정하는 최소 증거는 $\{E\}$ 또는 $\{B\}$다.
ko168 | SAME | ko147 | 1.00 | 두 조건을 모두 알 수 없다면, 승인 명세 $(E=0,B=0)$와 거절 명세 $(E=1,B=0)$가 양립하므로 판정을 보류한다.
ko169 | SAME | ko148 | 1.00 | 기술보고서만 요구한다는 사실, 즉 $\neg E$가 확인되면 $B$를 물어 어느 쪽인지 결정할 수 있다.
ko170 | SAME | ko149 | 1.00 | 반면 두 조건이 전부 미공개일 때는 하나의 예·아니오 질문만으로 모든 답변에 대해 판정을 확정하지 못한다.
ko171 | SAME | ko150 | 1.00 | 이것은 새로운 논리 규칙이 아니라 고전적인 유한 정보 집합 판정이다.
ko172 | SAME | ko151 | 1.00 | 별도 Python 코드는 네 명세의 공개 상태 아홉 가지, 최소 승인·거절 증거, 보류 상태의 대립 명세, 모순된 사실의 처리까지 검사했고 가 통과했다.
ko173 | SAME | ko152 | 1.00 | 이 테스트가 실제 검토자의 판단이나 원본 도서관 프로그램의 전체 동작을 재검증한 것은 아니다.
ko174 | SAME | ko153 | 1.00 | 또한 고정된 계약에 관한 사실을 알게 되는 것 과 계약 자체를 변경하는 것 을 구별해야 한다.
ko175 | SAME | ko154 | 1.00 | 앞의 경우에는 가능한 명세의 집합이 줄지만, 뒤의 경우에는 승인 조건 자체가 달라질 수 있다.
ko176 | SAME | ko155 | 1.00 | 같은 편집 범위에서 더 강한 요구도 충족할 수 있는지 확인하기 위해 두 번째 수정안을 실행했다.
ko177 | SAME | ko156 | 1.00 | 새 모듈 하나로 기술보고서와 정오표를 모두 처리했고 기존 책 출력도 보존했다.
ko178 | SAME | ko157 | 1.00 | 표 2에서 검토 중인 수정안이 거절되더라도, 같은 범위에서 다른 수정안을 찾을 수 있다.
ko179 | SAME | ko158 | 1.00 | 이 비교에서 얻은 것은 새로운 논리 규칙이 아니다.
ko180 | SAME | ko159 | 1.00 | 한 사실만 알아도 거절이 확정되는 경우와, 책 출력 약속을 물어야 하는 경우를 구체적인 호출 결과로 구분한 것이다.
ko181 | SAME | ko160 | 1.00 | 실제 리뷰에 적용하려면 요구서와 API 문서, 테스트 및 호출 기록에서 그 약속의 근거를 따로 찾아야 한다.
ko182 | SAME | ko161 | 1.00 | · 계약 조건을 하나 더 추가했을 때의 민감도.
ko183 | SAME | ko162 | 1.00 | 위의 승인 규칙은 두 조건만 관련된다는 전제에 의존한다.
ko184 | SAME | ko163 | 1.00 | 이 고정 패치가 다른 독립적인 보호 의무도 위반한다고 연구자가 가정하고, 그 의무가 현재 실제로 적용되는지를 $C$라고 두자.
ko185 | SAME | ko164 | 1.00 | 세 의무 가운데 하나라도 적용되면 패치를 거절하도록 승인 기준을 새로 정하면 $A_3(E,B,C)=\neg E\land\neg B\land\neg C$가 된다.
ko186 | SAME | ko165 | 1.00 | 이때 네 명세는 여덟 가지 완전 명세로, 아홉 공개 상태는 스물일곱 공개 상태로 확장된다.
ko187 | SAME | ko166 | 1.00 | 전수 계산 결과는 승인 1개, 거절 19개, 보류 7개다.
ko188 | SAME | ko167 | 1.00 | 특히 예전 두 조건이 모두 거짓이라고 알더라도 $C$가 미공개라면 기존의 승인은 보류 로 바뀐다.
ko189 | SAME | ko168 | 1.00 | 반대로 $C$가 적용되지 않는다고 명시적으로 확인하면 원래의 아홉 상태와 승인 1·거절 5·보류 3 분포가 복원된다.
ko190 | SAME | ko169 | 1.00 | 이 계산은 실제로 새로운 보안·성능 결함을 발견했다는 뜻이 아니다.
ko191 | SAME | ko170 | 1.00 | $C$는 연구자가 만든 제삼의 독립 의무이고, 새 기준은 기존 승인 기준보다 엄격하다.
ko192 | SAME | ko171 | 1.00 | 그 목적은 필요한 요구를 전부 열거했다는 근거 없이 기존의 승인 판정을 일반화할 수 없음 을 드러내는 것이다.
ko193 | SAME | ko172 | 1.00 | 그렇다고 실제 검토자가 가능한 모든 요구를 무한히 조사해야 하는 것도 아니다.
ko194 | SAME | ko173 | 1.00 | 어떤 요구가 승인 기준에 포함되는지는 적격한 주체와 계약 출처에 의해 제한돼야 한다.
ko195 | SAME | ko174 | 1.00 | [전수 계산 코드](./paper_b_three_obligation_sensitivity.py) · [회귀 테스트](./test_paper_b_three_obligation_sensitivity.py).
ko196 | SAME | ko175 | 1.00 | 완성된 수정안을 승인할지 판단하는 일과 서로 다른 설계가 앞으로 어떤 편집 비용을 낳는지 비교하는 일은 다르다.
ko197 | SAME | ko176 | 1.00 | 여기서는 앞의 질문에 해당하는 관찰만 남긴다.
ko198 | SAME | ko177 | 1.00 | 도형 렌더링에 새 옵션을 더했을 때 새 함수에서는 대괄호 출력이 가능했지만, 기존 함수에 bracketed=True 를 넘기면 인자를 거절했다.
ko199 | SAME | ko178 | 1.00 | 요구가 새 진입점에서 옵션을 제공하는 것이라면 기능은 구현됐다.
ko200 | SAME | ko179 | 1.00 | 기존 호출자도 같은 옵션을 사용해야 한다면 요구를 충족하지 못한다.
ko201 | SAME | ko180 | 1.00 | 새 기능이 있다는 사실과 요구된 호출 경로에서 쓸 수 있다는 사실 은 다르다.
ko202 | SAME | ko181 | 1.00 | 보호해야 할 기존 진입점이 무엇인지 확인하지 않으면, 같은 옵션을 새 함수에서 제공했다는 사실만으로 수정안의 적합성을 판정할 수 없다.
ko203 | SAME | ko182 | 1.00 | 도형별·연산별 구조와 기존 파일 수정 수에 관한 비교는 별도의 설계 선택 문제이므로 Paper B 통합 원고 12 · 한·영 문장 교정 및 에 원형 그대로 보존했다.
ko204 | SAME | ko183 | 1.00 | AI가 코드의 구조를 분류하고 문제를 설명하는 일이 일반화될수록, 개발자가 받는 조언은 명료해질 수 있지만 분류 결과가 어떤 구체적 행동을 정당화하는지는 별도 문제로 남는다.
ko205 | SAME | ko184 | 1.00 | 우리는 이 간극을 \*\*원칙→수정안 판단의 전이 문제(principle-to-patch transport problem)\*\*라고 부르자고 제안한다.
ko206 | SAME | ko185 | 1.00 | 이 표현은 기존 요구공학·계약 이론·검증 이론에서 비슷한 문제를 다루지 않았다는 선언이 아니다.
ko207 | SAME | ko186 | 1.00 | 원칙 위반 분류의 정확도, 그 분류를 받은 개발자의 실제 승인·거절 판단, 해당 판단에 대한 요구·계약의 승인 근거를 서로 다른 평가 대상으로 놓자 는 연구 제안이다.
ko208 | SAME | ko187 | 1.00 | 원칙이 특정 프로젝트에서 보호해야 하는 변경 축을 정확히 가리킨다면, 구조적 경고가 실제 리뷰에서 중요한 단서가 될 수 있기 때문이다.
ko209 | SAME | ko188 | 1.00 | 문제는 원칙을 폐기할 것인지가 아니라, 그 단서에 어느 범위의 결론 권한을 부여할 것인지다.
ko210 | SAME | ko189 | 1.00 | 마틴의 함수가 사각형부터 그린다는 사실만으로는 그 함수를 고쳐야 하는지 알 수 없다.
ko211 | SAME | ko190 | 1.00 | 그 순서를 보장하는 일이 함수의 책임인지 확인해야 한다.
ko212 | SAME | ko191 | 1.00 | 도서관에서도 수정안을 고정한 채 정오표 지원이 필수인 경우에는 거절이 결정됐고, 기술보고서만 필요한 경우에는 책 출력에 관한 약속이 판정을 갈랐다.
ko213 | SAME | ko192 | 1.00 | 특정 OCP 위반이 실제로 수정안 거절을 일으킨 사례를 발견했다는 뜻은 아니다.
ko214 | SAME | ko193 | 1.00 | 원칙 위반이라는 평가가 공학적 결정을 뒷받침하려면 무엇을 추가로 확인해야 하는가 가 이 논문에서 다룬 질문이다.
ko215 | SAME | ko194 | 1.00 | 후속 연구를 위한 네 가지 반증 가능 질문.
ko216 | SAME | ko195 | 1.00 | 첫째, 코드와 원칙 라벨만 받은 검토자는 요구서·API 계약을 함께 받은 검토자보다 실제 프로젝트의 승인 기준을 더 자주 잘못 적용하는가?
ko217 | SAME | ko196 | 1.00 | 둘째, 원칙을 언급하는 코드 리뷰가 실제로 명세나 호출자 의무를 인용하는 비율은 어느 정도이며, 그 인용의 유무가 판단과 상관되는가?
ko218 | SAME | ko197 | 1.00 | 셋째, 새 기능을 구현했지만 기존 진입점이 제공되지 않는 수정안은 실무자가 어떻게 평가하는가?
ko219 | SAME | ko198 | 1.00 | 넷째, 조건부 설계 지침이 보편적인 금지 규칙보다 새로운 요구에서 더 정확한 변경 영향 예측을 제공하는가?
ko220 | SAME | ko199 | 1.00 | 이 네 질문은 아직 측정하지 않은 제안이다.
ko221 | SAME | ko200 | 1.00 | 동등한 정보와 시간을 받은 일반 요구사항 추적 검토가 같은 결과를 낸다면, 새 방법의 실용적 우위는 기각하거나 좁혀야 한다.
ko222 | SAME | ko201 | 1.00 | 실제 기존 원칙들이 일부 조건에서 오히려 강한 예측력을 보인다면 그 경우도 연구 결과에 남겨야 한다.
ko223 | SAME | ko202 | 1.00 | 실제 검토에서 먼저 확인할 것은 수정안의 새 기능만이 아니라, 요구한 사람이나 합의된 문서가 그 기능을 어느 진입점에서 제공하도록 정했는지다.
ko224 | SAME | ko203 | 1.00 | 그다음 기존 호출자가 의존하는 동작 중 무엇이 보호 대상인지 요구서·API 문서·테스트·호출 코드에서 근거를 찾아야 한다.
ko225 | SAME | ko204 | 1.00 | 이 근거가 둘 이상의 가능한 계약을 남긴다면, 원칙 위반이라는 이름으로 결론을 확정하기보다 계약의 출처와 범위를 묻는 편이 정확하다.
ko226 | SAME | ko205 | 1.00 | 반대로 새로운 요구를 충족하지 못한다는 사실이 이미 확정됐다면, 어떤 기존 계약이 추가로 보호되는지 모두 조사하기 전에 해당 수정안을 거절할 수도 있다.
ko227 | SAME | ko206 | 1.00 | 이러한 질문의 순서는 이 논문의 구성 사례에서 나온 실무적 제안이지, 실제 개발 조직의 효율이 개선됐다는 관측 결과는 아니다.
ko228 | SAME | ko207 | 1.00 | 공개된 사실과 양립하는 명세를 남기고 판정의 일치 여부를 확인하는 절차는 단순한 논리다.
ko229 | SAME | ko208 | 1.00 | 문제는 실제 저장소에서 어떤 요청서, API 문서, 테스트, 호출 코드 또는 합의가 그 명세를 뒷받침하는지다.
ko230 | SAME | ko209 | 1.00 | 이 연구는 한 벤치마크의 저장 입력, 연구자가 구성한 실행 예제와 추가 의무에 관한 논리적 민감도 분석, 그리고 연구자가 후향적으로 선정한 두 외부 이슈의 텍스트 근거만을 다뤘다.
ko231 | SAME | ko210 | 1.00 | 실제 리뷰에서 과도한 공리화가 얼마나 흔한지, 누락된 계약을 어떤 방법으로 모두 찾을 수 있는지는 아직 알지 못한다.
ko232 | SAME | ko211 | 1.00 | §3–§4의 감사는 보관된 ZIP의 JSON과 JSONL을 읽는다.
ko233 | SAME | ko212 | 1.00 | 독립 감사 스크립트는 같은 ZIP을 실행 코드가 아닌 자료로 읽어 16개 JSONL 파일, 768행, 48개 고유 코드, 24개 틀, 64개 세부 집단을 재계산했고, Python 고유 코드 12개 중 주석이 있는 4개를 확인했다.
ko234 | SAME | ko213 | 1.00 | §5–§6은 이 연구에서 만든 예제를 실행한다.
ko235 | SAME | ko214 | 1.00 | 재현 자료에는 아카이브 SHA-256, Python 3.11 이상에서 쓸 명령, 저장 행과 참조 쌍의 위치가 있다.
ko236 | EDIT | ko215 | 0.87 | 12판에 있던 그림 1과 파일 배치 실험은 22판 본문에 싣지 않았으며, 원본 그림과 실행 기록을 12판에 보존했다.
ko237 | SAME | ko216 | 1.00 | ‘미공개’인 항목의 값은 두 가지 모두 가능하다.
ko238 | SAME | ko217 | 1.00 | 공개된 정보와 맞는 행에 승인과 거절이 모두 남으면 보류다.
ko239 | NEW | ko174 | 0.05 | Founding question and article type.
ko240 | NEW | ko184 | 0.05 | The original July 29, 2026 project dialogue asked a broader question than whether an individual patch should be rejected: can revisable SOLID design principles acquire the operational force of hard rules or apparent axio
ko241 | NEW | ko174 | 0.02 | We use operational quasi-axiomatization for this proposed phenomenon, without assuming it has occurred at industry scale or was caused by foundation-model training.
ko242 | NEW | ko030 | 0.03 | Our prompt audit and executable Go cases address only parts of the inferential mechanism.
ko243 | NEW | ko127 | 0.02 | The separately predesigned, still unexecuted four-arm coding-agent experiment compares NONE , HARD_SOLID , SCOPED_SOLID , and EVIDENCE_CONDITIONAL advice under the same pinned maintenance requirement; no agent-generated 
Summary ko: SAME 216, EDIT 1, NEW 26

### en (301 sentences)
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
en018 | NEW | en156 | 0.20 | · · The question as originally posed.
en019 | NEW | en243 | 0.14 | In the , the project owner distinguished a design principle from a binding rule and questioned whether tools such as Codex and Claude Code might make SOLID behave as though it were axiomatic.
en020 | NEW | en274 | 0.15 | The original proposal was to investigate how professional advice acquires practical authority and to revise that authority in light of code and counterexamples, not to demand a universal formal proof as a prerequisite fo
en021 | NEW | en028 | 0.14 | The records that ambition as a proposal.
en022 | NEW | en064 | 0.13 | These sources establish a project-internal chronology, not first-in-the-world priority or an observed industry-wide model behavior.
en023 | NEW | en040 | 0.19 | Four distinct senses of axiomatization.
en024 | NEW | en222 | 0.13 | Formal logical axiomatization is the legitimate practice of specifying premises, rules and scope.
en025 | NEW | en266 | 0.13 | Professional canon formation is a historical process of teaching and convention.
en026 | NEW | en201 | 0.16 | Operational quasi-axiomatization , our proposed behavioral target, occurs if a coding agent or evaluation loop treats a named design principle as a hard constraint even after legitimate conflicting requirement and contra
en027 | NEW | en134 | 0.18 | Whether a rejection is actually justified is a further normative question.
en028 | NEW | en136 | 0.11 | Conflating these categories would falsely turn a story about professional advice into a claim about unknown model weights or observed developer conduct.
en029 | SAME | en018 | 1.00 | Martin attributed the principle to Bertrand Meyer, citing page 23 of the 1988 first edition.
en030 | SAME | en019 | 1.00 | For Meyer, a closed module has a stable specification that other modules can rely on.
en031 | SAME | en020 | 1.00 | His library example gives this a practical meaning.
en032 | SAME | en021 | 1.00 | If a catalog handles publication types one by one, adding technical reports can require editing or recompiling existing modules.
en033 | SAME | en022 | 1.00 | Where the new code goes affects how much of the existing system must change.
en034 | SAME | en023 | 1.00 | In a June 1995 public exchange, Kyle Brown argued that developers had to be able to fix a badly designed class.
en035 | SAME | en024 | 1.00 | Martin asked whether an anticipated extension had to require an edit to existing source.
en036 | SAME | en025 | 1.00 | That answer still depends on which changes can be anticipated.
en037 | SAME | en026 | 1.00 | The public record uses SOLID for the five principles by 2007.
en038 | SAME | en027 | 1.00 | A 2009 discussion gave different advice for internal classes and public plugin APIs.
en039 | SAME | en028 | 1.00 | These records show particular uses and objections.
en040 | SAME | en029 | 1.00 | They do not establish that circulation of the SOLID label caused the governing conditions to change.
en041 | SAME | en030 | 1.00 | · · Martin made DrawAllShapes responsible for sorting.
en042 | SAME | en031 | 1.00 | In one implementation Circle::Precedes checks the other shape and puts a circle before a square.
en043 | SAME | en032 | 1.00 | Deciding where a third shape belongs relative to a circle can require an edit to Circle .
en044 | SAME | en033 | 1.00 | Placing the order of types in a table lets squares go first with a swap of two entries.
en045 | SAME | en034 | 1.00 | Sorting individual shapes by area would require information that the table does not hold.
en046 | SAME | en035 | 1.00 | Later in the article Martin compares two uses of dynamic_cast .
en047 | SAME | en036 | 1.00 | One version of DrawAllShapes draws circles and squares, and DrawSquaresOnly draws squares alone.
en048 | SAME | en037 | 1.00 | A triangle left undrawn is a missed output when the task is to draw all shapes.
en049 | SAME | en038 | 1.00 | When the task is to draw squares, skipping it is correct.
en050 | SAME | en039 | 1.00 | How much of that responsibility can a reviewer determine from code and a prompt?
en051 | SAME | en040 | 1.00 | · · We used two distinct sources of evidence.
en052 | SAME | en041 | 1.00 | We audited the saved benchmark inputs to determine what a classifier was actually asked to judge.
en053 | SAME | en042 | 1.00 | Separately, we fixed one catalog patch and varied the demands and protected caller commitments against which its execution was assessed.
en054 | SAME | en043 | 1.00 | The benchmark submissions are not instances of the catalog patch, and neither source records decisions by real reviewers.
en055 | SAME | en044 | 1.00 | The OCP reference material contains 48 before-and-after code pairs.
en056 | SAME | en045 | 1.00 | Sixteen saved JSONL files each contain 48 records, yielding 768 rows.
en057 | SAME | en046 | 1.00 | Exact source-string comparison found 48 distinct submitted programs, each appearing sixteen times.
en058 | SAME | en047 | 1.00 | We checked that each prompt contained its submitted code exactly once, replaced it with a common marker, and grouped the remaining instruction text by exact equality.
en059 | SAME | en048 | 1.00 | The result was 24 scaffolds.
en060 | SAME | en049 | 1.00 | Within each of 64 model–strategy–language combinations, the scaffold was constant across twelve programs.
en061 | SAME | en050 | 1.00 | The 768 records are repeated submissions, not independent maintenance cases.
en062 | SAME | en051 | 1.00 | We separately read the masked instructions for case-specific change requests and protected caller commitments.
en063 | SAME | en052 | 1.00 | An instruction to identify repeated branches where polymorphism might fit is a classification cue, not a request to support a new shape.
en064 | SAME | en053 | 1.00 | We inspected the text outside the submitted code, not the whole semantic context.
en065 | SAME | en054 | 1.00 | In a separate replication, the 192 saved Python rows reduced to twelve distinct code submissions; four contained a total of 46 comment tokens, and none had an AST-detected docstring.
en066 | SAME | en055 | 1.00 | These comments may convey implementation intent, but counting them does not establish a contract.
en067 | SAME | en056 | 1.00 | We did not perform the same comment-token audit for the other three languages.
en068 | SAME | en057 | 1.00 | We compared saved submissions with both reference sides under exact text, trimming outer whitespace and removing all whitespace.
en069 | SAME | en058 | 1.00 | For Python we also compared syntax trees, and separately identified method declarations removed from the reference revisions.
en070 | SAME | en059 | 1.00 | These tests do not establish whether inherited methods remain available or whether callers were promised a behavior.
en071 | SAME | en060 | 1.00 | We read code as archive data and did not execute it.
en072 | SAME | en061 | 1.00 | For the catalog, we fixed the baseline, candidate patch, calls and permission to add a module.
en073 | SAME | en062 | 1.00 | Executing the code established outputs and exceptions for those calls.
en074 | SAME | en063 | 1.00 | The possible demands (technical reports alone, or technical reports and errata), the two scopes of the book-output obligation, and the rule that an acceptable patch must meet its demand and preserve protected behavior we
en075 | SAME | en064 | 1.00 | Table 2 therefore applies authored criteria to observed behavior; it does not report independent human decisions.
en076 | SAME | en065 | 1.00 | For partial disclosure, we retained only the candidate specifications compatible with known facts.
en077 | SAME | en066 | 1.00 | We did not attempt to enumerate obligations outside these four constructed cases.
en078 | SAME | en067 | 1.00 | · · · Pehlivan et al. chose violation scenarios and refined the generated examples.
en079 | SAME | en068 | 1.00 | A second author independently checked the reference pairs for correctness and consistency, and the authors resolved disagreements through discussion.
en080 | SAME | en069 | 1.00 | The benchmark compares model classifications with the resulting labels.
en081 | SAME | en070 | 1.00 | After masking submitted code in the OCP records, we found 24 distinct templates: four DEFAULT, eight ENSEMBLE, eight EXAMPLE and four SMELL.
en082 | SAME | en071 | 1.00 | No two strategies shared a template string.
en083 | SAME | en072 | 1.00 | None of the templates separately stated the requested change or protected caller contract for an individual case.
en084 | SAME | en073 | 1.00 | An additional check found model-dependent scaffolds for ENSEMBLE and EXAMPLE even within a language: gpt-4o-mini differed from the other three models.
en085 | SAME | en074 | 1.00 | Holding model, strategy and language fixed left one scaffold shared across twelve programs.
en086 | SAME | en075 | 1.00 | No submission matched a reference side after removing all whitespace; no saved Python AST among 192 rows matched a Python reference AST.
en087 | SAME | en076 | 1.00 | These checks do not establish semantic independence or source lineage.
en088 | SAME | en077 | 1.00 | One Python EXAMPLE prompt directs the reviewer to repeated branches where polymorphism might fit.
en089 | SAME | en078 | 1.00 | The submitted AreaCalculator branches on shape type to calculate the area of a circle or rectangle.
en090 | SAME | en079 | 1.00 | If a new shape is needed, that branch is a place to look.
en091 | SAME | en080 | 1.00 | The prompt leaves open whether such a change was requested and whether the rectangle’s width query must survive a move of the area calculation.
en092 | SAME | en081 | 1.00 | The separate reference pair 37 moves area calculation onto the shapes and drops the declaration of Rectangle.get_width .
en093 | SAME | en082 | 1.00 | No submitted program matched a reference side under the reported textual normalizations, and the separate Python-only AST comparison also found no match.
en094 | SAME | en083 | 1.00 | Pair 37 establishes that a declaration was removed.
en095 | SAME | en084 | 1.00 | Turning that removal into grounds for rejecting a patch would require evidence that callers could rely on keeping the width query.
en096 | SAME | en085 | 1.00 | Evidence in the saved material and evidence needed to assess a patch.
en097 | SAME | en086 | 1.00 | The prompt example is in JSONL line 13 (record ID 12).
en098 | SAME | en087 | 1.00 | Pair 37 is in a separate reference JSON file.
en099 | SAME | en088 | 1.00 | · · · Bräuer et al. (2018) examined the measurement of design principles with experts; Cabral et al. (2024) studied understanding and extension under a bundled SOLID treatment; Zhu et al. (2026) supplied repository chang
en100 | SAME | en089 | 1.00 | These evaluate different objects.
en101 | SAME | en090 | 1.00 | Our audit does not contest the benchmark's classification task.
en102 | SAME | en091 | 1.00 | It asks what else would be needed to use such a classification as a reason to reject a patch.
en103 | SAME | en092 | 1.00 | · · Empirical review studies narrow the claim further.
en104 | SAME | en093 | 1.00 | Widyasari et al. (2025) coded 793 Gerrit review comments and identified explanation categories including appeals to rules or principles.
en105 | SAME | en094 | 1.00 | This shows that principle-based explanations appear in review practice; it does not show that such principles caused an unjustified patch rejection.
en106 | SAME | en095 | 1.00 | Papotti et al. (2024) experimentally studied 72 computer-science master's students deciding whether to adopt security patches proposed by automatic program repair tools, and found that information about the purported too
en107 | SAME | en096 | 1.00 | Unlike our stipulated Table 2 judgments, those were observed human choices.
en108 | SAME | en097 | 1.00 | · Jin and Chen (2026) tested five language models' judgments of canonical and buggy implementations against natural-language specifications across three programming benchmarks.
en109 | SAME | en098 | 1.00 | They reported false rejection of correct code and risks from prompts that demand explanations or fixes.
en110 | SAME | en099 | 1.00 | We cannot claim to have discovered LLM over-rejection or to improve its error rate: our archive does not record independent patch-acceptance judgments by those models.
en111 | SAME | en100 | 1.00 | Ling, Zou, and Liu (2026) examined public agent-associated contributions and distinguished merges, issue closures, and requirement satisfaction.
en112 | SAME | en101 | 1.00 | Conditional acceptance is not first discovered by this paper either.
en113 | SAME | en102 | 1.00 | Our narrower addition is to hold a patch's execution fixed and make explicit which partially disclosed requirement and contract facts warrant a verdict and which warrant further inquiry .
en114 | SAME | en103 | 1.00 | · This is not a new problem in general.
en115 | SAME | en104 | 1.00 | Kane (2013) argues that evidence supporting an interpretation of test scores does not automatically justify using those scores for a particular decision.
en116 | SAME | en105 | 1.00 | His work does not test software reviews; it establishes the importance of justifying an assessment's use .
en117 | SAME | en106 | 1.00 | Zave and Jackson (1997) distinguish requirements, machine specifications and knowledge of the environment, including which actor controls an action.
en118 | SAME | en107 | 1.00 | Whether sorting belongs to a caller or a drawing function is an instance of that longstanding question.
en119 | SAME | en108 | 1.00 | Jones (1981) likewise developed conditions for compatible environmental reliance and program guarantees in parallel programs.
en120 | SAME | en109 | 1.00 | We do not claim these distinctions as our invention.
en121 | SAME | en110 | 1.00 | · · Barr et al.'s (2015) survey of the test-oracle problem makes a related point about our executable fixture.
en122 | SAME | en111 | 1.00 | Tests establish outputs for chosen inputs; they do not, without an independently grounded oracle, establish which outputs a real project has promised to preserve.
en123 | SAME | en112 | 1.00 | Thus the demands and contracts in Section 5 are explicit assumptions rather than requirements recovered from a repository.
en124 | SAME | en113 | 1.00 | From a classification to a patch disposition.
en125 | SAME | en114 | 1.00 | Correctly naming a design-principle violation supports a judgment about a structural feature of code.
en126 | SAME | en115 | 1.00 | Rejecting a specific patch requires different grounds: (i) the source and scope of the new request, (ii) the behavior the project committed to existing callers, and (iii) the call path through which the request and those
en127 | SAME | en116 | 1.00 | Some clues may reside in source, but observed behavior is not automatically an authorized compatibility promise.
en128 | SAME | en117 | 1.00 | The same change in book output can be unacceptable under one declared contract and acceptable under another.
en129 | SAME | en118 | 1.00 | Section 5 supplies a fixed-patch, four-specification witness to that gap.
en130 | SAME | en119 | 1.00 | It does not disprove the benchmark's classification scores or establish that a real reviewer rejected a patch because of an OCP label.
en131 | SAME | en120 | 1.00 | The inference also depends on what information the classifier receives.
en132 | SAME | en121 | 1.00 | A source-only OCP classifier has the same input, and hence the same classification output, across our four fixed-code specifications.
en133 | SAME | en122 | 1.00 | A context-sensitive evaluator given authentic requests and caller contracts may rightly return different assessments.
en134 | SAME | en123 | 1.00 | Our witness therefore does not say that all OCP evaluations are constant across contexts.
en135 | SAME | en124 | 1.00 | It shows only that a label based solely on fixed code cannot identify which distinct maintenance decision binds under unspecified obligations .
en136 | SAME | en125 | 1.00 | Ordinary requirements traceability and compatibility checklists can ask for these same missing facts; we claim no exclusive ability to do so.
en137 | SAME | en126 | 1.00 | Reading contract authority from an external issue.
en138 | SAME | en127 | 1.00 | To check whether the distinction between a request and a test result survives outside our authored fixture, we inspected (May 2, 2025) and its subsequent discussion.
en139 | SAME | en128 | 1.00 | The reporter described nested router groups in which a middleware factory returning one mutable singleton handler sent requests to the final registered group.
en140 | SAME | en129 | 1.00 | Another participant proposed returning a fresh middleware instance on every factory invocation.
en141 | SAME | en130 | 1.00 | The reporter acknowledged knowing this workaround but reiterated the requested library-level behavior: correct routing with the singleton, or an explicit error on invalid reuse.
en142 | SAME | en131 | 1.00 | Successful responses from an implementation that abandons singleton reuse therefore do not, by themselves, establish satisfaction of the original API request.
en143 | SAME | en132 | 1.00 | Three evidence roles must stay separate: the reporter's requested behavior , the proposed application-level workaround , and a researcher's test oracle .
en144 | SAME | en133 | 1.00 | The reporter's acknowledgment of the workaround is not evidence of maintainer authorization of a new API contract.
en145 | SAME | en134 | 1.00 | Nor does the issue show that an OCP label caused an unjustified patch rejection.
en146 | SAME | en135 | 1.00 | We selected this historic issue after inspecting candidate sources, so it is an exploratory, nonblind example, not a prospective F38 cohort.
en147 | SAME | en136 | 1.00 | · The author of later corrected an initial complaint about regex handling on nested paths, stating that the regex problem did not reproduce in isolation.
en148 | SAME | en137 | 1.00 | This correction should not be mixed with the separate remaining report about method handling between static and parameterized routes.
en149 | SAME | en138 | 1.00 | Source chronology and author revisions are part of the evidence needed for a legitimate maintenance judgment, not extra facts inferable from a source-only design label.
en150 | NEW | en214 | 0.13 | Original four-arm coding-agent proposal, not a completed result.
en151 | NEW | en218 | 0.20 | The proposed four instruction conditions on identical pinned Go maintenance tasks, with the same source state, task specification, protected old-client obligations, tool permissions, budgets and independently fresh agent
en152 | NEW | en277 | 0.16 | NONE supplies no additional SOLID doctrine; HARD_SOLID gives unconditional guidance; SCOPED_SOLID conditions the advice on expected change and source boundaries; and EVIDENCE_CONDITIONAL calls for evidence-based alternat
en153 | NEW | en151 | 0.10 | Assignment order and model/task blocks must be fixed before running the agents.
en154 | NEW | en242 | 0.12 | There are no completed agent outputs or treatment-effect measurements in this paper.
en155 | NEW | en265 | 0.10 | The rivals matter as much as the leading hypothesis.
en156 | NEW | en115 | 0.12 | Lexical echo predicts stronger SOLID prose with no different source behavior.
en157 | NEW | en211 | 0.14 | Task-oracle dominance predicts identical admissible fixes across conditions because functional requirements and regression tests override advice.
en158 | NEW | en213 | 0.18 | Under some conditions, strong SOLID framing could help rather than harm maintenance; any effect sign must be tested.
en159 | NEW | en277 | 0.17 | Primary outcomes would be the same native Go contract tests and source-specific behavior; secondary outcomes should distinguish unnecessary abstractions, architecture choice, explicit exceptions, abstention and revision 
en160 | NEW | en055 | 0.12 | A controlled prompt effect would identify the impact of present instructions on tested agents , not unknown proprietary training weights or the long-run historical canonization of SOLID.
en161 | SAME | en139 | 1.00 | We built a small catalog based on Meyer’s example.
en162 | SAME | en140 | 1.00 | The client in client.py displays each publication through the catalog function passed to it.
en163 | SAME | en141 | 1.00 | The patch adds reports.py to wrap that function.
en164 | SAME | en142 | 1.00 | The source of catalog.py and client.py stays identical.
en165 | SAME | en143 | 1.00 | The resulting catalog displays technical reports and still rejects errata.
en166 | SAME | en144 | 1.00 | For books it now prints BOOK where it used to print book .
en167 | SAME | en145 | 1.00 | Suppose the only new requirement is to handle technical reports.
en168 | SAME | en146 | 1.00 | If callers were promised the original book output, the changed prefix is grounds for rejection.
en169 | SAME | en147 | 1.00 | If the book output is outside the contract, the same patch can be accepted.
en170 | SAME | en148 | 1.00 | Table 2 applies both contracts again when errata are also required.
en171 | SAME | en149 | 1.00 | Both contracts protect journal and proceedings output and the rejection of an unsupported type distinct from errata.
en172 | SAME | en150 | 1.00 | Excluding the book prefix from our stipulated contract is not evidence that real users have no expectation about it; it only means this example does not impose that obligation.
en173 | SAME | en151 | 1.00 | Two requirements for accepting a fixed patch.
en174 | SAME | en152 | 1.00 | Learning that errata are required leaves the last two rows of Table 2.
en175 | SAME | en153 | 1.00 | Both reject the patch, so the book contract need not be settled first.
en176 | SAME | en154 | 1.00 | Learning that technical reports are the whole request leaves the first two rows.
en177 | SAME | en155 | 1.00 | One accepts and one rejects.
en178 | SAME | en156 | 1.00 | The next question is whether the original book output is protected.
en179 | SAME | en157 | 1.00 | The procedure applies only if the actual specification is among these four authored cases.
en180 | SAME | en158 | 1.00 | If disclosure rules out every row, an empty candidate set is a reason to question the evidence or the candidate set, not to infer acceptance or rejection.
en181 | SAME | en159 | 1.00 | If the remaining rows disagree, the same information admits no single binary verdict that is right in every case.
en182 | SAME | en160 | 1.00 | The reviewer can give a conditional answer or defer judgment.
en183 | SAME | en161 | 1.00 | Appendix A gives the nine ways of disclosing or withholding the two fields in this example.
en184 | SAME | en162 | 1.00 | Minimum evidence for a decision.
en185 | SAME | en163 | 1.00 | Let $E$ indicate that errata support is required and $B$ that the previous book prefix is protected.
en186 | SAME | en164 | 1.00 | Within the four stipulated specifications, the acceptance predicate is $A(E,B)=\neg E\land\neg B$.
en187 | SAME | en165 | 1.00 | Its unique inclusion-minimal acceptance certificate is $\{\neg E,\neg B\}$; the two separate minimal rejection certificates are $\{E\}$ and $\{B\}$.
en188 | SAME | en166 | 1.00 | With both facts withheld, an accepting specification $(E=0,B=0)$ and a rejecting specification $(E=1,B=0)$ remain compatible, so deferral has explicit countermodels.
en189 | SAME | en167 | 1.00 | After confirming reports-only ($\neg E$), asking whether the book prefix is protected determines the verdict.
en190 | SAME | en168 | 1.00 | With both fields initially unknown, neither one binary question guarantees a verdict for every possible answer.
en191 | SAME | en169 | 1.00 | These are classical finite Boolean and version-space facts, not new inference rules.
en192 | SAME | en170 | 1.00 | A separate Python replay checked the four worlds, nine disclosure states, inclusion-minimal certificates, contradictory evidence, and pairs of opposite-verdict worlds for deferred states; its passed.
en193 | SAME | en171 | 1.00 | That verifies the bounded decision logic, not actual human decisions or complete source behavior.
en194 | SAME | en172 | 1.00 | Learning more about a fixed contract removes possible worlds; renegotiating that contract changes the legitimate obligation.
en195 | SAME | en173 | 1.00 | The two transitions must not be conflated.
en196 | SAME | en174 | 1.00 | We ran a second patch to see whether the stricter specification was feasible under the same edit boundary.
en197 | SAME | en175 | 1.00 | It adds one module, handles technical reports and errata, and keeps the original book output.
en198 | SAME | en176 | 1.00 | A rejection in Table 2 need not end the search for a patch within that boundary.
en199 | SAME | en177 | 1.00 | The contribution is not a new logical rule: it is a concrete account of why knowing that errata are required settles this decision, whereas a reports-only demand leaves the book-output commitment to be checked.
en200 | SAME | en178 | 1.00 | Applying it to a real review would require finding that commitment in a request, API documentation, tests or caller records.
en201 | SAME | en179 | 1.00 | · Sensitivity to an additional binding obligation.
en202 | SAME | en180 | 1.00 | The preceding approval depends on assuming that the two listed facts exhaust the criteria that matter.
en203 | SAME | en181 | 1.00 | Suppose, as another author-stipulated condition, that this same patch would violate a separate obligation if it were binding; let $C$ indicate whether that third obligation applies.
en204 | SAME | en182 | 1.00 | Under the stricter criterion $A_3(E,B,C)=\neg E\land\neg B\land\neg C$, the universe has eight complete specifications and twenty-seven partial disclosure states.
en205 | SAME | en183 | 1.00 | Exhaustive evaluation yields one ACCEPT, nineteen REJECT and seven DEFER states.
en206 | SAME | en184 | 1.00 | Crucially, evidence that both $E$ and $B$ are false no longer suffices to approve while $C$ remains unknown: the previous ACCEPT becomes DEFER.
en207 | SAME | en185 | 1.00 | If $C$ is explicitly false, the prior nine-state table and its one/five/three distribution are recovered.
en208 | SAME | en186 | 1.00 | This is not an empirically observed safety or performance defect.
en209 | SAME | en187 | 1.00 | The third obligation and stronger criterion were authored for sensitivity analysis.
en210 | SAME | en188 | 1.00 | The point is narrower: one cannot generalize an approval from the original four-world set without evidence that the listed obligations exhaust the relevant acceptance conditions.
en211 | SAME | en189 | 1.00 | Reviewers are not thereby required to investigate arbitrary imaginable obligations; a binding requirement still needs a legitimate source and scope.
en212 | SAME | en190 | 1.00 | [Enumeration code](./paper_b_three_obligation_sensitivity.py) · [regression tests](./test_paper_b_three_obligation_sensitivity.py).
en213 | SAME | en191 | 1.00 | Deciding whether to accept a completed patch differs from choosing an architecture for future edits.
en214 | SAME | en192 | 1.00 | We retain one observation relevant to acceptance.
en215 | SAME | en193 | 1.00 | In the drawing fixture, a new bracketed-rendering option worked through an added function, but the original function still rejected bracketed=True .
en216 | SAME | en194 | 1.00 | A requirement to offer the option at a new entry point was met; a requirement to offer it through the existing call path was not.
en217 | SAME | en195 | 1.00 | The presence of a feature is different from its availability along a required route .
en218 | SAME | en196 | 1.00 | Unless the original entry point and its compatibility obligations are identified, implementation through a separate function cannot by itself establish that the requested behavior is available to existing callers.
en219 | SAME | en197 | 1.00 | The operation-by-shape design comparison and existing-file edit counts address a separate question, preserved in Paper B 통합 원고 12 · 한·영 문장 교정 and its .
en220 | SAME | en198 | 1.00 | AI-assisted review can make structural patterns easier to classify and explain without automatically establishing which maintenance actions a classification warrants.
en221 | SAME | en199 | 1.00 | We propose calling this gap the principle-to-patch transport problem .
en222 | SAME | en200 | 1.00 | The term is a proposed research focus, not a declaration that requirements engineering, behavioral contracts, or validation theory overlooked the problem.
en223 | SAME | en201 | 1.00 | It recommends separating three evaluands: the accuracy of a principle classification, the downstream approve/reject decision, and the authority of the specific requirements and preserved old-client promises that make the
en224 | SAME | en202 | 1.00 | Such transport need not always be defective: a correctly scoped structural warning may genuinely help a project preserve intended changes.
en225 | SAME | en203 | 1.00 | The question is when its evidence supports a particular action, and with what uncertainty.
en226 | SAME | en204 | 1.00 | Drawing a square first establishes what a routine does, not whether it must be edited.
en227 | SAME | en205 | 1.00 | That depends on whether sorting belongs to the routine's obligations.
en228 | SAME | en206 | 1.00 | In our catalog, errata support settled rejection of the fixed patch, while a promise about book output determined the verdict when technical reports alone were required.
en229 | SAME | en207 | 1.00 | We did not observe a real OCP label being misused to reject a patch.
en230 | SAME | en208 | 1.00 | We asked what additional grounds a design-principle assessment needs before it can justify an engineering decision .
en231 | SAME | en209 | 1.00 | Four falsifiable directions.
en232 | SAME | en210 | 1.00 | First, do code-only reviewers given a principle label misapply real acceptance criteria more often than reviewers also supplied authentic requests and API commitments?
en233 | SAME | en211 | 1.00 | Second, how frequently do principle-citing review comments identify a binding requirement or preserved caller obligation, and is that associated with disposition?
en234 | SAME | en212 | 1.00 | Third, how do reviewers judge a patch that implements a feature through a new entry point but not the existing required call path?
en235 | SAME | en213 | 1.00 | Fourth, do conditional design policies predict maintenance impact on newly requested changes better than unconditional prohibitions?
en236 | SAME | en214 | 1.00 | These are proposals, not findings .
en237 | SAME | en215 | 1.00 | A conventional requirements-traceability review with equivalent sources and budget is an essential competitor; if it matches or outperforms the proposed framework, no distinct performance gain should be claimed.
en238 | SAME | en216 | 1.00 | Likewise, some traditional design principles may be strongly predictive under well-defined conditions, which this agenda should recover rather than dismiss.
en239 | SAME | en217 | 1.00 | A practical review should first ask not only whether the patch implements a feature but where the request or an authorized agreement requires that feature to be reachable.
en240 | SAME | en218 | 1.00 | The reviewer should then locate the source of each protected old-client obligation in requests, API documentation, tests and actual call paths, without automatically treating every observed response as a promise.
en241 | SAME | en219 | 1.00 | If those sources leave different legitimate contracts possible, asking who can settle the obligation is more defensible than turning an OCP label into a categorical rejection.
en242 | SAME | en220 | 1.00 | Conversely, a demonstrated failure to meet an already binding new demand may reject the fixed patch before every other old-client promise is resolved.
en243 | SAME | en221 | 1.00 | This sequence is a recommendation derived from our authored example, not evidence that it reduces actual review costs in an organization.
en244 | SAME | en222 | 1.00 | Keeping the specifications compatible with known facts and checking their verdicts is elementary logic.
en245 | SAME | en223 | 1.00 | The unresolved task is to identify the requests, API documentation, tests, callers or agreements that support those specifications in a real repository.
en246 | SAME | en224 | 1.00 | Our evidence is confined to one benchmark archive, authored executable examples, an authored logical sensitivity check, and two post hoc selected external issue threads.
en247 | SAME | en225 | 1.00 | We do not know how often over-axiomatization occurs in real reviews or how to recover every missing obligation.
en248 | SAME | en226 | 1.00 | The audits in Sections 3–4 read the archived JSON and JSONL as data.
en249 | SAME | en227 | 1.00 | A separate script reproduced sixteen JSONL files, 768 rows, 48 distinct submissions, 24 scaffolds and 64 fixed model–strategy–language groups, and counted Python comments in four of twelve unique submissions.
en250 | SAME | en228 | 1.00 | Section 5 and the call-path check in Section 6 use examples written for this study.
en251 | SAME | en229 | 0.95 | The shape-layout experiment and Figure 1 remain preserved in manuscript 12; manuscript 22 does not reframe them as a new measured maintenance-cost trial.
en252 | SAME | en230 | 1.00 | The reproduction notes give the SHA-256 digest, commands for Python 3.11 or later, and record and pair locators.
en253 | SAME | en231 | 1.00 | The table below gives the nine verdicts for Section 5.
en254 | SAME | en232 | 1.00 | Both values of a withheld field remain possible.
en255 | SAME | en233 | 1.00 | Defer means that the compatible rows include both acceptance and rejection. - Meyer, B.
en256 | SAME | en234 | 1.00 | Object-Oriented Software Construction (1st ed.), pp.
en257 | SAME | en235 | 1.00 | The Open–Closed Principle . . - Jones, C.
en258 | SAME | en236 | 1.00 | Development Methods for Computer Programs Including a Notion of Interference .
en259 | SAME | en237 | 1.00 | Oxford University Computing Laboratory, PRG-25.
en260 | SAME | en238 | 1.00 | · . - Pehlivan, F., Ergüzen, A.
en261 | SAME | en239 | 1.00 | M., Lami, M., & Koyuncu, A.
en262 | SAME | en240 | 1.00 | An Empirical Study on Prompting LLMs to Detect Design Principle Violations .
en263 | SAME | en241 | 1.00 | ASE 2025 NIER. . - Bräuer et al.
en264 | SAME | en242 | 1.00 | Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research . . - Cabral et al.
en265 | SAME | en243 | 1.00 | Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding . . - Zhu, H., Zhang, Q., Wang, J., Yang, Z., & Qiu, Y.
en266 | SAME | en244 | 1.00 | Needle in the Repo: A Benchmark for Maintainability in AI-Generated Repository Edits . . - Kane, M.
en267 | SAME | en245 | 1.00 | Validating the Interpretations and Uses of Test Scores .
en268 | SAME | en246 | 1.00 | Journal of Educational Measurement , 50(1), 1–73.
en269 | SAME | en247 | 1.00 | · . - Zave, P., & Jackson, M.
en270 | SAME | en248 | 1.00 | Four Dark Corners of Requirements Engineering .
en271 | SAME | en249 | 1.00 | ACM Transactions on Software Engineering and Methodology , 6(1), 1–30.
en272 | SAME | en250 | 1.00 | T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S.
en273 | SAME | en251 | 1.00 | The Oracle Problem in Software Testing: A Survey .
en274 | SAME | en252 | 1.00 | IEEE Transactions on Software Engineering .
en275 | SAME | en253 | 1.00 | · . - Widyasari, R., Zhang, T., Bouraffa, A., Maalej, W., & Lo, D.
en276 | SAME | en254 | 1.00 | Explaining Explanations: An Empirical Study of Explanations in Code Reviews .
en277 | SAME | en255 | 1.00 | ACM Transactions on Software Engineering and Methodology , 34(6), Article 177.
en278 | SAME | en256 | 1.00 | · . - Papotti, A., Paramitha, R., & Massacci, F.
en279 | SAME | en257 | 1.00 | On the acceptance by code reviewers of candidate security patches suggested by Automated Program Repair tools .
en280 | SAME | en258 | 1.00 | Empirical Software Engineering , 29, Article 132.
en281 | SAME | en259 | 1.00 | · . - Jin, H., & Chen, H.
en282 | SAME | en260 | 1.00 | Are LLMs Reliable Code Reviewers?
en283 | SAME | en261 | 1.00 | Systematic Overcorrection in Requirement Conformance Judgement .
en284 | SAME | en262 | 1.00 | · . - Ling, M., Zou, J., & Liu, X.
en285 | SAME | en263 | 1.00 | Negotiating Completion in Agentic Software Work: Acceptance Boundaries and Deferred Requirements .
en286 | SAME | en264 | 1.00 | 이 목록은 인용된 주요 자료를 확인할 수 있게 모은 집필용 서지이며, 서지형식·인용 위치·전수 대조를 마친 제출용 참고문헌은 아직 아니다.
en287 | SAME | en265 | 1.00 | / These are verified reading anchors, not yet a fully formatted submission bibliography.
en288 | SAME | en266 | 1.00 | Historical priority boundary.
en289 | SAME | en267 | 1.00 | Paper B's explicit conceptual genealogy in this research archive goes through early manuscript 01–02, the later “SOLID history and AI quasi-axiomatization” handoff, and the 2026-11-21 Plan B′ editorial debate.
en290 | SAME | en268 | 1.00 | Recovered Notion pages document the trajectory, but the earliest complete ChatGPT transcript could not be retrieved in this session.
en291 | SAME | en269 | 1.00 | Do not claim an unverified first-in-world date or independent discovery of requirements traceability, OCP conditionals, or Boolean information lattices.
en292 | SAME | en270 | 1.00 | Paper C: compare design configurations under prospective new change requests and an equal-information rival; study whether structural success reverses with edit boundaries and old API obligations.
en293 | SAME | en271 | 1.00 | Paper D: estimate prevalence and outcomes of AI-assisted principle citation in real reviews using independent annotators and provenance-coded requests.
en294 | SAME | en272 | 1.00 | EvoNOMOS mainline: search for generalizable conditional mechanisms of source organization without claiming broad proofs from a selected set of Go routers.
en295 | SAME | en273 | 1.00 | Formalization ceiling: a position paper does not require proving a general program equivalence or an undecidable semantic relation.
en296 | SAME | en274 | 1.00 | Any future claim of universal soundness, completeness, impossibility, P/NP separation or measured performance advantage would require a precisely stated formal/empirical problem and separate verification.
en297 | SAME | en275 | 1.00 | General program semantic equivalence and P-versus-NP complexity are distinct questions; no reduction or complexity ranking is proposed here.
en298 | SAME | en276 | 1.00 | Methodological authority: Meyer/Martin and later review studies are historical interlocutors and empirical competitors, not unquestionable authorities.
en299 | EDIT | en277 | 0.56 | If newer source-specific evidence supports a narrower or contrary conclusion, revise the candidate principle and document the contradiction. - , created 2026-07-29; user distinguishes principles from rules and proposes i
en300 | NEW | en273 | 0.14 | Read direct Drive original rather than depending solely on a modern summary. - , status 2026-10-09: historical-critical research program, “operational quasi-axiomatization”, hypotheses not established behavior. - , PRE-A
en301 | NEW | en275 | 0.18 | Neither a reduction to P vs NP nor any complexity ordering is established or claimed.
Summary en: SAME 276, EDIT 1, NEW 24

## v23 · [Source](https://app.notion.com/p/41fef561cf92813c890af618e7ee6971)
### ko (70 sentences)
ko001 | NEW | ko013 | 0.07 | SOLID는 설계 원칙 인데, AI 코딩 에이전트나 코드 검토에서는 언제 그 원칙이 마치 따라야 할 규칙 또는 공리 처럼 작동하게 되는가?
ko002 | NEW | ko013 | 0.16 | 이 질문은 2026년 7월 29일 EvoNOMOS의 초기 연구 대화에서 제기됐다.
ko003 | NEW | ko241 | 0.13 | 우리는 설계 조언에 반증 가능성과 적용 범위를 확인하지 않은 채 개별 수정안의 승인·거절을 결정할 권한을 부여하는 현상을 \*\*운영상의 준공리화(operational quasi-axiomatization)\*\*라는 연구 가설로 제안한다.
ko004 | NEW | ko173 | 0.06 | 수리논리학에서 공리화 자체를 비판하는 것은 아니다.
ko005 | NEW | ko010 | 0.07 | 역사적 원문과 SOLID 분류 벤치마크를 검토하고, 동일한 수정안의 승인 기준을 바꾸는 작은 실행 사례 및 실제 Go 라우터 이슈에서 요구와 우회책의 차이를 확인했다.
ko006 | NEW | ko066 | 0.07 | 이 자료는 실제 코딩 에이전트가 준공리화된 행동을 보인 비율이나 그 인과 메커니즘을 측정하지 않는다.
ko007 | NEW | ko143 | 0.06 | 우리는 네 가지 지시 조건—추가 지시 없음, 강제 SOLID, 조건부 SOLID, 요구·계약 근거 중심—을 동일한 Go 변경 과제에서 비교하는 후속 실험을 제안한다.
ko008 | NEW | ko020 | 0.03 | 설계 원칙을 제거하기보다, 원칙의 이름과 실행 가능한 근거 사이의 간극을 별도 연구 대상으로 만들자는 것이 목적이다.
ko009 | NEW | ko103 | 0.04 | 소프트웨어 개발자는 ‘개방–폐쇄 원칙을 위반했다’는 의견을 받을 수 있다.
ko010 | NEW | ko200 | 0.07 | 그 의견은 특정 의존 방향이나 분기 구조를 잘 설명할 수 있지만, 그 자체만으로 어느 변경 요구를 충족해야 하며 어떤 기존 호출자를 보호해야 하는지 알려 주지는 않는다.
ko011 | NEW | ko066 | 0.04 | 수정이 필요할 수도 있고, 원칙으로 기술된 패턴이 실제 요구에 잘 맞을 수도 있다.
ko012 | NEW | ko209 | 0.04 | 우리는 원칙을 항상 채택하거나 항상 반박하는 태도보다 원칙에 부여된 결론의 권한 을 구별하고자 한다.
ko013 | NEW | ko013 | 0.37 | 는 원칙과 강제 규칙을 구별하면서 Codex·Claude Code와 같은 코딩 도구가 SOLID를 공리처럼 취급할 가능성을 문제 삼았다.
ko014 | NEW | ko241 | 0.17 | 은 이를 operational quasi-axiomatization 으로 명명하고 최초 네 조건 실험을 제안했다.
ko015 | NEW | ko201 | 0.04 | 초기 문서가 증명하는 것은 이 연구의 문제 제기와 연대기이지, 산업계 전반에 그러한 현상이 이미 일어났다는 사실은 아니다.
ko016 | NEW | ko018 | 0.02 | 이 글의 기여는 (1) 준공리화를 판정 가능한 행동 가설로 좁혀 정의하고, (2) 원칙에 대한 구조적 분류에서 특정 패치에 대한 승인·거절로 넘어가는 문제를 하위 기제로 제시하며, (3) 이 가설을 반박할 수 있는 경쟁 설명과 실제 후속 실험을 제안하는 데 있다.
ko017 | NEW | ko129 | 0.03 | 객체지향의 역사는 한 개의 설계 규범이 축적된 역사가 아니다.
ko018 | NEW | ko041 | 0.03 | 시뮬레이션과 클래스의 Simula 전통, 메시지와 상호작용을 중시한 Smalltalk의 설명, 모듈 분해 기준을 제시한 Parnas의 논의, 행동적 하위 타입을 다룬 Liskov–Wing의 논의는 서로 다른 문제를 다뤘다.
ko019 | NEW | ko239 | 0.03 | Meyer와 Martin의 개방–폐쇄 원칙 역시 안정된 모듈 계약과 예상할 변경의 종류를 중요하게 다뤘다.
ko020 | NEW | ko021 | 0.04 | Martin은 1996년 ‘Strategic Closure’에서 모든 변경에 닫힌 모듈을 만드는 일이 불가능하므로 어떤 변경을 예상하는지가 중요하다고 설명한다.
ko021 | NEW | ko105 | 0.02 | 이러한 원문들은 동일하지도 무오류하지도 않다.
ko022 | NEW | ko144 | 0.05 | 오늘날의 변화에 대응하는 예측력이 있는지 별도로 시험해야 한다.
ko023 | NEW | ko016 | 0.06 | 여기서 형식적 공리화 는 전제와 추론 규칙을 정확하게 정의하는 수학적 활동이며, 직업적 정전화 는 교육·실무에서 반복된 조언이 정통적인 지식으로 받아들여지는 역사적 과정이다.
ko024 | NEW | ko018 | 0.07 | 운영상의 준공리화 는 더 좁은 행동적 주장이다.
ko025 | NEW | ko018 | 0.07 | 에이전트나 검토자가 현재 요구·명시된 예외·기존 호출자 계약에 반하는 근거를 받았는데도, 원칙 이름만으로 허용 가능한 대안을 배제하는가?
ko026 | NEW | ko173 | 0.05 | 강한 표현이 쓰였다는 이유만으로 이 가설이 참이 되는 것은 아니다.
ko027 | NEW | ko041 | 0.05 | 또한 인간 리뷰어의 승인 관행, 저장소의 로컬 지시문, 코딩 에이전트의 실행 반응, 기초 모델 훈련 자료는 서로 다른 층위다.
ko028 | NEW | ko136 | 0.05 | /18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md)에서 OCP 관련 저장 응답 행은 768개였다.
ko029 | NEW | ko050 | 0.06 | 이는 독립적인 768개 소프트웨어 변경 사례가 아니라 48개 고유 제출 코드가 각 16차례 나타난 기록 이다.
ko030 | NEW | ko053 | 0.04 | 프롬프트는 분류 범주를 평가하기 위한 자료이지, 각 제출 코드에 관한 실제 유지보수 요구와 승인된 구계약을 모두 전달하는 판정 자료는 아니다.
ko031 | NEW | ko066 | 0.04 | 코드 내부 단서가 일부 존재하므로 요구·계약 정보가 전혀 없었다고 단정하지도 않는다.
ko032 | NEW | ko177 | 0.09 | /31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md)에서는 한 패치가 기술보고서를 지원하지만 정오표 지원은 없고, 기존 책 출력의 접두어를 바꾼다.
ko033 | NEW | ko152 | 0.06 | 정오표가 필수거나 구접두어가 계약상 보호된다면 거절하지만, 그 둘이 모두 요구되지 않는 작은 명세에서는 승인할 수 있다.
ko034 | NEW | ko179 | 0.08 | 이는 연구자가 정의한 제한적인 기준의 반례형 예시 이지 실제 프로젝트의 완전한 승인 규칙이 아니다.
ko035 | NEW | ko023 | 0.06 | 제3의 별도 보호 의무를 추가하면 기존 승인이 미공개 상태에서 보류가 되는 것도 확인했다.
ko036 | NEW | ko124 | 0.19 | 는 원작성자가 싱글턴 미들웨어가 정상 동작하거나 잘못된 재사용을 명시적으로 알리기를 요청한 이슈다.
ko037 | NEW | ko213 | 0.09 | 인스턴스를 새로 만드는 우회책이 경로 테스트에 통과해도 원래 요청을 그대로 충족했다는 뜻은 아니다.
ko038 | NEW | ko131 | 0.15 | 에서는 최초의 정규식 경로 문제를 작성자가 후속 댓글에서 정정했다.
ko039 | NEW | ko129 | 0.11 | 두 이슈를 Go v5.1.0에서 제한적으로 재현했지만 OCP 지시가 실제 개발자에게 부당한 거절을 일으켰다는 자료는 아니다 .
ko040 | EDIT | ko205 | 0.62 | 우리는 구조적 패턴의 분류 와 특정 수정안의 처리 를 구분하는 문제를 \*\*원칙→수정안 판단의 전이 문제(principle-to-patch transport problem)\*\*라고 부르자고 제안한다.
ko041 | NEW | ko226 | 0.03 | 분류가 정확하더라도 그것이 패치를 거절할 충분한 이유인지는 새로운 요구, 보호받는 기존 동작, 편집 가능한 모듈 경계, 대체 구현의 가능성에 달려 있다.
ko042 | NEW | ko169 | 0.05 | 그 요건이 실제로 확인되었다면 원칙에 기초한 경고는 타당할 수 있다.
ko043 | NEW | ko156 | 0.08 | 이 개념이 요구공학이나 Design by Contract의 과거 연구에서 전혀 존재하지 않았다는 뜻은 아니다.
ko044 | NEW | ko068 | 0.04 | 새로 제안하는 것은 이 구별을 AI 설계 원칙 적용의 결과 변수 로 명시하고, (i) 코드 패턴 라벨의 정확도, (ii) 실제 수정안의 합격 가능성, (iii) 결정을 뒷받침하는 계약 근거, (iv) 반대 증거 이후 판단 변경을 독립적으로 측정하자는 연구 의제다.
ko045 | NEW | ko197 | 0.03 | 문맥이 불충분할 때의 질문·기권 역시 하나의 결과다.
ko046 | NEW | ko135 | 0.35 | NONE 은 추가 설계 원칙을 지시하지 않는다.
ko047 | NEW | ko136 | 0.46 | HARD_SOLID 는 강한 원칙 준수를 요구한다.
ko048 | NEW | ko137 | 0.33 | SCOPED_SOLID 는 변경 종류와 예상 안정성에 따라 원칙을 적용한다.
ko049 | NEW | ko138 | 0.44 | EVIDENCE_CONDITIONAL 은 코드·변경 요구·기존 계약·대안을 통해 판단하고 근거가 부족하면 질문하거나 보류한다.
ko050 | NEW | ko134 | 0.07 | 같은 소스 버전과 요구, 기존 계약, 도구, 모델·예산을 받되 설계 조언 단락만 다르게 해야 한다.
ko051 | NEW | ko018 | 0.04 | 원칙의 운영상 준공리화 가설 은 강제 지시가 다른 조건에 비해 계약에 어긋나는 구조적 고집이나 반례 이후 수정 불능을 더 많이 일으킬 수 있다고 예측한다.
ko052 | NEW | ko136 | 0.05 | 그러나 어휘 반복 가설 에 따르면 설명에서 SOLID만 더 자주 언급되고 코드는 달라지지 않는다.
ko053 | NEW | ko200 | 0.06 | 과제·테스트 지배 가설 에 따르면 모든 조건의 코드가 동일하게 요구를 충족한다.
ko054 | NEW | ko208 | 0.07 | 어떤 프로젝트에서는 강한 지시가 실제 개선을 가져올 수도 있다.
ko055 | NEW | ko139 | 0.12 | 새 에이전트 문맥에서의 실제 생성·실행은 아직 수행하지 않았다 .
ko056 | NEW | ko140 | 0.03 | 미래 연구의 최소 단위는 동일한 실제 Go 변경 요구에 대한 각각의 독립된 에이전트 실행이다.
ko057 | NEW | ko134 | 0.04 | 소스 버전·승인된 요구·구계약·수정 허용 범위·동일한 기능 오라클을 고정하고, 네 조건의 배정 순서와 모델별 균형을 기록한다.
ko058 | NEW | ko181 | 0.03 | 주요 결과는 기존/신규 Go 테스트 성공 및 API 보존이다.
ko059 | NEW | ko179 | 0.02 | 설명 속 원칙 인용, 새로운 추상화의 종류, 패치 크기, 반례를 제시한 후의 수정·기권은 별개의 결과 변수다.
ko060 | NEW | ko211 | 0.04 | 자동 검사와 독립적인 사람의 코드·계약 검토가 다르면 그 불일치를 보존해야 한다.
ko061 | NEW | ko023 | 0.03 | 기존 Go 두 구조에서 동일한 애플리케이션 필터를 추가하면 새 예약 경로 정책을 모두 충족한 은 이 방향의 중요한 고전적 동률 대조 사례 다.
ko062 | NEW | ko146 | 0.07 | 어떤 요구에서는 SOLID형 구조가 필수적이지 않다는 작은 근거일 뿐, 아직 네 프롬프트 조건의 에이전트 결과는 아니다.
ko063 | NEW | ko126 | 0.04 | 프로젝트 수준에서 예상 변경이 달라지면 더 깊은 변경 비용 비교는 Paper C로, AI 지침 준공리화의 실제 빈도와 문헌·리뷰 인용 분석은 Paper D로 보내는 편이 적합하다.
ko064 | NEW | ko126 | 0.09 | Paper B는 SOLID가 틀렸다고 선언하지 않는다.
ko065 | NEW | ko207 | 0.04 | 과거의 개발 지침이 현재 환경에서도 유용한 범위, 비효율적인 범위, 프로젝트 계약 때문에 강제되어야 하는 범위를 서로 다른 이유로 설명하자는 제안이다.
ko066 | NEW | ko173 | 0.05 | 수리논리학의 광범위한 완전성 정리나 임의 Go 프로그램의 동형 증명은 이 문제를 제안하기 위한 필수 선행 조건이 아니다.
ko067 | NEW | ko031 | 0.04 | 장래에 모든 코드에 대한 판정 가능성이나 효과의 보편성을 주장한다면 그때에는 정확한 수학적 정의와 별도 증명이 필요하다.
ko068 | NEW | ko135 | 0.05 | AI가 설계 원칙의 언어를 더 많이 사용할수록, 그 언어가 실제 변경 결정에 어느 정도의 권한을 갖는지 추적하는 연구도 필요하다.
ko069 | NEW | ko214 | 0.06 | 원칙을 믿는가 반박하는가보다 어떤 요구·구계약·반대 사례를 받고 실제 결정을 바꾸는가 가 더 좋은 실험 질문이다.
ko070 | NEW | ko234 | 0.02 | 이 원고는 완성된 효과 측정보다 이 연구 질문을 명명하고, 독립된 실험으로 반박할 수 있게 만드는 데 우선순위를 둔다. ---
Summary ko: SAME 0, EDIT 1, NEW 69

### en (79 sentences)
en001 | NEW | en265 | 0.17 | SOLID is a family of software-design principles .
en002 | NEW | en299 | 0.15 | Under what circumstances might AI coding agents or review workflows make these principles function as hard rules or apparent axioms ?
en003 | NEW | en018 | 0.20 | This question appeared in the original EvoNOMOS discussion on July 29, 2026.
en004 | NEW | en026 | 0.22 | We propose operational quasi-axiomatization as an empirical target: conditional design advice is granted authority to decide an individual patch without checking relevant changes, contracts, exceptions and competing impl
en005 | NEW | en014 | 0.17 | This is not a critique of formal axiomatic reasoning.
en006 | NEW | en101 | 0.15 | We situate the question historically, audit a stored OCP-classification benchmark, develop a fixed-patch contract counterexample, and examine third-party Go issue discussions distinguishing reported demands from passing 
en007 | NEW | en087 | 0.27 | These sources do not establish the prevalence or causes of such agent behavior.
en008 | NEW | en152 | 0.22 | We recover an earlier four-treatment proposal for agent experiments—no added guidance, hard SOLID, scoped SOLID and evidence-conditional design advice—and articulate behavioral outcomes and classical rivals.
en009 | NEW | en116 | 0.16 | The paper aims to establish a falsifiable research question, not to assert a universal software law.
en010 | NEW | en257 | 0.28 | A code review may warn that an implementation violates the Open–Closed Principle.
en011 | NEW | en185 | 0.15 | That warning can characterize a real structural feature, but it cannot alone determine which forthcoming change is required, which previously supported call must survive, or which repair the project is authorized to make
en012 | NEW | en039 | 0.18 | Both the warning and a rejection may be justified in a particular project.
en013 | NEW | en131 | 0.17 | The distinction is the authority assigned to the inference .
en014 | NEW | en019 | 0.46 | The distinguished a principle from a compulsory rule and asked whether tools including Codex and Claude Code might treat SOLID as though it were axiomatic.
en015 | NEW | en026 | 0.14 | The called this possibility operational quasi-axiomatization and outlined a controlled agent study.
en016 | NEW | en022 | 0.27 | These documents establish the internal chronology of an idea , not evidence that the phenomenon has been observed across the industry, or historical priority over all existing requirements research.
en017 | NEW | en207 | 0.15 | We contribute an explicit conceptual distinction, one bounded classification-to-action witness, and an empirically falsifiable agent-study proposal.
en018 | NEW | en027 | 0.12 | The ambition is to open a scientific question whose negative outcome would also be meaningful.
en019 | NEW | en256 | 0.28 | Object-oriented software design was not born as a single five-rule system.
en020 | NEW | en022 | 0.11 | Simula's modeling trajectory, Smalltalk's message-centered accounts, Parnas's modularity criterion, Liskov and Wing's behavioral subtyping, and Meyer and Martin's discussions of stable extension confront different proble
en021 | NEW | en222 | 0.13 | The Open–Closed Principle itself was not simply a claim that every old line must never change: Martin's 1996 discussion of Strategic Closure makes the choice of expected changes part of the engineering problem.
en022 | NEW | en298 | 0.28 | These authors are historical interlocutors, not infallible authorities over modern tool-mediated practice.
en023 | NEW | en120 | 0.13 | We distinguish four phenomena.
en024 | NEW | en024 | 0.39 | Formal axiomatization legitimately specifies premises and rules of inference.
en025 | NEW | en025 | 0.35 | Professional canonization is a historical process whereby memorable advice becomes authoritative in teaching or practice.
en026 | NEW | en026 | 0.31 | Operational quasi-axiomatization , our testable behavioral conjecture, arises when an agent or a reviewer continues to treat a principle name as binding even after relevant, credible contrary requirements or preserved co
en027 | NEW | en027 | 0.40 | Normative legitimacy asks whether that action was actually justified.
en028 | NEW | en144 | 0.11 | Strong wording alone is not evidence of harmful behavior.
en029 | NEW | en210 | 0.19 | Foundation-model weights, persistent repository files, immediate prompts, generated patches and human acceptance are distinct causal stages; our study cannot infer one from another without evidence.
en030 | NEW | en248 | 0.17 | Our [OCP archive audit](.
en031 | NEW | en061 | 0.19 | /18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md) examined 768 stored response rows , not 768 independent maintenance tasks.
en032 | NEW | en081 | 0.19 | The stored archive contains 48 distinct submitted code examples repeated 16 times and 24 distinct masked prompt scaffolds.
en033 | NEW | en101 | 0.23 | The benchmark assesses a violation-classification task; it does not by itself supply a complete, authority-bearing maintenance requirement for each submitted patch.
en034 | NEW | en120 | 0.16 | Some code includes hints, so we do not claim the inputs contain no relevant contextual information.
en035 | NEW | en031 | 0.18 | An [authored library-patch example](.
en036 | NEW | en242 | 0.14 | /31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md) demonstrates the distinction in a deliberately small setting.
en037 | NEW | en165 | 0.25 | The candidate implements technical-report handling, omits errata and changes an older book-display prefix.
en038 | NEW | en185 | 0.18 | Under the stipulated criteria it is admissible only when neither errata nor the previous prefix is a binding obligation.
en039 | NEW | en151 | 0.18 | Extending the universe with a third independently protected obligation changes what evidence is sufficient for approval.
en040 | NEW | en236 | 0.14 | These are author-defined worlds, not industrial acceptance statistics.
en041 | NEW | en141 | 0.20 | In , the reporter wanted singleton middleware reuse to route correctly or to fail explicitly.
en042 | NEW | en143 | 0.17 | A freshly allocated middleware instance was a practical workaround, yet passing its HTTP tests does not establish support for the originally requested singleton behavior.
en043 | NEW | en147 | 0.16 | The reporter of later withdrew one initial regex-subpath allegation, leaving a narrower method-precedence report.
en044 | NEW | en130 | 0.17 | Our pinned original-Go reproduction checks limited HTTP effects; neither issue documents a reviewer wrongfully rejecting a patch because of OCP.
en045 | NEW | en221 | 0.46 | We propose naming a narrower, testable mechanism: the principle-to-patch transport problem .
en046 | NEW | en062 | 0.19 | A structural classifier can correctly identify a pattern, but applying the label to approve, reject or demand a specific refactoring additionally requires knowledge about the requested change, protected caller behavior, 
en047 | NEW | en224 | 0.17 | The transport can be valid: a principle may genuinely summarize a binding project's need.
en048 | NEW | en035 | 0.14 | It can also be overextended where these sources remain unknown or conflicting.
en049 | NEW | en222 | 0.27 | We do not claim requirements engineering, Design by Contract or code-review research overlooked obligations and authority.
en050 | NEW | en026 | 0.22 | The proposed empirical contribution is to make four distinct evaluands explicit in AI-assisted design review: accuracy of structural labels, correctness of particular patch disposition, the provenance of binding requirem
en051 | NEW | en173 | 0.15 | Asking for missing requirements or abstaining can be an appropriate outcome.
en052 | NEW | en152 | 0.32 | The specified four conditions: NONE , no additional principle advice; HARD_SOLID , unconditional adherence; SCOPED_SOLID , advice linked to anticipated changes and interfaces; and EVIDENCE_CONDITIONAL , alternative compa
en053 | NEW | en151 | 0.16 | Each agent should see the same pinned Go task, original source, regression requirements, tool access and budget; only design-advice text changes.
en054 | NEW | en026 | 0.21 | Our operational quasi-axiomatization conjecture predicts that hard instructions may increase inappropriate adherence or resistance to valid counterevidence.
en055 | NEW | en156 | 0.25 | An equally serious lexical-echo rival predicts different SOLID explanations without different patches.
en056 | NEW | en055 | 0.17 | A task-and-tests dominance rival predicts no material code difference across treatments.
en057 | NEW | en158 | 0.09 | Hard guidance might even improve code under some demands.
en058 | NEW | en050 | 0.10 | We preclude a predetermined sign of advantage.
en059 | NEW | en252 | 0.11 | As of this manuscript no randomized fresh-agent invocations or agent-generated repair outcomes have been collected .
en060 | NEW | en151 | 0.19 | The proper experimental unit is a fresh independent agent execution on an originally frozen codebase with an authentic change request and preserved old-client contract.
en061 | NEW | en153 | 0.16 | Block by task and model and predetermine balanced treatment assignments; keep time and tool budgets equal.
en062 | NEW | en159 | 0.17 | Primary outcome categories should separate Go functional success, old-API behavior and an independent assessment of contractual admissibility.
en063 | NEW | en159 | 0.22 | Secondary categories include modified source surface, type of additional abstraction, written principle citations, stated exceptions, abstention and response to a negative counterexample.
en064 | NEW | en256 | 0.12 | Never score vocabulary frequency as software correctness.
en065 | NEW | en300 | 0.15 | Our existing demonstrates that two original router architectures can both satisfy the same researcher-authored reserved-path requirement using an ordinary outer wrapper, without editing frozen source arms.
en066 | NEW | en154 | 0.12 | That is a useful classical tie , not a four-treatment agent result or a general source-architecture theorem.
en067 | NEW | en293 | 0.18 | Paper C can compare architectural forecast reversals; Paper D can measure field prevalence of principle-citing reviews.
en068 | NEW | en071 | 0.17 | Neither should be reported as already executed.
en069 | NEW | en014 | 0.17 | This is not a claim that SOLID is wrong.
en070 | NEW | en158 | 0.17 | Established advice may be effective, ineffective, or indispensable depending on actual maintenance conditions, and such distinctions should be settled with source-grounded comparisons rather than inherited authority alon
en071 | NEW | en296 | 0.24 | A position paper can propose and constrain an empirical research program without proving equivalence of all possible programs ; any future claim of general soundness, complexity-class separation or population treatment e
en072 | NEW | en230 | 0.17 | The proposal is that AI-assisted engineering needs research into how much decision authority design-principle language receives , not merely whether the language appears in generated prose.
en073 | NEW | en238 | 0.18 | A strong result would identify the conditions under which the original principle correctly predicts a maintenance decision; an equally valuable negative result would show that code behavior follows the task requirements 
en074 | NEW | en251 | 0.15 | The manuscript claims a named, falsifiable question and transparent bounded evidence, not observed industrial dogmatism. --- - .
en075 | NEW | en300 | 0.17 | Project-internal origin record, not published scientific priority. - and . - Parnas (1972), On the criteria to be used in decomposing systems into modules , DOI 10.1145/361598.361623. - Meyer (1988), Object-Oriented Soft
en076 | NEW | en282 | 0.10 | (2025), Are We SOLID with LLMs? , .
en077 | NEW | en057 | 0.15 | Distinct benchmark source archive and submitted-code layers must remain separate. - Widyasari et al.
en078 | NEW | en285 | 0.14 | (2025), Explaining Explanations , DOI 10.1145/3708518; Papotti et al. (2024), security-patch reviewer acceptance, DOI 10.1007/s10664-024-10506-z; Jin & Chen (2026), Systematic Overcorrection , held, journal edition not l
en079 | NEW | en291 | 0.09 | /PAPER_B_BILINGUAL_INTEGRATED_22_20261122.md) retained without silently importing unverified findings.
Summary en: SAME 0, EDIT 0, NEW 79

## v24 · [Source](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/PAPER_B_BILINGUAL_POSITION_24_20261122.md)
### ko (89 sentences)
ko001 | NEW | ko001 | 0.10 | 소프트웨어 설계 원칙은 특정 변경에 대처하기 위한 조언이지만, 코드 검토와 AI 코딩 에이전트의 작업에서는 그 원칙의 이름이 때때로 수정안의 승인 또는 거절을 결정하는 규칙처럼 사용될 수 있다.
ko002 | NEW | ko003 | 0.34 | **우리는 조건부 설계 조언이 실제 요구와 반대 증거를 검토할 기회를 대체하며 구속력을 얻는 현상을 '운영상의 준공리화(operational quasi-axiomatization)'라는 반증 가능한 연구 대상으로 제안한다.
ko003 | NEW | ko004 | 0.11 | ** 이 표현은 수학적 공리화 자체를 비판하거나, 현재의 언어모델이 실제로 SOLID를 무조건 따르고 있다고 단정하지 않는다.
ko004 | NEW | ko019 | 0.20 | Meyer와 Martin의 개방–폐쇄 원칙 해석을 검토하면 설계가 무엇에 대해 닫혀 있어야 하는지는 예상하는 변경과 기존 호출자의 의무에 달려 있다.
ko005 | NEW | ko005 | 0.10 | 선행 SOLID 분류 벤치마크를 특정 코드 수정의 수용 판단과 구분하고, 같은 수정안을 서로 다른 요구와 보호 계약 아래 평가하는 제한적 재현 사례를 제시한다.
ko006 | NEW | ko006 | 0.04 | 이어 코딩 에이전트에 주어진 원칙 지시가 설명의 어휘만 바꾸는지, 실제 패치 선택을 바꾸는지, 반대 증거 이후의 판단까지 바꾸는지 시험하는 네 조건 연구를 제안한다.
ko007 | NEW | ko029 | 0.09 | 이 논문의 기여는 준공리화의 발생률을 보고하는 것이 아니라, 설계 원칙이 실제 소프트웨어 변경에 대해 어떤 권위를 행사하는지 경험적으로 묻는 독립적인 문제를 정의하는 데 있다.
ko008 | NEW | ko009 | 0.16 | 어떤 코드에 대해 '개방–폐쇄 원칙(OCP)을 위반했다'는 검토 의견이 나왔다고 하자.
ko009 | NEW | ko016 | 0.02 | 그 의견이 적절한 구조적 특징을 발견했을 수는 있다.
ko010 | NEW | ko010 | 0.05 | 그러나 해당 구조를 수정해야 하는지는 별개의 문제다.
ko011 | NEW | ko010 | 0.04 | 새 요구가 무엇인지, 기존 호출자가 어느 동작에 의존하는지, 수정할 수 있는 소스의 범위가 어디까지인지, 다른 구현이 가능한지에 따라 선택이 달라질 수 있다.
ko012 | NEW | ko046 | 0.08 | 설계 원칙이 설명하는 구조와, 그 원칙을 근거로 특정 패치를 승인하거나 거절하는 일은 동일하지 않다.
ko013 | NEW | ko009 | 0.04 | 이 차이가 중요한 것은 소프트웨어 설계의 조언이 점점 더 코드 생성·검토를 수행하는 도구에도 전달되기 때문이다.
ko014 | NEW | ko009 | 0.05 | 개발자는 원칙을 자신의 판단에 참고할 수도 있지만, 에이전트에게 명시적인 지시로 전달할 수도 있다.
ko015 | NEW | ko025 | 0.03 | 그 결과 원칙은 설명 문장에 머무르지 않고 어떤 파일을 고칠지, 어떤 리팩터링을 요구할지, 어느 대안을 배제할지에 영향을 줄 수 있다.
ko016 | NEW | ko008 | 0.03 | 다만 **원칙의 이름이 그 적용 범위를 입증하는 증거보다 더 큰 결정 권한을 갖게 되는지**는 따로 조사할 필요가 있다.
ko017 | NEW | ko024 | 0.21 | 우리는 이 문제를 '운영상의 준공리화'라고 부른다.
ko018 | NEW | ko022 | 0.03 | 이것은 AI가 실제로 그렇게 행동한다는 확정된 실증 결과가 아니라, 그러한 행동이 있는지 알아보기 위한 연구 가설이다.
ko019 | NEW | ko040 | 0.06 | 이 글은 (1) 역사적 설계 원칙에 원래 존재했던 조건과 예외를 복원하고, (2) 구조적 위반 분류와 특정 수정안의 수용 판단 사이에 필요한 근거를 구별하며, (3) 그 간극에서 AI 에이전트가 어떤 선택을 하는지 반증 가능하게 연구할 방법을 제안한다.
ko020 | NEW | ko064 | 0.09 | 객체지향 프로그래밍의 역사와 SOLID의 역사는 동일하지 않다.
ko021 | NEW | ko018 | 0.30 | Simula의 시뮬레이션·클래스, Smalltalk의 객체 메시지, Parnas의 정보 은닉, Liskov와 Wing의 행동적 하위타입은 서로 다른 문제와 평가 기준에서 발전했다.
ko022 | NEW | ko056 | 0.01 | 이들을 다섯 글자 약어가 처음부터 지배했던 단일한 설계 교리로 서술하면, 각각의 구별을 잃는다. , , .
ko023 | NEW | ko019 | 0.08 | Meyer의 초기 개방–폐쇄 설명은 모듈의 확장 가능성과 기존 사용자를 위한 안정된 설명을 함께 다룬다.
ko024 | NEW | ko020 | 0.06 | Martin은 의 도형 그리기 사례에서 새 도형의 지원과 도형 종류별 그리기 순서 변경을 구별했다.
ko025 | NEW | ko042 | 0.03 | 새로운 종류의 도형을 추가하는 데 적합했던 구조가, 이미 정해진 도형의 출력 순서를 바꾸는 요구에는 다른 수정 지점을 필요로 할 수 있다.
ko026 | NEW | ko020 | 0.06 | Martin의 핵심 문제는 모든 변화에 영원히 닫힌 설계를 찾는 일이 아니라 **어떤 변화에 대해 닫힘을 확보할지 선택하는 일**이었다.
ko027 | NEW | ko046 | 0.04 | 따라서 그 원저자를 무조건적인 형식 공리를 주장한 사람으로 취급하는 것은 역사적 근거에 맞지 않는다.
ko028 | NEW | ko019 | 0.08 | /13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md), [Martin 1996 사례 검토](.
ko029 | NEW | ko020 | 0.26 | /29_MARTIN_1996_STRATEGIC_CLOSURE.md).
ko030 | NEW | ko046 | 0.06 | 이 역사적 조건성은 과거 원칙이 현재에도 유용할 수 있다는 가능성을 배제하지 않는다.
ko031 | NEW | ko046 | 0.07 | 다만 원칙의 이름만으로 모든 코드 변경을 판정할 수 있다는 근거도 제공하지 않는다.
ko032 | NEW | ko020 | 0.03 | 어떤 변경 분포와 클라이언트 계약 아래에서 그 원칙이 좋은 예측을 하는지는 별도의 문제다.
ko033 | NEW | — | 0.00 | '공리'라는 비유에는 세 가지 혼동이 있다.
ko034 | NEW | ko023 | 0.17 | **형식적 공리화**는 명확한 전제와 추론 규칙을 설정하는 정당한 수학적 활동이다.
ko035 | NEW | ko023 | 0.13 | **전문직적 정전화**는 교육·문헌·실무를 거치며 특정 조언이 권위를 얻는 역사적 과정이다.
ko036 | NEW | ko024 | 0.09 | 그와 구별되는 **운영상의 준공리화**는 설계 원칙을 언급한 사실만으로, 실제 수정안을 판단하는 데 필요한 요구·계약·예외·대안의 검토가 생략되거나 밀려나는 행동에 관한 가설이다.
ko037 | NEW | ko024 | 0.03 | 어느 단계에서든 명시적 지시, 조직의 규칙 또는 계약이 원칙의 적용을 정당화한다면 이를 곧바로 부당한 준공리화로 분류해서는 안 된다.
ko038 | NEW | ko040 | 0.32 | 우리는 다음의 더 좁은 문제를 '원칙에서 수정안 판단으로의 전이(principle-to-patch transport)'라고 부른다.
ko039 | NEW | ko046 | 0.04 | 코드 (s)에 어떤 구조적 특징 (L(s))가 있다는 판정만으로 후보 수정안 (p)의 적법성이 결정되지 않는다.
ko040 | NEW | ko014 | 0.02 | 수정안을 받아들일 수 있는지는 적어도 새 요구 (D), 보존할 기존 동작 (C), 허가된 수정 권한 (A)와 실제 후보 (p)에 의해 달라진다. [ mathrm{Accept}(pmid D,C,A) eq f(L(s))quad ext{in general}.
ko041 | NEW | ko017 | 0.05 | ] 이 식은 새 계산법이나 독창적인 불가능성 정리가 아니다.
ko042 | NEW | ko005 | 0.04 | **구조적 라벨만으로 수정안의 승인 결정을 일반적으로 충분히 도출할 수 없다는 문제 제기를 압축한 표기**다.
ko043 | NEW | ko043 | 0.21 | 요구공학, Design by Contract, 문맥적 동등성과 기존 수정 탐색 연구는 이 구별의 중요한 선행 이론이다.
ko044 | NEW | ko068 | 0.05 | 우리가 새롭게 연구하자고 제안하는 것은 AI가 원칙의 언어를 사용할 때 이러한 다른 근거를 어디까지 고려하는지, 그리고 반대 증거가 주어지면 실제 결정을 어떻게 바꾸는지이다.
ko045 | NEW | ko062 | 0.05 | Pehlivan 등(2025)의 은 여러 프로그래밍 언어의 SOLID 위반을 LLM 프롬프트로 분류하는 문제를 다룬다.
ko046 | NEW | ko003 | 0.04 | 이 작업의 목적은 분류 성능을 조사하는 것이며, 개별 코드 수정안의 승인 권한을 실험했다는 뜻이 아니다.
ko047 | NEW | ko029 | 0.07 | 우리가 확보된 자료로 재감사한 OCP 부분에는 48개 제출 코드가 16번씩 나타난 768개 저장 응답 행과 24개의 서로 다른 마스킹된 지시문 틀이 있었다.
ko048 | NEW | ko046 | 0.08 | 이 수는 768개의 독립적인 유지보수 과제를 의미하지 않는다.
ko049 | NEW | ko031 | 0.07 | 저장 프롬프트에는 별도로 기술된 사례별 변경 요구나 보호할 호출자 계약이 없었지만, 코드 자체의 단서까지 전혀 없었다고 단정할 수는 없다.
ko050 | EDIT | ko028 | 0.60 | /18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md).
ko051 | NEW | ko066 | 0.03 | 이 차이를 검토하기 위해 우리는 오래된 도서관 프로그램을 변형한 작은 **연구자 작성 재현 사례**를 사용했다.
ko052 | NEW | ko032 | 0.22 | 한 고정 패치는 기술보고서를 추가하지만 정오표 지원은 제공하지 않고, 기존 책 출력의 접두어를 변경한다.
ko053 | NEW | ko025 | 0.05 | 정오표를 새 요구로 추가하거나 이전 접두어를 기존 호출자 계약으로 보호하면, 같은 패치에 대한 승인 판단이 달라진다.
ko054 | NEW | ko034 | 0.02 | 코드와 패치 자체가 변했기 때문이 아니라 **판정할 명세가 달라졌기 때문**이다.
ko055 | NEW | ko034 | 0.06 | 이는 우리가 지정한 네 조건에서 관찰된 제한적 결과이며 실제 프로젝트에서 이러한 상황이 얼마나 발생하는지 보여 주지 않는다.
ko056 | NEW | ko032 | 0.44 | /31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md).
ko057 | NEW | ko047 | 0.07 | 관건은 SOLID 위반을 분류하는 일이 무의미하다는 주장이 아니다.
ko058 | NEW | ko025 | 0.03 | 분류는 검토자가 의심해야 할 위치를 알려 줄 수 있다.
ko059 | NEW | ko010 | 0.03 | 다만 분류 정확도가 곧 특정 패치의 적법한 거절을 의미하지는 않는다.
ko060 | NEW | ko022 | 0.05 | 이 간극을 보고하려면 분류에 사용한 코드와, 실제 수정을 판단할 근거를 별도로 기록해야 한다.
ko061 | NEW | ko064 | 0.07 | 프로젝트 수준의 지침을 전달하는 통로가 존재한다고 해서 특정 모델이 SOLID를 공리로 학습했다는 결론은 나오지 않는다.
ko062 | NEW | ko064 | 0.06 | 예컨대 Gloaguen 등(2026)은 을 조사했지만, 이는 SOLID의 준공리화나 그 훈련 기원을 직접 검증하는 연구가 아니다.
ko063 | NEW | ko027 | 0.04 | 프롬프트, 저장소 규칙, 모델이 생성한 설명, 실제 패치, 사람의 최종 승인은 서로 다른 관찰 단위다.
ko064 | NEW | ko049 | 0.13 | 따라서 우리가 —추가 조언 없음(NONE), 강한 SOLID 지시(HARD_SOLID), 범위가 명시된 SOLID 지시(SCOPED_SOLID), 요구·계약 증거 중심 지시(EVIDENCE_CONDITIONAL)—은 동일한 소스 버전·요구·검사·도구 예산 아래에서 비교해야 한다.
ko065 | NEW | ko025 | 0.06 | 결과도 원칙을 언급한 단어 수, 실제 코드 변경, 기존 호출자 계약의 보존, 판단의 수정·기권으로 나누어 평가해야 한다.
ko066 | NEW | ko047 | 0.15 | 에이전트가 HARD_SOLID 지시를 따랐다는 사실 자체는 준공리화를 입증하지 않는다.
ko067 | NEW | ko009 | 0.05 | 에이전트는 원칙을 독립적인 진실로 믿는 대신, 방금 받은 명시적 지시에 복종했을 수 있다.
ko068 | NEW | ko022 | 0.03 | 설령 잘못된 패치가 나왔더라도 원인이 지시 충돌인지, 코드 이해 실패인지, 원칙의 부당한 권위 부여인지 구별해야 한다.
ko069 | NEW | ko044 | 0.04 | **일관된 원칙 언급과 반대 증거 이후에도 지속되는 불합리한 수정안 거절은 같은 관측이 아니다.
ko070 | NEW | ko014 | 0.15 | /53_PAPER_B_R11_COMPLIANCE_VS_QUASI_AXIOM_IDENTIFICATION.md).
ko071 | NEW | ko050 | 0.06 | 후속 실험에서는 원칙과 요구가 일치하는 과제, 기계적인 적용이 기존 계약과 충돌하는 과제, 필요한 정보가 불충분한 과제를 모두 포함해야 한다.
ko072 | NEW | ko013 | 0.06 | 강한 SOLID 지시가 어떤 과제에서는 성능을 개선할 수 있다는 가능성을 먼저 열어 둬야 한다.
ko073 | NEW | ko024 | 0.05 | 반대로 네 조건이 모두 동일한 올바른 코드를 생성하거나, 설명의 어휘만 달라진다면 준공리화에 대한 행동적 증거는 얻지 못한 것이다.
ko074 | NEW | ko056 | 0.04 | 정당한 반대 증거를 받은 뒤 에이전트가 수정을 재고하는지도 별도로 평가할 수 있지만, 그 근거는 동일한 지시 우선순위와 소스 계약 아래 해석해야 한다.
ko075 | NEW | ko062 | 0.04 | ** 프롬프트와 결과 기록기, 제한적 원본 Go 실험은 준비돼 있지만 이를 실제 네 조건 에이전트 비교의 결과로 바꾸어 서술해서는 안 된다.
ko076 | NEW | ko009 | 0.06 | 설계 원칙을 조건부로 다루자는 제안은 이미 오래된 소프트웨어 공학의 직관 및 형식 이론과 연결된다.
ko077 | NEW | ko030 | 0.03 | 이 논문의 주장은 모든 기존 원칙을 폐기하거나, 요구·계약을 처음 발견했다는 것이 아니다.
ko078 | NEW | ko008 | 0.03 | AI가 코드를 생성하거나 검토하는 과정에서 **원칙이 어떤 관찰 가능한 결정 권한을 행사하는지**를 연구의 중심 변수로 삼자는 것이다.
ko079 | NEW | ko042 | 0.02 | 충분히 명시된 요구 아래서 엄격한 설계 지침이 더 안정적인 코드를 만들 수 있다.
ko080 | NEW | ko064 | 0.09 | 명시적 지시가 없는 모델은 SOLID를 전혀 적용하지 않을 수 있다.
ko081 | NEW | ko054 | 0.04 | 강한 지시는 코드에는 영향을 주지 않고 설명에만 남을 수 있다.
ko082 | NEW | ko006 | 0.05 | 이러한 결과를 허용하지 않는 연구라면 '준공리화'라는 표현 자체가 또 다른 검증되지 않은 교리가 되고 만다.
ko083 | NEW | ko069 | 0.05 | 소프트웨어 공학이 앞으로 필요로 하는 것은 원칙을 따르는 모델이나 원칙을 반대하는 모델이라는 이분법보다, **원칙의 적용을 정당화하는 요구·계약·반대 증거를 확인하고 그에 따라 결정을 바꿀 수 있는 모델**인지 묻는 연구다.
ko084 | NEW | ko064 | 0.11 | 이러한 문제를 정의하는 것이 Paper B의 기여다.
ko085 | NEW | ko002 | 0.09 | 특정 아키텍처의 비용 우위, 장기적 조직 성과와 새 설계 법칙의 형식 증명은 EvoNOMOS의 후속 연구에서 별도로 검증할 수 있다.
ko086 | NEW | ko001 | 0.06 | SOLID 같은 설계 원칙의 가치는 모든 수정에 적용되는 규칙이라는 데 있지 않을 수 있다.
ko087 | NEW | ko010 | 0.05 | 오히려 어떤 변화에서 유용하고 어떤 계약 앞에서 수정되어야 하는지를 설명할 수 있을 때 그 조언은 더 신뢰할 만해진다.
ko088 | NEW | ko001 | 0.10 | 우리는 AI 코딩 에이전트 시대에 설계 원칙이 설명에서 실제 선택으로 넘어가는 순간을 독립적인 실증 연구 대상으로 제안했다.
ko089 | NEW | ko012 | 0.04 | **원칙의 이름이 아니라, 그 이름에 부여된 결정 권한과 반대 증거 이후의 행동을 연구하자.
Summary ko: SAME 0, EDIT 1, NEW 88

### en (92 sentences)
en001 | NEW | en001 | 0.25 | Software design principles offer guidance about how a system might accommodate change.
en002 | NEW | en050 | 0.15 | In code review and AI-assisted development, however, a principle's name may acquire the force of a rule for accepting, rejecting, or reshaping an individual patch.
en003 | NEW | en004 | 0.27 | We propose **operational quasi-axiomatization** as a falsifiable research target: the possibility that conditional design advice comes to displace examination of actual requirements, protected client behavior, exceptions
en004 | NEW | en005 | 0.19 | This is neither a critique of mathematical axiomatization nor an empirical claim that current coding agents already treat SOLID as an unconditional truth.
en005 | NEW | en010 | 0.19 | Early accounts of the Open–Closed Principle made extensibility relative to anticipated change and stable client obligations.
en006 | NEW | en050 | 0.20 | We distinguish a structural-violation classification from the decision whether a particular repair is acceptable, illustrate that distinction with one explicitly constructed, fixed-patch contract example, and outline con
en007 | NEW | en072 | 0.16 | The empirical target is not the frequency of SOLID vocabulary but the authority that principle language exercises over source changes and the way decisions respond to counterevidence.
en008 | NEW | en007 | 0.16 | We offer a position and research agenda, not an estimate of agent behavior.
en009 | NEW | en010 | 0.41 | Suppose a reviewer states that a module violates the Open–Closed Principle (OCP).
en010 | NEW | en046 | 0.11 | The statement may correctly identify a design pattern.
en011 | NEW | en011 | 0.14 | It does not, by itself, establish which future change is required, which existing clients must continue working, which source files can be edited, or whether a different repair is available.
en012 | NEW | en012 | 0.17 | The same pattern may be a useful warning in one maintenance task and irrelevant to the acceptance of a particular patch in another.
en013 | NEW | en054 | 0.13 | Recognizing a principle-related structure and using that recognition to dispose of a concrete patch are distinct acts.
en014 | NEW | en001 | 0.16 | This distinction matters as software design advice enters coding-agent workflows.
en015 | NEW | en017 | 0.12 | A human may consider a principle among several reasons; an agent may receive it as an explicit project instruction or task-specific constraint.
en016 | NEW | en054 | 0.12 | The instruction can then influence the code it writes and the alternatives it rejects.
en017 | NEW | en013 | 0.11 | Such influence may be useful and fully authorized.
en018 | NEW | en072 | 0.16 | The empirical question is whether a principle's *name* is sometimes given decision authority beyond the scope and evidence that justify its use.
en019 | EDIT | en015 | 0.48 | We call the possibility **operational quasi-axiomatization**.
en020 | NEW | en060 | 0.14 | We do not presume that it is prevalent, that a foundation model internally believes in SOLID, or that an original designer intended to state universal mathematical axioms.
en021 | NEW | en025 | 0.13 | We argue for a falsifiable research problem linking historical design advice, patch-specific authority, and the observable behavior of coding agents.
en022 | NEW | en019 | 0.16 | The histories of object orientation and SOLID should not be collapsed into one continuous five-rule doctrine.
en023 | NEW | en020 | 0.37 | Simula's class-based simulation, Smalltalk's message-oriented accounts, Parnas's information-hiding criterion, and Liskov and Wing's behavioral subtyping addressed different design questions.
en024 | NEW | en013 | 0.13 | Their differences matter because they associate software quality with distinct observations and changes rather than a single syntactic label. ; ; .
en025 | NEW | en020 | 0.12 | Meyer's account of open and closed modules joins extension with the stability of descriptions used by clients.
en026 | NEW | en021 | 0.15 | Martin's then makes strategic closure explicit.
en027 | NEW | en071 | 0.11 | A drawing routine may accommodate another kind of shape without revision while a request to change the ordering of shapes may require a different locus of modification.
en028 | NEW | en021 | 0.11 | Which change should be cheap is an engineering choice, not a universal property conferred by the OCP label.
en029 | NEW | en070 | 0.12 | It would mischaracterize Martin to claim that he formally established five unconditional design axioms.
en030 | NEW | en021 | 0.13 | /13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md); [Martin's strategic-closure example](.
en031 | NEW | en021 | 0.13 | /29_MARTIN_1996_STRATEGIC_CLOSURE.md).
en032 | NEW | en025 | 0.12 | Historical advice can remain useful in modern development without being beyond revision.
en033 | NEW | en049 | 0.15 | The question is which requirements and future changes justify its authority.
en034 | NEW | en077 | 0.12 | Three ideas must be separated.
en035 | EDIT | en024 | 0.59 | **Formal axiomatization** specifies premises and inference rules, which can be legitimate and precise.
en036 | NEW | en025 | 0.44 | **Professional canonization** describes a historical process in which repeated advice becomes widely authoritative.
en037 | NEW | en004 | 0.21 | **Operational quasi-axiomatization** concerns a narrower, potentially observable event: the use of a design principle as a decisive constraint in an actual modification despite relevant evidence that its purported author
en038 | NEW | en072 | 0.13 | The latter is not established merely because an agent uses imperative language or follows an explicitly authorized instruction.
en039 | NEW | en045 | 0.46 | We call the narrower inference step the **principle-to-patch transport problem**.
en040 | NEW | en053 | 0.11 | A structural label (L(s)) for source (s) does not generally determine whether a patch (p) should be accepted.
en041 | NEW | en070 | 0.14 | Acceptance depends on a specified demand (D), existing client obligations (C), edit authority (A), and the particular candidate.
en042 | NEW | en029 | 0.09 | Symbolically, (mathrm{Accept}(pmid D,C,A)) cannot in general be recovered from (L(s)) alone.
en043 | NEW | en015 | 0.08 | This is an explanatory notation, not a newly proven undecidability theorem.
en044 | NEW | en049 | 0.25 | Requirements engineering, Design by Contract, contextual equivalence, and source-aware repair all provide relevant prior theory.
en045 | NEW | en072 | 0.20 | Our proposed contribution is to turn the *operational authority* exercised by principle language into a direct research question for AI-assisted development. , studies prompting LLMs to identify SOLID violations across l
en046 | NEW | en012 | 0.15 | Such classification is not itself a test of whether a particular patch should be accepted or rejected.
en047 | NEW | en032 | 0.32 | In our prior inspection of its OCP archive, 48 submitted code examples occurred across 768 stored response rows, with 24 distinguishable masked prompt scaffolds.
en048 | NEW | en031 | 0.33 | These are not 768 independent maintenance tasks.
en049 | NEW | en052 | 0.16 | Item-specific protected client contracts or change demands were not separately stated in the saved prompt templates; code-internal clues may nonetheless remain.
en050 | NEW | en030 | 0.43 | /18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md).
en051 | NEW | en035 | 0.25 | To expose the difference we constructed a small library-patch example.
en052 | NEW | en037 | 0.42 | A fixed proposed addition supports technical reports but omits errata and changes an older book prefix.
en053 | NEW | en038 | 0.20 | Varying whether errata are required and whether the older prefix is contractually protected changes whether that *same patch* is admissible under the authored specification.
en054 | NEW | en016 | 0.15 | The difference is in the requirements against which the patch is evaluated, not an observed industrial reviewer or coding agent.
en055 | NEW | en036 | 0.39 | /31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md).
en056 | NEW | en033 | 0.09 | This example does not make structural classifiers useless.
en057 | NEW | en046 | 0.10 | A classifier may correctly direct attention to code that deserves scrutiny.
en058 | NEW | en070 | 0.20 | Our point is that an individual maintenance decision also requires traceable grounds for the scope of the request, client protections, edit authority, and alternatives.
en059 | NEW | en049 | 0.10 | Repository instructions are a real delivery channel for coding agents, but their availability says nothing by itself about the contents of model pretraining.
en060 | NEW | en006 | 0.12 | For example, examine repository-level context files and coding-agent task performance; they do not directly measure SOLID-induced patch rejection or prove a training-origin mechanism.
en061 | NEW | en029 | 0.15 | Prompts, source context, model explanations, generated patches, tests, and final review decisions must be measured separately.
en062 | NEW | en052 | 0.27 | Our inherited compares NONE, HARD_SOLID, SCOPED_SOLID, and EVIDENCE_CONDITIONAL advice on the same pinned source, task, tests, rights and tool budget.
en063 | NEW | en060 | 0.17 | Outcomes would distinguish code correctness and preserved clients from the language used to justify the patch; they would also record revision or abstention after independently sourced contrary evidence.
en064 | NEW | en055 | 0.11 | A serious identification objection arises here.
en065 | NEW | en060 | 0.12 | An agent that follows HARD_SOLID may simply be obeying the experiment's instruction, rather than treating SOLID as an independent truth.
en066 | NEW | en036 | 0.10 | Even a bad patch may result from conflicts between instructions, weak source comprehension, or incomplete tests.
en067 | NEW | en045 | 0.15 | We therefore propose examining tasks where principle-aligned design is valid, tasks where a mechanical refactoring would break a protected obligation, and cases where the available evidence does not warrant a disposition
en068 | NEW | en010 | 0.13 | A conforming hard-rule implementation may win in the first stratum; models may tie throughout; words may change without changes to source.
en069 | NEW | en027 | 0.12 | All of these are legitimate rival outcomes.
en070 | NEW | en052 | 0.12 | Subsequent factual rebuttals can test responsiveness, but must be interpreted under the actual instruction hierarchy rather than treated as direct access to internal beliefs.
en071 | NEW | en018 | 0.09 | [Identification analysis](.
en072 | NEW | en015 | 0.12 | /53_PAPER_B_R11_COMPLIANCE_VS_QUASI_AXIOM_IDENTIFICATION.md).
en073 | NEW | en060 | 0.13 | No independent four-arm coding-agent execution has yet been performed.
en074 | NEW | en054 | 0.14 | The proposed study can estimate certain **effects of present instructions** if implemented with valid randomization and evaluation.
en075 | NEW | en025 | 0.21 | It cannot, without further evidence, identify the causal influence of hidden pretraining examples or the long-run historical process of professional canonization.
en076 | NEW | en049 | 0.20 | Arguing that design advice should remain revisable is compatible with established software engineering theory; we do not claim to have invented contracts, exceptions, or contextual judgment.
en077 | NEW | en069 | 0.07 | Nor do we recommend discarding SOLID.
en078 | NEW | en072 | 0.14 | We instead ask that the authority principle language exercises in a coding workflow be an explicit empirical variable.
en079 | NEW | en054 | 0.17 | Its outcomes include justified adherence, unjustified insistence, evidence-responsive revision, ordinary instruction compliance, lexical repetition, and abstention when obligations are unknown.
en080 | NEW | en041 | 0.06 | This framing allows the hypothesis to fail.
en081 | NEW | en057 | 0.25 | Strict guidance might improve maintenance outcomes in some contexts.
en082 | NEW | en055 | 0.13 | Agents may generate equally good patches under all conditions.
en083 | NEW | en010 | 0.13 | A supposed principle effect may disappear once a source-aware classical planning baseline is given the same information.
en084 | NEW | en027 | 0.16 | Such results constrain the phenomenon rather than threaten the legitimacy of its investigation.
en085 | NEW | en026 | 0.17 | What matters is not whether a coding agent can recite a principle but whether its actual choices reflect the requirements, client contracts, and counterexamples that bear on the decision.
en086 | NEW | en067 | 0.13 | Source-level architectural reversal and maintenance cost can be investigated in separate EvoNOMOS studies; they need not be claimed by this position paper.
en087 | NEW | en049 | 0.16 | A design principle earns practical authority when its use can be justified for the changes and obligations at hand, not merely through repetition of its name.
en088 | NEW | en004 | 0.23 | We propose operational quasi-axiomatization as a falsifiable question about when AI-assisted software decisions elevate conditional advice into binding action.
en089 | NEW | en072 | 0.16 | The immediate research opportunity is to observe **what the principle changes in a patch, and what credible counterevidence changes in the agent's decision**.
en090 | NEW | en071 | 0.14 | This is the proposed object of study, not an already demonstrated fact. --- - The archival OCP counts, library reconstruction and original Go witnesses are prior EvoNOMOS work; none is an observed four-arm agent-effect e
en091 | NEW | en070 | 0.14 | The above text primarily paraphrases ideas and cites the recorded source chain. - F37's app-owned router negative control established equal capability for a bounded reserved-route wrapper; including its full details here
en092 | NEW | en072 | 0.15 | Keep in v22/v23 or supporting archive. - The earlier formal discussion of principle-to-patch inference has requirements-engineering precedents; do not claim first invention of that distinction. - A null result in the fut
Summary en: SAME 0, EDIT 2, NEW 90

## v25 · [Source](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/PAPER_B_BILINGUAL_POSITION_25_20261122.md)
### ko (98 sentences)
ko001 | SAME | ko001 | 1.00 | 소프트웨어 설계 원칙은 특정 변경에 대처하기 위한 조언이지만, 코드 검토와 AI 코딩 에이전트의 작업에서는 그 원칙의 이름이 때때로 수정안의 승인 또는 거절을 결정하는 규칙처럼 사용될 수 있다.
ko002 | SAME | ko002 | 1.00 | **우리는 조건부 설계 조언이 실제 요구와 반대 증거를 검토할 기회를 대체하며 구속력을 얻는 현상을 '운영상의 준공리화(operational quasi-axiomatization)'라는 반증 가능한 연구 대상으로 제안한다.
ko003 | SAME | ko003 | 1.00 | ** 이 표현은 수학적 공리화 자체를 비판하거나, 현재의 언어모델이 실제로 SOLID를 무조건 따르고 있다고 단정하지 않는다.
ko004 | SAME | ko004 | 1.00 | Meyer와 Martin의 개방–폐쇄 원칙 해석을 검토하면 설계가 무엇에 대해 닫혀 있어야 하는지는 예상하는 변경과 기존 호출자의 의무에 달려 있다.
ko005 | SAME | ko005 | 1.00 | 선행 SOLID 분류 벤치마크를 특정 코드 수정의 수용 판단과 구분하고, 같은 수정안을 서로 다른 요구와 보호 계약 아래 평가하는 제한적 재현 사례를 제시한다.
ko006 | SAME | ko006 | 1.00 | 이어 코딩 에이전트에 주어진 원칙 지시가 설명의 어휘만 바꾸는지, 실제 패치 선택을 바꾸는지, 반대 증거 이후의 판단까지 바꾸는지 시험하는 네 조건 연구를 제안한다.
ko007 | SAME | ko007 | 1.00 | 이 논문의 기여는 준공리화의 발생률을 보고하는 것이 아니라, 설계 원칙이 실제 소프트웨어 변경에 대해 어떤 권위를 행사하는지 경험적으로 묻는 독립적인 문제를 정의하는 데 있다.
ko008 | SAME | ko008 | 1.00 | 어떤 코드에 대해 '개방–폐쇄 원칙(OCP)을 위반했다'는 검토 의견이 나왔다고 하자.
ko009 | SAME | ko009 | 1.00 | 그 의견이 적절한 구조적 특징을 발견했을 수는 있다.
ko010 | SAME | ko010 | 1.00 | 그러나 해당 구조를 수정해야 하는지는 별개의 문제다.
ko011 | SAME | ko011 | 1.00 | 새 요구가 무엇인지, 기존 호출자가 어느 동작에 의존하는지, 수정할 수 있는 소스의 범위가 어디까지인지, 다른 구현이 가능한지에 따라 선택이 달라질 수 있다.
ko012 | SAME | ko012 | 1.00 | 설계 원칙이 설명하는 구조와, 그 원칙을 근거로 특정 패치를 승인하거나 거절하는 일은 동일하지 않다.
ko013 | SAME | ko013 | 1.00 | 이 차이가 중요한 것은 소프트웨어 설계의 조언이 점점 더 코드 생성·검토를 수행하는 도구에도 전달되기 때문이다.
ko014 | SAME | ko014 | 1.00 | 개발자는 원칙을 자신의 판단에 참고할 수도 있지만, 에이전트에게 명시적인 지시로 전달할 수도 있다.
ko015 | SAME | ko015 | 1.00 | 그 결과 원칙은 설명 문장에 머무르지 않고 어떤 파일을 고칠지, 어떤 리팩터링을 요구할지, 어느 대안을 배제할지에 영향을 줄 수 있다.
ko016 | SAME | ko016 | 1.00 | 다만 **원칙의 이름이 그 적용 범위를 입증하는 증거보다 더 큰 결정 권한을 갖게 되는지**는 따로 조사할 필요가 있다.
ko017 | SAME | ko017 | 1.00 | 우리는 이 문제를 '운영상의 준공리화'라고 부른다.
ko018 | SAME | ko018 | 1.00 | 이것은 AI가 실제로 그렇게 행동한다는 확정된 실증 결과가 아니라, 그러한 행동이 있는지 알아보기 위한 연구 가설이다.
ko019 | SAME | ko019 | 1.00 | 이 글은 (1) 역사적 설계 원칙에 원래 존재했던 조건과 예외를 복원하고, (2) 구조적 위반 분류와 특정 수정안의 수용 판단 사이에 필요한 근거를 구별하며, (3) 그 간극에서 AI 에이전트가 어떤 선택을 하는지 반증 가능하게 연구할 방법을 제안한다.
ko020 | SAME | ko020 | 1.00 | 객체지향 프로그래밍의 역사와 SOLID의 역사는 동일하지 않다.
ko021 | SAME | ko021 | 1.00 | Simula의 시뮬레이션·클래스, Smalltalk의 객체 메시지, Parnas의 정보 은닉, Liskov와 Wing의 행동적 하위타입은 서로 다른 문제와 평가 기준에서 발전했다.
ko022 | SAME | ko022 | 1.00 | 이들을 다섯 글자 약어가 처음부터 지배했던 단일한 설계 교리로 서술하면, 각각의 구별을 잃는다. , , .
ko023 | SAME | ko023 | 1.00 | Meyer의 초기 개방–폐쇄 설명은 모듈의 확장 가능성과 기존 사용자를 위한 안정된 설명을 함께 다룬다.
ko024 | SAME | ko024 | 1.00 | Martin은 의 도형 그리기 사례에서 새 도형의 지원과 도형 종류별 그리기 순서 변경을 구별했다.
ko025 | SAME | ko025 | 1.00 | 새로운 종류의 도형을 추가하는 데 적합했던 구조가, 이미 정해진 도형의 출력 순서를 바꾸는 요구에는 다른 수정 지점을 필요로 할 수 있다.
ko026 | SAME | ko026 | 1.00 | Martin의 핵심 문제는 모든 변화에 영원히 닫힌 설계를 찾는 일이 아니라 **어떤 변화에 대해 닫힘을 확보할지 선택하는 일**이었다.
ko027 | SAME | ko027 | 1.00 | 따라서 그 원저자를 무조건적인 형식 공리를 주장한 사람으로 취급하는 것은 역사적 근거에 맞지 않는다.
ko028 | SAME | ko028 | 1.00 | /13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md), [Martin 1996 사례 검토](.
ko029 | SAME | ko029 | 1.00 | /29_MARTIN_1996_STRATEGIC_CLOSURE.md).
ko030 | SAME | ko030 | 1.00 | 이 역사적 조건성은 과거 원칙이 현재에도 유용할 수 있다는 가능성을 배제하지 않는다.
ko031 | SAME | ko031 | 1.00 | 다만 원칙의 이름만으로 모든 코드 변경을 판정할 수 있다는 근거도 제공하지 않는다.
ko032 | SAME | ko032 | 1.00 | 어떤 변경 분포와 클라이언트 계약 아래에서 그 원칙이 좋은 예측을 하는지는 별도의 문제다.
ko033 | SAME | ko033 | 1.00 | '공리'라는 비유에는 세 가지 혼동이 있다.
ko034 | SAME | ko034 | 1.00 | **형식적 공리화**는 명확한 전제와 추론 규칙을 설정하는 정당한 수학적 활동이다.
ko035 | SAME | ko035 | 1.00 | **전문직적 정전화**는 교육·문헌·실무를 거치며 특정 조언이 권위를 얻는 역사적 과정이다.
ko036 | SAME | ko036 | 1.00 | 그와 구별되는 **운영상의 준공리화**는 설계 원칙을 언급한 사실만으로, 실제 수정안을 판단하는 데 필요한 요구·계약·예외·대안의 검토가 생략되거나 밀려나는 행동에 관한 가설이다.
ko037 | SAME | ko037 | 1.00 | 어느 단계에서든 명시적 지시, 조직의 규칙 또는 계약이 원칙의 적용을 정당화한다면 이를 곧바로 부당한 준공리화로 분류해서는 안 된다.
ko038 | SAME | ko038 | 1.00 | 우리는 다음의 더 좁은 문제를 '원칙에서 수정안 판단으로의 전이(principle-to-patch transport)'라고 부른다.
ko039 | SAME | ko039 | 1.00 | 코드 (s)에 어떤 구조적 특징 (L(s))가 있다는 판정만으로 후보 수정안 (p)의 적법성이 결정되지 않는다.
ko040 | SAME | ko040 | 1.00 | 수정안을 받아들일 수 있는지는 적어도 새 요구 (D), 보존할 기존 동작 (C), 허가된 수정 권한 (A)와 실제 후보 (p)에 의해 달라진다. [ mathrm{Accept}(pmid D,C,A) eq f(L(s))quad ext{in general}.
ko041 | SAME | ko041 | 1.00 | ] 이 식은 새 계산법이나 독창적인 불가능성 정리가 아니다.
ko042 | SAME | ko042 | 1.00 | **구조적 라벨만으로 수정안의 승인 결정을 일반적으로 충분히 도출할 수 없다는 문제 제기를 압축한 표기**다.
ko043 | SAME | ko043 | 1.00 | 요구공학, Design by Contract, 문맥적 동등성과 기존 수정 탐색 연구는 이 구별의 중요한 선행 이론이다.
ko044 | SAME | ko044 | 1.00 | 우리가 새롭게 연구하자고 제안하는 것은 AI가 원칙의 언어를 사용할 때 이러한 다른 근거를 어디까지 고려하는지, 그리고 반대 증거가 주어지면 실제 결정을 어떻게 바꾸는지이다.
ko045 | NEW | ko039 | 0.08 | 이 문제는 클래스 기반 코드에 한정되지 않는다.
ko046 | NEW | ko072 | 0.04 | Go에서는 인터페이스와 메서드뿐 아니라 함수를 값으로 전달하는 콜백 합성으로도 동작을 확장할 수 있다.
ko047 | NEW | ko039 | 0.11 | 어느 쪽이 OCP에 더 충실한지는 문법만으로 결정되지 않는다.
ko048 | NEW | ko025 | 0.03 | 예를 들어 새로운 처리 함수를 등록하는 요구에 두 설계가 모두 적합할 수도 있고, 기존 콜백 규약이나 인터페이스 계약을 변경하는 요구에는 각각 다른 영향 범위가 나타날 수도 있다.
ko049 | NEW | ko077 | 0.07 | Go를 순수 함수형 언어로 간주하거나, 함수 합성이 자동으로 더 좋은 설계라고 선언하려는 것이 아니다.
ko050 | NEW | ko060 | 0.08 | 이것은 **동일한 원칙 이름이 서로 다른 구현 관습에 적용될 때 실제 수정 판단의 근거를 별도로 확인해야 한다**는 가능성을 보여 주는 개념적 비교이며, 실측한 비용·성능 결과는 아니다. , , [비교 연구 메모](.
ko051 | NEW | ko070 | 0.09 | /55_PAPER_B_R13_PARADIGM_TRANSFER_AND_CALLBACK_NEGATIVE_CONTROL.md).
ko052 | SAME | ko045 | 1.00 | Pehlivan 등(2025)의 은 여러 프로그래밍 언어의 SOLID 위반을 LLM 프롬프트로 분류하는 문제를 다룬다.
ko053 | SAME | ko046 | 1.00 | 이 작업의 목적은 분류 성능을 조사하는 것이며, 개별 코드 수정안의 승인 권한을 실험했다는 뜻이 아니다.
ko054 | SAME | ko047 | 1.00 | 우리가 확보된 자료로 재감사한 OCP 부분에는 48개 제출 코드가 16번씩 나타난 768개 저장 응답 행과 24개의 서로 다른 마스킹된 지시문 틀이 있었다.
ko055 | SAME | ko048 | 1.00 | 이 수는 768개의 독립적인 유지보수 과제를 의미하지 않는다.
ko056 | SAME | ko049 | 1.00 | 저장 프롬프트에는 별도로 기술된 사례별 변경 요구나 보호할 호출자 계약이 없었지만, 코드 자체의 단서까지 전혀 없었다고 단정할 수는 없다.
ko057 | SAME | ko050 | 1.00 | /18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md).
ko058 | SAME | ko051 | 1.00 | 이 차이를 검토하기 위해 우리는 오래된 도서관 프로그램을 변형한 작은 **연구자 작성 재현 사례**를 사용했다.
ko059 | SAME | ko052 | 1.00 | 한 고정 패치는 기술보고서를 추가하지만 정오표 지원은 제공하지 않고, 기존 책 출력의 접두어를 변경한다.
ko060 | SAME | ko053 | 1.00 | 정오표를 새 요구로 추가하거나 이전 접두어를 기존 호출자 계약으로 보호하면, 같은 패치에 대한 승인 판단이 달라진다.
ko061 | SAME | ko054 | 1.00 | 코드와 패치 자체가 변했기 때문이 아니라 **판정할 명세가 달라졌기 때문**이다.
ko062 | SAME | ko055 | 1.00 | 이는 우리가 지정한 네 조건에서 관찰된 제한적 결과이며 실제 프로젝트에서 이러한 상황이 얼마나 발생하는지 보여 주지 않는다.
ko063 | SAME | ko056 | 1.00 | /31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md).
ko064 | SAME | ko057 | 1.00 | 관건은 SOLID 위반을 분류하는 일이 무의미하다는 주장이 아니다.
ko065 | SAME | ko058 | 1.00 | 분류는 검토자가 의심해야 할 위치를 알려 줄 수 있다.
ko066 | SAME | ko059 | 1.00 | 다만 분류 정확도가 곧 특정 패치의 적법한 거절을 의미하지는 않는다.
ko067 | SAME | ko060 | 1.00 | 이 간극을 보고하려면 분류에 사용한 코드와, 실제 수정을 판단할 근거를 별도로 기록해야 한다.
ko068 | SAME | ko061 | 1.00 | 프로젝트 수준의 지침을 전달하는 통로가 존재한다고 해서 특정 모델이 SOLID를 공리로 학습했다는 결론은 나오지 않는다.
ko069 | SAME | ko062 | 1.00 | 예컨대 Gloaguen 등(2026)은 을 조사했지만, 이는 SOLID의 준공리화나 그 훈련 기원을 직접 검증하는 연구가 아니다.
ko070 | SAME | ko063 | 1.00 | 프롬프트, 저장소 규칙, 모델이 생성한 설명, 실제 패치, 사람의 최종 승인은 서로 다른 관찰 단위다.
ko071 | SAME | ko064 | 1.00 | 따라서 우리가 —추가 조언 없음(NONE), 강한 SOLID 지시(HARD_SOLID), 범위가 명시된 SOLID 지시(SCOPED_SOLID), 요구·계약 증거 중심 지시(EVIDENCE_CONDITIONAL)—은 동일한 소스 버전·요구·검사·도구 예산 아래에서 비교해야 한다.
ko072 | SAME | ko065 | 1.00 | 결과도 원칙을 언급한 단어 수, 실제 코드 변경, 기존 호출자 계약의 보존, 판단의 수정·기권으로 나누어 평가해야 한다.
ko073 | SAME | ko066 | 1.00 | 에이전트가 HARD_SOLID 지시를 따랐다는 사실 자체는 준공리화를 입증하지 않는다.
ko074 | SAME | ko067 | 1.00 | 에이전트는 원칙을 독립적인 진실로 믿는 대신, 방금 받은 명시적 지시에 복종했을 수 있다.
ko075 | SAME | ko068 | 1.00 | 설령 잘못된 패치가 나왔더라도 원인이 지시 충돌인지, 코드 이해 실패인지, 원칙의 부당한 권위 부여인지 구별해야 한다.
ko076 | NEW | ko080 | 0.03 | 상위 지시가 특정 설계 형태를 정당하게 강제한다면, 그 형태를 고수하는 것은 명시된 정책의 준수일 수 있다.
ko077 | NEW | ko074 | 0.07 | 반대 증거의 출처와 지시 우선순위를 고정하지 않은 채 이를 '교조적 태도'로 점수화해서는 안 된다.
ko078 | SAME | ko069 | 1.00 | **일관된 원칙 언급과 반대 증거 이후에도 지속되는 불합리한 수정안 거절은 같은 관측이 아니다.
ko079 | SAME | ko070 | 1.00 | /53_PAPER_B_R11_COMPLIANCE_VS_QUASI_AXIOM_IDENTIFICATION.md).
ko080 | SAME | ko071 | 1.00 | 후속 실험에서는 원칙과 요구가 일치하는 과제, 기계적인 적용이 기존 계약과 충돌하는 과제, 필요한 정보가 불충분한 과제를 모두 포함해야 한다.
ko081 | SAME | ko072 | 1.00 | 강한 SOLID 지시가 어떤 과제에서는 성능을 개선할 수 있다는 가능성을 먼저 열어 둬야 한다.
ko082 | SAME | ko073 | 1.00 | 반대로 네 조건이 모두 동일한 올바른 코드를 생성하거나, 설명의 어휘만 달라진다면 준공리화에 대한 행동적 증거는 얻지 못한 것이다.
ko083 | SAME | ko074 | 1.00 | 정당한 반대 증거를 받은 뒤 에이전트가 수정을 재고하는지도 별도로 평가할 수 있지만, 그 근거는 동일한 지시 우선순위와 소스 계약 아래 해석해야 한다.
ko084 | SAME | ko075 | 1.00 | ** 프롬프트와 결과 기록기, 제한적 원본 Go 실험은 준비돼 있지만 이를 실제 네 조건 에이전트 비교의 결과로 바꾸어 서술해서는 안 된다.
ko085 | SAME | ko076 | 1.00 | 설계 원칙을 조건부로 다루자는 제안은 이미 오래된 소프트웨어 공학의 직관 및 형식 이론과 연결된다.
ko086 | SAME | ko077 | 1.00 | 이 논문의 주장은 모든 기존 원칙을 폐기하거나, 요구·계약을 처음 발견했다는 것이 아니다.
ko087 | SAME | ko078 | 1.00 | AI가 코드를 생성하거나 검토하는 과정에서 **원칙이 어떤 관찰 가능한 결정 권한을 행사하는지**를 연구의 중심 변수로 삼자는 것이다.
ko088 | SAME | ko079 | 1.00 | 충분히 명시된 요구 아래서 엄격한 설계 지침이 더 안정적인 코드를 만들 수 있다.
ko089 | SAME | ko080 | 1.00 | 명시적 지시가 없는 모델은 SOLID를 전혀 적용하지 않을 수 있다.
ko090 | SAME | ko081 | 1.00 | 강한 지시는 코드에는 영향을 주지 않고 설명에만 남을 수 있다.
ko091 | SAME | ko082 | 1.00 | 이러한 결과를 허용하지 않는 연구라면 '준공리화'라는 표현 자체가 또 다른 검증되지 않은 교리가 되고 만다.
ko092 | SAME | ko083 | 1.00 | 소프트웨어 공학이 앞으로 필요로 하는 것은 원칙을 따르는 모델이나 원칙을 반대하는 모델이라는 이분법보다, **원칙의 적용을 정당화하는 요구·계약·반대 증거를 확인하고 그에 따라 결정을 바꿀 수 있는 모델**인지 묻는 연구다.
ko093 | SAME | ko084 | 1.00 | 이러한 문제를 정의하는 것이 Paper B의 기여다.
ko094 | SAME | ko085 | 1.00 | 특정 아키텍처의 비용 우위, 장기적 조직 성과와 새 설계 법칙의 형식 증명은 EvoNOMOS의 후속 연구에서 별도로 검증할 수 있다.
ko095 | SAME | ko086 | 1.00 | SOLID 같은 설계 원칙의 가치는 모든 수정에 적용되는 규칙이라는 데 있지 않을 수 있다.
ko096 | SAME | ko087 | 1.00 | 오히려 어떤 변화에서 유용하고 어떤 계약 앞에서 수정되어야 하는지를 설명할 수 있을 때 그 조언은 더 신뢰할 만해진다.
ko097 | SAME | ko088 | 1.00 | 우리는 AI 코딩 에이전트 시대에 설계 원칙이 설명에서 실제 선택으로 넘어가는 순간을 독립적인 실증 연구 대상으로 제안했다.
ko098 | SAME | ko089 | 1.00 | **원칙의 이름이 아니라, 그 이름에 부여된 결정 권한과 반대 증거 이후의 행동을 연구하자.
Summary ko: SAME 89, EDIT 0, NEW 9

### en (101 sentences)
en001 | SAME | en001 | 1.00 | Software design principles offer guidance about how a system might accommodate change.
en002 | SAME | en002 | 1.00 | In code review and AI-assisted development, however, a principle's name may acquire the force of a rule for accepting, rejecting, or reshaping an individual patch.
en003 | SAME | en003 | 1.00 | We propose **operational quasi-axiomatization** as a falsifiable research target: the possibility that conditional design advice comes to displace examination of actual requirements, protected client behavior, exceptions
en004 | SAME | en004 | 1.00 | This is neither a critique of mathematical axiomatization nor an empirical claim that current coding agents already treat SOLID as an unconditional truth.
en005 | SAME | en005 | 1.00 | Early accounts of the Open–Closed Principle made extensibility relative to anticipated change and stable client obligations.
en006 | SAME | en006 | 1.00 | We distinguish a structural-violation classification from the decision whether a particular repair is acceptable, illustrate that distinction with one explicitly constructed, fixed-patch contract example, and outline con
en007 | SAME | en007 | 1.00 | The empirical target is not the frequency of SOLID vocabulary but the authority that principle language exercises over source changes and the way decisions respond to counterevidence.
en008 | SAME | en008 | 1.00 | We offer a position and research agenda, not an estimate of agent behavior.
en009 | SAME | en009 | 1.00 | Suppose a reviewer states that a module violates the Open–Closed Principle (OCP).
en010 | SAME | en010 | 1.00 | The statement may correctly identify a design pattern.
en011 | SAME | en011 | 1.00 | It does not, by itself, establish which future change is required, which existing clients must continue working, which source files can be edited, or whether a different repair is available.
en012 | SAME | en012 | 1.00 | The same pattern may be a useful warning in one maintenance task and irrelevant to the acceptance of a particular patch in another.
en013 | SAME | en013 | 1.00 | Recognizing a principle-related structure and using that recognition to dispose of a concrete patch are distinct acts.
en014 | SAME | en014 | 1.00 | This distinction matters as software design advice enters coding-agent workflows.
en015 | SAME | en015 | 1.00 | A human may consider a principle among several reasons; an agent may receive it as an explicit project instruction or task-specific constraint.
en016 | SAME | en016 | 1.00 | The instruction can then influence the code it writes and the alternatives it rejects.
en017 | SAME | en017 | 1.00 | Such influence may be useful and fully authorized.
en018 | SAME | en018 | 1.00 | The empirical question is whether a principle's *name* is sometimes given decision authority beyond the scope and evidence that justify its use.
en019 | SAME | en019 | 1.00 | We call the possibility **operational quasi-axiomatization**.
en020 | SAME | en020 | 1.00 | We do not presume that it is prevalent, that a foundation model internally believes in SOLID, or that an original designer intended to state universal mathematical axioms.
en021 | SAME | en021 | 1.00 | We argue for a falsifiable research problem linking historical design advice, patch-specific authority, and the observable behavior of coding agents.
en022 | SAME | en022 | 1.00 | The histories of object orientation and SOLID should not be collapsed into one continuous five-rule doctrine.
en023 | SAME | en023 | 1.00 | Simula's class-based simulation, Smalltalk's message-oriented accounts, Parnas's information-hiding criterion, and Liskov and Wing's behavioral subtyping addressed different design questions.
en024 | SAME | en024 | 1.00 | Their differences matter because they associate software quality with distinct observations and changes rather than a single syntactic label. ; ; .
en025 | SAME | en025 | 1.00 | Meyer's account of open and closed modules joins extension with the stability of descriptions used by clients.
en026 | SAME | en026 | 1.00 | Martin's then makes strategic closure explicit.
en027 | SAME | en027 | 1.00 | A drawing routine may accommodate another kind of shape without revision while a request to change the ordering of shapes may require a different locus of modification.
en028 | SAME | en028 | 1.00 | Which change should be cheap is an engineering choice, not a universal property conferred by the OCP label.
en029 | SAME | en029 | 1.00 | It would mischaracterize Martin to claim that he formally established five unconditional design axioms.
en030 | SAME | en030 | 1.00 | /13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md); [Martin's strategic-closure example](.
en031 | SAME | en031 | 1.00 | /29_MARTIN_1996_STRATEGIC_CLOSURE.md).
en032 | SAME | en032 | 1.00 | Historical advice can remain useful in modern development without being beyond revision.
en033 | SAME | en033 | 1.00 | The question is which requirements and future changes justify its authority.
en034 | SAME | en034 | 1.00 | Three ideas must be separated.
en035 | SAME | en035 | 1.00 | **Formal axiomatization** specifies premises and inference rules, which can be legitimate and precise.
en036 | SAME | en036 | 1.00 | **Professional canonization** describes a historical process in which repeated advice becomes widely authoritative.
en037 | SAME | en037 | 1.00 | **Operational quasi-axiomatization** concerns a narrower, potentially observable event: the use of a design principle as a decisive constraint in an actual modification despite relevant evidence that its purported author
en038 | SAME | en038 | 1.00 | The latter is not established merely because an agent uses imperative language or follows an explicitly authorized instruction.
en039 | SAME | en039 | 1.00 | We call the narrower inference step the **principle-to-patch transport problem**.
en040 | SAME | en040 | 1.00 | A structural label (L(s)) for source (s) does not generally determine whether a patch (p) should be accepted.
en041 | SAME | en041 | 1.00 | Acceptance depends on a specified demand (D), existing client obligations (C), edit authority (A), and the particular candidate.
en042 | SAME | en042 | 1.00 | Symbolically, (mathrm{Accept}(pmid D,C,A)) cannot in general be recovered from (L(s)) alone.
en043 | SAME | en043 | 1.00 | This is an explanatory notation, not a newly proven undecidability theorem.
en044 | SAME | en044 | 1.00 | Requirements engineering, Design by Contract, contextual equivalence, and source-aware repair all provide relevant prior theory.
en045 | EDIT | en045 | 0.72 | Our proposed contribution is to turn the *operational authority* exercised by principle language into a direct research question for AI-assisted development.
en046 | NEW | en033 | 0.13 | The question is not confined to class-based code.
en047 | NEW | en008 | 0.09 | Go offers interface methods as well as function values and callback composition.
en048 | NEW | en027 | 0.14 | Adding a handler can leave an existing dispatcher unchanged in either idiom, while a change to a callback protocol or interface obligation may propagate through different caller sets.
en049 | NEW | en006 | 0.16 | We do not claim that Go is a purely functional language or that either construction is inherently cheaper; the comparison is a **conceptual illustration**, not a measured result.
en050 | NEW | en040 | 0.20 | Its relevance is that a class-oriented OCP label cannot, without the actual requirement and client obligations, determine whether a callback-based patch should be accepted. ; ; [bounded analysis](.
en051 | NEW | en045 | 0.29 | /55_PAPER_B_R13_PARADIGM_TRANSFER_AND_CALLBACK_NEGATIVE_CONTROL.md). , studies prompting LLMs to identify SOLID violations across languages.
en052 | SAME | en046 | 1.00 | Such classification is not itself a test of whether a particular patch should be accepted or rejected.
en053 | SAME | en047 | 1.00 | In our prior inspection of its OCP archive, 48 submitted code examples occurred across 768 stored response rows, with 24 distinguishable masked prompt scaffolds.
en054 | SAME | en048 | 1.00 | These are not 768 independent maintenance tasks.
en055 | SAME | en049 | 1.00 | Item-specific protected client contracts or change demands were not separately stated in the saved prompt templates; code-internal clues may nonetheless remain.
en056 | SAME | en050 | 1.00 | /18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md).
en057 | SAME | en051 | 1.00 | To expose the difference we constructed a small library-patch example.
en058 | SAME | en052 | 1.00 | A fixed proposed addition supports technical reports but omits errata and changes an older book prefix.
en059 | SAME | en053 | 1.00 | Varying whether errata are required and whether the older prefix is contractually protected changes whether that *same patch* is admissible under the authored specification.
en060 | SAME | en054 | 1.00 | The difference is in the requirements against which the patch is evaluated, not an observed industrial reviewer or coding agent.
en061 | SAME | en055 | 1.00 | /31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md).
en062 | SAME | en056 | 1.00 | This example does not make structural classifiers useless.
en063 | SAME | en057 | 1.00 | A classifier may correctly direct attention to code that deserves scrutiny.
en064 | SAME | en058 | 1.00 | Our point is that an individual maintenance decision also requires traceable grounds for the scope of the request, client protections, edit authority, and alternatives.
en065 | SAME | en059 | 1.00 | Repository instructions are a real delivery channel for coding agents, but their availability says nothing by itself about the contents of model pretraining.
en066 | SAME | en060 | 1.00 | For example, examine repository-level context files and coding-agent task performance; they do not directly measure SOLID-induced patch rejection or prove a training-origin mechanism.
en067 | SAME | en061 | 1.00 | Prompts, source context, model explanations, generated patches, tests, and final review decisions must be measured separately.
en068 | SAME | en062 | 1.00 | Our inherited compares NONE, HARD_SOLID, SCOPED_SOLID, and EVIDENCE_CONDITIONAL advice on the same pinned source, task, tests, rights and tool budget.
en069 | SAME | en063 | 1.00 | Outcomes would distinguish code correctness and preserved clients from the language used to justify the patch; they would also record revision or abstention after independently sourced contrary evidence.
en070 | SAME | en064 | 1.00 | A serious identification objection arises here.
en071 | SAME | en065 | 1.00 | An agent that follows HARD_SOLID may simply be obeying the experiment's instruction, rather than treating SOLID as an independent truth.
en072 | SAME | en066 | 1.00 | Even a bad patch may result from conflicts between instructions, weak source comprehension, or incomplete tests.
en073 | NEW | en037 | 0.18 | Where a legitimately higher-priority instruction demands a particular design, adherence may be proper policy compliance; counterevidence must be evaluated against a specified authority hierarchy before stubbornness is sc
en074 | SAME | en067 | 1.00 | We therefore propose examining tasks where principle-aligned design is valid, tasks where a mechanical refactoring would break a protected obligation, and cases where the available evidence does not warrant a disposition
en075 | SAME | en068 | 1.00 | A conforming hard-rule implementation may win in the first stratum; models may tie throughout; words may change without changes to source.
en076 | SAME | en069 | 1.00 | All of these are legitimate rival outcomes.
en077 | SAME | en070 | 1.00 | Subsequent factual rebuttals can test responsiveness, but must be interpreted under the actual instruction hierarchy rather than treated as direct access to internal beliefs.
en078 | SAME | en071 | 1.00 | [Identification analysis](.
en079 | SAME | en072 | 1.00 | /53_PAPER_B_R11_COMPLIANCE_VS_QUASI_AXIOM_IDENTIFICATION.md).
en080 | SAME | en073 | 1.00 | No independent four-arm coding-agent execution has yet been performed.
en081 | SAME | en074 | 1.00 | The proposed study can estimate certain **effects of present instructions** if implemented with valid randomization and evaluation.
en082 | SAME | en075 | 1.00 | It cannot, without further evidence, identify the causal influence of hidden pretraining examples or the long-run historical process of professional canonization.
en083 | SAME | en076 | 1.00 | Arguing that design advice should remain revisable is compatible with established software engineering theory; we do not claim to have invented contracts, exceptions, or contextual judgment.
en084 | SAME | en077 | 1.00 | Nor do we recommend discarding SOLID.
en085 | SAME | en078 | 1.00 | We instead ask that the authority principle language exercises in a coding workflow be an explicit empirical variable.
en086 | SAME | en079 | 1.00 | Its outcomes include justified adherence, unjustified insistence, evidence-responsive revision, ordinary instruction compliance, lexical repetition, and abstention when obligations are unknown.
en087 | SAME | en080 | 1.00 | This framing allows the hypothesis to fail.
en088 | SAME | en081 | 1.00 | Strict guidance might improve maintenance outcomes in some contexts.
en089 | SAME | en082 | 1.00 | Agents may generate equally good patches under all conditions.
en090 | SAME | en083 | 1.00 | A supposed principle effect may disappear once a source-aware classical planning baseline is given the same information.
en091 | SAME | en084 | 1.00 | Such results constrain the phenomenon rather than threaten the legitimacy of its investigation.
en092 | SAME | en085 | 1.00 | What matters is not whether a coding agent can recite a principle but whether its actual choices reflect the requirements, client contracts, and counterexamples that bear on the decision.
en093 | SAME | en086 | 1.00 | Source-level architectural reversal and maintenance cost can be investigated in separate EvoNOMOS studies; they need not be claimed by this position paper.
en094 | SAME | en087 | 1.00 | A design principle earns practical authority when its use can be justified for the changes and obligations at hand, not merely through repetition of its name.
en095 | SAME | en088 | 1.00 | We propose operational quasi-axiomatization as a falsifiable question about when AI-assisted software decisions elevate conditional advice into binding action.
en096 | SAME | en089 | 1.00 | The immediate research opportunity is to observe **what the principle changes in a patch, and what credible counterevidence changes in the agent's decision**.
en097 | NEW | en090 | 0.24 | This is the proposed object of study, not an already demonstrated fact. --- - v25 added a cross-paradigm illustration and explicitly conditioned the rebuttal test on instruction priority.
en098 | NEW | en033 | 0.09 | Both are conceptual/editorial changes, not new original-Go or AI experiments.
en099 | EDIT | en090 | 0.77 | Previous v24 is preserved. - The archival OCP counts, library reconstruction and original Go witnesses are prior EvoNOMOS work; none is an observed four-arm agent-effect estimate. - Exact bibliographic formatting, origin
en100 | SAME | en091 | 1.00 | The above text primarily paraphrases ideas and cites the recorded source chain. - F37's app-owned router negative control established equal capability for a bounded reserved-route wrapper; including its full details here
en101 | SAME | en092 | 1.00 | Keep in v22/v23 or supporting archive. - The earlier formal discussion of principle-to-patch inference has requirements-engineering precedents; do not claim first invention of that distinction. - A null result in the fut
Summary en: SAME 90, EDIT 2, NEW 9

## v26 · [Source](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/PAPER_B_BILINGUAL_POSITION_26_20261122.md)
### ko (91 sentences)
ko001 | NEW | ko001 | 0.08 | 소프트웨어 설계 원칙은 좋은 코드를 만드는 데 유용한 판단 기준이지만, 그 원칙이 언제까지 유효한지까지 자동으로 알려 주지는 않는다.
ko002 | NEW | ko001 | 0.06 | 특히 AI 코딩 에이전트가 SOLID나 디자인 패턴을 설명할 뿐 아니라 실제 코드의 수정 방향을 선택하는 상황에서는, 역사적으로 조건부였던 조언이 마치 지켜야 할 규칙처럼 작동할 가능성을 다시 검토할 필요가 있다.
ko003 | NEW | ko002 | 0.34 | 우리는 이를 **설계 원칙의 운영상 준공리화(operational quasi-axiomatization)**라는 연구 질문으로 제안한다.
ko004 | NEW | ko007 | 0.06 | 핵심은 AI가 SOLID를 얼마나 자주 언급하는지가 아니라, 그 원칙이 요구사항과 기존 호출자 계약을 고려한 실제 패치 판단에 어떤 권위를 행사하며, 반대 증거가 나타났을 때 판단이 수정되는가이다.
ko005 | NEW | ko004 | 0.17 | Meyer와 Martin의 개방–폐쇄 원칙 논의, SOLID 위반 분류 연구, 고정된 패치의 조건부 수용 사례를 통해 질문의 범위를 정한다.
ko006 | NEW | ko006 | 0.12 | 이어 코딩 에이전트 지시 조건, 유지보수 요구, 계약 증거 및 결정 수정 행동을 구별하는 후속 연구를 제안한다.
ko007 | NEW | ko073 | 0.09 | **우리는 준공리화가 이미 널리 발생한다고 주장하거나 새로운 보편 설계 법칙을 제시하지 않는다.
ko008 | NEW | ko093 | 0.06 | ** 목적은 기존 설계 원칙의 적용 범위와 AI 시대의 의사결정을 함께 연구할 수 있는, 반증 가능한 문제를 제안하는 것이다.
ko009 | NEW | ko010 | 0.05 | 어떤 프로그램을 확장해야 하는 개발자가 있다고 하자.
ko010 | NEW | ko008 | 0.06 | 새 기능을 추가할 때마다 기존 코드를 고치는 구조는 개방–폐쇄 원칙에 어긋난다고 배웠을 수 있다.
ko011 | NEW | ko046 | 0.04 | 개발자는 이를 바탕으로 인터페이스를 추가하거나 객체를 분리하는 선택을 한다.
ko012 | NEW | ko045 | 0.05 | 그런데 실제 요구는 기존 코드 몇 줄의 단순한 수정으로 해결되고, 도입한 추상화는 지금도 이후에도 사용되지 않는다면 어떨까?
ko013 | NEW | ko046 | 0.04 | 반대로 애초에 변동이 많은 기능을 인터페이스 뒤에 격리한 덕분에 반복 변경을 안전하게 처리한다면 어떨까?
ko014 | NEW | ko039 | 0.13 | **설계 원칙에 이름이 붙어 있다는 사실만으로 특정 수정안의 품질은 결정되지 않는다.
ko015 | NEW | ko097 | 0.09 | ** 이 긴장은 AI 코딩 에이전트를 만나 새로운 형태로 드러난다.
ko016 | NEW | ko061 | 0.07 | 사람이 원칙을 참조하는 것뿐 아니라, 도구에 원칙을 강한 지침으로 주입하고 그 도구가 코드와 검토 의견을 생성할 수 있기 때문이다.
ko017 | NEW | ko080 | 0.08 | 더 중요한 요구나 기존 계약과 충돌하면 다른 방법을 선택하는가?
ko018 | NEW | ko076 | 0.04 | 충돌이 있을 때 기존 판단을 정당하게 수정하는가?
ko019 | NEW | ko086 | 0.13 | 우리의 제안은 SOLID를 폐기하거나 다른 다섯 가지 원칙을 대신 만들자는 것이 아니다.
ko020 | NEW | ko098 | 0.10 | **원칙의 실제 결정 권한을 독립적으로 연구하자**는 것이다.
ko021 | NEW | ko011 | 0.06 | 이 질문은 올바른 원칙이 어떤 환경에서 유용한지, 다른 구조가 더 적합한 조건은 무엇인지에 관한 미래 연구로 이어질 수 있다.
ko022 | NEW | ko020 | 0.09 | 객체지향의 역사는 한 개의 만능 설계 표준이 탄생한 역사가 아니다.
ko023 | EDIT | ko021 | 0.56 | Simula의 클래스와 시뮬레이션, Smalltalk의 메시지, Parnas의 정보 은닉, Liskov와 Wing의 행동적 하위타입은 서로 다른 기술적 질문에 답했다.
ko024 | NEW | ko020 | 0.07 | 이 차이를 무시하고 객체지향과 SOLID를 하나의 동일한 명령 체계로 취급하면, 설계를 평가할 때 필요한 전제를 놓치기 쉽다. ; ; .
ko025 | NEW | ko023 | 0.26 | Meyer의 개방–폐쇄 설명은 확장성과 기존 이용자의 안정된 설명을 결부했다.
ko026 | NEW | ko004 | 0.12 | Martin의 은 어떤 변경을 예상하는지에 따라 닫혀 있어야 할 부분이 달라짐을 구체적인 도형 사례로 설명한다.
ko027 | NEW | ko025 | 0.05 | 새 도형의 도입과 출력 순서의 변경은 같은 종류의 수정이 아니다.
ko028 | NEW | ko026 | 0.08 | 이 역사적 기록을 통해 확인되는 것은 원저자가 모든 미래 변경에 관해 유일한 구조를 보장했다는 사실이 아니라, **어떤 변화에 대비할 것인지 선택해야 한다는 조건성**이다.
ko029 | EDIT | ko028 | 0.71 | /13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md).
ko030 | NEW | ko027 | 0.06 | 그렇다면 문제의 중심은 “원저자가 잘못된 공리를 주장했는가”가 아니다.
ko031 | NEW | ko001 | 0.05 | 특정 상황에 맞는 조언이 교육, 코드 검토, 저장소 지침, 에이전트 프롬프트를 거치는 동안 적용 조건이 생략될 수 있는가이다.
ko032 | NEW | ko017 | 0.19 | 이 가능성을 설명하는 용어로 우리는 *운영상의 준공리화*를 제안한다.
ko033 | NEW | ko035 | 0.12 | **형식적 공리화**는 수학적 전제 설정이고, **전문직적 정전화**는 사회·역사적 권위 형성이다.
ko034 | NEW | ko036 | 0.16 | 여기서 제안하는 **운영상의 준공리화**는 실제 수정 결정에서 원칙이 요구·계약·예외의 증거보다 우선하는지에 관한 행동적 가설이다.
ko035 | NEW | ko020 | 0.06 | 이 문제는 우선 SOLID **분류**와 패치 **판정**을 분리할 때 선명해진다.
ko036 | NEW | ko064 | 0.13 | *은 언어모델이 코드의 SOLID 위반을 식별할 수 있는지 조사했다.
ko037 | NEW | ko010 | 0.02 | 하지만 “구조에 위반이 있는가”와 “지금 이 패치를 병합할 것인가”는 별개 질문이다.
ko038 | NEW | ko040 | 0.05 | 후자에는 해결할 요구, 보호할 기존 호출자 동작, 허용된 수정 권한, 실제 후보와 대안이 필요하다.
ko039 | NEW | ko097 | 0.05 | 이는 요구공학과 계약 기반 설계의 기존 전통을 대체하는 발견이 아니라, **원칙 이름이 수정 결정에 전달되는 단계**를 별도의 AI 연구 대상으로 만들자는 제안이다.
ko040 | NEW | ko059 | 0.47 | 우리가 작성한 도서관 패치는 기술보고서를 추가하지만 정오표를 지원하지 않고, 기존 책 출력의 접두어를 바꾼다.
ko041 | NEW | ko060 | 0.15 | 정오표 지원이 필수인지, 기존 접두어의 보존이 계약에 포함되는지를 바꾸면 **같은 패치**에 대한 승인 결과가 달라진다.
ko042 | NEW | ko041 | 0.02 | 이 결과는 연구자가 정의한 요구와 계약에 대한 실행 가능성 검산이다.
ko043 | NEW | ko073 | 0.10 | 실제 에이전트가 SOLID 때문에 패치를 잘못 거절했다는 결과가 아니다.
ko044 | SAME | ko063 | 1.00 | /31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md).
ko045 | NEW | ko016 | 0.02 | 코드 언어와 패러다임도 문제의 범위를 드러낸다.
ko046 | NEW | ko047 | 0.05 | Go의 함수 값·콜백과 인터페이스를 통한 확장은 서로 다른 구현 선택이지만, 하나의 OCP 라벨이 어느 쪽의 특정 수정을 반드시 거절해야 한다고 자동 판정해 주지 않는다.
ko047 | NEW | ko049 | 0.09 | Go는 순수 함수형 언어가 아니며, 이 예시는 특정 패러다임의 성능 우위를 입증하려는 비교가 아니다. ; [별도 비교 메모](.
ko048 | SAME | ko051 | 1.00 | /55_PAPER_B_R13_PARADIGM_TRANSFER_AND_CALLBACK_NEGATIVE_CONTROL.md).
ko049 | NEW | ko058 | 0.05 | 이 질문을 구체적인 연구 의제로 만들기 위해 우리는 기존에 작성한 네 가지 지시 조건을 활용할 수 있다.
ko050 | NEW | ko045 | 0.06 | **NONE**은 추가적인 설계 조언을 주지 않는다.
ko051 | NEW | ko073 | 0.15 | **HARD_SOLID**는 원칙을 강하게 지시한다.
ko052 | NEW | ko071 | 0.08 | **SCOPED_SOLID**는 변경 범위에 맞춰 적용한다.
ko053 | NEW | ko071 | 0.17 | **EVIDENCE_CONDITIONAL**은 요구·계약·대안의 증거를 기준으로 판단한다.
ko054 | NEW | ko080 | 0.08 | 실제 실험에서는 모든 조건에 동일한 소스, 수정 과제, 기존 클라이언트 계약과 검사 환경을 제공해야 한다. .
ko055 | NEW | ko081 | 0.13 | 강한 지시가 정당한 리팩터링을 개선할 수 있다.
ko056 | NEW | ko011 | 0.05 | 네 조건의 패치가 완전히 같고 설명만 달라질 수 있다.
ko057 | NEW | ko014 | 0.05 | 기존 테스트와 요구사항이 설계 지시의 효과를 압도할 수도 있다.
ko058 | NEW | ko014 | 0.06 | 엄격한 지시가 부적절한 추상화를 유도할 수도 있다.
ko059 | NEW | ko077 | 0.08 | **그 어느 것도 관찰하기 전에 승자로 정해서는 안 된다.
ko060 | NEW | ko039 | 0.02 | ** 여기에 가장 중요한 식별 문제가 있다.
ko061 | NEW | ko073 | 0.18 | 에이전트가 HARD_SOLID를 따르는 이유는 SOLID를 무오류의 공리로 받아들여서가 아니라 **방금 받은 유효한 지시를 따르기 때문**일 수 있다.
ko062 | NEW | ko037 | 0.11 | 따라서 강한 지시의 채택률을 곧바로 준공리화로 해석해서는 안 된다.
ko063 | NEW | ko083 | 0.11 | 계약과 소스에서 확인한 반대 증거가 주어졌을 때 에이전트가 어떻게 대응하는지, 그 증거가 실제 지시 우선순위에서 얼마나 구속력이 있는지, 대안의 적법성을 독립적으로 검증할 수 있는지를 함께 조사해야 한다.
ko064 | NEW | ko089 | 0.07 | 설명에서 SOLID를 더 많이 언급하는 현상과 소스 패치가 달라지는 현상도 구별해야 한다.
ko065 | NEW | ko084 | 0.11 | 실제 네 조건 코딩 에이전트 비교는 **아직 실행되지 않았다**.
ko066 | NEW | ko098 | 0.04 | 이 논문이 제시하는 것은 측정값이 아니라, 그 측정으로 무엇을 구별할 수 있고 구별할 수 없는지에 관한 연구 의제다.
ko067 | NEW | ko044 | 0.02 | **첫째, 원칙의 권위가 문헌과 지침에서 어떻게 표현되는가?
ko068 | NEW | ko030 | 0.05 | ** 역사적 원전과 현대 저장소 지침을 비교해 조건, 예외, 강제 표현의 유무를 분류할 수 있다.
ko069 | NEW | ko070 | 0.03 | 서로 다른 시대의 문헌 표현을 비교하는 것만으로 AI가 권위를 강화했다는 인과 결론을 낼 수는 없다.
ko070 | NEW | ko044 | 0.05 | **둘째, 원칙의 언어가 실제 패치를 바꾸는가?
ko071 | NEW | ko032 | 0.05 | ** 동일한 변경 요구에 대한 서로 다른 지시 조건의 패치를 비교하고, 올바른 수정을 도왔는지, 불필요한 추상화를 만들었는지, 기존 클라이언트 계약을 보존했는지 측정할 수 있다.
ko072 | NEW | ko066 | 0.07 | 와 는 각기 관련된 선행 출발점이지만, 이 질문의 특정 조건부 패치 판정을 그대로 해결하지는 않는다.
ko073 | NEW | ko098 | 0.10 | **셋째, 반대 증거 이후 판단을 바꾸는가?
ko074 | NEW | ko011 | 0.06 | ** 신뢰할 수 있는 계약과 기존 호출자 테스트를 제시한 뒤 판단 변경·보류·지시 충돌 보고를 서로 다르게 평가할 수 있다.
ko075 | NEW | ko073 | 0.06 | 처럼 개발자 지침과 바람직한 에이전트 행동을 분류한 연구가 이미 존재하므로, *우리가 최초로 에이전트 규칙을 연구한다*는 주장은 성립하지 않는다.
ko076 | NEW | ko095 | 0.06 | 우리의 초점은 **설계 원칙의 권위가 개별 수정 판단에서 어떻게 작동하는가**에 있다.
ko077 | NEW | ko055 | 0.04 | **넷째, 이러한 원칙의 적용이 후속 유지보수 비용에 어떤 영향을 미치는가?
ko078 | NEW | ko031 | 0.05 | ** 수정 파일 수, 전체 에이전트 토큰 사용량, 오류, 시간, 에너지 등을 별도 변수로 측정할 수 있다.
ko079 | NEW | ko077 | 0.06 | 원칙을 지켜 파일 수정이 줄었다는 사실만으로 토큰과 에너지가 줄었다고 추론해서는 안 된다.
ko080 | NEW | ko067 | 0.03 | 특히 AI 개발의 총비용은 초기 추상화 비용과 반복된 변경 요구를 함께 고려해야 한다.
ko081 | NEW | ko093 | 0.12 | 이 문제는 Paper B의 성과가 아니라 후속 연구를 위한 열린 질문이다.
ko082 | NEW | ko006 | 0.05 | 후속 실험에서 대다수 과제에 원칙에 따른 부당한 거절이 발견되지 않거나, 원칙 지시가 실제 코드가 아니라 설명의 어휘에만 영향을 주거나, 강한 원칙 지시가 검증된 계약 보존을 일관되게 개선할 수도 있다.
ko083 | NEW | ko010 | 0.08 | 어느 결과든 연구자가 공개한 가설의 범위를 수정해야 한다.
ko084 | NEW | ko042 | 0.03 | 기존 요구공학이나 강한 소스 인지 기준선이 동일한 현상을 충분히 설명할 수 있다면 새로운 기제를 발견했다고 주장할 수 없다.
ko085 | NEW | ko064 | 0.09 | 따라서 이 논문은 SOLID의 폐기 선언도, 운영상 준공리화의 존재 증명도 아니다.
ko086 | NEW | ko010 | 0.05 | **코드를 검사하는 도구가 원칙의 이름을 아는 것과, 언제 그 원칙을 수정 결정에 적용해야 하는지를 아는 것은 같은 능력인가?
ko087 | NEW | ko087 | 0.04 | ** 이 차이를 역사·코드·계약·에이전트 행동의 독립된 증거로 조사하자는 것이다.
ko088 | NEW | ko001 | 0.10 | 지난 수십 년간의 소프트웨어 설계 원칙은 변화에 대응하기 위한 언어를 제공했다.
ko089 | NEW | ko006 | 0.03 | 이제 그 언어 자체가 AI 개발 도구의 판단을 어떻게 구속하는지 시험할 이유가 생겼다.
ko090 | NEW | ko002 | 0.19 | 우리는 **운영상의 준공리화**를 특정 버그나 새 수학 법칙이 아니라, 설계 조언이 실제 수정안을 결정하는 데 행사하는 권위를 분석하기 위한 반증 가능한 연구 대상으로 제안한다.
ko091 | NEW | ko016 | 0.06 | 이 질문을 함께 검증하는 연구자들이 늘어난다면, 그 결과가 원칙의 정당성을 뒷받침하든 그 적용 범위를 좁히든 소프트웨어 공학에 유익할 것이다. ---
Summary ko: SAME 2, EDIT 2, NEW 87

### en (81 sentences)
en001 | NEW | en001 | 0.18 | Software design principles help developers reason about change, but they do not by themselves specify the circumstances under which their advice should be binding.
en002 | NEW | en002 | 0.20 | As AI coding agents move from describing designs to selecting and reviewing actual patches, historically conditional guidance may acquire the force of a seemingly unquestionable rule.
en003 | NEW | en095 | 0.35 | We propose **operational quasi-axiomatization** as a falsifiable research question: when, if ever, does a named design principle displace task requirements, protected client contracts, or relevant counterevidence in AI-m
en004 | NEW | en004 | 0.15 | This is not a claim that contemporary agents already exhibit such behavior or that a superior universal design law has been found.
en005 | NEW | en006 | 0.23 | We distinguish structural labels from patch dispositions, ground the question in earlier accounts of strategic closure and bounded contract examples, and propose a research agenda spanning historical documents, coding-ag
en006 | NEW | en045 | 0.20 | The intended contribution is to invite empirical investigation of the authority software design principles exercise in actual engineering decisions, not to report an already measured effect.
en007 | NEW | en019 | 0.12 | Suppose a developer is asked to add a capability to a mature application.
en008 | NEW | en005 | 0.14 | A familiar rule of thumb says that software should be open to extension while remaining closed to modification.
en009 | NEW | en002 | 0.11 | The developer may add an interface or split a class to make the new capability fit that principle.
en010 | NEW | en064 | 0.14 | In one project, the abstraction protects a frequently changing boundary and prevents regressions.
en011 | NEW | en033 | 0.19 | In another, the requirement could have been met by a small authorized change and the abstraction is never used again.
en012 | NEW | en064 | 0.14 | The mere naming of a principle does not decide which edit is better for the actual maintenance demand.
en013 | NEW | en014 | 0.18 | This ambiguity takes on a new form when design advice is supplied directly to coding agents.
en014 | NEW | en016 | 0.16 | An agent may not merely repeat the advice in prose; it may select files, construct interfaces, generate patches or reject alternatives.
en015 | NEW | en017 | 0.14 | Those actions may be useful or fully justified by a local project policy.
en016 | NEW | en045 | 0.23 | The research question is narrower: **when does the language of a historically conditional principle receive authority that exceeds its evidential or contractual scope?
en017 | NEW | en019 | 0.45 | ** We propose to study this possibility under the name *operational quasi-axiomatization*.
en018 | NEW | en020 | 0.14 | The point is not to replace SOLID with another mnemonic, to diagnose universal irrationality in current models or to declare an established design style obsolete.
en019 | NEW | en021 | 0.14 | It is to separate the act of recognizing design advice from the authority that advice actually exercises over a patch.
en020 | NEW | en022 | 0.32 | There is no reason to treat object orientation as a single continuous five-principle doctrine.
en021 | EDIT | en023 | 0.62 | Simula, Smalltalk, Parnas's information-hiding criterion and Liskov–Wing behavioral subtyping addressed materially different design questions. ; ; .
en022 | NEW | en005 | 0.23 | Meyer's open–closed account associates extensibility with descriptions on which existing clients may rely. explicitly emphasizes *strategic closure*: adding a new shape and changing the order in which shapes are drawn ar
en023 | NEW | en029 | 0.10 | A design optimized for one need not be equally suitable for the other.
en024 | NEW | en036 | 0.16 | These historical sources do not support a caricature in which the original authors mathematically asserted five unconditional axioms.
en025 | EDIT | en030 | 0.53 | /13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md).
en026 | NEW | en033 | 0.13 | The question is therefore not whether the first authors mistakenly derived immutable axioms.
en027 | NEW | en006 | 0.15 | It is whether advice that originated with identifiable conditions can lose those conditions as it passes through instruction files, code-review rubrics and agent prompts.
en028 | NEW | en019 | 0.30 | **Mathematical axiomatization**, **professional canonization** and **operational quasi-axiomatization** name different objects.
en029 | NEW | en037 | 0.14 | We use the last term only for a hypothesized observable decision process, not for claims about what a model internally believes or has encountered in training.
en030 | NEW | en051 | 0.20 | A structural label and a patch disposition require different evidence. addresses whether LLM prompts can detect SOLID violations across languages.
en031 | NEW | en052 | 0.24 | Detecting a pattern does not independently establish that a particular edit should be approved or rejected.
en032 | NEW | en064 | 0.26 | That decision also calls for the requested change, existing client commitments, authorized edits and feasible alternatives.
en033 | NEW | en044 | 0.28 | Requirements engineering and Design by Contract already study these obligations.
en034 | NEW | en045 | 0.30 | Our proposed target is the narrower **transition of design-principle language into operative patch authority** in AI development.
en035 | NEW | en058 | 0.29 | We illustrate the distinction with a bounded, author-constructed library modification: the same patch adds technical-report handling, does not handle errata, and changes an older book prefix.
en036 | NEW | en003 | 0.20 | When the stipulated requirements and protected old-client behavior change, the patch's acceptability changes.
en037 | NEW | en060 | 0.20 | The example is a witness about the logical insufficiency of a structural label, not evidence that an industrial reviewer or coding agent has rejected a real patch because of SOLID.
en038 | SAME | en061 | 1.00 | /31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md).
en039 | NEW | en046 | 0.17 | The phenomenon does not presuppose a class-based implementation.
en040 | NEW | en047 | 0.37 | In Go, methods and interfaces can coexist with function-valued callbacks.
en041 | NEW | en049 | 0.20 | Neither the use of classes nor the use of callbacks determines whether an actual extension meets its obligations; Go is not a purely functional language.
en042 | NEW | en049 | 0.10 | We do not claim that one paradigm has a general cost advantage. .
en043 | NEW | en068 | 0.45 | An earlier prospective study design compares four advice conditions: **NONE**, **HARD_SOLID**, **SCOPED_SOLID** and **EVIDENCE_CONDITIONAL**, under the same pinned source, client contracts, tasks, evaluator and tool budg
en044 | NEW | en080 | 0.23 | The design is prospective; no independent four-arm agent trial has been completed.
en045 | NEW | en076 | 0.11 | The possible outcomes are not limited to one favored theory.
en046 | NEW | en088 | 0.16 | Strict advice may improve correct repairs.
en047 | NEW | en089 | 0.16 | All conditions may yield identical code while explanations differ.
en048 | NEW | en033 | 0.15 | Tests and explicit requirements may dominate prompt style.
en049 | NEW | en006 | 0.10 | Strict design language may encourage an unnecessary abstraction or an unacceptable edit.
en050 | NEW | en100 | 0.11 | A useful experiment has to preserve all of these possibilities, including null effects and reversals.
en051 | NEW | en079 | 0.18 | Most importantly, compliance with an explicit HARD_SOLID instruction is not direct evidence of quasi-axiomatization.
en052 | NEW | en038 | 0.17 | An agent may be correctly following authorized policy.
en053 | NEW | en077 | 0.22 | A failure to revise after receiving contrary evidence likewise needs interpretation under the actual instruction hierarchy, authenticated source contract and available legal alternatives.
en054 | NEW | en081 | 0.23 | Even a randomized wording experiment can identify *effects of present instructions* without identifying either internal belief or pretraining origin.
en055 | NEW | en007 | 0.19 | The target is observable, source-grounded patch disposition and evidence-responsive revision, not the number of times an agent writes “SOLID.”
en056 | NEW | en078 | 0.43 | [Identification critique](.
en057 | SAME | en079 | 1.00 | /53_PAPER_B_R11_COMPLIANCE_VS_QUASI_AXIOM_IDENTIFICATION.md).
en058 | NEW | en003 | 0.17 | **Historical and documentary inquiry:** Under what conditions are exceptions and scopes preserved or omitted when design advice enters teaching materials, project rules and agent prompts?
en059 | NEW | en027 | 0.10 | Document shifts without inferring that AI caused them from a time trend alone.
en060 | NEW | en021 | 0.15 | **Agent behavior and patch adjudication:** Does advice wording change actual source repairs and contract preservation beyond explanatory vocabulary?
en061 | NEW | en088 | 0.11 | Compare fixed tasks and independent source-aware alternatives, including cases in which strict guidance is legitimately helpful.
en062 | NEW | en092 | 0.16 | **Revision under counterevidence:** When given authenticated client requirements and failing compatibility cases, do agents change their decisions, abstain or flag instruction conflicts?
en063 | NEW | en097 | 0.12 | What role does legitimate instruction priority play?
en064 | NEW | en096 | 0.16 | The already studies human-desired agent rules; our narrower interest is the use of **named design principles to dispose of particular code changes**.
en065 | NEW | en064 | 0.16 | **Downstream software and resource cost:** Across actual sequences of maintenance requests, do principles or alternative architectures alter patch sizes, repeated source-reading, token counts, regressions or energy cost?
en066 | NEW | en066 | 0.13 | Initial abstraction cost and repeated repair cost must be measured together; fewer edited files does not prove lower token or energy use.
en067 | NEW | en081 | 0.15 | This is a separate proposed study, not a present result.
en068 | NEW | en054 | 0.18 | These projects can be pursued independently.
en069 | NEW | en004 | 0.18 | A historical researcher need not first build a Go agent benchmark, and an empirical coding-agent researcher need not discover a new general mathematical law.
en070 | NEW | en091 | 0.09 | Their results can eventually inform one another.
en071 | NEW | en096 | 0.17 | If source-comparable agents normally revise unjustified principle-based choices after credible evidence, the proposed failure mode may be rare or absent in those settings.
en072 | NEW | en059 | 0.14 | If strict instruction only changes vocabulary or consistently improves contract correctness, the purported authority problem lacks the expected support there.
en073 | NEW | en100 | 0.17 | If established requirements traceability and source-aware conventional baselines fully explain the observed behavior, no novel causal mechanism is identified.
en074 | NEW | en019 | 0.15 | Each outcome would refine the research program, and none can be erased by renaming failure as a new kind of quasi-axiomatization.
en075 | NEW | en052 | 0.18 | Our invitation is deliberately modest: **does knowing a design principle entail knowing when it should govern a particular patch?
en076 | NEW | en021 | 0.15 | ** We propose studying the distance between those two abilities across historical evidence, real source tasks and controlled coding-agent behavior.
en077 | NEW | en001 | 0.25 | Software design principles have supplied a language for handling change.
en078 | NEW | en045 | 0.15 | The emergence of agents that can turn that language into concrete edits makes its operative authority worth studying in its own right.
en079 | EDIT | en095 | 0.54 | We propose operational quasi-axiomatization as a falsifiable question about when revisable advice becomes binding in AI-assisted engineering.
en080 | NEW | en076 | 0.11 | Researchers may find that the effect is substantial, negligible, legitimately beneficial or already explained by existing theories.
en081 | NEW | en099 | 0.15 | The contribution of this paper is to define that shared question and invite the evidence required to answer it. --- - Historical early-origin conversations establish project provenance, not global scholarly precedence. -
Summary en: SAME 2, EDIT 3, NEW 76

## v27 · [Source](https://github.com/WhoSia/EvoNOMOS/blob/research/law-r1-p44-r3-stateful-alias-court/active/g8-law-r1-p44/structural_law_return/prospective_cohort_20261111/paper_b/PAPER_B_BILINGUAL_POSITION_27_20261123.md)
### ko (94 sentences)
ko001 | NEW | ko086 | 0.17 | 설계 원칙을 이해하는 것과 그 원칙을 실제 소프트웨어 수정에 적용할 근거를 아는 것은 같은 능력일까?
ko002 | NEW | ko052 | 0.07 | 개방–폐쇄 원칙이나 SOLID는 변경에 대처하는 방법을 설명하지만, 어떤 변화가 예상되는지와 기존 사용자에게 무엇을 보존해야 하는지는 프로그램마다 다르다.
ko003 | NEW | ko002 | 0.10 | AI 코딩 에이전트가 이러한 조언을 읽고 코드 수정과 검토 판단까지 수행하는 상황에서, **조건부 설계 원칙이 적용 범위의 검토 없이 실질적인 승인·거절 규칙으로 사용되는가**라는 질문을 새롭게 연구할 필요가 있다.
ko004 | EDIT | ko003 | 0.55 | 우리는 이를 *운영상의 준공리화(operational quasi-axiomatization)*라는 반증 가능한 연구 대상으로 제안한다.
ko005 | NEW | ko005 | 0.11 | Martin의 서로 다른 도형 변경 요구, SOLID 위반 분류에 관한 저장 자료, 요구와 기존 계약에 따라 같은 수정안의 판정이 달라지는 연구자 작성 사례로 이 질문의 경계를 설명한다.
ko006 | NEW | ko007 | 0.09 | 이 자료는 에이전트의 준공리화 발생률이나 원인을 측정하지 않는다.
ko007 | NEW | ko006 | 0.11 | 대신 역사적 지침의 조건성을 조사하고, 동일한 소스·요구·계약 아래 네 가지 설계 지시를 비교하며, 신뢰할 수 있는 반대 증거에 대한 패치 판단의 수정을 검증하는 후속 연구를 제안한다.
ko008 | NEW | ko019 | 0.07 | 목적은 SOLID가 틀렸거나 더 우월한 설계 법칙을 발견했다고 선언하는 것이 아니라, **원칙의 이름이 실제 코드 결정에 행사하는 권위를 연구자들이 공동으로 측정할 수 있게 하는 것**이다.
ko009 | NEW | ko026 | 0.05 | Robert Martin이 1996년에 설명한 한 도형 프로그램은 객체가 자신의 그리기 동작을 제공하도록 하여 새 도형을 추가할 수 있게 했다.
ko010 | NEW | ko065 | 0.03 | 목록의 순서대로 그리는 기존 함수는 새 도형의 추가에는 적합했지만 이 요구를 자동으로 만족하지 않았다.
ko011 | NEW | ko038 | 0.02 | **원을 먼저 놓는 일이 함수의 책임인가, 호출자의 책임인가?
ko012 | NEW | ko069 | 0.11 | ** 기존 코드의 모습을 확인하는 것만으로 그 질문에 답할 수는 없다.
ko013 | NEW | ko026 | 0.07 | 이때의 개방–폐쇄 원칙은 어떤 변경을 예상하고 어떤 동작을 보존할지 선택하도록 돕는 조언이지, 어떤 코드에도 문맥 없이 적용되는 합격 판정이 아니다. ; .
ko014 | NEW | ko015 | 0.12 | 오늘날 이 구별은 코드 리뷰뿐 아니라 AI 코딩 에이전트의 수정 과정에서도 중요하다.
ko015 | NEW | ko086 | 0.09 | 원칙의 이름이 검토 설명에 등장하는 것과, 그 원칙을 이유로 특정 구현을 채택하거나 대안을 거절하는 것은 다르다.
ko016 | NEW | ko004 | 0.05 | 실제 코드의 요구와 오래된 호출자 계약을 아는 개발자는 원칙이 유용한 경우를 찾아낼 수 있다.
ko017 | NEW | ko058 | 0.05 | 반면 원칙을 기계적으로 적용하면 필요 없는 추상화를 만들거나 허용되는 수정안을 배제할 가능성도 있다.
ko018 | NEW | ko007 | 0.07 | **우리는 그런 일이 널리 벌어지고 있다고 단정하지 않는다.
ko019 | NEW | ko084 | 0.06 | ** 어떤 조건에서 실제로 벌어지는지, 혹은 기존 지시 준수와 요구공학으로 충분히 설명되는지 묻는다.
ko020 | NEW | ko003 | 0.17 | 이 글의 중심 제안은 설계 원칙의 *운영상의 권위(operational authority)*를 연구 대상으로 삼자는 것이다.
ko021 | NEW | ko070 | 0.05 | 원칙이 사용됐는지, 패치를 바꾸었는지, 그 결과가 문서화된 계약에 적합했는지, 반대 증거에 따라 판단이 바뀌었는지를 구별한다.
ko022 | NEW | ko016 | 0.07 | 이 질문이 AI 시대에 적절한 이유는 에이전트가 더 이상 설계 원칙을 서술하는 데 그치지 않고 실제 소스 코드에 적용할 수 있기 때문이다.
ko023 | NEW | ko058 | 0.04 | 그러나 이 능력의 존재가 곧 부적절한 권위 행사에 관한 실증 결과인 것은 아니다.
ko024 | NEW | ko024 | 0.08 | 객체지향 프로그래밍의 발전이 하나의 SOLID 규칙집에서 출발한 것은 아니다.
ko025 | EDIT | ko023 | 0.60 | Simula의 모델링과 클래스, Smalltalk의 메시지, Parnas의 정보 은닉, Liskov와 Wing의 행동적 하위타입은 서로 다른 설계 문제를 다뤘다.
ko026 | NEW | ko024 | 0.05 | 디자인 패턴에 관한 GoF의 고전적 작업과 SOLID 역시 서로 연관된 설계 지식을 제공하지만 동일한 개념이나 동일한 연대의 규범은 아니다.
ko027 | NEW | ko024 | 0.03 | 역사를 하나의 원칙 체계로 환원하기보다, 당시의 저자들이 어떤 요구를 해결하려 했는지 살펴야 한다. ; ; .
ko028 | NEW | ko025 | 0.16 | Bertrand Meyer의 개방–폐쇄 설명에는 기존 클라이언트가 의존하는 안정된 설명과 새 종류를 수용할 확장 지점이라는 서로 다른 요구가 함께 등장한다.
ko029 | NEW | ko026 | 0.05 | Martin은 1996년 논의에서 어떤 변화에 대비해 닫힘을 확보할지 선택하는 *strategic closure*를 강조한다.
ko030 | NEW | ko073 | 0.02 | 도형의 종류가 늘어나는 요구와 그리기 순서가 바뀌는 요구가 다른 판단을 요구하는 이유다.
ko031 | NEW | ko028 | 0.02 | 이 역사적 검토는 당시 저자들이 수학적으로 무조건적인 공리를 선포했다고 비판하는 근거가 아니라, 오히려 기존 원칙에도 적용할 조건이 포함돼 있음을 확인하게 해 준다.
ko032 | SAME | ko029 | 1.00 | /13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md).
ko033 | NEW | ko031 | 0.07 | 그런데 실무와 도구에서 원칙이 인용될 때는 원칙을 정당화한 조건이 생략될 수도 있다.
ko034 | NEW | ko033 | 0.14 | 이를 직접 검증할 수 있도록 우리는 **형식적 공리화**(명시적인 수학적 전제와 추론), **전문직적 정전화**(교육·실무에서 형성되는 역사적 권위), **운영상의 준공리화**(원칙의 이름이나 지침이 특정 수정 결정을 구속하는 행동)를 구별한다.
ko035 | NEW | ko043 | 0.09 | 마지막 개념은 첫 두 현상의 자동적인 결과가 아니다.
ko036 | NEW | ko088 | 0.03 | AI 모델의 내부 신념이나 특정 사전학습 자료를 추정하기 위한 이름도 아니다.
ko037 | NEW | ko090 | 0.04 | 소스의 구조적 특징을 보고 OCP 위반이라고 분류하는 것과, 실제 수정안의 승인 여부를 정하는 것은 요구하는 증거가 다르다.
ko038 | NEW | ko036 | 0.26 | 은 언어모델의 SOLID 위반 분류를 평가했다.
ko039 | NEW | ko062 | 0.10 | 이 연구가 코드 수정의 승인에 필요한 프로젝트별 요구·보호 계약까지 실험했다고 해석해서는 안 된다.
ko040 | NEW | ko046 | 0.02 | 우리가 보유한 OCP 저장 아카이브의 과거 독립 감사에는 **고유 제출 코드 48개, 저장 응답 768행, 서로 다른 마스킹된 프롬프트 틀 24개**가 기록되어 있다.
ko041 | NEW | ko006 | 0.05 | 여기서 768은 독립적인 유지보수 요구의 개수가 아니며, 일부 코드 내부에는 설명 주석도 존재했다. .
ko042 | NEW | ko009 | 0.06 | 이 둘의 차이를 명료하게 보여 주기 위해 이전 판본에서 작은 도서관 프로그램을 직접 구성했다.
ko043 | NEW | ko040 | 0.37 | 후보 수정안은 기술보고서를 처리하지만 정오표는 지원하지 않고, 기존 책 출력의 접두어를 에서 으로 바꾼다.
ko044 | NEW | ko090 | 0.02 | 소스와 수정안을 고정하고, 실제로 요구하는 기능과 보호할 계약만 바꿔 다음과 같이 판정한다.
ko045 | NEW | ko042 | 0.08 | 첫 행의 승인은 **연구자가 그 사례에 한정해 정한 요구·계약에 따른 승인**이다.
ko046 | NEW | ko043 | 0.08 | 실제 사용자가 기존 접두어를 기대하지 않았다고 관찰한 결과가 아니다.
ko047 | NEW | ko041 | 0.08 | 정오표 지원이 필수라면 접두어 보호 여부와 관계없이 거절할 수 있고, 기술보고서만 필요할 때 접두어 계약이 미공개라면 판정을 **보류**해야 한다.
ko048 | NEW | ko055 | 0.03 | 보호받는 의무가 하나 더 밝혀지면 기존 승인도 바뀔 수 있다.
ko049 | SAME | ko044 | 1.00 | /31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md); ; .
ko050 | NEW | ko044 | 0.09 | 이 사례는 요구공학과 Design by Contract가 오래전부터 다루어 온 문제를 보여 준다.
ko051 | NEW | ko007 | 0.15 | 우리는 계약을 처음 발견하거나 이를 새로운 정리로 증명했다고 주장하지 않는다.
ko052 | NEW | ko090 | 0.07 | 이 글에서 새로운 연구 대상으로 제안하는 것은 **기존 원칙을 인용하는 AI 에이전트가 이런 근거의 차이를 실제 수정 판단에 얼마나 반영하는지**다.
ko053 | NEW | ko007 | 0.05 | 부적절한 전이가 보편적으로 발생한다고 가정하지 않고, 발생한다면 어떤 요구와 지시 환경에서 나타나는지 검증하려는 것이다.
ko054 | NEW | ko085 | 0.04 | 원칙을 언급하는 문장은 위험 신호도 성공 지표도 아니다.
ko055 | NEW | ko073 | 0.10 | 원칙이 실제로 어느 판단을 바꾸었는지 알아야 한다.
ko056 | NEW | ko017 | 0.04 | 그 행동이 기존 계약을 어겼더라도 원인은 여러 가지일 수 있다.
ko057 | NEW | ko043 | 0.05 | 에이전트가 코드를 잘못 읽었거나, 사용자 지시와 프로젝트의 원칙이 충돌했거나, 불완전한 테스트가 오류를 발견하지 못했을 수 있다.
ko058 | NEW | ko061 | 0.12 | 특히 **강한 SOLID 지시를 따르는 것은 합당한 명시적 지시 준수일 수 있다.
ko059 | NEW | ko079 | 0.10 | ** 에이전트가 지시를 따른다는 사실만으로 독립적이고 무조건적인 SOLID 신념을 가졌다고 추론할 수 없다.
ko060 | NEW | ko063 | 0.06 | 우리가 제안하는 후속 관찰에서는 원칙의 적용 근거가 불충분한데도 적법한 대안이 배제됐는지, 반대 근거의 출처와 우선순위는 확정돼 있는지, 추가 근거를 받은 뒤 에이전트가 결정을 수정하거나 정당하게 기권할 수 있는지를 각각 따져야 한다.
ko061 | NEW | ko003 | 0.14 | /53_PAPER_B_R11_COMPLIANCE_VS_QUASI_AXIOM_IDENTIFICATION.md).
ko062 | NEW | ko039 | 0.05 | 이것은 하나의 새로운 진리 판정 시스템을 곧바로 구현하자는 제안이 아니다.
ko063 | NEW | ko063 | 0.05 | 구조적 위반 *분류*, 특정 패치의 *계약 적합성*, 검토자가 근거를 *제시할 수 있는지*, 반대 증거 뒤 *행동을 수정하는지*는 서로 다른 결과 변수다.
ko064 | NEW | ko036 | 0.08 | 모두 동일한 기준으로 점수를 매겨 하나의 SOLID 준수율로 합칠 이유도 없다.
ko065 | NEW | ko084 | 0.06 | 기존의 소스 인지 요구사항 추적이 판단을 충분히 설명한다면, 더 고유한 '준공리화 기제'가 있다는 주장은 철회하거나 좁혀야 한다.
ko066 | NEW | ko019 | 0.05 | **역사·문헌 연구:** SOLID를 설명하는 원전, 시대별 교육 자료, 저장소 지침에서 원칙이 어떤 조건과 예외와 함께 제시되는지 확인한다.
ko067 | NEW | ko068 | 0.07 | 표본 추출 시기와 문서 유형을 고정하고, 단순한 강제 표현의 증가가 과연 적용 범위의 삭제를 동반하는지 조사할 수 있다.
ko068 | NEW | ko043 | 0.04 | 아무런 변화가 없거나 문서 유형만 다르다는 결과도 가능하다.
ko069 | NEW | ko079 | 0.17 | 문헌의 변화만으로 AI가 그 변화를 일으켰다고 추론해서는 안 된다.
ko070 | NEW | ko053 | 0.14 | **실제 패치에 대한 지시 효과:** 소스 버전, 요구, 오래된 호출자 계약, 허용된 수정 범위, 기능 검사를 고정하고, 이전에 제안된 네 가지 지시 조건 **NONE / HARD_SOLID / SCOPED_SOLID / EVIDENCE_CONDITIONAL**을 새 에이전트 문맥에 배정할 수 있다.
ko071 | NEW | ko083 | 0.03 | 원칙에 적합한 설계가 실제로 도움이 되는 과제와 기계적 적용이 불리한 과제를 모두 포함해야 한다.
ko072 | NEW | ko017 | 0.02 | 결과는 코드의 정확성·보존 계약·수정 범위와 설명 어휘를 구분한다.
ko073 | NEW | ko051 | 0.13 | 네 조건 모두 같은 적법한 패치를 만들거나 HARD_SOLID가 더 좋은 수정을 만든다면 그대로 보고한다.
ko074 | NEW | ko022 | 0.03 | 이 비교의 인과 대상은 **주어진 지시 내용의 효과**이지 모델이 사전학습 중 어떤 철학을 받아들였는지가 아니다. .
ko075 | NEW | ko071 | 0.10 | **반대 증거에 대한 결정 수정:** 명세와 기존 클라이언트 테스트를 독립적으로 검증한 뒤, 같은 사실을 서로 다른 지시 조건의 에이전트에 제공해 수정·유지·기권·지시 충돌 보고를 구분한다.
ko076 | NEW | ko051 | 0.02 | 원칙을 고수한 이유가 문서화된 상위 지시인지, 부정확한 요구 해석인지, 실제로 근거 없는 권위 부여인지 별도 판정한다.
ko077 | NEW | ko084 | 0.06 | 전통적인 요구사항 추적 검토자와 같은 정보를 제공한 대조군이 동등하게 설명한다면 새로운 기제의 증거는 약해진다.
ko078 | NEW | ko083 | 0.03 | 세 연구는 같은 질문을 다른 방법으로 공격하며, 어느 하나가 먼저 성공해야 다른 연구자가 착수할 수 있는 것은 아니다.
ko079 | NEW | ko006 | 0.04 | 더 장기적으로는 SOLID형 구조와 함수·콜백 기반 설계의 실제 유지보수 요구, 수정 토큰·리뷰 노동·회귀 오류·에너지 등을 비교할 수도 있다.
ko080 | NEW | ko043 | 0.06 | 다만 그러한 **비용 절감 효과나 보편적인 상위 설계 법칙은 현재 논문에서 측정하거나 발견한 결과가 아니다.
ko081 | NEW | — | 0.00 | ** 다음 결과들은 제안의 강한 해석에 반대한다.
ko082 | NEW | ko042 | 0.07 | 첫째, 명확한 요구와 계약 아래 모든 에이전트가 원칙의 문구와 무관하게 동일한 적법한 패치를 만든다.
ko083 | NEW | ko051 | 0.07 | 둘째, 강한 SOLID 지시가 설명의 단어만 바꾸고 소스 코드는 바꾸지 않는다.
ko084 | NEW | ko082 | 0.06 | 셋째, 강한 원칙이 특정 과제에서 정확성이나 계약 보존을 개선한다.
ko085 | NEW | ko063 | 0.04 | 넷째, 관찰된 충돌과 실패가 원칙의 특별한 권위 때문이 아니라 정상적인 지시 우선순위, 불완전한 소스 정보 또는 기존 요구사항 추적으로 모두 설명된다.
ko086 | NEW | ko032 | 0.10 | 이런 결과라면 '운영상의 준공리화'가 널리 발생하는 독립적인 현상이라는 주장을 강화해서는 안 된다.
ko087 | NEW | ko019 | 0.05 | 우리의 문제 제기는 어떤 결론이 나와도 자동으로 맞는 것으로 정의된 이론이 아니다.
ko088 | NEW | ko004 | 0.03 | 오히려 **어떤 증거가 나오면 이 가설을 버려야 하는지 명시한 연구 질문**이 되어야 한다.
ko089 | NEW | ko049 | 0.03 | 현재 확인한 작은 반례와 분류 자료는 이 질문을 제기할 근거이지, 그 답은 아니다.
ko090 | NEW | ko088 | 0.39 | 소프트웨어 설계 원칙은 변화를 설명하는 언어를 제공했다.
ko091 | NEW | ko002 | 0.10 | AI 코딩 에이전트가 그 언어를 실제 수정 결정으로 옮길 수 있는 지금, 우리는 원칙이 *무엇을 설명하는가*뿐 아니라 *어떤 권위로 특정 패치를 결정하는가*를 따로 연구할 필요가 있다고 제안한다.
ko092 | NEW | ko007 | 0.11 | 이를 **운영상의 준공리화**라는 반증 가능한 연구 문제로 부르되, 현상의 보편성이나 역사적 원인, 새로운 설계 법칙의 발견은 주장하지 않는다.
ko093 | NEW | ko087 | 0.06 | 역사 연구자, 요구공학·프로그램 언어 연구자, AI 에이전트 실험 연구자가 각자의 방법으로 이 차이를 조사할 수 있다.
ko094 | NEW | ko091 | 0.11 | 그 답이 기존 원칙을 강화하든 그 적용 범위를 좁히든, 더 신뢰할 수 있는 설계 조언을 만드는 데 도움이 될 것이다. ---
Summary ko: SAME 2, EDIT 2, NEW 90

### en (99 sentences)
en001 | NEW | en075 | 0.38 | Does knowing a design principle entail knowing when that principle should govern an actual software change?
en002 | NEW | en003 | 0.19 | The Open–Closed Principle and related SOLID guidance describe how software might accommodate change, but the relevant changes and protected clients depend on the project.
en003 | NEW | en002 | 0.30 | As AI coding agents move from describing designs to producing and judging patches, **we propose asking whether conditional guidance sometimes acquires decision authority without an adequate account of its scope**.
en004 | NEW | en017 | 0.28 | We call this falsifiable research target *operational quasi-axiomatization*.
en005 | NEW | en030 | 0.19 | Martin's contrasting shape-change requirements, an archive used to classify SOLID violations, and an author-constructed fixed-patch example clarify the distinction between naming a structural concern and justifying a con
en006 | NEW | en076 | 0.13 | None establishes the prevalence or origin of such agent behavior.
en007 | NEW | en005 | 0.28 | We propose three research entry points: tracing the scope of design advice in historical and developer-facing texts, testing instruction effects on actual patches under matched contracts, and measuring evidence-responsiv
en008 | NEW | en006 | 0.27 | The objective is not to disprove SOLID or announce a superior mathematical design law but to invite a source-grounded investigation of **the authority principle language exercises over software modifications**.
en009 | NEW | en028 | 0.12 | In Robert Martin's 1996 discussion, a drawing routine can accommodate another kind of shape when objects provide their own drawing operations.
en010 | NEW | en036 | 0.17 | A new requirement changes the problem: every circle must be drawn before every square.
en011 | NEW | en033 | 0.12 | A routine that draws shapes in the order received does not satisfy that requirement by itself.
en012 | NEW | en032 | 0.07 | **Must the routine do the sorting, or must callers pass a sorted sequence?
en013 | NEW | en055 | 0.09 | ** Inspection of the loop alone cannot establish which party owns the responsibility.
en014 | NEW | en012 | 0.15 | A principle that helps anticipate one kind of change does not automatically decide a different requirement. ; .
en015 | NEW | en007 | 0.22 | The same distinction matters when a coding agent is asked to extend a mature application.
en016 | NEW | en031 | 0.16 | Citing OCP in an explanation is not identical to accepting one patch, generating a particular abstraction, or rejecting an otherwise feasible alternative because of that principle.
en017 | NEW | en015 | 0.33 | Those acts may be justified by project requirements and policies.
en018 | NEW | en033 | 0.12 | They might also omit relevant obligations.
en019 | NEW | en042 | 0.10 | We do **not** presume widespread agent misuse.
en020 | NEW | en073 | 0.21 | We propose finding out when any such divergence can be observed and when conventional instruction following or source-aware requirements reasoning already explains the decisions.
en021 | NEW | en034 | 0.22 | The object of study is a design principle's **operational authority**.
en022 | NEW | en005 | 0.19 | Did it affect the patch, did the resulting patch satisfy protected clients, could the agent support its disposition with source evidence, and did a credible counterexample lead to revision or justified abstention?
en023 | NEW | en016 | 0.16 | The ability to act on principle language makes these questions relevant to AI-assisted engineering; it does not answer them.
en024 | NEW | en020 | 0.14 | The history of object orientation was not the development of one immutable SOLID rulebook.
en025 | NEW | en021 | 0.44 | Simula's modeling and classes, Smalltalk's messaging, Parnas's information hiding, and Liskov and Wing's behavioral subtyping addressed distinct problems.
en026 | NEW | en076 | 0.11 | The GoF design-pattern catalog and the later SOLID mnemonic also have different histories, although their design concerns may overlap.
en027 | NEW | en017 | 0.11 | Their original problem settings deserve examination rather than being subsumed under a timeless slogan. ; ; .
en028 | NEW | en022 | 0.29 | Meyer's account combines extensibility with stable descriptions on which existing clients rely.
en029 | NEW | en022 | 0.12 | Martin makes the strategic choice of changes against which a module should be closed explicit.
en030 | NEW | en022 | 0.17 | Adding a shape and reordering existing kinds of shapes are different demands.
en031 | NEW | en024 | 0.33 | That history provides evidence of **conditional guidance**, not grounds to accuse the original authors of having asserted five universal mathematical axioms.
en032 | EDIT | en025 | 0.58 | [Meyer first-edition passage audit](.
en033 | SAME | en025 | 1.00 | /13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md); .
en034 | NEW | en027 | 0.32 | But conditions can be lost when guidance travels through textbooks, review rubrics, repository instructions, and agent prompts.
en035 | NEW | en003 | 0.19 | We distinguish **formal axiomatization**, the legitimate specification of premises and inference rules; **professional canonization**, historical authority gained through repeated use; and **operational quasi-axiomatizat
en036 | NEW | en029 | 0.13 | The third is not automatically caused by the first two and provides no direct access to a model's hidden beliefs or pretraining contents.
en037 | NEW | en030 | 0.44 | A structural classification and a patch disposition require different evidence. evaluates LLM-based SOLID-violation detection.
en038 | NEW | en031 | 0.14 | It should not be described as an experiment establishing which specific maintenance patches deserve rejection.
en039 | NEW | en005 | 0.18 | Our earlier independent inspection of its archived OCP subset distinguished **48 unique submitted code examples, 768 stored response rows and 24 masked prompt scaffolds**.
en040 | NEW | en061 | 0.14 | The 768 rows were not independent real maintenance tasks, and code-internal comments were present in some samples. .
en041 | NEW | en035 | 0.12 | To make the gap tangible, we previously constructed a small library-patch example.
en042 | NEW | en035 | 0.26 | The *same candidate* adds technical-report support but does not add errata support and changes the prefix of an existing book output from to .
en043 | NEW | en036 | 0.16 | Holding the candidate fixed while varying the stipulated task and protected client obligation yields: Acceptance in the first row is **conditional on this investigator-defined contract**, not proof that an actual client 
en044 | NEW | en035 | 0.11 | If protection of the book prefix is not disclosed, the report-only case is **Defer**.
en045 | NEW | en043 | 0.12 | An additional independent protected obligation may invalidate an earlier acceptance.
en046 | NEW | en038 | 0.18 | [Executable fixed-patch case](.
en047 | SAME | en038 | 1.00 | /31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md); ; .
en048 | NEW | en033 | 0.46 | Requirements engineering and Design by Contract already provide classical ways to express this distinction.
en049 | NEW | en006 | 0.13 | Our contribution is not the invention of those premises or a new proof about all programs.
en050 | NEW | en003 | 0.23 | We propose investigating **whether coding agents that invoke named design principles actually consult the relevant requirements and contracts when choosing, defending and revising a patch**.
en051 | NEW | en020 | 0.18 | Mentioning a principle is neither a failure nor a success indicator.
en052 | NEW | en034 | 0.18 | We need to observe whether principle language affects a disposition.
en053 | NEW | en062 | 0.15 | Even an unacceptable patch can have several explanations: incorrect code comprehension, conflicting instructions, missing test coverage, or an unjustified refusal to consider authorized alternatives.
en054 | NEW | en051 | 0.32 | **Following an explicit HARD_SOLID instruction may be legitimate policy compliance.
en055 | NEW | en037 | 0.15 | ** It is not evidence that an agent independently believes SOLID to be an infallible axiom.
en056 | NEW | en071 | 0.18 | Proposed future observations must therefore establish the authority of the source-backed requirement and contrary evidence, distinguish permissible from mandatory choices, and examine whether an agent can revise or appro
en057 | SAME | en056 | 1.00 | [Identification critique](.
en058 | SAME | en057 | 1.00 | /53_PAPER_B_R11_COMPLIANCE_VS_QUASI_AXIOM_IDENTIFICATION.md).
en059 | NEW | en030 | 0.17 | Structural *classification*, contractual *patch correctness*, the *provenance of reasons*, and *revision after rebuttal* are different outcomes.
en060 | NEW | en020 | 0.10 | They should not be collapsed into a single SOLID-adherence score.
en061 | NEW | en073 | 0.41 | If existing requirements-traceability methods with equal source information fully explain the observed behavior, there may be no new causal mechanism to identify.
en062 | NEW | en017 | 0.21 | The term operational quasi-axiomatization is a proposal for an observable research target, not a diagnosis of the agent's mental state.
en063 | NEW | en058 | 0.15 | **Historical and documentary analysis.
en064 | NEW | en005 | 0.13 | ** Compare primary SOLID discussions, educational documents and repository instructions to assess how explicitly scope and exceptions accompany principles.
en065 | NEW | en058 | 0.10 | Freeze sampling periods and document genres.
en066 | NEW | en080 | 0.09 | A null result or a difference explained by document type is as valid as a finding of context-stripping.
en067 | NEW | en031 | 0.15 | A temporal change in wording does not establish that AI caused the change.
en068 | NEW | en063 | 0.14 | **Instruction effects on actual patches.
en069 | NEW | en043 | 0.35 | ** Hold source commit, requirement, protected old clients, edit rights, test environment and tool budget constant, then compare fresh agent invocations assigned to the inherited four advice conditions: **NONE, HARD_SOLID
en070 | NEW | en020 | 0.13 | Include tasks where a principle-conforming structure helps and tasks where mechanical application would be disadvantageous.
en071 | NEW | en047 | 0.16 | Separate code and client-contract correctness from explanations.
en072 | NEW | en058 | 0.09 | If all arms produce the same acceptable patch or strict guidance performs better, preserve that outcome.
en073 | NEW | en054 | 0.21 | A randomized comparison may identify **effects of the injected advice**, not a causal mechanism in opaque pretraining. .
en074 | NEW | en062 | 0.23 | **Revision under authenticated counterevidence.
en075 | NEW | en031 | 0.16 | ** Establish protected caller tests and task specifications independently before providing the same credible fact to different agent conditions.
en076 | NEW | en062 | 0.17 | Distinguish justified revision, continued adherence, abstention and explicit instruction-conflict reports.
en077 | NEW | en053 | 0.15 | Source and instruction hierarchy must be considered before inferring that a refusal was unjustified.
en078 | NEW | en034 | 0.14 | If an ordinary source-aware requirements reviewer given the same information explains the outcome equally well, the claim of a distinctive principle-authority effect must be weakened.
en079 | NEW | en067 | 0.15 | These studies can start separately.
en080 | NEW | en069 | 0.32 | Historians need not first build a Go benchmark, and experimentalists need not establish a new mathematical software law.
en081 | NEW | en065 | 0.22 | Future work could also compare architectures under sequences of actual changes, measuring initial abstraction cost, agent tokens, reviewer effort, regressions and energy separately.
en082 | NEW | en054 | 0.11 | **No reduction in such costs has been demonstrated by the present paper.
en083 | NEW | en074 | 0.18 | ** Several outcomes would count against a strong quasi-axiomatization account.
en084 | NEW | en060 | 0.13 | Given clear tasks and contracts, agents may produce equally valid patches regardless of principle wording.
en085 | NEW | en060 | 0.17 | Strict guidance may change only explanatory vocabulary.
en086 | NEW | en046 | 0.14 | It may improve contract preservation on a class of tasks.
en087 | NEW | en003 | 0.16 | Apparent errors may be fully accounted for by valid instruction precedence, missing source evidence or ordinary requirements reasoning rather than a special design-principle effect.
en088 | NEW | en074 | 0.21 | Such cases would not license a stronger claim by renaming all behavior quasi-axiomatization.
en089 | NEW | en026 | 0.16 | The position is therefore an invitation to a **falsifiable question**, not a theory defined to succeed regardless of observation.
en090 | NEW | en035 | 0.15 | Existing constructed witnesses and classification records motivate that question but cannot answer it.
en091 | EDIT | en077 | 0.50 | Software design principles provide a language for engineering change.
en092 | NEW | en078 | 0.19 | Agents that can translate this language into executable patches make it worthwhile to study not only what a principle says but also **what authority it has over a particular modification**.
en093 | NEW | en003 | 0.27 | We propose operational quasi-axiomatization as a falsifiable research object without presuming its prevalence, its historical causes, or the discovery of a superior design law.
en094 | NEW | en005 | 0.17 | Historians, requirements and programming-language researchers, and coding-agent experimentalists can study its distinct aspects with their own evidence.
en095 | NEW | en081 | 0.20 | A result that strengthens familiar principles or limits their scope would both help make engineering advice more accountable. --- - This v27 manuscript deliberately restores: v01/v08 Martin responsibility opening; v09/v1
en096 | NEW | en024 | 0.10 | Prior source audit and executable witness are **inherited historical results**, not replicated today. - Cross-version sources: [R16](58_PAPER_B_R16_V01_V26_CROSS_VERSION_SALVAGE_LEDGER.md).
en097 | NEW | en057 | 0.11 | Multi-perspective review: [R17](59_PAPER_B_R17_FIVE_PASS_SIX_ROLE_ADVERSARIAL_INTEGRATION.md).
en098 | NEW | en065 | 0.15 | New research novelty has **not** been established against every relevant current publication. - Subsequent submission work needs accurate venue-dependent references, fact/source citation mapping, bilingual proofread, ind
en099 | NEW | en028 | 0.07 | No fake peer-review claim and no automatic submission.
Summary en: SAME 4, EDIT 2, NEW 93
