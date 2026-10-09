:- use_module(library(plunit)).

% Original finite transition/observation semantics in an independent language.
action(tick).
action(noop).
state(false).
state(true).
flip(false,true).
flip(true,false).

delta(toggle,S,tick,R) :- flip(S,R).
delta(toggle,S,noop,S).
delta(stutter,S,_,S).
delta(silent,S,_,S).

visible(toggle,S,S).
visible(stutter,S,S).
visible(silent,_,false).

run(_,S,[],S).
run(M,S,[A|Rest],Out) :-
    delta(M,S,A,Next),
    run(M,Next,Rest,Out).

observation(M,S,W,Val) :- run(M,S,W,T), visible(M,T,Val).

word_upto(K,W) :-
    between(0,K,N), length(W,N), maplist(action,W).

eq_at_depth(K,Ma,Sa,Mb,Sb) :-
    \+ (word_upto(K,W),
        observation(Ma,Sa,W,X),
        observation(Mb,Sb,W,Y),
        X \= Y).

first_separating(K,Ma,Sa,Mb,Sb,W) :-
    once((word_upto(K,W),
          observation(Ma,Sa,W,X),
          observation(Mb,Sb,W,Y),
          X \= Y)).

product_observe(M,S,Env,E,W,pair(X,Y)) :-
    observation(M,S,W,X), observation(Env,E,W,Y).

independent_product_agrees(K,A,Sa,B,Sb,E,Se) :-
    \+ (word_upto(K,W),
        product_observe(A,Sa,E,Se,W,X),
        product_observe(B,Sb,E,Se,W,Y),
        X \= Y).

leaky_probe(S,W,V) :- run(silent,S,W,V).

:- begin_tests(trace_depth_and_composition).

test(depth_zero_is_equal) :- eq_at_depth(0,toggle,false,stutter,false).
test(depth_one_is_not_equal,[fail]) :- eq_at_depth(1,toggle,false,stutter,false).
test(shortest_word_one_tick) :-
    first_separating(3,toggle,false,stutter,false,W),
    W == [tick].
test(hidden_same_all_prefixes) :- eq_at_depth(3,silent,false,silent,true).
test(leaky_state_distinguishes_empty) :-
    leaky_probe(false,[],X), leaky_probe(true,[],Y), X \= Y.
test(product_retain_equal_depth_zero) :-
    independent_product_agrees(0,toggle,false,stutter,false,toggle,false).
test(product_does_not_erase_distinguishing_word,[fail]) :-
    independent_product_agrees(1,toggle,false,stutter,false,toggle,false).
test(equivalent_pair_preserved,[forall(state(S))]) :-
    independent_product_agrees(3,stutter,S,stutter,S,toggle,false).
test(no_counterexample_to_bounded_depth_antitone,[forall(state(S))]) :-
    (eq_at_depth(2,stutter,S,stutter,S) -> eq_at_depth(1,stutter,S,stutter,S) ; true).

:- end_tests(trace_depth_and_composition).
