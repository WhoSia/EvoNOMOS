#!/usr/bin/env python3
"""P42 R11-P10-P7: research-first future repair residual-language math.

32 authored abstract rights/output/tag states, NOT original-Go source semantics.
The mathematical questions, expected bounds and counterexamples were frozen
in commit 0e2387fa before this implementation. Classical Myhill-Nerode/Mealy
minimization and strong-preservation predecessor work remain prior art.
"""
import json
from collections import defaultdict
from dataclasses import dataclass
from itertools import product
from pathlib import Path

ACTIONS=("A","B")
COST={"A":(1,0),"B":(0,1)}
OUTPUTS=tuple(product((0,1),repeat=2))

@dataclass(frozen=True,order=True)
class Source:
    a:int
    b:int
    right_a:int
    right_b:int
    tag:int

S=tuple(Source(*s) for s in product((0,1),repeat=5))
assert len(S)==32

def observe(s):
    return (s.a,s.b)

def edit(s,action):
    if action=="A":
        if s.a or not s.right_a:return None
        return (Source(1,s.b,0,s.right_b,s.tag),("A","A",COST["A"]))
    if action=="B":
        if s.b or not s.right_b:return None
        return (Source(s.a,1,s.right_a,0,s.tag),("B","B",COST["B"]))
    raise AssertionError("nonfrozen edit action")

def run(s,word):
    receipts=[]
    for action in word:
        result=edit(s,action)
        if result is None:
            return ("BLOCKED",)
        s,receipt=result
        receipts.append(receipt)
    return ("VALID",tuple(receipts),observe(s))

# Max two successful actions in this immutable finite grammar.
WORDS=((),("A",),("B",),("A","A"),("A","B"),("B","A"),("B","B"))
def key_receipt(s):
    return tuple(run(s,w) for w in WORDS)

def classes_by_signature(signature):
    groups=defaultdict(list)
    for s in S:groups[signature(s)].append(s)
    return list(groups.values())

def partition_minimize():
    partition=classes_by_signature(observe)
    rounds=[]
    for i in range(8):
        where={s:n for n,part in enumerate(partition) for s in part}
        def sig(s):
            choices=[]
            for a in ACTIONS:
                step=edit(s,a)
                choices.append(None if step is None else (step[1],where[step[0]]))
            return (observe(s),tuple(choices))
        refined=classes_by_signature(sig)
        rounds.append(len(refined))
        if {frozenset(g) for g in refined}=={frozenset(g) for g in partition}:
            return refined,rounds
        partition=refined
    raise AssertionError("partition refinement did not reach fixpoint")

def costs_reaching(s,goal):
    result=set()
    for w in WORDS:
        r=run(s,w)
        if r[0]=="VALID" and r[2] in goal:
            result.add(tuple(sum(x[2][i] for x in r[1]) for i in range(2)))
    return frozenset(result)

def saturate(cost,cap=1):
    return min(cap,cost)
def sat_machine_from(state,word):
    # All states have observational output "0" and "a" first always costs 1.
    edges={
       "x":{"a":("p",1)},"y":{"a":("q",1)},
       "p":{"b":("z",0)},"q":{"b":("z",1)}, "z":{}
    }
    total=0
    for a in word:
        t=edges[state].get(a)
        if t is None:return ("BLOCKED",)
        state,w=t
        total=saturate(total+w)
    return ("VALID",total,0)
def sat_language(s):
    words=((),("a",),("b",),("a","a"),("a","b"),("b","a"),("b","b"),
           ("a","b","a"),("a","b","b"))
    return tuple(sat_machine_from(s,w) for w in words)

def main():
    by_receipt=classes_by_signature(key_receipt)
    by_partition,rounds=partition_minimize()
    assert len(by_receipt)==9 and len(by_partition)==9,(len(by_receipt),len(by_partition))
    assert {frozenset(p) for p in by_receipt}=={frozenset(p) for p in by_partition}
    assert len(classes_by_signature(observe))==4
    assert len(classes_by_signature(lambda s:(s.a,s.b,s.right_a,s.right_b)))==16
    assert all(len(g)>=2 for g in by_receipt)
    assert sum(len(g) for g in by_receipt)==32
    # Every observable terminal goal language over the four installed pairs;
    # compare COMPLETE attainable cost sets, not only minima.
    goal_count=0
    for mask in range(1<<len(OUTPUTS)):
        goal=frozenset(o for i,o in enumerate(OUTPUTS) if (mask>>i)&1)
        goal_count+=1
        for block in by_receipt:
            costs={costs_reaching(s,goal) for s in block}
            assert len(costs)==1,("goal/repair frontier not congruent",goal,block,costs)
    # Verify right-language derivative (not merely same initial totals).
    for block in by_receipt:
        for s,t in product(block,repeat=2):
            for a in ACTIONS:
                e,f=edit(s,a),edit(t,a)
                assert (e is None)==(f is None)
                if e is not None:
                    assert e[1]==f[1]
                    assert key_receipt(e[0])==key_receipt(f[0])
    # Source/AST alone cannot decide owner authorization.
    deny=Source(0,0,0,0,0)
    allow=Source(0,0,1,0,0)
    assert observe(deny)==observe(allow) and deny.tag==allow.tag
    goal=frozenset({(1,0),(1,1)})
    assert not costs_reaching(deny,goal)
    assert costs_reaching(allow,goal)==frozenset({(1,0)})
    # Aggregating by saturated total cost *before* contextual decomposition
    # loses cancellation: equal language at x,y, different residuals at p,q.
    assert sat_language("x")==sat_language("y")
    assert sat_language("p")!=sat_language("q")
    assert sat_machine_from("x",("a","b"))==sat_machine_from("y",("a","b"))
    assert sat_machine_from("p",("b",))!=sat_machine_from("q",("b",))
    result={
      "protocol":"EVONOMOS_P42_R11_P10_P7_AUTHORIZED_FUTURE_EDIT_RIGHT_LANGUAGE",
      "verdict":"PASS_CLASSICAL_9_CLASS_RIGHT_CONGRUENCE_AND_2_NO_GO_COUNTEREXAMPLES",
      "frozen_commit":"0e2387faec0a8fe214c0c72d78eb22d948950f80",
      "synthetic_source_states":len(S),
      "observable_only_classes":4,
      "source_rights_without_irrelevant_tag_classes":16,
      "canonical_receipt_right_language_classes":len(by_receipt),
      "independent_partition_refinement_classes":len(by_partition),
      "refinement_round_class_counts":rounds,
      "all_goal_subsets_checked":goal_count,
      "max_successful_edit_word_length":2,
      "source_only_predicts_external_rights":"NO; formally indistinguishable input states with different authenticated edit ability",
      "premature_saturating_total_cost_right_congruence":False,
      "sat_cost_counterexample":"x and y cumulative capped-to-one cost languages agree but a successors p/q distinguish residual b costs 0 versus 1",
      "right_congruence_domain":"fixed, deterministic, finite, exact PER-STEP cost/event receipts, stagewise safety, owner rights included, authorized edit labels A/B",
      "actual_go_source_rights_certified":False,
      "actual_G1_to_G7_source_simulation":"OPEN",
      "strongest_classical_rival":"right-language/Mealy minimization, abstract interpretation completeness and strong preservation; no claimed advantage",
      "original_design_law":"NOT_PROVEN",
      "gate":"P42 RUNNING; R11-P10-P7 BOUNDED; P43 HOLD; LAW-R2 NOT_AUTHORIZED",
    }
    path=Path("out/p42-r11-p10-p7/right-language-classes-proof.json")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
    print(result["verdict"])
    print(f"P7_MATH_32_SOURCE_WORLDS_9_MINIMAL_RIGHT_CLASSES_16_OBSERVABLE_GOALS_PASS refinement={rounds}")
    print("P7_EXTERNAL_RIGHTS_SOURCE_ONLY_NO_GO_AND_COST_SATURATION_NO_CONGRUENCE_PASS")

if __name__=="__main__":
    main()
