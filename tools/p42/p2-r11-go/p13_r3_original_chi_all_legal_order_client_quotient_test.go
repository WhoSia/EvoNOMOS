package chi

// P13-R3: source-native permutation holdout court for one selected HTTP query language.
// Mathematical hypothesis H0 and 3,588 histories were frozen at f763a90b,
// BEFORE this research-owned Go test existed. This code is not an upstream edit.
import (
    "encoding/json"
    "fmt"
    "os"
    "path/filepath"
    "sort"
    "strings"
    "testing"
)

type p13r3Observation struct {
    Word string `json:"word"`
    Support string `json:"support"`
    Admitted bool `json:"admitted"`
    AllOldStagesOK bool `json:"all_old_stages_ok"`
    FirstMountFailure string `json:"first_mount_failure,omitempty"`
    Probes map[string]p13r2Probe `json:"probes"`
}
type p13r3Falsifier struct {
    Support string `json:"support"`
    FirstOrder string `json:"first_order"`
    SecondOrder string `json:"second_order"`
    HTTPPath string `json:"http_path"`
    First p13r2Probe `json:"first"`
    Second p13r2Probe `json:"second"`
}
type p13r3Summary struct {
    Protocol string `json:"protocol"`
    FrozenTheoryCommit string `json:"frozen_theory_commit"`
    MaintainedSourceCommit string `json:"maintained_source_commit"`
    SelectedFiniteHTTPAlphabet []string `json:"selected_http_alphabet"`
    ExpectedLegalHistories int `json:"expected_legal_histories"`
    ActualLegalHistories int `json:"actual_legal_histories"`
    DistinctInstalledSets int `json:"distinct_installed_sets"`
    SourceRegistrationFailures int `json:"source_registration_failures"`
    OldClientStageViolations int `json:"old_client_stage_violations"`
    SameSupportClientEffectMismatches int `json:"same_support_client_effect_mismatches"`
    EFPairSourceHTTPSeparations int `json:"e_f_pair_source_http_separations"`
    FirstFalsifiers []p13r3Falsifier `json:"first_falsifiers"`
    Cases []p13r3Observation `json:"cases"`
    Verdict string `json:"verdict"`
    Limits string `json:"limits"`
}
var p13r3Alphabet=[]string{
    "/old","/svc/123/item","/svc/abc/item",
    "/svc/a/item","/svc/b/item","/branch/one/item",
    "/branch/two/item","/svc/a/deep/item",
}
func p13r3Support(mask uint8) string {
    var out strings.Builder
    for i:=0;i<7;i++ {if mask&(1<<uint(i))!=0 {out.WriteByte(byte('A'+i))}}
    return out.String()
}
func p13r3ProbeExact(a,b p13r2Probe) bool {
    return a.Code==b.Code&&a.Body==b.Body&&a.Flushed==b.Flushed
}
func TestEvoNOMOSP13R3OriginalChiAllLegalOrdersJointFutureClientQuotient(t *testing.T) {
    edits:=[]p13Edit{
        {"A","/svc/a"},{"B","/svc/b"},
        {"C","/branch/one"},{"D","/branch/two"},
        {"E","/svc/{num:[0-9]+}"},{"F","/svc/{alpha:[a-z]+}"},
        {"G","/svc/a/deep"},
    }
    by:=map[byte]p13Edit{}
    for _,e:=range edits {by[e.Name[0]]=e}
    report:=p13r3Summary{
        Protocol:"EVONOMOS_P42_R11_P10_P13_R3_ORIGINAL_CHI_ALL_3588_ORDERS_REAL_EIGHT_HTTP_JOINT_QUOTIENT",
        FrozenTheoryCommit:"f763a90bceb9b5fd44aeb45164234278636d9dab",
        MaintainedSourceCommit:"167e1e3bd039d060696b99c8da4e876ae04f42c1",
        SelectedFiniteHTTPAlphabet:p13r3Alphabet,
        ExpectedLegalHistories:3588,
        Limits:"All 3588 accepted one-shot histories for 7 researcher-owned app Mount edits, 8 httptest GET probes; no all-HTTP/Go/upstream-ownership/real cost claim",
        Cases:[]p13r3Observation{},
        FirstFalsifiers:[]p13r3Falsifier{},
    }
    reference:=map[uint8]p13r3Observation{}
    var examine func(w string,mask uint8)
    examine=func(w string,mask uint8){
        r:=p13FreshParent()
        entry:=p13r3Observation{
            Word:w,Support:p13r3Support(mask),Admitted:true,
            AllOldStagesOK:p13OldOK(r),
            Probes:map[string]p13r2Probe{},
        }
        for i:=0;i<len(w);i++{
            ok,why:=p13Attempt(r,by[w[i]])
            if !ok {
                entry.Admitted=false
                entry.FirstMountFailure=fmt.Sprintf("edit=%c, why=%s",w[i],why)
                report.SourceRegistrationFailures++
                break
            }
            if !p13OldOK(r) {entry.AllOldStagesOK=false}
        }
        if !entry.AllOldStagesOK {report.OldClientStageViolations++}
        if entry.Admitted {
            for _,path:=range p13r3Alphabet {entry.Probes[path]=p13r2HTTP(r,path)}
            if ref,exists:=reference[mask];exists {
                for _,path:=range p13r3Alphabet {
                    a,b:=ref.Probes[path],entry.Probes[path]
                    if !p13r3ProbeExact(a,b) {
                        report.SameSupportClientEffectMismatches++
                        if len(report.FirstFalsifiers)<15 {
                            report.FirstFalsifiers=append(report.FirstFalsifiers,p13r3Falsifier{
                                Support:entry.Support,FirstOrder:ref.Word,SecondOrder:w,
                                HTTPPath:path,First:a,Second:b,
                            })
                        }
                    }
                }
            } else {reference[mask]=entry}
        }
        report.Cases=append(report.Cases,entry)
        report.ActualLegalHistories++
        // Generate ONLY the previously identified legal original-source language.
        for i:=0;i<7;i++{
            bit:=uint8(1<<uint(i))
            if mask&bit!=0{continue}
            if i==4 && mask&(1<<5)!=0{continue}
            if i==5 && mask&(1<<4)!=0{continue}
            examine(w+string(byte('A'+i)),mask|bit)
        }
    }
    examine("",0)
    report.DistinctInstalledSets=len(reference)
    // Every T subset has the two source contexts E and F; they must remain
    // different on the independently frozen actual HTTP client queries.
    for mask:=uint8(0);mask<128;mask++ {
        if mask&(1<<4)!=0 || mask&(1<<5)!=0 {continue}
        e,okE:=reference[mask|(1<<4)]
        f,okF:=reference[mask|(1<<5)]
        if !okE||!okF{continue}
        ep,fp:=e.Probes["/svc/123/item"],f.Probes["/svc/123/item"]
        ea,fa:=e.Probes["/svc/abc/item"],f.Probes["/svc/abc/item"]
        if !p13r3ProbeExact(ep,fp)&&!p13r3ProbeExact(ea,fa) {
            report.EFPairSourceHTTPSeparations++
        }
    }
    report.Verdict="H0_ORDER_EFFECT_FACTORING_FALSIFIED_PRESERVE_ORIGINAL_SOURCE_WITNESSES"
    if report.ActualLegalHistories==3588&&report.DistinctInstalledSets==96&&
       report.SourceRegistrationFailures==0&&report.OldClientStageViolations==0&&
       report.SameSupportClientEffectMismatches==0&&report.EFPairSourceHTTPSeparations==32 {
        report.Verdict="P13_R3_FROZEN_3588_ORDERS_EIGHT_HTTP_EFFECTS_AND_EXACT_96_JOINT_CLASSES_PASS"
    }
    // Always serialize the original-source evidence BEFORE marking a failed hypothesis.
    dir:="out/p42-r11-p10-p13-r3"
    if err:=os.MkdirAll(dir,0755);err!=nil{t.Fatal(err)}
    raw,err:=json.MarshalIndent(report,"","  ");if err!=nil{t.Fatal(err)}
    if err=os.WriteFile(filepath.Join(dir,"original-chi-all-legal-order-client-effects.json"),append(raw,'\n'),0644);err!=nil{t.Fatal(err)}
    sort.Slice(report.FirstFalsifiers,func(i,j int)bool{
        return report.FirstFalsifiers[i].Support<report.FirstFalsifiers[j].Support
    })
    t.Logf("P13_R3_SOURCE_ALL_ORDERS: cases=%d subsets=%d registration_fail=%d old_fail=%d same_subset_effect_diffs=%d independent_EF_effect_separations=%d verdict=%s",
        report.ActualLegalHistories,report.DistinctInstalledSets,report.SourceRegistrationFailures,
        report.OldClientStageViolations,report.SameSupportClientEffectMismatches,
        report.EFPairSourceHTTPSeparations,report.Verdict)
    for i,c:=range report.FirstFalsifiers {if i>=5 {break};t.Logf("P13_R3_NATIVE_FALSIFIER: %+v",c)}
    if report.Verdict!="P13_R3_FROZEN_3588_ORDERS_EIGHT_HTTP_EFFECTS_AND_EXACT_96_JOINT_CLASSES_PASS" {
        t.Fatalf("P13-R3 mathematical source-effect factorization H0 failed / hold: actual native receipts preserved")
    }
}
