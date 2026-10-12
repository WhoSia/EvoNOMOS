import json,sys,hashlib,pathlib
m=json.loads(pathlib.Path(sys.argv[1]).read_text())
assert m["protocol"]=="P42_P2_R9_REAL_CLIENT_CONTRACT_AND_REPAIR_PREFERENCE_FREEZE_V1"
assert m["status"]=="FROZEN_BEFORE_R9_GO_TESTS"
assert m["base"]["commit"]=="9ab8b62505c85a5e03be1ae97949e960e24b6d4f"
assert len(m["hypotheses"])==3 and len(m["requests"])==2
assert {x["id"] for x in m["hypotheses"]}=={"default-nop","legacy-adapter","shared-provider"}
print("P42_R9_CLIENT_DEMAND_PREREG_PASS",hashlib.sha256(pathlib.Path(sys.argv[1]).read_bytes()).hexdigest())
