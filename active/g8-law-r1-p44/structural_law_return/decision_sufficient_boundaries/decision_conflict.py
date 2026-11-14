"""Finite exhaustive decision-boundary conflict hypergraph (research prototype).

Classical decision theory / hypergraph combinatorics; NO novelty priority.
Reference implementation for small, fully specified contexts only.
"""
from fractions import Fraction as F
from itertools import combinations

def frac(x):
    return x if isinstance(x,F) else F(str(x))

def validate(rows):
    assert rows and all(len(r["losses"])==len(rows[0]["losses"])>0 for r in rows)
    assert len(set(r["id"] for r in rows))==len(rows)
    assert all(frac(r["p"])>0 for r in rows)
    assert sum((frac(r["p"]) for r in rows),F())==1

def argmin(row):
    a=[frac(x) for x in row["losses"]]
    return frozenset(i for i,x in enumerate(a) if x==min(a))

def fibers(rows):
    return [[r for r in rows if r["signal"]==key]
            for key in sorted({r["signal"] for r in rows})]

def conflicts(group):
    optimal=[argmin(row) for row in group]
    out=[]
    for k in range(2,len(group)+1):
        for subset in combinations(range(len(group)),k):
            common=set(optimal[subset[0]])
            for i in subset[1:]:common.intersection_update(optimal[i])
            if not common and not any(set(e).issubset(subset) for e in out):
                out.append(subset)
    return out

def exact_regret(rows):
    validate(rows)
    n=len(rows[0]["losses"])
    oracle=sum((frac(r["p"])*min(map(frac,r["losses"])) for r in rows),F())
    restricted=sum((min(sum((frac(r["p"])*frac(r["losses"][a]) for r in g),F())
                        for a in range(n)) for g in fibers(rows)),F())
    return restricted-oracle

def lower_bound(group):
    edges=conflicts(group)
    if not edges:return F()
    gaps=[]
    for r in group:
        values=tuple(map(frac,r["losses"]))
        gaps.append(min((v-min(values) for v in values if v>min(values)),default=F()))
    best=None
    for mask in range(1<<len(group)):
        chosen={i for i in range(len(group)) if mask & (1<<i)}
        if all(chosen.intersection(e) for e in edges):
            val=sum((frac(group[i]["p"])*gaps[i] for i in chosen),F())
            if best is None or val<best:best=val
    return best

def certificate(rows):
    validate(rows)
    return {"exact":str(exact_regret(rows)),
            "hypergraph_lower_bound":str(sum((lower_bound(g) for g in fibers(rows)),F())),
            "minimal_conflicts":[[[g[i]["id"] for i in edge] for edge in conflicts(g)]
                                 for g in fibers(rows)]}

def optimize_signals(rows,features,prices,authorized=None):
    """Minimize fixed signal cost plus Bayes regret; no unverified action rights."""
    validate(rows)
    if set(features)!=set(prices):raise ValueError("feature and price mismatch")
    if any(set(value)!={r["id"] for r in rows} for value in features.values()):
        raise ValueError("each signal must cover all contexts")
    if any(frac(v)<0 for v in prices.values()):raise ValueError("negative feature price")
    if authorized is not None and not set(authorized).issubset(features):
        raise ValueError("unknown authorized feature")
    keys=sorted(set(features) if authorized is None else set(authorized))
    best=None
    for k in range(len(keys)+1):
        for subset in combinations(keys,k):
            refined=[dict(r,signal=repr((r["signal"],tuple(str(features[j][r["id"]])
                                                       for j in subset)))) for r in rows]
            gap=exact_regret(refined)
            implementation=sum((frac(prices[j]) for j in subset),F())
            candidate=(gap+implementation,implementation,gap,subset)
            if best is None or candidate<best:best=candidate
    return {"total":str(best[0]),"interface_cost":str(best[1]),
            "regret":str(best[2]),"features":list(best[3])}

def restic_worlds():
    # L(KEEP)=0, L(REPACK)= +10.46 (locked) or -0.54 (metered).
    return [
        {"id":"prepaid","signal":"pack_usage","losses":("0","10.46"),"p":"1/2"},
        {"id":"metered","signal":"pack_usage","losses":("0","-0.54"),"p":"1/2"}]

def triple_conflict_worlds():
    # Every pair shares an optimal action; all three do not.
    return [
        {"id":"a","signal":"same","losses":(0,0,1),"p":"1/3"},
        {"id":"b","signal":"same","losses":(1,0,0),"p":"1/3"},
        {"id":"c","signal":"same","losses":(0,1,0),"p":"1/3"}]
