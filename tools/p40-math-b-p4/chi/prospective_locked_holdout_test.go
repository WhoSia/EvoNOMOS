package chi

import (
 "encoding/json"
 "fmt"
 "net/http"
 "net/http/httptest"
 "os"
 "strings"
 "testing"
 "github.com/go-chi/chi/v5"
)
type Edit struct {
 Method string `json:"method"`
 Pattern string `json:"pattern"`
 Probe string `json:"probe"`
 Response string `json:"response"`
}
type Case struct {
 ID string `json:"id"`
 Ecosystem string `json:"ecosystem"`
 Forecast string `json:"forecast"`
 Edits []Edit `json:"edits"`
}
type Prereg struct{
 Contract string `json:"contract"`
 Cases []Case `json:"cases"`
}
func readFrozen(t *testing.T) []Case{
 t.Helper()
 bytes,err:=os.ReadFile("../preregistered_predictions.json");if err!=nil{t.Fatal(err)}
 var r Prereg
 if err:=json.Unmarshal(bytes,&r);err!=nil{t.Fatal(err)}
 if r.Contract!="P40_MATH_B_P4_PREREG_V1"{t.Fatal("wrong prereg format")}
 return r.Cases
}

func parent() chi.Router{
 p:=chi.NewRouter()
 p.Get("/old",func(w http.ResponseWriter,_ *http.Request){fmt.Fprint(w,"unchanged")})
 return p
}
func apply(p chi.Router,e Edit){
 child:=chi.NewRouter()
 child.Method(e.Method,"/item",http.HandlerFunc(func(w http.ResponseWriter,_ *http.Request){fmt.Fprint(w,e.Response)}))
 p.Mount(e.Pattern,child)
}
func oracle(t *testing.T,p http.Handler,method,path,want string){
 t.Helper()
 r:=httptest.NewRecorder()
 p.ServeHTTP(r,httptest.NewRequest(method,path,nil))
 if r.Code!=200 || strings.TrimSpace(r.Body.String())!=want {
  t.Fatalf("%s %s got status %d body %q expected %q",method,path,r.Code,r.Body.String(),want)
 }
}
func attempt(p chi.Router,edits []Edit)(pan any){
 defer func(){pan=recover()}()
 for _,e:=range edits{apply(p,e)}
 return nil
}
func TestP40P4ProspectiveFrozenChi(t *testing.T){
 count,correct:=0,0
 for _,c:=range readFrozen(t){
  if c.Ecosystem!="chi"{continue}
  count++
  t.Run(c.ID,func(t *testing.T){
   if len(c.Edits)!=2{t.Fatal("two source edits required")}
   for _,e:=range c.Edits{
    isolated:=parent()
    if got:=attempt(isolated,[]Edit{e});got!=nil{t.Fatalf("locally rejected: %v",got)}
    oracle(t,isolated,"GET","/old","unchanged")
    oracle(t,isolated,e.Method,e.Probe,e.Response)
   }
   merged:=parent()
   pan:=attempt(merged,c.Edits)
   admit:=pan==nil
   if admit!=(c.Forecast=="accept"){
    t.Fatalf("P40_P4_PROSPECTIVE_MISMATCH id=%s expected=%s gotAdmit=%t panic=%v",c.ID,c.Forecast,admit,pan)
   }
   oracle(t,merged,"GET","/old","unchanged")
   if admit{
    for _,e:=range c.Edits{oracle(t,merged,e.Method,e.Probe,e.Response)}
   }else if !strings.Contains(fmt.Sprint(pan),"attempting to Mount() a handler on an existing path"){
    t.Fatalf("unanticipated panic signature: %v",pan)
   }
   correct++
   t.Logf("P40_P4_PREDICTION_CONFIRMED id=%s outcome=%s",c.ID,c.Forecast)
  })
 }
 if count!=5||correct!=5{t.Fatalf("expected five frozen chi holdouts count=%d correct=%d",count,correct)}
 t.Log("P40_P4_CHI_FROZEN_5_OF_5_SOURCE_ADMISSION_FORECASTS_PASS")
}
