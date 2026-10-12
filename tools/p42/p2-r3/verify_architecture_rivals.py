#!/usr/bin/env python3
"""R3 strict original-source architecture action court; does not infer net lifetime winner."""
import json,re,sys,hashlib
from pathlib import Path
if len(sys.argv)!=4:raise SystemExit("usage verify_rivals.py frozen.json original-go.log receipt.json")
p,l,out=map(Path,sys.argv[1:])
m=json.loads(p.read_text())
assert m["protocol"]=="EVONOMOS_P42_P2_R3_INITIAL_DEMAND_MATCHED_SOURCE_ARCHITECTURE_RIVALS_FREEZE_V1"
rows={}
for line in l.read_text().splitlines():
 match=re.search(r"P42_R3_TRACE\s+(\{[^\r\n]*\})",line)
 if match:
  obj=json.loads(match.group(1))
  key=(obj["rival"],obj["phase"],obj["request"])
  assert key not in rows
  rows[key]=obj
rivals=["SINGLE","SPLIT","SPLIT_REVERSE","SINGLE_REPAIRED"]
assert len(rows)==16
for name in rivals:
 for case in m["frozen_initial_demand"]:
  x=rows[(name,"initial",case["path"])]
  assert (x["status"],x["body"])==(case["want_status"],case["want_body"]),(name,case,x)
 for case in m["frozen_possible_late_demand"]:
  x=rows[(name,"late",case["path"])]
  if name=="SINGLE":
   assert x["status"]==404 and x["handler_calls"]==0
  else:
   assert (x["status"],x["body"])==(case["want_status"],case["want_body"]),(name,case,x)
 assert rows[(name,"initial","/health")]["handler_calls"]==1
 assert rows[(name,"initial","/r/foo:cancel")]["handler"]=="verb"
assert rows[("SINGLE","initial","/health")]["source_extra_registrations"]==1
assert rows[("SPLIT","initial","/health")]["source_extra_registrations"]==2
assert rows[("SPLIT_REVERSE","initial","/health")]["source_extra_registrations"]==2
assert rows[("SINGLE_REPAIRED","late","/r/foo")]["source_extra_registrations"]==2
assert rows[("SINGLE_REPAIRED","late","/r/foo")]["late_source_edits"]==1
assert rows[("SPLIT","late","/r/foo")]["late_source_edits"]==0
source_initial={"SINGLE":1,"SPLIT":2,"SPLIT_REVERSE":2}
source_late={"SINGLE_REPAIRED":1,"SPLIT":0,"SPLIT_REVERSE":0}
r={
 "protocol":"P42_R3_INITIAL_DEMAND_MATCHED_STRUCTURAL_RIVALS_NATIVE_GO_PASS",
 "manifest_sha256":hashlib.sha256(p.read_bytes()).hexdigest(),
 "original_go_log_sha256":hashlib.sha256(l.read_bytes()).hexdigest(),
 "original_upstream_echo_sha":m["unchanged_original_sha"],
 "original_upstream_code_edited":False,
 "researcher_authored_rival_source_assemblies":True,
 "client_http_tests":16,
 "initial_demand_behaviorally_equal":True,
 "single_initial_route_surface":1,
 "split_initial_route_surface":2,
 "single_late_change_operations_to_meet_named_legacy":1,
 "split_late_change_operations_to_meet_named_legacy":0,
 "late_repaired_single_and_split_named_client_behaviors_equal":True,
 "split_reverse_registration_order_named_clients_equal":True,
 "no_late_demand_single_lower_source_birth_surface":True,
 "late_demand_split_lower_incremental_edit_burden":True,
 "late_demand_both_end_at_two_route_registrations":True,
 "S_L_C_A_Q_scalar_winner":None,
 "genuine_OO_source_intervention":"handler route namespace partition into specific verb route plus generic fallback",
 "full_software_lifecycle_cost_winner_known":False,
 "broader_client_equivalence_proven":False,
 "historical_upstream_actor_authorization_proven":False,
 "new_TCS_or_OO_law_proven":False,
 "LAW_R2_authorized":False
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(r,indent=2)+"\n")
print("P42_R3_GENUINE_SOURCE_BOUNDARY_RIVALS_INITIAL_EQUAL_LATER_MAINTENANCE_TRADEOFF_PASS")
