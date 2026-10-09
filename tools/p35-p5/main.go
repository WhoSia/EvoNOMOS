// EvoNOMOS P35-P5. Go-native, deterministic source/history change prediction.
// Training must never read heldout co-change labels; evaluated runs require
// a byte-exact human-authored frozen model and reconstruct it before scoring.
package main

import (
 "bytes"
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "errors"
 "flag"
 "fmt"
 "go/ast"
 "go/parser"
 "go/token"
 "os"
 "os/exec"
 "sort"
 "strings"
)

const original = "67be7d9cafdaeb4e04e887ff78d09e030ee43b00"
const cutoff = "2020-01-01T00:00:00Z"
const end = "2024-06-28T14:29:28Z"
var triad=[]string{"mux.go","tree.go","context.go"}
var b2=map[string]string{"mux.go":"tree.go","tree.go":"context.go","context.go":"mux.go"}

type Prediction struct {
 B0 string
 B1 string
 B2 string
 B1SeedEvents int
 B1PairEvents int
 B1Conditional float64
 B1Abstain bool
 StaticScores map[string]int
}
type Seal struct {
 Original string
 Cutoff string
 End string
 TrainingSource string
 TrainingEvents int
 TrainingMulti int
 SelectionCaveat string
 B0Caveat string
 B1Caveat string
 B2Caveat string
 Predict map[string]Prediction
}
type Metric struct {
 Name string
 Total int
 Positives int
 Top1Hits int
 Singletons int
 SingletonAlerts int
 Abstentions int
}
type Evaluation struct {
 FrozenSHA256 string
 HeldoutCommits int
 HeldoutMultiCommits int
 SeedQueries int
 DisagreementQueries int
 Metrics []Metric
 PositiveCommitSHAs []string
 Verdict string
}
func git(root string, args ...string)(string,error){
 cmd:=exec.Command("git",append([]string{"-C",root},args...)...)
 b,e:=cmd.CombinedOutput()
 if e!=nil{return "",fmt.Errorf("git %s: %w (%s)",strings.Join(args," "),e,string(b))}
 return strings.TrimSpace(string(b)),nil
}
func check(root string)error{
 h,e:=git(root,"rev-parse","HEAD");if e!=nil{return e}
 if h!=original{return fmt.Errorf("wrong original chi SHA: %s",h)}
 // Full history is required; a shallow checkout must not fake B1 training.
 if _,e=git(root,"rev-parse","--is-shallow-repository");e!=nil{return e}
 s,_:=git(root,"rev-parse","--is-shallow-repository")
 if s=="true"{return errors.New("shallow clone forbidden")}
 return nil
}
func history(root,begin,until string)([][]string,error){
 args:=[]string{"log","--no-merges","--format=%H","--before="+until}
 if begin!=""{args=append(args,"--since="+begin)}
 args=append(args,"HEAD","--")
 args=append(args,triad...)
 raw,e:=git(root,args...);if e!=nil{return nil,e}
 ret:=[][]string{}
 for _,sha:=range strings.Fields(raw){
  paths,e:=git(root,"diff-tree","--no-commit-id","--name-only","-r",sha)
  if e!=nil{return nil,e}
  touched:=map[string]bool{}
  for _,p:=range strings.Split(paths,"\n"){touched[p]=true}
  row:=[]string{sha}
  for _,p:=range triad{if touched[p]{row=append(row,p)}}
  if len(row)>1{ret=append(ret,row)}
 }
 return ret,nil
}
func symbols(root,rev,name string)(map[string]bool,*ast.File,error){
 raw,e:=git(root,"show",rev+":"+name);if e!=nil{return nil,nil,e}
 f,e:=parser.ParseFile(token.NewFileSet(),name,raw,0);if e!=nil{return nil,nil,e}
 syms:=map[string]bool{}
 for _,n:=range f.Decls{
  switch d:=n.(type){
  case *ast.FuncDecl:if d.Recv==nil{syms[d.Name.Name]=true}
  case *ast.GenDecl:for _,sp:=range d.Specs{switch s:=sp.(type){
   case *ast.TypeSpec:syms[s.Name.Name]=true
   case *ast.ValueSpec:for _,v:=range s.Names{syms[v.Name]=true}
  }}
  }
 }
 return syms,f,nil
}
func staticGraph(root,revision string)(map[string]map[string]int,error){
 decl:=map[string]map[string]bool{}
 fs:=map[string]*ast.File{}
 for _,p:=range triad{
  syms,f,e:=symbols(root,revision,p);if e!=nil{return nil,e}
  decl[p]=syms;fs[p]=f
 }
 m:=map[string]map[string]int{}
 for _,from:=range triad{
  m[from]=map[string]int{}
  for _,to:=range triad{
   if from==to{continue}
   count:=0
   ast.Inspect(fs[from],func(n ast.Node)bool{
    if id,ok:=n.(*ast.Ident);ok&&decl[to][id.Name]{count++}
    return true
   })
   m[from][to]=count
  }
 }
 return m,nil
}
func pick(seed string,values map[string]int)(string,int){
 best:="";n:=-1
 for _,v:=range triad{
  if v==seed{continue}
  if values[v]>n||(values[v]==n&&(best==""||v<best)){best=v;n=values[v]}
 }
 return best,n
}
func model(root string)(Seal,error){
 if e:=check(root);e!=nil{return Seal{},e}
 // Both calls are bounded by 2020: NO postcutoff joint labels in training.
 rows,e:=history(root,"",cutoff);if e!=nil{return Seal{},e}
 trainRev,e:=git(root,"rev-list","-1","--before="+cutoff,"HEAD");if e!=nil{return Seal{},e}
 graph,e:=staticGraph(root,trainRev);if e!=nil{return Seal{},e}
 seeds:=map[string]int{}
 pair:=map[string]map[string]int{}
 for _,p:=range triad{pair[p]=map[string]int{}}
 positives:=0
 for _,row:=range rows{
  if len(row)>=3{positives++}
  for _,p:=range row[1:]{seeds[p]++;for _,q:=range row[1:]{if p!=q{pair[p][q]++}}}
 }
 s:=Seal{Original:original,Cutoff:cutoff,End:end,TrainingSource:trainRev,TrainingEvents:len(rows),TrainingMulti:positives,Predict:map[string]Prediction{},
 SelectionCaveat:"Triad and cutoff selected after total path-count scouting, including postcutoff aggregate counts and a few titles. Joint labels not consulted. NOT fully untouched holdout.",
 B0Caveat:"Go AST cross-file package-declaration identifier overlap at train cutoff; no symbol-resolved SSA/full CSDG. Lexicographic ties.",
 B1Caveat:"Real nonmerge git path cochange from before 2020. Top conditional count; abstain if seed <5 or frequency <0.10.",
 B2Caveat:"Predeclared Parnas-style qualitative mapping, NOT full DRSpaces/CSDG: mux->tree, tree->context, context->mux."}
 for _,seed:=range triad{
  values:=map[string]int{}
  for _,v:=range triad{if seed!=v{values[v]=graph[seed][v]+graph[v][seed]}}
  p0,_:=pick(seed,values);p1,n:=pick(seed,pair[seed])
  cond:=0.0;if seeds[seed]>0{cond=float64(n)/float64(seeds[seed])}
  s.Predict[seed]=Prediction{B0:p0,B1:p1,B2:b2[seed],B1SeedEvents:seeds[seed],B1PairEvents:n,B1Conditional:cond,B1Abstain:seeds[seed]<5||cond<0.10,StaticScores:values}
 }
 return s,nil
}
func marshal(v any)[]byte{
 b,e:=json.MarshalIndent(v,"","  ");if e!=nil{panic(e)}
 return b
}
func score(root string,s Seal,hash string)(Evaluation,error){
 rows,e:=history(root,cutoff,end);if e!=nil{return Evaluation{},e}
 names:=[]string{"B0plus_AST","B1_historical","B2_information_hiding"}
 metrics:=map[string]*Metric{}
 for _,name:=range names{metrics[name]=&Metric{Name:name}}
 result:=Evaluation{FrozenSHA256:hash,HeldoutCommits:len(rows),PositiveCommitSHAs:[]string{},Metrics:[]Metric{},Verdict:"HISTORICAL_COHANGE_SCORE_ONLY__NO_CAUSAL_NECESSITY_OR_NOVEL_SOLID_LAW"}
 for _,row:=range rows{
  if len(row)>2{result.HeldoutMultiCommits++;result.PositiveCommitSHAs=append(result.PositiveCommitSHAs,row[0])}
  for _,seed:=range row[1:]{
   result.SeedQueries++
   truth:=map[string]bool{}
   for _,v:=range row[1:]{if v!=seed{truth[v]=true}}
   p:=s.Predict[seed]
   if p.B0!=p.B1||p.B1!=p.B2{result.DisagreementQueries++}
   chosen:=map[string]string{"B0plus_AST":p.B0,"B1_historical":p.B1,"B2_information_hiding":p.B2}
   for _,name:=range names{
    m:=metrics[name];m.Total++
    if len(truth)>0{m.Positives++}else{m.Singletons++}
    if name=="B1_historical"&&p.B1Abstain{m.Abstentions++;continue}
    if truth[chosen[name]]{m.Top1Hits++}else if len(truth)==0{m.SingletonAlerts++}
   }
  }
 }
 for _,name:=range names{result.Metrics=append(result.Metrics,*metrics[name])}
 sort.Strings(result.PositiveCommitSHAs)
 return result,nil
}
func main(){
 mode:=flag.String("mode","train","train or evaluate")
 root:=flag.String("repo","","actual full-history original chi checkout")
 output:=flag.String("out","","JSON output")
 frozen:=flag.String("seal","","human-committed JSON model for evaluation")
 flag.Parse()
 if *root==""||*output==""{panic("repo/out required")}
 s,e:=model(*root);if e!=nil{panic(e)}
 data:=marshal(s)
 if *mode=="train"{
  if *frozen!=""{panic("train must not access seal or heldout")}
  if e=os.WriteFile(*output,append(data,'\n'),0644);e!=nil{panic(e)}
  compact,_:=json.Marshal(s)
  fmt.Println("P35P5_TRAIN_ONLY_PASS train_commits=",s.TrainingEvents,"multi=",s.TrainingMulti)
  fmt.Println("P35P5_SEALED_MODEL_JSON="+string(compact))
  return
 }
 if *mode!="evaluate"||*frozen==""{panic("evaluate requires a committed --seal")}
 sealed,e:=os.ReadFile(*frozen);if e!=nil{panic(e)}
 if !bytes.Equal(bytes.TrimSpace(sealed),data){panic("P35P5_TRAINING_SEAL_MISMATCH__NO_HELDOUT_OPENED")}
 hash:=sha256.Sum256(data)
 r,e:=score(*root,s,hex.EncodeToString(hash[:]));if e!=nil{panic(e)}
 if e=os.WriteFile(*output,append(marshal(r),'\n'),0644);e!=nil{panic(e)}
 fmt.Printf("P35P5_EVALUATED heldout=%d positive_commits=%d seed_queries=%d disagreements=%d\n",r.HeldoutCommits,r.HeldoutMultiCommits,r.SeedQueries,r.DisagreementQueries)
 for _,m:=range r.Metrics{fmt.Printf("P35P5_MODEL %s positive=%d hits=%d singletons=%d alerts=%d abstains=%d\n",m.Name,m.Positives,m.Top1Hits,m.Singletons,m.SingletonAlerts,m.Abstentions)}
}
