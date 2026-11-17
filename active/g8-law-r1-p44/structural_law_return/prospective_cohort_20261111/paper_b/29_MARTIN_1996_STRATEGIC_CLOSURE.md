# Paper B — Martin's Two Changes to One Drawing Routine

Direct reading of Robert C. Martin, [*The Open-Closed Principle* (1996)](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf), printed pp. 1–2 and 5–9. The document identifies the early formulation as a paraphrase of Meyer, cites the first edition at p. 23, and describes closure in strict source-edit language. The article's own counterexample shows that the judgment varies with the proposed change.

| Change | What the listing does | Where change or responsibility goes |
|---|---|---|
| Add a new shape subtype | Listing 2 calls the same virtual drawing operation on each supplied shape. | The shape subtype supplies its own operation. The drawing loop can remain identical. The collection must still receive the new shape. |
| Draw all circles before all squares | Listing 2 draws in input order. An input containing a square before a circle exhibits the mismatch if ordering is the routine's responsibility. | A caller that supplies an already correctly ordered list can leave the loop unchanged. That is a different allocation of responsibility from making the routine guarantee the order on an arbitrary list. |
| Change a type-order policy after Listing 6 | The new loop sorts using the comparison operation. Shape types take their precedence from a shared table. | Martin explicitly says the table still changes and can live in its own module. The article then points out the remaining issue of ordering by criteria other than shape type. |

The first two rows already coexist in the 1996 article. The 2003 textbook repeats the contrast in a later presentation, so it need not carry the first-attestation claim. The counterexample lets the manuscript change one variable at a time: hold the drawing routine fixed, vary the requested change and say who must satisfy it. In the last row, the unit of analysis changes the conclusion: the loop and shape subclasses can stay fixed while a policy table changes.

For the historical argument, juxtapose this passage with Meyer's stable description in §2.3. The 1995 Brown–Martin discussion then supplies evidence of a distinct debate over permission to edit and necessity of editing. A paper about what an automated verdict needs to know can keep these disagreements visible before turning to the archived benchmark. [Meyer first-edition audit](./13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md) · [1995 sources and later reception](./21_OCP_USENET_AND_EARLY_SOLID_RECEPTION.md).
