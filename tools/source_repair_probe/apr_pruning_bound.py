"""Exact finite-pool pruning bound, no actual certificate efficacy claim."""
import csv, itertools, json
from fractions import Fraction as F
from pathlib import Path
from math import factorial

def cost(order):
    for i, x in enumerate(order,1):
        if x:return i
    return len(order)

def expectation(n,k):
    if n==0:return F(0)
    if k==0:return F(n)
    return F(n+1,k+1)

def exhaustive(n,k):
    # enumerate subsets of success positions instead of duplicate permutations
    costs=[]
    for good in itertools.combinations(range(n),k):
        a=[i in good for i in range(n)]
        costs.append(cost(a))
    return F(sum(costs),len(costs))
checks=0
for n in range(1,11):
    for k in range(n+1):
        for m in range(n-k+1):
            assert exhaustive(n,k)-exhaustive(n-m,k)==F(m,k+1)
            checks+=1
rows=list(csv.DictReader(Path(__file__).with_name('preprocessed.csv').open()))
rank=F(0);prune=F(0);zeros=0;zero_count=0;positive_count=0
for r in rows:
    k,i,u,n=map(int,(r['correct'],r['incorrect'],r['unknown'],r['total']))
    assert u==0 and n==i+k
    rank+=F(i,k+1) if k else 0
    prune+=F(i,k+1)
    if not k:zeros+=n;zero_count+=1
    else:positive_count+=1
assert prune-rank==zeros
out={'finite_identity_checks':checks,'pools':len(rows),'zero_pools':zero_count,'zero_pool_candidates':zeros,'positive_pools':positive_count,'ranking_upper_bound':str(rank),'perfect_sound_pruning_upper_bound':str(prune),'pruning_overhead_break_even_per_pool':str(prune/len(rows)),'assumptions':'fixed finite pool; exact labels; no false exclusions; uniform random order; equal manual review cost; retained good candidates still need review; certificate cost and construction not measured; K=0 requires sound exclusion of every candidate to conclude no solution within pool; no external completeness claim'}
print(json.dumps(out,indent=2))
