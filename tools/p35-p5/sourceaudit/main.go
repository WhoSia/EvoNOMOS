// P35-P5 source-mechanism audit: post-score exploratory, NEVER an input
// to the sealed B0+/B1/B2 heldout predictions.
package main

import (
 "bytes"
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "flag"
 "fmt"
 "go/format"
 "go/parser"
 "go/token"
 "os"
 "os/exec"
 "sort"
 "strings"
)

const original="67be7d9cafdaeb4e04e887ff78d09e030ee43b00"
var targets=[]string{"mux.go","tree.go","context.go"}
type Row struct {
 Commit string
 Changed []string
 ASTChanged []string
 OnlySourceEquivalent []string
}
type Report struct {
 Provenance string
 Nature string
 CandidateCommits int
 TargetCochangeCommits int
 ASTCochangeCommits int
 Rows []Row
 Warnings []string
}
func git(repo string, args ...string)(string,error){
 c:=exec.Command("git",append([]string{"-C",repo},args...)...)
 b,e:=c.CombinedOutput();if e!=nil{return "",fmt.Errorf("git %s %w: %s",strings.Join(args," "),e,string(b))};return strings.TrimSpace(string(b)),nil
}
func norm(text string)(string,error){
 fset:=token.NewFileSet()
 f,e:=parser.ParseFile(fset,"source.go",text,0);if e!=nil{return "",e}
 b:=new(bytes.Buffer)
 e=format.Node(b,fset,f)
 if e!=nil{return "",e}
 return b.String(),nil
}
func read(repo,rev,path string)(string,error){return git(repo,"show",rev+":"+path)}
func run(repo string)(Report,error){
 h,e:=git(repo,"rev-parse","HEAD");if e!=nil{return Report{},e};if h!=original{return Report{},fmt.Errorf("unpinned original %s",h)}
 sh,e:=git(repo,"rev-parse","--is-shallow-repository");if e!=nil{return Report{},e};if sh!="false"{return Report{},fmt.Errorf("full history required")}
 args:=[]string{"log","--no-merges","--format=%H","--since=2020-01-01T00:00:00Z","--before=2024-06-28T14:29:28Z","HEAD","--"}
 args=append(args,targets...)
 raw,e:=git(repo,args...);if e!=nil{return Report{},e}
 report:=Report{Provenance:"Original go-chi/chi@"+original+"; post-score exploration only",Nature:"AST source changed differs from required semantic coupling. Go AST no-comments + format.Node.",Rows:[]Row{},Warnings:[]string{"AST shape change is not causally necessary joint modification.","Examples chosen after heldout scoring; never score as out-of-sample predictor.","Formatting/field layout shifts may change AST but not functional contracts."}}
 for _,rev:=range strings.Fields(raw){
  report.CandidateCommits++
  paths,e:=git(repo,"diff-tree","--no-commit-id","--name-only","-r",rev);if e!=nil{return Report{},e}
  touched:=[]string{}
  for _,f:=range targets{
   for _,v:=range strings.Split(paths,"\n"){if v==f {touched=append(touched,f);break}}
  }
  if len(touched)<2{continue}
  report.TargetCochangeCommits++
  row:=Row{Commit:rev,Changed:touched,ASTChanged:[]string{},OnlySourceEquivalent:[]string{}}
  for _,f:=range touched{
   before,e:=read(repo,rev+"^",f);if e!=nil{return Report{},e}
   after,e:=read(repo,rev,f);if e!=nil{return Report{},e}
   n0,e:=norm(before);if e!=nil{return Report{},e}
   n1,e:=norm(after);if e!=nil{return Report{},e}
   if n0!=n1{row.ASTChanged=append(row.ASTChanged,f)}else{row.OnlySourceEquivalent=append(row.OnlySourceEquivalent,f)}
  }
  if len(row.ASTChanged)>=2{report.ASTCochangeCommits++}
  report.Rows=append(report.Rows,row)
 }
 sort.Slice(report.Rows,func(i,j int)bool{return report.Rows[i].Commit<report.Rows[j].Commit})
 return report,nil
}
func main(){
 repo:=flag.String("repo","","chi clone");out:=flag.String("out","","json path");flag.Parse()
 if *repo==""||*out==""{panic("repo/out required")}
 r,e:=run(*repo);if e!=nil{panic(e)}
 data,e:=json.MarshalIndent(r,"","  ");if e!=nil{panic(e)}
 if e=os.WriteFile(*out,append(data,'\n'),0644);e!=nil{panic(e)}
 sum:=sha256.Sum256(data)
 fmt.Printf("P35P5_POSTSCORE_GO_AST_AUDIT total=%d core_coupled=%d AST_multi=%d sha256=%s\n",r.CandidateCommits,r.TargetCochangeCommits,r.ASTCochangeCommits,hex.EncodeToString(sum[:]))
 for _,x:=range r.Rows{fmt.Printf("P35P5_SOURCE_PATCH %s changed=%v ast=%v syntax_equivalent=%v\n",x.Commit[:12],x.Changed,x.ASTChanged,x.OnlySourceEquivalent)}
}
