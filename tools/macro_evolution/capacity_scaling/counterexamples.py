"""Exact boundary witnesses for homogeneous count quotient and independent fluid limit."""
from fractions import Fraction as F
import json
from pathlib import Path

def solve(P,c,g):
    n=len(c)
    A=[[F(i==j)-g*P[i][j] for j in range(n)]+[c[i]] for i in range(n)]
    for i in range(n):
        j=next(j for j in range(i,n) if A[j][i])
        A[i],A[j]=A[j],A[i]
        v=A[i][i];A[i]=[x/v for x in A[i]]
        for j in range(n):
            if j!=i:
                v=A[j][i];A[j]=[x-v*y for x,y in zip(A[j],A[i])]
    return [a[-1] for a in A]

def main():
    g=F(9,10);r=F(1,4);q=F(1,4);alpha=F(1,2)
    # q1=0, q2=1, capacity one: same count, different lawful repair effects.
    # Repair first module if bad, never repair second; check all actions.
    S=[(0,0),(0,1),(1,0),(1,1)]
    def step(x,a):return (x[0]*(1-a[0]),1)
    def cost(x,a):return F(sum(x))+r*sum(a)
    A=[(0,0),(1,0),(0,1)]
    pi=[(x[0],0) for x in S]
    P=[[F(y==step(x,a)) for y in S] for x,a in zip(S,pi)]
    v=solve(P,[cost(x,a) for x,a in zip(S,pi)],g)
    assert all(v[i]==min(cost(x,a)+g*v[S.index(step(x,a))] for a in A) for i,x in enumerate(S))
    assert v[1]!=v[2]
    # A common shock, independent of past and actions, sends all susceptible
    # modules to bad together; exact normalized states for every even n.
    Y=[F(0),F(1,2),F(1)]
    b=[min(y,alpha) for y in Y]
    P=[[F(0) for _ in Y] for _ in Y]
    for i,y in enumerate(Y):
        P[i][Y.index(y-b[i])]+=1-q;P[i][2]+=q
    u=solve(P,[y+r*z for y,z in zip(Y,b)],g)
    # Independent-transition fluid from y0=0 reaches q at t=1, stays q.
    fluid=g*q*(1+r)/(1-g)
    assert u[0]>fluid
    result={'heterogeneous':{'states':S,'value':list(map(str,v)),'same_count_values':[str(v[1]),str(v[2])]},'common_shock':{'normalized_states':list(map(str,Y)),'value':list(map(str,u)),'fluid_independent':str(fluid),'gap':str(u[0]-fluid),'scope':'every even n; fixed alpha=1/2; common-shock greedy policy (monotone coupling extends to common Bernoulli shock); not independent-binomial fluid model'}}
    Path(__file__).with_name('counterexamples_result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
