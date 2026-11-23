# EvoNOMOS R47 — Six Owned Primary Papers, Not a Missing-Literature List

**2026-11-23 KST · first-hand reading of six Drive PDFs** using authenticated text reads and checked metadata. Source titles, authors, date claims, numeric findings below are attributed to the authors. The goal is to disprove weak claims of novelty before expanding Paper B. Each file exists in the owner's Drive; primary evidence is *not* a hypothetical web abstract.

## Ownership / primary-source reading
| Author / year | Original PDF with verified Drive file ID | Source-body evidence and direct limit | What it defeats |
| --- | --- | --- | --- |
| Baldwin & Clark, 2000, *Design Rules, Vol. 1: The Power of Modularity* | [owned PDF](https://drive.google.com/file/d/1yQWVWQSVQRoRNaeH_SHDITdV1oDWr46K/view), verified parent outside canonical 10 | File existence and metadata checked; **book not reread in full this iteration**; cited public publisher/DOI | “modularity under uncertainty is our new invention” |
| Baldwin & Clark, 2002, *The Option Value of Modularity in Design* | [owned 10 PDF](https://drive.google.com/file/d/1r_OC3PX_37x_yx1leZq-SeOyP8rhoPlJ/view), metadata verified, not fully reread here | Design's flexibility/option value is classic | “we invented the option value of abstraction” |
| Sullivan, Griswold, Cai & Hallen, 2001, *The Structure and Value of Modularity in Software Design* | [owned 10 PDF](https://drive.google.com/file/d/1Gyt45QSE3T0RIiivwVIiw4ofxemxLXfr/view), **original 55,927 chars read** | FSE 2001; extends ordinary Design Structure Matrices with environment parameters (EDSM) because design-only matrix lacks the exogenous conditions driving Parnas' KWIC changes. Applies real-options value to the KWIC design comparison, not a future-blind natural dataset trial. Source §5.2 observes that premature decision-rule fixation can foreclose valuable design alternatives. | “putting design in context, or measuring design value in environment, is unprecedented” |
| Bräuer, Plösch, Saft & Körner, 2018, *Measuring Object-Oriented Design Principles: The Results of Focus Group-Based Research* | [owned 10 author preprint](https://drive.google.com/file/d/1ez5xnadnq_x3ttLln3cvU-G_CNqhxrXS/view), **100,547 chars read** | 6 online focus groups, 31 participants, Delphi-style review of measurable design practices related to 10 design principles. Their **abstract explicitly says abstract design principles are hard to apply without concrete rules**, thus they already study principles→operational practices. They acknowledge small and selected groups/text-only discussion as limits; not a randomized software maintenance outcome study. | “we are the first to convert principles into operational criteria/rules” |
| Cabral, Villamizar, Kalinowski, Escovedo, Baldassarre & Lopes, 2024, *Investigating the Impact of SOLID Design Principles on Machine Learning Code Understanding* | [owned 10 author preprint](https://drive.google.com/file/d/1Jej4TkYvBj-5IXZ_FUiO62aihMK5MsRf/view), **59,512 chars read** | CAIN 2024, 3 controlled trials, total 100 data scientists from universities/one company, comparing industrial ML code with an SOLID-oriented rewrite to original; code understanding outcomes are reported as statistically significant. Threats: volunteer/attention effects, context of selected ML artifact and groups, alpha=0.1 used for their Mann–Whitney test. **Not** long-horizon maintenance and cannot isolate each SOLID principle or structural dimension separately. | “there is no controlled empirical evidence of SOLID's benefits” |
| Yanakiev, Lazar & Capiluppi, 2025, *Applying SOLID Principles for the Refactoring of Legacy Code: An Experience Report* | [owned 10 PDF](https://drive.google.com/file/d/1AgrvMjuayztaJ9yp6JtYbzeRyOOcGCG3/view), **92,540 chars read** | Journal of Systems and Software 220 (2025), ASML legacy C/C++; applied DIP-centered recurring refactoring patterns to 5,000+ files. Conclusion reports removal of half of four illegal dependencies and reduction in illegally used exported symbols by >85%; team-specific and technical/organizational context limits generalizability. No source evidence of randomized architecture counterfactual in this paper. | “SOLID/DIP has never supported industrial structural improvement” |
| Wang et al., 2026, *Using LLMs in Software Design: An Empirical Study of GitHub and A Practitioner Survey* | [owned 10 PDF](https://drive.google.com/file/d/1YY3HsuvTBH2qCqEr0_0hPdtrOBxWpmIw/view), **132,533 chars read** | arXiv 2605.01392v2, 291 public developer–ChatGPT conversations and survey of 65 practitioners, categorizing actual design uses including architecture and patterns. Observational use/rationale analysis, not causal proof that an agent-selected principle improves future maintenance. | “AI-supported software design is unexplored” |
| Esposito et al., 2026, *Generative AI for Software Architecture: Applications, Challenges, and Future Directions* | [owned 10 PDF](https://drive.google.com/file/d/1Y_1mI4XFAdft4yp3tfNXOBILpH0DZ327/view), **117,175 chars read** | Journal of Systems and Software multivocal review. Identifies literature on GenAI for design and architecture decisions; full read of available text shows authors note sparse real architecture-quality/modifiability evaluation and calls for evaluation methodology. **Literature synthesis**, not source-level prospective intervention evidence. | “no one has synthesized GenAI for architecture” |
| Pehlivan et al., 2025, *Are We SOLID Yet?* | [owned 10 PDF](https://drive.google.com/file/d/1kSIAwqyLhcNWbwEuuL4uFqZ917Evyz1f/view), title and metadata verified; current iteration did not reread | LLM SOLID-violation identification already under investigation; previously directly read in v29 predecessor research | “SOLID violation classification is brand-new” |

Note: full text fetched for six central sources (Sullivan, Bräuer, Cabral, Yanakiev, Wang, Esposito); the Baldwin book, Baldwin 2002 PDF and Pehlivan source were checked for file ownership but not newly reread. Other relevant held 2006 MacCormack work [PDF](https://drive.google.com/file/d/1dpToLwPwDdba6PCViESNB_XU3tsd9i93/view) was verified as owned but not newly reread. **Do not describe all rows as newly full-text reviewed**.

## Consequence for Paper B v35

**Danger 1 — environment novelty has already been narrowed in 2001.** The Sullivan et al. paper did not merely value generic modularity; it explicitly introduced EXOGENOUS environment parameters missing from design-only structure matrices. Our “conditions and expected changes” description without a predictive/causal or new structural differentiator collides *directly* with that work.

**Danger 2 — operationalizing rules already existed in 2018.** Treating abstract SOLID principles as measurable criteria is not novel; Bräuer et al. used expert groups and a rule/measurement mapping. Our earlier idea of lexical “hardening” is a potentially interesting **historical-pragmatics inquiry**, but not the invention of concrete rules from principles.

**Danger 3 — SOLID is not a straw-man.** The 2024 controlled code understanding experiment and 2025 industrial refactoring report contain positive evidence of benefits in bounded contexts. The proposed conditional framework must be able to *predict those gains as well as failures*. Its success cannot be manufactured by always rejecting SOLID.

**Danger 4 — AI architecture literature exists.** Wang and Esposito show developers and researchers already use/study GenAI for design. A new paper cannot get priority merely by mentioning agents, architectural judgment and requirements.

**Residual hard problem:** construct a **pre-change source-observable, contract-respecting, real-project predictor of which specific structural intervention will help in which future change regime**, compare to 2001 EDSM, 2000/2002 real options, 2025 large industrial architectural complexity measures, and 2025 architectural change predictors. Find *failure regimes* and *inducible new structure* rather than relabel known criteria.

## One strong new synthesis from source collision

A five-stage falsifiable **principle promotion gate** (proposal, not experiment):
1. `Scope`: observed before any future changes, including semantics/contract and horizon.
2. `Intervention`: a real architecture edit distinguishable from the label OCP/SRP/etc.
3. `Comparator`: strongest admissible classical or task-specific alternative.
4. `Outcome`: validated real future maintainer/task results with code- and value-vector outputs.
5. `Revision`: prospective selection misses, shift detected, intervention fails; record defer/retract or narrower policy.
This gate could be an original *research protocol synthesis* if implemented and shown to improve decisions. It is **not** a novel mathematical law. Failure of any of stages 1–4 prevents treating an intuitive maxim as empirically proven.

### LIRA check (subjective)
- Distinguishing pre-change source-observable conditions: 0.97 **as a research target**, technical novelty not yet demonstrated.
- Integration of 2001 EDSM and 2026 AI architecture evidence: 0.94 as scholarly integrity, not novelty of method.
- “We invent operational SOLID measurement”: 0.08, **reject** based on Bräuer 2018.
- “We discover that SOLID can improve understanding”: 0.07, **reject** based on Cabral 2024.
- “We can identify a new general design law from the 12-task toy”: 0.05, **reject**; constructed toy is not evidence.
- “We offer a challenging empirical condition-selection and principle-induction research programme”: 0.92, **keep** with open firstness and real-world outcome limits.

**Status:** 6 OWNED PDF TEXTS READ / ADDITIONAL PRIMARY PDF OWNERSHIP AUDITED / PROMINENT PRIOR-ART DEFEATS RECORDED / REAL ARCHITECTURE-EFFECT TEST NOT RUN.
