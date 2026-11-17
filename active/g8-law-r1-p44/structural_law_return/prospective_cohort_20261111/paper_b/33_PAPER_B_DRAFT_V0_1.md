# Paper B, v0.1 — Before OCP Became a Code Label

Case-led draft · 2026-11-17 KST

## Opening

In 1988 Bertrand Meyer asked how a library program might be extended to handle technical reports. A module that names each supported kind of publication has to make another distinction when a new kind needs separate treatment. Other modules, meanwhile, need a description stable enough to use when they are written. Meyer's example brings these demands into the same program. What can be added, and what can the people using the existing module still count on? [Meyer, *Object-Oriented Software Construction*, first edition, pp. 22–25](./13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md).

Robert Martin's 1996 treatment moves that question into a C++ example. The same drawing function can accept another kind of shape through the Shape interface and still have to change when the customer asks for all circles to be drawn before any square. Martin calls the resulting choice strategic closure. Deciding where a design should be stable requires a judgment about which changes are likely. [Martin, pp. 1, 6–9](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf).

Now consider a review experiment in which a model is shown code and asked whether it violates the open–closed principle. Once the response is recorded as a label, what can someone deciding whether to merge an edit learn from it? A correct prediction of the label and a justified merge decision use evidence in different ways. This article follows what the historical examples make explicit, examines which of those premises were separately recorded in one automated classification study, and tests how the choice of premises affects the judgment of a fixed patch. [Classification archive audit](./18_ARE_WE_SOLID_OCP_ARCHIVE_AUDIT.md).

## One change with two possible judgments

Return to the library. A candidate provider adds technical reports, leaves the old source files in place, and renders an old book with a capitalized prefix. If the existing contract includes the precise book output, the patch breaks that promise. If the contract protects other results and allows that display change, the same patch can satisfy the same request. A further requirement to support errata changes the result again. The patch itself stays put. [Executable reconstruction](./31_OCP_FIXED_PATCH_DEMAND_AND_CONTRACT.md).

The point of the example is to let a proposed classification carry a visible burden of proof. State the requested extension. State what clients are supposed to be able to rely on. State the files or interfaces that have to stay untouched. A maintainer can then check each part of a decision and can say which premise they would need to settle a disputed case.

## Where the current paper fits

Bräuer and colleagues tested whether measurable practices captured their design principles. Cabral and colleagues gave participants a concrete extension scenario involving additional regressors and asked what benefits they saw under two presentations of the software. Zhu and colleagues evaluate generated edits against functional tests and structural oracles for concrete repository scenarios. Classroom examples, human assessments and machine judgments each make part of the problem visible. A fixed-patch comparison allows a further question: which facts must be recoverable from a review report for its conclusion to hold under the specifications that are still possible? [Close reading and references](./32_THREE_OCP_INSTRUMENTS_CLOSE_READING.md).
