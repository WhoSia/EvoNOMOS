package p42p2

import (
 "encoding/json"
 "net/http"
 "net/http/httptest"
 "os"
 "strings"
 "testing"
 echo "github.com/labstack/echo/v4"
)
type R2Trace struct {
 Version string `json:"version"`
 Context string `json:"context"`
 Status int `json:"status"`
 Body string `json:"body"`
 Handler string `json:"handler"`
 Template string `json:"template"`
 Params []string `json:"param_names"`
 Values []string `json:"param_values"`
 Name string `json:"name"`
 Calls int `json:"handler_count"`
 Panic string `json:"panic"`
}
func runR2(c string)(out R2Trace){
 out=R2Trace{Version:os.Getenv("P42_R2_VERSION"),Context:c}
 defer func(){if e:=recover();e!=nil{out.Panic="REGISTRATION_OR_EXECUTION_PANIC"}}()
 e:=echo.New()
 observe:=func(id string)echo.HandlerFunc{
  return func(ctx echo.Context)error{
   out.Handler=id;out.Template=ctx.Path();out.Params=append([]string{},ctx.ParamNames()...)
   out.Values=append([]string{},ctx.ParamValues()...)
   out.Name=ctx.Param("name");out.Calls++
   return ctx.String(200,id+"|"+out.Name+"|"+strings.Join(out.Params,",")+"|"+strings.Join(out.Values,","))
  }
 }
 path:="/health"
 switch c{
 case "health":e.GET("/health",observe("health"))
 case "bare","inline","other":
   e.GET(`/r/:name\:cancel`,observe("inline"))
   if c=="bare"{path="/r/foo"}else if c=="inline"{path="/r/foo:cancel"}else{path="/r/foo:other"}
 case "generic-fallback","inline-split":
   e.GET(`/r/:name\:v/:id/end`,observe("verb"))
   e.GET("/r/:name/other",observe("generic"))
   if c=="generic-fallback"{path="/r/a:vq/other"}else{path="/r/a:v/q/end"}
 case "wildcard-fallback":
   e.POST(`/r/:n\:v/*`,observe("post"))
   e.GET("/r/:n/*",observe("generic"))
   path="/r/a:v/q"
 case "mixed-param":
   e.GET(`/r/:name\:x/:id`,observe("verb"))
   e.GET("/r/:name/q",observe("generic"))
   path="/r/a:x/q"
 default:panic("unknown fixed client context")
 }
 rec:=httptest.NewRecorder()
 e.ServeHTTP(rec,httptest.NewRequest(http.MethodGet,path,nil))
 out.Status=rec.Code;out.Body=rec.Body.String()
 return
}
func TestP42R2AuthenticRevisionFaultDomain(t *testing.T){
 if os.Getenv("P42_R2_VERSION")==""{t.Fatal("source revision label needed")}
 for _,name:=range []string{"health","bare","inline","other","generic-fallback","inline-split","wildcard-fallback","mixed-param"}{
  tr:=runR2(name)
  b,err:=json.Marshal(tr);if err!=nil{t.Fatal(err)}
  t.Log("P42_R2_NATIVE_TRACE "+string(b))
 }
}
