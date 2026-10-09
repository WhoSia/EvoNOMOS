"""P37-E2: finite owner-product invariant and bridge reachability court.

This is a deliberately EXPLICIT model of version compatibility observed in the
separately pinned original gorilla/sessions + securecookie source APIs.
It does NOT enumerate source-code patches or prove deployment operations atomic.
"""
from collections import deque
from itertools import product

W0,W1=0,1
R0,R1,RDUAL=0,1,2
LEGACY_WINDOW,LEGACY_EXPIRED=1,0

def reader_accepts(reader,writer_version):
    return reader==RDUAL or reader==writer_version

def safe(state):
    writer,reader,window=state
    live=reader_accepts(reader,writer)
    historical=(not window) or reader_accepts(reader,W0)
    return live and historical

def successors(state,bridge,atomic,expiry):
    w,r,window=state
    candidates=[]
    if w==W0:candidates.append(("A_writer_switch",(W1,r,window)))
    if r==R0:
        candidates.append(("B_direct_reader_switch",(w,R1,window)))
        if bridge:candidates.append(("B_expand_to_dual_reader",(w,RDUAL,window)))
    if r==RDUAL:candidates.append(("B_contract_reader",(w,R1,window)))
    if expiry and window:candidates.append(("EXTERNAL_expire_historical_obligation",(w,r,LEGACY_EXPIRED)))
    if atomic and w==W0 and r==R0:
        candidates.append(("JOINT_ATOMIC_writer_and_reader",(W1,R1,window)))
    return [(label,s) for label,s in candidates if safe(s)]

def find_path(start,goal,bridge=False,atomic=False,expiry=True):
    if not safe(start) or not safe(goal):return None
    seen={start};queue=deque([(start,[])])
    while queue:
        node,path=queue.popleft()
        if node==goal:return path
        for label,next_state in successors(node,bridge,atomic,expiry):
            if next_state not in seen:
                seen.add(next_state)
                queue.append((next_state,path+[(label,next_state)]))
    return None

def check_binary_square_theorem():
    checked=0
    for mixed10,mixed01 in product((False,True),repeat=2):
        admissible={(0,0),(1,1)}
        if mixed10:admissible.add((1,0))
        if mixed01:admissible.add((0,1))
        # Exact two monotone interleavings under single-owner edits.
        paths=[[(0,0),(1,0),(1,1)],[(0,0),(0,1),(1,1)]]
        may=any(all(st in admissible for st in path) for path in paths)
        assert may==(mixed10 or mixed01)
        checked+=1
    assert checked==4
    return checked

def check_no_local_invariant_factorization():
    # A purely local safety conjunction I_A(w) AND I_B(r) cannot express
    # decoder/encoder compatibility because it is a non-rectangular relation.
    for window in (LEGACY_WINDOW,LEGACY_EXPIRED):
        pairs={(w,r) for w,r in product((W0,W1),(R0,R1,RDUAL)) if safe((w,r,window))}
        for a in product((False,True),repeat=2):
            for b in product((False,True),repeat=3):
                rectangular={(w,r) for w,r in product((W0,W1),(R0,R1,RDUAL)) if a[w] and b[r]}
                assert pairs!=rectangular
    return True

def main():
    assert check_binary_square_theorem()==4
    assert check_no_local_invariant_factorization()
    start=(W0,R0,LEGACY_WINDOW)
    target=(W1,R1,LEGACY_EXPIRED)
    no_bridge=find_path(start,target,bridge=False)
    assert no_bridge is None
    path=find_path(start,target,bridge=True)
    assert path is not None
    assert len(path)==4, path
    assert [x[0] for x in path]==[
        "B_expand_to_dual_reader","A_writer_switch",
        "EXTERNAL_expire_historical_obligation","B_contract_reader"]
    assert all(safe(s) for _,s in path)
    # Without permission/observation for legacy expiry, contraction is wrong.
    assert find_path(start,target,bridge=True,expiry=False) is None
    # Atomic edits are a DIFFERENT authority relation, not a sequential path.
    joint=find_path(start,target,atomic=True)
    assert joint is not None
    print("P37_E2_EXACT_BINARY_SQUARE_FOUR_VARIANTS_PASS")
    print("P37_E2_NONRECTANGULAR_GLOBAL_INVARIANT_NO_LOCAL_FACTOR_PASS")
    print("P37_E2_NO_BRIDGE_SEQUENTIAL_OWNER_PATH_UNREACHABLE_PASS")
    print("P37_E2_DUAL_COMPAT_BRIDGE_THEN_EXPLICIT_EXPIRY_PATH_PASS")
    print("P37_E2_ATOMIC_EDIT_HAS_SEPARATE_AUTHORITY_PASS")
    print("P37_E2_BRIDGE_PATH="+repr(path))
    print("CLASSICAL_PRODUCT_GRAPH_EXPAND_CONTRACT_NOT_NOVEL_SOFTWARE_LAW")
if __name__=="__main__":
    main()
