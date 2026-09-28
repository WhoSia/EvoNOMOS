% EvoNOMOS LawKit v0.5 — adversarial discovery rules.
% SWI-Prolog is used because admission is a declarative conjunction over
% candidate facts and because falsification-target queries are naturally relational.

:- use_module(library(http/json)).

bool(true).

high_corequirement("HIGH").
strong_boundary("STRONG").
strong_boundary("STRONG_OPTIONAL_CAPABILITY_SYSTEM").

clean_contamination(false).
clean_contamination("UNRESOLVED") :- fail.
clean_contamination(true) :- fail.

recoverable("LIKELY").
recoverable(true).

candidate_admissible(C) :-
    C.real_demand == true,
    strong_boundary(C.preexisting_boundary),
    high_corequirement(C.capability_corequirement),
    clean_contamination(C.implementation_contamination),
    recoverable(C.exact_source_recoverable).

cbl_falsifier_pressure(C, "HIGH") :-
    candidate_admissible(C),
    C.capability_corequirement == "HIGH".

pair_quality(C, "STRONG") :-
    C.paired_followup == true, !.
pair_quality(_, "SINGLE_DEMAND_ONLY").

explain_candidate(C, Out) :-
    ( candidate_admissible(C) -> Admission = "ADMITTABLE"
    ; Admission = "HOLD"
    ),
    ( C.implementation_contamination == true -> Contam = "TREATMENT_CONTAMINATED"
    ; Contam = "CLEAN_OR_UNRESOLVED"
    ),
    pair_quality(C, Pair),
    Out = _{
      id:C.id,
      repository:C.repository,
      issue:C.issue,
      admission:Admission,
      falsification_target:"CBL-C1",
      capability_corequirement:C.capability_corequirement,
      contamination:Contam,
      pair_quality:Pair
    }.

main :-
    current_prolog_flag(argv, [Input, Output]),
    setup_call_cleanup(
      open(Input, read, S),
      json_read_dict(S, D),
      close(S)
    ),
    maplist(explain_candidate, D.candidates, Results),
    include([X]>>(X.admission=="ADMITTABLE"), Results, Admissible),
    Out = _{
      protocol:"0.5",
      authority:"DISCOVERY_ONLY",
      candidates:Results,
      admissible:Admissible,
      promoted: @(null)
    },
    setup_call_cleanup(
      open(Output, write, O),
      json_write_dict(O, Out, [width(0)]),
      close(O)
    ).

:- initialization(main, main).
