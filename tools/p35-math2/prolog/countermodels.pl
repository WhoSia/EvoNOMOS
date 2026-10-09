:- use_module(library(plunit)).

repair(base,inline).
repair(base,helper).
with_helper(helper).

may(Start,Feature) :- repair(Start,X), call(Feature,X).
must(Start,Feature) :-
    once(repair(Start,_)),
    \+ (repair(Start,X), \+ call(Feature,X)).

step(a,zero,one).
step(a,two,four).
step(b,zero,two).
step(b,one,three).
two_step(A,B,S,F) :- step(A,S,Mid), step(B,Mid,F).

:- begin_tests(math2).
test(two_distinct_patch_witnesses) :-
    findall(X,repair(base,X),X0),sort(X0,[helper,inline]).
test(may_helper) :- may(base,with_helper).
test(not_must_helper,[fail]) :- must(base,with_helper).
test(ab_three) :- two_step(a,b,zero,three).
test(ba_not_three,[fail]) :- two_step(b,a,zero,three).
test(ba_four) :- two_step(b,a,zero,four).
test(ab_not_four,[fail]) :- two_step(a,b,zero,four).
test(noncommutation_is_not_all_orders_fail) :-
    two_step(a,b,zero,three), two_step(b,a,zero,four).
:- end_tests(math2).
