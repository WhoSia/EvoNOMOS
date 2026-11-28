"""Mixed-operand order is a separate diagnostic, not included in the fitted contract."""
import json
from worlds import ALL,materialize,load,classes
from observations import signature

def main():
    rows=[]
    for mask,H,T in [(0,False,False),(ALL,True,True)]:
        B=load(materialize(mask,H));C=classes(B,T)['optional']
        for field,a,b in [('day',10,20),('month',1,2),('year',2024,2025),('hour',3,8)]:
            expected=B(**{field:a})+B(**{field:b})
            for order in ('base_left','sub_left'):
                x=B(**{field:a})+C(**{field:b},tag='KEEP') if order=='base_left' else C(**{field:a},tag='KEEP')+B(**{field:b})
                rows.append({'mask':mask,'field':field,'order':order,'numeric_equal':signature(x,B)==signature(expected,B),'value':getattr(x,field),'expected':getattr(expected,field),'subtype':type(x)is C,'tag':getattr(x,'tag',None)})
    print(json.dumps({'rows':rows},indent=2))

if __name__=='__main__':main()
