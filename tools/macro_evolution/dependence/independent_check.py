from fractions import Fraction as F
from math import comb
import numpy as np
from scipy.optimize import linprog
import json
from pathlib import Path

def mix(n, atoms):
    return [sum(w*comb(n,k)*t**k*(1-t)**(n-k) for t,w in atoms) for k in range(n+1)]
def main():
    A=[(F(1,4),F(1,2)),(F(3,4),F(1,2))]
    B=[(F(0),F(1,8)),(F(1,2),F(3,4)),(F(1),F(1,8))]
    bounds=[(F(1,20),F(13,120)),(F(1,32),F(113,1120)),(F(7,320),F(163,1760)),(F(11,640),F(327,3680)),(F(19,1280),F(597,6880))]
    rows=[]
    for j,n in enumerate([5,10,20,40,80,160]):
        overflow=[]
        for law in [A,B]:
            p=mix(n,law)
            assert sum(p)==1
            mean=sum(F(k,n)*w for k,w in enumerate(p))
            var=sum((F(k,n)-mean)**2*w for k,w in enumerate(p))
            assert mean==F(1,2) and var==F(n+3,16*n)
            overflow.append(sum(max(F(0),F(k,n)-F(3,5))*w for k,w in enumerate(p)))
        assert overflow[0]>F(1,16)
        assert (overflow[1]>F(1,16))==(n<=10)
        row={'n':n,'overflow':[str(x) for x in overflow]}
        if j<len(bounds):
            y=np.arange(n+1,dtype=float)/n
            M=np.vstack([np.ones(n+1),y,y*y])
            rhs=[1,.5,float(F(1,4)+F(n+3,16*n))]
            c=np.maximum(y-.6,0)
            lo=linprog(c,A_eq=M,b_eq=rhs,bounds=(0,None),method='highs')
            hi=linprog(-c,A_eq=M,b_eq=rhs,bounds=(0,None),method='highs')
            assert lo.success and hi.success
            err=max(abs(lo.fun-float(bounds[j][0])),abs(-hi.fun-float(bounds[j][1])))
            assert err<1e-8
            row.update(lp_bounds=[lo.fun,-hi.fun],error=err)
        rows.append(row)
    Path(__file__).with_name('independent_result.json').write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps(rows,indent=2))
if __name__=='__main__':main()
