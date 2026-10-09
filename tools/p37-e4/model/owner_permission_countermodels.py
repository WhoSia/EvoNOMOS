"""P37-MATH-H independent authority vs invariant countermodels.

Each owner has a local 0→1 edit. These models show why theorem F2 needs
both rectangular I and an EXACT asynchronous product of permitted edits.
No novel law or actual-Go edit-graph exhaustiveness is claimed.
"""
from collections import deque

START=(0,0)
GOAL=(1,1)

def reachable(admissible, permission):
    q=deque([START])
    seen={START}
    while q:
        a,b=q.popleft()
        if (a,b)==GOAL:return True
        candidates=[]
        if a==0 and permission("owner_A",(a,b)):
            candidates.append((1,b))
        if b==0 and permission("owner_B",(a,b)):
            candidates.append((a,1))
        for cand in candidates:
            if cand in admissible and cand not in seen:
                seen.add(cand)
                q.append(cand)
    return False

def main():
    full={(0,0),(0,1),(1,0),(1,1)}
    diagonal={(0,0),(1,1)}
    always=lambda owner,s: True
    # Classically rectangular global invariant, but local edits are locked
    # unless the other owner is still at version 0. No last edit allowed.
    restricted=lambda owner,s: (s[1]==0 if owner=="owner_A" else s[0]==0)
    assert not reachable(full,restricted)
    # Complete independent local edit relation, but every intermediate
    # combination violates the nonrectangular global invariant.
    assert not reachable(diagonal,always)
    assert reachable(full,always)
    print("P37_MATH_H_RECTANGULAR_I_BUT_AUTHORITY_GAMMA_NONPRODUCT_NO_PATH_PASS")
    print("P37_MATH_H_INDEPENDENT_GAMMA_BUT_NONRECTANGULAR_I_NO_PATH_PASS")
    print("P37_MATH_H_BOTH_PRODUCT_ASSUMPTIONS_YIELD_PATH_PASS")
    print("CLASSICAL_PRODUCT_AUTOMATA_AND_ACCESS_CONTROL_NOT_NOVEL_LAW")
if __name__=="__main__":main()
