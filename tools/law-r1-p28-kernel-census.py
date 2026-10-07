#!/usr/bin/env python3
from itertools import product

BASE=(1,1,1)

def delta(after, before=BASE):
    return tuple(a-b for a,b in zip(after,before))

# Typed upstream DROP forces q'=0; g',y' remain binary observables.
rows={delta((0,g,y)) for g,y in product((0,1), repeat=2)}
expected={(-1,0,-1),(-1,-1,-1),(-1,0,0),(-1,-1,0)}
assert rows==expected, (rows, expected)

labels={
    (-1,0,-1):"N0_LAYER_INDEPENDENT_MEDIATION",
    (-1,-1,-1):"N1_CROSS_COUPLED_CONTROL",
    (-1,0,0):"X0_STABLE_GATE_BYPASS_OBSTRUCTION",
    (-1,-1,0):"X1_CROSS_COUPLED_BYPASS_OBSTRUCTION",
}
assert len(set(labels))==4

# Strong scalar mediation adds q-necessity, so y'=0 after q DROP.
strong={r for r in rows if r[2]==-1}
assert strong=={(-1,0,-1),(-1,-1,-1)}

# One directly measured DROP separates the complete weak four-row census.
assert len({labels[r] for r in rows})==4

# Rank-3 witness: mediated q-drop, gate-drop, matched-(q,g) action-only response.
def det3(a,b,c):
    return (
        a[0]*(b[1]*c[2]-b[2]*c[1])
        -a[1]*(b[0]*c[2]-b[2]*c[0])
        +a[2]*(b[0]*c[1]-b[1]*c[0])
    )

rank3_rows=[(-1,0,-1),(0,-1,-1),(0,0,-1)]
assert det3(*rank3_rows)!=0

print("P28_DROP_CENSUS=PASS")
print("P28_STRONG_SCALAR_EXHAUSTIVENESS=N0_N1_ONLY")
print("P28_WEAK_SCALAR_SIGNATURES=4")
print("P28_SINGLETON_SEPARATOR=PASS")
print("P28_RANK3_CANONICAL_WITNESS=PASS")
for row in sorted(rows):
    print(f"P28_ROW={row}:{labels[row]}")
