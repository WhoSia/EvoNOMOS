#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, random
from pathlib import Path

ARMS=("CONTEXT_ONLY","NAMED_PRINCIPLE_PRIME","EVIDENCE_CONDITIONED")

def perm(case_id,arm,rep):
    seed=int(hashlib.sha256(f"{case_id}|{arm}|{rep}|LAW-R1-P5".encode()).hexdigest()[:16],16)
    xs=["ACTION_A","ACTION_B","ABSTAIN"]
    random.Random(seed).shuffle(xs)
    return xs

def render(case,arm,rep):
    order=perm(case["id"],arm,rep)
    shown={f"Option {i+1}": case["action_map"][semantic] for i,semantic in enumerate(order)}
    intro="You are making one software-design decision from the evidence below. Do not assume any named design principle is universally valid."
    if arm=="NAMED_PRINCIPLE_PRIME":
        intro+=f" A reviewer explicitly asks you to consider the {case['principle_prime']}. Treat that principle as relevant guidance."
    elif arm=="EVIDENCE_CONDITIONED":
        intro+=" Use the observed moderators and falsifiers as the authority: prefer a structural rival only when the evidence supports its predicted maintenance effect; otherwise choose ABSTAIN."
    mod=""
    if arm=="EVIDENCE_CONDITIONED":
        mod="\nObserved moderators:\n"+json.dumps(case["moderators"],sort_keys=True)
    options="\n".join(f"{k}: {v}" for k,v in shown.items())
    prompt=f"""{intro}

Context:
{case['context']}{mod}

Choices:
{options}

Return exactly one JSON object, with no markdown:
{{"choice":"Option 1|Option 2|Option 3","confidence":0.0,"reason":"one short sentence"}}
"""
    return prompt, {f"Option {i+1}": semantic for i,semantic in enumerate(order)}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--corpus",required=True,type=Path)
    ap.add_argument("--out",required=True,type=Path)
    ap.add_argument("--replicates",type=int,default=3)
    a=ap.parse_args()
    corpus=json.loads(a.corpus.read_text())
    rows=[]
    for case in corpus["cases"]:
        for arm in ARMS:
            for rep in range(a.replicates):
                prompt,mapping=render(case,arm,rep)
                rows.append({
                    "case_id":case["id"],"family":case["family"],"cell":case["cell"],
                    "arm":arm,"replicate":rep,"principle_prime":case["principle_prime"],
                    "precommitted":case["precommitted"],"principle_congruent":case["principle_congruent"],
                    "option_to_semantic":mapping,"prompt":prompt
                })
    out={"schema_version":"law-r1-p5-prompt-packet-v1","replicates":a.replicates,"rows":rows}
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(f"LAW_R1_P5_PROMPTS={len(rows)}")

if __name__=="__main__":
    main()
