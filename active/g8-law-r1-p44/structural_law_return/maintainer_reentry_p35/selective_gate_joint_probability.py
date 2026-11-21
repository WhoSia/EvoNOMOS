"""Classical separately-calibrated source cochange gate on original go-chi Git history.

The source-scoring holdout aggregates were already read by researchers;
this is exploratory comparison. Training B1 model remains frozen.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import json

from selective_gate_original_history import (
    TRIAD, SOURCE, git, read_heldout, assess
)

def training_rows(root):
    revisions=git(root,"log","--no-merges","--format=%H",
                  "--before=2020-01-01T00:00:00Z","HEAD","--",*TRIAD).split()
    rows=[]
    for rev in revisions:
        touched=set(git(root,"diff-tree","--no-commit-id","--name-only","-r",rev).splitlines())
        relevant=tuple(f for f in TRIAD if f in touched)
        if relevant:rows.append((rev,relevant))
    assert len(rows)==121,("source training events changed",len(rows))
    assert sum(len(files)>=2 for _,files in rows)==43
    return rows

def train_full_gate(rows,seal):
    result={}
    for seed in TRIAD:
        p=seal["Predict"][seed]
        partner=p["B1"]
        seen=sum(seed in files for _,files in rows)
        any_count=sum(seed in files and len(files)>1 for _,files in rows)
        top_count=sum(seed in files and partner in files for _,files in rows)
        assert seen==p["B1SeedEvents"],(seed,seen,p["B1SeedEvents"])
        assert top_count==p["B1PairEvents"],(seed,top_count,p["B1PairEvents"])
        assert top_count<=any_count<=seen
        q_top=Fraction(top_count,seen)
        q_any=Fraction(any_count,seen)
        result[seed]={
            "top_partner":partner,
            "train_seed_events":seen,
            "train_partner_events":top_count,
            "train_any_extra_events":any_count,
            "p_top":str(q_top),
            "p_any":str(q_any),
            "p_top_float":float(q_top),
            "p_any_float":float(q_any),
            "alert":q_top+q_any>1,
        }
    return result

def evaluate_joint_gate(holdout,source_gate,seal):
    queries=[(sha,seed,tuple(f for f in touched if f!=seed))
             for sha,touched in holdout for seed in touched]
    correct=wrong=fp=miss=alerts=0
    for _,seed,partners in queries:
        if source_gate[seed]["alert"]:
            alerts+=1
            if not partners:fp+=1
            elif seal["Predict"][seed]["B1"] in partners:correct+=1
            else:wrong+=1
        elif partners:miss+=1
    assert correct+wrong+miss==13
    assert fp<=34
    return dict(alerts=alerts,correct_partner=correct,wrong_partner=wrong,
                false_singleton_alert=fp,missed_positive=miss,
                binary_loss_equal_cost=fp+wrong+miss)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--original",required=True)
    ap.add_argument("--seal",required=True)
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    seal=json.loads(Path(a.seal).read_text())
    assert seal["Original"]==SOURCE
    holdout=read_heldout(a.original)
    baselines=assess(holdout,seal)
    fit=train_full_gate(training_rows(a.original),seal)
    result={
        "authority":"EXPLORATORY_HISTORICAL_COCHANGE_NOT_CAUSAL",
        "source":SOURCE,
        "frozen_original_training_model":seal["TrainingSource"],
        "training_by_seed":fit,
        "base":baselines,
        "two_probability_gate":evaluate_joint_gate(holdout,fit,seal),
    }
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
