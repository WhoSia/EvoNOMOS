"""Exact finite compositional repair-policy model. NOT a source Go verifier."""
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product

@dataclass(frozen=True)
class Module:
    states: tuple
    actions: tuple
    probabilities: tuple
    observations: tuple
    feasible: tuple
    losses: tuple
    def check(self):
        n,k=len(self.states),len(self.actions)
        if not n or not k or len(set(self.states))!=n or len(set(self.actions))!=k:
            raise ValueError("invalid state/action names")
        if any(len(x)!=n for x in (self.probabilities,self.observations,self.feasible,self.losses)):
            raise ValueError("state shape mismatch")
        if any(p<=0 for p in self.probabilities) or sum(self.probabilities,Q())!=1:
            raise ValueError("probabilities must be positive, sum 1")
        if any(not s or not set(s).issubset(self.actions) for s in self.feasible):
            raise ValueError("empty or invalid state permission")
        if any(len(row)!=k for row in self.losses):
            raise ValueError("loss/action mismatch")
        return self

def risk(m):
    m.check()
    total=Q()
    for z in set(m.observations):
        ids=[i for i,t in enumerate(m.observations) if z==t]
        options=set(m.actions)
        for i in ids: options.intersection_update(m.feasible[i])
        if not options:return None
        total+=min(sum((m.probabilities[i]*m.losses[i][m.actions.index(a)] for i in ids),Q())
                   for a in options)
    return total

def oracle(m):
    m.check()
    return sum((m.probabilities[i]*min(m.losses[i][m.actions.index(a)] for a in m.feasible[i])
                for i in range(len(m.states))),Q())

def joint(a,b,joint_p=None,shared_actions=None,extra=None):
    """Actual global policy sees BOTH observations, must obey all fiber permissions."""
    a.check();b.check()
    ids=list(product(range(len(a.states)),range(len(b.states))))
    p={ij:(a.probabilities[ij[0]]*b.probabilities[ij[1]] if joint_p is None
           else joint_p.get(ij,Q())) for ij in ids}
    if any(w<0 for w in p.values()) or sum(p.values(),Q())!=1:
        raise ValueError("invalid joint prior")
    actions=set(product(a.actions,b.actions))
    if shared_actions is not None:actions.intersection_update(shared_actions)
    def permitted(ij):
        i,j=ij
        return {pair for pair in actions if pair[0] in a.feasible[i] and pair[1] in b.feasible[j]}
    def cost(ij,act):
        i,j=ij;u,v=act
        return (a.losses[i][a.actions.index(u)]+b.losses[j][b.actions.index(v)]+
                (Q() if extra is None else extra.get((i,j,u,v),Q())))
    active=[ij for ij in ids if p[ij]>0]
    if any(not permitted(ij) for ij in active):
        return {"status":"STATE_WITHOUT_ALLOWED_ACTION","oracle":None,"risk":None}
    full=sum((p[ij]*min(cost(ij,x) for x in permitted(ij)) for ij in active),Q())
    fibers={}
    for ij in active:
        z=(a.observations[ij[0]],b.observations[ij[1]])
        fibers.setdefault(z,[]).append(ij)
    limited=Q()
    for group in fibers.values():
        commons=set(actions)
        for ij in group:commons.intersection_update(permitted(ij))
        if not commons:
            return {"status":"NO_UNIFORM_AUTHORIZED_ACTION","oracle":full,"risk":None}
        limited+=min(sum((p[ij]*cost(ij,x) for ij in group),Q()) for x in commons)
    return {"status":"FEASIBLE","oracle":full,"risk":limited,"regret":limited-full}

def binary(observations=("unknown","unknown"),feasible=None,losses=None):
    if feasible is None:feasible=(frozenset({"0","1"}),)*2
    if losses is None:losses=((Q(0),Q(1)),(Q(1),Q(0)))
    return Module(("s0","s1"),("0","1"),(Q(1,2),Q(1,2)),
                  observations,feasible,losses).check()

def risk_decomposition(a,b,joint_p=None,shared_actions=None,extra=None):
    """Two distinct obstacles: loss from rights and loss from partial observation.

    Equal information is assumed at each benchmark; 'unrestricted oracle'
    discards permissions but retains the SAME loss and joint-world measure.
    If no robust fiberwise authorized policy exists, no finite split is claimed.
    """
    a.check();b.check()
    ids=list(product(range(len(a.states)),range(len(b.states))))
    p={ij:(a.probabilities[ij[0]]*b.probabilities[ij[1]] if joint_p is None
           else joint_p.get(ij,Q())) for ij in ids}
    if any(w<0 for w in p.values()) or sum(p.values(),Q())!=1:
        raise ValueError("invalid joint prior")
    all_actions=list(product(a.actions,b.actions))
    def cost(ij,act):
        i,j=ij;u,v=act
        return a.losses[i][a.actions.index(u)]+b.losses[j][b.actions.index(v)]+(
            Q() if extra is None else extra.get((i,j,u,v),Q()))
    unrestricted=sum((p[ij]*min(cost(ij,x) for x in all_actions)
                      for ij in ids if p[ij]),Q())
    restricted=joint(a,b,joint_p=joint_p,shared_actions=shared_actions,extra=extra)
    if restricted is None or restricted["status"]!="FEASIBLE":
        return {"status":"NO_CERTIFIED_UNIFORMLY_AUTHORIZED_POLICY",
                "unrestricted_oracle":unrestricted}
    authority=restricted["oracle"]-unrestricted
    observation=restricted["risk"]-restricted["oracle"]
    if authority<0 or observation<0:
        raise AssertionError("cost decomposition invariant violated")
    assert restricted["risk"]-unrestricted==authority+observation
    return {"status":"FEASIBLE","unrestricted_oracle":unrestricted,
            "authorized_oracle":restricted["oracle"],
            "observed_authorized_risk":restricted["risk"],
            "authority_deficit":authority,"observation_deficit":observation,
            "total_deficit":authority+observation}
