#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, re
from collections import defaultdict
from pathlib import Path

PRINCIPLE_TERMS=re.compile(r"\b(SOLID|single responsibility|open[- ]closed|liskov|interface segregation|dependency inversion|SRP|OCP|LSP|ISP|DIP)\b",re.I)

def mean(xs): return sum(xs)/len(xs) if xs else None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--packet",required=True,type=Path)
    ap.add_argument("--responses",required=True,type=Path)
    ap.add_argument("--out",required=True,type=Path)
    a=ap.parse_args()
    packet=json.loads(a.packet.read_text())
    expected={(r["case_id"],r["arm"],r["replicate"]):r for r in packet["rows"]}
    responses=json.loads(a.responses.read_text())
    parsed=[]
    invalid=[]
    for x in responses["rows"]:
        key=(x["case_id"],x["arm"],x["replicate"])
        meta=expected[key]
        try:
            obj=x["response"] if isinstance(x["response"],dict) else json.loads(x["response"])
            choice=obj["choice"]
            sem=meta["option_to_semantic"][choice]
            reason=str(obj.get("reason",""))
            conf=float(obj.get("confidence",0))
            valid=True
        except Exception as e:
            invalid.append({"key":key,"error":str(e),"raw":x.get("response")})
            continue
        parsed.append({
          **{k:meta[k] for k in ["case_id","family","cell","arm","replicate","precommitted","principle_congruent"]},
          "semantic_choice":sem,
          "aligned":sem==meta["precommitted"],
          "principle_choice":sem==meta["principle_congruent"],
          "abstain":sem=="ABSTAIN",
          "confidence":conf,
          "reason":reason,
          "unsolicited_principle_name": bool(PRINCIPLE_TERMS.search(reason)) if meta["arm"]=="CONTEXT_ONLY" else False
        })
    if invalid:
        raise SystemExit(f"invalid responses: {len(invalid)} first={invalid[0]}")

    groups=defaultdict(list)
    for r in parsed:
        groups[(r["arm"],r["cell"])].append(r)

    summary={}
    for arm in ["CONTEXT_ONLY","NAMED_PRINCIPLE_PRIME","EVIDENCE_CONDITIONED"]:
        rows=[r for r in parsed if r["arm"]==arm]
        non=[r for r in rows if r["cell"]!="APPLY"]
        app=[r for r in rows if r["cell"]=="APPLY"]
        abst=[r for r in rows if r["cell"]=="ABSTAIN"]
        summary[arm]={
          "n":len(rows),
          "alignment_rate":mean([r["aligned"] for r in rows]),
          "principle_congruent_rate_apply":mean([r["principle_choice"] for r in app]),
          "unsupported_maxim_rate_nonapply":mean([r["principle_choice"] for r in non]),
          "abstention_calibration":mean([r["abstain"] for r in abst]),
          "mean_confidence":mean([r["confidence"] for r in rows]),
          "name_mention_leak_rate":mean([r["unsolicited_principle_name"] for r in rows]) if arm=="CONTEXT_ONLY" else None
        }

    ctx=summary["CONTEXT_ONLY"]
    named=summary["NAMED_PRINCIPLE_PRIME"]
    evid=summary["EVIDENCE_CONDITIONED"]

    # paired case/replicate recovery on non-apply cells
    by={(r["case_id"],r["arm"],r["replicate"]):r for r in parsed}
    recover=[]
    flip_correct=[]
    for meta in packet["rows"]:
        if meta["arm"]!="CONTEXT_ONLY" or meta["cell"]=="APPLY": continue
        cid,rep=meta["case_id"],meta["replicate"]
        n=by[(cid,"NAMED_PRINCIPLE_PRIME",rep)]
        e=by[(cid,"EVIDENCE_CONDITIONED",rep)]
        recover.append(n["principle_choice"] and e["aligned"])
    families=sorted(set(r["family"] for r in parsed))
    pair_details=[]
    for fam in families:
        apply_ids=sorted(set(r["case_id"] for r in parsed if r["family"]==fam and r["cell"]=="APPLY"))
        non_ids=sorted(set(r["case_id"] for r in parsed if r["family"]==fam and r["cell"]!="APPLY"))
        if not apply_ids or not non_ids: continue
        for arm in ["CONTEXT_ONLY","NAMED_PRINCIPLE_PRIME","EVIDENCE_CONDITIONED"]:
            vals=[]
            for rep in sorted(set(r["replicate"] for r in parsed)):
                aa=by[(apply_ids[0],arm,rep)]
                nn=by[(non_ids[0],arm,rep)]
                vals.append(aa["aligned"] and nn["aligned"] and aa["semantic_choice"]!=nn["semantic_choice"])
            pair_details.append({"family":fam,"arm":arm,"correct_reversal_rate":mean(vals)})
            if arm=="EVIDENCE_CONDITIONED": flip_correct.extend(vals)

    descriptive={
      "named_principle_pull_nonapply": named["unsupported_maxim_rate_nonapply"]-ctx["unsupported_maxim_rate_nonapply"],
      "evidence_conditioning_reduction_nonapply": named["unsupported_maxim_rate_nonapply"]-evid["unsupported_maxim_rate_nonapply"],
      "named_to_evidence_recovery_rate":mean(recover),
      "evidence_conditioned_pair_reversal_rate":mean(flip_correct)
    }
    # pilot labels are descriptive, not population claims.
    if descriptive["named_principle_pull_nonapply"]>=0.15 and descriptive["evidence_conditioning_reduction_nonapply"]>=0.15:
        pilot="MAXIM_PRIOR_SIGNAL_WITH_EVIDENCE_RECOVERY"
    elif descriptive["named_principle_pull_nonapply"]<=-0.15:
        pilot="NO_MAXIM_PRIOR_SIGNAL_OR_REVERSE_PRIME_EFFECT"
    else:
        pilot="INCONCLUSIVE_MAXIM_PRIOR_PILOT"

    out={
      "schema_version":"law-r1-p5-score-v1",
      "model":responses.get("model"),
      "run_metadata":responses.get("run_metadata",{}),
      "n":len(parsed),
      "summary":summary,
      "descriptive_contrasts":descriptive,
      "paired_reversal":pair_details,
      "pilot_classification":pilot,
      "authority_ceiling":"MODEL_SPECIFIC_DESCRIPTIVE_PILOT",
      "solid_verdict":"WITHHELD",
      "llm_population_claim":"FORBIDDEN"
    }
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("LAW_R1_P5_SCORE=PASS")
    print(json.dumps({"model":out["model"],"pilot":pilot,"contrasts":descriptive},sort_keys=True))

if __name__=="__main__":
    main()
