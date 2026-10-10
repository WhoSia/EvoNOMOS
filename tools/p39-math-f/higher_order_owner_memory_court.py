"""P39-MATH-F: pure combinatorial source-edit rights court, no Go code.

Each vertex is a commuting one-shot source edit. Triple queries read its
relative-order parity. Optional pair queries detect pair order. All initial
permutations lead to one common source; poset section imposes safe prefixes.
Counts are synthetic mathematics, not empirical owner permissions.
"""
from itertools import combinations, permutations, product
from functools import lru_cache
from math import factorial


def triples(v):
    return tuple(combinations(v, 3))


def pairs(v):
    return tuple(combinations(v, 2))


def tvalue(order, ts):
    r = {v:i for i,v in enumerate(order)}
    return tuple((r[a] > r[b]) ^ (r[a] > r[c]) ^ (r[b] > r[c])
                 for a,b,c in ts)


def pvalue(order, es):
    r = {v:i for i,v in enumerate(order)}
    return tuple(r[a] < r[b] for a,b in es)


def cocycle(n, mask):
    es = pairs(range(1, n))
    bit = {edge: (mask >> i)&1 for i,edge in enumerate(es)}
    return tuple(bit[j,k] if i==0
                 else bit[i,j] ^ bit[i,k] ^ bit[j,k]
                 for i,j,k in triples(range(n)))


def connected(n, es):
    adj=[set() for _ in range(n)]
    for a,b in es:
        adj[a].add(b)
        adj[b].add(a)
    seen=set()
    todo=[0]
    while todo:
        v=todo.pop()
        if v not in seen:
            seen.add(v)
            todo.extend(adj[v]-seen)
    return len(seen)==n


def parity_court():
    for n in range(3,8):
        vs=tuple(range(n))
        ts=triples(vs)
        actual={tvalue(p,ts) for p in permutations(vs)}
        assert len(actual)==factorial(n-1)
        if n<=6:
            expected=1<<((n-1)*(n-2)//2)
            algebraic={cocycle(n,m) for m in range(expected)}
            assert len(algebraic)==expected and actual<=algebraic
            if n>=4:
                four={s:{tvalue(p,triples(s)) for p in permutations(s)}
                      for s in combinations(vs,4)}
                for profile in algebraic:
                    lookup=dict(zip(ts,profile))
                    locally=all(tuple(lookup[t] for t in triples(s)) in vals
                                for s,vals in four.items())
                    assert locally==(profile in actual)
            print(f"P39_F_CYCLIC n={n} profiles={len(actual)} "
                  f"algebraic={len(algebraic)} unrealizable={len(algebraic-actual)} PASS")
        else:
            print(f"P39_F_CYCLIC n={n} profiles={len(actual)} PASS")
    ts=triples(range(4))
    signatures=[tvalue(p,ts) for p in permutations(range(4))]
    bad={k:0 for k in range(1,5)}
    witness=None
    for k in range(1,5):
        for inds in combinations(range(4),k):
            for value in product((0,1),repeat=k):
                if not any(all(x[i]==v for i,v in zip(inds,value)) for x in signatures):
                    bad[k]+=1
                    if witness is None:
                        witness=(inds,value)
    assert bad=={1:0,2:0,3:8,4:10}
    assert witness==((0,1,2),(0,1,0))
    print("P39_F_MINIMAL_TERNARY_UNSAT size=3 size3_instances=8 "
          "algebraically_consistent_unrealizable=2 PASS")
    # Independently test EVERY ternary assignment, not only 2-cocycles.
    vs=tuple(range(5))
    ts=triples(vs)
    realized={tvalue(p,ts) for p in permutations(vs)}
    local={s:{tvalue(p,triples(s)) for p in permutations(s)}
           for s in combinations(vs,4)}
    for sign in product((0,1),repeat=len(ts)):
        record=dict(zip(ts,sign))
        admissible=all(tuple(record[t] for t in triples(s)) in vals
                       for s,vals in local.items())
        assert admissible==(sign in realized)
    print("P39_F_4_LOCAL_GLOBAL n=5 all_1024_raw_assignments PASS")


def mixed_court():
    for n,want in ((3,4),(4,38),(5,728)):
        vs=tuple(range(n))
        orders=tuple(permutations(vs))
        trip=triples(vs)
        tri=[tvalue(p,trip) for p in orders]
        edges=pairs(vs)
        successes=0
        for mask in range(1<<len(edges)):
            tested=tuple(e for j,e in enumerate(edges) if (mask>>j)&1)
            labels={(tri[j],pvalue(p,tested)) for j,p in enumerate(orders)}
            good=connected(n,tested)
            assert (len(labels)==factorial(n))==good
            successes+=good
        assert successes==want
        print(f"P39_F_MIXED_CONNECTIVITY n={n} graphs={1<<len(edges)} "
              f"connected={successes} PASS")
    n=6
    vs=tuple(range(n))
    ps=tuple(permutations(vs))
    tri=[tvalue(p,triples(vs)) for p in ps]
    for edges,want in (((0,1),(1,2),(2,3),(3,4),(4,5)),720),\
                      (((0,1),(1,2),(3,4),(4,5)),684):
        labels={(tri[j],pvalue(p,edges)) for j,p in enumerate(ps)}
        assert len(labels)==want
    print("P39_F_SIX_VERTEX_CONNECTED_DISCONNECTED_COUNTERCHECK PASS")


def adaptive_court():
    for n in range(3,11):
        v=tuple(range(n))
        rotations=[v[i:]+v[:i] for i in range(n)]
        queries=set()
        for a,b in pairs(v):
            mask=sum((1<<i) for i,p in enumerate(rotations)
                     if p.index(a)<p.index(b))
            queries.add(mask)
        full=(1<<n)-1
        @lru_cache(None)
        def depth(mask):
            if mask.bit_count()<=1:
                return 0
            return min(
                1+max(depth(mask&q),depth(mask&~q&full))
                for q in queries if mask&q and mask&~q&full
            )
        expected=(n-1).bit_length()
        assert depth(full)==expected
        print(f"P39_F_ADAPTIVE_VS_FIXED n={n} adaptive={expected} fixed={n-1} PASS")


def invariant_court():
    n=5
    rest=(1,2,3,4)
    all_orders=tuple(permutations(rest))
    tri=triples(range(n))
    checked=0
    for directions in product((-1,0,1),repeat=len(pairs(rest))):
        constraints=[]
        for (a,b),d in zip(pairs(rest),directions):
            if d==1: constraints.append((a,b))
            if d==-1: constraints.append((b,a))
        legal=[p for p in all_orders
               if all(p.index(a)<p.index(b) for a,b in constraints)]
        if not legal: continue
        checked+=1
        assert len({tvalue((0,)+p,tri) for p in legal})==len(legal)
    assert checked==543
    gated=[(0,)+p for p in all_orders if p.index(1)<p.index(2)]
    assert len(gated)==len({tvalue(p,tri) for p in gated})==12
    print("P39_F_PREFIX_CHECKPOINT_POSETS n=5 dags=543 "
          "source_equal_right_profiles=12 min_bits=4 PASS")




def sparse_owner_cycle_court():
    """Sparse triple questions can have unbounded minimal inconsistency.

    All questions contain anchor edit 0. After cyclic rotation to start at 0,
    each ternary parity becomes a required precedence edge. Directed cycles
    cannot be realized; removing any edge makes the system satisfiable.
    """
    # Minimal five-vertex example, checked against REAL permutations of this
    # synthetic alphabet rather than relying only on graph acyclicity.
    constraints = [
        ((0,1,2),0), ((0,2,3),0),
        ((0,3,4),0), ((0,1,4),1)
    ]
    orders=tuple(permutations(range(5)))
    def ok(order,selected):
        return all(tvalue(order,(t,))[0]==v for t,v in selected)
    assert not any(ok(order,constraints) for order in orders)
    assert all(any(ok(order,[x for j,x in enumerate(constraints)
                             if j!=removed]) for order in orders)
               for removed in range(4))
    for vs in combinations(range(5),4):
        local=[(t,v) for t,v in constraints if set(t)<=set(vs)]
        assert any(ok(order,local) for order in permutations(vs))
    print("P39_F_SPARSE_FIVE_VERTEX_LOCAL_GLOBAL_FAILURE "
          "triple_constraints=4 every_proper_subset_satisfiable PASS")

    # Directed k-cycle on k outer vertices, anchored by zero. Verify its
    # minimality and every proper vertex-restriction through k=9; the proof
    # works for arbitrary k>=3.
    def is_acyclic(nodes,edges):
        outgoing={v:[] for v in nodes}
        indeg={v:0 for v in nodes}
        for a,b in edges:
            outgoing[a].append(b)
            indeg[b]+=1
        todo=[v for v in nodes if indeg[v]==0]
        seen=0
        while todo:
            v=todo.pop()
            seen+=1
            for w in outgoing[v]:
                indeg[w]-=1
                if indeg[w]==0:
                    todo.append(w)
        return seen==len(nodes)
    for k in range(3,10):
        outer=tuple(range(1,k+1))
        edges=[(i,i+1) for i in range(1,k)]+[(k,1)]
        assert not is_acyclic(outer,edges)
        for j in range(k):
            assert is_acyclic(outer,[x for m,x in enumerate(edges) if m!=j])
        for mask in range(1,(1<<(k+1))-1):
            chosen={v for v in range(k+1) if mask>>v&1}
            restricted=[(a,b) for a,b in edges
                        if 0 in chosen and a in chosen and b in chosen]
            assert is_acyclic(outer,restricted)
        print(f"P39_F_UNBOUNDED_SPARSE_CYCLE k={k} "
              "all_proper_vertex_restrictions_satisfiable PASS")

if __name__=="__main__":
    parity_court()
    mixed_court()
    adaptive_court()
    invariant_court()
    sparse_owner_cycle_court()
    print("P39_MATH_F_PURE_THEORY_COURT_PASS_NO_NATIVE_GO")
