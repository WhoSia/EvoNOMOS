"""Narrow source-custody verification against exact Restic 2024 original.

This is NOT a proof of absence of all possible billing information in the
whole upstream software. Checks only declared data entry points and visible
source control flow at the pinned 2024 Git commit.
"""
from pathlib import Path
import argparse
import json
import re
import subprocess

PINNED="495982232cf1af184eac0a97871ef8161e8708ee"

def text_block(src: str, marker: str) -> str:
    start=src.find(marker)
    if start < 0:
        raise ValueError("Missing exact source marker: " + marker)
    end=src.find("\nfunc ",start+len(marker))
    if end < 0:
        end=len(src)
    return src[start:end]

def analyze(root: Path) -> dict:
    actual=subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"],text=True).strip()
    if actual != PINNED:
        raise ValueError("Upstream source changed: " + actual)
    cli=(root/"cmd/restic/cmd_prune.go").read_text()
    backend=(root/"internal/restic/backend.go").read_text()
    repack=(root/"internal/repository/repack.go").read_text()
    opts=text_block(cli,"type PruneOptions struct {").split("\n}",1)[0]
    planner=text_block(cli,"func planPrune(")
    selector=text_block(cli,"func decidePackAction(")
    interface=text_block(backend,"type Backend interface {").split("\n}",1)[0]
    if "decidePackAction(ctx, opts, repo, indexPack" not in planner:
        raise ValueError("prune selection entry changed")
    for expected in ("repo.List(","opts.maxUnusedBytes","repackCandidates"):
        if expected not in selector:
            raise ValueError("selection source missing "+expected)
    for expected in ("Save(ctx","Load(ctx","Stat(ctx","List(ctx","Remove(ctx"):
        if expected not in interface:
            raise ValueError("old backend interface changed: "+expected)
    if "func Repack(" not in repack:
        raise ValueError("repack execution site changed")
    economics_keywords=("billing","retention","price","monthly","storageclass")
    fields=opts.lower()
    explicit_fields=[term for term in economics_keywords if term in fields]
    return {
        "original_restic_source_commit": actual,
        "cli_file": "cmd/restic/cmd_prune.go",
        "policy_selector": "decidePackAction",
        "selection_calls_repo_list": True,
        "selection_uses_max_unused": True,
        "repack_execution_file": "internal/repository/repack.go",
        "backend_interface_file": "internal/restic/backend.go",
        "explicit_economic_metadata_terms_in_PruneOptions":explicit_fields,
        "interpretation_limit":"This syntactic check is not a full dataflow proof or upstream repair experiment."
    }

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--root",required=True,type=Path)
    a=p.parse_args()
    out=analyze(a.root)
    print(json.dumps(out,sort_keys=True,indent=2))
