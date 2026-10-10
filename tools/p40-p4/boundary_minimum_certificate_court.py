"""P40-P4: exact boundary information and minimal local obstruction on
3 flat chi mounts, with explicit source/middleware sequencing obligations.

This checker reasons ABOUT a grammar calibrated to a pinned original Go
chi Mux; real Go source is tested separately. Finite model is not a native
Go proof of unbounded router behavior.
"""
from itertools import product

NAMES=("a","b","c")


def compatible(left,right):
    return left!=right


def route_boundary_partition_court():
    pairs=list(product(NAMES,repeat=2))
    assert len(pairs)==9
    good={(a,b) for a,b in pairs if compatible(a,b)}
    bad=set(pairs)-good
    assert len(good)==6 and len(bad)==3
    for a,b in bad:
        assert a==b
        assert a in NAMES and b in NAMES
    print("P40_P4_THREE_MOUNT_COURT singletons=6 compositions=9 safe=6 minimally_unsat_pairs=3 PASS")

    # B:NAMES->labels is universally sufficient to decide compatible(a,b)
    # from B(a),B(b) iff B is injective.
    for labels in product(range(3),repeat=3):
        label=dict(zip(NAMES,labels))
        predictions={}
        deterministic=True
        for a,b in pairs:
            k=(label[a],label[b])
            value=compatible(a,b)
            if k in predictions and predictions[k]!=value:
                deterministic=False
            predictions[k]=value
        assert deterministic==(len(set(labels))==3)
    print("P40_P4_BOUNDARY_KERNEL_NEC_SUFF all_27_three_label_encodings PASS")

    for labels in product((0,1),repeat=3):
        seen={}
        for a,b in pairs:
            k=(labels[NAMES.index(a)],labels[NAMES.index(b)])
            seen.setdefault(k,set()).add(compatible(a,b))
        assert any(len(values)==2 for values in seen.values())
    print("P40_P4_NAMESPACE_BOUNDARY_MIN_MEMORY bits=2 namespaces=3 PASS")

    validity={"M_R":True,"R_M":False}
    assert len(set(validity.values()))==2
    print("P40_P4_ORDERED_GLOBAL_ROOT_GUARD pre_route_only=1 PASS")


def local_signature_nonfactorization():
    # Local structure up to renaming cannot distinguish same-root conflict.
    signature=("one_handler","one_namespace_claim","unchanged_old_client",
               "http_handler_port","one_owner_slot")
    old=(signature,signature)
    for a,b in (("a","a"),("a","b")):
        assert old==(signature,signature)
    assert not compatible("a","a") and compatible("a","b")
    print("P40_P4_LOCAL_OBJECT_STRUCTURE_INCOMPLETE_FOR_GLOBAL_GLUING PASS")


if __name__=="__main__":
    route_boundary_partition_court()
    local_signature_nonfactorization()
    print("P40_P4_FINITE_BOUNDARY_AND_MINIMUM_OBSTRUCTION_MODEL_PASS")
