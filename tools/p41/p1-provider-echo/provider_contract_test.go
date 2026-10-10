package p41provider

import (
 "net/http"
 "net/http/httptest"
 "testing"

 echo "github.com/labstack/echo/v5"
)

// These two providers satisfy the *real unchanged Echo v5 Router interface*
// by forwarding every method except the semantics-changing Route branch.
type forwarding struct {
 echo.Router
 routesCalled int
}
var _ echo.Router = (*forwarding)(nil)
func (r *forwarding) Route(c *echo.Context) echo.HandlerFunc {
 r.routesCalled++
 return r.Router.Route(c)
}

type diverted struct {
 echo.Router
 routesCalled int
}
var _ echo.Router = (*diverted)(nil)
func (r *diverted) Route(c *echo.Context) echo.HandlerFunc {
 r.routesCalled++
 // Legal signature, intentionally violates requested route/response contract.
 return func(c *echo.Context)error {
  c.Response().Header().Set("X-Provider-Origin","diverted")
  return c.String(200,"WRONG_PROVIDER")
 }
}

func serve(router echo.Router)(*httptest.ResponseRecorder,*echo.Echo){
 e:=echo.NewWithConfig(echo.Config{Router:router})
 e.GET("/p41/provider",func(c *echo.Context)error{
  c.Response().Header().Set("X-Provider-Origin","expected")
  return c.String(http.StatusOK,"CONTRACT_OK")
 })
 rec:=httptest.NewRecorder()
 e.ServeHTTP(rec,httptest.NewRequest(http.MethodGet,"/p41/provider",nil))
 return rec,e
}
func TestP41P1ActualEchoRouterStructuralCapabilityAndBehaviorNotEquivalent(t *testing.T){
 good:=&forwarding{Router:echo.NewRouter(echo.RouterConfig{})}
 bad:=&diverted{Router:echo.NewRouter(echo.RouterConfig{})}
 observed,_:=serve(good)
 diverged,_:=serve(bad)
 if good.routesCalled!=1||bad.routesCalled!=1 {
  t.Fatalf("both interface-typed provider implementations must execute: forward=%d diverted=%d",good.routesCalled,bad.routesCalled)
 }
 if observed.Code!=200||observed.Body.String()!="CONTRACT_OK"||
   observed.Header().Get("X-Provider-Origin")!="expected"{
  t.Fatalf("real Echo source router provider unexpected response: code=%d body=%q",observed.Code,observed.Body.String())
 }
 if diverged.Code!=200||diverged.Body.String()!="WRONG_PROVIDER"||
   diverged.Header().Get("X-Provider-Origin")!="diverted"{
  t.Fatalf("alternate structurally-typed provider unexpectedly changed: code=%d body=%q",diverged.Code,diverged.Body.String())
 }
 t.Log("P41_P1_TWO_NATIVE_INTERFACE_CONFORMING_PROVIDERS_DIFFERENT_BEHAVIOR_PASS")
}

func TestP41P1ProviderInterfaceSourceContractCompiles(t *testing.T){
 var provider echo.Router = &forwarding{Router:echo.NewRouter(echo.RouterConfig{})}
 if provider==nil{t.Fatal("typed Echo router provider missing")}
 t.Log("P41_P1_ORIGINAL_ECHO_ROUTER_INTERFACE_TYPECHECK_PASS")
}
