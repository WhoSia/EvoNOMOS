:- use_module(library(plunit)).

% Finite Boolean world model. This is model finding, NOT universal proof.
bit(false).
bit(true).

flip(false, true).
flip(true, false).

initial(B, world(B, B)) :- bit(B).
updated(world(B, C), world(B, N)) :- flip(C, N).

observe(live, world(_, Current), Current).
observe(snapshot, world(Built, _), Built).

countermodel(B, Initial, Later) :-
    initial(B, Initial),
    updated(Initial, Later),
    observe(live, Initial, X),
    observe(snapshot, Initial, X),
    observe(live, Later, Y),
    observe(snapshot, Later, Z),
    Y \= Z.

:- begin_tests(contextual_equivalence).

test(initial_same, [forall(bit(B))]) :-
    initial(B, W),
    observe(live, W, V),
    observe(snapshot, W, V).

test(updates_separate, [forall(bit(B))]) :-
    countermodel(B, _, _).

test(no_initial_counterexample, [fail]) :-
    initial(_, W),
    observe(live, W, X),
    observe(snapshot, W, Y),
    X \= Y.

test(exactly_two_boolean_counterexamples) :-
    findall(B, countermodel(B, _, _), Bs),
    sort(Bs, Unique),
    Unique == [false, true].

:- end_tests(contextual_equivalence).
