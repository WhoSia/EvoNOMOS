"""Native two-step histories with two distinct tags; optional subclass only."""
import json
from itertools import product
from worlds import ALL,materialize,load,classes,selected,KEYS
from observations import FIXTURES,OPERATIONS,signature

OPS=tuple(k for k in OPERATIONS if k not in ('date_add','reverse_date_add'))

def main():
    rows=[]; mismatch=0; core_mismatch=0
    for mask in range(ALL+1):
        B=load(materialize(mask,True)); C=classes(B,True)['optional']
        counts={'pairs':0,'retained':0,'collision':0,'irreversible_after_later_hook':0,'prediction_mismatches':0,'core_mismatches':0}
        for kw,a,b in product(FIXTURES,OPS,OPS):
            x,y=(C(**kw,tag=t) for t in ('A','B'))
            x,y=(OPERATIONS[a](z,B) for z in (x,y))
            first=(x.tag,y.tag)
            x,y=(OPERATIONS[b](z,B) for z in (x,y))
            last=(x.tag,y.tag)
            ref=OPERATIONS[b](OPERATIONS[a](B(**kw),B),B)
            core=signature(x,B)==signature(y,B)==signature(ref,B)
            retained=last==('A','B')
            collision=last==('DEFAULT','DEFAULT')
            want=selected(mask,a) and selected(mask,b)
            counts['pairs']+=1;counts['retained']+=retained;counts['collision']+=collision
            counts['irreversible_after_later_hook']+=first==('DEFAULT','DEFAULT') and selected(mask,b) and collision
            counts['prediction_mismatches']+=not (retained if want else collision)
            counts['core_mismatches']+=not core
        rows.append({'mask':mask,**counts})
        mismatch+=counts['prediction_mismatches'];core_mismatch+=counts['core_mismatches']
    result={'sites':KEYS,'operations':OPS,'worlds':len(rows),'paired_histories':sum(r['pairs'] for r in rows),'retained':sum(r['retained'] for r in rows),'collisions':sum(r['collision'] for r in rows),'irreversible_after_later_hook':sum(r['irreversible_after_later_hook'] for r in rows),'mismatches':mismatch,'core_mismatches':core_mismatch,'rows':rows}
    print(json.dumps(result,indent=2));assert mismatch==core_mismatch==0

if __name__=='__main__':main()
