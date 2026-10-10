package httprouter

import (
 "encoding/json"
 "fmt"
 "net/http"
 "net/http/httptest"
 "os"
 "strings"
 "testing"
 router "github.com/julienschmidt/httprouter"
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

func parent() *router.Router{
 p:=router.New()
 p.GET("/old",func(w http.ResponseWriter,_ *http.Request,_ router.Params){fmt.Fprint(w,"unchanged")})
 return p
}
func apply(p *router.Router,e Edit){
 p.Handle(e.Method,e.Pattern,func(w http.ResponseWriter,_ *http.Request,_ router.Params){fmt.Fprint(w,e.Response)})
}
func oracle(t *testing.T,p http.Handler,method,path,want string){
 t.Helper()
 r:=httptest.NewRecorder()
 p.ServeHTTP(r,httptest.NewRequest(method,path,nil))
 if r.Code!=200 || strings.TrimSpace(r.Body.String())!=want {
  t.Fatalf("%s %s got status %d body %q expected %q",method,path,r.Code,r.Body.String(),want)
 }
}
func attempt(p *router.Router,edits []Edit)(pan any){
 defer func(){pan=recover()}()
 for _,e:=range edits{apply(p,e)}
 return nil
}
func TestP40P4ProspectiveFrozenHttprouter(t *testing.T){
 count,correct:=0,0
 for _,c:=range readFrozen(t){
  if c.Ecosystem!="httprouter"{continue}
  count++
  t.Run(c.ID,func(t *testing.T){
   if len(c.Edits)!=2{t.Fatal("two edits required")}
   for _,e:=range c.Edits {
    solo:=parent()
    if got:=attempt(solo,[]Edit{e});got!=nil{t.Fatalf("independent edit invalid: %v",got)}
    oracle(t,solo,"GET","/old","unchanged")
    oracle(t,solo,e.Method,e.Probe,e.Response)
   }
   merged:=parent()
   pan:=attempt(merged,c.Edits)
   admit:=pan==nil
   if admit!=(c.Forecast=="accept"){
    t.Fatalf("P40_P4_PROSPECTIVE_MISMATCH id=%s expected=%s actual=%t panic=%v",c.ID,c.Forecast,admit,pan)
   }
   oracle(t,merged,"GET","/old","unchanged")
   if admit{
    for _,e:=range c.Edits{oracle(t,merged,e.Method,e.Probe,e.Response)}
   }else if !strings.Contains(fmt.Sprint(pan),"conflict") && !strings.Contains(fmt.Sprint(pan),"already registered"){
    t.Fatalf("unexpected native panic %v",pan)
   }
   correct++
   t.Logf("P40_P4_PREDICTION_CONFIRMED id=%s outcome=%s",c.ID,c.Forecast)
  })
 }
 if count!=6||correct!=6{t.Fatalf("expected six frozen httprouter holdouts count=%d correct=%d",count,correct)}
 t.Log("P40_P4_HTTPROUTER_FROZEN_6_OF_6_SOURCE_ADMISSION_FORECASTS_PASS")
}
