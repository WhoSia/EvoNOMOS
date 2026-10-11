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

type Observed struct {
 Revision string `json:"revision"`
 Case string `json:"case"`
 Method string `json:"method"`
 Path string `json:"path"`
 Status int `json:"status"`
 Body string `json:"body"`
 Header string `json:"header"`
 HandlerID string `json:"handler_id"`
 Template string `json:"template"`
 ParamNames []string `json:"param_names"`
 ParamValues []string `json:"param_values"`
 BoundName string `json:"bound_name"`
 Invocations int `json:"invocations"`
}

func observe(t *testing.T, label, path string, masked bool) Observed {
 t.Helper()
 e := echo.New()
 var invoked int
 var handlerID, template, bound string
 var paramNames, paramValues []string
 e.GET("/health",func(c echo.Context)error {
  invoked++
  handlerID="health"
  template=c.Path()
  c.Response().Header().Set("X-Evo-Handler","health")
  return c.String(200,"health")
 })
 e.GET(`/r/:name\:cancel`,func(c echo.Context)error {
  invoked++
  handlerID="route"
  template=c.Path()
  paramNames=append([]string{},c.ParamNames()...)
  paramValues=append([]string{},c.ParamValues()...)
  bound=c.Param("name")
  c.Response().Header().Set("X-Evo-Handler","route")
  if masked {
   return c.String(200,"MASKED")
  }
  return c.String(200,"names="+strings.Join(c.ParamNames(),",")+";name="+c.Param("name"))
 })
 req:=httptest.NewRequest(http.MethodGet,path,nil)
 rec:=httptest.NewRecorder()
 e.ServeHTTP(rec,req)
 return Observed{
  Revision:os.Getenv("P42_SOURCE_REVISION"),
  Case:label,
  Method:http.MethodGet,
  Path:path,
  Status:rec.Code,
  Body:rec.Body.String(),
  Header:rec.Header().Get("X-Evo-Handler"),
  HandlerID:handlerID,
  Template:template,
  ParamNames:paramNames,
  ParamValues:paramValues,
  BoundName:bound,
  Invocations:invoked,
 }
}

func TestP42HistoricalEchoSourceClients(t *testing.T) {
 revision:=os.Getenv("P42_SOURCE_REVISION")
 if revision!="pre" && revision!="post" {
  t.Fatal("set P42_SOURCE_REVISION=pre or post in source-pinned CI")
 }
 cases:=[]struct{
  name,path string
  masked bool
 }{
  {"health","/health",false},
  {"bare","/r/foo",false},
  {"inline","/r/foo:cancel",false},
  {"other","/r/foo:other",false},
  {"masked-inline","/r/foo:cancel",true},
 }
 for _,c:=range cases {
  t.Run(c.name,func(t *testing.T){
   obs:=observe(t,c.name,c.path,c.masked)
   if c.name=="health" && (obs.Status!=200||obs.Body!="health"||obs.Header!="health"||obs.HandlerID!="health"||obs.Invocations!=1){
    t.Fatalf("health fixture invalid %+v",obs)
   }
   if c.name=="masked-inline" && obs.Status==200 && obs.Body!="MASKED" {
    t.Fatalf("masked fixture HTTP body unexpected %+v",obs)
   }
   encoded,err:=json.Marshal(obs)
   if err!=nil {t.Fatal(err)}
   t.Logf("P42_P2_NATIVE_TRACE %s",encoded)
  })
 }
}
