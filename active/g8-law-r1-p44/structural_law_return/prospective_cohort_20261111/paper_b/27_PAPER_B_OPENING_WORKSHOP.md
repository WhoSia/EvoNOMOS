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

## Round 2 — refine the condition and introduce closure

**1.** 1988년, Bertrand Meyer는 도서관 프로그램에 기술보고서라는 새 자료 유형을 추가하는 예를 들었다.

**2.** 기술보고서에 별도 처리가 필요하면, 자료 유형을 코드에 하나씩 열거해 둔 모듈에도 새 분기를 추가해야 한다.

**3.** Meyer는 다른 모듈이 안정된 명세를 바탕으로 사용할 수 있는 모듈을 ‘닫혀 있다’고 했다.

- Line 2 specifies a decision in the displayed design. A catch-all that already satisfies the new requirement, or a dispatcher that looks up registered cases, shows why simply saying that a module distinguishes types was too broad. Whether any existing caller actually receives the new variant is tied to that caller's task.
- Line 3 states Meyer's definition on first-edition p. 23. The distinction between the printed definition and our test of observable behavior belongs in the later discussion of the reconstruction. [Primary passage reading](./13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md).
- The first paragraph can now give the reader two actors to follow: the module that introduces the new type and another module that has been using the old description. After author review, the Martin paragraph can hold one drawing routine fixed across two demands. The case gives the distinction a concrete reason to matter before the benchmark appears. [1996 comparison](./29_MARTIN_1996_STRATEGIC_CLOSURE.md).

Author question for the next revision: should line 3 name closure immediately, or should the paragraph first specify one thing a client needs to keep using?
