# Paper B — From Contested Advice to Automated Design Judgment

2026-11-13 KST · Working research note. P44 LAW-R2 HOLD.

## Founding record

[Archive 1](https://drive.google.com/file/d/1OyTP7Kc83ocpavk2mslZYKDaSBBWt4Er/view) introduces the distinction between advice and rules, operational quasi-axiomatization, agent/user autonomy, and an Open Principle Ledger. It also explicitly leaves the live Codex–Claude crossover unexecuted in its reported early versions. [Archive 5](https://drive.google.com/file/d/1L_YfIOq0RxVmLP8a0Nhs7h8O3RPutQUl/view) records the user's DIP-18 drift question and DIP-19's separation of semantic admissibility from conditional design preferences. [Archive 6](https://drive.google.com/file/d/1pTybpiZID2obS-0CzNnoWQfmZ73qlgu-/view) asks where an intervention's effect changes sign. [Archive 14](https://drive.google.com/file/d/1TuweqOEc1KY14ddEJVoPbBJAiT-i3thP/view) places the discovery of discriminating structures before representation and conditional recovery of SOLID. The archive is evidence of the project's questions and reported status.

## Dated evidence

- [Meyer 1997, §3.3](https://bertrandmeyer.com/wp-content/upLoads/OOSC2.pdf) discusses when a stable interface is ready for clients and, for specifications, approved and baselined. [Martin 1996, p. 6](https://www.cs.utexas.edu/~downing/papers/OCP-1996.pdf) asks designers to choose classes of change against which they seek closure.
- On 8 January 2009 [Hanselman #145](https://www.hanselman.com/blog/hanselminutes-podcast-145-solid-principles-with-uncle-bob-robert-c-martin) named SOLID explicitly. [Spolsky's excerpt from podcast #38](https://www.joelonsoftware.com/2009/01/31/from-podcast-38/) objects to routine interface proliferation while accepting contractual interface separation for public plugin APIs. [Atwood](https://blog.codinghorror.com/the-ferengi-programmer/) and [Martin's return on #150](https://www.hanselman.com/blog/hanselminutes-podcast-150-uncle-bob-martin-this-time-with-feeling) document a public dispute. These establish a terminus ante quem for circulation of the acronym and criticism of strong readings. The first coinage remains unverified.
- [GitHub's 6 August 2025 release](https://github.blog/changelog/2025-08-06-copilot-code-review-copilot-instruction-md-support-is-now-generally-available/) documents repository instructions reaching automated review. [Gloaguen et al.](https://www.sri.inf.ethz.ch/publications/gloaguen2026agentsmd) report instruction following and greater inference cost under tested context-file settings, with no task-success improvement in the authors' aggregate summary.
- [Pehlivan et al., §III-A–C](https://arxiv.org/html/2509.03093v1) use a model to draft examples in named violation categories, human review to refine and validate them, and other LLMs to classify the 240 synthetic snippets. The [replication package DOI](https://doi.org/10.5281/zenodo.17008546) is reported in the paper. Label agreement and independent maintenance outcome are different measurements. The package rows were not audited in this pass. There is no basis here for a training-data explanation or an industry trend.

## Executable review fixture

Run `python3 ocp_case.py check` to execute the four bundled reference patches with the Python standard library (Python 3.10+). Code executed by this command is fixed in the script. Run `python3 ocp_case.py prompt-fixture` or `python3 ocp_case.py blind-fixture` to emit full or demand-masked review inputs. These inputs share the same source, protected paths, representation rule and question. The difference is whether the request is supplied. The reference patches and results should remain outside a fresh reviewer's visible context.

| Design | Demand | Functional checks passed | Existing files edited |
|---|---|---:|---|
| operation-based dispatch | add a shape | 3 | render.py |
| shape-owned operations | add a shape | 3 | none |
| operation-based dispatch | add an operation | 4 | none |
| shape-owned operations | add an operation | 4 | circle.py, square.py |

Python 3.12.14 local run. Four patches, 14 functional checks. The two masked and four full inputs were checked for equality after removing the request field. The fixture follows the two extension axes of [Wadler 1998](https://homepages.inf.ed.ac.uk/wadler/topics/gj.html). It does not attempt his type-safety theorem or search all patches. Wrappers, registries, or changes to the layout can change the result. Existing-file edits count source changes under the stated representation, not human effort. No fresh model review, human review experiment or additional Chi run was made in this pass.

## Reading acquisition

Missing means no matching independent copy found in accessible Drive title/author searches; it is not a corpus-wide absence proof. Retain the prior Meyer/Martin/Expression Problem list. Add [Naur & Randell, Garmisch report](https://scrummanager.com/files/nato1968e.pdf), [Buxton & Randell, Rome report](https://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1969.PDF), [Shaw 1990](https://www.sei.cmu.edu/library/prospects-for-an-engineering-discipline-of-software/), the three 2009 primary reception sources above, [Yanakiev et al. 2025](https://doi.org/10.1016/j.jss.2024.112254), [McMillan 2026](https://arxiv.org/abs/2605.10039), [Investigating the Smells of LLM Generated Code](https://arxiv.org/abs/2510.03029), [A Causal Perspective on Measuring, Explaining and Mitigating Smells in LLM-Generated Code](https://www.microsoft.com/en-us/research/publication/a-causal-perspective-on-measuring-explaining-and-mitigating-smells-in-llm-generated-code/), and [RovoDev Code Reviewer](https://arxiv.org/abs/2601.01129). Gloaguen, Esposito, and Naur's Programming as Theory Building are already held.
