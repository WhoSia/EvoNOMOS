# Paper B — Source Closure and Caller Behavior in Meyer's Library Example

Meyer's first edition, *Object-Oriented Software Construction* (1988), pp. 22–25, defines closure around a stable description offered to clients and illustrates the open/closed problem by adding technical reports to an existing library program. The example discusses changes to dispatch and recompilation before presenting inheritance as an answer. The [recovered first-edition passage and edition audit](./13_MEYER_FIRST_EDITION_PASSAGE_RECOVERY.md) are the historical evidence. Martin's *The Open-Closed Principle* (1996), especially p. 6, makes the class of anticipated changes explicit. [Martin's paper](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf)

The Python fixture reconstructs the new-publication-kind demand. It fixes an existing client and catalog, then varies the catalog implementation or explicitly selects a wrapper at composition time. Existing-source preservation counts the text of exactly `client.py` and `catalog.py`. Client behavior compares the same caller's observations on books, journals, proceedings, and an unsupported kind. New demand satisfaction compares the rendered technical report with its expected output. The original catalog rejects that report.

| Candidate | Existing source edits | Changes to observed legacy behavior | Technical report works |
|---|---|---|---|
| Add a delegating provider | None | None | Yes |
| Edit the original dispatch compatibly | catalog.py | None | Yes |
| Add a provider with an override | None | Book output | Yes |
| Edit dispatch and book output | catalog.py | Book output | Yes |

Run `python3 meyer_library_case.py` to generate [the JSON results](./meyer_library_results.json). Python 3.12.14 reproduced the committed output byte for byte. The unchanged client uses the selected provider in all four cases. For the additive cases the original source files are preserved and the composition changes. The behavior comparison covers the four declared observations.

Within this fixture, preserving existing source and preserving these legacy observations are logically independent given a successful extension. Both properties can be required as separate acceptance conditions. This distinction supplies an example for a short historical position paper about the meanings packed into OCP. The construction uses modern Python composition. The historical example concerns inheritance, separately compiled modules, and the design environment described by Meyer.

In a later review experiment, evaluators can separately report the permitted edits, the caller observations required to remain stable, and whether a given extension passes. An instruction that says only “follow OCP” leaves the scoring criteria underdetermined for this example. Whether a model actually collapses the criteria remains an empirical question.
