"""Exact conditional macro composition calibration, not source evidence."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
S=list(product(range(2),repeat=2)); A=S; C=[a for a in A if sum(a)<=1]

def solve(P,c,g):
    n=len(c); m=[[F(i==j)-g*P[i][j] for j in range(n)]+[c[i]] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if m[k][j]);m[j],m[k]=m[k],m[j]
        z=m[j][j];m[j]=[v/z for v in m[j]]
        for i in range(n):
            if i!=j:
                z=m[i][j];m[i]=[v-z*w for v,w in zip(m[i],m[j])]
    return [r[-1] for r in m]

def local(x,a,q,r):
    p=q if x==0 or a else F(1)
    return x+r*a,[1-p,p]

def joint(x,a,q,r,mode):
    c1,p1=local(x[0],a[0],q,r);c2,p2=local(x[1],a[1],q,r)
    u,v=p1[1],p2[1]
    z={'lower':max(F(0),u+v-1),'independent':u*v,'upper':min(u,v)}[mode]
    P=[1-u-v+z,v-z,u-z,z]
    assert min(P)>=0 and sum(P)==1 and P[2]+P[3]==u and P[1]+P[3]==v
    return c1+c2,P

def dot(a,b):return sum(x*y for x,y in zip(a,b))

def opt(S,A,M,g):
    # Independent exhaustive stationary deterministic policy evaluation.
    vals=[]
    for pi in product(A,repeat=len(S)):
        rows=[M(x,a) for x,a in zip(S,pi)]
        vals.append(solve([p for c,p in rows],[c for c,p in rows],g))
    v=[min(w[i] for w in vals) for i in range(len(S))]
    pi=[]
    for i,x in enumerate(S):
        z=[(c+g*dot(p,v),a) for a in A for c,p in [M(x,a)]]
        best,a=min(z);assert best==v[i];pi.append(a)
    return v,pi

def main():
    rows=[];checks=0;positive_delayed=0;count=0
    for q,r,g in product([F(1,4),F(1,2),F(3,4)],[F(1,4),F(3,4)],[F(1,2),F(9,10)]):
        v,_=opt([0,1],[0,1],lambda x,a:local(x,a,q,r),g)
        W=[v[x]+v[y] for x,y in S]
        for mode in ('lower','independent','upper'):
            M=lambda x,a:joint(x,a,q,r,mode)
            def adv(x,a):
                i=S.index(x);c,p=M(x,a)
                z=c+g*dot(p,W)-W[i]
                parts=[]
                for j in range(2):
                    ci,pi=local(x[j],a[j],q,r);parts.append(ci+g*dot(pi,v)-v[x[j]])
                assert z==sum(parts) and min(parts)>=0
                return z
            for x in S:
                assert min(adv(x,a) for a in A)==0;checks+=1
            V,pi=opt(S,C,M,g);count+=len(C)**len(S)
            gap=[z-w for z,w in zip(V,W)];assert min(gap)>=0
            D,dpi=opt(S,C,lambda x,a:(adv(x,a),M(x,a)[1]),g);count+=len(C)**len(S)
            assert gap==D
            P=[M(x,a)[1] for x,a in zip(S,pi)]
            assert solve(P,[adv(x,a) for x,a in zip(S,pi)],g)==gap
            # Greatest controlled invariant set for zero loss.
            Z=set(range(len(S)))
            while True:
                N={i for i in Z if any(adv(S[i],a)==0 and all(not p or j in Z for j,p in enumerate(M(S[i],a)[1])) for a in C)}
                if N==Z:break
                Z=N
            assert Z=={i for i,z in enumerate(gap) if z==0}
            b=[min(adv(x,a) for a in C) for x in S]
            assert all(z>=w for z,w in zip(gap,b))
            greedy=[min(C,key=lambda a:(adv(x,a),a)) for x in S]
            GP=[M(x,a)[1] for x,a in zip(S,greedy)]
            upper=solve(GP,[adv(x,a) for x,a in zip(S,greedy)],g)
            assert all(lo<=hi for lo,hi in zip(gap,upper))
            positive_delayed+=b[0]==0 and gap[0]>0
            rows.append(dict(q=str(q),r=str(r),gamma=str(g),coupling=mode,W=list(map(str,W)),V=list(map(str,V)),gap=list(map(str,gap)),immediate=list(map(str,b)),greedy_upper=list(map(str,upper)),zero_states=sorted(Z),policy=pi))
    def get(q,r,g,mode):return next(x for x in rows if (x['q'],x['r'],x['gamma'],x['coupling'])==(q,r,g,mode))
    ex=[get('1/4','1/4','9/10',mode) for mode in ('lower','independent','upper')]
    result=dict(grid_cases=len(rows),joint_policy_evaluations=count,full_product_bellman_checks=checks,delayed_positive_cases=positive_delayed,example=ex,rows=rows,scope='Conditional additive costs, invariant local transition marginals, state-dependent joint feasibility; no actual labor or software source calibration.')
    Path(__file__).with_name('compositional_gap_result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
