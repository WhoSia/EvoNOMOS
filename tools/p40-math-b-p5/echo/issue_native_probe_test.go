package p40p5echo

import (
 "encoding/json"
 "fmt"
 "net/http"
 "net/http/httptest"
 "os"
 "strings"
 "testing"
 echo "github.com/labstack/echo/v5"
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
 if err=json.Unmarshal(b,&m);err!=nil{t.Fatal(err)}
 if m.Contract!="P40_MATH_B_P5_ISSUE_DERIVED_PREREG_V1"{t.Fatal("wrong prereg")}
 for _,f:=range m.Cases{
  if f.ID==id{
   if f.Ecosystem!="echo"{t.Fatalf("wrong ecosystem %s",id)}
   return f.Forecast
  }
 }
 t.Fatalf("unregistered holdout %s",id)
 return ""
}
func request(e *echo.Echo,method,path string)*httptest.ResponseRecorder{
 rec:=httptest.NewRecorder()
 e.ServeHTTP(rec,httptest.NewRequest(method,path,nil))
 return rec
}
func ensure(t *testing.T,id,want string){t.Helper();if got:=locked(t,id);got!=want{t.Fatalf("locked forecast differs %s: expected %s got %s",id,want,got)}}
func TestIssue2895DefaultHEAD(t *testing.T){
 const id="E-HEAD-DEFAULT"
 ensure(t,id,"HEAD_405")
 e:=echo.New()
 e.GET("/issue/head-default",func(c *echo.Context)error{return c.String(200,"default-payload")})
 rec:=request(e,http.MethodHead,"/issue/head-default")
 if rec.Code!=405{t.Fatalf("P40_P5_FORECAST_FALSIFIED %s status=%d body=%q",id,rec.Code,rec.Body.String())}
 if get:=request(e,http.MethodGet,"/issue/head-default");get.Code!=200||get.Body.String()!="default-payload"{t.Fatalf("GET control failed: %d %q",get.Code,get.Body.String())}
 t.Log("P40_P5_LOCKED_PREDICTION_PASS E-HEAD-DEFAULT")
}
func TestIssue2895OptInHEAD(t *testing.T){
 const id="E-HEAD-OPTIN"
 ensure(t,id,"HEAD_200_EMPTY_GET_EXECUTES")
 e:=echo.NewWithConfig(echo.Config{Router:echo.NewRouter(echo.RouterConfig{AutoHandleHEAD:true})})
 counter:=0
 e.GET("/issue/head-optin",func(c *echo.Context)error{
  counter++
  c.Response().Header().Set("X-Issue-Handler","get")
  return c.String(http.StatusOK,"head-get-payload")
 })
 rec:=request(e,http.MethodHead,"/issue/head-optin")
 if rec.Code!=200||rec.Body.Len()!=0||rec.Header().Get("X-Issue-Handler")!="get"||counter!=1{
  t.Fatalf("P40_P5_FORECAST_FALSIFIED %s status=%d body=%q header=%q invocations=%d",id,rec.Code,rec.Body.String(),rec.Header().Get("X-Issue-Handler"),counter)
 }
 t.Log("P40_P5_LOCKED_PREDICTION_PASS E-HEAD-OPTIN")
}
func TestIssue2895ExplicitHEADPriority(t *testing.T){
 const id="E-HEAD-EXPLICIT"
 ensure(t,id,"EXPLICIT_HEAD_PRIORITY")
 e:=echo.NewWithConfig(echo.Config{Router:echo.NewRouter(echo.RouterConfig{AutoHandleHEAD:true})})
 getCount:=0
 e.GET("/issue/head-explicit",func(c *echo.Context)error{
  getCount++
  c.Response().Header().Set("X-Issue-Handler","get")
  return c.String(http.StatusOK,"get-handler")
 })
 e.HEAD("/issue/head-explicit",func(c *echo.Context)error{
  c.Response().Header().Set("X-Issue-Handler","explicit")
  return c.NoContent(http.StatusOK)
 })
 rec:=request(e,http.MethodHead,"/issue/head-explicit")
 if rec.Code!=200||rec.Header().Get("X-Issue-Handler")!="explicit"||getCount!=0{
  t.Fatalf("P40_P5_FORECAST_FALSIFIED %s status=%d header=%q getCounter=%d",id,rec.Code,rec.Header().Get("X-Issue-Handler"),getCount)
 }
 t.Log("P40_P5_LOCKED_PREDICTION_PASS E-HEAD-EXPLICIT")
}
func TestIssue2619WildcardTransferAbstained(t *testing.T){
 const id="E-WILD-TRANSFER"
 ensure(t,id,"ABSTAIN")
 e:=echo.New()
 e.GET("/old",func(c *echo.Context)error{return c.String(200,"unchanged")})
 var registrationPanic any
 func(){
  defer func(){registrationPanic=recover()}()
  e.GET("/v2/*/tags/list",func(c *echo.Context)error{return c.String(200,"TAGS|"+c.Path())})
  e.GET("/v2/*/blobs/uploads/:ref",func(c *echo.Context)error{return c.String(200,"UPLOADS|"+c.Path())})
 }()
 rec:=request(e,http.MethodGet,"/v2/foo/bar/tags/list")
 old:=request(e,http.MethodGet,"/old")
 if old.Code!=200||old.Body.String()!="unchanged"{t.Fatal("unrelated old route changed")}
 // This is a predeclared abstention; record exact observed behavior, do not
 // classify any particular transfer outcome as a correct forecast.
 t.Logf("P40_P5_ABSTAIN_OBSERVATION id=%s pan=%q status=%d body=%q",id,fmt.Sprint(registrationPanic),rec.Code,strings.TrimSpace(rec.Body.String()))
}

func TestP40P5ExploratoryEqualHeadBodyDifferentGetEffects(t *testing.T){
 create:=func(withExplicit bool)(*echo.Echo,*int){
  e:=echo.NewWithConfig(echo.Config{Router:echo.NewRouter(echo.RouterConfig{AutoHandleHEAD:true})})
  hits:=new(int)
  e.GET("/issue/effect",func(c *echo.Context)error{
   *hits++
   return c.String(http.StatusOK,"body-never-visible-for-head")
  })
  if withExplicit{
   e.HEAD("/issue/effect",func(c *echo.Context)error{return c.NoContent(http.StatusOK)})
  }
  return e,hits
 }
 a,aHits:=create(false)
 b,bHits:=create(true)
 ar:=request(a,http.MethodHead,"/issue/effect")
 br:=request(b,http.MethodHead,"/issue/effect")
 if ar.Code!=200||br.Code!=200||ar.Body.String()!=br.Body.String()||
    ar.Body.Len()!=0||*aHits!=1||*bHits!=0{
  t.Fatalf("expected identical observed HEAD status/body but unequal handler side effects: a=%d/%q hits=%d b=%d/%q hits=%d",ar.Code,ar.Body.String(),*aHits,br.Code,br.Body.String(),*bHits)
 }
 t.Log("P40_P5_EXPLORATORY_SAME_HEAD_STATUS_BODY_DIFFERENT_GET_SIDE_EFFECTS_PASS")
}
func TestP40P5Issue2619PostHocBadRoutingReproduction(t *testing.T){
 // This checks an anomaly FIRST observed in the registered ABSTAIN case,
 // therefore it is post hoc confirmation and must NEVER count as a forecast.
 e:=echo.New()
 e.GET("/v2/*/tags/list",func(c *echo.Context)error{return c.String(200,"TAGS")})
 e.GET("/v2/*/blobs/uploads/:ref",func(c *echo.Context)error{return c.String(200,"UPLOADS")})
 rec:=request(e,http.MethodGet,"/v2/foo/bar/tags/list")
 if rec.Code!=200||rec.Body.String()!="UPLOADS"{
  t.Fatalf("posthoc v5 routing reproduction changed: %d %q",rec.Code,rec.Body.String())
 }
 t.Log("P40_P5_POSTHOC_ECHO_2619_V5_WRONG_HANDLER_REPRODUCTION_PASS_NOT_PREREG")
}
