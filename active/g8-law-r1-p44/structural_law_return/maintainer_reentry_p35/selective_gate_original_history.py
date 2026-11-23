"""Original Go Chi git-history heldout decision audit, descriptive only.

GitHub-trusted original *pre-2020* model seal supplies B1 predictions.
Historical postcutoff labels reconstruct ORIGINAL SOURCE COEDITS, not repair necessity.
"""
import argparse
import json
import subprocess
from fractions import Fraction
from pathlib import Path

TRIAD=("mux.go","tree.go","context.go")
SOURCE="67be7d9cafdaeb4e04e887ff78d09e030ee43b00"

def git(root,*args):
    return subprocess.check_output(["git","-C",str(root),*args],text=True).strip()

def read_heldout(root):
    assert git(root,"rev-parse","HEAD")==SOURCE,"Wrong original Go source SHA"
    assert git(root,"rev-parse","--is-shallow-repository")=="false","Full git history required"
    revs=git(root,"log","--no-merges","--format=%H",
             "--since=2020-01-01T00:00:00Z","--before=2024-06-28T14:29:28Z",
             "HEAD","--",*TRIAD).split()
    rows=[]
    for rev in revs:
        changed=set(git(root,"diff-tree","--no-commit-id","--name-only","-r",rev).splitlines())
        relevant=tuple(f for f in TRIAD if f in changed)
        if relevant:rows.append((rev,relevant))
    return rows

def assess(rows,model):
    # Original P35-P5 label count guard. Reject any source-window mismatch.
    queries=[(sha,seed,tuple(f for f in touched if f!=seed))
            for sha,touched in rows for seed in touched]
    positive=sum(bool(x[2]) for x in queries)
    assert (len(rows),len(queries),positive)==(40,47,13),(
        "Original P35 source count mismatch",len(rows),len(queries),positive)
    predictions=model["Predict"]
    for seed in TRIAD:
        assert predictions[seed]["B1"] in TRIAD
        assert predictions[seed]["B1"]!=seed
    decisions={}
    for policy in ("always","half","never"):
        metrics=dict(source_commits=len(rows),seed_queries=len(queries),positive=positive,
                     singleton=len(queries)-positive,alerts=0,correct_partner=0,
                     wrong_partner=0,false_singleton_alert=0,missed_positive=0)
        for sha,seed,others in queries:
            p=predictions[seed]
            use=policy=="always" or (
                policy=="half" and
                Fraction(p["B1PairEvents"],p["B1SeedEvents"])>Fraction(1,2))
            if use:
                metrics["alerts"]+=1
                if others:
                    if p["B1"] in others:metrics["correct_partner"]+=1
                    else:metrics["wrong_partner"]+=1
                else:metrics["false_singleton_alert"]+=1
            elif others:
                metrics["missed_positive"]+=1
        metrics["binary_loss_equal_cost"]=(
          metrics["false_singleton_alert"]+
          metrics["wrong_partner"]+
          metrics["missed_positive"])
        assert (metrics["correct_partner"]+metrics["wrong_partner"]+
                metrics["missed_positive"]==positive)
        assert metrics["false_singleton_alert"]<=metrics["singleton"]
        decisions[policy]=metrics
    assert decisions["always"]["correct_partner"]==9
    assert decisions["always"]["false_singleton_alert"]==34
    assert decisions["never"]["alerts"]==0
    assert decisions["half"]["alerts"]<decisions["always"]["alerts"]
    return decisions

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--original",required=True)
    ap.add_argument("--seal",required=True)
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    m=json.loads(Path(a.seal).read_text())
    assert m["Original"]==SOURCE
    assert m["Cutoff"]=="2020-01-01T00:00:00Z"
    assert m["End"]=="2024-06-28T14:29:28Z"
    out={"source":SOURCE,"status":"EXPLORATORY_AFTER_AGGREGATE_REVIEW",
         "training_frozen_original":m["TrainingSource"],
         "policies":assess(read_heldout(a.original),m)}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
