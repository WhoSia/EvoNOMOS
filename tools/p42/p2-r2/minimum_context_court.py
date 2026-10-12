#!/usr/bin/env python3
"""Finite observational partitions for AUTHENTIC historically committed Echo source.
Exact minimal separating cover by exhaustive enumeration of eight contexts.
No learned or novel automata theorem: classical equivalence/hitting set."""
import itertools,json,re,sys,hashlib
from pathlib import Path
def main():
 if len(sys.argv)!=4:raise SystemExit("audit.py frozen.json logs-folder receipt.json")
 manifest,root,out=Path(sys.argv[1]),Path(sys.argv[2]),Path(sys.argv[3])
 d=json.loads(manifest.read_text());assert d["protocol"]=="EVONOMOS_P42_P2_R2_AUTHENTIC_FAULT_DOMAIN_FREEZE_V1"
 versions=[x["id"] for x in d["variants"]];contexts=[x["id"] for x in d["contexts"]]
 traces={}
 for version in versions:
  txt=(root/(version+".log")).read_text()
  assert "--- FAIL:" not in txt and "\nFAIL\t" not in txt
  rows=[json.loads(m.group(1)) for m in re.finditer(r"P42_R2_NATIVE_TRACE\s+(\{[^\n\r]*\})",txt)]
  assert len(rows)==len(contexts),(version,len(rows))
  assert {x["context"] for x in rows}==set(contexts)
  traces[version]={r["context"]:r for r in rows}
 def view(v,c,mode):
  x=traces[v][c]
  if mode=="http":return (x["status"],x["body"],x["panic"])
  return (x["status"],x["body"],x["handler"],x["template"],tuple(x["param_names"] or []),tuple(x["param_values"] or []),x["name"],x["handler_count"],x["panic"])
 output={}
 for mode in ["http","trace"]:
  pairs=list(itertools.combinations(versions,2))
  distinguish={c:{(a,b) for a,b in pairs if view(a,c,mode)!=view(b,c,mode)} for c in contexts}
  target=set.union(set(),*distinguish.values())
  selected=None
  for k in range(len(contexts)+1):
   matching=[t for t in itertools.combinations(contexts,k) if set.union(set(),*(distinguish[c] for c in t))==target]
   if matching:
    selected=matching
    break
  assert selected is not None
  signatures={v:tuple(view(v,c,mode) for c in contexts) for v in versions}
  classes={}
  for v,sig in signatures.items():classes.setdefault(repr(sig),[]).append(v)
  output[mode]={"revision_classes":list(classes.values()),"distinguishable_pairs":len(target),"total_pairs":len(pairs),"minimal_suite_size":len(selected[0]),"all_minimal_suites":[list(q) for q in selected],"separating_context_pair_counts":{k:len(v) for k,v in distinguish.items()}}
 assert output["trace"]["distinguishable_pairs"]>=output["http"]["distinguishable_pairs"]
 assert output["trace"]["minimal_suite_size"]<=len(contexts)
 res={"protocol":"P42_P2_R2_AUTHENTIC_HISTORY_FINITE_MINIMAL_SEPARATION_VERIFIED","history_revisions":versions,"source_sha":[v["sha"] for v in d["variants"]],"contexts":contexts,"frozen_sha256":hashlib.sha256(manifest.read_bytes()).hexdigest(),"runs":len(versions)*len(contexts),"partitions":output,"exact_algorithm":"finite exhaustive classical minimum hitting set","self_claim_new_tcs_law":False,"source_to_lean_real_echo_simulation":False,"historical_revision_fault_domain_complete":False}
 out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(res,indent=2)+"\n")
 print("P42_R2_AUTHENTIC_HISTORY_CONTEXT_PARTITIONS_AND_MINIMUM_SET_COVER_PASS")
 print(json.dumps(output,ensure_ascii=False))
if __name__=="__main__":main()
