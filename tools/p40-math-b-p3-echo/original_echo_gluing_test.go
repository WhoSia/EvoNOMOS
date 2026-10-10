package p40mathbp3echo

import (
 "net/http"
 "net/http/httptest"
 "strings"
 "testing"
 echo "github.com/labstack/echo/v5"
)

const echoPinnedSHA = "3882266a3641a36fc2111b48cd597adab1c1ecea"

type edit struct{
 method string
 route string
 value string
}
func register(e *echo.Echo, x edit) {
 handler:=func(c *echo.Context)error{return c.String(http.StatusOK,x.value)}
 e.Add(x.method,x.route,handler)
}
func base()*echo.Echo {
 e:=echo.New()
 register(e,edit{"GET","/old","unchanged"})
 return e
}
func read(t *testing.T,e *echo.Echo,method,path,want string){
 t.Helper()
 rec:=httptest.NewRecorder()
 e.ServeHTTP(rec,httptest.NewRequest(method,path,nil))
 if rec.Code!=200 || strings.TrimSpace(rec.Body.String())!=want{
  t.Fatalf("%s %s got (%d,%q) expected 200,%q",method,path,rec.Code,rec.Body.String(),want)
 }
}
func TestOriginalEchoAllowsWildcardAndStaticDisjointPathsSameMethod(t *testing.T){
 a:=edit{"GET","/service/:name/a","A"}
 b:=edit{"GET","/service/static/b","B"}
 for _, x:=range []struct{e edit; method,path string}{
  {a,"GET","/service/example/a"},{b,"GET","/service/static/b"},
 }{
  e:=base()
  register(e,x.e)
  read(t,e,"GET","/old","unchanged")
  read(t,e,x.method,x.path,x.e.value)
 }
 for i,order:=range [][2]edit{{a,b},{b,a}}{
  e:=base()
  for _,x:=range order{register(e,x)}
  read(t,e,"GET","/old","unchanged")
  read(t,e,"GET","/service/example/a","A")
  read(t,e,"GET","/service/static/b","B")
  if len(e.Routes())<3{t.Fatalf("order %d: missing registered route metadata",i)}
 }
 t.Log("P40_MATH_B_P3_ORIGINAL_ECHO_WILDCARD_STATIC_DISJOINT_SAME_METHOD_GLUE_BOTH_ORDERS_PASS")
}
func TestOriginalEchoMethodPartitionAndLiteralControls(t *testing.T){
 for _,cases:=range [][2]edit{
  {{"GET","/service/:name/a","A"},{"POST","/service/static/b","B"}},
  {{"GET","/service/alice/a","A"},{"GET","/service/bob/b","B"}},
 } {
  for _,order:=range [][2]edit{cases,{cases[1],cases[0]}}{
   e:=base()
   for _,x:=range order{register(e,x)}
   read(t,e,"GET","/old","unchanged")
   for _,x:=range cases {
    if x.route=="/service/:name/a"{read(t,e,x.method,"/service/example/a",x.value)}else{read(t,e,x.method,x.route,x.value)}
   }
  }
 }
 t.Log("P40_MATH_B_P3_ORIGINAL_ECHO_METHOD_AND_STATIC_CONTROLS_PASS")
}
