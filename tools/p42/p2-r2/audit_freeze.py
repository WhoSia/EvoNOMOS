#!/usr/bin/env python3
import json,hashlib,sys
from pathlib import Path
if len(sys.argv)!=3:raise SystemExit("usage audit.py frozen.json receipt.json")
p,out=map(Path,sys.argv[1:]);m=json.loads(p.read_text())
assert m["protocol"]=="EVONOMOS_P42_P2_RAVEL_R2_HISTORICAL_ORIGINAL_SOURCE_FAULT_DOMAIN_FREEZE_V1"
assert m["context_count"]==len(m["contexts"])==16
assert len(m["actual_programs"])==12
assert len({x["sha"] for x in m["actual_programs"]})==12
assert len({x["id"] for x in m["contexts"]})==16
assert m["actual_programs"][0]["sha"]==m["source_before"]
assert m["actual_programs"][-1]["sha"]==m["source_merge"]
assert not m["prospective_blind_unseen"]
assert m["historical_upstream_edit_rights"]=="UNKNOWN"
assert not m["go_to_lean_full_refinement"] and not m["law_r2_authorized"]
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({"protocol":"P42_R2_PRETEST_REAL_12_SOURCE_16_CONTEXT_FREEZE_PASS","hash":hashlib.sha256(p.read_bytes()).hexdigest(),"n_sources":12,"n_clients":16,"native_harness_exists_at_freeze":False},indent=2)+"\n")
print("P42_R2_PRETEST_REAL_12_SOURCE_16_CONTEXT_FREEZE_PASS")
