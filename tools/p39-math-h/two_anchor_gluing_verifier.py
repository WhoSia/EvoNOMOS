"""Finite mathematical verifier for ternary cyclic-order shattering.
Checks an explicit two-common-vertex gluing construction.
"""
from itertools import permutations, product, combinations

SEED=((0,1,2),(0,1,3),(0,4,5),(1,4,5),(2,3,4),(2,3,5))

def parity(p,t):
    r={v:i for i,v in enumerate(p)}
    a,b,c=t
    return int((r[a]>r[b])^(r[a]>r[c])^(r[b]>r[c]))

def seed_table():
    table={}
    for p in permutations(range(1,6)):
        order=(0,)+p
        table.setdefault(tuple(parity(order,t) for t in SEED),order)
    assert len(table)==64
    return table

def construct(n,bits,table):
    k,rem=divmod(n-2,4)
    assert k>=1 and len(bits)==6*k+rem
    triples=[]; first=[]; second=[]
    for j in range(k):
        def ren(v):
            return v if v<2 else v+4*j
        triples.extend(tuple(ren(v) for v in t) for t in SEED)
        sub=tuple(ren(v) for v in table[tuple(bits[6*j:6*j+6])])
        one=sub.index(1)
        first.extend(sub[1:one]);second.extend(sub[one+1:])
    for j in range(rem):
        v=4*k+2+j
        triples.append((0,1,v))
        if bits[6*k+j]:first.append(v)
        else:second.append(v)
    order=(0,)+tuple(first)+(1,)+tuple(second)
    assert set(order)==set(range(n))
    assert tuple(parity(order,t) for t in triples)==tuple(bits)
    return order

def run():
    table=seed_table()
    for n in range(6,13):
        k,r=divmod(n-2,4);m=6*k+r
        for bits in product((0,1),repeat=m):
            construct(n,bits,table)
        print(f"P39_H_TWO_ANCHOR n={n} independent={m} profiles={1<<m} PASS")
    witness=((0,1,2),(0,1,3),(0,1,4),(0,1,5),(0,1,6),
             (2,3,4),(2,5,6))
    profiles={tuple(parity((0,)+p,t) for t in witness)
              for p in permutations(range(1,7))}
    assert len(profiles)==128
    print("P39_H_SEVEN_WITNESS_INDEPENDENT_PYTHON_PASS")
    for n in (4,5,6):
        edges=tuple(combinations(range(1,n),2))
        orders=tuple((0,)+p for p in permutations(range(1,n)))
        fcount=0
        for mask in range(1<<len(edges)):
            H=tuple(e for i,e in enumerate(edges) if mask>>i&1)
            # Independent simple graph union-find check.
            parent=list(range(n))
            def root(v):
                while parent[v]!=v:v=parent[v]
                return v
            forest=True
            for a,b in H:
                if root(a)==root(b):
                    forest=False;break
                parent[root(a)]=root(b)
            signatures={tuple(parity(p,(0,a,b)) for a,b in H)
                        for p in orders}
            assert (len(signatures)==1<<len(H))==forest
            fcount+=forest
        print(f"P39_H_ANCHORED_FOREST n={n} graphs={1<<len(edges)} forests={fcount} PASS")
    print("P39_MATH_H_ALL_SYNTHETIC_THEORY_CHECKS_PASS")

if __name__=="__main__":
    run()
