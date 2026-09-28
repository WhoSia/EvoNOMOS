% EvoNOMOS LawKit v0.5 — adversarial discovery rules.
% SWI-Prolog is used because admission is a declarative conjunction over
% candidate facts and falsification-target queries are naturally relational.

:- use_module(library(http/json)).

strong_boundary("STRONG").
strong_boundary("STRONG_OPTIONAL_CAPABILITY_SYSTEM").

high_corequirement("HIGH").

clean_contamination(false).

recoverable("LIKELY").
recoverable(true).

field(Dict, Key, Value) :-
    get_dict(Key, Dict, Value).

candidate_admissible(C) :-
    field(C, real_demand, true),
    field(C, preexisting_boundary, Boundary),
    strong_boundary(Boundary),
    field(C, capability_corequirement, Coreq),
    high_corequirement(Coreq),
    field(C, implementation_contamination, Contamination),
    clean_contamination(Contamination),
    field(C, exact_source_recoverable, Recoverability),
    recoverable(Recoverability).

pair_quality(C, "STRONG") :-
    field(C, paired_followup, true), !.
pair_quality(_, "SINGLE_DEMAND_ONLY").

candidate_id(C, Id) :- field(C, id, Id).

explain_candidate(C, Out) :-
    field(C, id, Id),
    field(C, repository, Repository),
    field(C, issue, Issue),
    field(C, capability_corequirement, Coreq),
    field(C, implementation_contamination, RawContamination),
    ( candidate_admissible(C) -> Admission = "ADMITTABLE"
    ; Admission = "HOLD"
    ),
    ( RawContamination == true -> Contam = "TREATMENT_CONTAMINATED"
    ; RawContamination == false -> Contam = "CLEAN"
    ; Contam = "UNRESOLVED"
    ),
    pair_quality(C, Pair),
    Out = _{
      id:Id,
      repository:Repository,
      issue:Issue,
      admission:Admission,
      falsification_target:"CBL-C1",
      capability_corequirement:Coreq,
      contamination:Contam,
      pair_quality:Pair
    }.

is_admissible(X) :-
    get_dict(admission, X, "ADMITTABLE").

main :-
    current_prolog_flag(argv, Args),
    ( Args = [Input, Output] -> true
    ; format(user_error, "usage: p12_rules.pl <input.json> <output.json>~n", []),
      halt(2)
    ),
    setup_call_cleanup(
      open(Input, read, S),
      json_read_dict(S, D),
      close(S)
    ),
    get_dict(candidates, D, Candidates),
    maplist(explain_candidate, Candidates, Results),
    include(is_admissible, Results, Admissible),
    Out = _{
      protocol:"0.5",
      authority:"DISCOVERY_ONLY",
      candidates:Results,
      admissible:Admissible,
      promoted:null
    },
    setup_call_cleanup(
      open(Output, write, O),
      json_write_dict(O, Out, [width(0)]),
      close(O)
    ).

:- initialization(main, main).
