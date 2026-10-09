"""P37 MATH-A: exhaustive finite repair-graph checks. Purely classical finite theorems."""
from itertools import product

def may(n, edges, accept, start):
    visited={start}
    stack=[start]
    while stack:
        u=stack.pop()
        if u in accept:
            return True
        for v in range(n):
            if (u,v) in edges and v not in visited:
                visited.add(v)
                stack.append(v)
    return False

def quotient_factorizes(n,edges,accept,q):
    outcome=[may(n,edges,accept,i) for i in range(n)]
    return all(q[i]!=q[j] or outcome[i]==outcome[j]
               for i in range(n) for j in range(n))

def no_go_obstruction():
    n=3
    edges={(0,2)}
    accept={2}
    q=(0,0,1)
    assert may(n,edges,accept,0)
    assert not may(n,edges,accept,1)
    assert not quotient_factorizes(n,edges,accept,q)

def path_count_negative():
    # Three separate graphs, paths differ but same May at start.
    one=(3,{(0,1)}, {1})
    two=(3,{(0,1),(0,2)}, {1,2})
    assert may(*one,0)==may(*two,0)==True

def exhaustive_small_graphs():
    checked=0
    counterexamples=0
    n=3
    possible=[(i,j) for i in range(n) for j in range(n) if i!=j]
    # Enumerate all directed graphs, accept subsets, present two-valued quotients.
    for e_bits in product([False,True],repeat=len(possible)):
        edges={e for e,yes in zip(possible,e_bits) if yes}
        for a_bits in product([False,True],repeat=n):
            accept={i for i,yes in enumerate(a_bits) if yes}
            for q in product([0,1],repeat=n):
                predicted=quotient_factorizes(n,edges,accept,q)
                # Directly construct a q-observer if and only if values are constant.
                truth=[may(n,edges,accept,i) for i in range(n)]
                lift={}
                feasible=True
                for i,a in enumerate(q):
                    if a in lift and lift[a]!=truth[i]:
                        feasible=False
                    lift[a]=truth[i]
                assert predicted==feasible
                checked+=1
                if not predicted:counterexamples+=1
    assert checked==64*8*8==4096
    assert counterexamples>0
    return checked,counterexamples

def forward_simulation_and_nonconverse():
    # Source a no edges, nonaccepting; target x -> accepting y.
    source=(1,set(),set())
    target=(2,{(0,1)},{1})
    assert not may(*source,0)
    assert may(*target,0)
    # Forward edge condition on mapping h(a)=x vacuous; converse fails.

def main():
    no_go_obstruction()
    path_count_negative()
    forward_simulation_and_nonconverse()
    checked,negative=exhaustive_small_graphs()
    print(f"P37_MATH_A_FINITE_CLASSICAL_PASS cases={checked} nonfactorizing={negative}")
    print("No new-law inference: classical quotient and directed simulation only.")

if __name__=="__main__":
    main()
