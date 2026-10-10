package p41p3

import (
 "net/http"
 "net/http/httptest"
 "testing"
 echo "github.com/labstack/echo/v5"
)
func probe(t *testing.T,e *echo.Echo,path string)(int,string){
 t.Helper()
 r:=httptest.NewRecorder()
 e.ServeHTTP(r,httptest.NewRequest(http.MethodGet,path,nil))
 return r.Code,r.Body.String()
}
func TestSRPAndOCPConditionalDisjointnessAndCollision(t *testing.T){
 e:=echo.New()
 e.GET("/old",func(c *echo.Context)error{return c.String(200,"OLD")})
 e.GET("/new",func(c *echo.Context)error{return c.String(200,"NEW1")})
 s,b:=probe(t,e,"/old")
 e.GET("/new",func(c *echo.Context)error{return c.String(200,"NEW2")})
 s2,b2:=probe(t,e,"/old")
 sn,bn:=probe(t,e,"/new")
 if s!=200||s2!=200||b!="OLD"||b2!=b||sn!=200||bn!="NEW2"{
  t.Fatalf("disjoint update result %d %q %d %q %d %q",s,b,s2,b2,sn,bn)
 }
 t.Log("P41_P3_SRP_DISJOINT_ROUTE_RESPONSIBILITY_FRAME_PASS")
 t.Log("P41_P3_OCP_DISJOINT_EXTENSION_FRAME_PASS")
 e.GET("/old",func(c *echo.Context)error{return c.String(200,"CHANGED")})
 so,bo:=probe(t,e,"/old")
 if so!=200||bo!="CHANGED"{t.Fatalf("overlap case %d %q",so,bo)}
 t.Log("P41_P3_OCP_UNRESTRICTED_OVERWRITE_COUNTERTRACE_PASS")
}
func TestLSPResponseOnlyNotSelectedRouteIdentity(t *testing.T){
 construct:=func(extra bool)(*echo.Echo,*string){
  e:=echo.New()
  picked:=new(string)
  e.GET("/v2/*/tags/list",func(c *echo.Context)error{
   *picked=c.Path();return c.String(200,"SAME")
  })
  if extra{
   e.GET("/v2/*/blobs/uploads/:ref",func(c *echo.Context)error{
    *picked=c.Path();return c.String(200,"SAME")
   })
  }
  return e,picked
 }
 a,ap:=construct(false)
 b,bp:=construct(true)
 sa,ba:=probe(t,a,"/v2/foo/bar/tags/list")
 sb,bb:=probe(t,b,"/v2/foo/bar/tags/list")
 if sa!=200||sb!=200||ba!="SAME"||bb!=ba||*ap==*bp{
  t.Fatalf("route witness a=%d/%q/%q b=%d/%q/%q",sa,ba,*ap,sb,bb,*bp)
 }
 t.Log("P41_P3_LSP_HTTP_ONLY_NOT_ROUTE_IDENTITY_PASS")
}
