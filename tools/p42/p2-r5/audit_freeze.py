#!/usr/bin/env python3
import json,hashlib,sys
from pathlib import Path
src,out=map(Path,sys.argv[1:])
m=json.loads(src.read_text())
assert m["protocol"]=="EVONOMOS_G8_LAW_R1_P42_P2_R5_CAPABILITY_OBLIGATION_COURT_FROZEN_V1"
assert m["version"]=="R5-FROZEN_BEFORE_GO_GENERATOR_AND_NATIVE_OUTCOMES"
assert len(m["predictions"])==16 and len({c["id"] for c in m["predictions"]})==16
for row in m["predictions"]:
 a,b=row["architecture"].split("_");d=row["demand"];x=row["expected"]
 n=2 if d in ["RX","C"] else 1
 assert x["composition_wiring_edits"]==n
 assert x["consumer_signature_edits"]==(n if b=="DIRECT" else 0)
 assert x["forced_irrelevant_methods"]==(n if a=="BUNDLE" and b=="PORT" and d!="C" else 0)
 assert x["touched_sites"]==sum(x[z] for z in ["consumer_signature_edits","composition_wiring_edits","forced_irrelevant_methods"])
assert m["post_freeze_go_source_oracle_exists"] is False
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({"protocol":"R5_PRETEST_16_CASES_FROZEN","manifest_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),"native_results_available":False},indent=2)+"\n")
print("P42_R5_16_CASE_GO_SOURCE_PRETEST_FREEZE_PASS")
