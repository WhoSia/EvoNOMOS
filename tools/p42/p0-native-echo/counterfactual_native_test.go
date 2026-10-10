package p42echo

import (
 "encoding/json"
 "net/http"
 "net/http/httptest"
 "testing"

 echo "github.com/labstack/echo/v5"
)
type ClientObs struct{
 Status int `json:"status"`
 Body string `json:"body"`
 ContractHeader string `json:"contract_header"`
 HandlerID string `json:"handler_id"`
 Invocations int `json:"invocations"`
}
type Case struct{
 ID string `json:"id"`
 Ecosystem string `json:"ecosystem"`
 SourceAdmitted bool `json:"source_admitted"`
 OldFrame string `json:"old_frame"`
 NewGoal string `json:"new_goal"`
 HandlerResult string `json:"handler_result"`
 Authority string `json:"authority"`
 Observation ClientObs `json:"observation"`
}
func endpoint(t *testing.T,e *echo.Echo,path string) ClientObs{
 t.Helper()
 request:=httptest.NewRequest(http.MethodGet,path,nil)
 recorder:=httptest.NewRecorder()
 e.ServeHTTP(recorder,request)
 return ClientObs{Status:recorder.Code,Body:recorder.Body.String(),ContractHeader:recorder.Header().Get("X-Contract")}
}
func outputCase(t *testing.T,c Case){
 t.Helper()
 b,err:=json.Marshal(c)
 if err!=nil{t.Fatal(err)}
 t.Log("P42_NATIVE_CASE "+string(b))
}
func TestP42EchoDisjointAndOverlappingSourceEdits(t *testing.T){
 oldCalls,addonCalls:=0,0
 e:=echo.New()
 e.GET("/p42/old",func(c *echo.Context)error{
  oldCalls++
  c.Response().Header().Set("X-Contract","old")
  return c.String(http.StatusOK,"OLD")
 })
 e.GET("/p42/extension",func(c *echo.Context)error{
  addonCalls++
  c.Response().Header().Set("X-Contract","extension")
  return c.String(http.StatusCreated,"NEW")
 })
 before:=endpoint(t,e,"/p42/old")
 before.HandlerID="OLD";before.Invocations=oldCalls
 newObs:=endpoint(t,e,"/p42/extension")
 if before.Status!=200||before.Body!="OLD"||before.ContractHeader!="old"||oldCalls!=1||newObs.Status!=201||newObs.Body!="NEW"||newObs.ContractHeader!="extension"||addonCalls!=1{
  t.Fatalf("fixture source semantics drift: before=%+v ext=%+v old=%d addon=%d",before,newObs,oldCalls,addonCalls)
 }
 outputCase(t,Case{"echo-disjoint","Echo",true,"PRESERVED","FULFILLED","OLD","UNKNOWN",before})
 replacementCalls:=0
 e.GET("/p42/old",func(c *echo.Context)error{
  replacementCalls++
  c.Response().Header().Set("X-Contract","replacement")
  return c.String(200,"REPLACED")
 })
 oldCalls=0
 after:=endpoint(t,e,"/p42/old")
 after.HandlerID="NEW";after.Invocations=oldCalls
 if after.Status!=200||after.Body!="REPLACED"||after.ContractHeader!="replacement"||replacementCalls!=1||oldCalls!=0{
  t.Fatalf("expected overwrite semantics changed %+v replacement=%d old=%d",after,replacementCalls,oldCalls)
 }
 outputCase(t,Case{"echo-collision","Echo",true,"VIOLATED","REPLACES_OLD","NEW","UNKNOWN",after})
}
type divertingRouter struct{echo.Router}
func (r *divertingRouter) Route(c *echo.Context)echo.HandlerFunc{
 return func(c *echo.Context)error{
  c.Response().Header().Set("X-Contract","provider")
  return c.String(200,"DIVERTED")
 }
}
var _ echo.Router=(*divertingRouter)(nil)
func TestP42EchoCounterfactualProviderReplacement(t *testing.T){
 invoked:=0
 e:=echo.NewWithConfig(echo.Config{Router:&divertingRouter{Router:echo.NewRouter(echo.RouterConfig{})}})
 e.GET("/p42/old",func(c *echo.Context)error{
  invoked++
  c.Response().Header().Set("X-Contract","old")
  return c.String(200,"OLD")
 })
 obs:=endpoint(t,e,"/p42/old")
 obs.HandlerID="PROVIDER";obs.Invocations=invoked
 if obs.Status!=200||obs.Body!="DIVERTED"||obs.ContractHeader!="provider"||invoked!=0{
  t.Fatalf("provider fixture drift %+v",obs)
 }
 outputCase(t,Case{"echo-provider","Echo",true,"VIOLATED","DIVERTED","PROVIDER","UNKNOWN",obs})
}
