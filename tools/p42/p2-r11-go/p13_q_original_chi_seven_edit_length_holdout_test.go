package chi

// P13-Q full-length heldout 7-edit grammar, complete source-native census.
// Math/counts fixed in ae04d558f8ed834901000a3baa521f87ed0910d6.
// This file is compiled together with the original P13 test *fixture*, but
// the Go/Chi maintained upstream router source is unchanged and pinned.
import (
    "encoding/json"
    "fmt"
    "os"
    "path/filepath"
    "testing"
)

type p13qSummary struct {
    Length int `json:"length"`
    Total int `json:"total"`
    PredictedAccepted int `json:"predicted_accepted"`
    ObservedAccepted int `json:"observed_accepted"`
    PredictionErrors int `json:"prediction_errors"`
}
type p13qWord struct {
    Word string `json:"word"`
    PredictedAccepted bool `json:"predicted_accepted"`
    ObservedAccepted bool `json:"observed_accepted"`
    StagewiseOldClientOK bool `json:"stagewise_old_client_ok"`
    AcceptedPrefix string `json:"accepted_prefix"`
    FailedEdit string `json:"failed_edit,omitempty"`
    NativeReason string `json:"native_reason,omitempty"`
}
type p13qReport struct {
    Protocol string `json:"protocol"`
    SourcePinnedCommit string `json:"source_pinned_commit"`
    FrozenTheoryCommit string `json:"frozen_theory_commit"`
    PriorInducedOnlyBinaryConflict string `json:"prior_induced_only_binary_conflict"`
    AllHoldoutWords int `json:"all_holdout_words"`
    Matched int `json:"matched"`
    Mismatches int `json:"mismatches"`
    Summaries []p13qSummary `json:"summaries"`
    Words []p13qWord `json:"words"`
    FirstFailures []p13qWord `json:"first_failures"`
    Verdict string `json:"verdict"`
    ScientificLimits string `json:"scientific_limits"`
}
func TestEvoNOMOSP13QFullSevenEditLengthHoldout(t *testing.T) {
    frozen:=map[int]struct{total,allowed int}{
        4:{840,600},5:{2520,1320},6:{5040,1440},7:{5040,0},
    }
    patterns:=[]p13Edit{
        {"A","/svc/a"},{"B","/svc/b"},
        {"C","/branch/one"},{"D","/branch/two"},
        {"E","/svc/{num:[0-9]+}"},{"F","/svc/{alpha:[a-z]+}"},
        {"G","/svc/a/deep"},
    }
    by:=map[byte]p13Edit{}
    for _,e:=range patterns{by[e.Name[0]]=e}
    report:=p13qReport{
        Protocol:"EVONOMOS_P42_R11_P10_P13_Q_SEVEN_EDIT_UNSEEN_LENGTHS",
        SourcePinnedCommit:"167e1e3bd039d060696b99c8da4e876ae04f42c1",
        FrozenTheoryCommit:"ae04d558f8ed834901000a3baa521f87ed0910d6",
        PriorInducedOnlyBinaryConflict:"EF",
        ScientificLimits:"Seven research-owned one-shot Mount edit commands with original Chi, old GET contract; not all Go, not upstream rights, not labor, not external PR forecast",
    }
    stats:=map[int]*p13qSummary{}
    for k:=4;k<=7;k++{stats[k]=&p13qSummary{Length:k}}
    var dfs func(word string,used uint8)
    dfs=func(word string,used uint8){
        if len(word)>=4{
            predicted:=!(containsEF(word))
            observed:=p13Run(word,by)
            if !observed.OldClientSafe{
                t.Fatalf("stagewise original old GET violated by source word=%s",word)
            }
            w:=p13qWord{
                Word:word,PredictedAccepted:predicted,
                ObservedAccepted:observed.Admission,
                StagewiseOldClientOK:observed.OldClientSafe,
                AcceptedPrefix:observed.AcceptedPrefix,
                FailedEdit:observed.FailedEdit,NativeReason:observed.FailureReason,
            }
            report.Words=append(report.Words,w)
            s:=stats[len(word)]
            s.Total++
            if predicted {s.PredictedAccepted++}
            if observed.Admission{s.ObservedAccepted++}
            if predicted!=observed.Admission{
                s.PredictionErrors++
                report.Mismatches++
                if len(report.FirstFailures)<10{report.FirstFailures=append(report.FirstFailures,w)}
            }else{report.Matched++}
        }
        if len(word)==7{return}
        for i:=0;i<7;i++{
            bit:=uint8(1<<uint(i))
            if used&bit==0{
                dfs(word+string(byte('A'+i)),used|bit)
            }
        }
    }
    dfs("",0)
    for k:=4;k<=7;k++{
        s:=*stats[k]
        report.Summaries=append(report.Summaries,s)
        if s.Total!=frozen[k].total||s.PredictedAccepted!=frozen[k].allowed{
            t.Fatalf("P13-Q frozen math enumeration differs at length %d: %+v",k,s)
        }
        t.Logf("P13_Q_LENGTH_%d: total=%d frozenPredictedLegal=%d originalNativeLegal=%d errors=%d",
            k,s.Total,s.PredictedAccepted,s.ObservedAccepted,s.PredictionErrors)
    }
    if report.Matched+report.Mismatches!=13440||len(report.Words)!=13440{
        t.Fatalf("holdout wrong census size %+v",report)
    }
    report.AllHoldoutWords=len(report.Words)
    report.Verdict="P13_Q_BINARY_GRAPH_SOURCE_HOLDOUT_PASS"
    if report.Mismatches>0{report.Verdict="P13_Q_SOURCE_FALSIFIER_KEEP_FIRST_NATIVE_WITNESS"}
    out:="out/p42-r11-p10-p13q"
    if err:=os.MkdirAll(out,0755);err!=nil{t.Fatal(err)}
    data,err:=json.MarshalIndent(report,"","  ");if err!=nil{t.Fatal(err)}
    if err:=os.WriteFile(filepath.Join(out,"all-13440-real-source-edits.json"),append(data,'\n'),0644);err!=nil{t.Fatal(err)}
    t.Logf("P13_Q_RESULT: verdict=%s matched=%d mismatches=%d",report.Verdict,report.Matched,report.Mismatches)
    if report.Mismatches>0{t.Fatalf("P13-Q frozen binary source forecast FALSIFIED in %d real original source words; consult emitted JSON",report.Mismatches)}
}
func containsEF(w string) bool {
    hasE,hasF:=false,false
    for i:=0;i<len(w);i++{if w[i]=='E'{hasE=true};if w[i]=='F'{hasF=true}}
    return hasE&&hasF
}
var _=fmt.Sprint
