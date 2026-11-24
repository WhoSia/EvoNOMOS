"""Synthetic R97: ex-post strict participation under public transfer menus.
No source-native or human-cost claims. Intervals are open; integer endpoints.
"""
from itertools import combinations
from fractions import Fraction


def candidates(intervals):
    endpoints = sorted({x for interval in intervals for x in interval})
    return [(a+b)/2 for a,b in zip(endpoints,endpoints[1:])]


def exact(intervals):
    if any(a>=b for a,b in intervals):
        return None
    points = candidates(intervals)
    masks = [sum(1<<i for i,(a,b) in enumerate(intervals) if a<t<b) for t in points]
    full = (1<<len(intervals))-1
    dp = {0:0}
    for mask in masks:
        for old,k in list(dp.items()):
            new = old|mask
            dp[new] = min(dp.get(new,len(intervals)+1),k+1)
    return dp[full]


def greedy(intervals):
    if any(a>=b for a,b in intervals):
        return None
    remaining = list(intervals)
    count = 0
    while remaining:
        _,right = min(remaining,key=lambda x:x[1])
        compatible = [(a,b) for a,b in remaining if a<right]
        left = max(a for a,b in compatible)
        t = (left+right)/2
        remaining = [(a,b) for a,b in remaining if not a<t<b]
        count += 1
    return count


def main():
    universe = list(combinations(map(Fraction,range(5)),2))
    checks = 0
    for mask in range(1<<len(universe)):
        family = [q for i,q in enumerate(universe) if mask>>i&1]
        assert exact(family)==greedy(family)
        checks += 1
    assert exact([(Fraction(1),Fraction(1))]) is None
    # Equal aggregate gains, opposite distribution: local=(5,5), p=1.
    # Shared=(0,6) and (6,0). Transfer t from A to B; intervals (1,4),(-5,-2).
    worlds = [(Fraction(1),Fraction(4)),(Fraction(-5),Fraction(-2))]
    assert exact(worlds)==2
    print({'families':checks,'invalid_interval_rejected':True,'example_min_public_messages':exact(worlds)})

if __name__=='__main__':
    main()
