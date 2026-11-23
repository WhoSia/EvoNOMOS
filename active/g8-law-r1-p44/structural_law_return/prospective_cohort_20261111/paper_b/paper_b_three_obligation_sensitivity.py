"""Exact authored third-obligation sensitivity, not an empirical software cohort.

E: new errata required; B: book prefix protected;
C: another independently binding, patch-violated constraint.
Acceptance iff none binds. Signed 0=no,1=yes,None=undisclosed.
"""
from itertools import product

FIELDS=("errata","book_prefix","additional_obligation")
VALUES=(False,True,None)
VERDICTS=("ACCEPT","REJECT","HOLD")

def compatible(evidence):
    if len(evidence)!=3:
        raise ValueError("Need three fields")
    if any(value not in VALUES or (value is not None and type(value) is not bool)
           for value in evidence):
        raise ValueError("Evidence values must be bool or None")
    return tuple(world for world in product((False,True),repeat=3)
                 if all(value is None or world[i]==value
                        for i,value in enumerate(evidence)))

def verdict(evidence):
    worlds=compatible(evidence)
    if not worlds:
        raise AssertionError("Every signed three-field evidence has a world")
    accepts=tuple(not any(world) for world in worlds)
    if all(accepts): return "ACCEPT"
    if not any(accepts): return "REJECT"
    return "HOLD"

def all_disclosures():
    return tuple(product(VALUES,repeat=3))

def statistics():
    return {decision:sum(verdict(evidence)==decision for evidence in all_disclosures())
            for decision in VERDICTS}

def countermodels(evidence):
    worlds=compatible(evidence)
    accepting=next((w for w in worlds if not any(w)),None)
    rejecting=next((w for w in worlds if any(w)),None)
    return (accepting,rejecting) if accepting is not None and rejecting is not None else None

def project_original_two_facts():
    """When C is explicitly false, recover the earlier nine-state decision table."""
    return tuple((e,b,verdict((e,b,False)))
                 for e,b in product(VALUES,repeat=2))

if __name__=="__main__":
    assert statistics()=={"ACCEPT":1,"REJECT":19,"HOLD":7}
    print("authored 3-obligation sensitivity: 8 worlds; 27 disclosure states; 1/19/7")
