#!/usr/bin/env python3
"""Second R6 tier: real Heroku source consumer compilation under historical
chi versions, with source-chronology and causal attribution limits."""
import json,hashlib,sys
from pathlib import Path
def main():
 if len(sys.argv)!=6:raise SystemExit("usage: audit_external.py frozen.json status.tsv pre.log post.log receipt.json")
 manifest,status,pre,post,out=map(Path,sys.argv[1:])
 lock=json.loads(manifest.read_text())
 assert lock["protocol"]=="EVONOMOS_P42_P2_R6_EXTERNAL_CONSUMER_CROSS_TEMPORAL_PREREG_V1"
 assert lock["status"]=="FROZEN_BEFORE_EXTERNAL_PROJECT_GO_COMPILATION"
 rows=[z.split("\t") for z in status.read_text().splitlines() if z.strip()]
 assert len(rows)==2 and {r[0] for r in rows}=={"pre","post"}
 assert all(len(r)==2 for r in rows)
 actual={r[0]:int(r[1]) for r in rows}
 observed={}
 for k,log in [("pre",pre),("post",post)]:
  text=log.read_text()
  observed[k]={
   "exit_code":actual[k],
   "native_go_test_success":actual[k]==0 and ("ok" in text or "?   " in text),
   "log_sha256":hashlib.sha256(log.read_bytes()).hexdigest()
  }
  # Exit status is kept even if the forecast was wrong; no self-granted PASS.
  if actual[k]==0 and not observed[k]["native_go_test_success"]:
   raise AssertionError("no Go test command completion indication")
 prediction_correct=(actual["pre"]==0 and actual["post"]==0)
 receipt={
  "protocol":"P42_R6_REAL_EXTERNAL_HEROKU_CONSUMER_CROSS_TEMPORAL_GO_COURT",
  "frozen_sha256":hashlib.sha256(manifest.read_bytes()).hexdigest(),
  "true_externally_maintained_repository":lock["consumer"]["repository"],
  "pinned_external_consumer_commit":lock["consumer"]["commit"],
  "consumer_source_temporal_relation_to_2024_edit":"NOT_ESTABLISHED",
  "historical_chi_source_read_only":True,
  "consumer_source_read_only":True,
  "identical_go_test_package":"./hmiddleware",
  "forecast_correct_both_versions":prediction_correct,
  "native_external_consumer_compiled_versions":sum(int(y["native_go_test_success"]) for y in observed.values()),
  "results":observed,
  "independent_blinded_2024_external_consumer_cohort":False,
  "LAW_R2_authorized":False
 }
 out.write_text(json.dumps(receipt,sort_keys=True,indent=2)+"\n")
 print("P42_R6_HEROKU_EXTERNAL_CONSUMER_RECEIPT_"+("TWO_PASSES" if prediction_correct else "HOLD_OR_COUNTEREXAMPLE"))
 if not prediction_correct:sys.exit(22)
if __name__=="__main__":main()
