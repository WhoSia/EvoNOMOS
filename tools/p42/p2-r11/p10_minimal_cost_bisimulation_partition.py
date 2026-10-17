#!/usr/bin/env python3
"""Exact finite coarsest cost-labelled repair bisimulation computation.

Classical partition-refinement, NOT new algorithmic priority.
Exhaustively checks every equivalence partition of the 8-state example
(Bell(8)=4140), independently certifying coarsest sound partition.
"""
import json
from collections import defaultdict
from pathlib import Path

from p10_structural_repair_quotient_court import (
    STATES, enabled_steps, old_clients_good, goal,
    is_cost_labelled_bisimulation, frontier
)

DEMANDS=("needs_Flush","must_not_expose_Flush")


def canonical(signatures):
    values=sorted(set(signatures.values()),key=repr)
    by={sig:i for i,sig in enumerate(values)}
    return {s:by[signatures[s]] for s in STATES}


def equivalent(a,b):
    return all((a[s]==a[t])==(b[s]==b[t]) for s in STATES for t in STATES)


def refine():
    parts=canonical({s:(old_clients_good(s),tuple(goal(s,d) for d in DEMANDS)) for s in STATES})
    counts=[len(set(parts.values()))]
    while True:
        signatures={}
        for s in STATES:
            steps=tuple(sorted(((name,cost,parts[nxt]) for name,cost,nxt in enabled_steps(s)),key=repr))
            signatures[s]=(parts[s],steps)
        nxt=canonical(signatures)
        if equivalent(nxt,parts):
            return parts,counts
        assert len(set(nxt.values()))>len(set(parts.values())), "refinement must split"
        parts=nxt
        counts.append(len(set(parts.values())))


def set_partitions(n):
    # Restricted-growth strings enumerate each set partition exactly once.
    def extend(prefix,maximum):
        if len(prefix)==n:
            yield tuple(prefix)
        else:
            for label in range(maximum+2):
                yield from extend(prefix+[label],max(maximum,label))
    yield from extend([0],0)


def main():
    partition,counts=refine()
    assert len(set(partition.values()))==4
    assert is_cost_labelled_bisimulation(lambda s:partition[s])
    # The quotient keeps only flush+rights, never the irrelevant source tag.
    for s in STATES:
        for t in STATES:
            assert (partition[s]==partition[t]) == (
                s.flush==t.flush and s.right_to_edit==t.right_to_edit)
    # Exhaustive independent finite optimality check, all 4,140 partitions.
    count,stable=0,0
    for labels in set_partitions(len(STATES)):
        count+=1
        allocation=dict(zip(STATES,labels))
        if is_cost_labelled_bisimulation(lambda s:allocation[s]):
            stable+=1
            # The candidate is no coarser than the calculated quotient:
            # if it merges states, the calculated quotient must merge them.
            for s in STATES:
                for t in STATES:
                    if allocation[s]==allocation[t]:
                        assert partition[s]==partition[t]
    assert count==4140,(count,stable)
    classes=defaultdict(list)
    for s,idx in partition.items():
        classes[idx].append({"flush":s.flush,"edit_right":s.right_to_edit,
                             "irrelevant_source_tag":s.irrelevant_tag})
    findings={
        "model":"8 finite source-history states; 2 demand predicates; Go optional-method signature; edit-right-labelled costs",
        "coarsest_strong_cost_bisimulation_class_count":len(classes),
        "partition_refinement_class_count_history":counts,
        "all_set_partitions_checked":count,
        "valid_cost_bisimulation_partitions":stable,
        "classes":dict(classes),
        "proof_scope":"Minimum number of states only among strong cost-labelled bisimulation quotients for these declared goals/actions; not all possible frontier predictors or real Go languages",
        "result":"CLASSICAL_AUTOMATA_PARTITION_REFINEMENT_AND_EXHAUSTIVE_MINIMALITY_PASS",
        "novelty":"NOT_CLAIMED"
    }
    dst=Path("out/p42-r11-p10/p10-coarsest-repair-bisimulation.json")
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(findings,indent=2,ensure_ascii=False)+"\n")
    print(findings["result"])
    print(json.dumps({k:findings[k] for k in ("coarsest_strong_cost_bisimulation_class_count","partition_refinement_class_count_history","all_set_partitions_checked","valid_cost_bisimulation_partitions")},sort_keys=True))


if __name__=="__main__":
    main()
