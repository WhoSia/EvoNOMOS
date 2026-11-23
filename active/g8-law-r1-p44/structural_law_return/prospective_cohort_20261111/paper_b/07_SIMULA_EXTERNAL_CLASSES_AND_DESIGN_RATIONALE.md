# Paper B — When Extension Was a Language Mechanism

## Intake

The following four files were identified from their contents, moved by metadata only, and read back for ID, size, name, and destination. The last two are Research OS items for NOMOS.

| Copy | Shelf | Bytes |
|---|---|---:|
| [Nygaard & Dahl (1981) — The Development of the SIMULA Languages — History of Programming Languages Chapter IX.pdf](https://drive.google.com/file/d/1_2y0MooTFXVe6cALYxzI0j3sFad1bobu/view) | 11_SOURCES | 3101001 |
| [Dahl & Nygaard (1966) — SIMULA - An ALGOL-Based Simulation Language.pdf](https://drive.google.com/file/d/19IbA59xMha2VY9xpuw6IrCPSnX8LsTZa/view) | 10_PAPERS | 1069917 |
| [Agan et al. (2024) — Can You Erase the Mark of a Criminal Record - Labor Market Impacts of Criminal Record Remediation — NBER WP 32394.pdf](https://drive.google.com/file/d/1k_xJbqIbLM_Ac3OXGTLNC_55Otx4xB7O/view) | 11_SOURCES | 928057 |
| [Lageson & Stewart (2024) — The Problem with Criminal Records - Discrepancies between State Reports and Private-Sector Background Checks.pdf](https://drive.google.com/file/d/1mwQKKCE3cTNM0NnHz_qm4RhWvLkRmJIy/view) | 10_PAPERS | 959284 |

The SIMULA history file is the Nygaard-first 1981 HOPL book chapter, pp. 439–493. Its copyright and ISBN identify this copy. It is separate from the 1978 HOPL contribution and NCC report. Agan is the May 2024 NBER working paper, not an automatic substitute for the later journal publication. Greenberg's BMJ download in 00 is the same work as the shelved article and has a different byte count. Both were kept; contents were not asserted byte-identical. The old Barth file in 00 is a one-page journal Literature Received notice quoting the abstract, not the 38-page institute report. Chess and traffic items were left in place.

## Language mechanism and architectural verdict

1. [Dahl and Nygaard 1966](https://www.cs.tufts.edu/comp/150FP/archive/kristen-nygaard/simula-cacm-1966.pdf), introduction, calls SIMULA an ALGOL 60 extension for describing discrete-event systems, highlighting quasi-parallel processing. That paper supports its own account of the problem and mechanism, not an account of what all later object-oriented design is for.
2. [Dahl, Myhrhaug and Nygaard, Some Features of the SIMULA 67 Language](https://informs-sim.org/wsc68papers/1968_0007.pdf), sections 5–6 of the scan, demonstrates another use. A separately compiled class can be selected in the main program through an external declaration and prefixed block. Separately compiled programs expose declarations that permit the compiler to check whether they are compatible. This is an early, concrete case where an extension and its boundary can be stated before a check. This is distinct from deciding which extension should be anticipated, or which customer-visible behavioral properties must survive.
3. [The 1981 retrospective](https://www.cs.tufts.edu/comp/150FP/archive/kristen-nygaard/hopl-simula.pdf) links *Some Uses of the External Class Concept in SIMULA 67* to the October 1968 NATO conference, noting Kjeldaas as presenter. The [Garmisch report](https://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1968.PDF), original p. 157, independently lists the contribution. The December simulation proceedings paper, October conference submission, and 1981 retrospective are three different documents. The October full text remains missing.
4. [Perry and Wolf 1992](https://www.cs.unibo.it/cianca/wwwpages/readings/perrywolf.pdf) treat rationale as integral to architecture, alongside elements and form. This is established prior art against treating explicit design rationale as EvoNOMOS's novelty. [MacLean et al. 1991](https://www.researchgate.net/profile/Victoria_Bellotti/publication/233367028_Questions_Options_and_Criteria_Elements_of_Design_Space_Analysis/links/00b7d53211940ad48e000000/Questions-Options-and-Criteria-Elements-of-Design-Space-Analysis.pdf) further document how questions, options, and criteria can represent design choices.

## Implication for Paper B

Compile-time compatibility can be certified against a stated interface; a design review still needs the demand and the scope of the behavior that must be preserved. EvoNOMOS can test what happens when those premises are unavailable to the evaluator. A strong audit asks for the observed request, the preserved contract, and either a witness or an explicit reason the answer remains open. A historical reception audit can use Greenberg's distinction among amplification and changing the epistemic strength of a claim as comparative method. It must show actual wording, the citation edge, and its change of force in the specific software documents, and cannot infer distortion from abbreviation alone.

No new model run, row-level ASE result, or field effect is claimed. LAW-R2 HOLD.
