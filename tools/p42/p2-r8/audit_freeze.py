#!/usr/bin/env python3
import json,sys,hashlib
from pathlib import Path
d=json.loads(Path(sys.argv[1]).read_text())
assert d["protocol"]=="P42_P2_R8_TYPED_VS_OBSERVATIONAL_REPAIR_PREREG_V1"
assert d["status"]=="FROZEN_BEFORE_NATIVE_TEST"
assert d["base"]["commit"]=="9ab8b62505c85a5e03be1ae97949e960e24b6d4f"
assert {x["id"] for x in d["cases"]}=={"normal-adapter","shared-alias-provider","identity-roundtrip"}
assert d["cases"][0]["isolated_while_outstanding"] and not d["cases"][1]["isolated_while_outstanding"]
assert d["base"]["source_read_only"]
print("P42_R8_OWNER_FAULT_DOMAIN_SOURCE_CONTRACT_FROZEN_PASS")
