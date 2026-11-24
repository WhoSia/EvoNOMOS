"""Synthetic two-world sequential owner-veto game with public signals.
Outside option zero for both. A pays proposal cost 1 even if rejected.
Accepted net A gains already include that cost. Equal prior probabilities.
No empirical or source-native cost interpretation.
"""
from fractions import Fraction
from itertools import product
from collections import Counter


def play(a, b, cells):
    # Backward induction: B accepts iff conditional gain is strictly positive.
    # If B rejects, A strictly prefers not to propose (cost 1).
    chosen = []
    for cell in cells:
        accept = sum(b[i] for i in cell) > 0
        propose = accept and sum(a[i] for i in cell) > 0
        chosen.extend(cell if propose else ())
    return (tuple(sorted(chosen)), Fraction(sum(a[i]+b[i] for i in chosen),2))


def planner(a, b, cells):
    chosen = [i for cell in cells if sum(a[i]+b[i] for i in cell)>0 for i in cell]
    return Fraction(sum(a[i]+b[i] for i in chosen),2)


def main():
    pooled = ((0,1),)
    full = ((0,),(1,))
    counts = Counter()
    for a0,a1,b0,b1 in product(range(-3,4),repeat=4):
        a,b = (a0,a1),(b0,b1)
        _,v0 = play(a,b,pooled)
        _,v1 = play(a,b,full)
        assert planner(a,b,full) >= planner(a,b,pooled)
        counts['grid_cases'] += 1
        counts['strategic_welfare_increases'] += v1>v0
        counts['strategic_welfare_decreases'] += v1<v0
        counts['strategic_welfare_ties'] += v1==v0
    a,b = (2,2),(3,-1)
    assert play(a,b,pooled) == ((0,1),Fraction(3))
    assert play(a,b,full) == ((0,),Fraction(5,2))
    assert planner(a,b,pooled)==planner(a,b,full)==3
    a,b = (2,2),(1,-3)
    assert play(a,b,pooled)[1]==0 and play(a,b,full)[1]==Fraction(3,2)
    print(dict(counts))

if __name__ == '__main__':
    main()
