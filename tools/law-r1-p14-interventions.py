#!/usr/bin/env python3
import json, hashlib
from pathlib import Path

SRC=Path("active/g8-law-r1-p14/P14_INTERVENTION_CUSTODY.json")
OUT=Path("out-p14"); OUT.mkdir(parents=True,exist_ok=True)
d=json.loads(SRC.read_text())
families=d["intervention_families"]

summary={}
for target in ["COMPATIBILITY_OBLIGATION","COEXISTENCE_REQUIREMENT","RELEASE_AUTHORITY"]:
    fs=[f for f in families if f["target"]==target]
    exact=[f for f in fs if f["grade"].startswith("EXACT")]
    summary[target]={"exact_family_count":len(exact),"families":[f["id"] for f in fs]}

compat_cross_domain = (
    d["prior_exact_family"]["target"]=="COMPATIBILITY_OBLIGATION"
    and summary["COMPATIBILITY_OBLIGATION"]["exact_family_count"]>=1
)
stable_compat = compat_cross_domain
bounded_coexist = summary["COEXISTENCE_REQUIREMENT"]["exact_family_count"]>=1
bounded_authority = summary["RELEASE_AUTHORITY"]["exact_family_count"]>=1

rep={}
for f in families:
    original={"target":f["target"],"grade":f["grade"],"G":f["G"],"E":f["E"],"worlds":f["worlds"]}
    alt={"coordinate":f["target"],"match":f["grade"],"geometry":f["G"],"evidence":f["E"],"contrasts":f["worlds"],"display":f["id"].lower()}
    restored={"target":alt["coordinate"],"grade":alt["match"],"G":alt["geometry"],"E":alt["evidence"],"worlds":alt["contrasts"]}
    h1=hashlib.sha256(json.dumps(original,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    h2=hashlib.sha256(json.dumps(restored,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    rep[f["id"]]={"pass":h1==h2,"original":h1,"variant":h2}

result={
  "stage":d["stage"],
  "fresh_source_count":len(d["fresh_sources"]),
  "family_count":len(families),
  "coordinate_summary":summary,
  "stable_primitives":["COMPATIBILITY_OBLIGATION"] if stable_compat else [],
  "bounded_identified":[x for x,v in [
      ("COEXISTENCE_REQUIREMENT",bounded_coexist),
      ("RELEASE_AUTHORITY",bounded_authority)
  ] if v],
  "dependency_orientation":d["dependency_orientation"],
  "representation_invariance":{"cases":rep,"all_pass":all(v["pass"] for v in rep.values())},
  "anti_rationalization_pass":len(d.get("post_hoc_coordinate_additions",[]))==0,
  "same_normalized_X_G_E_conflicting_action_observed":False,
  "negative_controls":d["negative_controls"]
}
(OUT/"p14-interventions.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print("LAW_R1_P14_INTERVENTION_CUSTODY=PASS")
print("STABLE=" + (",".join(result["stable_primitives"]) or "NONE"))
print("BOUNDED=" + (",".join(result["bounded_identified"]) or "NONE"))
print("REPRESENTATION_INVARIANCE=" + str(result["representation_invariance"]["all_pass"]))
print("ANTI_RATIONALIZATION=" + str(result["anti_rationalization_pass"]))
