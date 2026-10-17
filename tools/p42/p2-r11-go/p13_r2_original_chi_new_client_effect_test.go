package chi

// P13-R2 real-client HTTP effect probe with exact prior mathematical forecast
// frozen at 7d8bc1c1ed45cc764e3b7efca9dd30750fcdaff8 before code.
import (
    "encoding/json"
    "fmt"
    "net/http"
    "net/http/httptest"
    "os"
    "path/filepath"
    "strings"
    "testing"
)

type p13r2Probe struct {
    Code int `json:"code"`
    Body string `json:"body"`
    Flushed bool `json:"flushed"`
}
type p13r2Case struct {
    OtherSet string `json:"other_set"`
    InstalledVariant string `json:"installed_variant"`
    InstallationHistory string `json:"installation_history"`
    AllSourceStepsAdmitted bool `json:"all_source_steps_admitted"`
    NativePanic string `json:"native_panic,omitempty"`
    ProtectedOldAllStages bool `json:"protected_old_all_stages"`
    Probes map[string]p13r2Probe `json:"probes"`
    PredictionFailures []string `json:"prediction_failures,omitempty"`
}
type p13r2Report struct {
    Protocol string `json:"protocol"`
    FrozenTheoryCommit string `json:"frozen_theory_commit"`
    OriginalSourceCommit string `json:"original_source_commit"`
    SourceCases int `json:"source_cases"`
    FullyDistinguishedEPairs int `json:"fully_distinguished_e_f_pairs"`
    TotalPredictionFailures int `json:"total_prediction_failures"`
    Cases []p13r2Case `json:"cases"`
    Verdict string `json:"verdict"`
    Limits string `json:"limits"`
}
func p13r2HTTP(r Router,path string) p13r2Probe {
    recorder:=httptest.NewRecorder()
    r.ServeHTTP(recorder,httptest.NewRequest(http.MethodGet,path,nil))
    return p13r2Probe{Code:recorder.Code,Body:recorder.Body.String(),Flushed:recorder.Flushed}
}
func TestEvoNOMOSP13R2OriginalChiCustomerEffectSplit(t *testing.T){
    labels:=[]byte{'A','B','C','D','G'}
    edits:=[]p13Edit{
        {"A","/svc/a"},{"B","/svc/b"},{"C","/branch/one"},
        {"D","/branch/two"},{"E","/svc/{num:[0-9]+}"},
        {"F","/svc/{alpha:[a-z]+}"},{"G","/svc/a/deep"},
    }
    by:=map[byte]p13Edit{}
    for _,e:=range edits{by[e.Name[0]]=e}
    report:=p13r2Report{
        Protocol:"P42_R11_P10_P13_R2_SOURCE_ADMISSION_RIGHT_LANGUAGE_VS_REAL_HTTP_CLIENT_EFFECT",
        FrozenTheoryCommit:"7d8bc1c1ed45cc764e3b7efca9dd30750fcdaff8",
        OriginalSourceCommit:"167e1e3bd039d060696b99c8da4e876ae04f42c1",
        Limits:"64 canonical original Chi research-owned app worlds; recorded HTTP client alphabet only; no upstream edit rights and no all-Go observational proof",
    }
    for mask:=0;mask<32;mask++{
        var subset strings.Builder
        for i,e:=range labels{if mask&(1<<uint(i))!=0{subset.WriteByte(e)}}
        T:=subset.String()
        pair:=map[byte]p13r2Case{}
        for _,variant:=range []byte{'E','F'}{
            r:=p13FreshParent()
            h:=T+string(variant)
            c:=p13r2Case{OtherSet:T,InstalledVariant:string(variant),
                InstallationHistory:h,AllSourceStepsAdmitted:true,ProtectedOldAllStages:true,
                Probes:map[string]p13r2Probe{}}
            if !p13OldOK(r){c.ProtectedOldAllStages=false}
            for i:=0;i<len(h);i++{
                ok,why:=p13Attempt(r,by[h[i]])
                if !ok{
                    c.AllSourceStepsAdmitted=false
                    c.NativePanic=why
                    c.PredictionFailures=append(c.PredictionFailures,fmt.Sprintf("source_mount_failed_at_%d:%s",i,why))
                    break
                }
                if !p13OldOK(r){c.ProtectedOldAllStages=false}
            }
            if !c.ProtectedOldAllStages{c.PredictionFailures=append(c.PredictionFailures,"old_client_stagewise_failed")}
            paths:=[]string{"/old","/svc/123/item","/svc/abc/item",
                "/svc/a/item","/svc/b/item","/branch/one/item",
                "/branch/two/item","/svc/a/deep/item"}
            for _,path:=range paths{c.Probes[path]=p13r2HTTP(r,path)}
            if !c.AllSourceStepsAdmitted{
                c.PredictionFailures=append(c.PredictionFailures,"all_source_steps_should_admit")
            }
            if c.Probes["/old"].Code!=200||c.Probes["/old"].Body!="old"||c.Probes["/old"].Flushed{
                c.PredictionFailures=append(c.PredictionFailures,"old_final_http_contract")
            }
            numeric:=c.Probes["/svc/123/item"]
            alpha:=c.Probes["/svc/abc/item"]
            if variant=='E'{
                if numeric.Code!=200||numeric.Body!="E"||numeric.Flushed{
                    c.PredictionFailures=append(c.PredictionFailures,"E_numeric_client_expected_200_E")
                }
                if alpha.Code!=404||alpha.Flushed{
                    c.PredictionFailures=append(c.PredictionFailures,"E_alpha_client_expected_404")
                }
            }else{
                if numeric.Code!=404||numeric.Flushed{
                    c.PredictionFailures=append(c.PredictionFailures,"F_numeric_client_expected_404")
                }
                if alpha.Code!=200||alpha.Body!="F"||alpha.Flushed{
                    c.PredictionFailures=append(c.PredictionFailures,"F_alpha_client_expected_200_F")
                }
            }
            for _,p:=range c.Probes{if p.Flushed{c.PredictionFailures=append(c.PredictionFailures,"unexpected_HTTP_Flush")}}
            report.TotalPredictionFailures+=len(c.PredictionFailures)
            report.Cases=append(report.Cases,c)
            pair[variant]=c
        }
        e,f:=pair['E'],pair['F']
        en,fn:=e.Probes["/svc/123/item"],f.Probes["/svc/123/item"]
        ea,fa:=e.Probes["/svc/abc/item"],f.Probes["/svc/abc/item"]
        if (en.Code!=fn.Code||en.Body!=fn.Body)&&(ea.Code!=fa.Code||ea.Body!=fa.Body){
            report.FullyDistinguishedEPairs++
        }
    }
    report.SourceCases=len(report.Cases)
    report.Verdict="P13_R2_64_SOURCE_CLIENT_EFFECT_SPLITS_PASS"
    if report.SourceCases!=64||report.FullyDistinguishedEPairs!=32||report.TotalPredictionFailures!=0{
        report.Verdict="P13_R2_FROZEN_CLIENT_CONTRACT_FALSIFIED_OR_INCOMPLETE"
    }
    dir:="out/p42-r11-p10-p13-r2"
    if err:=os.MkdirAll(dir,0755);err!=nil{t.Fatal(err)}
    raw,err:=json.MarshalIndent(report,"","  ");if err!=nil{t.Fatal(err)}
    if err:=os.WriteFile(filepath.Join(dir,"source-native-real-client-effect-court.json"),append(raw,'\n'),0644);err!=nil{t.Fatal(err)}
    t.Logf("P13_R2_ORIGINAL_CHI_CLIENT_EFFECT: real_worlds=%d distinct_E_F_pairs=%d contract_failures=%d verdict=%s",
        report.SourceCases,report.FullyDistinguishedEPairs,report.TotalPredictionFailures,report.Verdict)
    if report.Verdict!="P13_R2_64_SOURCE_CLIENT_EFFECT_SPLITS_PASS"{
        for _,c:=range report.Cases{if len(c.PredictionFailures)>0{
            t.Logf("P13_R2_FALSIFIER subset=%q variant=%s problems=%v numeric=%+v alpha=%+v",
                c.OtherSet,c.InstalledVariant,c.PredictionFailures,c.Probes["/svc/123/item"],c.Probes["/svc/abc/item"])
            break
        }}
        t.Fatalf("P13-R2 predeclared new HTTP-client prediction falsified; see artifact")
    }
}
