package chi

// P13 original maintained Chi source (read-only checkout) research-owned test.
// P13 mathematical theory and ALL seven patterns were frozen in commit
// d18eebcc69b92bfe90b6ab0cca26f3b58726206f before this test was written.
// Source admission and old-client safety ONLY, not generalized Go equivalence.
import (
    "encoding/json"
    "fmt"
    "net/http"
    "net/http/httptest"
    "os"
    "path/filepath"
    "sort"
    "strings"
    "testing"
)

type p13Edit struct { Name, Pattern string }
type p13Case struct {
    Order string `json:"order"`
    Admission bool `json:"admission"`
    FailedEdit string `json:"failed_edit,omitempty"`
    FailureReason string `json:"failure_reason,omitempty"`
    AcceptedPrefix string `json:"accepted_prefix"`
    OldClientSafe bool `json:"old_client_safe"`
}
type p13Report struct {
    Protocol string `json:"protocol"`
    ExpectedPrograms int `json:"expected_programs"`
    Cases []p13Case `json:"cases"`
    Singles int `json:"singles_admitted"`
    BothOrderPairs []string `json:"both_order_pairs_admitted"`
    AllOrderTriples []string `json:"all_order_triples_admitted"`
    PairOnlyPredictedButTripleRejected []string `json:"pairwise_possible_but_triple_rejected"`
    BinaryGraphPredictionMismatches []string `json:"binary_graph_vs_triple_mismatches"`
    AdmissionFalsifiers []string `json:"presealed_control_falsifiers"`
    Verdict string `json:"verdict"`
    NoGeneralizedSourceClaim bool `json:"no_generalized_source_claim"`
}
func p13FreshParent() Router {
    r:=NewRouter()
    r.Get("/old",func(w http.ResponseWriter,_ *http.Request){_,_=fmt.Fprint(w,"old")})
    return r
}
func p13OldOK(r Router) bool {
    w:=httptest.NewRecorder()
    r.ServeHTTP(w,httptest.NewRequest(http.MethodGet,"/old",nil))
    return w.Code==200&&w.Body.String()=="old"&&!w.Flushed
}
func p13Attempt(r Router,e p13Edit) (ok bool,reason string) {
    defer func(){
        if caught:=recover();caught!=nil {
            ok=false
            reason=fmt.Sprint(caught)
        }
    }()
    child:=NewRouter()
    child.Get("/item",func(w http.ResponseWriter,_ *http.Request){_,_=fmt.Fprint(w,e.Name)})
    r.Mount(e.Pattern,child)
    return true,""
}
func p13Run(order string,by map[byte]p13Edit) p13Case {
    r:=p13FreshParent()
    c:=p13Case{Order:order,Admission:true,OldClientSafe:true}
    if !p13OldOK(r) {c.OldClientSafe=false}
    for i:=0;i<len(order);i++{
        e:=by[order[i]]
        ok,why:=p13Attempt(r,e)
        if !p13OldOK(r){c.OldClientSafe=false}
        if !ok{
            c.Admission=false
            c.FailedEdit=e.Name
            c.FailureReason=why
            break
        }
        c.AcceptedPrefix=order[:i+1]
    }
    return c
}
func TestEvoNOMOSP13OriginalChiHigherOrderMountAdmission(t *testing.T) {
    edits:=[]p13Edit{
        {"A","/svc/a"},{"B","/svc/b"},
        {"C","/branch/one"},{"D","/branch/two"},
        {"E","/svc/{num:[0-9]+}"},{"F","/svc/{alpha:[a-z]+}"},
        {"G","/svc/a/deep"},
    }
    by:=map[byte]p13Edit{}
    for _,e:=range edits {by[e.Name[0]]=e}
    var orders []string
    for _,a:=range edits {orders=append(orders,a.Name)}
    for _,a:=range edits {for _,b:=range edits {
        if a.Name!=b.Name{orders=append(orders,a.Name+b.Name)}
    }}
    for _,a:=range edits {for _,b:=range edits {for _,c:=range edits{
        if a.Name!=b.Name&&a.Name!=c.Name&&b.Name!=c.Name{
            orders=append(orders,a.Name+b.Name+c.Name)
        }
    }}}
    sort.Strings(orders)
    if len(orders)!=259{t.Fatalf("expected 259 source programs got %d",len(orders))}
    cases:=make(map[string]p13Case,len(orders))
    report:=p13Report{
        Protocol:"P42_R11_P10_P13_ORIGINAL_CHI_259_SOURCE_REGISTRATION_PERMUTATIONS",
        ExpectedPrograms:259,NoGeneralizedSourceClaim:true,
    }
    for _,word:=range orders{
        c:=p13Run(word,by)
        if !c.OldClientSafe{t.Fatalf("protected /old source client changed word=%s",word)}
        cases[word]=c
        report.Cases=append(report.Cases,c)
        if len(word)==1&&c.Admission{report.Singles++}
    }
    allPair:=map[string]bool{}
    for i:=0;i<len(edits);i++{for j:=i+1;j<len(edits);j++{
        p:=edits[i].Name+edits[j].Name
        v:=cases[p].Admission&&cases[edits[j].Name+edits[i].Name].Admission
        allPair[p]=v
        if v{report.BothOrderPairs=append(report.BothOrderPairs,p)}
    }}
    for i:=0;i<len(edits);i++{for j:=i+1;j<len(edits);j++{for k:=j+1;k<len(edits);k++{
        a,b,c:=edits[i].Name,edits[j].Name,edits[k].Name
        key:=a+b+c
        perms:=[]string{a+b+c,a+c+b,b+a+c,b+c+a,c+a+b,c+b+a}
        all:=true
        for _,p:=range perms{if !cases[p].Admission{all=false}}
        pairwise:=allPair[a+b]&&allPair[a+c]&&allPair[b+c]
        if all {report.AllOrderTriples=append(report.AllOrderTriples,key)}
        if pairwise&&!all {report.PairOnlyPredictedButTripleRejected=append(report.PairOnlyPredictedButTripleRejected,key)}
        if pairwise!=all{report.BinaryGraphPredictionMismatches=append(report.BinaryGraphPredictionMismatches,key)}
    }}}
    if report.Singles!=7{report.AdmissionFalsifiers=append(report.AdmissionFalsifiers,fmt.Sprintf("singletons=%d",report.Singles))}
    if !allPair["AB"]{report.AdmissionFalsifiers=append(report.AdmissionFalsifiers,"AB")}
    if !allPair["CD"]{report.AdmissionFalsifiers=append(report.AdmissionFalsifiers,"CD")}
    if allPair["EF"]{report.AdmissionFalsifiers=append(report.AdmissionFalsifiers,"EF expected both orders rejected")}
    report.Verdict="SOURCE_RESULTS_OBSERVED_NEED_INTERPRETATION"
    if len(report.AdmissionFalsifiers)>0{report.Verdict="PRESEALED_P13_CONTROLS_FALSIFIED"}
    out:="out/p42-r11-p10-p13"
    if err:=os.MkdirAll(out,0755);err!=nil{t.Fatal(err)}
    data,err:=json.MarshalIndent(report,"","  ");if err!=nil{t.Fatal(err)}
    if err=os.WriteFile(filepath.Join(out,"source-native-higher-order-census.json"),append(data,'\n'),0644);err!=nil{t.Fatal(err)}
    t.Logf("P13_CHI_NATIVE_SOURCE_259_PROGRAMS: singles=%d both_pairs=%d full_triples=%d triple_only=%d binary_model_mismatches=%d controls=%s",
        report.Singles,len(report.BothOrderPairs),len(report.AllOrderTriples),
        len(report.PairOnlyPredictedButTripleRejected),len(report.BinaryGraphPredictionMismatches),strings.Join(report.AdmissionFalsifiers,";"))
    t.Logf("P13_CHI_SOURCE_TRIPLE_ONLY: %v",report.PairOnlyPredictedButTripleRejected)
    t.Logf("P13_CHI_SOURCE_NONBINARY: %v",report.BinaryGraphPredictionMismatches)
    if len(report.AdmissionFalsifiers)>0{
        t.Fatalf("frozen source control falsification; preserve JSON and update THEORY separately, not after-the-fact labels: %v",report.AdmissionFalsifiers)
    }
}
