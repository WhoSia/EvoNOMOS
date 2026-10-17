package chi

// P13-R4: genuine original-source costed source-repair reachability for
// numeric/alpha client goals. Hypothesis frozen at commit 41b8be8e BEFORE test.
// Synthetic unit handler-edit cost, NOT measured human labor or upstream rights.
import (
 "encoding/json"
 "fmt"
 "net/http"
 "os"
 "path/filepath"
 "strings"
 "testing"
)
type p13r4Case struct{
 OtherSet string `json:"other_set"`
 Variant string `json:"variant"`
 SourceHistory string `json:"source_history"`
 ActualOldClientAllStages bool `json:"old_client_safe_at_every_stage"`
 Numeric p13r2Probe `json:"numeric"`
 Alpha p13r2Probe `json:"alpha"`
 PredictedNumericCost string `json:"predicted_numeric_cost"`
 PredictedAlphaCost string `json:"predicted_alpha_cost"`
 NativeFailures []string `json:"native_failures"`
}
type p13r4Report struct{
 Protocol string `json:"protocol"`
 TheoryFrozenCommit string `json:"theory_frozen_commit"`
 OriginalSourceCommit string `json:"original_source_commit"`
 Worlds int `json:"worlds"`
 Triples int `json:"triples"`
 NoneToE int `json:"none_to_e_success"`
 NoneToF int `json:"none_to_f_success"`
 EToFRejected int `json:"e_to_f_rejected"`
 FToERejected int `json:"f_to_e_rejected"`
 Failures int `json:"failures"`
 Cases []p13r4Case `json:"cases"`
 Verdict string `json:"verdict"`
 Limits string `json:"limits"`
}
func p13r4Build(T string,variant byte,by map[byte]p13Edit)(Router,bool,string){
 r:=p13FreshParent()
 oldOK:=p13OldOK(r)
 history:=T
 if variant!='N'{history+=string(variant)}
 for i:=0;i<len(history);i++ {
  ok,why:=p13Attempt(r,by[history[i]])
  if !ok{return r,false,history[:i]+": "+why}
  if !p13OldOK(r){oldOK=false}
 }
 return r,oldOK,""
}
func p13r4NumericGood(n,a p13r2Probe)bool{
 return n.Code==200&&n.Body=="E"&&!n.Flushed&&a.Code==404&&!a.Flushed
}
func p13r4AlphaGood(n,a p13r2Probe)bool{
 return n.Code==404&&!n.Flushed&&a.Code==200&&a.Body=="F"&&!a.Flushed
}
func TestEvoNOMOSP13R4OriginalChiSyntheticMinimumSourceRepairCosts(t *testing.T){
 labels:=[]byte{'A','B','C','D','G'}
 edits:=[]p13Edit{
  {"A","/svc/a"},{"B","/svc/b"},{"C","/branch/one"},
  {"D","/branch/two"},{"E","/svc/{num:[0-9]+}"},
  {"F","/svc/{alpha:[a-z]+}"},{"G","/svc/a/deep"},
 }
 by:=map[byte]p13Edit{}
 for _,e:=range edits{by[e.Name[0]]=e}
 report:=p13r4Report{
  Protocol:"P42_R11_P10_P13_R4_NATIVE_ORIGINAL_CHI_COSTED_REPAIR_ZERO_ONE_INFINITY",
  TheoryFrozenCommit:"41b8be8e7e7463f679505a727951239cf04ef3a9",
  OriginalSourceCommit:"167e1e3bd039d060696b99c8da4e876ae04f42c1",
  Cases:[]p13r4Case{},
  Limits:"Only 32 T × 3 variants from original Chi; two concrete new client goals, synthetic 1-unit app-owned edit cost, not human labor/maintainer rights",
 }
 for mask:=0;mask<32;mask++{
  var b strings.Builder
  for i,label:=range labels{if mask&(1<<uint(i))!=0 {b.WriteByte(label)}}
  T:=b.String()
  report.Triples++
  for _,variant:=range []byte{'N','E','F'}{
   r,oldOK,errText:=p13r4Build(T,variant,by)
   caseInfo:=p13r4Case{OtherSet:T,Variant:string(variant),SourceHistory:T,
    ActualOldClientAllStages:oldOK,NativeFailures:[]string{}}
   if variant!='N'{caseInfo.SourceHistory+=string(variant)}
   if errText!=""{caseInfo.NativeFailures=append(caseInfo.NativeFailures,"preexisting_source_edit:"+errText)}
   if !oldOK{caseInfo.NativeFailures=append(caseInfo.NativeFailures,"old_client_stagewise_violation")}
   caseInfo.Numeric=p13r2HTTP(r,"/svc/123/item")
   caseInfo.Alpha=p13r2HTTP(r,"/svc/abc/item")
   old:=p13r2HTTP(r,"/old")
   if old.Code!=http.StatusOK||old.Body!="old"||old.Flushed{
    caseInfo.NativeFailures=append(caseInfo.NativeFailures,"old_client_final_violation")
   }
   switch variant{
   case 'N':
    caseInfo.PredictedNumericCost="1"
    caseInfo.PredictedAlphaCost="1"
    if caseInfo.Numeric.Code!=404||caseInfo.Numeric.Flushed||
       caseInfo.Alpha.Code!=404||caseInfo.Alpha.Flushed{
      caseInfo.NativeFailures=append(caseInfo.NativeFailures,"none_should_start_with_no_numeric_or_alpha_route")
    }
    // Both one-edit repairs are witnessed in separately reconstructed ORIGINAL app worlds.
    for _,target:=range []byte{'E','F'}{
     owned,older,why:=p13r4Build(T,'N',by)
     if why!=""||!older{caseInfo.NativeFailures=append(caseInfo.NativeFailures,"before_add_"+string(target)+":"+why)}
     success,reason:=p13Attempt(owned,by[target])
     if !success{caseInfo.NativeFailures=append(caseInfo.NativeFailures,"one_owned_edit_rejected_"+string(target)+":"+reason)}
     if !p13OldOK(owned){caseInfo.NativeFailures=append(caseInfo.NativeFailures,"old_after_owned_"+string(target))}
     n,a:=p13r2HTTP(owned,"/svc/123/item"),p13r2HTTP(owned,"/svc/abc/item")
     if target=='E' {
      if success&&p13r4NumericGood(n,a){report.NoneToE++}else{
       caseInfo.NativeFailures=append(caseInfo.NativeFailures,"one_step_E_not_repair")
      }
     }else{
      if success&&p13r4AlphaGood(n,a){report.NoneToF++}else{
       caseInfo.NativeFailures=append(caseInfo.NativeFailures,"one_step_F_not_repair")
      }
     }
    }
   case 'E':
    caseInfo.PredictedNumericCost="0"
    caseInfo.PredictedAlphaCost="INF"
    if !p13r4NumericGood(caseInfo.Numeric,caseInfo.Alpha){
     caseInfo.NativeFailures=append(caseInfo.NativeFailures,"E_world_zero_numeric_cost_goal_fails")
    }
    success,reason:=p13Attempt(r,by['F'])
    if !success{report.EToFRejected++}else{
     caseInfo.NativeFailures=append(caseInfo.NativeFailures,"forbidden_E_to_F_source_registration_succeeded")
    }
    _=reason
   case 'F':
    caseInfo.PredictedNumericCost="INF"
    caseInfo.PredictedAlphaCost="0"
    if !p13r4AlphaGood(caseInfo.Numeric,caseInfo.Alpha){
     caseInfo.NativeFailures=append(caseInfo.NativeFailures,"F_world_zero_alpha_cost_goal_fails")
    }
    success,reason:=p13Attempt(r,by['E'])
    if !success{report.FToERejected++}else{
     caseInfo.NativeFailures=append(caseInfo.NativeFailures,"forbidden_F_to_E_source_registration_succeeded")
    }
    _=reason
   }
   report.Failures+=len(caseInfo.NativeFailures)
   report.Cases=append(report.Cases,caseInfo)
  }
 }
 report.Worlds=len(report.Cases)
 report.Verdict="P13_R4_FROZEN_REPAIR_COST_FORECAST_FALSIFIED_PRESERVE_SOURCE_COUNTEREXAMPLE"
 if report.Worlds==96&&report.Triples==32&&report.NoneToE==32&&report.NoneToF==32&&
  report.EToFRejected==32&&report.FToERejected==32&&report.Failures==0{
  report.Verdict="PASS_ORIGINAL_CHI_32_STRATA_TWO_CLIENT_MIN_COST_0_1_INF"
 }
 folder:="out/p42-r11-p10-p13-r4"
 if err:=os.MkdirAll(folder,0755);err!=nil{t.Fatal(err)}
 raw,err:=json.MarshalIndent(report,"","  ");if err!=nil{t.Fatal(err)}
 if err=os.WriteFile(filepath.Join(folder,"original-chi-96-worlds-minimum-repair-cost.json"),append(raw,'\n'),0644);err!=nil{t.Fatal(err)}
 t.Logf("P13_R4_SOURCE_MIN_REPAIR_COSTS: worlds=%d strata=%d noneE=%d noneF=%d EtoFblocked=%d FtoEblocked=%d failures=%d verdict=%s",
   report.Worlds,report.Triples,report.NoneToE,report.NoneToF,
   report.EToFRejected,report.FToERejected,report.Failures,report.Verdict)
 if report.Verdict!="PASS_ORIGINAL_CHI_32_STRATA_TWO_CLIENT_MIN_COST_0_1_INF"{
  for i,c:=range report.Cases{if len(c.NativeFailures)>0 && i<100{t.Logf("P13_R4_ORIGINAL_SOURCE_FALSIFIER: %+v",c);break}}
  t.Fatalf("Presealed original-source costed repair hypothesis falsified; evidence preserved before failure")
 }
}
var _=fmt.Sprint
