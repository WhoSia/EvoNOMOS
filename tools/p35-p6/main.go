// EvoNOMOS P35-P6. Go-native operator-conditioned historical source prediction.
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
 "go/format"
 "go/parser"
 "go/token"
 "os"
 "os/exec"
 "sort"
 "strings"
)

const original = "e94f6d0dd9a5e5738dca6bce03c4b1207ffbc0ec"
const cutoff = "2021-01-01T00:00:00Z"
const end = "2024-06-01T10:31:12Z"
var triad=[]string{"command.go","args.go","cobra.go"}
var b2=map[string]string{"command.go":"args.go","args.go":"command.go","cobra.go":"command.go"}


const none = "NONE"
const abstain = "ABSTAIN"
var operators=[]string{"TYPE_SHAPE","FUNCTION_ONLY","NO_DECL_CHANGE"}

type Predictor struct {
 B0 string
 B1Operator string
 B1SeedOnly string
 B2 string
 SeedTraining int
 SeedMulti int
 OperatorTraining int
 OperatorMulti int
 OperatorRate float64
 B1Rank string
 B1RankPairCount int
 StaticScore int
}
type Seal struct {
 Original string
 Cutoff string
 End string
 TrainingRevision string
 TrainingEvents int
 TrainingMulti int
 Cohort []string
 OperatorPrecedence []string
 B1Threshold float64
 B1MinSamples int
 Predictions map[string]map[string]Predictor
 Limitations []string
}
type Metric struct{
 Model string
 Total int
 Positive int
 Singleton int
 PositiveHits int
 CorrectNone int
 SingletonFalseAlerts int
 PositiveMissNone int
 PositiveWrongPartner int
 Abstained int
}
type Eval struct{
 FrozenSHA256 string
 HeldoutEvents int
 HeldoutMultiEvents int
 SeedQueries int
 ByOperator map[string]int
 Counts []Metric
 InterModelDisagreements int
 EventSHAs []string
 Caveat string
}
func git(root string, args ...string)(string,error){
 cmd:=exec.Command("git",append([]string{"-C",root},args...)...)
 b,e:=cmd.CombinedOutput()
 if e!=nil{return "",fmt.Errorf("git %s: %w (%s)",strings.Join(args," "),e,string(b))}
 return strings.TrimSpace(string(b)),nil
}
func check(root string)error{
 h,e:=git(root,"rev-parse","HEAD");if e!=nil{return e}
 if h!=original{return fmt.Errorf("wrong original Cobra SHA: %s",h)}
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

// declarationFingerprints deliberately excludes comments, imports and local
// formatting. Method declarations count as functions; types include struct layout.
// This is not semantic or interface-compatibility checking.
func fingerprints(src string)(map[string]string,map[string]string,error){
 fs:=token.NewFileSet()
 file,err:=parser.ParseFile(fs,"seed.go",src,0)
 if err!=nil{return nil,nil,err}
 types:=map[string]string{}
 funcs:=map[string]string{}
 for _,d:=range file.Decls{
  if fn,ok:=d.(*ast.FuncDecl);ok {
   name:=fn.Name.Name
   if fn.Recv!=nil{
    var b bytes.Buffer
    if err=format.Node(&b,fs,fn.Recv.List[0].Type);err!=nil{return nil,nil,err}
    name=b.String()+"."+name
   }
   var b bytes.Buffer
   if err=format.Node(&b,fs,fn);err!=nil{return nil,nil,err}
   funcs[name]=b.String()
  }
  if gen,ok:=d.(*ast.GenDecl);ok{
   for _,sp:=range gen.Specs{
    if ts,ok:=sp.(*ast.TypeSpec);ok{
     var b bytes.Buffer
     if err=format.Node(&b,fs,ts);err!=nil{return nil,nil,err}
     types[ts.Name.Name]=b.String()
    }
   }
  }
 }
 return types,funcs,nil
}
func differs(a,b map[string]string)bool{
 if len(a)!=len(b){return true}
 for k,v:=range a{if b[k]!=v{return true}}
 return false
}
func classifyText(before,after string)(string,error){
 ta,fa,e:=fingerprints(before);if e!=nil{return "",e}
 tb,fb,e:=fingerprints(after);if e!=nil{return "",e}
 if differs(ta,tb){return "TYPE_SHAPE",nil}
 if differs(fa,fb){return "FUNCTION_ONLY",nil}
 return "NO_DECL_CHANGE",nil
}
func operator(root,rev,seed string)(string,error){
 before,e:=git(root,"show",rev+"^:"+seed)
 if e!=nil{before="package cobra\n"} // an added source file.
 after,e:=git(root,"show",rev+":"+seed)
 if e!=nil{return "",fmt.Errorf("cannot obtain changed seed source %s at %s: %w",seed,rev,e)}
 return classifyText(before,after)
}
func newMap()(map[string]map[string]int){
 m:=map[string]map[string]int{}
 for _,seed:=range triad{m[seed]=map[string]int{}}
 return m
}
func chosen(seed string,partners map[string]int)(string,int){
 best:="";count:=0
 for _,candidate:=range triad{
  if candidate==seed {continue}
  n:=partners[candidate]
  if best==""||n>count||(n==count&&candidate<best){best=candidate;count=n}
 }
 return best,count
}
func rate(positive,total int)float64{
 if total<=0{return 0}
 return float64(positive)/float64(total)
}
func b1Gate(total,multi int,rank string)string{
 if total<5{return abstain}
 if rate(multi,total)<0.5{return none}
 return rank
}
func selectedCandidates(seed,kind string,static map[string]int,rank,rankSeed string,total,multi,totalSeed,multiSeed int)(string,string,string,string,int){
 best,score:=chosen(seed,static)
 b0:=none
 if kind=="TYPE_SHAPE"&&score>0{b0=best}
 b1:=b1Gate(total,multi,rank)
 seedOnly:=b1Gate(totalSeed,multiSeed,rankSeed)
 b2p:=none
 if kind=="TYPE_SHAPE"{b2p=b2[seed]}
 return b0,b1,seedOnly,b2p,score
}
func model(root string)(Seal,error){
 if err:=check(root);err!=nil{return Seal{},err}
 rows,err:=history(root,"",cutoff);if err!=nil{return Seal{},err}
 rev,err:=git(root,"rev-list","-1","--before="+cutoff,"HEAD");if err!=nil{return Seal{},err}
 graph,err:=staticGraph(root,rev);if err!=nil{return Seal{},err}
 key:=func(s,o string)string{return s+"|"+o}
 counts:=map[string]int{}
 multis:=map[string]int{}
 pairs:=map[string]map[string]int{}
 seedCount:=map[string]int{}
 seedMulti:=map[string]int{}
 seedPairs:=newMap()
 nMulti:=0
 for _,row:=range rows{
  if len(row)>=3{nMulti++}
  for _,seed:=range row[1:]{
   op,err:=operator(root,row[0],seed);if err!=nil{return Seal{},fmt.Errorf("train operator %s %s: %w",row[0],seed,err)}
   k:=key(seed,op)
   counts[k]++;seedCount[seed]++
   if len(row)>2{multis[k]++;seedMulti[seed]++}
   if pairs[k]==nil{pairs[k]=map[string]int{}}
   for _,p:=range row[1:]{
    if p!=seed{pairs[k][p]++;seedPairs[seed][p]++}
   }
  }
 }
 s:=Seal{Original:original,Cutoff:cutoff,End:end,TrainingRevision:rev,
  TrainingEvents:len(rows),TrainingMulti:nMulti,Cohort:triad,
  OperatorPrecedence:operators,B1Threshold:0.5,B1MinSamples:5,
  Predictions:map[string]map[string]Predictor{},
  Limitations:[]string{
   "Real Git coedit is a proxy, not counterfactual necessity.",
   "Completed seed patch available to all models. Future companion patches hidden until seal verification.",
   "AST declaration changes do not prove public-contract change; three coarse operators.",
   "B0 lexical static link and B2 qualitative owner mapping are not full CSDG/DRSpaces.",
   "A commit may yield correlated multiple seed queries; no independence claim.",
  }}
 for _,seed:=range triad{
  s.Predictions[seed]=map[string]Predictor{}
  cross:=map[string]int{}
  for _,other:=range triad{if seed!=other{cross[other]=graph[seed][other]+graph[other][seed]}}
  rs,_:=chosen(seed,seedPairs[seed])
  for _,op:=range operators{
   k:=key(seed,op)
   rk,rc:=chosen(seed,pairs[k])
   b0,b1,seedOnly,b2p,sc:=selectedCandidates(seed,op,cross,rk,rs,counts[k],multis[k],seedCount[seed],seedMulti[seed])
   s.Predictions[seed][op]=Predictor{B0:b0,B1Operator:b1,B1SeedOnly:seedOnly,B2:b2p,
    SeedTraining:seedCount[seed],SeedMulti:seedMulti[seed],OperatorTraining:counts[k],OperatorMulti:multis[k],OperatorRate:rate(multis[k],counts[k]),
    B1Rank:rk,B1RankPairCount:rc,StaticScore:sc}
  }
 }
 return s,nil
}
func marshal(v any)[]byte{b,e:=json.MarshalIndent(v,"","  ");if e!=nil{panic(e)};return b}
func evaluate(root string,s Seal,digest string)(Eval,error){
 rows,e:=history(root,cutoff,end);if e!=nil{return Eval{},e}
 names:=[]string{"B0plus_AST_operator","B1_history_operator","B1_history_seed_only","B2_information_hiding","ALWAYS_NONE"}
 m:=map[string]*Metric{}
 for _,n:=range names{m[n]=&Metric{Model:n}}
 out:=Eval{FrozenSHA256:digest,HeldoutEvents:len(rows),ByOperator:map[string]int{},EventSHAs:[]string{},
  Caveat:"Changed file paths are historical observations not required repairs; all input seed patch operators are available before target companion labels are used."}
 for _,row:=range rows{
  if len(row)>2{out.HeldoutMultiEvents++}
  out.EventSHAs=append(out.EventSHAs,row[0])
  for _,seed:=range row[1:]{
   op,e:=operator(root,row[0],seed);if e!=nil{return Eval{},e}
   out.SeedQueries++;out.ByOperator[op]++
   p:=s.Predictions[seed][op]
   preds:=map[string]string{"B0plus_AST_operator":p.B0,"B1_history_operator":p.B1Operator,"B1_history_seed_only":p.B1SeedOnly,"B2_information_hiding":p.B2,"ALWAYS_NONE":none}
   got:=map[string]bool{}
   for _,other:=range row[1:]{if other!=seed{got[other]=true}}
   if p.B0!=p.B1Operator||p.B1Operator!=p.B2{out.InterModelDisagreements++}
   for _,name:=range names{
    q:=m[name];q.Total++
    if len(got)==0{q.Singleton++}else{q.Positive++}
    answer:=preds[name]
    if answer==abstain{q.Abstained++;continue}
    if len(got)==0{
     if answer==none{q.CorrectNone++}else{q.SingletonFalseAlerts++}
    }else{
     if answer==none{q.PositiveMissNone++}else if got[answer]{q.PositiveHits++}else{q.PositiveWrongPartner++}
    }
   }
  }
 }
 sort.Strings(out.EventSHAs)
 for _,n:=range names{out.Counts=append(out.Counts,*m[n])}
 return out,nil
}
func main(){
 mode:=flag.String("mode","train","train or evaluate")
 root:=flag.String("repo","","full-history pinned original Cobra")
 out:=flag.String("out","","output json path")
 seal:=flag.String("seal","","frozen WhoSia-authored Go training model")
 flag.Parse()
 if *root==""||*out==""{panic("repo and out required")}
 m,e:=model(*root);if e!=nil{panic(e)}
 b:=marshal(m)
 if *mode=="train"{
  if *seal!=""{panic("train-only mode cannot accept evaluation seal")}
  if e=os.WriteFile(*out,append(b,'\n'),0644);e!=nil{panic(e)}
  compact,_:=json.Marshal(m)
  fmt.Printf("P35P6_TRAIN_ONLY events=%d multi=%d\n",m.TrainingEvents,m.TrainingMulti)
  fmt.Println("P35P6_FROZEN_MODEL_JSON="+string(compact))
  return
 }
 if *mode!="evaluate"||*seal==""{panic("evaluate requires human frozen seal")}
 existing,e:=os.ReadFile(*seal);if e!=nil{panic(e)}
 if !bytes.Equal(bytes.TrimSpace(existing),b){panic("P35P6_FROZEN_MODEL_MISMATCH__HELDOUT_NOT_OPENED")}
 sha:=sha256.Sum256(b)
 scored,e:=evaluate(*root,m,hex.EncodeToString(sha[:]));if e!=nil{panic(e)}
 if e=os.WriteFile(*out,append(marshal(scored),'\n'),0644);e!=nil{panic(e)}
 fmt.Printf("P35P6_EVAL events=%d multi=%d queries=%d disagreements=%d operators=%v\n",scored.HeldoutEvents,scored.HeldoutMultiEvents,scored.SeedQueries,scored.InterModelDisagreements,scored.ByOperator)
 for _,x:=range scored.Counts{fmt.Printf("P35P6_MODEL %s hits=%d positives=%d correctNone=%d singleton=%d falseAlerts=%d missNone=%d wrongPartner=%d abstain=%d\n",x.Model,x.PositiveHits,x.Positive,x.CorrectNone,x.Singleton,x.SingletonFalseAlerts,x.PositiveMissNone,x.PositiveWrongPartner,x.Abstained)}
}
