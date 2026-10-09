"""P37 Math-I exact finite theory checks; synthetic model, NOT a source experiment."""
from itertools import product, combinations

def partition(signatures):
    blocks = {}
    for state, signature in signatures.items():
        blocks.setdefault(tuple(signature), set()).add(state)
    return {frozenset(x) for x in blocks.values()}

def may(n, edges, accepts, start):
    seen = {start}
    stack = [start]
    while stack:
        state = stack.pop()
        if state in accepts: return True
        for a,b in edges:
            if a == state and b not in seen:
                seen.add(b)
                stack.append(b)
    return False

def signature(n, edges, demands):
    return {s:tuple(may(n,edges,accept,s) for accept in demands)
            for s in range(n)}

def exhaustive_demand_refinement():
    # 3 typed source states, 6 directed nonloop potential Γ edges;
    # two independent demand acceptance sets (each of 8 subsets).
    n=3
    pairs=[(a,b) for a in range(n) for b in range(n) if a!=b]
    cases=0; strict=0
    for mask in range(1<<len(pairs)):
        edges={e for i,e in enumerate(pairs) if mask & (1<<i)}
        for a_mask,b_mask in product(range(1<<n),repeat=2):
            accept_a={i for i in range(n) if a_mask&(1<<i)}
            accept_b={i for i in range(n) if b_mask&(1<<i)}
            base=partition(signature(n,edges,[accept_a]))
            extended=partition(signature(n,edges,[accept_a,accept_b]))
            # Every new block must lie inside exactly one old block.
            assert all(any(new <= old for old in base) for new in extended)
            assert len(extended) >= len(base)
            redundant=all(len({signature(n,edges,[accept_b])[s][0] for s in old})==1 for old in base)
            assert (base==extended)==redundant
            strict += len(extended)>len(base)
            cases+=1
    assert cases==4096
    return cases,strict

def coarse_abstraction_countermodel():
    # Exact module-level D: no repair target is reachable from 0 or 1.
    # When composed with a capable context, only state 1 gains the edit.
    # C cannot be represented by applying the module-only signature quotient.
    n=3; accepting={2}
    local=set()
    composed={(1,2)}
    assert signature(n,local,[accepting])[0] == signature(n,local,[accepting])[1]
    assert signature(n,composed,[accepting])[0] != signature(n,composed,[accepting])[1]
    return True

def joint_observation_refinement():
    present={0:0,1:0,2:1}
    future={0:(0,),1:(1,),2:(1,)}
    current=partition({s:(present[s],) for s in present})
    fut=partition(future)
    joint=partition({s:(present[s],)+future[s] for s in present})
    assert len(current)==2 and len(fut)==2 and len(joint)==3

if __name__=="__main__":
    n,strict=exhaustive_demand_refinement()
    assert coarse_abstraction_countermodel()
    joint_observation_refinement()
    print(f"P37_MATH_I_DEMAND_REFINEMENT_EXHAUSTIVE_PASS cases={n} strict_splits={strict}")
    print("P37_MATH_I_COMPOSE_THEN_QUOTIENT_NOT_QUOTIENT_THEN_COMPOSE_PASS")
    print("P37_MATH_I_PRESENT_FUTURE_MEET_EXCEEDS_BOTH_PARTITIONS_PASS")
    print("CLASSICAL_FACTORING_AND_CONTEXTUAL_EQUIVALENCE_NOT_NEW_LAW")
