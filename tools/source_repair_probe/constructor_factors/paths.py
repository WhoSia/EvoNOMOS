"""Exact monotone edit order count under protected native states and rights."""
import json
from math import factorial
from pathlib import Path
from worlds import ALL,KEYS

N=len(KEYS)+2
H=1<<len(KEYS);T=H<<1;GOAL=H|T|ALL

def index(r):return r['mask']|(H if r['H'] else 0)|(T if r['T'] else 0)

def path_count(safe,rights):
    ways={0:1}
    for s in range(GOAL+1):
        if s not in ways:continue
        for i in range(N):
            bit=1<<i
            if s&bit or not rights&bit:continue
            nxt=s|bit
            if nxt in safe:ways[nxt]=ways.get(nxt,0)+ways[s]
    return ways.get(GOAL,0)

def main():
    rows=json.loads(Path(__file__).with_name('results.json').read_text())['rows']
    native={index(r) for r in rows if r['protected_failures']==0}
    classical={s for s in range(GOAL+1) if not s&ALL or s&H}
    assert native==classical
    out=[]
    for rights in range(GOAL+1):
        a=path_count(native,rights);b=path_count(classical,rights)
        assert a==b
        out.append({'rights':rights,'shortest_orders':a})
    assert out[-1]['shortest_orders']==factorial(N)//(len(KEYS)+1)
    print(json.dumps({'rights_sets':len(out),'reachable':sum(bool(r['shortest_orders']) for r in out),'full_rights_orders':out[-1]['shortest_orders'],'distance':N,'classical_tie':True,'rows':out},indent=2))

if __name__=='__main__':main()
