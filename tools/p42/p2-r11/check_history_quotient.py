#!/usr/bin/env python3
"""R11-P2 finite history-erasure indistinguishability court.

Exhaustive over the 2x2 Ruby runtime lookup-precedence / independent edit-right
state space. This is not a formal verification of arbitrary Ruby or Go.
"""
from itertools import combinations, product
from json import dump
from pathlib import Path
states=[]
for order, grant in product(("trim_outer","guard_outer"), (False,True)):
    states.append({
      "source_inventory":"core|guard|trim",
      "order":order,"grant":grant,
      "old":True,
      "lenient":order=="trim_outer",
      "strict":order=="guard_outer",
      "may_edit":grant
    })
def signature(x, features):
    return tuple(x[z] for z in features)
def exact(features):
    groups={}
    for s in states:groups.setdefault(signature(s,features),[]).append(s)
    return all(len({(z["old"],z["lenient"],z["strict"],z["may_edit"]) for z in v})==1 for v in groups.values())
preds={}
for k in range(3):
    for features in combinations(("order","grant"),k):
        preds["+".join(features) or "source_only"] = exact(features)
assert preds=={"source_only":False,"order":False,"grant":False,"order+grant":True}, preds
out={
 "status":"R11_P2_TWO_BIT_MINIMAL_CONDITIONAL_SOURCE_AND_AUTHORITY_CERTIFICATE_FINITE_PASS",
 "states":states,
 "certificate_tests":preds,
 "theorem_boundary":"Finite 4-state countermodel. Correct summary requires runtime dispatch order AND edit grant; source inventory alone loses facts.",
 "general_theorem":"A quotient of a history-enriched deterministic partial edit LTS preserves all finite action-word prefix-safety and demand-goal judgments if it is saturated for build/rights/old-client/goal predicates and each action has identical enabledness and quotient successor on each fiber. Proof by induction on word length. Necessity for exact preservation of single-action enabledness/observable predicates follows from one-step test contexts. Standard labelled transition congruence, not novel.",
 "limits":"No physical Go/Ruby cross-language code was linked; this is a common metalanguage source/history semantics supported by separate Go and Ruby native falsifiers."
}
Path("out/p42-r11").mkdir(parents=True,exist_ok=True)
with open("out/p42-r11/p2-history-quotient.json","w") as f:dump(out,f,indent=2);f.write("\n")
print("R11_P2_FOUR_HISTORY_STATES_TWO_BIT_MINIMAL_QUOTIENT_PASS")
print(preds)
