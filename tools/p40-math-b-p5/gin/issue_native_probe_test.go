package p40p5gin

import (
 "encoding/json"
 "fmt"
 "net/http"
 "net/http/httptest"
 "os"
 "strings"
 "testing"
 gin "github.com/gin-gonic/gin"
)
type Forecast struct {
 ID string `json:"id"`
 Ecosystem string `json:"ecosystem"`
 Forecast string `json:"forecast"`
}
type Manifest struct {
 Contract string `json:"contract"`
 Cases []Forecast `json:"cases"`
}
func locked(t *testing.T,id string)string{
 t.Helper()
 b,err:=os.ReadFile("../issue_derived_prereg.json");if err!=nil{t.Fatal(err)}
 var m Manifest
 if err:=json.Unmarshal(b,&m);err!=nil{t.Fatal(err)}
 if m.Contract!="P40_MATH_B_P5_ISSUE_DERIVED_PREREG_V1"{t.Fatal("wrong prereg")}
 for _,f:=range m.Cases{if f.ID==id{
  if f.Ecosystem!="gin"{t.Fatalf("wrong case ecosystem %s",id)}
  return f.Forecast
 }}
 t.Fatalf("not registered %s",id);return ""
}
func ensure(t *testing.T,id,forecast string){
 t.Helper()
 if p:=locked(t,id);p!=forecast{t.Fatalf("locked forecast differs id=%s expected=%s actual=%s",id,forecast,p)}
}
func newRouter() *gin.Engine{
 gin.SetMode(gin.TestMode)
 r:=gin.New()
 r.GET("/old",func(c *gin.Context){c.String(200,"unchanged")})
 return r
}
func request(r *gin.Engine,method,path string)*httptest.ResponseRecorder{
 rec:=httptest.NewRecorder()
 r.ServeHTTP(rec,httptest.NewRequest(method,path,nil))
 return rec
}
func withPanic(fn func())(v any){
 defer func(){v=recover()}()
 fn()
 return nil
}
func TestIssue4641BareColonConflict(t *testing.T){
 const id="G-VERB-BARE"
 ensure(t,id,"SECOND_REGISTRATION_PANICS")
 r:=newRouter()
 r.POST("/issue/users:batchGet",func(c *gin.Context){c.String(200,"get")})
 got:=withPanic(func(){
  r.POST("/issue/users:batchCreate",func(c *gin.Context){c.String(200,"create")})
 })
 if got==nil||!strings.Contains(fmt.Sprint(got),"conflict"){
  t.Fatalf("P40_P5_FORECAST_FALSIFIED %s second route panic=%v",id,got)
 }
 if rec:=request(r,http.MethodGet,"/old");rec.Code!=200||rec.Body.String()!="unchanged"{
  t.Fatal("old client changed")
 }
 t.Logf("P40_P5_LOCKED_PREDICTION_PASS G-VERB-BARE panic=%q",fmt.Sprint(got))
}
func TestIssue4641EscapedLiteralVerb(t *testing.T){
 const id="G-VERB-ESCAPED"
 ensure(t,id,"BOTH_REGISTER_AND_SERVE")
 r:=newRouter()
 pan:=withPanic(func(){
  r.POST("/issue/users\\:batchGet",func(c *gin.Context){c.String(200,"get")})
  r.POST("/issue/users\\:batchCreate",func(c *gin.Context){c.String(200,"create")})
 })
 if pan!=nil{t.Fatalf("P40_P5_FORECAST_FALSIFIED %s registration panic=%v",id,pan)}
 get:=request(r,http.MethodPost,"/issue/users:batchGet")
 create:=request(r,http.MethodPost,"/issue/users:batchCreate")
 if get.Code!=200||get.Body.String()!="get"||create.Code!=200||create.Body.String()!="create"{
  t.Fatalf("P40_P5_FORECAST_FALSIFIED %s status/body get=%d/%q create=%d/%q",id,get.Code,get.Body.String(),create.Code,create.Body.String())
 }
 t.Log("P40_P5_LOCKED_PREDICTION_PASS G-VERB-ESCAPED")
}
func TestIssue4641ParamSuffixAbstention(t *testing.T){
 const id="G-VERB-PARAM-SUFFIX"
 ensure(t,id,"ABSTAIN")
 r:=newRouter()
 customerID,fullPath:="",""
 got:=withPanic(func(){
  r.POST("/issue/customers/:customer_id\\:mutate",func(c *gin.Context){
   customerID=c.Param("customer_id")
   fullPath=c.FullPath()
   c.String(200,"id="+customerID)
  })
 })
 rec:=request(r,http.MethodPost,"/issue/customers/123:mutate")
 t.Logf("P40_P5_ABSTAIN_OBSERVATION id=%s registrationPanic=%q status=%d body=%q customerID=%q fullPath=%q",id,fmt.Sprint(got),rec.Code,rec.Body.String(),customerID,fullPath)
}
func TestIssue4641StaticControl(t *testing.T){
 const id="G-STATIC-CONTROL"
 ensure(t,id,"BOTH_REGISTER_AND_SERVE")
 r:=newRouter()
 pan:=withPanic(func(){
  r.POST("/issue/static-a",func(c *gin.Context){c.String(200,"A")})
  r.POST("/issue/static-b",func(c *gin.Context){c.String(200,"B")})
 })
 if pan!=nil{t.Fatalf("P40_P5_FORECAST_FALSIFIED %s panic=%v",id,pan)}
 a,b:=request(r,http.MethodPost,"/issue/static-a"),request(r,http.MethodPost,"/issue/static-b")
 if a.Code!=200||a.Body.String()!="A"||b.Code!=200||b.Body.String()!="B"{t.Fatalf("P40_P5_FORECAST_FALSIFIED %s",id)}
 t.Log("P40_P5_LOCKED_PREDICTION_PASS G-STATIC-CONTROL")
}
