# 공리가 아니라 지도: 설계 원칙의 맥락적 정당화

**Not an Axiom but an Atlas: Mapping the Conditions of Software Design Principles**

EvoNOMOS Paper B | v38 CANDIDATE, 2026-11-23 | SHORT CONCEPTUAL POSITION | Not a mathematical theorem or empirical claim

## 한국어

우리는 소프트웨어 설계를 배울 때 원칙의 이름을 먼저 익힌다. SOLID, DRY, KISS, YAGNI, 정보 은닉은 오랜 경험을 압축해 주지만, 구체적인 코드를 바꿀 때에는 그 이름만으로 결론을 내릴 수 없다. ‘OCP를 위반했으니 수정해야 한다’는 말에는 변경될 기능, 기존 동작의 계약, 팀이 승인한 규칙, 앞으로의 비용이라는 판단의 전제가 빠져 있을 수 있다. 한 원칙을 비판하려는 것이 아니라, **판단의 근거를 생략한 원칙의 권위**를 묻고자 한다.

여기서 원칙보다 더 깊은 한 가지 수학적 공리계를 찾아야 한다고 전제할 필요는 없다. 오히려 각각의 원칙이 다른 조건에서 유용하고 때로는 서로 다른 관점에서 같은 설계를 가리킨다고 생각할 수 있다. 확장이 반복될 것으로 예상되는 시스템에서는 확장 지점을 미리 마련하는 편이 유리할 수 있지만, 확장이 거의 필요하지 않다면 같은 구조가 낭비가 될 수도 있다. 두 판단은 같은 질문의 모순된 답이라기보다 **서로 다른 맥락에서 내려진 조건부 판단**일 수 있다.

우리는 이 관계를 ‘설계 원칙의 맥락별 지도’라는 연구 대상으로 제안한다. 지도에는 원칙의 이름만이 아니라 변경 요구, 보존해야 하는 계약, 가능한 수리 방식, 조직이 제정한 규칙, 비용을 계산하는 기준, 현재의 증거가 함께 기록된다. 어떤 원칙은 한 영역에서 지지되고 다른 영역에서 반박되며, 자료가 부족한 영역에서는 판단을 유보할 수 있다. 더 나아가 한 영역에서 지지와 반박이 동시에 등장할 수도 있다. 그 경우 반대 증거를 지워 단일한 결론을 만들기보다 갈등을 지도 위에 남겨야 한다.

이 아이디어는 이미 존재하는 수학과 대화한다. 형식개념분석은 적용 조건과 포함관계를 질서 있게 나타내는 방법을 제공하고, 다치논리는 증거의 불완전성과 충돌을 구별하며, 형식명세의 institution 이론은 서로 다른 기호와 의미체계 사이의 보존 관계를 다룬다. 그러나 이런 이론이 있다고 해서 소프트웨어 설계 원칙들이 자동으로 하나의 격자나 범주, 또는 매끄러운 공간을 구성하는 것은 아니다. 우리는 **기존 수학을 단어로 장식하는 대신 어떤 설계 질문을 실제로 더 명확하게 만드는지** 검토해야 한다.

더 주의해야 할 것은 지도의 권한이다. 팀이 명시적으로 승인한 규칙은 지켜야 할 조직적 의무일 수 있고, 외부 동작 계약은 시험해야 할 의미론적 제약이며, 유지보수에 관한 조언은 비교할 근거가 있는 가설이다. 이 세 판단을 하나의 ‘좋은 코드 점수’로 뭉개면 설계 도구의 목적함수 자체가 설명되지 않는 공리가 된다. 따라서 원칙의 지도를 만드는 연구는 **원칙의 우열을 계산하는 연구인 동시에 누가 어떤 기준을 선택했는지 드러내는 연구**여야 한다.

결국 EvoNOMOS의 질문은 모든 설계 원칙을 하나의 절대적 정리에 넣을 수 있느냐가 아니다. 어떤 원칙의 판단이 어디에서 정당화되며, 그 정당화가 다른 맥락으로 이동할 때 무엇이 유지되고 무엇이 철회되어야 하는가? 원칙을 고정된 정답으로 섬기거나 폐기하는 대신, 원칙의 유효한 영역과 그 사이의 경계를 탐색해 보자는 것이다. **지도는 세계 자체가 아니다. 중요한 것은 지도의 이름이 아니라, 언제 어디에서 그 지도를 신뢰할 수 있는지 밝히는 일이다.**

## English

We first learn software design by learning names: SOLID, DRY, KISS, YAGNI, information hiding. They compress accumulated experience, but a name alone does not settle a concrete change. ‘This violates OCP’ omits premises about expected demands, preserved behavior, legitimate team rules, and future costs. Our question concerns the authority of advice when its supporting conditions have disappeared from view.

We need not presume that a deeper theory of design must be a single universal axiom system. Principles may instead give overlapping and sometimes divergent partial accounts. Preparing an extension point may be advantageous when extensions recur and wasteful when they do not. These are not necessarily contradictory answers to the same fully specified question; they may be conditional judgments in distinct contexts.

We propose a contextual atlas of design principles. Each entry records the demand, behavior contract, permitted repair, authority of local policy, objective function, and available evidence. A principle may be supported in one region, defeated in another, and undecidable from present evidence in a third. When support and counterevidence coexist, the map should preserve their disagreement rather than conceal it behind a single score.

Formal concept analysis, many-valued logics, and institution theory offer established tools for representing orders, evidential conflicts, and satisfaction across formal languages. Their existence does not establish that design principles form one lattice, category, or smooth manifold. The scientific challenge is to show which engineering distinctions the representation clarifies, and whether it improves over stronger existing alternatives.

A crucial type distinction remains. A binding local rule is a claim of legitimate authority, a behavioral contract imposes semantic obligations, and a maintainability heuristic makes a context-dependent comparative recommendation. Collapsing all three into a single software quality function risks turning the optimizer's own chosen objective into another unexplained axiom. An atlas should therefore make the authority of evaluation criteria visible too.

The central question is not whether every principle can be placed inside one absolute theorem. It is where a principle is warranted, and what must be preserved or revised when its context changes. We need neither worship the familiar names nor discard them. **A map is not the territory: what matters is knowing when and where its guidance is justified.**

## Provenance and guardrails

Original author question from EvoNOMOS 27.md; expands v37, which remains intact. Prior art: Ganter & Wille (1999), Belnap/Dunn four-valued evidence, Goguen & Burstall institutions, Naur (1985), Toulmin (1958/2003), Parnas (1972/1979). This is a position proposal: no claim of new formal mathematical construction, observed frequency of dogmatic design reviews, experimentally identified maintenance costs, or independent academic endorsement.

## LIRA checkpoint

KEEP: contextual atlas 0.98; objective-authority distinction 0.97; explicit four-state evidence 0.91; single universal structure as mandatory premise 0.11. Scores are subjective editorial recommendations, not probabilities of truth.

Status: v38 CANDIDATE, awaiting author review; v37 AUTHOR REVIEW preserved. LAW-R2 still HOLD.