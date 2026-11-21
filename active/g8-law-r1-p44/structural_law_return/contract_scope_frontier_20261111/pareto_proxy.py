"""Pareto *proxy* analysis of already executed original Go source edits.

Sites are syntactic locations, NOT human hours, expected defects or lifecycle cost.
Direct legacy violation is from an optional researcher-authored customer contract.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class ActualSourceCandidate:
    name: str
    edit_sites: int
    direct_legacy_contract_break: int
    route_contract_pass: bool

# Original native Go result #42932257551, identical for LIVE and SNAPSHOT.
REAL_GO_FINITE_ORACLE=(
    ActualSourceCandidate("constructor",1,1,True),
    ActualSourceCandidate("route_both",2,0,True),
    ActualSourceCandidate("match_lower",1,1,True),
    ActualSourceCandidate("none",0,0,False),
    ActualSourceCandidate("remove_lookup_lower",1,0,False),
)

def pareto(keep_direct_as_hard:bool=False,include_direct_risk:bool=True):
    feasible=[x for x in REAL_GO_FINITE_ORACLE
              if x.route_contract_pass and
              (not keep_direct_as_hard or x.direct_legacy_contract_break==0)]
    def coord(x):
        return (x.edit_sites,x.direct_legacy_contract_break) if include_direct_risk else (x.edit_sites,)
    def dominates(a,b):
        return all(x<=y for x,y in zip(coord(a),coord(b))) and any(
            x<y for x,y in zip(coord(a),coord(b)))
    return sorted(x.name for x in feasible if not any(
        dominates(y,x) for y in feasible if y!=x))

if __name__=="__main__":
    print("Two-dimensional source PROXY Pareto:",pareto())
    print("Router-only proxy Pareto:",pareto(include_direct_risk=False))
    print("Hard direct-client contract:",pareto(keep_direct_as_hard=True))
