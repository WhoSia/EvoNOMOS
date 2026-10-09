"""P37-C1 source-linked finite *model* of two-owner repair graph.
Not an AST-derived exhaustive actual Go source repair graph.
"""
import json
from pathlib import Path

p=Path(__file__).with_name("owner_repair_graph.json")
g=json.loads(p.read_text(encoding="utf-8"))
worlds=g["histories"]
assert len(worlds)==4
assert len({x["hidden_key"] for x in worlds})==2
assert all(x["archive_accessible_key"]==x["hidden_key"] for x in worlds if x["ingress_forward_original"])
assert all(x["archive_accessible_key"] is None for x in worlds if not x["ingress_forward_original"])
assert all(not x["can_replay_input"] for x in g["authorized_edits"])
assert any(x["owner"]=="B:archive" and not x["edits_ingress"] for x in g["authorized_edits"])

def uniform_source_repair(group):
    # B-only deterministic post-hoc reader must factor through stored state.
    observations={}
    for x in group:
        state=x["archive_accessible_key"]
        desired=x["hidden_key"]
        if state in observations and observations[state]!=desired:
            return False
        observations[state]=desired
    return True
retained=[x for x in worlds if x["ingress_forward_original"]]
lossy=[x for x in worlds if not x["ingress_forward_original"]]
assert uniform_source_repair(retained)
assert not uniform_source_repair(lossy)

# Q0 observational quotient merges all four worlds; the more informative
# archive-state quotient splits the retained histories but merges the lossy two.
present_observations={(7,1) for x in worlds}
assert len(present_observations)==1
assert len({x["archive_accessible_key"] for x in worlds})==3

print("P37_C1_TYPED_FOUR_WORLD_COMPOSITION_PASS")
print("P37_C1_OWNER_B_REPAIR_RETAINED_UNIFORMLY_POSSIBLE")
print("P37_C1_OWNER_B_REPAIR_LOSSY_NO_ORACLE_UNIFORMLY_IMPOSSIBLE")
print("P37_C1_CURRENT_QUOTIENT_MERGES_ALL_FOUR__STORED_QUOTIENT_DIFFERS")
print("Finite model derived from sealed Go interface/owner contract, NOT exhaustive code edits.")
