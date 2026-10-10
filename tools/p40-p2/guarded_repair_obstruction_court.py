"""P40-P2: independently enumerated guarded repair reachability vs exact formula.
Two source edits T/M, four source states 00,10,01,11, optional atomic T+M.
Mathematical model, classically BFS/DP; no production maintainer permission.
"""
from collections import Counter, deque

EDGES=((0,1,"T"),(0,2,"M"),(1,3,"M"),(2,3,"T"),(0,3,"atomic"))

def bfs(safe,rights):
    seen={0} if safe[0] else set()
    todo=deque(seen)
    while todo:
        current=todo.popleft()
        for i,(u,v,_) in enumerate(EDGES):
            if u==current and rights[i] and safe[v] and v not in seen:
                seen.add(v)
                todo.append(v)
    return 3 in seen

def exact(safe,rights):
    return bool(safe[0] and safe[3] and
                (rights[4] or
                 (safe[1] and rights[0] and rights[2]) or
                 (safe[2] and rights[1] and rights[3])))

def flags(bits,n):
    return tuple(bool(bits>>i & 1) for i in range(n))

def run():
    categories=Counter()
    for sm in range(16):
        safe=flags(sm,4)
        for em in range(32):
            rights=flags(em,5)
            observed=bfs(safe,rights)
            derived=exact(safe,rights)
            assert observed==derived,(sm,em)
            cause=("endpoint" if not safe[0] or not safe[3] else
                   "sequence" if not observed else "feasible")
            categories[cause]+=1
    assert dict(categories)=={"endpoint":384,"sequence":49,"feasible":79}
    print("P40_P2_512_GUARDED_GRIDS_FORMULA_EQ_BFS_PASS",dict(categories))
    worlds={
      "coupled_unprotected":(True,False,True,True),
      "coupled_protected":(True,False,True,False),
      "segregated_unprotected":(True,True,True,True),
      "segregated_protected":(True,True,True,True),
    }
    owners={
      "both":(True,True,True,True,False),
      "T_first":(True,False,True,False,False),
      "M_first":(False,True,False,True,False),
      "T_first_plus_atomic":(True,False,True,False,True),
      "atomic_only":(False,False,False,False,True),
    }
    expected={
      "coupled_unprotected":(True,False,True,True,True),
      "coupled_protected":(False,False,False,False,False),
      "segregated_unprotected":(True,True,True,True,True),
      "segregated_protected":(True,True,True,True,True),
    }
    for arch,safe in worlds.items():
        got=tuple(exact(safe,g) for g in owners.values())
        assert got==expected[arch],(arch,got)
        print(f"P40_P2_ARCHITECTURE_{arch} outcomes={got} PASS")
    assert not exact(worlds["coupled_unprotected"],owners["T_first"])
    assert exact(worlds["coupled_unprotected"],owners["T_first_plus_atomic"])
    assert not exact(worlds["coupled_protected"],owners["T_first_plus_atomic"])
    print("P40_P2_ENDPOINT_VS_SEQUENCE_AND_ATOMIC_PATCH_SCOPE_PASS")

if __name__=="__main__":
    run()
