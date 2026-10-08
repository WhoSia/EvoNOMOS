#!/usr/bin/env python3
"""P31 source-grounded fix for historical DIRECT display's Team-filter omission.
Scratch trees only; keeps DIRECT conversion local to TUI rather than moving
responsibility into the SHARED implementation.
"""
from pathlib import Path
import argparse, subprocess, json

DIRECT_FUNCTION = '''// p31DirectFilterPostings preserves this historical architecture's locally
// owned conversion of stored filter rows. It does not call sync.FilterRules.
func p31DirectFilterPostings(postings []store.Posting, filters []store.CompanyFilter) ([]store.Posting, error) {
    rules := make([]filter.Filter, 0, len(filters))
    for _, f := range filters {
        rules = append(rules, filter.Filter{Field: f.Field, Value: f.Value})
    }
    narrowed := make([]store.Posting, 0, len(postings))
    for _, p := range postings {
        match, err := filter.Match(filter.Posting{
            Department: p.Department, Location: p.Location, Team: p.Team,
        }, rules)
        if err != nil { return nil, err }
        if match { narrowed = append(narrowed, p) }
    }
    return narrowed, nil
}

'''
TEST_DIRECT='''package tui
import (
 "testing"
 "github.com/dklassen/swamp/store"
)
func TestP31PersistedTeamDisplayDirect(t *testing.T) {
 postings:=[]store.Posting{
  {IngestedFields:store.IngestedFields{Team:"Platform"}},
  {IngestedFields:store.IngestedFields{Team:"Infrastructure"}},
 }
 rules:=[]store.CompanyFilter{{Field:"team",Value:"platform"}}
 matched,err:=p31DirectFilterPostings(postings,rules)
 if err!=nil||len(matched)!=1||matched[0].Team!="Platform"{t.Fatalf("wrong persisted team display %+v %v",matched,err)}
}
'''
TEST_SHARED='''package tui
import (
 "testing"
 "github.com/dklassen/swamp/store"
)
func TestP31PersistedTeamDisplayShared(t *testing.T) {
 postings:=[]store.Posting{
  {IngestedFields:store.IngestedFields{Team:"Platform"}},
  {IngestedFields:store.IngestedFields{Team:"Infrastructure"}},
 }
 rules:=[]store.CompanyFilter{{Field:"team",Value:"platform"}}
 matched,err:=filterPostingsByCompanyFilters(postings,rules)
 if err!=nil||len(matched)!=1||matched[0].Team!="Platform"{t.Fatalf("wrong persisted team display %+v %v",matched,err)}
}
'''
def replace_once(path, a, b):
 s=path.read_text()
 if s.count(a)!=1:raise RuntimeError(f"Expected one anchor in {path}: got {s.count(a)}")
 path.write_text(s.replace(a,b,1))

def patch(root,variant):
 path=root/"tui/app.go"
 if variant=="DIRECT":
  replace_once(path,"postings = narrowPostingsToFilters(postings, departments, locations)",
    "postings, err = p31DirectFilterPostings(postings, companyFilters)\n\t\tif err != nil { return postingsLoadedMsg{err: err} }")
  before="func narrowPostingsToFilters(postings []store.Posting, departments, locations []string) []store.Posting {"
  replace_once(path,before,DIRECT_FUNCTION+before)
 else:
  if "postings, err = filterPostingsByCompanyFilters(postings, companyFilters)" not in path.read_text():raise RuntimeError("Shared source missing persisted filter path")
 file=root/"tui/p31_persisted_team_test.go"
 file.write_text(TEST_DIRECT if variant=="DIRECT" else TEST_SHARED)
 subprocess.run(["gofmt","-w",str(path),str(file)],check=True)
 return {"variant":variant,"display_path":"LOCAL_CONVERSION" if variant=="DIRECT" else "SHARED_SYNC_FILTER_RULES"}
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--direct",required=True);ap.add_argument("--shared",required=True)
 x=ap.parse_args()
 print(json.dumps({"status":"SOURCE_TREATMENT_NOT_YET_TESTED","arms":[patch(Path(x.direct),"DIRECT"),patch(Path(x.shared),"SHARED")]}))
if __name__=="__main__":main()
