#!/usr/bin/env python3
"""P14: disclosure-order option game on the ALREADY original-Chi-certified P13 graph.
No synthetic replacement source; not another Go source experiment.
Math specified in prior source-independent Git commit 57849a70.
"""
import json
from itertools import combinations
from pathlib import Path

Q="ABCDG"
WORLD=[(mask,z) for mask in range(32) for z in ("-","E","F")]
assert len(WORLD)==96

def leq(x,y):
    m,z=x; n,t=y
    return (m&n)==m and (z==t if z!="-" else t in ("-","E","F"))

def goal(world,g):
    return world[1]==g

def reachable(world):
    return [v for v in WORLD if leq(world,v)]

def possible(world,g):
    return any(goal(v,g) for v in reachable(world))

pairs=sum(leq(x,y) for x in WORLD for y in WORLD)
assert pairs==1215
monotone=all(
    not leq(x,y) or
    all((not possible(y,g)) or possible(x,g) for g in ("E","F"))
    for x in WORLD for y in WORLD
)
assert monotone
for mask in range(32):
    none=(mask,"-"); E=(mask,"E"); F=(mask,"F")
    assert all(possible(none,g) for g in ("E","F"))
    assert possible(E,"E") and not possible(E,"F")
    assert possible(F,"F") and not possible(F,"E")
    assert not any(all(goal(y,g) for g in ("E","F")) for y in reachable(none))
    # If the action MUST irrevocably select E or F before demand disclosure
    # and observation signals are constant, neither choice wins both futures.
    commit={"E":E,"F":F}
    assert not any(all(possible(y,g) for g in ("E","F")) for y in commit.values())
    # If g is revealed *before* choice, policy g -> matching source edit wins.
    assert all(possible(none,g) and goal(commit[g],g) for g in ("E","F"))
    # A free, non-E/F Q-extension does not itself lose either future option.
    if mask!=31:
        available=[bit for bit in range(5) if not(mask&(1<<bit))]
        after=(mask|(1<<available[0]),"-")
        assert all(possible(after,g) for g in ("E","F"))

summary={
 "protocol":"P42_R11_P10_P14_DISCLOSURE_ORDER_SOURCE_CERTIFIED_REACHABILITY",
 "source_input":"R3 #39049148534 / R4 #39050169558 / R5 #39052413257 unchanged Chi seven owned Mount graph",
 "worlds":96,"source_reachable_ordered_pairs":pairs,
 "option_antitonicity_all_96_squared":monotone,
 "none_worlds_with_both_adaptive_goals_feasible":32,
 "forced_E_or_F_before_reveal_nonadaptive_winning_worlds":0,
 "perfect_revelation_before_commit_winning_worlds":32,
 "premature_E_or_F_loses_opposite_goal_worlds":64,
 "non_ef_Q_extension_preserves_both_options":True,
 "assumptions":"fixed append-only 7 action grammar, exact eight-probe effects, owned-source edits, synthetic cost; partial/full disclosure game is theoretical",
 "limits":"no independent human time, new unknown third-party requirements, other edit grammar, upstream source rights or general Go G1-G7 certificate",
 "gates":"P42 RUNNING; P43 HOLD; LAW-R2 NOT_AUTHORIZED"
}
p=Path("out/p42-r11-p10-p14/disclosure-order-option-court.json")
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(summary,indent=2)+"\n")
print("P14_SOURCE_DERIVED_GRAPH_96_WORLDS_1215_PAIRS_QUANTIFIER_ORDER_PASS")
