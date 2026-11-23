"""Finite evidence atlas demonstration. Standard library only. Not empirical software-design evidence."""
from dataclasses import dataclass
from fractions import Fraction
from itertools import product

@dataclass(frozen=True)
class Evidence:
    support: bool = False
    defeat: bool = False

    def add(self, other):
        return Evidence(self.support or other.support, self.defeat or other.defeat)

    @property
    def status(self):
        return {(False,False):'NEITHER', (True,False):'SUPPORT',
                (False,True):'DEFEAT', (True,True):'BOTH'}[self.support,self.defeat]

def leq(x,y):
    return (not x.support or y.support) and (not x.defeat or y.defeat)

def meet(x,y):
    return Evidence(x.support and y.support, x.defeat and y.defeat)

def join(x,y):
    return x.add(y)

def cost(q,design):
    if not 0 <= q <= 1: raise ValueError('q out of [0,1]')
    return 4-2*q if design=='M' else 1+5*q if design=='S' else _unknown()

def _unknown():
    raise ValueError('unknown design')

def preference(q):
    m,s=cost(q,'M'),cost(q,'S')
    return 'M' if m<s else 'S' if s<m else 'TIE'

def gluable(left,right,global_admissible):
    if any(left[k]!=right[k] for k in set(left)&set(right)): return False
    return any(all(a.get(k)==v for k,v in left.items()) and
               all(a.get(k)==v for k,v in right.items()) for a in global_admissible)

def self_test():
    states=[Evidence(*x) for x in product((False,True),repeat=2)]
    for a,b,c in product(states,repeat=3):
        assert meet(a,b)==meet(b,a)
        assert join(a,b)==join(b,a)
        assert meet(a,join(a,b))==a
        assert join(a,meet(a,b))==a
        assert join(a,join(b,c))==join(join(a,b),c)
        assert leq(a,join(a,b))
    assert Evidence(True,False).add(Evidence(False,True)).status=='BOTH'
    assert preference(Fraction(0))=='S'
    assert preference(Fraction(3,7))=='TIE'
    assert preference(Fraction(1))=='M'
    assert preference(Fraction(3,7)-Fraction(1,1000))=='S'
    assert preference(Fraction(3,7)+Fraction(1,1000))=='M'
    admissible=[{'x':0,'y':0},{'x':1,'y':1}]
    assert not gluable({'x':0},{'y':1},admissible)
    assert gluable({'x':0},{'y':0},admissible)
    assert not gluable({'x':0},{'x':1},[{'x':0},{'x':1}])
    for q in [Fraction(-1,3),Fraction(4,3)]:
        try: cost(q,'M')
        except ValueError: pass
        else: raise AssertionError('invalid probability accepted')
    return {'tested_triples':len(states)**3,
            'crossover':'3/7','conflict':'BOTH','gluing':'PASS'}

if __name__=='__main__':
    print(self_test())
