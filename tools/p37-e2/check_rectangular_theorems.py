"""P37-MATH-F finite checks of classical owner-product factoring lemmas.

Scope: abstract finite directed two-state local edit relations, local invariants,
local final-demand sets, and their precise asynchronous product. Not actual
repository source-code-edit enumeration and not novel mathematical discovery.
"""
from itertools import product

A=(0,1)
B=(0,1,2)

def rectangular(rel):
    return all((a,d) in rel and (c,b) in rel
        for (a,b),(c,d) in product(rel,repeat=2))

def exact_rectangular_relation_court():
    entries=list(product(A,B))
    products={
        frozenset((a,b) for a,b in entries if a in sa and b in sb)
        for ma in range(4) for mb in range(8)
        for sa in [{a for a in A if ma&(1<<a)}]
        for sb in [{b for b in B if mb&(1<<b)}]
    }
    yes=0
    for mask in range(64):
        r=frozenset(p for i,p in enumerate(entries) if mask&(1<<i))
        inferred=(r in products)
        closure=rectangular(r)
        assert inferred==closure, (r,inferred,closure)
        if closure:yes+=1
    assert yes>0
    return yes

def local_may(start,allowed,edges,desired):
    if start not in allowed:return False
    seen={start};front=[start]
    while front:
        u=front.pop()
        if u in desired:return True
        for v in (0,1):
            if (u,v) in edges and v in allowed and v not in seen:
                seen.add(v);front.append(v)
    return False

def compositional_may(start,allowed_a,allowed_b,edges_a,edges_b,desired_a,desired_b):
    if start[0] not in allowed_a or start[1] not in allowed_b:return False
    seen={start};front=[start]
    while front:
        a,b=front.pop()
        if a in desired_a and b in desired_b:return True
        neighbors=[(u,b) for u in (0,1) if (a,u) in edges_a]
        neighbors += [(a,v) for v in (0,1) if (b,v) in edges_b]
        for u,v in neighbors:
            if u in allowed_a and v in allowed_b and (u,v) not in seen:
                seen.add((u,v));front.append((u,v))
    return False

def exact_product_reachability_court():
    checked=0
    directed=[(0,1),(1,0)]
    for ea_mask,eb_mask,ia_mask,ib_mask,da_mask,db_mask,sa,sb in product(range(4),range(4),range(4),range(4),range(4),range(4),range(2),range(2)):
        ea={edge for i,edge in enumerate(directed) if ea_mask & (1<<i)}
        eb={edge for i,edge in enumerate(directed) if eb_mask & (1<<i)}
        ia={i for i in A if ia_mask&(1<<i)}
        ib={i for i in A if ib_mask&(1<<i)}
        da={i for i in A if da_mask&(1<<i)}
        db={i for i in A if db_mask&(1<<i)}
        independent=local_may(sa,ia,ea,da) and local_may(sb,ib,eb,db)
        composed=compositional_may((sa,sb),ia,ib,ea,eb,da,db)
        assert independent==composed, (ea_mask,eb_mask,ia_mask,ib_mask,da_mask,db_mask,sa,sb)
        checked+=1
    assert checked==16384,checked
    return checked

if __name__=="__main__":
    n=exact_rectangular_relation_court()
    m=exact_product_reachability_court()
    print(f"P37_MATH_F_RECTANGULAR_ALL_64_RELATIONS_PASS rectangular={n}")
    print(f"P37_MATH_F_ASYNC_PRODUCT_MAY_FACTORING_PASS cases={m}")
    print("CLASSICAL_FINITE_RELATIONS_NOT_NOVEL_BEYOND_SOLID_LAW")
