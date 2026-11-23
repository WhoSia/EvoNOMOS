# R83 — 업스트림 증거·강한 선행실증·연구 범위 재판정

**작성일:** 2026-11-23 · **유형:** 연구 증거 감사 및 새 논문 초안의 사전 근거표 · **판정:** STOP(독립 ATLAS 이론), NARROW(계약 조건별 판단), MERGE(강한 ADR·AREL)

## 1. 이번 회차에 직접 재조회한 기술 증거

| 증거 | 출처와 고정 버전 | 실제 직접 확인 | 학술적으로 허용되는 주장 |
| --- | --- | --- | --- |
| U1 | [go-chi/chi `v5.1.0` `middleware/route_headers.go`](https://github.com/go-chi/chi/blob/v5.1.0/middleware/route_headers.go), Git blob `997bed569ad89aec1f30765bfc6e868a7f232b6d` | 빈 라우터 경로에서 `next.ServeHTTP` 이후 `return` 부재; R82 격리 재현 기록 | 과거 업스트림 코드의 특정 제어흐름과 이중 호출 |
| U2 | [go-chi/chi 공식 수정 커밋 `05f1ef7bb50b8a8cb33a9dd3ba1c5b94bff0f723`](https://github.com/go-chi/chi/commit/05f1ef7bb50b8a8cb33a9dd3ba1c5b94bff0f723) | 공식 수정에 `return` 추가 및 테스트 포함 | 이중 호출을 업스트림 개발자가 고쳐 회귀 검사를 추가했음 |
| U3 | [go-chi/chi `v5.2.5` `route_headers.go`](https://github.com/go-chi/chi/blob/v5.2.5/middleware/route_headers.go), Git blob `1c3334d35fc2b592f1ff01c03213e4779ddde338` | 수정된 `return`이 존재함 | 적어도 이 태그의 원본 코드에 해당 수정이 포함됨 |
| U4 | [go-chi/chi `v5.2.5` `route_headers_test.go`](https://github.com/go-chi/chi/blob/v5.2.5/middleware/route_headers_test.go), Git blob `819101a931c1ce011d5c4ebb72e25ac3d994ba59` | 정확히 한 번 호출되는지 검사하는 테스트 있음 | 공식 회귀 검사 소스 존재; 이번 회차에 전체 Chi를 재실행한 것은 아님 |
| T1 | [R80 재현 패키지](https://drive.google.com/file/d/1-COR8CAkyM6B6ExXPGonBGOVR142-X-K/view), SHA-256 `050a8c291e760c907700606a5d23b17e6e4204ef2b6b6d2b3c5439c41ac96a2c` | R80 소스 7개 Git blob 정확성, 팀 파생 4개 구현 × 3 suite의 예상 결과 12/12 | **팀이 만든 Chi 파생 구현**의 격리된 Go 실행. 업스트림 동일성이나 ATLAS 우위는 아님 |
| T2 | [R82 출처 검사기](https://github.com/WhoSia/EvoNOMOS/blob/main/tools/p35-p7/r82_upstream_fidelity_audit.py) | upstream Git blob과 팀 파생본 4개가 불일치 | 팀의 `original`은 **역사적으로 최초의 연구용 팔**이지 go-chi/chi 원본이 아님 |

## 2. 이번 회차에 새로 발굴한 강한 선행실증

- **Falessi, D., Briand, L. C., Cantone, G., Capilla, R., & Kruchten, P. (2013).** *The value of design rationale information.* ACM Transactions on Software Engineering and Methodology, 22(3), 1–32. DOI [10.1145/2491509.2491515](https://doi.org/10.1145/2491509.2491515). 저자 소속기관의 [논문 초록과 서지](https://pure.ul.ie/en/publications/the-value-of-design-rationale-information/)를 직접 조회. 초록에 따르면 **석사과정 학생 75명이 참가한 두 통제실험**에서 항목의 유형과 수행 과제에 따라 rationale 정보 가치가 달라졌으며, 활동별로 자주 필요했던 항목만 기록하면 완전한 문서의 약 절반 수준의 항목으로 축소할 수 있다고 보고. 원문 전체를 이 회차에 정독한 것은 아니므로 통계적 효과크기·세부 타당도·업무환경 일반화는 **미검증**. 이 선행실증은 **최소 맥락별 근거 기록**이라는 방향 자체가 새롭지 않음을 강하게 시사한다.
- **Bratthall, L., Johansson, E., & Regnell, B. (2000).** *Is a Design Rationale Vital when Predicting Change Impact? — A Controlled Experiment on Software Architecture Evolution.* [접근 가능한 초록/논문](https://ase.in.tum.de/lehrstuhl_1/files/teaching/Lehrstuhl/DesignRationaleWiSe2003/bratthall_et_al_2000.pdf). 웹에서 초록 텍스트를 확인했으며 **17명, 두 실시간 임베디드 시스템**, 한 시스템에서는 정확도·속도에 유의한 개선, 다른 시스템에서는 불확정 결과라고 보고. PDF 페이지 이미지를 이 회차에 안정적으로 재확인하지 못했으므로 본문 전체/표·검정 통계는 검증 완료로 표시하지 않는다. **설계 근거 제공이 변경 영향 분석의 속도·정확도를 높일 수 있는가**는 이미 실험된 질문이므로 새 논문의 독창성 근거가 될 수 없다.

## 3. 주장별 근거·범위 (논문 본문 게이트)

| 주장 ID | 주장 | 이번 단계 상태 | 본문 사용 제한 |
| --- | --- | --- | --- |
| C01 | go-chi/chi v5.1.0 빈 라우터에 두 번 호출되는 경로가 있다 | upstream + 공식 패치 + R82 isolated reproduction | 특정 태그와 빈 라우터 입력에 한정 |
| C02 | 공식 수정은 `return`을 추가하고 회귀 테스트를 작성했다 | upstream commit U2 + v5.2.5 source U3/U4 | EvoNOMOS가 먼저 발견하거나 기여했다고 하지 않음 |
| C03 | R80의 네 구현은 공식 원본이 아니라 연구 파생본이다 | upstream blob vs 팀 4 blobs | `original Chi`라는 표현 금지 |
| C04 | 팀이 정한 D8 요구는 원본 두 연구 팔에서 실패, 수정 두 연구 팔에서 충족 | R80 isolated four-arm replay 12 suites | 업스트림 결함이라고 분류하지 않음 |
| C05 | LIVE/SNAPSHOT은 서로 다른 사후 등록 가시성 계약을 만족한다 | R80 sequential regression | 동시성 전반이나 전역 우열을 주장하지 않음 |
| C06 | R81 비용 비교는 요청 재사용 횟수에 따른 구현별 교환관계를 시사한다 | R81 반복 벤치마크 기록, 팀 변형 2개 | 인간 유지보수 비용·실서비스 일반화·ATLAS 우위 금지 |
| C07 | 새로 추가한 계약 표시가 강한 ADR 대비 사람의 정확도/속도를 개선한다 | **NOT TESTED** | 연구 질문으로만 기술 |
| C08 | ATLAS에 독립적인 신규 학술 기여가 있다 | **NOT ESTABLISHED**; 기존 강한 ADR과 동률·원전 충돌 | 주장 불가 |
| C09 | 맥락별 rationale 항목 선택과 속도·정확도 비교는 새로운 아이디어다 | **CONTRADICTED BY PRIOR STUDIES** | Falessi 2013·Bratthall 2000의 선행성 명시 |

## 4. 새로운 집필 방향

새 논문은 보편 설계 법칙의 증명이나 ATLAS 기능 소개가 아니라, 실제 소프트웨어 변경 이력에 대한 **출처 충실도, 계약 명시, 후속 실험 설계**를 다룬 방법론적/재현성 보고다. 저자 제작 D8 의무와 upstream 공식 수정 이력을 구분해야 한다. 모든 표에서 **출처 단위(official tag / research-derived arm / reviewer-generated oracle)**를 표시한다.

**다음 실험 게이트:** blind/independent E1 사례 선정 → 실제 계약과 gold의 독립 판정 → 강한 ADR 대 최소 계약 필드 비교 → 기록비용·정확도 측정. 이미 내용을 알고 있는 upstream #1045는 **오염된 개발 예제**로만 쓰고 held-out 표본에서 제외.

**문헌 검토 범위:** Falessi 2013의 기관 초록을 확인했으며 논문 PDF 전문 검토는 미완료. Bratthall 2000의 웹 초록을 확인했으나 PDF 페이지 이미지 시각 검증은 이번에 실패. 본문에 수치 효과크기를 추가하려면 원전 표/통계 재검증이 필요.

**최종 판정:** `R83 STRONG_PRIOR_EMPIRICAL_ART FOUND · UPSTREAM v5.1.0/v5.2.5 SOURCE CHECKED · E1 NOT RUN · ATLAS STOP · NARROW/MERGE · PAPER B v50 HOLD`.
