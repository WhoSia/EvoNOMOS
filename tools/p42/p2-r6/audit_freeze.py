#!/usr/bin/env python3
"""R6 prereg guard: frozen historical upstream and seven predictions, no test oracle."""
import json,hashlib,pathlib,sys
def main():
 p=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);d=json.loads(p.read_text())
 assert d["protocol"]=="EVONOMOS_G8_LAW_R1_P42_P2_R6_CROSS_ECOLOGY_HISTORICAL_SOURCE_FREEZE_V1"
 assert d["status"]=="FROZEN_BEFORE_R6_NATIVE_CLIENT_ORACLE"
 assert {(x["repo"],x["pr"]) for x in d["upstreams"]}=={("go-chi/chi",926),("grpc/grpc-go",7356)}
 assert len(d["frozen_cases"])==7 and len({x["id"] for x in d["frozen_cases"]})==7
 assert sum(x["pre_compile"] for x in d["frozen_cases"])==4
 assert sum(x["post_compile"] for x in d["frozen_cases"])==5
 assert all(x["historical_2024_customer_status"]=="NOT_VERIFIED" for x in d["external_source_witnesses"])
 assert all(x["native_external_project_compiled"] is False for x in d["external_source_witnesses"])
 assert d["algebra"]["cut_definition"].startswith("source edit-set")
 out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps({"protocol":"P42_R6_FROZEN_TWO_REAL_HISTORICAL_PROJECTS_SEVEN_COMPILER_CASES_PASS","sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"researcher_authored_clients":True,"historic_external_consumers_compiled":False},indent=2)+"\n")
 print("P42_R6_FROZEN_TWO_REAL_HISTORICAL_PROJECTS_SEVEN_COMPILER_CASES_PASS")
if __name__=="__main__":main()
