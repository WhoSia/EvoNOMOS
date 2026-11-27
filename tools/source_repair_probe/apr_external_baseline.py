"""External APR aggregate reanalysis. No prospective or labor inference."""
import csv, hashlib, json, sys
from pathlib import Path
from math import comb
from fractions import Fraction as F
from statistics import median
from collections import Counter
PIN='b539da0a433d49d4d35e92ab95cb1b5a69b7921f'

def quantile(n,k,p):
    if not k:return None
    for j in range(1,n+1):
        if F(comb(n,j)-comb(n-k,j),comb(n,j))>=p:return j
    raise AssertionError('quantile')

def expected(n,k):
    if not k:return F(n)
    # Direct distribution of the first correct draw; independent of closed form.
    z=F(sum(t*comb(n-t,k-1) for t in range(1,n-k+2)),comb(n,k))
    assert z==F(n+1,k+1)
    return z

def analyze(raw):
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==PIN
    rd=csv.DictReader(raw.decode().splitlines());assert rd.fieldnames==['paper','Tool','Bug','correct','incorrect','unknown','total']
    rows=[]
    for r in rd:
        k,i,u,n=(int(r[x]) for x in ('correct','incorrect','unknown','total'))
        assert r['paper']=='submission' and min(k,i,u)>=0 and n==k+i+u and n>0
        assert u==0, 'Unknown label not treated as negative'
        e=expected(n,k); perfect=1 if k else n
        rows.append(dict(tool=r['Tool'],bug=r['Bug'],k=k,i=i,u=u,n=n,e=e,perfect=perfect,saving=e-perfect))
    assert len({(r['tool'],r['bug']) for r in rows})==len(rows)
    out={'blob':PIN,'input_sha256':hashlib.sha256(raw).hexdigest(),'rows':len(rows),'bugs':len({r['bug'] for r in rows}),'tools':len({r['tool'] for r in rows}),'patches':sum(r['n'] for r in rows),'pool_distribution':dict(Counter('zero_correct' if not r['k'] else 'all_correct' if r['k']==r['n'] else 'mixed' for r in rows)),'median_n':median([r['n'] for r in rows]),'mean_n':F(sum(r['n'] for r in rows),len(rows)),'total_random':sum(r['e'] for r in rows),'total_perfect':sum(r['perfect'] for r in rows),'total_saving':sum(r['saving'] for r in rows),'per_tool':{},'overhead':[],'threshold_policy':[]}
    for tool in sorted({r['tool'] for r in rows}):
        rs=[r for r in rows if r['tool']==tool];pos=[r for r in rs if r['k']]
        qs=[[quantile(r['n'],r['k'],F(p,100)) for r in pos] for p in (80,90,100)]
        out['per_tool'][tool]={'recorded':len(rs),'positive':len(pos),'median':[median(x) if x else None for x in qs],'max':[max(x) if x else None for x in qs]}
    for h in [F(0),F(1,4),F(1,2),F(1),F(2),F(5),F(10)]:
        out['overhead'].append({'h':h,'profitable_perfect_rank_pools':sum(r['saving']>h for r in rows),'ties':sum(r['saving']==h for r in rows),'always_rank_net':sum(r['saving']-h for r in rows),'oracle_gate_net':sum(max(F(0),r['saving']-h) for r in rows)})
        # Size-only routing uses visible N, not future correctness labels. Ranking still assumed perfect.
        for t in (1,2,3,5,10):
            eligible=[r for r in rows if r['n']>=t]
            out['threshold_policy'].append({'h':h,'min_n':t,'selected':len(eligible),'mixed':sum(r['saving']>0 for r in eligible),'net_upper_bound':sum(r['saving']-h for r in eligible)})
    out['top_savings']=[{k:v for k,v in r.items()} for r in sorted(rows,key=lambda r:r['saving'],reverse=True)[:8]]
    return out

def encode(x):
    if isinstance(x,F):return {'fraction':str(x),'float':float(x)}
    raise TypeError(type(x))

if __name__=='__main__':
    p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('preprocessed.csv')
    result=analyze(p.read_bytes())
    print(json.dumps(result,default=encode,indent=2))
