# Paper B — Opening Workshop, Round 1

## Draft lines for author review

**1.** 1988년, Bertrand Meyer는 도서관 프로그램에 기술보고서라는 새 자료 유형을 추가하는 예를 들었다.

**2.** 기존 모듈이 자료 유형을 직접 구별해 처리한다면, 새 유형에 대응하려면 그 모듈의 코드도 고쳐야 한다.

## Why start here

Line 1 identifies a single extension demand described in the first edition, pp. 24–25. It presents an example given by Meyer. Line 2 states the condition that creates work for an existing module. The case makes it possible to point to the original dispatch and later ask whether the affected clients still see the behavior they relied on. The finer distinction between editing and recompiling belongs where the manuscript explains the designs. [First-edition passage audit](./13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md) · [Executable reconstruction](./15_MEYER_LIBRARY_CLOSURE.md).

The existing English [opening](./19_BEFORE_OCP_BECAME_A_CODE_LABEL.md) begins with an abstract characterization of OCP, then introduces Meyer, Martin and the archive. This working proposal puts the maintenance problem first. The manuscript's later comparison still includes the explicit 1988–1996 citation and the modern classification case. A first reader can decide whether to emphasize the edit reaching existing modules here or bring Meyer's stable module description into the first paragraph sooner.

## Prior writing brought to this round

- [WRITING 3.0](https://app.notion.com/p/3faef561cf92813e8d8fefd9b9d166f1) drafts one unit that advances the argument and checks evidence and rhythm afterward. Two linked sentences are the unit for this round.
- In the [original RC example](https://app.notion.com/p/3faef561cf9281ceac48eb3b9b552d04), the component values and sampling interval were concrete, but the reader could not see why the author chose them. The [revision](https://app.notion.com/p/3faef561cf9281048ae6c4d08e7dc9a2) explains why a one-second time constant fits the recording window. Here line 2 likewise earns the use of a small library example by showing who faces an additional edit.
- [PPO feedback](https://app.notion.com/p/3faef561cf9281dfbaa4e6f92aef166f) exposed missing experimental choices beneath defensive prose. The [observation-report review](https://app.notion.com/p/3fbef561cf928189ac5cf27b6db0688f) kept uncertainty where observation warranted it and challenged repetitive qualification. Here the premise about direct type inspection stays in the sentence because it changes the result.
- The [Writing Loop source audit](https://app.notion.com/p/3ffef561cf92813a89dbeccc74566e87) records the originating RITHM/C3X discussion and the EvoNOMOS P15 example of a well-developed side paper drifting from its initial question. The present opening remains attached to this paper's problem of determining closure for a particular change. The [SIMULA source work](./26_SIMULA_EXTERNAL_CLASS_WITNESSES.md) supports a later comparison.

The two lines are proposals for author review. Preserve reactions and their reasons before extending the paragraph.
