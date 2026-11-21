# Paper B — Revision comparison and author review

2026-11-17 KST. Working versions preserve their own text. Proposed choice for the next pass: revise from v0.2 and retain v0.1's shorter transition from the library to the classification task.

| Question for the author | Earlier opening and outline | v0.1 | v0.2 |
|---|---|---|---|
| What does the reader meet first? | An account of where the OCP label came from, with a source scaffold. | Meyer's report case followed by Martin's two different changes. | The same opening sequence in the main text, preceded by an abstract stating the evidence question. |
| Where does the evidence for the historical claim sit? | In a reading table and a shorthand historical bridge. | The Meyer–Martin edge carries most of the opening. | The edge is in §1. Three later measurement instruments are in §2, with one classification archive inspected in §3. The later sources have roles as comparisons. |
| What do we demonstrate? | Distinct effects of source edits and caller observations. | A readable case where protected outputs and the demand change what a patch warrants. | The four executed cells plus a decision when one field is withheld. Acceptance, rejection and deferral arise from different available evidence. |
| What needs revision? | Several possibilities are outlined more fully than the current evidence warrants. | The archive evidence enters as a reference where it should be argued. | The opening to §2 can read like a second introduction. Carry the reader's problem forward through who knew the demand, who set the protected behavior and who could apply the rule. |

## One Korean opening for author review

> 1988년, 버트런드 마이어는 도서관 프로그램에 기술보고서를 추가하는 예를 들었다. 새 자료를 받을 수 있게 프로그램을 바꾸면서도, 이미 그 프로그램에 의존하는 다른 모듈은 계속 제 일을 할 수 있어야 했다. 로버트 마틴이 1996년에 든 그림 그리기 함수에도 같은 문제가 있었다. 도형 종류를 하나 늘릴 때는 함수가 그대로 일했지만, 원을 사각형보다 먼저 그리라는 요구가 들어오면 순서를 결정하는 방법부터 바꿔야 했다. 오늘날 자동 검토에서 코드에 ‘개방–폐쇄 원칙 위반’이라는 판정이 붙으면, 그 판정으로 실제 수정안을 어디까지 판단할 수 있을까?

- Sentence 2 supplies the legacy commitment before discussing automation. It frames the question that the original edition makes possible. Its wording should stay attached to the stable description, so a later paragraph can specify when source identity, recompilation, observed behavior and client reliance diverge.
- Sentence 4 should keep both requests because their difference earns the historical transition. Reword its English counterpart in the next draft: “The same routine receives different assessments when the proposed change is specified differently.”
- Sentence 5 frames the proposed contribution. The open choice is whether to name the reviewer or maintainer as the decision-maker in the first paragraph. The current v0.2 frames the action as deciding whether to merge a patch.

## Claim checks before expanding the paper

| Review standpoint | What could break the argument | What the working paper can substantiate |
|---|---|---|
| Historian | A chronological sequence could read as intellectual descent or inevitable loss of context. | Meyer to Martin is a citation edge. The later work documents other uses of OCP. The archive is one inspectable instrument. |
| Experimentalist | Coding knowledge, hidden oracles, prior familiarity or a specific task could explain model choices. | The fixed-patch witness establishes sensitivity to declared context. A future randomized review experiment can compare answers by disclosure and include cases where one known fact already settles rejection. |
| Maintainer | Documents disagree about what counts as protected and some restrictions may exist only in an evaluator. | Report which file, test or owner supports each obligation. A missing source for an obligation stays different from an explicit hidden research oracle. |
| Reader of SOLID | A result about accepting a patch may be mistaken for a claim about all useful static heuristics. | A label can help direct attention. The claim applies when the label is used to support a specified engineering decision. |

The working comparison draws on [v0.1](./33_PAPER_B_DRAFT_V0_1.md), [v0.2](./35_PAPER_B_DRAFT_V0_2.md), the [earlier workshop](./27_PAPER_B_OPENING_WORKSHOP.md), and [source notes](./32_THREE_OCP_INSTRUMENTS_CLOSE_READING.md).
