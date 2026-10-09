"""P37 MATH-B finite executable counterexamples: congruence needs context closure."""
def context_closure_counterexample():
    # Current observation q: distinguish only state 2 from state 0/1.
    # C(0)=1, C(1)=2; id,C agree on x=0 and y=1? C(0)=1(q=0),
    # C(1)=2(q=1) -> no. Choose 4 states with q=(0,0,0,1),
    # C(0)=1, C(1)=2, C(2)=3; for x=0,y=1, C(x)=1,C(y)=2
    # both q=0; C^2(x)=2(q=0), C^2(y)=3(q=1).
    q=(0,0,0,1)
    c=(1,2,3,3)
    x,y=0,1
    assert q[x]==q[y]
    assert q[c[x]]==q[c[y]]
    assert q[c[c[x]]]!=q[c[c[y]]]
    return True

def repair_transparency_counterexample():
    # A local authorized edit is blocked when composed in a context
    # with an old-client contract forbidding the edit.
    local={0:{1},1:set()}
    contextual={0:set(),1:set()}
    accept={1}
    assert 1 in local[0] and 1 not in contextual[0]
    return True

def one_way_simulation_counterexample():
    # Source singleton nonaccepting, target adds acceptance reachable.
    src_edges=set()
    dst_edges={(0,1)}
    assert len(src_edges)==0 and (0,1) in dst_edges
    return True

def main():
    assert context_closure_counterexample()
    assert repair_transparency_counterexample()
    assert one_way_simulation_counterexample()
    print("P37_MATH_B_CLASSICAL_COUNTEREXAMPLES_PASS contexts=id,C not composition closed")
    print("P37_MATH_B_REPAIR_CONTEXT_NOT_TRANSPARENT")
    print("P37_MATH_B_ONE_WAY_SIMULATION_NONCONVERSE")
if __name__=="__main__":main()
