package chi

// P13-R5: 1215 original Chi source repair paths and prospectively frozen
// composite-client goals; exact predictions were sealed at commit 32c6dd61
// BEFORE this file existed. 7 once-only research-owned Mount actions ONLY.
// Source-native read-only maintained Chi; unit Mount count is NOT human labor.
import (
 "encoding/json"
 "fmt"
 "os"
 "path/filepath"
 "strings"
 "testing"
)

type p13r5Receipt struct{
 From string `json:"from"`
 To string `json:"to"`
 Suffix string `json:"suffix"`
 StageOldSafe bool `json:"stage_old_safe"`
 Admitted bool `json:"admitted"`
 Error string `json:"error,omitempty"`
 Cost int `json:"cost"`
 GoalCD bool `json:"goal_cd"`
 GoalEC bool `json:"goal_ec"`
 GoalFD bool `json:"goal_fd"`
 GoalEF bool `json:"goal_ef"`
 Probes map[string]p13r2Probe `json:"probes"`
}
type p13r5World struct{
 Source string `json:"source"`
 Predicted map[string]string `json:"predicted"`
 Observed map[string]string `json:"observed"`
}
type p13r5Report struct{
 Protocol string `json:"protocol"`
 FrozenMathCommit string `json:"frozen_math_commit"`
 MaintainedChiCommit string `json:"maintained_chi_commit"`
 Worlds int `json:"worlds"`
 ReachablePairs int `json:"reachable_pairs"`
 NegativeControls int `json:"negative_controls"`
 ForecastCells int `json:"forecast_cells"`
 Disagreements int `json:"disagreements"`
 SourceOrOldFailures int `json:"source_or_old_failures"`
 FirstFailures []string `json:"first_failures"`
 WorldCosts []p13r5World `json:"world_costs"`
 ActualPaths []p13r5Receipt `json:"actual_paths"`
 Verdict string `json:"verdict"`
 Limits string `json:"limits"`
}
type p13r5State struct{ mask int; variant byte }
func (x p13r5State) name()string{
 var b strings.Builder
 labels:="ABCDG"
 for i:=0;i<5;i++{if x.mask&(1<<i)!=0{b.WriteByte(labels[i])}}
 if x.variant!='N'{b.WriteByte(x.variant)}
 if b.Len()==0{return "(empty)"}
 return b.String()
}
func p13r5States()[]p13r5State{
 out:=make([]p13r5State,0,96)
 for mask:=0;mask<32;mask++{
  for _,variant:=range []byte{'N','E','F'}{out=append(out,p13r5State{mask,variant})}
 }
 return out
}
func p13r5Reachable(x,y p13r5State)bool{
 if x.mask & y.mask != x.mask{return false}
 return x.variant=='N' || x.variant==y.variant
}
func p13r5Extensions(x,y p13r5State)string{
 var b strings.Builder
 labels:="ABCDG"
 for i:=0;i<5;i++{
  bit:=1<<i
  if (y.mask&bit)!=0 && (x.mask&bit)==0{b.WriteByte(labels[i])}
 }
 if x.variant=='N' && y.variant!='N'{b.WriteByte(y.variant)}
 return b.String()
}
func p13r5Edits()map[byte]p13Edit{
 edits:=[]p13Edit{
  {"A","/svc/a"},{"B","/svc/b"},
  {"C","/branch/one"},{"D","/branch/two"},
  {"E","/svc/{num:[0-9]+}"},{"F","/svc/{alpha:[a-z]+}"},
  {"G","/svc/a/deep"},
 }
 by:=map[byte]p13Edit{}
 for _,e:=range edits{by[e.Name[0]]=e}
 return by
}
func p13r5Build(x p13r5State,by map[byte]p13Edit)(Router,bool,string){
 r:=p13FreshParent()
 old:=p13OldOK(r)
 history:=x.name()
 if history=="(empty)"{history=""}
 for i:=0;i<len(history);i++{
  ok,reason:=p13Attempt(r,by[history[i]])
  if !ok{return r,false,fmt.Sprintf("initial step %c: %s",history[i],reason)}
  if !p13OldOK(r){old=false}
 }
 return r,old,""
}
func p13r5Good(p p13r2Probe,code int,body string)bool{
 return p.Code==code && (code==404 || p.Body==body) && !p.Flushed
}
func p13r5Probe(r Router)map[string]p13r2Probe{
 out:=map[string]p13r2Probe{}
 for _,path:=range []string{"/old","/branch/one/item","/branch/two/item","/svc/123/item","/svc/abc/item"}{
  out[path]=p13r2HTTP(r,path)
 }
 return out
}
func p13r5Goals(p map[string]p13r2Probe)[4]bool{
 c:=p13r5Good(p["/branch/one/item"],200,"C")
 d:=p13r5Good(p["/branch/two/item"],200,"D")
 e:=p13r5Good(p["/svc/123/item"],200,"E")
 f:=p13r5Good(p["/svc/abc/item"],200,"F")
 ne:=p13r5Good(p["/svc/123/item"],404,"")
 nf:=p13r5Good(p["/svc/abc/item"],404,"")
 old:=p13r5Good(p["/old"],200,"old")
 return [4]bool{old&&c&&d,old&&e&&nf&&c,old&&f&&ne&&d,old&&e&&f}
}
func p13r5Predicted(x p13r5State)[4]string{
 c:=1
 if x.mask & (1<<2)!=0{c=0}
 d:=1
 if x.mask & (1<<3)!=0{d=0}
 cd:=fmt.Sprint(c+d)
 ec:="INF"
 if x.variant!='F'{
  m:=c
  if x.variant=='N'{m++}
  ec=fmt.Sprint(m)
 }
 fd:="INF"
 if x.variant!='E'{
  m:=d
  if x.variant=='N'{m++}
  fd=fmt.Sprint(m)
 }
 return [4]string{cd,ec,fd,"INF"}
}
func p13r5CostString(n int)string{
 if n>7{return "INF"}
 return fmt.Sprint(n)
}
func TestEvoNOMOSP13R5OriginalChiCompositeCustomerAndExactRepairOptions(t *testing.T){
 states:=p13r5States()
 by:=p13r5Edits()
 report:=p13r5Report{
  Protocol:"EVONOMOS_G8_P42_R11_P10_P13_R5_PROSPECTIVE_COMPOSITE_CUSTOMER_GOALS",
  FrozenMathCommit:"32c6dd611edc70b88dd9aee816ee4c9e80c35354",
  MaintainedChiCommit:"167e1e3bd039d060696b99c8da4e876ae04f42c1",
  ActualPaths:[]p13r5Receipt{},WorldCosts:[]p13r5World{},FirstFailures:[]string{},
  Limits:"Research-owned 7 once-only source Mount edits, original maintained Chi unchanged; 5 old real HTTP probes, four new Boolean goals, unit added Mount cost not engineer labor; no upstream rights or unseen source edit class",
 }
 for _,x:=range states{
  initial,old,why:=p13r5Build(x,by)
  if why!=""||!old{
   report.SourceOrOldFailures++
   if len(report.FirstFailures)<12{report.FirstFailures=append(report.FirstFailures,"initial "+x.name()+" "+why)}
  }
  _=initial
  best:=[4]int{99,99,99,99}
  for _,y:=range states{
   if !p13r5Reachable(x,y){continue}
   report.ReachablePairs++
   r,safe,errText:=p13r5Build(x,by)
   if !safe || errText!="" {report.SourceOrOldFailures++}
   suffix:=p13r5Extensions(x,y)
   success:=errText==""
   for i:=0;i<len(suffix) && success;i++{
    ok,reason:=p13Attempt(r,by[suffix[i]])
    if !ok{success=false;errText=fmt.Sprintf("suffix %c: %s",suffix[i],reason)}
    if !p13OldOK(r){safe=false}
   }
   if !success||!safe{
    report.SourceOrOldFailures++
    if len(report.FirstFailures)<12{report.FirstFailures=append(report.FirstFailures,fmt.Sprintf("path %s->%s failure: %s safe=%v",x.name(),y.name(),errText,safe))}
   }
   p:=p13r5Probe(r)
   goals:=p13r5Goals(p)
   cost:=len(suffix)
   if success&&safe{
    for i,ok:=range goals{if ok&&cost<best[i]{best[i]=cost}}
   }
   report.ActualPaths=append(report.ActualPaths,p13r5Receipt{
    From:x.name(),To:y.name(),Suffix:suffix,StageOldSafe:safe,Admitted:success,Error:errText,Cost:cost,
    GoalCD:goals[0],GoalEC:goals[1],GoalFD:goals[2],GoalEF:goals[3],Probes:p,
   })
  }
  pred:=p13r5Predicted(x)
  names:=[4]string{"g_CD","g_EC","g_FD","g_EF"}
  expected:=map[string]string{}
  observed:=map[string]string{}
  for i,goal:=range names{
   report.ForecastCells++
   expected[goal]=pred[i]
   observed[goal]=p13r5CostString(best[i])
   if expected[goal]!=observed[goal]{
    report.Disagreements++
    if len(report.FirstFailures)<12{
     report.FirstFailures=append(report.FirstFailures,fmt.Sprintf("goal mismatch x=%s goal=%s predicted=%s actual=%s",x.name(),goal,pred[i],observed[goal]))
    }
   }
  }
  report.WorldCosts=append(report.WorldCosts,p13r5World{Source:x.name(),Predicted:expected,Observed:observed})
 }
 for mask:=0;mask<32;mask++{
  for _,variant:=range []byte{'E','F'}{
   x:=p13r5State{mask,variant}
   r,safe,why:=p13r5Build(x,by)
   if !safe||why!=""{report.SourceOrOldFailures++}
   target:=byte('F')
   if variant=='F'{target='E'}
   ok,_:=p13Attempt(r,by[target])
   report.NegativeControls++
   if ok{
    report.SourceOrOldFailures++
    if len(report.FirstFailures)<12{report.FirstFailures=append(report.FirstFailures,fmt.Sprintf("mutual exclusion violated %s+%c",x.name(),target))}
   }
  }
 }
 report.Worlds=len(report.WorldCosts)
 report.Verdict="P13_R5_PRESEALED_COMPOSITE_REPAIR_PREDICTION_FALSIFIED_PRESERVE_SOURCE_WITNESS"
 if report.Worlds==96&&report.ReachablePairs==1215&&
    report.NegativeControls==64&&report.ForecastCells==384&&
    report.Disagreements==0&&report.SourceOrOldFailures==0{
  report.Verdict="PASS_P13_R5_ORIGINAL_CHI_1215_FUTURE_REPAIRS_384_COMPOSITE_GOALS"
 }
 dir:="out/p42-r11-p10-p13-r5"
 if err:=os.MkdirAll(dir,0755);err!=nil{t.Fatal(err)}
 raw,err:=json.MarshalIndent(report,"","  ");if err!=nil{t.Fatal(err)}
 if err:=os.WriteFile(filepath.Join(dir,"source-native-1215-paths-composite-repair-cost.json"),append(raw,'\n'),0644);err!=nil{t.Fatal(err)}
 t.Logf("P13_R5_REAL_CHI_REPAIR: worlds=%d reached_pairs=%d exact_goal_cells=%d blocked_controls=%d errors=%d source_errors=%d verdict=%s",
   report.Worlds,report.ReachablePairs,report.ForecastCells,report.NegativeControls,report.Disagreements,report.SourceOrOldFailures,report.Verdict)
 if report.Verdict!="PASS_P13_R5_ORIGINAL_CHI_1215_FUTURE_REPAIRS_384_COMPOSITE_GOALS"{
  t.Fatalf("Presealed source composite repair forecast fails: first_falsifiers=%v (full JSON preserved)",report.FirstFailures)
 }
}
