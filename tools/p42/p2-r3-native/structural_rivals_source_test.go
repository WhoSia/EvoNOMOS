package p42r3

import (
  "encoding/json"
  "net/http"
  "net/http/httptest"
  "os"
  "testing"
  echo "github.com/labstack/echo/v4"
)
type NativeTrace struct {
  Rival string `json:"rival"`
  Phase string `json:"phase"`
  Request string `json:"request"`
  Status int `json:"status"`
  Body string `json:"body"`
  Header string `json:"header"`
  Handler string `json:"handler"`
  BoundName string `json:"bound_name"`
  HandlerCalls int `json:"handler_calls"`
  SourceExtraRegistrations int `json:"source_extra_registrations"`
  LateSourceEdits int `json:"late_source_edits"`
}
func execute(rival,phase,path string) NativeTrace {
 e:=echo.New()
 result:=NativeTrace{Rival:rival,Phase:phase,Request:path}
 makeHandler:=func(name string,render func(echo.Context)string)echo.HandlerFunc{
  return func(c echo.Context)error{
   result.HandlerCalls++
   result.Handler=name
   result.BoundName=c.Param("name")
   c.Response().Header().Set("X-Rival",name)
   return c.String(http.StatusOK,render(c))
  }
 }
 e.GET("/health",makeHandler("health",func(_ echo.Context)string{return "health"}))
 verb:=func(){e.GET(`/r/:name\:cancel`,makeHandler("verb",func(c echo.Context)string{return "new:"+c.Param("name")}));result.SourceExtraRegistrations++}
 generic:=func(){e.GET("/r/:name",makeHandler("generic",func(c echo.Context)string{return "legacy:"+c.Param("name")}));result.SourceExtraRegistrations++}
 switch rival {
 case "SINGLE": verb()
 case "SPLIT":verb();generic()
 case "SPLIT_REVERSE":generic();verb()
 case "SINGLE_REPAIRED":verb();generic();result.LateSourceEdits=1
 default:panic("unfrozen rival "+rival)
 }
 recorder:=httptest.NewRecorder()
 req:=httptest.NewRequest(http.MethodGet,path,nil)
 e.ServeHTTP(recorder,req)
 result.Status=recorder.Code;result.Body=recorder.Body.String()
 result.Header=recorder.Header().Get("X-Rival")
 return result
}
func TestR3SourceRealizedTemporalRivals(t *testing.T){
 if os.Getenv("P42_R3_ORIGINAL_SOURCE_SHA")!="f085ffbe8f99de165bd920746920000ab56bd6bc" {
  t.Fatal("No pinned original echo v4 source attest; refusing rival test")
 }
 initial:=[]string{"/health","/r/foo:cancel"}
 late:=[]string{"/r/foo","/r/foo:other"}
 for _,rival:=range []string{"SINGLE","SPLIT","SPLIT_REVERSE","SINGLE_REPAIRED"}{
  for _,path:=range initial{
   tr:=execute(rival,"initial",path)
   b,_:=json.Marshal(tr);t.Log("P42_R3_TRACE "+string(b))
  }
  for _,path:=range late{
   tr:=execute(rival,"late",path)
   b,_:=json.Marshal(tr);t.Log("P42_R3_TRACE "+string(b))
  }
 }
}
