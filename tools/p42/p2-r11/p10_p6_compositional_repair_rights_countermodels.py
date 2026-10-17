#!/usr/bin/env python3
"""P42 R11-P10-P6: exhaustive finite composition/repair-rights countermodels.
Pure abstract model, not a source-to-Go theorem. Standard Python only.
"""
from dataclasses import dataclass
from itertools import product
from collections import defaultdict
import json
from pathlib import Path

@dataclass(frozen=True)
class Independent:
    a:int
    b:int
    right_a:int
    right_b:int
    irrelevant_a:int
    irrelevant_b:int

@dataclass(frozen=True)
class Shared:
    a:int
    b:int
    shared_tokens:int

STATES=tuple(Independent(*v) for v in product((0,1),repeat=6))
SHARED=tuple(Shared(*v) for v in product((0,1),(0,1),(0,1,2)))

def transitions(s):
    if s.a==0 and s.right_a:
        yield ('edit_A',(1,0),Independent(1,s.b,0,s.right_b,s.irrelevant_a,s.irrelevant_b))
    if s.b==0 and s.right_b:
        yield ('edit_B',(0,1),Independent(s.a,1,s.right_a,0,s.irrelevant_a,s.irrelevant_b))

def transitions_shared(s):
    if s.a==0 and s.shared_tokens:
        yield ('edit_A',(1,0),Shared(1,s.b,s.shared_tokens-1))
    if s.b==0 and s.shared_tokens:
        yield ('edit_B',(0,1),Shared(s.a,1,s.shared_tokens-1))

def repair_paths(start, moves):
    out=[]
    def walk(s,cost,trace,seen):
        if s.a and s.b:out.append((cost,trace))
        for action,c,next_state in moves(s):
            if next_state not in seen:
                walk(next_state,tuple(x+y for x,y in zip(cost,c)),trace+(action,),seen|{next_state})
    walk(start,(0,0),(),{start})
    return out

def q_complete(s):return (s.a,s.b,s.right_a,s.right_b)
def q_without_rights(s):return (s.a,s.b)

def strong_bisim(states,moves,q):
    blocks=defaultdict(list)
    for s in states:blocks[q(s)].append(s)
    for fiber in blocks.values():
        for s,t in product(fiber,repeat=2):
            if (s.a and s.b)!=(t.a and t.b):return False
            sig=lambda v:{(action,cost,q(nxt)) for action,cost,nxt in moves(v)}
            if sig(s)!=sig(t):return False
    return True

def main():
    assert len(STATES)==64 and len(SHARED)==12
    assert strong_bisim(STATES,transitions,q_complete)
    assert not strong_bisim(STATES,transitions,q_without_rights)
    for s,t in product(STATES,repeat=2):
        if q_complete(s)==q_complete(t):
            assert set(repair_paths(s,transitions))==set(repair_paths(t,transitions))
    init=Independent(0,0,1,1,0,0)
    paths=repair_paths(init,transitions)
    assert set(paths)=={((1,1),('edit_A','edit_B')),((1,1),('edit_B','edit_A'))}
    assert len({trace for cost,trace in paths})==2
    one=Shared(0,0,1)
    assert len(list(transitions_shared(one)))==2
    assert repair_paths(one,transitions_shared)==[]
    two=Shared(0,0,2)
    assert set(repair_paths(two,transitions_shared))==set(paths)
    assert (one.a,one.b)==(two.a,two.b)
    assert repair_paths(Shared(0,0,0),transitions_shared)==[]
    result={
      "verdict":"P10_P6_FINITE_COMPOSITION_AND_SHARED_RIGHTS_COUNTERMODEL_PASS",
      "component_states_checked":len(STATES),
      "shared_global_budget_states":len(SHARED),
      "complete_rights_effect_quotient_strong_bisimilar":True,
      "rights_omitting_quotient_bisimilar":False,
      "independent_two_edit_cost_frontier":[[1,1]],
      "shared_one_token_joint_repair":"IMPOSSIBLE_IN_DECLARED_GRAMMAR",
      "shared_two_token_joint_repair_cost_frontier":[[1,1]],
      "different_ordered_effect_traces_same_final_components":2,
      "lifting_obligations":"factorized rights, frame noninterference, action/cost matching, effect-trace composition",
      "scope":"authored finite abstract semantics; no arbitrary third-party Go source soundness",
      "classical_rivals":"Cousot POPL 1977, effectful compositional semantics and weighted transition systems",
      "novel_universal_SOLID":"NOT_ESTABLISHED",
      "gates":"P42 RUNNING, P43 HOLD, LAW-R2 NOT_AUTHORIZED"
    }
    out=Path('out/p42-r11-p10-p6/composition-math-countermodels.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(result["verdict"])
    print("INDEPENDENT_64_STATE_BISIM_PASS; SHARED_12_STATE_BUDGET_NONFACTOR_PASS; ORDERED_EFFECTS_2")

if __name__=='__main__':
    main()
