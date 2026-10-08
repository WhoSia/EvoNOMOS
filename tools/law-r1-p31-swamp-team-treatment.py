#!/usr/bin/env python3
"""Frozen P31 programmatic Team-filter treatment; disposable upstream worktrees only.
Partial realization by design: does not claim the full TUI/schema rollout.
"""
from pathlib import Path
import argparse
import subprocess
import json

def replace_once(path, before, after):
    text=path.read_text()
    n=text.count(before)
    if n!=1:raise RuntimeError(f"{path}: expected one anchor, observed {n}: {before[:75]!r}")
    path.write_text(text.replace(before,after,1))

def patch(root, variant):
    assert variant in ("DIRECT","SHARED")
    p=root/"filter/filter.go"
    replace_once(p,"type Posting struct {\n\tDepartment string\n\tLocation   string\n}",
                 "type Posting struct {\n\tDepartment string\n\tLocation   string\n\tTeam       string\n}")
    if variant=="SHARED":
        replace_once(p,'\tFieldLocation   = "location"', '\tFieldLocation   = "location"\n\tFieldTeam       = "team"')
        replace_once(p,'\tFieldLocation:   func(p Posting) string { return p.Location },',
                     '\tFieldLocation:   func(p Posting) string { return p.Location },\n\tFieldTeam:       func(p Posting) string { return p.Team },')
    else:
        replace_once(p,'\t"location":   func(p Posting) string { return p.Location },',
                     '\t"location":   func(p Posting) string { return p.Location },\n\t"team":       func(p Posting) string { return p.Team },')
    sy=root/"sync/company.go"
    replace_once(sy,"filter.Posting{Department: p.Department, Location: p.Location}",
                 "filter.Posting{Department: p.Department, Location: p.Location, Team: p.Team}")
    tui=root/"tui/app.go"
    replace_once(tui,"filter.Posting{Department: p.Department, Location: p.Location}",
                 "filter.Posting{Department: p.Department, Location: p.Location, Team: p.Team}")
    test=root/"filter/p31_team_test.go"
    test.write_text('''package filter
import "testing"
func TestP31TeamMatching(t *testing.T) {
 cases := []struct {
  name string
  p Posting
  rules []Filter
  want bool
 }{
  {"team_match_case_insensitive", Posting{Department:"Engineering",Location:"Remote",Team:"Platform"}, []Filter{{Field:"team",Value:"platform"}}, true},
  {"team_mismatch", Posting{Team:"Infrastructure"}, []Filter{{Field:"team",Value:"Platform"}}, false},
  {"three_fields_and", Posting{Department:"Engineering",Location:"Remote",Team:"Platform"}, []Filter{{Field:"department",Value:"Engineering"},{Field:"location",Value:"Remote"},{Field:"team",Value:"Platform"}}, true},
  {"three_fields_one_mismatch", Posting{Department:"Engineering",Location:"Remote",Team:"Infrastructure"}, []Filter{{Field:"department",Value:"Engineering"},{Field:"location",Value:"Remote"},{Field:"team",Value:"Platform"}}, false},
 }
 for _, c := range cases {t.Run(c.name,func(t *testing.T){ got, err := Match(c.p,c.rules);if err!=nil || got!=c.want {t.Fatalf("got %v %v, want %v",got,err,c.want)}})}
}
''')
    subprocess.run(["gofmt","-w",str(p),str(sy),str(tui),str(test)],check=True)
    changed=subprocess.check_output(["git","-C",str(root),"status","--short"],text=True).splitlines()
    return {"variant":variant,"changes":changed,"runtime_code_treatment":"FILTER_MATCH_AND_TWO_CONSUMER_CONVERSION_ONLY","full_store_migration":False,"full_ui":False}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--direct",required=True)
    ap.add_argument("--shared",required=True)
    args=ap.parse_args()
    out=[patch(Path(args.direct),"DIRECT"),patch(Path(args.shared),"SHARED")]
    print(json.dumps({"stage":"LAW-R1-P31","status":"PARTIAL_REAL_CODE_TREATMENTS_READY_FOR_GO_TEST","arms":out,"mainline_claim":False},indent=2))
if __name__=="__main__": main()
