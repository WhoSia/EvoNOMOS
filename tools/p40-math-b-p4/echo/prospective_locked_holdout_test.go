package echo

import (
 "encoding/json"
 "net/http"
 "net/http/httptest"
 "os"
 "strings"
 "testing"
 echo "github.com/labstack/echo/v5"
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

func parent() *echo.Echo{
 p:=echo.New()
 p.GET("/old",func(c *echo.Context) error{return c.String(http.StatusOK,"unchanged")})
 return p
}
func apply(p *echo.Echo,e Edit){
 p.Add(e.Method,e.Pattern,func(c *echo.Context)error{return c.String(http.StatusOK,e.Response)})
}
func oracle(t *testing.T,p http.Handler,method,path,want string){
 t.Helper()
 r:=httptest.NewRecorder()
 p.ServeHTTP(r,httptest.NewRequest(method,path,nil))
 if r.Code!=200 || strings.TrimSpace(r.Body.String())!=want{
  t.Fatalf("%s %s got status %d body %q expected %q",method,path,r.Code,r.Body.String(),want)
 }
}
func attempt(p *echo.Echo,edits []Edit)(pan any){
 defer func(){pan=recover()}()
 for _,e:=range edits{apply(p,e)}
 return nil
}
func TestP40P4ProspectiveFrozenEcho(t *testing.T){
 count,correct:=0,0
 for _,c:=range readFrozen(t){
  if c.Ecosystem!="echo"{continue}
  count++
  t.Run(c.ID,func(t *testing.T){
   if len(c.Edits)!=2{t.Fatal("two edits required")}
   for _,e:=range c.Edits{
    solo:=parent()
    if pan:=attempt(solo,[]Edit{e});pan!=nil{t.Fatalf("locally invalid: %v",pan)}
    oracle(t,solo,"GET","/old","unchanged")
    oracle(t,solo,e.Method,e.Probe,e.Response)
   }
   merged:=parent()
   pan:=attempt(merged,c.Edits)
   admit:=pan==nil
   if admit!=(c.Forecast=="accept"){
    t.Fatalf("P40_P4_PROSPECTIVE_MISMATCH %s expected=%s actual=%t panic=%v",c.ID,c.Forecast,admit,pan)
   }
   oracle(t,merged,"GET","/old","unchanged")
   if admit {
    for i,e:=range c.Edits{
     if i==0 && c.Edits[0].Method==c.Edits[1].Method &&
       c.Edits[0].Pattern==c.Edits[1].Pattern{continue}
     oracle(t,merged,e.Method,e.Probe,e.Response)
    }
   }else if pan==nil {
    t.Fatal("rejection forecast did not carry source failure")
   }
   if admit && c.Edits[0].Method==c.Edits[1].Method &&
      c.Edits[0].Pattern==c.Edits[1].Pattern {
      // Source registration is permitted by Echo's overwrite policy, but the
      // FIRST module's new-client contract is no longer satisfied.
      last:=c.Edits[1]
      recorder:=httptest.NewRecorder()
      merged.ServeHTTP(recorder,httptest.NewRequest(last.Method,last.Probe,nil))
      if recorder.Code!=200 || strings.TrimSpace(recorder.Body.String())!=last.Response ||
         last.Response==c.Edits[0].Response{
         t.Fatal("expected last writer to supersede first isolated new-client demand")
      }
      t.Log("P40_P4_ECHO_ADMISSION_DOES_NOT_IMPLY_BOTH_NEW_CLIENT_CONTRACTS_PASS")
   }
   correct++
   t.Logf("P40_P4_PREDICTION_CONFIRMED id=%s outcome=%s",c.ID,c.Forecast)
  })
 }
 if count!=5||correct!=5{t.Fatalf("expected five frozen Echo holdouts count=%d correct=%d",count,correct)}
 t.Log("P40_P4_ECHO_FROZEN_5_OF_5_SOURCE_ADMISSION_FORECASTS_PASS")
}
