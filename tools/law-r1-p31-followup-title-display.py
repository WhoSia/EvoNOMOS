#!/usr/bin/env python3
"""P31 follow-up #173: bounded display-only title filtering on two real Go architectures.
No global persistence, workplace settings or end-user UI claim. Scratch source only.
"""
from pathlib import Path
import argparse,subprocess,json
ADDED=r'''// p31TitleVisibility is a display-only filter, NEVER an ingestion gate.
// Includes are OR, excludes are OR; explicit empty includes mean no restriction.
// Whole-word tokens use Unicode letter/digit boundaries, case-folded lowercase.
type p31TitleVisibility struct { Includes []string; Excludes []string }
func p31HasWholeWord(title, pattern string) bool {
 title, pattern = strings.ToLower(title), strings.ToLower(strings.TrimSpace(pattern))
 if pattern == "" { return false }
 isWord := func(r rune) bool { return unicode.IsLetter(r) || unicode.IsDigit(r) }
 for off := 0; off < len(title); {
  pos := strings.Index(title[off:],pattern)
  if pos < 0 { return false }
  lo := off + pos
  hi := lo + len(pattern)
  before := lo == 0
  if !before { prev, _ := utf8.DecodeLastRuneInString(title[:lo]); before = !isWord(prev) }
  after := hi == len(title)
  if !after { next, _ := utf8.DecodeRuneInString(title[hi:]); after = !isWord(next) }
  if before && after { return true }
  off = lo+1
 }
 return false
}
func p31TitleDisplayOnly(postings []store.Posting, rules p31TitleVisibility) ([]store.Posting,int) {
 visible := make([]store.Posting,0,len(postings))
 hidden := 0
 for _,p := range postings {
  included := len(rules.Includes)==0
  for _,v := range rules.Includes { if p31HasWholeWord(p.Title,v) {included=true;break} }
  for _,v := range rules.Excludes { if p31HasWholeWord(p.Title,v) {included=false;break} }
  if included {visible=append(visible,p)} else {hidden++}
 }
 return visible,hidden
}
'''
TEST=r'''package tui
import (
 "testing"
 "github.com/dklassen/swamp/store"
)
func TestP31TitleDisplayOnlyWordBounds(t *testing.T) {
 posts:=[]store.Posting{
  {IngestedFields:store.IngestedFields{Title:"Senior Engineer"}},
  {IngestedFields:store.IngestedFields{Title:"Engineering Manager"}},
  {IngestedFields:store.IngestedFields{Title:"Managerial Director"}},
  {IngestedFields:store.IngestedFields{Title:"Intern"}},
  {IngestedFields:store.IngestedFields{Title:"STAFF Engineer"}},
 }
 copyBefore:=append([]store.Posting(nil),posts...)
 only,hidden:=p31TitleDisplayOnly(posts,p31TitleVisibility{
  Includes:[]string{"engineer","staff"},Excludes:[]string{"manager"},
 })
 if len(only)!=2||hidden!=3||only[0].Title!="Senior Engineer"||only[1].Title!="STAFF Engineer" {
  t.Fatalf("visible=%+v hidden=%d",only,hidden)
 }
 if len(posts)!=len(copyBefore) {t.Fatal("display filter mutated ingestion snapshot")}
 for i:=range posts {if posts[i].Title!=copyBefore[i].Title {t.Fatal("mutated title")}}
 if !p31HasWholeWord("Manager-Engineer","engineer") {t.Fatal("hyphen should be boundary")}
 if p31HasWholeWord("Managerial Director","manager") {t.Fatal("partial match")}
 if !p31HasWholeWord("Senior Engineer","engineer") {t.Fatal("case-fold match")}
 if p31HasWholeWord("Engineer42","engineer") {t.Fatal("digit inside token")}
}
func TestP31TitleDisplayOnlyNilDefault(t *testing.T) {
 posts:=[]store.Posting{{IngestedFields:store.IngestedFields{Title:"Anything"}}}
 visible,hidden:=p31TitleDisplayOnly(posts,p31TitleVisibility{})
 if len(visible)!=1||hidden!=0 {t.Fatalf("default=%+v %d",visible,hidden)}
}
'''
def patch(root):
 f=root/"tui/app.go"
 s=f.read_text()
 import_line='\t"strings"\n'
 if import_line not in s: s=s.replace('import (\n','import (\n\t"strings"\n\t"unicode"\n\t"unicode/utf8"\n',1)
 else: s=s.replace('import (\n','import (\n\t"unicode"\n\t"unicode/utf8"\n',1)
 anchor="func loadPostings(s *store.Store, companyID int64, hideArchived bool) tea.Cmd {\n"
 if s.count(anchor)!=1:raise ValueError("loadPostings anchor invalid")
 replacement=ADDED+"\n"+anchor+''' return p31LoadPostingsWithTitleRules(s, companyID, hideArchived, p31TitleVisibility{})
}
func p31LoadPostingsWithTitleRules(s *store.Store, companyID int64, hideArchived bool, globalRules p31TitleVisibility) tea.Cmd {
'''
 s=s.replace(anchor,replacement,1)
 # Apply after already filtered company rules, before markup reads.
 mark="\n\t\tmarkup := make(map[int64]store.PostingMarkup, len(postings))"
 if s.count(mark)!=1:raise ValueError("markup anchor mismatch")
 s=s.replace(mark,"\n\t\tpostings, _ = p31TitleDisplayOnly(postings,globalRules)"+mark,1)
 f.write_text(s)
 test=root/"tui/p31_title_display_only_test.go"
 test.write_text(TEST)
 subprocess.run(["gofmt","-w",str(f),str(test)],check=True)
 return {"tree":str(root),"source":"tui/app.go","test":test.name,"only_display_path":True}
def main():
 p=argparse.ArgumentParser();p.add_argument("--direct",required=True);p.add_argument("--shared",required=True)
 a=p.parse_args()
 print(json.dumps({"status":"MATERIALIZED_NOT_YET_VERIFIED","source_issue":"dklassen/swamp#173","arms":[patch(Path(a.direct)),patch(Path(a.shared))]}))
if __name__=="__main__":main()
