package p42r2

import (
 "encoding/json"
 "fmt"
 "net/http"
 "net/http/httptest"
 "os"
 "strings"
 "testing"
 echo "github.com/labstack/echo/v4"
)

type ContextSpec struct { ID, Scenario, Method, Path string }
type Observation struct {
 Revision string `json:"revision"`
 ID string `json:"id"`
 Scenario string `json:"scenario"`
 Method string `json:"method"`
 Path string `json:"path"`
 RegistrationPanicked bool `json:"registration_panicked"`
 RequestPanicked bool `json:"request_panicked"`
 PanicClass string `json:"panic_class"`
 Status int `json:"status"`
 Body string `json:"body"`
 Header string `json:"header"`
 HandlerID string `json:"handler_id"`
 Template string `json:"template"`
 ParamNames []string `json:"param_names"`
 ParamValues []string `json:"param_values"`
 BoundName string `json:"bound_name"`
 HandlerCalls int `json:"handler_calls"`
}
var specs=[]ContextSpec{
 {"health","health_only","GET","/health"},
 {"inline_basic","inline_only","GET","/r/foo:cancel"},
 {"inline_bare","inline_only","GET","/r/foo"},
 {"inline_other","inline_only","GET","/r/foo:other"},
 {"generic_other","inline_plus_generic","GET","/r/foo:other"},
 {"generic_cancel","inline_plus_generic","GET","/r/foo:cancel"},
 {"order_cancel_rev","generic_then_inline","GET","/r/foo:cancel"},
 {"backtrack_generic","backtrack","GET","/r/a:vq/other"},
 {"backtrack_verb","backtrack","GET","/r/a:v/q/end"},
 {"wildcard_interaction","wildcard","GET","/r/a:x/info"},
 {"complex_param","complex","GET","/r/foo"},
 {"leaf_path","leaf","GET","/files/a/b"},
 {"encoded_colon","inline_plus_generic","GET","/r/foo%3Acancel"},
 {"method_fallback","method_mix","POST","/r/foo:cancel"},
 {"wildcard_backtrack","wildcard_post_get","GET","/r/a:v/q"},
 {"method_405","only_post_inline","GET","/r/foo:cancel"},
}
func traceOne(sp ContextSpec) (o Observation) {
 o=Observation{Revision:os.Getenv("P42_R2_REVISION"),ID:sp.ID,Scenario:sp.Scenario,Method:sp.Method,Path:sp.Path}
 defer func(){
  if r:=recover();r!=nil {
   o.PanicClass=fmt.Sprintf("%T",r)
   if o.Status==0{o.RegistrationPanicked=true}else{o.RequestPanicked=true}
  }
 }()
 e:=echo.New()
 register:=func(method,pattern,id string){
  e.Add(method,pattern,func(c echo.Context)error{
   o.HandlerCalls++
   o.HandlerID=id
   o.Template=c.Path()
   o.ParamNames=append([]string{},c.ParamNames()...)
   o.ParamValues=append([]string{},c.ParamValues()...)
   o.BoundName=c.Param("name")
   c.Response().Header().Set("X-P42-R2",id)
   return c.String(http.StatusOK,id+"|"+strings.Join(c.ParamNames(),",")+"|"+c.Param("name"))
  })
 }
 switch sp.Scenario {
 case "health_only":
  register("GET","/health","health")
 case "inline_only":
  register("GET",`/r/:name\:cancel`,"verb")
 case "inline_plus_generic":
  register("GET",`/r/:name\:cancel`,"verb")
  register("GET","/r/:name","generic")
 case "generic_then_inline":
  register("GET","/r/:name","generic")
  register("GET",`/r/:name\:cancel`,"verb")
 case "backtrack":
  register("GET",`/r/:name\:v/:id/end`,"nested")
  register("GET","/r/:name/other","generic-other")
 case "wildcard":
  register("GET",`/r/:name\:x/*`,"wild-verb")
  register("GET","/r/:id/info","generic-info")
 case "complex":
  register("GET",`/r/:name\:x:id`,"complex")
 case "leaf":
  register("GET","/files/:path","leaf")
  register("GET",`/files/:name\:cancel/x`,"inline-leaf")
 case "method_mix":
  register("GET",`/r/:name\:cancel`,"verb")
  register("POST","/r/:name","post-fallback")
 case "wildcard_post_get":
  register("POST",`/r/:n\:v/*`,"post-verb")
  register("GET","/r/:n/*","get-wildcard")
 case "only_post_inline":
  register("POST",`/r/:name\:cancel`,"only-post")
 default:
  panic("unrecognized frozen scenario "+sp.Scenario)
 }
 rec:=httptest.NewRecorder()
 req:=httptest.NewRequest(sp.Method,sp.Path,nil)
 e.ServeHTTP(rec,req)
 o.Status=rec.Code;o.Body=rec.Body.String();o.Header=rec.Header().Get("X-P42-R2")
 return
}
func TestR2RealHistoricalFaultDomain(t *testing.T){
 if os.Getenv("P42_R2_REVISION")==""{t.Fatal("revision must be pinned by CI to an original upstream commit")}
 for _,spec:=range specs{
  t.Run(spec.ID,func(t *testing.T){
   o:=traceOne(spec)
   b,err:=json.Marshal(o)
   if err!=nil{t.Fatal(err)}
   t.Log("P42_R2_OBS "+string(b))
  })
 }
}
