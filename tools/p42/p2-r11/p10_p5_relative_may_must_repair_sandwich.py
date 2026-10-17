#!/usr/bin/env python3
"""Relative may/must source-repair abstraction, with actual Chi native
effect truth table as FINITE input model, not a global Go semantic proof.

All research-owned toy revisions/edit rights/costs are explicitly hypothetical.
MAY predicts an optimistic lower bound, MUST supplies executable-path upper
witnesses. The information loss examples are classical abstract interpretation.
"""
import json
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from collections import defaultdict

@dataclass(frozen=True)
class S:
    revision:int  # 0=old authentic Chi, 1=actual merged Chi
    discard:int   # 0=normal writer, 1=Discard was set
    invocation:int # 0=direct Flush, 1=http.ResponseController.Flush
    right:int      # illustrative edit-right bit, NOT upstream authority

STATES=tuple(S(*a) for a in product((0,1),repeat=4))
def effect(s):
    # Source-native truth table from 8 actual Go events, under declared
    # no-interference/finite-input assumptions only.
    return not (s.revision==1 and s.discard==1)
def desired(s):
    return s.discard==1 and not effect(s)
def edges(s):
    # Hypothetical single edit in source-owned *model*, not an upstream right.
    if s.right and s.revision==0:
        yield ((1,1),S(1,s.discard,s.invocation,s.right))
def q_incomplete(s):
    return (s.discard,s.invocation,s.right) # forget source revision
def q_effect_complete(s):
    return (s.revision,s.discard,s.right) # invocation irrelevant to tested event

def goal_consistency(q):
    fibers=defaultdict(list)
    for s in STATES:
        fibers[q(s)].append(s)
    violations=[]
    for key,vals in fibers.items():
        if len({desired(s) for s in vals})>1:
            violations.append([key,len(vals)])
    return violations

def is_bisim(q):
    fibers=defaultdict(list)
    for s in STATES:fibers[q(s)].append(s)
    for vals in fibers.values():
        for s,t in product(vals,repeat=2):
            if desired(s)!=desired(t) or effect(s)!=effect(t):
                return False
            es={(cost,q(dst)) for cost,dst in edges(s)}
            et={(cost,q(dst)) for cost,dst in edges(t)}
            if es!=et:return False
    return True

def concrete_costs(s):
    # shortest simple paths suffice here: only 0->1 action, nonnegative.
    costs=set()
    if desired(s): costs.add((0,0))
    for cost,dst in edges(s):
        if desired(dst):costs.add(cost)
    return costs

def may_costs(s):
    # Valid MAY quotient: any state in this q fiber is a possible state.
    # Its path possibilities are an overapproximation; do not mistake them
    # for repairs executable from *this* exact source revision.
    fiber=[v for v in STATES if q_incomplete(v)==q_incomplete(s)]
    all_costs=set()
    for v in fiber:
        all_costs |= concrete_costs(v)
    return all_costs

def must_costs(s):
    # Explicit witnessed realization under the hypothetical owned edit
    # grammar. These concrete paths are a subset of possible paths.
    # No state-independent promises about all q fiber members are made.
    return concrete_costs(s)

def scalar_opt(costs,weights=(1,1)):
    return min((sum(a*b for a,b in zip(c,weights)) for c in costs),default=None)

def main():
    assert len(STATES)==16
    assert goal_consistency(q_incomplete) # a source revision effect collision
    assert not is_bisim(q_incomplete)
    assert not goal_consistency(q_effect_complete)
    assert is_bisim(q_effect_complete)
    for s in STATES:
        concrete=concrete_costs(s)
        optimistic=may_costs(s)
        witness=must_costs(s)
        assert witness<=concrete<=optimistic
        if concrete:
            assert scalar_opt(optimistic)<=scalar_opt(concrete)
        if witness:
            assert scalar_opt(concrete)<=scalar_opt(witness)
    old_editable=S(0,1,0,1)
    old_uneditable=S(0,1,0,0)
    assert concrete_costs(old_editable)=={(1,1)}
    assert (0,0) in may_costs(old_editable)
    assert concrete_costs(old_uneditable)==set()
    assert (0,0) in may_costs(old_uneditable)
    # Same old output/method set, different revision: only revision+discard
    # distinguishes the real transport effect on the 8 native samples.
    report={
       "verdict":"P10_P5_RELATIVE_MAY_MUST_REPAIR_SANDWICH_FINITE_CLASSICAL_PASS",
       "states":len(STATES),"real_native_effect_worlds_used":8,
       "hypothetical_owner_right_worlds":2,
       "incomplete_quotient_goal_violating_fibers":len(goal_consistency(q_incomplete)),
       "incomplete_quotient_is_strong_bisimulation":False,
       "effect_complete_quotient_is_strong_bisimulation":True,
       "rights_editable_old_source_exact_costs":[list(c) for c in sorted(concrete_costs(old_editable))],
       "optimistic_capability_only_incorrect_zero_cost":True,
       "rights_not_certified_for_real_upstream":"UNKNOWN",
       "must_witnesses_executable_in_actual_upstream_repo":"NOT_CLAIMED",
       "math":"cost-set sandwich K_must subset K_concrete subset K_may; for each nonnegative weight vector, inf may <= inf concrete <= inf must when defined",
       "error_controls":"insufficient goal projection and missing rights block exact source certification",
       "strong_equal_information_classical_rival":"YES; ordinary weighted transition-system abstract interpretation",
       "mathematical_priority":"CLASSICAL",
       "gates":"P42 RUNNING; P43 HOLD; LAW-R2 NOT_AUTHORIZED"
    }
    out=Path("out/p42-r11-p10-p5/may-must-finite-proof.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(report["verdict"])
    print(json.dumps({k:report[k] for k in ("states","incomplete_quotient_goal_violating_fibers","effect_complete_quotient_is_strong_bisimulation")}))
if __name__=="__main__":
    main()
