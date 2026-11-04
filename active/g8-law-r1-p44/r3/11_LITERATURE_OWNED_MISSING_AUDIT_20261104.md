# Literature possession audit — 2026-11-04

## Method and limitation
Google Drive metadata filename queries (not full-text DOI scan) were run for exact distinctive paper-title substrings and author names. 'Not found' = **not found by title in accessible Drive metadata at this audit**, NOT proof that bytes are universally absent (aliases, renamed scans, other folders, missing permissions may exist). Archives may mention a paper without owning it. Public bibliographic DOI/URLs checked on the web. This is a manuscript acquisition/watch list, not copies uploaded to Drive.

## Already in Google Drive by identifiable filenames
1. David L. Parnas (1972), *On the Criteria to Be Used in Decomposing Systems into Modules*, DOI https://doi.org/10.1145/361598.361623.
2. L. Prechelt et al. (2001), *A Controlled Experiment in Maintenance Comparing Design Patterns to Simpler Solutions*. Also Prechelt et al. (2002) *Two Controlled Experiments Assessing the Usefulness of Design Pattern Documentation in Program Maintenance*.
3. Dybå, Sjøberg & Cruzes (2012), *What Works for Whom, Where, When, and Why*.
4. Smith et al. (2015), *Is the Cure Worse Than the Disease? Overfitting in Automated Program Repair*.
5. Huang et al. (2023), *A Survey on Automated Program Repair Techniques*.
6. Jung et al. (2018), *Iris from the Ground Up*, DOI https://doi.org/10.1017/S0956796818000151.
7. Gaher et al. (2022), *Simuliris*, DOI https://doi.org/10.1145/3498689.
8. Song et al. (2023), *Conditional Contextual Refinement*, DOI https://doi.org/10.1145/3571232.
9. Song & Cho (2025), *CCR 2.0: Refinement, Unary, and Relational Separation Logic*.

## Priority missing (not found by exact distinguishing title in Drive filenames)
A. John C. Reynolds (2002), *Separation Logic: A Logic for Shared Mutable Data Structures*, DOI https://doi.org/10.1109/LICS.2002.1029817. **P0** fundamental alias/heap semantics.
B. Hongseok Yang & Peter W. O'Hearn (2002), *A Semantic Basis for Local Reasoning*, DOI https://doi.org/10.1007/3-540-45931-6_28. **P0** frame/locality foundations.
C. Calcagno, Distefano, O'Hearn & Yang (2009), *Compositional Shape Analysis by Means of Bi-Abduction*, DOI https://doi.org/10.1145/1480881.1480917. **P0** source-compositional pre/post and inferred missing heap.
D. Flanagan & Godefroid (2005), *Dynamic Partial-Order Reduction for Model Checking Software*, DOI https://doi.org/10.1145/1040305.1040315. **P0** schedule/interleaving search beyond one barrier case.
E. Musuvathi, Qadeer & Ball (2007), *CHESS: A Systematic Testing Tool for Concurrent Software*, Microsoft Research TR-2007-149, https://www.microsoft.com/en-us/research/publication/chess-a-systematic-testing-tool-for-concurrent-software/. **P0** systematic schedule validation.
F. Jimenez et al. (2024), *SWE-bench: Can Language Models Resolve Real-world GitHub Issues?*, ICLR 2024, https://proceedings.iclr.cc/paper_files/paper/2024/hash/edac78c3e300629acfe6cbe9ca88fb84-Abstract-Conference.html. **P1** actual issue/PR historical tests.
G. Ouyang, Yang & Zhang (2024), *Benchmarking Automated Program Repair: An Extensive Study on Both Real-World and Artificial Bugs*, DOI https://doi.org/10.1145/3650212.3652140. **P1** quality of real vs contrived test cohorts.
H. Sjøberg et al. (2005), *A Survey of Controlled Experiments in Software Engineering*, DOI https://doi.org/10.1109/TSE.2005.97. **P1** design of developer effort comparisons.
I. O'Hearn (2020), *Incorrectness Logic*, DOI https://doi.org/10.1145/3371078. **P1** witnessed erroneous source paths, negative-proof direction.
J. Hannemann & Kiczales (2002), *Design Pattern Implementation in Java and AspectJ*, https://www.cs.ubc.ca/~gregor/papers/hannemann-OOPSLA2002-aop-patterns.pdf. **P2** empirical/syntax dependence of pattern modularity.
K. Petke et al. (2024), *The Patch Overfitting Problem in Automated Program Repair*, DOI https://doi.org/10.1145/3663529.3663776. **P1** benchmark tests vs actual correctness caveat.
L. Clarke et al. (2000), *Counterexample-Guided Abstraction Refinement*, DOI https://doi.org/10.1007/10722167_15. **P0/P1** counterexample loop for a repair-eligibility abstraction.

## Distinctions
- Reading Iris or Simuliris already owned can give a modern concurrent separation-logic basis; acquiring Reynolds/Yang/Calcagno is for foundational originality audit, not an excuse to call their results new.
- SWE-bench is a practical task sampling pattern, NOT a proof that one can measure human time from commit timestamps.
- None of these 'missing' items has been newly downloaded or moved during this audit; status is searchable filenames only.
