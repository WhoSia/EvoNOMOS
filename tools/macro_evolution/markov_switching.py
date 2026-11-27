"""Exact finite stationary-policy check of a conditional macro switching model."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

STATES = list(product(range(2), repeat=2))  # (old design, observed demand)
POLICIES = list(product(range(2), repeat=4))  # new design per state

def solve(a):
    n=len(a)
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j])
        a[j],a[k]=a[k],a[j]
        x=a[j][j]; a[j]=[v/x for v in a[j]]
        for i in range(n):
            if i!=j:
                x=a[i][j]; a[i]=[v-x*w for v,w in zip(a[i],a[j])]
    return [row[-1] for row in a]

def policy_value(p,g,k,pi):
    a=[]
    for i,(old,demand) in enumerate(STATES):
        new=pi[i]; row=[F(i==j) for j in range(4)]
        for nd,prob in ((demand,1-p),(1-demand,p)):
            row[STATES.index((new,nd))]-=g*prob
        a.append(row+[k*(new!=old)+F(new!=demand)])
    return solve(a)

def optimal(p,g,k):
    values=[policy_value(p,g,k,pi) for pi in POLICIES]
    return [min(v[i] for v in values) for i in range(4)]

def analytic(p,g,k):
    d=min(k,1/(1-g*(1-2*p)))
    m=g*p*d/(1-g)
    return [m+(old!=demand)*d for old,demand in STATES]

def main():
    rows=[]; ties=0
    for p,g,k in product([F(i,10) for i in range(11)], [F(1,10),F(1,2),F(9,10),F(99,100)], [F(0),F(1,4),F(1,2),F(1),F(2),F(4),F(10)]):
        v=optimal(p,g,k); pred=analytic(p,g,k)
        assert v==pred,(p,g,k,v,pred)
        cutoff=1/(1-g*(1-2*p)); ties+=k==cutoff
        avg=sum(v)/4; static=1/(2*(1-g))
        assert avg==min(static,k*(F(1,2)+g*p/(1-g)))
        rows.append(dict(p=str(p),gamma=str(g),k=str(k),switch_cutoff=str(cutoff),flexible=str(avg),fixed=str(static),max_investment=str(static-avg)))
    examples=[]
    for p in [F(1,10),F(9,10)]:
        g=F(9,10); k=F(1); I=F(1); value=sum(optimal(p,g,k))/4
        static=1/(2*(1-g));examples.append(dict(p=str(p),flexible_with_investment=str(value+I),fixed=str(static),net_benefit=str(static-value-I)))
    # Explicit exact ties beyond the original grid.
    for p in [F(i,10) for i in range(11)]:
        g=F(9,10); k=1/(1-g*(1-2*p));assert optimal(p,g,k)==analytic(p,g,k)
    result=dict(grid_cases=len(rows),policy_evaluations=len(rows)*16,grid_ties=ties,extra_ties=11,examples=examples,rows=rows,scope='Exogenous symmetric demand, fully observed, two feasible designs, equal service costs, unit mismatch, no hard forbidden edits; no measured source costs.')
    Path(__file__).with_name('markov_switching_result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
