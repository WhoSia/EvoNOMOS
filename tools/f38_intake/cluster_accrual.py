"""Planning sensitivity for distinct repository accrual, not empirical rates."""
from math import comb, exp, log1p


def tail(n, k, p):
    return sum(comb(n, i) * p**i * (1-p)**(n-i) for i in range(k, n+1))


def target_probability(n, k, confidence):
    assert 0 < k <= n and 0 < confidence < 1
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo+hi)/2
        if tail(n, k, mid) < confidence:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def report(n=30, k=23, annual_issues=20, confidence=.8):
    p = target_probability(n, k, confidence)
    result = []
    for h in (.1, .03):
        for q in (1., .5):
            rate = annual_issues*h*q
            p14 = 1-exp(-rate*14/365)
            result.append(dict(h=h, q=q,
                expected_distinct_14days=n*p14,
                years_for_expected_k=(-log1p(-k/n)/rate if k<n else float('inf')),
                years_for_target_accrual_probability=-log1p(-p)/rate,
                probability_k_in_14days=tail(n,k,p14)))
    return dict(n=n,k=k,annual_issues=annual_issues,confidence=confidence,
                target_per_repo_probability=p,scenarios=result,
                scope='homogeneous independent Poisson arrivals and thinning; one decisive episode per repository; hypothetical, not measured, and accrual probability is not test power')


if __name__ == '__main__':
    import json
    print(json.dumps(report(),indent=2))
