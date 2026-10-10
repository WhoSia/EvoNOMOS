#!/usr/bin/env python3
"""P41 evidence-type checker, supports immutable P0 V1 and post-P1 V2.

Mechanically audits SOURCE STATUS CLAIMS and referenced CI identifiers; does
not reauthenticate a GitHub permission query or prove original Go semantics.
"""
import hashlib, json, sys
from pathlib import Path

EXPECTED={"A","B","C","D","E","F"}
P40_NATIVE={
  "A":(38060623268,"3882266a3641a36fc2111b48cd597adab1c1ecea"),
  "B":(38052437653,"3882266a3641a36fc2111b48cd597adab1c1ecea"),
  "D":(38051358314,"3882266a3641a36fc2111b48cd597adab1c1ecea"),
  "E":(38047274495,"167e1e3bd039d060696b99c8da4e876ae04f42c1"),
}

def main():
 if len(sys.argv)!=3:raise SystemExit("usage: p0_registry_audit.py evidence.json receipt.json")
 source,out=map(Path,sys.argv[1:])
 doc=json.loads(source.read_text())
 assert doc["protocol"] in {
  "EVONOMOS_G8_LAW_R1_P41_P0_EVIDENCE_MATRIX_V1",
  "EVONOMOS_G8_LAW_R1_P41_EVIDENCE_MATRIX_V2",
 }
 v2=doc["protocol"].endswith("V2")
 assert doc["status"]==("RUNNING" if v2 else "OPEN")
 definitions={x["code"]:x for x in doc["definitions"]}
 assert len(doc["definitions"])==6 and set(definitions)==EXPECTED
 for key, row in definitions.items():
  assert len(row["predicate"])>14 and len(row["observation"])>18
  assert len(row["missing"])>20
  if key in P40_NATIVE:
   assert row["evidence_status"]=="NATIVE_BOUNDED"
   assert row["source"]["repo"]=="WhoSia/EvoNOMOS"
   assert (row["source"]["run_id"],row["source"]["original_upstream_commit"])==P40_NATIVE[key]
  elif not v2:
   assert row["evidence_status"]=="SYNTHETIC_ONLY" and row["source"] is None
  elif key=="C":
   assert row["evidence_status"]=="PLATFORM_AUTHORITY_CURRENT_ROLE_AND_HISTORICAL_MERGE_LIMITED"
   a=row["source"]
   assert a["repo"]=="WhoSia/EvoNOMOS" and a["verification_workflow_run_id"]==38063852776
   assert a["reported_permission"]=="admin"
   snap=json.loads(Path("tools/p41/p1-authority/github_operational_authority_snapshot.json").read_text())
   assert snap["verification"][0]["observed_permission"]=="admin"
   assert snap["verification"][1]["observed_authenticated_permissions"]["admin"] is True
   assert snap["general_p41_C_axiom_status"]=="UNPROVED"
   assert a["external_merge_commit"]=="f085ffbe8f99de165bd920746920000ab56bd6bc"
   assert a["external_merge_actor"]=="vishr"
   assert a["external_merge_at_utc"]=="2026-09-30T01:00:17Z"
   historical=json.loads(Path("tools/p41/p1-authority/github_historical_merge_event.json").read_text())
   assert historical["merged"] is True
   assert historical["merge_commit_sha"]==a["external_merge_commit"]
   assert historical["merge_actor"]==a["external_merge_actor"]
   assert historical["merge_at_utc"]==a["external_merge_at_utc"]
   assert historical["not_proved"]
  else:
   assert key=="F" and row["evidence_status"]=="NATIVE_INTERFACE_BOUNDARY_ONLY"
   a=row["source"]
   assert a["repo"]=="WhoSia/EvoNOMOS" and a["run_id"]==38063852776
   assert a["original_upstream_commit"]=="3882266a3641a36fc2111b48cd597adab1c1ecea"
   assert a["interface"]=="echo.Router" and a["compile_rejection"]=="missing method Route"
 assert any("independence" in x for x in doc["proof_debt"])
 assert any("HOLD" in x for x in doc["proof_debt"])
 receipt={
  "protocol":"P41_P1_EPISTEMIC_EVIDENCE_V2_TYPE_AUDIT_PASS" if v2 else "P41_P0_EPISTEMIC_TYPE_AUDIT_PASS",
  "input_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
  "native_original_case_categories":4,
  "operational_platform_rights_snapshot_categories":1 if v2 else 0,
  "native_provider_interface_categories":1 if v2 else 0,
  "synthetic_only_categories":0 if v2 else 2,
  "auth_snapshot_independently_reauthenticated_in_CI":False,
  "historical_platform_merge_event_recorded":bool(v2),
  "branch_policy_and_normative_historical_authorization_proven":False,
  "complete_provider_semantic_contract_proven":False,
  "actual_A_F_semantic_independence_proven":False,
  "full_historical_SOLID_derived":False,
  "law_R2_authorized":False
 }
 out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n")
 print("P41_P0_PROVENANCE_BOUNDARY_AUDIT_PASS",receipt["protocol"])
if __name__=="__main__":main()
